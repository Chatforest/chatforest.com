---
title: "Mistral Medium 3.5 Review: 128B Dense, 77.6% SWE-Bench, and a Three-Model Consolidation"
date: 2026-05-13T23:00:00+09:00
description: "Mistral Medium 3.5 (April 29, 2026) is Mistral AI's most capable open-weights model to date: 128B dense parameters, 256K context, multimodal, and adjustable reasoning built in. It replaces three prior Mistral models — Medium 3.1, Magistral, and Devstral 2 — with a single API endpoint. SWE-Bench Verified 77.6%. $1.50/$7.50 per million tokens. Modified MIT license with a $20M/month revenue cap. The consolidation is real. So is the price increase. Rating: 3.5/5."
og_description: "Mistral Medium 3.5 (April 29, 2026): 128B dense, 256K context, multimodal, adjustable reasoning. SWE-Bench Verified 77.6%. τ³-Telecom 91.4%. API at $1.50/$7.50 per M tokens — 3.75× more than Medium 3. Modified MIT license: $20M/month revenue cap. Replaces Medium 3.1 + Magistral + Devstral 2. Self-host requires ~256GB VRAM (BF16) or 4×H100. Rating: 3.5/5."
card_description: "Mistral Medium 3.5 (released April 29, 2026) is Mistral AI's new flagship open-weights model: 128B parameters, all active (dense architecture, not MoE), 256K context window, text and image input. Released simultaneously with Vibe remote agents and Le Chat Work Mode. Key claim: unifies instruction-following, reasoning (via adjustable reasoning_effort parameter), and agentic coding into a single model, replacing three prior Mistral products — Mistral Medium 3.1 (in Le Chat), Magistral (in Le Chat reasoning mode), and Devstral 2 (in the Vibe coding agent). SWE-Bench Verified: 77.6% (above Claude 4.5 Opus 76.8%). τ³-Telecom agentic benchmark: 91.4%. Artificial Analysis Intelligence Index: 39.23 (ranked ~#20 overall — well below Claude Opus 4.7 at 57.28 and Gemini 3.1 Pro at 57.18). API speed: 163.4 tokens/second. Available on Mistral La Plateforme and NVIDIA NIM. HuggingFace: mistralai/Mistral-Medium-3.5-128B. License: Modified MIT — companies with >$20M/month global revenue must obtain a commercial license from Mistral. Self-hosting: ~256GB VRAM at BF16 (4×H100 80GB or equivalent); quantized GGUFs available from Unsloth (~70GB at Q4). Early release included a YaRN long-context bug, patched ~May 1. Note: a smaller sibling, Mistral Small 4 (119B MoE, only 6B active parameters), was released March 16, 2026 under Apache 2.0 with no commercial restrictions. Rating: 3.5/5."
tags: ["llm", "open-weight", "mistral", "dense", "agentic-ai", "coding", "multimodal", "reasoning", "long-context", "swe-bench"]
categories: ["reviews"]
rating: 3
ratingHalf: true
author: "ChatForest"
last_refreshed: 2026-05-13
---

**At a glance:** Mistral Medium 3.5, released April 29, 2026. 128B dense parameters, all active. 256K context. Text + image input. Adjustable reasoning. SWE-Bench Verified: 77.6%. API at $1.50/$7.50 per million tokens. Modified MIT license. Self-hosting requires ~256GB VRAM. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

Mistral AI's most compelling argument for Mistral Medium 3.5 is not a benchmark — it's an org chart.

By April 2026, Mistral had accumulated three separate specialized models doing overlapping jobs: Mistral Medium 3.1 handled general conversations in Le Chat, Magistral handled Le Chat's reasoning mode, and Devstral 2 powered the Vibe coding agent. Developers building on Mistral's API had to pick the right model for the task. The Vibe CLI used one model under the hood, the reasoning toggle used another, and the standard chat endpoint used a third.

Mistral Medium 3.5 collapses all three into a single 128B dense model. One endpoint. One API call with a `reasoning_effort` parameter for on-demand thinking. One model that Mistral's own products now run on. For enterprise teams and developers who have found Mistral's lineup confusing, the consolidation alone is worth something.

Whether it's worth a 3.75× price increase over its predecessor — and a Modified MIT license that narrows who can freely use it — is a different question. This review works through both.

---

## Release Context

