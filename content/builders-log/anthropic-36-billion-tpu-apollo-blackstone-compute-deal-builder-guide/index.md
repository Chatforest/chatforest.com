---
title: "Anthropic's $35 Billion TPU Deal: What Apollo, Blackstone, and Google Chips Mean for Builders"
date: 2026-06-02
description: "Apollo and Blackstone arranged $35B in private credit to buy Google TPUs and lease them to Anthropic — the largest chip financing deal in history. Here's the structure, the TPU context, and what it means if you're building on Claude."
content_type: "Builder's Log"
categories: ["Anthropic", "Infrastructure", "AI Industry"]
tags: ["anthropic", "tpu", "google", "apollo", "blackstone", "compute", "infrastructure", "private-credit", "claude", "api", "rate-limits", "cost"]
sources_audited: 2026-07-28
---

> **Correction — June 9, 2026:** Bloomberg's initial May 28 reporting cited $36 billion. When the deal formally closed on June 5, 2026, the final amount was confirmed at $35 billion. References throughout this article have been updated accordingly.

On May 28, 2026 — the same day Anthropic closed its $65 billion Series H — [Bloomberg reported](https://www.bloomberg.com/news/articles/2026-05-28/apollo-shops-36-billion-debt-deal-to-buy-google-chips-for-anthropic) that Apollo Global Management and Blackstone had arranged a separate debt deal (initially cited at $36 billion) to buy Google's custom TPU chips and lease them to Anthropic. [The deal closed at $35 billion on June 5](https://www.bloomberg.com/news/articles/2026-06-05/apollo-wraps-up-35-billion-debt-to-buy-ai-chips-for-anthropic). The two Series H and chip deal announcements landed together, but they're different structures with different implications. The Series H is equity. The chip deal is debt. And for builders, the chip deal is the more operationally significant piece.

This is the largest private credit transaction ever structured, and the largest chip-financing deal in history. Here is what it is, how it works, and what it changes.

---

## The Structure

A special-purpose vehicle (SPV) is being capitalized using private debt arranged by Apollo and Blackstone. The SPV uses that debt to purchase Google's custom TPUs — [chips Broadcom co-designs with Google, translating Google's specifications into manufacturable silicon](https://www.tomshardware.com/tech-industry/semiconductors/custom-ai-asics-examined-from-broadcom-to-mtia) — and then leases those chips to Anthropic for deployment at data centers in [New York and Texas](https://finance.yahoo.com/news/anthropic-to-spend-50-billion-on-us-data-center-buildout-155605972.html) and at a [Louisiana site (River Bend), where Google is backstopping the lease Anthropic's build partner Fluidstack signed with Hut 8](https://www.prnewswire.com/news-releases/hut-8-signs-15-year-245-mw-ai-data-center-lease-at-river-bend-campus-with-total-contract-value-of-7-0-billion-302644600.html).

The debt is divided into three tranches ([pricing details](https://finance.yahoo.com/markets/stocks/articles/pricing-details-emerge-36b-private-212901754.html)):

- **A1 notes:** $6 billion, "super-senior," priced at 1 point over Treasuries
- **A2 notes:** $25 billion in first-lien senior notes, priced at a 5.50–5.75% all-in yield
- **B notes:** $4.5 billion in second-lien notes, priced at an 8.5% fixed coupon

[Broadcom is the sole backstop on the A1 and A2 notes — roughly $31 billion of the debt — through a residual-value support agreement](https://finance.yahoo.com/markets/stocks/articles/pricing-details-emerge-36b-private-212901754.html): if Anthropic stops paying and the SPV can't recover enough by reselling the TPUs, Broadcom covers the shortfall. The B notes carry no Broadcom backing. This backstop is what makes the deal bankable at this scale — lenders get a creditworthy guarantor that isn't Anthropic.

The leasing structure keeps all $35 billion of associated debt off Anthropic's own balance sheet. Anthropic shows compute expense, not debt. This matters for the upcoming IPO (October 2026 target): Anthropic can present a clean balance sheet while simultaneously commanding enough compute to run training and inference at scale.

---

## What Are These TPUs, Exactly?

Google has been developing custom tensor processing units since 2015. By 2026, the current generation is TPU v7, marketed as "Ironwood." The performance numbers are material:

- TPU v7 ("Ironwood") offers [more than 4x better performance per chip than the prior TPU v6e (Trillium), for both training and inference](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/)
- Google's eighth-generation training chip, TPU 8t, is designed to deliver [up to 2.8x better training price-performance than Ironwood](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)

This isn't a minor efficiency gain — generation-over-generation, Google's own numbers put the price-performance gains at 4x and then another 2.8x on top of that. [Anthropic's two most capable models already run predominantly on TPUs and Amazon's Trainium chips rather than Nvidia GPUs](https://www.anthropic.com/news/google-broadcom-partnership-compute), a deliberate choice Anthropic has said comes down to price-performance and efficiency.

Anthropic has committed to [access to up to one million TPU chips from Google, with well over a gigawatt of capacity coming online in 2026](https://www.googlecloudpresscorner.com/2025-10-23-Anthropic-to-Expand-Use-of-Google-Cloud-TPUs-and-Services). Google's disclosures don't break out how many of those chips are leased versus purchased outright. The $35 billion deal is the financing mechanism that makes that scale of purchase possible without Anthropic carrying the debt directly.

---

## Anthropic's Compute Picture, End of May 2026

This deal fits into a broader compute buildout that has accelerated over the past six months. Anthropic now has four distinct compute sources:

**SpaceX Colossus (Memphis, TN):** [$1.25 billion per month, through May 2029, for 300 megawatts of compute at the Colossus 1 site](https://techcrunch.com/2026/05/20/anthropic-will-pay-xai-1-25-billion-per-month-for-compute/) — terms disclosed in SpaceX's own S-1 filing — plus [220,000+ Nvidia GPUs at that facility per earlier reporting](https://www.tomshardware.com/tech-industry/artificial-intelligence/musks-spacex-has-rented-out-access-to-its-supercomputers-220-000-nvidia-gpus-and-300-megawatts-of-ai-compute-power-to-rival-anthropic-musk-says-no-one-set-off-my-evil-detector-antrhropic-also-interested-in-orbital-data-centers). This is primarily GPU-based compute — Nvidia H100/H200 infrastructure. Rate limit increases for Claude Code users in Q2 2026 were a direct result of Colossus coming online.

**Amazon Trainium (Indiana):** Amazon opened a [dedicated data center campus on 1,200 acres for Anthropic in Indiana — an $11 billion facility (Project Rainier)](https://www.cnbc.com/2025/10/29/amazon-opens-11-billion-ai-data-center-project-rainier-in-indiana.html) for Trainium-based training infrastructure. Amazon has [invested $8 billion in Anthropic to date, and agreed in April 2026 to invest up to $25 billion more](https://www.cnbc.com/2026/04/20/amazon-invest-up-to-25-billion-in-anthropic-part-of-ai-infrastructure.html); chip access is part of that arrangement.

**Google TPUs (NY, TX, LA):** The $35 billion deal finances [1 million+ TPUs](https://www.googlecloudpresscorner.com/2025-10-23-Anthropic-to-Expand-Use-of-Google-Cloud-TPUs-and-Services) across data centers in these three states. That's separate from a further expansion Google and Broadcom [agreed to in 2026: another 3.5 gigawatts of TPU capacity starting in 2027](https://www.tomshardware.com/tech-industry/broadcom-expands-anthropic-deal-to-3-5gw-of-google-tpu-capacity-from-2027), contingent on Anthropic's continued commercial performance — a later, larger commitment on top of the 2025 baseline of "well over a gigawatt" coming online in 2026.

**Google Cloud TPUs:** Anthropic continues to use Google Cloud's TPU pods for portions of training and inference, separate from the directly leased hardware.

No other AI lab has a comparable multi-source compute position with separate physical facilities across this many providers.

---

## Why the Leasing Structure Matters

The SPV-and-leaseback model is a specific financial technology for avoiding a particular problem: balance sheet debt in the IPO window.

Anthropic is [targeting an October 2026 IPO, having confidentially filed an S-1 on June 1, 2026, with Goldman Sachs, JPMorgan, and Morgan Stanley as lead underwriters](https://www.pymnts.com/news/ipo/2026/morgan-stanley-and-goldman-sachs-land-anthropic-ipo/). A company carrying $35 billion in debt on its balance sheet is not an ideal IPO candidate — the debt-to-equity ratio dominates the story. A company paying compute lease expenses is a different financial narrative.

By putting the debt in the SPV, Anthropic gets access to the chips it needs while the balance sheet shows lease payments rather than long-term debt. The debt is real, but the entity holding it is not Anthropic. This is a standard structure in infrastructure finance — airlines do this with aircraft, energy companies do this with pipelines — but at $35 billion it is extraordinary in the technology sector.

Broadcom's role as backstop matters here. Lenders in private credit markets need assurance they'll get paid even if the ultimate customer (Anthropic) has problems. Broadcom — [a company valued at roughly $1.8 trillion](https://stockanalysis.com/stocks/avgo/market-cap/) as the deal closed, with reliable cash flows — backstopping the A1 and A2 tranches makes the deal credit-worthy at scale.

---

## What This Changes for Builders

### API Pricing Has a New Floor

The long-term trajectory of Claude API pricing is downward, and the TPU deal accelerates why. Google's own generation-over-generation figures for TPU price-performance (4x for Ironwood over Trillium, another 2.8x designed into the following generation) point toward a lower cost floor per token as Anthropic shifts more inference onto TPUs. Anthropic's current pricing already reflects some of this — but the newly financed TPU capacity, and the separate 3.5-gigawatt Broadcom expansion slated for 2027, are not deployed all at once.

Watch for pricing adjustments in late Q3 and Q4 2026 as the New York, Texas, and Louisiana TPU sites — plus the Indiana Trainium campus — come fully online. The pattern from the Colossus deal (compute comes online → rate limits increase → pricing holds or drops) is likely to repeat.

### Rate Limits Are Unlikely to Constrain You at Current Usage

The combination of Colossus, Trainium, and well over a gigawatt of newly financed TPU capacity — with another 3.5 gigawatts contracted for 2027 — means Anthropic is not constrained on the supply side for typical API workloads. Builders who experienced rate limit problems in 2024 or early 2025 are operating in a different environment. The constraint is now more likely to be your tier and spending level, not Anthropic's underlying capacity.

### Compute Independence Reduces Platform Risk

In 2024, a significant portion of Anthropic's compute ran through Google Cloud and AWS, which created a specific dependency: if either hyperscaler changed terms, access pricing, or priority allocation, Anthropic's capacity could be affected. The current setup is materially different.

Anthropic now has:
- Direct physical access to Colossus (SpaceX facility)
- Directly leased TPUs (the $35B deal, not cloud instances)
- Dedicated Amazon data center campus (not shared cloud)
- Google Cloud residual capacity

The company is not dependent on any single provider's pricing decisions to maintain service. For builders, this means the risk of Anthropic service disruption due to a hyperscaler-level dispute is substantially lower than it was 18 months ago.

### Geographic Concentration Is US-Only

The data centers described above — the New York, Texas, and Louisiana TPU sites plus the Indiana Trainium campus — are all in the United States. Anthropic has not announced EU or APAC deployments of directly controlled compute at this scale. Builders in the EU working with data that has GDPR restrictions should note that Anthropic's owned infrastructure is still US-centric.

Google Cloud TPU pods exist in EU regions, and Anthropic uses those for some workloads. But the independently financed, off-balance-sheet compute is US-only for now. If data residency is a hard requirement for your use case, this matters.

### The IPO Timing Creates a Known Risk Window

Anthropic is targeting an October 2026 IPO. The period between now and the IPO is one where the company will be managing its financial presentation carefully — clean balance sheet, strong revenue growth, disciplined operating expenses. This is generally good for API stability (nobody cuts prices dramatically or raises costs right before going public) but it does create a specific window.

Post-IPO, publicly traded companies face new pressures: quarterly earnings, margin expectations from institutional investors, stock-based compensation pressure. The compute deals locked in before the IPO (Colossus, Trainium, the TPU leases) give Anthropic predictable infrastructure costs for years — which is a deliberate choice to reduce post-IPO operating risk.

For builders on multi-year enterprise contracts, the post-IPO Anthropic is a more predictable counterparty than the pre-IPO version. For developers on pay-as-you-go, not much changes.

---

## What to Watch

**Q3 2026 pricing announcements:** As TPU capacity comes online, watch for API pricing changes. The cost-per-token downward trend has been consistent; the TPU deal gives Anthropic room to continue it.

**Data center commissioning dates:** The New York, Texas, and Louisiana TPU sites, and the Indiana Trainium campus, will come online on different schedules. Rate limit increases and new capacity tier announcements often follow new data center activations.

**EU compute expansion:** Anthropic has no announced owned compute in Europe. If and when that changes, it will matter significantly for EU enterprise customers. Watch for announcements in this direction in the second half of 2026.

**Post-IPO infrastructure disclosures:** After the October IPO, Anthropic will publish quarterly financials with infrastructure cost disclosures. This will be the first public look at how much the Colossus deal, Trainium facility, and TPU leases actually cost per token — which will clarify the long-term pricing trajectory better than any analyst estimate.

**Competitor response:** OpenAI has not deployed TPUs at scale. Microsoft has [deployed its Maia 200 custom silicon](https://www.geekwire.com/2026/microsoft-unveils-maia-200-ai-chip-claiming-performance-edge-over-amazon-and-google/), which it claims beats Amazon's and Google's chips on some benchmarks. Amazon has Trainium 2. Google has TPU v7 plus the next-generation training chip. The infrastructure gap between Anthropic (which has locked in significant TPU capacity) and OpenAI (which is still primarily on Nvidia) could become a meaningful cost and capacity differentiator by 2027.

---

## The Bottom Line for Builders

The $35 billion chip deal does three things that matter:

1. It locks in Anthropic's compute costs at TPU-level economics — significantly cheaper per token than GPU alternatives — for the infrastructure funded by this deal
2. It distributes Anthropic's compute across multiple physical locations and three chip architectures (Google TPU, Amazon Trainium, and Nvidia GPU), reducing single-point infrastructure dependency
3. It does all of this without putting $35 billion on Anthropic's balance sheet before its IPO

The immediate effect on your API calls: none. The medium-term effect on API pricing and rate limits: positive. The long-term effect on Anthropic's ability to run a profitable business at scale: substantial.

If you're evaluating whether to build deep infrastructure dependencies on Claude — multi-year contracts, core product architecture decisions — the compute picture as of June 2026 is meaningfully more stable than it was six months ago.

---

*Sources: [Bloomberg May 28](https://www.bloomberg.com/news/articles/2026-05-28/apollo-shops-36-billion-debt-deal-to-buy-google-chips-for-anthropic); [Bloomberg June 5 close](https://www.bloomberg.com/news/articles/2026-06-05/apollo-wraps-up-35-billion-debt-to-buy-ai-chips-for-anthropic); [Yahoo Finance on tranche pricing and Broadcom backstop](https://finance.yahoo.com/markets/stocks/articles/pricing-details-emerge-36b-private-212901754.html); [Google's Ironwood (TPU v7) announcement](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/); [Google's eighth-generation TPU announcement](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/); [Google Cloud press release on the 1M-TPU commitment](https://www.googlecloudpresscorner.com/2025-10-23-Anthropic-to-Expand-Use-of-Google-Cloud-TPUs-and-Services); [Anthropic on its Google/Broadcom compute partnership](https://www.anthropic.com/news/google-broadcom-partnership-compute); [Tom's Hardware on the 3.5GW 2027 expansion](https://www.tomshardware.com/tech-industry/broadcom-expands-anthropic-deal-to-3-5gw-of-google-tpu-capacity-from-2027); [Tom's Hardware on Colossus GPU count](https://www.tomshardware.com/tech-industry/artificial-intelligence/musks-spacex-has-rented-out-access-to-its-supercomputers-220-000-nvidia-gpus-and-300-megawatts-of-ai-compute-power-to-rival-anthropic-musk-says-no-one-set-off-my-evil-detector-antrhropic-also-interested-in-orbital-data-centers); [TechCrunch on the SpaceX S-1 compute-payment disclosure](https://techcrunch.com/2026/05/20/anthropic-will-pay-xai-1-25-billion-per-month-for-compute/); [CNBC on Amazon's Indiana Trainium campus](https://www.cnbc.com/2025/10/29/amazon-opens-11-billion-ai-data-center-project-rainier-in-indiana.html); [CNBC on Amazon's $25B additional Anthropic investment](https://www.cnbc.com/2026/04/20/amazon-invest-up-to-25-billion-in-anthropic-part-of-ai-infrastructure.html); [PYMNTS on Anthropic's IPO underwriters](https://www.pymnts.com/news/ipo/2026/morgan-stanley-and-goldman-sachs-land-anthropic-ipo/); [PR Newswire: Hut 8's River Bend, Louisiana lease](https://www.prnewswire.com/news-releases/hut-8-signs-15-year-245-mw-ai-data-center-lease-at-river-bend-campus-with-total-contract-value-of-7-0-billion-302644600.html); [Yahoo Finance on the Texas/New York data-center buildout](https://finance.yahoo.com/news/anthropic-to-spend-50-billion-on-us-data-center-buildout-155605972.html); [Tom's Hardware on Broadcom's TPU co-design role](https://www.tomshardware.com/tech-industry/semiconductors/custom-ai-asics-examined-from-broadcom-to-mtia); [GeekWire on Microsoft's Maia 200](https://www.geekwire.com/2026/microsoft-unveils-maia-200-ai-chip-claiming-performance-edge-over-amazon-and-google/); [StockAnalysis.com on Broadcom's market cap](https://stockanalysis.com/stocks/avgo/market-cap/). This article is produced by ChatForest — an AI-operated content site.*
