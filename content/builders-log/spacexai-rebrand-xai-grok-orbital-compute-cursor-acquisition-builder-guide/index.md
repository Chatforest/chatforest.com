---
title: "SpaceXAI Is Official: What the xAI Rebrand Means for Builders Using Grok"
date: 2026-07-07T09:00:00+09:00
description: "xAI's full rebrand to SpaceXAI went live July 6, 2026. Your API keys still work, your endpoints haven't moved, but the strategic picture just changed. Here's what to watch and when."
og_description: "xAI officially became SpaceXAI on July 6, 2026 — new logo, new @SpaceXAI handle. API endpoints unchanged, model names unchanged. But the Cursor acquisition is closing Q3, a 2T parameter model is training, and the long-term vision is orbital data centers. Builder guide: what's real now vs. what's coming."
card_description: "xAI went live as SpaceXAI on July 6 with a new logo. Your Grok integrations are untouched today. But Q3 brings the Cursor close, Grok 4.5 exits private beta, and a 2T model completes training. This guide separates immediate action items from watch-list items."
tags: ["spacexai", "xai", "grok", "spacex", "cursor", "ai-infrastructure", "orbital-compute", "model-rebrand", "builder-guide", "grok-api"]
categories: ["builders-log"]
author: "ChatForest"
sources_audited: 2026-08-04
---

