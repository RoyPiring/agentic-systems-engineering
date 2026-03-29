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
5. Pull request opened against review-gate checklist (`.github/pull-requests/PR_TEMPLATE.md`) with artifacts under the same dated slice as [`.github/SLICE_LAYOUT.md`](.github/SLICE_LAYOUT.md)
6. Squash merge to `main`, tag, GitHub Release

## Naming conventions

| Item | Convention | Example |
|------|-----------|---------|
| System folder | lowercase, hyphens only | `multimodal-knowledge-artifact-factory` |
| Feature branch | `feature/{slug}` or `feature/{slug}-p0X` | `feature/multimodal-knowledge-artifact-factory-p03` |
| Tags | `v1.0.0-{slug}` | `v1.0.0-multimodal-knowledge-artifact-factory` |
| Commit prefix | `feat({slug})`, `feat({slug}/P0X)`, `docs`, `fix`, `chore` | `feat(multimodal-knowledge-artifact-factory/P02): tts stub pipeline` |

## PR process

PR descriptions come from `.github/pull-requests/` under **`YYYY-MM-DD-<engineering-system-folder>/`**: one PR that day → `PR_BODY.md`; several PRs that day for the same system → `PR_BODY_P01.md`, `PR_BODY_P02.md`, … (see `.github/pull-requests/README.md` and `.github/SLICE_LAYOUT.md`). Pair with `changelog/<same-folder>/CHANGELOG.md` and optional `code-review/<same-folder>/`. Example: `gh pr create --body-file .github/pull-requests/2026-03-28-retrieval-backbone-for-multi-domain-knowledge-systems/PR_BODY.md`.

## Issues

Bug reports and gap/enhancement requests are welcome via GitHub Issues using the templates in `.github/ISSUE_TEMPLATE/`.
