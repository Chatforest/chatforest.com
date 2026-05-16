# Mistral Large 2 Review — 123B Dense, 128K Context, Apache 2.0 Open-Weight Flagship

> Mistral Large 2 (July 24, 2024) delivers 123B parameters under Apache 2.0 — the first open-weight flagship from Mistral. MMLU 84.0%, HumanEval 92.0% (matching Claude 3.5 Sonnet), GSM8K 93.0%, MATH 71.5%. 128K context. 13 languages. Single-node at 73 GB Q4. Ollama: mistral-large. Rating: 4/5.


**At a glance:** Mistral Large 2, released July 24, 2024. 123B dense parameters. 128K context. Apache 2.0. HumanEval: 92.0% (matching Claude 3.5 Sonnet). MMLU: 84.0%. GSM8K: 93.0%. Ollama: `mistral-large`. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

Mistral Large 2 is the first time Mistral AI released a flagship-scale model under Apache 2.0. Every major Mistral release before it — Mistral Large 1, Mistral Medium — was accessible only via the La Plateforme API, with no downloadable weights and no open-source license. Mistral Large 2 changed that: 123 billion parameters, Apache 2.0, weights on HuggingFace.

The timing was deliberate. Meta released [Llama 3.1 70B and 405B](/reviews/meta-llama-3-1-405b-open-weights-llm-review/) on July 23, 2024 — one day before Mistral Large 2's announcement on July 24. Mistral's blog post, titled "Large Enough," made the positioning explicit: the 123B model does not need to beat 405B on every benchmark — it needs to deliver near-frontier performance on a single enterprise node, where the 405B cannot run without multi-node orchestration. That is the thesis Mistral Large 2 is built around.

On that specific claim, it mostly holds. HumanEval at 92.0% matched Claude 3.5 Sonnet at release — a genuine achievement for any open-weight model in July 2024. MMLU at 84.0% trails Claude 3.5 Sonnet (88.3%) and GPT-4o (88.7%) by a meaningful gap, but beats Llama 3.1 70B (79.3%) by nearly 5 points. The 123B parameter count enables single-node Q4 deployment at 73 GB — achievable on a 4× 24 GB GPU node, which is expensive but not exotic for enterprise workloads.

---

## Background: From API-Only to Open-Weight

[Mistral AI](/reviews/mistral-ai-company-llm-model-review/) launched in 2023 with a deliberate two-track strategy: open-weight small models (Mistral 7B, Mixtral 8x7B) and API-only large models (Mistral Medium, Mistral Large 1). The small models built community credibility and adoption. The large models generated API revenue. The weights for the large models were never published.

**Mistral Large 1** (February 26, 2024) was the predecessor to Large 2 on the API track. Context window: 32K tokens. Native languages: English, French, Spanish, German, Italian. No downloadable weights. No open-source license. It was introduced as "the world's second-ranked AI model" in Mistral's announcement — trailing GPT-4 but ahead of Claude 2 at release, per Mistral's own benchmarking. It was not publicly available for self-hosting.

Mistral Large 2 broke this model. The decision to release under Apache 2.0 — the same license as [Mistral NeMo](/reviews/mistral-nemo-12b-128k-context-llm-review/) earlier that month — represented a policy shift: flagship-scale capability was now open-weight. This aligned Mistral more directly with Meta's strategy and against OpenAI's API-only model.

The November 2024 update — `mistral-large-2411` — made incremental refinements to the same model but did not change the architecture or the license. The core July 2024 release is what the industry refers to as "Mistral Large 2."

---

## Architecture

Mistral Large 2 is a dense decoder-only Transformer. No mixture-of-experts routing. Every token activates the full 123 billion parameters on every forward pass.

