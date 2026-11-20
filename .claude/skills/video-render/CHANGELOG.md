# CHANGELOG — video-render

## 2026-11-20 — v1.1 (from the 002 render by a separate agent)
- 002 Airlines: 11:27, 108 shots, 85 MB, −14.2 LUFS, 7 chapters. Music g-major → c-dorian.
- Problem found: an automatic close-up of a 12 s chart cropped its title to a fragment → SKILL now says to aim `focus` or use `nosplit`, and to check every auto close-up.
- Problem found: the 84-character greedy caption split left 19 flashes under 0.8 s → `assemble.py` now splits sentences into balanced parts and merges fragments < 24 characters (002: 190 captions, 0 flashes). `--srt-only` regenerates captions without re-rendering.

## 2026-11-20 — v1
- Created after the user asked for finished videos ("conținutul complet, fără să fac eu nimic, doar să public").
- Tested on 003 Costco: 9:30, 72 shots, 65 MB, −14.1 LUFS, 7 real chapters, 167 subtitle lines; render ≈ 3 min + voice ≈ 2 min on 4 CPUs.
- Fixes from the test: first render was −22.8 LUFS (too quiet for YouTube) → loudnorm to −14 LUFS added; FreePD (planned music source) has closed → original music generated with `tools/video/music.py`.
- Music beds used so far: 003 = bed-a-minor → bed-d-dorian. Regenerate all six with:
  `for a in "a-minor A minor 80 1" "d-dorian D dorian 88 2" "f-major F major 76 3" "e-minor E minor 92 4" "g-major G major 84 5" "c-dorian C dorian 78 6"; do set -- $a; ~/.cache/pricewhy/venv/bin/python tools/video/music.py ~/.cache/pricewhy/music/bed-$1.wav --key $2 --mood $3 --bpm $4 --seconds 150 --seed $5; done`
