#!/usr/bin/env python3
"""
P01 — Ingest Markdown/PDF from ./data into Qdrant via LlamaIndex + Unstructured + Ollama embeddings.

Run from this directory (build/):  python ingest.py

On Windows, very long repo paths can break native extension loads (Unstructured/spaCy); use
``run_ingest_windows.ps1`` in this folder (see ``README.md``).

Prerequisites: Docker Qdrant on QDRANT_URL (default http://localhost:6333), Ollama with nomic-embed-text.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import qdrant_client
from llama_index.core import Settings, SimpleDirectoryReader, StorageContext, VectorStoreIndex
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.readers.file import UnstructuredReader
from llama_index.vector_stores.qdrant import QdrantVectorStore


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Ingest build/data into Qdrant (P01).")
    p.add_argument(
        "--data-dir",
        type=Path,
        default=Path("./data"),
        help="Directory with .md / .pdf files (default: ./data)",
    )
    p.add_argument(
        "--qdrant-url",
        default=os.environ.get("QDRANT_URL", "http://localhost:6333"),
        help="Qdrant HTTP URL",
    )
    p.add_argument(
        "--collection",
        default=os.environ.get("QDRANT_COLLECTION", "multi_domain_docs"),
        help="Qdrant collection name",
    )
    p.add_argument(
        "--embed-model",
        default=os.environ.get("OLLAMA_EMBED_MODEL", "nomic-embed-text"),
        help="Ollama embedding model name",
    )
    return p.parse_args()


def main() -> int:
    args = parse_args()
    data_dir = args.data_dir.resolve()
    if not data_dir.is_dir():
        print(f"ERROR: data directory not found: {data_dir}", file=sys.stderr)
        return 1

    md_files = list(data_dir.glob("*.md")) + list(data_dir.glob("*.pdf"))
    if not md_files:
        print(f"ERROR: no .md or .pdf files under {data_dir}", file=sys.stderr)
        return 1

    Settings.embed_model = OllamaEmbedding(model_name=args.embed_model)
    Settings.llm = None

    extractor = {".pdf": UnstructuredReader(), ".md": UnstructuredReader()}
    reader = SimpleDirectoryReader(
        input_dir=str(data_dir),
        file_extractor=extractor,
    )
    documents = reader.load_data()
    print(f"Loaded {len(documents)} document nodes from {data_dir}.")

    try:
        client = qdrant_client.QdrantClient(url=args.qdrant_url)
        client.get_collections()
    except Exception as exc:
        print(
            f"ERROR: cannot reach Qdrant at {args.qdrant_url!r}: {exc}",
            file=sys.stderr,
        )
        print("Start Qdrant (e.g. docker run -p 6333:6333 qdrant/qdrant) and retry.", file=sys.stderr)
        return 1

    vector_store = QdrantVectorStore(client=client, collection_name=args.collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    VectorStoreIndex.from_documents(documents, storage_context=storage_context)
    print("Vector indexing complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
