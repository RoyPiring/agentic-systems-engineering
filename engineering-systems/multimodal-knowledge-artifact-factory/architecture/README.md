# Architecture artifacts

This folder mirrors the **Repository Packaging (RP)** layout from the Project Library series: per-phase folders for diagrams, screenshots, and supporting notes.

## Layout

```text
architecture/
├── README.md          ← you are here
├── P00/               ← series / system-level
│   ├── 01-Images/     ← diagrams, screenshots, exports
│   └── 02-Prompts/    ← prompts and short architecture notes
├── P01/ … P04/        ← same structure per project in the series
```

## How this relates to `architecture.md`

- **`architecture.md`** (at the engineering-system root) is the narrative: intent, Mermaid overview, ADRs, tradeoffs, failure modes, security, cost.
- **`architecture/`** holds **supplemental** assets that are awkward to inline (PNG/SVG exports, multi-page diagrams, prompt transcripts).

During the portfolio build, drop exports into `architecture/P0X/01-Images/` and optional prompt or decision notes into `architecture/P0X/02-Prompts/`.
