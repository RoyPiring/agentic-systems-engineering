# Pull request helpers

**Canonical PR scaffold:** [`PR_TEMPLATE.md`](./PR_TEMPLATE.md) — copy into the GitHub PR description, or use it to author bodies under a **date + system** folder.

**Slice index (same folder name → changelog + code review):** [`../SLICE_LAYOUT.md`](../SLICE_LAYOUT.md)

**Code review brief:** [`../code-review/codereview.md`](../code-review/codereview.md) · Portfolio gates: [`../code-review/CHECKLIST.md`](../code-review/CHECKLIST.md).

## Folders: `YYYY-MM-DD-<engineering-system-folder>/`

Use the **exact** folder name of the system under `engineering-systems/` (e.g. `multimodal-knowledge-artifact-factory`). Multiple PRs the **same day** for the **same** system → multiple body files (`PR_BODY_P01.md`, …). A **single** PR that day → `PR_BODY.md`.

| Folder | PR body file(s) | Changelog | Code review |
| ------ | ---------------- | --------- | ----------- |
| [`2026-03-26-multimodal-knowledge-artifact-factory/`](./2026-03-26-multimodal-knowledge-artifact-factory/) | `PR_BODY_P01.md`, `PR_BODY_P02.md` | [`CHANGELOG.md`](../changelog/2026-03-26-multimodal-knowledge-artifact-factory/CHANGELOG.md) | [`README`](../code-review/2026-03-26-multimodal-knowledge-artifact-factory/README.md) |
| [`2026-03-27-multimodal-knowledge-artifact-factory/`](./2026-03-27-multimodal-knowledge-artifact-factory/) | `PR_BODY.md` | [`CHANGELOG.md`](../changelog/2026-03-27-multimodal-knowledge-artifact-factory/CHANGELOG.md) | [`README`](../code-review/2026-03-27-multimodal-knowledge-artifact-factory/README.md) |
| [`2026-03-28-multimodal-knowledge-artifact-factory/`](./2026-03-28-multimodal-knowledge-artifact-factory/) | `PR_BODY.md` | [`CHANGELOG.md`](../changelog/2026-03-28-multimodal-knowledge-artifact-factory/CHANGELOG.md) | [`README`](../code-review/2026-03-28-multimodal-knowledge-artifact-factory/README.md) |
| [`2026-03-28-retrieval-backbone-for-multi-domain-knowledge-systems/`](./2026-03-28-retrieval-backbone-for-multi-domain-knowledge-systems/) | `PR_BODY.md` | [`CHANGELOG.md`](../changelog/2026-03-28-retrieval-backbone-for-multi-domain-knowledge-systems/CHANGELOG.md) | [`PRE_MERGE`](../code-review/2026-03-28-retrieval-backbone-for-multi-domain-knowledge-systems/PRE_MERGE_REVIEW.md) |

This repo **does not** use `.github/pull_request_template.md`.

**Examples — `gh pr create --body-file`:**

```bash
# Multimodal full series (one PR that day)
gh pr create --base main --head feature/multimodal-knowledge-artifact-factory-p03 \
  --title "feat(multimodal-knowledge-artifact-factory): full series — P04 + case study" \
  --body-file .github/pull-requests/2026-03-28-multimodal-knowledge-artifact-factory/PR_BODY.md
```

```bash
# Retrieval P01
gh pr create --base main --head feature/retrieval-backbone-for-multi-domain-knowledge-systems \
  --title "feat(retrieval-backbone): P01 ingest + Qdrant" \
  --body-file .github/pull-requests/2026-03-28-retrieval-backbone-for-multi-domain-knowledge-systems/PR_BODY.md
```

```bash
# Same date + system, second PR (historical): use the numbered body file
gh pr create --body-file .github/pull-requests/2026-03-26-multimodal-knowledge-artifact-factory/PR_BODY_P02.md
```

**Same change set — also complete:** `changelog/…/CHANGELOG.md`, CI green, issue templates as needed. See [SLICE_LAYOUT.md](../SLICE_LAYOUT.md).
