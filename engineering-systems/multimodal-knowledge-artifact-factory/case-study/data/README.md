# Case study data

| Path | Role |
| ---- | ---- |
| `script.md` | Narration script: starts with one `#` title so **P04** can build sections; body is plain paragraphs. Used for **P01**, **P02**, **P04** in [RUNBOOK.md](../RUNBOOK.md) |
| `audio/` | Optional **spoken** MP3 of `script.md` (Edge TTS). See [audio/README.md](./audio/README.md). Not used by P03’s **Play Narration** (that uses **`executions/evidence/p02/audio/`** stub WAVs). |
| `../tools/generate_edge_narration.py` | Regenerate `audio/` files (`--one-file`, `--merge`, `--merge-only`). |

**Note:** The **Knowledge Viewer** (P03) defaults to `build/samples/complex-sample.md`. For this case study, pass **`../case-study/data/script.md`** as the first CLI argument to **`knowledge_viewer`** after running P01→P02 on **`script.md`** so sections and stub WAV indices align (see [RUNBOOK.md](../RUNBOOK.md) §4).
