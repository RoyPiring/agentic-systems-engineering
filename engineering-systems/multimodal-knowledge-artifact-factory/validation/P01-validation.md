# P01 validation — Markdown parse pipeline

| | |
|--|--|
| **Plan** | [../executions/implementation/P01-implementation-plan.md](../executions/implementation/P01-implementation-plan.md) |
| **Result** | **PASS** (evidence under [../executions/evidence/](../executions/evidence/)) |

## Checks

| # | Criterion | Pass when |
|---|-----------|-----------|
| 1 | Crate layout | `build/Cargo.toml` and `build/src/main.rs` exist |
| 2 | Parser crate | `pulldown-cmark = "0.11"` in `Cargo.toml` |
| 3 | Build | `cargo build --release` succeeds from `build/` |
| 4 | Output shape | Complex sample shows `H*` and `P:` lines |
| 5 | Errors | Bad path → stderr + non-zero exit |
| 6 | Evidence | Toolchain + run transcripts in `executions/evidence/` |

## How to run

From `build/`:

```bash
cargo build --release
cargo run --release -- samples/complex-sample.md
cargo run --release -- does-not-exist.md
```

## Results

| Check | Expected | Actual |
| ----- | -------- | ------ |
| Build | OK | **PASS** — see [`p01-cargo-build.txt`](../executions/evidence/p01-cargo-build.txt) (`Finished release …`) |
| Sample | Structured H/P | **PASS** — see [`complex-sample-run.txt`](../executions/evidence/complex-sample-run.txt) (`H1:` … `P:` …) |
| Missing file | Exit ≠ 0 | **PASS** — exit code 1; stderr `read does-not-exist.md` in [`p01-negative-missing-file.txt`](../executions/evidence/p01-negative-missing-file.txt) |

## Delivery

| | |
|--|--|
| **PR** | (add link when you open the PR) |
| **Merge commit** | (short SHA on `main` after merge) |
