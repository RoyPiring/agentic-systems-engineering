# Build

Application code, scripts, configs, and infrastructure-as-code produced while executing the series (P01–P04).

Aligned with the series **Repository Packaging (RP)** manifest: runnable artifacts live here—not in the narrative docs at the engineering-system root.

## P01 — Markdown parse (`mkaf_md_parse`)

**Prerequisites:** Rust stable (`cargo`, `rustc`).

From this directory:

```bash
cargo build --release
cargo run --release
cargo run --release -- samples/complex-sample.md
```

- Default input path (no args): `samples/complex-sample.md` (relative to current working directory).
- Missing or unreadable files: message on stderr and exit code `1`.

## Rules

- Prefer real, runnable content over empty placeholders.
- Do not commit secrets; use environment variables or secret stores documented in `architecture.md` / `validation.md`.
- Keep paths and run instructions discoverable from `implementation.md` and the relevant `executions/P0X-*` records.
