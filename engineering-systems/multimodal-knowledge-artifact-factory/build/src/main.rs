//! P01: read a local `.md` file, parse with pulldown-cmark, emit headings and paragraph text for downstream TTS/UI.

use pulldown_cmark::{Event, HeadingLevel, Options, Parser, Tag, TagEnd};
use std::env;
use std::fs;
use std::process;

fn main() {
    process::exit(match run() {
        Ok(()) => 0,
        Err(e) => {
            eprintln!("error: {e}");
            1
        }
    });
}

fn run() -> Result<(), String> {
    let path = env::args()
        .nth(1)
        .unwrap_or_else(|| "samples/complex-sample.md".to_string());

    let markdown =
        fs::read_to_string(&path).map_err(|e| format!("read {path}: {e}"))?;

    let parser = Parser::new_ext(&markdown, Options::empty());

    println!("--- structured extract: {path} ---\n");

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
                        println!("H{}: {text}", heading_level_no(level));
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
                        println!("P: {text}\n");
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

    Ok(())
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
