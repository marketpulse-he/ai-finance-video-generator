"""
AI Finance Video Generator - Batch Shorts Generator
====================================================
Generate multiple YouTube Shorts in one command.
Supports Arabic (ar) and English (en) content.

Usage:
    python run_shorts.py                           # Generate 3 shorts (ar, en, ar)
    python run_shorts.py --count 9                 # Generate 9 shorts
    python run_shorts.py --langs en                # Generate only English
    python run_shorts.py --langs ar                # Generate only Arabic
    python run_shorts.py --langs en,ar,en          # Custom language sequence
    python run_shorts.py --list                    # List all generated shorts

Examples:
    # Generate 5 shorts alternating Arabic and English
    python run_shorts.py --count 5 --langs ar,en

    # Generate 6 English-only shorts
    python run_shorts.py --count 6 --langs en

    # See what you've already generated
    python run_shorts.py --list
"""

import argparse
import asyncio
import json
import os
import sys
import time
from pathlib import Path
from datetime import datetime

# Add current directory to path so we can import
sys.path.insert(0, str(Path(__file__).resolve().parent))

from generate_tiktok_short import main as gen_short


def list_videos() -> None:
    """List all generated shorts with their metadata."""
    from config.settings import VIDEO_DIR

    videos = sorted(VIDEO_DIR.glob("tiktok_*.mp4"))
    if not videos:
        print("  No videos yet. Run: python run_shorts.py")
        return

    print(f"\n  Generated Shorts ({len(videos)}):")
    print(f"  {'='*60}")
    for v in videos:
        meta_path = v.with_suffix(".json")
        if meta_path.exists():
            try:
                meta = json.load(open(meta_path, "r", encoding="utf-8"))
                title = meta.get("title", "?")
                lang = meta.get("language", "?")
                dur = meta.get("duration", 0)
                lang_tag = "AR" if lang == "ar" else "EN"
                print(f"    [{lang_tag}] {v.name}")
                print(f"         {title} ({dur:.0f}s)")
            except (json.JSONDecodeError, IOError):
                print(f"    [??] {v.name} (metadata corrupt)")
        else:
            print(f"    [??] {v.name} (no metadata)")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="AI Finance Video Generator - Batch Shorts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_shorts.py                        Generate 3 shorts
  python run_shorts.py --count 9              Generate 9 shorts
  python run_shorts.py --langs en             Generate English only
  python run_shorts.py --langs ar             Generate Arabic only
  python run_shorts.py --list                 List generated videos
        """,
    )
    parser.add_argument(
        "--count",
        type=int,
        default=3,
        help="Total shorts to generate (default: 3)",
    )
    parser.add_argument(
        "--langs",
        default="ar,en,ar",
        help="Language sequence, comma separated (default: ar,en,ar)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all generated shorts with metadata",
    )

    args = parser.parse_args()

    if args.list:
        list_videos()
        return

    if args.count < 1:
        print("[ERROR] --count must be 1 or more")
        sys.exit(1)

    # Build language sequence
    langs = [l.strip() for l in args.langs.split(",") if l.strip()]
    if not langs:
        print("[ERROR] No valid languages in --langs")
        sys.exit(1)

    # Validate languages
    for l in langs:
        if l not in ("ar", "en"):
            print(f"[ERROR] Invalid language: '{l}'. Use 'ar' or 'en'.")
            sys.exit(1)

    # Repeat the language pattern to reach --count
    lang_sequence = []
    while len(lang_sequence) < args.count:
        lang_sequence.extend(langs)
    lang_sequence = lang_sequence[: args.count]

    print(f"\n{'='*60}")
    print(f"  AI Finance Video Generator - Batch Mode")
    print(f"  Generating {args.count} shorts...")
    print(f"  Sequence: {', '.join(lang_sequence)}")
    print(f"{'='*60}\n")

    paths = []
    errors = []

    for i, lang in enumerate(lang_sequence):
        print(f"\n  --- Short {i+1}/{args.count} ---")

        # Set language via environment variable (overrides random selection)
        os.environ["FORCE_LANG"] = lang

        try:
            path = asyncio.run(gen_short())
            paths.append(path)
        except Exception as e:
            error_msg = f"Short {i+1} ({lang}) failed: {e}"
            print(f"  [ERROR] {error_msg}")
            errors.append(error_msg)

        # Brief cooldown between generations to avoid resource contention
        if i < args.count - 1:
            print("  Cooling down 3s...")
            time.sleep(3)

    # Print summary
    print(f"\n{'='*60}")
    print(f"  Generation Complete!")
    print(f"  Successful: {len(paths)} / {args.count}")
    if errors:
        print(f"  Failed: {len(errors)}")
        for err in errors:
            print(f"    - {err}")
    if paths:
        print(f"\n  Output files:")
        for p in paths:
            print(f"    ✓ {p}")
    print(f"\n  Next step: Upload to YouTube Shorts or TikTok!")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
