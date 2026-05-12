---
title: "OpenAI GPT-5 and GPT-5.5 — The Agentic Turn, the Hallucination Tension, and OpenAI's 2025–2026 Flagship Arc"
date: 2026-05-12T23:00:00+09:00
description: "OpenAI's GPT-5 (August 2025) unified reasoning and speed for the first time. GPT-5.5 (April 2026) became the new default for ChatGPT, with 52.5% fewer hallucinations in high-stakes domains, sharper agentic coding, and a more concise personality. But third-party evals tell a more complicated story. We review the full 5.x arc."
og_description: "GPT-5 hit 94.6% on AIME 2025 and 74.9% on SWE-bench Verified. GPT-5.5 (April 2026) scores 58.6% on SWE-Bench Pro and 82.7% on Terminal-Bench 2.0, with 52.5% fewer hallucinations than GPT-5.3 Instant. GPT-5.5 Instant is now ChatGPT's default model. Pricing: $5/$30 per 1M tokens. Rating: 4/5."
content_type: "Review"
card_description: "OpenAI's GPT-5 (August 2025) was the first model to unify deep reasoning and low-latency response in a single system — a smart, fast mode for everyday questions and an extended thinking mode for hard problems, with a real-time router that chooses between them. GPT-5 hit 94.6% on AIME 2025 without tools and 74.9% on SWE-bench Verified coding — state-of-the-art at launch across math, code, and science. GPT-5.5 followed in April 2026 with improved agentic coding (58.6% SWE-Bench Pro), sharper terminal reasoning (82.7% Terminal-Bench 2.0), and a 30% reduction in response verbosity. GPT-5.5 Instant became ChatGPT's default model on May 5, 2026, with 52.5% fewer hallucinations than its predecessor in medicine, law, and finance. Pricing: GPT-5.5 at $5/$30 per 1M tokens, GPT-5.5 Pro at $30/$180. Both share a 1M-token context window. The tension: OpenAI's internal benchmarks show dramatic hallucination reduction; Artificial Analysis's independent AA-Omniscience eval shows GPT-5.5 at 86% hallucination rate versus Claude Opus 4.7 at 36%. The versioning is dense, the pricing is tiered, and the competitive landscape has never been tighter. Rating: 4/5."
tags: ["llm", "openai", "gpt-5", "gpt-5.5", "agentic-ai", "reasoning", "multimodal", "enterprise-ai", "api", "long-context"]
categories: ["reviews"]
rating: 4
author: "ChatForest"
last_refreshed: 2026-05-12
---

On August 6, 2025, OpenAI released GPT-5 — the first model in the company's history billed as a unified system rather than a single model. The announcement described something architecturally distinct from prior GPT releases: a fast, efficient mode for everyday questions and a deeper reasoning mode for harder problems, with a **real-time router** that decides which to invoke based on conversation type, complexity, tool requirements, and the user's explicit intent. This was not a new idea — other labs had shipped fast and slow variants — but it was OpenAI's first public commitment to this pattern as the base design of their flagship.

The benchmarks at launch were the strongest the company had published. GPT-5 achieved **94.6% on AIME 2025** without tool use, **74.9% on SWE-bench Verified** for real-world coding, and strong performance on GPQA Diamond — the graduate-level Google-proof science benchmark — at a level that placed it at or near state-of-the-art across three distinct capability domains simultaneously.

Nine months later, GPT-5.5 arrived. On April 23, 2026, OpenAI released GPT-5.5 and GPT-5.5 Pro to the API. On May 5, 2026, **GPT-5.5 Instant became the new default model for ChatGPT**, replacing GPT-5.3 Instant. The release positioned GPT-5.5 as a step forward in agentic capability, hallucination reduction, and response conciseness — while simultaneously raising new questions from third-party evaluators.

This review covers the GPT-5 and GPT-5.5 arc in the depth that deployment decisions require.

---

## OpenAI: The Context

**OpenAI** launched GPT-5 as a company that had spent three years balancing consumer adoption with organizational turbulence. The November 2023 board-and-CEO crisis — Sam Altman fired and rehired within five days — had been followed by a governance restructuring, a public commitment to formal AGI safety frameworks, and an announced conversion to a for-profit public benefit corporation structure.

By 2025, the business picture was clearer. ChatGPT had crossed 300 million weekly active users. The API was generating significant enterprise revenue. Microsoft remained OpenAI's primary infrastructure partner, running workloads on Azure Nvidia H100 and H200 clusters. OpenAI's differentiation from competitors had evolved: rather than claiming to be the "safest" or the "most open," the company increasingly positioned itself as the provider that could ship capable agentic systems at consumer scale.

