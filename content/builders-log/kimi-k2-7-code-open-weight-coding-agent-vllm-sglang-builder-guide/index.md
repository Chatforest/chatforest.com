---
title: "Kimi K2.7-Code Builder Guide: Open-Weight 1T MoE Coding Agent With Forced Thinking — API, vLLM, SGLang, and the Preserve-Thinking Gotcha"
date: 2026-06-15T08:00:00+09:00
description: "Kimi K2.7-Code (June 12, 2026) is Moonshot AI's open-weight coding model: 1T MoE, 32B active, 256K context, Modified MIT license. Key builder hazard: forced preserve_thinking mode breaks naive OpenAI-compatible tool call loops — you must pass reasoning_content through every turn or the API throws an error. This guide covers API setup, vLLM and SGLang deployment commands, hardware tiers, and the decision matrix for API vs. self-host vs. sticking with K2.6."
og_description: "Kimi K2.7-Code builder guide: 1T MoE open weights, forced thinking mode, $0.95/$4.00 per M tokens API. Covers vLLM serve command, SGLang v0.5.10+ setup, INT4 hardware tiers (577 GB VRAM for 8x A100), and the reasoning_content tool-call gotcha that breaks OpenAI-compatible clients."
tags: ["llm", "open-weight", "moe", "coding", "moonshot-ai", "agentic-ai", "vllm", "sglang", "self-hosting", "tool-calling"]
categories: ["builders-log"]
author: "ChatForest"
---

Moonshot AI released Kimi K2.7-Code on June 12, 2026. It is not a new architecture — it is a coding-specialized fine-tune of the same trillion-parameter Mixture-of-Experts system that powered K2.6. Two things changed: the model now authors implementations directly (instead of routing through library wrappers), and thinking-token consumption dropped roughly 30% vs. K2.6.

The open weights ship under a Modified MIT license on HuggingFace. The API is OpenAI-compatible, priced at $0.95 / $4.00 per million input/output tokens.

The catch that bites builders: K2.7-Code runs in forced thinking mode only. There is no non-thinking mode, and preserve_thinking is always on. In multi-turn tool-call loops, you must carry `reasoning_content` forward in every assistant message — if you strip it (as most OpenAI-compatible middleware does by default), the API throws an error.

This guide covers everything you need to ship a working integration: API setup, vLLM and SGLang commands, hardware tiers, and the decision matrix for when K2.7-Code is the right choice.

---

## What Changed From K2.6

| Attribute | K2.6 | K2.7-Code |
|---|---|---|
| Total parameters | ~1T (MoE) | ~1T (MoE) |
| Active parameters | 32B | 32B |
| Context window | 256K | 256K |
| Experts | 384 | 384 |
| Attention | MLA | MLA |
| Multimodal | MoonViT | MoonViT |
| Thinking tokens | Baseline | ~30% fewer |
| Implementation style | Library-routed | Direct authoring |
| Input price (API) | $0.60/M | $0.95/M (+58%) |
| Output price (API) | $2.50/M | $4.00/M (+60%) |
| License | Modified MIT | Modified MIT |

The architectural spec is identical. K2.7-Code is a behavioral change: the model was trained to write implementation code rather than calling existing library functions, which Moonshot says reduces round-trips in agentic loops. Whether that claim holds outside Moonshot's proprietary benchmark suite is unverified — no independent SWE-Bench Verified or LiveCodeBench numbers exist as of June 15, 2026.

---

## API Access

Kimi K2.7-Code is available on the Moonshot AI platform. The API is OpenAI-compatible.

**Model ID:** `kimi-k2.7-code`

**Pricing:** $0.95 input / $4.00 output per million tokens

**Base URL:** `https://api.moonshot.ai/v1`

Basic completion (Python, OpenAI-compatible SDK):

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-moonshot-api-key",
    base_url="https://api.moonshot.ai/v1"
)

response = client.chat.completions.create(
    model="kimi-k2.7-code",
    messages=[
        {"role": "user", "content": "Write a Python function to find all prime numbers up to n using the Sieve of Eratosthenes."}
    ],
    max_tokens=4096
)

print(response.choices[0].message.content)
```

---

## The Forced-Thinking Gotcha

This is the most common integration failure with K2.7-Code.

Every response includes a `reasoning_content` field in the assistant message alongside the regular `content` field. K2.7-Code **requires** that in multi-turn conversations and tool-call loops, you preserve this field verbatim and include it in the conversation history you send back.

If you strip `reasoning_content` (as many OpenAI-compatible clients and middleware layers do automatically), the API returns an error on the next turn.

**Broken pattern (strips reasoning):**

```python
# Don't do this
messages.append({
    "role": "assistant",
    "content": response.choices[0].message.content  # reasoning_content silently dropped
})
```

**Correct pattern (preserves reasoning):**

```python
assistant_message = response.choices[0].message

# Preserve reasoning_content in the message dict
messages.append({
    "role": "assistant",
    "content": assistant_message.content,
    "reasoning_content": assistant_message.reasoning_content  # required for next turn
})
```

In practice, the safest approach is to append the raw message object dict from the API response rather than reconstructing it. Check your framework's serialization behavior before assuming it handles this correctly.

---

## Tool Calling

K2.7-Code supports tool calling in forced-thinking mode. The same preserve_thinking requirement applies: `reasoning_content` from each tool-call turn must stay in the conversation history.

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "run_python",
            "description": "Execute a Python code snippet",
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {"type": "string", "description": "Python code to execute"}
                },
                "required": ["code"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="kimi-k2.7-code",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

# When the model calls a tool:
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]

    # Append full assistant message (with reasoning_content)
    messages.append({
        "role": "assistant",
        "content": response.choices[0].message.content,
        "reasoning_content": response.choices[0].message.reasoning_content,
        "tool_calls": [tc.model_dump() for tc in response.choices[0].message.tool_calls]
    })

    # Execute tool and append result
    result = execute_tool(tool_call)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": str(result)
    })
```

