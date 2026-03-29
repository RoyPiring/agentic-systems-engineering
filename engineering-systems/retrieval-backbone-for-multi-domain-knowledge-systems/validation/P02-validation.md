# P02 validation — Citation-aware retrieval (LlamaIndex and Ollama)

**Status:** **Pending** — run [`build/query_pipeline.py`](../build/query_pipeline.py) locally and attach evidence per [user-guides/P02-user-guide.md](../user-guides/P02-user-guide.md).

## Scope

Prove **LlamaIndex** loads the **P01** Qdrant collection, uses **Ollama** for **LLM** (`llama3.2` default) and **embeddings** (`nomic-embed-text`, matching ingest), retrieves with **`similarity_top_k` = 3**, and returns an answer with **traceable source nodes** (printed **Citations** section).

## Operator runbook

Follow **[P02 user guide](../user-guides/P02-user-guide.md)** for prerequisites, commands, and suggested evidence filenames under [`../executions/evidence/p02/`](../executions/evidence/p02/).

## Checks (to close as PASS)

| # | Check | Command / action | Expected | Result |
| --- | --- | --- | --- | --- |
| V1 | Ollama models | `ollama list` | `llama3.2` and `nomic-embed-text` present | *pending* |
| V2 | Query run | From `build/`: `python query_pipeline.py --query "…"` | Exit **0**; **Answer** + **Citations**; ≤3 source nodes | *pending* |
| V3 | Citation metadata | Inspect stdout | Node ids / snippets; file metadata via safe keys | *pending* |
| V4 | Cost posture | Code review / config | No required OpenAI keys; **Settings** use Ollama | *pending* — see script |

## Evidence

Link transcripts in [`../executions/evidence/p02/`](../executions/evidence/p02/) (e.g. `p02-query-run.txt`, `p02-ollama-list.txt`, optional `p02-pip-freeze.txt`) as described in the user guide.

## Verdict

**Pending** — complete the table above and attach evidence to move to **PASS**.
