## Engineering System: multimodal-knowledge-artifact-factory

### What This PR Adds

**P01** of the Multimodal Knowledge Artifact Factory: a Rust CLI under `engineering-systems/multimodal-knowledge-artifact-factory/build/` that parses Markdown with `pulldown-cmark`, emits structured `H{n}:` / `P:` lines, and documents proof under `executions/` and `validation/`.

### Source

- Source specification: Multimodal Knowledge Artifact Factory
- **Projects in this PR:** P01 only (P02–P04 not in this PR)

### Review Gate Checklist

- [x] All 5 required files present: README, business-context, architecture, implementation, validation
- [x] README supports 90-second orientation
- [x] Tradeoffs and failure modes are visible (where applicable for P01)
- [x] Validation includes expected **and** actual/observed results for **each project in this PR**
- [x] No private-workspace paths or internal governance references in reader-facing text
- [x] Execution record updated in `executions/execution-record.md` for **each completed project**
- [x] Per-project plans in `executions/implementation/` (`P0X-implementation-plan.md`); run transcripts in `executions/evidence/`
- [x] Changelog: [CHANGELOG.md](../../changelog/2026-03-26-multimodal-knowledge-artifact-factory/CHANGELOG.md) (P01 section — shared file for **2026-03-26**)
- [x] Mermaid diagram(s) in `architecture.md` render in GitHub preview

### Evidence Summary

- `executions/implementation/P01-implementation-plan.md`
- `executions/evidence/`: toolchain, `cargo build`, sample run, negative path
- `validation/P01-validation.md` — **PASS**; `validation.md` rollup updated

### Gaps Identified

None blocking merge; P02+ tracked as future work on `main` after merge.
