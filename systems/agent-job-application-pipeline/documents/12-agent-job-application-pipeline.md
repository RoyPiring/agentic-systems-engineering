<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Build an AI Job Application Pipeline

**Project Link:** [View Project](https://learn.nextwork.org/projects/d33ab3da-82d6-4292-aa81-68a5ec51cdd6)

**Author:** Roy Piring Jr  
**Email:** rpiringhawaii@gmail.com

---

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/d33ab3da-82d6-4292-aa81-68a5ec51cdd6_7zl2bfvt)

## The Mission: Building an Unfair Advantage in a Crowded Market

### Project overview and goals

I successfully prepared the development environment required to build a multi-agent job application system by validating Node.js, Python, Git, and Obsidian, configuring the filesystem MCP server in Claude Desktop, and confirming Codex CLI authentication. This established a shared workspace where agents can access and update information stored within a centralized vault while maintaining traceability across the pipeline.

The primary objective of this project was to create a repeatable application workflow that raises consistency, reduces manual effort, and increases confidence in generated application materials. Instead of relying on a single AI model, the system uses independent validation between Claude and Codex to create a governance layer that helps identify unsupported claims before documents reach final review. This approach places evidence verification at the center of the application process and creates a structured path from job discovery to submission readiness.

### Tools and dual-model strategy

The foundation of the pipeline consists of Node.js, Python, Git, Obsidian, Claude Desktop, and Codex CLI. Obsidian serves as the knowledge repository, while the filesystem MCP connection allows agents to read and update project artifacts directly within the vault. Codex CLI was validated and connected to support independent review activities throughout the workflow.

The decision to use both Claude and Codex was based on reducing the risk of model-specific errors. Claude generates resumes, cover letters, and supporting content, while Codex performs adversarial fact-checking against available evidence. Because the models originate from different families and exhibit different failure patterns, cross-validation creates a stronger review process than self-checking alone. The result is a workflow where generated content must survive independent scrutiny before advancing through the pipeline.

## Designing the 12-Agent Architecture

### Architecture blueprint goals

This stage focused on establishing the technical foundation required to support a coordinated 12-agent system. The environment configuration, vault integration, and MCP connectivity created the infrastructure needed for agents to exchange information through a common source of truth while maintaining organized project state across multiple workflow stages.

The architecture was designed around specialization rather than generalization. Each agent performs a focused responsibility within discovery, content generation, validation, or refinement. By separating responsibilities and introducing governance checkpoints, the system reduces dependency on a single decision point. The design also supports scalability because individual agents can be refined or replaced without requiring a redesign of the entire workflow. The overall goal is predictable output quality supported by structured validation rather than blind automation.

### Why Claude + Codex CLI cross-validation

Claude is responsible for generating application content while Codex independently validates claims against supporting evidence stored in the vault. This separation creates a deliberate challenge mechanism where generated output must withstand review from a model that was not involved in creating it.

A key architectural principle is that a model cannot reliably validate its own assumptions. Self-review often shares the same reasoning path and blind spots that produced the original output. By introducing a second model family, the system gains an independent perspective capable of identifying unsupported statements, missing evidence, or inflated claims. Governance rules further strengthen the process by preventing Claude from overriding a Codex failure. Any flagged package requires manual review before it can proceed, ensuring that human oversight remains the final authority.

### Parallel vs. sequential agent execution

The dependency graph serves as the operational blueprint for the entire pipeline. It defines which activities must occur in sequence and which can execute simultaneously. Discovery activities flow through B1 and B2 before content generation begins, while synthesis agents such as resume generation, cover letter creation, and interview preparation can operate in parallel once prerequisite data is available.

The graph also separates recurring maintenance activities from application-specific workflows. Team A operates during setup and scheduled refresh cycles, while refinement functions run independently using historical metrics. Most importantly, the graph enforces quality controls through blocking rules. A failed D1 fact-check immediately halts downstream processing, preventing questionable content from reaching later stages. This dependency-driven design prioritizes accuracy and governance over raw speed.

## Auditing Roy's Professional Presence Through Three Expert Lenses

### Recruiter, Hiring Manager, and Lead Engineer perspectives

