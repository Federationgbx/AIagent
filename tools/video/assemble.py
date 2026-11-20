#!/usr/bin/env python3
"""Assemble a finished, upload-ready long video from narration + timeline.

  python3 tools/video/assemble.py content/003-costco-hot-dog

Needs (made by tools/video/tts.py):  build/narration.wav, build/timings.json
Needs (written per video):           timeline.json  (format: .claude/skills/video-render/SKILL.md)
Writes into build/:
  final.mp4                1920x1080, 30 fps, H.264 + AAC, ready to upload
  chapters.txt             real chapter timestamps for the description
  description-final.txt    package.md description with the real chapters
  subtitles.srt            captions to upload in YouTube Studio
Every shot gets a slow push-in/pull-out (Ken Burns) so nothing on screen is static;
shots longer than SPLIT seconds are cut into a wide + close-up pair automatically.
"""
import json
import math
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MUSIC_DIRS = [ROOT / "tools/video/music", Path.home() / ".cache/pricewhy/music"]
FPS, W, H = 30, 1920, 1080
SPLIT = 9.0          # seconds: longer image shots become wide + close-up
MUSIC_VOL = 0.07     # music bed level under the voice (~ -23 dB)
LOUDNORM = "loudnorm=I=-14:TP=-1.5:LRA=11"  # YouTube plays at about -14 LUFS


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"command failed: {' '.join(map(str, cmd))}\n{r.stderr[-2000:]}")
    return r.stdout


def fmt_ts(t, srt=False):
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    if srt:
        return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s % 1) * 1000)) % 1000:03d}"
    return f"{int(h)}:{int(m):02d}:{int(s):02d}" if h else f"{int(m)}:{int(s):02d}"


def audio_len(path):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                      "-of", "default=nw=1:nk=1", str(path)]).strip())


def plan_shots(segments, timings, audio_end):
    """Turn timeline segments into a flat list of shots with durations."""
    start_of = {t["p"]: t["start"] for t in timings}
    covered = [p for s in segments for p in s["p"]]
    missing = sorted(set(start_of) - set(covered))
    dupes = sorted({p for p in covered if covered.count(p) > 1})
    if missing or dupes:
        sys.exit(f"timeline.json must cover every ¶ exactly once. missing={missing} duplicated={dupes}")
    starts = [start_of[s["p"][0]] for s in segments]
    if starts != sorted(starts):
        sys.exit("timeline segments must be in ¶ order")
    shots, chapters = [], []
    for i, seg in enumerate(segments):
        t0 = 0.0 if i == 0 else starts[i]
        t1 = starts[i + 1] if i + 1 < len(segments) else audio_end
        if seg.get("chapter"):
            chapters.append((t0, seg["chapter"]))
        weights = [s.get("w", 1) for s in seg["shots"]]
        total = sum(weights)
        for shot, w in zip(seg["shots"], weights):
            d = (t1 - t0) * w / total
            if "img" in shot and d > SPLIT and not shot.get("nosplit"):
                n = math.ceil(d / 7.0)
                for k in range(n):
                    shots.append({**shot, "dur": d / n, "close": k % 2 == 1})
            else:
                shots.append({**shot, "dur": d, "close": False})
    return shots, chapters


def render_cards(shots, end_card, build, video_dir):
    cards = [s for s in shots if "card" in s] + ([end_card] if end_card else [])
    if not cards:
        return
    items = []
    for i, s in enumerate(cards):
        s["img_path"] = build / "cards" / f"card{i:03d}.png"
        items.append({"type": "card", **s["card"], "out": f"cards/card{i:03d}.png"})
    spec = build / "cards.json"
    spec.write_text(json.dumps({"items": items}, indent=1), encoding="utf-8")
    run(["node", str(ROOT / "tools/render/render.mjs"), str(spec)])


