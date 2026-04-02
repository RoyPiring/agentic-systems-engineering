# Operating Requirements — Agentic Systems Engineering

## Target Operating Expectations

Every engineering system in this repository is expected to:

- Start with a documented business or mission problem
- Include an architecture with explicit tradeoffs and failure modes
- Provide a phased implementation plan with sequencing rationale
- Validate claims against expected and observed results
- Link to evidence artifacts (logs, terminal output, execution transcripts, metrics)

## Audience Requirements

| Audience | Requirement |
|---|---|
| Recruiter (30 seconds) | Role fit and technology themes visible in README |
| Hiring manager (2 minutes) | Business problem and judgment signals in business-context.md |
| Peer engineer (5 minutes) | Technical depth in architecture.md and validation.md accessible in 3 clicks |

## Publication Requirements

A system is eligible for publication when:

- [ ] All five required documents exist: README, business-context, architecture, implementation, validation
- [ ] Validation includes expected AND observed results
- [ ] At least two failure modes are documented
- [ ] No private-workspace paths or internal governance references in reader-facing portfolio text
- [ ] Claude Sonnet evidence review gate: PASS
- [ ] PR opened from feature branch with changelog entry
