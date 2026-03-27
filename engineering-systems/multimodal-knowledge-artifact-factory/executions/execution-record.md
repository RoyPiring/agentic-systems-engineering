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

## P02 — (not started)

_Add a matching summary row when P02 begins._
