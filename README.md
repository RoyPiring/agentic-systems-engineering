![Documentation Quality](https://github.com/RoyPiring/agentic-systems-engineering/actions/workflows/docs-lint.yml/badge.svg)

# Agentic Systems Engineering

AI agent systems built to production standards — from problem framing through architecture, implementation, and evidence-backed validation.

Each engineering system starts with a real-world problem and works backward to the technology. Every claim traces to an artifact.

---

## Systems

| # | System | What It Solves | Tech Stack | Status |
|---|--------|---------------|-----------|--------|
| 1 | [Multimodal Knowledge Artifact Factory](./engineering-systems/multimodal-knowledge-artifact-factory/) | Turn markdown research into local audio, interactive UI, and study exports — $0 recurring cost | Rust, Python, Dioxus | ✅ P01–P04 shipped |
| 2–12 | *Planned* | | | 📋 |

**1 of 12 systems shipped.** Full roadmap → [ROADMAP.md](./ROADMAP.md)

---

## How Each System Is Built

Every system follows the same engineering standard:

1. **Business Context** — what problem, for whom, under what constraints
2. **Architecture** — components, boundaries, ADRs, tradeoffs, failure modes
3. **Implementation** — phased delivery with execution records and evidence
4. **Validation** — expected vs actual results, negative cases, explicit pass criteria

---

## Who This Is For

| You are a… | Start here | Time |
|-----------|-----------|:----:|
| **Recruiter** assessing role fit | This README — systems table + standards | 30 sec |
| **Hiring manager** evaluating judgment | [business-context.md](./engineering-systems/multimodal-knowledge-artifact-factory/business-context.md) → [architecture.md](./engineering-systems/multimodal-knowledge-artifact-factory/architecture.md) | 2 min |
| **Principal engineer** reviewing depth | [architecture.md](./engineering-systems/multimodal-knowledge-artifact-factory/architecture.md) → [validation.md](./engineering-systems/multimodal-knowledge-artifact-factory/validation.md) → [evidence/](./engineering-systems/multimodal-knowledge-artifact-factory/executions/evidence/) | 5 min |
| **Operator** who wants to run it | [user-guides/](./engineering-systems/multimodal-knowledge-artifact-factory/user-guides/) | 15+ min |

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
