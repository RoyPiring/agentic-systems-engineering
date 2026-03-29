# Runbook — Multi-domain retrieval smoke (scaffold)

**Before you start:** Complete [../user-guides/README.md](../user-guides/README.md) and confirm **Python**, **Docker** (for Qdrant), and **Ollama** match the phase guides. **Working directory** for commands is typically **`../build/`** once P01 code exists.

End-to-end order must follow [../user-guides/SERIES-user-guide.md](../user-guides/SERIES-user-guide.md) when that guide is no longer a placeholder.

## 0. Data

- See [`data/README.md`](./data/README.md) for committed samples or BYO files.

## 1. P01 — Ingest and index

Use [../executions/implementation/P01-implementation-plan.md](../executions/implementation/P01-implementation-plan.md) (replace placeholder before execution) and future `user-guides/P01-user-guide.md`.

**Expected:** Vectors and metadata visible in the target Qdrant collection; evidence under `../executions/evidence/p01/`.

## 2. P02 — Citation-aware retrieval

**Expected:** Answers include retrievable source references; evidence under `../executions/evidence/p02/`.

## 3. P03 — Live web (if included)

**Expected:** Crawled content indexed like file corpora; evidence under `../executions/evidence/p03/`.

## 4. P04 — Ragas and packaging

**Expected:** Metrics captured for the eval set; evidence under `../executions/evidence/p04/`.

## Verification

| ID | Requirement | Evidence (file / observation) |
| --- | --- | --- |
| R1 | Indexed corpus | TBD after P01 |
| R2 | Cited answers | TBD after P02 |
| R3 | Web slice (if in scope) | TBD after P03 |
| R4 | Measured quality | TBD after P04 |
