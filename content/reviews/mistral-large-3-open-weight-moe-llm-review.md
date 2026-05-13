---
title: "Mistral Large 3 — 675B MoE, Apache 2.0, and the Value Play for Enterprise"
date: 2026-05-13T15:00:00+09:00
description: "Mistral Large 3 (December 2, 2025) is Mistral AI's frontier open-weight release: 675B total parameters, 41B active per token via sparse MoE, Apache 2.0 license, 256K context, image understanding, and pricing at $0.50/$1.50 per million tokens — roughly 6x cheaper than Claude Sonnet. MMLU ~85.5%. HumanEval ~92%. Available on La Plateforme, AWS Bedrock, Azure, Ollama, Hugging Face. Not a reasoning model at launch. Rating: 3.5/5."
og_description: "Mistral Large 3 (Dec 2, 2025): 675B MoE / 41B active, Apache 2.0, 256K context, image input, $0.50/$1.50 per million tokens. MMLU ~85.5%, HumanEval ~92%, GPQA Diamond ~44%. Best-in-class multilingual (40+ languages). 6x cheaper than Claude Sonnet. Not a reasoning model. Rating: 3.5/5."
card_description: "Mistral Large 3 (December 2, 2025) is Mistral AI's flagship open-weight frontier model: 675B total parameters, 41B active per token (sparse MoE), 256K context window, image understanding, and a full Apache 2.0 license. Priced at $0.50/$1.50 per million tokens on La Plateforme — approximately 6x cheaper than Claude Sonnet 4.5. MMLU ~85.5%, HumanEval ~92%, GPQA Diamond ~43.9%. Best-in-class multilingual support across 40+ languages. Available on Mistral La Plateforme, Amazon Bedrock, Azure AI Foundry, IBM WatsonX, Hugging Face, OpenRouter, Ollama. No chain-of-thought reasoning at launch; a reasoning variant was listed as coming soon. Strong for enterprise multilingual, structured output, and cost-sensitive API workloads. Weaker on expert scientific QA and multi-step reasoning compared to frontier reasoning models. Rating: 3.5/5."
tags: ["llm", "open-weight", "mistral", "moe", "enterprise", "multilingual", "long-context", "apache-license", "structured-output", "function-calling"]
categories: ["reviews"]
rating: 3.5
author: "ChatForest"
last_refreshed: 2026-05-13
---

**At a glance:** Mistral Large 3, released December 2, 2025. 675B total parameters, 41B active per token (sparse MoE). Apache 2.0. 256K context. Image input. $0.50/$1.50 per million tokens. MMLU ~85.5%. HumanEval ~92%. GPQA Diamond ~43.9%. 40+ languages. No chain-of-thought reasoning at launch. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

"The best open-weight model that won't bankrupt your API budget."

That is, roughly, how developers characterized Mistral Large 3 in the weeks after its December 2, 2025 launch. At $0.50 per million input tokens — approximately six times cheaper than Claude Sonnet and far below GPT-4o — Mistral AI made a deliberate choice to compete on value over raw leaderboard position.

The model itself is substantial: 675 billion total parameters organized in a sparse Mixture-of-Experts architecture, active at only 41 billion parameters per token during inference. A 256K context window that swallows most enterprise codebases. A genuine Apache 2.0 license with no Mistral-specific use restrictions. Multimodal image input. And 40+ language support that community reviewers and enterprise users consistently rate as the best available outside English-first closed models.

The caveats are real too. Mistral Large 3 is not a reasoning model. At launch, no chain-of-thought or extended thinking variant existed. The GPQA Diamond score (~43.9%) reflects this gap plainly: expert-level scientific questions require something beyond what a base instruct model provides. A reasoning variant was announced as coming soon in December 2025. Whether it arrived and what it offered is a separate story.

What Mistral Large 3 *is* good at — enterprise multilingual pipelines, structured output, function calling, cost-sensitive high-volume inference, large-context RAG — it is genuinely strong at. This review covers where those strengths land, where they don't, and how to think about placing it in a production stack.

Companion to our **[Mistral AI review](/reviews/mistral-ai-le-chat-frontier-llm-company-review/)**, which covers the broader company and product landscape.

---

## Background: Mistral's December 2025 Release

Mistral AI has followed a consistent cadence since its 2023 founding: release capable open-weight models, price them aggressively, and let developers decide whether the frontier closed-source alternative is worth 5–10x the cost.

