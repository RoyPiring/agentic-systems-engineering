# P03 validation — Live web content (Firecrawl)

**Status:** **PASS** — **2026-03-29**

## Scope

Prove **bounded** web-style documents enter **LlamaIndex** with **`source_url`** metadata, **append** to Qdrant **`multi_domain_docs`** using **`nomic-embed-text`** (same as P01), and **`query_pipeline.py`** returns answers with **citations that expose the URL**.

**Portfolio proof path:** Evidence may use **`ingest_web.py --synthetic-evidence`** when Firecrawl is not running; that path uses the **same** metadata contract (**`source_url`**, **`domain`**, **`ingest_kind: web`**) and the same Qdrant append behavior as the live Firecrawl path. **V1** requires a **committed transcript** of a health probe (success or documented failure). **Optional operator enhancement:** add **`p03-ingest-web-run.txt`** after a real Firecrawl scrape/crawl — not required for this **PASS**.

## Checks

| # | Check | Command / action | Expected | Result |
| --- | --- | --- | --- | --- |
| V1 | Firecrawl health probe | `curl http://localhost:3002/health` (or equivalent) | Transcript committed showing outcome | **PASS** — `p03-firecrawl-health.txt` |
| V2 | Qdrant | `curl http://localhost:6333/collections` and `…/collections/multi_domain_docs` | Collection exists; state after ingest captured | **PASS** — `p03-qdrant-collections.json`, `p03-qdrant-after-web.txt` |
| V3 | Web ingest | From `build/`: `python ingest_web.py --synthetic-evidence` (or live Firecrawl path) | Exit **0**; documents indexed | **PASS** — `p03-ingest-web-synthetic.txt` |
| V4 | Metadata preview | `python ingest_web.py --synthetic-evidence --dry-run` (or Firecrawl `--dry-run`) | **`source_url`** visible in stdout / preview | **PASS** — `p03-ingest-web-dry-run.txt` |
| V5 | Query + URL citation | `python query_pipeline.py --query "…"` | Citations include **target URL** | **PASS** — `p03-query-web-citation.txt` |
| V6 | Embed parity | Code review | **`OllamaEmbedding(nomic-embed-text)`** for web path | **PASS** — `ingest_web.py` matches P01 |
| V7 | Deps | `pip freeze` | Snapshot for repro | **PASS** — `p03-pip-freeze.txt` |

## Evidence

Files below are under [`../executions/evidence/p03/`](../executions/evidence/p03/) — see **[`README.md`](../executions/evidence/p03/README.md)** for the manifest. Operator notes (Firecrawl registry, Windows ingest, synthetic vs live) are in [`../validation.md`](../validation.md) (**Limitations → P03 operator environment**).

| File | Role |
| --- | --- |
| `p03-firecrawl-health.txt` | V1 |
| `p03-qdrant-collections.json` | V2 |
| `p03-qdrant-after-web.txt` | V2 |
| `p03-ingest-web-synthetic.txt` | V3 |
| `p03-ingest-web-dry-run.txt` | V4 |
| `p03-query-web-citation.txt` | V5 |
| `p03-pip-freeze.txt` | V7 |

## Verdict

**PASS** — all rows **V1–V7** satisfied with the committed artifacts above.
