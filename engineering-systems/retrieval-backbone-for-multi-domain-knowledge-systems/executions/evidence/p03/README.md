# P03 evidence

Transcripts and HTTP captures for **Live web content (Firecrawl)** and the **synthetic fallback** when Firecrawl is unreachable. **[P03 validation](../../../validation/P03-validation.md)** lists each file against checks **V1–V7**; operator steps: **[P03 user guide](../../../user-guides/P03-user-guide.md)**.

## Files (this run)

| File | Contents |
| --- | --- |
| `p03-firecrawl-health.txt` | `curl` to Firecrawl `/health` (failed — no service) |
| `p03-ingest-web-dry-run.txt` | `python ingest_web.py --synthetic-evidence --dry-run` |
| `p03-ingest-web-synthetic.txt` | `python ingest_web.py --synthetic-evidence` (Qdrant append) |
| `p03-qdrant-collections.json` | `GET /collections` |
| `p03-qdrant-after-web.txt` | `GET /collections/multi_domain_docs` after ingest |
| `p03-query-web-citation.txt` | `query_pipeline.py` showing **`source_url:`** in Citations |
| `p03-pip-freeze.txt` | `pip freeze` (includes `firecrawl-py`) |

When Firecrawl is available, add: `p03-ingest-web-run.txt` (real scrape/crawl), optional `p03-firecrawl-health.txt` with **ok** status.
