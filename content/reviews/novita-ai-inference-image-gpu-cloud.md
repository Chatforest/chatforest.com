---
title: "Novita AI — 120+ LLMs, 10,000+ Image Models, Bootstrapped to $1.1M ARR (2026 Review)"
date: 2026-05-08T11:00:00+09:00
description: "Novita AI reviewed: bootstrapped inference platform with 120+ LLMs, 10,000+ image models, Hugging Face official partner, Agent Sandbox, and price leadership. Rating: 4/5."
og_description: "Novita AI (novita.ai): a developer-first serverless inference API and GPU cloud founded in late 2023 in San Francisco. Bootstrapped to $1.1M ARR with ~10 people. Offers 120+ LLMs (OpenAI-compatible endpoint), 10,000+ image generation models — the largest open-source image model catalog via API — plus GPU cloud instances and a Firecracker-based Agent Sandbox. DeepSeek V4 Pro: 1M context at $1.74/$3.48 per million tokens (vs. DeepInfra's 66k context at same price). GPQA Diamond #1 among all inference providers (79.0%). Official Hugging Face Inference Provider (April 2026). Agent Sandbox launched April 28, 2026 with sub-200ms startup. Partners: vLLM, SGLang. Customers: Quora, Fish Audio, beBee, Vercel top-10 AI provider. Rating: 4/5."
card_description: "Novita AI (novita.ai) is a bootstrapped developer-first inference platform offering 120+ LLMs and 10,000+ open-source image models via a single OpenAI-compatible API. Founded in late 2023 in San Francisco, the team of ~10 people reached $1.1M ARR without external venture funding. **Price leader on LLMs**: cheapest or near-cheapest on 70%+ of models compared to Fireworks AI; DeepSeek V4 Pro at $1.74/$3.48 per million tokens with **1M token context window** (vs. DeepInfra's 66k). **GPQA Diamond #1** accuracy across all inference providers (April 2026, Artificial Analysis). **10,000+ image models** including SDXL, FLUX, LoRAs, ControlNet variants — by far the largest open-source image model catalog available via API. **Agent Sandbox** launched April 28, 2026 — Firecracker microVMs with sub-200ms startup for secure autonomous agent execution. Official Hugging Face Inference Provider (April 2026). Partners: vLLM, SGLang. Customers include Quora, Fish Audio, beBee, Genspark, Kilo Code, Vercel. Weakness: slower throughput on large MoEs (33.5 t/s vs. Fireworks's 174 t/s on DeepSeek V4 Pro); no managed fine-tuning pipeline; ~10-person team creates execution risk. Part of our **AI/ML Tools** and **Developer Tools** categories. Rating: 4/5."
last_refreshed: 2026-05-08
categories: ["/categories/ai-ml-tools/", "/categories/developer-tools/"]
---

The inference API space is crowded with well-funded companies. Together AI raised $228 million. Fireworks AI closed a $52 million Series B. DeepInfra just landed a $107 million Series B last week, with NVIDIA as a strategic investor.

Novita AI has raised zero dollars.

That is not a gap in the pitch deck. It is a deliberate choice by a ten-person team in San Francisco that reached $1.1 million in annual recurring revenue without taking venture capital, in a space where the conventional wisdom holds that GPU infrastructure is impossible without nine-figure funding.

Worth understanding why — and what the trade-offs look like.

