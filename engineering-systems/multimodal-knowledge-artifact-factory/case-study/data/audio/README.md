# Narration audio (`script.md`)

These files are **spoken narration** of [`../script.md`](../script.md) using **Microsoft Edge TTS** (neural voice), not the repo’s P02 **stub** beeps.

| File | Role |
| ---- | ---- |
| `script-narration-full.mp3` | **One file** for the whole script (regenerate with `--one-file`) |
| `script-narration-part01.mp3` … | Multi-part run; play in order or use merged / M3U |
| `script-narration-merged.mp3` | Optional: `ffmpeg` concat of the parts (`--merge` or `--merge-only`) |
| `script-narration.m3u` | Playlist — open in **VLC**, etc. |

**Regenerate** (requires `pip install edge-tts`). Run from **`build/`** (engineering-system layout):

```bash
# Single MP3 (typical for this script length)
python ../case-study/tools/generate_edge_narration.py --one-file

# Or split parts + playlist (default)
python ../case-study/tools/generate_edge_narration.py

# Merge existing part01–03 into one file (needs ffmpeg on PATH)
python ../case-study/tools/generate_edge_narration.py --merge-only
```

If you run from **`case-study/tools/`** instead, use `python generate_edge_narration.py` (defaults find `../data/script.md`).

Options: `--voice en-US-JennyNeural`, `--rate +5%`, `--max-chars 2800` (multi-part only).

**Note:** Voice is **synthetic** (Edge TTS). For OpenAI TTS instead, set `OPENAI_API_KEY` and use the Codex speech CLI (`text_to_speech.py` `speak-batch`) with chunks ≤ 4096 characters.