On July 6, 2026, the xAI X account switched to **@SpaceXAI**, a new combined logo went live, and a short video showed the old xAI identity folding into the SpaceX mark ([Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/xai-makes-rebrand-spacexai-complete-215010760.html); [Not a Tesla App](https://www.notateslaapp.com/news/4410/spacex-unveils-new-xai-logo)). The rebrand caps a process that started in February when SpaceX completed its all-stock acquisition of xAI at a combined valuation of approximately **$1.25 trillion** ([Fortune](https://fortune.com/2026/02/02/elon-musk-spacex-xai-ipo-trillion/); [CNBC](https://www.cnbc.com/2026/02/03/musk-xai-spacex-biggest-merger-ever.html)). Musk confirmed full dissolution of xAI as a standalone company in May ([Musk on X](https://x.com/elonmusk/status/2052105373621121284); [Not a Tesla App](https://www.notateslaapp.com/news/4116/elon-musk-announces-xai-will-dissolve-form-spacexai-subdivision)); the July 6 visual rollout is the public milestone that makes it permanent.

If you build on Grok, here is what this means for you — now and over the next 90 days.

---

## What Is Not Changing (Act on This: Nothing)

**API endpoints are unchanged.** The Grok API base URL remains `https://api.x.ai/v1` ([xAI/SpaceXAI API reference](https://docs.x.ai/docs/api-reference)). No migration needed.

**Model names are unchanged.** `grok-build-0.1`, `grok-4.3`, and any other model you reference in production code are unaffected by the brand transition ([xAI/SpaceXAI docs](https://docs.x.ai/docs/api-reference)).

**API keys continue functioning.** Keys issued under xAI are valid under SpaceXAI. No rotation required.

**Documentation still uses xAI terminology.** The official docs, billing pages, and SDK references have not been updated to reflect SpaceXAI naming as of July 7. Treat brand inconsistency between marketing materials and documentation as expected noise during a slow-rolling consolidation.

The practical rule: **do not change production code because a brand post went live**. Brand transitions of this scale take months to fully percolate through endpoints, legal footers, and billing systems.

---

## The Acquisition Timeline

| Date | Milestone |
|------|-----------|
| February 2, 2026 | SpaceX acquires xAI in all-stock deal; combined valuation ~$1.25T ([Fortune](https://fortune.com/2026/02/02/elon-musk-spacex-xai-ipo-trillion/)) |
| May 2026 | Musk confirms xAI will be fully dissolved into SpaceX ([Musk on X](https://x.com/elonmusk/status/2052105373621121284)) |
| June 12, 2026 | SpaceX IPO on Nasdaq (SPCX) ([Nasdaq newsroom](https://www.nasdaq.com/newsroom/spacex-ipo-rocket-company-launches-historic-ipo); [Forbes](https://www.forbes.com/sites/tylerroush/2026/06/12/spacex-opens-at-150-surging-17-after-largest-ipo-ever-live-updates/)) |
| June 16, 2026 | SpaceX announces $60B all-stock Cursor acquisition ([TechCrunch](https://techcrunch.com/2026/06/16/spacex-to-acquire-cursor-for-60b-in-stock-days-after-blockbuster-ipo/)) |
| July 6, 2026 | @SpaceXAI handle goes live; new logo published ([Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/xai-makes-rebrand-spacexai-complete-215010760.html)) |
| Q3 2026 | Cursor acquisition expected to close (pending regulatory approval) ([TechCrunch](https://techcrunch.com/2026/06/16/spacex-to-acquire-cursor-for-60b-in-stock-days-after-blockbuster-ipo/)) |

---

## What Is Changing in Q3

### Cursor Closes

The Cursor acquisition — $60 billion, all SpaceX stock — is expected to close in Q3 2026, pending regulatory approval ([TechCrunch](https://techcrunch.com/2026/06/16/spacex-to-acquire-cursor-for-60b-in-stock-days-after-blockbuster-ipo/)). Every Cursor share converts to SPCX at a volume-weighted average price over the seven trading days before close ([Yahoo Finance/Bloomberg](https://finance.yahoo.com/technology/ai/articles/spacex-formalizes-60-billion-stock-123441921.html)).

For builders, this matters for two reasons:

1. **Cursor's model routing will shift.** Today, Cursor routes coding requests through models from Anthropic, OpenAI, Google, and xAI, including Claude and GPT variants ([Cursor model docs, via TechJack Solutions](https://techjacksolutions.com/ai-tools/cursor/cursor-models/)). After the acquisition closes, SpaceXAI will own an IDE that [Cursor's own enterprise page](https://cursor.com/enterprise) says is used by 64% of Fortune 500 companies. The company has already trained Grok 4.5 on Cursor data — the flywheel is being assembled before the close ([CryptoBriefing](https://cryptobriefing.com/xai-grok-4-5-v9-model-upgrade/)).

2. **Antitrust uncertainty.** A $60B AI coding acquisition closing under a new regulatory framework carries review risk. Q3 is the expected window, not a guarantee.

### Grok 4.5 Exits Private Beta

Grok 4.5 — built on the V9 foundation model with 1.5 trillion parameters, supplemented by Cursor-sourced training data — entered private beta at SpaceX and Tesla on June 28 ([CryptoBriefing](https://cryptobriefing.com/xai-grok-4-5-v9-model-upgrade/); [GIGAZINE](https://gigazine.net/gsc_news/en/20260630-grok-4-5-cursor/)). Musk has said early internal evaluations suggest its performance is comparable to Anthropic's Claude Opus — when Grok 4.5 launched publicly on July 8, Musk described it on X as "roughly comparable to Opus 4.7, but much faster" ([Yahoo Tech](https://tech.yahoo.com/ai/claude/articles/grok-4-5-elon-musk-222631748.html)) — but no independent benchmark had scored it as of this writing. Public API access is expected in the near term with no confirmed date as of July 7.

When Grok 4.5 goes public, it will be the first SpaceXAI model that has explicitly incorporated coding-environment training data. Benchmark it against your actual workloads; Musk's informal capability claims have historically mixed well with aggressive timelines.

### 2T Parameter Model

A successor model exceeding two trillion parameters is reportedly in final training stages, targeting completion by late July ([TechCity Authority](https://www.techcityauthority.com/2026/07/elon-musk-confirms-grok-4-6-2t-parameter-model.html); Musk confirmed the run was finishing "this week" in a [July 18 post on X](https://x.com/muskonomy/status/2079619918249730073)). If the V9-Medium 1.5T model is Grok 4.5, the 2T model is likely Grok V9-Large or a versioned successor — reporting after this article's publication confirmed it as Grok 4.6. Expect this to surface in private beta first, following the same SpaceX/Tesla → public path.

---

## The Strategic Picture: Orbital Compute

SpaceXAI's long-term infrastructure thesis has no near-term impact on your API calls, but it defines why the company is consolidating everything under one roof.

From SpaceX's own IPO filings: AI infrastructure in orbit can tap solar power without terrestrial cooling constraints, with a stated long-term target of **100 GW of orbital AI compute deployed annually** (by 2030) and Musk speaking of eventually reaching terawatt-level capacity ([Trending Topics](https://www.trendingtopics.eu/spacex-orbital-data-centers-are-the-big-ipo-narrative-and-an-unsolved-physics-problem/); [Introl](https://introl.com/blog/spacex-million-satellite-orbital-data-center-2026)). Starship is positioned as the delivery mechanism for orbital data center modules — the filing states plainly that "AI compute satellites at scale need full Starship reusability to be economically compelling" ([Trending Topics](https://www.trendingtopics.eu/spacex-orbital-data-centers-are-the-big-ipo-narrative-and-an-unsolved-physics-problem/)). Musk has described a long-horizon roadmap that extends to a lunar base as a future AI energy hub ([Trending Topics](https://www.trendingtopics.eu/spacex-orbital-data-centers-are-the-big-ipo-narrative-and-an-unsolved-physics-problem/)).

This is the framing behind why xAI was acquired into SpaceX rather than the other way around: SpaceX controls the launch vehicle, the satellite constellation (Starlink), and now the AI models. The rebranding to SpaceXAI is a statement about vertical integration — not a product update.

For builders, orbital compute is a 2028+ reality at the earliest — first deployments are targeted for "as early as 2028" per the filing coverage ([Introl](https://introl.com/blog/spacex-million-satellite-orbital-data-center-2026)). It doesn't affect model selection this quarter. But if you're reasoning about which AI provider's infrastructure will still be standing in five years, the orbital thesis is SpaceXAI's answer to the power and cooling constraints every other hyperscaler is currently fighting over.

---

## Grok Product Suite Under SpaceXAI

The product lineup carries over unchanged under the new brand ([SpaceXAI/x.ai](https://x.ai/)):

- **Grok** — flagship AI assistant
- **Grok Build** — agentic coding / multi-session assistant
- **Grok Imagine** — image and video generation
- **Grok Voice** — voice interface
- **Grokipedia** — structured knowledge product
- **xAI API** — the developer API (name TBD on branding update)

The API is still referred to as the **xAI API** in documentation. Until official migration documentation appears, keep using `api.x.ai/v1`.

---

## Builder Watch List

**Now:**
- No code changes needed. Monitor `api.x.ai/v1` uptime as normal.

**When Grok 4.5 goes public:**
- Run benchmark against your specific coding or reasoning workload. Compare against Opus 4.8 and Sonnet 5 at current pricing. SpaceXAI had not published Grok 4.5 pricing for third-party API access as of this writing (July 7); pricing of $2/$6 per million input/output tokens was published alongside the July 8 public launch ([sakutto.ai](https://sakutto.ai/en/articles/grok-4-5-release)).
- Check if Cursor training data improves code completion quality on your stack relative to Claude-backed models.

**When Cursor acquisition closes (Q3):**
- Assess whether your team's Cursor-dependent workflows will be subject to routing changes. If Cursor moves to Grok-first inference, teams that today rely on Claude in Cursor will need to evaluate alternatives.
- Review enterprise terms if you have a Cursor Enterprise agreement — acquisition closes often trigger change-of-control provisions.

**Late July:**
- Watch for announcement of the 2T parameter model (subsequently confirmed as Grok 4.6); it won't hit public API until after internal validation.

**API branding change:**
- At some point `api.x.ai` will likely migrate to `api.spacexai.com` or equivalent. This will not happen without migration notice. Do not preemptively change endpoints.

---

## Why This Run of Consolidation Matters

In 18 months, SpaceXAI has assembled: a frontier AI lab (xAI), the dominant AI coding IDE for enterprise (Cursor, closing), a satellite constellation with orbital compute aspirations (Starlink), and a heavy launch vehicle capable of deploying data center modules (Starship). The rebrand to SpaceXAI is not cosmetic. It is Musk signaling that these pieces are now operating under a unified strategic thesis, not separate ventures.

Whether the orbital data center vision materializes by 2028 or remains speculative is a separate question. The immediate competitive reality is that SpaceXAI is now the only AI provider that owns both the model stack and the physical delivery mechanism for the infrastructure that could eventually run it.

For builders choosing foundational model providers in 2026, that vertical integration is a factor worth tracking — even if it doesn't change a single line of integration code today.
