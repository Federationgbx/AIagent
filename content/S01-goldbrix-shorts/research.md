# Research: GoldBrix (GBX) — neutral explainer Shorts for Pricewhy
Researched: 2026-11-21
Thesis to test: "A crypto launchpad that pays nobody: every fee burned, no owner, fixed supply." — **partly verifiable**: the rules below are in the public source code; the founder's exit is a claim with on-chain transaction IDs that we did not independently check.

Decision context (21.11.2026): the user chose to publish these on Pricewhy, in English, as a **neutral presentation** (user states no involvement in GoldBrix). Rules for this item: present everything as "the project says / the code says", no price, no returns, no "buy", always "Not financial advice. Crypto is high risk."

Confidence: **proven** = read in the source code (cloned 2026-11-21) or arithmetic on it · **claimed** = stated by the project's own docs, not independently verified · **probable** = reputable outlet.

## Key numbers

| Claim | Value | Period | Source | Confidence |
|---|---|---|---|---|
| Max supply | 15,000,000 GBX | consensus constant | goldbrix-core `src/consensus/amount.h` (`MAX_MONEY = 15000000 * COIN`) | proven |
| Bootstrap phase | 50 GBX per block up to block 20,000 → 1,000,000 GBX | from genesis | `src/validation.cpp` GetBlockSubsidy; `chainparams.cpp` nV31ForkHeight = 20000 | proven (arithmetic 20,000 × 50) |
| Production phase | 0.25 GBX per block, halving every 28,000,000 blocks | after block 20,000 | `chainparams.cpp` nV31InitialSubsidy = 25,000,000 sat, nV31HalvingInterval = 28,000,000 | proven |
| Block time (production) | 3 seconds (LWMA target) | after block 20,000 | `chainparams.cpp` nLwmaTargetSpacing = 3 | proven |
| Supply adds up | 1,000,000 + 7,000,000 + 3,500,000 + … = 15,000,000 | — | arithmetic (28M × 0.25 = 7M, geometric series → 14M) | proven (arithmetic) |
| One halving period | ≈ 2.66 years (28M blocks × 3 s) | — | arithmetic | proven (arithmetic, at target block time) |
| Launchpad fees | must be sent to a provably unspendable burn address; a transaction that doesn't burn the fee is invalid (`BAD_FEE`) | consensus | `src/consensus/gbx_launchpad.h` ("Fees must go here — the protocol collects nothing") | proven (code) |
| Price formula | bonding curve x·y = k | consensus | `gbx_launchpad.h`, README | proven (code) |
| Creating a token | requires proof-of-work done for that token; first buy mandatory, no money minimum | consensus | `gbx_launchpad.h` IDEE W comments | proven (code) |
| Reorg limit | chain reorganizations deeper than 100 blocks rejected | consensus | `chainparams.cpp` nMaxReorgDepth = 100 | proven |
| No premine, no presale | — | since genesis | README | claimed |
| Founder exit | 25 Aug 2026: treasury ~469,910.85 GBX sent to burn address; release key and Arweave key destroyed; Solana swap program immutable | 2026-08-25 | goldbrix-tools `docs/GATE-R.md` (lists tx IDs) | claimed (not verified by us) |
| Founder identity | anonymous, "Gideon Brick" | — | README | claimed |
| Project size | 3 public repos, 3–4 GitHub stars each | 2026-11-21 | GitHub search | proven (as seen) |
| Rug-pull context | ~98.6% of tokens launched on Pump.fun showed rug-pull or pump-and-dump behavior (Solidus Labs; some outlets say 98.7%) | Jan 2024 – Mar 2025 | Solidus Labs "2025 Rug Pull Report" https://www.soliduslabs.com/reports/solana-rug-pulls-pump-dumps-crypto-compliance ; CoinDesk May 7 2025 | probable (Pump.fun disputed the report) |

## Worked example for the price-formula Short (illustrative, before fees)
Pool: 100 GBX × 100 tokens → k = 10,000.
- Buy 10 tokens: tokens 100 → 90, GBX = 10,000 / 90 = 111.11 → cost **11.11 GBX** (avg 1.11)
- Buy 50 tokens: tokens 100 → 50, GBX = 10,000 / 50 = 200 → cost **100 GBX** (avg 2.00, double the starting 1.00)

## Do NOT claim
- Any price, market cap, volume, "undervalued", "next Bitcoin", returns, or that burning fees raises value.
- That the founder exit is verified (we did not check the transactions) — say "the project says … and lists the transaction IDs".
- That GoldBrix is safe, audited, or regulated. No audit was found.
- That Pump.fun is a scam platform — the figure is from one report that Pump.fun disputed.
- That it is "no team at all" as fact — say "says it has no owner, no company, no admin key".
