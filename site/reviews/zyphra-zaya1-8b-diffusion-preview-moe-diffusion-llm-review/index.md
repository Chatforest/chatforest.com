# Zyphra ZAYA1-8B-Diffusion-Preview Review — First MoE Diffusion LLM Converted From Autoregressive

> Zyphra ZAYA1-8B-Diffusion-Preview (May 14, 2026) converts the ZAYA1-8B autoregressive reasoning model into a discrete diffusion LM using the TiDAR recipe. First MoE diffusion model in the field. Generates 16 tokens per forward pass. Claims 4.6x (lossless) to 7.7x (logit-mixing) inference speedup. Trained on AMD Instinct MI300X. Preview-stage: no RL training applied, pass@ evals only, weights not yet publicly confirmed. Rating: 3/5.


**At a glance:** ZAYA1-8B-Diffusion-Preview, released May 14, 2026. Discrete diffusion conversion of the [ZAYA1-8B MoE++ reasoning model](/reviews/zyphra-zaya1-8b-moe-reasoning-llm-review/). 8.4B total parameters, 760M active per token. Claims 4.6x–7.7x inference speedup via parallel token generation. Trained on AMD Instinct MI300X. Preview stage — no RL training, no confirmed public weights. Part of our **[AI Models & LLM reviews](/categories/ai-providers/)**.

---

Eight days after releasing ZAYA1-8B, Zyphra did something unusual: they published a second model built from the same weights.

The ZAYA1-8B-Diffusion-Preview is not a new model in the usual sense. It is the same 8.4B-parameter MoE++ architecture, with the same 760M active parameters per token, running the same AMD-trained checkpoint. What changed is the generation paradigm. Instead of producing tokens left-to-right one at a time, the Diffusion-Preview generates 16 tokens in parallel through a discrete diffusion denoising process. The result, Zyphra claims, is inference that runs 4.6x to 7.7x faster than the original autoregressive model.

This is architecturally significant for two specific reasons: it is the first mixture-of-experts model to be converted into a diffusion LLM, and it demonstrates that post-hoc conversion from an existing autoregressive checkpoint is a viable pathway rather than training from scratch. Whether it matters for production workloads is a separate question. The answer, at preview stage with no reinforcement learning training applied, is not yet.

For background on the base model and Zyphra as a company, see the [ZAYA1-8B review](/reviews/zyphra-zaya1-8b-moe-reasoning-llm-review/).

---

## The Conversion: TiDAR Recipe

The technical route Zyphra took is the **TiDAR recipe** (Think in Diffusion, Talk in Autoregression, arXiv:2511.08923). The approach treats diffusion conversion as a mid-training phase rather than a full retrain.

Starting from the ZAYA1-8B base checkpoint — already trained on 12 trillion tokens — Zyphra ran:

1. **600B tokens of diffusion mid-training** at 32k context, using a masked token prediction objective rather than next-token prediction. This adapts the model's weight representations from the unidirectional chain factorization to the bidirectional masked-token distribution that discrete diffusion requires.
2. **500B tokens of context extension** to 128k, matching the base model's context window.

The efficiency argument is that this reuse pathway is dramatically cheaper than training a large diffusion model from scratch. The AR pretraining compute is not wasted: because both objectives involve prediction over token sequences, the representation structure learned during AR training is transferable. TiDAR uses a dual objective during conversion — masked token prediction and next-token prediction together — specifically to preserve the AR representations while adding diffusion competence.

---

## Why Diffusion Changes the Inference Equation

Standard autoregressive generation is a sequential process. One forward pass produces one token. One hundred tokens requires one hundred forward passes. At the token rates typical of modern LLMs, this creates a hard latency floor per request, and the per-token compute scales with sequence length at inference.

Discrete diffusion breaks that chain. The model starts with a fully masked sequence of the target length and iteratively denoises it — filling in tokens across the entire sequence in parallel. Each forward pass produces multiple tokens. ZAYA1-8B-Diffusion-Preview drafts **16 tokens per forward pass**.

Zyphra's two inference samplers:

- **Lossless sampler (4.6x speedup):** Applies the speculative decoding acceptance criterion — compare each draft token's probability under the diffusion distribution against its probability under the original AR distribution, accept proportionally. Designed to match the AR model's output distribution. "Lossless" refers to distributional equivalence with the AR baseline, not to compression.
- **Logit-mixing sampler (7.7x speedup):** Blends the AR and diffusion logit distributions at runtime. Faster, at the cost of a quality tradeoff the researcher can tune.

The 16-token block drafting works because modern GPU inference is memory-bandwidth-bound, not compute-bound. Once the GPU has loaded the weights for a forward pass, accepting additional tokens from the same pass costs very little incremental compute. This is the same principle behind speculative decoding, but without a separate draft model: the diffusion process itself generates the drafts, and the lossless sampler applies the acceptance criterion using the same model's AR logits.

---

## Where CCA Matters Specifically for Diffusion

The Compressed Convolutional Attention architecture in ZAYA1-8B was designed for KV-cache efficiency during autoregressive decoding. For diffusion inference, it provides a different kind of value.

Diffusion converts decoding into prefill: all token positions are processed in parallel during each denoising step. CCA performs sequence mixing in a compressed latent space, reducing query dimension by 2x and KV-cache size by 8x relative to standard multi-head attention. In the diffusion regime, those savings translate directly into reduced per-step FLOP cost for the parallel denoising passes. Zyphra designed CCA into ZAYA1-8B before the diffusion conversion; the choice looks intentional in retrospect.

---

## The AMD and ROCm Context

The Diffusion-Preview was trained on the same AMD Instinct MI300X cluster as the base model: 1,024 GPUs, IBM Cloud infrastructure, AMD Pensando Pollara 400Gbps networking, ROCm software stack throughout. No NVIDIA hardware at any stage.

