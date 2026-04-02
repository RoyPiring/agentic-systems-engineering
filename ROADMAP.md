> ← [Home](./README.md)

# Roadmap — Agentic Systems Engineering

**Twelve portfolio slots** (dependency-first numbering). Only **slots with links** currently have a folder under [`engineering-systems/`](./engineering-systems/). Everything else is planned narrative until a feature branch lands.

**Today:** **#1 Retrieval Backbone** — P01–P04 executed and validation **PASS** (ingest, citation-aware query, web ingest, Ragas + packaged service — evidence under `executions/evidence/p04/`). **#10 Multimodal Knowledge Artifact Factory** — P01–P04 shipped on `main`.

## Published

| # | System | Focus area | Status |
|---|--------|------------|--------|
| 1 | [Retrieval Backbone — Multi-Domain Knowledge](./engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/) | Multi-domain knowledge retrieval (Unstructured, Qdrant, LlamaIndex, Ollama → web + Ragas) | ✅ **P01–P04** [PASS](./engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/validation.md) |
| 10 | [Multimodal Knowledge Artifact Factory](./engineering-systems/multimodal-knowledge-artifact-factory/) | Parse, local TTS, desktop UI, study exports | ✅ **P01–P04** shipped on `main` |

## Planned

Target quarters are directional planning signals, not delivery promises.

| # | System | Focus area | Target | Status |
|---|--------|------------|--------|--------|
| 2 | *Durable Agent Workflow Orchestrator* | Resilient orchestration of agentic workflows | Q2 2026 | 📋 Planned |
| 3 | *Agent Eval and Audit Command Center* | Evaluation, audit, and command logic for agents | Q2 2026 | 📋 Planned |
| 4 | *MCP Tool Service Mesh for Agents* | Secure tool routing and context protocol mesh | Q2 2026 | 📋 Planned |
| 5 | *Multi-Model Routing and Cost Governance Platform* | Model routing and token cost guardrails | Q2 2026 | 📋 Planned |
| 6 | *Cross-Domain Memory Service* | Persistent state and memory across agent domains | Q3 2026 | 📋 Planned |
| 7 | *Personal AI Operating System* | Personal agentic OS baseline and local routing | Q3 2026 | 📋 Planned |
| 8 | *Agentic Security and Trust Boundary Program* | Trust boundaries, enforcement, and governance | Q3 2026 | 📋 Planned |
| 9 | *Browser Research and Verification Fleet* | Multi-agent browser execution and verification | Q4 2026 | 📋 Planned |
| 11 | *Autonomous Research Improvement Loop* | Agentic research loops with self-improvement | Q4 2026 | 📋 Planned |
| 12 | *Multi-Domain Agent Service Layer* | Unified service layer across agent architectures | Q4 2026 | 📋 Planned |

**Status key:** ✅ Shipped on `main` · 🔨 Active / partial merge (feature branch or in progress) · 📋 Planned (no `engineering-systems/<slug>/` yet)

## Publication standard

A system is eligible for publication when:

- All five required documents exist (README, business-context, architecture, implementation, validation)
- Validation includes expected and observed results with at least two negative cases
- CI passes on the PR branch (markdown lint, link check, structure validation)
- Evidence artifacts are linked and resolve correctly

See [QUALITY_STANDARDS.md](./QUALITY_STANDARDS.md) for the full baseline.
