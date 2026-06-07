---
title: "ChatGPT Ads Go Full Performance: Conversion Campaigns, UK Launch, and What Builders Actually Need to Know"
date: 2026-06-07
description: "ChatGPT went from a $200K CPM pilot to a full performance ad channel in four months. Conversion-optimized campaigns launched June 5. The UK opened June 6. Japan, South Korea, Brazil, and Mexico are next. Here's the complete picture for builders."
og_description: "ChatGPT launched conversion-optimized campaigns on June 5 and opened the UK on June 6 — its first European market. The API stays ad-free. Free and Go users see ads. Plus, Pro, and Enterprise do not. Here's what this changes for builders."
content_type: "Builder's Log"
categories: ["OpenAI", "Platform Strategy", "Marketing"]
tags: ["chatgpt", "openai", "advertising", "ads-manager", "conversion-optimization", "performance-marketing", "platform-strategy", "builder-guide", "monetization", "uk"]
---

In four months, OpenAI turned ChatGPT into a performance advertising channel.

The arc: February 9, 2026 — ads launched in the US on Free and Go tiers with a $200,000–$250,000 minimum spend and a CPM model. By March 26, the pilot crossed $100 million in annualized run-rate revenue in under two months. April and May: the self-serve Ads Manager launched, CPC bidding was added, and the $50,000 minimum was dropped entirely. June 2: product feeds shipped. **June 5: conversion-optimized campaigns went live.** **June 6: the UK became the first European market.**

If you build software, AI tools, or products that target the people using ChatGPT — which is to say, most of the internet — this is now a distribution channel you need to understand.

---

## What ChatGPT Ads Actually Look Like

Ads appear in clearly labeled, subtly tinted boxes **below** AI responses — never woven into the answer itself. The format is a sponsored product card: brand logo, a "Sponsored" label, product name, price, stock status, and estimated delivery or prep time. OpenAI is explicit that the ad placement cannot influence ChatGPT's actual answer to a query.

Targeting is **conversation-contextual**, not keyword-based. The system matches ads against the current conversation topic, the user's chat history, and past ad interactions. This is meaningfully different from search advertising: there is no keyword auction. If your product is relevant to what users are actively discussing with ChatGPT, you can appear at the moment of engagement.

Ads are shown to **Free and Go tier users only**. Plus, Pro, and Enterprise subscribers see no ads.

---

## The June Milestones

### Conversion Optimization (June 5)

Until June 5, ChatGPT Ads was an awareness and traffic platform. Advertisers could buy clicks and impressions, but conversion measurement — tracking whether a ChatGPT ad led to a purchase, signup, or other downstream action — was not part of the product.

That changed with the June 5 launch of conversion-optimized campaigns. Accounts that set up OpenAI's Pixel or Conversions API before June 1 received early access; general rollout follows.

This is a structural shift. Awareness advertising asks "did the user see the ad?" Performance advertising asks "did the ad cause a business outcome?" The gap between those questions is where most ad budgets live. Conversion optimization opens ChatGPT to advertisers who have always measured on CPA and ROAS — not just brands running reach campaigns.

### UK Launch (June 6)

On June 6, OpenAI VP of Monetization Benji Shomair announced the UK as the first European market to go live. The UK is the largest English-language digital advertising market outside North America and one of the top five global digital ad markets overall.

International expansion continues to Japan, South Korea, Brazil, and Mexico in the coming weeks. The five-market plan was signaled May 7. The UK is the first activation.

---

## The Revenue Trajectory

| Period | Milestone |
|--------|-----------|
| February 9, 2026 | US pilot launch; $200K–$250K minimum, CPM model |
| March 26, 2026 | Crossed $100M annualized revenue in <2 months |
| April–May 2026 | Self-serve Ads Manager; CPC added; minimum dropped |
| June 2, 2026 | Product feeds shipped |
| June 5, 2026 | Conversion-optimized campaigns launched |
| June 6, 2026 | UK expansion; first European market |
| Weeks ahead | Japan, South Korea, Brazil, Mexico |

OpenAI's internal projection: **$2.5 billion in advertising revenue in 2026**. The longer-term target is $100 billion annually by 2030. That trajectory would make ChatGPT's ad business larger than any current ad platform in the US other than Google and Meta.

---

## How to Actually Buy Ads

The self-serve **OpenAI Ads Manager** is the entry point. No minimum spend. CPC and CPM bidding are both available.

