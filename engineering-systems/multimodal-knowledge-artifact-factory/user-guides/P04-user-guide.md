# User guide — P04: Study exports + AIRI bridge

## What you get

1. **`export`** (Rust) — builds **flashcards** and a **quiz** file from the markdown (default output folder: `executions/evidence/p04/exports/`).
2. **`integration.py`** (Python) — prints **full paths** for audio, exports, and the viewer; can start **AIRI** if you installed it.

## Getting ready (before you run)

1. **Same folders as P01** — system root on disk, then `cd build` so `Cargo.toml` is in your current folder.
2. **Rust + Python 3.10+** — same checks as [P01](./P01-user-guide.md) and [P02](./P02-user-guide.md).
3. **AIRI is optional** — you can run **`export`** and **`python integration.py --dry-run`** without AIRI. For a real AIRI launch, install AIRI and put it on your **PATH**, or set the **`AIRI_EXECUTABLE`** environment variable to the AIRI program path.

## Prerequisites (short list)

- **Rust** and **Python 3.10+** (same as earlier phases).
- **AIRI** — optional; only needed for an actual launch, not for `--dry-run` or `--print-env`.

## How to run — exports

From **`build/`**:

```bash
cargo build --release --bin export
cargo run --release --bin export
```

Optional: `cargo run --release --bin export -- path/to/file.md ../executions/evidence/p04/exports`

## How to run — integration

From **`build/`**:

```bash
python integration.py --help
python integration.py --dry-run
```

- **`--print-env`** — prints `MKAF_*` style variables you can export for another tool.
- **Launch AIRI** (when installed): `python integration.py` — passes `MKAF_ROOT`, `MKAF_P02_AUDIO`, `MKAF_P04_EXPORTS`, etc.

If AIRI is missing, the script exits **2** with a clear message (expected until you install it).

## Viewer binary note

The script looks for **`build/target/release/knowledge_viewer(.exe)`**. If you only build with a custom **`CARGO_TARGET_DIR`**, `MKAF_VIEWER_BINARY` may be empty until you build once at the default path or set paths manually.

## Next step

[Series — end-to-end](./SERIES-user-guide.md) for the full order.
