# Quality Standards

This document defines how completeness and credibility are evaluated for every engineering system in this repository.

## Quality Dimensions

| Dimension | Requirement |
|---|---|
| **Correctness** | Claims match what was actually built and observed |
| **Clarity** | A reviewer can understand the work in 90 seconds from the README |
| **Traceability** | Claims point to architecture decisions, validation, or evidence artifacts |
| **Reproducibility** | Another engineer can follow the implementation path with documented prerequisites |
| **Audience fit** | Works for non-technical readers AND senior technical reviewers |

## Review-Ready Criteria

A system is review-ready when:

- All required documents exist (README, business-context, architecture, implementation, validation)
- Scope, constraints, and success criteria are explicit
- Validation contains expected and observed results
- Evidence supports the strongest claims
- Links resolve correctly
- README supports 90-second orientation

## Audience Quality Gate

| Audience | Time Budget | Gate |
|---|---|---|
| Recruiter | 30 seconds | Role fit and outcomes visible |
| Hiring manager | 2 minutes | Business judgment accessible |
| Peer engineer | 5 minutes | Technical depth in 3 clicks |

## Review Checklist

- [ ] README leads with outcomes, not tools
- [ ] `Why This Matters` section exists
- [ ] `What This Proves` section exists with evidence links
- [ ] Intended audience is explicit
- [ ] Tradeoffs and failure modes are documented
- [ ] Validation includes expected and observed results
- [ ] Evidence artifacts are linked
- [ ] No broken internal links
