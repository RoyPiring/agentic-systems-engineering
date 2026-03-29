> ← [User guides](./README.md) · [System README](../README.md)

# User guide — P03: Live web content (Firecrawl)

**Validation:** [P03-validation.md](../validation/P03-validation.md) — **PASS** with evidence under [`../executions/evidence/p03/`](../executions/evidence/p03/) (see **[README.md](../executions/evidence/p03/README.md)** for the file manifest). Use **`--synthetic-evidence`** when Firecrawl is not reachable; add **`p03-ingest-web-run.txt`** when you run a live crawl.

## What you get

**`build/ingest_web.py`** calls a **self-hosted Firecrawl** API (default **`http://localhost:3002`**), obtains **markdown** for one URL (**`--mode scrape`**) or a **bounded crawl** (**`--mode crawl`**), wraps each page as a **LlamaIndex** `Document` with **`source_url`** (and **`domain`**, **`ingest_kind: web`**) in metadata, and **appends** embeddings to the existing Qdrant collection (**`multi_domain_docs`** by default) using **`nomic-embed-text`** — the **same** Ollama embedding model as **P01**.

**`build/query_pipeline.py`** (P02) prints an extra **`source_url:`** line under **Citations** when retrieved nodes carry that metadata, so you can prove web provenance.

## Getting ready (before you run)

1. **Complete [P01](./P01-user-guide.md)** and **[P02](./P02-user-guide.md)** — collection populated; **`query_pipeline.py`** works.
2. **Firecrawl** running locally (example):

   ```bash
   docker run -d -p 3002:3002 ghcr.io/mendableai/firecrawl
   curl http://localhost:3002/health
   ```

3. **Python venv under `build/`** — `pip install -r requirements.txt` (includes **`firecrawl-py`**).
4. **Qdrant** and **Ollama** (`nomic-embed-text`) — same as P01.
5. If your Firecrawl build rejects `Authorization: Bearer None`, set a dummy key the server accepts, e.g. PowerShell: `$env:FIRECRAWL_API_KEY=""` or a placeholder string documented by your Firecrawl image.

## Prerequisites (short list)

- P02 **PASS** (or equivalent) and non-empty **`multi_domain_docs`**.
- **Firecrawl** reachable at **`FIRECRAWL_URL`** (default **`http://localhost:3002`**).
- **Ollama** **`nomic-embed-text`** pulled.

## How to run

1. **Working directory:** **`build/`** (same as **`ingest.py`**).
2. **Synthetic evidence** (no Firecrawl — same **`source_url`** metadata contract; use for CI or blocked registry):

   ```bash
   python ingest_web.py --synthetic-evidence --dry-run
   python ingest_web.py --synthetic-evidence
   ```

   Then query e.g. PEP 405 / PYPREFIX (see step 6 below).

3. **Dry run** (no Qdrant writes — requires Firecrawl + markdown):

   ```bash
   python ingest_web.py --dry-run
   ```

4. **Ingest** default URL (stdlib `os.path` docs) into Qdrant:

   ```bash
   python ingest_web.py
   ```

5. **Optional — bounded crawl** (more pages; slower):

   ```bash
   python ingest_web.py --mode crawl --url https://docs.python.org/3/library/ --crawl-limit 5 --crawl-max-depth 1
   ```

6. **Query** for content that appears on the page you ingested, e.g. after ingesting the default `os.path` URL:

   ```bash
   python query_pipeline.py --query "According to the indexed documentation, what does os.path.join do?"
   ```

   After **`--synthetic-evidence`**, use e.g.:

   ```bash
   python query_pipeline.py --query "According to the indexed documentation snippet, what is PEP 405 about and what is PYPREFIX used for?"
   ```

   Confirm **Citations** include **`source_url:`** pointing at the docs URL.

## Common options

| Flag / env | Purpose |
| --- | --- |
| `--url` / `INGEST_WEB_URL` | Seed URL |
| `--firecrawl-url` / `FIRECRAWL_URL` | Firecrawl base URL |
| `--mode scrape` \| `crawl` | Single page vs bounded crawl |
| `--dry-run` | Print preview only |
| `--synthetic-evidence` | One fixed doc + **`source_url`**; no Firecrawl (validation / CI) |
| `QDRANT_URL`, `QDRANT_COLLECTION` | Same as P01/P02 |

## Evidence

Capture transcripts for [P03 validation](../validation/P03-validation.md): see [`executions/evidence/p03/README.md`](../executions/evidence/p03/README.md). Minimum set includes **`p03-query-web-citation.txt`**, **`p03-pip-freeze.txt`**, Qdrant JSON captures, and **`p03-firecrawl-health.txt`** (pass or fail). Operator caveats belong in [validation roll-up](../validation.md) (**Limitations**), not ad-hoc evidence files. Add **`p03-ingest-web-run.txt`** after a real Firecrawl ingest.

## Next

**P04** — Ragas / packaging (see [implementation plan](../executions/implementation/P04-implementation-plan.md)).
