# ADR-003: Build interactive knowledge views with Dioxus 0.7

## Status

Accepted

## Context

Learners need **interactive views** over parsed content (navigation, structured study UX) without standing up a separate front-end repo and cloud host. The series locks **Dioxus 0.7.3** for Rust UI.

## Decision

Implement interactive knowledge views as a **Dioxus** application (version aligned with P00), consuming the same structured data produced by the markdown parse stage.

## Alternatives considered

- **Static HTML generator only** — Simple to host but weak for stateful study flows and component reuse.
- **Electron + web stack** — Familiar to many teams but heavier runtime and more moving parts than a Rust-native UI for this scope.
- **Tauri** — Strong alternative for desktop shells; series explicitly chose Dioxus for the UI layer, so we align with the locked curriculum path.

## Consequences

**Positive:** Cohesive Rust workspace, component model suited to iterative P03 build steps.  
**Negative / tradeoffs:** Platform build matrix (desktop vs web target) must be documented for reproducibility.  
**Follow-ups:** Capture build/run commands and platform notes in execution records for P03.