Mistral Large 3 fits this pattern. It launched December 2, 2025, alongside the **Ministral family** (3B, 8B, and 14B dense models oriented toward edge and embedded deployment), branded together as the "Mistral 3" release. NVIDIA announced a partnership on the same day, shipping a co-developed NVFP4 quantized variant optimized for Blackwell-generation GPU inference. Amazon Web Services and IBM announced same-day availability on Bedrock and WatsonX respectively — a more coordinated launch than Mistral's earlier releases.

The release positioning was explicit: "frontier-class open-weight capability at enterprise price-per-token." Mistral has a history of delivering on this framing at the mid-tier (Mistral 7B, Mixtral 8x7B), and Large 3 was the attempt to do it at genuine frontier scale.

---

## Architecture: Granular MoE at 675B Total Parameters

Mistral Large 3 is a sparse Mixture-of-Experts (MoE) model. The architecture is described in Mistral's documentation as "granular MoE" — a routing design where each forward pass activates approximately 41 billion of the model's 675 billion total parameters.

**The practical inference math**: per-token compute runs at roughly 41B-parameter scale. For API inference, this is transparent — Mistral's pricing reflects the active parameter cost, not the total model size. For self-hosting, the full 675B must reside in memory (multi-GPU data-center hardware required; consumer self-hosting is not practical), but the FLOPs per token are proportional to 41B.

Additional architecture details:

- **Context window**: 256,000 tokens — large enough to ingest entire codebases or lengthy legal/scientific documents in a single call
- **Modality**: text + image; function calling and structured output support baked into the instruction-tuned variant
- **Fill-in-the-middle (FIM)**: code completion and editing without a full-context rewrite
- **Structured output / prefix completion**: strongly supported — a documented community strength
- **Speculative decoding**: an "Eagle" variant on HuggingFace supports faster inference via speculative decoding
- **NVFP4 quantization**: the NVIDIA partnership variant enables efficient deployment on Blackwell-class hardware without significant quality degradation

HuggingFace model IDs: `mistralai/Mistral-Large-3-675B-Instruct-2512` (instruction-tuned), `mistralai/Mistral-Large-3-675B-Base-2512` (base).

**What this architecture is not**: Mistral Large 3 does not implement chain-of-thought reasoning, extended thinking, or a tree-search inference-time compute mechanism. It is an instruct model — intelligent, capable, and efficient at generation, but not a model that "thinks through" hard problems with deliberate multi-step internal reasoning. This distinction matters substantially for the benchmark interpretation below.

---

## Benchmarks: Strong Generalist, Not a Reasoning Specialist

Mistral Large 3's benchmark profile is consistent with a high-quality frontier instruct model without reasoning augmentation.

| Benchmark | Score | Context |
|---|---|---|
| MMLU | ~85.5% | Strong general knowledge; competitive with late-2025 frontier |
| MMLU-Pro | low 80s | Harder multi-step questions; expected slight drop |
| HumanEval (pass@1) | ~92% | Strong code generation from docstrings |
| LiveCodeBench | ~82.8 | Competitive for recent-release evaluation |
| MATH-500 | ~93.6% | Strong on structured mathematical calculation |
| GPQA Diamond | ~43.9% | **Below frontier** — reflects lack of reasoning mode |
| SWE-bench | ~79% (small sample) | Verify against larger evals before concluding |

**The GPQA Diamond number is the most important data point to understand**. Graduate-level expert scientific questions require sustained multi-step reasoning — exactly what Mistral Large 3 does not provide in its base instruct configuration. Gemini 3 Pro posts ~91.9% on GPQA Diamond. Claude Opus 4.7 posts 94.2%. The ~44% from Mistral Large 3 is not a failure of knowledge; it is an architectural consequence of not having chain-of-thought reasoning at all. Models with thinking modes score roughly 2–2.5x higher on this benchmark.

**The MATH-500 result (~93.6%) looks inconsistent** with a 43.9% GPQA Diamond score, but the benchmarks test different things: MATH-500 rewards structured calculation (where instruct models can perform well with the right prompting), while GPQA Diamond rewards genuine scientific insight across disciplines where domain reasoning matters more than computation.

**SWE-bench caveat**: A community report of ~79% (38/48 tasks) is based on a small eval set. The metric is useful directionally but should not be compared directly to official SWE-bench Verified numbers from models evaluated on the full dataset. By early 2026, Mistral Large 3 was no longer competitive at the SWE-bench frontier.

**What the numbers suggest overall**: Mistral Large 3 is a strong generalist model and a genuinely capable coder. It is not a specialist reasoning model, and should not be evaluated as if it were one. For the use cases it targets — multilingual pipelines, RAG, structured output, function calling, large-context summarization — these benchmarks are adequate. For tasks requiring extended reasoning, look elsewhere or wait for the reasoning variant.

