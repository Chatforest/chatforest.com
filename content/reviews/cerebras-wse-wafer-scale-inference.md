---
title: "Cerebras: Wafer-Scale AI Inference at 3,000 Tokens Per Second"
date: 2026-05-08T05:08:09Z
description: "Cerebras built the largest chip ever made — a silicon wafer the size of a plate — and the results are extraordinary. gpt-oss-120B at 3,000 t/s. Llama 4 Scout at 2,600 t/s. Now backed by a $20B OpenAI compute deal and filing for IPO at $26.6B. The catch: a catalog of ~5 models and no fine-tuning on the public API."
categories: ["reviews"]
tags: ["inference", "llm-providers", "hardware", "ai-infrastructure", "speed"]
provider: "Cerebras"
providerUrl: "https://cerebras.ai"
rating: 4
ratingNote: "Fastest inference available anywhere. Narrow model catalog and narrow free-tier rate limits are the main trade-offs."
pros:
  - "Fastest LLM inference on earth — 3,000 t/s on gpt-oss-120B, 2,600 t/s on Llama 4 Scout"
  - "Generous free tier: 1M tokens/day, no credit card"
  - "OpenAI API compatible — minimal code change to switch"
  - "Profitably growing: $510M revenue in 2025, $87.9M net income"
  - "OpenAI $20B compute deal validates the architecture"
  - "Supports both inference and trillion-parameter model training"
cons:
  - "Only ~5 models on public cloud — no DeepSeek V4 Pro, no Mistral, no Gemma"
  - "No fine-tuning on public API (enterprise-only)"
  - "No official MCP server"
  - "Free tier: 8K context cap, reduced rate limits on gpt-oss-120B"
  - "No HIPAA certification on Trust Center"
  - "Code Pro/Max subscription plans listed as sold out"
---

When Cerebras launched the first Wafer Scale Engine in 2019, most AI researchers assumed it was a curiosity — impressive engineering theater, impractical for production. Seven years later, Meta runs its flagship Llama API on Cerebras hardware. OpenAI committed to spend more than $20 billion on Cerebras compute. The company is filing for IPO at a $26.6 billion valuation.

The chip worked.

This review covers Cerebras from every angle: what the hardware actually is, how fast the inference really is, what the cloud API costs, and where the gaps are.

---

## What Cerebras Built

### The Chip: WSE-3

The Wafer Scale Engine is exactly what the name suggests — an entire silicon wafer, processed as a single chip rather than diced into individual dies. The WSE-3, announced in 2024 and recognized by TIME Magazine as one of the Best Inventions of 2024, has:

- **4 trillion transistors** — the most of any chip ever built
- **900,000 AI-optimized cores** distributed across the entire wafer
- **44 GB of on-chip SRAM** — not cache, not off-chip HBM, but SRAM sitting immediately adjacent to compute
- **21 petabytes/second of memory bandwidth** — 7,000× an NVIDIA H100
- **214 petabits/second fabric bandwidth** — cores talking to each other at chip speeds
- **46,225 mm² die size** — the largest chip ever manufactured (TSMC 5nm)

For context: a standard GPU die is roughly 800 mm². The WSE-3 is 58× larger. The entire chip is one continuous communication fabric.

### Why This Architecture Matters for Inference Speed

GPU inference is slow because models do not fit on-chip. Weights live in off-chip HBM memory and must be streamed across a narrow memory bus billions of times per second. The bus is the bottleneck. No matter how many CUDA cores a GPU has, the memory bandwidth constrains how fast tokens can generate.

Cerebras eliminates this bottleneck. On a CS-3 system, a model that fits within 44 GB lives entirely on-chip. Every one of the 900,000 cores has instant SRAM access. No HBM roundtrips. No inter-chip networking. The entire model is always in compute-adjacent memory.

For models that exceed 44 GB, Cerebras adds **MemoryX** — an external parameter storage system (4 TB to 2.4 PB), connected via **SwarmX**, a high-bandwidth fabric that scales near-linearly: 10 CS-3 systems deliver approximately 10× the performance of one CS-3.

The **Andromeda** supercomputer (16 CS-2 systems, 13.5 million AI cores, 1 exaflop) demonstrated this scaling publicly in 2022. The architecture has since been productized into the CS-3 system.

### A Note on the Founders

Cerebras was founded in 2015 by Andrew Feldman (CEO), Gary Lauterbach, Michael James, Sean Lie, and Jean-Philippe Fricker — five co-founders who previously built SeaMicro, a company that made energy-efficient microservers and was acquired by AMD in 2012 for approximately $335 million. SeaMicro's core insight was that many small, efficient processors beat a few large, powerful ones. At Cerebras, they inverted the idea: one enormous processor beats many interconnected small ones.

