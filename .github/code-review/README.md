# Code review artifacts

| File | Purpose |
| ---- | -------- |
| **[codereview.md](./codereview.md)** | **code-reviewer** agent: plan alignment, code quality, architecture, severity-rated findings. Use after major steps or before merge. |
| **[CHECKLIST.md](./CHECKLIST.md)** | **agentic-systems-engineering** portfolio gates: public voice, breadcrumbs, evidence layout, ADR honesty (binary + rated checks). |

**PR flow:** Authors use [pull-requests/PR_TEMPLATE.md](../pull-requests/PR_TEMPLATE.md). Reviewers (human or AI) use **codereview.md** for depth and **CHECKLIST.md** for repo-specific doc/evidence rules.

**Automation:** [.github/workflows/ai-pr-review.yml](../workflows/ai-pr-review.yml) may consume these files when a full LLM step is wired; today it references the checklist in PR comments.
