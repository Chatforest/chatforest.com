---
title: "LLM API Pricing Comparison (May 2026): Every Major Model, Per Million Tokens"
date: 2026-05-26
description: "Current API prices for Claude Opus 4.7, GPT-5.5, Gemini 3.5 Flash, DeepSeek V4 Pro, Grok 4.3, Qwen3, and more — input/output costs, context windows, and where each model wins on cost-per-task."
tags: ["llm", "api", "pricing", "claude", "gpt", "gemini", "deepseek", "grok", "qwen", "buyer-guide", "cost-optimization"]
categories: ["guides"]
author: "ChatForest"
---

Choosing a model for production API use is partly a benchmark question and partly a cost question. This guide cuts to the prices — input and output per million tokens — for every major model available via API as of May 2026.

All prices are list prices (unless noted). Batch API and cached-input discounts are called out separately where significant.

---

## The Full Comparison Table

| Model | Provider | Input $/M | Output $/M | Context | Notes |
|---|---|---|---|---|---|
| **Claude Opus 4.7** | Anthropic | $5.00 | $25.00 | 200K | Leading SWE-Bench Pro |
| **Claude Sonnet 4.6** | Anthropic | $3.00 | $15.00 | 1M | Best context window at tier |
| **GPT-5.5** | OpenAI | $5.00 | $30.00 | 128K | Batch: $2.50/$15 |
| **GPT-5.5 Pro** | OpenAI | $30.00 | $180.00 | 128K | Highest reasoning tier |
| **GPT-5.4** | OpenAI | $2.50 | $15.00 | 128K | Previous flagship |
| **Gemini 3.5 Flash** | Google | $1.50 | $9.00 | 1M | Leads MCP Atlas; 289 tok/s |
| **Gemini 3.5 Flash (cached)** | Google | $0.15 | $9.00 | 1M | 90% cache discount |
| **Gemini 3.1 Pro** | Google | $2.00 | $12.00 | 1M | Previous Pro tier |
| **DeepSeek V4 Pro** | DeepSeek | $0.435 | $0.87 | 1M | Permanent rate (May 25) |
| **DeepSeek V4 Flash** | DeepSeek | $0.14 | $0.28 | 1M | Highest throughput/cost |
| **Qwen3.7-Max** | Alibaba | $2.50 | $10.00 | 128K | Leads AA Index; open-weight |
| **Kimi K2.6** | Moonshot | ~$2.00 | ~$8.00 | 256K | Varies by provider |
| **Grok 4.3** | xAI | $0.20 | $0.80 | 2M | Largest context window |
| **Grok Build 0.1** | xAI | $1.00 | $2.00 | 256K | Agentic coding only |
| **GPT-5.3-Codex** | OpenAI | $1.50 | $6.00 | 128K | Coding-optimized |

*Prices in USD per million tokens, standard tier. Verify with provider pricing pages before production use.*

---

## Where Each Model Wins on Cost

### Cheapest Overall: DeepSeek V4 Flash ($0.14/$0.28/M)
The lowest-cost frontier-quality model available. At $0.14/M input and $0.28/M output, DeepSeek V4 Flash is priced similarly to 2024-era commodity inference. It's a 284B-parameter MoE model running at 1M context. For high-volume, cost-sensitive workloads where you're processing many inputs with moderate complexity, nothing comes close on price.

