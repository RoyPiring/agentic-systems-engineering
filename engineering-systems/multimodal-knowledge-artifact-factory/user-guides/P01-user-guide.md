# User guide — P01: Markdown parse (CLI)

## What you get

A small **Rust** program reads a local `.md` file and prints **structured lines** to your screen (`H{n}:` for headings, `P:` for paragraphs). Later steps (P02–P04) use that same shape.

## Getting ready (before you run)

1. **You are in the right repo folder** — the **system root** contains `build/`, `user-guides/`, and `executions/`. If you only just cloned, open:  
   `engineering-systems/multimodal-knowledge-artifact-factory/`
2. **Rust is installed** — in any terminal, `cargo --version` should print a version. If not, install from [rustup](https://rustup.rs/) and open a **new** terminal.
3. **Go into `build/`** — this folder holds `Cargo.toml`. Example: `cd build` (from the system root).

## Prerequisites (short list)

- **Rust** stable: `cargo` and `rustc` on your **PATH**.

## How to run

1. Stay in **`build/`** (the folder that contains `Cargo.toml`).
2. Build and run:

```bash
cargo build --release
cargo run --release -- samples/complex-sample.md
```

- **Default** if you omit the path: `samples/complex-sample.md` (relative to `build/`).
- **Custom file:** `cargo run --release -- path/to/your.md`

## Success vs failure

- **Success:** Structured lines print to the terminal; exit code **0**.
- **Failure:** Missing/unreadable file → message on **stderr**, exit code **1**.

## Outputs

- **Stdout only** — redirect if you need a file for P02:

```bash
cargo run --release -- samples/complex-sample.md > ../executions/evidence/my-p01-out.txt
```

## Next step

Use that stdout with [P02 — Audio chunks](./P02-user-guide.md) (pipe or `--from-file`).
