# SpaceXAI Is Official: What the xAI Rebrand Means for Builders Using Grok

> xAI's full rebrand to SpaceXAI went live July 6, 2026. Your API keys still work, your endpoints haven't moved, but the strategic picture just changed. Here's what to watch and when.


On July 6, 2026, the xAI X account switched to **@SpaceXAI**, a new combined logo went live, and a short video showed the old xAI identity folding into the SpaceX mark. The rebrand caps a process that started in February when SpaceX completed its all-stock acquisition of xAI at a combined valuation of approximately **$1.25 trillion**. Musk confirmed full dissolution of xAI as a standalone company in May; the July 6 visual rollout is the public milestone that makes it permanent.

If you build on Grok, here is what this means for you — now and over the next 90 days.

---

## What Is Not Changing (Act on This: Nothing)

**API endpoints are unchanged.** The Grok API base URL remains `https://api.x.ai/v1`. No migration needed.

**Model names are unchanged.** `grok-build-0.1`, `grok-4-3`, and any other model you reference in production code are unaffected by the brand transition.

**API keys continue functioning.** Keys issued under xAI are valid under SpaceXAI. No rotation required.

**Documentation still uses xAI terminology.** The official docs, billing pages, and SDK references have not been updated to reflect SpaceXAI naming as of July 7. Treat brand inconsistency between marketing materials and documentation as expected noise during a slow-rolling consolidation.

The practical rule: **do not change production code because a brand post went live**. Brand transitions of this scale take months to fully percolate through endpoints, legal footers, and billing systems.

---

## The Acquisition Timeline

| Date | Milestone |
|------|-----------|
| February 2, 2026 | SpaceX acquires xAI in all-stock deal; combined valuation ~$1.25T |
| May 2026 | Musk confirms xAI will be fully dissolved into SpaceX |
| June 12, 2026 | SpaceX IPO on Nasdaq (SPCX) |
| June 16, 2026 | SpaceX announces $60B all-stock Cursor acquisition |
| July 6, 2026 | @SpaceXAI handle goes live; new logo published |
| Q3 2026 | Cursor acquisition expected to close (pending regulatory approval) |

---

## What Is Changing in Q3

### Cursor Closes

The Cursor acquisition — $60 billion, all SpaceX stock — is expected to close in Q3 2026, pending regulatory approval. Every Cursor share converts to SPCX at a volume-weighted average price over the seven days before close.

For builders, this matters for two reasons:

1. **Cursor's model routing will shift.** Today, Cursor routes coding requests through Claude and GPT. After the acquisition closes, SpaceXAI will own the IDE that a significant share of Fortune 500 developers use to write production code. The company has already trained Grok 4.5 on Cursor data — the flywheel is being assembled before the close.

2. **Antitrust uncertainty.** A $60B AI coding acquisition closing under a new regulatory framework carries review risk. Q3 is the expected window, not a guarantee.

### Grok 4.5 Exits Private Beta

Grok 4.5 — built on the V9 foundation model with 1.5 trillion parameters, supplemented by Cursor-sourced training data — entered private beta at SpaceX and Tesla in late June. Musk has said early evaluations put its performance near Claude Opus 4.8, but no independent benchmark has scored it. Public API access is expected in the near term with no confirmed date.

When Grok 4.5 goes public, it will be the first SpaceXAI model that has explicitly incorporated coding-environment training data. Benchmark it against your actual workloads; Musk's informal capability claims have historically mixed well with aggressive timelines.

### 2T Parameter Model

A successor model exceeding two trillion parameters is reportedly in final training stages, targeting completion by late July. If the V9-Medium 1.5T model is Grok 4.5, the 2T model is likely Grok V9-Large or a versioned successor. Expect this to surface in private beta first, following the same SpaceX/Tesla → public path.

---

## The Strategic Picture: Orbital Compute

SpaceXAI's long-term infrastructure thesis has no near-term impact on your API calls, but it defines why the company is consolidating everything under one roof.

From SpaceX's own filings: AI infrastructure in orbit can tap solar power without terrestrial cooling constraints, scaling to **100–200 GW annually** and eventually toward terawatt-level capacity. Starship is positioned as the delivery mechanism for orbital data center modules. Musk has described a long-horizon roadmap that extends to lunar-based compute.

This is the framing behind why xAI was acquired into SpaceX rather than the other way around: SpaceX controls the launch vehicle, the satellite constellation (Starlink), and now the AI models. The rebranding to SpaceXAI is a statement about vertical integration — not a product update.

For builders, orbital compute is a 2028+ reality at the earliest. It doesn't affect model selection this quarter. But if you're reasoning about which AI provider's infrastructure will still be standing in five years, the orbital thesis is SpaceXAI's answer to the power and cooling constraints every other hyperscaler is currently fighting over.

---

## Grok Product Suite Under SpaceXAI

The product lineup carries over unchanged under the new brand:

- **Grok** — flagship AI assistant
- **Grok Build** — agentic coding / multi-session assistant
- **Imagine** — image generation
- **Voice** — voice interface
- **Grokipedia** — structured knowledge product
- **xAI API** — the developer API (name TBD on branding update)

The API is still referred to as the **xAI API** in documentation. Until official migration documentation appears, keep using `api.x.ai/v1`.

---

## Builder Watch List

**Now:**
- No code changes needed. Monitor `api.x.ai/v1` uptime as normal.

**When Grok 4.5 goes public:**
- Run benchmark against your specific coding or reasoning workload. Compare against Opus 4.8 and Sonnet 5 at current pricing. SpaceXAI has not published Grok 4.5 pricing for third-party API access.
- Check if Cursor training data improves code completion quality on your stack relative to Claude-backed models.

**When Cursor acquisition closes (Q3):**
- Assess whether your team's Cursor-dependent workflows will be subject to routing changes. If Cursor moves to Grok-first inference, teams that today rely on Claude in Cursor will need to evaluate alternatives.
- Review enterprise terms if you have a Cursor Enterprise agreement — acquisition closes often trigger change-of-control provisions.

**Late July:**
- Watch for announcement of the 2T parameter model. This is likely Grok V10 or Grok 5's foundation; it won't hit public API until after internal validation.

**API branding change:**
- At some point `api.x.ai` will likely migrate to `api.spacexai.com` or equivalent. This will not happen without migration notice. Do not preemptively change endpoints.

---

## Why This Run of Consolidation Matters

In 18 months, SpaceXAI has assembled: a frontier AI lab (xAI), the dominant AI coding IDE for enterprise (Cursor, closing), a satellite constellation with orbital compute aspirations (Starlink), and a heavy launch vehicle capable of deploying data center modules (Starship). The rebrand to SpaceXAI is not cosmetic. It is Musk signaling that these pieces are now operating under a unified strategic thesis, not separate ventures.

Whether the orbital data center vision materializes by 2028 or remains speculative is a separate question. The immediate competitive reality is that SpaceXAI is now the only AI provider that owns both the model stack and the physical delivery mechanism for the infrastructure that could eventually run it.

For builders choosing foundational model providers in 2026, that vertical integration is a factor worth tracking — even if it doesn't change a single line of integration code today.

