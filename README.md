![Documentation Quality](https://github.com/RoyPiring/agentic-systems-engineering/actions/workflows/docs-lint.yml/badge.svg)

# Agentic Systems Engineering

AI agent systems built to production standards — from problem framing through architecture, implementation, and evidence-backed validation.

Each engineering system starts with a real-world problem and works backward to the technology. Every claim traces to an artifact.

---

## Systems

Portfolio slots **1–12** match [ROADMAP.md](./ROADMAP.md). **Published folders** today: **#1** and **#10** under [`engineering-systems/`](./engineering-systems/).

| # | System | What It Solves | Tech Stack | Status |
|---|--------|---------------|-----------|--------|
| 1 | [Retrieval Backbone — Multi-Domain Knowledge](./engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/) | Measured, citation-aware retrieval across files and web — local Qdrant + Ollama by default | Python, Qdrant, LlamaIndex, Ollama, Firecrawl (optional) | 🔨 **P01–P03** [PASS](./engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/validation.md); **P04** next |
| 2–9 | *Planned* | See roadmap | — | 📋 |
| 10 | [Multimodal Knowledge Artifact Factory](./engineering-systems/multimodal-knowledge-artifact-factory/) | Turn markdown research into local audio, interactive UI, and study exports — $0 recurring cost | Rust, Python, Dioxus | ✅ **P01–P04** on `main` |
| 11–12 | *Planned* | See roadmap | — | 📋 |

**Summary:** **#10** is the first system **fully merged** to `main`. **#1** has **P01–P03** with evidence and validation **PASS**. Full grid → [ROADMAP.md](./ROADMAP.md) · [Engineering systems index](./engineering-systems/README.md)

---

## How Each System Is Built

Every system follows the same engineering standard:

1. **Business Context** — what problem, for whom, under what constraints
2. **Architecture** — components, boundaries, ADRs, tradeoffs, failure modes
3. **Implementation** — phased delivery with execution records and evidence
4. **Validation** — expected vs actual results, negative cases, explicit pass criteria

---

## Who This Is For

| Role | You're trying to… | Start here | Time |
|------|-------------------|------------|:----:|
| **Recruiter** | Assess role or team fit from this portfolio | This README — systems table + how systems are built | 30 sec |
| **Hiring manager** | Judge problem framing and architectural judgment | [Engineering systems](./engineering-systems/README.md) → open a system → **`business-context.md`** → **`architecture.md`** | 2 min |
| **Engineer** | Run a system locally and reproduce results | Pick a system under [Engineering systems](./engineering-systems/README.md), then **`user-guides/`** (per-phase runbooks) | 15–60 min |
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

## Standards

- **Evidence-first** — every claim traces to an artifact
- **Progressive disclosure** — readable in 90 seconds at the top, deep enough to sustain a 45-minute technical review
- **PR-based workflow** — every system enters via feature branch and pull request
- **CI-enforced quality** — markdown lint, link check, and structure validation on every PR

See [OPERATING_REQUIREMENTS.md](./OPERATING_REQUIREMENTS.md) and [QUALITY_STANDARDS.md](./QUALITY_STANDARDS.md) for details.

---

## Legal and Maintenance

This repository is a **portfolio**: it presents engineering systems and project-series narratives for reviewers. It is not packaged as reusable open-source software. There is no `LICENSE` file and no `CODEOWNERS` — use the material as read-only context for how work is framed, built, and verified.