The audit process evaluated professional positioning through three separate viewpoints: recruiter, hiring manager, and lead engineer. Each perspective examined the same experience from a different decision-making angle, creating a broader understanding of how technical achievements are perceived during the hiring process.

This multi-perspective review highlights gaps that may not be visible when viewing a resume from a single lens. Recruiters focus on qualification alignment, hiring managers evaluate role fit and business value, while lead engineers assess technical depth and execution capability. Combining these viewpoints creates a more complete picture of professional positioning and provides clearer direction for future iterations. The exercise reinforced the importance of aligning technical accomplishments with the expectations of multiple stakeholders involved in hiring decisions.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/d33ab3da-82d6-4292-aa81-68a5ec51cdd6_90kget7e)

### Lowest-scoring bucket and top recommendation

The AI Leaders category received the lowest scores across all three evaluation groups. The assessment determined that the current profile demonstrates strong cloud and government-focused operational experience but provides limited visible evidence of ML infrastructure, large-scale distributed systems, or AI engineering work commonly expected by organizations in this bucket.

The most valuable recommendation was to publish the pipeline itself as a public engineering artifact. The project contains architecture decision records, dependency graphs, orchestration logic, governance controls, and dual-model validation workflows. These deliverables provide tangible evidence of system design, engineering decision-making, and AI-related implementation work. Publishing those artifacts increases visibility into capabilities that already exist but are not currently reflected in traditional resume content.

## Defining the Target: Vault Architecture and Client Identity

### Vault structure and search parameters

This phase focused on defining the organizational structure that supports pipeline operations. The vault serves as the central repository for application data, evidence, role definitions, scoring criteria, and workflow outputs. A structured layout allows agents to access information consistently while maintaining separation between source materials, generated content, and validation artifacts.

A clearly defined client identity configuration acts as the decision framework for discovery and scoring activities. By codifying preferences, exclusions, and target roles into configuration files, the system can evaluate opportunities consistently rather than relying on ad hoc decisions. This structure creates repeatability, reduces ambiguity, and ensures that future automation operates according to documented criteria rather than temporary assumptions.

### Role families and category buckets

The pipeline organizes opportunities into four target role families: Senior Cloud Engineer, Cloud Architect, Engineering Manager, and Staff Engineer. These role definitions provide focus for discovery activities and help ensure that generated application materials align with career objectives rather than chasing unrelated opportunities.

Opportunities are further grouped into four hiring buckets: AI Leaders, Big Tech, Government Contractors, and Other. Each bucket represents a different hiring environment with unique expectations and qualification standards. The configuration also includes exclusion criteria that automatically remove undesirable opportunities before they consume pipeline resources. Defining these categories early allows downstream scoring and prioritization agents to make consistent decisions based on documented rules rather than subjective interpretation.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/d33ab3da-82d6-4292-aa81-68a5ec51cdd6_st4wgzax)

### Three-channel job discovery protocol

The discovery process uses three independent channels to identify opportunities. LinkedIn browsing provides manually selected opportunities, Google Alerts surfaces role-related openings through keyword monitoring, and direct career page reviews capture positions that may not appear through other channels.

All discovery sources converge into a common intake file, creating a single entry point for downstream processing. This design simplifies orchestration because intake, scoring, and prioritization agents operate against one standardized source regardless of where opportunities originated. The approach balances manual review with structured collection methods while maintaining compliance with platform-specific limitations documented within the project architecture.

## Writing the 12-Agent Library Across Four Teams

### Agent prompts with clear input/output contracts

The pipeline is divided into four operational teams that collectively manage information extraction, opportunity discovery, application generation, and quality control. Team A transforms career history into structured claims, Team B evaluates opportunities, Team C generates tailored application materials, and Team D validates outputs before approval.

Each agent operates with defined inputs, outputs, and responsibilities. This contract-based design reduces ambiguity between workflow stages and creates predictable handoffs throughout the system. By clearly defining ownership boundaries, the architecture raises maintainability and troubleshooting while supporting future iterations. The result is a coordinated workflow where every agent contributes to a larger process without requiring awareness of the entire system.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/d33ab3da-82d6-4292-aa81-68a5ec51cdd6_ltz9tuis)

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/d33ab3da-82d6-4292-aa81-68a5ec51cdd6_t87aid6b)

### How the dependency graph prevents errors

