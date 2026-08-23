# Cohere Command A+ Review: 218B Sparse MoE, Apache 2.0, and Native Citations Built In

> Cohere Command A+ (May 20, 2026) is a 218B sparse MoE model with 25B active parameters per token, Apache 2.0 license, and native citation generation built into the architecture. First multimodal Cohere model. Runs on 2×H100 or 1×B200 GPU. Cohere has not published public per-token API pricing for it. Artificial Analysis Intelligence Index: 37 at launch (23 as of Aug 2026 under AA's revised v4.1 methodology). Knowledge cutoff April 2025. The Apache 2.0 licensing and enterprise citation feature are the headline story. Rating: 3.5/5.


**At a glance:** Cohere Command A+, released May 20, 2026. 218B sparse MoE, 25B active parameters per token. Apache 2.0 license. Native citation generation. No public per-token API pricing published by Cohere. Artificial Analysis Intelligence Index: 37 at launch, 23 as of this audit under AA's revised methodology. Knowledge cutoff April 1, 2025. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

Cohere's most important announcement in Command A+ has nothing to do with a benchmark.

Cohere's prior model, Command R+, shipped under CC-BY-NC 4.0 — meaning commercial deployment required an enterprise license from Cohere. You could evaluate it, research with it, and integrate it in non-commercial contexts, but the moment you shipped a product, you needed a licensing conversation. Command A+ drops that requirement entirely. Apache 2.0. Full commercial use. No revenue caps. No non-compete clauses. Take the weights, fine-tune on your classified data, deploy on an air-gapped server, ship a product. Cohere gets nothing from you except attribution in the license file.

That licensing shift, paired with a 218B sparse MoE architecture that runs on two H100 GPUs, makes Command A+ the most practically deployable open-weight enterprise model in the market. Cohere has not published public per-token API pricing for Command A+ (see [Pricing](#pricing) below); whether the self-hosting economics or a custom enterprise deal make sense — against alternatives that are cheaper or more capable on raw benchmarks — depends on what you're building.

---

## Release Context

Command A+ was [announced **May 20, 2026**](https://cohere.com/blog/command-a-plus) in a blog post titled "Introducing Command A+: Our Most Open, Capable, and Efficient Model Yet."

The release is a substantial departure from Cohere's prior release cadence. Command A (the predecessor) was released in March 2025 under CC-BY-NC 4.0 — the same terms as Command R+. Command A Reasoning, a thinking-mode variant, arrived later under similar restrictions. Command A+ collapses both into a single model with a fundamentally different license.

**Predecessor comparison:**

| Model | License | Architecture | Multimodal |
|---|---|---|---|
| Command R+ | CC-BY-NC 4.0 | Dense | No |
| Command A | CC-BY-NC 4.0 | MoE | No |
| Command A Reasoning | CC-BY-NC 4.0 | MoE | No |
| **Command A+** | **Apache 2.0** | **Sparse MoE** | **Yes** |

The licensing transition is the headline. The multimodal addition — Cohere's first — is the capability headline. Both matter.

---

## Architecture

### Sparse MoE with Selective Quantization

Command A+ uses a **sparse Mixture-of-Experts** decoder with 218 billion total parameters organized across 128 experts. Each token activates 8 experts plus 1 shared expert — meaning **25 billion parameters are active per inference call**, not 218 billion. This is the same architectural efficiency principle as Mistral Small 4 (6B of 119B active) or DeepSeek V4 (49B of 1.6T active): total parameter count overstates the compute cost of any single forward pass.

The genuinely innovative piece in Command A+ is **Quantization-Aware Distillation (QAD)**: rather than applying uniform quantization across the model, QAD preserves attention pathway weights at full precision while quantizing only the MoE expert layers. The result is near-lossless W4A4 quantization — Cohere claims the compressed model retains quality while running on significantly less hardware. Independent verification of "near-lossless" claims will take time to accumulate from the research community, but the hardware footprint reduction is concrete.

**W4A4 performance numbers (Cohere-reported, independently confirmed by [VentureBeat](https://venturebeat.com/technology/cohere-cracks-lossless-quantization-and-native-citations-with-first-full-apache-2-0-licensed-open-model-command-a)):**
- Output throughput: [375 tokens/second](https://venturebeat.com/technology/cohere-cracks-lossless-quantization-and-native-citations-with-first-full-apache-2-0-licensed-open-model-command-a) at low concurrency
- Time-to-First-Token: 113ms
- Hardware: 2×H100 or 1×Blackwell B200

For comparison: Command A Reasoning ran at ~237 tokens/second on the same inference setup. The QAD-compressed Command A+ is 63% faster than its predecessor while fitting on fewer GPUs.

### Specifications

| Specification | Value |
|---|---|
| Total parameters | 218B |
| Active parameters per token | 25B (8 of 128 experts + 1 shared) |
| Context window | 128,000 tokens input / 64,000 output |
| Modalities | Text + image input; text output |
| Languages | 48 (up from 23 in Command A) |
| Architecture | Sparse MoE decoder |
| Min. hardware (W4A4) | 2×H100 80GB or 1×NVIDIA B200 |
| Knowledge cutoff | April 1, 2025 |

---

## The Apache 2.0 Licensing Story

The license is what builders should read carefully before anything else.

**Apache 2.0 means:**
- Commercial use with no restrictions
- Modification and redistribution permitted
- No revenue caps (unlike Mistral's $20M/month Modified MIT)
- No non-compete clauses (unlike some Meta Llama licenses)
- Fine-tuning and derivative models permitted under same terms
- Air-gapped deployment — weights, quantization files, and all artifacts on HuggingFace are fully downloadable

**What this unlocks for enterprise:**

The practical unlock is in regulated industries. A hospital system building clinical decision support can fine-tune Command A+ on proprietary patient data without those data ever leaving their infrastructure. A financial institution can deploy Command A+ on hardware that has never touched the public internet. A defense contractor can run Command A+ on a classified network. None of these use cases were legally clean with CC-BY-NC 4.0 without a separate enterprise agreement.

**Comparison to the competition:**

| Model | License | Commercial use |
|---|---|---|
| Command A+ | Apache 2.0 | Unrestricted |
| Mistral Large 3 | Apache 2.0 | Unrestricted |
| Mistral Medium 3.5 | Modified MIT | Revenue cap ($20M/month) |
| Meta Llama 4 Scout/Maverick | Llama Community | MAU restrictions |
| Gemma 4 | Gemma Terms of Service | Some restrictions |
| DeepSeek V4 | MIT | Unrestricted |

Command A+ and Mistral Large 3 share the most open licensing profile among frontier-adjacent models. What differentiates them is Cohere's enterprise feature set: primarily the native citation system.

---

## Native Citations

This is the genuinely unique feature in Command A+, and it's worth explaining in detail.

Most RAG pipelines handle citation attribution as a post-processing step: the model generates an answer, then a separate component matches phrases in the answer to source chunks. This is fragile — the phrase matching can fail, the model can generate plausible-sounding content that doesn't map cleanly to a source, and the citation layer adds latency and infrastructure complexity.

Command A+ generates citations during inference using **`<co>` / `</co>` tags** that wrap factual claims directly in the output. Each tag links to a source document or database row by reference. There is no post-processing step — the model is trained to attribute as it generates.

**Practical implications:**

- Every factual claim in a response carries a machine-readable citation to its source
- Suitable for direct use in legal documents, clinical notes, financial reports — contexts where unsourced AI-generated claims are a liability
- Reduces the engineering complexity of building citation-aware RAG pipelines
- Cohere reports 20% improvement in "Agentic Question Answering accuracy" over Command A Reasoning, partly attributed to multimodal document understanding feeding into more accurate citations

For teams building in regulated industries, this is a meaningfully different capability from what other open-weight models provide. No other major open-weight model ships with architecture-level citation generation trained into the model itself.

---

## Benchmarks

### Agentic Performance: The Highlight Numbers

| Benchmark | Command A | Command A+ | Change |
|---|---|---|---|
| τ²-Bench Telecom | 37% | **85%** | +48 points |
| Terminal-Bench Hard (agentic coding) | 3% | **25%** | +22 points |
| AIME 25 (math) | 57% | **90%** | +33 points |
| Agentic QA Accuracy | baseline | +20% | — |
| Spreadsheet Analysis | baseline | +32% | — |

These are generation-over-generation improvements versus Command A Reasoning, [reported by Cohere](https://cohere.com/blog/command-a-plus), not absolute comparisons to frontier models. The τ²-Bench Telecom jump from 37% to 85% is the headline: Cohere's own agentic benchmark shows a substantial capability increase for sustained multi-step tool use.

### Broader Benchmarks

| Benchmark | Command A+ | Context |
|---|---|---|
| MMMU Pro | 63% | Multimodal reasoning |
| MMMU | 75.1% | Multimodal understanding |
| MathVista | 80.6% | Math + visual |
| CharXiv Reasoning | 52.7% | Chart reasoning |
| HLE | [~11%](https://venturebeat.com/technology/cohere-cracks-lossless-quantization-and-native-citations-with-first-full-apache-2-0-licensed-open-model-command-a) | Scientific reasoning |
| GPQA Diamond | [76%](https://venturebeat.com/technology/cohere-cracks-lossless-quantization-and-native-citations-with-first-full-apache-2-0-licensed-open-model-command-a) | Graduate-level science |
| AI Intelligence Index (Artificial Analysis) | **37 at launch / 23 current** | Composite (see below) |

### What the Intelligence Index Tells You

At launch, Command A+ scored [**37** on the Artificial Analysis Intelligence Index](https://artificialanalysis.ai/articles/cohere-launches-open-weights-model-command-a-more-than-a-year-since-the-command-a-release) (May 20, 2026) — in line with Claude 4.5 Haiku and just above NVIDIA Nemotron 3 Super at the time. **Update (August 2026):** Artificial Analysis has since revised its Intelligence Index methodology ([v4.1](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), introduced June 2026), which recalculated scores across every model on the index — not something specific to Command A+. As of this audit, Command A+ scores [**23**](https://artificialanalysis.ai/models/command-a-plus) on the current version of the index. Current scores for the same comparison set:

| Model | Intelligence Index (current, AA v4.1) |
|---|---|
| [Claude Opus 4.7](https://artificialanalysis.ai/models/claude-opus-4-7) | 55 |
| [GPT-5.5 (high)](https://artificialanalysis.ai/models/gpt-5-5-high) | 55 |
| [Gemini 3.1 Pro Preview](https://artificialanalysis.ai/models/gemini-3-1-pro-preview) | 48 |
| [Mistral Medium 3.5](https://artificialanalysis.ai/models/mistral-medium-3-5) | 30 |
| **Command A+** | **23** |

The relative story hasn't changed even though the absolute numbers have: Command A+ still trails Mistral Medium 3.5 on the composite index, and remains well below the frontier cluster. For tasks that require deep reasoning or graduate-level science (11% on HLE), Command A+ is not the best available option. Cohere's own launch materials do not include a dedicated coding benchmark for Command A+, so builders evaluating code-heavy use cases have no first-party signal here and should benchmark independently rather than assume parity with frontier coding models.

The benchmark profile is consistent with a model optimized for **enterprise tool use and RAG workflows** rather than raw reasoning capability. That's a legitimate product positioning — just not a frontier-tier general-purpose claim.

---

## Pricing

**Cohere API:** As of this audit (August 2026), Cohere has not published public per-token pricing for Command A+. It does not appear on [Cohere's public pricing page](https://cohere.com/pricing) (which lists only legacy models like Command and Command R+ 08-2024 at public rates), and [Cohere's own model documentation](https://docs.cohere.com/docs/command-a-plus) does not list a price for it either — access to hosted inference is arranged directly with Cohere rather than through a published self-serve rate card. Some third-party cost trackers list $2.50 input / $10.00 output per million tokens for Command A+, but that figure is identical to Command R+ 08-2024's published rate and could not be independently confirmed as Command A+'s own pricing from a Cohere source; treat it with caution until Cohere publishes a rate card for this model.

| Model | Input ($/M) | Output ($/M) | License |
|---|---|---|---|
| **Command A+** | *not publicly disclosed* | *not publicly disclosed* | Apache 2.0 |
| [Command R+ 08-2024](https://cohere.com/pricing) (predecessor) | $2.50 | $10.00 | CC-BY-NC |
| [GPT-5.5](https://developers.openai.com/api/docs/pricing) | $5.00 | $30.00 | Closed |
| [Claude Opus 4.7](https://platform.claude.com/docs/en/about-claude/pricing) | $5.00 | $25.00 | Closed |
| [Mistral Medium 3.5](https://mistral.ai/pricing/api) | $1.50 | $7.50 | Modified MIT |
| [DeepSeek V4 Pro](https://deepseek.ai/pricing) | $0.44 | $0.87 | MIT |

*(Table corrected 2026-08-23: the prior version of this table understated Command R+'s current rate, overstated Claude Opus 4.7's rate roughly 5x, understated GPT-5.5's output rate, and stated a Command A+ price that Cohere's own pricing and docs pages do not support. See sources linked in each row.)*

Without confirmed API pricing for Command A+ itself, a direct cost comparison against these alternatives isn't possible from public information. What is clear: self-hosting the Apache 2.0 weights sidesteps the question entirely.

For teams self-hosting: inference cost is whatever your hardware costs. At W4A4 on 2×H100, the marginal cost of additional output tokens is compute amortization, not a metered API fee. Self-hosting is where the Apache 2.0 license and efficient quantization combination delivers the most value — and, per Cohere's own materials, appears to be the primary way Command A+ is actually being accessed.

---

## Self-Hosting

The "runs on 2×H100" headline is accurate for the W4A4 quantized version. Practical details:

- **BF16 full precision:** ~8×H100 80GB (full precision MoE inference requires more memory due to all expert weights being loaded)
- **FP8:** ~4×H100 80GB
- **W4A4 (QAD quantized):** 2×H100 80GB or 1×NVIDIA B200 — the deployment target for the headline claim

At W4A4, Cohere reports 375 tokens/second output throughput and 113ms time-to-first-token. For most agentic applications (tool use, RAG, document processing), 375 t/s is more than adequate.

**Available on HuggingFace (CohereLabs):**
- BF16 weights: [CohereLabs/command-a-plus-05-2026](https://huggingface.co/CohereLabs/command-a-plus-05-2026)
- FP8: [CohereLabs/command-a-plus-05-2026-fp8](https://huggingface.co/CohereLabs/command-a-plus-05-2026-fp8)
- W4A4: quantized via QAD (Cohere's tooling)

vLLM and standard Transformers inference are supported from day one. [Azure AI Foundry integration](https://docs.cohere.com/docs/command-a-plus) is listed at launch (deployment ID `coherelabs-command-a-plus-05-2026-w4a4`); Cohere's own dashboard, AWS Bedrock, SageMaker, and Oracle listings show it as not yet available or coming soon.

---

## Multimodal

Command A+ is Cohere's first model to accept image input. The vision capability is focused on **document and spreadsheet processing** — the 32% improvement in spreadsheet analysis and 20% improvement in agentic QA accuracy are the multimodal capability claims Cohere leads with.

This is not a general image understanding model in the style of GPT-4o or Gemini 3.1 Pro. The MMMU scores (75.1%) are competitive but not leading. The practical use case is: upload a PDF, a chart, or a spreadsheet alongside a text query, and Command A+ will reason across both. For enterprise document workflows, that's the capability that matters. For general multimodal tasks, frontier alternatives are more capable.

---

## Comparison to the Cohere Ecosystem

**vs. Command R+ (the predecessor):** Command A+ is faster, multimodal, more capable on agentic benchmarks, more permissively licensed, and supports 48 vs. 23 languages. Command R+ should be retired for new projects.

**vs. Command A Reasoning:** Command A+ replaces Command A Reasoning as the flagship. The capability improvements (τ²-Bench +48 points, AIME +33 points) are substantial. The license upgrade (Apache 2.0 vs. CC-BY-NC) is the procurement argument.

**The self-hosting thesis:** Cohere's bet with Command A+ is that enterprise builders who need data sovereignty and citation-quality RAG will self-host rather than use the API. Apache 2.0 + W4A4 efficiency + native citations + 48 languages is a package designed for that buyer. The API exists for teams that want managed inference without the hardware commitment.

---

## Who Should Use Command A+

**Strong fit:**
- Regulated industry RAG pipelines (legal, finance, healthcare) that need machine-readable citations on factual claims
- Sovereign AI deployments requiring air-gapped or on-premise infrastructure with no vendor agreement
- Multilingual enterprise applications (48 languages, including several not well-served by US-headquartered models)
- Teams whose primary bottleneck is licensing flexibility, not raw reasoning capability

**Weak fit:**
- Coding-heavy applications — Cohere has not published a coding-specific benchmark for Command A+; teams should test it directly against GPT-5.5 or Claude Opus 4.7 rather than assume parity
- Graduate-level scientific reasoning — HLE at 11% is a significant gap vs. frontier models
- Latency-sensitive consumer applications — 113ms TTFT is competitive but not leading
- Knowledge cutoff sensitive applications — April 2025 is 13 months old at launch; if recency matters, check alternatives

---

## Rating: 3.5/5

**What earns the 3.5:**

The Apache 2.0 licensing is a genuine unlock — particularly for regulated industries and government deployments where CC-BY-NC required a separate agreement. Native citations are architecturally unique in the open-weight space: no other comparable model ships citation generation as a trained capability rather than a post-processing layer. The QAD quantization achieving 375 t/s on 2×H100 is a real infrastructure story, not a marketing claim. τ²-Bench Telecom at 85% (from 37%) represents a substantial agentic capability improvement for multi-step tool use.

**What limits the score:**

The AI Intelligence Index places Command A+ in the capable-but-not-frontier tier — 37 at launch (in the same band as Mistral Medium 3.5's then-39), and 23 as of this audit under Artificial Analysis's revised v4.1 methodology (Mistral Medium 3.5 now 30; the frontier cluster of GPT-5.5, Claude Opus 4.7, and Gemini 3.1 Pro now sits around 48-55). Either way, Command A+ trails Mistral Medium 3.5 and sits well below frontier models on this composite. The knowledge cutoff of April 1, 2025 was already 13 months old at launch — a meaningful gap for applications requiring current information. Cohere has not published public API pricing for Command A+, so a head-to-head cost comparison with Mistral Medium 3.5 ($1.50/$7.50) or other hosted alternatives isn't possible from public information. And Cohere has not published coding benchmarks for Command A+ — the most common reason builders reach for open-weight models — leaving that gap unaddressed rather than explicitly conceded.

Command A+ is the right model for a specific buyer profile: enterprise teams who need data sovereignty, machine-readable citations, and Apache 2.0 licensing for regulated industry deployments. For everyone else, the capability-to-cost profile relative to DeepSeek V4, Mistral alternatives, or the Qwen 3.x family requires more justification.

---

## Quick Reference

| | |
|---|---|
| **Company** | Cohere (Toronto, Canada) |
| **Released** | May 20, 2026 |
| **Parameters** | 218B total / 25B active per token |
| **Architecture** | Sparse MoE (128 experts, 8+1 active) |
| **Context** | 128K input / 64K output |
| **Modalities** | Text + image input; text output |
| **Languages** | 48 |
| **τ²-Bench Telecom** | 85% |
| **AIME 25** | 90% |
| **MMMU** | 75.1% |
| **Intelligence Index** | 37 at launch / 23 current (Artificial Analysis composite, v4.1 methodology) |
| **API pricing** | Not publicly disclosed by Cohere as of this audit |
| **License** | Apache 2.0 (no restrictions) |
| **HuggingFace** | CohereLabs/command-a-plus-05-2026 |
| **Min. hardware** | 2×H100 80GB (W4A4) or 1×B200 |
| **Knowledge cutoff** | April 1, 2025 |
| **Rating** | 3.5 / 5 |

---

---

## Sources

- [Introducing Command A+: Our Most Open, Capable, and Efficient Model Yet — Cohere blog, May 20, 2026](https://cohere.com/blog/command-a-plus) — architecture, benchmarks, licensing, hardware requirements
- [CohereLabs/command-a-plus-05-2026 — HuggingFace](https://huggingface.co/CohereLabs/command-a-plus-05-2026) — model weights, architecture details
- [Command A+ — docs.cohere.com](https://docs.cohere.com/docs/command-a-plus) — model card: context length, hardware, Azure AI Foundry availability, no published pricing
- [Cohere pricing page](https://cohere.com/pricing) — confirms no public Command A+ rate; legacy Command R+ 08-2024 rate ($2.50/$10.00 per M tokens)
- [Cohere cracks lossless quantization and native citations... — VentureBeat, May 20, 2026](https://venturebeat.com/technology/cohere-cracks-lossless-quantization-and-native-citations-with-first-full-apache-2-0-licensed-open-model-command-a) — independent confirmation of 375 tok/s throughput, 113ms TTFT, AIME 25, HLE, GPQA Diamond scores
- [Cohere launches open weights model Command A+ — Artificial Analysis, May 20, 2026](https://artificialanalysis.ai/articles/cohere-launches-open-weights-model-command-a-more-than-a-year-since-the-command-a-release) — launch-day Intelligence Index score (37)
- [Command A+ — Artificial Analysis Intelligence Index (current)](https://artificialanalysis.ai/models/command-a-plus) — current composite score (23) under AA's revised methodology
- [Artificial Analysis Intelligence Index v4.1.1 methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) — explains the June 2026 index-wide recalculation
- Current Intelligence Index scores for comparison models: [Claude Opus 4.7](https://artificialanalysis.ai/models/claude-opus-4-7), [GPT-5.5 (high)](https://artificialanalysis.ai/models/gpt-5-5-high), [Gemini 3.1 Pro Preview](https://artificialanalysis.ai/models/gemini-3-1-pro-preview), [Mistral Medium 3.5](https://artificialanalysis.ai/models/mistral-medium-3-5)
- Current competitor API pricing: [OpenAI GPT-5.5](https://developers.openai.com/api/docs/pricing), [Anthropic Claude Opus 4.7](https://platform.claude.com/docs/en/about-claude/pricing), [Mistral Medium 3.5](https://mistral.ai/pricing/api), [DeepSeek V4 Pro](https://deepseek.ai/pricing)

---

*Related ChatForest reviews: [Cohere Enterprise Platform](/reviews/cohere-enterprise-llm-rag-platform/) · [Mistral Medium 3.5](/reviews/mistral-medium-3-5-dense-128b-agentic-llm-review/) · [Mistral Large 3](/reviews/mistral-large-3-open-weight-moe-llm-review/) · [DeepSeek V4](/reviews/deepseek-v4-open-weight-llm-review/) · [Mistral Small 4](/reviews/mistral-small-4-119b-moe-reasoning-vision-coding-llm-review/)*

