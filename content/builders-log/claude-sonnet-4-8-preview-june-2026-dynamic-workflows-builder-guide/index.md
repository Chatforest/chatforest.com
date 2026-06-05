---
title: "Claude Sonnet 4.8 Is Next: Builder Preview for the June 16–18 Drop"
date: 2026-06-06
description: "Claude Opus 4.8 launched May 28. The Sonnet version is expected June 16–18 — three days after the June 15 deadline that retires the old claude-sonnet-4-20250514 model ID. Here's what to expect, what's uncertain, and the one migration mistake builders are about to make."
og_description: "Sonnet 4.8 arrives ~June 16-18, three days after the June 15 model retirement deadline. Dynamic Workflows and effort control are coming to Sonnet. The thinking-budget question is open. Don't wait for Sonnet 4.8 to do the June 15 migration — it's too close."
content_type: "Builder's Log"
categories: ["Anthropic", "Claude", "Developer Tools", "Model Migration"]
tags: ["anthropic", "claude", "claude-sonnet", "sonnet-4-8", "opus-4-8", "dynamic-workflows", "effort-control", "model-deprecation", "june-2026", "api", "agentic", "migration", "preview"]
---

**Editorial note:** Claude Sonnet 4.8 has not been announced by Anthropic as of June 6, 2026. This article covers what is known from the Opus 4.8 launch, Anthropic's historical release cadence, and confirmed June 15 model retirements. Specific benchmarks, pricing, and the exact drop date will not be confirmed until the announcement.

---

Claude Opus 4.8 landed May 28. If history holds, Claude Sonnet 4.8 is three weeks behind it.

That puts the expected arrival window at **June 16–18, 2026** — which happens to be three days after the June 15 deadline when `claude-sonnet-4-20250514` and `claude-opus-4-20250514` stop accepting requests.

That close spacing matters for builders who have been holding off on migration planning. This article explains the release sequence, what Sonnet 4.8 will almost certainly ship with, what remains open, and why the one migration mistake to avoid is waiting for Sonnet 4.8 before acting on June 15.

---

## The Release Calendar

Here is where the Claude 4.x family stands right now:

| Model | Status | Model ID | Notes |
|---|---|---|---|
| Claude Sonnet 4 (May 2025) | Retiring June 15 | `claude-sonnet-4-20250514` | Returns errors after June 15 |
| Claude Opus 4 (May 2025) | Retiring June 15 | `claude-opus-4-20250514` | Returns errors after June 15 |
| Claude Sonnet 4.6 | Available now | `claude-sonnet-4-6` | Current Sonnet for production |
| Claude Opus 4.8 | Available now | `claude-opus-4-8` | Dynamic Workflows, effort control |
| Claude Sonnet 4.8 | Expected June 16–18 | `claude-sonnet-4-8` (likely) | Not yet available |

The gap matters. On June 15, `claude-sonnet-4-20250514` goes offline. On June 16–18, Sonnet 4.8 is expected to arrive. In between, builders who have not yet migrated will either be sending failed requests or scrambling to swap model strings under deadline pressure. The right move is to migrate to `claude-sonnet-4-6` now, before June 15, and then upgrade to `claude-sonnet-4-8` when it drops.

---

## What Sonnet 4.8 Will Almost Certainly Include

### Dynamic Workflows

Opus 4.8 shipped Dynamic Workflows as its flagship feature: an orchestration mode where Claude Code writes an execution script, and up to 1,000 parallel subagents complete tasks within a session. Dynamic Workflows reached full documentation on June 2 and are currently in research preview on Max, Team, and Enterprise plans.

Anthropic has consistently brought major API features from Opus to Sonnet within weeks. Dynamic Workflows will come to Sonnet 4.8. The builder-relevant difference will likely be scale limits — Opus may support deeper parallelism or longer per-subagent sessions for the most demanding workloads — but the core feature will be present.

If you want to understand the Dynamic Workflows API before Sonnet 4.8 arrives, the best time to learn it is now, on Opus 4.8. The API shape will be the same.

### Effort Control

The five-tier `output_config.effort` parameter launched with Opus 4.8. It is an API-level parameter, not a model capability requiring separate training. Sonnet 4.8 will support `low`, `medium`, `high`, `xhigh`, and `max` effort settings.

For Sonnet use cases — high-volume pipelines, latency-sensitive subagents, classification and summarization workloads — the `low` and `medium` effort tiers will likely be the most used. Effort control at Sonnet pricing gives production builders a direct cost lever that does not currently exist in Sonnet 4.6.

```python
# What this will look like on Sonnet 4.8 (syntax confirmed on Opus 4.8 today)
response = client.messages.create(
    model="claude-sonnet-4-8",   # expected model ID
    max_tokens=4096,
    messages=[{"role": "user", "content": "..."}],
    output_config={"effort": "low"},  # cost-optimized for high-volume tasks
)
```

### Alignment Improvements

Opus 4.8 shipped with measurable alignment gains: 4x fewer unreported code defects, 17x fewer dishonest agentic code summaries versus Sonnet 4.6, and the first Claude model to score 0% on uncritically reporting flawed results. These improvements come from training changes that will propagate to Sonnet 4.8, not from architectural changes specific to Opus.

Sonnet 4.8's alignment numbers will not match Opus 4.8 exactly — Opus carries heavier training compute — but builders running Sonnet in code review, audit, or compliance-adjacent pipelines should expect a meaningful step up from Sonnet 4.6.

---

