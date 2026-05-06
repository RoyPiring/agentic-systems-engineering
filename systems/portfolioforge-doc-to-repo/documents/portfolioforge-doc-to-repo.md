---
nextwork_uuid: 0901297f-0e99-4908-943c-3075dce7a080
original_filename: legendary-0901297f-0e99-4908-943c-3075dce7a080.md
migrated_to: agentic-systems-engineering/portfolioforge-doc-to-repo.md
migrated_at: 2026-05-04
schema: nextwork-generator
---

<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# PortfolioForge: Doc to Repo

**Project Link:** [View Project](https://learn.nextwork.org/projects/0901297f-0e99-4908-943c-3075dce7a080)

**Author:** Roy Piring Jr  
**Email:** rpiringhawaii@gmail.com

---

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/0901297f-0e99-4908-943c-3075dce7a080_oiuykjuu)

## What is PortfolioForge?

### The problem this tool solves

PortfolioForge is a Claude Code skill designed to automate the conversion of raw project documentation into structured, portfolio-ready GitHub repositories.

The problem it solves is the manual overhead of translating notes into production-quality artifacts. Instead of rewriting documentation, structuring repositories, and adding supporting files by hand, the system standardizes this process into a repeatable pipeline. It ensures consistency in structure, completeness, and signal quality across portfolio projects.

## Setting Up the Development Environment

### Environment setup goals

The environment establishes the execution layer for the entire pipeline.

Required dependencies are installed, including Copier for template scaffolding and Pydantic for structured validation. The GitHub CLI is installed and authenticated to enable repository creation and management directly from the pipeline. The project directory is scaffolded locally, creating a controlled workspace where all components operate with consistent dependencies and access to external systems.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/0901297f-0e99-4908-943c-3075dce7a080_c6sd6dwl)

### Role of each tool in the pipeline

Each tool has a defined responsibility within the system.

Copier handles repository generation by rendering structured templates into complete projects. Pydantic enforces schema validation on all inputs, ensuring that incorrect or incomplete configurations fail early. The Claude Code skill acts as the orchestrator, collecting user intent, validating inputs, and triggering repository generation through Copier. This separation ensures that generation, validation, and orchestration remain independent and composable.

## Building the NextWork Doc Parser and Tier Detector

### Parser and tier detector goals

The system introduces a parsing layer that transforms unstructured Markdown into structured data.

A Pydantic model defines the expected schema for project documents, ensuring consistent structure across inputs. Parsing functions extract relevant sections from Markdown using predefined patterns, converting raw text into structured fields. The tier detector evaluates document complexity based on file count and structure, assigning a classification that drives downstream template behavior.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/0901297f-0e99-4908-943c-3075dce7a080_yx2rerxy)

### How tier detection works

Tier classification is determined by input structure.

A single Markdown file is classified as intern-level, a directory containing two to four sequential files is classified as mid-level, and five or more files indicate a senior-level project. This classification determines the level of detail and supporting artifacts included in the generated repository.

## Designing the Copier Template Foundation

### Template foundation goals

The template system defines the structure of generated repositories.

The copier.yml file specifies required inputs and variables, ensuring that all generated content adheres to a consistent schema. The README template follows a cognitive-funnel layout, adapting its structure based on project tier while maintaining a shared foundation. Base files such as licensing, attribution, and contribution guidelines are included across all tiers to ensure completeness.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/0901297f-0e99-4908-943c-3075dce7a080_1mz3uost)

### Tier-adaptive README logic

The README adapts based on project complexity.

Intern-level repositories include only essential sections, while mid and senior tiers introduce additional signal such as CI badges, audience targeting, architecture diagrams, and decision records. This approach scales content by adding depth rather than restructuring the entire document.

## Adding Tier-Conditional Files to the Template

### Conditional content goals

The system dynamically includes files based on project tier.

Community-related files and documentation directories are introduced only for mid and senior tiers, ensuring that complexity is matched to project scope. Continuous integration workflows are also conditionally included, reinforcing quality standards where appropriate.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/0901297f-0e99-4908-943c-3075dce7a080_1j14zlfz)

### How Copier evaluates conditional filenames

File inclusion is controlled at the template level.

Copier evaluates filename conditions before rendering content, determining whether a file should exist in the final repository. If conditions are not met, the file is omitted entirely, preventing unnecessary or irrelevant artifacts from being generated.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/0901297f-0e99-4908-943c-3075dce7a080_lxrf4qcr)

## Writing the 5 Parallel Subagent Prompts

### Subagent prompt goals

The system distributes work across specialized subagents.

Each agent operates independently, focusing on a specific transformation such as structuring documentation, generating diagrams, writing decision records, or handling attribution. This separation ensures that each component produces focused, high-quality output aligned with its responsibility.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/0901297f-0e99-4908-943c-3075dce7a080_jors1c4q)

### Why independence enables parallelism

Independent agents enable concurrent execution.

Because each agent operates on a bounded scope, they can run in parallel without dependency conflicts. This reduces total execution time and limits the risk of cross-contamination between outputs. Each agent’s result maps directly to a template variable, allowing outputs to be composed without additional transformation.

## Building the Orchestrator Skill and Conformance Checker

### Orchestrator and checker goals

The orchestrator defines how the system executes end to end.

The Claude Code skill coordinates all subagents, aggregates outputs, and passes structured data into the template engine. A conformance checker evaluates the generated repository against defined quality criteria, ensuring outputs meet minimum standards before completion.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/0901297f-0e99-4908-943c-3075dce7a080_nnk21j1v)

### How the self-healing retry loop works

The system enforces quality through controlled retries.

Each generated repository is evaluated against tier-specific thresholds. If the score does not meet the required target, the system identifies failing components and selectively regenerates them. This process is bounded to prevent infinite loops, ensuring that the system either meets quality requirements or exits with a clear result.

## Running the End-to-End Forge Pipeline

### End-to-end verification goals

The pipeline is validated by executing a full document-to-repository transformation.

A sample document is processed through parsing, subagent execution, template rendering, and validation. The output is a complete repository that reflects the input document’s structure and content while meeting defined quality standards.

### Conformance score results

The generated repository meets all applicable criteria.

The system achieves a perfect score for the intern tier, confirming that required files and structure are correctly implemented. Non-applicable criteria for higher tiers are excluded from evaluation, ensuring accurate scoring.

## Secret Mission: Adding OpenSSF Scorecard, Vale, and commitlint

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/0901297f-0e99-4908-943c-3075dce7a080_2mbtseqi)

### Most impactful quality tool

OpenSSF Scorecard provides the strongest external signal.

Its output is visible directly in the repository and communicates security posture without requiring code inspection. Unlike other tools, it delivers immediate credibility to external reviewers.

## Reflections and Takeaways

### Key tools and concepts learned

This project uses Copier, Pydantic, and GitHub CLI to build a structured generation pipeline.

The core concepts include template-based repository generation, schema validation, and multi-agent orchestration. Together, these components enable a repeatable process for producing high-quality portfolio artifacts.

### Time and challenges

This project took approximately 1 hour and 30 minutes.

The primary challenge was resolving YAML indentation issues within the CI workflow and ensuring that conditional template logic produced the correct directory structure across tiers.

### Looking ahead

This project establishes a foundation for automated portfolio generation.

The next step is improving prompt engineering for multi-agent systems, focusing on increasing reliability and reducing variance across generated outputs.

---

*Built with [NextWork](https://learn.nextwork.org) - [View this project](https://learn.nextwork.org/projects/0901297f-0e99-4908-943c-3075dce7a080)*
