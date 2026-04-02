#!/usr/bin/env python3
"""
P02 — Citation-aware RAG: load Qdrant index (P01), query with LlamaIndex + Ollama LLM/embeddings.

P04 — Uses ``RetrievalBackboneService`` (public packaged API) for all retrieval state.

Run from this directory (build/):  python query_pipeline.py --query "Your question"

Prerequisites: Qdrant with collection populated by ingest.py; Ollama with llama3.2 (or --llm-model)
and nomic-embed-text (must match P01 embed model).
"""

from __future__ import annotations

import argparse
import os
import sys

from retrieval_service import RetrievalBackboneConfig, RetrievalBackboneService


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Query Qdrant via LlamaIndex + Ollama (P02 / P04 service).")
    p.add_argument(
        "--query",
        default=os.environ.get("RAG_QUERY", "What is in the indexed documents? Summarize briefly."),
        help="Natural-language question (default: env RAG_QUERY or built-in demo)",
    )
    p.add_argument(
        "--qdrant-url",
        default=os.environ.get("QDRANT_URL", "http://localhost:6333"),
        help="Qdrant HTTP URL",
    )
    p.add_argument(
        "--collection",
        default=os.environ.get("QDRANT_COLLECTION", "multi_domain_docs"),
        help="Qdrant collection name (must match P01 ingest)",
    )
    p.add_argument(
        "--embed-model",
        default=os.environ.get("OLLAMA_EMBED_MODEL", "nomic-embed-text"),
        help="Ollama embedding model (must match P01)",
    )
    p.add_argument(
        "--llm-model",
        default=os.environ.get("OLLAMA_LLM_MODEL", "llama3.2"),
        help="Ollama chat/completion model for synthesis",
    )
    p.add_argument(
        "--similarity-top-k",
        type=int,
        default=3,
        help="Number of chunks to retrieve",
    )
    p.add_argument(
        "--ollama-request-timeout",
        type=float,
        default=120.0,
        help="Seconds to wait for Ollama generation",
    )
    return p.parse_args()


def print_answer_and_citations(answer: str, citations: list) -> None:
    print("Answer")
    print("------")
    print(answer if answer else "(empty)")
    print()
    print("Citations")
    print("---------")
    if not citations:
        print("  (no source nodes returned)")
        return
    for i, c in enumerate(citations, start=1):
        score_part = ""
        if c.score is not None:
            score_part = f" score={c.score:.4f}"
        print(f"  [{i}] node_id={c.node_id}{score_part}")
        print(f"      file: {c.label}")
        if c.source_url:
            print(f"      source_url: {c.source_url}")
        print(f"      text: {c.text_excerpt}")


def main() -> int:
    args = parse_args()
    cfg = RetrievalBackboneConfig(
        qdrant_url=args.qdrant_url,
        qdrant_collection=args.collection,
        ollama_embed_model=args.embed_model,
        ollama_llm_model=args.llm_model,
        similarity_top_k=args.similarity_top_k,
        ollama_request_timeout=args.ollama_request_timeout,
    )
    try:
        service = RetrievalBackboneService(cfg)
        result = service.query(args.query)
    except Exception as exc:
        print(
            f"ERROR: query failed ({exc!r}). Is Qdrant up and the collection populated?",
            file=sys.stderr,
        )
        return 1

    print_answer_and_citations(result.answer, result.citations)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
