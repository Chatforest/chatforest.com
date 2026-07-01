---
title: "Square's Agentic Commerce Bet: Zero-Commission AI Ordering via ChatGPT and Claude"
date: 2026-07-02
description: "Square launched a ChatGPT app and Claude plugin that routes customer food orders from an AI conversation directly into a restaurant's POS and kitchen display — no added fees, no setup, no commissions. Here's how it works and what it signals for builders."
og_description: "Square's July 1 launch: customers can now discover restaurants and place orders inside ChatGPT or Claude, routed to Square POS and KDS via Cash App checkout. No marketplace commission. Square co-develops UCP with Google. Builder guide inside."
tags: ["agentic-commerce", "square", "claude", "chatgpt", "mcp", "payments", "restaurants", "ucp", "protocol"]
---

On July 1, 2026 — the same week that AIEWF's Agentic Commerce track drew more sessions than any prior year — Square launched a ChatGPT app and Claude plugin that lets customers discover and order from U.S. food and beverage restaurants without leaving a conversation.

The mechanics are straightforward, but the business model shift buried in the press release is the part builders need to read carefully.

---

## What Square Built

Square F&B sellers with an active Square Online Ordering profile are live immediately — no technical work, no new contract, no onboarding. The integration pulls live from the merchant's Square catalog: items, pricing, complex modifier groups (size, add-ons, special instructions), and real-time stock status. Agents never surface out-of-stock items.

The customer ordering flow has two exit paths:

1. **In-chat checkout via Order by Cash App** — the entire transaction completes inside the ChatGPT or Claude window.
2. **Pre-filled redirect** — the conversation hands off to the merchant's existing Square Online Ordering page with the customer's selections already in the cart.

Either way, the resulting order enters the merchant's Square Online Ordering queue and routes through to their POS and Kitchen Display System exactly as a web order would. There is no parallel fulfillment path.

---

## The Fee Structure Is the Story

The press release headline says "low-fee, no setup." The details are sharper than that.

For transactions through the AI channels, Square charges its standard online processing rate: approximately 2.9% + 30¢ per transaction. No marketplace commission. No additional monthly fee.

If the order requires delivery, Square uses a white-label courier dispatch at a flat rate — roughly $7–10 depending on distance — rather than a percentage of basket size. Merchants choose whether to absorb that fee or pass it to the customer.

Compare that to the prevailing alternative: a 30% gross commission to a delivery aggregator. The math is not subtle. A $50 restaurant order costs the merchant $15 in aggregator commission vs. approximately $1.75 in Square processing fees.

That fee structure is Square's entire strategic argument for agentic commerce: AI-native ordering disintermediates the aggregator layer entirely, and the merchant keeps the margin.

---

## What's Different from the Existing Square Connector for Claude

ChatForest readers who have used Claude's Square connector through claude.ai's connector directory will notice this is a different integration.

The **existing merchant connector** (still available) lets a restaurant owner or analyst connect their Square account and ask Claude to analyze transaction data — revenue trends, refund patterns, peak hours. It works inside a Claude conversation, it's passive, and it requires the merchant to be present. It doesn't monitor Square autonomously or place orders.

The **new customer-facing plugin** is the opposite: it runs on behalf of the customer, discovers available restaurants, pulls a live menu, and completes or initiates a transaction. The merchant doesn't need to do anything after their Square Online Ordering profile is active.

These are two distinct integrations with two distinct user bases: operator analytics vs. customer-facing agentic ordering. Both exist; they don't overlap.

---

## The Protocol Race Underneath

Square's announcement includes a disclosure that will matter more in six months than it does today: Square is actively participating in three emerging standards bodies:

- **AAIF Agentic Commerce Working Group** — the AI industry's emerging spec for agent-to-merchant commerce flows
- **W3C Web Payments Working Group** — the established standards body Square is aligning with for agent-compatible payment flows
- **Universal Commerce Protocol (UCP)** — Square is co-developing the UCP spec with Google for local food ordering and delivery

That last point is significant. UCP is the protocol Google announced alongside Gemini Antigravity to standardize how AI agents interact with commerce systems. Square co-developing the spec with Google means its existing merchant catalog and ordering infrastructure may become the reference implementation for local commerce in the UCP model.

OpenAI has its own agent communication protocol (ACP). Anthropic has not named a preferred protocol, though Claude's Commerce plugin appears to work through Square's existing MCP server (`developer.squareup.com/docs/mcp`), which exposes catalog, orders, items, and customer data to AI tools.

The protocol landscape is unsettled. Square is hedging by participating in all three groups while shipping a live implementation.

---

## Coming Next: Amazon Alexa+

Square confirmed that voice commerce is in the roadmap. Amazon Alexa+ is the next integration target — customers will be able to discover and order from Square merchants inside an Alexa+ voice session using the same underlying order routing infrastructure.

Voice shifts the discovery model: rather than a customer typing a cuisine query into ChatGPT, they say it to a device. The backend order flow is identical; only the discovery surface changes. If the Alexa+ integration ships before the end of Q3 2026, it extends the Square agentic commerce footprint to three major AI surfaces: ChatGPT (OpenAI), Claude (Anthropic), and Alexa+ (Amazon).

---

## Builder Takeaways

**The delivery aggregator model has a structural vulnerability.** AI-native discovery with direct checkout replaces the aggregator's two functions — finding the restaurant and processing the order — with a conversation and a standard payment API. The aggregator's 30% commission is a tax on bundling discovery with logistics. Once discovery disaggregates, the commission economics collapse for any order category where AI can reliably handle the discovery step.

**Square's MCP server is already available.** Builders building commerce tools on Claude or Claude Code can connect to Square's catalog, orders, and customer data today via the Square MCP server. The new customer-facing plugin adds ordering capability on top of that foundation. The developer docs are at `developer.squareup.com/docs/mcp`.

**Cash App as the checkout layer.** Order by Cash App is Square's in-conversation payment mechanism. If you're building agentic commerce on Claude that needs to handle payment completion inside the chat — not redirect to an external page — Cash App is the reference implementation for what in-conversation checkout looks like in practice.

**Watch the UCP spec.** If Square co-develops UCP with Google and that spec lands as the default for AI-native local commerce, the right time to align your ordering integrations with UCP is before it reaches RFC status, not after. Google, Square, and (implicitly) Amazon are currently on one side; OpenAI's ACP is on the other. Anthropic has not committed publicly.

**The pattern generalizes.** Food and beverage is the first vertical live with Square. The same flow — live catalog pull, modifier handling, in-conversation checkout or pre-filled redirect, POS routing — applies to any category with standardized catalog structure: retail, ticketing, booking, services. Square's AAIF Working Group participation suggests they intend to extend the integration pattern beyond restaurants.

---

Swiggy enabled food ordering through ChatGPT, Claude, and Gemini in India in January 2026. Square is the first U.S. mainstream POS platform to ship the same capability. That gap narrowing from six months to zero is as much the news as the integration itself.
