# Case study data

## Committed corpus (canonical)

The **reference case study** uses the portfolio sample at:

| Path | Role |
| --- | --- |
| [`../build/data/sample.md`](../build/data/sample.md) | Markdown sections A–C (Qdrant, Ollama, PDF/Unstructured topic text) |
| [`../build/data/README.md`](../build/data/README.md) | Operator notes for `data/` |

**P01** ingests from **`build/data/`** per [../build/README.md](../build/README.md). No extra files are **required** under **`case-study/data/`** for the linear [RUNBOOK](../RUNBOOK.md).

## Optional: real PDF for stronger R1

[`sample.md`](../build/data/sample.md) Section C **describes** PDF + Unstructured; the **pdf_topic** Ragas row is grounded in that text. To exercise a **real** PDF partition through Unstructured:

1. Add a **small** PDF you have rights to redistribute under **`../build/data/`** (e.g. `sample.pdf`).
2. Re-run **`python ingest.py`** from **`build/`** with your ingest script configuration (see [P01 user guide](../user-guides/P01-user-guide.md)).
3. Re-verify citations and Ragas batch.

**License / source:** Only commit material you may redistribute.

## Queries

Exact strings for eval and spot checks: [queries.md](./queries.md).
