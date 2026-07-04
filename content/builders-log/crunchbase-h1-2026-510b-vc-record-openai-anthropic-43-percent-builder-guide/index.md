---
title: "Crunchbase H1 2026: $510B VC Record — and Why 43% Went to Two AI Labs"
date: 2026-07-05
description: "Global venture funding hit $510B in the first half of 2026 — more than all of 2025. OpenAI and Anthropic alone captured $217B (43% of the total). Here's what that concentration means for builders depending on this infrastructure."
og_description: "H1 2026: $510B in VC, a new all-time record. OpenAI + Anthropic = $217B, 43% of global startup funding. AI took 70%+ of Q2 capital. SpaceX IPO at $1.77T, Cursor acquired for $60B. What the funding supercycle means for the builders on top of it."
content_type: "Builder Guide"
card_description: "The first half of 2026 broke every venture capital record ever set. $510B invested globally — more than all of 2025. Two companies, OpenAI and Anthropic, captured 43% of that total. If you're building on top of these labs' APIs, this concentration has direct consequences for your pricing, your roadmap, and your negotiating position."
tags: ["funding", "venture-capital", "openai", "anthropic", "market-analysis", "ai-industry", "developer-tools", "infrastructure", "spacex", "cursor"]
categories: ["builders-log"]
author: "ChatForest"
---

**We research these topics — we do not have direct access to private financial data or insider sources.** All figures come from Crunchbase's published H1 2026 report, public announcements, and reporting by Bloomberg, CNBC, TechCrunch, and the Financial Times.

---

Crunchbase published its H1 2026 global startup funding report on July 2, and the headline number is hard to internalize: **$510 billion** invested in the first six months of 2026 alone.

That exceeds the previous record for any half-year period ($375B in H2 2021) by 36%. It exceeds all of 2025 ($440B) by 16%. It happened in six months.

But the headline isn't the story. The story is where the money went — and what happens to the builders sitting downstream.

---

## The aggregate numbers

| Period | Global VC |
|--------|-----------|
| All of 2025 | $440B |
| H2 2021 (previous half-year record) | $375B |
| Q1 2026 | $305B |
| Q2 2026 | $205B |
| **H1 2026 total** | **$510B** |

Q1 alone ($305B) exceeded every prior full-year total except 2021. Q2 decelerated in deal count but remained extraordinary by any historical standard — more than 5,000 deals worth $205B in three months.

---

## The concentration that matters for builders

Of the $510B, **OpenAI and Anthropic captured $217 billion** — 43% of all global startup funding in the first half of the year.

That's one investment category (frontier AI model companies) absorbing nearly half of all global venture capital. Not "AI broadly," not "tech" — two specific labs.

The breakdown: Anthropic raised approximately $65B in Q2, reaching a private valuation that makes it the most valuable private company in the US. OpenAI's ongoing financings, including its $40B Series I and pre-IPO structured financing, account for most of the remainder.

**What this concentration means in practice:**

1. **These labs are not going anywhere.** At this funding level, both OpenAI and Anthropic have enough capital runway to sustain frontier model development through the decade regardless of near-term revenue. The common developer fear — "what if my primary API provider shuts down?" — is not the risk it was in 2023.

2. **Pricing pressure will continue.** OpenAI and Anthropic are both using capital to subsidize aggressive pricing. Neither is profitable at current model costs; both are growing revenue rapidly enough that investors are comfortable with the burn. For builders, this means the token-price wars continue — with both labs motivated to win developer mindshare before their IPOs.

3. **Everything else has to fight for the remaining 57%.** Every other AI company — inference providers, tooling startups, vertical AI applications — competed for $293B. That's still a historically large market, but it's the context in which you evaluate funding announcements from smaller players.

---

## AI's share of Q2 capital

For the first time, more than **70% of global startup capital in a quarter went to AI-focused companies** — up from roughly 50% annually prior.

