---
title: "Cerebras — Wafer-Scale LLM Inference (2026 Review)"
date: 2026-05-07T15:30:00+09:00
description: "Cerebras reviewed: WSE-3 wafer-scale chip delivers 969 tokens/sec on Llama 3.1 405B — fastest ever for a 400B+ model. OpenAI-compatible API, 1M free tokens/day, IPO in progress at $22–25B. Rating: 4.5/5."
og_description: "Cerebras (cerebras.ai) reviewed: the Wafer-Scale Engine 3 (WSE-3) puts an entire 300mm silicon wafer to work as one chip — 4 trillion transistors, 900,000 AI cores, 44 GB of on-chip SRAM, and 21 petabytes/second of internal bandwidth. The result: 969 tokens/second on Llama 3.1 405B, the fastest throughput ever reported for a 400B+ model. ~3,000 tokens/second on GPT-OSS 120B. OpenAI-compatible cloud API with 1 million free tokens per day. OpenAI signed a $20B multi-year compute deal; Cerebras now powers GPT-OSS-Spark, OpenAI's first production model not running on NVIDIA hardware. $510M revenue in 2025, profitable. IPO filed April 2026 at $22–25B target valuation. Revenue concentration risk: 86% of 2025 revenue from two UAE entities. Rating: 4.5/5."
card_description: "Cerebras (cerebras.ai) is a cloud LLM inference API and hardware company built around the Wafer-Scale Engine — a chip the size of an entire silicon wafer. **4 trillion transistors. 44 GB on-chip SRAM. 21 PB/s internal bandwidth.** The WSE-3 delivers 969 tokens/second on Llama 3.1 405B (fastest ever for a 400B+ model), ~3,000 tokens/sec on GPT-OSS 120B, and ~2,500 tokens/sec on Llama 3.3 70B. OpenAI-compatible API; drop-in for any OpenAI integration. **1 million free tokens per day** — the most generous free tier of any inference API. Models: Llama 4 Scout/Maverick, Llama 3.3 70B, GPT-OSS 120B, Qwen3 32B, Qwen3 235B. **OpenAI signed a $20B compute deal** — Cerebras now powers GPT-OSS-Spark, OpenAI's first production model not running on NVIDIA. Revenue: $510M in 2025, profitable. IPO roadshow launched May 2026, targeting $22–25B valuation. Revenue concentrated: 86% from two UAE entities (MBZUAI, G42). Part of our **Developer Tools** category. Rating: 4.5/5."
last_refreshed: 2026-05-07
categories: ["/categories/developer-tools/"]
---

In February 2026, OpenAI launched GPT-OSS-Spark — a faster, cheaper version of Codex for developers. It ran at over 1,000 tokens per second. It was the first production OpenAI model not running on NVIDIA hardware.

It ran on Cerebras.

That a company founded in 2016 around a chip the size of a dinner plate had become the compute substrate for OpenAI's own inference workloads is a statement about how seriously the industry takes the performance numbers coming out of Sunnyvale. Cerebras's wafer-scale silicon produces throughput figures that GPU clusters cannot approach without marshaling dozens of H100s in tight coordination.

