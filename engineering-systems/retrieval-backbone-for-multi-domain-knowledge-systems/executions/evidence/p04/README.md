# P04 evidence — Ragas + packaged service

Transcripts for **[P04 validation](../../../validation/P04-validation.md)** (quality measurement and service packaging). Operator steps: **[P04 user guide](../../../user-guides/P04-user-guide.md)**.

## Files (2026-03-31 run)

| File | Role |
| --- | --- |
| `p04-docker-qdrant.txt` | Running Qdrant container (`qdrant-p01` on **6333**) |
| `p04-curl-qdrant-collection.txt` | `GET /collections/multi_domain_docs` after ingest |
| `p04-ollama-list.txt` | `ollama list` (generation + judge models) |
| `p04-python-version.txt` | Python interpreter used for this phase |
| `p04-ragas-baseline.txt` | `ragas_eval.py --mode baseline` (live pipeline) |
| `p04-ragas-batch.txt` | `ragas_eval.py --mode batch --sleep-between 2` |
| `p04-consumer-demo.txt` | `consumer_demo.py` (public API only) |
| `p04-pip-freeze.txt` | `pip freeze` (includes **ragas**, **langchain-ollama**) |

## Fallbacks

- **`ragas_eval.py --synthetic-rows`** — hand-crafted dataset rows + Ragas only when Qdrant is down (same metric contract as P03 synthetic ingest).
- **Judge LLM:** default **`OLLAMA_EVAL_LLM_MODEL=qwen3:8b`** for reliable JSON + structured outputs; RAG **generation** stays **`llama3.2`** via **`OLLAMA_LLM_MODEL`**.
