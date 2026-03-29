# Build

Application code, scripts, configs, and infrastructure-as-code produced while executing the series (P01–P04).

Runnable artifacts live here—not in the narrative docs at the engineering-system root.

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
