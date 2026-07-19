---
title: "Inkling: Thinking Machines' 975B Open-Weight MoE — Self-Host, API Pricing, and Fine-Tuning with Tinker"
date: 2026-07-17
description: "On July 15, 2026, Mira Murati's Thinking Machines Lab released Inkling — a 975B-parameter Mixture-of-Experts model under Apache 2.0, with native text/image/audio reasoning and a 1M-token context window. It is not the best model available. That's the whole point. Here's the architecture, benchmark numbers, access paths, and the builder case for fine-tuning it with Tinker."
tags: ["open-source", "fine-tuning", "moe", "thinking-machines", "mira-murati", "inkling", "tinker", "open-weight", "llm", "multimodal", "enterprise-ai"]
---

On July 15, 2026, [Thinking Machines Lab](https://thinkingmachines.ai/news/introducing-inkling/) — the AI startup founded by ex-OpenAI CTO Mira Murati and safety researcher John Schulman — released [Inkling](https://thinkingmachines.ai/inkling/), its first open-weight model. Full weights landed on [Hugging Face](https://huggingface.co/thinkingmachines/Inkling) under Apache 2.0, alongside same-day fine-tuning access on Tinker.

This is a research-based guide. We reviewed [Thinking Machines' official model card](https://thinkingmachines.ai/model-card/inkling/), primary coverage from [TechCrunch](https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/), [Axios](https://www.axios.com/2026/07/15/mira-murati-thinking-machines-open-weight-model-inkling), [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-15/murati-s-thinking-machines-releases-first-ai-model-for-broad-use), [TechTimes](https://www.techtimes.com/articles/320717/20260716/inkling-ships-muratis-lab-puts-largest-us-open-weight-ai-hugging-face.htm), [The Next Web](https://thenextweb.com/news/thinking-machines-inkling-open-weight-model), [HPCwire](https://www.hpcwire.com/aiwire/2026/07/16/thinking-machines-launches-open-weight-inkling-foundation-model-for-fine-tuning/), [Simon Willison's notes](https://simonwillison.net/2026/Jul/16/inkling/), and the [OpenRouter model page](https://openrouter.ai/thinkingmachines/inkling). We did not fine-tune or run the model ourselves.

---

## What Inkling is (and what it explicitly is not)

Thinking Machines published an unusual positioning statement alongside the release: Inkling is [not the strongest model available today, open or closed](https://thenextweb.com/news/thinking-machines-inkling-open-weight-model). The company frames that not as a disclaimer but as the design intent. Inkling is a starting point — a large, permissively licensed, multimodal base model meant to be narrowed and sharpened for specific workloads through Tinker, the company's fine-tuning platform.

The comparison class is Kimi K2.7 and NVIDIA Nemotron — Chinese and NVIDIA open-weight entries that compete for enterprise fine-tuning workloads. [TechStrong AI](https://techstrong.ai/articles/thinking-machines-launches-inkling-to-challenge-chinese-open-source-dominance/) framed Inkling specifically as a US challenge to Chinese open-source dominance in the customizable model tier.

---

## Architecture

According to the [official model card](https://thinkingmachines.ai/model-card/inkling/), Inkling is a 66-layer decoder-only transformer with sparse Mixture-of-Experts feed-forward layers. Each token is routed to 6 of 256 experts plus 2 shared experts. Total parameters: 975 billion. Active parameters per forward pass: approximately 41 billion — a 4.2% activation ratio, which keeps inference costs roughly in line with a 41B dense model despite the massive knowledge base encoded in the full weight set.

Training data: 45 trillion tokens spanning text, images, and audio. Thinking Machines describes the model as reasoning natively across all three modalities without adapter layers or modality-specific heads.

Context window: 1 million tokens.

---

## Benchmark numbers

From Thinking Machines' own release materials, [corroborated by HPCwire](https://www.hpcwire.com/aiwire/2026/07/16/thinking-machines-launches-open-weight-inkling-foundation-model-for-fine-tuning/):

| Benchmark | Score |
|---|---|
| HLE (text-only) | 29.7% |
| HLE (with tools) | 46.0% |
| AIME 2026 | 97.1% |
| GPQA Diamond | 87.2% |

The HLE scores put it behind the current frontier (Fable 5 and GPT-5.6 Sol score well above 50% with tools), which is consistent with Thinking Machines' self-assessment. The math benchmarks are strong: AIME 2026 at 97.1% is competitive with any model available today.

---

## VRAM requirements for self-hosting

Full weights are on [Hugging Face](https://huggingface.co/thinkingmachines/Inkling) in two checkpoints:

- **BF16 checkpoint:** Minimum 2 TB aggregate VRAM (approximately 16× H100 80GB or equivalent)
- **NVFP4 checkpoint:** Minimum 600 GB aggregate VRAM (approximately 8× H100 80GB), optimized for NVIDIA Blackwell systems

Self-hosting frameworks supported: [SGLang](https://github.com/sgl-project/sglang), vLLM, Llama.cpp, TokenSpeed, and Hugging Face Transformers. The Apache 2.0 license allows commercial use and derivative works without royalty obligations.

For most builders, 600 GB of VRAM is not a practical starting point. The managed inference and fine-tuning paths below are the realistic entry points.

---

## Managed inference: access without owning a cluster

Inkling is available through several third-party inference providers as of launch day, according to [SiliconANGLE](https://siliconangle.com/2026/07/15/mira-muratis-thinking-machines-drops-inkling-open-weights-model-anyone-can-access/) and the [OpenRouter listing](https://openrouter.ai/thinkingmachines/inkling):

- **TogetherAI**
- **Fireworks AI**
- **Modal**
- **Databricks**
- **Baseten**

Pricing varies by provider. On Thinking Machines' own [Tinker platform](https://tinker-docs.thinkingmachines.ai/tinker/models/), Inkling is priced at:

- **Input:** $1.87 per 1M tokens (64K context tier)
- **Output:** $4.68 per 1M tokens
- **Cached input:** $0.374 per 1M tokens
- **256K context tier:** approximately double the above rates

Thinking Machines is offering a 50% discount on Tinker pricing at launch. The revenue model is fine-tuning, not inference — Inkling at list price may not be the most competitive inference option compared to similarly-sized models, but the discount makes it accessible for experimentation.

---

## Fine-tuning with Tinker: the Bridgewater case study

The commercial rationale for Inkling is Tinker, the fine-tuning platform Thinking Machines launched in October 2025. Inkling gives Tinker customers a frontier-adjacent, permissively licensed base model to customize.

Thinking Machines disclosed one customer example at launch. Working with [Bridgewater Associates](https://www.axios.com/2026/07/15/mira-murati-thinking-machines-open-weight-model-inkling), Tinker was used to fine-tune a model on specialized financial data. The resulting system scored 84.7% on leading financial reasoning benchmarks — beating the most advanced proprietary alternatives at under 10% of the cost, per Thinking Machines' figures.

The Bridgewater case establishes the builder template:
1. Start with Inkling as the base (Apache 2.0, no royalties, weights you can inspect)
2. Fine-tune on your domain data via Tinker
3. The fine-tuned checkpoint becomes proprietary to you — Thinking Machines does not retain rights to derivative models under Apache 2.0

---

## What builders should evaluate

**Why Inkling over a proprietary API:**
- Fine-tuned weights are yours — no vendor lock-in, no per-token royalty on the derivative model
- Apache 2.0 is the most permissive major open license for commercial use
- 1M context window is competitive with any frontier model at launch
- Native multimodal (text + image + audio) without adapter layers

**Why Inkling might not be the right choice:**
- Raw benchmark performance is below Fable 5, GPT-5.6 Sol, and Gemini 3.5 Pro for general tasks
- 600 GB VRAM minimum for self-hosting puts it out of reach for most teams without a cluster partnership
- Tinker fine-tuning is Thinking Machines' proprietary platform — you'd be trading one vendor lock-in for another unless you self-host the fine-tuning process on the open weights

**When to consider Inkling:**
- You have a narrow, well-defined domain (financial analysis, legal review, scientific literature) where a fine-tuned 41B-active model can outperform a general frontier model at lower cost
- Your legal or compliance team requires full weight transparency and the ability to audit the model on-premises
- You want to build a product on customized weights you own, not on an API you rent

---

## Company context

Thinking Machines Lab is valued at [$12 billion](https://fortune.com/2026/07/15/what-is-mira-murati-thinking-machines-first-ai-model-inkling/), with revenue currently driven by Tinker. The existing Thinking Machines article on chatforest.com covers [the company's founding philosophy](https://chatforest.com/builders-log/thinking-machines-lab-future-worth-building-human-decentralized-alignment-customizable-weights-builder-guide/) — the core argument that centralized alignment concentrates power and that builders should own weights rather than rent API access. Inkling is the first product that operationalizes that argument.

---

## The short version

Inkling is a 975B MoE, 41B active, Apache 2.0, multimodal, 1M context, weights-on-Hugging-Face. It is not the strongest model available. It is designed to be fine-tuned into something narrow, purpose-built, and proprietary to you. Access it via Tinker at $1.87/$4.68 per MTok (50% launch discount), or via TogetherAI, Fireworks, Modal, Databricks, or Baseten. Self-hosting requires 600 GB VRAM minimum (NVFP4 checkpoint) or 2 TB (BF16). The Bridgewater financial fine-tune hit 84.7% on domain benchmarks at under 10% of proprietary model cost. If you need a domain-specific model you own outright, this is the most serious US open-weight option available today.
