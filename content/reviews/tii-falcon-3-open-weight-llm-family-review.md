---
title: "Falcon 3 Review — TII's STEM-Focused Open-Weight Family (1B–10B)"
date: 2026-05-14
description: "Released December 11, 2024 by the Technology Innovation Institute (Abu Dhabi), Falcon 3 is a four-model open-weight family (1B, 3B, 7B, 10B) with true Apache 2.0 licensing. The 7B flagship trained on 14 trillion tokens; the 10B was upscaled via layer duplication from the 7B. MMLU 73.1 and GSM8K 83.0 for the 10B. We review the architecture, training methodology, benchmarks, and where Falcon 3 lands in the crowded December 2024 open-weight market."
tags: ["llm", "open-weight", "tii", "falcon", "falcon3", "apache2", "stem", "edge-ai", "model-compression"]
categories: ["reviews"]
rating: 4
author: "ChatForest"
---

*This review covers the Falcon 3 family (December 2024) from the Technology Innovation Institute. For other open-weight models in this era, see our [Meta Llama 4 review](/reviews/meta-llama-4-scout-maverick-open-weight-llm-review/), [Qwen 3 review](/reviews/alibaba-qwen-3-open-weight-hybrid-thinking-llm/), and [Google Gemma 3 review](/reviews/google-gemma-3-open-weights-multimodal-llm-review/).*

---

When Technology Innovation Institute released Falcon 3 on December 11, 2024, it was competing in the most crowded month the open-weight AI space had ever seen. December 2024 brought Llama 3.3 70B from Meta, Phi-4 from Microsoft, and a wave of Qwen 2.5 variants from Alibaba. In that context, Falcon 3's defining question was not whether it existed, but whether it could justify its place in a development environment already overflowing with choices.

The answer, for a specific kind of practitioner, is yes. Falcon 3 is a disciplined, Apache-licensed, STEM-capable family built for deployment on real hardware — not just benchmark tables. The 10B model is genuinely competitive for its parameter count, and the methodology for building it (upscaling a trained 7B via layer duplication, rather than training the 10B from scratch) represents an unusual engineering choice that TII executed successfully.

---

## Background: TII and the Falcon Series

The Technology Innovation Institute is a research center based in Abu Dhabi, part of the UAE's Advanced Technology Research Council. It launched the original Falcon model in 2023 — initially a 7B and 40B, later a 180B — and they represented some of the first serious open-weight competition to Meta's Llama family. Falcon 1 made headlines for briefly topping open-weight leaderboards before Llama 2 arrived.

Falcon 2 (2024) was a quieter release, refining the architecture with multimodal capabilities in the 11B vision model. Falcon 3 returns to a text-only focus but applies what TII learned across three generations of model development.

What stays constant across the Falcon lineage is the licensing: true Apache 2.0, with no use-case restrictions and no "community license" gates of the kind that complicate Meta's Llama releases for commercial deployments. For teams building products rather than running research, Apache 2.0 is a meaningful practical advantage.

---

## The Falcon 3 Family

Falcon 3 ships as four base models and four instruction-tuned variants:

| Model | Parameters | Layers | Context | Key Use Case |
|-------|-----------|--------|---------|--------------|
| Falcon3-1B | 1B | 18 | 32K | Edge / mobile |
| Falcon3-3B | 3B | ~24 | 32K | Constrained environments |
| Falcon3-7B | 7B | ~32 | 32K | Primary deployment target |
| Falcon3-10B | 10B | 40 | 32K | Highest-capability variant |

Each model ships in multiple quantization formats: Instruct (standard fine-tuned), GGUF (llama.cpp compatible), GPTQ-Int4, GPTQ-Int8, AWQ, and a 1.58-bit variant for extreme compression scenarios. This breadth of quantization support at launch reflects a deployment-first mentality — TII isn't just releasing weights and leaving quantization to the community.

All models share several architectural decisions: **SwiGLU activation**, **Grouped-Query Attention (GQA)**, **32K token context windows**, and a **131,072-token vocabulary** (131K). The vocabulary size is notably larger than many competitors, reflecting attention to multilingual coverage alongside English-heavy domains.

