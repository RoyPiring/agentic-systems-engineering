# P04 validation — Quality measurement and service packaging (Ragas)

**Status:** **PASS** — **2026-03-31**

## Scope

Prove **Ragas** runs **context precision** and **answer relevancy** with **explicit Ollama** judge models (no paid API default), using rows produced from the **live** **`RetrievalBackboneService`** pipeline when Qdrant is available; prove a **separate consumer script** uses **only** the packaged public API.

## Checks

| # | Check | Command / action | Expected | Result |
| --- | --- | --- | --- | --- |
| V1 | Qdrant | Existing Docker container **`qdrant-p01`** started; collection **`multi_domain_docs`** | Points present after ingest | **PASS** — `p04-docker-qdrant.txt`, `p04-curl-qdrant-collection.txt` |
| V2 | Baseline Ragas | `python ragas_eval.py --mode baseline` | Non-NaN **context_precision** + **answer_relevancy** | **PASS** — `p04-ragas-baseline.txt` |
| V3 | Batch Ragas | `python ragas_eval.py --mode batch --sleep-between 2` | Aggregates for 3 labeled domains | **PASS** — `p04-ragas-batch.txt` |
| V4 | Consumer API | `python consumer_demo.py` | Answer + context count + citation labels | **PASS** — `p04-consumer-demo.txt` |
| V5 | Toolchain | `python --version`, `ollama list`, `pip freeze` | Repro snapshot | **PASS** — `p04-python-version.txt`, `p04-ollama-list.txt`, `p04-pip-freeze.txt` |
| V6 | No OpenAI default | Code review **`ragas_eval.py`** | Judge = **`ChatOllama`** only | **PASS** |

## Evidence

[`../executions/evidence/p04/`](../executions/evidence/p04/) — manifest **[`README.md`](../executions/evidence/p04/README.md)**.

## Limitations

- **Python 3.13.11** used for this run (plan text targets **3.12**).
- **Judge model:** **`qwen3:8b`** recommended default; **`llama3.2`** alone may yield **NaN** for Ragas when structured JSON parsing fails.
- **Indexed vectors** in Qdrant UI may show **0** while **`points_count`** > 0 until optimization catches up — see collection JSON in evidence.

## Verdict

**PASS** — V1–V6 satisfied with committed artifacts.
