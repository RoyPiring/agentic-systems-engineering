<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Ship a Repo Explainer Pipeline

**Project Link:** [View Project](https://learn.nextwork.org/projects/959497e2-faed-4bca-b74e-605c22c68469)

**Author:** Roy Piring Jr  
**Email:** rpiringhawaii@gmail.com

---

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/959497e2-faed-4bca-b74e-605c22c68469_p0ugqf8z)

## Building a Nine-Agent Content Foundry

### Project vision and goals

In this project, I built a nine-agent AI orchestration pipeline that transforms a public GitHub repository into polished explainer videos and carousel decks. The objective was to simulate a production-grade content generation system where specialized agents collaborate through structured contracts instead of operating as isolated prompts.

The system combines repository analysis, storyboard generation, diagram rendering, voice synthesis, animation composition, and adversarial review into a single automated workflow. Rather than treating AI as a single assistant, the project focused on designing an orchestrated multi-agent system with typed state management, governance boundaries, and deterministic outputs.

### Setting up the tool chain

I audited the environment for all required tooling, validated runtime versions, and scaffolded the project structure before agent orchestration began.

The environment included Node.js, Rust, Docker, Mermaid CLI, Puppeteer, ffmpeg, Whisper, Azure TTS, Remotion, and Codex CLI integrations. Establishing the tool chain early ensured the pipeline could move from analysis into rendering and delivery without dependency failures during execution.

## Verifying and Installing the Full Tool Chain

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/959497e2-faed-4bca-b74e-605c22c68469_6qxqwjma)

### Why Puppeteer is a required peer dependency

Mermaid CLI depends on Puppeteer to launch headless Chromium for deterministic diagram rendering.

Installing Puppeteer separately allows version pinning and avoids uncontrolled Chromium downloads across environments. This matters in rendering pipelines because reproducibility becomes part of the output contract. Without a stable browser layer, diagrams can shift visually between runs and break downstream composition checks.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/959497e2-faed-4bca-b74e-605c22c68469_fd2q01ax)

## Designing the State Machine and JSON Contracts

### Architecting typed inter-agent contracts

I designed a six-state orchestration model that controls how agents move through the pipeline.

Each agent communicates exclusively through typed JSON contracts, creating strict boundaries between analysis, creative generation, and validation. Eighteen JSON schemas were authored to define both input and output structures for all nine agents. This prevents hidden dependencies and ensures each stage remains deterministic and independently testable.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/959497e2-faed-4bca-b74e-605c22c68469_sm5w1jwz)

### Deep dive into one agent's input/output contract

The A6 Voice Director agent consumes structured storyboard data and transforms it into SSML-driven narration payloads for Azure TTS.

Its output includes voice assignments, pacing presets, pronunciation overrides, and duration estimates. This converts raw narration text into a production-ready voice synthesis package that downstream rendering systems can consume directly.

The important architectural pattern is separation of concern: narration generation and speech synthesis preparation are isolated into their own execution boundary.

## Authoring the Nine Specialist Agent Definitions

### What each agent definition achieves

The system separates responsibilities across distillation agents, creative agents, and council agents.

Distillation agents analyze repository structure and extract meaning. Creative agents generate scripts, diagrams, motion sequences, and narration. Council agents operate as adversarial validators responsible for factual accuracy, licensing checks, and compliance enforcement before release.

This creates a layered architecture where generation and validation remain intentionally independent.

### Tool sets across distillation, creative, and council agents

Each agent receives only the tools required for its role.

Analytical agents operate with read-focused permissions, while production agents receive controlled write access for artifact generation. Governance agents are intentionally restricted to observation and validation to prevent them from silently altering outputs during review.

This least-privilege model reduces unintended state corruption and limits cross-agent drift.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/959497e2-faed-4bca-b74e-605c22c68469_nn0xjigc)

### Preventing drift with refusal rules and re-anchor instructions

I implemented refusal rules and drift re-anchor instructions to constrain agent behavior.

Refusal rules block predictable failure modes such as fabricating paths, violating output contracts, or emitting prose instead of structured JSON. Re-anchor instructions act as recovery logic, redirecting agents back to their intended scope when they begin drifting toward adjacent responsibilities or unstructured outputs.

Together these controls function as behavioral governance for autonomous agents operating inside a shared orchestration environment.

## Building the Orchestrator with Mode Routing and Error Handling

### Orchestrating parallel agent waves

I built an orchestrator that dispatches agents in parallel execution waves while managing retries, schema validation, and mode routing.

The orchestrator supports short-form, long-form, and dual-output modes while maintaining state continuity across phases. Parallel execution significantly reduced total runtime by allowing independent stages to execute concurrently instead of serially.

### Handling council agent failures gracefully

Council agents act as release gates for factual accuracy and compliance validation.

If either council agent fails schema validation, times out, or produces an invalid verdict, the orchestrator halts immediately instead of continuing in degraded mode.

This decision prioritizes release integrity over completion speed. Missing governance validation means the pipeline no longer has proof the output is safe to publish.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/959497e2-faed-4bca-b74e-605c22c68469_h5w3fc79)

### Warm-start cache reuse in both-mode

In dual-output mode, the orchestrator reuses Phase 1 distillation outputs instead of re-running identical analysis steps.

State reuse avoids recomputing repository structure, branding, and system analysis when the repository SHA remains unchanged. Only creative and rendering phases are regenerated for the second output mode.

This reduced orchestration overhead and improved overall throughput without compromising determinism.

## Assembling the Visual and Audio Pipeline

### Mermaid rendering, Azure TTS, and Remotion compositions