| Property | Value |
|---|---|
| Total parameters | 123 billion |
| Architecture | Dense decoder-only Transformer |
| Layers | 64 |
| Hidden dimension | 12,288 |
| Attention heads (query) | 48 |
| KV heads | 8 (Grouped Query Attention) |
| FFN activation | SwiGLU |
| Normalization | RMS Normalization |
| Context window | 128,000 tokens (128K) |
| Tokenizer | Mistral V3 (byte-fallback BPE, 131K vocabulary) |
| HuggingFace ID | `mistralai/Mistral-Large-Instruct-2407` |

The Mistral V3 tokenizer is shared with Mixtral 8x22B, [Mistral Codestral](/reviews/mistral-codestral-22b-code-fill-in-the-middle-llm-review/), and Mathstral 7B. It uses byte-fallback BPE, which means the tokenizer never produces unknown tokens — any byte sequence can be encoded, which improves robustness on non-Latin scripts and source code. Vocabulary size of 131K is substantially larger than the 32K used in earlier Mistral models (7B, Mixtral 8x7B), which improves tokenization efficiency across languages.

The 64-layer depth with GQA (8 KV heads against 48 query heads) is the same GQA configuration used in [Mistral NeMo 12B](/reviews/mistral-nemo-12b-128k-context-llm-review/) — a 6:1 ratio that substantially reduces KV cache memory at inference compared to multi-head attention, enabling longer effective context utilization on memory-constrained hardware.

The 128K context window represents a 4× expansion over Mistral Large 1's 32K — catching up to the 128K window that had become a competitive baseline by mid-2024 ([Gemini 1.5 Pro](/reviews/google-gemini-1-5-pro-multimodal-llm-review/) had already pushed to 1M tokens; Claude 3.5 Sonnet supported 200K).

---

## Training

Mistral AI has not published a technical paper for Large 2 with full training details. What is publicly documented:

**Pretraining corpus**: A large multilingual dataset emphasizing both human language diversity and source code. Mistral states the model was trained on "a large proportion of multilingual text" covering the 13 documented languages, plus "a substantial corpus of source code" across 80+ programming languages. Specific token count and dataset composition are not disclosed.

**Post-training**: The instruct variant (`Mistral-Large-Instruct-2407`) received supervised fine-tuning and alignment training — the specific methodology (RLHF, DPO, or a hybrid) was not published. The model shows strong instruction-following behavior, native function calling, and JSON output mode, all of which require post-training to function reliably.

**Fine-tuning availability**: Fine-tuning for Large 2 was made available on La Plateforme at launch, implying the base model and instruct model were separately trained and offered.

---

## Benchmarks

All figures are for the instruct variant (`Mistral-Large-Instruct-2407`) unless noted.

| Benchmark | Score | Notes |
|---|---|---|
| MMLU (5-shot) | 84.0% | General knowledge across 57 subjects |
| HumanEval (pass@1) | 92.0% | Code generation |
| GSM8K | 93.0% | Grade school math word problems |
| MATH | 71.5% | Competition-level mathematics |

### Competitive context (July 2024)

| Model | Params | MMLU | HumanEval | GSM8K | License |
|---|---|---|---|---|---|
| **Mistral Large 2** | 123B dense | 84.0% | 92.0% | 93.0% | Apache 2.0 |
| Llama 3.1 70B | 70B dense | 79.3% | 80.5% | 93.0% | Llama Community |
| Llama 3.1 405B | 405B dense | 85.1% | 89.0% | 96.8% | Llama Community |
| GPT-4o (July 2024) | Undisclosed | 88.7% | 90.2% | 95.3% | Proprietary |
| Claude 3.5 Sonnet | Undisclosed | 88.3% | 92.0% | 96.4% | Proprietary |

The HumanEval tie with Claude 3.5 Sonnet (both 92.0%) was the headline benchmark in Mistral's launch announcement — a valid data point, and genuinely impressive for an open-weight model at the 123B scale.

