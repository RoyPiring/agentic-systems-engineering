> ← [User guides](./README.md) · [System README](../README.md)

# User guide — P02: Citation-aware retrieval (LlamaIndex and Ollama)

## What you get

**`build/query_pipeline.py`** loads the **existing** Qdrant collection from **P01** (default **`multi_domain_docs`**), runs a **LlamaIndex** query engine with **Ollama** for both **embeddings** and **LLM** synthesis, and prints an **Answer** plus a **Citations** section (retrieved node ids, scores, file metadata, text snippets). No OpenAI keys are used when `Settings` are set as in the script.

## Getting ready (before you run)

1. **Complete [P01](./P01-user-guide.md)** — collection populated; same **embedding model** as ingest (**`nomic-embed-text`**).
2. **System root** — same as P01: `engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/` (contains `build/`, `user-guides/`, `executions/`).
3. **Python venv under `build/`** — activate it, then install / refresh deps (includes the LLM integration):

```bash
cd build
pip install -r requirements.txt
```

4. **Qdrant** — running at **`http://localhost:6333`** (or `QDRANT_URL`) with the P01 collection.
5. **Ollama** — pull **both** models used by this phase:

```bash
ollama pull nomic-embed-text
ollama pull llama3.2
```

If your local tag differs, pass **`--llm-model`** / **`OLLAMA_LLM_MODEL`** (see Common options).

## Prerequisites (short list)

- **P01** **PASS** and non-empty **`multi_domain_docs`** (or your override collection name).
- **Python** 3.12+ with venv and **`build/requirements.txt`** installed (**`llama-index-llms-ollama`** required).
- **Ollama** serving **`llama3.2`** and **`nomic-embed-text`**.
- **No paid API keys** required on the default path.

## How to run

1. Working directory must be **`build/`** (same convention as **`ingest.py`**).
2. With venv active, Qdrant up, and Ollama up:

```bash
python query_pipeline.py --query "What is described in the indexed sample documents?"
```

### Common options

| Flag / env | Purpose |
| --- | --- |
| `--query TEXT` | Question (default: env **`RAG_QUERY`** or built-in demo string) |
| `--qdrant-url URL` | Qdrant HTTP URL (`QDRANT_URL`) |
| `--collection NAME` | Collection (`QDRANT_COLLECTION`, default `multi_domain_docs`) |
| `--embed-model NAME` | Must match P01 (`OLLAMA_EMBED_MODEL`, default `nomic-embed-text`) |
| `--llm-model NAME` | Ollama chat model (`OLLAMA_LLM_MODEL`, default `llama3.2`) |
| `--similarity-top-k N` | Chunks to retrieve (default **3**) |
| `--ollama-request-timeout SEC` | Generation timeout (default **120**) |

## Success vs failure

- **Success:** Stdout shows **Answer** then **Citations** with up to **k** nodes; exit code **0**.
- **Failure examples:**
  - Qdrant unreachable → stderr message, exit **1**.
  - Cannot load index from collection → stderr; run P01 ingest first.
  - Ollama down or model missing → error from client during query; fix service / `ollama pull`.

## Outputs

- **Terminal only** by default; redirect or copy into evidence files (below).

## Evidence (for validation)

When documenting a run for **[P02 validation](../validation/P02-validation.md)**, save transcripts under **`executions/evidence/p02/`** using names aligned with the implementation plan, for example:

| File | Suggested content |
| --- | --- |
| `p02-query-run.txt` | Full stdout/stderr from one or more representative **`query_pipeline.py`** runs |
| `p02-ollama-list.txt` | `ollama list` showing **`llama3.2`** and **`nomic-embed-text`** |
| `p02-pip-freeze.txt` | Optional: `pip freeze` from the same venv after `pip install -r requirements.txt` |

See [`executions/evidence/p02/README.md`](../executions/evidence/p02/README.md) for the folder intent.

## Proof and deeper detail

- [P02 implementation plan](../executions/implementation/P02-implementation-plan.md)
- [P02 validation](../validation/P02-validation.md)
- [build/README.md](../build/README.md)

## Next step

After **P02** is green, **P03** will extend ingestion sources (e.g. web); this query script remains the retrieval surface—watch [SERIES-user-guide.md](./SERIES-user-guide.md) and **`P03-user-guide.md`** when published.