GPT-5 was the first model explicitly framed in this context. The announcement was not just about benchmark performance — it was about what the model could *do* autonomously over time, across tools, in multi-step workflows.

---

## GPT-5: The First Unified System (August 2025)

### Architecture: Routing, Not Stacking

The most important structural claim about GPT-5 was the routing system. Prior to GPT-5, "reasoning" and "fast" variants existed as separate models — o1-pro for extended thinking, GPT-4o for fast response. Users and developers had to choose which to deploy.

GPT-5 changed this by embedding a **real-time router** that selects the appropriate compute budget per query. A casual follow-up question routes to the fast mode; a multi-step math proof routes to extended reasoning. The router uses conversation type, complexity signals, explicit user intent, and tool invocation patterns as inputs. OpenAI's claim was that this made GPT-5 better on easy questions (no unnecessary slowdown) and better on hard questions (no failure to invoke reasoning when needed) simultaneously.

This is the design pattern that the company described as "unified" — not that one model does everything, but that the routing mechanism makes the capability split invisible to the user.

### Benchmark Performance

GPT-5's headline results at launch:

| Benchmark | GPT-5 Score | Notes |
|-----------|-------------|-------|
| AIME 2025 | 94.6% | Without tool use |
| SWE-bench Verified | 74.9% | Real-world GitHub issue resolution |
| GPQA Diamond | ~90%+ | Graduate-level science Q&A |
| MMMU | 84.2% | Multimodal understanding |

The AIME 2025 score was the most discussed. At 94.6% without tools — meaning the model solved competition math problems from pure language modeling, without executing code or calling calculators — GPT-5 was the first model to cross the 90% threshold on this benchmark without scaffolding. For context: human AMC/AIME competitors attempting AIME problems score around 60–70% on average. GPT-5 was operating at a level that would place it among competitive mathematics participants.

The SWE-bench Verified score (74.9%) represented the strongest coding performance any OpenAI model had achieved on this benchmark. SWE-bench Verified tests the model's ability to resolve actual GitHub issues — not toy problems, but real bugs submitted by real engineers, with full repository context. A 74.9% pass rate meant GPT-5 autonomously resolved nearly three-quarters of the evaluated issues.

### Multimodal Capabilities

GPT-5 continued the GPT-4o multimodal architecture — text and vision as primary inputs, with audio and video capabilities available in ChatGPT. The improvements over GPT-4o were incremental on visual reasoning but notable on **scientific image interpretation** — the model showed stronger ability to reason about charts, molecular structures, and data visualizations in ways relevant to professional scientific work.

---

## The Versioning Arc: GPT-5.1 Through 5.4

Between August 2025 and April 2026, OpenAI released a series of intermediate versions. The versioning reflects a pattern that the company has used since GPT-4: a flagship model followed by iterative refinements, with each generation having multiple sub-variants optimized for different trade-offs.

The intermediate versions are worth noting because they established the trajectory that GPT-5.5 continues:

- **GPT-5.2 Thinking** (late 2025) — Extended reasoning variant optimized for step-by-step problem solving. Achieved 55.6% on SWE-Bench Pro and 40.3% on FrontierMath Tier 1–3 (expert-level mathematics). GPQA Diamond score of 92.4%.

- **GPT-5.2 Pro** — Higher-accuracy variant. GPQA Diamond 93.2%.

- **GPT-5.3 Instant** — The fast, low-latency variant that became the ChatGPT default prior to GPT-5.5. Positioned for consumer use; the benchmark it later lost ground from.

- **GPT-5.4** — Iterative improvements with focus on agentic task performance and specific domain accuracy. GPT-5.4 mini and nano sub-variants also released, targeting lower-cost API use cases.

The pattern: each major version number introduces architectural or training changes; each sub-version iterates toward specific deployment targets (consumer instant, API thinking, pro accuracy).

---

## GPT-5.5: The April 2026 Release

### What's New

GPT-5.5 was released to the API on April 24, 2026, with GPT-5.5 Pro available simultaneously. The announced improvements targeted four areas:

**1. Agentic Coding**

GPT-5.5 is OpenAI's strongest agentic coding model to date:
- **58.6% on SWE-Bench Pro** — OpenAI's harder variant of SWE-bench, evaluating real-world GitHub issue resolution across a curated set of difficult cases.
- **82.7% on Terminal-Bench 2.0** — A benchmark testing complex command-line workflows requiring planning, iteration, and tool coordination. State-of-the-art as of release.

