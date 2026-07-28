---
title: "Claude Opus 4.8 Is Here: Dynamic Workflows, Effort Control, and a June 15 Hard Deadline"
date: 2026-06-01
description: "Anthropic released Claude Opus 4.8 on May 28 with parallel subagent orchestration, five-tier effort control, and meaningfully better agentic benchmarks. The old Sonnet 4 and Opus 4 model IDs retire on June 15. Here is what changed, what the new API looks like, and what to do before the deadline."
og_description: "Claude Opus 4.8 launched May 28 with Dynamic Workflows (parallel subagents), five-level effort control, and 4x fewer unreported code defects. But the old claude-sonnet-4-20250514 and claude-opus-4-20250514 model IDs are being retired June 15 — that's 14 days to update your code."
content_type: "Builder's Log"
sources_audited: 2026-07-28
categories: ["Anthropic", "Claude", "Developer Tools"]
tags: ["anthropic", "claude", "claude-opus", "opus-4-8", "dynamic-workflows", "effort-control", "model-deprecation", "june-2026", "api", "agentic", "migration"]
---

[Anthropic released Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8) on May 28, 2026. The short description is: a meaningfully better agentic coding model at the same price as Opus 4.7, with two new features that change how you structure multi-step work.

There is also a deadline attached to this launch. The predecessor model IDs — `claude-sonnet-4-20250514` and `claude-opus-4-20250514` — retire on **June 15, 2026**. If you have either string hardcoded anywhere in production, you have 14 days to update it. API calls using those IDs will fail after the deadline.

---

## Benchmark Improvements

Opus 4.8's gains are concentrated in agentic coding and long-horizon tasks:

| Benchmark | Opus 4.8 | Opus 4.7 | Delta |
|---|---|---|---|
| SWE-bench Pro (agentic coding) | 69.2% | 64.3% | +4.9 pts |
| SWE-bench Verified | 88.6% | 87.6% | +1.0 pt |
| Terminal-Bench 2.1 | 74.6% | 66.1% | +8.5 pts |
| GDPval-AA Elo (knowledge work) | 1,890 | 1,753 | +137 pts |
| Artificial Analysis Intelligence Index | 61.4 | 57.3 | +4.1 pts |

