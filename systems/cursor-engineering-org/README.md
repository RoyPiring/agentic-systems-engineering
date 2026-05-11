# Command a 25-Engineer AI Org in Cursor

> Inside the [Agentic Systems Engineering](../../README.md) portfolio · *AI agents and orchestration that move from prompt to outcome.*

## Overview

A simulated 90-minute engineering sprint in which 25 Cursor subagents — organized into five parallel teams (Alpha, Bravo, Charlie, Delta, Echo) — deliver a shareholder-ready software package under real DevSecOps and governance controls. The system answers a specific question about agent orchestration: *what does it take to scale AI-assisted engineering from a single coding assistant to an entire org without losing reviewability, traceability, or incident discipline?*

Concurrency comes from **Cursor `/multitask` + git worktrees**, which let five teams operate on isolated branches simultaneously rather than serially. Governance comes from branch protection, ADRs (e.g. Axum over Actix for the Rust gateway), Cursor Rules / Skills / Hooks, and a security pipeline that runs Gitleaks, Semgrep, and Trivy on every PR. A mid-sprint Murphy's Law SQL-injection incident was contained in 8 minutes MTTR, and a Zero-Day CVE all-hands drill validated cross-team remediation. The sprint produced 25 merged PRs, a 96% first-pass security-gate success rate, and a KPI dashboard + executive summary built for the board.

The architecture below shows the operating shape: Cursor Max Mode multi-agent workspace → governance + sprint planning artifacts → five parallel engineering teams via `/multitask` and worktrees → DevSecOps CI gates → incident-response and hardening loop → executive reporting + retrospective.

## Architecture

```mermaid
---
title: Cursor 25-Engineer AI Org — Multi-Agent Sprint Orchestration
---
%%{init: {"theme":"base","themeVariables": {"primaryColor":"#1B4332","primaryTextColor":"#F4D03F","primaryBorderColor":"#F4D03F","secondaryColor":"#264653","tertiaryColor":"#2F5233","lineColor":"#F4D03F","fontFamily":"ui-monospace, SFMono-Regular, Menlo, Consolas, monospace","fontSize":"13px"}}}%%
flowchart TD
    classDef datastore fill:#264653,stroke:#F4D03F,stroke-width:2px,color:#FFFFFF
    classDef service fill:#1B4332,stroke:#F4D03F,stroke-width:2px,color:#F4D03F
    classDef event fill:#7B42BC,stroke:#F4D03F,stroke-width:2px,color:#FFFFFF
    classDef io fill:#0d1117,stroke:#F4D03F,stroke-width:1.5px,color:#F4D03F,font-style:italic

    Director[/Engineering Director: Operator + Orchestrator/]
    Murphy[/Murphy's Law Event: SQL Injection Mid-Sprint/]
    ZeroDay[/Zero-Day CVE: Cross-Team All-Hands Drill/]
    Shareholders[/Shareholders + Board: Executive Consumers/]

    subgraph Workspace["Cursor Multi-Agent Workspace"]
        CursorMax(Cursor Max Mode + Subagents)
        Multitask(/multitask: Concurrent Agent Execution)
        Worktrees(Git Worktrees: Isolated Branch Working Dirs)
        Monorepo[(Monorepo: React Dashboard + Rust Axum Gateway)]
        RulesSkills[(Cursor Rules / Skills / Hooks / Commands)]
    end

    subgraph Governance["Governance + Sprint Planning Artifacts"]
        BranchProtect{{Branch Protection: All Changes Require PR + Checks}}
        ADRs[(ADRs: Axum over Actix + Tradeoff Records)]
        SprintPlan[(Sprint Plan + Team Charters)]
        RiskRegister[(Risk Register)]
        SystemDiagrams[(System Diagrams: Pre-Execution Alignment)]
    end

    subgraph Teams["Five Parallel Engineering Teams"]
        Alpha(Team Alpha: Wave 1 Delivery)
        Bravo(Team Bravo: Wave 1 Delivery + Release Critical Path)
        Charlie(Team Charlie: Parallel Features + Deploy Verification)
        Delta(Team Delta: Infrastructure Updates)
        Echo(Team Echo: Parallel Features)
    end

    subgraph DevSecOps["DevSecOps Pipeline + CI Gates"]
        Gitleaks(Gitleaks: Secrets Scanning)
        Semgrep(Semgrep: SAST Policies)
        Trivy(Trivy: Dependency + Filesystem CVE)
        CIGate{{CI Gate: Critical Finding Fails Workflow}}
        PRMerge{{PR Merge Gate: 96% First-Pass Success}}
    end

    subgraph IncidentLoop["Incident Response + Hardening Loop"]
        Detect(Detect: SAST Catches SQL Injection)
        Remediate(Remediate: Parallel Subagent Hotfix)
        Regress(Regression Validation)
        PostMortem[(Post-Mortem: 8-Minute MTTR Recorded)]
        Harden(Harden: Semgrep Rules + Cursor Rules Tightened)
    end

    subgraph Reporting["Executive Reporting + Continuous Improvement"]
        KPIDash[(KPI Dashboard: PRs / Review-to-Merge / Security Gate Pass / MTTR)]
        ExecSummary[(Executive Summary: Velocity + Quality + Security Posture)]
        Retro[(Sprint Retrospective: What Succeeded + What Failed)]
        Release[(25 Merged PRs: Shareholder-Ready Package)]
    end

    Director -- "configure environment" --> CursorMax
    Director -- "scaffold sprint" --> SprintPlan
    CursorMax --> Multitask
    Multitask --> Worktrees
    Worktrees --> Monorepo
    RulesSkills -. "enforces standards across" .-> CursorMax

    SprintPlan -- "aligns" --> Teams
    ADRs -. "ratifies stack choices for" .-> Monorepo
    BranchProtect -. "guards" .-> Monorepo
    RiskRegister -. "informs" .-> IncidentLoop
    SystemDiagrams -. "primes" .-> Teams

    Multitask -- "spawns" --> Alpha
    Multitask -- "spawns" --> Bravo
    Multitask -- "spawns" --> Charlie
    Multitask -- "spawns" --> Delta
    Multitask -- "spawns" --> Echo

    Alpha -- "PRs to" --> CIGate
    Bravo -- "PRs to" --> CIGate
    Charlie -- "PRs to" --> CIGate
    Delta -- "PRs to" --> CIGate
    Echo -- "PRs to" --> CIGate

    Gitleaks --> CIGate
    Semgrep --> CIGate
    Trivy --> CIGate
    CIGate -- "pass" --> PRMerge
    CIGate -- "fail: block + notify" --> Detect
    PRMerge -- "merged to main" --> Release

    Murphy -- "injected mid-sprint" --> Detect
    ZeroDay -- "all-hands drill" --> Detect
    Detect --> Remediate
    Remediate --> Regress
    Regress -- "validated" --> PRMerge
    Regress --> PostMortem
    PostMortem --> Harden
    Harden -.-> Semgrep
    Harden -.-> RulesSkills

    Release --> KPIDash
    KPIDash --> ExecSummary
    PostMortem --> Retro
    KPIDash --> Retro
    ExecSummary -- "delivered to" --> Shareholders
    Retro -. "feedback into next sprint" .-> SprintPlan

    class Monorepo,RulesSkills,ADRs,SprintPlan,RiskRegister,SystemDiagrams,PostMortem,KPIDash,ExecSummary,Retro,Release datastore
    class CursorMax,Multitask,Worktrees,Alpha,Bravo,Charlie,Delta,Echo,Gitleaks,Semgrep,Trivy,Detect,Remediate,Regress,Harden service
    class BranchProtect,CIGate,PRMerge event
    class Director,Murphy,ZeroDay,Shareholders io
```

