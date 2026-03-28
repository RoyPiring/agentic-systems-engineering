//! P04: export flashcards JSON + quiz markdown from parsed markdown sections.

use mkaf_md_parse::{blocks_to_sections, parse_markdown_blocks};
use serde::Serialize;
use std::env;
use std::fmt::Write as _;
use std::fs;
use std::path::PathBuf;
use std::process;

#[derive(Serialize)]
struct Flashcard {
    term: String,
    definition: String,
}

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
    let mut args = env::args().skip(1);
    let input = args
        .next()
        .unwrap_or_else(|| "samples/complex-sample.md".to_string());
    let out_dir: PathBuf = args
        .next()
        .map(PathBuf::from)
        .unwrap_or_else(|| PathBuf::from("../executions/evidence/p04-exports"));

    fs::create_dir_all(&out_dir).map_err(|e| format!("create {}: {e}", out_dir.display()))?;

    let markdown = fs::read_to_string(&input).map_err(|e| format!("read {}: {e}", input))?;
    let blocks = parse_markdown_blocks(&markdown);
    let sections = blocks_to_sections(&blocks);

    let cards: Vec<Flashcard> = sections
        .iter()
        .map(|s| Flashcard {
            term: s.heading.clone(),
            definition: s.paragraphs.join("\n\n"),
        })
        .collect();

    let json_path = out_dir.join("flashcards.json");
    let json = serde_json::to_string_pretty(&cards).map_err(|e| e.to_string())?;
    fs::write(&json_path, json).map_err(|e| format!("write {}: {e}", json_path.display()))?;

    let quiz_path = out_dir.join("quiz.md");
    let mut quiz = String::new();
    quiz.push_str("# Study quiz\n\n");
    quiz.push_str("Generated from section headings; answers are folded behind `<details>` for self-testing.\n\n");

    for (i, section) in sections.iter().enumerate() {
        writeln!(quiz, "## Question {}\n", i + 1).unwrap();
        writeln!(quiz, "**Topic:** {}\n", section.heading).unwrap();
        writeln!(
            quiz,
            "Summarize the main ideas the reader should take from this section.\n"
        )
        .unwrap();
        writeln!(quiz, "<details>").unwrap();
        writeln!(quiz, "<summary>Reveal answer</summary>\n").unwrap();
        if section.paragraphs.is_empty() {
            writeln!(quiz, "_(No paragraph body under this heading.)_").unwrap();
        } else {
            for p in &section.paragraphs {
                writeln!(quiz, "{p}\n").unwrap();
            }
        }
        writeln!(quiz, "</details>\n").unwrap();
    }

    fs::write(&quiz_path, quiz).map_err(|e| format!("write {}: {e}", quiz_path.display()))?;

    println!("wrote {}", json_path.display());
    println!("wrote {}", quiz_path.display());
    println!("sections: {}", sections.len());
    Ok(())
}
