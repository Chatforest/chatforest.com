---
title: "Gemma 4: Google's Open-Weights Models Deliver a 13x Jump in Agentic Performance"
date: 2026-04-07T18:00:00+09:00
description: "Google released Gemma 4 on April 2, 2026 — four open-weights models (2B to 31B parameters) under Apache 2.0, with native function calling, 256K context, multimodal input (text/image/audio/video), and a τ2-bench agentic score of 86.4% vs. Gemma 3's 6.6%. The 26B MoE variant runs with only 3.8B active parameters, making production-grade agentic AI viable on consumer hardware."
content_type: "Guide"
card_description: "Google released Gemma 4 on April 2, 2026 — a family of four open-weights models under Apache 2.0. The headline number: on τ2-bench (agentic tool use), Gemma 4 31B scores 86.4% compared to Gemma 3 27B's 6.6%. That's not an incremental improvement — it's a generational leap that makes open-weights models competitive with proprietary systems for agentic workflows. The lineup includes a 31B dense model (256K context, Codeforces ELO 2150), a 26B MoE with only 3.8B active parameters matching the 31B on most benchmarks, and edge variants (E2B, E4B) that run on phones and Raspberry Pi. Native function calling, structured JSON output, and system prompt support make these models ready for MCP tool integration out of the box. This guide covers the architecture, benchmarks, agentic capabilities, competitive positioning against Llama 4 and Qwen 3.5, and what this release means for the MCP ecosystem."
last_refreshed: 2026-04-15
---

Google [announced Gemma 4](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/) on April 2, 2026 — four open-weights models that redefine what's possible with locally-deployed AI agents. The most important number isn't a benchmark score on a leaderboard. It's this: on [τ2-bench](https://deepmind.google/models/gemma/gemma-4/), which measures real-world agentic tool use, Gemma 4 31B scores 86.4%. Its predecessor, Gemma 3 27B, scored 6.6%.

That 13x improvement means open-weights models can now handle multi-step tool calling, reasoning about which tools to invoke, and sequencing complex workflows — capabilities that previously required proprietary models. For anyone building with [MCP](/guides/what-is-mcp/), this matters.

