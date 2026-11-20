#!/usr/bin/env python3
"""Weekly / monthly YouTube performance review.

Reads the "Table data.csv" file that YouTube Studio exports from
Analytics -> Advanced mode -> Content -> Export -> CSV, compares every video
against the channel's own averages, sorts videos into A / B / C groups and
writes a Markdown report with a diagnosis for weak videos.

Only the Python standard library is used, so it runs anywhere with Python 3.9+.

Usage:
    python3 tools/analytics/review.py "tracking/exports/2026-12-07/Table data.csv"
    python3 tools/analytics/review.py export.csv --log tracking/video-log.csv --out report.md

With --log, videos are joined to tracking/video-log.csv by title (or video id)
and averages are also computed per tag (pillar, structure, hook_type,
title_formula, thumb_template) for the monthly pattern review.
"""
from __future__ import annotations

import argparse
import csv
import statistics
import sys
from dataclasses import dataclass, field
from pathlib import Path

# YouTube Studio column names change slightly between languages/versions,
# so each metric accepts several spellings (compared case-insensitively).
COLUMN_ALIASES = {
    "video_id": ["content", "video id", "video"],
    "title": ["video title", "title"],
    "published": ["video publish time", "publish time", "published"],
    "duration_s": ["duration", "duration (seconds)"],
    "views": ["views"],
    "watch_hours": ["watch time (hours)", "watch time"],
    "subs": ["subscribers", "subscribers gained"],
    "avd": ["average view duration", "avg. view duration"],
    "pct_viewed": ["average percentage viewed (%)", "average percentage viewed"],
    "impressions": ["impressions"],
    "ctr": ["impressions click-through rate (%)", "impressions ctr (%)", "impressions click-through rate"],
}

TAG_COLUMNS = ["pillar", "structure", "hook_type", "title_formula", "thumb_template"]

# Thresholds (relative to the channel's own average). Kept in one place so the
# skill's CHANGELOG can record any change to them.
MIN_IMPRESSIONS = 500      # below this a video is "too early to judge"
WEAK_RATIO = 0.60          # under 60% of channel average => group C
HOOK_RETENTION_FLOOR = 60  # % viewed considered alarming when CTR is fine


@dataclass
class Video:
    video_id: str
    title: str
    published: str = ""
    duration_s: float | None = None
    views: float = 0.0
    watch_hours: float = 0.0
    subs: float = 0.0
    avd_s: float | None = None
    pct_viewed: float | None = None
    impressions: float | None = None
    ctr: float | None = None
    tags: dict = field(default_factory=dict)
    group: str = ""
    notes: list = field(default_factory=list)

    @property
    def subs_per_1k(self) -> float | None:
        return self.subs / self.views * 1000 if self.views else None


def _num(value: str) -> float | None:
    """Parse numbers like '1,234', '5.2', '5.2%', '' -> float or None."""
    if value is None:
        return None
    cleaned = value.strip().replace(",", "").replace("%", "")
    if cleaned in ("", "-", "—"):
        return None
    try:
        return float(cleaned)
    except ValueError:
        return None


def _duration(value: str) -> float | None:
    """Parse '0:04:12', '4:12' or plain seconds into seconds."""
    if value is None or not value.strip():
        return None
    parts = value.strip().split(":")
    try:
        nums = [float(p) for p in parts]
    except ValueError:
        return None
    seconds = 0.0
    for n in nums:
        seconds = seconds * 60 + n
    return seconds


def _find_columns(header: list[str]) -> dict[str, int]:
    lowered = [h.strip().lower() for h in header]
    found = {}
    for key, aliases in COLUMN_ALIASES.items():
        for alias in aliases:
            if alias in lowered:
                found[key] = lowered.index(alias)
                break
    return found