def render_shot(shot, idx, out):
    frames = max(2, round(shot["dur"] * FPS))
    fx, fy = shot.get("focus", [0.5, 0.5])
    if shot["close"]:
        z0, z1 = 1.10, 1.16   # gentle: keeps chart titles and labels on screen
    elif "card" in shot:
        z0, z1 = (1.0, 1.035) if idx % 2 == 0 else (1.035, 1.0)
    else:
        z0, z1 = (1.0, 1.07) if idx % 2 == 0 else (1.07, 1.0)
        fx, fy = (0.5, 0.5) if not shot.get("focus") else (fx, fy)
    z = f"{z0}+({z1}-{z0})*on/{frames - 1}"
    vf = (f"scale={W * 2}:{H * 2},zoompan=z='{z}':x='(iw-iw/zoom)*{fx}':y='(ih-ih/zoom)*{fy}'"
          f":d={frames}:s={W}x{H}:fps={FPS},format=yuv420p")
    run(["ffmpeg", "-y", "-v", "error", "-i", str(shot["img_path"]), "-vf", vf, "-frames:v", str(frames),
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-r", str(FPS), str(out)])
    return frames


def find_music(name):
    for d in MUSIC_DIRS:
        p = d / name
        if p.exists():
            return p
    return None


def build_audio(timeline, timings, narration, total, build):
    """Narration padded to the video length + optional music bed per section."""
    out = build / "mix.m4a"
    tracks = [m for m in timeline.get("music", []) if find_music(m["file"])]
    if not tracks:
        run(["ffmpeg", "-y", "-v", "error", "-i", str(narration), "-af", f"apad=whole_dur={total},{LOUDNORM}",
             "-c:a", "aac", "-b:a", "192k", str(out)])
        return out, False
    start_of = {t["p"]: t["start"] for t in timings}
    inputs, filters, labels = ["-i", str(narration)], [], []
    for i, m in enumerate(tracks):
        a = 0.0 if i == 0 else start_of[m["from_p"]]
        b = start_of[tracks[i + 1]["from_p"]] if i + 1 < len(tracks) else total
        d = b - a
        inputs += ["-stream_loop", "-1", "-i", str(find_music(m["file"]))]
        filters.append(f"[{i + 1}:a]atrim=0:{d:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=1.5,"
                       f"afade=t=out:st={max(0, d - 2):.3f}:d=2,volume={MUSIC_VOL},"
                       f"adelay={int(a * 1000)}|{int(a * 1000)}[m{i}]")
        labels.append(f"[m{i}]")
    filters.append(f"[0:a]apad=whole_dur={total},aformat=channel_layouts=stereo[v]")
    filters.append(f"[v]{''.join(labels)}amix=inputs={len(labels) + 1}:duration=first:normalize=0,{LOUDNORM}[a]")
    run(["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex", ";".join(filters), "-map", "[a]",
         "-t", f"{total:.3f}", "-ar", "48000", "-c:a", "aac", "-b:a", "192k", str(out)])
    return out, True


def caption_chunks(text, limit=84, min_len=24):
    """Sentence-aware captions: long sentences split into balanced parts,
    tiny fragments (e.g. "paid.") merged into a neighbour so nothing flashes."""
    pieces = [p.strip() for p in re.split(r"(?<=[.?!])\s+|\[pause\]", text) if p.strip()]
    chunks = []
    for p in pieces:
        words = p.split()
        n = max(1, math.ceil(len(p) / limit))
        target = len(p) / n
        cur = ""
        for w in words:
            if cur and len(cur) + len(w) + 1 > target and len(chunks) < 10_000 and n > 1 and len(cur) >= target * 0.8:
                chunks.append(cur)
                cur = w
            else:
                cur = f"{cur} {w}".strip()
        if cur:
            chunks.append(cur)
    merged = []
    for c in chunks:
        if merged and (len(c) < min_len or len(merged[-1]) < min_len) and len(merged[-1]) + len(c) + 1 <= limit + 30:
            merged[-1] = f"{merged[-1]} {c}"
        else:
            merged.append(c)
    return merged


def write_srt(timings, path):
    lines, n = [], 1
    for t in timings:
        text = re.sub(r"\s+", " ", t["text"].replace("**", "")).strip()
        chunks = caption_chunks(text)
        total_chars = sum(len(c) for c in chunks) or 1
        cur_t = t["start"]
        for c in chunks:
            d = (t["end"] - t["start"]) * len(c) / total_chars
            lines += [str(n), f"{fmt_ts(cur_t, True)} --> {fmt_ts(cur_t + d, True)}", c, ""]
            n += 1
            cur_t += d
    path.write_text("\n".join(lines), encoding="utf-8")


def final_description(video_dir, chapters):
    pkg = (video_dir / "package.md").read_text(encoding="utf-8")
    m = re.search(r"## Description.*?```\n(.*?)```", pkg, re.S)
    if not m:
        return None
    desc = m.group(1)
    block = "CHAPTERS\n" + "\n".join(f"{fmt_ts(t)} {name}" for t, name in chapters) + "\n"
    return re.sub(r"CHAPTERS\n(?:\d[^\n]*\n)+", block, desc)


def main():
    video_dir = Path(sys.argv[1]).resolve()
    build = video_dir / "build"
    if "--srt-only" in sys.argv:  # captions only, no re-render
        write_srt(json.loads((build / "timings.json").read_text(encoding="utf-8")), build / "subtitles.srt")
        print("subtitles.srt rewritten")
        return
    timeline = json.loads((video_dir / "timeline.json").read_text(encoding="utf-8"))
    timings = json.loads((build / "timings.json").read_text(encoding="utf-8"))
    narration = build / "narration.wav"
    speech_end = audio_len(narration)

    shots, chapters = plan_shots(timeline["segments"], timings, speech_end)
    end_card = None
    if timeline.get("end_card"):
        end_card = {"card": timeline["end_card"]["card"], "dur": timeline["end_card"].get("seconds", 12),
                    "close": False}
    for s in shots:
        if "img" in s:
            s["img_path"] = video_dir / "visuals/out" / s["img"]
            if not s["img_path"].exists():
                sys.exit(f"missing image: {s['img_path']}")
    render_cards(shots, end_card, build, video_dir)
    all_shots = shots + ([end_card] if end_card else [])

    shot_dir = build / "shots"
    shutil.rmtree(shot_dir, ignore_errors=True)
    shot_dir.mkdir(parents=True)
    concat, frames_total = [], 0
    for i, s in enumerate(all_shots):
        f = shot_dir / f"s{i:03d}.mp4"
        frames_total += render_shot(s, i, f)
        concat.append(f"file '{f}'")
        print(f"shot {i + 1}/{len(all_shots)}  {s['dur']:5.1f}s  {s.get('img') or s['card'].get('style')}", flush=True)
    (build / "concat.txt").write_text("\n".join(concat) + "\n", encoding="utf-8")
    total = frames_total / FPS
    video_only = build / "video.mp4"
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(build / "concat.txt"),
         "-c", "copy", str(video_only)])
    mix, has_music = build_audio(timeline, timings, narration, total, build)
    run(["ffmpeg", "-y", "-v", "error", "-i", str(video_only), "-i", str(mix), "-map", "0:v", "-map", "1:a",
         "-c", "copy", "-movflags", "+faststart", "-shortest", str(build / "final.mp4")])

    (build / "chapters.txt").write_text("\n".join(f"{fmt_ts(t)} {n}" for t, n in chapters) + "\n", encoding="utf-8")
    desc = final_description(video_dir, chapters)
    if desc:
        (build / "description-final.txt").write_text(desc, encoding="utf-8")
    write_srt(timings, build / "subtitles.srt")
    size = (build / "final.mp4").stat().st_size / 1e6
    print(f"final.mp4: {fmt_ts(total)} ({total:.1f}s), {len(all_shots)} shots, music={'yes' if has_music else 'no'}, {size:.0f} MB")


if __name__ == "__main__":
    main()