MMLU tells a different story. At 84.0%, Mistral Large 2 beats Llama 3.1 70B by 4.7 points but trails Llama 3.1 405B (85.1%), Claude 3.5 Sonnet (88.3%), and GPT-4o (88.7%). It occupies the upper tier of open-weight models — definitively better than 70B-class — without reaching frontier-tier general knowledge performance.

GSM8K at 93.0% is strong but not exceptional in the July 2024 field. MATH at 71.5% is competitive for a non-reasoning model — this predates the extended chain-of-thought architectures (OpenAI o1 launched September 2024) that would substantially raise the ceiling on competition mathematics tasks.

---

## Languages

Mistral Large 2 supports 13 human languages natively — a significant expansion from Mistral Large 1's five (English, French, Spanish, German, Italian):

- English, French, German, Spanish, Italian, Portuguese
- Dutch, Russian, Chinese (Mandarin), Japanese, Korean, Arabic, Hindi

The expansion to Arabic (right-to-left script), Chinese, Japanese, Korean, and Hindi reflects the larger and more diverse multilingual training corpus, aided by the Mistral V3 tokenizer's improved encoding efficiency for non-Latin scripts.

Programming language support: 80+, with explicit documentation of Python, Java, C, C++, JavaScript, TypeScript, Bash, Go, Rust, SQL.

---

## VRAM and Deployment

Mistral Large 2 is not consumer hardware. The 123B parameter count requires enterprise-grade multi-GPU configurations for practical deployment:

| Precision | VRAM Required | Notes |
|---|---|---|
| BF16 (full precision) | ~246 GB | 3× H100 80 GB minimum |
| Q8_0 | ~130 GB | 2× H100 or 6-7× 24 GB GPU |
| Q4_K_M | ~73 GB | 4× RTX 3090/4090 or 4× A100 40 GB |
| Q2_K | ~45 GB | Aggressive, notable quality loss |

**Ollama**: Available as `mistral-large`. Default tag pulls Q4_K_M at approximately 73 GB. Specific tags:
- `mistral-large:123b-instruct-2407-q4_K_M` (73 GB, recommended)
- `mistral-large:123b-instruct-2407-q5_K_M` (86 GB)
- `mistral-large:123b-instruct-2407-fp16` (245 GB)

At Q4_K_M the model fits on a 4× 24 GB GPU node — achievable with consumer RTX 4090 cards, which cost roughly $1,600–2,000 each as of 2024. It is not a living-room deployment. But it is meaningfully more approachable than Llama 3.1 405B, which requires 800+ GB and multi-node infrastructure.

Inference speed: Artificial Analysis benchmarked the November 2024 variant at approximately 31.9 tokens per second — below median for comparable open-weight models (around 72 t/s). The dense 123B architecture without MoE routing means every parameter is active on every token, which constrains throughput relative to sparse models serving the same effective capability.

---

## API Access

Via La Plateforme at launch:
- **Input**: $2.00 per million tokens
- **Output**: $6.00 per million tokens
- API identifier: `mistral-large-2407`

This placed Large 2 at the expensive end of the market for open-weight models — the Apache 2.0 license enabled self-hosting, but API users paid frontier model prices. By comparison, Mistral Large 3 (December 2025) launched at $0.50 input / $1.50 output — a 75% reduction in cost reflecting both the efficiency gains from MoE architecture and competitive pricing pressure.

The model was also available through Amazon Bedrock, Microsoft Azure AI Studio, Google Cloud Vertex AI, IBM WatsonX, and Snowflake Cortex AI — Mistral's cloud partnership portfolio as of July 2024.

---

## Weaknesses

**Not a reasoning model.** Large 2 predates the extended chain-of-thought paradigm. OpenAI o1 launched in September 2024; Mistral's own reasoning model (Magistral) did not arrive until June 2025. For tasks requiring multi-step deductive reasoning — competition mathematics beyond MATH, complex code debugging, formal logic — the architecture does not provide a pathway to scale compute against a problem the way reasoning models do.

