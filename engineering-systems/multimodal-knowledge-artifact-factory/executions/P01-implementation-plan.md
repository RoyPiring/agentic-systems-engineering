# Implementation Plan — P01: Scaffold the Pipeline and Parse Markdown Content

| Field | Value |
| ----- | ----- |
| System | multimodal-knowledge-artifact-factory |
| Date created | 2026-03-25 |
| Assistant used | Cursor |
| Guide reference | P01-Scaffold_the_Pipeline_and_Parse_Markdown_Content.md |
| Estimated time | 45–60 minutes |
| Difficulty | Beginner |
| Dependencies (prior projects) | None (standalone) |
| Recurring cost | $0 |

## Execution discipline

> Use this section for every project in this series when executing an implementation plan.

- **One step at a time:** Within each phase, follow the **Steps** table **in row order**. Do not start step `X.(Y+1)` until step `X.Y` is **fully complete**.
- **Fully complete (one row):** (1) **Action** performed, (2) **Expected outcome** verified true (not assumed), (3) every **Evidence to capture** item exists in the execution record, **then** (4) mark **Status** `[x]`. Do not batch-check at the end of a phase only.
- **No skipping:** If blocked, stop, log gaps, update `implementation.md` and/or the vault production guide per the **Human quality gate**, then resume from the blocked step.
- **Between phases:** Do not start the next `## Phase N` until the previous phase’s **Human quality gate** is satisfied, including **Proceed**.
- **Optional:** After each step, confirm with the operator before continuing.

## At a glance

When P01 is complete, the following should be true:

- A **Rust binary crate** lives under this engineering system’s `build/` directory (Cargo project root), not the Git repo root.
- **`pulldown-cmark` 0.11** is declared in `Cargo.toml` and **`cargo build`** succeeds.
- **`main.rs`** reads a local `.md` file, parses with pulldown-cmark, and extracts **headers and paragraph text** into structured console output, with **`Result`-based** error handling (no silent file-read failures).
- A **complex sample markdown** run demonstrates clean separation of structural elements, ready as structured input for **P02** (VibeVoice TTS).

## Guide alignment

| Guide section | This plan |
| ------------- | --------- |
| Step 0 — Before You Start (Rust/Cargo, skeleton) | Phase 1 |
| Step 1 — Baseline Implementation | Phase 2 — row 2.1 |
| Step 2 — Building on the Baseline (dependency) | Phase 2 — row 2.2 |
| Step 3 — Advanced or Final Build (parser) | Phase 2 — row 2.3 |
| Step 4 — Finalization / validation run | Phase 2 — row 2.4 and Phase 3 — row 3.1 |
| Step 4 stress / edge behavior | Phase 3 — rows 3.2–3.3 |

**Note:** The vault initiative layout uses `initiatives/.../build/`; in **this portfolio repo**, the Cargo project root is **`engineering-systems/multimodal-knowledge-artifact-factory/build/`** (same “artifact under `build/`” rule).

---

## Phase 1 — Review and Setup

### Purpose (Phase 1)

Confirm Rust toolchain, correct working directory for Cargo, and full understanding of P01 before creating or modifying code.

### Prerequisites (Phase 1)

- Workstation with **Rust** and **Cargo** installed.
- Clone or workspace open at **`agentic-systems-engineering`** repo root (or equivalent path where `engineering-systems/multimodal-knowledge-artifact-factory/` exists).
- Project guide read in full before claiming Phase 1 complete (row 1.4).

### Steps (Phase 1)

| Step | Action | Expected outcome | Evidence to capture | Status |
| ---- | ------ | ---------------- | ------------------- | ------ |
| 1.1 | Run `rustc --version` and `cargo --version` from a terminal | Both commands print version strings (no “not found”) | Paste stdout into execution record | [ ] |
| 1.2 | From repo root, verify directory `engineering-systems/multimodal-knowledge-artifact-factory/build/` exists (create empty `build/` only if your packaging standard allows an empty dir before `cargo init`) | Path exists; you know the exact absolute or repo-relative path you will `cd` into for `cargo init` | Note path + `dir` / `ls` listing in record | [ ] |
| 1.3 | Confirm **no prior-project artifacts** are required (guide: **DEPENDENCIES — None**) | Written confirmation: P00/portfolio context only; no missing upstream project outputs | One-line note in execution record | [ ] |
| 1.4 | Re-read `P01-Scaffold_the_Pipeline_and_Parse_Markdown_Content.md` (Steps 0–4); list numbered guide steps in your own words in the execution record | All guide steps and validation checkpoints understood before Phase 2 | Bullet list in execution record | [ ] |

### Definition of done (Phase 1)

- [ ] All Phase 1 **Status** cells are `[x]` in order (1.1 → 1.4).
- [ ] Evidence for each row is referenced from the execution record.

### Human quality gate (Phase 1)