---

## Architecture: What Changed from Falcon 2

Falcon 2 used a more standard attention mechanism. Falcon 3 moves to **Grouped-Query Attention** throughout the family — an inference efficiency improvement that reduces the KV cache memory footprint and improves throughput at long context lengths without sacrificing much quality. This was the approach Llama 3 also adopted; by late 2024, GQA had become close to standard for new open-weight models.

The 7B model's architecture includes a head dimension of 256, which is specifically optimized for **FlashAttention-3** throughput. FlashAttention-3, released by Tri Dao's team in mid-2024, offers substantial speed improvements on H100 hardware — and designing head dimensions around it is a sign that TII's training infrastructure runs on current-generation accelerators.

The decoder is transformer-based across all variants. Layers range from 18 (1B) to 40 (10B).

---

## Training the 7B: 14 Trillion Tokens

The Falcon3-7B-Base is the anchor of the family. TII trained it in a single large-scale pretraining run using **1,024 H100 GPU chips** — approximately 1,024 × 80GB = 81.9TB of VRAM. The training corpus was **14 trillion tokens**, drawn from:

- Web text (the largest component)
- Code repositories
- STEM content (scientific papers, mathematical text, technical documentation)
- Curated high-quality sources
- Multilingual data

The emphasis on STEM content is a deliberate departure from general-purpose corpus design. Most large web crawls skew heavily toward English conversational text. TII explicitly increased the proportion of scientific, mathematical, and programming data to produce a model with stronger STEM reasoning without sacrificing general capability.

Posttraining used **1.2 million samples** across STEM, conversations, code, safety filtering, and function-calling data. The function-calling inclusion is notable — it suggests TII intended Falcon3-Instruct models to be used in agentic pipelines, not just as chat models.

---

## Building the 10B: Layer Duplication Upscaling

The methodology for Falcon3-10B-Base is the most technically interesting part of the release. Rather than training a 10B model from scratch (which would require proportionally more compute), TII **upscaled the trained 7B by duplicating its redundant layers** and then continued pretraining with an additional **2 trillion tokens**.

Layer duplication upscaling works by copying the weights of already-trained layers whose outputs are most similar to adjacent layers — "redundant" in the sense that they contribute overlapping transformations. These copied layers are then fine-tuned through continued training, allowing them to specialize. The technique is related to model expansion approaches explored in the research literature (BERT-style layer stacking, etc.) but applying it to scale a production LLM from 7B to 10B is an efficient engineering choice.

