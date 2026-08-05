# NVIDIA Nemotron-Labs-Diffusion: One Model That Drafts and Verifies Itself — 6x More Tokens Per Forward Pass, No Draft Model Required

> NVIDIA's Nemotron-Labs-Diffusion paper (arXiv July 7) introduces a tri-mode language model: autoregressive, block diffusion, and self-speculation — all from one set of weights. The 8B model achieves 6x tokens per forward pass vs Qwen3-8B, with 4x real-world throughput on GB200. No separate draft model, no architectural changes to your serving stack.


NVIDIA Research published [Nemotron-Labs-Diffusion](https://arxiv.org/abs/2607.05722) on July 7, 2026 — a paper describing a language model family that operates in three distinct modes from a single set of weights: standard autoregressive (AR) decoding, block-wise diffusion denoising, and self-speculation. The last mode is the most immediately relevant for builders: it achieves 6x more accepted tokens per forward pass than Qwen3-8B at comparable accuracy, translating to 4x higher throughput on GB200 hardware — without requiring a separate draft model.

This is distinct from [NVIDIA's Nemotron-Labs-TwoTower](https://chatforest.com/builders-log/nvidia-nemotron-labs-twotower-diffusion-lm-2-42x-throughput-builder-guide/) work (July 2), which required splitting a frozen backbone and a diffusion denoiser across two GPUs. Nemotron-Labs-Diffusion runs on a single model, making it closer to a drop-in replacement.

## The Three Modes

The model learns three behaviors from a single set of parameters during training, enabling deployment-time switching:

**AR decoding** — Standard left-to-right token generation. Same interface as any existing LLM. Baseline mode when diffusion or self-speculation aren't needed.

**Block-wise diffusion denoising** — The model receives a sequence with some tokens masked and denoises the masked positions in parallel within each block. Not causal (diffusion sees future positions), which enables bidirectional attention during denoising. Faster than AR for parallel generation when output quality is acceptable at the parallel generation boundary.

**Self-speculation** — This is the mode that drives the throughput numbers. A two-pass process within a single model:
1. Diffusion mode appends k masked tokens to the current context and denoises them all in parallel — generating k candidate tokens in one forward pass
2. AR mode then runs a second forward pass over those k candidates using causal attention — verifying which ones its own predictions would agree with
3. The model accepts the longest contiguous prefix that matches, committing 1 to k+1 tokens per iteration while reusing KV cache

The key insight: both the drafting function (diffusion) and the verification function (AR) come from the same weights. Traditional speculative decoding requires a separate smaller draft model. Here, the model plays both roles.

## Why the Two Objectives Are Complementary, Not Competing

The natural question is whether training a model to both modes degrades each mode's individual quality. The paper argues — and shows empirically — that it doesn't, because the two objectives reinforce different capabilities:

**Diffusion training** improves lookahead planning. To denoise a masked token, the model must model the joint distribution of surrounding tokens, including future positions it can attend to. This makes the model better at predicting what should come later.

**AR training** anchors representations to natural language's left-to-right structure, preventing wasted capacity on arbitrary token orderings. It provides the linguistic priors that make the diffusion-generated drafts coherent rather than random.

At inference time in self-speculation mode, diffusion's lookahead strength generates better drafts; AR's left-to-right grounding provides a reliable verifier. Acceptance rates are high because both modes were trained jointly on the same weights.

## Training Setup

Two-stage, per [the paper's training section](https://arxiv.org/html/2607.05722v1):
1. **Stage 1 (1T tokens)**: Pure AR pretraining to establish linguistic priors
2. **Stage 2**: Joint training with a weighted combination of AR and diffusion losses (α=0.3 on the diffusion term). Global loss averaging treats all tokens equally across batches, stabilizing optimization despite variable masking ratios

## Benchmark Numbers

Figures below are from [the paper's benchmark tables](https://arxiv.org/html/2607.05722v1), evaluated across 10 tasks spanning QA, instruction-following, coding, and math (GPQA, IFEval, MMLU, HumanEval, MBPP, LiveCodeBench-CPP, Math500, GSM8K, AIME24, AIME25).

**8B Instruct (self-speculation with LoRA-enhanced linear self-speculation):**
- 5.99× tokens per forward pass (TPF) vs. Qwen3-8B's 1.0× baseline
- Average accuracy: 63.61% across 10 tasks vs. Qwen3-8B 62.75%
- 3.97× throughput on GB200 over standard AR

**3B Instruct:** 4.36× TPF, 55.00% accuracy
**14B Instruct:** 5.96× TPF, 66.36% accuracy

Importantly: accuracy holds. The throughput gains don't come from quality degradation — the model at 8B outperforms Qwen3-8B on both tokens per forward and average task accuracy.

## Hardware and Availability

Training required 256 NVIDIA H100 GPUs. Inference was evaluated at batch size 1, versus standard AR decoding on the same hardware ([per the paper's speed-of-light section](https://arxiv.org/html/2607.05722v1)):
- **GB200**: up to 3.3× over AR (3.97× with an optimized kernel, 1015 tok/sec)
- **RTX Pro 6000**: 3.46×/2.35× over AR (277/525 tok/sec, two quantization configs)
- **DGX Spark**: 3.14×/2.69× over AR (77.5/112.5 tok/sec, two quantization configs)

All three model sizes (3B, 8B, 14B) — including base, instruction-tuned, and vision-language variants — are available on [Hugging Face under the NVIDIA Nemotron-Labs-Diffusion collection](https://huggingface.co/collections/nvidia/nemotron-labs-diffusion). The weights are released under the [NVIDIA Nemotron Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license), which permits commercial use. The training and inference pipeline is released via [Megatron Bridge](https://github.com/NVIDIA-NeMo/Megatron-Bridge/pull/3105).

## Comparison to TwoTower

| | TwoTower (July 2) | Diffusion (July 7) |
|---|---|---|
| Architecture | Frozen 30B AR backbone + trained diffusion denoiser | Single model, joint-trained |
| Hardware requirement | 2 GPUs required | Single GPU |
| Throughput claim | 2.42× at 98.7% quality | 4× real (6× tokens per forward) |
| Draft model needed | No (denoiser is draft) | No (self-speculation) |
| Drop-in compatibility | Requires serving change | Closer to drop-in |
| Weights | Open | Open |

TwoTower is a larger-scale model (60B) with a different mechanism — frozen pretrained AR + separately trained diffusion denoiser across two GPUs. Nemotron-Labs-Diffusion is smaller (3B/8B/14B), single-model, and designed to serve as a practical replacement for standard AR deployments.

## Builder Implications

**Low-concurrency speedups are now viable.** Most speculative decoding approaches require high request concurrency to see real-world throughput gains. Self-speculation in this model delivers roughly 2.35–3.97× speedup over standard AR at batch size 1 across GB200, RTX Pro 6000, and DGX Spark ([per the paper](https://arxiv.org/html/2607.05722v1)) — meaning developers running inference on single-GPU workstations or small-batch production deployments can benefit, not just hyperscaler inference operators. (The paper separately reports a 2.4×/2.3×/1.8× speedup over Eagle3 — a different speculative-decoding baseline, not standard AR — at the same batch size; don't conflate the two comparisons.)

**No serving infrastructure changes required.** Because both the draft and verify steps use the same model weights, there's no second model to load, manage, or version-match. You load one checkpoint, serve with SGLang, and get the throughput benefit by switching decoding mode.

**The 8B Instruct variant is the practical starting point.** At 63.61% accuracy and 6× TPF with the LoRA-enhanced path, it outperforms Qwen3-8B (62.75%) while dramatically increasing throughput. For tasks where Qwen3-8B was already good enough, Nemotron-Labs-Diffusion is a direct upgrade.

**Vision-language variants ship alongside text-only.** If you're building multimodal workflows, the VL variant exists at all three sizes — this is not a text-only research release.

**76.5% additional parallelism headroom.** The [speed-of-light analysis in the paper](https://arxiv.org/html/2607.05722v1) identifies that diffusion-only mode can theoretically yield up to 76.5% more tokens per forward than current self-speculation under an optimal sampler. That ceiling hasn't been reached yet, which means future inference optimizations (better samplers, faster denoising heads) will continue improving throughput without retraining the model.

## What This Doesn't Change

The model competes at the 3–14B scale. It doesn't replace frontier-class models for tasks requiring maximum intelligence — Sonnet 5, Sol, or Fable 5 aren't in scope here.

The 256 H100 training requirement also means replicating the training approach is out of reach for most teams. But the weights are available, and inference is the relevant operation for most builders.

---

Nemotron-Labs-Diffusion represents a different design point than TwoTower or [Google DeepMind's DiffusionGemma](https://deepmind.google/models/gemma/diffusiongemma/): a small, single-checkpoint model where three decoding modes — including draft-free speculative decoding — are unlocked from one set of weights. If you run inference at modest scale on NVIDIA hardware and Qwen3-8B is currently in your stack, this is worth evaluating.

