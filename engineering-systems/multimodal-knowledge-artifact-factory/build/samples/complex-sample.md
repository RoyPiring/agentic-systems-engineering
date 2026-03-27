# Multimodal pipeline overview

This document exercises **multiple heading levels**, plain paragraphs, lists, and a block quote so the P01 parser can separate *structural* blocks.

## Nested topic: ingestion

Markdown is the trust boundary for local research notes. The parser should surface headings and body text without mixing adjacent sections.

### Detail level three

Short paragraph after a deep heading.

## Lists and structure

- First item with inline `code` inside a list
- Second item spanning
  continuation emphasis

> A block quote should not confuse paragraph detection when quotes contain multiple lines.

## Code block (informational)

The following fenced block is structural markdown; P01 focuses on headings and paragraphs, not code-block extraction.

```text
example = "not emitted as P in P01"
```

## Closing section

Final paragraph for smoke tests: soft breaks  
and **inline strong** should land inside one `P` when they share a paragraph.