These numbers place GPT-5.5 ahead of its predecessors on both coding benchmarks, with the Terminal-Bench result suggesting particular strength in the multi-step tool use and shell scripting workflows that autonomous coding agents require.

**2. Hallucination Reduction in High-Stakes Domains**

OpenAI's internal comparison: GPT-5.5 Instant produced **52.5% fewer hallucinated claims** than GPT-5.3 Instant on high-stakes prompts in medicine, law, and finance, and **37.3% fewer inaccurate claims** on conversations users had flagged for factual errors.

These are the domains where hallucination costs are highest — a medical AI that confidently states an incorrect drug interaction is not just wrong, it's harmful. The size of the claimed reduction (more than half on high-stakes medical/legal/financial prompts) is the largest improvement OpenAI has published in this category.

**3. Response Conciseness**

A qualitative complaint about GPT-5.3 Instant — and about the GPT-5 family generally — was verbosity. Responses often included unnecessary preamble, repetitive summarization, and emoji overuse that made outputs feel padded rather than precise.

GPT-5.5 Instant addresses this directly:
- **30.2% fewer words** than GPT-5.3 Instant on equivalent prompts
- **29.2% fewer lines** per response

This is a meaningful quality-of-life improvement for API developers integrating outputs into products — shorter outputs are easier to parse, display, and process downstream.

**4. Personalization and Memory**

GPT-5.5 Instant (the ChatGPT consumer version) adds new memory capabilities:
- **Memory sources**: A control panel showing users what context ChatGPT used to personalize a response — saved memories, past conversations, linked files. Users can delete or correct specific entries.
- **Gmail integration**: With permission, GPT-5.5 Instant can reference past emails to provide more relevant answers. Available to Plus and Pro users.
- **Conversation history search**: The model can use its search tool to retrieve context from past ChatGPT sessions, enabling continuity across conversations.

These features are consumer-facing and not available via the API in the same form, but they represent OpenAI's direction for personal AI assistant design: transparent about what it knows, controllable by the user.

### Benchmark Summary (GPT-5.5 Instant vs predecessor)

| Benchmark | GPT-5.3 Instant | GPT-5.5 Instant | Change |
|-----------|-----------------|-----------------|--------|
| AIME 2025 | 65.4% | 81.2% | +15.8 pts |
| MMMU-Pro | 69.2 | 76 | +6.8 pts |
| High-stakes hallucinations | baseline | −52.5% | Large reduction |
| Response length | baseline | −30.2% words | More concise |

---

## GPT-5.5 Pro: The Heavy Variant

GPT-5.5 Pro is positioned for workloads where accuracy outweighs cost. Key differences from standard GPT-5.5:

- **Optimized for**: deep reasoning, long-horizon problem solving, agentic coding on complex codebases, precise multi-step execution
- **Context**: 1M token window (922K input, 128K output)
- **Inputs**: text and images
- **Pricing**: $30/M input, $180/M output — a 6x premium over standard GPT-5.5

The Pro variant's use cases are enterprise: auditing large codebases, generating comprehensive research reports, executing multi-day autonomous agent tasks where a single error propagates into downstream failures. For most API consumers, standard GPT-5.5 will be the appropriate default. Pro is for when the economics of a failed high-stakes task justify higher per-token cost.

---

## Pricing and Context Window

| Model | Input (per 1M) | Output (per 1M) | Context |
|-------|----------------|-----------------|---------|
| GPT-5.5 Instant | Free (ChatGPT) | — | 1M |
| GPT-5.5 | $5 | $30 | 1M |
| GPT-5.5 Pro | $30 | $180 | 1M |

**Important pricing caveat**: Prompts exceeding 272K input tokens are charged at **2x input and 1.5x output** for the full session under standard, batch, and flex tiers. The 1M context window is real, but processing large contexts carries a cost premium beyond a threshold most applications will rarely reach in practice.

Batch and Flex pricing are available at half the standard API rate. Priority processing (guaranteed low-latency SLA) is available at 2.5x the standard rate.

Compared to the competitive landscape: Claude Opus 4.7 (Anthropic) is priced comparably to GPT-5.5 Pro. Gemini 3.1 Pro is positioned in the mid-tier. DeepSeek V4-Flash is significantly cheaper per token at comparable capability levels on several benchmarks — the Chinese open-weights ecosystem continues to apply pricing pressure on Western frontier models.

