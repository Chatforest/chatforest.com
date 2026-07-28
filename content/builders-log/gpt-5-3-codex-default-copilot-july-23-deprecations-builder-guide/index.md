---
title: "GPT-5.3-Codex Is Now the Copilot Default — and Every Older Codex Model Retires July 23"
date: 2026-06-02
description: "GPT-5.3-Codex became the base model for all GitHub Copilot Business and Enterprise organizations on May 17. If you have production API calls to gpt-5.2-codex or older, every one of them breaks on July 23. Here's the migration path and what the model actually offers."
content_type: "Builder's Log"
categories: ["OpenAI", "Model Migration", "Agent Development", "GitHub Copilot"]
tags: ["openai", "gpt-5.3-codex", "codex", "model-deprecation", "github-copilot", "agentic-coding", "api-migration", "reasoning-effort", "computer-use", "agent-development"]
sources_audited: 2026-07-28
---

[GPT-5.3-Codex has been OpenAI's primary agentic coding model since February 5, 2026](https://openai.com/index/introducing-gpt-5-3-codex/). [On May 17 it became the base model for all GitHub Copilot Business and Enterprise organizations](https://github.blog/changelog/2026-05-17-gpt-5-3-codex-is-now-the-base-model-for-copilot-business-and-enterprise/), replacing GPT-4.1 as the default. On June 5, GPT-5.2-Codex was removed from most Copilot model pickers.

And on July 23, 2026, [every earlier Codex API model was originally scheduled to shut down](https://developers.openai.com/api/docs/deprecations).

If you have any production calls to `gpt-5-codex`, `gpt-5.1-codex`, `gpt-5.1-codex-max`, `gpt-5.2-codex`, or `gpt-5.1-codex-mini`, those calls fail in 51 days.

> **Update, 2026-07-28:** OpenAI has since pushed the shutdown date for these five Codex model IDs back to **October 23, 2026**, per the [live OpenAI deprecations page](https://developers.openai.com/api/docs/deprecations) — replacement models are now listed as `gpt-5.6-sol` (for `gpt-5-codex`, `gpt-5.1-codex`, `gpt-5.1-codex-max`, `gpt-5.2-codex`) and `gpt-5.6-terra` (for `gpt-5.1-codex-mini`), part of the [GPT-5.6 family OpenAI previewed](https://openai.com/index/previewing-gpt-5-6-sol/) in July 2026. The rest of this article reflects what was true and published as of June 2, 2026; the migration advice (move off these model IDs to `gpt-5.3-codex` or newer) still stands, you now have more runway to do it.

---

## What Is Being Shut Down

The following model IDs were originally set to reach end-of-life on **July 23, 2026**, per [OpenAI's deprecations page](https://developers.openai.com/api/docs/deprecations) as published at the time of this article (see the update note above for the revised October 23, 2026 date):

| Model ID | Status (as of original publication) |
|---|---|
| `gpt-5-codex` | Shutting down July 23 |
| `gpt-5.1-codex` | Shutting down July 23 |
| `gpt-5.1-codex-max` | Shutting down July 23 |
| `gpt-5.1-codex-mini` | Shutting down July 23 |
| `gpt-5.2-codex` | Shutting down July 23 |

The legacy `codex-mini-latest` model was [removed from the API on February 12, 2026](https://developers.openai.com/api/docs/deprecations), replaced by `gpt-5-codex-mini`.

`gpt-5.3-codex` is not on this list. It has a [long-term support commitment](https://github.blog/changelog/2026-03-18-gpt-5-3-codex-long-term-support-in-github-copilot/) in GitHub Copilot Business and Enterprise through February 4, 2027.

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

[GPT-5.3-Codex combines two training stacks that were previously separate](https://openai.com/index/introducing-gpt-5-3-codex/): the specialized coding training from the Codex lineage (GPT-5.2-Codex) and the broader reasoning and professional knowledge from the GPT-5.2 base. Earlier Codex models were optimized narrowly for code generation. GPT-5.3-Codex handles the full agentic coding loop — research, planning, writing, running, debugging — without needing a separate orchestration model for non-code steps.

[OpenAI describes the model as working "much like a colleague"](https://openai.com/index/introducing-gpt-5-3-codex/) during interactive sessions: you can steer it during long multi-file tasks without losing context, ask it to pause and replan, or hand off partial work to a human reviewer mid-task.

[The model was used during its own development](https://openai.com/index/introducing-gpt-5-3-codex/) — OpenAI describes GPT-5.3-Codex as the first model in the family "instrumental in creating itself," with early versions used to debug training runs, optimize deployment infrastructure, and build data pipelines for model evaluation.

---

## Capabilities Worth Knowing

### Reasoning Effort Settings

[GPT-5.3-Codex supports four reasoning effort levels](https://developers.openai.com/api/docs/models/gpt-5.3-codex) via the API:

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

GPT-5.3-Codex can interact with a desktop through screenshots, [scoring 64.7% on OSWorld-Verified](https://www.datacamp.com/blog/gpt-5-4) — a benchmark for vision-based desktop task completion. This applies to coding tasks involving legacy tooling that lacks an API: filling forms in a web IDE, clicking through a UI-only deployment pipeline, or navigating a GUI-based database tool. The model accepts screenshot inputs and outputs structured actions or Playwright scripts. Note that OpenAI's subsequent GPT-5.4 release is billed as the first general-purpose OpenAI model with *native* computer-use built in, and is a stronger choice specifically for computer-use-heavy workflows.

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

GPT-5.3-Codex scores 77.3% on [Terminal-Bench 2.0](https://llm-stats.com/benchmarks/terminal-bench-2), a benchmark for command-line agentic tasks — shell scripting, build systems, package management, file manipulation pipelines — up from GPT-5.2-Codex's 64.0%. That was the top score on the benchmark at GPT-5.3-Codex's February 2026 launch; GPT-5.5, released in April 2026, has since taken the top spot at 82.7%. If your agent runs in a terminal or interacts with shell commands as a core workflow, benchmark performance here is directly relevant.

---

## Specifications

Per [OpenAI's Codex model documentation](https://learn.chatgpt.com/docs/models) and [GitHub's Copilot pricing docs](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing):

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

- [**February 9, 2026**: GA for Copilot Pro, Pro+, Business, Enterprise](https://github.blog/changelog/2026-02-09-gpt-5-3-codex-is-now-generally-available-for-github-copilot/)
- [**February 25, 2026**: Available in GitHub.com, GitHub Mobile, and Visual Studio](https://github.blog/changelog/2026-02-25-gpt-5-3-codex-is-now-available-in-github-com-github-mobile-and-visual-studio/)
- [**March 18, 2026**: Long-term support commitment announced](https://github.blog/changelog/2026-03-18-gpt-5-3-codex-long-term-support-in-github-copilot/) — guaranteed available in Copilot Business and Enterprise through February 4, 2027
- [**May 17, 2026**: Became the base/default model for all Copilot Business and Enterprise organizations](https://github.blog/changelog/2026-05-17-gpt-5-3-codex-is-now-the-base-model-for-copilot-business-and-enterprise/)
- [**June 5, 2026**: GPT-5.2-Codex deprecated from most Copilot experiences](https://github.blog/changelog/2026-06-05-gpt-5-2-and-gpt-5-2-codex-deprecated/); GPT-5.3-Codex and GPT-5.5 are the recommended replacements

For teams using Copilot via GitHub's UI, this migration happened automatically on May 17. If you had explicit model selection set to `gpt-5.2-codex` in VS Code or JetBrains settings, check whether those overrides are still active — they may cause inconsistent behavior between your IDE and the Copilot API.

---

## GPT-5.3-Codex vs. GPT-5.5

GPT-5.5 is OpenAI's current top model. [OpenAI's Codex documentation](https://learn.chatgpt.com/docs/models) lists GPT-5.5 among its "Recommended models" for complex coding, computer use, knowledge work, and research workflows, with GPT-5.3-Codex positioned as the Codex-tuned alternative for coding-heavy sessions.

The distinction is specialization vs. breadth:

- **GPT-5.5** handles coding plus everything else (writing, analysis, multimodal tasks, professional documents). It is the right choice when your agent does coding alongside non-coding work.
- **GPT-5.3-Codex** is optimized for the agentic coding loop specifically. On Terminal-Bench 2.0 it trails GPT-5.5 (77.3% vs. 82.7%) but at a lower per-token input cost ([$1.75 vs. GPT-5.5's $5.00](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing)).

If your agent is exclusively writing, running, and debugging code — no document generation, no multimodal input — GPT-5.3-Codex remains cost-competitive at the task it was designed for.

---

## GPT-5.3-Codex-Spark

[OpenAI has released `gpt-5.3-codex-spark`](https://openai.com/index/introducing-gpt-5-3-codex-spark/) as a research preview. It is optimized for near-instant coding iteration at ultra-low latency (1,000+ tokens/sec via Cerebras hardware). Currently available to ChatGPT Pro users and in the Codex app, Codex CLI, and VS Code extension — no general API access as of June 2026. Watch this space for a broader rollout.

---

## Builder Actions

1. **Audit your API calls now.** Search your codebase for `gpt-5-codex`, `gpt-5.1-codex`, `gpt-5.1-codex-max`, `gpt-5.1-codex-mini`, `gpt-5.2-codex`. Every instance of these model IDs breaks on July 23.
2. **Swap to `gpt-5.3-codex`.** No other code changes required for most workloads.
3. **Validate reasoning effort values.** If you pass a `reasoning_effort` parameter, confirm your value is one of `"low"`, `"medium"`, `"high"`, or `"xhigh"`.
4. **Check Copilot IDE settings.** If you have explicit model overrides in VS Code, JetBrains, or CLI settings, verify they point to `gpt-5.3-codex` or `gpt-5.5`.
5. **Evaluate GPT-5.5 if you are on a mixed workload.** For agents that combine coding with document generation, analysis, or multimodal inputs, GPT-5.5 is now recommended as the primary model.

At original publication, July 23 was 51 days out; per the update note above, OpenAI has since moved that shutdown to October 23, 2026. The migration is still a one-line change. Do it before it is urgent.
