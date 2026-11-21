# Research (comparison baseline): how typical launchpads and token launches work
Researched: 2026-11-21 · For: L01 GoldBrix audit
Purpose: a factual yardstick for GoldBrix. Describe mechanics and data only. No named project is called a scam, spam or fraud unless a court, regulator or prosecutor found so.

Confidence: **proven** = primary source (official docs, report, filing, DefiLlama API) or arithmetic on it · **probable** = reputable outlet / several agree · **uncertain** = weak, preprint, or self-reported.

## Key numbers
| Claim | Value | Period | Source URL | Confidence |
|---|---|---|---|---|
| Pump.fun bonding-curve fee | 1.25% per trade (0.95% protocol + 0.30% creator); coin creation free | help page dated 26 Sep 2025 | https://intercom.help/pumpfun-web/en/articles/11002413-transaction-fees-on-pump-fun | proven (for that date) |
| Same fee, later | 0.95% protocol + 0.05% creator; Pump.fun "can change these fees at any time without notice" | filing 21 Sep 2026 | https://blockworks.com/token-transparency/filing/pump | probable |
| PumpSwap (after graduation) | tiered by market cap: 1.25% down to 0.30% (0.20% LP / 0.05% protocol / 0.05% creator) | Sep 2025 | intercom page above | proven |
| PumpSwap launch | 0.25% fee (0.20% LP, 0.05% protocol); removed the 6 SOL migration fee to Raydium | 20 Mar 2025 | https://www.theblock.co/post/347360 | probable |
| Pump (all products) fees / revenue, lifetime | $2.44B fees / $1.41B revenue | 1 Mar 2024 – 20 Nov 2026 | https://defillama.com/protocol/pump (API: api.llama.fi/summary/fees/pump) | proven |
| pump.fun launchpad only, lifetime | $1.34B fees / $1.21B revenue | same | https://defillama.com/protocol/pump-fun | proven |
| Pump (all products), calendar 2025 | $988M fees / $653M revenue | 2025 | DefiLlama daily series, our sum | proven (arithmetic) |
| PUMP token public sale | $600M in 12 min at $0.004; FDV $4B | 12 Jul 2025 | https://www.theblock.co/post/362320 (citing Bloomberg) | probable |
| PUMP allocation | ICO 33% ($1.32B incl. private), team 20%, existing investors 13%; insiders locked 12 months, then linear vesting to Jul 2029 | 2025–2029 | Blockworks filing above | probable |
| Pump.fun tokens analysed by Solidus | >7M with ≥5 trades; only ~97,000 kept >$1,000 liquidity | Jan 2024 – Mar 2025 | https://www.soliduslabs.com/reports/solana-rug-pulls-pump-dumps-crypto-compliance | proven |
| Solidus headline | 98.6% of Pump.fun tokens (98.7% in its summary) | same | same | proven (that the report says it) |
| Raydium pools | ~93% of 388,000 pools "exhibited soft rug pull characteristics"; median $2,832; largest $1.9M | same | same | proven (that the report says it) |
| Total Pump.fun launches | "over 11.9 million" | to Jun 2026 | https://en.cryptonomist.ch/2026/06/10/pump-fun-solana-token-launches/ (platform's own claim) | uncertain |
| Tokens launched, all chains | 2,063,519 | 2024 | https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/ | proven |
| …with pump-and-dump characteristics | 3.59% (74,037) | 2024 | same | proven |
| Suspected pools rugged by pool creator | ~94% (69,897 of 74,312) | 2024 | same | proven |
| MC/FDV of tokens launched in 2024 | 12.3% (as of 14 Apr 2024); recent launches 6–20% circulating | 2024 | https://public.bnbstatic.com/static/files/research/low-float-and-high-fdv-how-did-we-get-here.pdf | proven |
| Token unlocks ahead | ~$155B, 2024–2030 (Token Unlocks estimate) | 2024–2030 | same PDF | proven (as an estimate) |
| Unlock price effect | 90% of unlocks "create negative price pressure"; team unlocks worst (−25%) | 16,000+ events, 40 tokens | https://keyrock.com/from-locked-to-liquidity-what-16000-token-unlocks-teach-us/ | probable |
| Bitcoin | 21M max; ~10-min blocks; subsidy started at 50, halves every 210,000 blocks (≈4 years) | protocol | https://bitcoin.org/en/faq ; https://developer.bitcoin.org/reference/block_chain.html | proven |

