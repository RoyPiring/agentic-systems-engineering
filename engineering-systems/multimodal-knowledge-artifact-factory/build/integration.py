#!/usr/bin/env python3
"""
P04 — Resolve multimodal asset paths and optionally launch AIRI.

Paths are resolved from the engineering-system root (parent of this `build/` folder).
Set AIRI_EXECUTABLE to your AIRI binary if it is not named `airi` on PATH.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


def engineering_system_root() -> Path:
    return Path(__file__).resolve().parent.parent


def viewer_release_binary(root: Path) -> Path | None:
    release = root / "build" / "target" / "release"
    for name in ("knowledge_viewer.exe", "knowledge_viewer"):
        p = release / name
        if p.is_file():
            return p
    return None


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Map P02/P03/P04 paths and optionally launch AIRI with MKAF_* env vars."
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="Print paths and env; do not launch AIRI.",
    )
    ap.add_argument(
        "--print-env",
        action="store_true",
        help="Print suggested export-style environment variables only.",
    )
    args = ap.parse_args()

    root = engineering_system_root()
    p02 = root / "executions" / "evidence" / "p02" / "audio"
    p04 = root / "executions" / "evidence" / "p04" / "exports"
    viewer_src = root / "build" / "src" / "bin" / "knowledge_viewer.rs"
    viewer_bin = viewer_release_binary(root)

    env_export = {
        "MKAF_ROOT": str(root),
        "MKAF_P02_AUDIO": str(p02),
        "MKAF_P04_EXPORTS": str(p04),
        "MKAF_VIEWER_SOURCE": str(viewer_src),
        "MKAF_VIEWER_BINARY": str(viewer_bin) if viewer_bin else "",
    }

    if args.print_env:
        for k, v in env_export.items():
            print(f"{k}={v}")
        return 0

    print(f"engineering_system_root={root}")
    print(f"p02_audio={p02} exists={p02.is_dir()}")
    print(f"p04_exports={p04} exists={p04.is_dir()}")
    print(f"knowledge_viewer.rs={viewer_src} exists={viewer_src.is_file()}")
    print(
        f"knowledge_viewer_release={viewer_bin or '(not built; run cargo build --release --features viewer --bin knowledge_viewer)'}"
    )

    airi_exe = os.environ.get("AIRI_EXECUTABLE", "airi")
    resolved = shutil.which(airi_exe)
    if not resolved:
        print(
            f"error: AIRI not found ({airi_exe!r} not on PATH). "
            "Install AIRI or set AIRI_EXECUTABLE to the full path.",
            file=sys.stderr,
        )
        if args.dry_run:
            return 0
        return 2

    print(f"airi_executable={resolved}")

    if args.dry_run:
        print("dry-run: skipping AIRI launch")
        return 0

    env = os.environ.copy()
    env.update({k: v for k, v in env_export.items() if v})

    try:
        subprocess.run([resolved], cwd=str(root), env=env, check=False)
    except OSError as e:
        print(f"error: failed to start AIRI: {e}", file=sys.stderr)
        return 3

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
