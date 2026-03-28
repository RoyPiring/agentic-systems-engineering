//! Shared markdown → structured blocks for the P01 CLI and the P03 Dioxus viewer.

use pulldown_cmark::{Event, HeadingLevel, Options, Parser, Tag, TagEnd};
use std::fs;
use std::path::{Path, PathBuf};

/// One structural unit in document order (matches P01 stdout stream).
#[derive(Debug, Clone, PartialEq, Eq)]
pub enum Block {
    Heading { level: u8, text: String },
    Paragraph(String),
}

/// A heading and its following paragraphs until the next heading.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct Section {
    pub heading_level: u8,
    pub heading: String,
    pub paragraphs: Vec<String>,
}

fn heading_level_no(level: HeadingLevel) -> u8 {
    level as u8
}

fn take_trimmed_non_empty(buf: &mut String) -> Option<String> {
    let trimmed = buf.trim();
    if trimmed.is_empty() {
        buf.clear();
        None
    } else {
        let out = trimmed.to_string();
        buf.clear();
        Some(out)
    }
}

/// Parse markdown into `H` / `P` blocks (same order as legacy P01 stdout).
pub fn parse_markdown_blocks(markdown: &str) -> Vec<Block> {
    let parser = Parser::new_ext(markdown, Options::empty());
    let mut out = Vec::new();
    let mut capture = String::new();
    #[derive(Copy, Clone)]
    enum Focus {
        None,
        Heading(HeadingLevel),
        Paragraph,
    }
    let mut focus = Focus::None;

    for event in parser {
        match event {
            Event::Start(Tag::Heading { level, .. }) => {
                focus = Focus::Heading(level);
                capture.clear();
            }
            Event::End(TagEnd::Heading(_)) => {
                if let Focus::Heading(level) = focus {
                    if let Some(text) = take_trimmed_non_empty(&mut capture) {
                        out.push(Block::Heading {
                            level: heading_level_no(level),
                            text,
                        });
                    }
                }
                focus = Focus::None;
            }
            Event::Start(Tag::Paragraph) => {
                focus = Focus::Paragraph;
                capture.clear();
            }
            Event::End(TagEnd::Paragraph) => {
                if let Focus::Paragraph = focus {
                    if let Some(text) = take_trimmed_non_empty(&mut capture) {
                        out.push(Block::Paragraph(text));
                    }
                }
                focus = Focus::None;
            }
            Event::Text(t) => match focus {
                Focus::Heading(_) | Focus::Paragraph => capture.push_str(&t),
                Focus::None => {}
            },
            Event::Code(c) => {
                if matches!(focus, Focus::Paragraph | Focus::Heading(_)) {
                    capture.push_str(&c);
                }
            }
            Event::SoftBreak => {
                if matches!(focus, Focus::Paragraph | Focus::Heading(_)) {
                    capture.push(' ');
                }
            }
            Event::HardBreak => {
                if matches!(focus, Focus::Paragraph | Focus::Heading(_)) {
                    capture.push('\n');
                }
            }
            _ => {}
        }
    }

    out
}

/// Print blocks in P01-compatible format (for `tts_inference.py` and evidence diffs).
pub fn print_blocks_cli(blocks: &[Block], source_label: &str) {
    println!("--- structured extract: {source_label} ---\n");
    for b in blocks {
        match b {
            Block::Heading { level, text } => {
                println!("H{level}: {text}");
            }
            Block::Paragraph(p) => {
                println!("P: {p}\n");
            }
        }
    }
}

/// Group flat blocks into sections for UI rendering.
pub fn blocks_to_sections(blocks: &[Block]) -> Vec<Section> {
    let mut sections = Vec::new();
    let mut current: Option<Section> = None;

    for b in blocks {
        match b {
            Block::Heading { level, text } => {
                if let Some(s) = current.take() {
                    sections.push(s);
                }
                current = Some(Section {
                    heading_level: *level,
                    heading: text.clone(),
                    paragraphs: Vec::new(),
                });
            }
            Block::Paragraph(p) => {
                if let Some(s) = &mut current {
                    s.paragraphs.push(p.clone());
                }
            }
        }
    }
    if let Some(s) = current {
        sections.push(s);
    }
    sections
}

/// Sorted `*.wav` paths under `dir` (for P02 audio → UI mapping).
pub fn list_p02_wavs_sorted(dir: &Path) -> Vec<PathBuf> {
    let Ok(entries) = fs::read_dir(dir) else {
        return Vec::new();
    };
    let mut paths: Vec<PathBuf> = entries
        .filter_map(|e| e.ok())
        .map(|e| e.path())
        .filter(|p| p.extension().is_some_and(|x| x == "wav"))
        .filter(|p| {
            p.file_name()
                .and_then(|n| n.to_str())
                .is_some_and(|n| n.starts_with("p02-chunk-"))
        })
        .collect();
    paths.sort();
    paths
}

#[cfg(test)]
mod tests {
    use super::*;

    fn format_blocks_like_cli(blocks: &[Block], source_label: &str) -> String {
        let mut out = String::new();
        out.push_str(&format!("--- structured extract: {source_label} ---\n\n"));
        for b in blocks {
            match b {
                Block::Heading { level, text } => {
                    out.push_str(&format!("H{level}: {text}\n"));
                }
                Block::Paragraph(p) => {
                    out.push_str(&format!("P: {p}\n\n"));
                }
            }
        }
        out
    }

    #[test]
    fn structured_stdout_matches_p02_golden() {
        let md = include_str!("../samples/complex-sample.md");
        let blocks = parse_markdown_blocks(md);
        let actual = format_blocks_like_cli(&blocks, "samples/complex-sample.md");
        let golden = include_str!("../../executions/evidence/p01-stdout-for-p02.txt");
        let actual_n = actual.replace("\r\n", "\n");
        let golden_n = golden.replace("\r\n", "\n");
        assert_eq!(
            actual_n, golden_n,
            "P01 stdout shape must stay stable for P02 tts_inference.py"
        );
    }
}
