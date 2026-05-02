 ---

    <div align="center">
      <img src="cover.png" alt="AI Finance Video Generator" width="600">

      <h1>AI Finance Video Generator</h1>
      <h3>Auto-Create YouTube Shorts in Minutes — Zero Experience Needed</h3>

      <p><strong>Price: $19</strong> (One-time payment, lifetime updates)</p>

      <p>
        <a href="mailto:124549483@qq.com"><strong>Contact to Purchase</strong></a>
      </p>

      <p><em>WeChat / Email: 124549483@qq.com</em></p>
    </div>

    ---
# AI Finance Video Generator
### Auto-Create YouTube Shorts in Minutes — Zero Experience Needed

Turn your finance knowledge into viral YouTube Shorts and TikTok videos with AI-powered automation. Generate professional, narrated finance videos in both **English** and **Arabic** at the click of a button.

**No API keys. No monthly fees. No video editing skills required.**

---

## What Can You Create With This?

| Video Type | Example | Audience |
|---|---|---|
| Finance Tips | "The 50-30-20 Rule Explained" | Personal finance enthusiasts |
| Crypto News | "Bitcoin Update: +10.9% Today" | Crypto traders & investors |
| Money Facts | "Top 1% Own 45% of Global Wealth" | General audience |
| Market Analysis | Stock market breakdowns | Investors & traders |
| Arabic Content | نصائح مالية بالعربية | Arabic-speaking audience (600M+) |

---

## Features

1. **One-Click Video Generation** — Run one command and get a complete 1080x1920 vertical video with AI voiceover, text overlay, and call-to-action. No editing required.

2. **Dual Language Support (EN/AR)** — Generate content in English OR Arabic with proper right-to-left text rendering and native-accent voices. Tap into the Arabic finance market (600M+ speakers).

3. **3 Content Templates** — Choose from "Market Tips," "Crypto News," and "Money Facts." Each template has professionally crafted scripts optimized for engagement and retention.

4. **Natural AI Voiceovers** — Uses Microsoft Edge's neural TTS engine (edge-tts) with crystal-clear voices. English: JennyNeural. Arabic: ZariyahNeural. No robotic sound.

5. **Fully Customizable** — Every template, script line, color, voice, and timing can be edited in plain text. No coding skills needed — just edit simple Python dictionaries.

6. **Batch Generation** — Generate 3, 6, or 50 shorts in one command. Perfect for building a content library or scheduling a month of posts in one session.

7. **No API Keys Required** — Everything is free and open-source. No OpenAI, no ElevenLabs, no monthly subscriptions. Just install and run.

8. **Professional Visual Style** — Dark theme with gold accent bars, shadowed text for readability, and "FOLLOW FOR MORE" call-to-action. Designed for maximum retention.

---

## What's Included

```
AI-Finance-Video-Generator/
  |
  |-- generate_tiktok_short.py   # Core generator - creates one video
  |-- run_shorts.py              # Batch generator - creates multiple videos
  |-- requirements.txt           # All dependencies (one command install)
  |-- setup.sh                   # One-click installer (Mac/Linux)
  |-- setup.bat                  # One-click installer (Windows)
  |
  |-- config/
  |   |-- settings.py            # All settings - colors, voices, durations
  |   |-- templates.py           # All scripts & content data - easy to edit
  |
  |-- example/
  |   |-- example_output.md      # See exactly what you'll get
  |
  |-- output/                    # Created automatically
       |-- audio/                # Voiceover .mp3 files
       |-- video/                # Final .mp4 videos + .json metadata
```

---

## System Requirements

| Requirement | Details |
|---|---|
| **Python** | 3.8 or higher (3.10+ recommended) |
| **OS** | Windows 10/11, macOS 10.15+, Ubuntu 20.04+ |
| **RAM** | 2 GB minimum (4 GB recommended for batch generation) |
| **Storage** | 500 MB for dependencies + generated videos |
| **Internet** | Required only for edge-tts voice synthesis (first run) |

### What You DON'T Need
- No API keys
- No OpenAI account
- No ElevenLabs subscription
- No cloud services
- No GPU
- No video editing software
- No design skills

