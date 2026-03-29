# P03 validation — Live web content (Firecrawl)

**Status:** **Pending** — execute per [`../executions/implementation/P03-implementation-plan.md`](../executions/implementation/P03-implementation-plan.md).

## Scope

Prove **Firecrawl** (local) ingests **bounded** web pages into **LlamaIndex** `Document` objects with **`source_url`** metadata, **appends** embeddings to existing Qdrant **`multi_domain_docs`** using **`nomic-embed-text`** (same as P01), and **`query_pipeline.py`** returns answers with **citations that expose the live URL**.

## Checks

| # | Check | Command / action | Expected | Result |
| --- | --- | --- | --- | --- |
| V1 | Firecrawl health | `curl http://localhost:3002/health` | **`status` ok** (or documented equivalent) | **Pending** — `p03-firecrawl-health.txt` |
| V2 | Qdrant | `curl http://localhost:6333/collections/multi_domain_docs` | Collection exists; **points increase** after web ingest | **Pending** — `p03-qdrant-after-web.txt` (optional before snapshot) |
| V3 | Web ingest | From `build/`: `python ingest_web.py` (or documented CLI) | Exit **0**; bounded crawl; documents indexed | **Pending** — `p03-firecrawl-sample.txt` / run log |
| V4 | Metadata | Code review or debug print | Each web `Document` has **`source_url`** in metadata | **Pending** |
| V5 | Query + URL citation | `python query_pipeline.py` with web-only question | Answer grounded; citations include **target URL** | **Pending** — `p03-query-web-citation.txt` |
| V6 | Embed parity | Code review | **`OllamaEmbedding(nomic-embed-text)`** only for web path | **Pending** — match P01 |
| V7 | Deps | `pip freeze` after adding **firecrawl-py** | Snapshot for repro | **Pending** — `p03-pip-freeze.txt` |

## Evidence

[`../executions/evidence/p03/`](../executions/evidence/p03/) — populate when P03 is executed.

## Verdict

**Pending** — run checks **V1–V7** and set this file to **PASS** with dates and file pointers when accepted.
