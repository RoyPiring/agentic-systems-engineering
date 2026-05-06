<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Build a Voice-Enabled AI Tutor

**Project Link:** [View Project](https://learn.nextwork.org/projects/09722f01-6a11-410a-8927-e0095cec8f54)

**Author:** Roy Piring Jr  
**Email:** rpiringhawaii@gmail.com

---

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/09722f01-6a11-410a-8927-e0095cec8f54_r3w8n5vj)

## What I Built and Why It Matters

### Project vision and goals

The main loop orchestrates the full system.

It manages input selection, retrieval, generation, safety validation, and output delivery, acting as the control layer for the tutor.

## Setting Up the Local AI Development Environment

### Virtual environment and dependencies

The environment establishes the execution layer for all components.

A Python virtual environment isolates dependencies, while required packages and ffmpeg support audio processing. Local models are pulled and configured to ensure the system runs without external API dependency, enabling full control over performance and cost.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/09722f01-6a11-410a-8927-e0095cec8f54_rn3t8w2j)

### Pulling models with Ollama and configuring Claude Desktop

Local model orchestration is handled through Ollama.

ChromaDB is selected as the vector store due to its low setup overhead, allowing focus on retrieval logic instead of infrastructure management. This keeps the system lightweight while still demonstrating core vector search behavior.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/09722f01-6a11-410a-8927-e0095cec8f54_jw4n6h8f)

## Ingesting Curriculum Content into ChromaDB

### Generating the water cycle curriculum document

Safety is enforced through Guardrails AI validators.

These checks ensure that generated content does not include harmful language, inappropriate terms, or sensitive information.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/09722f01-6a11-410a-8927-e0095cec8f54_r4t7bx2q)

### Chunking, embedding, and storing with mxbai-embed-large

Content is split into overlapping chunks before embedding.

Overlap ensures context is preserved between segments, preventing loss of meaning during retrieval. The embedding model converts text into vectors that enable semantic search across the dataset.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/09722f01-6a11-410a-8927-e0095cec8f54_jm3qf9yk)

### Verifying retrieval with a test similarity search

Retrieval is validated through similarity queries.

Relevant chunks are returned based on semantic alignment with the question, confirming that the vector store and embeddings are functioning as expected.

## Building the RAG Retrieval Pipeline with Age-Tier Prompts

### LangChain LCEL chain with ChromaDB and qwen3:8b

The RAG pipeline forms the core reasoning system.

It retrieves relevant content, applies prompt templates based on age tier, and generates responses using a local LLM. This ensures answers are both accurate and context-aware.

### Engineering three age-tier prompt templates

Prompt templates control how responses are generated.

Each tier adjusts vocabulary, tone, and complexity while using the same retrieved content. This separates knowledge retrieval from presentation logic.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/09722f01-6a11-410a-8927-e0095cec8f54_bq7f2ynx)

### Testing the same question across all three tiers

Testing confirms that output varies appropriately by age group.

Elementary responses simplify concepts, while higher tiers introduce technical language and deeper explanations, validating that prompt design controls output effectively.

## Adding Voice Input and Output

### Whisper speech-to-text with GPU acceleration

Voice input is handled through Whisper for transcription.

This allows spoken questions to be converted into text for processing, enabling a full voice interaction loop.

### pyttsx3 text-to-speech with age-adjusted speech rates

Text-to-speech converts responses into audio output.

Speech rates are adjusted by age tier to match comprehension levels, improving usability for different audiences.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/09722f01-6a11-410a-8927-e0095cec8f54_dn5p7xwk)

### End-to-end voice loop: speak, transcribe, retrieve, read aloud

The system completes a full interaction cycle.

User input is captured, processed through retrieval and generation, then returned as spoken output, creating a continuous voice-driven experience.

## Wiring Up Guardrails AI for Student Safety

### Installing toxic language, profanity, and PII validators

Safety is enforced through Guardrails AI validators.

These checks ensure that generated content does not include harmful language, inappropriate terms, or sensitive information.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/09722f01-6a11-410a-8927-e0095cec8f54_rt4v9qbj)

### Building the safety wrapper with fallback messaging

A wrapper intercepts model output before delivery.

If content is flagged, the system returns a controlled fallback response instead of unsafe output, maintaining a safe interaction environment.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/09722f01-6a11-410a-8927-e0095cec8f54_qf3j7ypn)

### Testing guardrails with deliberate jailbreak attempts

The system is tested with adversarial prompts.

This validates whether guardrails can block unsafe or manipulated outputs before reaching the user.

## Running the Full Prototype and Evaluating Performance

### Building the complete interactive main.py loop

The main loop orchestrates the full system.

It manages input selection, retrieval, generation, safety validation, and output delivery, acting as the control layer for the tutor.

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/09722f01-6a11-410a-8927-e0095cec8f54_b9f3k7md)

### 5-question evaluation matrix: faithfulness, age-appropriateness, safety

Evaluation measures system performance across key dimensions.

Faithfulness ensures answers align with the curriculum, age-appropriateness measures clarity and tone, and safety verifies guardrail effectiveness.

### Jailbreak block rate and final evaluation summary

Guardrail performance revealed a gap.

A 0% block rate indicates that unsafe prompts were not intercepted, showing that validator configuration or integration needs improvement.

## Secret Mission: Multilingual Support in Japanese and Spanish

![Image](https://learn.nextwork.org/refreshed_maroon_timid_jujube/uploads/09722f01-6a11-410a-8927-e0095cec8f54_kw7m3xp2)

### Cross-language faithfulness and fluency comparison

The system is extended to support multiple languages.

This introduces complexity in retrieval, as the source data remains in English while responses are generated in other languages.

## Reflections and What's Next

### Key skills demonstrated

This project demonstrates integration of RAG pipelines, voice interfaces, and safety controls within a local system.

It combines retrieval, prompt engineering, and validation into a single workflow.

### Lessons learned building a fully local AI system

The main challenge was maintaining consistency across multilingual outputs and ensuring retrieval accuracy.

Local systems provide control but require careful tuning to maintain quality across components.

### How this applies to real-world education technology

This architecture can be extended into production learning systems.

It provides a foundation for adaptive education tools that combine structured content, personalization, and safety controls.

---

*Built with [NextWork](https://learn.nextwork.org) - [View this project](https://learn.nextwork.org/projects/09722f01-6a11-410a-8927-e0095cec8f54)*