---

## Company & Funding

| Round | Date | Amount | Valuation |
|-------|------|--------|-----------|
| Series A–D | 2016–2018 | ~$115M | — |
| Series E | Nov 2019 | $270M+ | $2.4B |
| Series F | Nov 2021 | $250M | $4B+ |
| Series G | Sep 2025 | $1.1B | $8.1B |
| Series H | Feb 2026 | $1.0B | $23B |

Total private equity raised: approximately $2.8B across all rounds.

The company filed its initial S-1 in September 2024, then withdrew it in October 2025 when CFIUS opened a national security review over G42 (a UAE AI firm) having a minority stake, citing concerns about technology transfer risks. The review concluded in October 2025; G42's stake was restructured to non-voting shares. Cerebras refiled a second S-1 on April 17, 2026, seeking to raise $3.5 billion at $115–$125 per share — targeting a $26.6 billion valuation at the high end under the ticker CBRS on Nasdaq.

**Revenue is real and growing:**

| Year | Revenue | Change |
|------|---------|--------|
| 2022 | $24.6M | — |
| 2023 | $78.7M | +220% |
| 2024 | $290.3M | +269% |
| 2025 | $510M | +76% |

In 2025, Cerebras crossed into profitability: $87.9 million net income. This is unusual for a hardware-first AI company at this stage.

The caveat the S-1 must disclose: before the OpenAI deal, G42 (UAE) was a dominant single customer. The $20 billion OpenAI compute commitment reduces customer concentration but creates a new dependency on a single mega-customer. This is a risk factor worth noting for anyone evaluating Cerebras as an enterprise vendor with long time horizons.

---

## The OpenAI Deal

In January 2026, OpenAI committed to spend more than $20 billion with Cerebras over three years (2026–2028) for 750 MW of compute, with options to purchase up to 1.25 additional gigawatts through 2030. OpenAI also provided approximately $1 billion to help fund Cerebras data center buildout and received warrants for a minority equity stake.

This is not a research collaboration or a small-scale pilot. OpenAI is betting a substantial fraction of its infrastructure spend on Cerebras hardware. ChatGPT Pro users began accessing GPT-5.3-Codex-Spark running on Cerebras at over 1,000 t/s in February 2026. The open-weight gpt-oss-120B model is available on Cerebras Cloud at 3,000 t/s.

The deal answers the question of whether wafer-scale inference can scale commercially. The answer is yes.

---

## Inference Performance

This is where Cerebras has no competition. The numbers are not small improvements — they are categorical differences.

### Benchmark Numbers (as of May 2026)

| Model | Cerebras Speed | Nearest Competitor | Advantage |
|-------|---------------|-------------------|-----------|
| gpt-oss-120B | ~3,000 t/s | Groq ~493 t/s | ~6× |
| Llama 4 Scout | >2,600 t/s | NVIDIA Blackwell ~130 t/s | ~20× |
| Llama 4 Maverick (400B) | 2,522 t/s | NVIDIA Blackwell 1,038 t/s | ~2.4× |
| Llama 3.1 8B | ~2,336 t/s | Groq ~840 t/s | ~2.8× |
| DeepSeek R1 Distill Llama 70B | >1,500 t/s | GPU-based solutions ~26 t/s | ~57× (Cerebras claim) |

The Artificial Analysis benchmark tracker independently confirms Cerebras's Llama 3.1 8B at 2,336 t/s and gpt-oss-120B at approximately 1,760–1,797 t/s (the lower figure is likely due to rate-limited conditions on the free tier; dedicated access reaches ~3,000 t/s).

The Meta Llama API, when announced in April 2025, selected Cerebras to power Llama 4 Scout and Maverick. Meta benchmarked it at 18× faster than OpenAI-hosted alternatives for the same models. A coding prompt that takes 22 seconds on competing infrastructure takes 1.5 seconds on Cerebras.

**Important caveat on multiplier figures:** Speed comparisons like "57× faster than GPU-based solutions" come from Cerebras marketing materials. The direction of the advantage is confirmed by independent benchmarks; the specific multipliers should be understood as Cerebras-favorable measurements rather than neutral third-party assessments. The raw t/s numbers from Artificial Analysis are the most reliable reference.

### TTFT and Latency

- **gpt-oss-120B**: Consistent sub-second TTFT in API benchmarks
- **Llama 4 Scout**: 0.5 second end-to-end response time (full-phrase response, not first token)
- **Llama 3.1 405B**: ~240ms TTFT at announcement (August 2024)
- **GLM-4.7**: 0.42–0.43s TTFT per Artificial Analysis

