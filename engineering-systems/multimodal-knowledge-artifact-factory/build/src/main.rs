//! P01 CLI: read a local `.md` file, parse with pulldown-cmark, emit headings and paragraph text.

use mkaf_md_parse::{parse_markdown_blocks, print_blocks_cli};
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

    let markdown = fs::read_to_string(&path).map_err(|e| format!("read {path}: {e}"))?;
    let blocks = parse_markdown_blocks(&markdown);
    print_blocks_cli(&blocks, &path);
    Ok(())
}
