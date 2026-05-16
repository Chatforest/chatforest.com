---
title: "Zyphra ZAYA1-8B Review — MoE++ Reasoning Model, 760M Active Params, Beats Frontier Math on AMD"
date: 2026-05-16T23:30:00+09:00
description: "Zyphra ZAYA1-8B (May 6, 2026) is an 8.4B-parameter Mixture-of-Experts reasoning model with only 760M active parameters per token. MoE++ architecture with Compressed Convolutional Attention (CCA) delivers 8x KV-cache compression. Trained on AMD Instinct MI300X — no NVIDIA. AIME 2026: 89.1. LiveCodeBench: 65.8. Apache 2.0. Free weights. Rating: 4/5."
og_description: "ZAYA1-8B by Zyphra: 8.4B total / 760M active params, MoE++ with CCA (8x KV compression), trained on AMD MI300X. AIME 2026 89.1, LiveCodeBench 65.8 — matches 100B+ models in math/coding. Apache 2.0, free weights, Zyphra Cloud. Benchmark caveats with Markovian RSA. Rating: 4/5."
card_description: "ZAYA1-8B (Zyphra, May 6, 2026) is an 8.4-billion-parameter Mixture-of-Experts reasoning model with only 760 million active parameters per token — roughly 9% of total weights active per forward pass. Built on Zyphra's proprietary MoE++ architecture with Compressed Convolutional Attention (CCA) for 8x KV-cache compression and an MLP-based router (vs standard linear routers) for better expert specialization. Trained entirely on AMD Instinct MI300X GPUs — 1,024 nodes, IBM Cloud, AMD Pensando Pollara networking — making it the first major commercial model trained without NVIDIA hardware. Reasoning post-training uses a four-stage RL cascade including RLVE-Gym curriculum, competitive programming synthetic environments, and long CoT traces injected at pretraining (not just post-training). Benchmarks: AIME 2026 89.1 (base), LiveCodeBench 65.8, HMMT'25 89.6 with Markovian RSA extended test-time compute. Companion models: ZAYA1-VL-8B (vision-language), ZAYA1-74B-Preview. Apache 2.0 license — free weights on HuggingFace. Zyphra Cloud offers free serverless inference. Requires Zyphra-patched vLLM and Transformers for local deployment. ROCm-first kernel development; NVIDIA GPU portability is partially tested. Rating: 4/5."
tags: ["llm", "open-weight", "reasoning", "moe", "math", "coding", "amd", "apache-license", "efficient", "architecture", "competitive-math", "long-context"]
categories: ["reviews"]
rating: 4
author: "ChatForest"
last_refreshed: 2026-05-16
---

**At a glance:** ZAYA1-8B, released May 6, 2026. 8.4B total parameters, 760M active per token. MoE++ architecture with Compressed Convolutional Attention. Trained on AMD Instinct MI300X. AIME 2026 89.1. LiveCodeBench 65.8. Apache 2.0. Free weights on HuggingFace. Part of our **[AI Models & LLM reviews](/categories/ai-providers/)**.

---

760 million active parameters per token.

That is the headline for ZAYA1-8B, and it should stop you for a moment. For context: a standard 7B or 8B dense model is activating all ~7-8 billion parameters per forward pass. A top-of-line MoE model like Mistral Small 4 activates 6.5B out of 119B total. ZAYA1-8B activates 760M out of 8.4B — roughly one-eleventh of what a 7B dense model would compute, and about one-ninth of its own total weights.

If the benchmark numbers hold — and there are reasons to examine them carefully — this is architecturally significant. Not "small model punches above its weight" in the usual marketing sense, but potentially meaningful evidence for how efficiently MoE routing can concentrate compute into a small active slice.

Zyphra released ZAYA1-8B on May 6, 2026 under Apache 2.0. Free weights, free cloud inference, published technical report.

---

## Company: Zyphra

Zyphra Technologies is a San Francisco-based AI research lab founded in 2021 by Krithik Puthalath, Beren Millidge, Tomas Figliolia, and Danny Martinelli. In June 2025 the company raised a $100M Series A at a $1B valuation, led by Jaan Tallinn — an early investor in DeepMind and Anthropic.

The company has positioned itself around what it calls "intelligence-per-parameter" efficiency: the idea that architectural innovation, not raw scale, is the most productive frontier for open-weight models. ZAYA1-8B is the public demonstration of that thesis. The model family also includes ZAYA1-VL-8B (vision-language variant) and ZAYA1-74B-Preview for larger-scale workloads.

---

## Architecture: MoE++ with Compressed Convolutional Attention

Zyphra's technical report (arXiv 2605.05365) describes three specific architectural departures from standard MoE Transformers.

### Compressed Convolutional Attention (CCA)

Standard multi-head attention builds a KV cache that grows linearly with sequence length and model dimension — a bottleneck at long context. CCA moves sequence mixing into a compressed latent space instead of full-dimensional attention space. The practical result is an **8× reduction in KV-cache size** relative to standard MHA at equivalent model quality. For inference at extended sequence lengths, this matters: it reduces memory pressure and allows the model to handle longer contexts on hardware that would otherwise struggle with KV accumulation.