The diagram shows the topology and data flow of the system as built. The full architectural narrative, with screenshots and prose, lives in [`documents/cursor-engineering-org.md`](./documents/cursor-engineering-org.md).

## Implementation

This system is built across **8 phases**:

1. **Leading a 25-Engineer AI Organization**
2. **Establishing Governance and Branch Protection**
3. **Producing Industry-Standard Planning Artifacts**
4. **Configuring the Engineering Culture Layer and DevSecOps Pipeline**
5. **Delivering 25 PRs Through Parallel Sprint Execution**
6. **Responding to a Murphy's Law Security Incident**
7. **Delivering a Shareholder-Ready Executive Package**
8. **💎 Secret Mission: Zero-Day CVE All-Hands Incident Response**

For the full walkthrough with screenshots and step-by-step content, see [`documents/cursor-engineering-org.md`](./documents/cursor-engineering-org.md).

## Validation

Build outcomes verified end-to-end. Each phase below is captured with screenshots, configuration, and observable behavior in [`documents/cursor-engineering-org.md`](./documents/cursor-engineering-org.md):

- ✅ Leading a 25-Engineer AI Organization
- ✅ Establishing Governance and Branch Protection
- ✅ Producing Industry-Standard Planning Artifacts
- ✅ Configuring the Engineering Culture Layer and DevSecOps Pipeline
- ✅ Delivering 25 PRs Through Parallel Sprint Execution
- ✅ Responding to a Murphy's Law Security Incident
- ✅ Delivering a Shareholder-Ready Executive Package
- ✅ 💎 Secret Mission: Zero-Day CVE All-Hands Incident Response
