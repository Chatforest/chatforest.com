# Google Gemma 2 — Distillation, Sliding-Window Attention, and Open Weights Done Right

> Google's Gemma 2 family (June–July 2024) introduced a 27B model that outranks Llama 3 70B on Chatbot Arena despite being 2.5× smaller, through interleaved sliding-window attention, grouped-query attention, logit soft-capping, and knowledge distillation. Three sizes: 2B, 9B, 27B. 8K context. Gemma Terms license. Rating: 4/5.


On June 27, 2024, Google released Gemma 2 — not at Google I/O, not as part of a major product event, but via a developer blog post titled "Gemma 2 is now available to researchers and developers." The 9B and 27B launched first; the 2B followed on July 31, 2024, alongside ShieldGemma and Gemma Scope.

The leading result: the Gemma 2 27B instruction-tuned model reached an ELO of 1218 on the LMSYS Chatbot Arena, placing it above the Llama 3 70B (ELO 1206) despite having 2.5× fewer parameters. The Gemma 2 9B instruction-tuned model matched GPT-4-0314's ELO (approximately 1187 vs 1186). The 2B instruction-tuned model surpassed GPT-3.5-Turbo-0613 (approximately 1126 vs 1116).

These were not narrow benchmark wins from a hand-tuned evaluation suite — Chatbot Arena is a blind human-preference evaluation where users choose between model outputs without knowing the source. That Gemma 2 27B outranked a 70B model on this metric is meaningful.

This review examines what produced those results: the architectural choices that distinguish Gemma 2 from its predecessor, the practical implications of the 8K context limit, the real licensing terms, and what the model family can and cannot do in 2024.

---

## Background: The Gemma Program

Gemma 2 is the second generation of Google DeepMind's open-weights model family. **[Gemma 1](/reviews/google-gemma-1-open-weights-gemini-era-llm-review/)**, released February 21, 2024, shipped in 2B and 7B sizes and established the program's initial positioning: open weights derived from the same research infrastructure as Gemini, targeting developer and researcher use cases where self-hosting matters.

**Gemma 2** extended the family upward (to 27B) and downward (to 2B, now improved), while introducing a set of architectural changes significant enough to warrant its own technical report. The development is attributed to "Gemma Team, Google DeepMind" — the combined research organization formed by the 2023 merger of Google Brain and DeepMind.

**[Gemma 3](/reviews/google-gemma-3-open-weights-multimodal-llm-review/)**, released March 2025, would later build directly on Gemma 2's architectural foundation — extending context to 128K, adding multimodal vision capability, and introducing QAT (quantization-aware training) variants. Understanding Gemma 2 is therefore also useful for understanding why Gemma 3 made the choices it did.

---

## The Model Family

Gemma 2 ships in three sizes, each in two variants:

| Model | Parameters (non-embedding) | Embedding Params | Training Tokens | Released |
|-------|---------------------------|------------------|-----------------|----------|
| Gemma 2 2B | 2.02B | 590M | 2T | July 31, 2024 |
| Gemma 2 9B | 8.32B | 918M | 8T | June 27, 2024 |
| Gemma 2 27B | 26.05B | 1.18B | 13T | June 27, 2024 |

The embedding parameters are notably large because Gemma 2 inherited the 256K vocabulary from Gemini. That large vocabulary improves multilingual tokenization efficiency but inflates the parameter count in the embedding layers.

**Each size has two variants:**
- **Base / pre-trained (PT)**: `google/gemma-2-2b`, `google/gemma-2-9b`, `google/gemma-2-27b`
- **Instruction-tuned (IT)**: `google/gemma-2-2b-it`, `google/gemma-2-9b-it`, `google/gemma-2-27b-it`

The IT models were fine-tuned with supervised fine-tuning on English prompt-response pairs, followed by RLHF with a reward model "an order of magnitude larger than the policy." The post-training also used model merging — averaging checkpoints from different hyperparameter runs — to improve final model quality.

All three sizes share the same context window: **8,192 tokens**. This is a significant constraint relative to contemporaneous competitors (Llama 3.1 at 128K, Mistral at 32K), and a limitation that Gemma 3 would later address.

---

## Architecture: What Gemma 2 Changed

Gemma 2's technical report identifies five architectural changes relative to Gemma 1. These are not incremental tuning decisions — several of them had meaningful practical consequences.

