---
title: "DeepInfra Review: The Open-Source Inference Specialist"
date: 2026-05-08
description: "DeepInfra runs 5 trillion tokens per week across 150+ open-source models, owns its own GPUs, and just raised $107M Series B with NVIDIA as an investor. We review the inference platform built by the team behind imo messenger."
tags: ["ai-infrastructure", "inference", "open-source", "llm-hosting", "api"]
categories: ["reviews"]
rating: 4
author: "ChatForest"
---

Three ex-engineers from imo messenger — a messaging app with over a billion Play Store downloads — looked at the AI inference landscape in 2022 and saw a systems problem, not a research problem.

Running large language models in production was expensive, slow, and complicated. Every team that wanted to use open-source models had to provision their own GPU clusters, manage batching, handle scaling, and negotiate with cloud providers. The people best positioned to fix this weren't ML researchers. They were infrastructure engineers who had spent years figuring out how to handle billions of messages cheaply.

That's the origin story of DeepInfra. Four years later, the company processes nearly five trillion tokens per week across more than 150 open-source models, owns its own data centers, and just closed a $107 million Series B round with NVIDIA as one of the investors.

---

## Company Background

DeepInfra was incorporated in September 2022 and emerged from stealth in 2023. The founding team — **Nikola Borisov** (CEO), **Yessenzhar Kanapin**, and **Georgios Papoutsis** — all came from imo.im, a messaging platform with over 200 million monthly active users.

Borisov spent a decade at imo (2010–2020), eventually serving as Director of Engineering. The infrastructure he helped build supported hundreds of millions of users with a backend that ran lean — imo competed against WhatsApp, LINE, and WeChat while remaining small by big-tech standards. That experience — doing a lot with constrained resources — shapes how DeepInfra thinks about inference economics.

The thesis when DeepInfra launched was simple: **inference, not training, would become the dominant driver of enterprise AI workloads**. The compute required to run models in production would eventually dwarf the compute used to train them. Building infrastructure optimized for inference from day one — rather than retrofitting training infrastructure — would be a durable competitive advantage.

That thesis looks prescient in 2026. Nearly 30% of DeepInfra's token volume is now driven by autonomous agents running without human oversight.

### Funding

- **Seed**: $8 million (2023), led by A.Capital Ventures and Felicis
- **Series B**: $107 million (May 4, 2026), co-led by 500 Global and Georges Harik (former Google VP of Engineering), with participation from A.Capital Ventures, Crescent Cove, Felicis, **NVIDIA**, Peak6, Samsung Next, Supermicro, and Upper90
- **Total funding**: $133 million+

The NVIDIA participation matters more than the dollar figure. NVIDIA is not a passive financial investor — the company has designated DeepInfra as an early infrastructure collaborator in its open AI ecosystem. That means early access to new hardware and software frameworks, including NVIDIA Dynamo (discussed below).

DeepInfra has scaled token volume 25x since its Series A and 8,000x since its seed round. Revenue tripled in the first months of 2026 alone, though absolute figures are not disclosed.

---

## Infrastructure

DeepInfra owns and operates its own hardware across **eight data centers in the United States**. This vertical integration is a core strategic choice, not an accident of scale.

Inference is one workload. A company that owns GPUs dedicated exclusively to serving inference can optimize every layer of the stack — networking, batching, scheduling, memory management — in ways that are harder to achieve when sharing infrastructure with training jobs and general cloud workloads.

Available GPU hardware includes:
- NVIDIA A100, H100, H200
- NVIDIA B200 and B300 (latest Blackwell generation)
- Configurations ranging from single-GPU deployments to multi-node clusters

**NVIDIA Dynamo partnership**: DeepInfra is one of the early adopters of NVIDIA Dynamo, NVIDIA's inference optimization software. The company also supports Nemotron models and the NemoClaw agent framework. NVIDIA's upcoming Vera Rubin GPU generation, combined with Dynamo, is expected to deliver up to 20x improvement in inference cost efficiency — a number DeepInfra will be positioned to pass through to customers.

---

## Model Catalog

DeepInfra's catalog spans more than 150 open-source models across multiple modalities. This is one of the broadest selections among inference API providers.

### Large Language Models

Key models available as of May 2026:

- **DeepSeek**: V4 Pro, V4 Flash, V3.2, R1, R1 Distill Llama 70B
- **Meta Llama**: Llama 4 Maverick, Llama 3.3 70B, Llama 3.1 70B and 8B
- **Qwen**: Qwen3 235B-A22B, Qwen3.5 72B, smaller Qwen3 and Qwen3.5 variants
- **Mistral**: Mistral 7B, Mixtral 8x7B and 8x22B
- **Google**: Gemma 3 series
- **NVIDIA**: Nemotron series (including gpt-oss-120b)
- **Zhipu**: GLM-5 and variants

