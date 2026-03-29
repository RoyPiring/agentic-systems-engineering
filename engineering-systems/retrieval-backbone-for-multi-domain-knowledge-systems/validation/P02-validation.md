# P02 validation — Citation-aware retrieval (LlamaIndex and Ollama)

**Status:** **PASS** (2026-03-29) — see evidence under [`../executions/evidence/p02/`](../executions/evidence/p02/). Operator runbook: [user-guides/P02-user-guide.md](../user-guides/P02-user-guide.md).

## Scope

Prove **LlamaIndex** loads the **P01** Qdrant collection, uses **Ollama** for **LLM** (`llama3.2`) and **embeddings** (`nomic-embed-text`, matching ingest), retrieves with **`similarity_top_k` = 3**, and returns an answer with **traceable source nodes** (printed **Citations** section).

## Checks

| # | Check | Command / action | Expected | Result |
| --- | --- | --- | --- | --- |
| V1 | Qdrant HTTP | `curl http://localhost:6333` | JSON with version | **PASS** — [`p02-curl-qdrant.txt`](../executions/evidence/p02/p02-curl-qdrant.txt) (v1.17.1) |
| V2 | Ollama models | `ollama list` | `llama3.2` and `nomic-embed-text` present | **PASS** — [`p02-ollama-list.txt`](../executions/evidence/p02/p02-ollama-list.txt) |
| V3 | Query run | From `build/`: `python query_pipeline.py --query "…"` | Exit **0**; **Answer** + **Citations**; ≤3 source nodes | **PASS** — [`p02-query-run.txt`](../executions/evidence/p02/p02-query-run.txt) |
| V4 | Collection | Qdrant API `GET /collections/multi_domain_docs` | Collection **green** with points | **PASS** — [`p02-qdrant-collection.txt`](../executions/evidence/p02/p02-qdrant-collection.txt) (`points_count` 4, dim 768) |
| V5 | Cost posture | Code review / config | No required OpenAI keys; **Settings** use Ollama | **PASS** — [`query_pipeline.py`](../build/query_pipeline.py) |
| V6 | Deps | `pip freeze` in venv | Pinned snapshot for repro | **PASS** — [`p02-pip-freeze.txt`](../executions/evidence/p02/p02-pip-freeze.txt) |

## Evidence

[`../executions/evidence/p02/`](../executions/evidence/p02/) — `p02-query-run.txt`, `p02-ollama-list.txt`, `p02-curl-qdrant.txt`, `p02-qdrant-collection.txt`, `p02-pip-freeze.txt`, `p02-python-version.txt`.

## Verdict

**PASS** — **V1–V6** satisfied. **Note:** Validation host **Python 3.13.11**; `llama-index-core` **0.14.19** with `llama-index-vector-stores-qdrant` **0.10.0** required for **qdrant-client** **1.17.x** — documented in [`build/requirements.txt`](../build/requirements.txt) and freeze file.
