## [System folder name] — short title

**What:** One or two sentences: what this PR changes and why it matters for that engineering system.

**Scope:** Which phase(s) (e.g. P03) or area (docs-only, CI, cross-system link). Call out if behavior vs documentation only.

**How to review:**

1. Skim the system `README.md` (orientation) and `validation.md` (PASS rows).
2. Follow links to `executions/evidence/` for this slice — filenames should match validation text.
3. For code changes, start from `build/` and the relevant `executions/implementation/P0X-implementation-plan.md`.

**Proof:** List the main evidence paths or validation file(s) (no need to paste logs).

### Checklist

- [ ] CI green on this branch (docs lint / workflows as configured).
- [ ] No private workspace paths or secrets in committed markdown or code.
- [ ] Slice artifacts updated when required: see [.github/SLICE_LAYOUT.md](../SLICE_LAYOUT.md) (changelog + optional `code-review/` / `pull-requests/` dated folder for that system).

**Follow-ups (optional):** Non-blocking items after merge; keep this short or omit.
