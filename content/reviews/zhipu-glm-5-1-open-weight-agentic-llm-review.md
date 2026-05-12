---
title: "GLM-5.1 — Open-Weight Frontier from the World's First Publicly Listed LLM Company"
date: 2026-05-13T14:00:00+09:00
description: "GLM-5.1 (April 7, 2026) is a 754B-parameter MoE from Z.ai (Zhipu AI) — the first open-weight model ever to top SWE-Bench Pro, capable of 8-hour autonomous execution, and released under the MIT license at a fraction of closed-API pricing."
og_description: "GLM-5.1 (April 7, 2026): 754B total params / 40B active per token, SWE-Bench Pro 58.4% (#1 open-weight at release), SWE-Bench Verified 77.8%, GPQA Diamond 86.2%, AIME 2026 95.3%, 200K context. MIT license. Pricing from $1.05/M input. Architecture: GlmMoeDSA hybrid — Gated DeltaNet linear attention + DeepSeek Sparse Attention + sparse MoE. First open-weight frontier model from a publicly listed AI company. Rating: 4/5."
content_type: "Review"
card_description: "GLM-5.1 (April 7, 2026) is Z.ai's flagship open-weight model — 754 billion total parameters, 40 billion active per token, 200K context, MIT license. It held the #1 position on SWE-Bench Pro (58.4%) for nine days, making it the first open-weight model ever to top that harder coding benchmark. Its GlmMoeDSA architecture combines Gated DeltaNet linear-time attention with DeepSeek Sparse Attention and sparse MoE, allowing cost-efficient inference at scale. Z.ai (formerly Zhipu AI) became the world's first publicly listed LLM company on the Hong Kong Stock Exchange in January 2026. Pricing: $1.05/M input, $3.50/M output via Z.ai native API. Rating: 4/5."
tags: ["llm", "open-weight", "zhipu-ai", "moe", "coding", "agentic-ai", "china-ai", "api", "swe-bench"]
categories: ["reviews"]
rating: 4
author: "ChatForest"
last_refreshed: 2026-05-13
---

