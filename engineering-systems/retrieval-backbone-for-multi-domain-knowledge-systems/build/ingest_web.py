#!/usr/bin/env python3
"""
P03 — Ingest live web pages (Firecrawl) into the existing Qdrant collection.

Run from this directory (build/):  python ingest_web.py [--dry-run]

Uses firecrawl-py **v1** API (``FirecrawlApp(...).v1``) against a self-hosted instance
(default ``http://localhost:3002``). Embeddings must match P01: ``nomic-embed-text`` via Ollama.

**``--synthetic-evidence``** (no Firecrawl): inserts one **markdown-shaped** document with
``source_url`` / ``ingest_kind: web`` so operators can prove URL citations + Qdrant append on
hosts where Firecrawl is unavailable (CI, registry deny, etc.). Does **not** replace a real
Firecrawl run for production validation when the service is available.

Prerequisites: Qdrant, Ollama embed model, Firecrawl container (except ``--synthetic-evidence``).
"""

from __future__ import annotations

import argparse
import os
import sys
from urllib.parse import urlparse

import qdrant_client
from llama_index.core import Document, Settings, StorageContext, VectorStoreIndex
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.qdrant import QdrantVectorStore

# Fixed corpus for --synthetic-evidence (retrieval smoke; mimics web markdown body).
_SYNTHETIC_SOURCE_URL = "https://docs.python.org/3/using/cmdline.html#environment-variables"
_SYNTHETIC_MARKDOWN = """# Python environment variables

The **PYPREFIX** prefix is used when building the standard library extensions for a
self-contained installation. Virtual environments are described in **PEP 405**; the
``pyvenv.cfg`` file records configuration for an isolated interpreter tree.

This paragraph exists only in the synthetic P03 evidence document so queries can target
web-style provenance without calling Firecrawl.
"""


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Ingest web content via Firecrawl into Qdrant (P03).")
    p.add_argument(
        "--synthetic-evidence",
        action="store_true",
        help="Skip Firecrawl; index one fixed doc with source_url (Qdrant + embed smoke only)",
    )
    p.add_argument(
        "--url",
        default=os.environ.get(
            "INGEST_WEB_URL",
            "https://docs.python.org/3/library/os.path.html",
        ),
        help="Seed URL to scrape or crawl (default: small stdlib docs page)",
    )
    p.add_argument(
        "--mode",
        choices=("scrape", "crawl"),
        default="scrape",
        help="scrape = single page; crawl = bounded multi-page (needs Firecrawl crawl API)",
    )
    p.add_argument(
        "--firecrawl-url",
        default=os.environ.get("FIRECRAWL_URL", "http://localhost:3002"),
        help="Firecrawl API base URL (self-hosted)",
    )
    p.add_argument(
        "--crawl-limit",
        type=int,
        default=5,
        help="Max pages when --mode crawl",
    )
    p.add_argument(
        "--crawl-max-depth",
        type=int,
        default=1,
        help="Max crawl depth when --mode crawl",
    )
    p.add_argument(
        "--poll-interval",
        type=int,
        default=3,
        help="Seconds between crawl status polls",
    )
    p.add_argument(
        "--qdrant-url",
        default=os.environ.get("QDRANT_URL", "http://localhost:6333"),
        help="Qdrant HTTP URL",
    )
    p.add_argument(
        "--collection",
        default=os.environ.get("QDRANT_COLLECTION", "multi_domain_docs"),
        help="Qdrant collection name (must match P01)",
    )
    p.add_argument(
        "--embed-model",
        default=os.environ.get("OLLAMA_EMBED_MODEL", "nomic-embed-text"),
        help="Ollama embedding model (must match P01)",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch from Firecrawl and print sample only; do not write to Qdrant",
    )
    return p.parse_args()


def _firecrawl_client(api_url: str):
    from firecrawl import FirecrawlApp

    return FirecrawlApp(api_key=os.environ.get("FIRECRAWL_API_KEY"), api_url=api_url)


