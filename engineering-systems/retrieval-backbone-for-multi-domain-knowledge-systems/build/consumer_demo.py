#!/usr/bin/env python3
"""
P04 — Consumer smoke: use **only** the public packaged API (no direct Qdrant/LlamaIndex imports).

Run from ``build/``:
  python consumer_demo.py
  python consumer_demo.py --query "What vector database is named in the corpus?"
"""

from __future__ import annotations

import argparse
import os
import sys

from retrieval_service import RetrievalBackboneConfig, RetrievalBackboneService


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Consumer demo for RetrievalBackboneService (P04).")
    p.add_argument(
        "--query",
        default=os.environ.get(
            "CONSUMER_DEMO_QUERY",
            "What vector database does the indexed documentation mention?",
        ),
    )
    return p.parse_args()


def main() -> int:
    args = parse_args()
    # Explicit: config from defaults/env inside RetrievalBackboneConfig (no hardcoded paths).
    service = RetrievalBackboneService(RetrievalBackboneConfig())
    try:
        result = service.query(args.query)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("answer:", result.answer)
    print("contexts (count):", len(result.contexts))
    for i, c in enumerate(result.citations, start=1):
        extra = f" | url={c.source_url}" if c.source_url else ""
        print(f"  [{i}] {c.label}{extra}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
