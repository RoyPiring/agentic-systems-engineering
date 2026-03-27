# Implementation

How this system is phased from a working **parse path** through media and UI. Per-project plans live in [`executions/implementation/`](./executions/implementation/) (`P0X-implementation-plan.md`); run evidence lives in [`executions/evidence/`](./executions/evidence/). This page is the rolling **system** view.

## Strategy

Work moves **P01 → P04**: Markdown → structured text → audio/UI → assembly. Each phase stays testable on its own.

## Phases

### P01 — Foundation

| | |
|--|--|
| **Plan** | [executions/implementation/P01-implementation-plan.md](./executions/implementation/P01-implementation-plan.md) |
| **Goal** | Rust binary under `build/` turns `.md` into structured lines (`H{n}:`, `P:`) for downstream use |
| **Inputs** | CLI path or default `samples/complex-sample.md` (cwd = `build/`) |
| **Output** | Structured stdout; stderr + exit `1` on read errors |

**Artifacts:** `build/Cargo.toml`, `build/src/main.rs`, `build/samples/complex-sample.md`, [`build/README.md`](./build/README.md).

### P02 — Core build

VibeVoice / TTS from structured text. **Not started** here; depends on P01 (now **PASS** — see [`validation/P01-validation.md`](./validation/P01-validation.md)).

### P03 — Hardening

UI (e.g. Dioxus), edge cases, performance—later.

### P04 — Validation

End-to-end proof; evidence under [`executions/evidence/`](./executions/evidence/); roll-up in [`validation.md`](./validation.md).

## How to run (P01)

1. Install Rust.  
2. `cd build`  
3. `cargo build --release`  
4. `cargo run --release -- samples/complex-sample.md`  

## Decisions

| Topic | Choice |
| ----- | ------ |
| Crate location | `build/`, not repo root |
| Parser | `pulldown-cmark` **0.11** (ADR-002) |
| Default sample | `samples/complex-sample.md` |

## Reproduce

Use stable Rust; run commands from `build/`. Evidence and status: [`executions/execution-record.md`](./executions/execution-record.md) and [`validation/P01-validation.md`](./validation/P01-validation.md).