This guide covers the architecture, benchmarks, agentic capabilities, and competitive positioning. Our analysis draws on Google's [official announcement](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/), the [Google Developers Blog](https://developers.googleblog.com/bring-state-of-the-art-agentic-skills-to-the-edge-with-gemma-4/), [DeepMind's model page](https://deepmind.google/models/gemma/gemma-4/), the [model card](https://ai.google.dev/gemma/docs/core/model_card_4), coverage from [The Register](https://www.theregister.com/2026/04/02/googles_gemma_4_open_weights/), and independent analysis — we research and analyze rather than testing models hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

---

## The Four Models

Gemma 4 ships as [four variants](https://ai.google.dev/gemma/docs/core/model_card_4), each targeting a different deployment scenario:

| Variant | Total Params | Active Params | Context | Modalities | Architecture |
|---------|-------------|---------------|---------|------------|-------------|
| **E2B** | 5.1B | 2.3B | 128K | Text, Image, Audio, Video | Dense |
| **E4B** | 8B | 4.5B | 128K | Text, Image, Audio, Video | Dense |
| **26B MoE** | 25.2B | 3.8B | 256K | Text, Image | MoE (8 active / 128 total + 1 shared) |
| **31B Dense** | 30.7B | 30.7B | 256K | Text, Image | Dense |

The MoE variant is the efficiency story. With [128 expert layers but only 8 active per token](https://huggingface.co/blog/gemma4) (plus one shared), the 26B model matches the 31B on most benchmarks while using only 3.8B active parameters during inference — [achieving 97% of the 31B's quality at ~8x less compute](https://ai.rs/ai-developer/gemma-4-vs-qwen-3-5-vs-llama-4-compared). That makes it practical to run on hardware where the 31B dense model would be too expensive.

### Architecture Details

All variants use a [hybrid attention mechanism](https://huggingface.co/blog/gemma4) that interleaves local sliding window attention with full global attention. The sliding window is [512 tokens for edge models and 1024 for the larger variants](https://ai.google.dev/gemma/docs/core/model_card_4). Vision encoding uses [~150M parameters on edge models and ~550M on the 26B/31B](https://ai.google.dev/gemma/docs/core/model_card_4). The E2B and E4B add a ~300M parameter audio encoder, supporting speech recognition and translation for clips up to 30 seconds, plus video understanding up to 60 seconds.

The entire family is [built from Gemini 3 research and technology](https://deepmind.google/models/gemma/gemma-4/). The larger models don't support audio — a curious gap that suggests Google is prioritizing vision quality at the 26B+ scale while audio support matures.

---

## Benchmark Performance

### Core Benchmarks

| Benchmark | E2B | E4B | 26B MoE | 31B Dense |
|-----------|-----|-----|---------|-----------|
| MMLU Pro | 60.0% | 69.4% | 82.6% | 85.2% |
| AIME 2026 (math) | 37.5% | 42.5% | 88.3% | 89.2% |
| LiveCodeBench v6 | 44.0% | 52.0% | 77.1% | 80.0% |
| Codeforces ELO | 633 | 940 | 1718 | 2150 |
| GPQA Diamond (science) | 43.4% | 58.6% | 82.3% | 84.3% |
| BigBench Extra Hard | 21.9% | 33.1% | 64.8% | 74.4% |
| MMMLU (multilingual) | 67.4% | 76.6% | 86.3% | 88.4% |

### Vision

| Benchmark | E2B | E4B | 26B MoE | 31B Dense |
|-----------|-----|-----|---------|-----------|
| MMMU Pro | 44.2% | 52.6% | 73.8% | 76.9% |
| MATH-Vision | 52.4% | 59.5% | 82.4% | 85.6% |

### Arena Rankings

On [Arena AI (text)](https://deepmind.google/models/gemma/gemma-4/), the 31B dense scores an ELO of 1452 and the 26B MoE scores 1441. For context, Qwen 3.5 27B sits at 1403 and DeepSeek-V3.2 at approximately 1425. The 31B currently [ranks #3 among open models](https://siliconangle.com/2026/04/02/googles-new-gemma-4-models-bring-complex-reasoning-skills-low-power-devices/) on the Arena AI text leaderboard.

---

## The Agentic Breakthrough

This is where Gemma 4 changes the conversation.

### τ2-bench: From 6.6% to 86.4%

[τ2-bench](https://deepmind.google/models/gemma/gemma-4/) measures a model's ability to use tools in realistic multi-step scenarios — selecting the right tools, calling them in the correct sequence, handling errors, and completing complex tasks. Gemma 3 27B scored 6.6%. Gemma 4 31B scores 86.4%, with the [26B MoE close behind at 85.5%](https://huggingface.co/blog/gemma4).

This isn't a benchmark where models were already doing well and Gemma improved incrementally. Gemma 3 effectively couldn't do agentic tool use at a practical level. Gemma 4 can. The coding leap is equally dramatic: [Codeforces ELO went from 110 (Gemma 3 27B) to 2150 (Gemma 4 31B)](https://huggingface.co/blog/gemma4). Combined with a "thinking mode" for step-by-step reasoning, the 31B becomes a viable backbone for autonomous agent workflows.

### Native Function Calling

Gemma 4 ships with [built-in function calling support](https://ai.google.dev/gemma/docs/capabilities/text/function-calling-gemma4) — no fine-tuning required. The model uses [6 dedicated control tokens](https://ai.google.dev/gemma/docs/capabilities/text/function-calling-gemma4) (`<|tool>`, `<|tool_call>`, `<|tool_response>`, and their closing variants) to structure tool interactions. The model can:

- Parse tool definitions and select appropriate tools for a given task
- Generate structured JSON output for tool invocations
- Handle multi-turn tool-use conversations where results feed back into reasoning
- Follow native system instructions that define agent behavior boundaries

This matters for MCP integration. An MCP client backed by Gemma 4 can discover available tools from an MCP server and invoke them with structured parameters, following the same pattern that proprietary models use. The constrained decoding ensures outputs remain valid JSON, reducing the parsing failures that plagued earlier open models in tool-calling scenarios.

### Edge Deployment for Agentic AI

The E2B and E4B variants make on-device agents practical. Per the [Google Developers Blog](https://developers.googleblog.com/bring-state-of-the-art-agentic-skills-to-the-edge-with-gemma-4/):

- **Raspberry Pi 5 (CPU):** 133 prefill tokens/s, 7.6 decode tokens/s
- **Qualcomm Dragonwing IQ8 (NPU):** 3,700 prefill tokens/s, 31 decode tokens/s
- **Mobile:** 4,000 input tokens across 2 distinct skills processed in under 3 seconds
- **Memory:** E2B runs in [under 1.5GB RAM](https://developers.googleblog.com/bring-state-of-the-art-agentic-skills-to-the-edge-with-gemma-4/) with 2-bit quantization

These aren't demo numbers. A Raspberry Pi running the E2B can serve as a local MCP client that processes sensor data, calls tools, and takes actions — a genuine edge agent, not a cloud proxy. Google has also announced [Android AICore Developer Preview](https://android-developers.googleblog.com/2026/04/AI-Core-Developer-Preview.html) with native Gemma 4 support, signaling a push toward on-device agentic AI on Android.

---

## Competitive Positioning

### vs. Llama 4

Meta's Llama 4 leads on context length (10M tokens vs. Gemma 4's 256K) and offers larger models at the top end. But Gemma 4's MoE efficiency (3.8B active parameters matching 31B quality) gives it the edge for resource-constrained deployments. On [GPQA Diamond, Gemma 4 31B scores 84.3% vs. Llama 4 Scout's 74.3%](https://ai.rs/ai-developer/gemma-4-vs-qwen-3-5-vs-llama-4-compared). Licensing also differs: Gemma 4's Apache 2.0 has no restrictions, while [Llama 4's community license imposes a 700M monthly active user threshold](https://ai.rs/ai-developer/gemma-4-vs-qwen-3-5-vs-llama-4-compared).

### vs. Qwen 3.5

Qwen 3.5's 397B flagship operates in a different class entirely. At the ~30B tier, Gemma 4 31B edges out Qwen 3.5 27B on Arena ELO (1452 vs. 1403) and most benchmarks. Qwen's MoE variant (Qwen 3.5 235B A22B) offers more active parameters but requires significantly more hardware.

### vs. DeepSeek

DeepSeek-V3.2 scores approximately 1425 on Arena ELO compared to Gemma 4 31B's 1452. Google [explicitly positions Gemma 4 as a competitive response to Chinese open-weights models](https://www.theregister.com/2026/04/02/googles_gemma_4_open_weights/) from Moonshot AI, Alibaba, and Z.AI — a geopolitical angle that matters for enterprise procurement decisions.

### The License Shift

Previous Gemma releases used a restrictive license that prohibited certain uses and reserved Google's right to terminate access. Gemma 4 ships under **Apache 2.0** — the same permissive license used by most open-source infrastructure. As [VentureBeat argues](https://venturebeat.com/technology/google-releases-gemma-4-under-apache-2-0-and-that-license-change-may-matter-more-than-benchmarks), this license change "may matter more than benchmarks" — it removes the legal uncertainty that made enterprises hesitate on earlier Gemma versions. No usage restrictions, no termination clauses, no ambiguity.

---

## What This Means for the MCP Ecosystem

### Self-Hosted MCP Agents Become Viable

The combination of strong agentic benchmarks, [native function calling](https://ai.google.dev/gemma/docs/capabilities/text/function-calling-gemma4), and [Apache 2.0 licensing](https://venturebeat.com/technology/google-releases-gemma-4-under-apache-2-0-and-that-license-change-may-matter-more-than-benchmarks) means organizations can now build MCP-based agent systems without depending on proprietary API providers. A 26B MoE model running on a single GPU can serve as the reasoning engine for an MCP client that connects to enterprise tool servers — no API keys, no usage-based billing, no data leaving the network.

This is particularly relevant for enterprises with strict data residency requirements. Pinterest's [production MCP deployment](/guides/pinterest-mcp-production-case-study/) processes 66,000 invocations monthly through cloud-hosted servers — but some organizations can't send queries to external LLM providers. Gemma 4 makes fully on-premises MCP architectures practical.

### Edge Agents Get Real

The E2B running on a Raspberry Pi with MCP tool-calling opens use cases that cloud-dependent agents can't serve: factory floor automation, field service tools, offline-capable assistants, and IoT orchestration. With 128K context and under 1.5GB RAM at 2-bit quantization, these agents can maintain substantial conversation history while operating on hardware that costs under $100.

### The Open-Weights Agentic Gap Closes

Six months ago, agentic workflows required proprietary models. The τ2-bench numbers show that gap has closed for the 31B class. This will accelerate MCP adoption in environments where proprietary model dependencies were the blocker — government, healthcare, financial services, and defense.

---

## Hardware Requirements

| Model | Unquantized (FP16) | 4-bit Quantized |
|-------|-------------------|-----------------|
| 31B Dense | [Single 80GB H100](https://www.theregister.com/2026/04/02/googles_gemma_4_open_weights/) | [24GB GPU (RTX 4090, RX 7900 XTX)](https://www.theregister.com/2026/04/02/googles_gemma_4_open_weights/) |
| 26B MoE | Similar to 31B (sparse activation reduces compute, not memory for weights) | 24GB GPU |
| E4B | Consumer GPU / high-end phone | CPU or mobile NPU |
| E2B | Raspberry Pi 5 | Any modern device |

Supported inference frameworks include [vLLM, SGLang, Llama.cpp, MLX, mistral.rs, transformers.js, ONNX](https://huggingface.co/blog/gemma4), [Ollama](https://ollama.com/library/gemma4), and over a dozen others with day-one support.

---

## Honest Limitations

- **No audio on larger models.** The 26B and 31B only handle text and image input. Audio and video support is limited to the smaller E2B and E4B variants, which have substantially lower benchmark scores.
- **Long-context performance drops.** On [MRCR v2 (8-needle, 128K context)](https://huggingface.co/blog/gemma4), the 31B scores only 66.4% and the 26B MoE drops to 44.1% — decent but not exceptional. Real-world RAG and document analysis at full context length may underperform expectations.
- **Training cutoff: [January 2025](https://ai.google.dev/gemma/docs/core/model_card_4).** Over a year of stale knowledge. Agents using these models will need retrieval or tool access for current information.
- **Agentic benchmarks are synthetic.** τ2-bench is a good proxy for tool use, but production agentic deployments surface failure modes (timeout handling, partial results, cascading errors) that benchmarks don't capture.
- **MoE memory paradox.** The 26B MoE uses only 3.8B active parameters for compute, but all 25.2B parameters must be loaded into memory. Inference is fast, but memory requirements are similar to the 31B dense model.
- **"Open weights" ≠ open source.** The training data, training code, and fine-tuning recipes are not released. Apache 2.0 covers the weights, not the reproduction pipeline. Nathan Lambert's [analysis of what makes an open model](https://www.interconnects.ai/p/gemma-4-and-what-makes-an-open-model) explores this distinction in depth.

---

## Summary

Gemma 4 represents the moment open-weights models became serious options for agentic AI. The τ2-bench jump from 6.6% to 86.4% isn't a marketing number — it reflects a genuine capability shift that makes self-hosted MCP agents viable for the first time. The Apache 2.0 license removes the last major adoption barrier.

For the MCP ecosystem, this creates a new deployment tier: organizations that want the security and cost benefits of on-premises AI can now pair Gemma 4 with [MCP servers](/guides/what-is-mcp/) and get competitive agentic performance without external API dependencies.

The models are available now on [Hugging Face](https://huggingface.co/collections/google/gemma-4), [Ollama](https://ollama.com/library/gemma4), [Kaggle](https://kaggle.com), [LM Studio](https://lmstudio.ai), and [Docker](https://docker.com), with framework support from vLLM, SGLang, JAX, Keras, and Google AI Edge. Fine-tuning is supported via [TRL, Vertex AI, and Unsloth Studio](https://huggingface.co/blog/gemma4).

---

*This guide will be updated as community benchmarks and production deployment reports emerge. Last updated April 15, 2026.*

## Related Guides

- [What Is MCP?](/guides/what-is-mcp/) — introduction to the Model Context Protocol and how AI agents connect to tools
- [AI Agent SDKs in 2026](/guides/mcp-agent-sdks-2026/) — comparison of frameworks for building AI agents, including model selection
- [MCP Dev Summit 2026](/guides/mcp-dev-summit-2026-guide/) — key sessions and themes from the first MCP conference, including SDK V2 and cross-platform interoperability
- [Holo3: H Company's Open MoE Model Sets OSWorld Record](/guides/holo3-desktop-agent-osworld-record/) — another open MoE model pushing agentic boundaries
- [Meta's AI Crisis: The Death of Fully Open Source](/guides/meta-ai-crisis-alexandr-wang-open-source-pivot/) — Meta abandoning fully open-source AI means Gemma and other partially open models become more important to the open ecosystem
