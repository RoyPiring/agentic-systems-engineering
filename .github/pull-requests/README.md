# Pull request helpers

**Canonical PR scaffold:** [`PR_TEMPLATE.md`](./PR_TEMPLATE.md) — copy into the GitHub PR description, or use it to author a new `PR_BODY_*_FILLED.md`.

**Code review brief:** [`../code-review/codereview.md`](../code-review/codereview.md) (**code-reviewer** agent — plan alignment, code quality, severity-rated findings). Portfolio doc gates: [`../code-review/CHECKLIST.md`](../code-review/CHECKLIST.md).

**Filled bodies (CLI / `gh`):** `PR_BODY_MULTIMODAL_P01_FILLED.md`, `PR_BODY_MULTIMODAL_P02_FILLED.md`, `PR_BODY_MULTIMODAL_P03_FILLED.md`, `PR_BODY_MULTIMODAL_FULL_SERIES_FILLED.md`, …

This repo **does not** use `.github/pull_request_template.md`. That avoids two diverging copies; GitHub will not auto-inject a body — paste from here or use `--body-file` below.

**Recommended CLI** (avoids broken escaping and stray tooling footers):

```bash
gh pr create --base main --head feature/multimodal-knowledge-artifact-factory-p03 \
  --title "feat(multimodal-knowledge-artifact-factory): full series — P04 + case study" \
  --body-file .github/pull-requests/PR_BODY_MULTIMODAL_FULL_SERIES_FILLED.md
```

Refresh an open PR description:

```bash
gh pr edit <n> --body-file .github/pull-requests/PR_BODY_MULTIMODAL_FULL_SERIES_FILLED.md
```

**Same change set — also complete:**

1. **Changelog** — `.github/changelog/YYYY-MM-DD-<slug>[-p0X].md` from [`../changelog/CHANGELOG_ENTRY_TEMPLATE.md`](../changelog/CHANGELOG_ENTRY_TEMPLATE.md); link it in the PR checklist.
2. **Workflows** — `.github/workflows/` (e.g. docs lint on `**/*.md`) green before merge.
3. **Issue templates** — `.github/ISSUE_TEMPLATE/` for bug / feature reports (optional for private repos; recommended for public portfolio).

Align changelog, body file, and CI with the same change set before merge (portfolio workflow Steps 66, 72, 73).
