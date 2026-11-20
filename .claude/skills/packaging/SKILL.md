---
name: packaging
description: Use when a Pricewhy script.md is final and the video needs everything for upload - 10 titles, 3 thumbnail specs rendered to PNG, description with sources and chapters, tags, pinned comment, on-screen chart PNGs. Triggers - "package video N", "make thumbnails for N". Not for writing the script or Shorts.
---

# packaging — titles, thumbnails, description, charts

One job: produce `content/<NNN>/package.md` and `content/<NNN>/visuals/` (specs + rendered PNGs) so the user can upload by copy-paste.

## Steps

1. **Read** `script.md`, `research.md`, `docs/05-ctr-retention-system.md` §3–4 and `docs/02-channel-identity.md` §5.
2. **10 titles** using different formulas from 05 §3. Mark the chosen main title and 2 test titles. Main title ≤ 55 characters (count and print it).
3. **3 thumbnail concepts** on 3 different templates (A receipt / B sliced / C two prices / D chart). Thumbnail text ≤ 3 words or one number, and it must not repeat the title. Every number on a thumbnail comes from research.
4. **Write `visuals/specs.json`** for `tools/render/render.mjs`: the 3 thumbnails + every chart the scene list asks for (receipt, stacked, compare). Brand tag "PRICEWHY", source line on every chart.
5. **Render**: `node tools/render/render.mjs content/<NNN>/visuals/specs.json`, then **look at each PNG** (Read the image). Fix overlaps or unreadable text, re-render. Check the thumbnails at small size mentally (160×90): one subject, one number.
6. **Description** from `templates/package-template.md`: first 2 lines answer the question + main phrase; chapters with timestamps from the scene list (first one 0:00); sources list (only sources actually used); the fixed footer (synthetic voice, not financial advice, affiliate note if any links).
7. **Tags** (8–15, lowercase), **pinned comment** (sources pointer + question for the next video), **end screen target** (one named video), **playlist**.
8. **Upload settings block**: category Education, language English, "AI use" per docs/11 §3, paid promotion = no (unless sponsored).

## Rules

- No faces of real people, no other creators' logos, no company logo as the main element (product/object illustration instead).
- Never promise in the title/thumbnail what the first 30 seconds don't show.
- No ALL-CAPS titles; max one emphasised word.
- Chapters only if ≥ 3 and each ≥ 10 s (YouTube requirement).
- Nothing is uploaded or published by Claude — the user does it.

## Good example 1 — title set excerpt

- MAIN: The $1.50 Trick That Built Costco (34 chars)
- TEST: Costco Doesn't Make Money Where You Think (41)
- TEST: Why Costco's Hot Dog Still Costs $1.50 (38)

Why good: three different formulas (trick / contradiction / why-question), all under 55 characters, all true to the script.

## Good example 2 — thumbnail spec

Template C, hot dog illustration, left "1985 · $1.50" (green), right "2026 · $1.50" (yellow), no other text.

Why good: one idea (the price never moved), confirmed in the first 5 seconds of the script, complements rather than repeats the title.

## Bad example (do not do this)

Title: "COSTCO'S SECRET THEY DON'T WANT YOU TO KNOW!!! (Shocking)" — thumbnail: shocked AI face + 6 words of text.

Why bad: clickbait that the video can't confirm, all caps, fake human face (policy + trust risk, see docs/11), unreadable at phone size.