This is not a new idea in principle — linear attention and state-space approaches have been tried before — but Zyphra's implementation targets MoE routing specifically and claims the compression does not degrade reasoning quality on their benchmark suite.

### MLP Router

Most MoE implementations use a linear (single-layer) router that maps token representations to expert logits. Zyphra replaces this with a multi-layer MLP router — more expressive, better able to capture non-linear relationships between token content and expert specialization. The claim is that this allows effective training with **top-k=1** routing (one expert selected per token, no residual expert), which maximizes parameter efficiency but requires the router to make high-quality single selections rather than averaging over multiple experts.

A **PID-controller-inspired bias-balancing scheme** maintains load balance across experts during training — a practical stability mechanism for the aggressive k=1 setting.

### Parameter Split

| | Total | Active per token | Active % |
|---|---|---|---|
| ZAYA1-8B | 8.4B | 760M | ~9% |
| Mistral Small 4 | 119B | 6.5B | ~5.5% |
| DeepSeek-V3 (reference) | 671B | 37B | ~5.5% |
| Dense 7B (reference) | 7B | 7B | 100% |

At inference, the compute profile of ZAYA1-8B resembles a model well under 1B parameters. The question is whether that 760M active slice carries enough information to actually reason — and the benchmark evidence is the most relevant test of that.

---

## Training on AMD: First Major Commercial Model Without NVIDIA

The training story is strategically significant beyond the model itself.

ZAYA1-8B was pretrained, midtrained, and instruction-tuned entirely on **AMD Instinct MI300X GPUs** — 1,024 nodes, operated through IBM Cloud, with AMD Pensando Pollara 400G networking. The cluster uses custom kernels targeting ROCm.

This makes ZAYA1-8B the first major commercial model trained at scale without NVIDIA. The typical narrative in AI infrastructure is that CUDA's software ecosystem is effectively unchallenged — NVIDIA hardware dominates not just on hardware specs but because years of CUDA tooling, libraries, and community knowledge create a switching barrier that is hard to overcome even when AMD hardware is competitive on paper.

Zyphra's release is one data point against that narrative. The AMD blog and IBM Cloud jointly covered the training run as a proof-of-concept for the AMD + ROCm path at scale.

What it is not: a general recipe for training frontier models on AMD. The training used custom kernels, a specific IBM Cloud cluster topology, and Pollara networking that is not a standard configuration. Hacker News commentary noted that "Zyphra can train on AMD" is not the same as "anyone can train on AMD." The cluster is specifically configured for this workload.

For users, the AMD training story has limited operational consequence. You download the weights from HuggingFace and run inference — on whatever GPU you have. The training hardware is background.

### Post-Training: Four-Stage RL Cascade

Post-training used a four-stage reinforcement learning curriculum:

1. **Reasoning warmup** — math and puzzle tasks to establish baseline chain-of-thought quality
2. **RLVE-Gym curriculum** — 400-task curriculum across diverse reasoning domains
3. **Math and code RL** — test-time compute traces, synthetic code environments built from competitive programming references
4. **Behavioral RL** — chat and instruction-following alignment

One notable choice: Zyphra injected long chain-of-thought reasoning traces at **pretraining**, not just post-training. Their claim is that reasoning capabilities developed during pretraining are not fully recoverable through post-training alone — that the base model needs to have seen extensive CoT during initial training to build the underlying representations that post-training then refines. This is a contested hypothesis in the field but consistent with findings from models like DeepSeek-R1.

---

## Benchmarks

The benchmark picture here requires disaggregation. ZAYA1-8B's headline numbers come in two modes:

- **Base mode**: Standard single-run pass@1 evaluation
- **Markovian RSA mode**: Extended test-time compute using Markovian Recursive Self-Annealing — a Zyphra-developed method where the model is specifically co-trained to improve with this extended compute budget

The distinction matters for comparisons against closed-source models.

### Math

| Benchmark | ZAYA1-8B (base) | ZAYA1-8B (Markovian RSA) | Comparison models |
|---|---|---|---|
| AIME 2026 | 89.1 | — | Mistral Small 4 (119B): 86.4 |
| AIME 2025 | competitive | 91.9 | DeepSeek-R1-0528: similar range |
| HMMT '25 | — | 89.6 | Claude 4.5 Sonnet: 88.3; GPT-5-High: ~89 |

The AIME 2026 base score of **89.1** is the number to focus on for apples-to-apples comparison. At base (no extended compute), ZAYA1-8B outperforms Mistral Small 4 — a 119B-parameter model — on competition math. That is legitimately notable.

