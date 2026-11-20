---
name: video-render
description: Use when a Pricewhy video has script.md + package.md + rendered visuals and must become a finished, upload-ready MP4 (voice, motion graphics, music, real chapters, subtitles) — triggers "render video N", "make the final video", or step 5 of the weekly "start week N" command. Not for writing scripts, thumbnails or Shorts scripts.
---

# video-render — from script to finished MP4

One job: produce `content/<NNN>/build/final.mp4` plus its upload kit, so the user only uploads. Nothing is published by Claude.

## Steps

1. **Setup (once per machine):** `bash tools/video/setup.sh` — Kokoro TTS (Apache-2.0, commercial use allowed) + model in `~/.cache/pricewhy`. Music beds: `tools/video/music.py` (original, generated; 6 beds in `~/.cache/pricewhy/music/`, regenerate with the commands in CHANGELOG if missing).
2. **Voice:** `~/.cache/pricewhy/venv/bin/python tools/video/tts.py content/<NNN>` → `build/narration.wav` + `build/timings.json`. Channel voice: **af_heart, speed 1.0** (docs/02 §4). Never change voice between videos.
3. **Write `content/<NNN>/timeline.json`** (format below): every ¶ covered exactly once, in order; **one shot per 4–8 seconds** of narration (look at `timings.json` durations); each chapter heading in the script starts a segment with `"chapter"` and a `chapter` card.
4. **Assemble:** `python3 tools/video/assemble.py content/<NNN>` → `final.mp4`, `chapters.txt`, `description-final.txt`, `subtitles.srt`.
5. **Check:** extract 6 frames (`ffmpeg -ss <t> -i final.mp4 -frames:v 1 f.jpg`) across the video and **look at them**; loudness must be ≈ −14 LUFS (`ffmpeg -i final.mp4 -af ebur128 -f null -`). Fix the timeline/cards, re-run step 4.
6. **Deliver:** `python3 tools/export/bundle.py <scratchpad>/final --final` → send `Pricewhy-<NNN>.mp4` + `...-UPLOAD-KIT.zip` to the user in chat (SendUserFile).

## timeline.json format

```json
{
  "music": [ {"file": "bed-a-minor.wav", "from_p": 1}, {"file": "bed-d-dorian.wav", "from_p": 16} ],
  "segments": [
    { "p": [1], "chapter": "The $1.50 hot dog", "shots": [
      { "card": {"style": "stat", "value": "$1.50", "label": "...", "sub": "...", "object": "hotdog", "source": "..."} },
      { "img": "cpi-hotdog.png", "w": 2, "focus": [0.6, 0.5] }
    ]}
  ],
  "end_card": { "seconds": 12, "card": {"style": "text", "text": "Next: ...", "object": "plane"} }
}
```
- `img`: a PNG from `visuals/out/`. Shots > 9 s are split automatically into wide + close-up (close-up centres on `focus`, x/y 0–1).
- `card` styles: `chapter` (kicker, title) · `stat` (value, label, sub, tone, size) · `quote` (quote, who, size) · `text` (text, sub, tone, size) · `list` (title, rows[{left,right,tone}], left_w) · `math` (expr, sub). Optional `object` (illustration), `source` (always for numbers and quotes).
- `w`: relative duration weight inside the segment (default 1).
- `music`: change bed at the twist; never use the same pair of beds as the previous video (docs/11 rule 3).
- `end_card`: 12 s so YouTube end-screen elements fit.

## Rules

- Every number or quote on a card must exist in `research.md` and carry its `source`.
- No realistic AI images of people, places or events; only our charts, cards and flat illustrations.
- Card text ≤ 12 words for `text`, ≤ 35 words for `quote`; use the script's wording.
- Keep "AI use: Yes" in the upload settings (synthetic voice).

## Good example 1
A 26-second ¶ about membership fees → receipt step (wide), `stat` card "$5.3B · membership fees, fiscal 2025" with source, `share.png` chart (w 2, auto-split into wide + close-up). Four visual changes, every number sourced.

## Good example 2
Chapter starts → `chapter` card "CHAPTER 4 · The twist: the card in your wallet", and the music bed switches at that ¶.

## Bad example (do not do this)
One chart held for 40 seconds with no card changes, or a card saying "Costco makes almost all its money from fees" — static (viewers leave) and false (research: ~51% of operating income).
