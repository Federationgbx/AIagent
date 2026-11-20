---
name: analytics-review
description: Use when the user adds a YouTube Studio CSV export to tracking/exports/ or asks for the weekly or monthly Pricewhy review ("weekly review", "monthly review", "how are the videos doing"). Produces a review file with A/B/C groups, diagnoses and at most 3 actions. Not for planning new videos from scratch.
---

# analytics-review — weekly and monthly performance review

One job: turn the Studio export into decisions. Output: `tracking/reviews/<YYYY-MM-DD>-weekly.md` or `tracking/reviews/<YYYY-MM>-monthly.md`.

## Steps

1. **Find the export**: newest folder in `tracking/exports/`, file `Table data.csv`. If missing, tell the user exactly how to export (docs/09 §4) and stop.
2. **Run the tool**:
   - weekly: `python3 tools/analytics/review.py "<path>/Table data.csv"`
   - monthly: add `--log tracking/video-log.csv` for the per-tag patterns
3. **Read the output** and fill `templates/weekly-review.md` (or `monthly-review.md`).
4. **Diagnose every C video** with the tree in docs/09 §3 — say which signal failed (reach, CTR, 30-second retention, % viewed, subs per 1k) and the one fix.
5. **For A videos** propose 2 follow-up ideas on the same pattern (add them to the review, not to docs/04 yet).
6. **Write at most 3 actions** for next week, each concrete ("Change #004 title to formula 3: …").
7. **Monthly only**: answer the 6 questions in docs/09 §5, show the progress to 1,000 subs + 8,000 hours, and **propose** a reordered top 20 for docs/04 as a diff. Apply it only after the user says OK.
8. **Update `tracking/video-log.csv`** with the A/B/C group of each video.

## Rules

- Compare videos with the channel's own averages, not internet benchmarks (except in the first month).
- Under 500 impressions = "too early", no verdict.
- Never invent numbers: if a column is missing from the export, say so.
- Never change titles/thumbnails yourself — propose; the user applies them in Studio.
- Keep it short: the user reads it on a phone.

## Good example 1 — a diagnosis line

> **C — Why Is Canada So Expensive?** CTR 1.9% vs channel 5.2% → packaging. Action: new title (formula 2, "Why Canada Costs More Than the US"), keep thumbnail test running.

Why good: the failing signal, the size of the gap, one specific fix.

## Good example 2 — an A-video follow-up

> **A — Costco's $1.50 hot dog** (CTR 9.1%, 52% viewed). Same pattern = "a famous cheap item + the hidden business model". Next: #73 dollar stores, #74 razor-and-blades.

Why good: names the pattern, not just the topic, and maps it to existing ideas.

## Bad example (do not do this)

> Video 4 did badly, probably the algorithm. Let's post more often and use trending hashtags.

Why bad: no signal named, blames "the algorithm", and the actions are generic and unmeasurable.