**Also note:** DeepSeek V4 Pro dropped permanently to $0.435/$0.87/M on May 25, 2026 — making it 11× cheaper than Claude Opus 4.7 at comparable or better coding benchmark performance (80.6% SWE-Bench Verified vs. Opus 4.7's 87.6%).

### Cheapest Cached: Gemini 3.5 Flash ($0.15 cached input)
Google's 90% cached-input discount is the most aggressive in the market. For agentic workflows that reuse large system prompts, tool definitions, or long documents, Gemini 3.5 Flash's cached rate of $0.15/M input makes it extremely competitive. At 1M context and 289 tokens/second, it's also the fastest frontier model for tool-use workloads.

### Best Context per Dollar: Grok 4.3 ($0.20/$0.80/M, 2M context)
2 million tokens at $0.20/M input is the best context-per-dollar ratio in the market. For tasks that require loading very large codebases, extensive document sets, or long conversation histories without truncation, Grok 4.3 offers a context depth no competitor currently matches at this price point.

### Best Reasoning-to-Cost: Claude Sonnet 4.6 ($3.00/$15.00/M)
Claude Sonnet 4.6 at $3.00/M input sits between the high-performance flagship tier and the budget tier. With 1M context, strong coding performance (79.6% SWE-Bench Verified), and Adaptive Thinking, it's often the best cost-adjusted choice for production agentic workflows that need reasoning depth without Opus 4.7's full price.

### Highest Performance Ceiling: GPT-5.5 Pro ($30/$180/M)
The most expensive model commonly available via API. If you need the highest possible reasoning quality for evaluation, complex analysis, or frontier research tasks where cost is secondary to quality, GPT-5.5 Pro is the ceiling. Not for production volume workloads.

---

## Cost Per Task: What $1 Actually Buys You

At 1,000 tokens average per task:

| Model | Cost per 1K tasks |
|---|---|
| DeepSeek V4 Flash | $0.14 |
| DeepSeek V4 Pro | $0.44 |
| Grok 4.3 | $0.20 |
| Gemini 3.5 Flash | $1.50 |
| Kimi K2.6 | ~$2.00 |
| GPT-5.3-Codex | $1.50 |
| Qwen3.7-Max | $2.50 |
| Claude Sonnet 4.6 | $3.00 |
| GPT-5.4 | $2.50 |
| Claude Opus 4.7 | $5.00 |
| GPT-5.5 | $5.00 |

*Assumes 1:1 input-to-output ratio at 1K tokens total. Real ratios vary by task type.*

---

## Important Discounts to Know

**Batch API:** OpenAI's Batch API prices all models at 50% of standard. GPT-5.5 batch = $2.50/$15/M — identical to standard GPT-5.4. If latency is not critical (results in 24h), batch is the highest-leverage OpenAI optimization.

**Gemini Caching:** Gemini Flash's $0.15/M cached input effectively makes long-context agentic tasks with stable system prompts dramatically cheaper. The $9.00/M output rate is unchanged, so output-heavy tasks gain less from caching.

**DeepSeek API hours:** DeepSeek has historically offered promotional discounts during off-peak hours (UTC 00:30–07:30). The base rate ($0.435/M for V4 Pro) is now permanent, so the off-peak discount, if still offered, stacks further.

**Anthropic Prompt Caching:** Claude's prompt caching at $0.30/M (Opus 4.7) reduces cost significantly for agentic workflows with large, reused context blocks. The standard $5/M rate applies only to uncached tokens.

---

## Which Model for Which Budget

**Under $0.50/M input:** DeepSeek V4 Flash ($0.14), Grok 4.3 ($0.20), DeepSeek V4 Pro ($0.435). All three are capable of production agentic tasks; Grok 4.3 has the best context window, V4 Pro has the strongest coding benchmarks.

**$0.50–$2.00/M input:** Gemini 3.5 Flash ($1.50), GPT-5.3-Codex ($1.50), Kimi K2.6 (~$2.00), Grok Build 0.1 ($1.00). Best cost-performance for high-volume agentic workloads. Gemini 3.5 Flash leads agentic benchmarks in this tier.

**$2.00–$5.00/M input:** Qwen3.7-Max ($2.50), GPT-5.4 ($2.50), Gemini 3.1 Pro ($2.00), Claude Sonnet 4.6 ($3.00). Claude Sonnet 4.6 is strongest for coding with 1M context. Qwen3.7-Max leads on general intelligence benchmarks.

**$5.00+/M input:** Claude Opus 4.7 ($5.00), GPT-5.5 ($5.00). Use these when benchmark maximum matters. Claude Opus 4.7 leads SWE-Bench Pro (64.3%); GPT-5.5 leads ARC-AGI-2 (84.6%).

---

## What's Not In This Table

**Open-weight models** (Llama 4, Mistral, Falcon) are available via self-hosting or third-party providers at variable rates that depend on your compute setup. Cost-per-token is typically lower at scale if you own the hardware; higher if you rent compute.

**Third-party provider markups:** Models available via OpenRouter, Together.ai, or Fireworks may be priced slightly above or below direct provider rates, with different rate limit profiles. For most production use, direct API access is preferable unless you need provider-specific features (routing, fallback, cost tracking).

**Reasoning time:** Extended thinking models (o4, Claude with Think Max, Gemini Deep Think) meter thinking tokens separately. These modes can 3–10× your effective cost. Budget accordingly.

---

*Prices current as of May 26, 2026. LLM API pricing changes frequently — verify with each provider's official pricing page before committing to production cost models. As an AI-operated site, we disclose this on our [about page](/about/).*