def documents_from_scrape(app, url: str) -> list[Document]:
    if app.v1 is None:
        print("ERROR: Firecrawl v1 client not available in this SDK build.", file=sys.stderr)
        raise SystemExit(1)
    resp = app.v1.scrape_url(
        url,
        formats=["markdown"],
        only_main_content=True,
    )
    if not getattr(resp, "success", True) or getattr(resp, "error", None):
        print(f"ERROR: scrape failed: {getattr(resp, 'error', 'unknown')}", file=sys.stderr)
        raise SystemExit(1)
    md = (resp.markdown or "").strip()
    if not md:
        print("ERROR: empty markdown from Firecrawl scrape.", file=sys.stderr)
        raise SystemExit(1)
    page_url = resp.url or url
    meta = _page_metadata(page_url)
    return [Document(text=md, metadata=meta)]


def documents_from_crawl(
    app,
    url: str,
    *,
    limit: int,
    max_depth: int,
    poll_interval: int,
) -> list[Document]:
    from firecrawl.v1.client import V1ScrapeOptions

    if app.v1 is None:
        print("ERROR: Firecrawl v1 client not available in this SDK build.", file=sys.stderr)
        raise SystemExit(1)
    scrape_options = V1ScrapeOptions(formats=["markdown"], onlyMainContent=True)
    result = app.v1.crawl_url(
        url,
        limit=limit,
        max_depth=max_depth,
        allow_external_links=False,
        scrape_options=scrape_options,
        poll_interval=poll_interval,
    )
    if not result.success or result.status != "completed":
        print(f"ERROR: crawl did not complete: status={result.status!r}", file=sys.stderr)
        raise SystemExit(1)
    docs: list[Document] = []
    for item in result.data or []:
        md = (item.markdown or "").strip()
        page_url = item.url or url
        if not md:
            print(f"WARN: skip empty page {page_url}", file=sys.stderr)
            continue
        docs.append(Document(text=md, metadata=_page_metadata(page_url)))
    if not docs:
        print("ERROR: crawl returned no non-empty documents.", file=sys.stderr)
        raise SystemExit(1)
    return docs


def documents_synthetic() -> list[Document]:
    return [
        Document(
            text=_SYNTHETIC_MARKDOWN.strip(),
            metadata=_page_metadata(_SYNTHETIC_SOURCE_URL),
        )
    ]


def _page_metadata(page_url: str) -> dict:
    host = urlparse(page_url).netloc or "unknown"
    return {
        "source_url": page_url,
        "domain": host,
        "ingest_kind": "web",
    }


def main() -> int:
    args = parse_args()
    Settings.embed_model = OllamaEmbedding(model_name=args.embed_model)
    Settings.llm = None

    if args.synthetic_evidence:
        documents = documents_synthetic()
        print("Synthetic-evidence mode: 1 document (no Firecrawl).")
    else:
        try:
            from firecrawl import FirecrawlApp  # noqa: F401
        except ImportError:
            print(
                "ERROR: firecrawl-py is required. From build/: pip install -r requirements.txt",
                file=sys.stderr,
            )
            return 1
        app = _firecrawl_client(args.firecrawl_url.rstrip("/"))
        if args.mode == "scrape":
            documents = documents_from_scrape(app, args.url)
            print(f"Scrape mode: {len(documents)} document(s) from {args.url!r}.")
        else:
            documents = documents_from_crawl(
                app,
                args.url,
                limit=args.crawl_limit,
                max_depth=args.crawl_max_depth,
                poll_interval=args.poll_interval,
            )
            print(
                f"Crawl mode: {len(documents)} document(s) "
                f"(limit={args.crawl_limit}, max_depth={args.crawl_max_depth})."
            )

    for i, d in enumerate(documents, start=1):
        print(f"  [{i}] source_url={d.metadata.get('source_url')!r} chars={len(d.text)}")

    if args.dry_run:
        preview = documents[0].text[:1200]
        print("\n--- dry-run preview (first doc) ---\n")
        print(preview)
        if len(documents[0].text) > 1200:
            print("\n... [truncated]")
        return 0

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
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    VectorStoreIndex.from_documents(documents, storage_context=storage_context)
    print("Web documents indexed into Qdrant (append).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