The catalog also includes reasoning-specialized models and coding-focused models. DeepInfra adds new models quickly — the latency from a model's public release to availability on the platform is typically measured in days.

### Embeddings and Reranking

DeepInfra maintains a selection of embedding models for search and retrieval-augmented generation (RAG) applications:
- BGE embedding models (M3 and variants)
- Qwen3 Embedding series (up to 8B parameters)
- Reranker models for search quality improvement

### Image Generation

- FLUX (Black Forest Labs) — FLUX.1 [schnell] and [dev]
- Stable Diffusion variants
- LoRA adapter support (load LoRA adapters from Civitai for custom image styles)

### Other Modalities

- **Automatic Speech Recognition**: Whisper (large-v3 and variants)
- **Text-to-video**: Available in catalog

The breadth here is unusual. Most inference API providers specialize in LLMs. DeepInfra's multimodal catalog means a developer can build image generation, transcription, embeddings, and LLM calls all from a single API key with a single billing relationship.

---

## API and Developer Experience

DeepInfra provides a fully OpenAI-compatible REST API. Drop-in replacement is as simple as changing the base URL from `api.openai.com/v1` to `api.deepinfra.com/v1/openai` — the same OpenAI SDK, the same request format, the same response structure.

This is the inference API standard in 2026. Every serious inference provider offers OpenAI compatibility, and DeepInfra's implementation is thorough.

Additional API features:
- **Tool calling / function calling**: Available on supported models
- **Streaming**: Standard SSE streaming for real-time token delivery
- **Context windows**: Up to 262,144 tokens on recent models (e.g., Qwen3.6 27B)
- **Batch inference**: Not prominently documented as a named product, but high-throughput throughput is available

The documentation at docs.deepinfra.com is clear and developer-oriented. Quick-start guides, model-specific examples, and clear parameter descriptions.

### No Official MCP Server

DeepInfra does not currently offer an official Model Context Protocol (MCP) server. There is a community-built MCP server (`mcp-deeinfra` by phuihock) that wraps DeepInfra's API and provides image generation, text processing, embeddings, and speech recognition capabilities. It is available on GitHub and indexed by MCP server directories, but it is not affiliated with or maintained by DeepInfra.

For developers building MCP-connected agent workflows, this means an extra integration step or relying on an unofficial community project.

---

## Performance Benchmarks

DeepInfra publishes its own benchmark blog posts for key models, including detailed latency and throughput numbers across providers. Selected figures from third-party tracking (Artificial Analysis and BenchLM):

| Model | Output Speed | TTFT |
|---|---|---|
| DeepSeek V3.2 | ~97 t/s | ~0.82s |
| DeepSeek R1 Distill Llama 70B | ~41.6 t/s | ~0.40s |
| Qwen3.5 0.8B FP8 | ~360 t/s | — |
| Qwen3.5 2B FP8 | ~356 t/s | — |

For DeepSeek R1 Distill Llama 70B, DeepInfra recorded the **lowest time-to-first-token** among tracked providers in recent benchmarks — competitive with providers that market themselves primarily on speed.

DeepInfra is not a pure-speed leader. Cerebras (WSE chips), SambaNova (RDU), and Groq (LPU) achieve higher output speeds for specific models, particularly on the largest reasoning models, because their hardware architectures are purpose-built for it. What DeepInfra offers is **broad coverage** — competitive performance across a wide model catalog at low cost, rather than maximum speed on a narrow selection.

---

## Pricing

DeepInfra consistently offers some of the most competitive pricing in the open-source inference market. Selected prices as of May 2026:

| Model | Input | Output |
|---|---|---|
| Llama 3.1 8B (Turbo FP8) | $0.02/M | $0.02/M |
| DeepSeek V4 Flash | $0.14/M | $0.28/M |
| DeepSeek V3.2 | $0.26/M | $0.38/M |
| DeepSeek V4 Pro (FP4) | — | — |
| GLM-5 | ~$1.24/M blended | — |

Full pricing is listed at deepinfra.com/pricing. The range across all models runs from approximately **$0.02 to $82.50 per million tokens**, with the high end covering specialized or computationally expensive models.

For DeepSeek V3.2, $0.26/$0.38 per million tokens puts DeepInfra at or near the bottom of the price range across providers. For GLM-5 (a powerful open-source reasoning model), DeepInfra has claimed the lowest blended price on the market at $1.24/M — roughly 20% below the industry average for that model.

There are no minimum commitments, no setup fees, and no long-term contracts required for the shared inference API. You pay per token.

---

## Custom Deployments and Fine-Tuning

DeepInfra offers a **private deployment** tier for teams that need to run custom or fine-tuned models.

