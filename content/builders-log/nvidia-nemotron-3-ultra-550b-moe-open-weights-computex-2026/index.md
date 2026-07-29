---
title: "Nemotron 3 Ultra: NVIDIA's 550B Open-Weights Model Is the Fastest US Frontier Model — and Still Behind China"
date: 2026-06-03
description: "NVIDIA announced Nemotron 3 Ultra at Computex 2026 — 550B total parameters, 55B active, hybrid Mamba-Transformer MoE. Available June 4 on HuggingFace, OpenRouter, and NIM. 300+ tokens/second. Leads all US open-weights models on intelligence benchmarks. Trails Kimi K2.6 from China."
og_description: "Nemotron 3 Ultra (550B/55B active MoE) launches June 4 on HuggingFace, OpenRouter, and NVIDIA NIM. 300+ tokens/sec, 1M token context, NVIDIA Open Model License (commercial OK). Tops US open-weights intelligence rankings but trails China's Kimi K2.6. Requires datacenter GPUs to self-host."
content_type: "Builder Guide"
card_description: "NVIDIA Nemotron 3 Ultra, announced June 1 at Computex 2026, is a 550B total parameter, 55B active MoE model with hybrid Mamba-2 Transformer architecture. Launches June 4 on HuggingFace, OpenRouter, and NVIDIA NIM. Claims 300+ tokens/second throughput, 5x faster inference than comparable open-weights models, 30% lower inference cost, and 1 million token context window. Tops US open-weights intelligence rankings (48 on Artificial Analysis index) but trails China's Kimi K2.6 (54). Requires A100/H100 datacenter infrastructure to self-host. NVIDIA Open Model License permits commercial use. Agentic post-training via RL is the key architectural differentiator."
tags: ["nvidia", "nemotron", "open-weights", "moe", "llm", "computex-2026", "inference", "agents", "open-source", "benchmarks"]
categories: ["builders-log"]
author: "ChatForest"
sources_audited: 2026-07-29
---

