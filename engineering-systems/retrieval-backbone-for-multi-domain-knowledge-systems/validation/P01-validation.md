# P01 validation — Document ingestion and vector indexing

**Status:** **PASS** (2026-03-28) — see evidence under [`../executions/evidence/p01/`](../executions/evidence/p01/).

## Scope

Prove local **Unstructured → LlamaIndex → Ollama embeddings → Qdrant** for **`build/data/`** samples and collection **`multi_domain_docs`**.

## Checks

| # | Check | Command / action | Expected | Result |
| --- | --- | --- | --- | --- |
| V1 | Qdrant HTTP | `curl http://localhost:6333` | JSON with version | **PASS** — `p01-curl-qdrant.txt` (v1.17.1) |
| V2 | Ollama model | `ollama list` | `nomic-embed-text` present | **PASS** — `p01-ollama-list.txt` |
| V3 | Ingest run | From `build/`: `run_ingest_windows.ps1` or short-path `python ingest.py` | Exit **0**; prints load count + indexing success | **PASS** — `p01-ingest-run.txt` (2 nodes, “Vector indexing complete.”) |
| V4 | Collection | Qdrant API | **`multi_domain_docs`** exists with points | **PASS** — `p01-qdrant-collection.txt` (`points_count` 2, vectors dim 768) |
| V5 | Cost posture | Code review / config | No required OpenAI (or other paid) keys for this path | **PASS** — Ollama + local Qdrant only; LLM unset (`MockLLM` warning acceptable for index-only) |

## Evidence

Link transcripts in [`../executions/evidence/p01/`](../executions/evidence/p01/) (e.g. `p01-ingest-run.txt`, `p01-curl-qdrant.txt`).

## Negative / edge (at least one)

| Scenario | What to observe | Result |
| --- | --- | --- |
| Empty or missing `build/data/` | Clear error or zero-doc handling | **PASS** — exit **1**, stderr explains no `.md`/`.pdf` (`p01-negative-edge.txt`) |
| Bad Qdrant URL | Connection error surfaced | **PASS** — “cannot reach Qdrant”, exit **1** (`p01-negative-edge.txt`) |

## Verdict

**PASS** — **V1–V5** satisfied; negatives documented in [`../executions/evidence/p01/p01-negative-edge.txt`](../executions/evidence/p01/p01-negative-edge.txt). **Note:** Validation host used **Python 3.13.11** and **Windows long-path workarounds** (`run_ingest_windows.ps1`, sdist `charset-normalizer`); reproduce on **3.12** / Linux per `implementation.md` if needed.
