# Script: We Fact-Checked a Crypto That Says It Has No Owner
Video: L01 · Structure: **Autopsy as an audit** (12 claims → check → result) · Hook type: 2 (contradiction) + 7 (public secret) · Target ~11 min
Narration words: see header count after TTS. Twist: the claims we could test held up — but the project's own exit document has a typo, and the claims that matter most for trust (treasury burn, no premine) we could not verify because its servers didn't answer.
Rules for this video (CLAUDE.md, crypto exception): neutral, "the code says / the project says", no price, no returns, no "buy", no app link; risk line in the ending; no named project called a scam — only what official bodies found.
Sources: `research-evidence.md` (our own checks) and `research-compare.md` (market data).

---

## VOICE-READY narration (paste into the voice tool, one ¶ at a time)

**[HOOK]**

¶1 In twenty twenty-four, about two million new crypto tokens were launched. Chainalysis flagged roughly seventy-four thousand of them for pump-and-dump patterns. And in about ninety-four percent of those suspicious pools, the money was pulled out by the same person who created them.

¶2 Now here's a small crypto called GoldBrix. It says it was built so that can't happen. No owner. No company. No admin key. Every fee burned. [pause] Every scam says nice things about itself. So we didn't listen to what it says. We checked.

¶3 Twelve claims. We tested them against the source code, three other blockchains, and the project's own archives. By the end, you'll see which ones held up, which ones we couldn't check, and the mistake we found in its own paperwork. Let's open it up.

