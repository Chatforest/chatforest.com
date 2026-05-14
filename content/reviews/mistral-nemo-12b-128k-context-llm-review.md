---
title: "Mistral NeMo Review — 12B Model, 128K Context, Nvidia Co-Release, Apache 2.0"
date: 2026-05-15
description: "Mistral NeMo (July 18, 2024) is a 12.2B parameter language model built jointly by Mistral AI and NVIDIA. 128K context window, new Tekken tokenizer with 2–3× better multilingual compression, Apache 2.0, FP8-ready. MMLU 68.0%, HellaSwag 83.5%. Runs at ~7 GB VRAM. Ollama: mistral-nemo. Rating: 4/5."
og_description: "Mistral NeMo (July 2024): 12B model co-built with NVIDIA. 128K context at 12B scale was unique at launch. Tekken tokenizer compresses Korean 2× better, Arabic 3× better. FP8 inference without performance loss. Apache 2.0. MMLU 68.0%. Superseded by Small 3.1 but still the most accessible 128K open-weight model at 7 GB VRAM. Rating: 4/5."
card_description: "Mistral NeMo (released July 18, 2024) is a 12.2-billion-parameter dense language model co-developed by Mistral AI and NVIDIA. Context window: 128,000 tokens (128K) — largest at its size class at launch. Architecture: 40 transformer layers, 5120 hidden dim, 32 attention heads with 8 KV heads (GQA), SwiGLU activation, RoPE theta=1M for long-context. New Tekken tokenizer (based on Tiktoken, 131K vocab, 100+ languages): ~30% more efficient for source code, Chinese, Italian, French, German, Spanish, and Russian; 2× more efficient for Korean; 3× more efficient for Arabic. Quantization-aware training enables FP8 inference without performance degradation. Benchmarks: MMLU 68.0% (5-shot), HellaSwag 83.5% (0-shot), Winogrande 76.8%, TriviaQA 73.8% (5-shot). VRAM: ~24 GB BF16; ~7 GB Q4 (runs on a single 8 GB GPU). Ollama: mistral-nemo. License: Apache 2.0. Also available as an NVIDIA NIM inference microservice. Identifier: mistralai/Mistral-Nemo-Instruct-2407. Rating: 4/5."
tags: ["llm-review", "mistral", "open-weights", "nvidia", "multilingual"]
categories: ["ai-tools"]
rating: 4
---

**At a glance:** Mistral NeMo, released July 18, 2024. 12.2B parameters. 128K context. Apache 2.0. New Tekken tokenizer. MMLU: 68.0%. FP8-ready. Ollama: `mistral-nemo`. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

Mistral NeMo is an unusual release in the 2024 open-weight model landscape: a formal collaboration between [Mistral AI](/reviews/mistral-ai-open-weight-llm-european-ai/) and NVIDIA, announced together on July 18, 2024 — two weeks before Meta's Llama 3.1 would redefine the open-weight frontier. The NeMo name reflects NVIDIA's NeMo framework for model training and the NIM microservice ecosystem for enterprise deployment. The Mistral contribution is the training methodology, the architecture, and the new Tekken tokenizer.

The central claim at launch: **128,000 tokens of context at 12B scale**, with an Apache 2.0 license and Ollama-ready weights that run on consumer GPUs. At the time, Llama 3 8B and Gemma 2 9B both offered 8K context windows. NeMo's 16× advantage on context was not incremental — it represented a different capability class at similar hardware requirements.

Two years later, Mistral Small 3.1 (March 2025) has formally superseded NeMo for new deployments with its 24B dense architecture, multimodal vision, and improved benchmarks at similar hardware costs. But NeMo retains one meaningful distinction: it runs cleanly at **Q4 quantization in roughly 7 GB of VRAM**, making it accessible on 8 GB consumer GPUs where Small 3.1 cannot fit. For long-document tasks where context matters more than peak accuracy, it remains a practical choice.

---

## Background: Why 12B + 128K in July 2024

The timing matters. In mid-2024, the open-weight model landscape looked like this:

- **Mistral 7B** (September 2023): 8K context, 7B parameters — the developer favorite for efficiency, but context-limited.
- **Mixtral 8x7B** (December 2023): 32K context, ~13B active parameters — much larger, required more VRAM than consumer hardware could typically provide.
- **Llama 3 8B** (April 2024): 8K context, strong benchmarks — but 8K context remained a pain point for document processing.
- **Gemma 2 9B** (June 2024): 8K context, Google's dense 9B option — competitive on benchmarks, same context ceiling.

The gap: no open-weight model at the 8–12B scale offered more than 8K context without jumping to a significantly larger model. Long-document tasks — processing PDFs, summarizing transcripts, maintaining conversation history, reading entire codebases — were out of reach for small models.

NeMo filled that gap with 128K context in a 12B package that could fit on a single NVIDIA A100 (80 GB) or H100 for production, or on a consumer GPU at Q4 for local use. The NVIDIA partnership provided the training infrastructure (Megatron-LM) and the enterprise deployment path (NIM microservices + TensorRT-LLM optimization). Mistral provided the architecture and the Tekken tokenizer — a component that would propagate to all subsequent Mistral models.

---

## Architecture

Mistral NeMo is a dense decoder-only Transformer. The architecture follows the Mistral lineage with modifications for long-context efficiency:

| Property | Value |
|---|---|
| Parameters | 12.2 billion |
| Context window | 128,000 tokens (128K) |
| Architecture | Dense decoder-only Transformer |
| Layers | 40 |
| Hidden dimension | 5,120 |
| Attention heads | 32 query heads, 8 KV heads (GQA) |
| FFN hidden dimension | 14,436 |
| Activation | SwiGLU |
| Position encoding | RoPE (theta = 1,000,000) |
| Tokenizer | Tekken (131,072 vocabulary) |
| Precision | BF16 |
| VRAM (BF16) | ~24 GB |
| VRAM (Q4_K_M) | ~6.8 GB |

**Grouped Query Attention (GQA)**: 32 query heads sharing 8 KV heads reduces the KV cache memory footprint during inference — important at 128K context, where the KV cache for a full context window at BF16 would otherwise be enormous.

**RoPE theta = 1,000,000**: The rotary position embedding theta controls how quickly positional information decays at distance. A theta of 1M (versus the 10,000 used in original transformer models) allows the model to maintain meaningful position encoding at distances measured in tens of thousands of tokens. This is the architectural mechanism that makes 128K context functional rather than nominal.

**FP8 quantization-aware training**: NeMo was trained with quantization awareness built in, allowing FP8 inference without performance degradation. This was notable at launch — most models required post-hoc quantization that degraded quality. FP8-native inference on H100s (which have dedicated FP8 tensor cores) provides throughput roughly 2× higher than BF16 at the same accuracy.

---

## Tekken Tokenizer

Tekken is the most technically durable contribution from the NeMo release — it subsequently became the standard tokenizer for the Mistral Small 3.x series and later models.

Previous Mistral models (7B, Mixtral 8x7B) used SentencePiece tokenizers with a 32K vocabulary. Tekken switches to a **Tiktoken-based byte-pair encoding** with a **131,072-token vocabulary**, trained on a dataset spanning **100+ languages**. The compression efficiency improvements are substantial:

| Language / Domain | Compression improvement vs. SentencePiece |
|---|---|
| Source code | ~30% more efficient |
| Chinese | ~30% more efficient |
| Italian, French, German, Spanish, Russian | ~30% more efficient |
| Korean | ~2× more efficient |
| Arabic | ~3× more efficient |

Compression efficiency matters for two reasons. First, more tokens per inference call means more cost if you pay by the token (the tokenizer advantage translates directly to price savings for multilingual workloads). Second, for models with fixed context windows, a more efficient tokenizer fits more information — a document that requires 40K Mistral-7B tokens might require only 28K Tekken tokens, changing whether it fits in a 32K window.

The vocabulary size jump from 32K to 131K also reduces the frequency of multi-token splits for technical terms, URLs, and code identifiers — improving generation consistency for structured outputs.

---

## Benchmarks

Mistral published the following benchmark scores for Mistral NeMo at launch:

| Benchmark | Score | Setting |
|---|---|---|
| MMLU | 68.0% | 5-shot |
| HellaSwag | 83.5% | 0-shot |
| Winogrande | 76.8% | 0-shot |
| TriviaQA | 73.8% | 5-shot |

**On MMLU**: 68.0% (5-shot) is behind Llama 3.1 8B (73%, 0-shot) — though the different shot settings complicate direct comparison. Llama 3.1 8B was released on July 23, 2024 — five days after NeMo — and represented Meta's benchmark push. NeMo's positioning was never "highest MMLU at 12B"; it was "most accessible 128K context at 12B."

**HumanEval not published**: Mistral did not release an official HumanEval score for NeMo at launch. Community requests for coding benchmarks appeared in the Hugging Face model card discussion thread. Qualitative evaluations from practitioners found NeMo competitive on practical coding tasks — function completion, docstring generation, bug identification — relative to Llama 3 8B.

**Multilingual advantage**: NeMo was positioned by both Mistral and NVIDIA as a multilingual model for enterprise use. The Tekken tokenizer's compression efficiency across European and East Asian languages translates to meaningful real-world performance improvements for non-English tasks.

---

## Deployment

### Ollama

```bash
ollama pull mistral-nemo
ollama run mistral-nemo
```

The default Ollama tag pulls the Q4_K_M quantized variant at approximately 6.8 GB. This fits on an 8 GB GPU (NVIDIA RTX 3060, 3070 Ti, 4060 Ti 8GB) with enough headroom for context. At Q6_K (~10 GB), an RTX 4070 (12 GB) is the natural fit.

### NVIDIA NIM

NVIDIA provides Mistral NeMo as a **NIM inference microservice** — a packaged container optimized with TensorRT-LLM for H100/A100 deployment. The NIM format provides:
- FP8 inference on H100 hardware with no quality penalty
- Triton-based serving with batching and concurrency optimization
- Docker container pull with no model conversion step

For enterprise teams already on NVIDIA infrastructure, the NIM path provides higher throughput than a generic vLLM deployment of the same weights.

### Hugging Face

```
mistralai/Mistral-Nemo-Base-2407   (base model)
mistralai/Mistral-Nemo-Instruct-2407   (instruction-tuned)
nvidia/Mistral-NeMo-12B-Base
nvidia/Mistral-NeMo-12B-Instruct
```

Both Mistral AI and NVIDIA host the weights, with the NVIDIA variants optimized for their NIM deployment stack.

---

## NeMo vs. The Competition at Launch (July 2024)

| Model | Parameters | Context | License | MMLU |
|---|---|---|---|---|
| **Mistral NeMo 12B** | 12.2B | 128K | Apache 2.0 | 68.0% |
| Llama 3 8B | 8B | 8K | Llama Community | ~66% |
| Gemma 2 9B | 9B | 8K | Gemma ToU | ~71% |
| Mistral 7B | 7B | 8K | Apache 2.0 | 63.0% |
| Mixtral 8x7B | 46B (~13B active) | 32K | Apache 2.0 | ~70% |

