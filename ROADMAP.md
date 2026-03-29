> ← [Home](./README.md)

# Roadmap — Agentic Systems Engineering

**Twelve portfolio slots** (dependency-first numbering). Only **slots with links** currently have a folder under [`engineering-systems/`](./engineering-systems/). Everything else is planned narrative until a feature branch lands.

**Today:** **#1 Retrieval Backbone** — P01–P03 executed and validation **PASS** (ingest, citation-aware query, web ingest path with committed evidence). **#10 Multimodal Knowledge Artifact Factory** — P01–P04 shipped on `main`.

| # | System | Focus area | Status |
|---|--------|------------|--------|
| 1 | [Retrieval Backbone — Multi-Domain Knowledge](./engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/) | Multi-domain knowledge retrieval (Unstructured, Qdrant, LlamaIndex, Ollama → web + Ragas) | 🔨 **P01–P03** [PASS](./engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/validation.md); **P04** planned |
| 2 | *Durable Agent Workflow Orchestrator* | Resilient orchestration of agentic workflows | 📋 Planned |
| 3 | *Agent Eval and Audit Command Center* | Evaluation, audit, and command logic for agents | 📋 Planned |
| 4 | *MCP Tool Service Mesh for Agents* | Secure tool routing and context protocol mesh | 📋 Planned |
| 5 | *Multi-Model Routing and Cost Governance Platform* | Model routing and token cost guardrails | 📋 Planned |
| 6 | *Cross-Domain Memory Service* | Persistent state and memory across agent domains | 📋 Planned |
| 7 | *Personal AI Operating System* | Personal agentic OS baseline and local routing | 📋 Planned |
| 8 | *Agentic Security and Trust Boundary Program* | Trust boundaries, enforcement, and governance | 📋 Planned |
| 9 | *Browser Research and Verification Fleet* | Multi-agent browser execution and verification | 📋 Planned |
| 10 | [Multimodal Knowledge Artifact Factory](./engineering-systems/multimodal-knowledge-artifact-factory/) | Parse, local TTS, desktop UI, study exports | ✅ **P01–P04** shipped on `main` |
| 11 | *Autonomous Research Improvement Loop* | Agentic research loops with self-improvement | 📋 Planned |
| 12 | *Multi-Domain Agent Service Layer* | Unified service layer across agent architectures | 📋 Planned |

**Status key:** ✅ Shipped on `main` · 🔨 Active / partial merge (feature branch or in progress) · 📋 Planned (no `engineering-systems/<slug>/` yet)

## Publication standard

A system is eligible for publication when:

- All five required documents exist (README, business-context, architecture, implementation, validation)
- Validation includes expected and observed results with at least two negative cases
- CI passes on the PR branch (markdown lint, link check, structure validation)
- Evidence artifacts are linked and resolve correctly

See [QUALITY_STANDARDS.md](./QUALITY_STANDARDS.md) for the full baseline.