Part of our **[AI/ML Tools category](/categories/ai-ml-tools/)** and **[Developer Tools category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Service** | [Novita AI](https://novita.ai/) |
| **Founded** | Late 2023, San Francisco, CA |
| **Key founders** | Junyu Huang (COO, ex-Scale AI, ex-Toma) |
| **Team size** | ~10 people |
| **External funding** | $0 (bootstrapped) |
| **Revenue** | $1.1M ARR (Latka, 2025) |
| **LLM catalog** | 120+ models |
| **Image model catalog** | 10,000+ models |
| **API compatibility** | OpenAI-compatible |
| **Cheapest LLM** | $0.02/1M input (Llama 3.1 8B) |
| **DeepSeek V4 Pro** | $1.74/$3.48 per million tokens, 1M context |
| **GPU fleet** | RTX 3090 → H200, 16+ global data centers |
| **GPU spot pricing** | H100 ~$1.30–1.55/hr (on-demand $2.59/hr) |
| **Hugging Face** | Official Inference Provider (April 2026) |
| **Accuracy** | GPQA Diamond #1 among inference providers (79.0%) |
| **Agent Sandbox** | Launched April 28, 2026 — Firecracker microVMs |
| **Partners** | vLLM, SGLang, OpenRouter |

---

## The Case for Bootstrapping in a Capital-Intensive Space

The conventional analysis of GPU inference economics goes like this: margins are thin, GPU procurement requires capital, demand is spiky, and you need scale to win on pricing. Venture capital is not optional — it is the mechanism that buys you GPUs, buys you engineering talent, and lets you underprice until you have enough volume to make unit economics work.

Novita's existence challenges this framing.

The company's COO, Junyu Huang, came from Scale AI and Toma, not from an AI lab or a cloud infrastructure giant. The founding team had production AI systems experience and a clear thesis: the open-source model ecosystem needed a price-competitive, model-diverse inference platform that didn't treat image generation as an afterthought. They built to their strengths rather than trying to mirror the capital structure of better-funded competitors.

The result is a company that looks fragile on a funding slide but surprisingly robust in practice. At $1.1M ARR with ten employees, the revenue-per-employee ratio is strong. The platform has survived long enough to become an official Hugging Face inference partner — a designation that exposes Novita to millions of developers who discover models on Hugging Face and want to deploy them immediately.

Bootstrapping also creates structural discipline. Every model you add has to be worth running. Every feature has to pull its weight. There is no Series B war chest to burn through while chasing market share. That discipline shows up in pricing — Novita is cheaper than Fireworks on 40 out of 55 shared models — and in the product focus on highest-leverage differentiators.

---

## The LLM Inference API: Price Leader With Full Context Windows

Novita's LLM offering is built on a single OpenAI-compatible endpoint:

```
https://api.novita.ai/v3/openai
```

The interface supports everything you would expect from a modern inference API: streaming, tool calling, structured JSON output, prompt caching, log probabilities, vision/multimodal inputs, and reasoning model support. Switching an existing OpenAI SDK integration to Novita requires changing one URL and one API key.

### What's Unusual About the Pricing

The headline number is $1.74/$3.48 per million input/output tokens for DeepSeek V4 Pro. That is identical to several competitors. The difference is context: **Novita offers 1 million tokens of context** on DeepSeek V4 Pro. DeepInfra — reviewed last run — caps DeepSeek V4 Pro at 66,000 tokens at the same price point. That is a significant gap for any workload involving long documents, large codebases, or extended agentic conversations.

The broader pattern holds. Novita prices below Fireworks AI on the majority of shared models:

| Model | Novita (input/output) | Fireworks AI (input/output) |
|---|---|---|
| DeepSeek V3 | $0.40 / $1.30 | $0.56 / $1.68 |
| Llama 3.3 70B | $0.51 / $0.74 | $0.90 / $0.90 |
| Qwen2.5 72B | $0.38 / $0.40 | $0.90 / $0.90 |
| Llama 3.1 8B | $0.02 / $0.05 | varies |
| DeepSeek V4 Pro | $1.74 / $3.48 | comparable |

Novita is cheaper on approximately 73% of models where prices can be directly compared. For high-volume workloads where speed is secondary to cost, this is a meaningful operational advantage.

**Batch inference** adds another layer: 50% discount on input and output tokens for asynchronous workloads. For offline document processing, classification pipelines, or any task where you can tolerate latency, this brings effective token costs to half the already-low headline rates.

### The Model Catalog

120+ LLMs across the major open-source families:

- **DeepSeek family**: V3, V3.1, V3.2, V4 Flash, V4 Pro, DeepSeek-OCR (a specialized document processing model achieving 307 tokens/second on Novita)
- **Qwen family**: Qwen2.5 7B through 72B, Qwen3 4B through 235B, Qwen3 Coder, Qwen3 Max, Qwen3 VL
- **Meta Llama**: 3.1 8B, 3.3 70B, Llama 4 Scout, Llama 4 Maverick
- **Reasoning models**: 43 reasoning-focused variants
- **Kimi K2.5, K2.6** (MoE), **MiniMax M2.5**, **GLM-5/5.1**, **Phi**, **Mistral**, **Gemma**
- **OpenAI open-weight**: gpt-oss-20B, gpt-oss-120B

Novita has cultivated a reputation for "Day 0" availability — listing new open-source models on launch day. The platform was a Day 0 partner for Google's Gemma 4 model on Hugging Face.

### Accuracy: GPQA Diamond #1

Speed and price are obvious competitive metrics. Accuracy is harder to measure and easier to ignore. Artificial Analysis's April 2026 evaluation placed Novita at the top of all inference providers on GPQA Diamond — a benchmark testing graduate-level scientific reasoning — at 79.0% (16 runs). On AIME 2025 (advanced mathematics), Novita scored 93.3% across 32 runs, matching top providers.

For developers building research assistants, scientific tools, or any application where factual precision matters, this is worth knowing. You are not sacrificing accuracy to get lower prices.

---

## Speed: Mixed Results Depending on Model

Novita is not the fastest inference provider. On the models where speed matters most, there are real trade-offs.

### DeepSeek V4 Pro

Artificial Analysis benchmarks:
- **Novita**: 33.5 tokens/second
- **Fireworks AI**: 174.0 tokens/second

That is a 5.2x difference. For interactive applications — chatbots, coding assistants, real-time agents — Fireworks is dramatically faster on this particular model. Novita's price advantage and context window advantage do not compensate for a 5x throughput gap in latency-sensitive use cases.

### Where Novita Is Competitive

The picture is better on other models:

- **DeepSeek V4 Flash**: 89.4 t/s on Novita — fastest available on this model
- **DeepSeek V3.2 Experimental (reasoning)**: 38.6 t/s, 0.81s TTFT — lowest TTFT of all providers
- **DeepSeek OCR**: 307.6 t/s
- **Ling 2.6 Flash**: 206 t/s
- **Qwen3 Next 80B A3B**: 202 t/s
- **Llama 4 Maverick** TTFT: 0.38s (33% faster than DeepInfra's 0.57s)

The pattern: Novita performs well on smaller models, specialized models, and models where it has been specifically optimized. On the largest MoE flagship models — the ones developers most want for complex tasks — Fireworks and Groq retain significant speed advantages.

For batch workloads where throughput matters more than TTFT, and for interactive workloads on mid-sized models, Novita is fully competitive.

---

## The Image Generation API: 10,000 Models and Why It Matters

This is where Novita genuinely has no peer.

The LLM inference space has multiple well-funded competitors offering broadly similar catalogs at broadly similar prices. The image generation API space has Novita on one end — with 10,000+ models — and everyone else a significant distance behind.

The catalog is built on the open-source image model ecosystem that grew up around Civitai, the community hub for Stable Diffusion fine-tunes, LoRA adapters, and custom checkpoints. There are millions of users who have trained custom image models on specific art styles, characters, product categories, or aesthetic niches. Previously, deploying those models required running your own infrastructure. Novita productized the Civitai ecosystem into a single API.

### What's Available

**Foundation models**: Stable Diffusion XL, SD 1.5, and all the major custom fine-tunes
**State-of-the-art**: FLUX.1 Kontext Dev ($0.0225/image), Hunyuan Image 3 ($0.10/image), Seedream 4.5 (ByteDance)
**Specialist tools**: Background removal ($0.017/image), face restoration, upscaling, inpainting, image-to-image, ControlNet variants

**Video** (adjacent product): Kling V1.6 ($0.27/5s 720P), Kling 2.6 (with audio sync), Vidu Q3 Pro, Seedance 1.5 Pro, Wan 2.1

**TTS**: Fish Audio ($15/1M characters), MiniMax speech-02-hd ($80/1M characters)

### Why Image Generation Matters for Novita's Business

The 10,000-model catalog is not just a product feature. It is a distribution strategy. Developers building image-heavy applications — product photo tools, avatar generators, style transfer apps, visual content pipelines — need specific models that larger inference providers don't carry. When they search for "Stable Diffusion SDXL API" or "LoRA inference endpoint," Novita shows up. That catalog breadth drives inbound traffic and customer acquisition that pure LLM inference providers cannot replicate.

Fish Audio, a notable customer, uses Novita for GPU infrastructure to run its own text-to-speech models. beBee, a professional networking platform, reports that Novita powers over 90% of their token usage. These are customers who came for specific capabilities and stayed because the economics worked.

---

## The GPU Cloud: RTX 3090 to H200, 16 Global Data Centers

Beyond serverless inference, Novita operates a GPU cloud for users who need raw compute access — training runs, custom inference setups, or long-running workloads that don't fit the serverless model.

**Available hardware**: RTX 3090, L40S, RTX 5090, A100 80GB, H100 80GB, H200

**On-demand pricing** (selected):
- RTX 3090: $0.21/hr
- L40S: $0.55/hr
- RTX 5090: $0.72/hr
- A100 80GB: $1.60/hr
- H100 80GB: $2.59/hr

**Spot pricing**: ~40–60% cheaper than on-demand. H100 spot: roughly $1.30–1.55/hr.

**Geographic reach**: 16+ data centers across Australia, Brazil, Germany, Hong Kong, Iceland, India, Japan, Singapore, South Africa, UAE, UK, and multiple U.S. locations. This is notably broader geographic coverage than DeepInfra, which remains U.S.-only.

Instances launch pre-configured with CUDA drivers and common ML frameworks. JupyterLab included. Deployment in under two minutes is the advertised target.

The fine-tuning story here is raw-compute rather than managed pipeline: provision H100 instances, run your training code, export the model. Contrast with Together AI and Fireworks, which offer managed fine-tuning APIs. Novita's approach is more flexible (supports any training framework) but requires more operational setup from the user.

---

## The Agent Sandbox: Moving Up the Stack

On April 28, 2026 — just ten days before this review — Novita launched its Agent Sandbox, a managed execution environment for autonomous AI agents.

The architecture is notable: Firecracker microVMs, the same isolation technology used in AWS Lambda. Each agent task gets its own isolated kernel, memory, and ephemeral filesystem. Cross-agent contamination and credential leakage — real problems in multi-agent systems where a compromised sub-agent can access the parent environment — are addressed at the infrastructure level rather than through application-layer policies.

Key specifications:
- **Sub-200ms startup** — fast enough for interactive agent chains
- **Stateful execution** — ~1-second pause/resume for checkpointing long-running agents
- **Parallel scale** — designed for thousands of concurrent microVMs
- **Compatible runtimes**: OpenClaw, Hermes Agent, E2B
- **Billing**: Per-second for CPU and RAM

The E2B compatibility is strategically important. E2B is a widely-used agent sandbox with established integrations across many agent frameworks. By offering E2B-compatible APIs, Novita can serve as a drop-in replacement for teams already building on that ecosystem.

This launch signals Novita's ambition beyond pure inference. An inference API is a commodity; an execution platform for autonomous agents is a higher-margin, stickier product. Whether a ten-person bootstrapped team can execute on that ambition against well-funded competitors (including E2B itself) is an open question.

---

## The Hugging Face Partnership

On April 14, 2026, Novita became an official Hugging Face Inference Partner — the same designation that DeepInfra received in the same month.

The mechanics: on any supported model's Hugging Face page, a "Deploy on Novita" button appears alongside similar options for other partner providers. The five million-plus monthly visitors to Hugging Face — researchers, developers, and students exploring open-source models — see Novita as a first-class deployment option.

This is a significant distribution advantage for a bootstrapped company without a marketing budget. The Hugging Face partnership effectively gives Novita reach it could not buy with paid acquisition at any reasonable cost structure.

The partnership also establishes a quality signal. Hugging Face does not add infrastructure partners casually. The vLLM partnership (April 2025) and SGLang partnership (May 2025) — both marquee open-source inference engine projects — preceded the Hugging Face designation and helped establish Novita's credibility in the open-source ecosystem before the partnership was announced.

---

## Ecosystem and Customers

**OpenRouter integration**: Novita is available as a backend provider on OpenRouter, meaning developers who use OpenRouter's unified API for model routing can route to Novita without direct integration.

**Vercel**: Novita is ranked in Vercel's top 10 AI providers on Vercel's AI Gateway — meaningful given Vercel's developer reach.

**Confirmed customers**:
- **Quora** — for LLM inference
- **Fish Audio** — GPU infrastructure for TTS model serving
- **beBee** — "powers over 90% of our token usage"
- **Genspark** — AI-native search
- **Kilo Code** — AI coding assistant
- **Gizmo AI**, **Wiz.ai**, **Hygo**, **TiDB**, **Monica**

The customer list spans LLM inference, image generation, GPU compute, and TTS — reflecting the breadth of Novita's product surface relative to its team size.

---

## Weaknesses

### Throughput on Large MoEs

The most concrete limitation: on flagship reasoning models like DeepSeek V4 Pro, Novita runs at 33.5 tokens/second versus Fireworks's 174 t/s. This is a 5x difference that matters for any interactive application at scale. For real-time coding assistants, customer-facing chatbots, or high-concurrency agentic systems where output latency is a product quality metric, Fireworks is the better choice on these specific models.

### No Managed Fine-Tuning Pipeline

Together AI and Fireworks both offer fine-tuning APIs where you submit a training dataset and get back a deployable model. Novita's path to fine-tuning is manual: provision GPU instances, run your own training code, manage your own model artifacts. This is fine for experienced ML engineers and more friction for teams that want a turnkey solution.

### SOC 2 Not Yet Confirmed

For enterprise buyers with compliance requirements, the absence of confirmed SOC 2 certification is a potential blocker. DeepInfra holds both SOC 2 and ISO 27001. Novita has not publicly confirmed equivalent certifications as of this review.

### Small Team Execution Risk

Ten people running an inference API, a 10,000-model image platform, a GPU cloud, and an agent sandbox is an ambitious surface area. The upside is a lean organization with low overhead. The downside is that any significant disruption — a key employee departure, an unexpected infrastructure incident, a major customer churn event — hits a company with limited redundancy. Enterprise customers conducting vendor due diligence should account for this.

### No Fixed Subscription Tiers

Purely usage-based pricing is developer-friendly but creates budget predictability challenges for enterprise procurement. Some teams need a monthly cap or committed spend tier with SLA guarantees. Novita does offer custom enterprise agreements, but the standard product is entirely pay-as-you-go.

### Free Tier Ambiguity

Novita advertises a "free tier" that turns out to be signup credits rather than a permanent ongoing allowance. Users who discover this after relying on it for development work have noted frustration in reviews. The credits are sufficient for evaluation, but the boundary between "free" and "paid" could be clearer in the product onboarding.

---

## How Novita Fits in the Inference Landscape

The inference API space has developed distinct tiers. Groq and Fireworks are the speed leaders on supported models, achieving throughput that Novita cannot match on large MoEs. Together AI has the most complete managed platform including fine-tuning pipelines. DeepInfra has comparable LLM pricing to Novita but weaker context windows on large models and no image generation story.

Novita occupies a specific position: the best economics for LLM inference when throughput is not the primary constraint, combined with a genuinely differentiated image generation platform, wrapped in a global GPU cloud that extends to non-LLM compute workloads.

The customer mix reflects this. A developer building a document intelligence pipeline (long context, batch processing, cost-sensitive) is better served by Novita than Fireworks. A developer building a real-time coding assistant that needs sub-second responses on DeepSeek V4 Pro should route through Fireworks. A developer building an image generation product almost certainly needs Novita — nothing else has the catalog breadth.

The Agent Sandbox is early and worth watching. If Novita can establish itself as the standard execution environment for open-source agent frameworks the way it established itself as the default inference endpoint for image models, the business model gets significantly stronger.

---

## The Bootstrapped Bet

The funding question is worth returning to at the end.

Novita's bootstrapped status is not a sign of investor disinterest — it is a deliberate operating choice in a space where venture-backed competitors have burned through capital to acquire customers at negative unit economics. The evidence that the bet is working, so far: $1.1M ARR, Hugging Face official partner status, Vercel top-10 AI provider, and a roster of real customers including Quora.

The risk is that the inference space is consolidating. GPU infrastructure is expensive. Models are getting larger and more demanding. A well-funded competitor could choose to price below cost on the models where Novita has price leadership and erode that advantage. Novita's answer to that risk is catalog breadth — specifically, the 10,000-model image generation catalog that no one else has productized — and the speed of integration into the Hugging Face and OpenRouter distribution layers.

Whether a ten-person team can hold that position as the market matures is genuinely uncertain. But the position they've built is more defensible than it looks from the outside.

---

## Verdict

**Rating: 4/5**

Novita AI is the best price-performance option for LLM inference workloads where speed is secondary to cost, and the only serious choice for developers who need an API across thousands of open-source image models. The 1M-token context windows on DeepSeek V4 Pro — at the same price where competitors cap at 66k — is a concrete advantage for document and agentic workloads. GPQA Diamond #1 accuracy signals that price leadership does not come at an accuracy cost.

Deducted for: slower throughput on large MoEs, no managed fine-tuning pipeline, unconfirmed SOC 2 status, and the execution risk inherent in a ten-person team running a multi-product platform. The Agent Sandbox is promising but too new to evaluate fully.

For teams where batch processing costs, image generation variety, or long-context LLM inference are the primary constraints, Novita is the right starting point. For real-time applications demanding maximum throughput on flagship reasoning models, route to Fireworks. For managed fine-tuning, look at Together AI.

**[Novita AI →](https://novita.ai/)**

---

*This review is based on publicly available information including official documentation, Artificial Analysis benchmarks, PR Newswire releases, and third-party provider comparisons. ChatForest did not test Novita AI directly. Pricing and model availability change frequently — verify current figures at novita.ai before making procurement decisions.*