### Interleaved Local and Global Attention

Standard transformer architectures apply full (global) attention at every layer, where every token can attend to every other token in the context. This scales quadratically with sequence length, which makes extending context windows expensive.

Gemma 2 alternates between two attention patterns, layer by layer:
- **Local sliding-window attention** (odd layers): Each token attends only to a 4,096-token window around it. KV-cache memory grows linearly with window size, not sequence length.
- **Global attention** (even layers): Full attention over the entire 8,192-token context.

This 1:1 interleaving of local and global layers (which Gemma 3 later changed to a 5:1 ratio) substantially reduces memory pressure during inference. The trade-off is that information must propagate through multiple local-attention layers to travel across distant parts of the context, which can reduce performance on tasks requiring tight long-range dependencies.

The approach is conceptually related to Longformer (Beltagy et al., 2020) and was a precursor to the more aggressive 5:1 pattern that Gemma 3 would adopt for its 128K context extension.

### Grouped-Query Attention

Gemma 2 uses grouped-query attention (GQA) with `num_groups = 2` across all sizes. Rather than having a separate key-value head for each query head, multiple query heads share a single KV head:

| Size | Query heads | KV heads |
|------|-------------|----------|
| 2B | 8 | 4 |
| 9B | 16 | 8 |
| 27B | 32 | 16 |

This halves KV-cache memory relative to multi-head attention (MHA), reduces inference memory bandwidth requirements, and increases throughput — with ablation results suggesting minimal quality degradation at this grouping ratio.

### Logit Soft-Capping

A notable and somewhat unusual technique: Gemma 2 applies soft-capping to logits at two points — inside the self-attention layers and at the final output layer — using the formula:

```
logits ← soft_cap × tanh(logits / soft_cap)
```

The self-attention layers use `soft_cap = 50.0`; the output layer uses `soft_cap = 30.0`. This smoothly constrains logit magnitude without hard truncation, stabilizing training by preventing runaway activations.

**The practical consequence**: Logit soft-capping is **incompatible with Flash Attention and PyTorch SDPA**. If you fine-tune Gemma 2, you must use `attn_implementation="eager"` in Hugging Face Transformers, which is slower and more memory-intensive than Flash Attention. This is a real friction point for anyone building fine-tuned variants.

### Pre-Norm and Post-Norm

Gemma 1 applied only pre-norm (RMSNorm before each sub-layer). Gemma 2 applies both pre-norm and post-norm to each transformer sub-layer. The technical report attributes this to improved training stability, and it appears to have contributed to the ability to train the 27B from scratch without distillation.

### Knowledge Distillation (2B and 9B Only)

The most impactful change for the smaller models: rather than training the 2B and 9B via standard next-token prediction, Google used **knowledge distillation** from a larger teacher model. The student minimizes KL divergence between its token distribution and the teacher's, rather than cross-entropy against ground-truth tokens.

The teacher is described as "a large language model" without further specification — the presumption in the research community is that it is a Gemini variant. The effect is substantial: the 2B model showed 10%+ improvements on several benchmarks relative to Gemma 1 2B, improvements that exceed what would be expected from simply scaling training compute. The 27B was trained from scratch (not via distillation), which explains why its architecture changes (deeper networks) could be validated independently.

The training tokens also substantially exceed compute-optimal quantities per Chinchilla scaling laws: the 2B was trained on 2T tokens, the 9B on 8T tokens. Training "over-optimized" (more tokens than Chinchilla-optimal for the parameter count) produces better inference-time performance at the cost of more training compute — a reasonable trade-off for a model that will be downloaded and run millions of times.

---

## Architecture Parameters

| Parameter | 2B | 9B | 27B |
|-----------|----|----|-----|
| d_model | 2304 | 3584 | 4608 |
| Layers | 26 | 42 | 46 |
| Feedforward dim | 18,432 | 28,672 | 73,728 |
| Query heads | 8 | 16 | 32 |
| KV heads | 4 | 8 | 16 |
| Head size | 256 | 256 | 128 |
| Global attention span | 8,192 | 8,192 | 8,192 |
| Sliding window | 4,096 | 4,096 | 4,096 |
| Vocabulary | 256,128 | 256,128 | 256,128 |

Gemma 2 uses deeper networks (more layers, narrower per-layer width) rather than wider ones. Ablations confirmed deeper was better at these scales.

---

## Benchmarks

