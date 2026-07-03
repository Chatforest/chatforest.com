---
title: "Together AI's $800M Series C: What the Open-Model Neocloud's Funding Means for Builders"
date: 2026-07-04
description: "Together AI closed an $800M Series C at $8.3B valuation on July 1, with Aramco leading and NVIDIA participating. Annual bookings hit $1.15B. Here's what the funding signals and how it should shape your inference stack decisions."
og_description: "Together AI raised $800M at $8.3B valuation on July 1, 2026 — with 500 MW in compute commitments and plans to grow capacity 50x. Here's what it means for builders running open-model inference."
content_type: "Builder's Log"
categories: ["Infrastructure", "Funding", "Open Source"]
tags: ["together-ai", "open-models", "inference", "neocloud", "series-c", "aramco", "nvidia", "deepseek", "llama", "kimi", "july-2026", "ai-infrastructure", "gpu-cloud"]
---

Together AI raised an $800 million Series C on July 1, 2026, valuing the company at $8.3 billion. Aramco Ventures led the round; NVIDIA, Vista Equity Partners, General Catalyst, Emergence Capital, Pegatron, and others participated. The company disclosed that annual bookings surpassed $1.15 billion in Q2 2026 — roughly 3.6× the revenue run-rate typically associated with their $3.3B Series B valuation from 16 months prior.

This round matters to builders beyond the headline number. Together AI is, in practice, the largest dedicated inference platform for open-weight models — Llama, DeepSeek, Qwen, Kimi, Nemotron. If you route traffic through open models at meaningful scale, you are likely already using it or have it on your shortlist. Understanding what this funding enables and what it signals about the market helps you plan your infrastructure bets.

## What Together AI Actually Is

Together AI is not a model lab. It does not train frontier models. It is an inference provider — its product is letting you call open-weight models via API at production latency, without managing GPU clusters yourself.

Three core products:

- **Serverless Inference**: Pay per token across a wide catalog of open models ($0.05–$9.00 per million tokens depending on model). No commitment. Scales to zero.
- **Dedicated Inference**: Single-tenant GPU instances by the hour ($6.49/hr for H100 SXM). Predictable latency, no cold starts, suitable for production SLAs.
- **Batch Inference API**: 50% discount for workloads that don't need sub-second response. Ideal for synthetic data generation, offline evaluation, document processing pipelines.

The company also sells GPU Clusters for training and fine-tuning at $3.99–$5.49/hr per H100 depending on commitment length.

Underlying everything is ATLAS, Together's proprietary inference engine. It uses speculative decoding and other optimization techniques to push throughput — the company now claims #1 output speed among GPU-based providers for DeepSeek-R1, DeepSeek-V3.1, Kimi-K2, Qwen-3-Coder-480B, and GPT-OSS-120B. In internal benchmarks, ATLAS delivers up to 400% acceleration over baseline serving on select models, and up to 2× faster serverless inference versus the prior generation of their stack.

## The Funding Math

**Series B (February 2025):** $305M at $3.3B valuation.

**Series C (July 1, 2026):** $800M at $8.3B valuation.

The valuation grew 2.5× in 16 months — faster than the broader AI infrastructure market compression seen in the same period. The catalyst is bookings. A $1.15B annualized bookings rate at Q2 close means the business is real, not speculative. Aramco Ventures — the investment arm of Saudi Aramco — led the round. This is a strategic bet from a sovereign-adjacent capital pool with both the capacity and the incentive to back long-duration infrastructure plays.

NVIDIA's continued participation matters for a different reason: it confirms that NVIDIA sees open-model inference providers as distribution for its GPU supply, not competitors. The relationship is complementary — Together runs on H100s and H200s, and NVIDIA benefits from every token processed.

## Use of Funds: 50× Capacity

The company disclosed commitments for more than 500 megawatts of compute as part of the fundraise. That maps to a plan to grow capacity roughly 50 times over five years.

To put 500 MW in context: a hyperscale data center is typically 50–200 MW. Together AI is committing to the equivalent of multiple hyperscale builds, dedicated to open-model inference. The capital structure from this round likely supports long-term power purchase agreements and hardware procurement at a scale that drives their per-GPU cost down, which gets passed to builders through lower token pricing.

For builders, 50× capacity growth has a specific implication: rate limits and queue times — the two biggest operational friction points on serverless inference — should decrease materially over the next 18 months. If you've been batching requests because Together's rate limits forced it, that changes.

## Why Aramco Leading Is Significant

