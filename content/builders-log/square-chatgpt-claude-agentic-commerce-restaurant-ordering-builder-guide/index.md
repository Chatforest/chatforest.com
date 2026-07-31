---
title: "Square's Agentic Commerce Bet: Zero-Commission AI Ordering via ChatGPT and Claude"
date: 2026-07-02
description: "Square launched a ChatGPT app and Claude plugin that routes customer food orders from an AI conversation directly into a restaurant's POS and kitchen display — no added fees, no setup, no commissions. Here's how it works and what it signals for builders."
og_description: "Square's July 1 launch: customers can now discover restaurants and place orders inside ChatGPT or Claude, routed to Square POS and KDS via Cash App checkout. No marketplace commission. Square co-develops UCP with Google. Builder guide inside."
tags: ["agentic-commerce", "square", "claude", "chatgpt", "mcp", "payments", "restaurants", "ucp", "protocol"]
sources_audited: 2026-08-01
---

On July 1, 2026 — the same week as the [Agentic Commerce track at AI Engineer World's Fair](https://www.ai.engineer/worldsfair/schedule) in San Francisco — [Square launched a ChatGPT app and Claude plugin](https://squareup.com/us/en/press/claude-chatgpt-integrations) that lets customers discover and order from U.S. food and beverage restaurants without leaving a conversation.

The mechanics are straightforward, but the business model shift buried in the press release is the part builders need to read carefully.

---

## What Square Built

Square F&B sellers with an active Square Online Ordering profile are live immediately: Square's own announcement says [eligible sellers are opted in "with no additional work, setup, or fees required. There is no API to build, no new tool to configure, and no added cost."](https://squareup.com/us/en/press/claude-chatgpt-integrations) Square syncs the merchant's business information, menu data, hours, and ordering information [in real time](https://squareup.com/us/en/press/claude-chatgpt-integrations), and the source of each order is visible in the seller's existing Square reporting.

The customer completes checkout inside the ChatGPT or Claude conversation using [Order by Cash App](https://squareup.com/us/en/press/claude-chatgpt-integrations). The resulting order [routes directly into the merchant's existing Square Online Ordering setup, including POS and Kitchen Display System](https://squareup.com/us/en/press/claude-chatgpt-integrations) — there is no parallel fulfillment path.

---

## The Fee Structure Is the Story

The press release headline says "low-fee, no setup." Square's own release confirms [no additional marketplace commission and no added monthly fee](https://squareup.com/us/en/press/claude-chatgpt-integrations) for orders placed through the AI channels — but it does not quote a specific processing percentage for this integration.

What applies instead is Square's standard online processing rate. Per [Square's own published fee schedule](https://squareup.com/help/us/en/article/5068-what-are-square-s-fees), that's 3.3% + 30¢ per transaction on the Free plan, or 2.9% + 30¢ on the paid Plus and Premium plans. [VentureBeat's coverage of the launch](https://venturebeat.com/technology/restaurants-can-now-accept-orders-placed-directly-from-chatgpt-and-claude-thanks-to-squares-new-low-fee-no-setup-integration) reports the same tiered rate applying to orders placed through ChatGPT and Claude — no separate "AI channel" fee.

Compare Square's rate to a typical third-party delivery aggregator commission. [DoorDash's published merchant pricing](https://merchants.doordash.com/en-us/pricing) runs 15%, 25%, or 30% per delivery order depending on plan tier. On a $50 order, a 30% aggregator commission is $15; Square's processing fee on the same order is $1.75–$1.95 depending on plan. That gap is Square's strategic argument for agentic commerce: AI-native ordering that routes around the aggregator layer lets the merchant keep the difference.

---

## What's Different from the Existing Square Connector for Claude

ChatForest readers who have used Claude's [Square connector](https://claude.com/connectors/square) through claude.ai's connector directory will notice this is a different integration.

The **existing merchant connector** (still available) lets a restaurant owner or analyst [connect their Square account and ask Claude to analyze transaction data](https://claude.com/connectors/square) — revenue trends, refund patterns, peak hours. It works inside a Claude conversation, it's passive, and it requires the merchant to be present. It doesn't monitor Square autonomously or place orders.

The **new customer-facing plugin** is the opposite: it runs on behalf of the customer, discovers available restaurants, pulls a live menu, and completes or initiates a transaction. The merchant doesn't need to do anything after their Square Online Ordering profile is active.

These are two distinct integrations with two distinct user bases: operator analytics vs. customer-facing agentic ordering. Both exist; they don't overlap.

---

## The Protocol Race Underneath

Square's announcement includes a disclosure that will matter more in six months than it does today: Square says it's [actively participating in emerging agentic commerce protocol groups](https://squareup.com/us/en/press/claude-chatgpt-integrations), naming three:

- **[AAIF Agentic Commerce Working Group](https://aaif.io/working-groups)** — one of seven working groups under the Linux Foundation's [Agentic AI Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation), focused on AI agents conducting transactions and financial operations autonomously
- **[W3C Web Payments Working Group](https://www.w3.org/Payments/WG/charter-2022.html)** — the W3C's standing effort to standardize messages and message flow for initiating, confirming, and completing web payments
- **Universal Commerce Protocol (UCP)** — Square's release says it's ["partnering with Google to co-develop the UCP spec for local food ordering and delivery"](https://squareup.com/us/en/press/claude-chatgpt-integrations)

Worth separating Square's role from UCP's origin: UCP itself is a broader, pre-existing effort. [Google and Shopify announced the open protocol on January 11, 2026 at the National Retail Federation conference](https://developers.googleblog.com/under-the-hood-universal-commerce-protocol-ucp/), and more than 20 companies — including Etsy, Wayfair, Target, Walmart, Visa, Mastercard, and Stripe — have endorsed it. Square's press release describes Square's own contribution as co-developing the local-food-ordering piece of that spec with Google, not the protocol as a whole.

OpenAI has a competing standard: the [Agentic Commerce Protocol (ACP)](https://developers.openai.com/commerce), which OpenAI [co-developed with Stripe and launched September 29, 2025 with Etsy as the first integrated marketplace](https://stripe.com/newsroom/news/stripe-openai-instant-checkout). Anthropic has not named a preferred protocol. Square also runs a [separate developer-facing MCP server](https://developer.squareup.com/docs/mcp) exposing catalog, orders, items, and customer data for builders — but Square's press release doesn't say the new Claude ordering plugin runs on it, and we found no source confirming that link, so treat the two as distinct until Square documents otherwise.

The protocol landscape is unsettled. Square is hedging by participating in multiple groups while shipping a live implementation.

---

## Amazon Alexa+: A Different Category, Already Live

Square's press release says it's ["also working with Amazon to bring sellers into Alexa+ experiences, extending AI-powered discovery into voice commerce"](https://squareup.com/us/en/press/claude-chatgpt-integrations) — without saying which merchant categories, or on what timeline.

It's worth being precise here, because it's easy to assume this means restaurant ordering extending to voice. It doesn't, at least not yet. Square and Amazon already shipped a live Alexa+ integration months before this July announcement, and it's about a different vertical entirely: [Amazon's own announcement](https://www.aboutamazon.com/news/devices/alexa-plus-voice-booking-integrations) and [TechCrunch's coverage](https://techcrunch.com/2025/12/23/amazons-ai-assistant-alexa-now-works-with-angi-expedia-square-and-yelp/) describe a December 2025 launch letting Alexa+ users discover and book appointments with Square's beauty-and-wellness sellers — spas, hair and nail salons, barbershops — not restaurants, and not food ordering.

Whether Square's new food-ordering flow will extend to Alexa+ specifically, and when, isn't stated in Square's press release or in any other source we found for this piece. Treat "voice ordering is coming to Alexa+" as a plausible next step, not a confirmed one.

---

## Builder Takeaways

**The delivery aggregator model has a structural vulnerability.** AI-native discovery with direct checkout replaces the aggregator's two functions — finding the restaurant and processing the order — with a conversation and a standard payment API. A [15-30% aggregator commission](https://merchants.doordash.com/en-us/pricing) is, in large part, a tax on bundling discovery with logistics. Once discovery disaggregates, the commission economics compress for any order category where AI can reliably handle the discovery step.

**Square's MCP server is already available.** Builders building commerce tools on Claude or Claude Code can connect to Square's catalog, orders, and customer data today via the [Square MCP server](https://developer.squareup.com/docs/mcp), independent of the new customer-facing ordering plugin discussed above.

**Cash App as the checkout layer.** Order by Cash App is Square's in-conversation payment mechanism. If you're building agentic commerce on Claude that needs to handle payment completion inside the chat — not redirect to an external page — Cash App is the reference implementation for what in-conversation checkout looks like in practice.

**Watch the UCP spec.** Square's own release describes it as co-developing the food-ordering piece of UCP with Google; Google and Shopify are the protocol's broader backers. If UCP lands as a default for AI-native local commerce, the right time to align your ordering integrations with it is before it reaches wide adoption, not after. Google and Square are on one side; OpenAI's ACP (co-developed with Stripe) is on the other. Anthropic has not committed publicly to either.

**The pattern generalizes, cautiously.** Food and beverage is the first vertical live with Square. The same underlying flow — live catalog pull, in-conversation checkout, POS routing — plausibly applies to any category with a standardized catalog: retail, ticketing, booking, services. Square's AAIF Working Group participation is a hint they intend to extend the pattern beyond restaurants, but Square hasn't said so directly.

---

[Swiggy enabled food and grocery ordering through ChatGPT, Claude, and Gemini in India](https://yourstory.com/2026/01/swiggy-lets-users-order-through-chatgpt-claude-gemini), rolling out on [January 27–28, 2026](https://www.medianama.com/2026/01/223-ordering-chatgpt-swiggy-services-working/). Square is now shipping a comparable capability for U.S. restaurants roughly six months later. That gap narrowing is as much the news as the integration itself.