I built a deterministic rendering pipeline that combines Mermaid diagrams, Azure Neural TTS narration, and Remotion-based video composition.

Diagram rendering outputs PNG assets at fixed dimensions for stable rendering behavior. Azure TTS uses SSML pacing presets for narration control, while Piper acts as a fallback engine for resiliency. Remotion compositions manage sequencing, animation timing, and final frame rendering.

The system behaves more like a media build pipeline than a traditional AI workflow.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/959497e2-faed-4bca-b74e-605c22c68469_fabgpr1g)

### Why PNG over SVG for deterministic diagram output

PNG was selected because Remotion can render rasterized assets consistently across Chromium rendering sessions.

SVG introduced variability in font rendering and layout behavior between environments, which created instability in readability validation and animation sequencing. PNG locked diagrams into deterministic pixel dimensions, making them easier to validate and render reliably.

The tradeoff was larger file size, but deterministic output mattered more than scalability in a video-rendering pipeline.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/959497e2-faed-4bca-b74e-605c22c68469_3gfntsri)

## Building the Carousel and Composition Pipeline

### Carousel rendering and ffmpeg mux scripts

I created HTML-based carousel templates rendered through Playwright and combined them with ffmpeg-based composition scripts.

This allowed the pipeline to generate both short-form social content and long-form explainer videos from the same orchestration state. PowerShell bootstrap scripts validated dependencies, pinned versions, and automated environment setup for reproducible execution.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/959497e2-faed-4bca-b74e-605c22c68469_0f1ecb0m)

### Caption burn-in vs. SRT sidecar across modes

Short-form outputs burn captions directly into the rendered video to guarantee visibility on platforms that strip subtitle tracks.

Long-form outputs generate separate SRT sidecar files so captions remain toggleable and localizable without requiring re-encoding.

This separation reflects platform-specific delivery constraints instead of applying a single rendering strategy universally.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/959497e2-faed-4bca-b74e-605c22c68469_djcoezv2)

## Running the Pipeline End-to-End Against a Live Repo

### Executing the full short-mode run

I executed the orchestrator against the charmbracelet/bubbletea repository in short-mode and monitored the pipeline across all orchestration phases.

Distillation, creative generation, rendering, narration, and council review were executed through parallel waves. Final validation confirmed that all required artifacts, diagrams, videos, captions, and reports were successfully generated.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/959497e2-faed-4bca-b74e-605c22c68469_df0utp0b)

### Parallel Phase 1 dispatch and the 3-agent wave limit

Phase 1 ran A1 Repo Anatomist, A2 System Distiller, and the A4-brand slice of Visual Director in parallel because each agent depended only on the source repository, README, and documentation.

The three-agent limit was intentional. It balanced throughput against rate limits, context usage, and auditability. Running more agents at once would add orchestration overhead without guaranteed speed gains, especially when each subagent consumes context and produces outputs that must be merged back into shared state.

The limit also preserved a clean causal chain. When later council agents reviewed the output, it remained clear which upstream agent produced each artifact and how that artifact influenced the final explainer.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/959497e2-faed-4bca-b74e-605c22c68469_p0ugqf8z)

### How A8 and A9 run the adversarial council review

A8 Quality Auditor and A9 Compliance Gate operate as independent release gates.

A8 validates content quality and technical accuracy. It checks whether claims are grounded in the actual repository, whether files or APIs were hallucinated, whether diagrams are readable, whether narration matches the visuals, and whether the output uses weak AI-generated phrasing. It also performs a second-model cross-check so technical claims are not approved by a single reasoning pass.

A9 validates release safety. It checks the repository license, confirms asset and music rights, verifies brand-kit compliance, and compares generated captions against the audio transcript using speech-to-text. If the transcript and captions drift too far apart, the release is blocked.

The important design choice is that A8 and A9 can only pass or veto. They are not allowed to fix the output they review. That separation prevents the review layer from hiding its own findings and keeps quality control independent from gen

## Secret Mission: Long-Mode YouTube Explainer with Chapter Markers

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/959497e2-faed-4bca-b74e-605c22c68469_v611xa11)

### Wall-clock performance and longest phase analysis

The full long-mode pipeline completed in approximately 31 minutes end-to-end.

The largest bottleneck was the Remotion rendering phase, which processed over 15,000 frames at 1080p resolution using parallel Chromium tabs. The second-largest phase was adversarial council review, where A8 audited repository details and detected diagram readability violations before release approval.

This reinforced that rendering and governance become the dominant scaling factors in large multi-agent media systems.

## Reflections and Key Takeaways

### Tools and concepts mastered

This project combined multi-agent orchestration, Mermaid rendering, Azure Neural TTS, Remotion, ffmpeg, Whisper, and Codex CLI into a unified production pipeline.

The concepts reinforced throughout the project included orchestration state machines, typed inter-agent contracts, adversarial validation, deterministic rendering, media composition pipelines, and AI-driven workflow governance.

### Time investment and challenges

This project took approximately 90 minutes to complete. The most difficult part was optimizing the long-form rendering pipeline while maintaining deterministic output quality.

The Remotion render stage exposed the practical limits of compute-heavy orchestration workloads, especially when scaling into high-frame-count video generation.

### Looking ahead

The most important takeaway was understanding how specialized AI agents can coordinate through strict contracts instead of relying on shared conversational context.

The next area I want to improve is large-scale orchestration management and software project coordination across longer-running AI execution pipelines.

---

*Built with [NextWork](https://learn.nextwork.org) - [View this project](https://learn.nextwork.org/projects/959497e2-faed-4bca-b74e-605c22c68469)*