Mistral Medium 3.5 was announced on **April 29, 2026** in a blog post titled "Remote agents in Vibe. Powered by Mistral Medium 3.5." The release was bundled with two product announcements:

1. **Vibe Remote Agents** — the Vibe CLI coding agent now runs cloud-based sessions with parallel execution, GitHub integration, and the ability to continue work asynchronously
2. **Le Chat Work Mode** — a new agentic mode in Mistral's consumer chat product enabling cross-tool workflows across email, calendar, and documents

This release structure — model and product together — signals that Medium 3.5 is less a standalone model drop and more a platform capability upgrade. Mistral isn't just selling API access; they're building vertically integrated agentic products on top.

**Predecessor context:** Medium 3.5 formally supersedes three models:

| Model superseded | Role | License |
|---|---|---|
| Mistral Medium 3.1 (`mistral-medium-2508`) | Le Chat general conversation | Premier (closed) |
| Magistral | Le Chat reasoning mode | Commercial |
| Devstral 2 (123B) | Vibe CLI coding agent | Apache 2.0 |

The Devstral 2 supersession is the most noteworthy: Devstral 2 was Apache 2.0 with no commercial restrictions. Medium 3.5 is Modified MIT with a $20M/month revenue cap. Developers who chose Devstral 2 specifically for its license terms now have an upstream model that's less permissive. That's a strategic shift, not a coincidence.

**One month earlier:** Mistral Small 4 (119B MoE, 6B active, Apache 2.0) launched March 16, 2026. Understanding why Medium 3.5 and Small 4 coexist — despite similar parameter counts — requires looking at the architecture.

---

## Architecture

### Dense, Not MoE

The first thing to understand about Mistral Medium 3.5 is that it is a **dense model** — all 128 billion parameters are active during every inference call. This is a deliberate architectural choice in 2026, when the industry has broadly shifted toward Mixture-of-Experts (MoE) architectures that activate only a fraction of parameters per token to reduce inference cost.

Mistral's own Small 4, released just six weeks earlier, is a 119B MoE with only **6 billion active parameters** per token. DeepSeek V4 is 1.6 trillion total with **49 billion active**. Qwen 3.6 is a MoE family with efficient active-parameter-per-token profiles.

Medium 3.5 runs all 128 billion parameters on every token. This is not a mistake — it's a choice. Dense models tend to produce more consistent quality on sustained, long-context agentic tasks because all representations are always available. MoEs with expert routing can under-activate specialists on corner-case inputs. For a model intended to power long multi-step coding agents (Vibe) and extended chat sessions, the dense architecture has a defensible rationale.

But it also means inference is more expensive in hardware terms, and quantization introduces more quality tradeoff than in MoEs.

### Specifications

| Specification | Value |
|---|---|
| Total parameters | 128 billion |
| Active parameters per token | 128 billion (dense) |
| Context window | 256,000 tokens |
| Modalities | Text + image input, text output |
| Vision encoder | Purpose-built for variable image sizes/aspect ratios |
| Languages | 24 (including Chinese, Arabic, Japanese, Korean, Hindi) |
| Reasoning | Adjustable via `reasoning_effort` parameter |
| Architecture ID | `Mistral3ForConditionalGeneration` |
| Recommended inference | vLLM (tensor-parallel-size 8) / SGLang |

### Adjustable Reasoning

Medium 3.5's reasoning mechanism is worth explaining carefully, because it differs from dedicated reasoning models like Magistral or Qwen QwQ.

The API exposes a `reasoning_effort` parameter with two settings:

- **`reasoning_effort="none"` (default):** No extended thinking. Immediate responses. Temperature range 0.0–0.7. Behaves like a standard instruct model.
- **`reasoning_effort="high"`:** Extended thinking mode. Temperature 0.7, top_p 0.95. Output includes "a reasoning chunk with the model's thinking traces, followed by the final answer." Slower but more rigorous.

This is different from Claude Sonnet's "extended thinking" or Gemini's "Deep Think" in one key way: the model isn't a reasoning specialist with always-on chain-of-thought. It's a general model with a switchable reasoning mode. Whether that produces reasoning traces as deep as a dedicated reasoning model is not established by Mistral's published data.

The practical value is composability: an agentic coding system can call `reasoning_effort="none"` for fast tool calls and format operations, and `reasoning_effort="high"` for complex planning steps, within the same model and deployment.

