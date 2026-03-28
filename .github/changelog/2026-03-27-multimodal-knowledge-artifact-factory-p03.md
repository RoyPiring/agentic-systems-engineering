## Multimodal Knowledge Artifact Factory — Added (P03)

**Date:** 2026-03-27
**Type:** Engineering System — Update
**PR:** _(fill number after open — use `.github/pull-requests/PR_BODY_MULTIMODAL_P03_FILLED.md` with `gh pr create --body-file …`)_

### Summary

Shipped **P03** interactive **Knowledge Viewer** as a second Rust binary (`knowledge_viewer`) using **Dioxus 0.7.3** desktop, behind Cargo feature `viewer`. Parser logic moved to `build/src/lib.rs` so the P01 CLI and UI share one parse model; a unit test locks stdout against `executions/evidence/p01-stdout-for-p02.txt` for P02 compatibility. Per-section **Play Narration** logs mapped paths into `executions/evidence/p02-audio/`.

### Projects

- P01: Markdown parse CLI (unchanged output contract)
- P02: Stub TTS bridge (unchanged)
- P03: Dioxus desktop knowledge viewer + narration path mapping
- P04: _(not in this change)_

### Evidence

- `engineering-systems/multimodal-knowledge-artifact-factory/executions/evidence/p03-*.txt`
- `validation/P03-validation.md` — **PASS**
- `build/README.md` — run instructions
