---
title: "DeepSeek Review: The $6M Training Claim That Rattled Nvidia and Rewrote AI Economics"
date: 2026-05-09
description: "DeepSeek is a Chinese AI lab that trained V3 and R1 for a fraction of what Western labs spend, open-sourced both models under MIT license, and briefly sent Nvidia's stock down 17% in a single day. We examine the technology, the economics, the privacy concerns, and what it actually means for teams considering using these models."
tags: ["inference", "open-source", "llm", "reasoning", "review", "china", "moe"]
categories: ["reviews"]
rating: 3
author: "ChatForest"
---

On January 20, 2025, DeepSeek released R1 — a reasoning model they claimed had been trained for roughly $6 million that matched OpenAI's o1 on multiple benchmarks. The DeepSeek app went to #1 on the US App Store. One week later, Nvidia stock dropped approximately 17% in a single trading session, erasing an estimated $593 billion in market capitalization. No AI company announcement had caused that kind of ripple since the original ChatGPT launch.

The question worth asking is not whether DeepSeek's models are impressive — they clearly are. The question is: **who should actually use them, and how?**

---

## The Origin: A Quant Hedge Fund That Built an AI Lab

DeepSeek's backstory is genuinely unusual in the AI landscape, which skews heavily toward researchers-turned-entrepreneurs or ex-Google/Meta engineers.

**Liang Wenfeng** founded High-Flyer (幻方科技) in 2015 in Hangzhou, China. High-Flyer is a quantitative hedge fund — one of China's largest and most successful, reportedly managing tens of billions of yuan in assets. The fund's edge was systematic, data-driven trading using statistical and machine learning models. Liang (born 1985, Shantou, Guangdong; studied electrical engineering at Zhejiang University) built a firm that was profitable not through fundamental analysis but through compute-intensive pattern recognition on market data.

That background matters because it explains how DeepSeek was funded and how it operates. High-Flyer is the parent company and primary financial backer. There was no venture capital round, no Andreessen Horowitz term sheet, no pitch deck. The lab is an extension of a profitable private firm — one that was already investing heavily in GPU infrastructure and machine learning research for its own trading operations.

The GPU stockpile is central to the DeepSeek story. Before US export controls tightened in late 2022 and again in late 2023, High-Flyer reportedly acquired approximately **10,000 Nvidia A100 GPUs**. When the A100 was added to the US export control list, that stockpile became a strategic asset. DeepSeek did not have access to the latest H100s in the same volume that Western labs were deploying — and that constraint drove the technical innovations that made the models globally significant.

DeepSeek as a standalone AI lab was formally constituted in **late 2023**, operating under the High-Flyer umbrella with a reported team of several hundred researchers. Liang Wenfeng rarely gives interviews and does not appear on the conference circuit. The lab publishes detailed technical reports, open-sources model weights, and lets the work speak for itself.

---

## The Model Lineage

DeepSeek has released models at a pace that surprised the Western AI community, which had not been paying close attention to Chinese AI research output.

| Model | Release | Architecture | Parameters |
|-------|---------|-------------|------------|
| DeepSeek-Coder | Nov 2023 | Dense transformer | 1B–33B |
| DeepSeek-V1 | Jan 2024 | MoE | 67B total / 7B active |
| DeepSeek-V2 | May 2024 | MoE + MLA | 236B total / 21B active |
| DeepSeek-V2.5 | Sep 2024 | MoE + MLA | 236B total / 21B active |
| DeepSeek-V3 | Dec 26, 2024 | MoE + MLA + MTP | 671B total / 37B active |
| DeepSeek-R1 | Jan 20, 2025 | V3 backbone + RL reasoning | 671B total / 37B active |
| DeepSeek-V3-0324 | Mar 24, 2025 | Updated V3 | 671B total / 37B active |

The trajectory from V1 to V3 in roughly twelve months is striking. Each generation introduced architectural improvements that reduced compute requirements per quality point — not just incremental model scaling.

---

## The V3 Training Cost Claim: What the $5.576M Actually Means

DeepSeek's technical report for V3 claimed training the model required **2.788 million H800 GPU-hours**, at a rental cost of approximately **$2 per H800-hour**, totaling roughly **$5.576 million**. This number was immediately contested and requires careful interpretation.

**What the figure includes:** The final pre-training run on the 671B model, executed at high efficiency thanks to the architectural optimizations described below.

