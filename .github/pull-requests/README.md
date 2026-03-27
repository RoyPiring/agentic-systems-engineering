# Pull request helpers

- **Default PR body (GitHub web UI):** [../pull_request_template.md](../pull_request_template.md) — must live at repo root under `.github/` for GitHub to pre-fill new PRs.
- **Filled bodies for CLI:** `PR_BODY_MULTIMODAL_P01_FILLED.md`, `PR_BODY_MULTIMODAL_P02_FILLED.md`, etc.

Recommended CLI (avoids broken escaping and stray tooling footers):

```bash
gh pr create --base main --head <branch> --title "…" --body-file .github/pull-requests/PR_BODY_<topic>_FILLED.md
```

To refresh an open PR description:

```bash
gh pr edit <n> --body-file .github/pull-requests/PR_BODY_<topic>_FILLED.md
```
