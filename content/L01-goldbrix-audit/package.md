# Package: L01 — We Fact-Checked a Crypto That Says It Has No Owner

Publish: **Wednesday 2 December 2026, 21:00 Germany (15:00 New York)** — extra video, outside the Tue/Fri rhythm · Playlist: *How They Make Money* · End screen → 002 *How Airlines Really Make Money*

## Titles (10)

| # | Formula (05 §3) | Title | Chars | Use |
|---|---|---|---|---|
| 1 | 2 — contradiction | We Fact-Checked a Crypto That Says It Has No Owner | 50 | **MAIN** |
| 2 | 8 — let's do the math | This Crypto Says Nobody Owns It. We Checked. | 44 | **TEST** |
| 3 | 9 — we followed | We Checked 12 Claims From an Ownerless Crypto | 45 | **TEST** |
| 4 | 5 — how X makes money | A Crypto Launchpad Where Nobody Gets the Fees | 45 | backup |
| 5 | 4 — the real cost | Who Gets Paid When You Trade a New Token? | 41 | backup |
| 6 | 10 — nobody explains | How to Check a Crypto Without Trusting It | 41 | backup |
| 7 | 3 | "No Owner, No Admin Key" — Is It True? | 37 | backup |
| 8 | 7 — the trick | The One-Digit Typo We Found in a Crypto's Exit | 46 | backup |
| 9 | 6 | Why This Crypto Burns Every Fee (We Checked) | 44 | backup |
| 10 | 2 | 11 Out of 12: Auditing a Crypto's Promises | 42 | backup |

## Thumbnails (3 — Test & Compare)

| File | Template | Text | Idea |
|---|---|---|---|
| `visuals/out/thumb-D-scoreboard.png` | D — chart | WE CHECKED · 11 vs 1 | The scoreboard, honest result |
| `visuals/out/thumb-B-fees.png` | B — sliced | FEES TO OWNER 0% · BURNED 100% | Follow the money |
| `visuals/out/thumb-A-receipt.png` | A — receipt | NO OWNER? · "Typo found 1" circled | Curiosity + the finding |

## Description (copy-paste)

```
A small crypto called GoldBrix says it has no owner, no admin key, and burns every fee. We didn't take its word for it: we checked 12 claims against its source code, three other blockchains and its own archives. 11 held up, 1 we couldn't verify, and we found a typo in its exit document.
Not financial advice. Crypto is high risk; you can lose everything. We are not affiliated with GoldBrix and hold no GBX.

CHAPTERS
0:00 12 claims, checked
1:00 Why "trust us" isn't enough
3:00 The supply
4:00 The launchpad rules
6:00 Can anyone pull the money?
7:00 Outside the chain
8:30 What we couldn't check — and the typo
10:00 The verdict

CHECK IT YOURSELF (21 Nov 2026)
- Source: github.com/GOLDBRIX-GBX/goldbrix-core (commit 4441eb34) — src/consensus/amount.h:26, src/kernel/chainparams.cpp:112-123, src/consensus/gbx_curve.h:43-44, src/consensus/gbx_launchpad.h:27, 53-55, 80
- Solana: getAccountInfo 3BVHXX3SKP9Z9hDe5SoiRP8TCNHd9kFK9va1JyXd4k7Q (program AAbKiRpmY5jYfC37DuQ9aTsWnNqxZXLe4fvyGSb3YS1F) -> "authority": null
- Base: owner() on 0x8e351c32dfb27aa22334a20dcf7262f54f78e0c0 -> reverts
- Arbitrum: owner() on 0xa43813d90adb98a5c400113ce2cc29d43d4ab867 -> reverts
- Arweave: xsVFhwVAkHyZwc7zT2X4Ml_Qhx8c9EofAk3tbizAhmc -> SHA-256 bd5cdf3eed5c7ca314d19c22b2a5a50cbe8c6957ef255b44b822c3e6a330c5a2 ; nVkgMqVScD8iq5e5RyxxCzImsREJkKCR7Qs-VSj2kOc -> 368814f002bb0b21e8d78072dd3756323b0ade43b06c0a6a6c531ec0b3f6585a
- Typo: GATE-R.md lists 0x8e35...dcf7272f... (no contract there)
- Not verified: treasury burn and "no premine" (GoldBrix nodes did not answer us)

MARKET SOURCES
- Chainalysis, 2025 Crypto Crime Report (2024 token launches): chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/
- Pump.fun fees (help center, 26 Sep 2025): intercom.help/pumpfun-web/en/articles/11002413-transaction-fees-on-pump-fun
- DefiLlama, Pump revenue (to 20 Nov 2026): defillama.com/protocol/pump
- Binance Research, Low Float & High FDV (2024): public.bnbstatic.com/static/files/research/low-float-and-high-fdv-how-did-we-get-here.pdf
- SafeMoon case: US DOJ (E.D.N.Y.) / IRS-CI releases, May 2025 and Feb 2026
- Bitcoin: bitcoin.org/en/faq

Pricewhy takes one price apart every week — line by line.
Narration uses a synthetic voice. Every number is sourced above.
Educational content, not financial advice.
```

## Tags
crypto, crypto fact check, goldbrix, gbx, proof of work, memecoin launchpad, rug pull, how to check a crypto, pump fun fees, crypto explained, blockchain explained, pricewhy

## Pinned comment
> Every check in this video can be repeated — the commands and addresses are in the description. If you find something we got wrong, tell us and we'll pin the correction. 🧾 Not financial advice.

## Upload settings
- Category: **Education** · Language: **English** · Made for kids: **No**
- AI use (Details → Attributes): **Yes** — synthetic narration (docs/11 §3)
- Paid promotion: **No** — the user states no involvement in GoldBrix (see CLAUDE.md, crypto exception). If that ever changes, tick it and change the "not affiliated" sentence.
- Playlist: **How They Make Money** · End screen: **002 How Airlines Really Make Money** + subscribe (optional, computer only)
- Subtitles: upload `subtitles.srt` from the UPLOAD-KIT (Studio → Subtitles → Upload file → With timing)
- Chapters: `description.txt` in the UPLOAD-KIT already has the real timestamps of the rendered video — paste it as is