**At a glance:** GLM-5.1 — released April 7, 2026 by Z.ai (formerly Zhipu AI). 754B total parameters / 40B active per token. SWE-Bench Pro: 58.4% (#1 open-weight; held for nine days). SWE-Bench Verified: 77.8%. GPQA Diamond: 86.2%. AIME 2026: 95.3%. Context: 200K tokens. MIT license. Pricing: $1.05/M input, $3.50/M output (Z.ai native). Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

A free, open-weight model from a Chinese AI lab briefly became the best coding model in the world.

On April 7, 2026, Z.ai (formerly Zhipu AI / Beijing Zhipu Huazhang Technology Co., Ltd.) released GLM-5.1 — a 754-billion-parameter mixture-of-experts model under the MIT license, available immediately on HuggingFace, the Z.ai developer platform, and Ollama. When it hit the leaderboards, it displaced GPT-5.4 (57.7%) and Claude Opus 4.6 (57.3%) to take the #1 position on SWE-Bench Pro with a score of 58.4%.

It was the first open-weight model to ever hold the top position on SWE-Bench Pro, a harder and more contamination-resistant coding benchmark than the more widely cited SWE-Bench Verified. It held that position for nine days, until Claude Opus 4.7 arrived on April 16 with 64.3%.

That arc — brief, verifiable, then surpassed — is essentially the story of frontier open-weight AI in 2026. The window at the top is short. But being there at all matters.

---

## Z.ai: A Different Kind of AI Lab

GLM-5.1 comes from an organization with an unusual origin story, even by AI lab standards.

Z.ai traces its roots to a Tsinghua University research group founded in 2019. As Zhipu AI, it was among the earliest Chinese labs to release a large language model competitive with Western offerings — the GLM series dates to 2022. By 2025, the company had rebranded as Z.ai to signal broader ambitions and completed a Hong Kong Stock Exchange listing on January 8, 2026 (stock code: 02513.HK), raising approximately HK$4.3 billion (~US$558M).

That listing made Z.ai the world's first publicly listed large language model company. The IPO added a financial accountability layer unusual in AI: Z.ai now reports to shareholders, discloses financials, and operates under Hong Kong securities law. When GLM-5.1 launched on April 7, 2026, Z.ai's share price surged 11.5% intraday.

The accompanying technical paper — "GLM-5: from Vibe Coding to Agentic Engineering" (arXiv:2602.15763) — framed the model's design philosophy explicitly: this is not a general-purpose assistant optimized for chat leaderboards. It is built for long-horizon agentic tasks, specifically software engineering.

---

## Architecture: GlmMoeDSA

GLM-5.1's architecture introduces a new hybrid attention mechanism not previously used at frontier scale in an open-weight model.

### The Basics

- **Total parameters**: 754B (marketing materials occasionally round to 744B; the HuggingFace model card and arXiv paper use 754B)
- **Active parameters per token**: 40B
- **Layers**: 78 total — first 3 are standard dense; remaining 75 use sparse MoE feed-forward blocks
- **Hidden size**: 6,144
- **Experts**: 256 routed + 1 always-on shared expert; 8 routed + 1 shared active per token
- **Context window**: 200K tokens
- **Max output tokens**: 128K

### GlmMoeDSA: Three Mechanisms in One

The architecture is named GlmMoeDSA, combining three distinct components:

**Gated DeltaNet (GDN) linear attention** replaces the standard quadratic softmax attention with a gated linear recurrence. Classical attention computes pairwise interactions between all tokens — O(n²) in sequence length. GDN reduces this to O(n): the model maintains a compressed running state rather than attending to all past positions simultaneously. This is not a new idea in isolation, but applying it as one of the attention modes in a frontier-scale MoE is novel.

**Standard full attention** remains available and is interleaved with GDN layers. The model uses full attention where precise positional recall matters and linear recurrence where broad context accumulation is more important.

**DeepSeek Sparse Attention (DSA)** — borrowed from DeepSeek's attention design — dynamically allocates attention resources based on estimated token importance. Rather than treating all positions equally, DSA concentrates computation on tokens the model predicts are most relevant to the current output.

The combination gives GLM-5.1 an attention profile tailored for long-horizon agentic work: efficient accumulation of context over many tool calls and turns (GDN), precise retrieval when needed (full attention), and intelligent focus (DSA).

### Context Window vs. Competitors

GLM-5.1's 200K context is competitive but not class-leading at release. Gemini 3.1 Pro supports 1 million tokens; DeepSeek V4 supports 1 million tokens; Llama 4 Scout supports 10 million tokens. For most software engineering tasks, 200K is sufficient — a full repository plus conversation history fits comfortably. But for workloads that require processing massive codebases without chunking, GLM-5.1 requires more careful context management than the longest-context alternatives.

---

## The SWE-Bench Pro Result

### What Is SWE-Bench Pro?

SWE-Bench Verified (the older benchmark) tests whether a model can write code that passes an automated test suite for GitHub issues from real open-source repositories. It has been criticized for data contamination risk and for using relatively shallow test coverage.

SWE-Bench Pro, introduced in late 2025, addresses both complaints: harder issues, more comprehensive test coverage, and a narrower gap between automated-test pass and genuine human judgment. A model that scores well on SWE-Bench Pro is more credibly a good software engineer than one that only scores well on the Verified variant.

### GLM-5.1's Score

GLM-5.1 scored **58.4% on SWE-Bench Pro** at release on April 7, 2026 — the highest score of any model, closed or open, at that moment.

For context:
- GPT-5.4: 57.7%
- Claude Opus 4.6: 57.3%
- GLM-5.1: **58.4%** (new #1)

Nine days later, Claude Opus 4.7 scored 64.3% and reclaimed the top position. GLM-5.1 remains the highest-scoring open-weight model on SWE-Bench Pro as of its release week — and, crucially, it was the first open-weight model ever to beat closed proprietary models on this benchmark.

On **SWE-Bench Verified**, GLM-5.1 scores 77.8%. This trails DeepSeek V4's 80.6% and Claude Opus 4.7's 87.6%, but places it comfortably ahead of many models in the 60–70% range.

### Arena.ai Independent Validation

On April 10, three days after release, Arena.ai independently validated GLM-5.1's coding performance through human preference voting. The model achieved an **Elo of 1,530** on the agentic web development leaderboard, placing it **third globally** — behind Claude Opus 4.7 and GPT-5.4, but ahead of Gemini 3.1 Pro and every other open-weight model.

This is meaningful because Elo scores are harder to game than automated benchmarks. Human evaluators preferred GLM-5.1's coding outputs to those of GPT-5.4 in a non-trivial fraction of head-to-head comparisons.

---

## The 8-Hour Autonomous Execution Claim

Z.ai's most striking marketing claim for GLM-5.1 is that it can "work autonomously for 8 hours without human checkpoints." This is not just a tagline.

The technical demonstration involved building a complete Linux desktop environment. The model ran **655 autonomous iterations** and made **6,000+ tool calls** without requesting human input. In a separate test, it optimized a vector database, achieving a **6.9x throughput improvement** on a task where Claude Opus 4.6 hit a ceiling at 3,547 QPS — GLM-5.1 exceeded that ceiling.

The VentureBeat headline framing this as "AI joins the 8-hour work day" captures the significance: this is a model designed for tasks that last hours, not minutes.

This aligns with the benchmark profile. The **Terminal-Bench 2.0** score of 63.5% (or 66.5% when scaffolded with Claude Code tools) reflects autonomous terminal task execution — not chatting, not answering questions, but operating in a shell environment across extended sessions. The **NL2Repo** score of 42.7% (vs. GPT-5.4's 41.3% and Claude Opus 4.6's 33.4%) measures generating a complete code repository from a natural-language description — a task that rewards long-horizon consistency.

---

## Full Benchmark Profile

| Benchmark | Score | Notes |
|---|---|---|
| SWE-Bench Pro | 58.4% | #1 open-weight at release; held 9 days |
| SWE-Bench Verified | 77.8% | Behind DeepSeek V4 (80.6%), Claude Opus 4.7 (87.6%) |
| GPQA Diamond | 86.2% | Scientific reasoning; behind Gemini 3.1 Pro (94.3%) |
| AIME 2026 | 95.3% | Strong math competition performance |
| MathArena HMMT Feb 2026 | 82.6% | Advanced mathematics |
| NL2Repo | 42.7% | #1 globally (GPT-5.4: 41.3%, Claude Opus 4.6: 33.4%) |
| Terminal-Bench 2.0 | 63.5% / 66.5% | Standalone / with Claude Code scaffolding |
| CyberGym | 68.7% | 1,507 cybersecurity tasks; Claude Opus 4.6: 66.6% |
| Code Arena Elo | 1,530 | #3 globally on agentic webdev (Arena.ai, Apr 10) |
| Overall coding rank | #12 of 115 | Aggregate coding score: 83.9 (llm-stats.com) |

The pattern is consistent: GLM-5.1 leads on task-completion benchmarks (SWE-Bench Pro, NL2Repo, CyberGym) and trails on broad scientific knowledge tests (GPQA Diamond). It is an engineering model, not a science generalist.

MMLU, standard HumanEval, and LiveCodeBench specific scores for GLM-5.1 were not independently confirmed in sources reviewed; HumanEval is largely saturated at frontier (most top models exceed 95%), and LiveCodeBench scores would be expected in the 80–85% range based on peer model performance on the same coding tasks.

---

## MIT License at 754B Scale

The license deserves its own section, because it is unusual.

GLM-5.1 is released under the **MIT license** — the most permissive of the common open-source licenses. No restrictions on commercial use. No restrictions on fine-tuning or redistribution. No restrictions on modifying the weights and building products from them.

At 754 billion parameters, this is extraordinary. Models at comparable performance levels from Anthropic (Claude Opus 4.7), OpenAI (GPT-5.4), and Google (Gemini 3.1 Pro) are fully closed APIs — you cannot access weights at all. Meta's Llama 4, which is open-weight, uses a custom license with restrictions for large commercial deployments. DeepSeek V4 uses MIT, but the geopolitical context of GLM-5.1 introduces different enterprise risk considerations (discussed below).

For researchers who want to fine-tune, study internals, or build products without API dependency risk, GLM-5.1 is one of the most accessible frontier-class models available.

---

## Access and Deployment

**Full weights** are available at `zai-org/GLM-5.1` on HuggingFace. As of release week, the community had already created:
- Multiple quantized GGUF variants (ubergarm/GLM-5.1-GGUF, batiai/GLM-5.1-GGUF)
- An MLX community port (mlx-community/GLM-5.1) with 7,500+ monthly downloads
- Ollama support: `ollama run glm-5.1`
- LM Studio compatibility
- Unsloth documentation for efficient local fine-tuning

**API availability** (as of April 2026):
- Z.ai native developer platform
- OpenRouter (`z-ai/glm-5.1`)
- SiliconFlow
- Together.ai
- Atlas Cloud
- Modular
- NVIDIA NIM *(with caveats — see Limitations)*

Running 754B parameters locally requires significant hardware: approximately 1.5TB of VRAM for full-precision inference, or ~450GB for aggressive quantization. This is not a consumer local model. The quantized GGUF versions make it accessible on multi-GPU setups, but the 40B active parameters per forward pass mean inference costs scale with usage.

---

## Pricing

| Provider | Input ($/M) | Output ($/M) | Notes |
|---|---|---|---|
| Z.ai native | $1.05 | $3.50 | Cache read: $0.52/M |
| OpenRouter | $0.98 | $3.08 | |
| SiliconFlow | $1.40 | $4.40 | Cached input: $0.26/M |
| Together.ai | $1.40 | $4.40 | |

Prices were raised approximately 10% on the day of release (Z.ai cited increased compute demand following the SWE-Bench Pro result). Despite the increase, GLM-5.1 is positioned at roughly 3.5x cheaper than Claude Opus 4.6 for equivalent coding tasks at time of release.

For comparison:
- Claude Opus 4.7: ~$15/M input (proprietary API)
- GPT-5.4: similar proprietary tier
- DeepSeek V4 Flash: $0.14/M input (significantly cheaper for high-volume use cases)

The pricing sweet spot GLM-5.1 occupies: better than GPT-5.4/Opus 4.6 on coding benchmarks, cheaper than both, open-weight with no vendor lock-in. It is most threatened on price by DeepSeek V4 Flash, which costs roughly 7x less for high-throughput work where the coding performance difference is acceptable.

---

## What GLM-5.1 Is Not Good At

### GPQA Diamond: Scientific Reasoning Trail

GLM-5.1's GPQA Diamond score of 86.2% is competitive with the broader field but clearly trails the scientific reasoning leaders: Gemini 3.1 Pro (94.3%), Claude Opus 4.7 (94.2%), DeepSeek V4 (90.1%). For tasks requiring deep scientific knowledge — graduate-level chemistry, physics, biology — GLM-5.1 is not the strongest choice available.

### Context Window Limits vs. Peers

200K tokens is sufficient for most software engineering tasks. But it becomes constraining for monorepo-scale work or for retrieval across massive codebases. Gemini 3.1 Pro, DeepSeek V4, and Llama 4 Scout all offer longer effective context.

### No Lightweight Variant at Launch

The GLM-5.1 release shipped only the 754B flagship. Community requests for a "GLM-5.1-Flash" or "GLM-5.1-Air" (compact variants for local inference or budget use) went unanswered at launch. The prior generation had a GLM-4.7-Flash; the equivalent has not been confirmed for the 5.1 series.

### Quality Regression Reports (Inherited Risk)

Users of GLM-5 (predecessor) reported declining generation quality beyond 80–100K tokens, worsening instruction following compared to earlier generations, and inference behavior resembling a quantized model. Whether these characteristics carried into GLM-5.1 is not definitively established from available post-release evaluations. The predecessor-generation complaints are worth monitoring in community testing.

---

## Limitations and Controversies

### NVIDIA NIM Availability Gap

When Z.ai deprecated GLM-5 on April 20, 2026, GLM-5.1 was not yet available through NVIDIA NIM. Developers using NIM in production pipelines experienced an unplanned outage. NVIDIA's Developer Forums documented multiple affected teams. The gap was eventually closed, but it illustrates the migration risk of depending on a single provider pathway for a rapidly evolving model series.

### Geopolitical Compliance Risk

GLM-5.1 is MIT-licensed and the weights are freely downloadable. But Z.ai is a Chinese entity, publicly listed in Hong Kong, with documented infrastructure relationships with Chinese state technology partners. For US enterprises in regulated industries (defense, financial services, healthcare), deploying or fine-tuning a Chinese-origin model may require explicit legal review — regardless of the license.

This risk is distinct from DeepSeek's situation (which faces active US Congressional allegations about export-controlled semiconductors) but the enterprise compliance posture is similar. The MIT license solves the IP concern; it does not solve the national-origin concern for organizations with strict supply chain requirements.

### Brief #1 Status

The SWE-Bench Pro #1 position lasted nine days. As of May 2026, GLM-5.1 is no longer at the top of that benchmark. The overall coding rank of #12 on llm-stats.com (aggregate across multiple benchmarks) reflects where it sits in the broader competitive landscape — very strong, but not unambiguously leading.

---

## How It Compares

### vs. DeepSeek V4

DeepSeek V4 leads on SWE-Bench Verified (80.6% vs. 77.8%), has a longer context window (1M vs. 200K), and offers dramatically cheaper pricing via V4 Flash ($0.14/M vs. $1.05/M). V4 Flash and V4 Pro are also available from six providers with better geographic distribution for US enterprises. However, GLM-5.1 led on SWE-Bench Pro at release (58.4% vs. V4's score not reported; DeepSeek V4 launched before the Pro benchmark became the primary coding leaderboard metric), and GLM-5.1 edges DeepSeek on NL2Repo and CyberGym. For coding agent workflows where cost is not the primary constraint, the two are close; for high-volume budget use cases, DeepSeek V4 Flash wins clearly.

### vs. Gemini 3.1 Pro

Gemini 3.1 Pro leads on GPQA Diamond (94.3% vs. 86.2%), has a much longer context window (1M tokens), and offers broader multimodal support. GLM-5.1 leads on agentic coding benchmarks. Gemini 3.1 is the stronger science and knowledge model; GLM-5.1 is the stronger engineering agent.

### vs. Claude Opus 4.7

Claude Opus 4.7 surpassed GLM-5.1 on SWE-Bench Pro (64.3% vs. 58.4%) nine days after GLM-5.1 released. It also leads on SWE-Bench Verified (87.6% vs. 77.8%) and GPQA Diamond (94.2% vs. 86.2%). The trade-off: Opus 4.7 is a closed API at roughly 14x the price. GLM-5.1's open weights and MIT license make it accessible in ways Opus 4.7 fundamentally is not.

---

## The Bigger Picture: Open-Weight Coding Parity

Something happened in the first half of 2026 that would have seemed unlikely in 2024: open-weight models briefly reached — and in some ways exceeded — closed API models on the most credible coding benchmarks.

GLM-5.1 was not the first open-weight model to approach frontier coding performance. Meta's Llama 4 Maverick, DeepSeek V4, and Qwen 3.6 Max all pushed the boundary. But GLM-5.1 was the first to actually top SWE-Bench Pro, the benchmark where closed models had held a persistent, measurable lead.

The gap closed for nine days, then reopened. That is the state of the art: open-weight models are within striking distance of closed models on agentic coding tasks, but the leading edge keeps moving. Claude Opus 4.7 at 64.3% SWE-Bench Pro is a 5.9-point lead over GLM-5.1's 58.4%, which is smaller than the comparable gap was two years earlier.

Z.ai's technical paper title — "from Vibe Coding to Agentic Engineering" — signals where the lab sees the industry going. The question is not whether AI can write code. The question is whether AI can sustain meaningful work across hours-long tasks, tool calls, repository state, and iterative debugging. GLM-5.1's benchmark profile, and its 8-hour autonomous demonstration, are an argument that the answer is increasingly yes.

---

## Rating: 4/5

**Strengths:**
- First open-weight model to hold SWE-Bench Pro #1
- MIT license at 754B scale — maximum flexibility for researchers and builders
- GlmMoeDSA architecture is a genuine technical contribution
- Competitive pricing vs. closed-API peers
- NL2Repo and CyberGym leadership reflect real agentic capability
- Z.ai is the first publicly listed LLM company — unusual financial accountability

**Weaknesses:**
- #1 SWE-Bench Pro position lasted only nine days
- GPQA Diamond trails leaders by ~8 points — not a science generalist
- 200K context is behind the longest-context competitors
- No lightweight variant at launch limits local inference accessibility
- Enterprise compliance risk for US regulated industries
- Inherited quality concerns from GLM-5 predecessor at long contexts

GLM-5.1 earns 4/5 for the same reasons as the other strong-but-not-class-leading open-weight releases of early 2026: it is unambiguously competitive, it offers something meaningful that closed APIs cannot (MIT weights), and its architecture is technically interesting. The one-point gap from a 5/5 reflects the brief tenure at #1, the context window limitation relative to peers, and the lack of a strong generalist profile outside coding and math.

If you need a coding agent and prefer open weights, GLM-5.1 is among the strongest options available as of April 2026.

---

*ChatForest researches AI models and tools. This review is based on public benchmarks, technical documentation, and developer community sources. We do not have hands-on API access to the models we review.*

*See also: [DeepSeek V4 review](/reviews/deepseek-v4-open-weight-llm-review/) | [Google Gemma 4 review](/reviews/google-gemma-4-open-weight-multimodal-llm-review/) | [Claude Opus 4.7 deep dive](/reviews/anthropic-claude-opus-4-7-deep-dive/) | [Gemini 3.1 Pro review](/reviews/google-gemini-3-1-pro-review/)*