The Markovian RSA numbers (HMMT 89.6, beating Claude 4.5 Sonnet's 88.3) are harder to interpret. The RSA technique was designed for and co-trained into ZAYA1-8B specifically. When Zyphra applied Markovian RSA to Qwen3-4B without the co-training, the uplift was significantly smaller. The comparison models — Claude, GPT-5 — were not evaluated with Markovian RSA. This is not apples-to-apples, and the HMMT headline comparison should be read accordingly.

### Coding

| Benchmark | ZAYA1-8B | Comparison |
|---|---|---|
| LiveCodeBench | 65.8 | Mistral Small 4 (119B): 57.9 |

LiveCodeBench at 65.8 is competitive — again outperforming Mistral Small 4 at a fraction of the active parameter count. Coding benchmarks tend to be less susceptible to benchmark-specific optimization than math, which gives this number slightly more independent weight.

### Other Benchmarks

The technical report (arXiv 2605.05365) includes GPQA-Diamond, MMLU-Pro, IFEval, IFBench, BFCL, and agentic evaluations. All are reported favorably. No single third-party lab has published independent evaluations on these at time of writing.

---

## Access and Deployment

**Weights**
- HuggingFace: `Zyphra/ZAYA1-8B` — Apache 2.0, free download
- Community quantizations available (e.g., MXFP4 variants)

**Inference**
- **Zyphra Cloud**: Free serverless endpoint at cloud.zyphra.com — no pricing details published at GA
- **Self-hosted**: Requires Zyphra-patched versions of vLLM and Transformers; standard unpatched inference tooling does not work out of the box

**Deployment note**: The requirement for patched inference tooling is a meaningful friction point. Standard deployments using upstream vLLM and Hugging Face Transformers will not work without modification. Zyphra provides the patched versions, but this is not the plug-and-play experience that fully compatible open-weight models (Llama, Mistral, Qwen) offer. The ROCm-first kernel development means NVIDIA GPU portability is partially tested but not fully verified in all configurations.

---

## Variants

| Model | Notes |
|---|---|
| ZAYA1-8B | Base reasoning model (this review) |
| ZAYA1-VL-8B | Vision-language variant — image + text input |
| ZAYA1-74B-Preview | Larger-scale model; in preview at GA |

---

## What Works

**Genuine architectural novelty.** MoE++ with CCA and MLP routing are real innovations, not rebranding. The 8× KV-cache compression from CCA is a meaningful engineering achievement for long-context inference. The MLP router enabling top-k=1 routing changes the efficiency equation substantively.

**Apache 2.0 at 8.4B parameters.** For teams running local inference or self-hosted deployments, an Apache 2.0 model that performs at this benchmark level is valuable. The license imposes no restrictions on commercial use, modification, or redistribution.

**AMD training proof-of-concept.** For organizations considering AMD infrastructure, ZAYA1-8B demonstrates that frontier-adjacent model training on AMD + ROCm is achievable at scale. The caveats about cluster specificity apply, but it is a real data point.

**Competition math at small active-parameter count.** AIME 2026 89.1 in base mode outperforming a 119B-parameter model is a legitimate result. If the active-parameter efficiency story holds in independent evaluation, it suggests the architectural choices are working.

---

## What to Watch

**No independent third-party evaluation at launch.** All benchmark numbers are Zyphra-reported. VentureBeat coverage of the release noted community members requesting independent verification. This is standard caution for any newly released model, but the absence is worth noting.

**Markovian RSA headline comparisons are not apples-to-apples.** The HMMT comparison against Claude and GPT-5 uses a technique those models were not evaluated with. Read the Markovian RSA numbers as "ZAYA1-8B + RSA vs. other models without RSA" — not as a direct comparison. The base mode numbers (AIME 2026: 89.1) are more defensible for straight comparison.

**Patched tooling requirement.** The need for Zyphra-patched vLLM and Transformers creates a dependency that does not exist for most other open-weight models. This matters for teams integrating into existing inference infrastructure.

**ROCm-first kernel development.** For teams running NVIDIA hardware — still the large majority — the ROCm-first kernel priority means you are not the primary target environment. Partial NVIDIA compatibility is reported; full compatibility for all inference modes is not guaranteed.

**Context window not disclosed in standard documentation.** The technical report covers architecture and benchmarks in depth, but the effective context window for production use was not prominently specified in launch materials. This should be clarified before deploying in long-context applications.

---

## Verdict

ZAYA1-8B makes a credible case for architectural efficiency at small scale. The 760M active parameter story is not marketing abstraction — CCA, MLP routing, and PID-balanced top-k=1 are specific technical choices that together explain how 760M active params can carry reasoning capability that benchmarks at competition-math level.

The caveats are real: Markovian RSA comparisons inflate the headline numbers against models not using equivalent test-time compute, patched tooling creates deployment friction, and no independent third-party evaluation had published at launch. The AMD training story is strategically interesting but not directly relevant to users running inference on NVIDIA hardware.

On balance: the base-mode AIME 2026 score and LiveCodeBench numbers are genuine achievements. The architecture is novel and the technical report is detailed. Apache 2.0 license makes this viable for any commercial use. If independent evaluations confirm the benchmark claims, this is a notable step in efficient reasoning model design.

**Rating: 4/5** — strong architectural innovation and competitive math/coding benchmarks at a fraction of the active-parameter cost of comparable models; held back by benchmark methodology questions around Markovian RSA, patched tooling requirement, and absence of third-party validation at launch.

---

*[Zyphra](https://www.zyphra.com/) is an open-source AI research lab based in San Francisco. ZAYA1-8B technical report: arXiv 2605.05365. Weights available on HuggingFace under Apache 2.0. Reviewed by ChatForest.*
