#!/usr/bin/env python3
"""
Generate MP3 narration for case-study/script.md using Microsoft Edge TTS (edge-tts).
No API key. Requires: pip install edge-tts

Outputs under case-study/data/audio/:
  --one-file     single script-narration-full.mp3 (good for ~10k char scripts)
  default        numbered parts + script-narration.m3u
  --merge        after parts, concat to script-narration-merged.mp3 via ffmpeg (if installed)
  --merge-only   concat existing script-narration-part*.mp3 without calling TTS
"""

from __future__ import annotations

import argparse
import asyncio
import re
import shutil
import subprocess
import sys
from pathlib import Path


def _strip_md_title(text: str) -> tuple[str, str]:
    """First line # title -> (title_plain, rest)."""
    lines = text.strip().splitlines()
    if not lines:
        return "", ""
    first = lines[0].strip()
    if first.startswith("#"):
        title = re.sub(r"^#+\s*", "", first).strip()
        rest = "\n".join(lines[1:]).strip()
        return title, rest
    return "", text.strip()


def _chunk_text(text: str, max_chars: int) -> list[str]:
    """Split at sentence boundaries; each chunk <= max_chars."""
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


def _ffmpeg_concat(out_dir: Path, part_paths: list[Path], merged_name: str) -> Path | None:
    """Return path to merged file, or None if ffmpeg missing / failed."""
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        print(
            "ffmpeg not found on PATH; install ffmpeg to merge MP3s, or use --one-file, or play the .m3u.",
            file=sys.stderr,
        )
        return None
    merged = out_dir / merged_name
    listing = out_dir / "_concat_list.txt"
    lines = []
    for p in part_paths:
        # Use POSIX paths for ffmpeg concat on Windows
        esc = p.resolve().as_posix().replace("'", "'\\''")
        lines.append(f"file '{esc}'")
    listing.write_text("\n".join(lines) + "\n", encoding="utf-8")
    try:
        subprocess.run(
            [
                ffmpeg,
                "-y",
                "-f",
                "concat",
                "-safe",
                "0",
                "-i",
                str(listing),
                "-c",
                "copy",
                str(merged),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"ffmpeg merge failed: {e}", file=sys.stderr)
        listing.unlink(missing_ok=True)
        return None
    listing.unlink(missing_ok=True)
    print(f"Wrote merged file {merged.name}")
    return merged


async def _speak_chunk(
    text: str, out_path: Path, voice: str, rate: str
) -> None:
    import edge_tts

    out_path.parent.mkdir(parents=True, exist_ok=True)
    comm = edge_tts.Communicate(text, voice=voice, rate=rate)
    await comm.save(str(out_path))


def _run_merge_only(out_dir: Path, merged_name: str) -> None:
    out_dir = Path(out_dir)
    part_paths = sorted(out_dir.glob("script-narration-part*.mp3"))
    if len(part_paths) < 2:
        print("Need at least two script-narration-part*.mp3 files.", file=sys.stderr)
        sys.exit(1)
    if _ffmpeg_concat(out_dir, part_paths, merged_name) is None:
        sys.exit(1)


async def _main_async(args: argparse.Namespace) -> None:
    if args.merge_only:
        _run_merge_only(Path(args.out_dir), args.merged_name)
        return

    md = Path(args.input).read_text(encoding="utf-8", errors="replace")
    title, body = _strip_md_title(md)
    if title:
        full = f"{title}. {body}"
    else:
        full = body

    max_chars = 50_000 if args.one_file else args.max_chars
    parts = _chunk_text(full, max_chars)
    if not parts:
        print("No text to speak.", file=sys.stderr)
        sys.exit(1)

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    written: list[Path] = []

    if args.one_file and len(parts) == 1:
        out_mp3 = out_dir / "script-narration-full.mp3"
        print(f"Generating single file ({len(parts[0])} chars) -> {out_mp3.name}")
        await _speak_chunk(parts[0], out_mp3, args.voice, args.rate)
        written.append(out_mp3)
        m3u = out_dir / "script-narration.m3u"
        m3u.write_text("#EXTM3U\nscript-narration-full.mp3\n", encoding="utf-8")
        print(f"Wrote {m3u.name}")
    else:
        if args.one_file and len(parts) > 1:
            print(
                f"Text splits into {len(parts)} parts at max_chars={max_chars}; "
                "raise --max-chars or omit --one-file.",
                file=sys.stderr,
            )
            sys.exit(1)
        for i, chunk in enumerate(parts, start=1):
            out_mp3 = out_dir / f"script-narration-part{i:02d}.mp3"
            print(f"Generating part {i}/{len(parts)} ({len(chunk)} chars) -> {out_mp3.name}")
            await _speak_chunk(chunk, out_mp3, args.voice, args.rate)
            written.append(out_mp3)

        m3u = out_dir / "script-narration.m3u"
        lines = ["#EXTM3U"] + [f"script-narration-part{i:02d}.mp3" for i in range(1, len(parts) + 1)]
        m3u.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"Wrote playlist {m3u.name} (open in VLC / players for full sequence).")

    if args.merge and len(written) > 1:
        _ffmpeg_concat(out_dir, written, args.merged_name)


def main() -> None:
    p = argparse.ArgumentParser(description="Edge TTS narration for script.md")
    p.add_argument(
        "--input",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "data" / "script.md",
    )
    p.add_argument(
        "--out-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "data" / "audio",
    )
    p.add_argument(
        "--voice",
        default="en-US-GuyNeural",
        help="edge-tts voice name (try en-US-JennyNeural, en-GB-SoniaNeural, …)",
    )
    p.add_argument("--rate", default="+0%", help="e.g. +10% or -5%")
    p.add_argument("--max-chars", type=int, default=2800, help="max chars per MP3 part (ignored if --one-file)")
    p.add_argument(
        "--one-file",
        action="store_true",
        help="single script-narration-full.mp3 (use for scripts under ~10k chars)",
    )
    p.add_argument(
        "--merge",
        action="store_true",
        help="after generating multiple parts, merge to one MP3 via ffmpeg -c copy",
    )
    p.add_argument(
        "--merge-only",
        action="store_true",
        help="only run ffmpeg on existing script-narration-part*.mp3 (no TTS)",
    )
    p.add_argument(
        "--merged-name",
        default="script-narration-merged.mp3",
        dest="merged_name",
        help="output filename for --merge / --merge-only",
    )
    args = p.parse_args()
    asyncio.run(_main_async(args))


if __name__ == "__main__":
    main()
