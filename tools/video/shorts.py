#!/usr/bin/env python3
"""Render vertical Shorts (1080x1920) from content/<NNN>/shorts.md — for YouTube Shorts, TikTok, Reels.

  ~/.cache/pricewhy/venv/bin/python tools/video/shorts.py content/003-costco-hot-dog [--only 1,3]

For every "## Short N" section it reads the hook text, narration, visuals (any
`name.png` from visuals/out mentioned there) and titles, then:
  voice per sentence (Kokoro, af_heart) -> exact caption timing
  one frame per caption (hook on top, chart in the middle, big caption below)
  slow push-in on every frame, quiet music bed, loudness -14 LUFS
Writes build/shorts/short-N.mp4 and shorts/short-N.txt (title + caption + publish day).
"""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

ROOT = Path(__file__).resolve().parents[2]
KDIR = Path(os.environ.get("PRICEWHY_HOME", Path.home() / ".cache/pricewhy")) / "kokoro"
MUSIC = Path.home() / ".cache/pricewhy/music"
BEDS = ["bed-g-major.wav", "bed-e-minor.wav", "bed-c-dorian.wav", "bed-f-major.wav", "bed-a-minor.wav", "bed-d-dorian.wav"]
FPS, SR = 30, 24000
LOUDNORM = "loudnorm=I=-14:TP=-1.5:LRA=11"


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"failed: {' '.join(map(str, cmd))}\n{r.stderr[-1500:]}")


def field(block, label):
    m = re.search(r"\*\*" + label + r"[^*]*:\*\*\s*(.+)", block)
    return m.group(1).strip() if m else ""


def parse(md, visuals):
    shorts = []
    for m in re.finditer(r"^## Short (\d+)[^\n]*\n(.*?)(?=^## |\Z)", md, re.S | re.M):
        num, block = int(m.group(1)), m.group(2)
        pngs = [p for p in re.findall(r"([\w.-]+\.png)", field(block, "Visuals")) if (visuals / p).exists()]
        steps = re.findall(r"([\w-]+)-step01…\d+\.png|([\w-]+)-step01\.\.\.\d+\.png", field(block, "Visuals"))
        for a, b in steps:  # "receipt-step01…06.png" means the whole reveal sequence
            base = a or b
            pngs = sorted(p.name for p in visuals.glob(f"{base}-step*.png")) + pngs
        shorts.append({
            "num": num,
            "hook": re.sub(r"[*_`]", "", field(block, "Hook text")),
            "narration": re.sub(r"[*_`]", "", field(block, "Narration")),
            "pngs": list(dict.fromkeys(pngs)),
            "title": re.sub(r"\s*\(\d+\)\s*$", "", field(block, "YouTube Shorts title")),
            "caption": field(block, "TikTok"),
            "publish": field(block, "Publish"),
        })
    return shorts


def sentences(text):
    out = []
    for part in text.split("[pause]"):
        for s in re.split(r"(?<=[.?!])\s+", part.strip()):
            if s.strip():
                out.append(s.strip())
        out.append(None)          # pause marker
    return out[:-1]


def speakable(t):
    return re.sub(r"\s+—\s+|—", ", ", t).replace("–", " to ")


def caption_chunks(sentence):
    """Split long sentences into 2 captions (time shared by length)."""
    if len(sentence) <= 70:
        return [sentence]
    mid = len(sentence) // 2
    cut = min((i for i in [sentence.rfind(",", 0, mid + 15), sentence.find(" ", mid)] if i > 0), key=lambda i: abs(i - mid))
    return [sentence[:cut + 1].strip(), sentence[cut + 1:].strip()]