The MI300X's 192GB HBM3 per GPU memory configuration is relevant here: diffusion training requires holding more state in memory during parallel denoising passes than autoregressive training does at equivalent sequence length. The large-memory footprint of MI300X makes it a more natural fit for diffusion training than GPUs with smaller VRAM.

Zyphra's broader positioning here is that ZAYA1-8B and the Diffusion-Preview together constitute a proof-of-concept: frontier-tier models are now trainable on AMD hardware at reasonable cost and quality. A noted caveat from outside analysts is that while the AMD hardware argument holds, the ROCm software ecosystem still lags CUDA in tooling maturity for some workloads — fine-tuning and custom kernel development in particular.

---

## The Diffusion LLM Landscape in 2026

ZAYA1-8B-Diffusion-Preview enters a field that is small but active. The major comparison points:

**Inception Labs / Mercury:** The most commercially developed diffusion LLM. Mercury 2 reports 1,000+ tokens per second on H100s and is available via commercial API. Built as a native diffusion model (not converted). Mercury Coder is the primary product. Inception has not published MoE architectures.

**LLaDA:** Academic 8B-parameter model. Demonstrates that discrete masked diffusion can match LLaMA 3 on downstream benchmarks at similar scale. Trained from scratch.

**Google Gemini Diffusion:** Experimental, demonstrated at 2025 AI presentations with fast generation claims. Not publicly available as a standalone API.

**Dream7B:** Open-weight, academic.

ZAYA1-8B-Diffusion-Preview's specific claims to novelty: first MoE diffusion LLM, and first demonstrated conversion from a production AR checkpoint. Neither claim has been disputed in available sources. Mercury is a stronger inference product today; ZAYA1-8B-Diffusion-Preview is a more architecturally interesting research artifact.

---

## Benchmarks and Limitations

Zyphra explicitly chose **pass@k evaluations** for this model rather than the greedy/beam accuracy benchmarks used for the base ZAYA1-8B. The reason they give: this is a mid-train checkpoint that has not undergone RL post-training, and greedy accuracy is not a meaningful measure of a model at this stage. Pass@k asks whether at least one of k samples is correct, capturing the capability ceiling without penalizing for sampling noise in an immature model.

The claimed result is no systematic degradation relative to the AR baseline on pass@ evaluations, with some benchmarks showing gains including LCB-v6 (LiveCodeBench).

What these benchmarks do not show: how the model performs relative to the RL-trained ZAYA1-8B on the headline numbers that make the base model notable — AIME 2026 89.1, HMMT'25 89.6. Those were achieved with the four-stage RL cascade. The Diffusion-Preview has not been through that pipeline.

The specific limitations Zyphra discloses:
1. No RL post-training applied
2. Pass@k evaluations only; greedy accuracy numbers are not appropriate yet
3. Logit-mixing sampler involves a quality tradeoff selectable at runtime
4. Preview status; this is "early work" in diffusion-language models by Zyphra's own framing

---

## Access and Availability

As of this writing, the model weights have not been confirmed as publicly available on Hugging Face. Zyphra's organization page lists a range of models from the ZAYA1 family, but a dedicated `ZAYA1-8B-Diffusion-Preview` card is not confirmed present. The primary Zyphra blog post URL for this model was intermittently inaccessible at time of research. There is no announced public inference API for the Diffusion-Preview.

If you want to run this model today, the path is to contact Zyphra directly or monitor their HuggingFace page. This is a meaningful limitation compared to the base ZAYA1-8B, which has free weights and free serverless inference via Zyphra Cloud.

---

## What to Watch

The ZAYA1-8B-Diffusion-Preview is a research release that previews a path, not a production tool. What would make this significant in a practical sense:

- **RL post-training applied to the diffusion model.** If the four-stage RL cascade from ZAYA1-8B translates to the diffusion variant, the headline benchmark numbers become relevant.
- **Public weights and inference code.** Currently the model is not usable by most builders.
- **ZAYA1-74B-Diffusion.** The larger model in Zyphra's lineup. If diffusion conversion scales to 74B parameters with similar efficiency gains, the throughput story becomes substantially more interesting for production deployments.
- **Competing conversions from other labs.** If the TiDAR recipe proves generalizable, other open-weight model families will attempt the same conversion. A Llama 4 Diffusion or Mistral Diffusion following the same playbook would be a larger story.

---

## Summary

ZAYA1-8B-Diffusion-Preview is the most architecturally interesting model release in the diffusion LLM space this month — not because it benchmarks best, but because it demonstrates that a high-quality MoE autoregressive checkpoint can be converted to diffusion inference with measurable speedup and no claimed systematic quality degradation. The 4.6x lossless speedup is the credible number; the 7.7x logit-mixing number involves a tunable quality tradeoff.

The caveats are real. Preview stage, no RL training, no confirmed public weights, pass@k only. Builders looking for a fast production LLM should look at Mercury 2. Builders interested in where inference efficiency is headed architecturally should be watching this space.

**Rating: 3/5** — architecturally pioneering, not production-ready.

| Dimension | Details |
|---|---|
| Total parameters | 8.4B |
| Active parameters per token | 760M |
| Generation method | Discrete diffusion, 16 tokens/pass |
| Lossless speedup | 4.6x vs AR baseline |
| Logit-mixing speedup | 7.7x vs AR baseline |
| Context window | 128k tokens |
| Training hardware | 1,024 AMD Instinct MI300X + IBM Cloud |
| Post-training | None (RL not applied) |
| License | Apache 2.0 (base model; Diffusion-Preview TBC) |
| Public weights | Not confirmed at time of writing |
| Release date | May 14, 2026 |

