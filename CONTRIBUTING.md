> ← [Home](./README.md)

# Contributing

This is a **portfolio repository**, not a collaborative open-source project. It is maintained by a single engineer to demonstrate systems engineering work in the agentic AI domain.

## How systems are added

1. Feature branch from `main` — `feature/{system-slug}` or `feature/{system-slug}-p0X` for incremental slices
2. Scaffold system folder under `engineering-systems/{slug}/`
3. Five required documents must exist before merge:
   - `README.md`
   - `business-context.md`
   - `architecture.md`
   - `implementation.md`
   - `validation.md`
4. CI must pass: markdown lint, link check, and structure validation
5. Pull request opened against review-gate checklist (`.github/pull-requests/PR_TEMPLATE.md`)
6. Squash merge to `main`, tag, GitHub Release

## Naming conventions

| Item | Convention | Example |
|------|-----------|---------|
| System folder | lowercase, hyphens only | `multimodal-knowledge-artifact-factory` |
| Feature branch | `feature/{slug}` or `feature/{slug}-p0X` | `feature/multimodal-knowledge-artifact-factory-p03` |
| Tags | `v1.0.0-{slug}` | `v1.0.0-multimodal-knowledge-artifact-factory` |
| Commit prefix | `feat({slug})`, `feat({slug}/P0X)`, `docs`, `fix`, `chore` | `feat(multimodal-knowledge-artifact-factory/P02): tts stub pipeline` |

## PR process

PR descriptions come from `.github/pull-requests/` — either the blank `PR_TEMPLATE.md` or a pre-filled `PR_BODY_*_FILLED.md`. Use `gh pr create --body-file .github/pull-requests/PR_BODY_<name>.md` to paste directly.

## Issues

Bug reports and gap/enhancement requests are welcome via GitHub Issues using the templates in `.github/ISSUE_TEMPLATE/`.
