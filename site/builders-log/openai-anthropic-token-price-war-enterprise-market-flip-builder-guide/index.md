# OpenAI Is About to Cut Token Prices. Here's What Builders Should Do Before It Happens.

> Anthropic passed OpenAI in enterprise revenue and market share for the first time in May 2026. The Wall Street Journal reported OpenAI is weighing drastic price cuts in response. GPT-5.6 Luna at $1/$6 is the first signal. What builders should know before the next pricing announcement.


For the first time in the industry's history, [Anthropic passed OpenAI in enterprise AI market share](https://ramp.com/data/ai-index). [The Wall Street Journal reported on June 11 that OpenAI is weighing drastic token price cuts](https://www.cnbc.com/2026/06/11/openai-mulls-slashing-prices-ahead-of-competition-from-anthropic-wsj.html) in response. [GPT-5.6 Luna's $1 per million token input price — announced June 26](https://www.axios.com/2026/06/26/openai-gpt-sol-terra-luna-trump) — appears to be that response starting to land.

Here is what the market shift means, what price cuts are likely to look like, and what to do before the next announcement.

---

## How the Market Flipped

The clearest read on where enterprise money is flowing comes from Ramp's AI spending index, which tracks actual software purchasing across its business-card customer base.

**[May 2026 Ramp AI Index](https://ramp.com/data/ai-index):** Anthropic 34.4%, OpenAI 32.3% — the first time Anthropic has led.

A March 2026 Ramp figure drove the point harder: [Anthropic captured **73% of all enterprise spending among companies buying AI tools for the first time**](https://venturebeat.com/technology/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead/) that month — [up from a 50/50 split in January 2026](https://sherwood.news/tech/anthropic-capturing-73-of-first-time-enterprise-ai-spend-up-from-50-in/). That is the new-customer pipeline, the leading indicator for where total market share goes next.

Revenue followed the same direction. Anthropic's annualized revenue run rate went from [roughly $1 billion in January 2025](https://www.saastr.com/anthropic-just-hit-14-billion-in-arr-up-from-1-billion-just-14-months-ago/) to [**$47 billion by May 2026**, according to Anthropic's own announcement](https://www.anthropic.com/news/series-h) — a 47x increase in sixteen months. OpenAI grew in the same period from [$13.07 billion in full-year 2025 revenue](https://www.techspot.com/news/112794-openai-made-13-billion-2025-lost-21-billion.html) to [approximately **$25 billion** annualized by early 2026](https://finance.yahoo.com/news/openai-tops-25-billion-annualized-033836274.html) — still large, but roughly 2x growth while Anthropic posted 47x.

The valuation gap inverted on a similar timeline. Anthropic's [Series H closed at a $965 billion post-money valuation in late May 2026](https://www.anthropic.com/news/series-h), surpassing [OpenAI's $852 billion valuation from its March 2026 funding round](https://openai.com/index/accelerating-the-next-phase-ai/) — [the first time Anthropic has led on valuation](https://www.cnbc.com/2026/05/28/anthropic-open-ai-startup-value.html), ending a streak of OpenAI valuation leadership that dated to the company's founding.

The mechanism behind Anthropic's growth is not complicated: Claude Code adoption drove what [CEO Dario Amodei called "80x" annualized revenue growth in Q1 2026 — "crazy" and "too hard to handle"](https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth) against internal plans for 10x, putting Anthropic on track for [its first profitable quarter](https://winbuzzer.com/2026/05/21/anthropic-targets-first-profit-as-revenue-hits-109b-xcxwbn/) since the company's [January 2021 founding](https://en.wikipedia.org/wiki/Anthropic). The [$200/month Max plan](https://claude.com/pricing) converted a large base of individual developers into recurring revenue, and enterprise Claude Code licenses added API token billing on top of seat fees.

---

## OpenAI's Response

[The Wall Street Journal reported on June 11 that OpenAI is "preparing to slash the prices it charges for AI tokens"](https://www.cnbc.com/2026/06/11/openai-mulls-slashing-prices-ahead-of-competition-from-anthropic-wsj.html) with cuts aimed explicitly at winning customers from Anthropic. Sam Altman acknowledged that [costs had become "a huge issue"](https://www.forbes.com/sites/siladityaray/2026/06/11/openai-wants-to-slash-prices-after-altman-said-steep-costs-were-huge-issue-report-says/) for enterprise customers. No specific cut amounts, model targets, or timing were announced at time of reporting — discussions were "still in flux."

[GPT-5.6, which launched on June 26 as a limited preview for roughly 20 government-vetted organizations](https://techcrunch.com/2026/06/26/openai-limits-gpt-5-6-rollout-after-government-request-says-restrictions-shouldnt-be-the-norm/) following [a White House request to limit the initial rollout](https://www.axios.com/2026/06/26/openai-gpt-sol-terra-luna-trump), provides the first concrete pricing signal:

| Model | Role | Input per 1M | Output per 1M |
|-------|------|--------------|---------------|
| **Sol** | Frontier — agentic, coding, biology | $5.00 | $30.00 |
| **Terra** | Balanced — everyday work, 2x cheaper than GPT-5.5 | $2.50 | $15.00 |
| **Luna** | Fast, cheap — high-volume routine tasks | $1.00 | $6.00 |

*[Launch pricing as of June 26, 2026](https://www.axios.com/2026/06/26/openai-gpt-sol-terra-luna-trump). Note for readers after this article's publish date: [OpenAI cut Terra to $2/$12 and Luna to $0.20/$1.20 on July 30](https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html); Sol was not discounted.*

Luna at $1/$6 per million tokens is a real repricing signal. [DeepSeek V4-Flash is $0.14/M input](/builders-log/deepseek-v4-flash-migration-deadline-builder-guide/), so Luna is not price-competitive with open-weight alternatives — but it is dramatically cheaper than [GPT-5.5's $5/$30](https://developers.openai.com/api/docs/models/gpt-5.5) and positions OpenAI to compete on cost-sensitive tiers it was previously ceding.

Three likely next moves from OpenAI, in rough probability order:
1. **GPT-5.5 cuts 30-50%** once GPT-5.6 reaches general availability — lowering the everyday-tier cost to pressure Anthropic on Sonnet 4.6 and Haiku 4.5 pricing
2. **Enterprise volume discounts** protecting headline per-token pricing while reducing effective rates for large-volume customers
3. **No further headline cuts before IPO** — protecting gross margin narrative for S-1 investor presentations ([OpenAI filed its S-1 confidentially on June 8](https://www.forbes.com/sites/zacharyfolk/2026/06/08/openai-says-it-filed-paperwork-to-go-public/); [Altman told staff to expect a listing "within the next year"](https://www.pymnts.com/artificial-intelligence-2/2026/openai-ceo-tells-staff-to-expect-ipo-within-the-next-year/))

The IPO timing is the complicating factor. A sustained price war compresses margins at a moment when both companies are preparing public market narratives. [Anthropic is targeting an October 2026 listing](https://www.startuphub.ai/ai-news/ipo-watch/2026/anthropic-ipo-roadshow-investor-meetings-2026-07-15). Infrastructure costs are rising for both: [OpenAI's own inference spend had already reached $8.67 billion through the first nine months of 2025 alone](https://www.wheresyoured.at/oai_docs/), per leaked financial documents. Pricing down while costs go up is a difficult story for either company's S-1.

The most likely outcome is a carefully staged sequence: GPT-5.6 GA (coming weeks) with Luna's $1 price broadly available, followed by GPT-5.5 cuts framed as "making the previous generation accessible" while the new flagship holds pricing.

---

## What the Efficiency Shift Means for Your Budget

The tokenmaxxing era — where developers burned tokens as a proxy for productivity — is [well documented](/reviews/tokenmaxxing-claude-code-ai-cost-crisis-developer-cult-2026/). The shift to efficiency is already visible in the same enterprise data.

[Lindy, a 25-person AI agent startup, moved most of its managed-agent model traffic from Claude to DeepSeek](https://www.lindy.ai/blog/migrating-from-claude-to-deepseek) (Sonnet still runs when a user explicitly selects it), cutting inference costs on the migrated traffic by about 90% — its CEO called the move "a matter of survival for the business," while saying he'd switch back if Anthropic cut prices. Uber, which [burned through its entire 2026 AI budget in four months](/builders-log/microsoft-uber-claude-code-enterprise-ai-cost-governance-builder-guide/), [capped spending at $1,500/month per engineer per AI coding tool](https://techcrunch.com/2026/06/02/uber-caps-employee-ai-spending-after-blowing-through-budget-in-four-months/). Finance teams that were invisible when AI spend was small are now active participants in model selection decisions.

This is the new baseline: CFO scrutiny is standard, ROI measurement is expected, and "we use the best model" is no longer a complete justification for a bill that grew 4x in a quarter.

Price cuts from OpenAI do not change this dynamic. If anything, cheaper tokens make the ROI case easier to quantify — and harder to avoid quantifying.

---

## Builder Audit: Four Things to Do Before the Next Announcement

**1. Baseline your current API costs by model and workload.** When OpenAI announces cuts, you want to calculate the savings immediately — not reconstruct three months of billing history. Export your usage dashboard now and tag it by workflow type.

**2. Avoid locking annual contracts at current pricing.** OpenAI's discussions are "still in flux" but directionally clear. Any contract signed in the next 60 days should include a "most-favored pricing" clause that passes future price reductions through automatically — or use quarterly terms.

**3. Audit which workloads actually need frontier pricing.** Luna at $1/$6 and [DeepSeek V4-Flash at $0.14/$0.28](/builders-log/deepseek-v4-flash-migration-deadline-builder-guide/) cover a large share of production workloads that are currently running on $5/$30 models because nobody made the routing decision explicitly. Make it explicit now, before prices change and the urgency disappears.

**4. Benchmark Sol and Fable 5 against your actual tasks, not published scores.** Sol (GPT-5.6) and Fable 5 post different benchmark results — [Sol's Terminal-Bench 2.1 score is 88.8%](https://llm-boss.com/blog/gpt-5-6-benchmarks) (91.9% in its multi-agent "ultra" mode), [Fable 5's SWE-Bench Pro lead is roughly 22 points over GPT-5.5 (80.3% vs. 58.6%)](https://thenextweb.com/news/anthropic-fable-5-vs-openai-gpt-5-5-benchmark-comparison). One important caveat if you're planning that bake-off: Fable 5 [was pulled offline worldwide by a US export-control order from June 12 to July 1, 2026](https://www.anthropic.com/news/fable-mythos-access) — confirm current availability before you build a comparison around it. Neither benchmark tells you which model performs better on your codebase, your retrieval pipeline, or your document workflows. When GPT-5.6 reaches general availability, benchmark both on your highest-value tasks. Published scores are starting positions, not decisions.

---

The price cut is coming. The exact timing and magnitude are uncertain, but the direction is not: OpenAI has lost the enterprise market lead it held for three years and has clearly signaled repricing as its response. Builders who have baselined their costs, negotiated flexible contracts, and routed workloads appropriately will capture the savings immediately when the announcement lands. Those who have not will get the same price — and spend a month figuring out what to do with it.

