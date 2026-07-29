# Coinbase SPCX-PERP: Pre-IPO Perpetuals Launch for SpaceX — and AI Startup Exposure Is Next

> Coinbase launched SPCX-PERP on June 4 — the first contract in a planned pipeline of pre-IPO perpetual futures for international investors. Here's how it works, what happens at the June 12 IPO conversion, and why OKX and Crypto.com are already listing OpenAI and Anthropic perps.


Coinbase [launched SPCX-PERP on June 4, 2026](https://www.coinbase.com/blog/pre-ipos-are-launching-on-coinbase-starting-with-spacex) — a pre-IPO perpetual futures contract on SpaceX equity, available to international users through the Coinbase International Exchange. [CNBC confirmed](https://www.cnbc.com/2026/06/04/investors-can-buy-spacex-early-with-coinbase-perpetual-futures-on-pre-ipos.html) the product details including the 5x max leverage and USDC settlement structure.

This is the first contract in what [Coinbase has explicitly described](https://www.coinbase.com/blog/pre-ipos-are-launching-on-coinbase-starting-with-spacex) as a planned pipeline of pre-IPO perpetuals spanning technology, AI, energy, and space. The AI implication is direct: [OKX](https://www.okx.com/en-us/help/okx-to-list-pre-ipo-pre-market-perpetual-futures-for-spacex-usdt-openai-usdt-and-anthropic-usdt) and [Crypto.com](https://crypto.com/en/research/pre-ipo-perps-may-2026) have already listed perpetual contracts tracking OpenAI, Anthropic, and SpaceX valuations. Coinbase's entry adds a regulated, SEC-adjacent exchange brand to a product category that previously existed mainly on offshore derivatives platforms outside US oversight.

If you are building in the AI space, this matters less as a trading opportunity and more as a signal: AI startup equity is becoming a tradable crypto-native asset class, and the pre-IPO speculation market is now accessible months before any S-1 becomes public.

---

## What SPCX-PERP Is

SPCX-PERP is a USDC-settled perpetual futures contract offered through [Coinbase Bermuda Ltd.](https://www.coindesk.com/business/2023/04/20/crypto-exchange-coinbase-receives-license-to-operate-in-bermuda), which holds a Class F digital-asset license from the Bermuda Monetary Authority, on the Coinbase International Exchange. It tracks SpaceX's pre-IPO valuation, calibrated to the [$135-per-share IPO price SpaceX disclosed in its S-1 Amendment No. 1 on June 1](https://unchainedcrypto.com/coinbase-debuts-pre-ipo-perpetual-futures-on-international-exchange-starting-with-spacex-ahead-of-june-12-listing/), a price later [confirmed by CNBC](https://www.cnbc.com/2026/06/03/spacex-ipo-stock-price-roadshow-musk.html) as the fixed IPO price for its 555.6 million-share offering.

Key product specs:

| Feature | Details |
|---------|---------|
| Settlement | USDC |
| Expiry | None (perpetual) |
| Maximum leverage | 5x |
| Position limit at 2x | Up to $350,000 notional |
| Position limit at 5x | Up to $200,000 notional |
| Total notional cap | $60 million across all positions above default leverage |
| Market hours | 24/7 |
| Availability | International users only — NOT available to US persons |

*Specs per [CryptoTimes](https://www.cryptotimes.io/2026/06/04/coinbase-lists-spacex-pre-ipo-perpetuals-after-spcx-sets-135-price/) and [Coinbase's own pre-IPO perpetuals help documentation](https://help.coinbase.com/en/international-exchange/pre-ipo-markets/what-are-pre-ipo-perpetual-futures).*

The 5x maximum is lower than the [10x Coinbase offers](https://www.cryptotimes.io/2026/06/04/coinbase-lists-spacex-pre-ipo-perpetuals-after-spcx-sets-135-price/) on its existing stock perpetual futures for already-listed companies. The lower cap reflects the higher basis risk of a pre-IPO contract.

---

## Who Can Use This

**Not available to US persons.** The contract is offered through [Coinbase Bermuda Ltd.](https://www.coindesk.com/business/2023/04/20/crypto-exchange-coinbase-receives-license-to-operate-in-bermuda) under Bermuda regulatory frameworks. US residents and citizens are explicitly excluded regardless of where they hold accounts.

For international builders and investors — particularly in Europe, Asia, Latin America, and parts of the Middle East — this opens a route to speculate on SpaceX's public market debut without waiting for June 12 and without accessing US brokerage platforms that have their own allocation constraints.

The product requires a Coinbase International Exchange account (separate from standard Coinbase accounts) with identity verification complete.

---

## What Happens at the June 12 IPO

SpaceX is set to [begin trading on Nasdaq under the ticker SPCX on June 12](https://www.cnbc.com/2026/06/03/spacex-ipo-stock-price-roadshow-musk.html). At that point, the pre-IPO perpetual converts into a standard per-share equity perpetual future.

The conversion process, [per Coinbase](https://help.coinbase.com/en/international-exchange/pre-ipo-markets/what-are-pre-ipo-perpetual-futures) and [confirmed by Unchained](https://unchainedcrypto.com/coinbase-debuts-pre-ipo-perpetual-futures-on-international-exchange-starting-with-spacex-ahead-of-june-12-listing/):

1. Coinbase pauses SPCX-PERP trading when the final 424B4 prospectus is filed with the SEC
2. Open orders are cancelled
3. A five-minute TWAP (time-weighted average price) bridges the contract from the pre-IPO valuation index to the live SPCX equity price feed
4. Trading resumes as a standard equity perpetual future
5. The conversion is designed to be P&L-neutral for existing position holders

In practice, this means holders of SPCX-PERP before June 12 are expressing a view on whether SpaceX will open above or below $135. If SPCX opens at $160, a long SPCX-PERP position benefits. If it opens at $110, it does not.

---

## The Risk Profile

Pre-IPO perpetuals carry risks distinct from standard equity derivatives:

**Basis risk.** The pre-IPO valuation index is constructed from secondary market trades, reported fundraising rounds, and implied valuations — not a live exchange price. The gap between the index and the eventual IPO price can be material. SpaceX's IPO was structured as a [fixed-price offering at $135 per share](https://www.tradingkey.com/analysis/stocks/us-stocks/261957856-spacex-ipo-at-135-what-the-s-1-financials-actually-say-tradingkey) rather than a traditional multi-week bookbuild range, so pre-IPO perpetual holders had a shorter window of public price signals to gauge basis risk against before the June 12 open.

**Funding rate risk.** Perpetual futures use funding rates to keep the contract price anchored near the index. In a highly bullish environment, the funding rate paid by longs to shorts can be substantial — particularly over the days leading up to an IPO when speculative demand spikes.

**Conversion uncertainty.** The 5-minute TWAP conversion is designed to be neutral, but TWAP-based conversions during high-volatility events (IPO open) carry execution risk. If SPCX opens with significant price discovery volatility in the first minutes, the TWAP window may bridge at a price that diverges from the "true" open.

**Leverage amplification.** At 5x, a 20% adverse move wipes out the full position. Pre-IPO contracts can move significantly in response to news about IPO pricing, book demand signals, and macro conditions. The [SPCX roadshow runs June 4–11](https://www.cnbc.com/2026/06/03/spacex-ipo-stock-price-roadshow-musk.html), with final pricing set the evening of June 11 ahead of the June 12 debut; pricing news during this window will move the perpetual.

**Counterparty and regulatory risk.** Coinbase Bermuda Ltd. is regulated in Bermuda. International regulatory frameworks for crypto derivatives vary significantly. Non-US users should verify their own jurisdiction's treatment of perpetual futures contracts.

---

## The AI Startup Pipeline

[Coinbase said](https://www.coinbase.com/blog/pre-ipos-are-launching-on-coinbase-starting-with-spacex) SpaceX is "only the first listing in a planned pipeline of pre-IPO perpetual futures spanning technology, artificial intelligence, energy, and space sectors."

Two other major crypto exchanges have already moved ahead:

**OKX** has [launched perpetual futures contracts](https://www.okx.com/en-us/help/okx-to-list-pre-ipo-pre-market-perpetual-futures-for-spacex-usdt-openai-usdt-and-anthropic-usdt) tracking OpenAI, SpaceX, and Anthropic. On OpenAI: the company was [last privately valued at $852 billion](https://openai.com/index/accelerating-the-next-phase-ai/) after closing a $122 billion funding round in March 2026, and the Wall Street Journal [reported in May 2026](https://www.forbes.com/sites/aliciapark/2026/05/20/openai-reportedly-could-file-for-ipo-this-week-teeing-up-showdown-with-musks-spacex/) that OpenAI was targeting a confidential S-1 filing and a September 2026 public listing at a valuation that could top $1 trillion — though OpenAI has not confirmed a specific listing date. On Anthropic: the company [confidentially submitted a draft S-1 to the SEC on June 1, 2026](https://www.anthropic.com/news/confidential-draft-s1-sec), days after a $65 billion Series H round that [pushed its valuation to $965 billion](https://techcrunch.com/2026/06/01/anthropic-files-to-go-public/); Bloomberg has since reported bankers are targeting a possible October 2026 listing, though Anthropic itself has said timing "will depend on market conditions and other factors."

**Crypto.com** [launched Pre-IPO Perpetual Contracts](https://crypto.com/en/research/pre-ipo-perps-may-2026), [available to eligible institutional clients upon request](https://goodmoneyguide.com/usa/crypto-com-launches-pre-ipo-perpetuals/), covering OpenAI, SpaceX, and Anthropic.

**Binance** [launched SpaceX pre-IPO perpetuals in a press release on May 21, 2026](https://www.prnewswire.com/news-releases/binance-launches-perpetual-futures-for-pre-ipo-market-exposure-starting-with-spacex-302778513.html) — before Coinbase's June 4 SPCX-PERP launch — and Coinbase explicitly positions its product as entering a market Binance already opened.

The pattern is clear: ahead of the most anticipated AI IPO wave in history — SpaceX (June 12), OpenAI (September), Anthropic (October) — crypto exchanges are building infrastructure to let international investors speculate on outcomes before shares are available to buy on traditional exchanges.

---

## What This Means for AI Builders

Most AI builders are not trading derivatives on private company equity. This article is not a recommendation to do so.

But the emergence of this product class matters as context:

**AI startup equity is now a global trading asset.** The presence of SPCX-PERP, Anthropic perps, and OpenAI perps on multiple exchanges means that price signals are flowing back to the companies themselves before they go public. This creates feedback loops between developer sentiment, investor speculation, and platform strategy decisions that didn't exist two years ago.

**Anthropic's valuation momentum affects its API strategy.** [Anthropic filed a confidential S-1 on June 1](https://www.anthropic.com/news/confidential-draft-s1-sec) [at a ~$965B valuation](https://techcrunch.com/2026/06/01/anthropic-files-to-go-public/). Public market pressure — especially if SPCX trades well on June 12 — will shape how aggressively Anthropic pursues enterprise contracts and API pricing in Q3. A successful SpaceX IPO may pull Anthropic's timeline forward.

**If you work outside the US**, the traditional route to AI startup exposure (secondary markets, AngelList, accredited investor funds) is expensive and illiquid. Pre-IPO perpetuals on regulated exchanges like Coinbase's Bermuda platform are a qualitatively different kind of access — albeit a derivatives instrument rather than ownership.

**The conversion date matters.** SPCX-PERP converts to an equity perpetual on June 12. If you are building anything that involves SpaceX infrastructure — Starlink connectivity, orbital compute, Colossus cluster access via the [SpaceX-xAI merger](https://x.ai/news/xai-joins-spacex) that [closed February 2, 2026](https://www.cnbc.com/2026/02/03/musk-xai-spacex-biggest-merger-ever.html) — the IPO outcome establishes the public market signal on whether the AI infrastructure buildout is investor-endorsed. Watch the first-day performance for the same reason you watch HFCE on June 9.

---

## At a Glance: The Pre-IPO Perps Landscape

| Exchange | Available Contracts | Users |
|----------|-------------------|-------|
| Coinbase International (Bermuda) | SPCX-PERP | International (non-US) |
| OKX | OpenAI, SpaceX, Anthropic | International |
| Crypto.com | OpenAI, SpaceX, Anthropic | Eligible institutional clients |
| Binance | SpaceX | International |

---

## Related Coverage

- [SPCX Roadshow: What's Actually Happening Between Now and June 12](/builders-log/spacex-spcx-ipo-roadshow-week-june-4-12-what-to-watch/)
- [How to (Actually) Buy SPCX — Platform-by-Platform Retail Guide](/reviews/spacex-ipo-spcx-retail-investor-guide-how-to-buy-2026/)
- [SpaceX S-1: AI Infrastructure, Colossus, and xAI](/reviews/spacex-ipo-s1-ai-infrastructure-colossus-xai-anthropic-2026/)
- [Anthropic S-1: Builder API Implications](/builders-log/anthropic-s1-ipo-confidential-filing-june-2026-builder-api-implications/)
- [Hugging Face IPO June 9: What HFCE Means for Open-Source AI](/builders-log/hugging-face-ipo-june-9-hfce-nasdaq-open-source-ai-builder-guide/)