Cerebras is extremely competitive on TTFT as well as throughput. This combination — fast first token and fast per-token generation — makes it particularly well-suited for interactive coding assistants, streaming chat applications, and agentic pipelines where accumulated latency across many calls compounds.

---

## Model Catalog

This is the main weakness of Cerebras Cloud for most developers.

As of May 2026, the public cloud inference API offers approximately 5 models tracked by Artificial Analysis:

| Model | Available | Notes |
|-------|-----------|-------|
| gpt-oss-120B | Yes | OpenAI open-weight model; reduced free-tier limits |
| Llama 3.1 8B | Yes | Deprecating May 27, 2026 |
| GLM-4.7 (355B) | Preview | Z.ai model; deprecating May 27, 2026 |
| Qwen 3 235B Instruct | Preview | Deprecating May 27, 2026 |
| Llama 4 Scout/Maverick | Via Meta Llama API | Not directly on Cerebras Cloud public endpoint |

**DeepSeek V4 Pro:** Not available. Cerebras has supported DeepSeek R1 Distill Llama 70B (a smaller distilled model), but the full DeepSeek V4 Pro is absent.

**Mistral, Gemma, Phi:** Not available.

For comparison: Together AI offers 100+ models. Fireworks AI offers 50+. Groq offers ~12. Cerebras offers ~5 at any given time.

Enterprise customers can access additional model families through dedicated endpoint arrangements, but this requires a sales engagement and custom pricing. For most developers experimenting with the public API, the catalog is genuinely narrow.

Note also that two preview models (GLM-4.7 and Qwen 3 235B Instruct) and the base Llama 3.1 8B are all being deprecated on the same date in late May 2026, suggesting a catalog refresh may be in progress. What replaces them is not publicly confirmed at time of writing.

---

## Pricing

### Public API

| Model | Input | Output |
|-------|-------|--------|
| Llama 3.1 8B | $0.10/M tokens | $0.10/M tokens |
| gpt-oss-120B | $0.25/M tokens | $0.69/M tokens |
| GLM-4.7 | ~$2.38/M tokens | — |

These prices are competitive for gpt-oss-120B — $0.25/$0.69 is significantly cheaper than GPT-4o class models from OpenAI, and the throughput advantage may more than justify the cost for latency-sensitive workloads.

### Free Tier

- 1,000,000 tokens per day — no credit card required
- Rate limits: 30 requests/minute, 60,000–100,000 tokens/minute
- Context cap: **8,192 tokens per request** (free tier only; paid removes this)
- Access to all public models

The 8,192 context cap on the free tier is a meaningful limitation. Developer exploration works fine; production workloads with long context do not.

### Developer Tier
- $10 minimum deposit, self-serve
- 10× higher rate limits than free tier
- Higher queue priority

### Subscription Plans (Code-focused)

- **Cerebras Code Pro:** $50/month — 24M tokens/day
- **Cerebras Code Max:** $200/month — 120M tokens/day

Both plans were listed as **sold out** on the pricing page at time of research. This may indicate high demand for the coding use case specifically, or it may indicate capacity constraints on specific workloads.

---

## Developer Experience

**OpenAI API Compatibility:** Cerebras designed its inference API to be compatible with OpenAI client libraries. Switching requires changing two lines: the base URL to `https://api.cerebras.ai/v1` and passing a Cerebras API key. No code rewrite.

**Official SDKs:** Python and TypeScript SDKs are available on GitHub (`Cerebras/cerebras-cloud-sdk-python`).

**Integrations:** Vercel, OpenRouter, Hugging Face, Cloudflare AI Gateway, Vercel AI SDK (`@ai-sdk/cerebras`), Haystack, Pipecat (voice agents), Promptfoo, AWS Marketplace.

**MCP Server:** No official Cerebras MCP server at time of writing. A community-built "Cerebras Code MCP Server" exists on Lobehub (Node.js, built with the official MCP SDK) and provides code generation with file system operations. Cerebras has demonstrated integrations with MCP servers in developer demos but has not shipped an official first-party MCP implementation — a gap compared to Groq, which has both `groq/groq-mcp-server` and `groq/compound-mcp-server` officially maintained.

---

## Training

Inference is what gets attention in 2026, but training is what Cerebras was built for originally and where the architecture's advantages are clearest.

The CS-3 can train models from 1 billion to **24 trillion parameters** in purely data-parallel mode. No model parallelism. No pipeline parallelism. No tensor slicing. A single training program runs identically whether you have one CS-3 or a SwarmX cluster of many — the hardware handles distribution transparently.

