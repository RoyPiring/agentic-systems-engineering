# Build an AI Memory Palace Coach

> Inside the [Agentic Systems Engineering](../../README.md) portfolio · *AI agents and orchestration that move from prompt to outcome.*

## Overview

This project builds a local Python MCP server that transforms Claude into a structured memory palace coach using the Method of Loci and FSRS-based spaced repetition.

The system is designed to move beyond passive note-taking into an active cognitive training loop. It encodes information into spatial memory structures, reinforces recall through guided sessions, and schedules reviews based on retention probability. The goal is not just storing knowledge, but improving long-term recall through a system that combines spatial anchoring, imagery, and adaptive review intervals.

The architecture is built across **8 phases**, anchored by **Building an AI Memory Coach with the Science of World Champions** on the input side and **Dresler 2017 Certification Test** at the end. Each phase is listed in the Implementation section below.

## Architecture

```mermaid
---
title: Build an AI Memory Palace Coach
---
%%{init: {"theme":"base","themeVariables": {"primaryColor":"#1B4332","primaryTextColor":"#F4D03F","primaryBorderColor":"#F4D03F","secondaryColor":"#264653","tertiaryColor":"#2F5233","lineColor":"#F4D03F","fontFamily":"ui-monospace, SFMono-Regular, Menlo, Consolas, monospace","fontSize":"13px"}}}%%
flowchart LR
    classDef datastore fill:#264653,stroke:#F4D03F,stroke-width:2px,color:#FFFFFF
    classDef service fill:#1B4332,stroke:#F4D03F,stroke-width:2px,color:#F4D03F
    classDef event fill:#7B42BC,stroke:#F4D03F,stroke-width:2px,color:#FFFFFF
    classDef io fill:#0d1117,stroke:#F4D03F,stroke-width:1.5px,color:#F4D03F,font-style:italic







    User[/User via Claude Desktop/]
    Claude(Claude Orchestrator)
    FastMCP(FastMCP Server)

    User -->|"natural language request"| Claude
    Claude <-->|"JSON-RPC over stdin/stdout"| FastMCP

    subgraph Encoding
        LociMgr(Loci Manager)
        Validator{{Dresler Loci Confirmation}}
        Encoder(Bizarre Imagery Encoder)
    end

    subgraph Retrieval
        WalkSession(Walk Session Runner)
        Grader(FSRS Recall Grader)
    end

    subgraph Reinforcement
        FSRS(FSRS Scheduler)
        StruggleFlag{{Struggle Loci Flag}}
    end

    DB[(SQLite: palaces / loci / encodings / cards / sessions)]

    FastMCP -->|"create_palace, add_loci"| LociMgr
    LociMgr -->|"validates anchors"| Validator
    Validator -->|"confirms loci"| LociMgr
    LociMgr -->|"persists palace structure"| DB

    FastMCP -->|"encode_content"| Encoder
    Encoder -->|"binds image to locus"| DB

    FastMCP -->|"start_walk_session"| WalkSession
    WalkSession -->|"retrieves encodings in spatial order"| DB
    WalkSession -->|"prompts recall"| Claude
    Claude -->|"recall attempt"| Grader
    Grader -->|"writes session log + score"| DB

    Grader -->|"feeds rating 1-4"| FSRS
    FSRS -->|"recalculates next due date"| DB
    Grader -->|"low score triggers"| StruggleFlag
    StruggleFlag -->|"prioritizes review"| FSRS

    DB -->|"get_due_reviews"| FastMCP
    FSRS -->|"targets 0.9 retention"| WalkSession

    Output[/Coached recall + retention metrics/]
    WalkSession --> Output
    class DB datastore
    class Claude,FastMCP,LociMgr,Encoder,WalkSession,Grader,FSRS service
    class Validator,StruggleFlag event
    class User,Output io
```

The diagram shows the topology and data flow of the system as built. The full architectural narrative, with screenshots and prose, lives in [`documents/ai-memory-palace-coach.md`](./documents/ai-memory-palace-coach.md).

## Implementation

This system is built across **8 phases**:

1. **Building an AI Memory Coach with the Science of World Champions**
2. **Setting Up the MCP Server Foundation**
3. **Designing the Memory Palace Database**
4. **Encoding Memories with Bizarre Imagery**
5. **Building the Coached Recall and Grading System**
6. **Integrating FSRS Spaced Repetition Scheduling**
7. **Connecting to Claude Desktop and Running a Live Session**
8. **Dresler 2017 Certification Test**

For the full walkthrough with screenshots and step-by-step content, see [`documents/ai-memory-palace-coach.md`](./documents/ai-memory-palace-coach.md).

## Validation

Each build phase below is documented in [`documents/ai-memory-palace-coach.md`](./documents/ai-memory-palace-coach.md), with screenshots, configuration, and notes as captured during the build:

- ✅ Building an AI Memory Coach with the Science of World Champions
- ✅ Setting Up the MCP Server Foundation
- ✅ Designing the Memory Palace Database
- ✅ Encoding Memories with Bizarre Imagery
- ✅ Building the Coached Recall and Grading System
- ✅ Integrating FSRS Spaced Repetition Scheduling
- ✅ Connecting to Claude Desktop and Running a Live Session
- ✅ Dresler 2017 Certification Test