---

## Multilingual: 40+ Languages, a Genuine Differentiator

Multilingual capability is one of Mistral Large 3's clearest advantages over the field.

The model supports 40+ languages, with documented strength in English, French, Spanish, German, Italian, Portuguese, Dutch, Chinese, Japanese, Korean, and Arabic. Multiple enterprise reviews describe its non-English instruction following as best-in-class for an open-weight model, and competitive with or superior to closed-source alternatives (including GPT-4o) for European languages in particular.

This reflects Mistral AI's French origin and European enterprise focus. Mistral has historically invested in multilingual training data depth that American-headquartered labs have deprioritized. For companies with significant non-English user bases — European e-commerce, LATAM finance, APAC enterprise — this is a material capability difference that raw English-language benchmark comparisons obscure.

---

## Pricing and Availability

**Mistral La Plateforme pricing** (as of December 2025):
- Input: $0.50 per million tokens
- Output: $1.50 per million tokens
- Free trial tier available (rate-limited)

For context:
- Claude Sonnet 4.5: ~$3.00/$15.00 per million tokens (~6x more expensive on input)
- GPT-4o: higher than Mistral Large 3 at comparable quality tier
- DeepSeek V3 API: competitive (though China-domiciled, raising enterprise compliance questions for some use cases)

**Available on at launch**:
- Mistral La Plateforme (primary API)
- Amazon Bedrock
- Azure AI Foundry
- IBM WatsonX
- Hugging Face (open weights)
- OpenRouter
- Fireworks AI
- Together AI
- Modal
- DigitalOcean
- Unsloth AI (for fine-tuning)
- Ollama (`ollama run mistral-large-3` — requires data-center-class hardware for the full 675B)

The breadth of availability at launch was notable. Amazon Bedrock and IBM WatsonX on day one signals enterprise readiness and Mistral's deliberate targeting of the cloud enterprise segment, not just developer-API consumers.

The Apache 2.0 license also matters for enterprise procurement. Unlike Llama models (Meta Community License) or models with Mistral's older Mistral License terms, Apache 2.0 permits unrestricted commercial use, redistribution, and derivative works. Legal and compliance teams at regulated enterprises (finance, healthcare, government) can clear Apache 2.0 models faster than custom licenses.

---

## What It Excels At

**Multilingual enterprise content**: 40+ languages, best-in-class non-English instruction following. Significant advantage for companies serving European, LATAM, and APAC markets.

**Structured output and JSON generation**: Community feedback consistently notes that Mistral Large 3 produces reliable, well-formed structured output and adheres to JSON schemas even in complex nested scenarios. Developers in the Hacker News thread describe it outperforming "smarter" models (which score higher on benchmarks but fail in structured output adherence pipelines).

**Function calling and multi-tool agentic workflows**: Strong support for multi-function calling, parallel tool use, and stateful agent architectures. The 256K context is useful for maintaining large tool-use histories.

**Large-context RAG**: Legal documents, technical manuals, scientific papers, codebases — 256K tokens is enough to ingest most single-domain document sets without chunking. This reduces retrieval engineering overhead in RAG pipelines.

**Cost-sensitive high-volume inference**: At $0.50/million input tokens, Mistral Large 3 enables workloads that would be economically unviable at Claude or GPT-4o pricing. High-volume document processing, content classification, multilingual summarization at scale.

**Privacy-sensitive on-premise deployment**: Apache 2.0 open weights mean the model can be deployed behind enterprise firewalls with no data leaving the organization. For healthcare, finance, and government, this is often non-negotiable.

**Code generation from context**: HumanEval ~92% and FIM support make it a credible primary coding assistant for most development workflows that don't require deep agentic repo traversal.

---

## What It Doesn't Do Well

**Expert scientific reasoning**: GPQA Diamond ~43.9% is the bluntest indicator. If your application requires solving graduate-level physics, chemistry, or biology problems with reliable accuracy, Mistral Large 3 is not the right tool. Use a model with chain-of-thought reasoning (Gemini 3.1 Pro, Claude Opus 4.7, o3) for these workloads.

**Competitive programming and SWE-bench frontier**: By early 2026, Mistral Large 3 had been surpassed on SWE-bench by multiple specialized models. It is a capable general coder, not a frontier agentic developer.

**Extended multi-step reasoning**: Tasks that require planning 10+ steps ahead, exploring multiple solution paths, or maintaining a long internal reasoning trace are better handled by models with dedicated reasoning infrastructure. Hacker News community reactions specifically called out "unimpressive" multi-step reasoning in real-world evaluations.

