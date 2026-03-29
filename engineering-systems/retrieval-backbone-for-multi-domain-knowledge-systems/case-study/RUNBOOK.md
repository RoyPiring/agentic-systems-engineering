# Runbook — Multi-domain retrieval smoke (scaffold)

**Before you start:** Open [../user-guides/README.md](../user-guides/README.md) and confirm **Python**, **Docker** (for Qdrant), and **Ollama** match the phase guides. **Working directory** for runnable scripts is **`../build/`**.

End-to-end order follows [../user-guides/SERIES-user-guide.md](../user-guides/SERIES-user-guide.md) (P01–P03 linked; P04 pending).

## 0. Data

- See [`data/README.md`](./data/README.md) for committed samples or BYO files. The portfolio **`build/data/`** sample is exercised by P01/P02 evidence.

## 1. P01 — Ingest and index

Follow [../user-guides/P01-user-guide.md](../user-guides/P01-user-guide.md) and [../executions/implementation/P01-implementation-plan.md](../executions/implementation/P01-implementation-plan.md).

**Expected:** Vectors and metadata in Qdrant collection **`multi_domain_docs`**; evidence under [../executions/evidence/p01/](../executions/evidence/p01/).

## 2. P02 — Citation-aware retrieval

Follow [../user-guides/P02-user-guide.md](../user-guides/P02-user-guide.md) and [../executions/implementation/P02-implementation-plan.md](../executions/implementation/P02-implementation-plan.md). Run **`python query_pipeline.py`** from **`build/`**.

**Expected:** Stdout **Answer** + **Citations** mapping to stored nodes; evidence under [../executions/evidence/p02/](../executions/evidence/p02/).

## 3. P03 — Live web (Firecrawl or synthetic)

Follow [../user-guides/P03-user-guide.md](../user-guides/P03-user-guide.md) and [../executions/implementation/P03-implementation-plan.md](../executions/implementation/P03-implementation-plan.md). From **`build/`**: **`python ingest_web.py`** (Firecrawl up) or **`python ingest_web.py --synthetic-evidence`** when Firecrawl is unavailable; then **`python query_pipeline.py`** and confirm **`source_url:`** in **Citations**.

**Expected:** Appended vectors with web metadata; evidence under [../executions/evidence/p03/](../executions/evidence/p03/) — see [P03 validation](../validation/P03-validation.md) **PASS** and [README](../executions/evidence/p03/README.md).

## 4. P04 — Ragas and packaging

**Expected:** Metrics captured for the eval set; evidence under `../executions/evidence/p04/` (guide **TBD**).

## Verification

| ID | Requirement | Evidence (file / observation) |
| --- | --- | --- |
| R1 | Indexed corpus | **PASS** — [validation/P01-validation.md](../validation/P01-validation.md); e.g. [p01-ingest-run.txt](../executions/evidence/p01/p01-ingest-run.txt), [p01-qdrant-collection.txt](../executions/evidence/p01/p01-qdrant-collection.txt) |
| R2 | Cited answers | **PASS** — [validation/P02-validation.md](../validation/P02-validation.md); e.g. [p02-query-run.txt](../executions/evidence/p02/p02-query-run.txt) |
| R3 | Web slice (if in scope) | **PASS** — [validation/P03-validation.md](../validation/P03-validation.md); [p03-query-web-citation.txt](../executions/evidence/p03/p03-query-web-citation.txt); manifest [README](../executions/evidence/p03/README.md); caveats [validation.md](../validation.md#limitations) |
| R4 | Measured quality | **TBD** — P04 |