def load_export(path: Path) -> list[Video]:
    with path.open(newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.reader(fh))
    if not rows:
        raise ValueError(f"{path} is empty")
    cols = _find_columns(rows[0])
    missing = [k for k in ("title", "views") if k not in cols]
    if missing:
        raise ValueError(
            f"{path}: missing required column(s) {missing}. Found header: {rows[0]}"
        )

    def cell(row, key):
        idx = cols.get(key)
        return row[idx] if idx is not None and idx < len(row) else ""

    videos = []
    for row in rows[1:]:
        if not row or cell(row, "video_id").strip().lower() == "total":
            continue  # YouTube puts a "Total" row first
        title = cell(row, "title").strip()
        if not title:
            continue
        videos.append(
            Video(
                video_id=cell(row, "video_id").strip(),
                title=title,
                published=cell(row, "published").strip(),
                duration_s=_duration(cell(row, "duration_s")),
                views=_num(cell(row, "views")) or 0.0,
                watch_hours=_num(cell(row, "watch_hours")) or 0.0,
                subs=_num(cell(row, "subs")) or 0.0,
                avd_s=_duration(cell(row, "avd")),
                pct_viewed=_num(cell(row, "pct_viewed")),
                impressions=_num(cell(row, "impressions")),
                ctr=_num(cell(row, "ctr")),
            )
        )
    return videos


def attach_tags(videos: list[Video], log_path: Path) -> None:
    """Join tags from tracking/video-log.csv by video id or exact title."""
    with log_path.open(newline="", encoding="utf-8") as fh:
        log_rows = list(csv.DictReader(fh))
    by_id = {r.get("youtube_id", "").strip(): r for r in log_rows if r.get("youtube_id")}
    by_title = {r.get("title", "").strip().lower(): r for r in log_rows if r.get("title")}
    for v in videos:
        row = by_id.get(v.video_id) or by_title.get(v.title.lower())
        if row:
            v.tags = {t: (row.get(t) or "").strip() for t in TAG_COLUMNS}


def _mean(values):
    values = [x for x in values if x is not None]
    return statistics.mean(values) if values else None


def classify(videos: list[Video]) -> dict:
    """Compare each video with the channel's own averages and assign A/B/C."""
    judged = [v for v in videos if (v.impressions or 0) >= MIN_IMPRESSIONS]
    avg = {
        "ctr": _mean(v.ctr for v in judged),
        "pct_viewed": _mean(v.pct_viewed for v in judged),
        "avd_s": _mean(v.avd_s for v in judged),
        "subs_per_1k": _mean(v.subs_per_1k for v in judged),
        "impressions": _mean(v.impressions for v in judged),
    }
    for v in videos:
        if (v.impressions or 0) < MIN_IMPRESSIONS:
            v.group = "too early"
            v.notes.append(f"Under {MIN_IMPRESSIONS} impressions: wait before judging.")
            continue
        # Use % viewed when present, otherwise average view duration.
        ret_key = "pct_viewed" if v.pct_viewed is not None and avg["pct_viewed"] else "avd_s"
        ret_val = getattr(v, ret_key)
        ctr_ratio = v.ctr / avg["ctr"] if v.ctr is not None and avg["ctr"] else None
        ret_ratio = ret_val / avg[ret_key] if ret_val is not None and avg[ret_key] else None

        weak_ctr = ctr_ratio is not None and ctr_ratio < WEAK_RATIO
        weak_ret = ret_ratio is not None and ret_ratio < WEAK_RATIO
        if weak_ctr or weak_ret:
            v.group = "C"
            v.notes.extend(diagnose(v, avg, weak_ctr, weak_ret))
        elif (ctr_ratio or 0) >= 1 and (ret_ratio or 0) >= 1:
            v.group = "A"
            v.notes.append("Above channel average on clicks AND retention: make 2 more like this.")
        else:
            v.group = "B"
    return avg


def diagnose(v: Video, avg: dict, weak_ctr: bool, weak_ret: bool) -> list[str]:
    """Plain-language diagnosis following docs/09 section 3."""
    notes = []
    low_reach = avg["impressions"] and (v.impressions or 0) < 0.5 * avg["impressions"]
    if weak_ctr:
        notes.append("Packaging problem: CTR under 60% of channel average -> new title (other formula), then new thumbnail template.")
    if weak_ret and not weak_ctr:
        notes.append("Promise/hook mismatch or slow structure: people click but leave -> check the retention graph for the first 30 s and any 'cliff'.")
    if weak_ret and weak_ctr:
        notes.append("Both clicks and retention weak: topic may not fit this audience -> lower priority for similar ideas.")
    if low_reach and not weak_ctr:
        notes.append("Low reach with fine CTR: limited demand or still being tested -> make a Short that links to it; optimise title/description for search.")
    subs = v.subs_per_1k
    if subs is not None and avg["subs_per_1k"] and subs < WEAK_RATIO * avg["subs_per_1k"]:
        notes.append("Few subscribers per 1,000 views: add the channel promise + series mention after the best moment.")
    return notes


