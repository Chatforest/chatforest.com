---
title: "Qwen3.7-Plus: The Multimodal Half of the Qwen Stack Builders Are Missing"
date: 2026-06-05
description: "Qwen3.7-Plus launched June 2 with image and video input, 79.0 on ScreenSpot Pro (best in class for GUI grounding), and pricing at $0.40/$1.60 per million tokens — 6x cheaper than the text-only Max. Here is what it is, what it is not, and the routing pattern that makes both models work."
og_description: "Qwen3.7-Plus (June 2, 2026): $0.40/$1.60/M tokens. ScreenSpot Pro 79.0 — beats GPT-5.4 at 67.4 and Claude Opus-4.6 at 49.5. 1M context. Multimodal: text + image + video. OpenAI-compatible API via Bailian/OpenRouter. Proprietary (no open weights). Builder guide to what it is, how it differs from Qwen3.7-Max, and when to route traffic through each."
content_type: "Builder's Log"
categories: ["AI Models", "Agentic AI", "AI Infrastructure"]
tags: ["alibaba", "qwen", "multimodal", "gui-agent", "vision", "long-context", "agent-models", "openrouter", "chinese-ai", "builders-log"]
---

Qwen3.7-Max launched May 19 as a text-only reasoning model — and [we reviewed it then](/reviews/alibaba-qwen3-7-max-agentic-reasoning-model-review/). If you missed it: it benchmarks competitively with Claude Opus-4.6, supports Anthropic-protocol APIs natively, and costs $2.50/$7.50 per million tokens.

Qwen3.7-Plus launched June 2 and is not the same model at a lower price point. It is a different model with a different job.

---

## What Qwen3.7-Plus Actually Is

Qwen3.7-Plus is a multimodal model: it accepts text, images, and video as input and produces text output. It adds GUI agent grounding — the ability to look at a screenshot and return exact pixel coordinates to interact with. That is a meaningfully different capability from Max, which is text-only.

The pricing reflects the positioning: **$0.40/$1.60 per million input/output tokens**, with $0.08 for cached input reads. That is roughly 6x cheaper than Max on input, 4.7x cheaper on output.

| | Qwen3.7-Max | Qwen3.7-Plus |
|---|---|---|
| Modalities | Text only | Text + image + video |
| Context window | 1M tokens | 1M tokens |
| Max output | 65K tokens | 65K tokens |
| CoT budget | 256K tokens | 256K tokens |
| Input pricing | $2.50/M | $0.40/M |
| Output pricing | $7.50/M | $1.60/M |
| Cached input | $0.50/M | $0.08/M |
| Open weights | No | No |
| Protocol | Anthropic API + OpenAI | OpenAI |
| SWE-Bench Pro | ~61% | ~59% |
| ScreenSpot Pro | Not tested | 79.0 |

---

## The GUI Grounding Benchmark That Matters

The benchmark worth paying attention to is **ScreenSpot Pro**, which tests localized interface understanding: given a screenshot, point to the correct element. This is the core technical challenge behind GUI automation agents.

Qwen3.7-Plus scored **79.0 on ScreenSpot Pro**.

For reference:
- GPT-5.4 (xhigh): 67.4
- Claude Opus-4.6: 49.5

A 12-point lead over GPT-5.4 on GUI grounding is not incremental. It places Qwen3.7-Plus at the top of the non-Western multimodal field for this specific capability. The practical implication: if you are building agents that navigate application UIs, web browsers, or desktop interfaces, the Plus model's perception layer is stronger than what OpenAI or Anthropic currently offers at any price point.

---

## Architecture: Early Fusion Training

Unlike some multimodal models that bolt vision on top of a text-first architecture, Qwen3.7-Plus was trained with early fusion: vision and language tokens are processed together from the first layer, not integrated at a late stage. Alibaba reports the model was trained on trillions of multimodal tokens with this approach.

The practical effect: the model does not just describe images — it reasons about them with the same chain-of-thought depth as the text-only Max. The CoT budget of up to 256K tokens applies to visual reasoning tasks, not just text problems.

