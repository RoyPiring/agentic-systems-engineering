//! P03: Dioxus desktop **Knowledge Viewer** — renders parsed sections and maps **Play Narration** to P02 stub WAVs.

use dioxus::prelude::*;
use mkaf_md_parse::{blocks_to_sections, list_p02_wavs_sorted, parse_markdown_blocks, Section};
use std::fs;
use std::path::PathBuf;
use std::sync::OnceLock;

fn loaded_content() -> (&'static [Section], &'static [PathBuf]) {
    static DATA: OnceLock<(Vec<Section>, Vec<PathBuf>)> = OnceLock::new();
    let d = DATA.get_or_init(|| {
        let root = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
        let md_path = root.join("samples/complex-sample.md");
        let markdown = fs::read_to_string(&md_path).expect("read samples/complex-sample.md");
        let blocks = parse_markdown_blocks(&markdown);
        let sections = blocks_to_sections(&blocks);
        let audio_dir = root.join("../executions/evidence/p02-audio");
        let wavs = list_p02_wavs_sorted(&audio_dir);
        (sections, wavs)
    });
    let (s, w) = d;
    (s.as_slice(), w.as_slice())
}

fn wav_for_section(wavs: &[PathBuf], index: usize) -> Option<PathBuf> {
    if wavs.is_empty() {
        return None;
    }
    wavs.get(index)
        .cloned()
        .or_else(|| wavs.first().cloned())
}

fn main() {
    let cfg = dioxus::desktop::Config::new().with_window(
        dioxus::desktop::WindowBuilder::new().with_title("Knowledge Viewer"),
    );
    dioxus::LaunchBuilder::new()
        .with_cfg(cfg)
        .launch(App);
}

#[component]
fn App() -> Element {
    let (sections, wavs) = loaded_content();

    rsx! {
        div {
            width: "100%",
            height: "100%",
            padding: "16px",
            font_family: "system-ui, sans-serif",
            background_color: "rgb(250, 250, 252)",
            color: "rgb(30, 30, 35)",
            h1 { margin_top: "0", "Knowledge Viewer" }
            p { font_size: "14px",
                "Sections from samples/complex-sample.md. Play Narration prints the chosen P02 WAV path to the terminal (section index maps to chunk order when files exist)."
            }
            if sections.is_empty() {
                p { color: "crimson", "No sections parsed — check samples/complex-sample.md." }
            }
            for (i, section) in sections.iter().cloned().enumerate() {
                SectionCard { index: i, section, wavs }
            }
        }
    }
}

#[component]
fn SectionCard(index: usize, section: Section, wavs: &'static [PathBuf]) -> Element {
    let margin_top = match section.heading_level {
        1 => "8px",
        2 => "12px",
        3 => "16px",
        _ => "20px",
    };
    let font_size = if section.heading_level <= 2 {
        "1.35rem"
    } else {
        "1.15rem"
    };
    let heading = section.heading.clone();
    let paragraphs = section.paragraphs.clone();

    rsx! {
        div {
            margin_bottom: "20px",
            padding: "12px",
            border_radius: "8px",
            background_color: "white",
            box_shadow: "0 1px 3px rgba(0,0,0,0.08)",
            div {
                display: "flex",
                flex_wrap: "wrap",
                align_items: "baseline",
                gap: "10px",
                h2 {
                    margin: "0",
                    margin_top: "{margin_top}",
                    font_size: "{font_size}",
                    "{heading}"
                }
                button {
                    padding: "6px 12px",
                    font_size: "13px",
                    cursor: "pointer",
                    border_radius: "6px",
                    border: "1px solid rgb(180, 180, 200)",
                    background_color: "rgb(240, 242, 255)",
                    onclick: move |_| {
                        let msg = match wav_for_section(wavs, index) {
                            Some(p) => format!(
                                "[Knowledge Viewer] Play Narration -> {}",
                                p.display()
                            ),
                            None => format!(
                                "[Knowledge Viewer] Play Narration: no WAV under ../executions/evidence/p02-audio/ (section {index})"
                            ),
                        };
                        println!("{msg}");
                    },
                    "Play Narration"
                }
            }
            for para in paragraphs {
                p {
                    margin: "8px 0 0 0",
                    line_height: "1.5",
                    white_space: "pre-wrap",
                    "{para}"
                }
            }
        }
    }
}