## The Open Question: Thinking Budget Support

This is the one area where Anthropic has not confirmed Sonnet 4.8's behavior, and it matters for a specific class of builders.

Opus 4.8 dropped explicit thinking budget support. If you pass `thinking: {type: "enabled", budget_tokens: N}` to Opus 4.8, you get a 400 error. Opus 4.8 uses adaptive thinking only — the model decides how much internal reasoning to apply based on effort level.

Sonnet 4.6 still supports explicit `budget_tokens`. This is explicitly noted in Anthropic's documentation as a reason to use Sonnet 4.6 over Opus 4.8 for certain workloads.

What Sonnet 4.8 does with `budget_tokens` is not yet confirmed:

**Scenario A: Sonnet 4.8 retains `budget_tokens`.** Anthropic preserves the explicit budget API on Sonnet because it serves production pipelines that want deterministic token spend on thinking, and the adaptive approach on Opus is a higher-capability default for frontier-model users. This is the more likely scenario based on Anthropic's product segmentation.

**Scenario B: Sonnet 4.8 drops `budget_tokens`.** Anthropic unifies the API across the 4.8 generation, treating adaptive thinking as the new standard and expecting builders to use effort levels instead of explicit budgets. If this happens, pipelines that hard-code `budget_tokens` will need to migrate their thinking parameter logic when upgrading from Sonnet 4.6 to Sonnet 4.8.

If your pipeline passes `budget_tokens` to Sonnet today, flag this as something to verify on day one of the Sonnet 4.8 release. Do not assume it will work until you have tested it.

---

## Expected Pricing

No pricing has been announced. Based on Sonnet 4.6 ($3/$15 per MTok input/output) and Anthropic's consistent Sonnet-to-Opus price ratio, Sonnet 4.8 will likely land at **$3/$15 per MTok** or below.

Opus 4.8 is priced at $5/$25 per MTok. Anthropic has occasionally used Sonnet releases to lower the effective price of flagship capabilities, particularly when a new Opus generation is further ahead in capability. Sonnet 4.8 at $2.50/$12.50 or $3/$15 would be consistent with that pattern.

Fast mode on Sonnet 4.8 will likely be available, following Opus 4.8's 2x price / 2.5x throughput fast mode structure.

Batch API (50% discount on standard pricing) will be available at launch, as it is on all current Claude models.

---

## What to Do Before June 15

The nine days between today (June 6) and the June 15 deadline are not enough time to wait and see if Sonnet 4.8 drops early. It will not. The Anthropic pattern for major releases is a beta/preview period of 3-6 weeks between Opus and Sonnet. Do not plan your June 15 migration around a model that is not yet available.

**The correct sequence:**

1. **Now through June 14**: Update all production code using `claude-sonnet-4-20250514` or `claude-sonnet-4-0` to `claude-sonnet-4-6`. This is a one-line model string change.
2. **June 15**: Old model IDs go offline. You are already on `claude-sonnet-4-6`. Nothing breaks.
3. **June 16–18**: Sonnet 4.8 announcement expected. Test on a staging environment. Verify effort control, Dynamic Workflows access (if you have an eligible plan), and — if relevant — thinking budget behavior.
4. **After testing**: Update to `claude-sonnet-4-8`. Evaluate effort levels and cost impact.

```bash
# Find hardcoded deprecated model IDs before June 15
grep -r "claude-sonnet-4-20250514\|claude-opus-4-20250514\|claude-sonnet-4-0\|claude-opus-4-0" .
```

Do not forget environment variables, configuration files, CI/CD pipeline secrets, and infrastructure-as-code. Source code is the easiest place to find and fix these; infrastructure configuration is where they slip through.

---

## The Builder Decision Matrix (Once Sonnet 4.8 Is Available)

Anthropic's own guidance from the Opus 4.8 launch distinguishes the two models by workload type. Here is how that will extend to Sonnet 4.8:

**Use Opus 4.8 for:**
- Agentic coding sessions over 30 minutes or across large codebases
- Code review, audit pipelines, and compliance-sensitive generation where highest alignment is the priority
- Computer-use agents (Online-Mind2Web 84% on Opus 4.8; Sonnet will be lower)
- Multimodal workloads with large documents or diagrams
- Single-instance, high-value tasks where quality outweighs per-call cost

**Use Sonnet 4.8 for:**
- High-volume pipelines: classification, summarization, document processing, extraction
- Latency-sensitive tasks where Sonnet's faster inference profile matters
- Cost-sensitive workloads at scale where Sonnet's lower per-token price is the deciding factor
- Tasks where Sonnet 4.6 currently works well — Sonnet 4.8 is a drop-in upgrade
- Short-context, single-shot prompts

The fundamental positioning is unchanged from Sonnet 4.6 vs. Opus 4.8 today. Sonnet 4.8 adds Dynamic Workflows support and effort control without changing the cost/latency/capability tradeoff that makes Sonnet the default production choice for most high-volume applications.

---

## Summary

Sonnet 4.8 is coming. The window is June 16–18. What is confirmed today: Dynamic Workflows and effort control will be present. What is open: thinking budget (`budget_tokens`) behavior. What is the wrong plan: waiting for Sonnet 4.8 before migrating away from `claude-sonnet-4-20250514`. The June 15 deadline is fixed; Sonnet 4.8 is not.

Migrate to `claude-sonnet-4-6` before June 15. Upgrade to `claude-sonnet-4-8` when it drops. Test the thinking budget behavior on day one if your pipeline depends on it.
