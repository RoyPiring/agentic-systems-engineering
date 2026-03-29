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
| `venv/` | Local Python 3.12 environment (typically gitignored) |

**Run ingest:** open a terminal with cwd **`build/`**, activate `venv`, ensure Qdrant and Ollama are up, then `python ingest.py`.

**Qdrant data:** Docker volume (e.g. `qdrant_storage` next to where you run `docker`) is operator-local—not required inside this folder.
