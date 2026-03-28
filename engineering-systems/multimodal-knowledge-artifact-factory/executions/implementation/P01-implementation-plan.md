# Implementation plan — P01: Markdown parse pipeline

| | |
|--|--|
| **System** | multimodal-knowledge-artifact-factory |
| **Last updated** | 2026-03 |

## Outcome

Ship a **Rust** CLI under `build/` that reads Markdown, parses with **pulldown-cmark 0.11**, and prints a simple structured stream: **headings** as `H{n}: …` and **paragraphs** as `P: …`. I/O failures go to **stderr** with a non-zero exit—no silent failures. A **complex** sample under `build/samples/` proves the shape of the data for later phases (e.g. TTS).

## Roadmap

| Phase | Focus |
| ----- | ----- |
| **1** | Toolchain + confirm `build/` is the Cargo root |
| **2** | Crate, dependency, parser in `main.rs` |
| **3** | Smoke: happy path + bad input path |
| **4** | Evidence on disk, validation, narrative docs |

## Phase 1 — Setup

| Step | Complete when |
| ---- | ------------- |
| Rust available | Versions saved to [`../evidence/p01/rust-toolchain.txt`](../evidence/p01/rust-toolchain.txt) |
| Layout | All Cargo work happens from [`build/`](../../build/) |

## Phase 2 — Build

| Step | Complete when |
| ---- | ------------- |
| Crate | `cargo build` succeeds from `build/` |
| Dependency | `pulldown-cmark = "0.11"` in [`Cargo.toml`](../../build/Cargo.toml) |
| Parser | [`main.rs`](../../build/src/main.rs) reads `.md` (arg or default `samples/complex-sample.md`) and emits `H*` / `P:` lines |
| Sample | Run against [`complex-sample.md`](../../build/samples/complex-sample.md) produces clean structure |

## Phase 3 — Smoke

| Check | Complete when |
| ----- | ------------- |
| Regression | Same sample run as Phase 2; output stable |
| Failure | Missing file → stderr + exit `1` |

## Phase 4 — Wrap-up

| Item | Complete when |
| ---- | ------------- |
| Summary | [Execution record](../execution-record.md) updated for P01 |
| Evidence | Run logs / transcripts in [`../evidence/p01/`](../evidence/p01/) |
| Validation | [P01 validation](../../validation/P01-validation.md) shows **PASS** |

## Done when

- [x] `cargo build` / `cargo run` verified with transcripts under [`../evidence/p01/`](../evidence/p01/) (`p01-cargo-build.txt`, `complex-sample-run.txt`, `p01-negative-missing-file.txt`).
- [x] Validation **PASS** and system docs aligned.

## Next

**P02** consumes this structured text (e.g. TTS). Keep the same short plan + execution-summary pattern.
