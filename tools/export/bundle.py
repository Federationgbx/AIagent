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

Usage: python3 tools/export/bundle.py <output-dir>
"""
import re
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
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    made = []
    for folder in sorted((ROOT / "content").iterdir()):
        if folder.is_dir():
            z = bundle_video(folder, out)
            if z:
                made.append(z)
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
