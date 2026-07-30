---
title: "NVIDIA Nemotron 3 Nano Omni: A 3B-Active Omnimodal Sub-Agent for Single-GPU Deployment — Builder Guide"
date: 2026-06-17
description: "Nemotron 3 Nano Omni is a 30B Mamba-Transformer MoE model with only 3B active parameters per token, designed as a multimodal perception sub-agent. It natively processes text, image, video, and audio in a single model. Available free on Hugging Face and OpenRouter."
og_description: "NVIDIA Nemotron 3 Nano Omni — 30B MoE, 3B active, omnimodal (text + image + video + audio), 82.1% AIME25 (no tools), 63.2% LiveCodeBench, up to 9x per-GPU throughput vs Qwen3-Omni, free open weights. Builder guide: architecture, benchmarks, pricing, sub-agent design patterns."
content_type: "Builder's Log"
categories: ["Open Source Models", "Agents", "Developer Tools", "LLMs", "Multimodal"]
tags: ["nvidia", "nemotron", "nemotron-3-nano-omni", "mamba", "moe", "omnimodal", "multimodal", "open-weights", "sub-agent", "edge-ai", "builder-guide", "2026", "agentic", "nim"]
sources_audited: 2026-07-30
---

On April 28, 2026, NVIDIA released **Nemotron 3 Nano Omni** — a 30B-parameter hybrid Mamba-Transformer Mixture of Experts model that unifies text, image, video, and audio understanding in a single open-weight checkpoint. Details from the [NVIDIA Blog announcement](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/) and the [NVIDIA Technical Blog deep dive](https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/). It is designed explicitly as a perception and reasoning sub-agent in compound AI systems, and it costs nothing to access: the weights are free on Hugging Face, and the API is free on OpenRouter.

The technical headline is unusual: **~31 billion total parameters, but only ~3 billion active per forward pass**, per the [Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16). That active-parameter count is what determines inference cost.

This guide covers the architecture, benchmarks, deployment options, and agentic use cases for builders evaluating Nano Omni as a component in multi-agent systems.

---

## The One-Sentence Summary

