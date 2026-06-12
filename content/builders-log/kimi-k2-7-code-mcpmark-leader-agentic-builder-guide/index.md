---
title: "Kimi K2.7 Code Tops MCPMark Over Claude Opus, Drops 30% of Thinking Tokens — Builder Setup Guide"
date: 2026-06-13
description: "Moonshot AI released Kimi K2.7 Code on June 12, 2026. It beats Claude Opus 4.8 on MCPMark tool use (81.1% vs 76.4%), uses 30% fewer thinking tokens than K2.6, and drops into Claude Code via an Anthropic-compatible endpoint. Builder setup guide and K2.6 migration notes."
og_description: "Kimi K2.7 Code: 1T MoE, 32B active, 256K context, open-weight MIT. Beats Claude Opus 4.8 on MCPMark (81.1% vs 76.4%), 30% leaner thinking tokens, preserve_thinking mode for multi-turn agentic loops, Anthropic-compatible endpoint for Claude Code/Cline. $0.95/$4.00 per M tokens."
content_type: "Builder's Log"
categories: ["Models", "AI Infrastructure", "Open Source"]
tags: ["kimi", "kimi-k2-7", "moonshot-ai", "open-source", "mcpmark", "coding-agent", "tool-use", "anthropic-compatible", "builder-guide", "june-2026", "vllm", "mcp"]
---

Moonshot AI released Kimi K2.7 Code on June 12, 2026 — the fifth major release in the K2 line in under a year. It is a coding-focused upgrade to K2.6 with two headline changes: it beats Claude Opus 4.8 on MCPMark (the MCP tool-calling benchmark), and it uses 30% fewer thinking tokens than K2.6 while scoring higher on every coding benchmark Moonshot tracks. It also introduces an Anthropic-compatible API endpoint, which means K2.7 Code can run inside Claude Code, Cline, and RooCode without modification.

