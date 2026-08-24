---
title: "Falcon 3 Review — TII's STEM-Focused Open-Weight Family (1B–10B + Mamba)"
date: 2026-05-14
description: "Released December 17, 2024 by the Technology Innovation Institute (Abu Dhabi), Falcon 3 is a five-model open-weight family (1B, 3B, 7B, 10B, plus a Mamba-7B SSM variant) under TII's Apache-2.0-derived Falcon-LLM License (permissive, but with an Acceptable Use Policy and attribution clause — not literal unrestricted Apache 2.0). The 7B flagship trained on 14 trillion tokens; the 10B was upscaled via layer duplication. MMLU 73.1 and GSM8K 81.4 for the 10B. We review the architecture, Mamba variant, training methodology, benchmarks, and where Falcon 3 lands in the crowded December 2024 open-weight market."
tags: ["llm", "open-weight", "tii", "falcon", "falcon3", "falcon-llm-license", "stem", "edge-ai", "model-compression"]
sources_audited: 2026-08-24
categories: ["reviews"]
rating: 4
author: "ChatForest"
---

*This review covers the Falcon 3 family (December 17, 2024) from the Technology Innovation Institute. For other open-weight models in this era, see our [Meta Llama 4 review](/reviews/meta-llama-4-scout-maverick-open-weight-llm-review/), [Qwen 3 review](/reviews/alibaba-qwen-3-open-weight-hybrid-thinking-llm/), and [Google Gemma 3 review](/reviews/google-gemma-3-open-weights-multimodal-llm-review/).*

---