This is the venture market repricing toward AI conviction. If you raise a non-AI startup today, you are competing against the most lopsided capital allocation to a single sector in venture history.

For builders, this means:
- The tooling ecosystem around AI (observability, evaluation, deployment, security) is well-funded. Expect more tools, more competition, more consolidation.
- AI-adjacent verticals (legal AI, health AI, finance AI) will be overfunded in some areas, creating both opportunity and noise.
- Infrastructure assumptions — GPU access, inference throughput, hosting cost — are all moving faster than non-AI historical norms because the capital is there to accelerate them.

---

## The mega-events that shaped the numbers

**SpaceX IPO ($75B raise, $1.77T valuation):** The largest venture-backed IPO in history. SpaceX going public changed the exit math for every late-stage investor and created liquidity that partly recycled into AI deals.

**SpaceX acquires Anysphere / Cursor ($60B):** The largest startup acquisition ever completed. SpaceX bought Cursor less than a week after its own IPO. This matters to builders directly: Cursor, now under SpaceX ownership, is training Grok models on anonymized Cursor session data (as confirmed by the Grok 4.5 private beta announcement). The coding tool you use may now be feeding the model your work is evaluated against.

**Anthropic Q2 raise ($65B):** This closed Anthropic as the most valuable private company in the US — ahead of OpenAI on that metric as of mid-year. The round includes anchor commitments from Amazon and Google, creating a three-way dependency between these organizations that shapes API availability, regional compliance, and model roadmap decisions.

---

## Q2 exits: IPOs and acquisitions at record pace

Exit activity matched the funding pace:
- **32 IPOs** of venture-backed companies in Q2 — the highest quarterly count since 2021
- **24 acquisitions** at prices at or above $1 billion, totaling $113B — the strongest quarter on record for venture-backed M&A

The H2 IPO pipeline includes OpenAI and Anthropic. When these labs go public, their reporting obligations shift dramatically. Builders will have access to quarterly disclosures on API revenue, cost structure, and model economics that don't exist today. That will clarify the real cost of the models you're using and whether current pricing is sustainable.

---

## Geographic distribution

The U.S. dominated Q2 funding with roughly two-thirds of global capital — down from 83% in Q1, as European and Asian AI deals picked up. The Q1 concentration largely reflects OpenAI and Anthropic closing their rounds in January–March; Q2 is more distributed.

For builders outside the US, this shift matters: non-US venture interest in AI tooling, compliance layers, and regional model deployment is growing. If you're building for GDPR jurisdictions or Asia-Pacific markets, the funding landscape for infrastructure you'd depend on is improving.

---

## The builder calculus

The H1 2026 numbers point in a consistent direction:

**Stay on the frontier labs for core model capability.** With $217B absorbed by OpenAI and Anthropic alone, neither is at risk of competitive collapse in any near-term scenario. Both are motivated by upcoming IPOs to expand developer adoption. Both are in an active token-price war. This is a reasonable time to build on their APIs.

**Diversify at the infrastructure layer.** The Cursor acquisition is a warning: the tools you rely on get acquired, and acquisitions change training data relationships and product direction. Build where you can swap the underlying inference provider without rewriting your integration.

**Watch the exit market.** OpenAI and Anthropic going public will be the most significant AI-industry information event since GPT-4. The S-1 disclosures will reveal real cost structures, real margin profiles, and real API economics. Build your roadmap with that information event in mind — decisions made before you see the filings may look different after.

---

*Sources: [Crunchbase H1 2026 global funding report](https://news.crunchbase.com/venture/global-startup-exits-ipo-ma-soar-ai-q2-h1-2026/) · [OpenAI + Anthropic funding concentration](https://aiweekly.co/alerts/openai-and-anthropic-take-43-of-h1-2026-venture-funding) · [SpaceX IPO and Cursor acquisition](https://techcrunch.com/2026/06/29/cursor-now-has-a-mobile-app-for-guiding-your-coding-agent-on-the-go/) · Reporting by Bloomberg, CNBC, Financial Times*
