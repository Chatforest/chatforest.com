# Google Gemma 3 — Open Weights, 128K Context, and the QAT Advantage

> Google's Gemma 3 family (March 2025) delivers a 27B model that outscores LLaMA 3.1 405B on LMArena, four sizes from 270M to 27B, vision-language capabilities on three of those sizes, and official quantization-aware training (QAT) variants for consumer GPU deployment. Gemma Terms license, not Apache 2.0. We review the full family.


On March 12, 2025, Google released Gemma 3 with a claim that needed unpacking: a 27-billion-parameter open-weights model comparable to Gemini 1.5 Pro. On LMArena's competitive text-only arena, the 27B reached an Elo of 1338–1339, placing it ninth globally and ahead of both Meta's LLaMA 3.1 405B (Elo 1269) and Alibaba's Qwen 72B (Elo 1257).

That is a meaningful result. A 27B model outperforming a 405B model on blind human preference evaluation is not primarily a story about benchmark engineering — it reflects genuine instruction-following capability and conversational quality.

The rest of the Gemma 3 story is worth understanding carefully, because the family includes both genuine technical innovations (QAT, Pan & Scan, the 5:1 local-to-global attention architecture) and real limitations (the 1B being text-only with 32K context, a 10-point SimpleQA score, and a license that is open-weights but not OSI-compliant open source). By the time of Google I/O 2025, Google had also announced Gemma 3n — an architecturally distinct successor designed for on-device mobile inference — suggesting the roadmap moves fast.

This review covers the full Gemma 3 family in the detail that deployment and research decisions require.

---

## Google DeepMind and the Gemma Program

The Gemma name was first used in February 2024 with the release of Gemma 1 — Google's initial attempt to offer open-weights models derived from the same research and infrastructure that produced Gemini. **[Gemma 1](/reviews/google-gemma-1-open-weights-gemini-era-llm-review/)** shipped in two sizes (2B and 7B) and attracted significant developer attention, though it was technically modest compared to concurrent open-weights releases from Meta and Mistral.

**[Gemma 2](/reviews/google-gemma-2-open-weights-distillation-llm-review/)** followed in June 2024, introducing 9B and 27B sizes with a distinctive architectural choice: interleaved sliding-window and global attention layers. Standard transformers apply full (global) attention at every layer, which scales quadratically with sequence length. Gemma 2's hybrid approach reduced KV-cache memory substantially while maintaining quality — enabling longer context windows at lower memory cost than fully dense attention architectures.

**Gemma 3**, released March 12, 2025, built on this foundation with several additions: 128K context across the mid-to-large sizes, multimodal vision-language capability, a refreshed 256K-vocabulary tokenizer shared with Gemini 2.0, and official quantization-aware training (QAT) variants. It also added smaller sizes — the 270M and 1B — extending the family downward toward edge deployment.

The models are developed and maintained by **Google DeepMind**, the combined research organization formed by the 2023 merger of Google Brain and DeepMind. The Gemma 3 technical report (arXiv:2503.19786) describes training on Google's TPU v4p, v5p, and v5e clusters using JAX and ML Pathways.

---

## The Full Lineup

Gemma 3 ships in five sizes. They are not equivalent in capability, context, or modality — and the differences matter:

| Model | Parameters | Context | Multimodal | Training Tokens |
|-------|-----------|---------|------------|-----------------|
| Gemma 3 270M | 270M | 32K | Text only | — |
| Gemma 3 1B | 1B | **32K** | Text only | 2T |
| Gemma 3 4B | 4B | 128K | Text + images | 4T |
| Gemma 3 12B | 12B | 128K | Text + images | 12T |
| Gemma 3 27B | 27B | 128K | Text + images | 14T |

**The 270M** was added to the family after the initial launch and does not appear in all official documentation. It is primarily useful for ultra-constrained edge scenarios where even the 1B is too large.

**The 1B is text-only with a 32K context window.** This surprises developers who assume all Gemma 3 models share the 128K context. The distinction is real: only the 4B and above have the extended context and vision encoder.

**Each size ships in two variants**: a pre-trained (pt) base model and an instruction-tuned (it) model fine-tuned for conversational use. Benchmark numbers in this review refer to instruction-tuned variants unless noted.

---

## Architecture: What Changed From Gemma 2

