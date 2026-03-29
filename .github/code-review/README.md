# Code review artifacts

| File | Purpose |
| ---- | -------- |
| **[codereview.md](./codereview.md)** | **code-reviewer** agent: plan alignment, code quality, architecture, severity-rated findings. |
| **[CHECKLIST.md](./CHECKLIST.md)** | Portfolio gates: public voice, breadcrumbs, evidence layout, ADR honesty. |

## Per-slice folders: `YYYY-MM-DD-<engineering-system-folder>/`

Same folder name as [pull-requests/](../pull-requests/) and [changelog/](../changelog/) for that **date + series**.

- **`README.md`** — hub linking PR body file(s), changelog, and the canonical briefs above.
- **`PRE_MERGE_REVIEW.md`** — optional; add when you record a pre-merge review (one file per slice, or split by project if needed).

**Master index:** [SLICE_LAYOUT.md](../SLICE_LAYOUT.md)

**Automation:** [.github/workflows/ai-pr-review.yml](../workflows/ai-pr-review.yml) references the root briefs; slice folders are for human-recorded outcomes.
