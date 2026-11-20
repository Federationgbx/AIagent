---
name: shorts-repurpose
description: Use when a Pricewhy long video has its script.md and you need 3-5 vertical clips for YouTube Shorts, TikTok and Instagram Reels (shorts.md with hook text, narration, cut points and captions). Triggers - "make shorts for N", "repurpose video N". Not for long-form scripts or thumbnails.
---

# shorts-repurpose — 3–5 vertical clips per long video

One job: write `content/<NNN>/shorts.md` — 3–5 clips of 30–55 seconds, each built around **one** surprising fact from the long video, each sending viewers to the long video.

## Steps

1. **Read** `script.md` and `research.md`. List the 5–8 strongest single facts (numbers that surprise on their own).
2. **Pick 3–5**, each from a different chapter. At least one "pause and guess" clip (guess → reveal).
3. **For each clip write** (use `templates/shorts-template.md`):
   - **On-screen hook text** (≤ 7 words, visible from frame 1)
   - **Narration** (60–130 words): fact → why it's surprising → twist → "full breakdown on Pricewhy"
   - **Cut source**: timestamps/scene numbers from the long video to reuse, or new 9:16 visuals (chart specs for `tools/render` if needed)
   - **Caption** for TikTok/Reels (≤ 150 characters, 3–5 hashtags) and **title** for YouTube Shorts (≤ 60 characters)
   - **Related video**: the long video's title (to link in YouTube's "Related video" field)
4. **Order** the clips for publishing: the strongest one goes out on the long video's publish day.

## Rules

- First frame = the object or the number. No logo intro.
- One fact per clip. If it needs context, it's the wrong fact.
- Same sourcing rules as the long video; probable facts keep their "reportedly".
- Export without another platform's watermark (download from CapCut, not from TikTok).
- Captions burned in (most people watch muted).

## Good example 1

Hook text: "Costco's real product isn't food" · Narration opens: "Costco made about ten point four billion dollars in operating profit in fiscal 2025. About half of that — five point three billion — came from one thing: the membership card…" · ends "Full receipt on Pricewhy."

Why good: one fact, sourced, a twist, and a reason to watch the long video.

## Good example 2

Hook text: "Guess what this costs Costco" (hot dog on screen) · "Pause and guess… Costco has never published it. But here's what its former CEO said…"

Why good: interactive (comments with guesses), honest about what is unknown.

## Bad example (do not do this)

A 55-second clip that summarises the whole 11-minute video in fast narration with six numbers and a "like and subscribe" at the start.

Why bad: no single payoff, too dense to follow muted, the ask comes before any value — viewers swipe away in the first 2 seconds.