**Self-hosting at consumer scale**: 675B total parameters requires multi-GPU data-center infrastructure. Unlike smaller Mistral models (7B, 8x7B, 24B), the full Mistral Large 3 is not practically self-hostable on consumer hardware. Quantized variants (NVFP4) reduce memory requirements significantly but still require enterprise-grade hardware.

**Hallucination rates**: Acknowledged in community evaluations as a known weakness. Like all current LLMs, Mistral Large 3 can confidently produce incorrect information; hybrid retrieval or fact-checking pipelines are recommended for factuality-critical applications.

---

## Community Reception

The Hacker News thread (item 46121889) at launch showed a split reaction characteristic of Mistral releases: strong positive from enterprise developers who value reliability and cost, skeptical from benchmark-focused users who compared it unfavorably to frontier reasoning models.

The dominant developer thread was about **reliability vs. raw intelligence** — multiple developers explicitly noted that Mistral Large 3 outperformed more capable benchmark models for strict production requirements like JSON compliance, rate stability, and multi-language consistency. This is a recurring Mistral theme: their models often over-perform their benchmark scores in production structured-output workloads.

A Substack analysis ("Mistral Large 3: Not a Reasoning Model" by Benjamin Marie on the Kaitchup newsletter) attracted attention for directly naming the gap: without chain-of-thought reasoning, Mistral Large 3 lags smaller specialized models on math and science. The critique was well-reasoned and accurate; it was also somewhat beside the point for the enterprise multilingual/pipeline use case Mistral is explicitly targeting.

Early Reddit reactions included some "dead on arrival vs. DeepSeek V3" commentary — widely dismissed as premature. Technical reviewers noted architectural similarities between Mistral Large 3 and DeepSeek V3 (granular MoE convergence) as a sign of open-weight best-practice cross-pollination rather than competitive displacement.

---

## Rating: 3.5 / 5

Mistral Large 3 is a well-executed model for a clearly defined niche: Apache-licensed, enterprise-grade, multilingual, cost-efficient inference at frontier parameter scale.

The 675B MoE / 41B active design is architecturally sensible. The 256K context, strong function calling, and structured output reliability are production-grade. Apache 2.0 is the right license choice for enterprise adoption. And at $0.50 per million tokens, the economics are genuinely compelling for high-volume workloads where frontier-tier pricing is prohibitive.

What holds it at 3.5 rather than 4 is the missing reasoning layer. A GPQA Diamond of ~43.9% is a significant gap when competing models at the frontier post 85–94% via extended thinking. The lack of a chain-of-thought or reasoning variant at launch left a visible hole in the capability profile that Mistral acknowledged but didn't fill on day one. By the time this review was written (May 2026), the competitive landscape had moved substantially; early-2026 models have set new benchmarks on SWE-bench and agentic coding that leave Mistral Large 3 squarely in the second tier for those tasks.

For enterprise teams prioritizing multilingual coverage, structured output consistency, cost efficiency, and open-weight licensing over frontier reasoning performance, Mistral Large 3 is a strong fit. For teams needing the best reasoning, the best agentic coding, or the best scientific QA — this is not the model.

**Rating: 3.5/5**

---

## Quick Reference

| Attribute | Value |
|---|---|
| Release date | December 2, 2025 |
| Developer | Mistral AI |
| Architecture | Sparse MoE (granular) |
| Total parameters | 675B |
| Active parameters per token | 41B |
| Context window | 256K tokens |
| Modality | Text + image |
| License | Apache 2.0 |
| Input price | $0.50 / million tokens |
| Output price | $1.50 / million tokens |
| MMLU | ~85.5% |
| HumanEval | ~92% |
| GPQA Diamond | ~43.9% |
| Reasoning mode | None at launch |
| Languages | 40+ |
| Ollama | `ollama run mistral-large-3` (datacenter GPU required) |

---

**Update:** Mistral AI released [Mistral Medium 3.5](/reviews/mistral-medium-3-5-dense-128b-agentic-llm-review/) on April 29, 2026 — a 128B dense model that unifies instruction-following, reasoning, and coding in a single endpoint, superseding Devstral 2 as the Vibe CLI backend. Large 3 remains the better choice for cost-sensitive multilingual API workloads; Medium 3.5 targets long-horizon agentic coding at significantly higher pricing.

---

*Review written May 13, 2026. Benchmarks and pricing reflect information available at time of writing. Verify current pricing on [Mistral La Plateforme](https://mistral.ai). All benchmark figures sourced from community evaluations; treat with appropriate skepticism for production decisions.*
