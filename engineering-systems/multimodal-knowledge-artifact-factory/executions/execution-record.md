# Execution record

Rolling summary for **P01–P04**. Each project has a plan in [`implementation/`](./implementation/); **this file only summarizes what was executed**—not a full duplicate of the plan. Run transcripts stay in [`evidence/`](./evidence/).

## P01 — Markdown parse pipeline

| | |
|--|--|
| **Plan** | [`implementation/P01-implementation-plan.md`](./implementation/P01-implementation-plan.md) |
| **Window** | Mar 2026 |
| **Owner** | Roy |

### Summary

| Phase | What shipped | Status | Evidence |
| ----- | ------------ | ------ | -------- |
| 1 | Toolchain recorded; `build/` is Cargo root | Done | [`evidence/rust-toolchain.txt`](./evidence/rust-toolchain.txt) |
| 2 | Crate `mkaf_md_parse`, `pulldown-cmark` 0.11.x, structured stdout | Done | [`build/`](../build/), [`evidence/p01-cargo-build.txt`](./evidence/p01-cargo-build.txt) |
| 3 | Happy path + missing-file run | Done | [`evidence/complex-sample-run.txt`](./evidence/complex-sample-run.txt), [`evidence/p01-negative-missing-file.txt`](./evidence/p01-negative-missing-file.txt) |
| 4 | Rollups + P01 validation | Done | [`../validation/P01-validation.md`](../validation/P01-validation.md), [`../validation.md`](../validation.md) |

### Commands (from `build/`)

```bash
cargo build --release
cargo run --release -- samples/complex-sample.md
cargo run --release -- does-not-exist.md
```

### Notes

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

### Summary

| Phase | Target | Status | Evidence |
| ----- | ------ | ------ | -------- |
| 1 | Python venv, `tts_inference.py` scaffold, model load | Not started | _(add `p02-*.txt` under [`evidence/`](./evidence/) when run)_ |
| 2 | P01 → chunk → strip for TTS | Not started | — |
| 3 | `.wav` files with unique names | Not started | — |
| 4 | P02 validation **PASS**, rollups | Not started | [`../validation/P02-validation.md`](../validation/P02-validation.md) |

### Commands (preview)

_From `build/` after implementation:_

```bash
# Example: pipe P01 stdout into Python (exact invocation TBD in plan execution)
cargo run --release -- samples/complex-sample.md | python tts_inference.py
```

_Phase table and real commands replace this section when P02 executes._

---
