# P02 stub WAV output

`tts_inference.py` writes **`p02-chunk-*.wav`** here by default (mono PCM, stub tones). Regenerate from **`build/`**:

```bash
cargo run --release -- samples/complex-sample.md | python tts_inference.py --stdin
```

This folder may be empty in git if `.wav` files are ignored; run the pipeline locally to populate.
