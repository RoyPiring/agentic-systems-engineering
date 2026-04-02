# Build

Application code, scripts, configs, and infrastructure-as-code produced while executing the series (P01–P04).

Runnable artifacts live here—not in the narrative docs at the engineering-system root.

## Committed tree (P01–P04)

Everything below is part of the delivered build; there are no auxiliary one-off test scripts in this folder (use `executions/evidence/` for transcripts).

| Path | Phase |
| --- | --- |
| `requirements.txt` | P01–P04 deps |
| `ingest.py` | P01 |
| `run_ingest_windows.ps1` | P01 (Windows **MAX_PATH** helper for `ingest.py`) |
| `data/sample.md`, `data/README.md` | P01 sample corpus |
| `query_pipeline.py` | P02 (uses **`retrieval_service`** in P04) |
| `ingest_web.py` | P03 (Firecrawl path + **`--synthetic-evidence`** for the same index contract without Firecrawl) |
| `retrieval_service.py` | P04 packaged API (**`RetrievalBackboneService`**) |
| `ragas_eval.py` | P04 Ragas baseline / batch |
| `consumer_demo.py` | P04 consumer smoke (public imports only) |

`venv/` is local-only (typically gitignored).

## Rules

- Prefer real, runnable content over empty placeholders.
- Do not commit secrets; use environment variables or secret stores documented in `architecture.md` / `validation.md`.
- Keep paths and run instructions discoverable from `implementation.md`, each `executions/implementation/P0X-implementation-plan.md`, and `executions/execution-record.md`.

## P01 layout (target)

| Path | Purpose |
| --- | --- |
| `data/` | Sample **`.md`** / **`.pdf`** inputs for ingestion (operator-owned or small committed samples) |
| `ingest.py` | Unstructured readers + Ollama embeddings + Qdrant upsert per [P01 implementation plan](../executions/implementation/P01-implementation-plan.md) |
| `venv/` | Local Python environment (typically gitignored; plan targets **3.12**; **3.13** validated 2026-03-28) |
| `run_ingest_windows.ps1` | **Windows:** runs `ingest.py` via `subst R:` so native deps (spacy, etc.) load under **MAX_PATH** limits |

**Run ingest:** open a terminal with cwd **`build/`**, activate `venv`, ensure Qdrant and Ollama are up, then `python ingest.py`.

**Windows (long clone path):** If you see DLL load errors mentioning a path that is “too long”, either enable [long paths](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation) for the OS, or run `.\run_ingest_windows.ps1` (requires a free **`R:`** drive letter). After `pip install -r requirements.txt`, if `charset_normalizer` fails to import, reinstall it from source: `pip install --no-binary charset-normalizer "charset-normalizer>=3.4.4,<4"`.

**Qdrant data:** Docker volume (e.g. `qdrant_storage` next to where you run `docker`) is operator-local—not required inside this folder.

## P02 layout (citation-aware query)

| Path | Purpose |
| --- | --- |
| `query_pipeline.py` | Load **`multi_domain_docs`** from Qdrant; **Ollama** `llama3.2` + `nomic-embed-text`; print **Answer** + **Citations** ([plan](../executions/implementation/P02-implementation-plan.md), [operator guide](../user-guides/P02-user-guide.md)) |

**Run query:** cwd **`build/`**, venv active, **Qdrant** + **Ollama** running, P01 ingest completed once. Then:

```bash
ollama pull llama3.2
python query_pipeline.py --query "What topics appear in the sample corpus?"
```

Optional env: `QDRANT_URL`, `QDRANT_COLLECTION`, `OLLAMA_EMBED_MODEL`, `OLLAMA_LLM_MODEL`, `RAG_QUERY`. Capture stdout under [`executions/evidence/p02/`](../executions/evidence/p02/) when closing validation.

**P02 deps:** `requirements.txt` pins **`llama-index-vector-stores-qdrant>=0.10.0`** so **`query_pipeline.py`** works with **qdrant-client 1.17+**. If you see **`QdrantClient` has no attribute `search`**, recreate the venv and reinstall from this file — see [P02 user guide — Troubleshooting](../user-guides/P02-user-guide.md#troubleshooting-dependency-stack).

## P03 layout (Firecrawl → Qdrant append)

| Path | Purpose |
| --- | --- |
| `ingest_web.py` | **Firecrawl** (self-hosted) scrape or bounded **crawl** → **LlamaIndex** `Document` with **`source_url`** → append vectors to **`multi_domain_docs`** ([plan](../executions/implementation/P03-implementation-plan.md), [operator guide](../user-guides/P03-user-guide.md)) |

**Firecrawl (Docker example):**

```bash
docker run -d -p 3002:3002 ghcr.io/mendableai/firecrawl
curl http://localhost:3002/health
```

**Run (cwd `build/`, venv active):**

```bash
pip install -r requirements.txt
# When Firecrawl is down or the image is unavailable: prove Qdrant + source_url citations (no network scrape)
python ingest_web.py --synthetic-evidence --dry-run
python ingest_web.py --synthetic-evidence
# With Firecrawl up — optional: prove fetch only (no Qdrant writes)
python ingest_web.py --dry-run
python ingest_web.py
# Multi-page (strict limits; slower)
python ingest_web.py --mode crawl --url https://docs.python.org/3/library/ --crawl-limit 5 --crawl-max-depth 1
```

Env: **`FIRECRAWL_URL`** (default `http://localhost:3002`), **`FIRECRAWL_API_KEY`** (empty or omit for many self-hosted images; SDK sends `Authorization: Bearer …`), **`INGEST_WEB_URL`**, same Qdrant/Ollama vars as P01.

**Then query** with a question that targets the ingested page (see [P03 user guide](../user-guides/P03-user-guide.md)); **`query_pipeline.py`** prints **`source_url:`** in **Citations** when node metadata includes it.

## P04 layout (Ragas + packaged service)

| Path | Purpose |
| --- | --- |
| `retrieval_service.py` | **`RetrievalBackboneConfig`** + **`RetrievalBackboneService.query()`** → **`QueryResult`** (`answer`, `contexts`, `citations`) — env/injected config, instance-scoped clients ([plan](../executions/implementation/P04-implementation-plan.md), [operator guide](../user-guides/P04-user-guide.md)) |
| `ragas_eval.py` | Build Ragas dataset from the live pipeline; run **context_precision** + **answer_relevancy** with **Ollama** judge models (**`OLLAMA_EVAL_LLM_MODEL`**, default **`qwen3:8b`**) |
| `consumer_demo.py` | Instantiate service + one query — **only** imports from `retrieval_service` |

**Run (cwd `build/`, venv active, Qdrant + Ollama up, collection populated):**

```bash
pip install -r requirements.txt
python consumer_demo.py
python ragas_eval.py --mode baseline
python ragas_eval.py --mode batch --sleep-between 2
```

**When Qdrant is down:** `python ragas_eval.py --mode batch --synthetic-rows` (hand-crafted rows + Ragas only).

Capture stdout under [`../executions/evidence/p04/`](../executions/evidence/p04/) when closing validation.