def render_short(video_dir, short, k, bed, out_dir):
    work = out_dir / f"s{short['num']}"
    work.mkdir(parents=True, exist_ok=True)
    visuals = video_dir / "visuals/out"
    pngs = short["pngs"] or [p.name for p in sorted(visuals.glob("thumb-C*.png"))][:1]
    audio, frames, t = [], [], 0.0
    sent = sentences(short["narration"])
    spoken = [s for s in sent if s]
    for s in sent:
        if s is None:
            audio.append(np.zeros(int(0.6 * SR), np.float32))
            if frames:
                frames[-1]["dur"] += 0.6
            t += 0.6
            continue
        a, _ = k.create(speakable(s), voice="af_heart", speed=1.05, lang="en-us")
        audio.append(a.astype(np.float32))
        audio.append(np.zeros(int(0.15 * SR), np.float32))
        d = len(a) / SR + 0.15
        idx = spoken.index(s) if s in spoken else 0
        img = pngs[min(len(pngs) - 1, idx * len(pngs) // max(1, len(spoken)))]
        chunks = caption_chunks(s)
        total_len = sum(len(c) for c in chunks)
        for c in chunks:
            frames.append({"caption": c, "img": img, "dur": d * len(c) / total_len})
        t += d
    voice = np.concatenate(audio)
    sf.write(work / "voice.wav", voice, SR)

    items = []
    for i, f in enumerate(frames):
        items.append({"type": "vertical", "hook": short["hook"], "img": str(visuals / f["img"]),
                      "caption": f["caption"], "out": f"f{i:02d}.png"})
    (work / "frames.json").write_text(json.dumps({"items": items}), encoding="utf-8")
    run(["node", str(ROOT / "tools/render/render.mjs"), str(work / "frames.json")])

    concat = []
    for i, f in enumerate(frames):
        n = max(2, round(f["dur"] * FPS))
        z = f"1.0+0.035*on/{n - 1}" if i % 2 == 0 else f"1.035-0.035*on/{n - 1}"
        vf = f"scale=2160:3840,zoompan=z='{z}':x='(iw-iw/zoom)/2':y='(ih-ih/zoom)/2':d={n}:s=1080x1920:fps={FPS},format=yuv420p"
        clip = work / f"c{i:02d}.mp4"
        run(["ffmpeg", "-y", "-v", "error", "-i", str(work / f"f{i:02d}.png"), "-vf", vf, "-frames:v", str(n),
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-r", str(FPS), str(clip)])
        concat.append(f"file '{clip}'")
    (work / "concat.txt").write_text("\n".join(concat) + "\n")
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(work / "concat.txt"), "-c", "copy", str(work / "video.mp4")])
    dur = len(voice) / SR + 0.4
    out = out_dir / f"short-{short['num']}.mp4"
    music = MUSIC / bed
    if music.exists():
        fc = (f"[1:a]atrim=0:{dur:.2f},afade=t=out:st={max(0, dur - 1.5):.2f}:d=1.5,volume=0.07[m];"
              f"[0:a]apad=whole_dur={dur:.2f},aformat=channel_layouts=stereo[v];[v][m]amix=inputs=2:duration=first:normalize=0,{LOUDNORM}[a]")
        run(["ffmpeg", "-y", "-v", "error", "-i", str(work / "voice.wav"), "-stream_loop", "-1", "-i", str(music),
             "-i", str(work / "video.mp4"), "-filter_complex", fc, "-map", "2:v", "-map", "[a]", "-c:v", "copy",
             "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-shortest", "-movflags", "+faststart", str(out)])
    else:
        run(["ffmpeg", "-y", "-v", "error", "-i", str(work / "video.mp4"), "-i", str(work / "voice.wav"), "-map", "0:v",
             "-map", "1:a", "-af", LOUDNORM, "-c:v", "copy", "-c:a", "aac", "-shortest", str(out)])
    return out, dur


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video_dir", type=Path)
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    video_dir = a.video_dir.resolve()
    shorts = parse((video_dir / "shorts.md").read_text(encoding="utf-8"), video_dir / "visuals/out")
    if a.only:
        keep = {int(x) for x in a.only.split(",")}
        shorts = [s for s in shorts if s["num"] in keep]
    out_dir = video_dir / "build/shorts"
    out_dir.mkdir(parents=True, exist_ok=True)
    txt_dir = video_dir / "shorts"
    txt_dir.mkdir(exist_ok=True)
    k = Kokoro(str(KDIR / "model.onnx"), str(KDIR / "voices.bin"))
    for i, s in enumerate(shorts):
        out, dur = render_short(video_dir, s, k, BEDS[(s["num"] + len(video_dir.name)) % len(BEDS)], out_dir)
        (txt_dir / f"short-{s['num']}.txt").write_text(
            f"PUBLISH: {s['publish']}\nYOUTUBE SHORTS TITLE: {s['title']}\n"
            f"TIKTOK / REELS CAPTION: {s['caption']}\nRELATED VIDEO (YouTube): the long video of this folder\n"
            "AI use: Yes (synthetic voice)\n", encoding="utf-8")
        print(f"short-{s['num']}: {dur:.1f}s, {len(s['pngs'])} visuals -> {out.name}", flush=True)


if __name__ == "__main__":
    main()