| Gate item | Pass criteria |
| --------- | ------------- |
| Steps complete | Every Phase 1 **Status** checked **in order** after outcome + evidence; definition of done satisfied |
| Evidence | Version output, path confirmation, and guide summary exist and are linked from the execution record |
| Gaps review | **No gaps** OR **Gaps listed** (short bullets) |
| Gap closure — project file | If any gap: update `implementation.md` at system root (`engineering-systems/multimodal-knowledge-artifact-factory/implementation.md`); commit per workflow before Phase 2 |
| Gap closure — source guide (conditional) | If the vault P01 guide is wrong (version, path): fix `P01-Scaffold_the_Pipeline_and_Parse_Markdown_Content.md` in vault (separate commit if required) |
| Proceed | **Proceed to Phase 2** [ ] (date / initials optional) |

---

## Phase 2 — Core Build

### Purpose (Phase 2)

Scaffold the Rust binary under `build/`, add **pulldown-cmark 0.11**, implement markdown parsing in `main.rs`, and run against a **complex** sample per the guide.

### Prerequisites (Phase 2)

- Phase 1 human quality gate passed (including **Proceed**).
- Terminal session ready with network for `cargo` crate download if needed.

### Steps (Phase 2)

| Step | Action | Expected outcome | Evidence to capture | Status |
| ---- | ------ | ---------------- | ------------------- | ------ |
| 2.1 | `cd` to `engineering-systems/multimodal-knowledge-artifact-factory/build/`. Run `cargo init` (or equivalent) to create a **binary** crate so `Cargo.toml` and `src/main.rs` exist under `build/` | `cargo build` succeeds from `build/`; `Cargo.toml` at crate root under `build/` | `cargo build` stdout; tree or listing of `build/` | [ ] |
| 2.2 | Edit Cargo.toml: under [dependencies], add pulldown-cmark with version 0.11 (exact). Run cargo build | Dependency resolves; build completes without errors | Cargo.toml snippet + cargo build output in record | [ ] |
| 2.3 | Implement parsing in `src/main.rs`: open a local `.md` file (relative path or CLI arg), read contents, iterate pulldown-cmark events, extract **headers and paragraph text**, print structured output; use **`Result`** for I/O and parse errors | Running the binary on a sample file prints clearly separated structural elements; errors are not silent | Sample command line + stdout + relevant `main.rs` excerpt or commit hash in record | [ ] |
| 2.4 | Run the binary against a **complex** markdown sample (multiple headings, paragraphs, nested structure as appropriate) | Output cleanly separates structural elements; pipeline is credibly ready to feed structured text to **VibeVoice** in P02 | Command + stdout (or saved log) in record; path to sample file | [ ] |

### Validation checkpoints (from project guide)

| Guide step | Checkpoint | Pass when |
| ---------- | ---------- | --------- |
| Step 1 | Project initializes without errors | `cargo build` OK from `build/` |
| Step 1 | `Cargo.toml` present at crate root under `build/` | File exists at expected path |
| Step 2 | `pulldown-cmark` added | Manifest shows `0.11` |
| Step 2 | Project builds | `cargo build` succeeds |
| Step 3 | Parser reads sample file | Run shows file content processed |
| Step 3 | Text elements isolated and printed | Console output reflects headers/paragraphs |
| Step 4 | Complex sample | Structural separation visible in output |

### Definition of done (Phase 2)

- [ ] Rows 2.1–2.4 completed **in order** with evidence.
- [ ] All validation checkpoints above satisfied or explicitly documented with rationale.

### Human quality gate (Phase 2)

| Gate item | Pass criteria |
| --------- | ------------- |
| Steps complete | Phase 2 **Status** rows `[x]` in order; definition of done satisfied |
| Evidence | Build logs, commands, and sample paths in execution record |
| Gaps review | **No gaps** OR **Gaps listed** |
| Gap closure — project file | If gaps: update `implementation.md` (Phase 1 / Foundation or equivalent section for P01); commit before Phase 3 |
| Gap closure — source guide (conditional) | Vault P01 guide updated if procedure or version was wrong |
| Proceed | **Proceed to Phase 3** [ ] |

### Notes from the project guide

- **Wrong directory for `cargo init`:** Run Cargo from **`build/`**, not the engineering system root or repo root.
- **Wrong crate version:** Use **`pulldown-cmark` 0.11** exactly as in the guide.
- **Hardcoded absolute paths:** Prefer relative paths or CLI arguments for the input `.md` file.
- **Silent failures:** Handle file read errors with **`Result`** (e.g. print error to stderr, non-zero exit).
- **Dioxus:** Named in the series context; **P01** scope is the **parse path** — interactive UI wiring is for later projects.

---

## Phase 3 — Integration and Smoke Test

### Purpose (Phase 3)

Confirm end-to-end behavior, document expected vs observed, and verify at least one controlled failure path.

### Prerequisites (Phase 3)

- Phase 2 human quality gate passed.

### Steps (Phase 3)