The dependency graph acts as a governance mechanism rather than simply a scheduling tool. Content generation agents are restricted to using scored opportunities and validated source claims, ensuring that outputs remain grounded in available evidence.

Placing D1 fact-checking ahead of final quality review creates a hard checkpoint that prevents unsupported content from progressing. A failed validation immediately stops the package and requires intervention before any additional processing occurs. Because approval authority remains outside the generating model, the workflow avoids self-approval scenarios that could allow errors to propagate. This structure creates multiple opportunities to detect issues while preserving accountability throughout the process.

## Ingesting Roy's Resume and Generating Four Category Variants

### Atomic claims with evidence traceability

This stage converts resume content into atomic claims that can be individually verified and referenced. Breaking professional experience into smaller evidence-backed statements raises traceability and creates a structured foundation for future resume customization and validation activities.

The generated claims support the creation of multiple role-specific resume variants while maintaining consistency with source material. Because each statement can be traced back to supporting evidence, the pipeline gains stronger governance controls and reduces the likelihood of introducing unsupported content during customization. This approach transforms the resume from a static document into a reusable dataset that can be adapted across multiple opportunity categories while preserving factual accuracy.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/d33ab3da-82d6-4292-aa81-68a5ec51cdd6_8632jepi)

### Codex CLI fact-check results and remediation

The initial validation cycle demonstrated the value of adversarial review. Codex flagged all twelve claims that were previously marked as supported because the evidence references lacked concrete artifacts such as file paths, identifiers, URLs, or other verifiable sources.

The findings revealed an important distinction between evidence categories and evidence artifacts. Simply referencing certifications or employment documentation was insufficient without traceable supporting material. The remediation plan focused on populating the evidence repository with identifiable artifacts and refining claim wording where necessary. The exercise validated the governance model by proving that unsupported assertions could be detected before entering production workflows, reinforcing the importance of evidence-first automation.

## Building the Command-Center Dashboard

### Seven operational views for daily pipeline management

The dashboard serves as the operational interface for monitoring and managing the pipeline. Development included establishing a Next.js application with TypeScript, Tailwind CSS, Recharts, and supporting database integrations to provide visibility into pipeline activity.

The Home, Queue, and Job Detail views were prioritized to support daily operational workflows. These views provide centralized access to application status, validation outcomes, and workflow progress. The dashboard transforms backend automation into an observable system where decisions, bottlenecks, and results can be reviewed through a single interface. This visibility is essential for maintaining trust in automated processes while preserving human oversight over critical actions.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/d33ab3da-82d6-4292-aa81-68a5ec51cdd6_gk26cuqr)

### SQLite schema and activity log design

The SQLite schema was designed to capture both workflow state and historical performance. Tables store application lifecycles, evidence-backed claims, resume variants, weekly metrics, cover-letter approaches, profile updates, throughput benchmarks, and activity history.

The activity log functions as the operational audit trail for the entire platform. Every significant action performed by an agent is recorded with timestamps and contextual details, creating transparency into system behavior. This design supports troubleshooting, performance analysis, and governance reviews by providing a chronological record of pipeline activity. The audit trail also strengthens accountability by making automated decisions observable and traceable across all workflow stages.

## Wiring Gmail API for Automated Response Tracking

### OAuth setup and response classification

This phase focused on integrating external communication data into the pipeline. Gmail API connectivity introduces the ability to monitor recruiter interactions, interview requests, and rejection notices while maintaining controlled access through read-only permissions.

Automated response classification extends the pipeline beyond application generation and into outcome tracking. By categorizing incoming responses, the system can begin correlating recruiter engagement with specific resume variants, application strategies, and opportunity categories. This creates the foundation for future refinement efforts by connecting application activity with measurable hiring outcomes and feedback signals.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/d33ab3da-82d6-4292-aa81-68a5ec51cdd6_2xyvfb1l)

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/d33ab3da-82d6-4292-aa81-68a5ec51cdd6_89uxf2vk)

## Validating the Full Pipeline End-to-End

### End-to-end validation with 10 seed applications

The validation exercise tested the complete workflow using seed opportunities distributed across all target buckets. Discovery, scoring, content generation, validation, and approval stages were executed to evaluate whether the architecture functioned as intended under realistic conditions.