**What the figure excludes:**
- Research and experimentation costs (ablations, failed runs, hyperparameter searches)
- The cost of building and validating the training infrastructure
- Post-training (RLHF, reinforcement learning for R1)
- The embedded cost of the A100 hardware High-Flyer already owned
- Salaries, data acquisition, evaluation infrastructure

Western AI researchers pointed out that achieving $5.576M in final training costs presupposes enormous prior investment in research and tooling. Anthropic's Dario Amodei estimated that replicating V3's results from scratch — including all the prerequisite research — would cost hundreds of millions. The $5.576M figure is accurate as stated but describes the final production run of a well-optimized pipeline built on years of research, not the total cost of producing a comparable model from a standing start.

That said, even the narrowly-defined number is significant. V3's final training cost is meaningfully lower than comparable Western models at similar capability levels, and the architectural choices that made it possible are real and reproducible.

---

## The Technical Innovations That Matter

DeepSeek's competitive moat isn't cheaper hardware or more data — it's a set of architectural innovations that reduce compute requirements without sacrificing quality. Three are worth understanding.

### Multi-Head Latent Attention (MLA)

Standard transformer attention requires storing a key-value (KV) cache that scales linearly with sequence length and number of attention heads. For very long contexts, this cache becomes the primary memory bottleneck. MLA, introduced in V2, compresses the KV cache by projecting keys and values into a **low-rank latent space**. DeepSeek claims approximately **93% reduction in KV cache size** compared to standard multi-head attention, enabling much longer contexts on the same hardware.

This is not a trick or approximation — it's a mathematically equivalent representation that reduces memory without losing attention expressivity. Several Western labs subsequently published research validating the approach.

### DeepSeekMoE: Fine-Grained Mixture of Experts

Standard MoE models (like Mixtral) route tokens to a small number of large expert networks. DeepSeekMoE uses a much finer-grained approach: many smaller experts, one shared expert that processes every token plus a larger set of routed specialists. The 671B V3 model has 256 routed experts and 1 shared expert, with each token activating approximately **37B parameters** out of 671B total.

The key advantage: finer granularity allows each expert to specialize more narrowly, improving routing efficiency. The shared expert prevents common patterns from being fragmented across routed specialists.

### Multi-Token Prediction (MTP)

Standard language models predict one token at a time. V3 was trained with an auxiliary loss requiring the model to predict **two additional future tokens** simultaneously. This changes the gradient signal during training — the model receives information about longer-range dependencies earlier in training. The technique, borrowed from recent research on speculative decoding and draft models, reportedly accelerated training convergence.

### FP8 Mixed Precision Training

V3 was trained with **FP8 precision** (8-bit floating point) for most operations, with selective higher precision for numerically sensitive operations. H800 GPUs support FP8 natively; the challenge is numerical stability. DeepSeek's engineers published a detailed account of which operations required higher precision and how they managed the stability issues — a practical engineering contribution that enabled significant memory and compute savings.

---

## DeepSeek-R1: The Reasoning Breakthrough

R1 is structurally different from V3 and from OpenAI's o1 in one important respect: how the reasoning capability was obtained.

OpenAI has been opaque about o1's training process. The dominant assumption is that o1 was trained on large amounts of human-curated chain-of-thought data with sophisticated RLHF.

DeepSeek published R1's training process in detail. The core innovation is **R1-Zero**: a model trained *purely through reinforcement learning* with only rule-based rewards (correctness on math problems, format adherence) and **no supervised fine-tuning on human reasoning examples**. R1-Zero developed chain-of-thought reasoning spontaneously as a strategy to maximize the reward signal. The model independently discovered that showing its work improved its answers.

The final R1 model refined R1-Zero through cold-start SFT and additional RL stages, but the demonstration that robust reasoning could emerge from RL alone — without massive human-generated chain-of-thought data — was the conceptually significant finding.