**Text-only input.** No image, audio, or document parsing. Large 2 is a text-in, text-out model. This was addressed in [Mistral Large 3](/reviews/mistral-large-3-moe-vision-256k-context-llm-review/) (December 2025), which added multimodal image input.

**Multi-GPU enterprise hardware required.** The 123B dense architecture means Q4 deployment at 73 GB — four enterprise or prosumer GPUs minimum. This is accessible to well-resourced teams, not individuals. Smaller developers on the same Apache 2.0 requirement were better served by [Mistral NeMo 12B](/reviews/mistral-nemo-12b-128k-context-llm-review/) (7 GB Q4) or [Mistral Small 3.x](/reviews/mistral-small-3-1-vision-24b-llm-review/) (15 GB Q4) at the same license tier.

**No built-in content moderation.** Mistral explicitly shipped Large 2 without embedded safety filters, stating the model relies on community-developed guardrails. This is consistent with Mistral's general philosophy of providing capability without baked-in content restrictions, but it creates integration overhead for production deployments in regulated or consumer-facing contexts.

**API pricing.** At $2.00/$6.00 per million tokens, self-hosting on capable hardware often penciled out cheaper than sustained API use for high-volume workloads. The Apache 2.0 license made this a viable option — but the model weights required hardware few organizations had on hand in 2024.

---

## Successor: Mistral Large 3

[Mistral Large 3](/reviews/mistral-large-3-moe-vision-256k-context-llm-review/) launched December 2, 2025. It is architecturally distinct from Large 2:

- **MoE architecture**: 675B total parameters, 41B active per token — versus Large 2's dense 123B
- **Context**: 256K tokens (2× Large 2's 128K)
- **Vision**: Multimodal image input added (Large 2 is text-only)
- **Languages**: 40+ human languages (3× Large 2's 13)
- **License**: Apache 2.0 retained
- **API pricing**: $0.50 input / $1.50 output per million tokens — 75% cheaper than Large 2 at launch
- **Reasoning**: Still not a native reasoning model at launch, consistent with Large 2

For most use cases where Large 2 was appropriate in late 2024 and 2025, Mistral Large 3 is now the correct choice — better capability, lower cost, multimodal support, and the same license. Large 2 retains relevance only for deployments locked to specific model identifiers or where the November 2024 variant has been heavily fine-tuned.

---

## Rating: 4/5

Mistral Large 2 was a significant release in July 2024. The Apache 2.0 license at 123B scale was a genuine policy change for Mistral — the first time flagship-class capability was available for self-hosting and commercial use without a Mistral API agreement. The HumanEval 92% score matching Claude 3.5 Sonnet was not marketing noise; it was a real benchmark result that held up against scrutiny.

The case for 5/5 fails on the gaps: MMLU trails frontier models by 4–5 percentage points, hardware requirements exclude everyone without four high-end GPUs, inference throughput is below the open-weight median, and the text-only architecture was already one cycle behind multimodal competitors at launch. For a model positioned as a flagship, those limitations matter.

At 4/5, Mistral Large 2 earns its rating as a capable, honestly licensed model that solved a specific real problem — open-weight, single-node, near-frontier — for the teams with hardware to run it. Its 2025 and 2026 successors addressed most of the weaknesses. The original release holds up as the model that changed Mistral's open-weight strategy at scale.

---

*Part of our [Mistral AI coverage](/reviews/mistral-ai-company-llm-model-review/). Related: [Mistral NeMo 12B](/reviews/mistral-nemo-12b-128k-context-llm-review/) — the Apache 2.0 small model from the same July 2024 period. [Mistral Codestral](/reviews/mistral-codestral-22b-code-fill-in-the-middle-llm-review/) — the code-specialist 22B from May 2024. [Mistral Large 3](/reviews/mistral-large-3-moe-vision-256k-context-llm-review/) — the December 2025 MoE successor.*

