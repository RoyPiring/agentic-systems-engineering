# Requirements — Local knowledge spine (case study)

**Scenario (one line):** Prove the Retrieval Backbone runs **end-to-end** for a small team that indexes **Markdown** (+ optional PDF), adds a **web-shaped** slice, answers with **citations**, and **measures** quality locally—aligned with [`SCENARIO.md`](./SCENARIO.md).

When every item below is true after [RUNBOOK.md](./RUNBOOK.md), this case study is satisfied **by design**.

## Acceptance criteria

1. **R1 — Indexed corpus:** Committed corpus under [`../build/data/`](../build/data/) (at minimum [`sample.md`](../build/data/sample.md)) is ingested into **Qdrant** collection **`multi_domain_docs`** with stable chunk metadata (**P01**).
2. **R2 — Cited answers:** For fixed questions, the **P02** pipeline returns answers whose citations map to stored chunks (no orphan references). **Portfolio:** validated **PASS** — see [`../validation/P02-validation.md`](../validation/P02-validation.md) and [`../executions/evidence/p02/p02-query-run.txt`](../executions/evidence/p02/p02-query-run.txt).
3. **R3 — Web slice:** At least one web-derived (or **`--synthetic-evidence`**) document participates in retrieval; **Citations** can expose **`source_url:`** under the same contract as file corpora (**P03**).
4. **R4 — Measured quality:** **P04** Ragas scores (**context_precision**, **answer_relevancy**) are recorded for the batch eval set; **`consumer_demo.py`** exercises the public service surface only.

**Out of scope:** Production SLOs, authn/z, cloud deployment, mandatory paid APIs.

## Representative queries

These match **`build/ragas_eval.py`** `batch_rows()` (and manual **`query_pipeline.py`** checks in the RUNBOOK):

| Domain label | Question (verbatim) |
| ------------- | -------------------- |
| `markdown_file` | What vector database does the indexed documentation say is used locally in this series? |
| `pdf_topic` | According to the indexed corpus, what file type can Unstructured partition for the same Qdrant collection as Markdown? |
| `web_synthetic` | According to the indexed documentation about Python environment variables, what does PEP 405 describe? |

Full list with notes: [data/queries.md](./data/queries.md).
