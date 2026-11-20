---
name: script-writer
description: Use when a Pricewhy video has a finished research.md and needs its long-form narration script (script.md with scene list and VOICE-READY text). Triggers - "write the script for 00N", "script video N". Not for research, titles, thumbnails or Shorts.
---

# script-writer — the 9–12 minute narration script

One job: turn `content/<NNN>/research.md` into `content/<NNN>/script.md` — a script that confirms the thumbnail in second one, keeps people watching, and never says a number that is not in the research file.

## Steps

1. **Read** `research.md` fully, `docs/02-channel-identity.md` §4 (voice) and `docs/05-ctr-retention-system.md` §5–9.
2. **Choose the structure** (05 §7): Autopsy, Detective, Follow-the-Dollar or Timeline. Do not use the same structure as the previous video in `tracking/video-log.csv`.
3. **Pick the twist**: the research's thesis verdict. If the popular belief is wrong, the twist goes at ~50–60% of the runtime.
4. **Write the hook (0–30 s)** with three beats: show the object + price → stakes/reversal → open loop. No greeting, no channel intro.
5. **Write 4–6 chapters.** Each opens with a question, delivers 1–3 sourced facts, adds one receipt line, ends with a hand-off to the next question.
6. **Insert the fixed devices**: receipt lines (one per chapter), one "pause and guess", the Price Board segment if research has comparable country data, one comment question at ~30%, one value-based subscribe line at ~65%, the end hand-off to one named next video.
7. **Write the VOICE-READY narration** in numbered paragraphs (¶1, ¶2 …): narration only, numbers spelled the way they should be spoken ("nine forty-nine"), `[pause]` marks, no visual notes. One ¶ = one voice chunk the user can regenerate alone.
8. **Fill the scene list** in `templates/script-template.md`: for every ¶ — on-screen visual (chart file from `visuals/`, stock search phrase, or text), source line, approx. time. The scene list references ¶ numbers instead of repeating the narration.
9. **Fact check**: list every number in the script and the research row it comes from. Any number without a row is removed.
10. **Length check**: 1,400–1,900 words of narration (≈ 9–12 min at ~155 wpm). Report the count.

## Rules

- "We" or neutral voice. Never invent a person ("I'm Mike, an analyst"). Never give personal financial advice.
- Every number says its year/period once ("in fiscal 2025").
- Short sentences. One idea per sentence. Concrete over vague ("$1.87 of every $100", not "a small amount").
- Respect the research's "Do NOT claim" list and its confidence labels: probable → "reportedly"/"according to"; uncertain → leave out.
- Quotes are exact and attributed as in research.
- Fairness: if a company is criticised, include its best sourced counterpoint.
- The ending pays off the hook's open loop explicitly.

## Good example 1 — hook

> This hot dog has cost a dollar fifty since 1985. [pause] Adjusted for inflation, it should be about four fifty. Costco sells two hundred forty-five million of them a year — and everyone assumes it loses money on every one. It doesn't. The real trick is a sixty-five dollar card in your wallet. Let's itemize it.

Why good: object + price in the first sentence, a surprising number, a reversal of the common belief, an open loop ("the real trick") — all sourced.

## Good example 2 — chapter opener with re-hook

> So who actually gets your ticket money? [pause] Here's the part almost nobody reads: page forty of AMC's annual report.

Why good: opens with a question, promises a specific payoff, signals original research.

## Bad example (do not do this)

> Hey guys, welcome back to the channel! Today we're going to talk about Costco, one of the most popular stores in the world. Before we start, make sure to like and subscribe! Costco makes basically all its money from memberships…

Why bad: 15 seconds without the object or a number, a subscribe ask before any value, and a false claim ("basically all" — research says ~51% of operating income). Retention drops and the comments correct us.