### Multimodal Vision

The vision encoder is described as "trained from scratch to handle variable image sizes and aspect ratios." This is a meaningful architectural detail — many multimodal models bolt adapters onto vision transformers originally designed for fixed-size inputs. A purpose-built variable-resolution encoder typically handles documents, screenshots, and diagrams more gracefully than adapters do.

No specific vision benchmark data was published by Mistral at launch. The vision capability appears designed for practical use cases (code screenshots, UI design files, document understanding) rather than competitive leaderboard performance.

---

## Benchmarks

Mistral's benchmark reporting for Medium 3.5 is narrower than their prior major releases. The two explicitly highlighted scores:

### SWE-Bench Verified: 77.6%

This is Mistral's headline claim and their most defensible competitive number. SWE-Bench Verified tests real GitHub software engineering tasks — identifying and patching bugs in open-source Python repos — under independently verified conditions.

For context at release:

| Model | SWE-Bench Verified |
|---|---|
| Mistral Medium 3.5 | **77.6%** |
| Claude 4.5 Opus (high reasoning) | 76.8% |
| Gemini 3.1 Flash (high reasoning) | 75.8% |
| DeepSeek V4 Pro | 80.6% |
| Qwen 3.6 Max Preview | ~82% |

Medium 3.5 leads Claude 4.5 Opus by a narrow 0.8% on this specific benchmark, which is a legitimate achievement for an open-weights model. Notably, it arrives at this score **without** the dedicated reasoning-specialist architecture of most high-SWE-Bench models.

The important caveat: DeepSeek V4 Pro and Qwen 3.6 Max Preview both exceed 77.6% at competitive pricing — V4 Pro at $1.74/$3.48 per million tokens and Qwen 3.6 at significantly lower rates. Medium 3.5's $1.50/$7.50 output pricing makes direct SWE-Bench comparison more complex when cost-efficiency is a factor.

### τ³-Telecom: 91.4%

The τ³-Telecom benchmark tests sustained multi-tool agentic capability in telecom industry scenarios — a specialized evaluation designed to measure whether models can complete complex, multi-step workflows reliably. 91.4% is a strong score on this benchmark, but it's an industry-vertical evaluation, not a general agentic capability measure. The score is best interpreted as supporting evidence for Mistral's core claim: Medium 3.5 is optimized for long-horizon tool use.

### What's Missing

Mistral did not publish GPQA Diamond, MMLU, Math-500, AIME, LiveCodeBench, or HumanEval scores in their launch materials. This is unusual for a flagship model launch. The SWE-Bench and τ³-Telecom emphasis is clearly strategic — both benchmarks show the model well, but neither gives a complete picture of general reasoning or scientific capability.

Independent evaluation by Artificial Analysis provides the broader view:

| Model | AI Intelligence Index | Speed (t/s) |
|---|---|---|
| GPT-5.5 | 60.24 | — |
| Claude Opus 4.7 | 57.28 | — |
| Gemini 3.1 Pro | 57.18 | — |
| Qwen 3.6 Max Preview | 51.81 | — |
| **Mistral Medium 3.5** | **39.23** | **163.4** |

The 39.23 Intelligence Index places Medium 3.5 approximately **20th overall** in the Artificial Analysis ranking — well below the frontier tier where its SWE-Bench number might suggest it belongs. The Artificial Analysis index incorporates a broader evaluation suite (GPQA Diamond, HLE, SciCode, and others) that reveals the narrow benchmark selection in Mistral's announcement.

Speed is a genuine advantage: 163.4 tokens/second ranks 9th fastest among the 61 models in the evaluation. For latency-sensitive agentic applications, that's a meaningful differentiator against slower frontier models.

---

## Pricing

**Mistral API (La Plateforme):**
- Input: **$1.50 per million tokens**
- Output: **$7.50 per million tokens**

For comparison:

| Model | Input ($/M) | Output ($/M) |
|---|---|---|
| **Mistral Medium 3.5** | **$1.50** | **$7.50** |
| Mistral Medium 3 (predecessor) | $0.40 | $2.00 |
| GPT-4.1 (OpenAI) | $2.00 | $8.00 |
| Claude Opus 4.6 (Anthropic) | $15.00 | $75.00 |
| DeepSeek V4 Pro | $1.74 | $3.48 |
| Mistral Large 3 | $0.50 | $1.50 |

