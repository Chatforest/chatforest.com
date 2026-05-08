---
title: "Groq — The LPU Inference Speed Leader (2026 Review)"
date: 2026-05-08T13:00:00+09:00
description: "Groq reviewed: LPU delivers 276 t/s on Llama 3.3 70B — fastest open-model inference available. $750M Series E at $6.9B valuation, $20B Nvidia technology licensing deal (December 2025). Official MCP server. SOC 2 Type II + HIPAA. Narrow catalog, no fine-tuning. Rating: 4/5."
og_description: "Groq (groq.com): LPU-powered inference provider delivering 276 t/s on Llama 3.3 70B — consistently fastest open-model API across independent benchmarks. Founded 2016 by Jonathan Ross (Google TPU designer). $640M Series D (August 2024, $2.8B valuation) → $750M Series E (September 2025, $6.9B valuation) → December 2025: Nvidia agrees to license Groq's inference technology for ~$20B — Nvidia's largest-ever deal. Saudi Arabia $1.5B infrastructure commitment (February 2025). GroqCloud serves 360,000+ developers and 75% of Fortune 100. Llama 3.1 8B: ~840 t/s. Llama 3.3 70B: 276 t/s (3x faster than Fireworks AI). Official MCP server with Compound agentic system. Free tier (no credit card). SOC 2 Type II + HIPAA. Weakness: ~12-model catalog (no DeepSeek V4 Pro, no image gen, no fine-tuning), 2025 revenue projection cut from $2B+ to $500M+. Rating: 4/5."
card_description: "Groq (groq.com) is the speed leader of open-model inference, powered by its proprietary **Language Processing Unit (LPU)** — custom silicon designed from the ground up for linear algebra workloads. **276 t/s on Llama 3.3 70B** (Artificial Analysis benchmark) — roughly **3x faster than Fireworks AI** and **5x faster than Together AI** on equivalent models. **840 t/s on Llama 3.1 8B**. Founded 2016 by **Jonathan Ross**, designer of Google's original TPU. **$750M Series E (September 2025)** at **$6.9B valuation**; then December 2025: **Nvidia agreed to license Groq's inference technology for ~$20B** — Nvidia's largest-ever deal, while GroqCloud continues as an independent operation. Saudi Arabia committed **$1.5B** for Groq-powered infrastructure (February 2025). GroqCloud serves **360,000+ developers** and **75% of Fortune 100** companies. Official **MCP server** (plus a Compound-specific server). **Compound** agentic AI system (GA October 2025): web search + code execution, claims 25% higher accuracy than OpenAI Web Search Preview. **SOC 2 Type II, HIPAA**. Weakness: narrow catalog (~12 models — no DeepSeek V4 Pro, no image generation, no fine-tuning, no custom model deployment); 2025 revenue projection cut from $2B+ to $500M+. Part of our **AI/ML Tools** and **Developer Tools** categories. Rating: 4/5."
last_refreshed: 2026-05-08
categories: ["/categories/ai-ml-tools/", "/categories/developer-tools/"]
---

Every provider comparison starts with DeepSeek V4 Pro throughput numbers, and Fireworks AI keeps anchoring the GPU-based leaderboard at 167–174 t/s. That gap looked definitive until you remember that Groq does not run DeepSeek V4 Pro.

Groq's catalog is narrow — roughly 12 models. You will not find the newest DeepSeek release, image generation, or fine-tuning. What you will find is Llama 3.3 70B at **276 t/s** on Artificial Analysis's independent benchmark — roughly three times faster than Fireworks AI on the same model, at half the price. Llama 3.1 8B: approximately **840 t/s**.

For latency-critical workloads — voice applications, real-time chat, interactive agents requiring sub-second response times — Groq offers something no GPU cluster currently replicates at scale. The reason is the hardware itself: a custom chip that Jonathan Ross began designing after he left Google, where his previous chip project became the Tensor Processing Unit that now runs more than half of Google's compute infrastructure.

In December 2025, Nvidia agreed to license Groq's inference technology for approximately **$20 billion** — Nvidia's largest-ever deal. GroqCloud continues operating independently. Ross moved to Nvidia. The technology licensing deal is the most consequential event in AI inference hardware since the GPU became the default training substrate. Understanding what Groq built, and why Nvidia paid to own the IP, is the context behind everything that follows.

