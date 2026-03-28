# Case-study artifacts (optional copies)

**Source of truth for P04 exports:** **`../executions/evidence/p04/exports/`** (`flashcards.json`, `quiz.md`).

This folder holds **optional reviewer-facing copies** of those files after you run the case-study pipeline. Commit them only if you want the PR to show study outputs without opening the evidence tree.

## Sync (PowerShell)

After **[RUNBOOK.md](../RUNBOOK.md) §2** succeeds, **cwd = `build/`**:

```powershell
Copy-Item ..\executions\evidence\p04\exports\flashcards.json ..\case-study\artifacts\ -Force
Copy-Item ..\executions\evidence\p04\exports\quiz.md ..\case-study\artifacts\ -Force
```

**cwd = system root** (folder that contains `build/` and `case-study/`):

```powershell
Copy-Item .\executions\evidence\p04\exports\flashcards.json .\case-study\artifacts\ -Force
Copy-Item .\executions\evidence\p04\exports\quiz.md .\case-study\artifacts\ -Force
```

**Do not** treat this folder as the integration script’s write target — **`integration.py`** still resolves **`MKAF_P04_EXPORTS`** to **`executions/evidence/p04/exports/`**.