**R1 benchmark results (DeepSeek's own reporting, January 2025):**
- AIME 2024: 79.8% pass@1 (vs. o1-2024-12-17 at 79.2%)
- MATH-500: 97.3% (vs. o1 at 96.4%)
- Codeforces: 96.3rd percentile (vs. o1 at 96.6th percentile)
- GPQA Diamond: 71.5% (vs. o1 at 75.7%)
- SWE-Bench Verified: 49.2%

These figures are self-reported. Independent evaluations on Chatbot Arena and other third-party benchmarks generally confirmed that R1 was competitive with o1 on mathematical reasoning, somewhat weaker on general knowledge and writing quality, and significantly ahead on cost per token.

---

## Pricing

DeepSeek's API pricing is among the lowest in the industry — roughly 20–50x cheaper than comparable OpenAI or Anthropic models.

| Model | Input (per 1M tokens) | Output (per 1M tokens) | Cache Hit Input |
|-------|----------------------|------------------------|-----------------|
| DeepSeek-V3 | $0.27 | $1.10 | $0.07 |
| DeepSeek-R1 | $0.55 | $2.19 | $0.14 |

Context window: 64K tokens for both models via the API (full 128K context available for some use cases; the technical architecture supports longer contexts).

Comparison: GPT-4o at $2.50/$10.00 per million tokens is roughly 9x more expensive on input. OpenAI o1 at $15.00/$60.00 per million tokens is roughly 27x more expensive on R1-equivalent tasks.

These prices apply to **DeepSeek's own API** (api.deepseek.com). Third-party providers (Together AI, Fireworks AI, Hyperbolic) offer DeepSeek model hosting at varying price points, typically with better latency than DeepSeek's own API for Western users.

---

## The Privacy and Data Sovereignty Problem

This is the section that matters most for any team evaluating DeepSeek for professional use.

**Using DeepSeek's cloud API means sending data to servers in China.** DeepSeek's privacy policy acknowledges that data may be stored and processed in China, and Chinese law applies. China's **National Intelligence Law (Article 7, 2017)** requires organizations and citizens to "support, assist, and cooperate with national intelligence work." This is not hypothetical: it is a structural legal requirement with no carve-out for foreign customer data.

This concern has produced concrete regulatory responses:

- **Italy** (January 2025): Data protection regulator ordered DeepSeek to block access for Italian users pending investigation
- **South Korea**: Privacy watchdog launched an investigation
- **Australia**: Government agencies warned against using DeepSeek on government systems
- **United States**: Multiple states (Texas, Virginia, New York, and others) banned DeepSeek on government-issued devices; the US Navy issued a similar ban; legislation was introduced in Congress to restrict federal use

For **regulated industries** — healthcare (HIPAA), financial services (SOC 2, FCA/SEC requirements), legal (attorney-client privilege, data residency requirements), defense contractors — using the DeepSeek cloud API is essentially off the table for production workloads involving sensitive data.

**Censorship limitations** are a separate issue. DeepSeek's models, when accessed via DeepSeek's own API, decline to discuss:

- The 1989 Tiananmen Square protests
- Taiwan's independence status
- Xinjiang internment camps
- Tibet
- Criticism of Xi Jinping or CCP leadership
- Other topics sensitive to Chinese government

This is enforced at the API level for cloud usage. The censorship does not apply when running the open-weight models self-hosted — the weights themselves do not have hardcoded refusals for these topics in the same way. However, the training data composition and RLHF process may still produce models with subtle biases that reward testers would not encounter in normal use.

For many use cases these limitations are irrelevant. A developer building a coding assistant or a math tutoring app doesn't care about Tiananmen. But for teams using AI to monitor geopolitical news, analyze policy, or produce internationally neutral research, it matters.

---

## The Self-Hosting Option: Why It Changes the Equation

The MIT license on V3 and R1 is not marketing. These are genuinely open weights with no commercial restrictions.

Self-hosting V3 (671B parameters) requires significant infrastructure. In FP4 quantization, the full model fits on approximately 8 × H100 80GB GPUs. At FP8, roughly 4–6 H100s are needed depending on batching requirements. For teams with on-premise GPU infrastructure, or with cloud VPC arrangements that satisfy data residency requirements, self-hosting removes essentially all the data sovereignty concerns.

The ecosystem support is extensive:

- **Ollama**: Supports DeepSeek-R1 in various sizes (distill variants from 1.5B to 70B, plus the full 671B via API mode)
- **vLLM**: Full V3 and R1 support with optimized serving
- **Hugging Face**: Complete model weights for V3 and R1, including all intermediate checkpoints
- **llama.cpp**: CPU-accessible smaller distill variants (R1 distill in 7B, 14B, 32B sizes)

The distill variants deserve special mention. DeepSeek released smaller models (1.5B to 70B) distilled from R1 that retain substantial reasoning capability while running on consumer hardware. DeepSeek-R1-Distill-7B runs on a single consumer GPU with 12GB VRAM and outperforms GPT-3.5 on many reasoning tasks. For teams experimenting with local AI, these are genuinely useful.

---

## Competitive Context: What DeepSeek Actually Disrupted

The January 2025 market reaction — Nvidia down 17%, AI infrastructure stocks broadly lower — was partly rational and partly panic. The rational part: if comparable model quality can be achieved with significantly fewer GPUs and smarter software, the trajectory of GPU demand growth might be lower than analysts projected. The panic part: DeepSeek's approach requires *some* GPUs, just fewer, and inference demand for any capable model is still GPU-bound.

What DeepSeek actually demonstrated:

1. **Algorithmic efficiency is underweighted.** The US AI industry had been assuming that more compute + more data = better results, with diminishing returns manageable through scale. DeepSeek showed that architectural improvements could substitute substantially for raw compute.

2. **Export controls have an unintended consequence.** Constrained from buying H100s at scale, Chinese AI researchers had strong incentive to find ways to do more with less. The constraint produced innovation. Whether the US export controls remain strategic given this outcome is now actively debated in policy circles.

3. **Open-source can match closed frontier models.** Prior to R1, the conventional wisdom was that open-source models lagged closed models by 6–12 months and one to two capability tiers. R1 closed that gap to near-zero on specific benchmarks. Meta's Llama 4 and subsequent releases have also improved, but DeepSeek forced the pace.

4. **Chinese AI research is serious.** Industry observers who had been dismissing Chinese AI labs as primarily derivative of Western research had to revise their assessments. DeepSeek's technical reports — MLA, the MoE architecture, the R1 RL training methodology — are genuine research contributions, not reproductions.

---

## Who DeepSeek Is For

**Strong use cases:**
- Developers and researchers who can self-host or use third-party US-based hosting
- High-volume consumer applications where cost per token is the primary constraint
- Mathematical reasoning and coding workloads (R1's strongest domains)
- Organizations experimenting with open-source AI infrastructure
- Teams that want to understand frontier model capabilities without API lock-in

**Poor fit:**
- Any organization handling data subject to HIPAA, GDPR (for data to China), FERPA, or SOC 2 requirements — unless self-hosting
- Organizations whose workflows require geopolitical analysis or content that conflicts with Chinese government positions
- Teams requiring enterprise SLAs, dedicated support, or compliance documentation
- Production workloads that need consistent API uptime (DeepSeek's own API has had reliability issues during peak demand)

---

## The Bottom Line

DeepSeek is a genuine technical achievement and one of the more important stories in AI's recent history. The training cost claims require context, but the architectural innovations that made them possible are real, reproducible, and have already influenced how Western labs are approaching model design. R1's RL-only reasoning emergence is conceptually significant independent of whether you ever use the model.

The business model is unusual: a profitable quant hedge fund subsidizing an open-source AI lab with no venture investors and no clear near-term monetization path. This creates an interesting set of incentives — DeepSeek has no pressure to monetize quickly, can price the API at cost or below cost, and can open-source freely without investor concern about giving away the company's only asset. The downside is that there is no enterprise support structure, no committed roadmap, and no SLA to hold them to.

**For Western developers building on self-hosted DeepSeek models**: this is a high-quality option with minimal downsides. The MIT license is genuine, the weights perform as benchmarked, and the ecosystem support (Ollama, vLLM, Hugging Face) is excellent.

**For anyone considering the DeepSeek cloud API**: the data sovereignty risk is real and not theoretical. Many teams will find it acceptable for low-sensitivity workloads. Regulated industries and government-adjacent organizations should not use it for anything they would not be comfortable sharing with an adversarial intelligence service.

**Rating: 3/5** — World-class open-source models that advanced the entire field; rating constrained by data sovereignty risks for cloud API use, censorship limitations, and absence of enterprise support infrastructure. Self-hosted deployments warrant a 4/5 reassessment.

---

*DeepSeek does not have an official enterprise partnership program, compliance certifications, or publicly disclosed revenue figures. This review is based on published technical reports, publicly available pricing, independent benchmark evaluations, and regulatory filings from January–May 2026. ChatForest researches AI platforms and tools; we do not have hands-on API access to the systems we review.*
