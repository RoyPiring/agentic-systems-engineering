> ← [Home](../README.md)

# Engineering Systems — Full Index

All engineering systems in this repository. Each system has five required documents: README, business-context, architecture, implementation, validation.

## Systems

| # | System | Scope | Tech Stack | Status |
|---|--------|-------|-----------|--------|
| 10 | [multimodal-knowledge-artifact-factory](./multimodal-knowledge-artifact-factory/) | Local pipeline: markdown → parse → audio → Dioxus viewer → study exports | Rust, Python, Dioxus | ✅ P01–P04 |

## How systems are added

Systems enter via feature branch and pull request. The PR must pass CI (markdown lint, link check, structure validation) and the review-gate checklist before merge. See [CONTRIBUTING.md](../CONTRIBUTING.md) for the full process.
