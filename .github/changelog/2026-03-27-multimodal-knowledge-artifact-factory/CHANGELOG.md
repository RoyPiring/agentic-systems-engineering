# Changelog — multimodal-knowledge-artifact-factory — 2026-03-27

## P03 — Knowledge Viewer (Dioxus)

**PR:** #4  
**Type:** Engineering System — Update

### Summary

Shipped **P03** interactive **Knowledge Viewer** as a second Rust binary (`knowledge_viewer`) using **Dioxus 0.7.3** desktop, behind Cargo feature `viewer`. Parser logic moved to `build/src/lib.rs` so the P01 CLI and UI share one parse model; a unit test locks stdout against `executions/evidence/p01-stdout-for-p02.txt` for P02 compatibility. Per-section **Play Narration** logs mapped paths into `executions/evidence/p02-audio/`.

### Projects (this PR)

- P01: Markdown parse CLI (unchanged output contract)
- P02: Stub TTS bridge (unchanged)
- P03: Dioxus desktop knowledge viewer + narration path mapping
- P04: _(not in this change)_

### Evidence

- `engineering-systems/multimodal-knowledge-artifact-factory/executions/evidence/p03-*.txt`
- `validation/P03-validation.md` — **PASS**
- `build/README.md` — run instructions
