---
name: research-brief
description: Use when starting a new Pricewhy video (or when the user says "research #N" / "start video N") to produce content/<NNN>-<slug>/research.md — the sourced fact sheet every later step relies on. Not for writing the script (use script-writer) or for titles/thumbnails (use packaging).
---

# research-brief — the sourced fact sheet

One job: turn a topic from `docs/04-video-ideas-100.md` into `content/<NNN>-<slug>/research.md`, where **every number has a source, a period and a confidence level**. Nothing goes into a script that is not in this file.

## Steps

1. **Pick the slot.** Next free number in `content/` (3 digits) + short English slug: `004-why-australia-so-expensive`.
2. **State the thesis to TEST** (not to prove) in one line at the top. Example: "Theaters keep only a small part of the ticket and live on popcorn."
3. **Search primary sources first**: SEC filings (10-K, proxy), annual reports, investor decks, government statistics (BLS, EIA, ONS, ABS, StatCan), court/regulator documents. Then reputable media (Reuters, Bloomberg, WSJ, FT, NPR, CNBC). Blogs only as leads.
4. **Use the latest full year** available on today's date and say which fiscal year it is.
5. **Fill the template** `templates/research-template.md` (sections below).
6. **Show arithmetic** for every derived number (`5,323 / 10,383 = 51.3%`).
7. **Price Board** (02 §5.3): if comparable prices exist for US / UK / Canada / Australia, collect them with date and source. If not comparable, write "no fair comparison" — never force one.
8. **Thesis verdict**: true / partly true / false, in one sentence. A twist ("the hot dog is NOT a loss leader any more") is a gift for the script — keep it.
9. **Do NOT claim** list: popular myths and numbers you could not verify.
10. End with a 5-line summary to the user: thesis verdict, best 3 facts, biggest uncertainty.

## Rules

- Confidence labels: **proven** (read in the primary source, or arithmetic on it) · **probable** (reputable outlet or several agree) · **uncertain** (single weak or outdated source).
- Never round in a way that changes the story (51.3% is "about half", not "most").
- Estimates by analysts are labelled as analyst estimates, with the firm's name.
- Quotes: exact wording, original source, date. Second-hand quotes are labelled ("Jelinek recalled that Sinegal said…").
- No personal data, no paywalled text copied in bulk.
- If a fact is politically or medically sensitive, add both sides' best sourced numbers.

## Good example 1 — a key-numbers row

| Membership fees as % of operating income | 51.3% (5,323 / 10,383) | FY2025 | sec.gov/…/cost-20250831.htm | proven (arithmetic) |

Why good: value, arithmetic, period, primary source, confidence — the script can say "about half" safely.

## Good example 2 — a Do NOT claim entry

- "Costco loses $30–40M a year on chicken." The 2015 figure was gross margin given up versus charging $5.99, not a confirmed loss; Costco declined to say in 2019.

Why good: names the myth, explains exactly why it fails, points to the real number.

## Bad example (do not do this)

| Popcorn margin | 85% | — | various sources | proven |

Why bad: no period, no specific source, "various sources" cannot be checked, and the label "proven" is false. A number like this ends up on screen and gets corrected in the comments.
