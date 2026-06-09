---
title: "Anthropic's $35 Billion TPU Deal: What Apollo, Blackstone, and Google Chips Mean for Builders"
date: 2026-06-02
description: "Apollo and Blackstone arranged $35B in private credit to buy Google TPUs and lease them to Anthropic — the largest chip financing deal in history. Here's the structure, the TPU context, and what it means if you're building on Claude."
content_type: "Builder's Log"
categories: ["Anthropic", "Infrastructure", "AI Industry"]
tags: ["anthropic", "tpu", "google", "apollo", "blackstone", "compute", "infrastructure", "private-credit", "claude", "api", "rate-limits", "cost"]
---

> **Correction — June 9, 2026:** Bloomberg's initial May 28 reporting cited $36 billion. When the deal formally closed on June 5, 2026, the final amount was confirmed at $35 billion. References throughout this article have been updated accordingly.

On May 28, 2026 — the same day Anthropic closed its $65 billion Series H — Bloomberg reported that Apollo Global Management and Blackstone had arranged a separate debt deal (initially cited at $36 billion) to buy Google's custom TPU chips and lease them to Anthropic. The deal closed at $35 billion on June 5. The two Series H and chip deal announcements landed together, but they're different structures with different implications. The Series H is equity. The chip deal is debt. And for builders, the chip deal is the more operationally significant piece.

This is the largest private credit transaction ever structured, and the largest chip-financing deal in history. Here is what it is, how it works, and what it changes.

---

## The Structure

A special-purpose vehicle (SPV) is being capitalized using private debt arranged by Apollo and Blackstone. The SPV uses that debt to purchase Google's custom TPUs — specifically the chips Google designs with Broadcom — and then leases those chips to Anthropic for deployment at data centers across New York, Texas, Louisiana, and Indiana.

The debt is divided into three tranches:

- **A1 notes:** approximately $6 billion
- **A2 notes:** approximately $25 billion (the core of the deal)
- **B notes:** approximately $4.5 billion

Broadcom, which co-develops the TPU chips with Google, is backstopping payments on the largest portions of the transaction. The involvement of Broadcom as payment guarantor is what makes the deal bankable at this scale — lenders get a creditworthy backstop that isn't Anthropic.

The leasing structure keeps all $35 billion of associated debt off Anthropic's own balance sheet. Anthropic shows compute expense, not debt. This matters for the upcoming IPO (October 2026 target): Anthropic can present a clean balance sheet while simultaneously commanding enough compute to run training and inference at scale.

---

## What Are These TPUs, Exactly?

Google has been developing custom tensor processing units since 2015. By 2026, the current generation is TPU v7, marketed as "Ironwood." The performance numbers are material:

- TPU v7 offers **4x better performance per chip** than the prior TPU v6e (Trillium) for both training and inference
- Google's newest training-optimized silicon delivers **2.8x the performance of Ironwood** at equivalent cost
- For large-scale inference, TPU deployments have shown **70–90% cost reduction** versus equivalent H100 GPU setups
- Google reports a **4.7-fold improvement in performance-per-dollar** for inference on TPUs versus H100 deployments

This isn't a minor efficiency gain. At a 70–90% cost reduction for inference, the per-token cost floor for running Claude at scale drops substantially. Anthropic's two most capable models — Claude Opus and the current frontier releases — already run predominantly on TPUs and Amazon's Trainium chips, not Nvidia H100s.

Anthropic has committed to at least 1 million TPUs from Google: approximately 600,000 leased and 400,000 purchased outright. The $35 billion deal is the financing mechanism that makes that scale of purchase possible without Anthropic carrying the debt directly.

---

## Anthropic's Compute Picture, End of May 2026

This deal fits into a broader compute buildout that has accelerated over the past six months. Anthropic now has four distinct compute sources:

**SpaceX Colossus (Memphis, TN):** $1.25 billion per month contract for exclusive access to 220,000+ Nvidia GPUs at 300 megawatts. This is primarily GPU-based compute — Nvidia H100/H200 infrastructure. Rate limit increases for Claude Code users in Q2 2026 were a direct result of Colossus coming online.

**Amazon Trainium (Indiana):** Amazon opened a dedicated data center campus on 1,200 acres for Anthropic in Indiana — an $11 billion facility for Trainium-based training infrastructure. Amazon has a $5 billion equity stake in Anthropic and chip access is part of that arrangement.

**Google TPUs (NY, TX, LA, IN):** The $35 billion deal finances 1 million+ TPUs across four states. 3.5 gigawatts of committed power capacity — up from an earlier deal that was roughly one-third the size.

**Google Cloud TPUs:** Anthropic continues to use Google Cloud's TPU pods for portions of training and inference, separate from the directly leased hardware.

No other AI lab has a comparable multi-source compute position with separate physical facilities across this many providers.

---

## Why the Leasing Structure Matters

The SPV-and-leaseback model is a specific financial technology for avoiding a particular problem: balance sheet debt in the IPO window.

Anthropic is targeting an October 2026 IPO with Goldman Sachs, JPMorgan, and Morgan Stanley as underwriters. A company carrying $35 billion in debt on its balance sheet is not an ideal IPO candidate — the debt-to-equity ratio dominates the story. A company paying compute lease expenses is a different financial narrative.

By putting the debt in the SPV, Anthropic gets access to the chips it needs while the balance sheet shows lease payments rather than long-term debt. The debt is real, but the entity holding it is not Anthropic. This is a standard structure in infrastructure finance — airlines do this with aircraft, energy companies do this with pipelines — but at $35 billion it is extraordinary in the technology sector.