When [Technology Innovation Institute](https://www.tii.ae/news/falcon-3-uaes-technology-innovation-institute-launches-worlds-most-powerful-small-ai-models) released [Falcon 3 on December 17, 2024](https://huggingface.co/blog/falcon3), it was competing in the most crowded month the open-weight AI space had ever seen. December 2024 brought Llama 3.3 70B from Meta, Phi-4 from Microsoft, and a wave of Qwen 2.5 variants from Alibaba. In that context, Falcon 3's defining question was not whether it existed, but whether it could justify its place in a development environment already overflowing with choices.

The answer, for a specific kind of practitioner, is yes. Falcon 3 is a disciplined, permissively-licensed, STEM-capable family built for deployment on real hardware — not just benchmark tables. The 10B model is genuinely competitive for its parameter count, and the methodology for building it (upscaling a trained 7B via layer duplication, rather than training the 10B from scratch) represents an unusual engineering choice that TII executed successfully.

---

## Background: TII and the Falcon Series

The Technology Innovation Institute is a research center based in Abu Dhabi, part of the UAE's Advanced Technology Research Council. It launched the original Falcon model in 2023 — initially a 7B and 40B, later a 180B — and they represented some of the first serious open-weight competition to Meta's Llama family. Falcon 1 made headlines for briefly topping open-weight leaderboards before Llama 2 arrived.

Falcon 2 (2024) was a quieter release, refining the architecture with multimodal capabilities in the 11B vision model. Falcon 3 returns to a text-only focus but applies what TII learned across three generations of model development.

What stays constant across the Falcon lineage is the licensing approach: a permissive, Apache-2.0-derived license with no monthly-active-user threshold of the kind that complicates Meta's Llama releases for commercial deployments. For teams building products rather than running research, that's a meaningful practical advantage — see the correction below for what the license actually is, which is not literal Apache 2.0.

**Correction (2026-08-24):** the original version of this review repeatedly described Falcon 3's license as "true Apache 2.0." That's inaccurate. Falcon 3's [model cards](https://huggingface.co/tiiuae/Falcon3-7B-Base) list `license: other`, `license_name: falcon-llm-license`, linking to the [TII Falcon-LLM License 2.0](https://falconllm.tii.ae/falcon-terms-and-conditions.html) — a document TII itself describes as "in part, based on the Apache License Version 2.0... with a series of modifications." Those modifications include a mandatory external [Acceptable Use Policy](https://falconllm.tii.ae/falcon-terms-and-conditions.html) and a required public attribution notice ("[name of work] is built using Falcon LLM technology from the Technology Innovation Institute") — obligations plain Apache 2.0 does not carry. It is still meaningfully more permissive than Meta's Llama Community License (no 700M-MAU threshold), but it is not the no-strings-attached Apache 2.0 this review previously claimed. Every "Apache 2.0" reference below has been corrected to reflect this.

---

## The Falcon 3 Family

Falcon 3 launched with five distinct model lines and 30 total checkpoints counting all quantization variants:

| Model | Parameters | Layers | Context | Architecture |
|-------|-----------|--------|---------|--------------|
| Falcon3-1B | 1B | 18 | **8K** | Transformer (Llama-compatible) |
| Falcon3-3B | 3B | — | 32K | Transformer (Llama-compatible) |
| Falcon3-7B | 7B | 28 | 32K | Transformer (Llama-compatible) |
| Falcon3-10B | 10B | 40 | 32K | Transformer (Llama-compatible) |
| Falcon3-Mamba-7B | 7B | 64 | 32K | State Space Model (SSM) |

Each transformer model ships in Base, Instruct, GGUF (llama.cpp compatible), GPTQ-Int4, GPTQ-Int8, AWQ, and a 1.58-bit variant. The Mamba model has its own quantization variants. This breadth of quantization support at launch reflects a deployment-first mentality — TII isn't just releasing weights and leaving quantization to the community.

TII launched **Falcon Playground** alongside the model release — a hosted sandbox environment for developers to evaluate the models before committing to local setup or API integration.

At launch, TII claimed [Falcon3-10B-Instruct and Falcon3-7B-Instruct held the **#1 position on Hugging Face's Open LLM Leaderboard**](https://huggingface.co/blog/falcon3) for models under 13 billion parameters.

All models share several architectural decisions: **SwiGLU activation**, **Grouped-Query Attention (GQA)**, **32K token context windows**, and a **131,072-token vocabulary** (131K). The vocabulary size is notably larger than many competitors, reflecting attention to multilingual coverage alongside English-heavy domains.

---

## Architecture: What Changed from Falcon 2

Falcon 2 used TII's own multi-query attention architecture. Falcon 3 makes a deliberate shift to a **Llama-compatible architecture** for the transformer models — an ecosystem decision as much as a technical one. Llama compatibility means direct integration with llama.cpp, Ollama, vLLM, Hugging Face Transformers, and virtually every open-source inference stack without custom code. This substantially reduces the integration burden for practitioners.

Within that Llama-compatible foundation, Falcon 3 adopts **Grouped-Query Attention (GQA)** throughout — an inference efficiency improvement that reduces the KV cache memory footprint and improves throughput at long context lengths. By late 2024, GQA had become close to standard for new open-weight models.

The 7B model's architecture includes a head dimension of 256, specifically optimized for **FlashAttention-3** throughput — a sign that TII's training infrastructure runs on current-generation H100 accelerators.

The transformer layers range from 18 (1B) to 40 (10B). The vocabulary is 131K tokens (except the Mamba variant, which uses 65K).

### The Mamba Variant

Falcon3-Mamba-7B is what TII calls a **State Space Language Model ([SSLM](https://falconllm.tii.ae/tii-releases-first-sslm-with-falcon-mamba-7b.html))** — it contains no transformer attention mechanism at all. SSMs process sequences through structured state transitions rather than attention, which gives them linear (not quadratic) time and memory scaling with sequence length.

TII positioned Falcon3-Mamba-7B as the top-performing SSLM available at release, claiming it matches or exceeds transformer-based 7B models on many tasks while offering memory efficiency advantages for long sequences. With 64 layers (compared to 28 for the transformer 7B), it is architecturally deeper despite the same parameter count.

The Mamba variant has its own vocabulary (65K vs. 131K for transformer models) and is not Llama-compatible by definition — it requires different inference infrastructure. For most practitioners, the transformer models are the path of least resistance. But for research teams exploring alternative architectures or applications with very long sequences, Falcon3-Mamba-7B offers a production-quality SSM from a credible institution.

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
| GSM8K | 81.4 | 5-shot, math reasoning |
| MATH-Lvl5 | 22.9 | 4-shot, hard competition math |
| MBPP | 73.8 | Python coding |

(TII's [original December 2024 announcement blog](https://huggingface.co/blog/falcon3) listed GSM8K at 83.0; the current [Falcon3-10B-Base model card](https://huggingface.co/tiiuae/Falcon3-10B-Base) — the more specific, actively maintained source — shows 81.4. This table uses the model card's figure as of this audit.)

### Falcon3-7B-Base

| Benchmark | Score | Notes |
|-----------|-------|-------|
| MMLU | 67.4 | 5-shot |
| MMLU-PRO | 39.2 | 5-shot |

### Falcon3-10B-Instruct

| Benchmark | Score | Notes |
|-----------|-------|-------|
| Multipl-E | 45.8 | Code generalization across languages |
| BFCL | 86.3 | Berkeley Function-Calling Leaderboard |

The 10B MMLU score of 73.1 is competitive for sub-13B models in late 2024. For context, Mistral 7B scored ~64 on MMLU; Llama 3.1 8B scored ~73 — so Falcon3-10B is roughly competitive with Llama 3.1 8B while having 2B more parameters. The GSM8K score of 81.4 reflects the STEM emphasis in training.

Where Falcon 3 faces more competition is in the December 2024 landscape specifically. [**Microsoft Phi-4**](https://huggingface.co/microsoft/phi-4) (14B) achieved 84.8% on MMLU and 80.4% on the standard MATH benchmark, per [Microsoft's Phi-4 technical report](https://arxiv.org/pdf/2412.08905), using a heavily synthetic data approach. (Falcon3-10B's 22.9 score above is on MATH-Lvl5, the hardest competition-level subset of MATH — not the same slice, so the two numbers aren't directly comparable, but Phi-4's math-specialized training gives it a real edge at the 14B size.) For users who can accommodate 14B parameters, Phi-4 outperformed Falcon3-10B by a significant margin on math tasks. Phi-4's weights were released [under a plain MIT license in January 2025](https://the-decoder.com/microsoft-releases-full-phi-4-model-with-weights-under-mit-license/) — Microsoft had initially signaled a more restrictive research license at the December 2024 announcement but shipped MIT instead, with no special fine-tuning conditions. That makes the license comparison closer than it first appears: Falcon 3's Apache-derived license carries its own conditions (see correction above), while Phi-4 shipped unconditioned MIT.

[**Qwen 2.5 7B**](https://huggingface.co/Qwen/Qwen2.5-7B) (September 2024) also scored competitively — ~74% MMLU for the 7B, comparable to Falcon3-10B with fewer parameters. Qwen 2.5 had a head start of several months by the time Falcon 3 shipped.

---

## Hardware Deployment: Intel Partnership

One differentiator for Falcon 3 is first-day support from Intel:

- **[Intel Gaudi 2 and Gaudi 3 AI accelerators](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-ai-solutions-support-falcon-3-fdn-models.html)**: Validated for Falcon 3 inference
- **Intel Xeon 6 processors**: 7B inference with next-token latency under 50ms (dual-socket configuration with Performance cores)
- **OPEA (Open Platform for Enterprise AI)**: Intel's contributions enabled Falcon 3 7B and 10B support in this enterprise deployment framework

The Xeon 6 sub-50ms latency benchmark is meaningful for on-premises enterprise deployments where GPU hardware is not available or not approved. Many enterprise environments run on Xeon-class servers; having a validated 7B that delivers usable latency on CPU infrastructure is a legitimate differentiator that Llama 3 and Qwen 2.5 did not have at equivalent hardware.

The Gaudi partnerships matter in a different context: organizations running EU or Middle East cloud infrastructure, where Gaudi hardware is deployed in certain configurations, have a validated path to production.

---

## License: the TII Falcon-LLM License 2.0

Falcon 3 carries the **[TII Falcon-LLM License 2.0](https://falconllm.tii.ae/falcon-terms-and-conditions.html)** across all models — base and instruct. Every Falcon 3 model card on Hugging Face lists `license: other`, `license_name: falcon-llm-license` (e.g. [Falcon3-7B-Base](https://huggingface.co/tiiuae/Falcon3-7B-Base)), not `apache-2.0`. TII describes the document as based in part on Apache 2.0 "with a series of modifications," and those modifications are real:

- No monthly-active-user threshold or "community license" gating for commercial deployment (unlike Llama)
- Fine-tuning and derivative works permitted
- **But**: a mandatory external [Acceptable Use Policy](https://falconllm.tii.ae/falcon-terms-and-conditions.html) applies, and derivative public works must carry the attribution line "[name of work] is built using Falcon LLM technology from the Technology Innovation Institute" — obligations plain Apache 2.0 does not impose

This is still meaningfully permissive in the late 2024 landscape. Meta's Llama 3 models use the Llama 3 Community License, which restricts use in products serving over 700 million monthly active users and requires Meta attribution. Microsoft's Phi-4 shipped under a plain MIT license (see above). Google's Gemma uses the Gemma Terms of Use.

Falcon 3's license is genuinely more permissive than Llama's on the MAU-cap dimension specifically, which matters for enterprise legal teams evaluating scale risk. But it is not the "no-strings" open license this review previously described — a compliance team doing a license review should read the actual Falcon-LLM License 2.0 text and Acceptable Use Policy, not assume Apache 2.0 terms apply.

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

Falcon 3's clearest competitive advantage over all of these is: **a permissive, no-MAU-cap license at the 10B scale** (TII's Apache-derived Falcon-LLM License — see correction above, it does carry an attribution and acceptable-use clause) + **STEM specialization** + **Intel hardware certification** + **validated edge deployment**. No single competitor covers all four.

---

## Arabic Language Extension

About five months after the initial Falcon 3 release, TII published **[Falcon Arabic](https://www.tii.ae/news/middle-easts-leading-ai-powerhouse-tii-launches-two-new-ai-models-falcon-arabic-first-arabic)** (May 21, 2025) — built on the Falcon3-7B architecture and described by TII as "the first-ever Arabic language model in the Falcon series." TII has geographic and institutional advantages here: as an Abu Dhabi institution with deep regional networks, it can invest in Arabic language quality in ways that US and Chinese labs typically do not prioritize.

For Arabic-language enterprise applications in the Gulf region and broader MENA markets, the Arabic variant of Falcon 3 represents one of the few credible open-weight options from a regionally based institution. This positions TII differently from Meta, Google, and Alibaba in that specific market segment.

---

## 2026 Status and Reception

As of 2026, the Falcon 3 family remains available on Hugging Face and is maintained by TII. The models were adopted in enterprise and research contexts where the permissive, no-MAU-cap license and Intel Gaudi support mattered.

TII has continued releasing models since Falcon 3 — including [Falcon Arabic](https://www.tii.ae/news/middle-easts-leading-ai-powerhouse-tii-launches-two-new-ai-models-falcon-arabic-first-arabic) and the [Falcon-H1 family](https://www.hpcwire.com/aiwire/2026/01/05/uaes-tii-launches-falcon-h1-arabic-models-in-3b-7b-and-34b-configurations/) — and the Falcon brand has remained a known quantity in the open-weight space, one of the few non-US, non-China model series with genuine institutional backing.

The 7B and 10B variants see the most production usage. The 1B and 3B distilled models have found adoption in mobile and edge AI contexts where parameter constraints are hard.

Community reception was positive but measured. Practitioners acknowledged the competitive benchmarks for the parameter count and appreciated the licensing clarity, but the December 2024 market was simply too crowded with strong releases for any individual model to capture outsized attention. Falcon 3 was good news for practitioners who needed it — not the breakthrough that o1-mini or Qwen 3 became.

---

## Verdict

**Rating: 4/5**

Falcon 3 does exactly what TII designed it to do. It is a STEM-capable, permissively-licensed, deployment-ready open-weight family with an unusual and effective training methodology for the 10B model and broad hardware certification.

The reasons to choose Falcon 3 over alternatives are specific but real:
- You need a permissive license with no Llama-style user-count cap (though TII's Falcon-LLM License 2.0 does carry an attribution requirement and Acceptable Use Policy — read it before assuming plain Apache 2.0 terms apply)
- You're deploying on Intel Gaudi or Xeon 6 infrastructure
- Your use case is STEM-heavy (scientific text, code, math)
- You need validated quantization options including GGUF for edge

The reasons it falls short of a 5/5 are also specific: in December 2024, Microsoft Phi-4 outperformed it on math tasks (with more parameters), Qwen 2.5 7B matched it with fewer parameters, and the general market had options in every direction. Falcon 3 is excellent at what it is. It's not a generational leap.

The 10B via layer-duplication upscaling is a technically noteworthy approach that deserves attention — it's not the industry-standard training path, and TII's success with it opens questions about whether this methodology will propagate. In that sense, Falcon 3 has a technical contribution that goes beyond its benchmark position.

---

*All benchmarks from [TII's official Falcon 3 release materials](https://huggingface.co/blog/falcon3) (December 2024). Competitive context from public benchmark results available at time of publication. Weights available at [Hugging Face tiiuae/Falcon3-10B-Base](https://huggingface.co/tiiuae/Falcon3-10B-Base).*
