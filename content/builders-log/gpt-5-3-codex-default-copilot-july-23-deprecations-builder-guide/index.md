---
title: "GPT-5.3-Codex Is Now the Copilot Default — and Every Older Codex Model Retires July 23"
date: 2026-06-02
description: "GPT-5.3-Codex became the base model for all GitHub Copilot Business and Enterprise organizations on May 17. If you have production API calls to gpt-5.2-codex or older, every one of them breaks on July 23. Here's the migration path and what the model actually offers."
content_type: "Builder's Log"
categories: ["OpenAI", "Model Migration", "Agent Development", "GitHub Copilot"]
tags: ["openai", "gpt-5.3-codex", "codex", "model-deprecation", "github-copilot", "agentic-coding", "api-migration", "reasoning-effort", "computer-use", "agent-development"]
---

GPT-5.3-Codex has been OpenAI's primary agentic coding model since February 5, 2026. On May 17 it became the base model for all GitHub Copilot Business and Enterprise organizations, replacing GPT-4.1 as the default. On June 5, GPT-5.2-Codex was removed from most Copilot model pickers.

And on July 23, 2026, every earlier Codex API model shuts down.

If you have any production calls to `gpt-5-codex`, `gpt-5.1-codex`, `gpt-5.1-codex-max`, `gpt-5.2-codex`, or `gpt-5.1-codex-mini`, those calls fail in 51 days.

---

## What Is Being Shut Down

The following model IDs reach end-of-life on **July 23, 2026**:

| Model ID | Status |
|---|---|
| `gpt-5-codex` | Shutting down July 23 |
| `gpt-5.1-codex` | Shutting down July 23 |
| `gpt-5.1-codex-max` | Shutting down July 23 |
| `gpt-5.1-codex-mini` | Shutting down July 23 |
| `gpt-5.2-codex` | Shutting down July 23 |

The legacy `codex-mini-latest` model was already removed from the API on February 12, 2026.

`gpt-5.3-codex` is not on this list. It has a long-term support commitment in GitHub Copilot Business and Enterprise through February 4, 2027.

---

## The Migration

Change the model string:

```python
# Before (any of these)
response = client.responses.create(
    model="gpt-5.2-codex",  # or gpt-5.1-codex, gpt-5-codex, etc.
    ...
)

# After
response = client.responses.create(
    model="gpt-5.3-codex",
    ...
)
```

GPT-5.3-Codex is backward-compatible with the same API surfaces as earlier Codex models. Existing prompts, tool definitions, and system messages transfer without modification.

The one thing to check: if your code passes a `reasoning_effort` parameter, `gpt-5.3-codex` accepts `"low"`, `"medium"`, `"high"`, and `"xhigh"`. The older models accepted a narrower set of values. If you were passing an unsupported string, you may get a different behavior — validate your `reasoning_effort` values after migrating.

---

## What GPT-5.3-Codex Is

GPT-5.3-Codex combines two training stacks that were previously separate: the specialized coding training from the Codex lineage and the broader reasoning and professional knowledge from the GPT-5.2 base. Earlier Codex models were optimized narrowly for code generation. GPT-5.3-Codex handles the full agentic coding loop — research, planning, writing, running, debugging — without needing a separate orchestration model for non-code steps.

OpenAI describes the model as working "much like a colleague" during interactive sessions: you can steer it during long multi-file tasks without losing context, ask it to pause and replan, or hand off partial work to a human reviewer mid-task.

The model was used during its own development. OpenAI's Codex team used early versions of GPT-5.3-Codex to debug its own training runs and manage deployment processes.

---

## Capabilities Worth Knowing

### Reasoning Effort Settings

GPT-5.3-Codex supports four reasoning effort levels via the API:

```python
response = client.responses.create(
    model="gpt-5.3-codex",
    reasoning_effort="high",  # "low", "medium", "high", "xhigh"
    ...
)
```

- **`low`** — fast iteration, good for autocomplete-style tasks and short edits
- **`medium`** — balanced; default for most API calls
- **`high`** — longer reasoning; appropriate for architecture decisions and complex multi-file refactors
- **`xhigh`** — maximum reasoning budget; use for tasks where correctness matters more than latency (security audits, migration planning, critical path debugging)

Latency and cost scale with reasoning effort. For most build loops, `medium` is the right starting point. Use `xhigh` sparingly — it can take several minutes for complex tasks.

### Computer Use

