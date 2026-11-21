# Evidence log: GoldBrix (GBX) — what Pricewhy checked itself
Checked: 2026-11-21 (14:00–16:35 CET) from a cloud server. Every line below says HOW it was checked, so anyone can repeat it.

Confidence: **proven** = we ran the check ourselves and it matched · **claimed** = the project says so; we could not check it · **mismatch** = we checked and found a difference.

## A. Source code (GitHub `GOLDBRIX-GBX/goldbrix-core`, commit `4441eb34`, 12 Sep 2026)

| Claim | Evidence (file : line) | Confidence |
|---|---|---|
| Hard cap 15,000,000 GBX | `src/consensus/amount.h:26` `MAX_MONEY = 15000000 * COIN` | proven |
| 50 GBX/block until block 20,000 | `src/validation.cpp:1969-1993`, `src/kernel/chainparams.cpp:117` `nV31ForkHeight = 20000` | proven |
| Then 0.25 GBX/block, halving every 28M blocks | `chainparams.cpp:118` `nV31HalvingInterval = 28000000`, `:123` `nV31InitialSubsidy = 25000000` (sat) | proven |
| 3-second blocks | `chainparams.cpp:112` `nLwmaTargetSpacing = 3` | proven |
| Supply adds to exactly 15,000,000 | 20,000 × 50 + Σ 28,000,000 × 0.25 / 2ⁱ = 1,000,000 + 14,000,000 | proven (arithmetic) |
| Reorgs deeper than 100 blocks rejected (≈ 5 minutes at 3 s) | `chainparams.cpp:119` `nMaxReorgDepth = 100` | proven (code) |
| Launchpad trade fee 0.50%, AMM fee 0.30% — both burned | `src/consensus/gbx_curve.h:43-44` (`CURVE_FEE_BPS = 50`, `POOL_FEE_BPS = 30`, "BURNED, never collected") | proven (code) |
| A trade that doesn't burn its fee is invalid | `gbx_launchpad.h:162` `BAD_FEE` "the protocol fee was not burned"; `:197-199` burn script "the protocol collects nothing" | proven (code) |
| Price formula x·y = k | `gbx_curve.h:46-123` | proven (code) |
| Creating a coin needs proof-of-work for THAT coin, 32× easier than a block, proof must be < 100 blocks old | `gbx_launchpad.h:53-55` (`CREATE_POW_SHIFT = 5`, `CREATE_POW_MAX_AGE = 100`) | proven (code) |
| No minimum in money to create; first buy mandatory | `gbx_launchpad.h:30-35` (`CURVE_MIN_DEV_BUY_SAT = 1`) | proven (code) |
| Idle curve refundable after 864,000 blocks (30 days at 3 s) | `gbx_launchpad.h:80`, `chainparams.cpp:114` | proven (code) |
| Only 7 operations exist: create, buy, sell, refund, graduate, pool-buy, pool-sell — **no withdraw** | `gbx_launchpad.h:27` `enum class CurveOp` | proven (code) |
| Sell rate limits / per-address caps | in `lp-box` (liquidity-gateway software run by each LP), **not** in consensus | proven (location) — say "in the gateway software" |

## B. On other blockchains (public RPCs)

| Claim | How we checked | Result | Confidence |
|---|---|---|---|
| Solana swap program can never be upgraded | Solana RPC `getAccountInfo` on program `AAbKiRpmY5jYfC37DuQ9aTsWnNqxZXLe4fvyGSb3YS1F` → ProgramData `3BVHXX3SKP9Z9hDe5SoiRP8TCNHd9kFK9va1JyXd4k7Q` | `"authority": null` (slot 472,189,831) | **proven** |
| Base swap contract exists, no owner | `eth_getCode` + `eth_call owner()` on Base `0x8e351c32dfb27aa22334a20dcf7262f54f78e0c0` | 3,419 bytes of code; `owner()` reverts | **proven** |
| Arbitrum swap contract exists, no owner | same on Arbitrum `0xa43813d90adb98a5c400113ce2cc29d43d4ab867` | 3,419 bytes; `owner()` reverts | **proven** |
| Same code on both chains | byte comparison of the two deployments | identical except two 32-byte windows (bytes 1394–1425 and 1703–1734) = the per-chain domain separator, as the README explains | **proven** (README says 1702–1733 for the second window: off by one) |
| GATE-R.md lists the Base address | `docs/GATE-R.md` writes `0x8e35…dcf7272f…` | **no contract at that address** (code 0x, 0 transactions); the evm-htlc README's `…dcf7262f…` is the real one | **mismatch** — a typo in the project's exit document |

## C. Permanent archives (Arweave)

| Claim (GATE-R.md) | How we checked | Result | Confidence |
|---|---|---|---|
| core-final archive SHA-256 `bd5cdf3e…a330c5a2` | downloaded `arweave.net/xsVFhwVA…` (13,760,615 bytes), `sha256sum` | exact match; its `src/consensus/` is identical to GitHub's | **proven** |
| tools-final archive SHA-256 `368814f0…f3b6585a` | downloaded via `arweave.net/raw/nVkgMqVS…` and `ar-io.net` (73,839,074 bytes) | exact match | **proven** |

## D. The GoldBrix chain itself — NOT checked

| Claim | Why not checked | Confidence |
|---|---|---|
| Treasury ≈ 469,910.85 GBX burned on 25 Aug 2026 (tx `0cce2e8e…`) | public nodes unreachable from our server on 21 Nov 2026 (goldbrix.app: connection reset; one node's API answered 502) | claimed |
| Network-wide burn total, node count, pool fee 0 in practice | same | claimed |
| No premine, no presale | needs the chain from genesis | claimed |

How a viewer can check D themselves: any node's `/v3/explorer.html` and `/api/burns`, or run a node (`run-node/install-node.sh`).

## E. Size and context
- GitHub: 3 public repositories, 3–4 stars each (21 Nov 2026). No third-party security audit found.
- Founder: anonymous ("Gideon Brick"); project marked "finalized" on 25 Aug 2026.
