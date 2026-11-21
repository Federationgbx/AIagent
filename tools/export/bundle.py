#!/usr/bin/env python3
"""Build phone-friendly ZIP bundles for the user (no GitHub needed).

For every content/<NNN>-<slug>/ that has a script.md it writes
<out>/Pricewhy-<NNN>-<slug>.zip containing:
  voice.txt        narration only, ready to paste into the voice tool
                   ([pause] -> "...", chapter labels and ¶ numbers removed)
  description.txt  the YouTube description block from package.md
  script.md, package.md, shorts.md, research.md
  images/          every rendered PNG from visuals/out/
It also writes Pricewhy-brand.zip (logo + banner) and Pricewhy-plan.zip (docs).

With --final it also copies every rendered build/final.mp4 as Pricewhy-<video>.mp4
plus Pricewhy-<video>-UPLOAD-KIT.zip (upload.txt, description.txt with real
chapters, subtitles.srt, thumbnails) and any rendered Shorts.

Usage: python3 tools/export/bundle.py <output-dir> [--final]
"""
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def voice_text(script: str) -> str:
    """Narration paragraphs from the VOICE-READY section, cleaned for TTS."""
    m = re.search(r"## VOICE-READY.*?\n(.*?)(?=\n## )", script, re.S)
    if not m:
        return ""
    paras = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line.startswith("¶"):
            continue
        line = re.sub(r"^¶\s*\d+\s*", "", line)
        line = line.replace("[pause]", "...")
        paras.append(re.sub(r"\s{2,}", " ", line).strip())
    return "\n\n".join(paras) + "\n"


def description(package: str) -> str:
    m = re.search(r"## Description.*?```\n(.*?)```", package, re.S)
    return m.group(1) if m else ""


def upload_text(package: str) -> str:
    """Title, tags and settings — everything to type into YouTube Studio."""
    title = ""
    for line in package.splitlines():
        if "**MAIN**" in line:
            title = [c.strip() for c in line.strip("|").split("|")][2]
            break
    tags = re.search(r"## Tags\n(.*?)\n", package)
    settings = re.search(r"## Upload settings\n(.*?)(?=\n## |\Z)", package, re.S)
    return (f"TITLE\n{title}\n\nTAGS\n{tags.group(1).strip() if tags else ''}\n\n"
            f"SETTINGS\n{settings.group(1).strip() if settings else ''}\n\n"
            "Description: description.txt (chapters already timed to this video)\n"
            "Subtitles: subtitles.srt (Studio → Subtitles → Upload file → With timing)\n"
            "Thumbnails: the 3 thumb-*.png → Test & Compare\n")


def upload_kit(folder: Path, out: Path) -> list[Path]:
    """Finished video + everything needed to upload it, if the video was rendered."""
    build = folder / "build"
    final = build / "final.mp4"
    if not final.exists():
        return shorts_only_kit(folder, out)
    made = []
    mp4 = out / f"Pricewhy-{folder.name}.mp4"
    shutil.copyfile(final, mp4)
    made.append(mp4)
    kit = out / f"Pricewhy-{folder.name}-UPLOAD-KIT.zip"
    pkg = (folder / "package.md").read_text(encoding="utf-8")
    with zipfile.ZipFile(kit, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("upload.txt", upload_text(pkg))
        guide = ROOT / "docs" / "13-cum-publici.md"
        if guide.exists():
            z.write(guide, "CUM-PUBLICI.txt")
        desc = build / "description-final.txt"
        z.writestr("description.txt", desc.read_text(encoding="utf-8") if desc.exists() else description(pkg))
        if (build / "subtitles.srt").exists():
            z.write(build / "subtitles.srt", "subtitles.srt")
        for png in sorted((folder / "visuals" / "out").glob("thumb-*.png")):
            z.write(png, png.name)
        if (folder / "shorts").exists():
            for f in sorted((folder / "shorts").glob("*.txt")):
                z.write(f, f"shorts/{f.name}")
    made.append(kit)
    shorts_dir = build / "shorts"
    for f in sorted(shorts_dir.glob("short-*.mp4")) if shorts_dir.exists() else []:
        dst = out / f"Pricewhy-{folder.name}-{f.name}"
        shutil.copyfile(f, dst)
        made.append(dst)
    return made


def shorts_only_kit(folder: Path, out: Path) -> list[Path]:
    """Folders with Shorts but no long video (e.g. content/S01-...)."""
    shorts = sorted((folder / "build" / "shorts").glob("short-*.mp4")) if (folder / "build" / "shorts").exists() else []
    if not shorts:
        return []
    made = []
    kit = out / f"Pricewhy-{folder.name}-SHORTS-KIT.zip"
    with zipfile.ZipFile(kit, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted((folder / "shorts").glob("*.txt")):
            z.write(f, f"shorts/{f.name}")
        guide = ROOT / "docs" / "13-cum-publici.md"
        if guide.exists():
            z.write(guide, "CUM-PUBLICI.txt")
    made.append(kit)
    for f in shorts:
        dst = out / f"Pricewhy-{folder.name}-{f.name}"
        shutil.copyfile(f, dst)
        made.append(dst)
    return made


def bundle_video(folder: Path, out: Path) -> Path | None:
    script = folder / "script.md"
    if not script.exists():
        return None
    target = out / f"Pricewhy-{folder.name}.zip"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("voice.txt", voice_text(script.read_text(encoding="utf-8")))
        pkg = folder / "package.md"
        if pkg.exists():
            z.writestr("description.txt", description(pkg.read_text(encoding="utf-8")))
        for name in ("script.md", "package.md", "shorts.md", "research.md"):
            f = folder / name
            if f.exists():
                z.write(f, name)
        for png in sorted((folder / "visuals" / "out").glob("*.png")):
            z.write(png, f"images/{png.name}")
    return target


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 1
    out = Path(args[0])
    out.mkdir(parents=True, exist_ok=True)
    made = []
    for folder in sorted((ROOT / "content").iterdir()):
        if folder.is_dir():
            z = bundle_video(folder, out)
            if z:
                made.append(z)
            if "--final" in sys.argv:
                made += upload_kit(folder, out)
    brand = out / "Pricewhy-brand.zip"
    with zipfile.ZipFile(brand, "w", zipfile.ZIP_DEFLATED) as z:
        for png in sorted((ROOT / "brand" / "out").glob("*.png")):
            z.write(png, png.name)
    made.append(brand)
    plan = out / "Pricewhy-plan.zip"
    with zipfile.ZipFile(plan, "w", zipfile.ZIP_DEFLATED) as z:
        for f in [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]:
            z.write(f, f.relative_to(ROOT))
    made.append(plan)
    for m in made:
        print(f"{m}  ({m.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
