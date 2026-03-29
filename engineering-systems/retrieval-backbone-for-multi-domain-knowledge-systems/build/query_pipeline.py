#!/usr/bin/env python3
"""
P02 — Citation-aware RAG: load Qdrant index (P01), query with LlamaIndex + Ollama LLM/embeddings.

Run from this directory (build/):  python query_pipeline.py --query "Your question"

Prerequisites: Qdrant with collection populated by ingest.py; Ollama with llama3.2 (or --llm-model)
and nomic-embed-text (must match P01 embed model).
"""

from __future__ import annotations

import argparse
import os
import sys

import qdrant_client
from llama_index.core import Settings, PromptTemplate, VectorStoreIndex
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.qdrant import QdrantVectorStore

# Prompt must include {context_str} and {query_str} for default LlamaIndex text QA synthesis.
CITATION_AWARE_QA_TEMPLATE = PromptTemplate(
    template=(
        "Context information is below.\n"
        "---------------------\n"
        "{context_str}\n"
        "---------------------\n"
        "You are a helpful assistant. Use only the context above to answer the question.\n"
        "When you use information from the context, cite it explicitly using the document name "
        "or identifier shown in the context (for example: [Source: filename]).\n"
        "If the context does not contain the answer, say you do not have enough information.\n"
        "Question: {query_str}\n"
        "Answer: "
    )
)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Query Qdrant via LlamaIndex + Ollama (P02).")
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


def response_text(response: object) -> str:
    """Normalize LlamaIndex Response to a string."""
    r = getattr(response, "response", None)
    if r is not None:
        return str(r).strip()
    return str(response).strip()


def run_query(query_engine: object, query: str) -> tuple[str, list]:
    """Execute query_engine.query and return (answer_text, source_nodes list)."""
    result = query_engine.query(query)
    nodes = getattr(result, "source_nodes", None) or []
    return response_text(result), list(nodes)


def print_answer_and_citations(answer: str, source_nodes: list) -> None:
    print("Answer")
    print("------")
    print(answer if answer else "(empty)")
    print()
    print("Citations")
    print("---------")
    if not source_nodes:
        print("  (no source nodes returned)")
        return
    for i, sn in enumerate(source_nodes, start=1):
        node = sn.node
        node_id = getattr(node, "node_id", None) or getattr(node, "id_", "?")
        score = getattr(sn, "score", None)
        score_part = ""
        if score is not None:
            try:
                score_part = f" score={float(score):.4f}"
            except (TypeError, ValueError):
                score_part = f" score={score!r}"
        meta = node.metadata or {}
        file_name = meta.get("file_name") or meta.get("file_path") or meta.get("document_id", "unknown")
        snippet = node.get_content().strip().replace("\n", " ")
        if len(snippet) > 280:
            snippet = snippet[:277] + "..."
        print(f"  [{i}] node_id={node_id}{score_part}")
        print(f"      file: {file_name}")
        print(f"      text: {snippet}")


def main() -> int:
    args = parse_args()

    Settings.embed_model = OllamaEmbedding(model_name=args.embed_model)
    Settings.llm = Ollama(
        model=args.llm_model,
        request_timeout=args.ollama_request_timeout,
    )

    try:
        client = qdrant_client.QdrantClient(url=args.qdrant_url)
        client.get_collections()
    except Exception as exc:
        print(
            f"ERROR: cannot reach Qdrant at {args.qdrant_url!r}: {exc}",
            file=sys.stderr,
        )
        return 1

    vector_store = QdrantVectorStore(client=client, collection_name=args.collection)
    try:
        index = VectorStoreIndex.from_vector_store(
            vector_store=vector_store,
            embed_model=Settings.embed_model,
        )
    except Exception as exc:
        print(
            f"ERROR: failed to load VectorStoreIndex from Qdrant collection "
            f"{args.collection!r}: {exc}",
            file=sys.stderr,
        )
        print("Run P01 ingest.py first so the collection exists and has vectors.", file=sys.stderr)
        return 1

    query_engine = index.as_query_engine(
        similarity_top_k=args.similarity_top_k,
        text_qa_template=CITATION_AWARE_QA_TEMPLATE,
    )

    answer, source_nodes = run_query(query_engine, args.query)
    print_answer_and_citations(answer, source_nodes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
