# Architecture scaffold

This folder is the **canonical place** for architecture evidence alongside root `architecture.md`:

| Subfolder | Purpose |
|-----------|---------|
| `diagrams/` | Mermaid source (`.mmd`), exported SVG/PNG, and diagram notes. Prefer versioned sources you can diff in PRs. |
| `adr/` | Architecture Decision Records — one file per decision (`ADR-NNN-short-title.md`). |

Root `architecture.md` should keep the **overview** (intent, summary Mermaid, component table, tradeoffs, failure modes). **Detailed decisions** live in `adr/`; **full diagram sources** live in `diagrams/`.

## Naming

- Diagrams: use the **standard five** below (`01`–`05`, kebab-case slug, `.mmd`). Add `06-*.mmd` only for edge cases (e.g. a second region or DR site).
- ADRs: `ADR-001-local-first-pipeline.md` — zero-padded index, kebab-case slug, `.md` only.

## Conventions

- Link from `architecture.md` using relative paths, e.g. `./architecture/adr/ADR-001-your-decision.md`.
- When GitHub cannot render `.mmd` natively, paste the same graph in `architecture.md` inside a `mermaid` fence **or** link to a rendered export under `diagrams/`.

## Standard diagram set (five views)

Use these five Mermaid sources in every engineering system’s `architecture/diagrams/` folder.

**Architectural topology** and **deployment (technology) topology** are intentionally separate: the first describes *logical building blocks and dependencies* (solution shape); the second describes *where those capabilities run* (hosts, clusters, regions, desktop vs cloud). That split matches common enterprise practice and frameworks such as **TOGAF** (separate concerns across architecture domains / viewpoints), without requiring full TOGAF adoption.

| File | View | What it must answer |
| ---- | ---- | ------------------- |
| `01-system-context.mmd` | **System context** | Who/what is outside the system? In scope vs external actors (users, SaaS, APIs). |
| `02-architectural-topology.mmd` | **Architectural (logical) topology** | What are the major **logical** capabilities, layers, or applications and how do they depend on each other? No requirement to name servers here. |
| `03-deployment-topology.mmd` | **Deployment / technology topology** | Where do those capabilities **execute** (environments, nodes, runtimes, containers)? Refine per phase if topology changes during delivery. |
| `04-roadmap-phases.mmd` | **Roadmap / delivery phases** | How is work sequenced (P01–P*n*, milestones, releases)? |
| `05-data-flow.mmd` | **Data / information flow** | What artifacts or records move between parts? Optional: trust boundaries on the same diagram. |

### TOGAF-style playbook mapping (informative)

| This repo’s diagram | Rough TOGAF / SA framing (not a certification checklist) |
| ------------------- | -------------------------------------------------------- |
| System context | Motivation + stakeholder / ecosystem view; boundary of the solution. |
| Architectural topology | **Application** architecture (logical structure of software building blocks) plus relevant **Business** touchpoints when you show capabilities. |
| Deployment topology | **Technology** architecture (platforms, nodes, hosting, networks). |
| Roadmap phases | **Migration / implementation** trajectory (ADM-style sequencing at a high level). |
| Data flow | **Data** architecture and information exchange (often paired with security boundaries). |

**Optional:** `diagrams/exports/` for committed SVG/PNG when viewers cannot render Mermaid. **Root `architecture.md`** should link all five sources and may embed a summary Mermaid block for GitHub preview.

**Tooling:** `.mmd` stays the source of truth; keep labels consistent with `implementation.md` and ADRs.
