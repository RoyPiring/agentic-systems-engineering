## Engineering System: multimodal-knowledge-artifact-factory

### What This PR Adds

**P03** for Multimodal Knowledge Artifact Factory: Dioxus **0.7.3** desktop **Knowledge Viewer** (`knowledge_viewer` binary, Cargo feature `viewer`). Shared parser in `build/src/lib.rs`; P01 CLI output contract locked by unit test vs `executions/evidence/p01-stdout-for-p02.txt`. Per-section **Play Narration** maps to P02 stub WAVs under `executions/evidence/p02-audio/`. Portfolio `Cargo.toml` keeps Dioxus **default** crate features with `features = ["desktop"]`; Windows **LNK1104** mitigations documented in `build/README.md` and `executions/evidence/p03-viewer-build.txt`.

### Source

- Source specification: Multimodal Knowledge Artifact Factory
- **Projects in this PR:** P03 only (P01–P02 already on `main`)

### Review Gate Checklist

- [x] All 5 required files present: README, business-context, architecture, implementation, validation
- [x] README supports 90-second orientation
- [x] Tradeoffs and failure modes are visible (where applicable)
- [x] Validation includes expected **and** actual/observed results for **each project in this PR**
- [x] No private-workspace paths or internal governance references in reader-facing text
- [x] Execution record updated in `executions/execution-record.md` for **each completed project**
- [x] Per-project plans in `executions/implementation/`; run transcripts in `executions/evidence/`
- [x] Changelog: [CHANGELOG.md](../../changelog/2026-03-27-multimodal-knowledge-artifact-factory/CHANGELOG.md)
- [x] Mermaid diagram(s) in `architecture.md` render in GitHub preview
- [x] `.github/workflows/` — documentation workflow expected green on this branch (Step 73)
- [x] `.github/ISSUE_TEMPLATE/` — present for bug / feature triage

### Evidence Summary

- `executions/implementation/P03-implementation-plan.md`
- `build/src/lib.rs`, `build/src/main.rs`, `build/src/bin/knowledge_viewer.rs`, `build/Cargo.toml`, `build/README.md`
- `executions/evidence/p03-*.txt` (tests, CLI, viewer build notes, release success transcript)
- `validation/P03-validation.md` — **PASS**; `validation.md` rollup

### Gaps Identified

- Windows **LNK1104** on very long `target/` paths — use short `CARGO_TARGET_DIR`, `cargo clean`, AV exclusion, or shorter clone path (see evidence files).
- Optional UI screenshot under `executions/evidence/` — follow-up after local viewer run.

### Verify

From `engineering-systems/multimodal-knowledge-artifact-factory/build/`:

```bash
cargo test
cargo build --release
cargo run --release -- samples/complex-sample.md
```

Viewer (if default `target/` fails on Windows, set `CARGO_TARGET_DIR` to a short path first):

```bash
cargo build --release --features viewer --bin knowledge_viewer
cargo run --release --features viewer --bin knowledge_viewer
```

Commands and caveats: `validation/P03-validation.md`, `build/README.md`.