## 1. Pump.fun — mechanics, fees, money
- Each coin is minted with a fixed 1,000,000,000 supply and trades on a bonding curve; at a threshold it "graduates" to an AMM (Raydium until March 2025, PumpSwap since).
- **Fees go to people, not to a burn:** protocol, coin creator and LPs each take a slice. Creator fees were added in 2025. Rates changed several times (compare Sep 2025 vs Sep 2026 rows) and the company says it can change them.
- **Buybacks:** DefiLlama's methodology says protocol revenue was redirected to PUMP buybacks from 14 Jul 2025; Blockworks' filing says 50% of net revenue buys and burns PUMP since 28 Apr 2026 (1-year commitment), and the rate can be changed by the config authority with no timelock.
- **Upgrade key:** one address controls upgrades of both the bonding-curve and PumpSwap programs; signers/threshold not disclosed (Blockworks filing).
- DefiLlama "revenue" = Pump's slice of fees, **not profit**.

## 2. Solidus Labs 2025 Rug Pull Report (May 2025) and the reply
- Method: a Pump.fun token counted in the 98.6% if it had ≥5 trades and its liquidity fell **below $1,000**; graduated tokens excluded. Raydium "soft rug" = deployer removed ≥90% of the pool's LP tokens.
- Pump.fun's reply (spokesperson Troy Gravitt, CoinDesk, 8 May 2025): "What Solidus Labs lacks is a basic understanding of memecoins." He argued most memecoins, like most NFTs or artworks, end up worth little, that this is "precisely the point", and that the value is a working marketplace. https://www.coindesk.com/business/2025/05/07/98-of-tokens-on-pump-fun-have-been-rug-pulls-or-an-act-of-fraud-new-report-says

## 3. Chainalysis (2025 Crypto Crime Report chapter, 29 Jan 2025, updated 13 Feb 2025)
- Criteria: an address added liquidity and later removed ≥65% (worth ≥$1,000), pool now inactive, >100 transactions. Chainalysis says this "tracks patterns of behavior and not intent".
- 74,037 ÷ 873,957 DEX-listed tokens ≈ **8.5%** of DEX-listed tokens (our arithmetic, assuming all flagged tokens were DEX-listed).
- 2026 report (covering 2025): we found no comparable memecoin/pump-and-dump figure and **no Chainalysis figure on "share of tokens with insider wallets"**.

## 4. Typical token launches (VC-backed)
- Binance Research (17 May 2024): low float + high FDV; at MC/FDV 12.3%, ~US$80B of new demand would be needed just to hold prices as supply unlocks. It notes most memecoins launch with MC/FDV ≈ 1 (all supply circulating).
- Worked example: PUMP itself reserved 33% for team + existing investors, locked 12 months then vesting monthly.
- Industry "typical" team/investor shares (15–20% team etc.) appear only in vendor blogs: **uncertain**, not used.

