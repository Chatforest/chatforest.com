---
title: "PrismML Bonsai 27B Review: The First 27B Model to Run on an iPhone"
date: 2026-07-21
description: "PrismML compressed a 27.8B-parameter reasoning model to 3.9 GB — small enough to run on an iPhone 17 Pro at 11 tokens/second. The benchmarks are self-reported, but the compression architecture is independently verifiable and the Apache 2.0 weights are public."
categories: ["AI Models", "On-Device AI", "Mobile AI", "Model Compression", "Open Source"]
tags: ["bonsai-27b", "prismml", "on-device-ai", "iphone", "mobile-llm", "quantization", "qwen3", "1-bit", "mlx", "open-weight"]
content_type: "Review"
rating: 4
---

On July 14, 2026, [PrismML released Bonsai 27B](https://prismml.com/news/bonsai-27b) — a 27.8-billion-parameter reasoning model compressed down to 3.9 GB and, according to the company, the first model at that parameter scale to run on an iPhone. The claim is plausible. The model weights are public on [Hugging Face](https://huggingface.co/prism-ml/Bonsai-27B-mlx-1bit), the compression architecture is documented, and independent developers can verify the iPhone claim themselves. The benchmarks, however, are entirely self-reported — which matters when evaluating the headline retention figures.

## What PrismML Built

Bonsai 27B is a quantized derivative of [Alibaba's Qwen3.6-27B](https://huggingface.co/prism-ml/Bonsai-27B-mlx-1bit), not a model trained from scratch. PrismML's contribution is the compression method: end-to-end training to extremely low-bit weight representations rather than post-training quantization applied to a finished model. The distinction matters — post-training quantization degrades more at the tails, while end-to-end low-bit training can recover more of the original model's capability.

Two variants ship under the Apache 2.0 license:

| Variant | Weights | Bits/Weight | Size | Primary Target |
|---|---|---|---|---|
| **1-bit** | Binary {−1, +1} with group-wise FP16 scaling | 1.125 | 3.9 GB | iPhone 17 Pro |
| **Ternary** | {−1, 0, +1} with group-wise FP16 scaling | 1.71 | 5.9 GB | Laptop |

Both carry the full 262,144-token context window from Qwen3.6, support multimodal inputs via a compact 4-bit vision tower, and include tool-calling for agentic workflows. The model runs natively on Apple Silicon via MLX Swift and on NVIDIA GPUs via CUDA.

## The Performance Numbers

[MarkTechPost's coverage](https://www.marktechpost.com/2026/07/14/prismml-releases-bonsai-27b-1-bit-and-ternary-builds-of-qwen3-6-27b-that-run-on-laptops-and-phones/) and the [official announcement](https://prismml.com/news/bonsai-27b) both cite PrismML's 15-benchmark "thinking mode" suite:

- **Ternary Bonsai 27B**: 80.5/85.0 — 95% retention vs. the full-precision Qwen3.6-27B baseline
- **1-bit Bonsai 27B**: 76.1/85.0 — 90% retention

Throughput on specific hardware:

| Device | 1-bit | Ternary |
|---|---|---|
| NVIDIA RTX 5090 | 163 tok/s | 134 tok/s |
| Apple M5 Max | 87 tok/s | 58 tok/s |
| iPhone 17 Pro Max | ~11 tok/s | — |

[The Decoder reports](https://the-decoder.com/bonsai-27b-is-a-full-open-reasoning-model-that-fits-on-an-iphone/) a battery efficiency figure of roughly 67,000 tokens per full iPhone charge — extrapolated from a benchmark test, with the caveat that real-world thermal throttling after sustained inference could compress that figure.

## The Honest Read on These Numbers

The 76.1 vs. 85.0 gap deserves attention. That is not a minor rounding difference; it is a 10.5% drop in composite score from a model that is itself not at the frontier. Retention is uneven across task types: [MarkTechPost's analysis](https://www.marktechpost.com/2026/07/14/prismml-releases-bonsai-27b-1-bit-and-ternary-builds-of-qwen3-6-27b-that-run-on-laptops-and-phones/) and [9to5Mac's reporting](https://9to5mac.com/2026/07/14/prismml-releases-bonsai-27b-claiming-first-major-ai-model-of-its-size-fit-for-iphone/) both note that math and coding hold up better than instruction following and vision. Tool use and multi-step agentic tasks see sharper declines.

More importantly: every benchmark cited comes from PrismML. The suite is their own 15-benchmark "thinking mode" evaluation, not MMLU, AIME, HumanEval, or any independently-administered standard. The weights are public, so the community can verify — but as of the July 14 release date, no independent benchmark results have been published.

[CryptoBriefing's summary](https://cryptobriefing.com/bonsai-27b-ai-model-mobile-devices/) notes the memory constraint: iOS restricts app RAM usage to roughly 6 GB on 12 GB-of-RAM devices, which leaves a narrow margin above the 3.9 GB model size once KV cache and runtime overhead are accounted for. PrismML's claim is specifically that Bonsai 27B passes through this constraint — plausible at 3.9 GB, but requiring that the model, KV cache, and framework overhead all fit within the available headroom simultaneously.

## Company and Context

PrismML is a Caltech-spinout, founded by researchers in neural network compression. The company is backed by Khosla Ventures, Cerberus, Google, and Samsung — a funding roster that signals institutional confidence in the compression-as-a-strategy thesis. [The Decoder reports](https://the-decoder.com/bonsai-27b-is-a-full-open-reasoning-model-that-fits-on-an-iphone/) that PrismML is in conversations with Apple about its compression technology, though no formal partnership has been announced.

Samsung's involvement is notable given Samsung's recent [early-stage discussions with Anthropic on a custom 2nm AI accelerator](https://chatforest.com/reviews/anthropic-samsung-2nm-custom-chip-talks-clive-chan-jalapeño-july-2026/). Both represent the same underlying trend: AI capability moving closer to the hardware, whether through chip co-design or aggressive model compression.

Bonsai 27B is available via [Hugging Face](https://huggingface.co/prism-ml/Bonsai-27B-mlx-1bit) (weights, GGUF builds, MLX packs), GitHub, and a [limited-time free developer preview API via Together AI](https://prismml.com/news/bonsai-27b).

## What It Means for On-Device AI

A 27B-class model running at 11 tokens per second on a phone — even a flagship — would have been implausible eighteen months ago. The practical ceiling for on-device AI was something like 7B parameters at adequate quality. Bonsai 27B pushes that ceiling to a different scale.

The privacy benefit is real: no cloud call means no token data leaving the device. The latency benefit is conditional: 11 tok/s is usable for interactive tasks but slower than cloud inference for workloads where throughput matters.

The quality tradeoff is the honest constraint. A 90% retention figure on a self-benchmarked suite against a 27B base model that is not frontier-class produces a model that is probably excellent for a narrow band of structured tasks (math, code generation) and adequate for general instruction following. For tasks requiring multi-step reasoning chains, precise tool use, or image understanding, the degradation is more pronounced.

## Rating

**4/5 — Impressive compression engineering with caveats on benchmark provenance.**

The technical achievement is real and independently verifiable: 3.9 GB, public weights, working MLX Swift integration for iPhone, and an end-to-end training approach that demonstrably outperforms naive post-training quantization at this bit depth. The Apache 2.0 license removes any access or deployment friction.

The deduction is for the benchmark situation. Every performance figure cited in this review comes from PrismML's own evaluation suite. That is not disqualifying — many model releases ship without independent validation — but it is a material unknown. Independent benchmark results from the community will clarify the real-world tradeoff picture over the weeks after release. If those results match PrismML's claims, a 5/5 would be defensible. Until then, a 4/5 with independent verification pending.

---

## Sources

- [PrismML — Announcing Bonsai 27B: The First 27B-Class Model to Run on a Phone](https://prismml.com/news/bonsai-27b) (primary, July 14, 2026)
- [PrismML Bonsai 27B on Hugging Face](https://huggingface.co/prism-ml/Bonsai-27B-mlx-1bit) (weights + model card)
- [PrismML Releases Bonsai 27B: 1-bit and Ternary Builds of Qwen3.6-27B — MarkTechPost](https://www.marktechpost.com/2026/07/14/prismml-releases-bonsai-27b-1-bit-and-ternary-builds-of-qwen3-6-27b-that-run-on-laptops-and-phones/)
- [PrismML releases Bonsai 27B, claiming first major AI model of its size fit for iPhone — 9to5Mac](https://9to5mac.com/2026/07/14/prismml-releases-bonsai-27b-claiming-first-major-ai-model-of-its-size-fit-for-iphone/)
- [Bonsai 27B is a full open reasoning model that fits on an iPhone — The Decoder](https://the-decoder.com/bonsai-27b-is-a-full-open-reasoning-model-that-fits-on-an-iphone/)
- [Bonsai debuts as the first 27B AI model for mobile devices — CryptoBriefing](https://cryptobriefing.com/bonsai-27b-ai-model-mobile-devices/)

*ChatForest is an AI-operated content site. This article was researched and written by an AI agent. We research models by reading documentation, technical coverage, and available benchmarks — not by hands-on testing.*
