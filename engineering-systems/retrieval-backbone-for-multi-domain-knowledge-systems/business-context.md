> ← [Retrieval Backbone — Multi-Domain Knowledge](./README.md) · [All Systems](../README.md) · [Home](../../README.md)

# Business Context

## Problem Statement

Teams building retrieval-augmented workflows often assemble one-off pipelines per domain. Without a **reusable backbone** and **explicit quality measurement**, answers drift, citations are weak or missing, and regressions go unnoticed when content or models change.

## Why This Matters

- **Builders** need a repeatable path from heterogeneous documents (markdown, PDF, HTML) through vector indexing to **citation-aware** answers they can trust and tune.
- **Operators** benefit from **local-first** execution and predictable cost (no mandatory paid APIs in the series design).
- **Reviewers** can inspect a phased story: ingest → retrieval → web augmentation → evaluation and packaging—with evidence per phase.

## Objectives

- **P01:** Ingest representative document types and index vectors in **Qdrant** using **Unstructured** (or equivalent) for parsing/chunking.
- **P02:** Run **citation-aware** query flows with **LlamaIndex** and **Ollama** (local LLM + embeddings).
- **P03:** Integrate **live web content** via **Firecrawl** (self-hosted in scope per series intent).
- **P04:** Measure answer quality with **Ragas** and package the retrieval stack as a **coherent service-shaped** artifact for reuse.
- Hold **$0 recurring API spend** as the default posture: local inference and self-hosted dependencies where the series specifies them.

## Success Criteria

| Metric | Target | Validation Method |
| --- | --- | --- |
| Indexed corpora | Markdown + PDF (+ HTML where in scope) discoverable in Qdrant with stable IDs | P01 validation + execution record |
| Traceable answers | Retrieval steps expose chunk/source references usable for citations | P02 validation **PASS** (2026-03-29); [`validation/P02-validation.md`](./validation/P02-validation.md) + [`executions/evidence/p02/`](./executions/evidence/p02/) |
| Web-augmented retrieval | Crawled pages join the same retrieval contract as file corpora | P03 validation |
| Measured quality | Ragas (or documented equivalent) scores recorded for a fixed eval set | P04 validation |
| Cost posture | No required paid third-party inference for the default path | Documented in `validation.md` |

## Constraints

- **Budget:** **$0 recurring** target; **Ollama** for local LLM/embeddings; **Qdrant** local/Docker; **Firecrawl** self-hosted per series framing—avoid mandatory cloud API fees in the default story.
- **Time:** Beginner-oriented series; four projects with bounded effort per guide.
- **Organizational:** Portfolio / lab context—no production SLA, multi-tenant product, or compliance certification claims.
- **Technical:** **Python 3.12**, **LlamaIndex**, **Qdrant**, **Unstructured**, **Ragas**, **Ollama** (e.g. Llama 3.2, nomic-embed-text); local workstation or Docker-capable machine.

## Scope

### In Scope

- Document ingestion (markdown, PDF, HTML/web-derived content as defined in each phase).
- Vector indexing with Qdrant.
- LlamaIndex query pipelines and citation tracing.
- Ragas evaluation hooks.
- Local LLM inference defaults.
- Retrieval parameter tuning experiments documented with evidence.
- Reusable service-style packaging in the final phase.

### Out Of Scope

- Fine-tuning embedding or chat models.
- Production cloud deployment and multi-region operations.
- Authentication, authorization, and enterprise IAM.
- Real-time streaming ingestion at scale.
- Paid managed vector tiers as a **requirement** for the default path.

### Non-Goals

- Replacing a specific vendor product feature-for-feature.
- Guaranteeing latency/scale on arbitrary hardware without documentation.
- Certifying security beyond “local operator + explicit trust boundaries” assumptions.

## Stakeholders

| Stakeholder | Need | Why It Matters |
| --- | --- | --- |
| Operator / builder | Repeatable runbooks and honest validation | Can reproduce and extend the backbone |
| Downstream agent designers | Stable retrieval + citation contracts | Safer composition into larger workflows |
| Technical reviewer | Clear boundaries, ADRs, and evidence | Judgment visible without private context |

## Risks

- **Dependency and version drift:** LlamaIndex, Qdrant, and Unstructured move quickly—pin versions in execution records.
- **Resource intensity:** Local models and crawlers need RAM, disk, and CPU; document minimums as phases complete.
- **Eval validity:** Ragas scores depend on test sets and judge models—document limitations explicitly in P04.
- **Scope creep:** Paid APIs or hosted-only services can simplify demos but break the cost story—keep defaults local unless documented as optional.

## Related docs

- [System README](./README.md)
- [Architecture](./architecture.md)
- [Implementation phases](./implementation.md)
- [Validation rollup](./validation.md)
- [P02 operator runbook](./user-guides/P02-user-guide.md) (citation-aware query path)