**[CHAPTER 1 — Why "trust us" isn't enough]**

¶4 First, the normal way this works. The biggest memecoin launchpad, Pump fun, listed a fee of one point two five percent per trade in September twenty twenty-five. Point nine five percent went to the platform, point three to the coin's creator. According to DefiLlama, Pump's products have brought in about one point four billion dollars in revenue since March twenty twenty-four. That's not a crime. It's a business. The fee goes to somebody.

¶5 Then there's what happens after launch. Binance Research found that tokens launched in twenty twenty-four had, on average, only about twelve percent of their value actually circulating. The rest was locked up, often for teams and early investors, to be released later.

¶6 And sometimes "locked" doesn't mean locked. SafeMoon told investors its liquidity was locked. US prosecutors said insiders kept access to the pools and took tokens out. In May twenty twenty-five, a jury convicted its CEO. In February twenty twenty-six, he was sentenced to one hundred months in prison.

¶7 That's the lesson for this whole video. "Locked", "burned", "no owner" are just words. The only thing that counts is what the code allows, and what the blockchain shows. So, claim number one.

**[CHAPTER 2 — The supply]**

¶8 GoldBrix says there will only ever be fifteen million coins. In its source code, there's a constant called max money. Its value: fifteen million coins. No transaction can create more than that.

¶9 But a cap is only honest if the issuing schedule actually adds up to it. So we did the math. The first twenty thousand blocks paid fifty coins each. That's one million. Then blocks speed up to one every three seconds, paying a quarter coin, and the reward halves every twenty-eight million blocks, about every two point seven years. Seven million, then three and a half, then one point seven five, and so on, adding up to fourteen million. Plus the first million. [pause] Exactly fifteen million. Claims one and two: checked.

¶10 For comparison, Bitcoin caps at twenty-one million, with blocks about every ten minutes, halving every two hundred ten thousand blocks. Same idea, different clock.

**[CHAPTER 3 — The launchpad rules]**

¶11 Now the part that's supposed to make GoldBrix different: its launchpad, where anyone can create a coin. Claim three: every fee is burned.

¶12 Here are the two lines of code. A fee of half a percent on the bonding curve, and three tenths of a percent on the pool after a coin graduates. Next to both, the developers wrote: burned, never collected. And it's not just a comment. The network checks it. A trade that doesn't send its fee to the burn address gets rejected, with an error literally called bad fee. Checked.

¶13 Claim four: creating a coin costs work, not money. To create a coin, your device has to do proof-of-work for that specific coin, thirty-two times easier than mining a block, and the proof must be less than a hundred blocks old. The minimum amount of money is one satoshi, the smallest unit there is. A big wallet can't skip the work. Checked.

¶14 Claim five: everyone pays by the same formula. It's x times y equals k. Picture a pool with one hundred coins and one hundred tokens. Before fees, buying ten tokens costs about eleven coins. Buying fifty costs one hundred. [pause] The more you take, the more each one costs. Same formula for a tiny trade and a huge one. Checked.

¶15 Claim six: if a coin dies, you can get out. If a coin's curve sees no trades for eight hundred sixty-four thousand blocks, refunds open. At three seconds a block, that's exactly thirty days. It's in the code. Checked.

¶16 Quick question before we go on. What's the one thing you'd check first before trusting any crypto? Tell us in the comments. We read them.

**[CHAPTER 4 — Can anyone pull the money?]**

¶17 This is the claim that matters most. Can someone take the money out of a pool? So we went looking for the withdraw function.

¶18 Here is every operation the GoldBrix launchpad accepts. Create. Buy. Sell. Refund. Graduate. Pool buy. Pool sell. That's the whole list. There is no withdraw. If an operation isn't on this list, the network rejects it. Claim seven: checked.

¶19 Claim eight: nobody can rewrite history. The code rejects any reorganization deeper than one hundred blocks. At three seconds per block, that's about five minutes. After that, a transaction can't be undone by out-mining the network. Checked.

¶20 Every week, we take something you pay for apart, line by line, with the sources on screen. If that's your kind of video, subscribe.

**[CHAPTER 5 — Outside the chain]**

¶21 GoldBrix also lets people swap with USDC on three other blockchains. That's where a hidden admin key could hide. So we asked those blockchains directly.

¶22 Claim nine: on Solana, the swap program can never be changed. Every upgradeable Solana program has an upgrade authority, the key that can replace its code. We queried it. The answer: null. No key. Nobody can upgrade it. Checked.

¶23 Claim ten: on Base and Arbitrum, the swap contracts have no owner. We called the owner function on both. Both calls failed, because the function doesn't exist. Then we downloaded both contracts and compared them byte by byte. Three thousand three hundred fifty-five of three thousand four hundred nineteen bytes are identical. The other sixty-four are each chain's own signature domain, exactly as the project's documentation predicts. Checked.

¶24 Claim eleven: the final code is stored forever. The project says that when its founder left, the source was archived on Arweave, with its fingerprint published. We downloaded both archives and computed the SHA-256 hashes ourselves. Both matched, character for character. And the core rules inside are identical to the code on GitHub. Checked.

**[CHAPTER 6 — What we couldn't check, and the typo]**

¶25 Now the part most videos would skip. Claim twelve. The project says its anonymous founder, known as Gideon Brick, burned about four hundred seventy thousand coins from the treasury on August twenty-fifth, twenty twenty-six, and that there was never a premine. Those are claims about its own blockchain. We tried to check them. GoldBrix's public servers didn't answer us. So this one stays: not verified.

¶26 And the mistake. In the document describing the founder's exit, the Base contract address has a one-digit typo. At the address as written, there's no contract at all. The real one, listed in another file, is where we found the code. It's not a hidden key. But it's exactly the kind of detail you only catch by checking.

¶27 And there's a lot the code can't tell you. Whether anyone actually uses it. What it's worth, if anything. On GitHub, it has three repositories and a handful of stars. We found no independent security audit. And no owner cuts both ways. Nobody can rug it. Nobody can fix a bug either.

**[CHAPTER 7 — The verdict]**

¶28 So, the receipt. Twelve claims. Eleven checked and confirmed against the code and three other blockchains. One we couldn't verify. One typo in the paperwork. And no part of the fees we could trace goes to anyone.

¶29 Here's what that means, and what it doesn't. It means this project's rules are written where anyone can read them, and the ones we tested do what they say. It doesn't mean it's a good investment. Code that keeps its promises can still be worth nothing.

¶30 If you take one thing from this video, take the method. Before any crypto: who holds the keys? Where do the fees go? Did insiders get coins first? Can someone pull the liquidity? Can you read the code? Then check the answers yourself. This is not financial advice. Crypto is high risk, and you can lose everything.

¶31 If you like following the money, the airline video is even stranger: airlines earn billions from a credit card. That one's right here.

---

## Fact check

| Number / claim in script | Source row |
|---|---|
| 2,063,519 tokens in 2024; 74,037 (3.59%) pump-and-dump; ~94% of suspect pools emptied by creator | research-compare: Chainalysis 2024 |
| Pump.fun 1.25% (0.95% platform, 0.30% creator), Sep 2025 | research-compare: Pump.fun help page 26 Sep 2025 |
| ~$1.4B revenue since Mar 2024 (DefiLlama, to 20 Nov 2026) | research-compare: $1.41B |
| ~12% circulating at launch (12.3%), 2024 tokens | research-compare: Binance Research |
| SafeMoon: "locked"; insiders retained access; convicted 21 May 2025; 100 months 10 Feb 2026 | research-compare §6 (DOJ/IRS releases) |
| 15M cap (`MAX_MONEY`) | research-evidence A |
| 20,000 × 50; 0.25; 28M halving; 3 s; = 15,000,000; ≈ 2.7 years | research-evidence A + arithmetic |
| Bitcoin 21M, ~10 min, 210,000 blocks | research-compare: bitcoin.org |
| 0.50% / 0.30% burned; BAD_FEE | research-evidence A |
| 32× easier, < 100 blocks old, 1 satoshi | research-evidence A |
| x·y=k example 11.1 / 100 | S01 research (arithmetic) |
| 864,000 blocks = 30 days | research-evidence A |
| 7 operations, no withdraw | research-evidence A |
| reorg limit 100 blocks ≈ 5 min | research-evidence A |
| Solana authority null | research-evidence B |
| owner() reverts; 3,355 of 3,419 identical; 64 = domain separator | research-evidence B |
| Archives match SHA-256; consensus identical to GitHub | research-evidence C |
| ≈ 470,000 GBX treasury burn claim, 25 Aug 2026; nodes unreachable | research-evidence D |
| Typo in exit document | research-evidence B (mismatch) |
| 3 repos, a handful of stars; no audit found | research-evidence E |