The comparison illustrates the trade-off NeMo was designed to resolve. At launch:
- For context-limited tasks (<8K), Llama 3 8B or Gemma 2 9B match or exceed NeMo's MMLU at smaller VRAM footprints.
- For long-context tasks, NeMo's 128K was the only open-weight option at ≤15B parameters.
- Mixtral 8x7B offered 32K context (4× smaller than NeMo's 128K) at ~3× the VRAM requirement.

---

## Relation to Subsequent Mistral Models

NeMo is a transitional model — released during the gap between the MoE-era (Mixtral 8x7B, 2023) and the Small 3.x series (2025). Its successors:

**Mistral Small 3 (January 2025)**: 24B dense, 32K context, Apache 2.0. Larger than NeMo but with significantly improved instruction-following at the cost of 4× the context window.

**[Mistral Small 3.1 (March 2025)](/reviews/mistral-small-3-1-vision-24b-llm-review/)**: 24B, 128K context, Apache 2.0, multimodal vision. Effectively the formal successor to NeMo's 128K positioning — but requires ~55 GB BF16 or ~16 GB Q4. Does not fit in an 8 GB GPU at any practical quantization.

**[Mistral Small 3.2 (June 2025)](/reviews/mistral-small-3-2-24b-instruct-refinement-llm-review/)**: Same 24B base with improved instruction-following (Arena Hard: +23.5pp, HumanEval Plus: +3.9pp). Same hardware profile as Small 3.1.

NeMo's niche after these releases: tasks requiring 128K context that run on a single 8 GB consumer GPU. No other Apache 2.0 model covers that overlap as of mid-2026.

**Mistral-NeMo-Minitron 8B (NVIDIA, late 2024)**: NVIDIA independently pruned and distilled NeMo from 12B to 8B, releasing an 8B variant that matched or exceeded the 12B version on several benchmarks. This is a derivative, not an official Mistral AI release, but demonstrates the base model quality.

---

## Use Cases Where NeMo Fits

**Long document processing**: Legal contracts, research papers, technical manuals — 128K fits ~90,000 words. Practically the entire text of most books.

**Multilingual enterprise tasks**: The Tekken tokenizer's efficiency gains for Korean, Arabic, and European languages make NeMo a practical choice for non-English workloads where token count directly affects API cost.

**Edge and consumer GPU deployment**: At Q4_K_M, NeMo fits in 6.8 GB of VRAM. This is the most capable Apache 2.0 model that runs on an 8 GB RTX card with 128K context.

**NVIDIA-stack enterprise deployment**: For organizations already running H100 infrastructure, the NIM container path provides FP8-optimized serving without the overhead of configuring custom quantization pipelines.

---

## What Was Missing at Launch

**HumanEval not published**: The omission of official coding benchmarks was conspicuous. Community evaluations filled the gap but created uncertainty about where NeMo actually sits on the HumanEval leaderboard.

**No vision**: NeMo is text-only. Llama 3.2 (September 2024) introduced multimodal 11B and 90B models in the same tier.

**MMLU below Gemma 2 9B**: For general knowledge tasks, Gemma 2 9B (~71% MMLU) outperforms NeMo (68.0%) at lower VRAM. NeMo wins on context; Gemma 2 wins on raw benchmark numbers for typical workloads.

---

## Verdict

Mistral NeMo solved a real problem: in July 2024, there was no open-weight model at 8–12B that offered 128K context with an Apache 2.0 license. NeMo provided exactly that, and the NVIDIA partnership added enterprise-grade deployment infrastructure via NIM and FP8 support via quantization-aware training. The Tekken tokenizer was the most technically durable contribution from the release — it propagated through the entire Mistral Small 3.x lineage.

The model's limitations are honest rather than surprising. MMLU lags Gemma 2 9B. HumanEval was never officially published. It has no vision capability. And Mistral Small 3.1 (March 2025) formally superseded it for any deployment where VRAM is not the hard constraint.

What keeps NeMo at four stars rather than three is the combination of constraints it resolved simultaneously: Apache 2.0, 128K context, 12B scale, 7 GB at Q4 — no other model has covered all four of those at once, before or after NeMo's release.

**Rating: 4/5** — A purpose-built solution that delivered on its stated constraints. Architecturally transitional, but still the most accessible 128K Apache 2.0 model for 8 GB GPU users in mid-2026.

---

## Companion Reviews

- **[Mistral AI — Company Review](/reviews/mistral-ai-open-weight-llm-european-ai/)** — Full breakdown of Mistral's business, team, models, and competitive position
- **[Mistral Small 3.1 — 24B Vision Model](/reviews/mistral-small-3-1-vision-24b-llm-review/)** — Formal successor with multimodal vision and improved instruction-following
- **[Mistral Small 3.2 — Instruct Refinement](/reviews/mistral-small-3-2-24b-instruct-refinement-llm-review/)** — +23.5pp Arena Hard, +3.9pp HumanEval Plus over Small 3.1
- **[Mistral Codestral — Code Specialist](/reviews/mistral-codestral-22b-code-fill-in-the-middle-llm-review/)** — 22B with native fill-in-the-middle, 81.1% HumanEval
- **[Mistral Large 3 — Flagship MoE](/reviews/mistral-large-3-open-weight-moe-llm-review/)** — 675B total, 41B active, 256K context
