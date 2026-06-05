# Nemotron 3 Ultra: NVIDIA's 550B Open-Weights Model Is the Fastest US Frontier Model — and Still Behind China

> NVIDIA announced Nemotron 3 Ultra at Computex 2026 — 550B total parameters, 55B active, hybrid Mamba-Transformer MoE. Available June 4 on HuggingFace, OpenRouter, and NIM. 300+ tokens/second. Leads all US open-weights models on intelligence benchmarks. Trails Kimi K2.6 from China.


**At a glance:** Nemotron 3 Ultra, announced June 1, 2026 at NVIDIA's Computex 2026 keynote. 550B total parameters, 55B active per token (MoE). Hybrid Mamba-2 / Transformer / MoE architecture. 1 million token context. Launches June 4 on HuggingFace (open weights), OpenRouter, and NVIDIA NIM. Leads all US open-weights models on intelligence benchmarks. Trails China's Kimi K2.6. NVIDIA Open Model License: commercial use permitted. Requires datacenter infrastructure to self-host. Part of our **[Builder's Log](/builders-log/)**.

---

**Launch update (June 4, 2026):** Weights are live. Nemotron 3 Ultra is available on HuggingFace, OpenRouter, ModelScope, and NVIDIA NIM as of June 4. Thirteen early adopters confirmed: Accenture, CrowdStrike, Palantir, Perplexity, and others. Ultra pricing on OpenRouter has not yet been indexed publicly — check [openrouter.ai/nvidia](https://openrouter.ai/nvidia) directly for current rates. Everything below was accurate at launch; we will update with confirmed pricing once it is stable.

---

Jensen Huang announced Nemotron 3 Ultra from the stage in Taipei. "Open innovation is the foundation of AI progress," he said. "With Nemotron, we're transforming advanced AI into an open platform that gives developers the transparency and efficiency they need to build agentic systems at scale."

That framing — agentic, open, at scale — is precise. Nemotron 3 Ultra is not competing on being the smartest model in the world. It is competing on being the fastest open frontier model with a US data residency story, commercial licensing, and a published training recipe.

On speed, the claim is strong. On intelligence ranking, it leads every US open-weights model and trails the Chinese frontier. That is the honest summary.

---

## Architecture

Nemotron 3 Ultra uses what NVIDIA calls a **Hybrid Latent MoE** architecture. Three components work together:

- **Mamba-2 state-space layers:** Efficient sequence processing that scales better than attention for very long contexts. This is the primary engine for handling the 1-million-token context window.
- **Transformer attention blocks:** Retained for tasks where attention mechanisms outperform state-space models.
- **Mixture-of-Experts routing:** 550B total parameters, 55B activated per token. 10:1 sparsity ratio; approximately 90% of parameters are dormant on any given forward pass.

The combination lets Ultra maintain frontier-class quality while dramatically reducing the compute cost per token compared to a dense 550B model. A dense model at this scale would require roughly 10x the compute per inference call.

**Multi-Token Prediction (MTP):** The model is trained to predict multiple future tokens simultaneously, not just the next one. This is one of the mechanisms behind the 300+ tokens/second throughput claim — the system generates multiple tokens per forward pass rather than one.

**Training precision:** NVFP4 (NVIDIA's 4-bit floating point format, native to Blackwell architecture). Approximately 85% of layers are NVFP4. Attention and projection layers are retained in BF16/MXFP8. This is designed specifically to maximize throughput on GB300 and Blackwell Ultra platforms.

**Post-training:** Reinforcement learning across interactive environments, specifically targeting multi-step agentic task execution. NVIDIA describes this as the differentiating factor: "the first open frontier model built for agents."

---

## Benchmarks: What the Numbers Actually Show

On the **Artificial Analysis Intelligence Index** (as of June 2026):

| Model | Intelligence Index |
|---|---|
| Kimi K2.6 (Moonshot AI, China) | 54 |
| **Nemotron 3 Ultra (NVIDIA, US)** | **48** |
| Gemma 4 31B (Google) | 39 |
| Nemotron 3 Super 120B (NVIDIA) | 36 |
| GPT-oss-120B (OpenAI) | 33 |

Nemotron 3 Ultra is the top-ranked US open-weights model. It is not the top-ranked open-weights model overall. Kimi K2.6 leads by a margin of 6 points (54 vs 48). Decrypt's headline said it plainly: "Nvidia Releases Its Best Open AI Model Yet — But Still Lags Behind China."

**Task-specific benchmarks reported by NVIDIA:**
- HumanEval (coding): 92.1%
- MMLU (knowledge): 89.4%
- Long-context RULER at 256K tokens: 94.2%
- Long-context RULER at 1M tokens: 95% (keynote slide)
- Agent productivity benchmark: 91%

**Speed:** On a pre-release DeepInfra endpoint, Artificial Analysis recorded 300+ tokens/second. Comparably-sized Chinese open models typically run at 50–100 tokens/second in available hosted deployments, partly due to deployment optimization differences. NVIDIA claims 5x faster inference than "comparable competitors" and 30% lower inference cost than "open frontier models in its class." The comparison baselines are not formally specified.

**What matters for builders:** The speed advantage is real and substantial in the context of US-hosted open-weights models. The intelligence gap versus Kimi K2.6 is also real. If raw reasoning performance is the primary constraint, Ultra is not the frontier. If throughput, latency, and US deployment options are the primary constraints, Ultra is the current leader.

---

## Context Window

**1 million tokens.** The 95% RULER score at 1M tokens (from the keynote slide) is the supporting benchmark. RULER (Realistic Uniform Long-context Retrieval) tests the model's ability to retrieve specific information from very long contexts — a better signal than simple "accepts N tokens" claims.

For comparison, most frontier models in the 100–200K token range score in the high 80s to mid-90s on RULER at their claimed limits. A 95% score at 1M tokens, if it holds under third-party evaluation, would be a meaningful long-context capability.

---

## Availability and Licensing

**Launch date:** June 4, 2026

**Where to access:**
- **HuggingFace:** Open weights download (BF16 and NVFP4 quantization formats)
- **ModelScope:** Parallel to HuggingFace
- **OpenRouter:** Vendor-neutral API access
- **NVIDIA NIM:** Hosted microservice at build.nvidia.com — lowest-friction path for most builders

NVIDIA is also releasing the training recipes, data toolchain, and evaluation scripts alongside the weights.

**License:** NVIDIA Open Model License (also called the NVIDIA Open Model Agreement). Key terms:
- Commercial use permitted
- Modification and distribution permitted
- No attribution to NVIDIA required in outputs
- Slightly more restrictive than Apache 2.0 or MIT on certain redistribution conditions — read the full license before packaging for SaaS redistribution

For most builder use cases (calling the API, running on your own infrastructure, fine-tuning for internal products), the license is permissive enough to proceed without legal complexity. For redistribution or embedding in a product sold to others, verify the specific terms.

---

## Hardware Requirements for Self-Hosting

This model cannot run on consumer hardware. The scale requires datacenter infrastructure:

- **Minimum:** A100 or H100 cluster, 300GB+ VRAM after quantization
- **Recommended:** Multi-GPU setup (NVLink fabric preferred)
- **Optimal:** NVIDIA DGX with NVLink, GB300/Blackwell Ultra platforms with native NVFP4 support

The NVFP4 format reduces VRAM requirements by 50–75% compared to BF16, but 55B active parameters at FP4 precision still requires substantial GPU memory. Budget for the infrastructure cost before planning a self-hosted deployment.

**For most builders:** NVIDIA NIM or OpenRouter API access is the practical starting point. The self-hosted path is for organizations with existing DGX infrastructure or a specific data residency requirement that precludes API usage.

---

## Fine-Tuning

NVIDIA is releasing a **Nemotron 3 Ultra Base** checkpoint — the pre-instruction-tuned weights — as a starting point for custom fine-tuning and RL post-training pipelines.

The toolchain includes:
- **NeMo-RL:** Distributed reinforcement learning framework for post-training
- **NeMo-Gym:** Interactive environment simulation for agentic RL training
- **NVFP4 training schedules and quantization recipes**
- **Data-designer toolchain:** Corpus curation tools (deduplication, sequence structuring)

If you are building a specialized agent — one that operates in a specific domain, follows domain-specific protocols, or needs to behave differently from a general assistant — the Ultra Base + NeMo-RL combination is NVIDIA's intended path.

The Nano variant already has community fine-tuning support (Unsloth). Ultra community tooling will develop over the weeks following the June 4 launch.

---

## How Ultra Fits in the Nemotron 3 Family

The Nemotron 3 family released in 2026 covers a range of size/speed trade-offs:

| Model | Total Params | Active Params | Notes |
|---|---|---|---|
| Nemotron 3 Nano Omni | 30B | 3B | Multimodal (text, image, audio, video); edge to DGX |
| Nemotron 3 Super | 120B | 12B | Mid-tier; $0.09/1M input on OpenRouter |
| Nemotron 3 Ultra | 550B | 55B | Frontier-class reasoning; datacenter only |

For most builders, the decision is whether Ultra's intelligence gain over Super justifies the infrastructure cost. On OpenRouter, Super pricing is $0.09/1M input tokens. Ultra pricing was not confirmed before the June 4 launch — expect it to be significantly higher.

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
- Multilingual capability is critical — Qwen 3 significantly outperforms on Asian languages
- You need to self-host without datacenter infrastructure
- You are building multimodal applications — use Nano Omni instead
- Budget is the primary constraint — wait for confirmed Ultra pricing before committing

**The benchmark gap with Kimi K2.6 is real.** 48 vs 54 on the Artificial Analysis Intelligence Index is a meaningful difference, not a rounding error. For builders where intelligence index translates directly to task performance, evaluate both. For builders where throughput, latency, or US data residency are the binding constraints, Ultra is currently the best available option.

---

## What to Watch

- **June 4:** Weights drop on HuggingFace; NIM endpoint goes live; OpenRouter pricing confirmed
- **Community benchmarks:** Third-party reproduction of the 300+ tokens/second and RULER scores will be available within days of the weight release
- **Pricing disclosure:** Ultra pricing on OpenRouter and NIM will determine cost-per-task economics compared to closed frontier models
- **Community fine-tuning support:** Unsloth and similar frameworks will take time to support the NVFP4 weight format
- **Kimi K2.6 availability:** If Moonshot AI opens a US-region API or OSS release improves, the intelligence gap becomes the primary competitive question

---

*Nemotron 3 Ultra was announced by Jensen Huang at NVIDIA's Computex 2026 keynote in Taipei, June 1, 2026. Sources: [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-debuts-nemotron-3-family-of-open-models), [Artificial Analysis](https://artificialanalysis.ai/articles/nvidia-nemotron-3-ultra-launch-announced), [Decrypt](https://decrypt.co/369689/nvidia-open-ai-model-nemotron-3-ultra), [NVIDIA Nemotron Developer Page](https://developer.nvidia.com/nemotron).*