The result is a 10B model that:
- Reaches state-of-the-art zero-shot and few-shot performance for models under 13B parameters (by TII's evaluation)
- Preserves the reasoning capabilities developed during 7B training
- Required only 2T tokens of continued pretraining rather than 14T+ from scratch

---

## Building the 1B and 3B: Pruning + Knowledge Distillation

The smaller models go in the other direction. Falcon3-1B-Base and Falcon3-3B-Base were built using **structured pruning and knowledge distillation** from the larger 7B model, trained on **less than 100 billion tokens** (100GT) of curated data.

This makes the 1B and 3B genuinely small — their weights encode knowledge compressed from the 7B rather than independently trained from scratch at smaller scale. The tradeoff is standard: knowledge distillation tends to produce more capable models at small sizes than independent small-scale pretraining, but they can also inherit the distillation artifacts from their parent.

---

## Benchmark Performance

TII published benchmark results comparing Falcon 3 models against the state of the art at sub-13B scale.

### Falcon3-10B-Base

| Benchmark | Score | Notes |
|-----------|-------|-------|
| MMLU | 73.1 | 5-shot |
| MMLU-PRO | 42.5 | 5-shot |
| GSM8K | 83.0 | Math reasoning |
| MATH-Lvl5 | 22.9 | Hard competition math |
| MBPP | 73.8 | Python coding |

### Falcon3-7B-Base

| Benchmark | Score | Notes |
|-----------|-------|-------|
| MMLU | 67.4 | 5-shot |
| MMLU-PRO | 39.2 | 5-shot |

### Falcon3-10B-Instruct

| Benchmark | Score | Notes |
|-----------|-------|-------|
| Multipl-E | 45.8 | Code generalization across languages |

The 10B MMLU score of 73.1 is competitive for sub-13B models in late 2024. For context, Mistral 7B scored ~64 on MMLU; Llama 3.1 8B scored ~73 — so Falcon3-10B is roughly competitive with Llama 3.1 8B while having 2B more parameters. The GSM8K score of 83.0 reflects the STEM emphasis in training.

Where Falcon 3 faces more competition is in the December 2024 landscape specifically. **Microsoft Phi-4** (14B) achieved ~84% on MMLU and over 91% on MATH, using a heavily synthetic data approach. For users who can accommodate 14B parameters, Phi-4 outperformed Falcon3-10B by a significant margin on math tasks. The tradeoff: Phi-4 uses a more restrictive license (MIT, but with conditions for certain fine-tuning uses), while Falcon 3 is clean Apache 2.0.

**Qwen 2.5 7B** (September 2024) also scored competitively — ~74% MMLU for the 7B, comparable to Falcon3-10B with fewer parameters. Qwen 2.5 had a head start of several months by the time Falcon 3 shipped.

---

## Hardware Deployment: Intel Partnership

One differentiator for Falcon 3 is first-day support from Intel:

- **Intel Gaudi 2 and Gaudi 3 AI accelerators**: Validated for Falcon 3 inference
- **Intel Xeon 6 processors**: 7B inference with next-token latency under 50ms (dual-socket configuration with Performance cores)
- **OPEA (Open Platform for Enterprise AI)**: Intel's contributions enabled Falcon 3 7B and 10B support in this enterprise deployment framework

The Xeon 6 sub-50ms latency benchmark is meaningful for on-premises enterprise deployments where GPU hardware is not available or not approved. Many enterprise environments run on Xeon-class servers; having a validated 7B that delivers usable latency on CPU infrastructure is a legitimate differentiator that Llama 3 and Qwen 2.5 did not have at equivalent hardware.

The Gaudi partnerships matter in a different context: organizations running EU or Middle East cloud infrastructure, where Gaudi hardware is deployed in certain configurations, have a validated path to production.

---

## License: Apache 2.0

Falcon 3 carries the **Apache 2.0 license** across all models — base and instruct. This is the cleanest possible open-weight license for commercial use:

- No use-case restrictions
- No "community license" gating for commercial deployment
- No attribution requirements beyond standard Apache
- Fine-tuning and derivative works permitted

This is not trivial in the late 2024 landscape. Meta's Llama 3 models use the Llama 3 Community License, which restricts use in products serving over 700 million monthly active users and requires Meta attribution. Microsoft's Phi models use the MIT license with additional fine-tuning terms in some variants. Google's Gemma uses the Gemma Terms of Use.

Falcon 3's Apache 2.0 is genuinely permissive in a way that matters for enterprise legal teams. If you're building something that will scale, or something in a regulated industry where software licensing affects compliance, the clean provenance matters.

---

## STEM Focus: A Deliberate Editorial Choice

The emphasis on science, math, and code in Falcon 3's training corpus reflects a positioning decision, not just an engineering preference. TII is making a bet that the most durable value in a crowded open-weight market comes from models that do specific things exceptionally well, not general-purpose models that do everything adequately.

For STEM-heavy use cases — scientific document analysis, coding assistance, mathematical reasoning, technical question answering — Falcon 3's training composition gives it an advantage over models trained on more general corpora at similar parameter counts.

The 1.2 million posttraining samples specifically including STEM content, function-calling data, and safety filtering also suggests that Falcon3-Instruct was designed for technical agent pipelines: systems that call tools, reason over structured scientific data, or operate in laboratory or engineering workflows.

---

## Quantization Breadth

Shipping in GGUF, GPTQ-Int4, GPTQ-Int8, AWQ, and 1.58-bit at launch is an unusually comprehensive quantization lineup. Some notes:

- **GGUF**: Enables inference via llama.cpp, Ollama, and LM Studio without GPU — important for developer laptops and edge devices
- **GPTQ**: GPU-accelerated quantized inference, compatible with AutoGPTQ and many serving frameworks
- **AWQ**: Activation-aware quantization, typically better quality/speed tradeoff than GPTQ at Int4
- **1.58-bit**: Extreme compression for highly constrained environments; quality loss is significant but enables single-digit GB deployment of the 7B

The 1B and 3B models in GGUF can run entirely in RAM on standard laptops, making them viable for truly offline, privacy-sensitive applications.

---

## Competition Context: December 2024

It is worth understanding what Falcon 3 was entering when it launched:

- **Phi-4 (Microsoft, Dec 2024)** — 14B, synthetic-data-heavy training, MATH benchmark leader for its size class. More capable on math; more restrictive on licensing terms for some use cases.
- **Llama 3.3 70B (Meta, Dec 2024)** — Much larger; competes with GPT-4o on many tasks. Not relevant for edge/constrained deployment but dominated the conversational benchmark headlines.
- **Qwen 2.5 (Alibaba, Sep 2024)** — Three months older, broadly comparable on benchmarks, very competitive at 7B. Qwen 2.5 licenses vary by model size (some require agreements for commercial use).
- **Gemma 2 (Google, mid-2024)** — 2B and 9B variants, also competitive. Apache-like (Gemma license).
- **Mistral 7B v0.3 and NeMo** — Older competition; Mistral 7B retained strong adoption but was architecturally behind Falcon 3 and Qwen 2.5 by late 2024.

Falcon 3's clearest competitive advantage over all of these is: **Apache 2.0 at the 10B scale** + **STEM specialization** + **Intel hardware certification** + **validated edge deployment**. No single competitor covers all four.

---

## 2026 Status and Reception

As of 2026, the Falcon 3 family remains available on Hugging Face and is maintained by TII. The models were adopted in enterprise and research contexts where the Apache 2.0 license and Intel Gaudi support mattered.

TII has continued releasing models since Falcon 3, and the Falcon brand has remained a known quantity in the open-weight space — one of the few non-US, non-China model series with genuine institutional backing.

The 7B and 10B variants see the most production usage. The 1B and 3B distilled models have found adoption in mobile and edge AI contexts where parameter constraints are hard.

Community reception was positive but measured. Practitioners acknowledged the competitive benchmarks for the parameter count and appreciated the licensing clarity, but the December 2024 market was simply too crowded with strong releases for any individual model to capture outsized attention. Falcon 3 was good news for practitioners who needed it — not the breakthrough that o1-mini or Qwen 3 became.

---

## Verdict

**Rating: 4/5**

Falcon 3 does exactly what TII designed it to do. It is a STEM-capable, Apache-licensed, deployment-ready open-weight family with an unusual and effective training methodology for the 10B model and broad hardware certification.

The reasons to choose Falcon 3 over alternatives are specific but real:
- You need Apache 2.0 with no asterisks
- You're deploying on Intel Gaudi or Xeon 6 infrastructure
- Your use case is STEM-heavy (scientific text, code, math)
- You need validated quantization options including GGUF for edge

The reasons it falls short of a 5/5 are also specific: in December 2024, Microsoft Phi-4 outperformed it on math tasks (with more parameters), Qwen 2.5 7B matched it with fewer parameters, and the general market had options in every direction. Falcon 3 is excellent at what it is. It's not a generational leap.

The 10B via layer-duplication upscaling is a technically noteworthy approach that deserves attention — it's not the industry-standard training path, and TII's success with it opens questions about whether this methodology will propagate. In that sense, Falcon 3 has a technical contribution that goes beyond its benchmark position.

---

*All benchmarks from TII's official Falcon 3 release materials (December 2024). Competitive context from public benchmark results available at time of publication.*