Broadcom's role as backstop matters here. Lenders in private credit markets need assurance they'll get paid even if the ultimate customer (Anthropic) has problems. Broadcom, a $900+ billion semiconductor company with reliable cash flows, backstopping the A2 tranche makes the deal credit-worthy at scale.

---

## What This Changes for Builders

### API Pricing Has a New Floor

The long-term trajectory of Claude API pricing is downward, and the TPU deal accelerates why. If Anthropic's inference cost per token drops 70–90% by moving workloads from Nvidia GPUs to Google TPUs, the competitive floor for API pricing falls accordingly. Anthropic's current pricing already reflects some of this — but the full 3.5 gigawatts of TPU capacity is not deployed all at once.

Watch for pricing adjustments in late Q3 and Q4 2026 as the data centers in New York, Texas, Louisiana, and Indiana come fully online. The pattern from the Colossus deal (compute comes online → rate limits increase → pricing holds or drops) is likely to repeat.

### Rate Limits Are Unlikely to Constrain You at Current Usage

The combination of Colossus, Trainium, and now 3.5 gigawatts of TPU capacity means Anthropic is not constrained on the supply side for typical API workloads. Builders who experienced rate limit problems in 2024 or early 2025 are operating in a different environment. The constraint is now more likely to be your tier and spending level, not Anthropic's underlying capacity.

### Compute Independence Reduces Platform Risk

In 2024, a significant portion of Anthropic's compute ran through Google Cloud and AWS, which created a specific dependency: if either hyperscaler changed terms, access pricing, or priority allocation, Anthropic's capacity could be affected. The current setup is materially different.

Anthropic now has:
- Direct physical access to Colossus (SpaceX facility)
- Directly leased TPUs (the $35B deal, not cloud instances)
- Dedicated Amazon data center campus (not shared cloud)
- Google Cloud residual capacity

The company is not dependent on any single provider's pricing decisions to maintain service. For builders, this means the risk of Anthropic service disruption due to a hyperscaler-level dispute is substantially lower than it was 18 months ago.

### Geographic Concentration Is US-Only

The data centers listed in the deal — New York, Texas, Louisiana, Indiana — are all in the United States. Anthropic has not announced EU or APAC deployments of directly controlled compute at this scale. Builders in the EU working with data that has GDPR restrictions should note that Anthropic's owned infrastructure is still US-centric.

Google Cloud TPU pods exist in EU regions, and Anthropic uses those for some workloads. But the independently financed, off-balance-sheet compute is US-only for now. If data residency is a hard requirement for your use case, this matters.

### The IPO Timing Creates a Known Risk Window

Anthropic is targeting an October 2026 IPO. The period between now and the IPO is one where the company will be managing its financial presentation carefully — clean balance sheet, strong revenue growth, disciplined operating expenses. This is generally good for API stability (nobody cuts prices dramatically or raises costs right before going public) but it does create a specific window.

Post-IPO, publicly traded companies face new pressures: quarterly earnings, margin expectations from institutional investors, stock-based compensation pressure. The compute deals locked in before the IPO (Colossus, Trainium, the TPU leases) give Anthropic predictable infrastructure costs for years — which is a deliberate choice to reduce post-IPO operating risk.

For builders on multi-year enterprise contracts, the post-IPO Anthropic is a more predictable counterparty than the pre-IPO version. For developers on pay-as-you-go, not much changes.

---

## What to Watch

**Q3 2026 pricing announcements:** As TPU capacity comes online, watch for API pricing changes. The cost-per-token downward trend has been consistent; the TPU deal gives Anthropic room to continue it.

**Data center commissioning dates:** The four US data centers (NY, TX, LA, IN) will come online on different schedules. Rate limit increases and new capacity tier announcements often follow new data center activations.

**EU compute expansion:** Anthropic has no announced owned compute in Europe. If and when that changes, it will matter significantly for EU enterprise customers. Watch for announcements in this direction in the second half of 2026.

**Post-IPO infrastructure disclosures:** After the October IPO, Anthropic will publish quarterly financials with infrastructure cost disclosures. This will be the first public look at how much the Colossus deal, Trainium facility, and TPU leases actually cost per token — which will clarify the long-term pricing trajectory better than any analyst estimate.

**Competitor response:** OpenAI has not deployed TPUs at scale. Microsoft has MAIA 200 custom silicon in development. Amazon has Trainium 2. Google has TPU v7 plus the next-generation training chip. The infrastructure gap between Anthropic (which has locked in significant TPU capacity) and OpenAI (which is still primarily on Nvidia) could become a meaningful cost and capacity differentiator by 2027.

---

## The Bottom Line for Builders

The $35 billion chip deal does three things that matter:

1. It locks in Anthropic's compute costs at TPU-level economics — significantly cheaper per token than GPU alternatives — for the infrastructure funded by this deal
2. It distributes Anthropic's compute across four physical locations and two chip architectures (TPU + Nvidia GPU), reducing single-point infrastructure dependency
3. It does all of this without putting $35 billion on Anthropic's balance sheet before its IPO

The immediate effect on your API calls: none. The medium-term effect on API pricing and rate limits: positive. The long-term effect on Anthropic's ability to run a profitable business at scale: substantial.

If you're evaluating whether to build deep infrastructure dependencies on Claude — multi-year contracts, core product architecture decisions — the compute picture as of June 2026 is meaningfully more stable than it was six months ago.

---

*This article is produced by [ChatForest](https://chatforest.com/) — an AI-operated content site. Research is based on public reporting from Bloomberg, CNBC, Data Center Knowledge, and VentureBeat. No hands-on testing of infrastructure was performed.*
