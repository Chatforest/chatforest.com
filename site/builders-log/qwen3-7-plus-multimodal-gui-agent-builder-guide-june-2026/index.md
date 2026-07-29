# Qwen3.7-Plus: The Multimodal Half of the Qwen Stack Builders Are Missing

> Qwen3.7-Plus launched June 2 with image and video input, 79.0 on ScreenSpot Pro (ahead of GPT-5.4 and Claude Opus-4.6 on Alibaba's own vendor-run benchmark), and pricing at $0.40/$1.60 per million tokens — 6x cheaper than the text-only Max. Here is what it is, what it is not, and the routing pattern that makes both models work.


Qwen3.7-Max launched May 19 as a text-only reasoning model — and [we reviewed it then](/reviews/alibaba-qwen3-7-max-agentic-reasoning-model-review/). If you missed it: it benchmarks competitively with Claude Opus-4.6, supports Anthropic-protocol APIs natively, and costs $2.50/$7.50 per million tokens.

Qwen3.7-Plus [launched June 2](https://x.com/Alibaba_Qwen/status/2061506641120641494) and is not the same model at a lower price point. It is a different model with a different job.

---

## What Qwen3.7-Plus Actually Is

Qwen3.7-Plus is a multimodal model: it accepts [text, images, and video as input and produces text output](https://www.marktechpost.com/2026/06/02/alibabas-qwen-team-launches-qwen3-7-plus-adding-vision-deep-reasoning-tool-invocation-and-autonomous-iteration-on-the-bailian-platform/). It adds GUI agent grounding — the ability to look at a screenshot and return exact pixel coordinates to interact with. That is a meaningfully different capability from Max, which is text-only.

The pricing reflects the positioning: **[$0.40/$1.60 per million input/output tokens](https://artificialanalysis.ai/models/qwen3-7-plus)**, with cached input reads discounted to roughly [$0.04–$0.08 per million tokens depending on cache type](https://www.cometapi.com/qwen3-7-plus-api-pricing/) (explicit cache hits price lower than implicit ones). That is roughly 6x cheaper than Max on input, 4.7x cheaper on output than [Max's $2.50/$7.50 pricing](/reviews/alibaba-qwen3-7-max-agentic-reasoning-model-review/).

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
| Protocol | Anthropic API + OpenAI | Anthropic API (via [Coding Plan](https://www.alibabacloud.com/help/en/model-studio/claude-code)) + OpenAI |
| SWE-Bench Pro | ~60.6% | ~57.6% |
| ScreenSpot Pro | Not tested | 79.0 |

Sources: pricing and specs from [Artificial Analysis](https://artificialanalysis.ai/models/comparisons/qwen3-7-plus-vs-qwen3-7-max) and [Alibaba Cloud Model Studio Claude Code docs](https://www.alibabacloud.com/help/en/model-studio/claude-code); SWE-Bench Pro figures are third-party-tracked, not an Alibaba-published head-to-head, and should be treated as approximate.

---

## The GUI Grounding Benchmark That Matters

The benchmark worth paying attention to is **ScreenSpot Pro**, which tests localized interface understanding: given a screenshot, point to the correct element. This is the core technical challenge behind GUI automation agents.

Qwen3.7-Plus scored **[79.0 on ScreenSpot Pro](https://venturebeat.com/technology/alibabas-qwen3-7-plus-supports-text-video-and-imagery-inputs-at-low-cost-of-0-4-1-6-per-1m-token-but-its-proprietary)**, a figure Alibaba's own team [reported at launch](https://x.com/Alibaba_Qwen/status/2061506641120641494) and multiple outlets independently repeated.

For reference:
- [GPT-5.4 (xhigh): 67.4](https://mlq.ai/news/alibaba-launches-qwen37-plus-a-multimodal-agent-model-that-sees-screens-and-writes-code/)
- [Claude Opus-4.6: 49.5](https://artificialanalysis.ai/models/comparisons/qwen3-7-plus-vs-claude-opus-4-6-adaptive)

A 12-point lead over GPT-5.4 on GUI grounding is not incremental. The practical implication: if you are building agents that navigate application UIs, web browsers, or desktop interfaces, the Plus model's perception layer benchmarks stronger than what OpenAI or Anthropic currently offer at any price point — on this specific, vendor-run benchmark. Note the caveat that applies to all three numbers: this is Alibaba's own comparison, reportedly run with the competing models' extended-thinking modes off, so treat it as a directional signal rather than a neutral, third-party-verified ranking.

---

## Architecture: What's Actually Confirmed

Alibaba has not published detailed architecture specifics for Qwen3.7-Plus (parameter count, training data composition, and fusion method are undisclosed in the launch materials reviewed for this piece). Qwen's prior generation, Qwen3.5, was documented as using an early-fusion approach — text, image, and video tokens processed jointly from early in pretraining rather than bolted on via adapters — but that claim is specific to Qwen3.5's own [documented training approach](https://trilogyai.substack.com/p/deep-dive-qwen-35-brings-native-multimodality) and has not been confirmed by Alibaba for Qwen3.7-Plus specifically, so it should not be assumed to carry over.

What is confirmed: the model reasons about visual input with chain-of-thought, not just description, and the [CoT budget of up to 256K tokens applies to visual reasoning tasks](https://www.digitalapplied.com/blog/qwen-3-7-plus-alibaba-multimodal-agent-model-2026-release), not just text problems.

The 1M context window extends to multimodal inputs. That means a long document with embedded images, a video with interleaved screenshots, or a session of GUI interactions over time — all manageable within a single context.

---

## Where Max Still Wins

Plus is not a straight upgrade over Max. On text-only reasoning:

- **SWE-Bench Pro**: Max edges Plus by [roughly 3 points (60.6% vs 57.6%, third-party-tracked)](https://artificialanalysis.ai/models/comparisons/qwen3-7-plus-vs-qwen3-7-max)
- **Throughput**: Max is [substantially faster on text-only requests](https://artificialanalysis.ai/models/comparisons/qwen3-7-plus-vs-qwen3-7-max) — roughly 4x higher output tokens/second in third-party benchmarking (202.8 vs 52.7 tokens/sec), consistent with Plus's extra vision-processing overhead
- **Protocol**: Both models can be used with the Anthropic API protocol. Max supports it as its default DashScope interface; Plus reaches it through Alibaba's [Coding Plan / Claude Code integration](https://www.alibabacloud.com/help/en/model-studio/claude-code) rather than as the default DashScope endpoint format (which is OpenAI-compatible)

For purely textual coding agents, document processing, or MCP tool orchestration, Max remains the stronger choice.

---

## Access

**Alibaba Cloud Model Studio (Bailian)**

The production endpoint for international users is:

```
base_url: https://dashscope.aliyuncs.com/compatible-mode/v1
model: qwen3.7-plus
```

Standard OpenAI-compatible chat completions format, per [Alibaba Cloud Model Studio's documentation](https://www.alibabacloud.com/help/en/model-studio/models). You will need an Alibaba Cloud account and API key.

**OpenRouter**

Available as [`qwen/qwen3.7-plus`](https://openrouter.ai/qwen/qwen3.7-plus). OpenRouter's routing layer handles key management and provides a unified billing surface if you are already routing multiple models through OpenRouter. Note OpenRouter's own routed pricing can differ from Alibaba's list price (it has fluctuated toward $0.32/$1.28 per million tokens on some routes) — check current rates before budgeting.

---

## The Trust Consideration

Both Qwen3.7-Max and Qwen3.7-Plus are proprietary, API-only models from Alibaba. Neither has open weights.

This is a change from the [Qwen 3.6 series, which shipped under Apache 2.0](https://github.com/QwenLM/Qwen3.6) (e.g. Qwen3.6-27B, Qwen3.6-35B-A3B). The 3.7 tier is managed APIs only. The practical consequence: you cannot run these on your own infrastructure, inspect their behavior at the weight level, or verify training data claims independently.

For builders evaluating Chinese AI infrastructure, the same considerations that applied to Max apply here: data routing goes through Alibaba Cloud, the model's behavior is not independently auditable, and the benchmarks are self-reported with limited third-party replication at this stage.

[Artificial Analysis lists Qwen3.7-Plus at an Intelligence Index score of 39](https://artificialanalysis.ai/models/qwen3-7-plus), placing it above the median for its price tier (16). That is a credible third-party data point, though it reflects aggregate performance, not ScreenSpot Pro specifically.

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

If you are building GUI agents or multimodal pipelines, Plus's ScreenSpot Pro score is a compelling capability claim, beating GPT-5.4 and Claude Opus-4.6 on Alibaba's own vendor-run comparison. The pricing makes it practical to use for high-volume visual perception steps without routing those calls through GPT-5.4 or Claude.

The caveat that carries: self-reported benchmarks, proprietary weights, Alibaba Cloud infrastructure. Evaluate in your environment before committing.

---

*Qwen3.7-Plus launched June 2, 2026. Pricing from [Alibaba Cloud Model Studio](https://www.alibabacloud.com/help/en/model-studio/models) and [OpenRouter](https://openrouter.ai/qwen/qwen3.7-plus). Benchmarks from [Alibaba's launch announcement](https://x.com/Alibaba_Qwen/status/2061506641120641494), [independent launch coverage](https://venturebeat.com/technology/alibabas-qwen3-7-plus-supports-text-video-and-imagery-inputs-at-low-cost-of-0-4-1-6-per-1m-token-but-its-proprietary), and [Artificial Analysis](https://artificialanalysis.ai/models/qwen3-7-plus)'s third-party index. This is a research-based summary — we did not test the model directly.*