Understanding Gemma 3's architecture helps explain both its efficiency and its context-length capabilities.

**5:1 local-to-global attention** (inherited from Gemma 2): For every five transformer layers using local sliding-window attention over 1,024-token spans, one layer uses full global attention over the entire context. This hybrid pattern reduces the KV-cache memory requirement by approximately 85% compared to full global attention at 32K context — the underlying reason the models can achieve 128K context windows without prohibitive memory costs. The tradeoff is that information must propagate across many layers to travel across distant parts of the context, which can theoretically reduce performance on tasks requiring tight long-range dependencies.

**256K vocabulary tokenizer** (new in Gemma 3): The tokenizer is shared with Gemini 2.0 and is specifically optimized for multilingual coverage, including improved handling of Chinese, Japanese, and Korean. For reference, GPT-4 uses a ~100K vocabulary and LLaMA 3 uses a 128K vocabulary — Gemma 3's is among the largest tokenizer vocabularies in open-weights models.

**128K context via RoPE frequency scaling**: The 4B, 12B, and 27B models were pretrained on 32K sequences, then extended to 128K through post-pretraining with the RoPE base frequency increased from 10K (Gemma 2) to 1M, with an 8x scaling factor. This is a technique used across several frontier models rather than native pre-training at full context length.

**Knowledge distillation in pretraining**: The post-training recipe applies distillation from a teacher model (256 logits per token, weighted by teacher probabilities), combined with RLHF (using Google's BOND, WARM, and WARP variants), reinforcement learning from math feedback (RLMF), and reinforcement learning from code execution feedback (RLEF). This four-component training stack is more elaborate than most open-weights model post-training processes.

---

## Vision: How Image Input Works

For the 4B, 12B, and 27B models, image input is handled by a **SigLIP-based vision encoder** with approximately 400M parameters. This encoder is shared across all three sizes.

**Resolution handling**: Images are encoded at 896×896 pixels into 256 tokens per image. This fixed resolution is augmented by a technique called **Pan & Scan**: for non-square or high-resolution images, an adaptive algorithm crops the image into multiple overlapping segments (each processed at 896×896) and combines the resulting token sequences. This mitigates the information loss that would occur from simply resizing a 3:2 landscape photo to a square crop.

**Attention asymmetry**: Text uses causal (one-directional) attention, while image tokens use bidirectional (full) attention. This reflects the different structural properties of the two modalities — text has sequential dependencies, images have spatial ones.

**Practical note from real-world testing**: Vision capabilities are not exposed through Google's hosted AI Studio API as of early 2025 for some integrations. Direct local deployment via Hugging Face Transformers or Ollama exposes full multimodal capability. If you are using a third-party library wrapper, verify multimodal support is implemented before building vision-dependent pipelines on top of it.

---

## QAT: The Consumer GPU Story

One of Gemma 3's most practically significant features is official **Quantization-Aware Training (QAT)** variants. Google released int4 QAT checkpoints for all instruction-tuned sizes: 1B, 4B, 12B, and 27B. These are available as both unquantized checkpoints (for custom quantization pipelines) and as pre-quantized GGUF files ready for llama.cpp and Ollama.

**Why QAT matters**: Standard post-hoc quantization (taking a full-precision model and rounding weights after training) degrades model quality, especially at int4 precision where each weight is stored in 4 bits. Quantization-aware training incorporates the quantization error signal into the training process itself, teaching the model to compensate for the imprecision that will be present at inference time. The result is a quantized model that retains quality much closer to the BF16 original than post-hoc quantization achieves.

**Memory implications**: The Gemma 3 27B in BF16 requires approximately 54GB of VRAM — beyond even a high-end 3×GPU consumer setup. The QAT int4 variant reduces this to approximately 17–18GB, bringing the 27B within range of a single NVIDIA RTX 3090 or RTX 4090 (24GB). Google specifically cited the RTX 3090 as a target consumer GPU when announcing the QAT releases.

Most open-weights model releases from other labs ship official BF16 and FP16 weights, with community-created quantizations on Hugging Face (often from TheBloke or ggml-org). Having official QAT variants from the model developer is a quality guarantee that community quantizations cannot match.

---

## Benchmark Performance

### Gemma 3 27B — Flagship

The 27B model's strongest competitive signal comes from human preference evaluations rather than academic benchmarks:

**LMArena (human preference arena, text-only)**: Elo **1338–1339**, rank 9th globally. This places it ahead of LLaMA 3.1 405B (Elo ~1269) and Qwen 72B (~1257), and roughly comparable to o1-preview. For a 27B model, this is the headline result.

Academic benchmark scores for 27B-IT:

| Benchmark | Score |
|-----------|-------|
| MMLU (5-shot) | 76.9–78.6 |
| MMLU-Pro | 67.5 |
| GPQA Diamond | 42.4 |
| MATH (4-shot) | 89.0 |
| GSM8K | 95.9 |
| HumanEval | 87.8 |
| MBPP | 74.4 |
| LiveCodeBench | 39.0 |
| BIG-Bench Hard | 77.7 |
| DocVQA | 86.6 |
| MMMU (multimodal) | 64.9 |
| ChartQA | 76.3 |
| Global MMLU-Lite | 75.1 |
| SimpleQA | **10.0** |

The **GPQA Diamond score of 42.4** is respectable for a 27B model, though well below frontier closed models (Claude 3.5 Sonnet and GPT-4o typically score in the low 50s). The **MATH score of 89.0** and **HumanEval of 87.8** are strong for the size class.

The **SimpleQA score of 10.0** warrants attention. SimpleQA tests basic factual recall — questions with single, unambiguous correct answers. A score of 10% means the model answers approximately 1 in 10 such questions correctly. This is a known phenomenon in models trained heavily on reasoning and RLHF: they can develop a form of calibrated uncertainty that makes them reluctant to state simple facts confidently, or reasoning processes that overcomplicate retrieval tasks. It is a real limitation for applications that depend on factual Q&A over common knowledge.

### Gemma 3 12B

| Benchmark (PT) | Score |
|----------------|-------|
| MMLU (5-shot) | 74.5 |
| MMLU-Pro COT | 45.3 |
| GPQA (5-shot) | 25.4 |
| MATH (4-shot) | 43.3 |
| HumanEval | 45.7 |
| MBPP | 60.4 |

### Gemma 3 4B-IT

| Benchmark | Score |
|-----------|-------|
| MMLU (5-shot) | 59.6 |
| MATH (4-shot) | 24.2 |
| BIG-Bench Hard | 50.9 |
| HumanEval | 36.0 |
| MBPP | 46.0 |
| DocVQA | 72.8 |
| ChartQA | 63.6 |

Google's technical report claims that **Gemma 3-4B-IT reaches parity with Gemma 2-27B-IT** on aggregated benchmarks — a generational efficiency improvement, if confirmed in your specific use case. The 4B's DocVQA score of 72.8 and ChartQA of 63.6 are competitive for a model this size with vision capability.

---

## Hardware Requirements

| Model | BF16 VRAM | QAT int4 VRAM | Ollama file |
|-------|-----------|----------------|-------------|
| 270M | ~0.6 GB | — | 292 MB |
| 1B | ~2–3 GB | minimal | 815 MB |
| 4B | ~8–10 GB | ~3–4 GB | 3.3 GB |
| 12B | ~24 GB | ~8–9 GB | 8.1 GB |
| 27B | ~54 GB | **~17–18 GB** | 17 GB |

The 4B BF16 is comfortable on an 8–12GB GPU (RTX 3060/3070 range). The 12B BF16 needs 24GB (single RTX 3090/4090). The 27B in full precision requires multi-GPU consumer setups or professional cards. With QAT int4, the 27B becomes single-GPU on a 24GB consumer card.

---

## Deployment Options

**Hugging Face**: All Gemma 3 models are hosted at `google/gemma-3-[size]-[pt|it]`. Requires accepting the Gemma Terms of Use (click-through on Hugging Face). Requires `transformers>=4.50.0` and the `Gemma3ForConditionalGeneration` class. The 4B-IT model has approximately 2.1 million monthly downloads as of early 2025 — one of the most-downloaded open-weight models on the platform.

**Google AI Studio**: Free web interface and API access for testing and prototyping. The free tier uses conversations to improve Google products.

**Vertex AI / Model Garden**: Enterprise deployment on Google Cloud with managed serving infrastructure. Per-token pricing follows Vertex AI custom model deployment compute costs rather than a published per-million-token rate.

**Ollama**: `ollama pull gemma3` defaults to the 4B. Specific pulls: `gemma3:1b`, `gemma3:4b`, `gemma3:12b`, `gemma3:27b`. Cloud-hosted variants (4b-cloud, 12b-cloud, 27b-cloud) are available via Ollama with usage-based pricing. The QAT GGUF files are also available through llama.cpp's ggml-org collection.

**Other frameworks**: vLLM, SGLang, LM Studio, Jan, MLX (Apple Silicon via mlx-community), NVIDIA NIM. Note: early vLLM users reported compatibility issues (output repetition, crashes) in the weeks immediately following launch — these were largely resolved in subsequent releases but worth checking if you are pinned to an older vLLM version.

**Kaggle**: Hosted notebooks and model artifacts, useful for experimentation without local hardware.

---

## The License Question

Gemma 3 is **not Apache 2.0** and not MIT. It operates under the **Google Gemma Terms of Use** — a proprietary license that permits commercial use and derivative models but is not OSI-compliant open source.

Key points for those who care about licensing:

**What is permitted**: Commercial deployment including hosted APIs. Creating derivative models, fine-tunes, and distillations. Sublicensing to downstream users.

**What is required**: Downstream distributors must pass the use restrictions through their own licensing to end users. The Gemma Terms must be enforced through the distribution chain — you cannot use Gemma 3 to build a product that permits uses the Gemma Terms prohibit.

**What is prohibited**: Uses violating Google's Prohibited Use Policy (ai.google.dev/gemma/prohibited_use_policy). Disputes are governed by California law in Santa Clara County.

**The key practical difference from Apache 2.0**: The use restrictions that flow downstream. Apache 2.0 puts no constraints on what users do with derivative works beyond attribution and patent clauses. Gemma Terms require that prohibited uses remain prohibited at every point in the distribution chain. For compliance-sensitive applications, legal review of the full terms is advisable.

It is worth noting that the Gemma Terms are more permissive than many commercial model licenses (no MAU caps, no revenue thresholds, no prohibition on competitors). For most developers building products, the practical difference from Apache 2.0 is minimal. For open-source purists or organizations with policies requiring OSI-compliant licenses, Gemma 3 does not qualify.

---

## Gemma 3n: The Next Direction

At Google I/O 2025 (May 2025), Google announced **Gemma 3n** — an architecturally distinct model family designed for on-device inference on phones, tablets, and laptops. Understanding Gemma 3n clarifies the roadmap context for Gemma 3 itself.

Gemma 3n introduces two architectural techniques not present in Gemma 3:

**MatFormer (Matryoshka Transformer)**: A nested architecture where the larger E4B model contains a fully functional E2B sub-model inside it. The E4B's feed-forward and attention layers are structured so that a smaller subset of dimensions constitutes a complete, independently runnable model. This enables "Mix-and-Match" inference: developers can select any intermediate size between E2B and E4B by adjusting which dimensions are active, without retraining.

**Per-Layer Embeddings (PLE)**: Embedding parameters are designed to reside in CPU or fast storage memory rather than GPU/NPU VRAM. The embeddings are computed separately and added during inference. The result is that the model's total parameter count is substantially larger than its accelerator memory footprint — a technique that allows deploying more capable models on memory-constrained mobile hardware.

The E4B model has approximately 8B total parameters but an effective accelerator footprint of ~4B. It achieves an LMArena score above 1300, described by Google as "the first model under 10B parameters to reach this benchmark." Gemma 3n supports text (140+ languages), images (via a MobileNet-V5 300M vision encoder), audio (via a Universal Speech Model encoder, 35 languages, up to 30 seconds), and video.

For the purposes of this Gemma 3 review: Gemma 3n is not a replacement for Gemma 3. It is a parallel development targeting mobile/edge hardware specifically. The Gemma 3 family remains the primary offering for server-side deployment.

---

## ShieldGemma 2

Released alongside Gemma 3 on March 12, 2025, **ShieldGemma 2** is a specialized 4B image safety classifier built on the Gemma 3 4B-IT checkpoint. It is a companion tool, not a general-purpose model.

ShieldGemma 2 takes an image and a policy definition prompt, then returns a probability score for whether the image violates that policy. It operates in scoring mode (next-token probability evaluation) rather than generating explanatory text. Three built-in safety categories are supported: sexually explicit content, dangerous content (explosives, terrorism, self-harm instructions), and violence and gore.

On published precision/recall benchmarks, ShieldGemma 2 outperforms both LlavaGuard 7B and GPT-4o mini across all three categories. For teams building moderation pipelines that accept image input, it provides a purpose-built tool within the Gemma ecosystem.

---

## Limitations

**The 1B gotcha**: The 1B model is text-only with a 32K context window. This will surprise developers who assume all Gemma 3 sizes share the 128K context and vision capabilities of the 4B and above.

**SimpleQA at 10.0**: This is a genuine weakness for factual knowledge applications. The 27B answers approximately 1 in 10 SimpleQA questions correctly. Applications requiring strong factual recall over common knowledge should test this carefully.

**Max output: 8,192 tokens**: Despite the 128K input context, the maximum output length is 8,192 tokens. This limits the model for long-form generation tasks (extended documents, multi-section reports).

**License complexity**: Not OSI-compliant. Organizations with policies requiring Apache 2.0 or MIT cannot use Gemma 3. Downstream use restriction enforcement requirements may complicate some product architectures.

**Vision API availability varies by integration**: Multimodal capabilities are not uniformly available through all wrappers and third-party integrations. Verify before building.

**Early framework compatibility issues**: vLLM and FP8 quantization had reported instability in the first weeks post-launch. These appear resolved in recent versions, but lock files and pinned dependencies in production environments may still hit these issues.

---

## Competitive Positioning

Gemma 3 27B is the reference model for open-weights inference in the under-30B class as of mid-2025. The LMArena position (9th globally, ahead of LLaMA 3.1 405B) is a strong signal about instruction-following and conversational quality. The QAT int4 variants making the 27B consumer-GPU-accessible is a meaningful accessibility advantage.

The primary open-weights competition at the 27B tier:
- **Mistral Small 3 (24B)**: Similar parameter range, Apache 2.0 license, competitive instruction-following
- **Qwen 3 30B-A3B** (MoE): 30B total with only 3B active parameters, hybrid thinking mode, Apache 2.0 — different efficiency tradeoff
- **LLaMA 3.3 70B**: Stronger on many benchmarks but 2.5x the parameters and proportionally higher hardware requirements

For vision-language use cases specifically, the 4B, 12B, and 27B variants with the SigLIP encoder plus Pan & Scan provide production-quality image understanding at sizes competitive with dedicated vision-language models.

For edge and mobile deployment, Gemma 3n has largely superseded Gemma 3's smaller sizes in Google's roadmap — the E2B and E4B models are more architecturally suited to mobile constraints than Gemma 3 1B or 4B.

---

## Rating: 4 out of 5

Gemma 3 27B earns its position at the top of the open-weights leaderboard. The LMArena result is not easily gamed, the QAT variants are a genuine community contribution, the vision-language capability is solid, and the 128K context across three sizes is functional. Google's post-training stack (RLHF + RLMF + RLEF + distillation) produces instruction-following quality that translates to human preference.

The deductions: the license is not truly open-source, which matters for some deployment contexts. The SimpleQA score of 10.0 is a real limitation for knowledge-intensive applications. The 8K output cap is restrictive at 128K input context. And the 1B size is meaningfully weaker than the rest of the family in both capability and context window.

At 27B with QAT, Gemma 3 is the strongest open-weights choice for teams who want frontier-adjacent conversational quality on consumer hardware. For organizations that need Apache 2.0 or MIT licensing, Qwen 3 or Mistral Small 3 are the alternatives to evaluate.

---

*Review based on the Gemma 3 technical report (arXiv:2503.19786), Google DeepMind's Hugging Face model cards, benchmark data from Artificial Analysis, human preference evaluation data from LMArena, and community deployment documentation as of May 2025. ChatForest researches these models through public documentation — we do not operate the models directly or independently verify benchmark claims.*

**Update (May 2026):** Gemma 4 released April 2, 2026. Apache 2.0 (true open source), four sizes including a 26B MoE running at ~4B active params / 14GB VRAM, 256K context on the larger models, audio input on E2B/E4B, and a substantial benchmark improvement over this generation. See our **[Gemma 4 review](/reviews/google-gemma-4-open-weight-multimodal-llm-review/)**.