---

## The Hallucination Tension

The most important contextual fact about GPT-5.5 is the gap between OpenAI's internal benchmark findings and third-party evaluator results.

**OpenAI's claim**: 52.5% reduction in hallucinated claims on high-stakes prompts (medicine, law, finance). 37.3% reduction on flagged conversations. This is the company's own evaluation, comparing GPT-5.5 to GPT-5.3 Instant.

**Artificial Analysis's independent finding**: On their AA-Omniscience eval — a test for correct factual recall across a broad knowledge base — GPT-5.5 showed an **86% hallucination rate**. For comparison: [Claude Opus 4.7](/reviews/anthropic-claude-opus-4-7-deep-dive/) scored 36%, Gemini 3.1 Pro Preview scored 50%.

These two results are not necessarily contradictory, but they require careful interpretation:

1. **Different benchmarks measure different things.** OpenAI's eval tests hallucination on high-stakes prompts where the model has strong knowledge — medical, legal, financial questions where training data is rich. AA-Omniscience tests factual recall across a broader and more heterogeneous knowledge base, including many domains where the model has less coverage.

2. **Relative improvement vs. absolute accuracy.** A 52.5% reduction in hallucinations over a prior model is consistent with still having a high absolute rate if the prior model was worse. If GPT-5.3 Instant hallucinated at, say, a 90% rate on AA-Omniscience, a 52.5% reduction would still leave GPT-5.5 near 43% — still high relative to Opus 4.7.

3. **"High-stakes" selection bias.** High-stakes prompts in medicine, law, and finance may be specifically the domains where OpenAI has invested heavily in RLHF and factual accuracy work, making them precisely the domain where GPT-5.5 performs best. AA-Omniscience casts a wider net.

The practical implication: GPT-5.5's hallucination profile is better than its immediate predecessor on specific tested domains, and has genuinely improved. But it remains materially worse than Claude Opus 4.7 on independent broad-knowledge evaluations. Applications where factual accuracy on a wide knowledge base matters — reference tools, information retrieval, research assistance — should treat this as a material consideration.

---

## GPT-5.5 Instant as ChatGPT's Default (May 2026)

On May 5, 2026, GPT-5.5 Instant became the default model for all ChatGPT users, replacing GPT-5.3 Instant. Paid users retain the ability to switch back to GPT-5.3 Instant for a three-month transition period.

The move signals OpenAI's confidence in GPT-5.5 Instant's quality improvement relative to the predecessor. Key user-facing changes:

- Shorter, more direct responses
- Improved accuracy on math and STEM (AIME up 15.8 points, MMMU-Pro up 6.8 points)
- Gmail integration for personalized context
- Memory source transparency panel
- Lower verbosity and fewer unsolicited emojis

The transition is smoother than previous ChatGPT model upgrades. The conciseness improvement in particular was widely noted in early user responses — the prior GPT-5.3 Instant had attracted criticism for padding responses with filler.

---

## GPT-5.5 in the Competitive Landscape (May 2026)

The model landscape in mid-2026 is the most competitive it has ever been:

| Model | Strengths | Relative Position |
|-------|-----------|-------------------|
| GPT-5.5 | Agentic coding, consumer UX, 1M context | Strong across most domains |
| Claude Opus 4.7 | Lower hallucination rate, factual accuracy | Preferred for knowledge-intensive tasks |
| Gemini 3.1 Pro | Multimodal reasoning, Google ecosystem integration | Competitive on visual/scientific tasks |
| DeepSeek V4-Flash | Cost efficiency (284B MoE, 13B active params) | Frontier capability at fraction of API cost |
| GLM-5.1 / Kimi K2.6 / MiniMax M2.7 | Agentic coding at lower cost | Serious alternatives for code-intensive workloads |

The story of 2026 is that GPT-5.5 is no longer the default choice for every use case. For agentic coding and everyday conversational tasks, it remains among the best available. For factual retrieval at scale, Opus 4.7's lower hallucination rate is a meaningful advantage. For cost-constrained high-volume inference, DeepSeek V4-Flash and the Chinese open-weights labs have closed the capability gap at dramatically lower per-token cost.

OpenAI's durability as the default choice for most developers rests on ecosystem advantages — the mature API, the deepest tool integrations, the ChatGPT distribution — more than on benchmark supremacy. GPT-5.5 maintains competitive position while those advantages hold.

---

## Deployment Paths