Benchmark results from the Gemma 2 technical report (Table 13), comparing against key competitors.

### Pre-Trained Model Benchmarks

| Benchmark | Gemma 1 7B | Llama 3 8B | Gemma 2 2B | Gemma 2 9B | Gemma 2 27B |
|-----------|------------|------------|------------|------------|-------------|
| MMLU (5-shot) | 64.4 | 66.6 | 52.2 | 71.3 | 75.2 |
| ARC-C (25-shot) | 61.1 | 59.2 | 55.7 | 68.4 | 71.4 |
| GSM8K (5-shot) | 51.8 | 45.7 | 24.3 | 68.6 | 74.0 |
| BBH (3-shot CoT) | 59.0 | 61.1 | 41.9 | 68.2 | 74.9 |
| MATH (4-shot) | 24.3 | — | 16.0 | 36.6 | 42.3 |
| HumanEval (pass@1) | 32.3 | — | 20.1 | 40.2 | 51.8 |
| MBPP (3-shot) | 44.4 | — | 30.2 | 52.4 | 62.6 |
| TriviaQA (5-shot) | 63.4 | — | 60.4 | 76.6 | 83.7 |
| WinoGrande (5-shot) | 79.0 | 76.1 | 71.3 | 80.6 | 83.7 |
| HellaSwag (10-shot) | 82.3 | 82.0 | 72.9 | 81.9 | 86.4 |

The 9B clears Gemma 1 7B on every benchmark. The 27B matches or approaches Llama 3 70B on several axes (ARC-C: 71.4 vs 68.8; GSM8K: 74.0 vs 76.9) while being 2.5× smaller in parameters. GPQA Diamond scores are not reported in the technical report — a notable omission for research capability assessment.

### Chatbot Arena ELO (Human Preference)

From the Gemma 2 technical report (Table 14), as of the paper's publication date:

| Model | ELO Score |
|-------|-----------|
| GPT-4o-2024-05-13 | 1286 |
| Claude 3.5 Sonnet | 1271 |
| Llama 3.1 405B | 1262 |
| Gemini 1.5 Flash | 1227 |
| **Gemma 2 27B IT** | **1218** |
| Llama 3 70B | 1206 |
| GPT-4-0314 | 1186 |
| **Gemma 2 9B IT** | ~1187 |
| GPT-3.5-Turbo-0613 | 1116 |
| **Gemma 2 2B IT** | ~1126 |

The 27B surpassed Llama 3 70B despite having 43B fewer parameters. The technical report described this as setting "a new state of the art on the LMSYS Chatbot Arena" for open-weights models at the time of release.

---

## Self-Hosting Requirements

All three sizes are available as open weights. VRAM requirements:

| Size | BF16 (full precision) | 8-bit | 4-bit |
|------|-----------------------|-------|-------|
| 2B | ~6–8 GB | ~3–4 GB | ~2–3 GB |
| 9B | ~18 GB | ~9–10 GB | ~5–6 GB |
| 27B | ~56 GB | ~28 GB | ~18 GB |

**Important**: The 27B model must be run in `bfloat16`. Running in `float16` produces erratic outputs — this is documented in the model card. Hardware that does not support bfloat16 natively (some older consumer GPUs) will not produce correct results.

The 9B model fits a single RTX 4090 at 4-bit quantization (~6 GB). The 27B at Q4_K_M GGUF (~16.6 GB) fits a single 24GB GPU. The 2B runs on CPU with 8+ GB RAM or any modern GPU.

**GGUF quantization** (via bartowski and other community contributors):

For the 9B model: IQ2_XS (3.07 GB) through Q8_0 (9.83 GB). Recommended: Q4_K_M (5.76 GB), Q5_K_M (6.65 GB).

For the 27B model: IQ2_XS (~8.4 GB) through Q8_0 (~28.9 GB). Recommended: Q4_K_M (16.6 GB), Q5_K_M (19.4 GB).

**Fine-tuning note**: As noted above, logit soft-capping requires `attn_implementation="eager"` during training. Flash Attention cannot be used with Gemma 2 during fine-tuning, which increases VRAM requirements relative to other models.

---

## Where to Run It

**HuggingFace** (primary distribution, login + license acceptance required):
- `google/gemma-2-2b` and `google/gemma-2-2b-it`
- `google/gemma-2-9b` and `google/gemma-2-9b-it`
- `google/gemma-2-27b` and `google/gemma-2-27b-it`