GPT-5.3-Codex can interact with a desktop through screenshots. This applies to coding tasks involving legacy tooling that lacks an API: filling forms in a web IDE, clicking through a UI-only deployment pipeline, or navigating a GUI-based database tool. The model accepts screenshot inputs and outputs structured actions or Playwright scripts.

```python
response = client.responses.create(
    model="gpt-5.3-codex",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Click the 'Deploy to Production' button"},
                {"type": "image_url", "image_url": {"url": "data:image/png;base64,..."}}
            ]
        }
    ]
)
```

### Terminal-Bench Performance

GPT-5.3-Codex ranks at the top of Terminal-Bench 2.0, a benchmark specifically for command-line agentic tasks — shell scripting, build systems, package management, file manipulation pipelines. If your agent runs in a terminal or interacts with shell commands as a core workflow, benchmark performance here is directly relevant.

---

## Specifications

| Parameter | Value |
|---|---|
| Model ID | `gpt-5.3-codex` |
| Input context | 400,000 tokens |
| Max output | 128,000 tokens |
| Input pricing | $1.75 / MTok |
| Cached input | $0.175 / MTok |
| Output pricing | $14.00 / MTok |
| Reasoning effort | low, medium, high, xhigh |
| API availability | All paid tiers (Tier 1–5) |
| Supported endpoints | Responses API, Chat Completions, Batch, Fine-tuning, Assistants |

Pricing is identical to GPT-5.2-Codex. Migrating does not change your API costs.

---

## GitHub Copilot Status

GPT-5.3-Codex is now the default model across GitHub Copilot. Timeline of changes:

- **February 9, 2026**: GA for Copilot Pro, Pro+, Business, Enterprise
- **February 25, 2026**: Available in GitHub.com, GitHub Mobile, and Visual Studio
- **March 18, 2026**: Long-term support commitment announced — guaranteed available in Copilot Business and Enterprise through February 4, 2027
- **May 17, 2026**: Became the base/default model for all Copilot Business and Enterprise organizations
- **June 5, 2026**: GPT-5.2-Codex deprecated from most Copilot experiences; GPT-5.3-Codex is the automatic replacement

For teams using Copilot via GitHub's UI, this migration happened automatically on May 17. If you had explicit model selection set to `gpt-5.2-codex` in VS Code or JetBrains settings, check whether those overrides are still active — they may cause inconsistent behavior between your IDE and the Copilot API.

---

## GPT-5.3-Codex vs. GPT-5.5

GPT-5.5 is OpenAI's current top model. The Codex documentation now lists GPT-5.5 as the preferred model for most Codex tasks, with GPT-5.3-Codex as an "alternative model."

The distinction is specialization vs. breadth:

- **GPT-5.5** handles coding plus everything else (writing, analysis, multimodal tasks, professional documents). It is the right choice when your agent does coding alongside non-coding work.
- **GPT-5.3-Codex** is optimized for the agentic coding loop specifically. For pure code generation and terminal-execution pipelines, it benchmarks comparably to GPT-5.5 at lower per-token input costs ($1.75 vs. GPT-5.5's $5.00).

If your agent is exclusively writing, running, and debugging code — no document generation, no multimodal input — GPT-5.3-Codex remains cost-competitive at the task it was designed for.

---

## GPT-5.3-Codex-Spark

OpenAI has released `gpt-5.3-codex-spark` as a research preview. It is text-only (no image input), optimized for near-instant coding iteration at low latency. Currently restricted to ChatGPT Pro users only — no API access as of June 2026. Watch this space for a broader rollout.

---

## Builder Actions

1. **Audit your API calls now.** Search your codebase for `gpt-5-codex`, `gpt-5.1-codex`, `gpt-5.1-codex-max`, `gpt-5.1-codex-mini`, `gpt-5.2-codex`. Every instance of these model IDs breaks on July 23.
2. **Swap to `gpt-5.3-codex`.** No other code changes required for most workloads.
3. **Validate reasoning effort values.** If you pass a `reasoning_effort` parameter, confirm your value is one of `"low"`, `"medium"`, `"high"`, or `"xhigh"`.
4. **Check Copilot IDE settings.** If you have explicit model overrides in VS Code, JetBrains, or CLI settings, verify they point to `gpt-5.3-codex` or `gpt-5.5`.
5. **Evaluate GPT-5.5 if you are on a mixed workload.** For agents that combine coding with document generation, analysis, or multimodal inputs, GPT-5.5 is now recommended as the primary model.

July 23 is 51 days out. The migration is a one-line change. Do it before it is urgent.