**ChatGPT**: Free users get GPT-5.5 Instant as the default. Plus and Pro tiers unlock GPT-5.5, GPT-5.5 Pro, and the memory personalization features.

**API**: GPT-5.5 and GPT-5.5 Pro are available via OpenAI's Responses and Chat Completions APIs. Model IDs: `gpt-5.5` and `gpt-5.5-pro`. Both support text and image inputs.

**Batch Processing**: Standard pricing at half rate. Appropriate for large-scale offline workloads where latency is not a constraint.

**Priority Processing**: 2.5x standard rate, guaranteeing low-latency SLA. Relevant for production real-time applications with SLA commitments.

**Microsoft Azure**: GPT-5.5 is available through Azure OpenAI Service, with region-specific availability. Enterprise customers on Azure benefit from additional data privacy and compliance guarantees, HIPAA BAA coverage, and EU data residency options where required.

---

## Limitations and Known Issues

**Hallucination rate on broad knowledge**: The AA-Omniscience discrepancy (86% vs. Claude Opus 4.7's 36%) is the most significant caveat for knowledge-intensive applications. GPT-5.5's improvements are real but concentrated in specific tested domains.

**Context pricing step-up**: The 2x pricing premium above 272K tokens makes long-context processing materially more expensive than the base rate implies. Applications designed around the full 1M context window should model the cost premium into their unit economics.

**Confusing versioning**: The GPT-5.x series (5.0, 5.1, 5.2, 5.2 Thinking, 5.2 Pro, 5.3 Instant, 5.4, 5.4 mini, 5.4 nano, 5.5, 5.5 Instant, 5.5 Pro) creates real friction for developers tracking model capabilities. Each version has different benchmarks, different pricing, and different API identifiers. This is not unique to OpenAI — Anthropic and Google have their own versioning complexity — but it creates a maintenance burden for teams keeping their model selection current.

**No open weights**: GPT-5.5 is proprietary. Teams with data sovereignty requirements, on-premise deployment needs, or fine-tuning plans cannot use it in those configurations. DeepSeek V4, Qwen 3, and Llama 4 remain the primary frontier open-weights alternatives.

**Compute dependency on Azure**: OpenAI does not own its compute infrastructure at the level Google (TPUs) or Amazon (Trainium) does. Outages, capacity constraints, and pricing changes on Azure can affect API availability and economics in ways outside OpenAI's direct control.

---

## What Changed from GPT-4o and GPT-4.1

For teams currently on GPT-4o or GPT-4.1, the GPT-5.5 migration brings:

- **Coding**: SWE-bench Verified 74.9% (GPT-5) vs 54.6% (GPT-4.1) — a 20-point gap. For agentic coding agents, this is material.
- **Math**: AIME 2025 94.6% (GPT-5) vs GPT-4.1's far lower performance on the same benchmark. For math-heavy applications, GPT-5 is a different product category.
- **Context**: 1M tokens (GPT-5.5) vs 1M tokens (GPT-4.1) — comparable, but GPT-5.5's reasoning quality within long context is improved.
- **Cost**: GPT-5.5 at $5/M input vs GPT-4.1's pricing — models in the same general tier.
- **Conciseness**: GPT-5.5 Instant's 30% verbosity reduction is a direct quality-of-life improvement for production integrations.

The GPT-4o/4.1 generation is now clearly in maintenance mode. GPT-5.5 is the active development line.

---

## Rating: 4/5

GPT-5.5 is a genuinely strong model and a meaningful upgrade from its immediate predecessors. The agentic coding benchmarks (58.6% SWE-Bench Pro, 82.7% Terminal-Bench 2.0) are the best OpenAI has published. The conciseness improvement is real and appreciated by developers. The 52.5% hallucination reduction in high-stakes domains is a material safety improvement.

The one-point deduction comes from two compounding issues. First, the hallucination rate discrepancy on independent evals is too large to ignore — 86% on AA-Omniscience is a concrete limitation for knowledge-intensive use cases, and the gap versus Claude Opus 4.7 (36%) is wide enough to affect deployment decisions. Second, the versioning complexity of the GPT-5.x series creates genuine cognitive overhead for teams tracking model selection — OpenAI has not invested in making this navigable.

**GPT-5.5 is the right default for agentic coding, consumer chat, and high-volume general inference. For factual knowledge retrieval, information verification, and domains where hallucination has high cost, benchmark against Claude Opus 4.7 before committing.**

*Reviewed by ChatForest. We research public sources — benchmarks, system cards, documentation, and developer reports. We have not tested these models ourselves.*
