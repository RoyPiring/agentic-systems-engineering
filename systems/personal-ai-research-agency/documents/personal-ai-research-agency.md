<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Personal AI Research Agency

**Project Link:** [View Project](https://nextwork.ai/projects/a5a18c66-7788-4fc8-8cd6-7a3bb01b16b9)

**Author:** Roy Piring Jr  
**Email:** rpiringhawaii@gmail.com

---

![Image](https://nextwork.ai/refreshed_maroon_timid_jujube/uploads/a5a18c66-7788-4fc8-8cd6-7a3bb01b16b9_96pzuph6)

## Architecting a Multi-Agent Research Firm

### Project vision and agentic approach

I verified authentication for the required CLIs: Claude, Codex, and Gemini/Antigravity. I also configured the Firecrawl MCP tool inside the Claude Code environment and completed the initial scaffold for the research agency.

I populated preflight.json with system metadata, binary status, and credit limits. That file gave the build a verified operating baseline so the research workflow could track the tools, limits, and access paths it was built on.

![Image](https://nextwork.ai/refreshed_maroon_timid_jujube/uploads/a5a18c66-7788-4fc8-8cd6-7a3bb01b16b9_dngvxflo)

### Recording live limits and binary configuration

I recorded the live state of the CLI environment before building the agency. Claude was available at claude 2.1.123, Codex was available at codex 0.136.0, Gemini was ineligible, and Antigravity was available through agy 1.0.0. I also recorded Firecrawl's live balance: 1076 credits remaining against a 1000/month cap, with the key shared with the studio build.

That mattered because the system needed to build from ground truth, not template assumptions. Gemini was a dead end in this environment, Antigravity was the working binary, and the Firecrawl balance was higher than the template expected.

I also captured the operating constraints that could break the workflow later. Everything ran in native PowerShell, not WSL. The CLIs used subscription-flat access, so no model was pinned. Firecrawl credits came from a shared pool, which meant the system had to track shared usage to avoid surprise failures and surprise spend.

## Configuring the Orchestration Environment

### Setup goals and verification strategy

I launched the Claude Code session inside the research-agency directory and confirmed that the Firecrawl MCP tools were integrated and visible in the available tools list. That gave the Director agent access to the live research toolchain.

I finalized preflight.json with the environment-specific values, including the confirmed agy binary, model information, and current Firecrawl credit status. This made the orchestration environment ready for the next build steps because the agency had a known tool state before routing any work.

![Image](https://nextwork.ai/refreshed_maroon_timid_jujube/uploads/a5a18c66-7788-4fc8-8cd6-7a3bb01b16b9_aa669402)

### Firecrawl credits and Gemini binary selection

The Gemini binary was recorded as agy for Antigravity inside gemini_binary because gemini failed authentication on the consumer AI Pro tier. That kept the system honest about which binary could be called.

Firecrawl showed 1076 credits remaining against a 1000/month cap, including bonus credits above the free cap. That value came from the live /v2/team/credit-usage API.

Both values were saved in preflight.json as verified environment facts. They replaced the tutorial placeholders that assumed gemini would work and Firecrawl would have exactly 1000 credits.

## Designing the System Before Writing Code

### Design-first philosophy and pre-artifact goals

I completed the system design phase before writing the implementation files. That kept the agency from becoming a loose set of scripts and gave the build a clear architecture before execution.

I authored four Architecture Decision Records that documented the core system choices. These covered Claude Code as the primary orchestrator, a modular MCP-based tool architecture, adversarial verification, and schema-based content fencing for security.

I also mapped the system with Mermaid diagrams to show the request routing flow and the adversarial eval harness. Then I finalized the implementation plan so the research modules could be integrated in a controlled order.

### Four ADRs and the CLAUDE.md-first build order

I wrote four ADRs to lock the major system decisions before implementation. The records covered Claude Code as the agentic orchestrator, the four research methods across Claude with MCP, Firecrawl, Gemini or agy long-context, and Codex reasoning, the content fencing strategy for prompt-injection defense, and the subscription-only cost model with quota tracking.

CLAUDE.md had to come first because it acted as the orchestration brain. It defined the Director identity, team roster, pipeline phases, and the CLI-adapter invocation contract that the rest of the build depended on.

Nothing else could be built correctly until CLAUDE.md existed. cli_adapters.py, the quota tracker, and the eval harness all depended on the interface and roles declared there.

![Image](https://nextwork.ai/refreshed_maroon_timid_jujube/uploads/a5a18c66-7788-4fc8-8cd6-7a3bb01b16b9_4qjf7ahz)

### Semantic routing in action

The system routed by capability instead of keywords. It sent SQ3, which asked which saunas were buyable at around $1,500, to Firecrawl because that task needed live market data even though the words price, current, and scrape were not in the question.

It also split same-topic sub-questions by the type of work each one required. SQ1 went to Codex because it needed evidence appraisal and reasoning. SQ2 went to agy because it needed long-context handling for full cohort papers. The topic stayed the same, but the capability need changed.

Each route included a reason. The Director explained whether the sub-question needed live data, long-context reading, or reasoning, which matched the routing behavior defined in CLAUDE.md.

## Building the Safety Layer and Deterministic Utilities

### Purpose of the CLI adapter and quota tracker

I implemented CLI adapters for Gemini and Codex with 120-second timeouts, circuit breakers, and mandatory content fencing. These controls kept external tool calls bounded and reduced the risk that fetched content could act as instructions.

I also deployed the persistent quota tracker. It stopped command dispatch once monthly credit limits were reached, which kept the agency from spending beyond its recorded limits.

I stress-tested the utilities by simulating hung processes and quota exhaustion. The system halted and reported failures back to Claude Code instead of hanging, crashing, or pretending the call succeeded.

![Image](https://nextwork.ai/refreshed_maroon_timid_jujube/uploads/a5a18c66-7788-4fc8-8cd6-7a3bb01b16b9_dakwwqg9)

### Timeout, circuit breaker, and overspend prevention

The CLI adapter enforced a 120-second timeout, which was proven live when agy hung. It also used a circuit breaker that blocked a method after 3 consecutive failures with a 60-second cooldown. Every external output was wrapped in <<<UNTRUSTED_DATA_*>>> markers so fetched text could not be treated as system instructions.

The adapter also degraded cleanly when a binary timed out, crashed, or could not launch. Instead of taking down the run, it returned an {"error": ...} dictionary that Claude Code could handle.

The quota tracker kept a persistent per-method counter in quota_state.json and checked can_dispatch() before each call. When a method reached zero, the tracker refused the call, and consume() would not decrement below zero. Together, the adapter bounded each call while the tracker prevented calls the agency could not afford.

## Running Two Case Studies Simultaneously

### Orchestrating sauna and brain research in parallel

I ran both research case studies inside the Claude Code terminal. The goal was to test whether the agency could manage parallel research work while still routing tasks by capability and verifying claims before producing final packages.

During the run, I monitored the pipeline to confirm that adversarial verification filtered ungrounded claims and identified conflicting information. That mattered because the system was built to produce decision-grade research, not just fluent summaries.

The run produced two professional research packages and saved them in the build output directories. That validated the orchestration path from question routing to final package generation.

![Image](https://nextwork.ai/refreshed_maroon_timid_jujube/uploads/a5a18c66-7788-4fc8-8cd6-7a3bb01b16b9_ikqktnoo)

### Director routing decisions explained

The Director sent live-data routes to Firecrawl. SQ3, which asked which saunas were buyable at around $1,500 now, and SQ4, which needed current specs and EMF details, both required volatile retail data that could change quickly and could be rendered through JavaScript.

The evidence routes split by capability. SQ1 went to Codex because it required reasoning over evidence quality. SQ2 and SQ5 were routed toward Gemini long-context for full-paper reading, but that path degraded to Firecrawl plus Codex because agy authentication was unconfirmed, and the gap was flagged.

The principle held across the run. Routes were chosen by the capability each sub-question demanded, such as live data, reasoning, or long-context reading. When the best method was unavailable, the Director degraded gracefully instead of faking coverage.

## Scoring Results and Establishing Regression Baselines

### Eval harness goals and baseline strategy

I built a deterministic eval harness to score research outputs against six fixed metrics with pass/fail thresholds. The purpose was to turn research quality into something repeatable and measurable.

I used the harness to score the sauna and brain capacity case studies and establish day-1 regression baselines. Those baselines gave the agency a known starting point for future changes.

I also drafted the walkthrough to document the architecture and the hardening roadmap across the 1/30/90/180-day milestones. That gave the build both a current-state explanation and a forward path for making the system stricter over time.

### Why coverage and grounding demand 100%

The eval harness measured six areas: coverage, grounding, contradiction rate, unsupported-claim rate, source freshness, and citation retrievability. Coverage measured whether each sub-question was answered or explicitly marked not found. Grounding measured whether load-bearing claims traced back to retrievable source URLs.

Coverage and grounding required a 100% bar because a research package is only decision-grade when it answers the full question and every important claim can be traced to a real source. A missed sub-question creates a silent gap, and an ungrounded claim is the exact failure the agency was built to prevent.

The other four metrics had more room. Contradiction rate and unsupported-claim rate had small tolerances, while freshness and retrievability gave context about source quality. The hard line stayed on coverage and grounding because that is where trust either holds or breaks.

## Defending Against Prompt Injection

### Red-team test results and blast-radius containment

The red-team test showed that the layered defense worked, but it also showed where the limits were. On the hostile page, content fencing wrapped the page as data, the pattern scanner flagged 3 obvious injections, and the denylist rejected fake-studies.net.

The test also proved that pattern matching was limited. A rephrased semantic injection with no trigger words passed the pattern scanner and returned scan_for_injection → [], which matched the warning in defenses.py.

The real backstop was verification, not regex. In the live sauna run, the actual injection was caught during verification when the Firecrawl upsell was refused. That confirmed the design thesis: adversarial verifiers contain the claims that earlier filters miss.

### Honest caveats and the verification backstop

Pattern matching only caught obvious attacks. scan_for_injection flagged known phrases such as ignore previous, you are now, and new instructions:, but semantic injection could still pass when hostile intent was rewritten as normal text.

Reputation checks were also only as strong as the operator-maintained lists. Unknown domains were allowed and flagged for extra verification instead of being blocked by default, so a hostile page on an unlisted domain could still pass the reputation layer.

The defense was layered, not airtight. Fencing, patterns, and reputation checks acted as cheap first filters, while verification subagents served as the primary backstop by cutting claims that lacked retrievable, reputable sources.

## Reflections and What Comes Next

### Tools and concepts mastered

The key tools I used included Claude Code for primary orchestration, Firecrawl for web scraping through MCP, and the Codex and Gemini CLIs for multi-model integration.

The main concepts I learned included semantic agent routing, multi-agent adversarial verification, secure prompt-injection defense with content fencing, and Architecture Decision Records for keeping system decisions clear through the build.

The larger lesson was that an agentic research system needs more than agents. It needs routing logic, tool limits, verification rules, source discipline, and failure handling so the final output can be trusted.

### Time investment and hardest challenges

This build took me approximately 90 minutes to complete. The work included environment verification, CLI setup, Firecrawl MCP integration, system design, adapter and quota controls, dual case-study execution, red-team testing, and baseline scoring.

The hardest part was configuring multi-agent orchestration so each research question went to the right tool for the right reason. The system had to route by capability, not keywords, and still degrade safely when an ideal tool was unavailable.

The prompt-injection defense was also a key challenge. The system had to catch hostile content without creating false positives that would break valid research, while still relying on verification as the final trust boundary.

### Personal takeaways and next learning goals

I completed this build today to learn how to architect a multi-agent research system where Claude Code acts as the Director. The Director coordinated specialized tools, routed work by semantic need, and used adversarial verification to test the quality of the final research.

The next skill I want to build is automated monitoring and cost tracking for agentic workflows. That would help the agency stay efficient and secure as the number of tools, agents, case studies, and research runs grows.

---

*Built with [NextWork](https://nextwork.ai) - [View this project](https://nextwork.ai/projects/a5a18c66-7788-4fc8-8cd6-7a3bb01b16b9)*