The predecessor comparison is the most striking: Medium 3 was $0.40/$2.00 per million. Medium 3.5 is **3.75× more expensive on input and 3.75× more expensive on output**. This is not incremental pricing drift — it's a deliberate repositioning.

Against GPT-4.1 ($2.00/$8.00), Medium 3.5 is priced competitively and slightly cheaper. Against DeepSeek V4 Pro ($1.74/$3.48), Medium 3.5's output pricing is more than double. The competitive pressure from DeepSeek is real in the mid-tier pricing band.

**Availability:** Mistral La Plateforme and NVIDIA NIM confirmed at launch. AWS Bedrock, Azure AI Foundry, and Google Cloud Vertex — where Medium 3 was available — not yet confirmed for Medium 3.5 as of May 13, 2026. These are likely to follow.

---

## License

Mistral Medium 3.5 is released under a **Modified MIT License** — not standard MIT, not Apache 2.0.

**The key restriction:**

> Companies with global consolidated monthly revenue exceeding **$20 million** are not authorized to use the model under this license. They must obtain a separate commercial license from Mistral AI (sales@mistral.ai) or use the model exclusively through Mistral's hosted API.

For individual developers and startups, the $20M/month threshold ($240M/year in annual revenue) is effectively unrestricting — the vast majority of developers will never approach it. For mid-to-large enterprises, procurement review is required.

**By OSI standards:** This is not open source. The Open Source Initiative requires licenses not to discriminate against groups based on business size or use case. A revenue cap fails that test. The correct framing is "open weights with commercial restrictions" — similar to Meta's Llama license terms. This is increasingly common in the frontier open-weights space, but it's worth being precise about.

**Historical comparison:**
- Devstral 2, which Medium 3.5 supersedes in Vibe: **Apache 2.0** (no commercial restrictions)
- Mistral Small 4, released one month earlier: **Apache 2.0** (no commercial restrictions)
- Mistral Large 3: **Apache 2.0** (no commercial restrictions)

The pattern suggests that Apache 2.0 licensing is reserved for smaller or older Mistral models, while the flagship Medium tier now carries a restricted license. This is a strategic shift: Mistral gains leverage to negotiate enterprise licenses with large companies that want to self-host the most capable models.

---

## Self-Hosting

Mistral's announcement says Medium 3.5 "runs self-hosted on as few as four GPUs." This is technically accurate and practically qualified.

**Memory requirements:**
- At BF16 (full precision): ~256GB VRAM — requires 4×H100 80GB SXM, 4×H200 80GB, or equivalent
- At Q4 quantization (~4 bits): ~70GB — achievable on a single high-memory card or multi-consumer GPU setup

**Recommended configuration (from HuggingFace README):**
```bash
vllm serve mistralai/Mistral-Medium-3.5-128B \
  --tensor-parallel-size 8 \
  --tool-call-parser mistral \
  --enable-auto-tool-choice \
  --reasoning-parser mistral \
  --max_num_batched_tokens 16384 \
  --max_num_seqs 128 \
  --gpu_memory_utilization 0.8
```

Note that `--tensor-parallel-size 8` is the **recommended** config — 8 GPUs, not 4. The "4 GPU" headline is technically achievable at reduced settings or with quantization, but 8 GPUs is what Mistral uses for production-quality inference.

**Community-tested configurations:**
- 2× RTX Pro 6000 Blackwell (96GB each, ~192GB total): ~30 tokens/second at BF16
- M3 Ultra Mac Studio (192GB unified, ~819 GB/s bandwidth): ~6 tokens/second at Q4 — functional but slow for interactive coding
- Consumer multi-GPU setups with Q4 quantization: 3–7 tokens/second typical

For context: interactive coding agents typically need 30+ tokens/second for a usable experience. The 2× RTX Pro 6000 setup (at approximately $12K–$18K per card) achieves this. Consumer hardware generally doesn't.

**EAGLE speculative decoding:** Mistral released `mistralai/Mistral-Medium-3.5-128B-EAGLE` — a companion model for speculative decoding that accelerates inference with vLLM and SGLang. This can improve effective throughput on supported setups.

