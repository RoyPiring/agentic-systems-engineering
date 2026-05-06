---
nextwork_uuid: c2b8ab27-596b-4287-82f1-756d164d2c25
original_filename: legendary-c2b8ab27-596b-4287-82f1-756d164d2c25.md
migrated_to: productivity-engineering/ai-memory-palace-coach.md
migrated_at: 2026-05-04
schema: nextwork-generator
---

<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Build an AI Memory Palace Coach

**Project Link:** [View Project](https://learn.nextwork.org/projects/c2b8ab27-596b-4287-82f1-756d164d2c25)

**Author:** Roy Piring Jr  
**Email:** rpiringhawaii@gmail.com

---

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/c2b8ab27-596b-4287-82f1-756d164d2c25_pj84at1d)

## Building an AI Memory Coach with the Science of World Champions

### Project vision and goals

This project builds a local Python MCP server that transforms Claude into a structured memory palace coach using the Method of Loci and FSRS-based spaced repetition.

The system is designed to move beyond passive note-taking into an active cognitive training loop. It encodes information into spatial memory structures, reinforces recall through guided sessions, and schedules reviews based on retention probability. The goal is not just storing knowledge, but improving long-term recall through a system that combines spatial anchoring, imagery, and adaptive review intervals.

## Setting Up the MCP Server Foundation

### Step goals

The foundation establishes a local execution layer for all memory operations.

Python is installed and verified, a virtual environment is created to isolate dependencies, and required libraries such as MCP SDK and FSRS are installed. A minimal MCP server file is created and executed to confirm that the runtime is stable before introducing state, persistence, or tool logic.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/c2b8ab27-596b-4287-82f1-756d164d2c25_wyppuxq4)

### How FastMCP and Claude Desktop communicate

FastMCP abstracts the JSON-RPC layer required for tool execution.

Claude Desktop launches the MCP server as a subprocess and communicates through stdin and stdout using structured messages. Each tool call is serialized as JSON, executed within the Python runtime, and returned as a structured response. This architecture separates orchestration from execution, allowing Claude to act as the controller while Python handles deterministic logic.

## Designing the Memory Palace Database

### Step goals

The system introduces persistence through a structured SQLite schema.

The database models palaces, loci, encodings, FSRS cards, and session logs. This schema enables the system to track spatial memory structures, associated content, review history, and recall performance over time.

### Mapping schema to memory palace concepts

The schema directly represents the Method of Loci.

The loci table defines ordered spatial anchors within a palace, each tied to a parent structure through a foreign key. These anchors form the backbone of recall, allowing encoded information to be retrieved through spatial navigation. Without this structure, the system cannot reliably map content to memory locations.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/c2b8ab27-596b-4287-82f1-756d164d2c25_vnm5lc4c)

### The Dresler protocol and loci confirmation

The system enforces validation of loci before encoding begins.

Only locations that can be clearly visualized are confirmed and used for memory encoding. This prevents weak anchors from entering the system, ensuring that downstream recall relies on stable spatial references. This aligns with the Dresler protocol, where early validation improves long-term retention quality.

## Encoding Memories with Bizarre Imagery

### Step goals

Encoding introduces the transformation layer between content and memory.

Content is mapped to confirmed loci, and each item is associated with a vivid, exaggerated mental image. Retrieval functions return encodings in spatial order, enabling guided recall sessions that follow the structure of the palace.

### The cognitive science behind sticky memories

The system leverages the brain’s preference for novelty and distinctiveness.

Bizarre imagery increases memorability by engaging multiple cognitive pathways, including visual, emotional, and spatial processing. When combined with a fixed location, this creates multiple retrieval paths, increasing the likelihood of successful recall under different conditions.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/c2b8ab27-596b-4287-82f1-756d164d2c25_ev5mk263)

## Building the Coached Recall and Grading System

### Step goals

The system introduces structured recall sessions with measurable outcomes.

Sessions track progression through loci, record recall attempts, and assign scores based on the FSRS scale. This creates a feedback loop where recall performance is quantified and stored for future scheduling decisions.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/c2b8ab27-596b-4287-82f1-756d164d2c25_q95m7xhd)

### Identifying struggle loci for priority review

The system flags weak recall points automatically.

Loci with low recall scores are identified and stored as priority review targets. This ensures that difficult items are revisited sooner, aligning review frequency with actual performance rather than fixed intervals.

## Integrating FSRS Spaced Repetition Scheduling

### Step goals

FSRS introduces adaptive scheduling based on recall performance.

Each encoding is treated as a card with a dynamic review schedule. After each recall attempt, the system recalculates the next due date, ensuring that review timing aligns with predicted retention decay.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/c2b8ab27-596b-4287-82f1-756d164d2c25_psaew7d9)

### Targeting 90% retention with the Dresler protocol

The system targets a retention probability of 0.9.

This balances review frequency with cognitive effort, ensuring that items are reviewed before they are forgotten while still requiring active recall. Adjusting this value shifts the tradeoff between workload and retention accuracy.

## Connecting to Claude Desktop and Running a Live Session

### Step goals

The system is integrated into Claude Desktop for interactive use.

The MCP server is registered, and the connection is validated. A memory palace is created, content is encoded, and a full recall session is executed to confirm that all components operate as a unified system.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/c2b8ab27-596b-4287-82f1-756d164d2c25_snng2rg1)

### How the MCP config launches the server

The configuration ensures consistent runtime execution.

Claude Desktop launches the MCP server using the virtual environment’s Python interpreter, guaranteeing that all dependencies are resolved correctly. Communication is maintained through stdin and stdout, enabling continuous interaction between Claude and the server.

## Secret Mission: Dresler 2017 Certification Test

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/c2b8ab27-596b-4287-82f1-756d164d2c25_j05j8pv1)

### Comparing recall scores to published research baselines

The results align with expected learning curves.

Initial improvements reflect skill acquisition rather than scale, indicating that encoding quality has a larger impact early in the process. However, results depend on consistent practice and full implementation of the protocol, not isolated sessions.

## Reflections and Key Takeaways

### Tools and concepts mastered

This project uses a Python MCP server, SQLite for persistence, and FSRS for adaptive scheduling.

The system combines the Method of Loci, spaced repetition, and AI-driven orchestration to create a structured cognitive training workflow that moves beyond static knowledge storage.

### Time and challenges

This project took approximately 1 hours and 30 minutes.

The main challenge was debugging syntax errors within the certification test tools, particularly ensuring that tool execution aligned with MCP expectations and returned structured outputs.

### Looking ahead

This project focuses on building a system that improves memory through structured encoding and adaptive review.

The next step is refining spaced repetition implementation and expanding the system to support larger-scale knowledge ingestion and long-term retention workflows.

---

*Built with [NextWork](https://learn.nextwork.org) - [View this project](https://learn.nextwork.org/projects/c2b8ab27-596b-4287-82f1-756d164d2c25)*