Saudi Aramco does not typically lead AI infrastructure rounds. This is not a general tech investment — it is a resource diversification play by the world's largest oil company.

The bet: AI compute demand will grow for at least a decade. Data centers consume enormous amounts of power. A sovereign energy producer that backs the infrastructure consuming that power captures a non-correlated revenue stream as fossil fuel demand becomes less predictable. Aramco is also heavily involved in building data center capacity in the Gulf region; Together AI's international capacity commitments likely have geographic components that map to this.

For builders, the Aramco angle is mostly irrelevant to day-to-day API calls — the company still bills in USD, the API still serves the same models, and the infrastructure stack doesn't change. What it does signal: Together AI now has access to capital on a scale that lets it negotiate power and hardware contracts that were previously only available to hyperscalers. That improves their unit economics, which should eventually improve pricing.

## The Builder Decision: When Together AI, When Not

Together AI makes sense when one or more of the following is true:

**You're running an open model and want managed inference.** Running DeepSeek-R1, Llama 4, Kimi K2, or Qwen-3 yourself on provisioned GPUs has real operational overhead. Together's Serverless Inference removes that. If your throughput isn't high enough to amortize the ops cost of self-hosting, the API is the correct choice.

**You need cost leverage over closed APIs.** Together AI's published rates are 6–60× cheaper than equivalent closed-model pricing for comparable quality on certain tasks. This range is wide because "equivalent quality" varies by task. Coding, summarization, and structured extraction tend to have the smallest quality gap. Nuanced reasoning, long-context tasks, and anything requiring the latest training data tend to have a larger gap. Run evaluations against your actual tasks.

**You need batch processing at scale.** The 50%-off Batch Inference API is underused by builders. If you're running offline pipelines — synthetic data generation, nightly document processing, evaluation suites — there's no reason to pay real-time pricing.

Together AI is not the right call when:

**You need the latest closed-model capabilities.** Together's catalog does not include Claude, GPT-5, or Gemini. If your use case benefits from these models' specific strengths (instruction-following quality, tool-use reliability, safety guarantees, or the latest training cutoff), you need the first-party APIs.

**You need SLA guarantees you can enforce contractually.** Together AI has an enterprise tier, but it is not AWS, Azure, or GCP. For production workloads where downtime has direct financial consequences and you need SLAs with credit-backed compensation, the hyperscaler model APIs offer more formal guarantees.

**You need a dedicated GPU instance with predictable latency but no ops overhead.** The Dedicated Inference product gets you most of the way there, but it's more expensive than serverless for low-throughput workloads and requires more configuration than calling an API endpoint.

## What the 50× Build Signals About the Market

Three months ago, the open-model inference market was tight. Rate limits were frequent, queue latencies spiked during peak hours, and builders with production workloads often had to maintain secondary provider fallbacks. Together AI was not the only neocloud in this position — Fireworks AI, Groq, Lepton, and others were similarly constrained.

The $800M round — combined with Crusoe's $3B raise (also announced this week at $30B valuation) and CoreWeave's earlier IPO — signals that infrastructure capital has concluded the AI inference demand curve is real and durable. These are not speculative bets. They are capacity commitments.

The practical effect for builders: the open-model inference market is about to have significantly more supply. More supply means lower prices, better availability, and more provider competition. If you locked in prices with a provider a year ago, they should renegotiate when your contract comes up. If you've been on a waitlist for dedicated instances, the list will clear faster.

The risk: this is the same dynamic that played out in cloud compute in 2012–2016. A lot of capital built a lot of capacity. Prices fell dramatically. Several neocloud providers that couldn't get to sufficient scale went out of business or got acquired. Together AI is in a strong position with $1.15B in bookings and fresh capital, but the field will consolidate.

## What to Watch

- **Pricing updates**: Together typically revises its model catalog pricing after major funding events. Watch their pricing page over the next 30 days for any changes to the serverless per-token rates.
- **New model additions**: More capital means more GPU capacity means more models they can afford to serve at inference scale. Expect additions from the Qwen 3 family and possibly Mistral Large 3 if they haven't already added it.
- **ATLAS public details**: The company has been tightening the engine. A technical blog post or academic paper about ATLAS internals would signal the maturity of their proprietary moat.
- **Enterprise contracts**: With Aramco Ventures' network, expect announcements about enterprise customers in the Gulf region and potentially a European infrastructure expansion tied to the capital.

---

*Together AI's $800M round closed July 1, 2026. Crusoe closed its $3B raise approximately the same week. Both are available for AI infrastructure use.*