**GGUFs:** Available from Unsloth on HuggingFace. **Note:** GGUFs generated before approximately May 2, 2026 include a YaRN long-context bug from an incorrect Transformers config entry. This degrades quality on long contexts. Affected GGUFs were generated with the original model configuration before a corrective commit (`c4be198050fb5789774a55b92ed697becfbf20ae`). Download GGUFs created after May 2 to avoid this issue.

---

## Vibe Remote Agents

The Vibe CLI coding agent received its major capability upgrade alongside Medium 3.5. Prior to this release, Vibe ran synchronous local sessions. With remote agents:

- Sessions execute in **cloud-hosted isolated sandboxes**
- **Session continuity:** a local CLI session can be "teleported" to the cloud — history, state, and pending approvals carry over
- **Parallel execution:** multiple agent tasks can run simultaneously
- **Async operation:** agents continue working while the developer is away
- **Integrations:** GitHub (code and PRs), Linear and Jira (issues), Sentry (incidents), Slack and Microsoft Teams

Vibe installs via `uv pip install mistral-vibe`. Designed for long-horizon tasks: module refactors, test generation, dependency upgrades, CI investigations, and bug fixing.

The τ³-Telecom 91.4% and SWE-Bench 77.6% scores are the model-level justifications for why Medium 3.5 — not a prior Mistral model — powers this. Whether remote Vibe sessions translate to those benchmark numbers in practice depends on the task structure and tooling setup, but the benchmark selection is coherent with the use case.

**Le Chat Work Mode:** Announced simultaneously, this adds agentic capabilities to Mistral's consumer chat product — cross-tool workflows across email, calendar, documents. Connectors (including mailboxes) are on by default; write operations (sending, modifying data) require explicit user approval before execution. This is Mistral's answer to ChatGPT Tasks and Claude's computer use capabilities.

---

## Community Reception

**HackerNews (500 points, 229 comments at launch):** Strong engagement with mixed reactions.

The positive camp focused on the SWE-Bench achievement, the "merged model" consolidation story, and the accessibility of Q4 quantization (~70GB). Developers appreciated no longer needing to choose between Mistral's reasoning model and coding model.

The critical camp raised several recurring concerns:

**Benchmark cherry-picking:** "Almost every open weight model launch this year has come with claims that it matches or exceeds Sonnet. I've been trying a lot of them and I have yet to see it in practice" was a common sentiment. Mistral's emphasis on SWE-Bench and τ³-Telecom while omitting GPQA, MMLU, and LiveCodeBench looked selective.

**Efficiency paradox:** Multiple commenters noted that Qwen 3.6 35B A3B (a MoE with far fewer active parameters, 4.7× smaller) shows comparable real-world performance in coding tasks. A dense 128B model is harder to justify when efficient MoEs can match it while consuming a fraction of the compute.

**Speed at quantization:** Q4 on consumer hardware (M3 Ultra, multi-3090 setups) reaches 3–7 tokens/second. This is "theoretically running locally" in the same way a diesel generator is "theoretically a power source." For practical interactive use, it's not viable without data-center hardware.

**Price reaction:** The 3.75× price increase from Medium 3 was consistently flagged as steep. Developers who had built workflows on Medium 3 face a pricing renegotiation.

**"A little sad since they once were prominent":** A minority but notable reaction pointing to Mistral's earlier reputation for efficiency innovation with Mixtral MoE, and questioning whether a large dense model is the right architectural direction in 2026.

HuggingFace community (317 likes) was more constructive: deployment-focused discussions, successful reports of 30 t/s on 2× RTX Pro 6000 hardware, research community interest (requests for academic citation DOI), and quantized format support questions.

---

## The Internal Competition Problem

The awkward fact in Mistral's lineup is that **Mistral Small 4** — released one month earlier — complicates Medium 3.5's value proposition for most developers.

| | Mistral Small 4 | Mistral Medium 3.5 |
|---|---|---|
| Release date | March 16, 2026 | April 29, 2026 |
| Total parameters | 119B | 128B |
| Active parameters/token | 6B (MoE) | 128B (dense) |
| Context window | 128K | 256K |
| License | Apache 2.0 | Modified MIT ($20M cap) |
| Self-hosting VRAM | ~12GB (6B active) | ~256GB (128B active) |
| AI Intelligence Index | ~35 | 39.23 |
| Use case | General API, cost-efficient | Long-horizon agentic, Vibe |