Nemotron 3 Nano Omni is a ~30B-total/~3B-active Mamba-Transformer MoE model that accepts text, images, video, and audio as input, scores 82.1% on AIME 2025 (no tools) and 63.2% on LiveCodeBench in its own [technical report](https://arxiv.org/abs/2604.24954) — a modest step down from its text-only sibling [Nemotron 3 Nano](https://arxiv.org/abs/2512.20848) (89.1% / 68.3% on the same two benchmarks), the expected tradeoff of unifying reasoning across four modalities — and is available as open weights and free API, built specifically to serve as the multimodal perception layer in compound agent architectures.

---

## Why This Matters for Builders

Three constraints have historically made omnimodal agents expensive or impractical:

| Problem | Previous workaround | Nano Omni approach |
|---|---|---|
| Separate model stacks per modality | Run vision model + audio model + LLM in sequence | Single model handles all modalities in one reasoning pass |
| Omnimodal = slow | Accept high latency or sacrifice quality | Mamba layers eliminate the quadratic attention bottleneck |
| Frontier capability = large active footprint | Use a 70B+ dense model or pay closed-model API rates | MoE routing keeps active parameters at ~3B |

If you are building a system that needs to reason across a video transcript, an uploaded image, a voice memo, and a text document in the same context window — and you want to do this affordably, with open weights, on-premise — Nano Omni is one of the few models that addresses all four constraints at once (we have not surveyed every open omnimodal release to confirm it is literally the first).

---

## Architecture: Mamba-Transformer Hybrid MoE

### Why Mamba?

Standard transformer attention scales quadratically with sequence length. For an omnimodal model processing a video (many frames) alongside a long document, this quadratic cost becomes prohibitive. Mamba-2 is a state-space model that replaces the attention mechanism with a recurrent formulation, achieving **linear sequence complexity** — the cost of processing frame 1000 of a video is the same as processing frame 1.

NVIDIA's design combines Mamba's sequence efficiency with transformer attention's ability to perform precise local reasoning across a context window. The result is a hybrid:

| Layer type | Count | Role |
|---|---|---|
| Mamba-2 layers | 23 | Sequence compression, memory efficiency, long-range state |
| MoE Transformer layers | 23 | Sparse expert routing for domain specialization |
| Attention layers (GQA) | 6 | Precise local context reasoning |

Total: 52 layers. Model dimension: 2688. Query heads: 32. KV heads: 2. Head dimension: 128. (Per the model's [published `config.json`](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16/raw/main/config.json).)

### Why MoE?

The ~31B total parameters are divided among 128 routed experts per MoE layer plus 1 shared expert. Each forward pass activates 6 of the 128 routed experts per token (the shared expert activates on every token) — [confirmed in the model config](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16/raw/main/config.json). The result: ~3 billion parameters active per inference call — a compute cost comparable to a small dense model, with capacity comparable to a much larger one.

The practical implication: Nano Omni can run inference on a single GPU rather than requiring multi-GPU tensor parallelism — a single H100 80GB at full BF16 precision, or as small as a single RTX 5090 32GB using the NVFP4-quantized release, per the [Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16). This matters for edge agents and on-premise deployments where multi-node infrastructure is not available.

### Omnimodal: Native, Not Adapted

Most multimodal models attach vision or audio via an adapter trained on a frozen language backbone. Nano Omni integrates all modalities from training step zero — there is no seam between the vision encoder, audio processor, and language reasoning. This matters for tasks that require cross-modal reasoning: interpreting a chart from a screenshot while writing code to reproduce it, or summarizing a video while citing timestamps in a document.

**Accepted inputs** (per the [Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16)):
- Text (up to a 256K-token context window)
- Images (static)
- Video (multi-frame)
- Audio

**Output:** Text only.

---

## Benchmarks in Context

### Math and Reasoning

NVIDIA's own [Nano Omni technical report](https://arxiv.org/abs/2604.24954) (Table 10) benchmarks the multimodal model's text reasoning directly against its text-only sibling, [Nemotron 3 Nano](https://arxiv.org/abs/2512.20848):

| Benchmark | Nano Omni | Nemotron 3 Nano (text-only sibling) |
|---|---|---|
| **AIME 2025 (no tools)** | 82.1% | 89.1% |
| **GPQA (no tools)** | 72.2% | — |
| **MMLU-Pro** | 77.3% | — |

Unifying text, image, video, and audio reasoning into a single model costs Nano Omni roughly 7 points of AIME accuracy versus the text-only sibling that shares its backbone — a real tradeoff, not a wash. NVIDIA's technical report does not publish a Nano-Omni-specific comparison against Qwen3-30B-A3B or GPT-OSS-20B on these text benchmarks, so this guide does not claim one.

### Code

| Benchmark | Nano Omni | Nemotron 3 Nano (text-only sibling) |
|---|---|---|
| **LiveCodeBench** | 63.2% | 68.3% |

Same pattern as AIME: the omnimodal model trails its text-only sibling on LiveCodeBench, per the same [technical report](https://arxiv.org/abs/2604.24954) table. No head-to-head Nano-Omni-vs-Qwen3-30B-A3B or Nano-Omni-vs-GPT-OSS-20B code benchmark has been published by NVIDIA as of this writing.

### Throughput and Multimodal

[MediaPerf](https://www.coactive.ai/blog/mediaperf-nvidia-omni) — an open benchmark from Coactive that scores multimodal models on real media-industry video tasks, reporting quality, cost, and latency together — found Nano Omni delivering the **highest throughput and lowest inference cost of any benchmarked model, open or closed**, on the video-tagging task (9.91 hours of video processed per hour, at $14.27 per unit of work), beating GPT-5.1, Gemini 3.0 Pro, and Qwen3-VL as well as other open omnimodal models. NVIDIA's own [technical report](https://arxiv.org/abs/2604.24954) cites, specifically versus **Qwen3-Omni** on a B200 GPU: up to **3x higher single-stream output token throughput**, and up to **9x higher output token throughput per GPU** at a fixed interactivity target.

These numbers reflect the architectural benefit of Mamba-2 layers: processing long video frame sequences does not incur the quadratic attention penalty that hits transformer-only competitors. (Note: a commonly repeated "3.3x faster than GPT-OSS-20B and Qwen3-30B-A3B-Thinking-2507" throughput figure comes from NVIDIA's report on the **text-only** Nemotron 3 Nano sibling, not from Nano Omni — it does not apply to the multimodal model covered here.)

---

## Where Sub-Agent Design Fits

NVIDIA explicitly positions Nano Omni as a **perception and context sub-agent**, not an orchestrator. In compound agent architectures, the model makes sense as the layer that:

1. **Ingests raw multimodal input** (a user-uploaded PDF, a screen recording, a voice note) and converts it to structured text context
2. **Performs initial analysis** (summarize, extract entities, identify anomalies)
3. **Passes context to an orchestrating model** (Claude, GPT-5.x, or similar) for decision-making and action planning

This fits a common pattern in enterprise AI systems where a specialized, efficient perception model runs locally or at low cost, and the more expensive orchestrating model only receives processed context — not raw frames or audio.

Example architecture:

```
[Raw input: video + document + voice memo]
         ↓
[Nano Omni — multimodal perception sub-agent]
         ↓ structured summary, extracted facts
[Orchestrator — Claude / GPT-5.x / internal LLM]
         ↓ decisions + tool calls
[Action layer — APIs, databases, downstream tools]
```

The benefit: Nano Omni's per-token cost is near zero (free API tiers exist), so you can process large volumes of raw multimodal input without expensive orchestrator tokens.

---

## Deployment Options

### Free API Access

| Platform | Access | Notes |
|---|---|---|
| **OpenRouter** | Free tier | [`nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`](https://openrouter.ai/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free) |
| **build.nvidia.com** | NVIDIA NIM | Hosted API endpoints are free for prototyping; production deployment requires an [NVIDIA AI Enterprise license](https://www.nvidia.com/en-us/data-center/products/ai-enterprise/get-started/) (a free 90-day evaluation license is available) |
| **fal.ai** | Available | Serverless inference, per the [NVIDIA technical blog](https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/) |

### Open Weights (Self-Hosted)

Full weights are available on [Hugging Face](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16) under NVIDIA's open model license. Review the model card for commercial use terms before deploying in a production product.

Supported inference frameworks, per the [Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16):
- **vLLM** — recommended for high-throughput server deployments
- **SGLang** — structured generation, tool-calling pipelines
- **Ollama** — local desktop or developer-workstation deployment
- **llama.cpp** — CPU-capable; useful for true edge devices

### NVIDIA NIM (Enterprise)

For production enterprise deployments, NVIDIA offers Nano Omni as a NIM microservice. Production use requires an **[NVIDIA AI Enterprise license](https://www.nvidia.com/en-us/data-center/products/ai-enterprise/get-started/)**. Per the [NVIDIA launch blog](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/), early adopters include Palantir and Foxconn (among others); Dell Technologies is listed as **evaluating** the model, not yet a confirmed production adopter.

---

## When to Use Nano Omni vs. Alternatives

| Scenario | Recommendation |
|---|---|
| Need multimodal perception at zero API cost | **Nano Omni** — free on OpenRouter and Hugging Face |
| Need to process video + audio + images in one model | **Nano Omni** — unifies all four modalities in one open-weight checkpoint at ~3B active parameters |
| Running a perception sub-agent at edge (single GPU) | **Nano Omni** — 3B active parameters, supports Ollama/llama.cpp |
| Need proprietary fine-tuning on domain video/audio | **Nano Omni** — open weights allow this |
| Need maximum raw coding or reasoning performance | Evaluate closed models (Claude, GPT-5.x); Nano Omni is strong but not at closed-frontier ceiling |
| Text-only agent with no multimodal input | Nano Omni works but Qwen3-30B-A3B or similar may offer better text-only throughput/cost tradeoffs |
| Long-context document processing (256K+) | Nano Omni supports 256K; for beyond that, check provider-specific limits |

---

## What to Watch

- **Community fine-tunes**: The open weights will attract domain-specific variants — medical imaging sub-agents, industrial video analysis models, audio transcription specialists built on Nano Omni's base.
- **Self-hosting throughput data**: Real-world vLLM benchmarks on A100/H100 will determine whether 9x throughput advantage holds on user hardware vs. NVIDIA's reference clusters.
- **License clarification**: NVIDIA's open model licenses have historically included restrictions (commercial use, redistribution). Verify the current Hugging Face model card before committing to a production build.
- **Competitor response**: At the 30B-A3B efficiency class, Qwen3-30B-A3B-Thinking and GPT-OSS-20B are the nearest text-only competitors. A true omnimodal equivalent from either family would change the landscape.

---

*This analysis is based on NVIDIA's published technical blog, the Nemotron 3 Nano technical report (arXiv), OpenRouter and DeepInfra benchmark data, and the Hugging Face model card as of April–June 2026. ChatForest researches and analyzes public sources — we do not run our own model evaluations or production deployments.*