The base specs are the same as K2.6: 1 trillion parameters, 32 billion active per token, 256K context, Modified MIT license. Part of the **[Builder's Log](/builders-log/)**.

---

## What Changed from K2.6

K2.7 is not a new architecture — it is a refined fine-tune of K2.6 with a specific target: agentic tool use. Moonshot describes it as "building upon K2.6 to strengthen end-to-end task completion across complex software engineering workflows while improving token efficiency." That is narrow scope by design.

**What is new:**

| Change | K2.6 | K2.7 Code |
|---|---|---|
| Thinking token usage | Baseline | ~30% lower |
| MCPMark score | 72.8% | **81.1%** |
| Kimi Code Bench v2 | 50.9 | **62.0** (+21.8%) |
| Program Bench | Baseline | +11.0% |
| MLS Bench Lite | Baseline | +31.5% |
| preserve_thinking mode | Not available | Available |
| Anthropic-compatible API | Not available | Available |

**What did not change:** architecture (1T MoE, 32B active, 384 experts, MLA), context window (256K), output limit (66K tokens), pricing ($0.95/$4.00 per M tokens), native INT4 quantization, HuggingFace weights under Modified MIT.

---

## Benchmark Position

### MCPMark — the headline number

MCPMark tests how well a model invokes tools via the Model Context Protocol: multi-step tool calls, correctly structured payloads, recovery from partial failures, and sustained accuracy across a long tool-use session. It is the benchmark most directly predictive of performance in the agentic loops builders actually run.

**MCPMark Verified scores (June 2026):**

| Model | MCPMark | Type |
|---|---|---|
| **Kimi K2.7 Code** | **81.1%** | Open-weight |
| Claude Opus 4.8 | 76.4% | Proprietary |
| Kimi K2.6 | 72.8% | Open-weight |

K2.7 Code's 4.7-point margin over Claude Opus 4.8 on MCPMark is not noise. Anthropic's flagship proprietary model is the current standard for agentic coding quality; K2.7 beating it on the tool-use-specific benchmark while costing roughly 10x less per million input tokens is a real signal.

**Caveat:** MCPMark performance does not directly predict SWE-Bench Verified. On SWE-Bench Verified, K2.6 scored 80.2%; K2.7-specific SWE-Bench numbers are not yet published by independent evaluators. Expect results in the same range until an independent run lands.

### Coding benchmarks

Moonshot's internal benchmarks show larger gains:

- **Kimi Code Bench v2**: 50.9 → 62.0, a 21.8% absolute improvement. This benchmark measures full agentic software engineering sessions — plan → implement → test → debug cycles — on real repositories.
- **Program Bench**: +11.0% vs K2.6 on structured programming tasks.
- **MLS Bench Lite**: +31.5%, which covers multi-language synthesis tasks.

These are Moonshot's own benchmarks, not third-party evaluations. Treat them as directional rather than definitive, but the MCPMark result is third-party and replicable.

---

## Thinking Tokens and preserve_thinking Mode

K2.6 uses extended thinking for hard multi-step problems, but its thinking-token budget was not well-calibrated for agentic loops — it frequently over-reasoned on tool-call planning steps that did not need deep reasoning. K2.7 corrects this:

**30% fewer thinking tokens** means a 100K-token agentic session that previously consumed 12K tokens in thinking overhead now consumes ~8K. For high-volume coding pipelines running thousands of sessions per day, this is a real cost reduction without any capability regression on the tasks where thinking matters.

**preserve_thinking mode** is a new K2.7 feature that retains the model's full reasoning content across multi-turn interactions. In practice: when your agent calls a tool, gets a result, and calls another tool in the next turn, K2.7 preserves the reasoning chain from the prior turn rather than re-deriving context from scratch. Moonshot says this "enhances performance in coding agent scenarios" — the mechanism is that the model does not pay the startup cost of re-establishing intent on each turn of a long session.

To activate preserve_thinking in the API:

```python
response = client.chat.completions.create(
    model="kimi-k2.7-code",
    messages=[...],
    extra_body={
        "thinking": {
            "type": "enabled",
            "preserve": True        # new in K2.7
        }
    }
)
```

In non-thinking sessions, preserve_thinking has no effect. It is only relevant when thinking mode is enabled.

---

## API Setup

### OpenAI-compatible endpoint

K2.7 Code is available on the same Moonshot API platform as K2.6, with the new model ID:

```
Base URL:  https://api.moonshot.ai/v1
Model ID:  kimi-k2.7-code
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_MOONSHOT_API_KEY",
    base_url="https://api.moonshot.ai/v1"
)

response = client.chat.completions.create(
    model="kimi-k2.7-code",
    messages=[
        {"role": "user", "content": "Review this PR diff and list the security concerns."}
    ]
)
```

Tool calling uses the OpenAI format (`tools`, `tool_choice`, `tool_calls`). No schema changes from K2.6 — only the model string changes.

### Anthropic-compatible endpoint (new in K2.7)

K2.7 Code exposes a second endpoint that speaks the Anthropic Messages API spec. Claude Code, Cline, and RooCode all communicate over this spec, which means you can point them at K2.7 with three environment variables:

```bash
# Linux / macOS
export ANTHROPIC_BASE_URL="https://api.moonshot.ai/anthropic"
export ANTHROPIC_API_KEY="YOUR_MOONSHOT_API_KEY"
export ANTHROPIC_MODEL="kimi-k2.7-code"
```

```powershell
# Windows PowerShell
$env:ANTHROPIC_BASE_URL = "https://api.moonshot.ai/anthropic"
$env:ANTHROPIC_API_KEY = "YOUR_MOONSHOT_API_KEY"
$env:ANTHROPIC_MODEL = "kimi-k2.7-code"
```

After setting these, launch Claude Code normally. It sends its standard payload — system prompts, conversation history, tool definitions — to Moonshot's endpoint, and K2.7 processes and returns responses that Claude Code reads as native Anthropic responses. File editing, bash execution, codebase analysis, sub-agent spawning all work without modification.

**One known limitation:** extended thinking tokens are billed at K2.7's output-token rate ($4.00/M), same as before. The 30% efficiency gain applies to how many reasoning tokens the model generates, not to how they are priced.

---

## Self-Hosting

Weights are on Hugging Face:

```
moonshotai/Kimi-K2.7-Code
```

Serving stacks supported by Moonshot: **vLLM**, **SGLang**, **KTransformers**. The native INT4 quantization ships with the weights.

**Minimum hardware (from K2.6, applicable to K2.7):**
- INT4 / reduced context: 4 × H100 80GB
- Full 256K context: 8 × H100

K2.7 and K2.6 share the same base architecture (same MLA + SwiGLU MoE design). If you have K2.6 deployment configs, they carry forward — change the weights path and serve.

---

## Pricing

Pricing is unchanged from K2.6:

| Tier | Input | Output | Cached input |
|---|---|---|---|
| K2.7 Code | $0.95/M | $4.00/M | $0.16/M |
| Claude Fable 5 | $10.00/M | $50.00/M | — |
| Claude Opus 4.8 | $15.00/M | $75.00/M | — |

At the same $0.95/$4.00 price point, the 30% thinking-token reduction means K2.7 is effectively ~6–8% cheaper than K2.6 on thinking-heavy sessions, with no input/output rate change.

**Cost comparison, 50K-token agentic session:**

| Model | Input (50K) | Output (5K) |
|---|---|---|
| Claude Opus 4.8 | $0.75 | $0.38 |
| Claude Fable 5 | $0.50 | $0.25 |
| Kimi K2.7 Code | $0.048 | $0.020 |
| K2.7 cached input | $0.008 | $0.020 |

The 10–15x cost gap over Anthropic's flagships is not a rounding error. For high-volume pipelines, it changes the unit economics of what is viable to automate.

---

## K2.7 vs K2.6: When to Upgrade

K2.7 Code is a coding-only model — it drops K2.6's multimodal capabilities (image and video input are not supported). If your workload includes vision tasks, stay on K2.6.

For coding-focused workloads:

| Scenario | Use |
|---|---|
| Running MCP tool-calling pipelines | K2.7 Code — MCPMark leader |
| High-volume agentic coding at scale | K2.7 Code — 30% less thinking spend |
| Claude Code / Cline drop-in replacement | K2.7 Code — Anthropic-compatible endpoint |
| Multi-turn coding sessions needing reasoning chain continuity | K2.7 Code — preserve_thinking mode |
| Image/video input in agentic loops | K2.6 — K2.7 is text-only |
| General reasoning, non-coding tasks | K2.6 or Claude Fable 5 |

---

## Compliance Notes

K2.7 Code is developed and operated by Moonshot AI, a Beijing-based company. The same compliance considerations from K2.6 apply:

- **Kimi API endpoint**: routes through Moonshot's China infrastructure. Not suitable for EU personal data, US government data, or regulated data under data-residency requirements.
- **Self-hosted path**: resolves data-residency concerns entirely — weights are under Modified MIT, no egress.
- **US government / defense contractors**: check your approved vendor list before deploying via API.

---

## Builder Checklist

- [ ] Update model string from `moonshot-v1-k2-6` → `kimi-k2.7-code` (OpenAI endpoint)
- [ ] Set `ANTHROPIC_BASE_URL=https://api.moonshot.ai/anthropic` and `ANTHROPIC_MODEL=kimi-k2.7-code` to run K2.7 inside Claude Code or Cline
- [ ] Enable `"preserve": true` in thinking config for multi-turn agentic sessions
- [ ] Benchmark your pipeline's MCPMark-style tool calls — K2.7's 81.1% vs K2.6's 72.8% should show up in real-world tool-call reliability
- [ ] If you use image/video input anywhere in your pipeline, keep those tasks on K2.6 — K2.7 is text-only
- [ ] Run a cost comparison on your average session's thinking-token ratio to size the 30% efficiency gain in your actual workload

---

**Quick reference:**

- HuggingFace: `moonshotai/Kimi-K2.7-Code`
- API (OpenAI-compatible): `https://api.moonshot.ai/v1`, model `kimi-k2.7-code`
- API (Anthropic-compatible): `https://api.moonshot.ai/anthropic`
- Pricing: $0.95 input / $4.00 output / $0.16 cached input (per million tokens)
- Context: 256K tokens, 66K max output
- MCPMark: 81.1% (vs Claude Opus 4.8 at 76.4%)
- License: Modified MIT (attribution above 100M MAU or $20M/month revenue)
- Released: June 12, 2026
