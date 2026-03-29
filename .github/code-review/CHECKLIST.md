# PR Review Checklist

Used by: **AI / human pre-flight** against **[codereview.md](./codereview.md)** (plan + code depth) and this file (**portfolio doc gates**). Automated GitHub Action validation references these paths.

For a full step or phase review, load **codereview.md** first, then tick the layers below for Markdown / engineering-system PRs.

## Layer 1 — Portfolio Voice and Navigation (Binary)

- [ ] No private-workspace labels, internal curriculum codenames, or paths that only exist outside this repository in modified reader-facing files
- [ ] Breadcrumb navigation present at the top of all modified nested markdown docs
- [ ] Audience routing table is present and robust in the root `README.md`
- [ ] System `README.md` opens with a 3-line Problem/Approach/Outcome block
- [ ] Screenshot or documented HTML comment placeholder present in system `README.md`
- [ ] "Related systems" section present in system `README.md`

## Layer 2 — Evidence Integrity (Binary)

- [ ] Every "PASS" claim is linked to an evidence file or directory
- [ ] "PASS (conditional)" reserved for cases where a **named** dependency is still unverified locally (e.g. AIRI desktop for multimodal P04). If every validation row cites **committed** transcripts under `executions/evidence/p0X/` (including documented health outcomes or approved synthetic paths per plan), use plain **PASS** — e.g. retrieval **P03** with **`p03-*`** + **`validation/P03-validation.md`**, not conditional
- [ ] Evidence paths trace correctly to `executions/evidence/p0X/` format; filenames in validation and implementation plans match files actually committed (no phantom **`p03-*`** names)
- [ ] Reproducibility section (OS, toolchain, date, Cargo.lock) present in `validation.md`

## Layer 3 — Judgment Quality (Rated 1–3)

- [ ] Tradeoff honesty: are rejected alternatives present and is "why not" answered?
- [ ] Failure modes: ≥3 distinct modes outlining blast radius, detection, and mitigation?
- [ ] Problem statement: does it lead with the business/mission constraint rather than the technology?
- [ ] Validation honesty: does validation exactly reflect what was built?
- [ ] ADRs: do they cite real constraints with ≥2 alternatives each?

## Out of Scope

- Rust or Python core logic styling (handled by `cargo fmt` and `clippy`)
- Line-level grammar suggestions
- Architectural redesign proposals
- Files not present in the PR diff