Part of our **[AI/ML Tools category](/categories/ai-ml-tools/)** and **[Developer Tools category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Service** | [Groq](https://groq.com/) |
| **Founded** | 2016, Mountain View, California |
| **Founder / CEO** | Jonathan Ross (founder; moved to Nvidia December 2025). Simon Edwards (current CEO) |
| **LPU origin** | Tensor Streaming Processor (TSP), originally codenamed "Alan" — rebranded LPU post-ChatGPT |
| **Series D** | $640M (August 2024, BlackRock Private Equity lead, $2.8B valuation) |
| **Series E** | $750M (September 2025, Disruptive + BlackRock lead, $6.9B valuation) |
| **Total raised** | ~$1.75B |
| **Nvidia deal** | ~$20B technology licensing agreement (December 2025, non-exclusive, non-acquisition) |
| **Saudi Arabia** | $1.5B infrastructure commitment (February 2025, LEAP conference) |
| **Revenue (2025)** | ~$500M+ (revised projection; originally $2B+) |
| **Developers** | 360,000+ registered on GroqCloud |
| **Enterprise reach** | 75% of Fortune 100 companies maintain GroqCloud accounts |
| **Model catalog** | ~12 actively supported models (Llama, Qwen, gpt-oss variants, Whisper) |
| **Top throughput** | 840 t/s (Llama 3.1 8B), 276 t/s (Llama 3.3 70B) — Artificial Analysis benchmark |
| **TTFT** | 0.6–0.9s consistently across catalog |
| **Free tier** | Yes — no credit card required; 30 RPM / 6,000 TPM / 1,000 RPD |
| **Fine-tuning** | No |
| **Image generation** | No |
| **Enterprise compliance** | SOC 2 Type II, HIPAA (BAAs available) |
| **MCP server** | Yes — official groq/groq-mcp-server + groq/compound-mcp-server |
| **On-premise hardware** | GroqRack (64–576+ LPUs per rack), custom enterprise contracts |

---

## The Origin: Jonathan Ross and the TPU That Became the LPU

In 2013, Jonathan Ross was a software engineer at Google who noticed that the company's AI workloads were growing faster than general-purpose processors could handle them. He started a "20% project" — Google's internal policy allowing engineers to spend a fifth of their time on speculative ideas — to design a custom accelerator for neural network inference.

That project became Google's Tensor Processing Unit (TPU). TPUs now run more than half of Google's total compute infrastructure and power every Gemini inference query. Ross built the chip that makes Google AI work.

In 2016, Ross left Google to build a second chip. He co-founded Groq with Douglas Wightman, with the premise that inference — not training — was the bottleneck worth solving at the hardware level. Training happens once. Inference happens billions of times per day and keeps happening. A chip purpose-built for inference could achieve throughput and latency profiles impossible on general-purpose GPUs.

The chip was originally called the **Tensor Streaming Processor (TSP)**, codenamed "Alan." After ChatGPT transformed the market's vocabulary in late 2022, Groq rebranded it the **Language Processing Unit (LPU)** — a name that more precisely described its primary commercial application.

---

## How the LPU Works

The LPU's architectural advantage comes from eliminating everything that makes GPU inference non-deterministic.

GPU-based inference involves DRAM, caches, dynamic schedulers, and synchronization overhead between compute units. Every one of these elements introduces variable latency. The GPU was designed as a general-purpose parallel processor. Inference is a specific workload: matrix multiplication, attention, and activation functions, executed in a predictable sequence. The GPU's generality is overhead when you only need those operations.

The LPU makes different choices:

**On-chip SRAM as primary weight storage.** A GPU loads model weights from off-chip DRAM on demand, with cache misses introducing latency spikes. The LPU uses hundreds of megabytes of on-chip SRAM as the primary weight store — compute units pull weights at full memory bandwidth, every cycle, without going to slower off-chip memory. This is the primary mechanical reason for Groq's low time-to-first-token (TTFT).

**Static scheduling.** The compiler schedules every instruction and data movement at compile time. There is no dynamic scheduler in hardware. Every step of the inference computation is predetermined — the chip executes a known sequence with no decision-making overhead during execution. Groq calls this "deterministic execution."

**Data conveyor belts.** Instructions and data move between SIMD (single-instruction/multiple-data) function units along statically scheduled "conveyor belts." No synchronization is needed between units because timing is compiled in. The chip never waits for a lock or a cache fill.

**Scale-out tensor parallelism.** A single model layer is split across multiple LPUs for larger models. The inter-chip interconnects are designed for this at the hardware level — the interconnect latency is predictable, which lets the compiler schedule across chips the same way it schedules within a chip.

The result: consistent throughput at scale, with TTFT that is nearly independent of model size for models the LPU supports. Where GPU TTFT scales with context length and batch size in complex ways, Groq's LPU maintains 0.6–0.9s TTFT across its catalog under production load.

---

## Funding History and the Nvidia Deal

Groq's funding history spans nearly a decade:

| Round | Date | Amount | Lead Investors | Valuation |
|---|---|---|---|---|
| Series A–B | 2017–2020 | Not publicized | Various | — |
| Series C | April 2021 | $300M | Tiger Global, D1 Capital | — |
| Series D | August 2024 | $640M | BlackRock Private Equity | $2.8B |
| Series E | September 2025 | $750M | Disruptive, BlackRock, Neuberger Berman, Samsung, Cisco, Altimeter | $6.9B |

Total raised: approximately **$1.75 billion** across six rounds.

**Saudi Arabia infrastructure commitment (February 2025):** At LEAP 2025, Saudi Arabia announced a $1.5 billion commitment for Groq-powered AI infrastructure. This was a deployment and infrastructure contract — not equity — with Aramco Digital ordering hundreds of GroqRacks. A Dammam data center went operational, described as the region's largest inference cluster at time of deployment. It was reportedly built in eight days.

**The Nvidia deal (December 2025):** The most consequential event in Groq's history came at the end of 2025. Nvidia agreed to license Groq's AI inference technology and assets for approximately **$20 billion** — Nvidia's largest-ever single deal. The structure was a non-exclusive licensing agreement, not an acquisition. Groq's GroqCloud business is not part of the transaction.

Jonathan Ross and President Sunny Madra moved to Nvidia. Simon Edwards became Groq's new CEO. Nvidia paid approximately 2.9× the September 2025 $6.9B valuation for the technology rights.

The strategic logic: Nvidia's GPU-based inference dominance faces structural pressure from purpose-built inference chips. Rather than compete with Groq's LPU IP from scratch, Nvidia licensed it. The deal lets Nvidia integrate LPU-derived techniques into the NVIDIA AI Factory architecture while neutralizing Groq as an independent hardware competitor. Groq continues operating GroqCloud independently with access to the technology, but the most valuable IP now has a pathway into Nvidia's broader ecosystem.

---

## GroqCloud: The Inference API

GroqCloud is Groq's "tokens-as-a-service" API — a cloud inference service running exclusively on LPU hardware. The API surface is OpenAI-compatible; migration requires changing the base URL and API key.

### Model Catalog

The catalog is intentionally narrow — approximately 12 actively maintained models as of early 2026:

| Model | Context Window | Input ($/1M) | Output ($/1M) |
|---|---|---|---|
| Llama 3.1 8B Instant | 128K | $0.05 | $0.08 |
| Llama 3.3 70B Versatile | 128K | $0.59 | $0.79 |
| Llama 4 Scout 17B (MoE) | 131K | — | — |
| Qwen3 32B | 128K | — | — |
| QwQ-32B (reasoning) | 128K | — | — |
| gpt-oss-20B (high/low) | 131K | — | — |
| gpt-oss-120B (high/low) | 131K | — | — |
| Llama 3.2 11B Vision | 128K | — | — |
| Whisper large-v3 (ASR) | — | — | — |

Pricing ranges from $0.05/1M input tokens (Llama 3.1 8B, one of the cheapest available anywhere) to $0.59/1M (Llama 3.3 70B). Output tokens cost 35–60% more than input, consistent with industry standard.

**What is not available:** DeepSeek V4 Pro (DeepSeek-R1-Distill-Llama-70B was deprecated September 2, 2025, and the current V3/V4 generation is not on GroqCloud). No Mistral, no Gemma 3, no Claude, no proprietary closed models. No image generation. No embedding models (this absence matters for RAG pipelines that want a single provider).

### Pricing Multipliers

**Batch API:** 50% discount on all models. Asynchronous processing, 24-hour to 7-day turnaround for non-real-time workloads.

**Prompt caching:** 50% discount on cached input tokens. Stacks with batch API — batch + caching brings effective cost to approximately 25% of on-demand rates for workloads with repeated context prefixes.

**Free tier:** No credit card required. 30 requests per minute, 6,000 tokens per minute, 1,000 requests per day for most models. This is a genuine free tier — not a trial credit, not a time-limited promotion. For developers building on Llama 3.1 8B, the $0.05/1M pricing and free tier make Groq the cheapest starting point in the market.

---

## Speed: What the Benchmarks Actually Show

Groq's marketing materials describe the LPU as delivering "10x" speed compared to GPU inference. The real-world numbers from independent benchmarks are more nuanced — and still compelling.

**Artificial Analysis (independent, 72-hour median):**

| Model | Groq | Fireworks AI | Together AI | DeepInfra |
|---|---|---|---|---|
| Llama 3.3 70B | **276 t/s** | ~83–90 t/s | ~83–90 t/s | ~70 t/s |
| Llama 3.1 8B | **~840 t/s** | ~174 t/s | ~150 t/s | ~120 t/s |

On Llama 3.3 70B, Groq delivers approximately **3× Fireworks AI's throughput** and **4× Together AI's throughput** at roughly one-third the price ($0.59/1M vs. $1.74–2.10/1M for providers that serve larger catalogs at higher margins).

On Llama 3.1 8B at $0.05/1M, Groq delivers ~840 t/s — making it simultaneously the cheapest and fastest option for that model.

**Time to first token (TTFT):** Groq consistently achieves 0.6–0.9s TTFT under load. Fireworks AI and Together AI typically run 7–9s end-to-end response time for 70B models. For a voice application where 2+ seconds of perceived latency makes the interaction feel broken, that 0.9s TTFT is not a benchmark number — it is the difference between a working product and a non-working one.

**Cerebras comparison:** Cerebras WSE chips (a different architecture — wafer-scale integration) achieve approximately **3,000 t/s on gpt-oss-120B** — significantly faster than Groq's ~476–500 t/s on the same model. Cerebras wins on peak throughput for specific models. Groq wins on TTFT consistency and slightly broader catalog coverage. Both are far ahead of GPU-based providers on speed.

**The DeepSeek V4 Pro gap:** Groq cannot benchmark against the providers reviewed in this series on DeepSeek V4 Pro because Groq does not offer the model. This is the most significant limitation when comparing across the inference provider landscape: the model that has become the reference benchmark for the industry is not available on Groq.

---

## Compound: Groq's Agentic AI System

In April 2025, Groq launched **Compound Beta** — a compound AI system that combines LLM inference with built-in agentic tools: web search and code execution. In October 2025, it moved to general availability as **Compound**.

Compound is built on gpt-oss-120B and Llama models, running on GroqCloud's LPU infrastructure. Groq claims approximately **25% higher accuracy and 50% fewer mistakes** compared to OpenAI's Web Search Preview and Perplexity Sonar on accuracy benchmarks.

Independent evaluation of these claims is limited, but the architectural premise is sound: running retrieval-augmented generation and tool-calling inference on LPU hardware means the compound AI system benefits from the same TTFT advantages as raw inference. An agent that can search the web and execute code with sub-second response latency per step is qualitatively different from one that takes 8+ seconds per step.

Compound is available as a separate API endpoint. Groq also maintains a dedicated `compound-mcp-server` GitHub repository for MCP-based access.

---

## MCP Integration

Groq has invested meaningfully in the MCP ecosystem — more so than any other inference provider reviewed in this series.

**Official groq-mcp-server:** Maintained at `github.com/groq/groq-mcp-server`. Supports querying Groq models, vision inputs, text-to-speech, batch processing, and documentation access from Claude and other MCP clients.

**Official compound-mcp-server:** Maintained at `github.com/groq/compound-mcp-server`. Dedicated server for accessing the Compound agentic AI system via MCP.

**Remote MCP support (beta):** GroqCloud launched support for models running on GroqCloud to consume external MCP servers as tools via the Responses API. This means Groq-hosted models can call external MCP tools during inference — not just Groq being an MCP server, but Groq being an MCP client.

**MCP Connectors:** Groq-maintained wrappers for Google Workspace — Gmail, Drive, Calendar — letting AI agents interact with Google Workspace tools without building their own MCP server.

**Community bounty:** Groq ran an MCP + Responses API Bounty Challenge in 2025, offering $250 in API credits plus community spotlight for useful MCP integrations. The combination of first-party servers, client support, and community program puts Groq's MCP ecosystem ahead of Fireworks AI, Together AI, DeepInfra, and Novita AI in breadth of official tooling.

---

## Enterprise: Hardware, Compliance, and On-Premise Options

### GroqRack and GroqNode

For enterprises requiring data residency, regulatory isolation, or workloads where GroqCloud's multi-tenant architecture is insufficient, Groq sells on-premise hardware:

- **GroqNode:** Individual compute unit containing Groq LPUs.
- **GroqRack:** Enterprise rack system containing 64–576+ LPUs per rack. Targets hyperscalers, sovereign clouds, and regulated industries.

Pricing is not publicly disclosed — custom contracts only. Aramco Digital ordered hundreds of racks. Saudi Arabia's Dammam deployment used GroqRacks.

### Compliance

- **SOC 2 Type II:** Certified as of mid-2024.
- **HIPAA:** Compliant; Business Associate Agreements (BAAs) available on enterprise plans.
- **Data handling:** No customer data stored, no training on customer data, logical isolation per customer in multi-tenant deployment.
- **Trust Center:** trust.groq.com (authoritative compliance documentation).

Enterprise SLA specifics are not publicly documented — available through enterprise sales engagement.

---

## The Revenue Projection Cut

In July 2025, Groq cut its 2025 revenue projection from **$2B+ to approximately $500M+** — a $1.5 billion reduction. The reported cause: data center capacity constraints and manufacturing delays (Samsung Foundry manufactures the LPU chips). The revision reportedly affected Samsung's foundry business, which had planned capacity around Groq's original projections.

One independent estimate (Latka) puts 2025 annualized revenue at ~$172.5M — though this appears to be a mid-year run-rate snapshot, not full-year revenue.

This matters for two reasons. First, it suggests that Groq's supply chain — the ability to manufacture LPUs at scale — is a meaningful operational constraint on growth, and that demand has outpaced chip production. Second, it provides context for the Nvidia deal: licensing technology to Nvidia may generate more reliable cash flow than scaling physical chip manufacturing.

The $500M+ revised projection, if accurate for 2025, would represent strong absolute revenue growth. But the gap between original projections and revised ones indicates that Groq's capacity to serve demand is more constrained than the company's marketing suggested going into 2025.

---

## Limitations

**Narrow model catalog (~12 models):** For teams needing DeepSeek V4 Pro, any Mistral model, Gemma 3, Claude, or proprietary closed models, Groq is not an option. The catalog depth is roughly one-thirtieth of Fireworks AI's 400+ models and a tiny fraction of DeepInfra's breadth.

**No fine-tuning:** Groq does not offer managed fine-tuning. Teams needing SFT, DPO, or reinforcement fine-tuning must go to Fireworks AI, Together AI, or another provider. Fine-tuned models cannot be deployed on GroqCloud's LPU infrastructure.

**No image generation:** Unlike Together AI or Novita AI, Groq has no diffusion or image generation models.

**No embedding models:** For RAG pipelines wanting a single-provider solution for both embeddings and generation, Groq is incomplete.

**Context window ceiling:** 128K–131K tokens — competitive, but not the 1M+ context available from Together AI on some models, or Fireworks AI's full 1M on DeepSeek V4 Pro.

**No dedicated endpoints:** Teams cannot deploy custom fine-tuned models on Groq's LPUs. Deployment options are GroqCloud's shared multi-tenant API or GroqRack on-premise hardware.

**Revenue projection miss and strategic uncertainty:** The Nvidia technology licensing deal has fundamentally altered Groq's competitive position. GroqCloud continues operating, and the company retains access to the technology, but the path forward — whether Groq continues innovating on LPU architecture independently, or becomes primarily a GroqCloud inference service running on licensed technology while Nvidia integrates LPU IP into its own products — is genuinely unclear as of mid-2026. Simon Edwards is a new CEO leading a company whose founder just moved to the entity that licensed its core technology. This is not a reason to avoid GroqCloud for current workloads, but it is relevant context for infrastructure decisions with 2–3 year horizons.

---

## Who Should Use Groq

**Best fit:**

- **Voice and real-time applications:** If your product requires sub-second LLM response latency — voice AI, real-time conversational interfaces, interactive coding tools — Groq's 0.6–0.9s TTFT is a functional requirement, not a benchmark preference.
- **High-throughput Llama or Qwen workloads:** If you are running Llama 3.3 70B or Llama 3.1 8B at scale, Groq delivers the same output at 3–5× higher throughput and lower cost than GPU-based alternatives.
- **MCP-first AI agents:** Groq's official MCP tooling is the most complete among inference providers reviewed to date.
- **Prototyping and development:** The free tier (no credit card, 1,000 requests/day) makes GroqCloud the easiest starting point for developers experimenting with open-weight models.

**Not a fit:**

- **Teams needing DeepSeek V4 Pro, Mistral, Gemma 3, or proprietary models:** Groq's catalog does not include these.
- **Fine-tuning pipelines:** Groq offers no training or fine-tuning services.
- **Image generation:** Not available.
- **Maximum model breadth:** DeepInfra and Together AI offer dramatically wider catalogs.

---

## Competitive Summary

| | Groq | Fireworks AI | Together AI | DeepInfra |
|---|---|---|---|---|
| **Speed (Llama 3.3 70B)** | **276 t/s** | ~85 t/s | ~85 t/s | ~70 t/s |
| **DeepSeek V4 Pro** | No | Yes (167–174 t/s) | Yes (52–60 t/s) | Yes (33 t/s) |
| **Model catalog** | ~12 | 400+ | 200+ | 200+ |
| **Fine-tuning** | No | Yes (SFT/DPO/RFT) | Yes (SFT/DPO/RL) | No |
| **Image generation** | No | Limited | Yes | Yes |
| **Free tier** | Yes | No | No | No |
| **Official MCP server** | Yes (2 servers) | No | No | No |
| **SOC 2 Type II** | Yes | Yes | Yes | — |
| **HIPAA** | Yes | Yes | Yes | — |
| **On-premise hardware** | Yes (GroqRack) | No | No | No |
| **Pricing (70B input)** | $0.59/1M | $1.74/1M | $2.10/1M | $0.28/1M |

**Choose Groq when:** Latency is the primary constraint — voice, real-time chat, interactive agents, developer tooling requiring sub-second response times. Also when running Llama-family models at scale and cost-per-token matters.

**Choose Fireworks AI when:** Speed matters alongside fine-tuning pipeline access, structured output reliability, and the widest enterprise compliance footprint.

**Choose Together AI when:** You need model variety (especially image generation), GPU cluster access, or the deepest fine-tuning options including RL-based fine-tuning.

**Choose DeepInfra when:** Catalog breadth at the lowest possible price is the priority — DeepInfra prices some models below Groq's Llama 3.3 70B at $0.28/1M input.

---

## The Verdict

Groq built something real: a chip that delivers inference throughput and latency no GPU-based provider has matched on equivalent models. The benchmarks are not Groq's marketing materials — they are Artificial Analysis's continuous independent measurements across 72-hour windows. The 276 t/s on Llama 3.3 70B is not a peak figure; it is a median.

The limitations are also real. A 12-model catalog is not competitive for teams needing the full landscape of open-weight models available in 2026. No fine-tuning means Groq is not a full-stack inference platform — it is a speed specialist. The Nvidia technology licensing deal, while financially massive, introduces strategic uncertainty about where Groq's LPU roadmap goes from here.

For the workloads Groq supports, it remains the fastest option available. The official MCP tooling is the most complete in the inference provider category. The free tier is the most accessible. The TTFT is the lowest.

If your workload fits Groq's catalog, it belongs in your evaluation. If it does not, the catalog limitation is disqualifying — and no amount of speed advantage on Llama 3.3 70B compensates for a model not being available.

**Rating: 4/5** — best-in-class inference speed on supported models, excellent MCP ecosystem, and meaningful enterprise compliance. Held back by a narrow catalog, no fine-tuning, and strategic uncertainty following the Nvidia technology licensing deal.