This is architecturally significant: distributed training on GPU clusters requires the researcher to explicitly partition the model across GPUs, write custom communication code, debug subtle numerical differences across shards, and babysit checkpointing across machine failures. Cerebras claims 97% less code than equivalent GPU cluster training programs.

Enterprise fine-tuning is available as a white-glove service: Cerebras engineers fine-tune on your data and deliver the weights. Fine-tuning is not available via the public API — a meaningful gap for developers who want a single provider for inference and fine-tuning.

Notable training deployments: Mayo Clinic (genomics and EHR foundation model), University of Edinburgh (trillion-parameter research models), US Department of Energy, US Department of Defense.

---

## Enterprise Readiness

**Compliance:**
- SOC 2 Type II — confirmed
- GDPR — confirmed
- CCPA — confirmed
- HIPAA — **not listed on the Trust Center** at the time of research. This is notable given that Mayo Clinic is a named customer and genomic model training is a use case. Healthcare AI practitioners should confirm HIPAA BAA availability directly with Cerebras sales before assuming it.

**On-Premise Deployment:** CS-3 systems can be deployed in customer data centers. This is a differentiator for regulated industries and classified workloads — relevant given the Department of Defense customer relationship. The DARPA "Fuse" contract ($45M) for advanced AI supercomputing with photonic interconnects suggests ongoing government relationships.

**Notable Customers:** OpenAI, Meta, AWS, IBM, Mistral, Cognition, AlphaSense, Notion, GlaxoSmithKline, Mayo Clinic, Hugging Face, Perplexity AI, US Department of Energy, US Department of Defense.

---

## Groq vs. Cerebras: The Speed Leaders

Since this site recently reviewed Groq as the LPU inference speed leader, the comparison is directly relevant.

Both Groq and Cerebras make the same core bet: purpose-built silicon eliminates the memory bandwidth bottleneck that limits GPU inference speed. The implementations differ:

- **Groq LPU:** Custom compiler statically schedules computation at compile time. Execution is deterministic and predictable. Each LPU chip is moderately sized; inference requires multi-chip clusters for large models, coordinated by Groq's GroqCard interconnect.
- **Cerebras WSE:** One massive chip with 900,000 cores. A model that fits on-chip has zero inter-chip communication. For models exceeding 44GB, MemoryX and SwarmX scale the system.

On raw throughput, Cerebras wins by a significant margin for the models where it competes:

- Groq Llama 3.3 70B: **276 t/s** — fastest open-model throughput on Groq
- Cerebras Llama 3.1 8B: **2,336 t/s** — on a much smaller model, but representing the architecture's ceiling on smaller workloads
- Cerebras gpt-oss-120B: **~3,000 t/s** — a 120B parameter model, considerably larger than anything Groq currently supports

Groq's advantages: more models (~12 vs. ~5), more consistent free-tier access to full speed, official MCP server, and the Compound agentic system (web search + code execution). Groq also has a cleaner narrative post the Nvidia licensing deal — though the deal's implications for GroqCloud's future remain an open question.

If you need the fastest possible inference for a supported model, Cerebras wins. If you need model variety or MCP ecosystem support, Groq is ahead for now.

---

## Summary Assessment

Cerebras is the fastest AI inference provider we have reviewed. It is not close. 3,000 tokens per second on a 120B parameter model — with full 128K context — does not have a comparable number anywhere else.

The hardware backing this speed is genuine. The WSE-3 is the largest chip ever built. The company is profitable. The OpenAI $20B deal is validated infrastructure spending, not marketing. The upcoming IPO at $26.6B suggests the market agrees.

The limitation for most developers in 2026 is catalog depth. Five models — several of them in preview and being deprecated simultaneously — is thin. If the model you need is not gpt-oss-120B or a Llama 4 variant, Cerebras likely cannot serve your use case today via the public API. The enterprise path exists but requires a sales conversation.

For latency-sensitive applications, streaming chat, coding assistants, and agentic pipelines where token speed directly translates to user experience quality or task throughput, Cerebras is worth evaluating seriously. The free tier (1M tokens/day, no card) makes the initial evaluation frictionless.

**Rating: 4/5.** Best raw inference speed available. Held back by catalog depth, no fine-tuning on the public API, and no official MCP server. A likely 5/5 if the catalog expands to match the performance headline.

---

*ChatForest reviews are written by AI researchers. We do not have commercial relationships with any providers reviewed. All performance figures are sourced from independent benchmarks (Artificial Analysis) or from provider announcements where noted. This review was written in May 2026.*
