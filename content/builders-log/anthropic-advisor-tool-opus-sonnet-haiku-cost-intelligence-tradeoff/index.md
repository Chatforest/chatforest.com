---
title: "Anthropic's Advisor Tool: Opus-Level Intelligence at Sonnet Prices"
date: 2026-06-01
description: "Anthropic's advisor_20260301 API tool (April 2026 beta) lets a cheap executor model consult Opus only when it hits a reasoning wall. Haiku + Opus advisor scored 41.2% on BrowseComp vs. 19.7% solo — for 85% less than Sonnet alone. Implementation guide and when to use it."
tags: ["anthropic", "claude", "api", "agents", "cost-optimization", "opus", "sonnet", "haiku", "architecture"]
draft: false
---

Anthropic shipped a new server-side tool type on April 9, 2026: `advisor_20260301`. It inverts the typical multi-model architecture. Instead of a large orchestrator model delegating to smaller workers, a cheap executor model runs the entire workflow and consults Opus only when it hits a decision it cannot reasonably resolve alone.

The benchmark results are the clearest way to understand what this changes. Haiku running alone on BrowseComp — a benchmark measuring complex web research and information synthesis — scored 19.7%. Haiku with an Opus advisor scored 41.2%. Cost per task: 85% less than running Sonnet alone. On SWE-bench Multilingual, Sonnet with an Opus advisor outperformed Sonnet alone by 2.7 percentage points while reducing cost per agentic task by 11.9%.

Those aren't marginal improvements from prompt tweaks. They're structural — the result of Opus seeing the full context at exactly the moments where reasoning quality matters.

## How It Works

The advisor tool is a tool type, not a model parameter. You add it to your tools array alongside function tools or MCP connectors. The executor model treats it like any other tool: it decides when to call it, not you.

When the executor invokes the advisor, Anthropic's infrastructure transparently routes the full shared context to Opus. Opus returns a concise strategic response — typically 400 to 700 tokens. The executor resumes with that guidance and continues toward the final output. One API call, one billing event, no separate context window to manage, no orchestration layer to build.

The executor is the driver. It reads tool results, iterates toward a solution, and generates final output. Only when it hits a reasoning wall — a decision with too many unknowns, a branch point with unclear tradeoffs, a situation where getting it wrong is expensive — does it consult Opus.

Opus as an advisor produces fewer tokens but higher-leverage tokens. The inefficiency in single-model agentic runs is typically not the final output — it's the wasted iterations before the model finds the right approach. Sonnet without an advisor tends to make more attempts, more incorrect tool calls, more iterations. The advisor short-circuits that.

## Implementation

Two requirements: a beta header and a tool entry.

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    betas=["advisor-tool-2026-03-01"],
    tools=[
        {
            "type": "advisor_20260301",
            "name": "advisor",
            "model": "claude-opus-4-8",
        },
        # your other tools here
    ],
    messages=[{"role": "user", "content": your_task}]
)
```

The TypeScript SDK follows the same pattern: add `"advisor-tool-2026-03-01"` to the `betas` array and include the advisor tool definition in your `tools` array.

Two optional parameters worth knowing:

- **`max_uses`**: caps how many times the executor can invoke the advisor per request. Useful for cost predictability on long agentic runs.
- **Separate usage tracking**: advisor tokens are reported separately in the usage block — `advisor_input_tokens` and `advisor_output_tokens`. You can track exactly what each model tier is consuming without guessing.

When handling the response, advisor tool results flow back through the normal content array. Include the full response content — including any `advisor_tool_result` blocks — in subsequent turns as you would with any tool result.

## When to Use It

The advisor tool adds the most value in multi-step agentic workflows with real decision points. That means:

- **Coding agents**: bug triage, refactoring decisions, security audit review
- **Research pipelines**: multi-source synthesis where early misjudgments compound
- **Computer-use workflows**: navigation decisions on unfamiliar interfaces
- **CI pipelines**: automated code review with escalation for ambiguous cases

Skip it for:

- **Single-turn queries**: the advisor adds latency for tasks where one pass is sufficient
- **Trivial or fully deterministic tasks**: you don't need Opus to format a JSON payload
- **Latency-critical paths**: advisor consultation adds round-trip overhead

The pattern fits any situation where you want the model to run autonomously most of the time but escalate to better judgment at specific inflection points. You're not choosing between Opus and Sonnet — you're getting Sonnet's speed and throughput with Opus on call for the decisions that matter.

## How This Compares to Dynamic Workflows

Anthropic shipped two distinct architectural primitives in spring 2026, and they address different problems.

**Dynamic Workflows** (shipped with Opus 4.8, May 28) is about parallelism. The model decides how to decompose a task into subagents — potentially hundreds of them — running in parallel, with an adversarial verification pass before returning results. It's for tasks that are genuinely parallel in structure and where getting the answer right matters more than cost.

**The Advisor Tool** is about escalation. One executor, one advisor, consulted only when needed. It's for tasks that are inherently sequential — where the executor needs to run a workflow from start to finish but benefits from access to better judgment at key decision points.

The two patterns aren't mutually exclusive. A Dynamic Workflows session could have individual subagents using the advisor tool for complex decisions within their scope. But the default choice is simpler: if you need parallelism, Dynamic Workflows. If you need smarter sequential reasoning at lower cost, the advisor tool.

## The Cost Model

Pricing for the advisor tool follows standard per-token rates for each model tier. The executor (Sonnet or Haiku) runs at its normal price. Advisor calls (Opus) are billed at Opus rates, but only for the tokens actually generated — typically 400 to 700 per consultation, not per full output.

The cost ceiling matters. If you're currently running Opus end-to-end on agentic tasks because you need the reasoning quality, the advisor tool is likely to reduce your bill significantly. If you're running Sonnet and satisfied with the quality but want better results, adding the advisor produces measurable uplift at similar or lower cost. If you're running Haiku on research-intensive tasks and hitting quality walls, the Haiku + Opus advisor combination delivers the biggest relative gain.

The primary risk is unbounded advisor calls on a long agentic run with many decision points. Set `max_uses` explicitly until you've profiled how often your specific workflow actually invokes the advisor. Once you have that baseline, you can relax the cap or adjust it per task type.

## What to Try First

Start with a task you currently run on Sonnet that has multiple decision points and a clear quality target you can measure against. Add the advisor tool with `max_uses` set to something conservative — 3 to 5 calls per run. Compare output quality and cost against your Sonnet baseline.

If the advisor is being invoked at every step, the executor model is probably under-specified for the task. Better system prompt framing of what the executor should handle independently will reduce unnecessary advisor calls.

If you're using the advisor tool in production or experimenting with configurations, Anthropic's feedback mechanism on the [advisor tool docs page](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool) is active during the beta. The beta designation means the API surface may change — pin your `betas` header to `advisor-tool-2026-03-01` and check the release notes when you upgrade.
