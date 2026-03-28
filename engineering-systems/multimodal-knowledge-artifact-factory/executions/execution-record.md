# Execution record

Rolling summary for **P01–P04**. Each project has a plan in [`implementation/`](./implementation/); **this file only summarizes what was executed**—not a full duplicate of the plan. Run transcripts stay in [`evidence/`](./evidence/).

## P01 — Markdown parse pipeline

| | |
|--|--|
| **Plan** | [`implementation/P01-implementation-plan.md`](./implementation/P01-implementation-plan.md) |
| **Window** | Mar 2026 |
| **Owner** | Roy |

### P01 — phase summary

| Phase | What shipped | Status | Evidence |
| ----- | ------------ | ------ | -------- |
| 1 | Toolchain recorded; `build/` is Cargo root | Done | [`evidence/rust-toolchain.txt`](./evidence/rust-toolchain.txt) |
| 2 | Crate `mkaf_md_parse`, `pulldown-cmark` 0.11.x, structured stdout | Done | [`build/`](../build/), [`evidence/p01-cargo-build.txt`](./evidence/p01-cargo-build.txt) |
| 3 | Happy path + missing-file run | Done | [`evidence/complex-sample-run.txt`](./evidence/complex-sample-run.txt), [`evidence/p01-negative-missing-file.txt`](./evidence/p01-negative-missing-file.txt) |
| 4 | Rollups + P01 validation | Done | [`../validation/P01-validation.md`](../validation/P01-validation.md), [`../validation.md`](../validation.md) |

### P01 — commands (from `build/`)

```bash
cargo build --release
cargo run --release -- samples/complex-sample.md
cargo run --release -- does-not-exist.md
```

### P01 — notes

- Default sample path is relative to cwd `build/`.
- Stdout format `H{n}:` / `P:` is the handoff contract toward audio/UI in later phases.
- `Cargo.lock` is committed under `build/` for reproducible dependency resolution.

---

## P02 — Local audio narrations (VibeVoice)

| | |
|--|--|
| **Plan** | [`implementation/P02-implementation-plan.md`](./implementation/P02-implementation-plan.md) |
| **Window** | Mar 2026 |
| **Owner** | Roy |

### P02 — phase summary

| Phase | Target | Status | Evidence |
| ----- | ------ | ------ | -------- |
| 1 | Python 3.x recorded; `tts_inference.py`; **stub** backend (no pip deps) | Done | [`evidence/p02-python-version.txt`](./evidence/p02-python-version.txt), [`../build/tts_inference.py`](../build/tts_inference.py), [`../build/requirements-p02.txt`](../build/requirements-p02.txt) |
| 2 | P01 → chunk → strip for TTS | Done | [`evidence/p01-stdout-for-p02.txt`](./evidence/p01-stdout-for-p02.txt), [`evidence/p02-pipeline-run.txt`](./evidence/p02-pipeline-run.txt) |
| 3 | `.wav` files with unique names; empty-input edge | Done | [`evidence/p02-audio/`](./evidence/p02-audio/), [`evidence/p02-audio-listing.txt`](./evidence/p02-audio-listing.txt), [`evidence/p02-edge-empty-stderr.txt`](./evidence/p02-edge-empty-stderr.txt) |
| 4 | P02 validation **PASS**, rollups | Done | [`../validation/P02-validation.md`](../validation/P02-validation.md), [`../implementation.md`](../implementation.md), [`../validation.md`](../validation.md) |

### P02 — commands (from `build/`)

```bash
cargo run --release -- samples/complex-sample.md > ../executions/evidence/p01-stdout-for-p02.txt
python tts_inference.py --from-file ../executions/evidence/p01-stdout-for-p02.txt

# Or pipe
cargo run --release -- samples/complex-sample.md | python tts_inference.py --stdin
```

### P02 — notes

- Default WAV output directory: `../executions/evidence/p02-audio/` (override with `--output-dir`).
- **VibeVoice-TTS-1.5B** public inference is not wired: upstream repo disabled/removed TTS quick try; **`--backend stub`** proves the pipeline. See [`../build/README.md`](../build/README.md).

---

## P03 — Interactive knowledge views (Dioxus)

| | |
|--|--|
| **Plan** | [`implementation/P03-implementation-plan.md`](./implementation/P03-implementation-plan.md) |
| **Window** | Mar 2026 |
| **Owner** | Roy |

### P03 — phase summary

