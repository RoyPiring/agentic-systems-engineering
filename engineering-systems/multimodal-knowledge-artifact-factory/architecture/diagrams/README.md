# Diagrams

- **`.mmd` files** — Mermaid source (text). Easy to review in diffs; render with [mermaid.live](https://mermaid.live) or your editor.
- **Exports** — Optional `.svg` / `.png` under `exports/` when viewers cannot run Mermaid.

## Standard five (portfolio)

**Logical architecture** (`02`) and **deployment / technology** (`03`) are different views—same idea as separating application vs technology layers in TOGAF-style playbooks. Full spec and TOGAF mapping table:

`02-BUILD/07-GitHub-Protifilo/00-template-systems-engineering/02-system-templates/scaffold-architecture-README.md` → **Standard diagram set (five views)**.

| File | View |
|------|------|
| `01-system-context.mmd` | System vs operator and external apps (scope boundary) |
| `02-architectural-topology.mmd` | Logical building blocks: ingestion → parse → narrate → present → export → AIRI |
| `03-deployment-topology.mmd` | Where things run: local host, Rust/Python processes, filesystem, AIRI desktop |
| `04-roadmap-phases.mmd` | P01–P04 delivery sequence |
| `05-data-flow.mmd` | Artifact movement from markdown through pipeline into AIRI |
