# Agentic Systems Engineering

AI agents, LLM routing, RAG, eval pipelines, memory, and MCP — built to production standards with observable, governed, and reliable agent systems.

---

## Why This Matters

This repository shows how problems in **Agentic** are framed, designed, built, and verified.
Each engineering system starts with a real-world problem and works backward to the technology.

## What This Proves

| Capability | What A Reviewer Should Conclude | Source |
|---|---|---|
| Problem framing | Work starts with business or mission need — not tools | `engineering-systems/*/business-context.md` |
| Architectural judgment | Tradeoffs, boundaries, risks, and decisions are explicit | `engineering-systems/*/architecture.md` |
| Delivery discipline | Systems implemented in phases with documented sequencing | `engineering-systems/*/implementation.md` |
| Evidence rigor | Claims backed by validation artifacts and observed results | `engineering-systems/*/validation.md` |

## Intended Audience

- **Recruiters / non-technical** — start here for role fit, themes, and outcomes
- **Hiring managers** — use featured systems and business context to evaluate judgment
- **Peer engineers / principal reviewers** — use architecture, implementation, and validation for technical depth

## How To Navigate

1. Read this README for the repository story and top signals
2. Open `FEATURE_SYSTEMS.md` for the fastest path to the strongest systems
3. Open `engineering-systems/README.md` for the full index
4. Open a system's documents in order: business-context → architecture → implementation → validation

## Featured Systems

*Updated as systems are published.*

| System | What It Demonstrates | Status |
|---|---|---|
| multimodal-knowledge-artifact-factory | P01–P03: Markdown parse CLI, stub-audio bridge, Dioxus **Knowledge Viewer**; ADRs + validation per phase | In flight on feature branch through **P03** (merge when PR green); **P04** planned |

## Project Library Source

Systems in this repo are built from the **06-Agentic** categories of the PineappleKingdom Project Library.

## Legal and maintenance posture

This repository is a **portfolio**: it presents **engineering systems and practical project-series narratives** for reviewers and learners. It is **not** packaged or positioned as reusable open-source software that requires a SPDX license grant. There is **no `LICENSE` file** and **no `CODEOWNERS`** — use the material as **read-only context** for how work is framed, built, and verified.

## Operating Standards

- Evidence-first — every claim traces to an artifact
- Progressive disclosure — readable in 90 seconds at the top, deep enough to sustain a 45-minute technical interview
- PR-based workflow — every system enters via feature branch and PR
- Audience-aware — engineered for recruiters, hiring managers, and principal engineers simultaneously

See `OPERATING_REQUIREMENTS.md` and `QUALITY_STANDARDS.md` for the full baseline.
