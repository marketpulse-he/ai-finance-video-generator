"""
AI Finance Video Generator - Generate YouTube Shorts
=====================================================
Creates 1080x1920 vertical finance shorts with voiceover.
Supports Arabic and English content generation.

Usage:
    python generate_tiktok_short.py

Environment variables:
    FORCE_LANG=en   or   FORCE_LANG=ar   (skip random language selection)

Output:
    - output/video/tiktok_{lang}_{timestamp}.mp4  (video file)
    - output/video/tiktok_{lang}_{timestamp}.json (metadata)
    - output/audio/tiktok_short_{timestamp}.mp3   (audio file)
"""

import json
import os
import random
import sys
import asyncio
from pathlib import Path
from datetime import datetime

# Fix Windows console encoding for Arabic text display
if sys.stdout.encoding and sys.stdout.encoding.lower() in ('gbk', 'cp936'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass  # Python < 3.7 doesn't have reconfigure

# Add parent to path so we can import config
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Import configuration
from config.settings import (
    VIDEO_RESOLUTION,
    FPS,
    DEFAULT_BG_COLOR,
    ACCENT_COLOR,
    FONT_SIZE,
    MAX_TEXT_WIDTH,
    TEXT_COLOR,
    SHADOW_COLOR,
    AUDIO_DIR,
    VIDEO_DIR,
    CHANNEL_NAME,
    TIKTOK_VIDEO_LENGTH_SECONDS,
    EDGE_TTS_EN_VOICE,
    EDGE_TTS_AR_VOICE,
    TTS_RATE_EN,
    TTS_RATE_AR,
    FORCE_LANG,
)

# Import templates and content data
from config.templates import (
    AR_SCRIPTS,
    EN_SCRIPTS,
    get_ar_content,
    get_en_content,
)

import numpy as np
from PIL import Image, ImageDraw, ImageFont


# ===== TEXT RENDERING =====

def render_text_on_frame(text: str) -> Image.Image:
    """Render a single text frame with centered text on dark background.

    Creates a 1080x1920 vertical video frame with:
    - Dark background
    - Golden accent bar at top
    - Centered white text with shadow
    - "FOLLOW FOR MORE" call-to-action bar at bottom
    """
    W, H = VIDEO_RESOLUTION
    img = Image.new("RGB", (W, H), DEFAULT_BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Load font - tries system fonts, falls back to default
    font = _load_font()

    # Draw decorative accent bar at top
    draw.rectangle([(80, 80), (W - 80, 84)], fill=ACCENT_COLOR)

    # Word-wrap text to fit screen width
    lines = _wrap_text(text, draw, font, MAX_TEXT_WIDTH)

    # Calculate vertical centering
    line_height = FONT_SIZE + 12
    total_height = len(lines) * line_height
    y_start = (H - total_height) // 2

    # Draw each line centered with shadow for readability
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font)
        w_px = bbox[2] - bbox[0]
        x = (W - w_px) // 2
        y = y_start + i * line_height
        # Shadow (offset by 2px)
        draw.text((x + 2, y + 2), line, fill=SHADOW_COLOR, font=font)
        # Main text
        draw.text((x, y), line, fill=TEXT_COLOR, font=font)

    # Draw bottom call-to-action bar
    draw.rectangle([(80, H - 120), (W - 80, H - 80)], fill=ACCENT_COLOR)
    bar_font = _load_font(font_size=40)
    draw.text(
        (W // 2, H - 105),
        "FOLLOW FOR MORE",
        fill=(0, 0, 0),
        font=bar_font,
        anchor="mm",
    )

    return img


def _load_font(font_size: int = None) -> ImageFont:
    """Try to load a system font, falling back to default."""
    size = font_size or FONT_SIZE
    font_paths = [
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/msgothic.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/System/Library/Fonts/Helvetica.ttc",  # macOS
    ]
    for fp in font_paths:
        try:
            if Path(fp).exists():
                return ImageFont.truetype(fp, size)
        except Exception:
            continue
    return ImageFont.load_default()


def _wrap_text(text: str, draw: ImageDraw, font: ImageFont, max_width: int) -> list:
    """Wrap text to fit within max_width pixels."""
    words = text.split()
    lines = []
    current_line = ""
    for w in words:
        test = current_line + " " + w if current_line else w
        bbox = draw.textbbox((0, 0), test, font=font)
        w_px = bbox[2] - bbox[0]
        if w_px < max_width:
            current_line = test
        else:
            lines.append(current_line)
            current_line = w
    if current_line:
        lines.append(current_line)
    return lines


def render_text_frames(text: str, duration_sec: float) -> list:
    """Create a sequence of video frames for a single text block."""
    total_frames = int(duration_sec * FPS)
    img = render_text_on_frame(text)
    return [np.array(img) for _ in range(total_frames)]


def format_segments(text: str, data: dict) -> str:
    """Format template text with data, gracefully handling missing keys."""
    try:
        return text.format(**data)
    except KeyError:
        return text


# ===== AUDIO GENERATION =====

async def generate_short_audio(text: str, lang: str = "en") -> str:
    """Generate narration audio using edge-tts (COMPLETELY FREE, no API key).

    Uses Microsoft Edge's neural TTS engine with over 100 voices.
    Voice list: https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support
    """
    import edge_tts

    voice = EDGE_TTS_AR_VOICE if lang == "ar" else EDGE_TTS_EN_VOICE
    rate = TTS_RATE_AR if lang == "ar" else TTS_RATE_EN
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = str(AUDIO_DIR / f"tiktok_short_{timestamp}.mp3")

    communicate = edge_tts.Communicate(
        text,
        voice,
        rate=rate,
        pitch="+0Hz",
    )
    await communicate.save(out_path)
    return out_path


# ===== MAIN GENERATION PIPELINE =====

async def main() -> str:
    """Main pipeline: generate a complete TikTok/YouTube Short video.

    Returns:
        Path to the generated .mp4 video file.

    Workflow:
        1. Select language and script template
        2. Generate content data (tips, facts, prices)
        3. Build full script text from template segments
        4. Generate audio narration via edge-tts
        5. Render text frames for each segment
        6. Combine frames + audio into MP4 video
        7. Save metadata JSON alongside video
    """
    print("=== AI Finance Video Generator ===")
    print(f"  Channel: {CHANNEL_NAME}")

    # --- Step 1: Select language ---
    if FORCE_LANG in ("ar", "en"):
        lang = FORCE_LANG
    else:
        lang = random.choices(["ar", "en"], weights=[60, 40])[0]

    script_lib = AR_SCRIPTS if lang == "ar" else EN_SCRIPTS
    data_fn = get_ar_content if lang == "ar" else get_en_content

    # --- Step 2: Pick a random script type and generate content ---
    script_type = random.choice(list(script_lib.keys()))
    template = script_lib[script_type]
    data = data_fn()

    # --- Step 3: Build full script ---
    segments_text = []
    for seg in template["segments"]:
        segments_text.append(format_segments(seg, data))

    full_text = " ".join(segments_text)
    title = format_segments(template["title"], data)

    print(f"  Language: {'Arabic' if lang == 'ar' else 'English'}")
    print(f"  Title: {title}")
    print(f"  Type: {script_type}")

    # --- Step 4: Generate audio narration ---
    print("  Generating audio with edge-tts (free, no API key)...")
    try:
        audio_path = await generate_short_audio(full_text, lang)
        print(f"  Audio saved: {audio_path}")
    except Exception as e:
        print(f"  [ERROR] Audio generation failed: {e}")
        print("  Make sure edge-tts is installed: pip install edge-tts")
        raise

    # --- Step 5: Get audio duration ---
    try:
        from moviepy import AudioFileClip

        audio_clip = AudioFileClip(audio_path)
        audio_duration = audio_clip.duration
        print(f"  Audio duration: {audio_duration:.1f}s")
    except Exception as e:
        print(f"  [ERROR] Could not read audio file: {e}")
        raise

    # Calculate display time per segment proportional to text length
    total_chars = sum(len(s) for s in segments_text)
    segment_times = []
    for seg in segments_text:
        seg_dur = max(2.5, (len(seg) / total_chars) * audio_duration)
        segment_times.append(seg_dur)

    # --- Step 6: Render all frames ---
    print("  Rendering frames...")
    all_frames = []
    for i, seg_text in enumerate(segments_text):
        seg_dur = segment_times[i]
        frames = render_text_frames(format_segments(seg_text, data), seg_dur)
        all_frames.extend(frames)

    # Pad or trim frames to exactly match audio duration
    target_frames = int(audio_duration * FPS)
    if len(all_frames) < target_frames:
        pad = [all_frames[-1]] * (target_frames - len(all_frames))
        all_frames.extend(pad)
    elif len(all_frames) > target_frames:
        all_frames = all_frames[:target_frames]

    # --- Step 7: Encode video with audio ---
    print("  Encoding video...")
    try:
        from moviepy import ImageClip, concatenate_videoclips

        clips = []
        for frame in all_frames:
            clip = ImageClip(frame, duration=1.0 / FPS)
            clips.append(clip)

        final = concatenate_videoclips(clips, method="chain")
        final = final.with_audio(audio_clip)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        lang_tag = "ar" if lang == "ar" else "en"
        output_path = str(VIDEO_DIR / f"tiktok_{lang_tag}_{timestamp}.mp4")

        final.write_videofile(
            output_path,
            fps=FPS,
            codec="libx264",
            audio_codec="aac",
            preset="medium",
            bitrate="4000k",
            threads=2,
            logger=None,
        )

        print(f"\n  ✓ Video saved: {output_path}")
        print(f"  Duration: {audio_duration:.1f}s")
        print(f"  Language: {'Arabic' if lang == 'ar' else 'English'}")
        print(f"  Title: {title}")

        # --- Step 8: Save metadata ---
        meta_path = output_path.replace(".mp4", ".json")
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "title": title,
                    "language": lang,
                    "duration": audio_duration,
                    "script_type": script_type,
                    "segments": segments_text,
                },
                f,
                ensure_ascii=False,
                indent=2,
            )

        audio_clip.close()
        return output_path

    except Exception as e:
        print(f"  [ERROR] Video encoding failed: {e}")
        raise


# ===== ENTRY POINT =====

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n  Cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n  [FATAL] {e}")
        sys.exit(1)
