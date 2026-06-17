---
title: "NVIDIA Nemotron 3 Nano Omni: A 3B-Active Omnimodal Sub-Agent That Runs on Any GPU — Builder Guide"
date: 2026-06-17
description: "Nemotron 3 Nano Omni is a 30B Mamba-Transformer MoE model with only 3B active parameters per token, designed as a multimodal perception sub-agent. It natively processes text, image, video, and audio in a single model. Available free on Hugging Face and OpenRouter."
og_description: "NVIDIA Nemotron 3 Nano Omni — 30B MoE, 3B active, omnimodal (text + image + video + audio), 89.1% AIME, 68.3% LiveCodeBench, 9x throughput vs competing omnimodal models, free open weights. Builder guide: architecture, benchmarks, pricing, sub-agent design patterns."
content_type: "Builder's Log"
categories: ["Open Source Models", "Agents", "Developer Tools", "LLMs", "Multimodal"]
tags: ["nvidia", "nemotron", "nemotron-3-nano-omni", "mamba", "moe", "omnimodal", "multimodal", "open-weights", "sub-agent", "edge-ai", "builder-guide", "2026", "agentic", "nim"]
---

On April 28, 2026, NVIDIA released **Nemotron 3 Nano Omni** — a 30B-parameter hybrid Mamba-Transformer Mixture of Experts model that unifies text, image, video, and audio understanding in a single open-weight checkpoint. It is designed explicitly as a perception and reasoning sub-agent in compound AI systems, and it costs nothing to access: the weights are free on Hugging Face, and the API is free on OpenRouter.

The technical headline is unusual: 31.6 billion total parameters, but only ~3.2–3.6 billion active per forward pass. That active-parameter count is what determines inference cost — making Nano Omni one of the most compute-efficient omnimodal models available in 2026.

This guide covers the architecture, benchmarks, deployment options, and agentic use cases for builders evaluating Nano Omni as a component in multi-agent systems.

---

## The One-Sentence Summary

Nemotron 3 Nano Omni is a 30B-total/3B-active Mamba-Transformer MoE model that accepts text, images, video, and audio as input, achieves 89.1% on AIME 2025 without tools (99.2% with Python), tops LiveCodeBench v6 among models in its efficiency class, and is available as open weights and free API — built specifically to serve as the multimodal perception layer in compound agent architectures.

---

## Why This Matters for Builders

Three constraints have historically made omnimodal agents expensive or impractical:

| Problem | Previous workaround | Nano Omni approach |
|---|---|---|
| Separate model stacks per modality | Run vision model + audio model + LLM in sequence | Single model handles all modalities in one reasoning pass |
| Omnimodal = slow | Accept high latency or sacrifice quality | Mamba layers eliminate the quadratic attention bottleneck |
| Frontier capability = large active footprint | Use a 70B+ dense model or pay closed-model API rates | MoE routing keeps active parameters at ~3B |

If you are building a system that needs to reason across a video transcript, an uploaded image, a voice memo, and a text document in the same context window — and you want to do this affordably, with open weights, on-premise — Nano Omni is the first model that addresses all four constraints simultaneously.

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

Total: 52 layers. Model dimension: 2688. Query heads: 32. KV heads: 2. Head dimension: 128.

### Why MoE?

The 31.6B total parameters are divided among 128 routed experts per MoE layer. Each forward pass activates only 6 of those 128 experts per token (plus shared experts that activate on every token). The result: ~3.2–3.6 billion parameters active per inference call — a compute cost comparable to a small dense model, with capacity comparable to a much larger one.

The practical implication: Nano Omni can run inference on a single high-end GPU (A100 80GB or equivalent) rather than requiring multi-GPU tensor parallelism. This matters for edge agents and on-premise deployments where multi-node infrastructure is not available.

### Omnimodal: Native, Not Adapted

Most multimodal models attach vision or audio via an adapter trained on a frozen language backbone. Nano Omni integrates all modalities from training step zero — there is no seam between the vision encoder, audio processor, and language reasoning. This matters for tasks that require cross-modal reasoning: interpreting a chart from a screenshot while writing code to reproduce it, or summarizing a video while citing timestamps in a document.

**Accepted inputs:**
- Text (up to 256K token context window)
- Images (static)
- Video (multi-frame)
- Audio

**Output:** Text only.

---

## Benchmarks in Context

### Math and Reasoning

| Benchmark | Nano Omni | Qwen3-30B-A3B | GPT-OSS-20B |
|---|---|---|---|
| **AIME 2025 (no tools)** | 89.1% | 85.0% | 91.7% |
| **AIME 2025 (+ Python)** | **99.2%** | — | — |

Without tool assistance, Nano Omni slots between Qwen3-30B-A3B and GPT-OSS-20B on hard competition math. With Python interpreter access, it reaches 99.2% — strong evidence that the model is well-trained for tool-augmented reasoning loops, not just standalone generation.

### Code

| Benchmark | Nano Omni | Qwen3-30B-A3B | GPT-OSS-20B |
|---|---|---|---|
| **LiveCodeBench v6** | **68.3%** | 66.0% | 61.0% |

Nano Omni tops both Qwen3-30B-A3B and GPT-OSS-20B at this efficiency tier on LiveCodeBench v6, which tests competitive programming problems from recent contests.

### Throughput and Multimodal

The MediaPerf benchmark — an industry benchmark measuring throughput, cost, and quality across video understanding tasks — shows Nano Omni achieving the **highest throughput and lowest inference cost** for video-level tagging across competing omnimodal models. NVIDIA cites 9x higher throughput overall versus competing open omnimodal models.

For inference throughput versus the closest text-capable competitors:

- **3.3x higher throughput** than GPT-OSS-20B
- **3.3x higher throughput** than Qwen3-30B-A3B-Thinking-2507

These numbers reflect the architectural benefit of Mamba-2 layers: processing long video frame sequences does not incur the quadratic attention penalty that hits competing models.

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
| **OpenRouter** | Free tier | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` |
| **build.nvidia.com** | NVIDIA NIM | Free for evaluation; Enterprise license for production |
| **fal.ai** | Available | Serverless inference |

### Open Weights (Self-Hosted)

Full weights are available on Hugging Face under NVIDIA's open license. Review the model card for commercial use terms before deploying in a production product.

Supported inference frameworks:
- **vLLM** — recommended for high-throughput server deployments
- **SGLang** — structured generation, tool-calling pipelines
- **Ollama** — local desktop or developer-workstation deployment
- **llama.cpp** — CPU-capable; useful for true edge devices

### NVIDIA NIM (Enterprise)

For production enterprise deployments, NVIDIA offers Nano Omni as a NIM microservice — containerized, optimized, with SLA guarantees. Requires an **NVIDIA AI Enterprise license**. Partners including Palantir, Foxconn, and Dell have adopted the NIM deployment path.

---

## When to Use Nano Omni vs. Alternatives

| Scenario | Recommendation |
|---|---|
| Need multimodal perception at zero API cost | **Nano Omni** — free on OpenRouter and Hugging Face |
| Need to process video + audio + images in one model | **Nano Omni** — no other open model unifies all four modalities at this efficiency |
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
