![Documentation Quality](https://github.com/RoyPiring/agentic-systems-engineering/actions/workflows/docs-lint.yml/badge.svg)

# Agentic Systems Engineering

AI agent systems built to production standards — from problem framing through architecture, implementation, and evidence-backed validation.

Each engineering system starts with a real-world problem and works backward to the technology. Every claim traces to an artifact.

---

## Published Now

Published folders today: **#1** and **#10** under [`engineering-systems/`](./engineering-systems/).

| # | System | What It Solves | Tech Stack | Status |
|---|--------|---------------|-----------|--------|
| 1 | [Retrieval Backbone — Multi-Domain Knowledge](./engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/) | Measured, citation-aware retrieval across files and web — local Qdrant + Ollama by default | Python, Qdrant, LlamaIndex, Ollama, Firecrawl (optional), Ragas | ✅ **P01–P04** [PASS](./engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/validation.md) |
| 10 | [Multimodal Knowledge Artifact Factory](./engineering-systems/multimodal-knowledge-artifact-factory/) | Turn markdown research into local audio, interactive UI, and study exports — $0 recurring cost | Rust, Python, Dioxus | ✅ **P01–P04** on `main` |

**Summary:** **#10** is fully merged to `main` with **P01–P04** shipped. **#1** has **P01–P04** with committed evidence and validation **PASS**. Full grid: [ROADMAP.md](./ROADMAP.md) · [Engineering systems index](./engineering-systems/README.md)

## Portfolio KPI Snapshot

| Metric | Current |
|---|---:|
| Published systems | 2 |
| Systems with roll-up validation **PASS** | 2 |
| Systems with per-phase operator guides | 2 |
| Systems with committed execution evidence | 2 |
| Root-level CI quality gate | 1 active workflow badge |

## Proof At A Glance

| System | Strongest proof | Why it matters |
|---|---|---|
| [Retrieval Backbone](./engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/) | [P04 validation](./engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/validation/P04-validation.md), [Ragas batch evidence](./engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/executions/evidence/p04/p04-ragas-batch.txt), [consumer demo](./engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/executions/evidence/p04/p04-consumer-demo.txt) | Shows measured retrieval quality and a service-shaped public interface, not just ingestion scripts |
| [Multimodal Artifact Factory](./engineering-systems/multimodal-knowledge-artifact-factory/) | [validation](./engineering-systems/multimodal-knowledge-artifact-factory/validation.md), [P03 viewer build evidence](./engineering-systems/multimodal-knowledge-artifact-factory/executions/evidence/p03/p03-viewer-build.txt), [P04 exports](./engineering-systems/multimodal-knowledge-artifact-factory/executions/evidence/p04/exports/) | Shows an end-to-end local system from parser to UI to study artifacts |

## 2-Minute Review Path

1. Start with the published systems table above.
2. Open [Retrieval Backbone](./engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/) or [Multimodal Knowledge Artifact Factory](./engineering-systems/multimodal-knowledge-artifact-factory/).
3. Read that system's `README.md` and `validation.md`.
4. Open the linked `Best Evidence` artifacts if you need proof before code.

---

## How Each System Is Built

Every system follows the same engineering standard:

1. **Business Context** — what problem, for whom, under what constraints
2. **Architecture** — components, boundaries, ADRs, tradeoffs, failure modes
3. **Implementation** — phased delivery with execution records and evidence
4. **Validation** — expected vs actual results, negative cases, explicit pass criteria

---

## Engineering Judgment

This portfolio is organized around systems, not isolated demos, because hiring teams need to see tradeoffs, sequencing, and proof in the same place. Local-first defaults and explicit validation gates are deliberate: they expose how each system behaves under practical constraints instead of hiding behind managed services or claims without evidence. The result is a portfolio optimized for technical trust, not just presentation.

---

## Who This Is For

| Role | You're trying to… | Start here | Time |
|------|-------------------|------------|:----:|
| **Recruiter** | Assess role or team fit from this portfolio | This README — systems table + how systems are built | 30 sec |
| **Hiring manager** | Judge problem framing and architectural judgment | [Engineering systems](./engineering-systems/README.md) → open a system → **`business-context.md`** → **`architecture.md`** | 2 min |
| **Engineer** | Understand how a system is designed and delivered — peer-level technical read | Pick a system under [Engineering systems](./engineering-systems/README.md) → **`architecture.md`** → **`implementation.md`** → **`executions/`** (record, plans, evidence) | 15–45 min |
| **Operator** | Operate, hand off, or verify against committed proof | Same system folder → **`user-guides/`**, **`validation.md`** (PASS rows + limitations), and **`executions/evidence/`** | 15–45 min |

---

## What This Proves

| Capability | What a reviewer should conclude | Source |
|------------|--------------------------------|--------|
| Problem framing | Work starts with a business or mission need — not tools | `engineering-systems/*/business-context.md` |
| Architectural judgment | Tradeoffs, boundaries, risks, and ADRs are explicit | `engineering-systems/*/architecture.md` |
| Delivery discipline | Systems implemented in phases with documented sequencing and evidence | `engineering-systems/*/implementation.md` |
| Evidence rigor | Claims backed by validation artifacts and observed results | `engineering-systems/*/validation.md` |

---

## Roadmap

Portfolio slots **1–12** match [ROADMAP.md](./ROADMAP.md). Planned systems and target quarters live there so the landing page can lead with shipped work instead of future inventory.

---

## Standards

- **Evidence-first** — every claim traces to an artifact
- **Progressive disclosure** — readable in 90 seconds at the top, deep enough to sustain a 45-minute technical review
- **PR-based workflow** — every system enters via feature branch and pull request
- **CI-enforced quality** — markdown lint, link check, and structure validation on every PR

See [OPERATING_REQUIREMENTS.md](./OPERATING_REQUIREMENTS.md) and [QUALITY_STANDARDS.md](./QUALITY_STANDARDS.md) for details.

---

## Legal and Maintenance

This repository is a **portfolio**: it presents engineering systems and project-series narratives for reviewers. It is not packaged as reusable open-source software. There is no `LICENSE` file and no `CODEOWNERS` — use the material as read-only context for how work is framed, built, and verified.