The company is now on the cusp of an IPO. $510 million in revenue in 2025. Profitable. Part of our **[Developer Tools category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Product** | [Cerebras Inference API](https://inference.cerebras.ai/) + CS-3 hardware |
| **Hardware** | WSE-3 (Wafer-Scale Engine 3) |
| **Founded** | 2016 |
| **CEO** | Andrew Feldman |
| **Funding** | $1.1B Series G (Sept 2025); $8.1B post-money valuation |
| **Revenue** | $510M (2025); $87.9M net income (profitable) |
| **IPO** | S-1 filed April 17, 2026; roadshow launched May 2026; target valuation $22–25B |
| **OpenAI deal** | $20B multi-year compute agreement; $1B loan from OpenAI |
| **API** | OpenAI-compatible (`api.inference.cerebras.ai/v1`) |
| **Free tier** | 1,000,000 tokens/day (no credit card required) |
| **GitHub** | [github.com/Cerebras](https://github.com/Cerebras) |

---

## The Core Technology: One Chip, One Wafer

GPU systems are built from chiplets — discrete silicon dies wired together on a package, then connected to other dies via NVLink, InfiniBand, or PCIe. Each interconnect boundary is a latency and bandwidth bottleneck. When you run inference on a 70B-parameter model across a GPU cluster, weights and activations travel across those boundaries constantly. The interconnect is often the limiting factor, not the compute cores.

Cerebras's answer: eliminate the boundary.

The Wafer-Scale Engine takes a standard 300mm silicon wafer — the same substrate used to make individual chips — and instead of dicing it into dozens of separate dies, treats the entire wafer as one processor. The WSE-3 is the third generation of this approach:

| WSE-3 Specification | Value |
|---|---|
| Transistors | 4 trillion |
| AI compute cores | 900,000 |
| On-chip SRAM | 44 GB |
| On-chip memory bandwidth | 21 PB/s (21,000 TB/s) |
| Compute performance | 125 PFLOPS |
| Process node | TSMC 5nm |
| Physical dimensions | ~215mm × 215mm |

For comparison, a single NVIDIA H100 GPU has roughly 80 GB of HBM at ~3.35 TB/s bandwidth. An H100 cluster of 16 GPUs delivers ~53 TB/s aggregate bandwidth — across multiple chips, boards, and cables, with all the coordination overhead that entails. The WSE-3's 21 PB/s of internal bandwidth is on one die, with zero inter-chip communication overhead for models that fit.

**The memory constraint:** The on-chip SRAM cap of 44 GB is the primary architectural limitation. A Llama 3.3 70B model in FP16 requires approximately 140 GB — well beyond the WSE-3's on-chip capacity. Cerebras handles this with **weight streaming**: model weights are stored in external MemoryX DRAM banks and streamed to the wafer during inference. Weight streaming makes arbitrarily large models feasible, but introduces some dependency on external memory bandwidth that pure on-chip storage avoids. The CS-3 system — Cerebras's server unit — combines the WSE-3 wafer with MemoryX storage, SwarmX networking fabric for multi-node clusters, and a separate CPU preprocessing node (LSX).

---

## Performance: Real Numbers

Cerebras's headline benchmark is Llama 3.1 405B at **969 tokens per second** — a throughput figure no GPU cluster has matched for a model of that size without massive parallelism. At 405 billion parameters, GPU-based inference typically requires 8–16 H100s working in tight coordination. Cerebras achieves comparable or greater throughput with a different architectural trade-off.

| Model | Cerebras (tokens/sec) |
|---|---|
| GPT-OSS 120B | ~3,000 |
| Llama 3.3 70B | ~2,500 |
| Qwen3 235B | ~525 |
| Llama 3.1 405B | **969** (world record for 400B+ class) |
| Llama 4 Scout (multimodal) | varies by request |

Third-party independent tests confirm API throughput close to advertised figures. One developer documented 2,600 tokens/second on Llama 4 Scout in a public benchmark. For comparison, a well-tuned H100 server returns 100–300 tokens/second on a 70B model.

**Where the Cerebras advantage peaks:** large models. The bigger the model, the more pronounced the advantage over GPU inference — because GPU clusters must shard weights across more cards with more coordination overhead. Cerebras's weight streaming handles 405B as cleanly as a GPU handles 7B.

**Where Groq (now NVIDIA's LPU technology) still leads:** time-to-first-token (TTFT). Groq's LPU architecture was optimized for consistently sub-100ms first token responses — the metric that determines perceived responsiveness in chat and voice applications. Cerebras is fast, but TTFT consistency under concurrent load is Groq's historical differentiator. For batch processing, high-throughput pipelines, and document summarization — where TTFT matters less than total throughput — Cerebras is the stronger choice.

---

## The Inference API

Cerebras's cloud API lives at `api.inference.cerebras.ai/v1` and mirrors the OpenAI chat completions interface exactly. Base URL swap + API key is a complete migration from any OpenAI-based application.

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-cerebras-api-key",
    base_url="https://api.inference.cerebras.ai/v1"
)

response = client.chat.completions.create(
    model="llama-3.3-70b",
    messages=[{"role": "user", "content": "Explain weight streaming in one sentence."}]
)
```

The Cerebras Python SDK (`pip install cerebras-cloud-sdk`) wraps this with a slightly more ergonomic client object. Both approaches work; the OpenAI SDK path works for teams that want zero additional dependencies.

**Ecosystem integrations:** Vercel AI SDK has an official Cerebras provider (`@ai-sdk/cerebras`). Cloudflare AI Gateway supports Cerebras. Haystack, LlamaIndex, and Promptfoo all have native integrations. Any tool that routes to OpenAI-compatible endpoints works without modifications.

**Model catalog (May 2026):**

| Model | Context | Notes |
|---|---|---|
| Llama 4 Scout | 10M tokens | Multimodal, 17B active / 109B total MoE |
| Llama 4 Maverick | 1M tokens | 17B active / 400B total, 128 experts |
| Llama 3.3 70B | 128K | Strong instruction following |
| GPT-OSS 120B | 64K | OpenAI's open-weight model; powers ChatGPT features |
| Qwen3 32B | 64K | Alibaba's strong mid-size model |
| Qwen3 235B Instruct | 32K | Best open-weight reasoning in class |
| Qwen3 235B Thinking | 32K | Chain-of-thought mode |
| Qwen3 Coder 480B | 64K | Developer tier only |
| ZAI GLM-4.7 | varies | Multilingual |

The Llama 4 models are notable: Scout's 10-million-token context window handles entire codebases or book-length documents in a single request. Llama 3.1 8B is being deprecated May 27, 2026.

---

## Pricing

Cerebras's free tier is the most generous of any LLM inference API: **1,000,000 tokens per day, no credit card required**. Rate limits on free tier are 30 requests/minute; context windows are capped at 8,192 tokens per request even for models that support longer contexts. Enough for serious development; insufficient for production at scale.

Paid tiers unlock higher rate limits, full context windows, and access to larger models like Qwen3 Coder 480B. Per-token pricing ranges from roughly $0.60/million tokens (smaller models) to $6–$12/million tokens (405B+). Exact pricing is available at [cerebras.ai/pricing](https://cerebras.ai/pricing); models are priced individually.

The CS-3 hardware for on-premise deployment is not publicly priced. Community estimates from analyst discussions and developer forums place single-node pricing at approximately $2–3 million. Enterprise deployments typically involve multiple nodes plus the MemoryX and SwarmX components; cost runs into tens of millions for meaningful clusters.

---

## The OpenAI Partnership

On January 23, 2026, Cerebras began delivering compute to OpenAI under a multi-year contract. The deal, announced publicly in connection with Cerebras's April 2026 IPO filing, involves:

- Up to **750 MW of computing capacity** delivered to OpenAI through 2028
- Total contract value cited at over **$20 billion**
- A **$1 billion loan** from OpenAI to Cerebras at 6% annual interest to fund data center buildout
- OpenAI received warrants for 33.4 million shares of Cerebras non-voting Class N stock

On February 12, 2026, OpenAI launched GPT-OSS-Spark, running at over 1,000 tokens per second — the first OpenAI production model not running on NVIDIA hardware. It runs on Cerebras.

Separately, Amazon announced in March 2026 that Cerebras services would be available through AWS Marketplace, with Amazon agreeing to purchase approximately $270 million in Cerebras Class N stock.

These are not marketing partnerships. They are multibillion-dollar infrastructure commitments from the two companies that arguably matter most in AI deployment. Cerebras's technology was validated at the highest level the industry offers.

---

## The IPO

Cerebras filed its original S-1 in September 2024. CFIUS (the Committee on Foreign Investment in the United States) opened a national security review of minority investor G42's prior ties to Chinese technology firms. The IPO was withdrawn. CFIUS granted clearance on March 31, 2025, after G42 divested its Chinese investments and restructured its Cerebras stake to non-voting shares.

The company raised a $1.1 billion Series G in September 2025 at an $8.1 billion valuation, then refiled its S-1 on April 17, 2026, with materially stronger financials and the OpenAI deal prominently disclosed. Roadshow launched May 4, 2026. The target listing valuation is $22–25 billion, with some analyst estimates running higher.

Key financials from the S-1:
- **Revenue 2025:** $510M (+76% YoY)
- **Net income 2025:** $87.9M (profitable; compared to a $485M net loss in 2024)
- **Revenue concentration:** 86% from two UAE entities — MBZUAI (62%) and G42 (24%)

The revenue concentration is the most significant business risk disclosed. If either UAE relationship changes — due to geopolitical shifts, regulatory action, or commercial disagreement — Cerebras's financials would be severely affected. The S-1 flags this explicitly. The OpenAI and AWS deals represent meaningful diversification in progress, but the UAE concentration existed through all of 2025.

---

## Limitations

**Free tier context window cap.** 8,192 tokens per request on the free tier, regardless of model. Llama 4 Scout's 10M token context — one of the most compelling features in the catalog — requires a paid account to use at full depth.

**No fine-tuning on the public API.** You run Cerebras's deployed catalog. Custom model weights, LoRA adapters, or domain-specific fine-tunes are not supported for external users. If your production use case requires a fine-tuned model, you need either a different provider or CS-3 hardware of your own.

**Weight streaming complexity for very large models.** When model weights exceed 44 GB on-chip SRAM, Cerebras streams them from external MemoryX storage. This is engineering-invisible to API users, but it means Cerebras's architecture is not "all on-chip" for the models it most prominently benchmarks. The performance is still excellent; the architectural purity is not quite what the wafer-scale framing implies for 100B+ models.

**Hardware access requires millions of dollars.** CS-3 systems are not available for small teams. On-premise deployment is for national labs, enterprises, and governments with the budget to match. The cloud API is the practical access point for almost everyone.

**Revenue concentration risk.** This is a business risk, not a technical one, but it affects whether Cerebras continues as an independent provider five years from now. 86% of 2025 revenue from two entities in one country is a fragile revenue base. The IPO proceeds, the OpenAI deal, and the AWS relationship are all structural improvements — none of them resolved the concentration as of the filing date.

**No Apple Silicon support.** The WSE SDK does not target Apple hardware. Self-hosted Cerebras tooling requires Linux + NVIDIA or AMD GPU for the preprocessing and coordination components. Not relevant for cloud API users; relevant for teams exploring hybrid setups.

---

## vs. GPU-Based and Competing Inference Options

| | Cerebras | Groq (NVIDIA LPU) | vLLM (GPU) | SGLang (GPU) |
|---|---|---|---|---|
| **Best throughput** | ~3,000 TPS (120B) | ~2,800 TPS (9B) | 300–500 TPS | 300–500 TPS |
| **TTFT consistency** | Good | Excellent | Variable | Variable |
| **Large model advantage** | Yes — 405B at 969 TPS | Limited | Requires multi-GPU | Requires multi-GPU |
| **Custom models** | No | No | Yes | Yes |
| **Fine-tuning** | No | Enterprise only | Bring your own | Bring your own |
| **Free tier** | 1M tokens/day | Strict RPM limits | Self-hosted | Self-hosted |
| **OpenAI-compatible** | Yes | Yes | Yes | Yes |
| **On-premise hardware** | CS-3 (~$2–3M/unit) | GroqRack (millions) | Any GPU server | Any GPU server |
| **Data sovereignty** | Cloud only (API) | Cloud only (API) | Full control | Full control |
| **Provider status** | Independent (IPO 2026) | NVIDIA-owned (Dec 2025) | Open source | Open source |

Cerebras's strongest head-to-head is against Groq's LPU: for large model throughput, Cerebras wins by a wide margin. For TTFT under concurrent load with small models, Groq historically led. With Groq now operating under NVIDIA ownership and engineering uncertainty, Cerebras is effectively the remaining major independent competitor in the ultra-fast inference hardware category.

---

## Notable Production Users

- **OpenAI** — GPT-OSS-Spark, running in production to ChatGPT Pro users since February 2026
- **Argonne National Laboratory, Lawrence Livermore National Laboratory, Sandia National Laboratories** — US government AI research
- **GlaxoSmithKline** — epigenomics modeling
- **Mayo Clinic** — medical AI diagnostics
- **Government of Guyana** — MOU for up to 100 MW domestic AI data center
- **MBZUAI and G42** — UAE AI research (dominant revenue source through 2025)

---

## Who Should Use Cerebras

**Strong fit for:**
- Developers who need 1M free tokens/day without rate-limit headaches
- High-throughput inference pipelines where latency matters but TTFT is not the primary constraint
- Applications using large models (70B–400B+) where GPU alternatives require expensive multi-node clusters
- Any OpenAI-based application wanting drop-in speed improvement without code changes
- Teams that want an alternative to NVIDIA-ecosystem inference with strong business backing

**Weaker fit for:**
- Real-time voice or chat applications where sub-100ms TTFT is the primary UX requirement (consider Groq for TTFT-first workloads)
- Teams needing fine-tuned or custom model weights on a cloud API
- On-premise deployments without multi-million-dollar hardware budgets
- Projects requiring guaranteed uptime SLAs before the company's IPO settles

---

## Verdict

Cerebras built a genuinely unusual chip — large enough to be strange, fast enough to be impossible to ignore. The performance numbers are real, independently verified, and unmatched for large model throughput. OpenAI's decision to stake production inference on WSE-3 hardware is the most credible external validation available.

The business is strong: $510 million in revenue, profitable, an IPO in progress, and partnerships with OpenAI and Amazon that will diversify the revenue base. The one material weakness is concentration — 86% of current revenue from two UAE entities is a real structural fragility, and it will take several years of OpenAI and AWS delivery to meaningfully shift that ratio.

For developers: the free tier alone (1M tokens/day, no credit card) is worth signing up for. The API is clean, fully OpenAI-compatible, and fast. For teams running inference on 70B+ models at scale, Cerebras deserves a serious look.

**Rating: 4.5/5** — Best-in-class throughput for large models, powered by genuinely novel silicon. The OpenAI partnership and profitability represent significant business maturity. Half-point deduction for revenue concentration risk (86% UAE entities) and the API's constraint that no custom or fine-tuned models can be served — a ceiling that will limit advanced production use cases.