For teams managing multiple clients or accounts at scale, OpenAI has API connections through certified partners: **Criteo**, **Kargo**, **Adobe**, **Pacvue**, and **StackAdapt**. Criteo reported more than 1,000 brands running campaigns through its API connection as of May 5. A first-party API for programmatic buying directly via OpenAI is expected but not yet publicly documented.

The product feed integration (added June 2) allows e-commerce merchants to connect structured product catalogs and auto-generate ad creatives from product names, images, and attributes. This is the same model as Google Shopping and Meta Advantage+ catalog ads — a format that dramatically lowers the cost of producing ad creatives at scale.

For conversion tracking, you will need to implement either OpenAI's Pixel (JavaScript tag) or the Conversions API (server-to-server event sending). The same infrastructure you likely already have for Google and Meta will work here with minimal modification.

---

## What Builders Need to Know

### The API is ad-free

If you access ChatGPT through the OpenAI API — for any product you build — no ads appear. The advertising layer exists only in the ChatGPT.com UI for Free and Go users. Your API calls are not modified, annotated, or influenced by the advertising system.

This distinction matters if you are building on the OpenAI API and worried that ads will contaminate responses or change model behavior in your product. They will not.

### Your users may see ads depending on their ChatGPT tier

If you build a product that directs users to ChatGPT.com directly — or if your users also use ChatGPT on the Free or Go tier — they will see ads below responses. Plus, Pro, and Enterprise subscribers do not.

For builder tools, developer utilities, and professional-tier AI products, the user base that matters most is typically on paid tiers, so the impact may be minimal. For consumer-facing AI products targeting price-sensitive users on Free tiers, ads are now part of the user experience you are building around.

### ChatGPT is now a legitimate acquisition channel for AI tools

The audience inside ChatGPT is now over one billion monthly active users. The majority are on Free or Go tiers. They are, by definition, people who use AI tools actively.

If you build an AI product that complements or extends ChatGPT — a specialized coding agent, a writing assistant, a data tool, an MCP server — advertising inside ChatGPT reaches a highly self-selected AI-tool buyer. The conversation-contextual targeting means your ad can appear when a user is actively discussing the exact problem your tool solves.

This is closer to intent-based advertising (search) than impression-based advertising (display), but without a keyword auction. The first-mover advantage is real: early advertisers in a new channel set the baseline for what works before costs normalize.

### Product catalog integration is e-commerce native

The June 2 product feed integration makes ChatGPT Ads immediately relevant to any builder shipping a commerce layer inside an AI product. If you have a product catalog — physical goods, software subscriptions, digital products — you can connect it to ChatGPT Ads and auto-generate sponsored cards from structured data. This is the same workflow as Google Merchant Center and Meta Commerce Manager.

### International timing

The UK is live as of June 6. If you have UK users or advertisers, you can run now. Japan, South Korea, Brazil, and Mexico are weeks away. If those markets matter for your distribution strategy, set up your Ads Manager account now so campaigns can go live on day one of each market opening.

---

## What Is Not Yet Available

A direct programmatic API from OpenAI for buying ads without going through a partner is not yet public. Attribution windows and cross-channel measurement standards are still evolving. The platform does not yet offer audience lookalike targeting or retargeting (though Dreaming V3 — ChatGPT's new persistent memory system — will likely enable more sophisticated user segmentation over time).

Geographic targeting below the country level is not confirmed for most markets.

---

## The Bigger Picture

OpenAI went from "we will never run ads" to a full performance advertising platform in roughly a year. The February launch, March $100M milestone, and June conversion-optimization upgrade represent the fastest ad platform ramp in the history of digital advertising.

Whether that changes the fundamental calculus of building on OpenAI's platform depends on what you build. If you build through the API: nothing changes. If you build consumer products or use ChatGPT.com as part of your user journey: ads are now a structural part of that environment.

The advertising system is currently OpenAI's most visible path to covering the cost of inference at scale without relying entirely on subscription revenue. For builders, that has an indirect benefit: a more financially sustainable model at the platform level reduces the likelihood of dramatic pricing changes to the API.

---

*ChatGPT Ads Manager is accessible at [ads.openai.com](https://ads.openai.com). UK advertisers can apply now. API-based campaign management is available through Criteo, Kargo, Adobe, Pacvue, and StackAdapt.*