def tag_breakdown(videos: list[Video]) -> dict:
    """Average CTR / % viewed / subs per 1k for every tag value (monthly review)."""
    out = {}
    for tag in TAG_COLUMNS:
        buckets: dict[str, list[Video]] = {}
        for v in videos:
            value = v.tags.get(tag)
            if value and v.group != "too early":
                buckets.setdefault(value, []).append(v)
        if buckets:
            out[tag] = {
                value: {
                    "n": len(vs),
                    "ctr": _mean(x.ctr for x in vs),
                    "pct_viewed": _mean(x.pct_viewed for x in vs),
                    "subs_per_1k": _mean(x.subs_per_1k for x in vs),
                    "watch_hours": sum(x.watch_hours for x in vs),
                }
                for value, vs in sorted(buckets.items())
            }
    return out


def _fmt(value, suffix="", digits=1):
    return "–" if value is None else f"{value:,.{digits}f}{suffix}"


def _fmt_dur(seconds):
    if seconds is None:
        return "–"
    m, s = divmod(int(round(seconds)), 60)
    return f"{m}:{s:02d}"


def render(videos: list[Video], avg: dict, tags: dict, source: str) -> str:
    total_hours = sum(v.watch_hours for v in videos)
    total_subs = sum(v.subs for v in videos)
    lines = [
        "# Performance review",
        "",
        f"Source file: `{source}`",
        "",
        "## Channel averages (videos with enough impressions)",
        "",
        "| CTR | % viewed | Avg view duration | Subs per 1k views | Impressions |",
        "|---|---|---|---|---|",
        f"| {_fmt(avg['ctr'], '%')} | {_fmt(avg['pct_viewed'], '%')} | {_fmt_dur(avg['avd_s'])} "
        f"| {_fmt(avg['subs_per_1k'])} | {_fmt(avg['impressions'], digits=0)} |",
        "",
        f"Watch hours in this export: **{_fmt(total_hours)}** · Subscribers gained: **{_fmt(total_subs, digits=0)}**",
        "",
        "## Videos",
        "",
        "| Group | Title | Views | Watch h | CTR | % viewed | AVD | Subs/1k |",
        "|---|---|---|---|---|---|---|---|",
    ]
    order = {"A": 0, "B": 1, "C": 2, "too early": 3}
    for v in sorted(videos, key=lambda x: (order.get(x.group, 9), -x.views)):
        lines.append(
            f"| {v.group} | {v.title} | {_fmt(v.views, digits=0)} | {_fmt(v.watch_hours)} "
            f"| {_fmt(v.ctr, '%')} | {_fmt(v.pct_viewed, '%')} | {_fmt_dur(v.avd_s)} | {_fmt(v.subs_per_1k)} |"
        )
    lines += ["", "## Diagnosis and actions", ""]
    for v in videos:
        if v.notes and v.group in ("A", "C"):
            lines.append(f"**{v.group} — {v.title}**")
            lines.extend(f"- {n}" for n in v.notes)
            lines.append("")
    if tags:
        lines += ["## Patterns by tag (monthly review)", ""]
        for tag, values in tags.items():
            lines += [f"### {tag}", "", "| Value | Videos | CTR | % viewed | Subs/1k | Watch h |", "|---|---|---|---|---|---|"]
            for value, m in values.items():
                lines.append(
                    f"| {value} | {m['n']} | {_fmt(m['ctr'], '%')} | {_fmt(m['pct_viewed'], '%')} "
                    f"| {_fmt(m['subs_per_1k'])} | {_fmt(m['watch_hours'])} |"
                )
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("export", type=Path, help="Table data.csv exported from YouTube Studio")
    parser.add_argument("--log", type=Path, help="tracking/video-log.csv to join tags")
    parser.add_argument("--out", type=Path, help="write the Markdown report here instead of stdout")
    args = parser.parse_args(argv)

    videos = load_export(args.export)
    if not videos:
        print("No videos found in export.", file=sys.stderr)
        return 1
    if args.log:
        attach_tags(videos, args.log)
    avg = classify(videos)
    report = render(videos, avg, tag_breakdown(videos) if args.log else {}, str(args.export))
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(report, encoding="utf-8")
        print(f"Report written to {args.out}")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
