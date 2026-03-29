> ← [Multimodal Knowledge Artifact Factory](../README.md) · [All Systems](../../../engineering-systems/README.md) · [Home](../../../README.md)

# User guides — Multimodal Knowledge Artifact Factory

These guides are for people who want to **use** this system on their own machine. You do **not** need to read implementation plans or validation proofs first.

---

## Start here — get to the point where you can run something

**1. Get the code**  
Clone or download the **agentic-systems-engineering** portfolio repository. On your machine, open the folder:

`engineering-systems/multimodal-knowledge-artifact-factory/`

That folder is the **system root**. It should contain `build/`, `executions/`, `validation/`, and this `user-guides/` folder.

### 2. Install what the commands need

| You need | Why | Check |
| -------- | --- | ----- |
| **Rust** (includes `cargo` and `rustc`) | P01, P03, and P04 use Rust programs | Open a terminal and run `cargo --version`. If that fails, install from [rustup](https://rustup.rs/). |
| **Python 3.10 or newer** | P02 and P04 use small Python scripts | Run `python --version` (or `py -3 --version` on Windows). |
| **WebView2** (Windows only, for the desktop viewer) | P03 opens a window using the system web view | Usually already present with Microsoft Edge. |

**3. Open the right folder in the terminal**  
Almost every command in these guides expects your terminal’s **current folder** to be **`build/`** — the one that contains `Cargo.toml`. From the system root:

- **Windows (PowerShell):** `cd build`
- **macOS / Linux:** `cd build`

### 4. Pick your path

- **First time, want the smallest win:** open [P01 — Parse markdown](./P01-user-guide.md), do the “Getting ready” box, then run the two `cargo` commands.
- **Want the whole pipeline in order:** open [Series — end-to-end](./SERIES-user-guide.md) and follow it top to bottom.
- **Case study + real voice for `script.md`:** [Case study RUNBOOK](../case-study/RUNBOOK.md) for P01→P04 (+ optional viewer with **`script.md`** path, **`artifacts/`** export copies). P02 stub = beeps only. For **spoken MP3** of that script, see [P02 — Real spoken audio](./P02-user-guide.md) and [`../case-study/data/audio/README.md`](../case-study/data/audio/README.md).

**5. If paths in another doc don’t match**  
Some mirrors or older copies of this project use folder names like `execution/` (singular) or `initiatives/...`. **This repository** uses **`executions/`** (plural) under **`engineering-systems/<slug>/`**. **`integration.py`** env vars → [`../build/README.md`](../build/README.md) § P04.

---

## Guide index

| Guide | What it covers |
| ----- | ---------------- |
| [P01 — Parse markdown to structured text](./P01-user-guide.md) | Rust CLI: `build/` → structured text on screen |
| [P02 — Audio chunks from structured text](./P02-user-guide.md) | Python: **stub** → `.wav` (beeps); optional **Edge TTS MP3** for case-study script |
| [P03 — Desktop Knowledge Viewer](./P03-user-guide.md) | Desktop app: sections + narration |
| [P04 — Study exports + AIRI handoff](./P04-user-guide.md) | Export files + optional AIRI launcher |
| [Series — end-to-end](./SERIES-user-guide.md) | Full pipeline in order, one after the other |

**Convention:** Unless a guide says otherwise, run commands from **`build/`**. The **system root** is the parent of `build/` (where `executions/` and `validation/` live).

More for builders and reviewers: [`../README.md`](../README.md), [`../build/README.md`](../build/README.md), [`../implementation.md`](../implementation.md).