(Scores per [Anthropic's Opus 4.8 announcement](https://www.anthropic.com/news/claude-opus-4-8) and the [Opus 4.8 system card](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf); independently corroborated by benchmark trackers including [llm-stats.com](https://llm-stats.com/blog/research/claude-opus-4-8-launch).)

The alignment improvements matter for code review and audit pipelines, per the [system card](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf) and [Anthropic's launch post](https://www.anthropic.com/news/claude-opus-4-8):

- **4x fewer unreported code defects** vs. Opus 4.7 — Anthropic describes Opus 4.8 as "around four times less likely than its predecessor to allow flaws in code it has written to pass unremarked"
- **First Claude model to score 0% on uncritically reporting flawed results** vs. Opus 4.7 — it will surface problems rather than smooth over them
- **10x+ reduction in overconfidence** vs. Opus 4.7 — more calibrated uncertainty surfacing

That last point has a practical implication. If you have a pipeline that treats high-confidence Claude outputs as automatically actionable, Opus 4.8 will surface uncertainty more visibly than 4.7. That is a feature for code review use cases and a friction point for confidence-dependent generation pipelines.

---

## Effort Control

Effort control is the simpler of the two new features. All five levels are available via the [API today, no beta header required](https://platform.claude.com/docs/en/build-with-claude/effort).

The parameter is `output_config.effort` in the Messages API request body:

```python
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    messages=[{"role": "user", "content": "..."}],
    output_config={"effort": "medium"},
)
```

| Level | API string | Intended use |
|---|---|---|
| Low | `"low"` | Simple lookups, high-volume pipelines, latency-sensitive subagents |
| Medium | `"medium"` | Balanced cost/performance, most agentic workflows |
| High | `"high"` | Complex reasoning, difficult coding tasks (this is the default) |
| Extra | `"xhigh"` | Long-horizon agentic coding sessions (30+ minutes), repeated tool calling |
| Max | `"max"` | Frontier problems requiring deepest possible reasoning |

Omitting the parameter entirely gives you `high`. [Anthropic recommends starting at `xhigh` for coding and agentic use cases](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8).

### No Manual Extended Thinking

This is the most common migration gotcha. [Opus 4.8 uses **adaptive thinking only**](https://platform.claude.com/docs/en/about-claude/models/migration-guide). If you set `thinking: {type: "enabled", budget_tokens: N}`, you will get a 400 error. The correct parameter is:

```python
thinking={"type": "adaptive"}
```

The model decides when to think and how deeply based on the request and your effort level. You influence thinking depth by raising or lowering effort, not by setting a token budget directly.

### No Sampling Parameters

Also returns 400 errors on Opus 4.8 (and Opus 4.7): setting `temperature`, `top_p`, or `top_k` to non-default values. Per [Anthropic's model deprecations page](https://platform.claude.com/docs/en/about-claude/model-deprecations), this restriction applies to Claude Opus 4.7 and all later models — not to earlier Opus 4.x releases like 4.5 or 4.6. Steer response behavior via prompting instead.

---

## Dynamic Workflows

Dynamic Workflows launched in [**research preview**, available on **Enterprise, Team, and Max plans only** via Claude Code](https://www.anthropic.com/news/claude-opus-4-8); it was not available through the API at launch.

The feature lets Claude plan a complex task, fan it out across parallel subagents within a single session, run adversarial verification passes, and confirm results against your test suite before reporting back. You do not write orchestration code — Claude writes its own orchestration scripts at planning time.

In practice, this means:
- **Codebase migrations** at scale: changes across hundreds of thousands of lines, with the test suite as the pass/fail bar
- **Parallelized research**: independent agents attack problems from different angles and report back for synthesis
- **Multi-stage verification pipelines**: a checking pass runs before any output reaches you

In Claude Code, this surfaces as [**"ultracode" mode**](https://code.claude.com/docs/en/workflows) — a setting combining `xhigh` effort with automatic workflow orchestration. For builders who want to replicate the behavior in their own harnesses, [Anthropic's docs describe a "Build an orchestration mode" pattern](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-effort-example), but the underlying multi-agent dispatch is not yet fully exposed via the Messages API.

### The Token Math

Dynamic Workflows is intentionally token-intensive. Anthropic's own documentation is explicit that ["a workflow spawns many agents, so a single run can use meaningfully more tokens than working through the same task in conversation"](https://code.claude.com/docs/en/workflows#cost) — Claude Code flags a run as "large" once it schedules more than 25 agents or its projected token total passes 1.5 million.

If you are on an Enterprise plan and considering Dynamic Workflows for production batch workloads, set `max_tokens` explicitly, profile a representative sample before scaling, and plan for higher per-task costs than your current Opus 4.7 baseline.

---

## Pricing

[Unchanged from Opus 4.7](https://platform.claude.com/docs/en/about-claude/pricing):

| Mode | Input | Output |
|---|---|---|
| Standard | $5 / MTok | $25 / MTok |
| Fast mode | $10 / MTok | $50 / MTok |

[Prompt cache hits: $0.50/MTok input. Batch API: 50% discount on standard pricing.](https://platform.claude.com/docs/en/about-claude/pricing#prompt-caching)

[Fast mode delivers approximately 2.5x the throughput](https://www.anthropic.com/news/claude-opus-4-8) at 2x the standard price. Context window is 1M tokens; maximum output is 128k tokens.

---

## Opus 4.8 vs. Sonnet 4.6: Which One to Use

Use **Opus 4.8** when:
- Running agentic coding sessions over 30 minutes or involving large codebases
- You need the highest alignment guarantees — code review, audit pipelines, compliance-sensitive generation
- [Working with computer-use agents (84% on Online-Mind2Web)](https://www.anthropic.com/news/claude-opus-4-8)
- Handling legal, finance, or professional-domain tasks
- [Processing multimodal workloads with large documents or diagrams (Databricks reported approximately 61% token cost reduction in these workloads vs. prior Opus)](https://www.anthropic.com/news/claude-opus-4-8)

Use **Sonnet 4.6** when:
- Single-shot prompts or short context tasks
- Latency is a primary constraint (Sonnet 4.6 is faster)
- [Cost is the deciding factor: Sonnet 4.6 is $3/$15 per MTok vs. $5/$25 for Opus 4.8](https://platform.claude.com/docs/en/about-claude/pricing)
- High-volume pipelines: classification, generation, summarization
- [You need extended thinking with an explicit token budget (`budget_tokens`) — Sonnet 4.6 still supports it](https://platform.claude.com/docs/en/about-claude/models/migration-guide), unlike Opus 4.8

---

## June 15 Migration: What to Update

On **June 15, 2026**, the following model IDs [stop accepting requests](https://platform.claude.com/docs/en/about-claude/model-deprecations):

| Retired model ID | Replacement |
|---|---|
| `claude-sonnet-4-20250514` | `claude-sonnet-4-6` |
| `claude-opus-4-20250514` | `claude-opus-4-8` |

Both were deprecated on April 14, 2026. After June 15, calls using either ID return an error. The API format, authentication, and response structure are unchanged — the migration is a string replacement in your model configuration.

If you are also running `claude-opus-4-0` or `claude-sonnet-4-0` (the version aliases), [those alias to the deprecated `-20250514` IDs](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) and retire on the same date, since no other snapshot exists for either alias to fall back to. Update those too.

The [official Anthropic model deprecations page](https://platform.claude.com/docs/en/about-claude/model-deprecations) also lists `claude-3-opus-20240229` (Claude Opus 3) as now recommending `claude-opus-4-8` as its replacement — worth checking if you have legacy Opus 3 references in any older integrations.

### Finding Hardcoded Model IDs

If you manage multiple codebases, a quick sweep:

```bash
# Find hardcoded deprecated model IDs
grep -r "claude-sonnet-4-20250514\|claude-opus-4-20250514\|claude-sonnet-4-0\|claude-opus-4-0" .
```

Environment variables, configuration files, CI/CD pipelines, and infrastructure-as-code are the most common places these slip through after source code is updated.

---

## Key Takeaways for Builders

**Today (June 1):** Claude Opus 4.8 is available at `claude-opus-4-8`. Same price as 4.7, better agentic benchmarks, five-level effort control, no manual thinking budget or sampling parameters.

**Before June 15:** Update any production code using `claude-sonnet-4-20250514` or `claude-opus-4-20250514`. Two weeks is enough time but not unlimited time.

**Dynamic Workflows:** Research preview in Claude Code (Enterprise/Team/Max only). Powerful for long-horizon coding and migration tasks, expensive on tokens by design — profile before scaling.

**Effort gotcha:** Start at `xhigh` for complex agentic work. Omitting the parameter gives you `high`, which is not always sufficient for extended coding sessions. The difference in output quality at `xhigh` vs. `high` is measurable on multi-step agentic tasks.
