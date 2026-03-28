# PR Review Checklist

Used by: AI pre-flight review (Appendix O) and automated GitHub Action validation.

## Layer 1 — Portfolio Voice and Navigation (Binary)
- [ ] No insider jargon (`PineappleKingdom`, `Project Library` as proper noun, `vault`, `gap-log`) in modified files
- [ ] Breadcrumb navigation present at the top of all modified nested markdown docs
- [ ] Audience routing table is present and robust in the root `README.md`
- [ ] System `README.md` opens with a 3-line Problem/Approach/Outcome block
- [ ] Screenshot or documented HTML comment placeholder present in system `README.md`
- [ ] "Related systems" section present in system `README.md`

## Layer 2 — Evidence Integrity (Binary)
- [ ] Every "PASS" claim is linked to an evidence file or directory
- [ ] "PASS (conditional)" used appropriately where a system dependency (e.g. neural path or AIRI) is unverified locally
- [ ] Evidence paths trace correctly to `executions/evidence/p0X/` format
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
