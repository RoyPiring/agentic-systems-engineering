#!/usr/bin/env python3
"""
P02: Bridge from P01 structured stdout (H{n}: / P:) to chunked WAV artifacts.

Default backend ``stub`` writes valid mono PCM WAV using the standard library only
(no PyTorch / HF), so the pipeline runs anywhere. For Microsoft VibeVoice-TTS-1.5B,
see build/README.md — upstream removed public TTS inference code from the main repo.

Usage (from ``build/``)::

    cargo run --release -- samples/complex-sample.md | python tts_inference.py --stdin

    python tts_inference.py --from-file ../executions/evidence/p01/p01-stdout-for-p02.txt
"""

from __future__ import annotations

import argparse
import math
import re
import struct
import sys
import wave
from pathlib import Path


def parse_structured_lines(lines: list[str]) -> list[str]:
    """Extract plain utterances from P01 lines (headings and paragraphs)."""
    utterances: list[str] = []
    h_re = re.compile(r"^H\d+:\s*(.*)$")
    p_re = re.compile(r"^P:\s*(.*)$")
    for raw in lines:
        line = raw.rstrip("\n")
        m = h_re.match(line)
        if m:
            utterances.append(m.group(1).strip())
            continue
        m = p_re.match(line)
        if m:
            utterances.append(m.group(1).strip())
    return [u for u in utterances if u]


def strip_markdown_noise(text: str) -> str:
    """Remove common markdown tokens that could leak into TTS."""
    t = text
    t = re.sub(r"\*\*([^*]+)\*\*", r"\1", t)
    t = re.sub(r"`([^`]+)`", r"\1", t)
    t = re.sub(r"#+\s*", "", t)
    return re.sub(r"\s+", " ", t).strip()


def chunk_text(text: str, max_chars: int) -> list[str]:
    """Split into chunks under max_chars, preferring sentence / line boundaries."""
    text = text.strip()
    if not text:
        return []
    if len(text) <= max_chars:
        return [text]

    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        if end < len(text):
            cut = text.rfind(". ", start, end)
            if cut == -1 or cut < start + max_chars // 4:
                cut = text.rfind(" ", start, end)
            if cut > start:
                end = cut + 1
        piece = text[start:end].strip()
        if piece:
            chunks.append(piece)
        start = end
    return chunks


def write_stub_wav(path: Path, chunk_index: int, text: str) -> None:
    """Write a short sine-tone WAV; duration scales slightly with text length (demo)."""
    sample_rate = 22050
    duration = min(2.5, max(0.12, 0.08 + len(text) / 200.0))
    freq = 220 + (chunk_index % 5) * 55
    n_samples = int(sample_rate * duration)
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sample_rate)
        for i in range(n_samples):
            sample = int(32767 * 0.25 * math.sin(2 * math.pi * freq * i / sample_rate))
            w.writeframes(struct.pack("<h", sample))


def synthesize(backend: str, chunk_index: int, text: str, out_path: Path) -> None:
    if backend == "stub":
        write_stub_wav(out_path, chunk_index, text)
        return
    if backend == "vibevoice":
        raise SystemExit(
            "backend 'vibevoice' is not wired in this repo: Microsoft removed public "
            "VibeVoice-TTS inference from github.com/microsoft/VibeVoice (see README "
            "there — TTS quick try disabled). Use --backend stub for the pipeline, or "
            "integrate a supported stack (e.g. VibeVoice-Realtime docs / Colab) yourself."
        )
    raise SystemExit(f"unknown backend: {backend}")


def read_input_lines(args: argparse.Namespace) -> list[str]:
    if args.stdin and args.from_file:
        raise SystemExit("use either --stdin or --from-file, not both")
    if args.stdin:
        return sys.stdin.readlines()
    if args.from_file:
        p = Path(args.from_file)
        if not p.is_file():
            raise SystemExit(f"file not found: {p}")
        return p.read_text(encoding="utf-8", errors="replace").splitlines()
    raise SystemExit("specify --stdin or --from-file")


def main() -> None:
    ap = argparse.ArgumentParser(description="P02 TTS bridge: P01 structured text → WAV chunks.")
    ap.add_argument(
        "--stdin",
        action="store_true",
        help="read structured lines from stdin (e.g. pipe from cargo run)",
    )
    ap.add_argument(
        "--from-file",
        metavar="PATH",
        help="read structured lines from a saved transcript file",
    )
    ap.add_argument(
        "--output-dir",
        default="../executions/evidence/p02/audio",
        help="directory for p02-chunk-NNNN.wav (default: ../executions/evidence/p02/audio)",
    )
    ap.add_argument(
        "--max-chunk-chars",
        type=int,
        default=400,
        help="soft max characters per TTS chunk",
    )
    ap.add_argument(
        "--backend",
        default="stub",
        choices=("stub", "vibevoice"),
        help="stub = stdlib WAV demo; vibevoice = reserved (see error text)",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="print chunks only, do not write WAV files",
    )
    args = ap.parse_args()
    if not args.stdin and not args.from_file:
        ap.error("one of --stdin or --from-file is required")

    lines = read_input_lines(args)
    utterances = [strip_markdown_noise(u) for u in parse_structured_lines(lines)]
    all_chunks: list[str] = []
    for u in utterances:
        all_chunks.extend(chunk_text(u, args.max_chunk_chars))

    if not all_chunks:
        print("warning: no H:/P: utterances found; no WAV files written", file=sys.stderr)
        return

    out_dir = Path(args.output_dir)
    print(f"backend={args.backend} chunks={len(all_chunks)} output_dir={out_dir.resolve()}")
    for i, chunk in enumerate(all_chunks):
        preview = chunk[:72] + ("…" if len(chunk) > 72 else "")
        print(f"  chunk {i:04d} len={len(chunk)} | {preview!r}")
        if args.dry_run:
            continue
        out_path = out_dir / f"p02-chunk-{i:04d}.wav"
        synthesize(args.backend, i, chunk, out_path)
        print(f"    -> {out_path}")


if __name__ == "__main__":
    main()
