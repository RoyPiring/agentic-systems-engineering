# Requirements — Multi-domain retrieval smoke (scaffold)

Plain-language criteria. When every item is true after [RUNBOOK.md](./RUNBOOK.md), this case study scenario is satisfied **by design**.

1. **R1 — Indexed corpus:** A small mixed corpus (e.g. markdown + PDF) from [`data/`](./data/) is ingested and queryable from **Qdrant** with stable chunk metadata (**P01**).
2. **R2 — Cited answers:** For fixed questions, the **P02** pipeline returns answers whose citations map to stored chunks (no orphan references).
3. **R3 — Web slice (optional for minimal smoke):** If **P03** is in scope for this run, at least one crawled page participates in retrieval under the same contract as file corpora.
4. **R4 — Measured quality:** **P04** Ragas (or documented equivalent) scores are recorded for the eval set used in this scenario.

**Out of scope for this scaffold:** Production SLOs, authn/z, cloud deployment, paid API requirements.