Private deployments support:
- **Custom fine-tuned LLMs**: Upload your own fine-tuned weights and deploy them on DeepInfra's infrastructure
- **LoRA adapters**: Add LoRA fine-tuned adapters on top of supported base models — for both text LLMs and image generation models
- **GPU selection**: A100-80GB, H100-80GB, with newer generations available

Private deployments are billed **per GPU-hour** rather than per token. You pay for the time the GPU is allocated to your deployment, regardless of actual token traffic. Autoscaling is available — deployments can scale from zero to many instances based on load.

For teams that have done their own fine-tuning and want production-grade serving without managing their own infrastructure, this is a meaningful offering. DeepInfra handles the operational complexity; you bring the model.

---

## Compliance and Security

- **SOC 2 Type II**: Certified
- **ISO 27001**: Certified
- **Zero data retention**: Prompts and completions are not stored after the API response is returned
- **Enterprise support**: Available for production workloads

The combination of SOC 2 + ISO 27001 + zero data retention is enterprise-grade from day one. This is not a startup feature gap that needs to be roadmapped — it's already in place.

---

## Competitive Position

DeepInfra sits in an increasingly crowded segment: open-source inference APIs. Direct competitors include Together AI, Fireworks AI, Replicate, Hugging Face Inference API, and the inference layers added by cloud providers.

What distinguishes DeepInfra:

**Infrastructure ownership**: DeepInfra owns its GPUs and data centers. Many competitors rent cloud capacity and resell it with an inference wrapper. Ownership means cost control, optimization latitude, and — as the NVIDIA Dynamo relationship shows — the ability to adopt next-generation software closer to launch.

**Catalog breadth**: 150+ models including text, embeddings, image, audio, and video. Most competitors are LLM-only. The multimodal catalog simplifies API consolidation for teams building complex applications.

**Price**: Consistently at or near the lowest cost in the market for open-source models. The $0.02/M token price for small models is aggressive; so is the V3.2 price at $0.26/$0.38.

**NVIDIA alignment**: The Series B investor list includes NVIDIA, Supermicro (a key Blackwell server manufacturer), and Samsung Next. This is not passive capital — it's a network of infrastructure supply chain relationships.

**Agent workload growth**: 30% of token volume is agent-driven, and that percentage is growing. DeepInfra's low-cost, high-throughput positioning is aligned with agent workloads, which generate high token volumes at cost-sensitive margins.

### Limitations

- **Not the fastest**: For maximum output speed on the largest models, purpose-built silicon providers (Cerebras, SambaNova, Groq) win. DeepInfra is competitive, but that's different from being the leader.
- **No official MCP server**: The ecosystem play for agent-integrated tools is absent here. Groq, Crusoe, and Anthropic's own tools have official MCP servers; DeepInfra doesn't.
- **Brand awareness**: DeepInfra is less visible in developer communities than Together AI or Fireworks AI, despite comparable or better pricing. Discovery happens through aggregators and benchmark sites more than organic reputation.
- **Limited public financials**: Revenue is growing fast, but no absolute figures or valuation disclosure.

---

## Who Should Use DeepInfra

**Best fit:**
- Teams running high-volume, cost-sensitive inference workloads on open-source models
- Developers who want one API for LLMs, embeddings, image generation, and ASR
- Companies with fine-tuned models that need managed serving without running their own infrastructure
- Enterprise teams requiring SOC 2 + ISO 27001 compliance with zero data retention
- Agent platform builders who need broad model coverage at low cost

**Consider alternatives if:**
- Maximum output speed is the primary requirement (evaluate Cerebras, Groq, or SambaNova)
- You need a proprietary model with ecosystem lock-in that isn't open-source
- An official MCP server is important for your toolchain (Groq or Crusoe have these)

---

## Rating: 4 / 5

DeepInfra has built infrastructure for the era when inference, not training, is the primary AI cost center. The founders understood the problem early, built the right architecture, and maintained competitive pricing through genuine cost efficiency rather than loss-leader pricing.

The Series B investor roster — NVIDIA, Supermicro, Samsung Next alongside institutional VCs — suggests this is not speculative positioning. It's a supply-chain-aligned bet on a company that owns its hardware and is technically prepared for next-generation GPU generations (Blackwell and Vera Rubin with Dynamo).

The weaknesses are real: no official MCP server, no speed records on large models, limited brand awareness in developer communities. These are gaps to watch, not disqualifiers.

For open-source inference at scale — especially if you need breadth across modalities, enterprise compliance, and the lowest per-token cost you can find — DeepInfra is one of the strongest options in the market.

---

*ChatForest reviews AI infrastructure providers based on public information, documentation, and published benchmarks. We do not conduct hands-on testing of the platforms reviewed. Pricing and features may change — verify current details at [deepinfra.com](https://deepinfra.com/).*
