#!/usr/bin/env python3
"""
P04 — Ragas evaluation over the packaged ``RetrievalBackboneService`` (Ollama + Qdrant path).

Uses **explicit** LangChain-Ollama LLMs for Ragas (no OpenAI defaults):
- ``context_precision`` → ``ChatOllama(..., format="json")`` (structured verdicts)
- ``answer_relevancy`` → plain ``ChatOllama`` (generates questions from answers)

Default judge model is ``OLLAMA_EVAL_LLM_MODEL=qwen3:8b`` because many small models
return invalid JSON for both prompts; override if your stack differs.

Run from ``build/``:
  python ragas_eval.py --mode baseline
  python ragas_eval.py --mode batch --sleep-between 2
  python ragas_eval.py --dry-dataset --mode batch   # no Ragas / no judge LLM calls
  python ragas_eval.py --mode batch --synthetic-rows  # fixed rows + Ragas only (no Qdrant)
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
from typing import Any

from datasets import Dataset
from ragas import evaluate
from ragas.metrics import answer_relevancy, context_precision
from ragas.run_config import RunConfig
from langchain_ollama import ChatOllama, OllamaEmbeddings

from retrieval_service import RetrievalBackboneConfig, RetrievalBackboneService


def _env_float(key: str, default: float) -> float:
    raw = os.environ.get(key)
    if raw is None or raw == "":
        return default
    return float(raw)


def _eval_llm_model() -> str:
    return os.environ.get("OLLAMA_EVAL_LLM_MODEL") or os.environ.get(
        "OLLAMA_RAGAS_EVAL_MODEL", "qwen3:8b"
    )


def _embed_model() -> str:
    return os.environ.get("OLLAMA_EMBED_MODEL", "nomic-embed-text")


def build_embeddings() -> OllamaEmbeddings:
    return OllamaEmbeddings(model=_embed_model())


def build_context_precision_llm() -> ChatOllama:
    return ChatOllama(
        model=_eval_llm_model(),
        temperature=0.0,
        timeout=_env_float("OLLAMA_EVAL_TIMEOUT", 180.0),
        format="json",
    )


def build_answer_relevancy_llm() -> ChatOllama:
    return ChatOllama(
        model=_eval_llm_model(),
        temperature=0.0,
        timeout=_env_float("OLLAMA_EVAL_TIMEOUT", 180.0),
    )


def baseline_rows() -> list[dict[str, Any]]:
    """Single-row smoke aligned with P02/P03 corpus + web synthetic doc."""
    return [
        {
            "domain": "markdown_file",
            "user_input": "What vector database does the indexed documentation say is used locally in this series?",
            "reference": "Qdrant is used locally.",
        }
    ]


def synthetic_baseline_rows() -> list[dict[str, Any]]:
    """Hand-crafted row: coherent Q/A/contexts for Ragas smoke when Qdrant is unavailable."""
    return [
        {
            "domain": "synthetic",
            "user_input": "What vector database does the indexed documentation say is used locally?",
            "response": "The documentation states that Qdrant is used locally in this series.",
            "retrieved_contexts": [
                "Vector databases store embeddings for similarity search. Qdrant is used locally in this series."
            ],
            "reference": "Qdrant is used locally.",
        }
    ]


def synthetic_batch_rows() -> list[dict[str, Any]]:
    """Three coherent rows (markdown / PDF-topic / web-style) for multi-domain batch without Qdrant."""
    return [
        {
            "domain": "markdown_file",
            "user_input": "What vector database does the indexed documentation say is used locally?",
            "response": "Qdrant is used locally for vector storage in this series.",
            "retrieved_contexts": [
                "Vector databases store embeddings for similarity search. Qdrant is used locally in this series."
            ],
            "reference": "Qdrant is used locally for this series.",
        },
        {
            "domain": "pdf_topic",
            "user_input": "What file type can Unstructured partition for the same Qdrant collection as Markdown?",
            "response": "Unstructured can partition PDF documents into elements for the same Qdrant collection.",
            "retrieved_contexts": [
                "Unstructured can partition PDF documents into elements for the same Qdrant collection as Markdown."
            ],
            "reference": "PDF documents can be partitioned by Unstructured into the same collection.",
        },
        {
            "domain": "web_synthetic",
            "user_input": "According to the documentation about Python environment variables, what does PEP 405 describe?",
            "response": "PEP 405 describes virtual environments in Python.",
            "retrieved_contexts": [
                "Virtual environments are described in PEP 405; the pyvenv.cfg file records configuration."
            ],
            "reference": "PEP 405 describes Python virtual environments.",
        },
    ]


def batch_rows() -> list[dict[str, Any]]:
    """Multi-domain labels: markdown file corpus, PDF-topic line in sample.md, web synthetic doc."""
    return [
        {
            "domain": "markdown_file",
            "user_input": "What vector database does the indexed documentation say is used locally in this series?",
            "reference": "Qdrant is used locally for this series.",
        },
        {
            "domain": "pdf_topic",
            "user_input": "According to the indexed corpus, what file type can Unstructured partition for the same Qdrant collection as Markdown?",
            "reference": "PDF documents can be partitioned by Unstructured into the same collection.",
        },
        {
            "domain": "web_synthetic",
            "user_input": (
                "According to the indexed documentation about Python environment variables, "
                "what does PEP 405 describe?"
            ),
            "reference": "PEP 405 describes Python virtual environments.",
        },
    ]


def run_pipeline_rows(
    service: RetrievalBackboneService,
    specs: list[dict[str, Any]],
    sleep_s: float,
) -> list[dict[str, Any]]:
    rows_out: list[dict[str, Any]] = []
    for i, spec in enumerate(specs):
        if i > 0 and sleep_s > 0:
            time.sleep(sleep_s)
        q = spec["user_input"]
        r = service.query(q)
        if not r.contexts:
            print(
                f"WARNING: zero retrieved contexts for row {i} ({spec.get('domain')!r}). "
                "Re-run P01 ingest (updated sample.md) and P03 synthetic web ingest.",
                file=sys.stderr,
            )
        rows_out.append(
            {
                "domain": spec["domain"],
                "user_input": q,
                "response": r.answer,
                "retrieved_contexts": r.contexts,
                "reference": spec["reference"],
            }
        )
    return rows_out


def run_ragas(dataset: Dataset, run_config: RunConfig) -> dict[str, float]:
    emb = build_embeddings()
    llm_json = build_context_precision_llm()
    llm_plain = build_answer_relevancy_llm()
    agg: dict[str, float] = {}
    r1 = evaluate(
        dataset,
        metrics=[context_precision],
        llm=llm_json,
        embeddings=emb,
        run_config=run_config,
        show_progress=True,
    )
    r2 = evaluate(
        dataset,
        metrics=[answer_relevancy],
        llm=llm_plain,
        embeddings=emb,
        run_config=run_config,
        show_progress=True,
    )
    # EvaluationResult is not dict()-convertible (KeyError on integer keys during copy).
    for r in (r1, r2):
        repr_dict = getattr(r, "_repr_dict", None) or {}
        for k, v in repr_dict.items():
            fv = _finite_float(v)
            if fv is not None:
                agg[k] = fv
    return agg


def _finite_float(v: Any) -> float | None:
    try:
        x = float(v)
    except (TypeError, ValueError):
        return None
    if math.isnan(x):
        return None
    return x


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Ragas eval for retrieval backbone (P04).")
    p.add_argument("--mode", choices=("baseline", "batch"), default="baseline")
    p.add_argument(
        "--sleep-between",
        type=float,
        default=0.0,
        help="Seconds to sleep between pipeline queries (local Ollama throttle)",
    )
    p.add_argument(
        "--dry-dataset",
        action="store_true",
        help="Print HuggingFace-style dataset rows as JSON and exit (no Ragas judge calls)",
    )
    p.add_argument(
        "--synthetic-rows",
        action="store_true",
        help="Skip Qdrant pipeline; use hand-crafted rows then run Ragas (CI / no collection)",
    )
    p.add_argument(
        "--run-config-timeout",
        type=int,
        default=240,
        help="Ragas RunConfig timeout (seconds) per metric batch",
    )
    return p.parse_args()


def main() -> int:
    args = parse_args()
    if args.synthetic_rows:
        rows = (
            synthetic_baseline_rows()
            if args.mode == "baseline"
            else synthetic_batch_rows()
        )
    else:
        specs = baseline_rows() if args.mode == "baseline" else batch_rows()
        cfg = RetrievalBackboneConfig()
        try:
            service = RetrievalBackboneService(cfg)
        except Exception as exc:
            print(f"ERROR: cannot start RetrievalBackboneService: {exc}", file=sys.stderr)
            return 1
        rows = run_pipeline_rows(service, specs, args.sleep_between)
    ds = Dataset.from_list(
        [
            {
                "user_input": r["user_input"],
                "response": r["response"],
                "retrieved_contexts": r["retrieved_contexts"],
                "reference": r["reference"],
            }
            for r in rows
        ]
    )

    if args.dry_dataset:
        print(json.dumps(rows, indent=2))
        return 0

    rc = RunConfig(timeout=args.run_config_timeout, max_retries=5)
    try:
        scores = run_ragas(ds, rc)
    except Exception as exc:
        print(f"ERROR: Ragas evaluate failed: {exc}", file=sys.stderr)
        return 1

    print("Ragas aggregate (non-NaN metrics)")
    print("---------------------------------")
    for k in sorted(scores.keys()):
        print(f"  {k}: {scores[k]:.4f}")
    print()
    print("Per-row domains (pipeline)")
    for r in rows:
        print(f"  - {r['domain']}: contexts={len(r['retrieved_contexts'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
