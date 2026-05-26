# Gemini 3.5 Flash Is Out. Gemini 3.5 Pro Is Not.

> Google shipped Gemini 3.5 Flash at Google I/O on May 19 — a 1M-context model with strong agentic benchmarks at $1.50/9.00 per million tokens. Gemini 3.5 Pro was delayed to June. Here's what shipped, what was skipped, and what it means for builders evaluating Google's API.


Google I/O ran on May 19, 2026. Builders watching for Gemini 3.5 Pro got something different: Gemini 3.5 Flash. The Pro model was acknowledged, promised, and deferred to June. Flash launched immediately and globally.

Here is what actually shipped, what the benchmarks show, and how to think about where it fits.

## What Is Gemini 3.5 Flash

Gemini 3.5 Flash is Google's mid-tier model in the 3.5 family — positioned above the experimental and Lite variants, below the forthcoming Pro. It is available now in the Gemini API and Google AI Studio, with no waitlist.

Context window: **1 million tokens**. That number is not new for Google — the 1M context window has been a selling point since Gemini 1.5 Pro. What is new is the combination of that window with 3.5-generation reasoning on agentic benchmarks at a Flash-tier price point.

Pricing: **$1.50 per million input tokens, $9.00 per million output tokens**. That makes it comparable in cost to Claude 3.5 Haiku and GPT-5.5 Instant — the mid-range price bracket where most production pipelines live.

## The Benchmark Numbers

Google reported Gemini 3.5 Flash outperforms Gemini 3.1 Pro on coding and agentic tasks. The headline scores from Google's own benchmarks:

- **Terminal-Bench 2.1**: 76.2%
- **MCP Atlas** (agentic tool-use benchmark): 83.6%

For context on Terminal-Bench: GPT-5.5 Instant scores in the high 70s on earlier Terminal-Bench versions, and Claude 3.5 Sonnet sits in the low 70s. Gemini 3.5 Flash's 76.2% on the updated version (2.1) is a credible mid-tier showing — not the top performer in long-horizon terminal tasks, but not trailing either.

Google also reports improvement over Gemini 3.1 Pro specifically on agentic tool-call chains — the MCP Atlas score reflects that. The practical implication: if you were using Gemini 3.1 Pro in an agent pipeline, 3.5 Flash should be a straightforward upgrade, at substantially lower cost.

One caveat worth naming: both benchmark names are Google's own reporting. Independent third-party runs on external benchmarks were not available at launch. That is standard for day-one releases — treat the numbers as directional until the community runs its own evals.

## What Was Not Shipped: Gemini 3.5 Pro

The more interesting story from Google I/O is what did not launch.

Gemini 3.5 Pro was expected to headline the release. Sundar Pichai addressed the gap directly during the keynote: "We are using it internally and we look forward to rolling it out next month." The "next month" is June 2026.

Why the delay matters: Gemini 3.5 Pro is Google's direct competitor to Claude 3.7 Sonnet and GPT-5.5 on frontier reasoning tasks — the tier where serious builders run complex coding agents, multi-step research pipelines, and high-stakes document processing. The Flash model is not a substitute for that use case; it is a different price-performance trade-off.

If you are waiting to evaluate Google's competitive position on frontier tasks, June is the window. The Flash launch today does not tell you how 3.5 Pro will perform.

## The Wider I/O Context

Google I/O 2026 was heavier on infrastructure signals than model capabilities.

**Google Gemini Antigravity** was introduced as an "agent-first" development platform — described as moving beyond code-generation assistance toward agents that take action inside enterprise workflows. No public API at launch; the developer program is invite-only.

**TPU 8t** was announced for large-scale pretraining. Google disclosed that its model APIs are now processing approximately 19 billion tokens per minute across all Gemini products, and that more than 375 Google Cloud customers each processed over 1 trillion tokens in the past 12 months. These are capacity announcements aimed at enterprise buyers, but they also signal Google is running at scale — the API is not a research preview.

**Gemini Omni** also launched — a multimodal model capable of any-to-any generation including video output. It is a different product category from the Flash/Pro reasoning tier and aimed at creative and media production use cases rather than developer pipelines.

## How It Stacks Up

A rough positioning comparison for the mid-tier ($1-2/M input) bracket:

| Model | Input Price | Context | Notable |
|---|---|---|---|
| Gemini 3.5 Flash | $1.50/M | 1M tokens | Strong agentic benchmarks at launch |
| Claude 3.5 Haiku | ~$0.80/M | 200K tokens | Lower cost, shorter context |
| GPT-5.5 Instant | ~$1.25/M | 128K tokens | Fast default; strong terminal tasks |

Gemini 3.5 Flash wins on raw context window by a significant margin. The 1M-token window is practically useful if you are processing large codebases, long documents, or extended conversation histories in a single call — tasks where the alternatives require chunking or retrieval.

The pricing is not the cheapest in the tier. But it is not expensive either, and the context-window advantage partly justifies the premium over Claude 3.5 Haiku.

## What Builders Should Do Now

**If you are already using Gemini 3.1 Pro** in a production pipeline, it is worth running a direct A/B evaluation of Gemini 3.5 Flash on your actual tasks. The reported improvements on coding and agentic tasks are plausible — but "outperforms on agentic benchmarks" is a Google claim on Google's benchmarks. Run it on your workload before committing.

**If you are evaluating Google's API for the first time**, start with the Flash tier. It is available now, the pricing is reasonable, and the 1M context window makes it the easiest entry point for testing large-context use cases. Wait for 3.5 Pro before drawing conclusions about Google's frontier tier.

**If you are building multi-step agents with tool calls**, the MCP Atlas result is worth paying attention to. Tool-use reliability has historically been a weak point in the Gemini family. If 3.5 Flash has improved there, it materially expands the model's usefulness in agentic architectures.

**Mark June on your calendar.** If Pichai's "next month" holds, Gemini 3.5 Pro will be the first real frontier-tier Gemini release since 3.1 Pro. That is the benchmark that will determine whether Google is competitive on the tasks that matter most — complex reasoning, multi-step coding agents, and high-accuracy document work.

## Bottom Line

Gemini 3.5 Flash is a real release with a useful combination of capabilities: 1M context, mid-range pricing, improved agentic benchmark scores. The fact that Pro was deferred is neither alarming nor a surprise — Google has a track record of releasing the Flash tier ahead of Pro in its Gemini generations.

The story of Google I/O 2026, for builders, is: Google is running at inference scale, has a credible mid-tier model available today, and is promising its frontier competitor to GPT-5.5 and Claude in June. Flash is good enough to test seriously. Pro is the release that will answer the harder question about Google's frontier position.