The exercise provided an opportunity to observe how information moved through the system and identify operational constraints before larger-scale usage. Running the full pipeline exposed workflow dependencies, validation bottlenecks, and configuration impacts that would have been difficult to identify through isolated testing. The result was a practical assessment of readiness based on actual execution rather than theoretical design assumptions.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/d33ab3da-82d6-4292-aa81-68a5ec51cdd6_pdxfbpj6)

### Fit scores and bucket assignment accuracy

The scoring engine produced a wide distribution of results, demonstrating that the qualification logic was actively differentiating opportunities based on configured criteria. Several positions qualified successfully while others were excluded because of geographic or clearance-related restrictions.

One of the more interesting observations was how company classification affected bucket assignment. Organizations with multiple business units could appear in different buckets depending on the specific role and configuration rules. The exercise highlighted the importance of maintaining accurate categorization logic because bucket placement directly influences scoring behavior, prioritization decisions, and downstream application strategies. These findings provided valuable feedback for refining configuration accuracy.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/d33ab3da-82d6-4292-aa81-68a5ec51cdd6_6k3sjevm)

### Pipeline throughput benchmark

The complete validation run processed a batch of twenty-seven URLs in approximately fifty to fifty-five minutes. Discovery, synthesis, fact-checking, and quality review each contributed to overall execution time, producing an average throughput of roughly ten to eleven minutes per qualifying application package.

The test revealed that throughput was not limited by model context size during this run. Instead, the primary constraints were qualification filtering, missing evidence artifacts, and exclusion rules. These findings are significant because they identify operational bottlenecks that can be addressed without redesigning the architecture. Understanding where time is spent allows future refinement efforts to focus on the highest-impact areas of the workflow.

## The Adversarial Council: A Self-Refining Pipeline

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/d33ab3da-82d6-4292-aa81-68a5ec51cdd6_po12jm7h)

### How Codex challenges Claude to prevent drift

The Adversarial Council introduces a structured mechanism for continuous refinement while protecting against uncontrolled drift. Claude can propose changes based on observed results, but it cannot approve those recommendations independently. Validation authority remains external to the proposing model.

Codex evaluates recommendations against multiple risk categories, including statistical validity, resume drift, content quality, bucket concentration, and claim consistency. This review process prevents the system from tuning around weak signals or introducing changes that conflict with documented evidence. During testing, the council successfully identified recommendations that violated protocol requirements and escalated them for manual review. The result is a controlled feedback loop designed to raise performance without compromising governance standards.

## Reflections and Lessons Learned

### Key tools and concepts

This project combined several technologies into a unified workflow. Node.js supported dashboard development and MCP integration, Python powered automation activities, Obsidian served as the knowledge repository, Claude Desktop orchestrated agents, and Codex CLI provided independent validation.

Beyond the tools themselves, the project reinforced several important engineering concepts. These included multi-agent architecture design, evidence-driven automation, cross-model validation, operational observability, and governance-focused workflow design. Building the pipeline demonstrated how specialized agents can collaborate through structured interfaces while maintaining traceability and accountability across complex processes. The project also highlighted the importance of treating validation as a core architectural component rather than an afterthought.

### Time investment and challenges

This project took approximately three hours to complete. The most time-consuming challenge involved configuring the filesystem MCP server and ensuring reliable connectivity between Claude Desktop and the local Obsidian vault. Establishing consistent pathing and permissions required multiple iterations before the environment behaved predictably.

Additional effort was spent troubleshooting dashboard development, particularly around integrating Recharts with SQLite-backed data sources. Ensuring that dependencies, schemas, and component mappings aligned correctly required careful testing and validation. These challenges reinforced the importance of foundational infrastructure work, as even small configuration issues can affect the reliability of larger automation systems built on top of them.

I completed this project to learn how to design an autonomous 12-agent application pipeline that combines dual-model validation with operational visibility through a custom dashboard. The next area I plan to explore is extending these patterns into additional administrative workflows, applying the same automation, governance, and validation principles to other professional productivity challenges.

---

*Built with [NextWork](https://learn.nextwork.org) - [View this project](https://learn.nextwork.org/projects/d33ab3da-82d6-4292-aa81-68a5ec51cdd6)*