| Step | Action | Expected outcome | Evidence to capture | Status |
| ---- | ------ | ---------------- | ------------------- | ------ |
| 3.1 | Run the binary on the **same** complex sample used in 2.4 (or a documented alternate) | Behavior matches Phase 2 validation; no regression | Command + stdout in record | [ ] |
| 3.2 | Fill **Expected vs observed** below for the primary check | Documented match or justified delta | Completed block in execution record | [ ] |
| 3.3 | Run one **negative** case: e.g. **missing file path**, **empty file**, or **invalid path** | User-visible error (stderr message and/or non-zero exit); **no** silent success | Command + stderr / exit code in record | [ ] |

**Expected vs observed (fill during execution):**

```text
Check: Primary complex-sample run
Expected:
Observed:
Delta (if any):

Check: Negative case (specify which)
Expected:
Observed:
```

### Definition of done (Phase 3)

- [ ] 3.1–3.3 complete with evidence attached to the execution record.

### Human quality gate (Phase 3)

| Gate item | Pass criteria |
| --------- | ------------- |
| Steps complete | Phase 3 table completed in order |
| Evidence | Expected vs observed and failure-case transcript in record |
| Gaps review | **No gaps** OR **Gaps listed** |
| Gap closure — project file | `implementation.md` updated if behavior or scope changed |
| Gap closure — source guide (conditional) | Vault guide updated if test procedure was wrong |
| Proceed | **Proceed to Phase 4** [ ] |

---

## Phase 4 — Documentation and Evidence Capture

### Purpose (Phase 4)

Record execution, capture artifacts, route gaps, update the system implementation doc, and hand off to per-project validation per SOP.

### Prerequisites (Phase 4)

- Phase 3 human quality gate passed.

### Steps (Phase 4)

| Step | Action | Expected outcome | Evidence to capture | Status |
| ---- | ------ | ---------------- | ------------------- | ------ |
| 4.1 | Write all executed steps into `P01-execution-record.md` (create when executing this project) | Execution record reflects Phases 1–3 (and 4 as you go) | Link to record in repo | [ ] |
| 4.2 | Save evidence under `executions/P01-evidence/` (logs, screenshots as needed) | Artifacts exist at documented paths | List of file paths in record | [ ] |
| 4.3 | Complete **Gaps identified** in execution record | Each gap noted or explicit **None found** | Excerpt in record | [ ] |
| 4.4 | If any vault guide step was wrong, fix `P01-Scaffold_the_Pipeline_and_Parse_Markdown_Content.md` in the vault | Guide matches what worked | Commit reference or **N/A** | [ ] |
| 4.5 | Update `implementation.md` for **P01 / Foundation** (goals, inputs, outputs, decisions) | Document matches built state | Summary or diff reference in record | [ ] |
| 4.6 | Complete STEP 5.5 per SOP: add P01-validation.md with PASS | Validation documented | Link to validation doc when PASS; after build and smoke per SOP | [ ] |

### Definition of done (Phase 4)

- [ ] Rows 4.1–4.5 addressed during close-out; 4.6 completed when validation gate is satisfied.

### Human quality gate (Phase 4)

| Gate item | Pass criteria |
| --------- | ------------- |
| Steps complete | Phase 4 steps done per SOP; 4.6 when P01-validation.md is PASS |
| Evidence | Record + evidence folder references complete |
| Gaps review | **No gaps** OR gaps routed and documented |
| Gap closure — project file | `implementation.md` reflects P01 |
| Gap closure — source guide (conditional) | Vault guide updated if needed |
| Proceed | **Proceed to acceptance / P02 planning** [ ] |

---

## Acceptance criteria

This project is complete when:

- [ ] **Execution discipline** followed (no skipped steps; no batch-only checkoffs)
- [ ] All Phase 1–4 step rows are `[x]` in order with evidence in the execution record
- [ ] All four **Human quality gates** completed with no open gaps (or gaps closed in `implementation.md` / vault guide)
- [ ] Execution record exists and is complete
- [ ] Per-project validation: **PASS** (`P01-validation.md`)
- [ ] `implementation.md` updated for this phase
- [ ] Commits follow SOP message convention (`docs(...)`, `feat(...)`, etc.)

## Handoff to P02

The next project in the series uses **VibeVoice** (and related integration) to turn structured parsed text into audio. **Before starting P02:**

- P01 binary runs from `build/` and produces **structured text output** suitable as TTS input.
- Sample markdown path(s) and commands are documented in the execution record.
- **`P02-implementation-plan.md`** should copy the same **Execution discipline** and **Human quality gate** cadence as this document (reuse the **Implementation Plan Template** referenced from **PORTFOLIO-BUILD-SOP** STEP 5.1, or duplicate this file’s structure).

---

## Reference

- **Implementation Plan Template** — canonical skeleton linked from **PORTFOLIO-BUILD-SOP** (STEP 5.1).
- **PORTFOLIO-BUILD-SOP** — STEP 5.1 through 5.5 for plan, build, validation, and execution record.
