## Engineering System: multimodal-knowledge-artifact-factory

### What This PR Adds

**Full-series finish** on branch `feature/multimodal-knowledge-artifact-factory-p03`: **P04** (study exports + `integration.py` AIRI bridge), complete **`user-guides/`** (P01–P04 + **`SERIES-user-guide.md`**), evidence under **`executions/evidence/p01/`…`p04/`** (per-project folders), and **`case-study/`** (requirements, sample data, runbook, optional Edge TTS narration). Domain discovery files (**`README.md`**, **`FEATURE_SYSTEMS.md`**, **`engineering-systems/README.md`**) updated so featured rows match **`implementation.md`** / **`validation.md`**.

**Note:** P01–P03 may already be on `main` from prior merges; this PR carries the remaining delta through **P04**, guides, evidence layout, and case study in one reviewable slice (or supersedes an open P03-only PR—rebase if needed).

### Source

- Source specification: Multimodal Knowledge Artifact Factory
- **Projects in this PR:** **P01–P04** narrative closure + operator docs + case study (not an incremental P0X-only slice)

### Review Gate Checklist

- [x] All five required files present: README, business-context, architecture, implementation, validation
- [x] README supports 90-second orientation; links **`user-guides/`** and **`case-study/`**
- [x] Tradeoffs and failure modes visible (stub TTS, AIRI conditional, Windows path caveats)
- [x] Validation rollup + per-project **`validation/P0X-validation.md`** honest for shipped phases
- [x] No private-workspace paths in reader-facing portfolio text
- [x] **`executions/execution-record.md`** and **`executions/implementation/`** aligned with evidence paths
- [x] Evidence uses **`p01/`…`p04/`** layout (not flat-only legacy paths)
- [x] Changelog: `.github/changelog/2026-03-28-multimodal-knowledge-artifact-factory-full-series.md`
- [x] Mermaid in **`architecture.md`** renders in GitHub preview
- [x] `.github/workflows/` — Documentation Quality workflow expected green
- [x] `.github/ISSUE_TEMPLATE/` — bug / feature templates present

### Evidence Summary

- **`executions/evidence/p01/`** … **`p04/`** — transcripts, **`p02/audio/`** stub WAVs, **`p04/exports/`** as documented
- **`executions/implementation/P01-implementation-plan.md`** … **`P04-implementation-plan.md`**
- **`build/`** — Rust CLI, viewer (`--features viewer`), **`export`**, **`tts_inference.py`**, **`integration.py`**
- **`case-study/`** — README, REQUIREMENTS, RUNBOOK, **`data/`**, optional **`tools/generate_edge_narration.py`**

### Gaps / Follow-ups

- **AIRI** desktop launch remains **operator-dependent**; P04 validation states conditional PASS where AIRI is not exercised.
- Windows **LNK1104** / long paths — see **`build/README.md`** and evidence notes (`CARGO_TARGET_DIR`, short clone path).

### Verify

From **`engineering-systems/multimodal-knowledge-artifact-factory/build/`**:

```bash
cargo fmt --all --check
cargo clippy --all-targets --all-features -- -D warnings
cargo test --all
cargo build --release
cargo run --release -- samples/complex-sample.md
```

Viewer:

```bash
cargo build --release --features viewer --bin knowledge_viewer
cargo run --release --features viewer --bin knowledge_viewer
```

End-to-end order: **`user-guides/SERIES-user-guide.md`** and **`case-study/RUNBOOK.md`**.
