# CHANGELOG — packaging

## 2026-11-21 — v1.2 (user correction, approved with "Ok")
- The L01 description had "->" arrows; YouTube rejects "<" and ">" in descriptions, so the user had to fix it by hand. New rule: no "<" or ">" in titles, descriptions or tags; bundle.py now refuses to build a kit that contains them.

## 2026-11-20 — v1.1
- Added YouTube limits (description ≤ 5,000, tags ≤ 500 characters) after checking 003 (3,439 / 243).
- Renderer fixes from the 001/002 tests: compare-chart labels now have a fixed height (long labels no longer lift bars off the baseline); receipt charts accept `"show_total": false` so the total isn't revealed early. All three videos re-rendered.
- The Mastercard-like circles on the card illustration were replaced by generic contactless waves (trademark risk spotted during the 003 review).

## 2026-11-20 — v1 — tested on 3 real cases
- 003 Costco: 10 titles, 3 thumbnails (C/B/A), 11 charts → 20 PNGs.
- 001 Popcorn (separate agent): 3 thumbnails (C/A/B), 34 PNGs; fixed 4 layout issues through spec text alone.
- 002 Airlines (separate agent): 3 thumbnails (C/D/A), 22 PNGs; changed the main title from "(It's Not Flying)" to "(It's Your Credit Card)" because the research's Do NOT claim list forbade the first — the rule "never promise what the video can't confirm" worked.
- From the first renderer test: template A headline overlapped the illustration and template C's arrow crossed the object → layouts fixed; step 5 ("look at each PNG") added because of this.
- Known limit: no 9:16 chart size yet — Shorts reframe the 16:9 charts in CapCut.
