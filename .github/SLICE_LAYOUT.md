# Portfolio slice layout (multi-project series)

Group work by **calendar date** + **engineering-system folder name** (same string as `engineering-systems/<name>/`). Use the **same folder name** under `pull-requests/`, `changelog/`, and `code-review/`.

**Pattern:** `.github/{pull-requests|changelog|code-review}/YYYY-MM-DD-<engineering-system-folder>/`

- **One changelog file per folder:** `CHANGELOG.md` — if several projects merge that day for that system, add multiple `##` sections (see **2026-03-26** multimodal: P01 + P02).
- **Pull request bodies:** If **one** PR that day → `PR_BODY.md`. If **several** → `PR_BODY_P01.md`, `PR_BODY_P02.md`, … (use with `gh pr create --body-file …`).
- **Code review:** `README.md` hub + optional `PRE_MERGE_REVIEW.md` (or per-PR filenames when needed).

| Folder (`YYYY-MM-DD-<system>/`) | System folder | PR bodies | Changelog | Code review hub |
| ------------------------------- | ------------- | --------- | --------- | --------------- |
| `2026-03-26-multimodal-knowledge-artifact-factory` | `multimodal-knowledge-artifact-factory` | [P01](./pull-requests/2026-03-26-multimodal-knowledge-artifact-factory/PR_BODY_P01.md), [P02](./pull-requests/2026-03-26-multimodal-knowledge-artifact-factory/PR_BODY_P02.md) | [CHANGELOG.md](./changelog/2026-03-26-multimodal-knowledge-artifact-factory/CHANGELOG.md) | [README.md](./code-review/2026-03-26-multimodal-knowledge-artifact-factory/README.md) |
| `2026-03-27-multimodal-knowledge-artifact-factory` | `multimodal-knowledge-artifact-factory` | [PR_BODY.md](./pull-requests/2026-03-27-multimodal-knowledge-artifact-factory/PR_BODY.md) | [CHANGELOG.md](./changelog/2026-03-27-multimodal-knowledge-artifact-factory/CHANGELOG.md) | [README.md](./code-review/2026-03-27-multimodal-knowledge-artifact-factory/README.md) |
| `2026-03-28-multimodal-knowledge-artifact-factory` | `multimodal-knowledge-artifact-factory` | [PR_BODY.md](./pull-requests/2026-03-28-multimodal-knowledge-artifact-factory/PR_BODY.md) | [CHANGELOG.md](./changelog/2026-03-28-multimodal-knowledge-artifact-factory/CHANGELOG.md) | [README.md](./code-review/2026-03-28-multimodal-knowledge-artifact-factory/README.md) |
| `2026-03-28-retrieval-backbone-for-multi-domain-knowledge-systems` | `retrieval-backbone-for-multi-domain-knowledge-systems` | [PR_BODY.md](./pull-requests/2026-03-28-retrieval-backbone-for-multi-domain-knowledge-systems/PR_BODY.md) | [CHANGELOG.md](./changelog/2026-03-28-retrieval-backbone-for-multi-domain-knowledge-systems/CHANGELOG.md) | [README.md](./code-review/2026-03-28-retrieval-backbone-for-multi-domain-knowledge-systems/README.md) · [PRE_MERGE_REVIEW.md](./code-review/2026-03-28-retrieval-backbone-for-multi-domain-knowledge-systems/PRE_MERGE_REVIEW.md) |
| `2026-03-29-retrieval-backbone-for-multi-domain-knowledge-systems` | `retrieval-backbone-for-multi-domain-knowledge-systems` | [PR_BODY.md](./pull-requests/2026-03-29-retrieval-backbone-for-multi-domain-knowledge-systems/PR_BODY.md) | [CHANGELOG.md](./changelog/2026-03-29-retrieval-backbone-for-multi-domain-knowledge-systems/CHANGELOG.md) | [README.md](./code-review/2026-03-29-retrieval-backbone-for-multi-domain-knowledge-systems/README.md) · [PRE_MERGE_REVIEW.md](./code-review/2026-03-29-retrieval-backbone-for-multi-domain-knowledge-systems/PRE_MERGE_REVIEW.md) |

**Shared templates (not slice-specific):**

- PR scaffold: [pull-requests/PR_TEMPLATE.md](./pull-requests/PR_TEMPLATE.md)
- Changelog scaffold: [changelog/CHANGELOG_ENTRY_TEMPLATE.md](./changelog/CHANGELOG_ENTRY_TEMPLATE.md)
- Review briefs: [code-review/codereview.md](./code-review/codereview.md), [code-review/CHECKLIST.md](./code-review/CHECKLIST.md)
