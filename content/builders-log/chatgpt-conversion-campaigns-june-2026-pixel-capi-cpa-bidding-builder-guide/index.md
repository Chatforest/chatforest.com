---
title: "ChatGPT Conversion Campaigns: Pixel, CAPI, and CPA Bidding — What Changed June 5"
date: 2026-06-06
description: "OpenAI rolled out conversion-optimized campaigns on June 5, 2026, letting eligible ChatGPT advertisers pay for actual purchases or leads rather than clicks or impressions. The shift requires a Pixel or Conversions API setup from before June 1 to qualify. Here's what the technical change means for builders building on or advertising through the ChatGPT platform."
og_description: "ChatGPT ads now support CPA bidding for eligible advertisers (Pixel or CAPI live before June 1). The shift from click to conversion optimization changes attribution, bidding strategy, and how you evaluate campaign performance. OpenAI recommends a 30-day attribution window; early Criteo data shows AI-referred conversions approaching 2x traditional search in some categories."
content_type: "Builder's Log"
categories: ["OpenAI", "ChatGPT", "Advertising", "Performance Marketing"]
tags: ["openai", "chatgpt", "advertising", "conversion-campaigns", "cpa-bidding", "pixel", "conversions-api", "capi", "performance-marketing", "chatgpt-ads-manager", "attribution", "builder-guide"]
sources_audited: 2026-07-29
---

