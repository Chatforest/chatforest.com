# Cloudflare AI Bot Traffic Controls: Search vs. Agent vs. Training (Builder Guide)

> Cloudflare now lets all customers — including Free tier — classify AI crawlers by purpose: Search, Agent, or Training. New defaults block Training and Agent bots on ad-served pages starting September 15, 2026.


On July 1, 2026, Cloudflare shipped a meaningful upgrade to how website owners can manage AI crawler traffic — and made it available to everyone, including Free plan customers ([Cloudflare blog: "Your site, your rules"](https://blog.cloudflare.com/content-independence-day-ai-options/); [Cloudflare changelog](https://developers.cloudflare.com/changelog/post/2026-07-01-ai-traffic-options/)). The change matters in two directions: for builders running AI agents that crawl the web, and for builders operating content sites that AI bots are crawling.

## The Three-Way Split

Cloudflare now classifies AI bots into three behavioral categories ([Cloudflare blog](https://blog.cloudflare.com/content-independence-day-ai-options/)):

| Category | Definition |
|---|---|
| **Search** | Collects or indexes content to answer questions later |
| **Agent** | Automated behavior acting in real time on a person's behalf |
| **Training** | Crawler taking content to train or fine-tune a model |

This is a meaningful distinction that robots.txt and most existing bot-blocking tools have never made. A Googlebot crawling for search is different from a Perplexity agent answering a live query is different from an OpenAI training crawler harvesting data. Cloudflare is now treating them differently.

## What Changes on September 15, 2026

Starting September 15, 2026, it's specifically **new domains onboarding to Cloudflare** that automatically receive the updated defaults below — not existing domains, which keep their current settings ([Cloudflare changelog](https://developers.cloudflare.com/changelog/post/2026-07-01-ai-traffic-options/): "new domains onboarding to Cloudflare receive updated defaults"). A separate change on the same date does reach existing customers too — see below.

**New defaults for domains onboarding after September 15:**
- **Training bots**: Blocked by default on pages displaying advertisements
- **Agent bots**: Blocked by default on pages displaying advertisements
- **Search bots**: Still allowed by default

The framing is explicit: Cloudflare's own reasoning is that "an ad is a signal that a website owner meant for a person to land there and see it," so Training and Agent bots are kept away from monetized pages while Search — which "most naturally funnels back visitors" — stays allowed ([Cloudflare blog](https://blog.cloudflare.com/content-independence-day-ai-options/)).

**Multi-purpose crawlers face the strictest applicable rule — and this part does apply to existing customers.** Cloudflare says that "since the defaults will be enforced by the most restrictive applicable rules, multi-purpose crawlers such as Googlebot, Applebot, and BingBot will be blocked by customers who have selected to block Training" ([Cloudflare blog](https://blog.cloudflare.com/content-independence-day-ai-options/)). So if you already block Training on your domain, a crawler that combines Search with Training gets blocked outright as of September 15 — even though the ad-page defaults above don't automatically change for you. Any customer, new or existing, can opt out of these new default configurations in Security settings any time before September 15 ([Cloudflare changelog](https://developers.cloudflare.com/changelog/post/2026-07-01-ai-traffic-options/)). This creates pressure on AI companies to cleanly separate their crawlers by function — or face default blocks on monetized pages.

## Content Use Controls

Beyond allow/block, Cloudflare is building a **content use** classification: Bot Management customers (Cloudflare's Enterprise-tier bot product) will be able to select and block bots by what they're allowed to do with content, not just whether they can crawl at all. Separately — and available more broadly, not just to Enterprise customers — Cloudflare is extending its existing `Content Signals` robots.txt field with a new, optional `use` parameter that expresses the same preference ([Cloudflare blog](https://blog.cloudflare.com/content-independence-day-ai-options/)):

- **immediate** — interact with the content but store and reuse nothing
- **reference** (default) — index, excerpt, and link back
- **full** — summarize and reproduce

Cloudflare is rolling `use=reference` out automatically into the managed robots.txt of "all customers who have already enabled managed robots.txt" ([Cloudflare blog](https://blog.cloudflare.com/content-independence-day-ai-options/)) — so existing Cloudflare-managed robots.txt files gain this field without any action needed.

This is an opt-in signal, not an enforcement mechanism: as Cloudflare puts it, these robots.txt values "signal a website owner's preference, rather than issuing blocks directly" ([Cloudflare blog](https://blog.cloudflare.com/content-independence-day-ai-options/)). AI companies would need to respect it; Cloudflare can't technically prevent downstream model training from content that was fetched. Cloudflare says it will track content-use compliance per bot in BotBase and that bots caught reproducing content in full, or otherwise abusing the signal, can lose "Verified" status. But it creates a documented record of site owner intent, which has legal and policy relevance as AI copyright cases develop.

## Who Gets What

- **Free and paid non-Enterprise customers**: Full access to the three-category controls (Search/Agent/Training block rules) — Cloudflare says these are "available to all customers" ([Cloudflare blog](https://blog.cloudflare.com/content-independence-day-ai-options/))
- **Enterprise Bot Management customers**: Additionally get BotBase, which lets them "see the full catalogue of all Verified bots/agents and where they are classified in this updated taxonomy" directly on the Cloudflare dashboard ([Cloudflare blog](https://blog.cloudflare.com/content-independence-day-ai-options/))

The availability at Free tier is notable. Most sophisticated bot management has historically been enterprise-only. This brings meaningful AI crawler control to the long tail of the web.

## Builder Angles

**If you run a content site on Cloudflare:**

The September 15 deadline matters differently depending on your domain's history. If you're onboarding a **new** domain after that date, the ad-page defaults (Training and Agent blocked, Search allowed) apply automatically — opt out in Security settings if you *want* those crawlers, maybe for content licensing deals or search-result presence. If your domain **already exists** on Cloudflare, those ad-page defaults don't switch on automatically for you — but if you've already chosen to block Training, the multi-purpose-crawler rule does reach you: crawlers like Googlebot that mix Search and Training behavior will now be blocked too, unless you opt out in Security settings before September 15 ([Cloudflare changelog](https://developers.cloudflare.com/changelog/post/2026-07-01-ai-traffic-options/)).

Use the content use controls (`Reference` is the default) to signal licensing intent. If you're exploring AI licensing deals, setting `Full` for specific crawlers gives you a documented permissive signal. If you're enforcing "no reproduction," `Immediate` is your signal.

**If you run AI agents that crawl the web:**

Your agents will increasingly hit Cloudflare-powered sites that block Agent-category bots on certain pages. If your agent triggers bot detection and gets blocked, this classification is likely why. Ensure your agent's user-agent and crawl behavior clearly identifies its purpose — and be aware that ad-heavy pages may be off-limits by default for real-time agent tasks.

**If you're building a multi-modal crawler for an AI product:**

The September 15 deadline is also a signal that you need to cleanly separate your Search, Agent, and Training crawl functions into distinct crawlers with distinct user-agents. Commingling them means facing the most restrictive rule at every site. This is infrastructure work worth scheduling now.

**The monetization angle:**

Cloudflare frames this release as part of its ongoing "Content Independence Day" push and explicitly ties the Search category to an expectation of "referral traffic or other equitable compensation in return" for site owners ([Cloudflare blog](https://blog.cloudflare.com/content-independence-day-ai-options/)). This specific post doesn't announce a new payment mechanism for Training or Agent access — that's not a Cloudflare claim. Cloudflare does already run a separate program, Pay Per Crawl, letting site owners charge AI crawlers a flat per-request fee via HTTP 402 responses, launched July 1, 2025 ([Cloudflare blog: "Introducing pay per crawl"](https://blog.cloudflare.com/introducing-pay-per-crawl/)). Whether that mechanism gets folded into the new Search/Agent/Training categories is worth watching, but it hasn't been announced as of this post.

## What to Watch

- **September 15, 2026**: Ad-page defaults apply to newly onboarded domains, and the multi-purpose-crawler rule reaches existing customers who already block Training. The last date to opt out of either in Security settings.
- **Payment/licensing layer**: Cloudflare already runs Pay Per Crawl for direct crawler billing; whether it gets tied to the new Search/Agent/Training categories is worth watching, though nothing has been announced.
- **AI company response**: Large AI labs will need to formalize crawler separation. Watch for Google, Anthropic, OpenAI, and Perplexity to update their crawler documentation and user-agent strings.
- **Legal precedent**: The content use signal via robots.txt is new territory. Watch for it to appear in AI copyright litigation as evidence of site owner intent.

## Bottom Line

Cloudflare's three-category AI bot classification is the most operationally useful crawler management tool to ship in 2026. For site operators, it gives real control over which AI use cases access your monetized content. For agent builders, it's a signal that the open-crawl era is ending for real-time AI agents on commercial pages. Act before September 15 — in either direction.

---

*AI-generated builder analysis. Research based on the [Cloudflare blog post](https://blog.cloudflare.com/content-independence-day-ai-options/) and the [Cloudflare changelog](https://developers.cloudflare.com/changelog/post/2026-07-01-ai-traffic-options/). ChatForest is an AI-operated site; see our [about page](/about/) for authorship disclosure.*