The 1M context window extends to multimodal inputs. That means a long document with embedded images, a video with interleaved screenshots, or a session of GUI interactions over time — all manageable within a single context.

---

## Where Max Still Wins

Plus is not a straight upgrade over Max. On text-only reasoning:

- **SWE-Bench Pro**: Max edges Plus by roughly 2 points
- **Throughput**: Max is approximately 10% faster on text-only requests
- **Protocol**: Max supports both OpenAI-compatible and Anthropic API protocol. Plus is OpenAI-compatible only — it does not work as a drop-in replacement inside Claude Code or Anthropic SDK toolchains without an adapter

For purely textual coding agents, document processing, or MCP tool orchestration, Max remains the stronger choice.

---

## Access

**Alibaba Cloud Model Studio (Bailian)**

The production endpoint for international users is:

```
base_url: https://dashscope.aliyuncs.com/compatible-mode/v1
model: qwen3.7-plus
```

Standard OpenAI-compatible chat completions format. You will need an Alibaba Cloud account and API key.

**OpenRouter**

Available as `qwen/qwen3.7-plus`. OpenRouter's routing layer handles key management and provides a unified billing surface if you are already routing multiple models through OpenRouter.

---

## The Trust Consideration

Both Qwen3.7-Max and Qwen3.7-Plus are proprietary, API-only models from Alibaba. Neither has open weights.

This is a change from the Qwen 3.6 series, which shipped under Apache 2.0. The 3.7 tier is managed APIs only. The practical consequence: you cannot run these on your own infrastructure, inspect their behavior at the weight level, or verify training data claims independently.

For builders evaluating Chinese AI infrastructure, the same considerations that applied to Max apply here: data routing goes through Alibaba Cloud, the model's behavior is not independently auditable, and the benchmarks are self-reported with limited third-party replication at this stage.

Artificial Analysis lists Qwen3.7-Plus at an Intelligence Index score of 53, placing it above average among similarly priced models (median for the price tier: 23). That is a credible third-party data point, though it reflects aggregate performance, not ScreenSpot Pro specifically.

---

## The Routing Pattern

The practical builder architecture for June 2026: route between Max and Plus based on task type.

```
# Text input → Qwen3.7-Max
# Image/video input, GUI grounding → Qwen3.7-Plus

def route_qwen(task):
    if task.has_visual_input or task.requires_gui_grounding:
        return "qwen/qwen3.7-plus"   # $0.40/$1.60/M
    else:
        return "qwen/qwen3.7-max"    # $2.50/$7.50/M
```

For mixed agentic loops — where an agent might be given a screenshot to interpret and then asked to write code based on what it sees — one pattern is to call Plus for the visual interpretation step and Max for the subsequent reasoning and code generation step. The cheaper visual call does not need Max's text-reasoning horsepower; the code generation step does not need Plus's vision capability.

At current pricing, a 50/50 mix of visual perception calls (Plus) and code generation calls (Max) costs roughly $1.45/$4.55 per million tokens blended — a meaningful reduction from using Max for everything.

---

## What This Means for Builders

Qwen3.7-Plus is not a model to evaluate in isolation. Its value depends on whether you are building anything that involves visual inputs: web scraping that requires element identification, desktop automation, document pipelines with embedded figures, or UI testing.

If your agent stack is text-only, Max remains the relevant Qwen model.

If you are building GUI agents or multimodal pipelines, Plus's ScreenSpot Pro score is the most compelling capability claim in the current non-Western model market. The pricing makes it practical to use for high-volume visual perception steps without routing those calls through GPT-5.4 or Claude.

The caveat that carries: self-reported benchmarks, proprietary weights, Alibaba Cloud infrastructure. Evaluate in your environment before committing.

---

*Qwen3.7-Plus launched June 2, 2026. Pricing from Alibaba Cloud Model Studio and OpenRouter. Benchmarks from Alibaba's launch materials and Artificial Analysis third-party index. ScreenSpot Pro comparison figures from the model card. This is a research-based summary — we did not test the model directly.*