---

## Quick Start Guide

### Step 1: Install Python

If you don't have Python installed:

- **Windows**: Download from [python.org](https://www.python.org/downloads/) — make sure to check **"Add Python to PATH"**
- **Mac**: `brew install python` or download from python.org
- **Linux**: `sudo apt install python3 python3-pip` (Ubuntu/Debian)

### Step 2: Download the Package

Extract the AI-Finance-Video-Generator folder to your computer.

### Step 3: Install Dependencies

**Windows:** Double-click `setup.bat` or run in Command Prompt:
```
cd AI-Finance-Video-Generator
setup.bat
```

**Mac/Linux:** Run in Terminal:
```
cd AI-Finance-Video-Generator
bash setup.sh
```

Or install manually:
```
pip install -r requirements.txt
```

### Step 4: Generate Your First Short

```
python generate_tiktok_short.py
```

That's it. Your first video will be created in `output/video/` within **30-90 seconds**.

### Step 5: Generate Multiple Shorts

```
python run_shorts.py --count 9
```

This generates 9 shorts mixing Arabic and English content. Find them all in `output/video/`.

---

## Customization Guide

### Changing Your Channel Name

In `config/settings.py`, find and edit:
```python
CHANNEL_NAME = "Your Channel Name Here"
```

### Changing Colors

Also in `config/settings.py`:
```python
DEFAULT_BG_COLOR = (15, 15, 35)    # Background (R, G, B)
ACCENT_COLOR = (255, 200, 50)       # Gold accent bars
TEXT_COLOR = (255, 255, 255)        # Text color
SHADOW_COLOR = (0, 0, 0)            # Text shadow
```

Try: `(0, 120, 60)` for a green finance theme, or `(180, 40, 40)` for urgent crypto alerts.

### Changing Voices

In `config/settings.py`:
```python
EDGE_TTS_EN_VOICE = "en-US-JennyNeural"   # English voice
EDGE_TTS_AR_VOICE = "ar-SA-ZariyahNeural" # Arabic voice
```

**Popular English voices:**
- `en-US-JennyNeural` — Female, US (recommended)
- `en-US-GuyNeural` — Male, US
- `en-GB-SoniaNeural` — Female, British
- `en-AU-NatashaNeural` — Female, Australian

**Popular Arabic voices:**
- `ar-SA-ZariyahNeural` — Female, Saudi
- `ar-EG-SalmaNeural` — Female, Egyptian

Full list: run `edge-tts --list-voices` in terminal.

### Editing Script Templates

Open `config/templates.py`. You'll see clearly commented sections for:
- **AR_SCRIPTS** — Arabic script templates
- **EN_SCRIPTS** — English script templates
- **AR_TIPS / EN_TIPS** — Finance tip content
- **AR_FACTS / EN_FACTS** — Finance facts
- **AR_COINS / EN_COINS** — Cryptocurrency data

**Example: Add a new finance tip:**
```python
EN_TIPS.append({
    "title": "Pay Yourself First",
    "body": "Before paying any bills, automatically transfer 10% of your income to savings. You'll be surprised how fast it adds up."
})
```

**Example: Add a new template type:**
```python
EN_SCRIPTS["stock_pick"] = {
    "title": "Stock of the Week: {ticker}",
    "segments": [
        "{greeting}! Here's my stock pick for this week",
        "{ticker} is a company that {description}",
        "Why I like it: {reason}",
        "Price target: ${target}",
        "Always do your own research before investing.",
        "Follow for weekly stock picks!",
    ]
}
```

### Changing Speech Speed

In `config/settings.py`:
```python
TTS_RATE_EN = "-5%"   # -5% = slightly slower for clarity
TTS_RATE_AR = "-10%"  # -15% for even slower Arabic speech
```

### Forcing a Language

```bash
# Force English
FORCE_LANG=en python generate_tiktok_short.py

# Force Arabic
FORCE_LANG=ar python generate_tiktok_short.py
```

Or set environment variable:
```bash
export FORCE_LANG=en   # Mac/Linux
set FORCE_LANG=en      # Windows
```

---

## Use Cases

### 1. Personal Finance Channel (English)
Generate daily "Quick Finance Tips" videos. Post one every day to build an audience of people looking to improve their finances. With batch generation, create a month's worth of content in 30 minutes.

### 2. Crypto News Channel
Keep your audience updated with daily crypto price movements and analysis. The built-in crypto templates cover Bitcoin, Ethereum, and Stablecoins with randomized (realistic) prices.

### 3. Arabic Finance Education
There's a massive gap in Arabic finance content on YouTube. Generate professional Arabic videos that tap into 600M+ Arabic speakers. The templates use natural financial terminology and culturally appropriate examples.

### 4. Multi-Language Strategy
Generate the same content in both English and Arabic to reach different audiences. The batch system automatically alternates languages.

### 5. Content Funnel for Courses
Use these shorts as lead magnets. The "Follow for More" CTA drives viewers to your channel. The finance tips establish your authority and lead to your paid course or consultation.

### 6. Social Media Growth
Short, valuable finance content performs exceptionally well on YouTube Shorts and TikTok. The 30-60 second format is optimized for the algorithm.

---

## FAQ

### Q: Do I need any API keys?
**No.** Everything works completely free. The text-to-speech uses Microsoft Edge's built-in TTS engine (edge-tts) which requires no API key or registration.

### Q: Is the content real market data?
The tips and facts are real financial education content. The crypto prices are randomly generated within realistic ranges for demo purposes. For real market data, you can integrate a free financial API like Yahoo Finance.

### Q: Can I use the videos commercially?
**Yes.** You own 100% of the content generated. Use it for your YouTube channel, TikTok, Instagram Reels, or any commercial purpose.

### Q: How long does each video take to generate?
Typically **30-90 seconds** per short. Batch generation adds a 3-second cooldown between videos to prevent resource contention.

### Q: Can I add background music?
Currently the generator outputs clean voiceover audio. You can easily add background music by editing the final video in any free editor (DaVinci Resolve, CapCut, etc.).

### Q: Will the voice sound robotic?
No. Microsoft Edge's neural TTS (JennyNeural, ZariyahNeural) produces natural-sounding speech with proper intonation. The difference from a human voice is barely noticeable.

### Q: Can I edit the text that appears on screen?
**Absolutely.** Every script template is in `config/templates.py`. You can add, remove, or change any line of text. The templates are just plain text files.

### Q: Does it work on Mac / Linux?
Yes! The setup.sh script handles Mac and Linux automatically. The core libraries (Pillow, MoviePy, edge-tts) are cross-platform.

### Q: I'm not a programmer. Can I still use this?
Yes. The setup is one click. Editing templates is as simple as editing a text file — just find the text you want to change and type your new text. If you can edit a Word document, you can customize this.

### Q: What if I get an error?
The scripts have built-in error handling that will tell you exactly what went wrong. Most issues are solved by running `pip install -r requirements.txt` again. For any issues, check the error message — it usually points to the solution.

### Q: Can I add more languages?
Yes. The architecture supports any language that edge-tts supports (100+ languages). Add your templates to `templates.py` and set the voice in `settings.py`.

### Q: What resolution are the videos?
1080x1920 (Full HD vertical) — optimal for YouTube Shorts, TikTok, and Instagram Reels.

---

## Technical Details

- **Video Engine**: MoviePy (FFmpeg backend)
- **Text Rendering**: Pillow (PIL) with word-wrapping
- **TTS Engine**: edge-tts (Microsoft Edge neural voices)
- **Codec**: H.264 + AAC in MP4 container
- **Frame Rate**: 24 FPS
- **Bitrate**: 4000 kbps

---

## License

This product is licensed for personal and commercial use. You may generate unlimited videos for your own channels and clients. Redistribution of the source code is not permitted.

---

* <div align="center">
      <p><strong>Ready to start? Contact: 124549483@qq.com</strong></p>
      <p><em>$19 — One-time payment — Lifetime access — Commercial use allowed</em></p>
    </div>*