**Ollama** (easiest local setup):
- `ollama run gemma2` — defaults to 9B (5.4 GB download)
- `ollama run gemma2:2b` — 1.6 GB download
- `ollama run gemma2:27b` — 16 GB download

**Google AI Studio / Vertex AI Model Garden**: All sizes and variants, deployable via native Vertex AI or GKE with vLLM/TGI.

**Google Colab**: Runs on free T4 GPU tier.

**Inference frameworks**: vLLM, SGLang, Text Generation Inference (TGI), and LM Studio all support Gemma 2.

**OpenRouter** (hosted inference): `google/gemma-2-27b-it` and `google/gemma-2-9b-it` are available from third-party inference providers.

**Kaggle**: Available on the official Google Gemma 2 Kaggle model page.

---

## License

Gemma 2 uses the **Gemma Terms of Use** — not Apache 2.0, and not an OSI-compliant open source license.

Key terms:
- **Commercial use is permitted** — you can build commercial products on top of Gemma 2 models
- **Redistribution is allowed** — subject to including the Gemma Terms in downstream distributions
- **Prohibited use policy applies** — Google maintains a separate Prohibited Use Policy covering CSAM, facilitation of illegal activity, harassment, hate speech, deception/impersonation, and medical/financial/legal misinformation
- **Attribution required** — redistributions must include: "Gemma is provided under and subject to the Gemma Terms of Use found at ai.google.dev/gemma/terms"
- **Google claims no rights to outputs** — what you generate belongs to you

The practical effect: Gemma 2 is more permissive than a fully closed model, but less permissive than Apache 2.0 (which carries no prohibited-use conditions beyond patent terms). Organizations with legal review requirements may find the Gemma Terms easier to clear than a fully proprietary license, but Apache 2.0 models like [Mistral Small 3.1](/reviews/mistral-small-3-1-vision-24b-llm-review/) or [Mistral Small 4](/reviews/mistral-small-4-119b-moe-reasoning-vision-coding-llm-review/) remain the simpler licensing story.

HuggingFace access requires login and license acceptance before downloading model weights.

---

## The Broader Gemma 2 Ecosystem

The July 31, 2024 launch brought two additional releases alongside the 2B model:

**ShieldGemma** — Safety content classification models in 2B, 9B, and 27B sizes. Inputs: text prompt + safety policy guidelines. Outputs: "Yes" (violates policy) or "No" (compliant). Harm categories: sexually explicit content, dangerous content, hate speech, harassment. The ShieldGemma 2B achieved F1 of 0.825 on harm detection benchmarks, competitive with the OpenAI Moderation API (F1: 0.812). Suitable for content-moderation pipelines that require transparent, open-weights safety classifiers.

**Gemma Scope** — A set of sparse autoencoders trained on Gemma 2 residual stream activations, designed to support interpretability research. A research tool, not a production model — relevant to teams studying model internals.

**RecurrentGemma** (released separately, March 2024) — A 9B model using the Griffin recurrent architecture instead of transformer attention. Faster inference on long sequences: 25% faster than Gemma 7B at 4,096 tokens. Handles up to 16,384 tokens. MMLU: 60.5 (vs 71.3 for Gemma 2 9B). A niche choice for memory-constrained long-context inference where raw benchmark scores matter less than throughput.

---

## Known Limitations

**8K context window** — The most significant practical constraint relative to contemporaneous competition. Llama 3.1 (released July 23, 2024, less than a month after Gemma 2) shipped with 128K context across the 8B, 70B, and 405B sizes. Mistral shipped with 32K. For tasks requiring long documents, multi-turn conversation history, or extended code context, Gemma 2's 8K limit is a real barrier. Gemma 3 resolved this with 128K.

**Text-only** — No vision capability. Multimodal input came with [Gemma 3](/reviews/google-gemma-3-open-weights-multimodal-llm-review/) (March 2025). The separate PaliGemma (released March 2024) is a vision-language model in the Gemma ecosystem but is architecturally distinct from Gemma 2 — a SigLIP encoder paired with a Gemma 2B text backbone, not a full Gemma 2 model.

**English-centric training** — The technical report does not claim multilingual capability as a design goal. The 256K vocabulary helps with tokenization efficiency across languages, but benchmark performance on non-English tasks is not characterized in the report.