## 5. Rug-pull mechanics (definitions differ)
- **CertiK (May 2022):** hard rug = team "suddenly withdraws the funds" (backdoor code, liquidity removal, sell restrictions); soft rug = founders dump their own tokens "whilst maintaining a front". https://www.certik.com/blog/what-is-a-soft-rugpull-vs-a-hard-rugpull
- **Solidus:** hard rug = "encoded directly into the smart contract" (honeypots, infinite-mint backdoors); soft rug = "sudden liquidity drains or massive token dumps by creators". https://www.soliduslabs.com/solutions/token-monitoring
- Note: liquidity removal is "hard" for CertiK, "soft" for Solidus. Say which definition you use.
- Solana tokens carry a **mint authority** (can create supply) and **freeze authority** (can freeze holders' accounts); both can be revoked. PUMP's are null (Blockworks); guides say Pump.fun coins have mint revoked (probable, not checked on-chain).
- Share of Solana tokens keeping mint/freeze authority: **no reputable figure found.** Closest: SolRugDetector preprint (arXiv 2603.24625, Mar 2026) flagged 76,469 of 100,063 new Solana tokens (H1 2025); only 461 as "freeze authority abuse" — **uncertain** (preprint, heuristic).

## 6. Cases where an official body acted (describe only as stated)
1. **SafeMoon (DOJ, E.D.N.Y.).** 21 May 2025: jury convicted CEO Braden John Karony of conspiracy to commit securities fraud, wire fraud and money laundering. DOJ: investors were told liquidity was "locked"; insiders "retained access to the SafeMoon liquidity pools" and diverted tokens. 10 Feb 2026: 100 months in prison, ~$7.5M forfeiture. https://www.irs.gov/node/147471 ; https://www.irs.gov/node/156136 (DOJ release: justice.gov/usao-edny)
2. **Operation Token Mirrors (DOJ, D. Mass.).** 9 Oct 2024: 18 individuals/entities charged — token companies (e.g., Saitama, Robo Inu) and market makers (Gotbit, ZM Quant, CLS Global, MyTrade); alleged wash trading and "pump and dump"; FBI created its own token, NexFundAI; >$25M seized. Charges "are allegations". June 2025: Gotbit sentenced to 5 years' probation and ~$23M forfeiture; founder 8 months (Reuters: time already served). https://www.irs.gov/node/139431 ; https://www.theblock.co/news/regulation/2025-06-13-gotbit-founder-aleksei-andriunin-sentenced-to-8-months-following-wash-trading-scheme-358107
3. **SEC v. Hydrogen Technology (S.D.N.Y.).** Complaint 28 Sep 2022: market maker hired to "create the false appearance of robust market activity" for the Hydro token, yielding >$2M. Final consent judgments 26 May 2023 (without admitting or denying): Hydrogen ~$2.8M total, ex-CEO ~$0.26M. https://www.sec.gov/litigation/litreleases/lr-25737

## 7. Bitcoin reference
- "Only 21 million bitcoins will ever be created"; blocks "approximately every 10 minutes on average" (bitcoin.org FAQ). Subsidy "started at 50 bitcoins and is being halved every 210,000 blocks—approximately once every four years" (developer.bitcoin.org).
- No premine: coins enter circulation only as block rewards (whitepaper §6, https://bitcoin.org/bitcoin.pdf); the genesis block's 50 BTC "can't be spent" (https://en.bitcoin.it/wiki/Genesis_block) — probable.

## Do NOT claim
- "98% of Pump.fun tokens are scams/frauds." Say: Solidus found ~98.6% ended below $1,000 liquidity and classified that as rug pull or pump-and-dump; Pump.fun disputed it. "Fraud" is headline wording, not a finding.
- "93% of Raydium pools were rug pulls." Say: "showed soft-rug characteristics" (deployer pulled ≥90% of liquidity).
- That Pump.fun, LIBRA, M3M3, Hawk Tuah or any other named project is a scam. Pump.fun's operator faces a private class action (Aguilar v. Baton Corp., S.D.N.Y., filed 30 Jan 2025): allegations only; we found no final judgment.
- CoinDesk's line that "the SEC filed a class action" against Meteora: SEC does not file class actions; do not repeat.
- A trend from Chainalysis 54% (2023, Ethereum) to 3.59% (2024): criteria were tightened.
- A single "typical" team/VC allocation %.
- "Pump.fun keeps all fees" (creators/LPs get shares) or DefiLlama revenue = profit.
- "Pump.fun coins can be minted at will": per-coin supply is fixed, so GoldBrix's fixed supply is not unique against them. Real contrasts: where fees go (burned vs company/creators), upgrade key (none vs one undisclosed signer set), fees changeable vs consensus rule.
- Current Pump.fun fee rates as permanent; always date them.
- "Gotbit's founder served 8 months in prison" (time served).
- Satoshi's holdings (~1M BTC estimates are unverified); "halves exactly every 4 years" (it's 210,000 blocks).
- S01 line "Most crypto projects have a team that can mint coins, pause trading, or pull the money": no dataset supports "most"; use "many projects keep such controls".

## 7b. Addendum (21 Nov 2026): Bitcoin's founder walked away
| Claim | Value | Source | Confidence |
|---|---|---|---|
| Satoshi Nakamoto's last public forum post | 12 Dec 2010 (Bitcointalk; some records show a login on 13 Dec) | https://blockworks.co/news/satoshi-nakamoto-last-online ; https://news.bit2me.com/en/December-12--2010-Satoshi-Nakamoto-wrote-his-last-message | proven (date of post) |
| Last known private emails | April 2011 (to Mike Hearn, 23 Apr; to Gavin Andresen, 26 Apr): had "moved on to other things" (wording varies by outlet) | https://cointelegraph.com/news/satoshi-nakamoto-final-email-revisited-after-13-years | probable |
Do NOT claim: an exact quote beyond "moved on"; that Bitcoin is "abandoned" (its founder left; development continued by others).
