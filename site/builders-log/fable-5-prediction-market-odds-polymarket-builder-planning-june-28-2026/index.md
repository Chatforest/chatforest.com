# The Fable 5 Odds: What Prediction Markets Actually Priced In, Corrected Against the Raw Data

> Polymarket's own price history shows Claude Fable 5 restoration odds at 29% for July 1 and 67% for July 10 on June 28 — not the higher figures first reported here. A Manifold market on full global restoration sat near 9%. Corrected against primary sources.


**Update (2026-07-31):** By July 1, 2026, the Commerce Department lifted the export controls and Anthropic restored Fable 5 for US customers — Polymarket's "by July 1" contract resolved YES ([Anthropic: Redeploying Fable 5](https://www.anthropic.com/news/redeploying-fable-5); [CNBC](https://www.cnbc.com/2026/06/30/anthropic-says-trump-admin-has-lifted-export-controls-on-claude-fable-5-and-mythos-5.html)). This piece is kept as a record of what prediction markets were actually pricing on June 28, before that outcome was known. **A 2026-07-31 citation audit found the original odds table did not match the market's own historical price data** — several figures were pulled from an earlier, more optimistic moment in the market's history rather than the June 28 snapshot the piece claimed. The numbers below have been corrected directly against [Polymarket's own price-history data](https://polymarket.com/event/claude-fable-5-restored-for-us-customers-by-20260613193753196) for the market in question.

When the government restricts a frontier model and keeps its timeline private, prediction markets fill the information gap. Multi-million-dollar Polymarket volume priced Claude Fable 5's return every day from June 29 through December 31, 2026.

Here is what the market was actually saying on June 28 — and how builders should have interpreted it.

---

## The Polymarket Numbers, as of June 28

Polymarket tracks ["Claude Fable 5 restored for US customers"](https://polymarket.com/event/claude-fable-5-restored-for-us-customers-by-20260613193753196) across multiple resolution dates. Pulled directly from the market's own price-history data at roughly midday UTC on June 28:

| Date | Probability |
|------|-------------|
| June 29 | 9.5% |
| June 30 | 16.5% |
| July 1 | 29.0% |
| July 10 | 67.0% |
| July 17 | 78.5% |
| July 31 | 91.8% |
| August 31 | 94.7% |
| December 31 | 98.3% |

[CryptoSlate's tracking](https://cryptoslate.com/predictions/market/claude-fable-5-restored-for-us-customers/) of this market put volume at roughly $2.3M, liquidity around $329K, and open interest near $615K during this stretch. That is not casual speculation — builders and traders with real money were pricing these outcomes daily. Volume kept climbing after June 28; the market closed at $5.43M in total volume when the contracts resolved on July 2 ([Polymarket](https://polymarket.com/event/claude-fable-5-restored-for-us-customers-by-20260613193753196)).

---

## The Axios Test

On June 27, [Axios reported](https://www.axios.com/2026/06/27/anthropic-fable-5-return-soon) that insider sources expect Fable 5 to return "as soon as this coming week" — the business week beginning June 30.

The market's response to that signal: July 1 sat at 29% by midday June 28, per [Polymarket's own price history](https://polymarket.com/event/claude-fable-5-restored-for-us-customers-by-20260613193753196).

That means traders were giving the Axios scoop well under a coin flip. And the direction is telling: the July 1 contract had already fallen sharply from a mid-June peak (see below) *before* Axios published, and it kept fading afterward rather than rallying on the scoop. Anonymous government sources have been wrong about Fable 5 timelines before, and traders appear to have priced that skepticism in rather than betting on the insider report.

The remaining gate is Pentagon and NSA sign-off, neither of which had been publicly confirmed as of June 28 ([Axios](https://www.axios.com/2026/06/27/anthropic-fable-5-return-soon)). Those agencies operate on their own timelines, and Axios's sources did not have visibility into their review schedule.

---

## The July 10 Zone

The clearest consensus in the market is the July 10 window at 67%, per Polymarket's price history for that contract. This is where traders saw the most likely restoration zone — past the immediate "this week" window but before the end of July.

Why July 10? A few anchors:

**The July 8 date.** [Anthropic's privacy policy update](/builders-log/anthropic-fable-5-july-8-biometric-verification-persona-consumer-builder-guide/) — which adds biometric and identity verification mechanisms — takes effect July 8. This date was flagged in the June 12 directive as relevant to compliance review. If those verification mechanisms satisfy the government's conditions, access could resume shortly after.

**Still-pending review.** As of June 28, Axios reported that Pentagon and NSA sign-off remained outstanding, with no review timeline disclosed publicly ([Axios](https://www.axios.com/2026/06/27/anthropic-fable-5-return-soon)). The June 12 directive was 16 days old by June 28.

**Political pressure.** Commerce Secretary Howard Lutnick and Treasury Secretary Scott Bessent were both directly involved in the negotiations that ultimately led Commerce to lift the export controls ([CNBC](https://www.cnbc.com/2026/06/30/anthropic-says-trump-admin-has-lifted-export-controls-on-claude-fable-5-and-mythos-5.html)). The longer the suspension ran, the more pressure accumulated from the industry side of those departments.

---

## Why Two Markets Show Different Odds

You may have seen [Manifold Markets](https://manifold.markets/PhilipDowdell/will-anthropic-restore-access-to-fa) put Fable 5 restoration at around 9% by June 30 (confirmed directly against Manifold's own bet history for that market), while [Polymarket](https://polymarket.com/event/claude-fable-5-restored-for-us-customers-by-20260613193753196) showed 16.5% for its US-customers contract for the same approximate date. These are not conflicting reads on the same question — they are pricing different questions.

**Polymarket resolution:** "Claude Fable 5 is restored for US customers." This resolves YES if US-based subscribers can access the model, even with nationality restrictions still in place.

**Manifold resolution:** ["Will Anthropic restore access to Fable 5 to all customers by the end of June?"](https://manifold.markets/PhilipDowdell/will-anthropic-restore-access-to-fa) — resolves YES only if Fable 5 is "generally available to every customer on a sufficiently high plan, regardless of nationality." That means the foreign-national restriction must be fully lifted — a French builder using the Claude API would need to be able to access Fable 5 the same as an American one.

These are very different outcomes. The Manifold question is asking whether Anthropic wins the full restoration, including lifting the nationality-based restriction that was the core of the June 12 directive. The Polymarket question is asking whether US users get access back, even if non-US users are still blocked.

For most US-based builders, the Polymarket resolution criteria is what matters. For builders with non-US team members, international users, or products that need consistent global API access, the Manifold criteria is closer to your real requirement.

---

## The Historical Movement

The Polymarket contract was not always this pessimistic about near-term dates. Around June 18-19 — when early restoration rumors circulated — the July 1 contract spiked as high as 73-77% ([Prediction News](https://predictionnews.com/story/polymarket-odds-hit-73-that-claude-fable-5-returns-to-us-customers-before-july-1); [Binance](https://www.binance.com/en/square/post/06-19-2026-polymarket-odds-rise-to-73-that-claude-fable-5-will-return-to-u-s-customers-before-july-1-335677172136417)). It cooled only gradually at first — still around 65-67% on June 20, per the market's own price history — before fading hard over the following week to the 29% level seen on June 28. No single announcement caused the slide; it was a steady deflation as no confirmation materialized.

This volatility should calibrate how much weight you give any single data point. The market is pricing a government process that is opaque, politically sensitive, and subject to agency-level review cycles that do not follow normal corporate timelines. Multi-million-dollar volume shows this matters to a lot of people; the price swings show that even well-capitalized traders have been wrong about timing multiple times.

---

## What This Tells Builders

**If you are a US-only builder:** The market gave you just under 3-in-10 odds of restoration within the next two or three business days, and 67% odds by July 10. If you needed to make planning decisions on June 28, the market was saying: don't count on the Axios-reported "this week" scenario — build assuming Fable 5 returns in the second week of July, and treat anything sooner as a bonus.

**If you need global access:** You are betting on the harder question — the one Manifold was pricing at 9% for June 30 ([Manifold](https://manifold.markets/PhilipDowdell/will-anthropic-restore-access-to-fa)). The market's July 31 odds for full US-only restoration (91.8% on Polymarket's US-only question) do not translate directly to your situation. Build contingency plans that extend through August.

**On the competitive gap:** [GPT-5.6 Sol was also government-restricted](https://techcrunch.com/2026/06/26/openai-limits-gpt-5-6-rollout-after-government-request-says-restrictions-shouldnt-be-the-norm/) at the time (approximately 20 approved companies, no general access — also reported by [TheNextWeb](https://thenextweb.com/news/openai-gpt-5-6-sol-limited-preview-government-approved-partners)). If Fable 5 returned in the July 10 zone, it would come back ahead of Sol reaching general availability. That window mattered for builders wanting to establish Fable 5 integrations before Sol became a direct comparison option for their users.

**On the partial-restore ambiguity:** Polymarket's contract notes that settlement could be contested if Anthropic releases Fable 5 in a limited form — waitlist only, specific plan tiers, or enterprise-only access. If the first restoration looked like Mythos 5's restoration (a defined set of roughly 100 US organizations, restored June 26 for critical-infrastructure defense per Commerce Secretary Lutnick's letter — [TechTimes](https://www.techtimes.com/articles/319213/20260628/claude-fable-5-still-offline-us-clears-mythos-5-critical-infrastructure.htm)), the market could resolve YES while some builders still couldn't access the model. Reading the release announcement carefully before concluding full access is available remained the safest move.

---

**Previous coverage in this series:**
- [Day 17: Axios Says Return "As Soon as This Coming Week"](/builders-log/fable-5-day-17-return-imminent-builder-action-week-june-28-2026/) — June 28
- [Day 16: Mythos 5 Critical Infrastructure Restored, Garbarino Demo](/builders-log/anthropic-fable-5-day-16-mythos-critical-infrastructure-garbarino-demo-builder-guide/) — June 27

