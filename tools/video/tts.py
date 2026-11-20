#!/usr/bin/env python3
"""Narration audio from a script.md (VOICE-READY section) with Kokoro TTS.

Run with the venv created by tools/video/setup.sh:
  ~/.cache/pricewhy/venv/bin/python tools/video/tts.py content/003-costco-hot-dog [--voice af_heart] [--speed 1.0]

Writes into content/<video>/build/:
  narration.wav   the whole narration (24 kHz mono)
  timings.json    [{"p": 1, "start": 0.0, "end": 14.8, "text": "...", "chapter": "HOOK"}, ...]
Pauses: "[pause]" -> 0.7 s, between paragraphs 0.35 s, before a chapter 0.9 s.
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

KDIR = Path(os.environ.get("PRICEWHY_HOME", Path.home() / ".cache/pricewhy")) / "kokoro"
PAUSE, GAP, CHAPTER_GAP = 0.7, 0.35, 0.9


def paragraphs(script: str):
    """Yield (number, text, chapter_label_or_None) from the VOICE-READY section."""
    m = re.search(r"## VOICE-READY.*?\n(.*?)(?=\n## )", script, re.S)
    if not m:
        sys.exit("No '## VOICE-READY' section found")
    chapter = None
    for line in m.group(1).splitlines():
        line = line.strip()
        head = re.match(r"^\*\*\[(.+?)\]\*\*$", line)
        if head:
            chapter = head.group(1)
            continue
        pm = re.match(r"^¶\s*(\d+)\s+(.*)$", line)
        if pm:
            yield int(pm.group(1)), pm.group(2), chapter
            chapter = None


def speakable(text: str) -> str:
    """Light clean-up so the voice reads naturally."""
    text = text.replace("**", "").replace("*", "")
    text = re.sub(r"\s+—\s+", ", ", text)        # em dash -> comma pause
    text = text.replace("—", ", ").replace("–", " to ")
    return re.sub(r"\s{2,}", " ", text).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video_dir", type=Path)
    ap.add_argument("--voice", default="af_heart")
    ap.add_argument("--speed", type=float, default=1.0)
    args = ap.parse_args()

    script = (args.video_dir / "script.md").read_text(encoding="utf-8")
    out = args.video_dir / "build"
    out.mkdir(parents=True, exist_ok=True)
    k = Kokoro(str(KDIR / "model.onnx"), str(KDIR / "voices.bin"))

    sr = 24000
    chunks, timings, t = [], [], 0.0

    def silence(sec):
        return np.zeros(int(sec * sr), dtype=np.float32)

    for i, (num, text, chapter) in enumerate(paragraphs(script)):
        if i > 0:
            gap = CHAPTER_GAP if chapter else GAP
            chunks.append(silence(gap))
            t += gap
        start = t
        parts = [p.strip() for p in text.split("[pause]")]
        for j, part in enumerate(parts):
            if j > 0:
                chunks.append(silence(PAUSE))
                t += PAUSE
            if not part:
                continue
            audio, sr_out = k.create(speakable(part), voice=args.voice, speed=args.speed, lang="en-us")
            assert sr_out == sr
            chunks.append(audio.astype(np.float32))
            t += len(audio) / sr
        timings.append({"p": num, "start": round(start, 3), "end": round(t, 3),
                        "text": text, "chapter": chapter})
        print(f"¶{num:>2}  {start:7.2f}–{t:7.2f}s")

    chunks.append(silence(0.6))
    audio = np.concatenate(chunks)
    peak = float(np.max(np.abs(audio))) or 1.0
    audio = audio / peak * 0.89                       # normalise to about -1 dBFS
    sf.write(out / "narration.wav", audio, sr)
    (out / "timings.json").write_text(json.dumps(timings, indent=1), encoding="utf-8")
    print(f"narration: {len(audio) / sr / 60:.2f} min, voice {args.voice}, speed {args.speed}")


if __name__ == "__main__":
    main()