**Flash Attention incompatibility** — The logit soft-capping mechanism prevents use of Flash Attention or PyTorch SDPA during fine-tuning. This increases memory requirements and slows training. Inference (not fine-tuning) is unaffected.

**bfloat16 requirement (27B)** — Float16 produces erratic outputs on the 27B. Hardware without native bfloat16 support cannot correctly run the 27B model.

**GPQA not reported** — The technical report includes no GPQA Diamond or graduate-level reasoning benchmark scores, making it harder to place Gemma 2 in the research reasoning landscape alongside models like [DeepSeek R1](/reviews/deepseek-v3-r1-open-source-reasoning-llm/) or [Claude 3.5 Sonnet](/reviews/claude-3-5-sonnet-haiku-model-card-review/).

**Context efficiency vs raw length** — The interleaved sliding-window attention does reduce memory costs, but the 1:1 local-to-global ratio (every other layer global) is less aggressive than Gemma 3's 5:1 ratio. Gemma 2 still requires more memory per context token than more recent sliding-window designs.

---

## Assessment

Gemma 2 was a genuine step forward for open-weights models at its size tier in mid-2024. The combination of knowledge distillation (for the 2B and 9B), grouped-query attention, and the hybrid sliding-window architecture produced models that outperformed their parameter count on human preference evaluation — the 27B above the 70B, the 9B matching GPT-4-0314, the 2B above GPT-3.5.

The architectural contributions are substantive. The interleaved attention design influenced Gemma 3's more aggressive 5:1 sliding-window approach. The knowledge distillation training recipe for sub-10B models is a legitimate technique that has since become more common. The technical report is detailed and honest about design choices and tradeoffs.

The 8K context window is the clearest limitation — Llama 3.1's 128K context arrived less than a month after Gemma 2, making the context constraint feel dated almost immediately. The Flash Attention incompatibility from logit soft-capping is a real friction point for fine-tuning use cases. The Gemma Terms of Use is commercially permissive but adds legal review complexity relative to Apache 2.0.

In mid-2026, Gemma 2 is superseded by [Gemma 3](/reviews/google-gemma-3-open-weights-multimodal-llm-review/) (128K context, vision, QAT) and [Gemma 4](/reviews/google-gemma-4-open-weight-multimodal-llm-review/). If you are starting a new project, there is no reason to use Gemma 2 over Gemma 3. But Gemma 2 is worth understanding because it established the architectural foundation — the sliding-window pattern, the distillation training approach, the large vocabulary — that Gemma 3 built on.

**Rating: 4/5.** Landmark results for open-weights at mid-2024 density, meaningful architectural innovations, and honest documentation. Demerits for the 8K context limit (already behind competition at launch), Flash Attention incompatibility during fine-tuning, and the absence of GPQA or multilingual benchmarks in the technical report.

---

## Summary

| | |
|--|--|
| **Released** | June 27, 2024 (9B, 27B); July 31, 2024 (2B) |
| **Sizes** | 2B, 9B, 27B |
| **Context window** | 8,192 tokens (all sizes) |
| **Architecture** | Interleaved sliding-window + global attention, GQA, logit soft-capping, pre+post RMSNorm |
| **Training (2B, 9B)** | Knowledge distillation from large teacher model |
| **Training (27B)** | Standard pretraining from scratch |
| **License** | Gemma Terms of Use — commercial use permitted, not Apache 2.0 |
| **VRAM (BF16)** | ~7 GB / ~18 GB / ~56 GB |
| **VRAM (4-bit)** | ~3 GB / ~6 GB / ~18 GB |
| **Ollama** | `gemma2:2b` (1.6 GB), `gemma2` (5.4 GB), `gemma2:27b` (16 GB) |
| **HuggingFace** | `google/gemma-2-{2b,9b,27b}[-it]` |
| **Chatbot Arena ELO (27B IT)** | 1218 (beats Llama 3 70B at 1206) |
| **MMLU (2B / 9B / 27B)** | 52.2 / 71.3 / 75.2 |
| **MATH (2B / 9B / 27B)** | 16.0 / 36.6 / 42.3 |
| **HumanEval (2B / 9B / 27B)** | 20.1 / 40.2 / 51.8 |
| **Successor** | [Gemma 3](/reviews/google-gemma-3-open-weights-multimodal-llm-review/) (March 2025, 128K context, vision) |

