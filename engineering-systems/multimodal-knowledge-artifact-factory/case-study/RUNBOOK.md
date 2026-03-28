# Runbook — Multimodal Knowledge Artifact Factory case study

Follow [`../user-guides/README.md`](../user-guides/README.md) (“Start here”) first: Rust, Python 3.10+, then open a terminal at **`build/`** (the folder that contains `Cargo.toml`).

Phase order matches [`../user-guides/SERIES-user-guide.md`](../user-guides/SERIES-user-guide.md). Commands assume **current working directory = `build/`**.

Input file for **P01 / P02 / P04**: **`../case-study/data/script.md`**. It must include **at least one `#` heading** before body text so **P04 export** can build sections (orphan paragraphs before the first heading produce **zero** flashcards in this crate).

---

## 1 — P01 → P02 (parse + stub audio)

See [`../user-guides/P01-user-guide.md`](../user-guides/P01-user-guide.md) and [`../user-guides/P02-user-guide.md`](../user-guides/P02-user-guide.md).

```bash
cargo build --release
cargo run --release -- ../case-study/data/script.md | python tts_inference.py --stdin
```

**Expected:** Terminal shows structured lines from P01; P02 lists chunk paths; `../executions/evidence/p02/audio/` contains new `p02-chunk-*.wav` files.

**What you will hear (important):** The default **`stub`** backend in `tts_inference.py` does **not** read your script aloud. It writes a **short sine tone** per chunk (a beep); text length only changes **duration** and **pitch** slightly. That is intentional so the repo runs everywhere without neural TTS. **`p02-chunk-0000.wav`** is often **very short** because it is usually the **heading line** only (e.g. the `#` title), not the full narration. The **whole** of `script.md` is still covered across **all** numbered chunks—each file is a placeholder, not speech. For real voice, you need a different backend or service (see [`../build/README.md`](../build/README.md); `vibevoice` is not wired in this tree).

**Real narration for `script.md` (optional):** Spoken MP3s live under [`data/audio/`](./data/audio/). From **`build/`** (after `pip install edge-tts`):

```bash
python ../case-study/tools/generate_edge_narration.py --one-file
```

That writes **`../case-study/data/audio/script-narration-full.mp3`** (single file for typical script length). Alternatives: default run → numbered parts + `script-narration.m3u`; with **ffmpeg** on PATH, `python ../case-study/tools/generate_edge_narration.py --merge-only` merges existing `part*.mp3` into **`script-narration-merged.mp3`**. Details: [`data/audio/README.md`](./data/audio/README.md).

---

## 2 — P04 export (flashcards + quiz)

See [`../user-guides/P04-user-guide.md`](../user-guides/P04-user-guide.md) (export section).

Write to the **default** export folder so [`../build/integration.py`](../build/integration.py) resolves `executions/evidence/p04/exports` in later steps:

```bash
cargo build --release --bin export
cargo run --release --bin export -- ../case-study/data/script.md ../executions/evidence/p04/exports
```

**Expected:** `../executions/evidence/p04/exports/flashcards.json` and `quiz.md` exist and are non-empty.

---

## 3 — P04 integration (path map)

See [`../user-guides/P04-user-guide.md`](../user-guides/P04-user-guide.md) (integration section).

**Always safe (AIRI optional):**

```bash
python integration.py --dry-run
```

**Expected:** Exit code **0**. Prints resolved roots for **`MKAF_*`** paths.

**Full AIRI launch** (requires **`airi`** on **`PATH`** or **`AIRI_EXECUTABLE`** set to the binary):

```bash
python integration.py
```

**Expected:** If AIRI is missing → exit **2**, clear stderr (still **PASS (conditional)** in validation). If AIRI is present → process starts; behavior is operator-dependent.

---

## 4 — P03 — Knowledge Viewer with **`script.md`**

After **§1**, **`p02/audio/`** contains stub WAVs aligned to **`script.md`**. The viewer accepts an **optional** markdown path (relative to **`build/`** or absolute). **Do not** run **§1** for `complex-sample.md` in between if you want section indices to match **`script.md`** chunks.

```bash
cargo build --release --features viewer --bin knowledge_viewer
cargo run --release --features viewer --bin knowledge_viewer -- ../case-study/data/script.md
```

**Expected:** Window title includes **`script.md`**; sections match the script; **Play Narration** logs paths under `../executions/evidence/p02/audio/` (see [`../user-guides/P03-user-guide.md`](../user-guides/P03-user-guide.md)).

**Default sample (tutorial only):** To use **`samples/complex-sample.md`** instead, omit the trailing path and regenerate WAVs from that sample first (see **SERIES** guide).

---

## 5 — Optional: copy exports into **`case-study/artifacts/`**

For PRs that should show **flashcards** / **quiz** next to the case study without digging into **`executions/evidence/`**, copy after **§2**:

See **[artifacts/README.md](./artifacts/README.md)** for exact **`Copy-Item`** commands (PowerShell).

---

## Verification

| ID | How you know |
| -- | ------------- |
| R1 | `cargo run --release -- ../case-study/data/script.md` prints `H`/`P` lines, exit **0** |
| R2 | `../executions/evidence/p02/audio/p02-chunk-0000.wav` (or similar) exists after §1 |
| R3 | `../executions/evidence/p04/exports/flashcards.json` and `quiz.md` updated after §2 |
| R4 | `python integration.py --dry-run` → exit **0** |
| R5 | Optional: §4 window opens with **`script.md`** argument |
| R6 | Optional: **`case-study/artifacts/`** copies match **`p04/exports/`** after sync |

**Last verified:** 2026-03-27 — runbook + evidence layout **`p01/`**…**`p04/`**; viewer optional markdown path.
