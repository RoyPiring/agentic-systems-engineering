# Executions

| Artifact | Purpose |
| -------- | ------- |
| `execution-record.md` | **One** log for P01–P04 — add `## P0X — …` per project (**summary**: phase status, key commands, evidence links) |
| `implementation/` | Per-project **plans** (`P0X-implementation-plan.md`) |
| `evidence/` | Run artifacts only (logs, transcripts, toolchain capture). Use flat **`evidence/p01/`** … **`evidence/p04/`** (name files with a `p0X-` prefix so they sort cleanly). Add **series-specific** subfolders only if a project guide requires them. |

| Project | Plan | Record | Validation | More evidence (examples) |
| ------- | ---- | ------ | ---------- | ------------------------ |
| P01 | `implementation/P01-implementation-plan.md` | `execution-record.md` (P01 section) | `../validation/P01-validation.md` | `evidence/p01/p01-*.txt` |
| P02 | `implementation/P02-implementation-plan.md` | `execution-record.md` | `../validation/P02-validation.md` | `evidence/p02/` |
| P03 | `implementation/P03-implementation-plan.md` | `execution-record.md` | `../validation/P03-validation.md` | `evidence/p03/` |
| P04 | `implementation/P04-implementation-plan.md` | `execution-record.md` | `../validation/P04-validation.md` | `evidence/p04/` |

When you change a plan or `validation/P0X-validation.md`, update **`implementation.md`** and **`validation.md`** in the same commit. Keep internal review notes out of this folder—they do not belong in the public engineering-system tree.