On June 5, 2026, [OpenAI began rolling out conversion-optimized campaigns](https://digiday.com/marketing/openai-turns-on-cost-per-action-ads-inside-chatgpt/) to eligible ChatGPT advertisers, per [MediaPost](https://www.mediapost.com/publications/article/415465/openai-races-to-add-conversion-optimized-campaigns.html) and [ppc.land](https://ppc.land/openais-chatgpt-ads-are-getting-conversion-optimization-heres-what-changes/). The change is structural: the platform moves from charging for clicks and impressions toward charging for measurable outcomes — purchases, signups, completed trials. For advertisers who had the Pixel or Conversions API connected before June 1, access opened automatically. For anyone who did not, the eligibility gate is now set and the next access window hasn't been announced.

This is part of **[Builder's Log](/builders-log/)**, tracking the technical edges of the AI ecosystem.

---

## What Changed, and Why It Matters

[ChatGPT Ads Manager launched in self-serve form on May 5, 2026](https://ppc.land/openai-opens-chatgpt-ads-manager-to-all-us-businesses-with-cpc-bidding/), with two buying models: cost-per-mille (CPM) impressions and cost-per-click (CPC) clicks. The minimum spend floor was removed, OpenAI recommended CPC bids of $3–$5, and [the self-serve Ads Manager opened to US businesses of all sizes without requiring a sales relationship](https://www.mediapost.com/publications/article/414857/openai-opens-ad-platform-to-cpc-bidding-self-serv.html). That was the awareness-and-reach phase.

Conversion campaigns represent the next layer. Instead of bidding on showing your ad or getting a click, you bid on the actual conversion event — a user completes a purchase, fills out a lead form, starts a trial, or books a call after clicking through. The platform optimizes delivery toward users it predicts are more likely to complete that event, not just users likely to click.

The practical significance: conversion optimization shifts budget allocation responsibility from the advertiser to the platform. Google Search Ads and Meta's Advantage+ have operated this way for years. ChatGPT Ads Manager now has the infrastructure to do the same, but with a fundamentally different user intent profile underneath it.

---

## Eligibility for the June 5 Rollout

Access to conversion-optimized campaigns in the initial wave [requires having at least one conversion event flowing through either the JavaScript Pixel or the Conversions API before June 1, 2026](https://ppc.land/openais-chatgpt-ads-are-getting-conversion-optimization-heres-what-changes/). Accounts that met this condition should have received access automatically when the rollout opened June 5.

Accounts that installed the Pixel or CAPI after June 1 are not included in this initial access wave. OpenAI has not published a timeline for when the broader rollout opens to all accounts.

The eligibility gate is a data-readiness requirement: conversion optimization requires post-click behavioral data to train on. An account with no conversion signal connected has no training data for the optimization algorithm to work with.

---

## The Two Measurement Tools

### JavaScript Pixel

The OpenAI Pixel is a browser-side JavaScript SDK that tracks what happens on your site after an ad click. [It must be loaded in the `<head>` tag, not the `<body>`](https://developers.openai.com/ads/measurement-pixel). Loading it in the body causes it to initialize after DOM content loads, which means it can miss early page-view events and fail to register the session if the user navigates away quickly.

The pixel supports [ten standard event types](https://developers.openai.com/ads/supported-events):

- `page_viewed`
- `registration_completed`
- `lead_created`
- `order_created`
- `subscription_created`
- `trial_started`
- `appointment_scheduled`
- `checkout_started`
- `contents_viewed`
- `items_added`

Standard implementation: add the base pixel to every page, then fire the specific event on the relevant completion page (e.g., `order_created` on your order confirmation page). OpenAI provides [a Google Tag Manager template](https://github.com/openai/ads-measurement-pixel-gtm-template) if you manage tags through GTM.

### Conversions API (CAPI)

The Conversions API sends conversion events server-to-server, from your backend directly to OpenAI's measurement infrastructure, rather than through the browser. Server-side tracking bypasses browser restrictions and ad blockers, which improves data completeness — particularly for users in privacy-protective browser configurations.

The deduplication requirement: if you fire the same conversion event from both the browser pixel and the server, [each event must include a shared `event_id`](https://developers.openai.com/ads/conversions-api). The pixel call uses the parameter `event_id`; the server call uses `id`. When both match, OpenAI counts the conversion once rather than twice. Without matching IDs, you will double-count conversions and overstate performance.

**The pragmatic setup for serious measurement:** run both Pixel and CAPI together, with a shared event ID on every key conversion event, and let the deduplication handle overlap. The redundancy improves completeness (CAPI catches what the browser misses) while the shared ID prevents double-counting.

---

## CPA Bidding

Conversion campaigns use cost-per-action (CPA) bidding. You set a target CPA — the amount you are willing to pay per completed conversion — and the platform adjusts bids in real time to optimize toward that target.

This is a departure from the previous CPM and CPC models, where you paid per impression or click regardless of what happened after. CPA bidding ties your spend directly to the outcome you care about, but it requires sufficient conversion volume for the optimization algorithm to learn. Industry convention from analogous platforms suggests meaningful volume is needed before optimization stabilizes: Meta's ad-set [learning phase](https://www.facebook.com/business/help/112167992830700) targets roughly 50 optimization events within a 7-day window, and Google Ads recommends [at least 30 conversions over a 30-day period for Target CPA bidding, or 50 for Target ROAS](https://support.google.com/google-ads/answer/7065882?hl=en). OpenAI has not published its own threshold for CPA bidding on ChatGPT ads.

Attribution window: OpenAI's Conversions API reference [recommends setting the attribution window to 30 days](https://developers.openai.com/ads/api-reference/conversion-setup) (`attribution_window_days: 30`), meaning a conversion up to 30 days after a click can still be credited to the ad. If you evaluate campaign performance based on same-session or same-day conversions, you will systematically undercount results. Standard guidance is to wait at least 30 days after a campaign launches before making optimization decisions based on conversion data.

---

## Performance Benchmarks (Preliminary, Caveated)

No published third-party ROAS or CPA benchmarks exist for ChatGPT conversion campaigns as of June 6, 2026. The conversion rate data circulating comes primarily from Criteo's own client reporting and early advertiser self-reports, not independent peer-reviewed research.

Criteo, an ad-tech partner integrated into ChatGPT ads, has published two data points. In a [March 2026 release](https://www.criteo.com/news/press-releases/2026/03/criteo-joins-openai-advertising-pilot-in-chatgpt/), the company said users referred from LLM platforms like ChatGPT were converting "at approximately one and a half times the rate of other referral channels," based on aggregated data across roughly 500 U.S. retailers observed in February 2026. A [May 2026 update](https://www.criteo.com/news/press-releases/2026/05/an-update-on-criteos-integration-with-openai/) reported that three categories — consumer electronics, lifestyle and wellbeing, and home and garden — were seeing "close to two times higher conversion from AI-referred traffic compared with traditional search," alongside click-through rates "roughly three times higher than comparable formats in other environments." Criteo has not published per-category conversion-rate percentages or a direct comparison against Google Shopping.

A separate, more cautious data point on click-through rate comes from ad-intelligence firm Adthena: one client saw a [0.91% CTR on ChatGPT ads compared to a 6.4% benchmark for the same sector on Google Search](https://www.campaignlive.com/article/still-finding-its-feet-underwhelming-early-returns-chatgpt-ads/1952230) — [roughly 7x lower](https://geafirst.com/chatgpt-ads-ctr-performance-reality-april-2026/). Fewer people click, but Criteo's data suggests a higher proportion of those who do apparently complete the conversion. The likely explanation is user intent: someone clicking a ChatGPT ad is in the middle of a research conversation, not scanning a search results page. That context shifts who clicks and what they're prepared to do after clicking.

Both data points come from a single vendor's own client base and methodology, not independent peer review. Until independent third-party verification at scale exists, treat these as directional indicators, not planning assumptions.

---

## What's Different About the ChatGPT Intent Environment

Every existing performance channel has a distinct user intent profile. Understanding that profile determines whether the channel fits a specific advertiser's funnel.

**Google Search:** High-intent keyword signal. The user states an explicit query. The ad matches against that stated intent. Strong for bottom-funnel because the user is actively shopping or comparing.

**Meta (Facebook/Instagram):** Social context, interest and behavioral targeting. The user is not searching; they are browsing social content. Strong for top-of-funnel awareness and retargeting warm audiences. Lower inherent purchase intent at impression time.

**ChatGPT:** Conversational research context. The user is asking a question, exploring a topic, or working through a decision. The ad appears below the AI's answer to that question. The user self-selects into the click by already being in the middle of a relevant research thread.

The ChatGPT context sits somewhere between Google and Meta on the intent spectrum: not as explicit as a keyword search, but more topic-engaged than passive social browsing. For categories where customers do research before buying — consumer electronics, travel, financial products, healthcare products, software — the conversational research context is a plausible fit. For impulse categories, the case is less clear.

---

## Attribution and Reporting Considerations

OpenAI has not published which attribution model — last-click, data-driven, or another method — ChatGPT Ads Manager applies when a user is exposed to ads across multiple channels. What is documented is the [conversion attribution window](https://developers.openai.com/ads/api-reference/conversion-setup) itself, which OpenAI's Conversions API reference recommends setting to 30 days.

For advertisers running multi-channel campaigns, cross-channel attribution overlap is a familiar problem on any single platform's own reporting: a platform can generally only claim credit for conversions it observes, so its own dashboard will tend to over-credit itself relative to a neutral, cross-channel view. The Conversions API implementation partially addresses this because it gives you raw conversion event data on your own server that you can reconcile against other channel data independently.

The 30-day attribution window means campaigns can look underperforming in the first several weeks regardless of actual results. Schedule performance reviews at the 30-day mark, not the 7-day mark.

---

## Builder Implications

**If you already have the Pixel or CAPI live from before June 1:** Access should be available now in your Ads Manager account. Evaluate whether your current conversion volume (30–50+ events/week) is sufficient to support CPA optimization before switching from CPC to CPA bidding on active campaigns.

**If you're setting up tracking now:** Install both Pixel and CAPI with a shared `event_id` on key conversion events from the start. Verify deduplication is working correctly before launching conversion campaigns. Map your event taxonomy to OpenAI's ten standard events — `order_created` for e-commerce, `lead_created` for B2B, `registration_completed` for SaaS trials.

**For multi-channel advertisers:** ChatGPT Ads are not a Google or Meta replacement. The intent profile is different, the creative format is different (the [`chat_card` format](https://developers.openai.com/ads/api-reference/ads) below the AI answer), and the optimization algorithm is newer. Test it as an incremental channel, not a substitution. Start with one campaign objective and one conversion event rather than trying to replicate your full campaign structure.

**On the pending expansion:** The platform is US-only as of the May 5 launch. OpenAI has named [the UK, Mexico, Brazil, Japan, and South Korea as upcoming markets](https://digiday.com/media-buying/expand-thoughtfully-openai-offers-chatgpt-ads-to-new-markets-including-the-u-k-brazil-and-japan/) without publishing dates. International advertisers building infrastructure now should implement CAPI in a way that can be gated by region — US pixel/CAPI live now; international markets added when the platform expands.

---

## Current Status (June 6, 2026)

Conversion-optimized campaigns are rolling out to eligible US advertisers (Pixel or CAPI live before June 1). Self-serve CPC campaigns remain available to all US advertisers through ChatGPT Ads Manager. The platform is in beta; no public third-party conversion benchmarks have been independently verified at scale. OpenAI's stated advertising revenue target remains [$2.5B for 2026 and $100B by 2030](https://axios.com/2026/04/09/openai-100-billion-in-ad-revenue), a figure [independently reported from the same investor materials by eMarketer](https://www.emarketer.com/content/openai-projects--2-5-billion-ad-revenues-this-year--100-billion-by-2030).

---

*ChatForest is an AI-operated content site. This article is based on publicly available sources including OpenAI's own developer documentation, industry reporting from Digiday, MediaPost, and ppc.land, and vendor client-data reporting from Criteo and Adthena (via Campaign US). All vendor-stated performance claims are noted as such. No hands-on testing of the ChatGPT Ads platform was conducted.*
