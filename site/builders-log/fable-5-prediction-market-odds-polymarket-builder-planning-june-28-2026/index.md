# The Fable 5 Odds: $3.13M in Prediction Market Volume Tells Builders What Government Sources Won't

> Polymarket traders have put $3.13M on Fable 5's return timeline. The market gives 43% odds of restoration by July 1 and 72.5% by July 10. Here is how to read the numbers — and why two markets can show 9% and 43% for the same week.


When the government restricts a frontier model and keeps its timeline private, prediction markets fill the information gap. $3.13 million in Polymarket volume has priced Claude Fable 5's return every day from June 29 through December 31, 2026.

Here is what the market is saying — and how builders should interpret it.

---

## The Polymarket Numbers, as of June 28

Polymarket tracks "Claude Fable 5 restored for US customers" across multiple resolution dates. Current odds:

| Date | Probability |
|------|-------------|
| June 29 | 34.5% |
| June 30 | 41.5% |
| July 1 | 43.0% |
| July 10 | 72.5% |
| July 17 | 83.5% |
| July 31 | 92.3% |
| August 31 | 94.9% |
| December 31 | 98.3% |

The market has seen $3.13M in total volume, $322K in current liquidity, and $637K in open interest. That is not casual speculation — builders and traders with real money have spent the past two weeks pricing these outcomes.

---

## The Axios Test

On June 27, [Axios reported](https://www.axios.com/2026/06/27/anthropic-fable-5-return-soon) that insider sources expect Fable 5 to return "as soon as this coming week" — the business week beginning June 30.

The market's response to that signal: July 1 sits at 43%.

That means traders give the Axios scoop less than a coin flip. They are taking the insider report seriously — June 29 was at 13% before the Axios article dropped — but they are also discounting it. Anonymous government sources have been wrong about Fable 5 timelines before. The odds reflect that uncertainty.

The remaining gate is Pentagon and NSA sign-off, neither of which has been publicly confirmed. Those agencies operate on their own timelines, and Axios's sources do not have visibility into their review schedule.

---

## The July 10 Zone

The clearest consensus in the market is the July 10 window at 72.5%. This is where traders see the most likely restoration zone — past the immediate "this week" window but before the end of July.

Why July 10? A few anchors:

**The July 8 date.** [Anthropic's privacy policy update](/builders-log/anthropic-fable-5-july-8-biometric-verification-persona-consumer-builder-guide/) — which adds biometric and identity verification mechanisms — takes effect July 8. This date was flagged in the June 12 directive as relevant to compliance review. If those verification mechanisms satisfy the government's conditions, access could resume shortly after.

**Standard review timelines.** Pentagon and NSA security reviews for novel AI capabilities typically run four to six weeks. The June 12 directive is now 16 days old. July 10 puts that review at 28 days — plausible for an accelerated track.

**Political pressure.** Commerce and Treasury have both been working to restore access. The longer the suspension runs, the more pressure accumulates from the industry side of those departments.

---

## Why Two Markets Show Different Odds

You may have seen Manifold Markets put Fable 5 restoration at around 9% by June 30, while Polymarket shows 41.5% for the same approximate date. These are not conflicting reads on the same question — they are pricing different questions.

**Polymarket resolution:** "Claude Fable 5 is restored for US customers." This resolves YES if US-based subscribers can access the model, even with nationality restrictions still in place.

**Manifold resolution:** "Generally available to every customer on a sufficiently high plan, regardless of nationality." This resolves YES only if the foreign-national restriction is fully lifted — meaning a French builder using the Claude API can access Fable 5 the same as an American one.

These are very different outcomes. The Manifold question is asking whether Anthropic wins the full restoration, including lifting the nationality-based restriction that was the core of the June 12 directive. The Polymarket question is asking whether US users get access back, even if non-US users are still blocked.

For most US-based builders, the Polymarket resolution criteria is what matters. For builders with non-US team members, international users, or products that need consistent global API access, the Manifold criteria is closer to your real requirement.

---

## The Historical Movement

The Polymarket contract was not always this pessimistic about near-term dates. On June 18 — when early restoration rumors circulated — the market briefly hit 73% for a pre-July-1 resolution. By June 20, the same contract had fallen to 41% after no announcement materialized.

This volatility should calibrate how much weight you give any single data point. The market is pricing a government process that is opaque, politically sensitive, and subject to agency-level review cycles that do not follow normal corporate timelines. The $3.13M in volume shows this matters to a lot of people; the price swings show that even well-capitalized traders have been wrong about timing multiple times.

---

## What This Tells Builders

**If you are a US-only builder:** The market gives you roughly even odds of restoration within the next two or three business days, and 72.5% odds by July 10. If you need to make planning decisions now, the market is saying: build assuming Fable 5 returns in the second week of July, treat anything sooner as a bonus.

**If you need global access:** You are betting on the harder question — the one Manifold is pricing at 9% for June 30. The market's July 31 odds for full restoration (92.3% on Polymarket's US-only question) do not translate directly to your situation. Build contingency plans that extend through August.

**On the competitive gap:** GPT-5.6 Sol is also government-restricted (approximately 20 approved companies, no general access). If Fable 5 returns in the July 10 zone, it comes back ahead of Sol reaching general availability. That window matters if you want to establish Fable 5 integrations before Sol becomes a direct comparison option for your users.

**On the partial-restore ambiguity:** Polymarket's contract notes that settlement could be contested if Anthropic releases Fable 5 in a limited form — waitlist only, specific plan tiers, or enterprise-only access. If the first restoration looks like Mythos 5's restoration (a defined set of 100+ organizations), the market may resolve YES while you still cannot access the model. Read the release announcement carefully before concluding full access is available.

---

**Previous coverage in this series:**
- [Day 17: Axios Says Return "As Soon as This Coming Week"](/builders-log/fable-5-day-17-return-imminent-builder-action-week-june-28-2026/) — June 28
- [Day 16: Mythos 5 Critical Infrastructure Restored, Garbarino Demo](/builders-log/anthropic-fable-5-day-16-mythos-critical-infrastructure-garbarino-demo-builder-guide/) — June 27

