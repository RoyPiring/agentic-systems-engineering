# Architecture scaffold

This folder is the **canonical place** for architecture evidence alongside root `architecture.md`:

| Subfolder | Purpose |
|-----------|---------|
| `diagrams/` | **Standard five** Mermaid sources (`.mmd`): context, **logical architectural topology**, **deployment topology**, roadmap phases, data flow. See `diagrams/README.md`. |
| `adr/` | Architecture Decision Records — one file per decision (`ADR-NNN-short-title.md`). |

Root `architecture.md` should keep the **overview** (intent, summary Mermaid, component table, tradeoffs, failure modes). **Detailed decisions** live in `adr/`; **full diagram sources** live in `diagrams/`.

## Standard diagram files

| File | Purpose |
|------|---------|
| `diagrams/01-system-context.mmd` | External actors and system boundary |
| `diagrams/02-architectural-topology.mmd` | **Logical** system design (capabilities, dependencies)—not hosting |
| `diagrams/03-deployment-topology.mmd` | **Technology** view: nodes, runtimes, environments |
| `diagrams/04-roadmap-phases.mmd` | Delivery phases (e.g. P01–P04) |
| `diagrams/05-data-flow.mmd` | Information / artifact flow between parts |

Portfolio-wide wording and TOGAF-style mapping: `02-BUILD/07-GitHub-Protifilo/00-template-systems-engineering/02-system-templates/scaffold-architecture-README.md`.

## Naming

- ADRs: `ADR-001-short-slug.md` — zero-padded index, kebab-case slug, `.md` only.

## Conventions

- Link from `architecture.md` using relative paths, e.g. `./architecture/adr/ADR-001-local-first-zero-cost-multimodal-pipeline.md`.
- When GitHub cannot render `.mmd` natively, paste the same graph in `architecture.md` inside a `mermaid` fence **or** link to a rendered export under `diagrams/exports/`.