For standard API workloads — RAG pipelines, document processing, coding assistance, chat — Mistral Small 4 offers comparable intelligence scores, runs on consumer GPUs, and carries a fully permissive license. The question "why pay 3.75× more and accept a revenue cap?" has a specific answer: sustained long-horizon agentic tasks where dense architecture consistency matters.

That's a legitimate niche. But it's a narrower audience than Mistral's announcement language suggests.

---

## Comparison to the Mistral Ecosystem

**vs. Mistral Large 3 (675B MoE, 41B active, Apache 2.0, $0.50/$1.50):**
Medium 3.5 has superior benchmark scores and the adjustable reasoning capability. Large 3 is dramatically cheaper and fully open-source. Large 3 still makes sense for high-throughput multilingual deployments at minimum cost.

**vs. Devstral 2 (123B, Apache 2.0 — what Medium 3.5 replaces in Vibe):**
Medium 3.5 is demonstrably more capable on SWE-Bench and adds vision and reasoning. The tradeoff is a more restrictive license and higher API costs. For teams self-hosting a coding agent, the Apache 2.0 → Modified MIT transition is a real procurement consideration.

---

## Rating: 3.5/5

**What earns the 3.5:**

The consolidation story is genuine and useful. Having one model replace three in Mistral's own product suite is an engineering achievement, and developers benefit from not needing to pick between Medium 3.1, Magistral, and Devstral 2. SWE-Bench Verified 77.6% is a real number — the model can do serious coding work. The adjustable reasoning design is practical and composable. The 256K context window is competitive. Speed at 163.4 t/s is genuinely fast for a 128B model.

**What limits the score:**

The Artificial Analysis Intelligence Index (39.23) places Medium 3.5 around 20th overall — a meaningful gap below frontier models (Gemini 3.1 Pro: 57.18, Claude Opus 4.7: 57.28). The omission of GPQA, MMLU, and science benchmarks in Mistral's own launch materials is a telling gap. The 3.75× price increase from Medium 3 is steep, especially against DeepSeek V4 Pro which exceeds Medium 3.5 on SWE-Bench while pricing output 53% cheaper. The Modified MIT license is less generous than Apache 2.0 (the license on Devstral 2, Small 4, and Large 3), which will matter to enterprises and research institutions. And the dense 128B architecture, while defensible for long-horizon agentic use, looks inefficient against MoE alternatives at similar or lower API costs.

Medium 3.5 is a capable model for a specific use case: long-horizon agentic coding via Vibe, or API workloads that need a single endpoint for instruction-following, reasoning, and coding without model-switching. Outside that use case, the pricing and benchmark profile relative to DeepSeek V4 Pro and Qwen 3.6 is harder to justify.

For teams already in the Mistral ecosystem building with Vibe or Le Chat: the consolidation and capability upgrade make Medium 3.5 the obvious choice. For teams evaluating from scratch: the value proposition is narrower than the SWE-Bench headline suggests.

---

## Quick Reference

| | |
|---|---|
| **Company** | Mistral AI (Paris, France) |
| **Released** | April 29, 2026 |
| **Parameters** | 128B (all active, dense) |
| **Context** | 256K tokens |
| **Modalities** | Text + image in; text out |
| **Reasoning** | Adjustable (`reasoning_effort` param) |
| **SWE-Bench Verified** | 77.6% |
| **τ³-Telecom** | 91.4% |
| **AI Intelligence Index** | 39.23 (~#20 overall, Artificial Analysis) |
| **API speed** | 163.4 t/s (9th fastest) |
| **API pricing** | $1.50 input / $7.50 output per M tokens |
| **License** | Modified MIT ($20M/month revenue cap) |
| **HuggingFace** | [mistralai/Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B) |
| **Self-host min.** | ~256GB VRAM (BF16); Q4 ~70GB |
| **Rating** | 3.5 / 5 |

---

*Related ChatForest reviews: [Mistral Large 3](/reviews/mistral-large-3-open-weight-moe-llm-review/) · [Mistral AI overview](/reviews/mistral-ai-open-weight-llm-european-ai/) · [DeepSeek V4](/reviews/deepseek-v4-open-weight-llm-review/) · [Qwen 3.6 Max Preview](/reviews/alibaba-qwen-3-6-max-preview-closed-weight-agentic-llm-review/)*
