> ← [User guides](./README.md) · [System README](../README.md)

# User guide — P01: Document ingestion and vector indexing

## What you get

**Markdown and PDF** files under `build/data/` are parsed with **Unstructured** (via LlamaIndex), embedded with **Ollama** `nomic-embed-text`, and written to a **Qdrant** collection named **`multi_domain_docs`** (default). Later phases (P02–P04) assume this collection exists.

## Getting ready (before you run)

1. **You are in the right repo folder** — the **system root** contains `build/`, `user-guides/`, and `executions/`. From the monorepo, open:  
   `engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/`
2. **Python venv under `build/`** — from the system root:

```bash
cd build
python -m venv venv
```

Activate the venv (Unix: `source venv/bin/activate`; Windows: `.\venv\Scripts\Activate.ps1`), then:

```bash
pip install -r requirements.txt
```

The implementation plan targets **Python 3.12**; **3.13** is known to work on a validated host. Refresh pins after upgrades with `pip freeze` and capture evidence per [validation/P01-validation.md](../validation/P01-validation.md).

1. **Qdrant (Docker)** — must accept HTTP on **`http://localhost:6333`** (or set `QDRANT_URL`).

```bash
docker run -p 6333:6333 -p 6334:6334 -v "$(pwd)/qdrant_storage:/qdrant/storage:z" qdrant/qdrant
```

PowerShell volume example: `-v "${PWD}/qdrant_storage:/qdrant/storage"`.

1. **Ollama** — embedding model on the host Ollama API (default `http://localhost:11434` used by the client library):

```bash
ollama pull nomic-embed-text
```

1. **Optional: Windows long paths** — if native libraries fail with “filename or extension is too long”, see [build/README.md](../build/README.md) (`run_ingest_windows.ps1`, `charset-normalizer` sdist reinstall).

## Prerequisites (short list)

- **Python** 3.12+ (3.12 recommended for parity with the plan).
- **Docker** (or another Qdrant install) exposing **6333**.
- **Ollama** with **`nomic-embed-text`** pulled.
- **No paid API keys required** for this path (local embed + local vectors).

## How to run

1. Put at least one **`.md`** or **`.pdf`** in **`build/data/`** (a small sample may already be committed).
2. Working directory must be **`build/`** so `./data` resolves correctly.
3. With venv active and Qdrant + Ollama up:

```bash
python ingest.py
```

### Common options

| Flag / env | Purpose |
| --- | --- |
| `--data-dir PATH` | Input folder (default `./data`) |
| `--qdrant-url URL` | Qdrant HTTP URL (default `http://localhost:6333`, or `QDRANT_URL`) |
| `--collection NAME` | Collection name (default `multi_domain_docs`, or `QDRANT_COLLECTION`) |
| `--embed-model NAME` | Ollama embedding model (default `nomic-embed-text`, or `OLLAMA_EMBED_MODEL`) |

### Windows (long clone path)

From **`build/`**:

```powershell
.\run_ingest_windows.ps1
```

Pass-through arguments are forwarded to `ingest.py` (for example `.\run_ingest_windows.ps1 --collection my_collection`).

## Success vs failure

- **Success:** Stdout shows a loaded document count and **`Vector indexing complete.`**; exit code **0**.
- **Failure examples:**
  - No `.md`/`.pdf` in the data dir → message on **stderr**, exit **1**.
  - Qdrant unreachable → connection error on **stderr**, exit **1**.
  - Missing Ollama model or embed API down → error during indexing (non-zero exit).

## Outputs

- **Qdrant** holds vectors and payload under the chosen collection (verify in the dashboard at `http://localhost:6333/dashboard` or via the collections API).
- **Stdout/stderr** only from the script; capture transcripts under `executions/evidence/p01/` when documenting a run (see [execution-record.md](../executions/execution-record.md)).

## Proof and deeper detail

- [P01 implementation plan](../executions/implementation/P01-implementation-plan.md)
- [P01 validation](../validation/P01-validation.md)
- [build/README.md](../build/README.md)

## Next step

After **P01** is green, use the indexed collection for citation-aware retrieval in **P02** (see [SERIES-user-guide.md](./SERIES-user-guide.md); **P02-user-guide.md** when published).
