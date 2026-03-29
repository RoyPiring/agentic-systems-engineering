# P01 validation — Document ingestion and vector indexing

**Status:** **Pending** — execute after [`../executions/implementation/P01-implementation-plan.md`](../executions/implementation/P01-implementation-plan.md).

## Scope

Prove local **Unstructured → LlamaIndex → Ollama embeddings → Qdrant** for **`build/data/`** samples and collection **`multi_domain_docs`**.

## Checks

| # | Check | Command / action | Expected | Result |
| --- | --- | --- | --- | --- |
| V1 | Qdrant HTTP | `curl http://localhost:6333` | JSON with version | Pending |
| V2 | Ollama model | `ollama list` | `nomic-embed-text` present | Pending |
| V3 | Ingest run | From `build/`: `python ingest.py` | Exit **0**; prints load count + indexing success | Pending |
| V4 | Collection | Qdrant dashboard or API | **`multi_domain_docs`** exists with points | Pending |
| V5 | Cost posture | Code review / config | No required OpenAI (or other paid) keys for this path | Pending |

## Evidence

Link transcripts in [`../executions/evidence/p01/`](../executions/evidence/p01/) (e.g. `p01-ingest-run.txt`, `p01-curl-qdrant.txt`).

## Negative / edge (at least one)

| Scenario | What to observe | Result |
| --- | --- | --- |
| Empty or missing `build/data/` | Clear error or zero-doc handling | Pending |
| Optional: bad Qdrant URL | Connection error surfaced | Pending |

## Verdict

**Pending** — set to **PASS** when all **V1–V5** are satisfied and negatives documented as tested or **N/A** with rationale.