| Phase | Target | Status | Evidence |
| ----- | ------ | ------ | -------- |
| 1 | Dioxus desktop shell; **Knowledge Viewer** window; crate layout supports CLI + UI | Done | [`evidence/p03-viewer-build.txt`](./evidence/p03-viewer-build.txt), [`../build/README.md`](../build/README.md) |
| 2 | Parsed markdown in UI state; section rendering | Done | `build/src/lib.rs`, `build/src/bin/knowledge_viewer.rs` |
| 3 | Per-section **Play Narration** (or equivalent) → P02 `.wav` paths | Done | `println!` path log; mapping note in [`evidence/p03-viewer-build.txt`](./evidence/p03-viewer-build.txt) |
| 4 | Evidence, [`../validation/P03-validation.md`](../validation/P03-validation.md) **PASS**, rollups | Done | [`evidence/p03-cargo-test-lib.txt`](./evidence/p03-cargo-test-lib.txt), [`evidence/p03-cargo-release-cli.txt`](./evidence/p03-cargo-release-cli.txt) |

### P03 — commands (from `build/`)

```bash
cargo test --lib
cargo build --release
cargo run --release -- samples/complex-sample.md
cargo build --release --features viewer --bin knowledge_viewer
cargo run --release --features viewer --bin knowledge_viewer
```

### P03 — notes

- Architectural intent: [ADR-003](../architecture/adr/ADR-003-dioxus-for-interactive-knowledge-views.md).
- Parser lives in `build/src/lib.rs`; P01 stdout shape locked by unit test against [`evidence/p01-stdout-for-p02.txt`](./evidence/p01-stdout-for-p02.txt).
- Dioxus **`Cargo.toml`:** keep default crate features on (`features = ["desktop"]` only); `default-features = false` without `macro`/`launch` broke compilation (see gap log).
- Desktop **LNK1104** on very long `target/` paths is environmental — short **`CARGO_TARGET_DIR`**, `cargo clean`, or AV exclusion; see [`evidence/p03-viewer-build.txt`](./evidence/p03-viewer-build.txt) and [`evidence/p03-viewer-release-build-success.txt`](./evidence/p03-viewer-release-build-success.txt).

---

## P04 — Multimodal assembly (AIRI)

| | |
|--|--|
| **Plan** | [`implementation/P04-implementation-plan.md`](./implementation/P04-implementation-plan.md) |
| **Window** | Mar 2026 |
| **Owner** | Roy |

### P04 — phase summary

| Phase | Target | Status | Evidence |
| ----- | ------ | ------ | -------- |
| 1 | `serde` / `serde_json`; **`export`** binary; `flashcards.json` + `quiz.md` | Done | [`evidence/p04-export-run.txt`](./evidence/p04-export-run.txt), [`evidence/p04-export-listing.txt`](./evidence/p04-export-listing.txt), [`evidence/p04-exports/`](./evidence/p04-exports/) |
| 2 | `build/integration.py`; path map; AIRI contract | Done | [`evidence/p04-integration-help.txt`](./evidence/p04-integration-help.txt), [`evidence/p04-integration-dry-run.txt`](./evidence/p04-integration-dry-run.txt), [`evidence/p04-integration-no-airi.txt`](./evidence/p04-integration-no-airi.txt) |
| 3 | P01 → P02 → export ordering | Done | [`evidence/p04-e2e-summary.txt`](./evidence/p04-e2e-summary.txt), [`evidence/p04-e2e-p02.txt`](./evidence/p04-e2e-p02.txt), [`evidence/p04-e2e-export.txt`](./evidence/p04-e2e-export.txt) |
| 4 | [`../validation/P04-validation.md`](../validation/P04-validation.md) **PASS (conditional)**, rollups | Done | This record + root rollups |

### P04 — commands (from `build/`)

```bash
cargo build --release --bin export
cargo run --release --bin export

python integration.py --help
python integration.py --dry-run
python integration.py   # exits 2 if AIRI not on PATH

# E2E slice (reuse or regenerate P01 stdout, then P02, then export)
cargo run --release -- samples/complex-sample.md > ../executions/evidence/p04-e2e-p01-stdout.txt
python tts_inference.py --from-file ../executions/evidence/p04-e2e-p01-stdout.txt --output-dir ../executions/evidence/p02-audio
cargo run --release --bin export
```

### P04 — notes

- **AIRI:** Full desktop launch not observed in this environment (`airi` absent on PATH). Integration script behavior and exit codes are evidenced in `p04-integration-*.txt`. Operators with AIRI set `AIRI_EXECUTABLE` or install on PATH, then run `python integration.py` (non–dry-run).
- Export uses `parse_markdown_blocks` / `blocks_to_sections` from `build/src/lib.rs` ([ADR-004](../architecture/adr/ADR-004-vibevoice-tts-and-airi-multimodal-assembly.md)).

---