**At a glance:** Nemotron 3 Ultra, announced June 1, 2026 at NVIDIA's Computex 2026 keynote. 550B total parameters, 55B active per token (MoE). Hybrid Mamba-2 / Transformer / MoE architecture. 1 million token context. Launches June 4 on HuggingFace (open weights), OpenRouter, and NVIDIA NIM. Leads all US open-weights models on intelligence benchmarks. Trails China's Kimi K2.6. NVIDIA Open Model License: commercial use permitted. Requires datacenter infrastructure to self-host. Part of our **[Builder's Log](/builders-log/)**.

---

**Launch update (June 4, 2026):** Weights are live. Nemotron 3 Ultra is available on HuggingFace, OpenRouter, ModelScope, and NVIDIA NIM as of June 4 ([NVIDIA Technical Blog](https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/)). Thirteen early adopters confirmed: Accenture, Cadence, CrowdStrike, Cursor, Deloitte, EY, Oracle Cloud Infrastructure, Palantir, Perplexity, ServiceNow, Siemens, Synopsys, and Zoom ([NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-debuts-nemotron-3-family-of-open-models)). Ultra pricing on OpenRouter has not yet been indexed publicly — check [openrouter.ai/nvidia](https://openrouter.ai/nvidia) directly for current rates. Everything below was accurate at launch; we will update with confirmed pricing once it is stable.

---

Jensen Huang announced Nemotron 3 Ultra from the stage in Taipei on June 1, 2026 ([Computex 2026 keynote coverage](https://www.tomshardware.com/tech-industry/nvidia-keynote-computex-2026-gtc-taipei-where-to-watch)). "Open innovation is the foundation of AI progress," he said. "With Nemotron, we're transforming advanced AI into an open platform that gives developers the transparency and efficiency they need to build agentic systems at scale." ([NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-debuts-nemotron-3-family-of-open-models))

That framing — agentic, open, at scale — is precise. Nemotron 3 Ultra is not competing on being the smartest model in the world. It is competing on being the fastest open frontier model with a US data residency story, commercial licensing, and a published training recipe.

On speed, the claim is strong. On intelligence ranking, it leads every US open-weights model and trails the Chinese frontier. That is the honest summary.

---

## Architecture

Nemotron 3 Ultra uses what NVIDIA's technical report calls a **hybrid Mamba-Attention Mixture-of-Experts architecture** ([NVIDIA Nemotron 3 Ultra Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf), [NVIDIA Nemotron developer page](https://developer.nvidia.com/nemotron)). Three components work together:

- **Mamba-2 state-space layers:** Efficient sequence processing that scales better than attention for very long contexts. This is the primary engine for handling the 1-million-token context window.
- **Transformer attention blocks:** Retained for tasks where attention mechanisms outperform state-space models.
- **Mixture-of-Experts routing (LatentMoE):** 550B total parameters, 55B activated per token — a 10:1 sparsity ratio, meaning roughly 90% of parameters are dormant on any given forward pass ([NVIDIA Nemotron 3 Ultra Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf)).

The combination lets Ultra maintain frontier-class quality while dramatically reducing the compute cost per token compared to a dense 550B model.

**Multi-Token Prediction (MTP):** The model is trained with two shared-weight MTP heads to predict multiple future tokens simultaneously, accelerating inference via speculative decoding ([NVIDIA Nemotron 3 Ultra Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf)).

**Training precision:** NVFP4 (NVIDIA's 4-bit floating point format, native to Blackwell architecture). NVIDIA's technical report states the final 15% of the network (16 of 108 layers) — Mamba output projections, latent projections, QKV/attention projections, MTP layers, and embedding layers — was kept in higher precision, meaning roughly 85% of layers trained in NVFP4 ([NVIDIA Nemotron 3 Ultra Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf)).

**Post-training:** Supervised fine-tuning, reinforcement learning with verifiable reward (RLVR), and multi-teacher on-policy distillation (MOPD) across interactive agentic environments, targeting multi-step tool use, terminal operation, and software-engineering task execution ([NVIDIA Nemotron 3 Ultra Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf)). NVIDIA positions Ultra as its first open model built around this agentic-loop training rather than single-turn conversation quality ([NVIDIA Technical Blog](https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/)).

---

## Benchmarks: What the Numbers Actually Show

On the **[Artificial Analysis Intelligence Index](https://artificialanalysis.ai/articles/nvidia-nemotron-3-ultra-launch-announced)** (as of June 2026):

| Model | Intelligence Index |
|---|---|
| Kimi K2.6 (Moonshot AI, China) | 54 |
| **Nemotron 3 Ultra (NVIDIA, US)** | **48** |
| Gemma 4 31B (Google) | 39 |
| Nemotron 3 Super 120B (NVIDIA) | 36 |
| GPT-oss-120B (OpenAI) | 33 |

Nemotron 3 Ultra is the top-ranked US open-weights model. It is not the top-ranked open-weights model overall. Kimi K2.6 leads by a margin of 6 points (54 vs 48). Decrypt's headline said it plainly: "[Nvidia Releases Its Best Open AI Model Yet — But Still Lags Behind China](https://decrypt.co/369689/nvidia-open-ai-model-nemotron-3-ultra)."

**Benchmarks reported by NVIDIA's technical report** ([NVIDIA Nemotron 3 Ultra Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf)) use a different suite than older-generation LLM benchmarks like HumanEval or MMLU: Terminal-Bench 2.1, SWE-Bench Verified and Multilingual, TauBench V3, GDPVal, ProfBench, PinchBench, IOI 2025, and RULER at 1M context. NVIDIA's technical blog reports Ultra scores **95% on RULER at 1M tokens** and SWE-Bench Verified scores in the 65–70.4% range depending on harness ([NVIDIA Technical Blog](https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/)). NVIDIA describes the model as achieving "on-par accuracy" with other state-of-the-art open LLMs on this suite while running substantially faster ([NVIDIA Nemotron 3 Ultra Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf)).

**Speed:** On a pre-release DeepInfra endpoint, Artificial Analysis recorded over 300 output tokens/second; it notes peer Chinese-lab open models (DeepSeek, Kimi) are typically served at 50–100 tokens/second in the market today ([Artificial Analysis](https://artificialanalysis.ai/articles/nvidia-nemotron-3-ultra-launch-announced), [Decrypt](https://decrypt.co/369689/nvidia-open-ai-model-nemotron-3-ultra)). NVIDIA's own technical report measured 5.9x, 4.8x, and 1.6x higher inference throughput than GLM-5.1-754B-A40B, Kimi-K2.6-1T-A32B, and Qwen-3.5-397B-17B respectively, on an 8K-input/64K-output setting ([NVIDIA Nemotron 3 Ultra Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf)). Separately, NVIDIA's technical blog claims Ultra lowers the cost of completing agentic tasks by up to 30%, based on token-efficiency comparisons on SWE-bench and Terminal-Bench 2.0 ([NVIDIA Technical Blog](https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/)).

**What matters for builders:** The speed advantage is real and substantial in the context of US-hosted open-weights models. The intelligence gap versus Kimi K2.6 is also real. If raw reasoning performance is the primary constraint, Ultra is not the frontier. If throughput, latency, and US deployment options are the primary constraints, Ultra is the current leader.

---

## Context Window

**1 million tokens.** NVIDIA's technical blog reports a 95% RULER score at 1M tokens as the supporting benchmark ([NVIDIA Technical Blog](https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/)). RULER (Realistic Uniform Long-context Retrieval) tests the model's ability to retrieve specific information from very long contexts — a better signal than simple "accepts N tokens" claims.

A 95% score at 1M tokens, if it holds under third-party evaluation, would be a meaningful long-context capability.

---

## Availability and Licensing

**Launch date:** June 4, 2026

**Where to access:**
- **HuggingFace:** Open weights download (BF16 and NVFP4 quantization formats)
- **ModelScope:** Parallel to HuggingFace
- **OpenRouter:** Vendor-neutral API access
- **NVIDIA NIM:** Hosted microservice at build.nvidia.com — lowest-friction path for most builders

NVIDIA is also releasing the training recipes, data toolchain, and evaluation scripts alongside the weights ([NVIDIA Nemotron 3 Ultra Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf)).

**License:** [NVIDIA Nemotron Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license). Key terms:
- Commercial use permitted, without royalty fees
- Modification and distribution of derivative works permitted
- No attribution required in model outputs, but a "Licensed by NVIDIA Corporation under the NVIDIA Nemotron Model License" notice must accompany any distributed derivative work
- Includes a patent-litigation termination clause not found in Apache 2.0/MIT — read the full license before packaging for SaaS redistribution

For most builder use cases (calling the API, running on your own infrastructure, fine-tuning for internal products), the license is permissive enough to proceed without legal complexity. For redistribution or embedding in a product sold to others, verify the specific terms.

---

## Hardware Requirements for Self-Hosting

This model cannot run on consumer hardware. NVIDIA's own NIM deployment reference lists minimum hardware as 4x GB200, 4x B200, 4x GB300, 4x B300, or 8x H100 GPUs, with a single-node 4x B200 configuration recommended as sufficient to fit the NVFP4 weights plus KV cache with headroom ([NVIDIA NIM deployment reference](https://docs.api.nvidia.com/nim/reference/nvidia-nemotron-3-ultra-550b-a55b)).

Budget for datacenter-class infrastructure cost before planning a self-hosted deployment.

**For most builders:** NVIDIA NIM or OpenRouter API access is the practical starting point. The self-hosted path is for organizations with existing DGX infrastructure or a specific data residency requirement that precludes API usage.

---

## Fine-Tuning

NVIDIA is releasing a **Nemotron 3 Ultra 550B-A55B Base** checkpoint — the pre-instruction-tuned weights, alongside the post-trained and NVFP4-quantized checkpoints — as a starting point for custom fine-tuning and RL post-training pipelines ([NVIDIA Nemotron 3 Ultra Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf)).

The toolchain NVIDIA describes in its technical report includes reinforcement learning and distillation infrastructure (MOPD, RLVR), a Nemo Data Designer synthetic-data pipeline, and NVFP4 training recipes ([NVIDIA Nemotron 3 Ultra Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf); training recipes and code at [github.com/NVIDIA-NeMo/Nemotron](https://github.com/NVIDIA-NeMo/Nemotron)).

If you are building a specialized agent — one that operates in a specific domain, follows domain-specific protocols, or needs to behave differently from a general assistant — the Ultra Base checkpoint plus NVIDIA's published RL recipe is the intended path.

Community fine-tuning tooling, including [Unsloth](https://unsloth.ai/docs/models/nemotron-3-ultra), already documents support for running and fine-tuning Nemotron 3 Ultra locally ([NVIDIA Nemotron developer page](https://developer.nvidia.com/nemotron)).

---

## How Ultra Fits in the Nemotron 3 Family

The Nemotron 3 family released in 2026 covers a range of size/speed trade-offs:

| Model | Total Params | Active Params | Notes |
|---|---|---|---|
| Nemotron 3 Nano Omni | 30B | 3B | Multimodal (text, image, audio, video) ([NVIDIA Blog](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/)) |
| Nemotron 3 Super | 120B | 12B | Mid-tier; ~$0.085–0.09/1M input on OpenRouter ([OpenRouter pricing](https://openrouter.ai/nvidia/nemotron-3-super-120b-a12b/pricing)) |
| Nemotron 3 Ultra | 550B | 55B | Frontier-class reasoning; datacenter only |

For most builders, the decision is whether Ultra's intelligence gain over Super justifies the infrastructure cost. Ultra pricing was not confirmed before the June 4 launch — expect it to be significantly higher than Super's.

If the task is multi-step agentic reasoning, complex code generation, or deep analytical tasks, Ultra is the right tier. If the task is straightforward content generation, classification, or moderate-complexity reasoning, Super may deliver adequate quality at lower cost.

---

## The Honest Builder's Assessment

**Choose Nemotron 3 Ultra if:**
- You need the fastest US-jurisdiction open-weights frontier model
- Your agentic pipeline benefits from RL-tuned multi-step reasoning
- You require commercial-friendly open weights with a published training recipe
- You have or can access datacenter GPU infrastructure (or are comfortable with NIM/OpenRouter API costs)
- Long context (up to 1M tokens) is a meaningful requirement

**Do not choose Nemotron 3 Ultra if:**
- Maximum reasoning quality is the primary criterion — Kimi K2.6 leads on benchmarks
- Multilingual capability, especially in Asian languages, is critical — Nemotron 3 does not market multilingual performance as a differentiator; evaluate dedicated multilingual models for that requirement
- You need to self-host without datacenter infrastructure
- You are building multimodal applications — use Nano Omni instead
- Budget is the primary constraint — wait for confirmed Ultra pricing before committing

**The benchmark gap with Kimi K2.6 is real.** 48 vs 54 on the Artificial Analysis Intelligence Index is a meaningful difference, not a rounding error. For builders where intelligence index translates directly to task performance, evaluate both. For builders where throughput, latency, or US data residency are the binding constraints, Ultra is currently the best available option.

---

## What to Watch

- **June 4:** Weights drop on HuggingFace; NIM endpoint goes live; OpenRouter pricing confirmed
- **Community benchmarks:** Third-party reproduction of the 300+ tokens/second and RULER scores will be available within days of the weight release
- **Pricing disclosure:** Ultra pricing on OpenRouter and NIM will determine cost-per-task economics compared to closed frontier models
- **Community fine-tuning support:** watch for broader framework support beyond Unsloth's initial coverage for the NVFP4 weight format
- **Kimi K2.6 availability:** If Moonshot AI opens a US-region API or OSS release improves, the intelligence gap becomes the primary competitive question

---

*Nemotron 3 Ultra was announced by Jensen Huang at NVIDIA's Computex 2026 keynote in Taipei, June 1, 2026. Sources: [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-debuts-nemotron-3-family-of-open-models), [Artificial Analysis](https://artificialanalysis.ai/articles/nvidia-nemotron-3-ultra-launch-announced), [Decrypt](https://decrypt.co/369689/nvidia-open-ai-model-nemotron-3-ultra), [NVIDIA Nemotron Developer Page](https://developer.nvidia.com/nemotron).*