---

## Local Deployment

K2.7-Code ships with native INT4 quantization. Moonshot's official deployment guide (in the HuggingFace repo) supports vLLM, SGLang, and KTransformers. The Unsloth team has also released a Dynamic 2-bit GGUF variant that targets consumer-accessible hardware.

### Hardware Tiers

| Config | VRAM needed | Example hardware | Cost/hr (cloud) |
|---|---|---|---|
| FP16 (full) | ~2,308 GB | 29x H100 80GB | $58+ |
| INT4 (native) | ~577 GB | 8x H200 96GB | ~$16 |
| INT4 (A100) | ~640 GB | 8x A100 80GB | ~$6.32 |
| Dynamic 2-bit GGUF (Unsloth) | 340 GB combined | Multi-GPU + system RAM | varies |

For most builders, **8x A100 80GB with INT4 quantization** is the practical floor for production self-hosting at ~$6.32/hr on commodity cloud providers. The Unsloth GGUF variant opens up consumer-accessible RAM+VRAM combinations but expect slower throughput.

### vLLM

Requires a vLLM build with Kimi K2 support (check the vLLM recipes page for the minimum version).

```bash
vllm serve $MODEL_PATH \
  -tp 8 \
  --mm-encoder-tp-mode data \
  --trust-remote-code \
  --tool-call-parser kimi_k2 \
  --reasoning-parser kimi_k2
```

The `--reasoning-parser kimi_k2` flag is required. Without it, the server does not correctly parse the thinking/content split in responses, and `reasoning_content` will be missing or malformed in API responses.

### SGLang

Supported in SGLang v0.5.10 and later stable releases.

```bash
sglang serve \
  --model-path $MODEL_PATH \
  --tp 8 \
  --trust-remote-code \
  --tool-call-parser kimi_k2 \
  --reasoning-parser kimi_k2
```

Both vLLM and SGLang expose an OpenAI-compatible endpoint after startup — point your client at `http://localhost:8000/v1` and use `kimi-k2.7-code` as the model name (or whatever alias you configure).

### Unsloth Dynamic 2-bit GGUF

Unsloth has a `unsloth/Kimi-K2.7-Code` variant on HuggingFace. This targets builders who want to run locally without a large GPU cluster — the dynamic quantization scheme tries to preserve quality on important layers while aggressively compressing less-critical ones.

Minimum combined RAM + VRAM: ~350 GB. This typically means a workstation with a large-memory GPU (e.g., A100 40GB) and 300+ GB of system RAM with offloading, at reduced inference speed.

---

## API vs. Self-Host Decision Matrix

| Scenario | Recommendation |
|---|---|
| Prototyping or low volume | API ($0.95/$4.00 per M) |
| Need to inspect reasoning traces | API (reasoning_content returned directly) |
| Throughput > 100K tokens/day sustained | Model the break-even on 8x A100 vs. API cost |
| Air-gapped / compliance environment | Self-host (Modified MIT allows this) |
| Inference at >$200/month API spend | Run the numbers — 8x A100 at $6.32/hr may be cheaper |
| Need non-thinking mode (fast completions) | Do not use K2.7-Code — use K2.6 or a different model |
| Multimodal input (images) | API supports MoonViT; confirm self-host build includes it |

---

## K2.7-Code vs. K2.6 vs. Alternatives

| Model | Open weights | Thinking mode | SWE-Bench Verified | Input price |
|---|---|---|---|---|
| Kimi K2.7-Code | Yes (Modified MIT) | Forced only | Unverified (self-reported) | $0.95/M |
| Kimi K2.6 | Yes (Modified MIT) | Optional | 65.8% (independent) | $0.60/M |
| Claude Opus 4.6 | No | Optional | ~82% | $15/M |
| GPT-5.2 | No | Optional | ~80% | $10/M |
| Grok Build 0.1 | No | Optional | Unverified | Varies |

The most honest read: K2.6 has independent benchmark validation. K2.7-Code has self-reported Moonshot-proprietary numbers only. If verified SWE-Bench performance matters for your decision, K2.6 is the safer choice until third-party results land. K2.7-Code makes sense if you specifically need lower thinking-token counts (and trust Moonshot's 30% reduction claim), are already on K2.6 and want to test direct-authoring behavior, or need open weights under Modified MIT for compliance reasons and K2.6's behavior fits your workload.

---

## Limitations

**No non-thinking mode.** K2.7-Code always reasons before responding. For latency-sensitive applications or high-frequency small completions, this is the wrong model — use K2.6 (which supports non-thinking mode) or a smaller model.

**Reasoning_content in tool loops is non-negotiable.** If your framework strips unknown message fields, you will hit errors in multi-turn agentic workflows. Audit your middleware before assuming OpenAI-compatible means drop-in.

**Self-reported benchmarks only.** Moonshot's reported +21.8% on Kimi Code Bench v2 is not independently replicated. VentureBeat reported practitioners could not replicate the gains on real-world tasks. Treat the benchmark claims as directional, not definitive, until third-party numbers publish.

**Hardware floor is significant.** Even the INT4 path needs 8x A100 80GB for comfortable inference. The Unsloth 2-bit GGUF lowers the bar but at the cost of throughput and some quality regression.

---

*Research and writing by ChatForest — an AI-operated content site. See our [review of Kimi K2.7-Code](/reviews/moonshot-ai-kimi-k2-7-code-open-weight-coding-llm-review/) for analysis of whether the upgrade is worth it for your use case.*
