---
title: "Claude Sonnet 5 Is Live: Pricing Window, Benchmarks, and the Migration Decision"
date: 2026-06-30
description: "Claude Sonnet 5 launched June 30 at 33% below standard pricing through August 31. Near-Opus 4.8 performance, 1M context, adaptive thinking, and effort:high by default — here is what builders need to know."
tags: ["anthropic", "claude", "sonnet", "model-release", "api", "pricing", "agentic", "builder-guide", "migration"]
---

Anthropic released Claude Sonnet 5 on June 30, 2026, and made it the default model for Free and Pro users on claude.ai the following day. For builders on the API, it is available now at introductory pricing that expires August 31. After that, standard pricing applies — which is the same as Sonnet 4.6.

That introductory window is the most immediate call to action. If you are running Sonnet 4.6 in production, the current Sonnet 5 pricing is 33% cheaper on both input and output, with substantially better performance. There is no argument for staying on 4.6 until September.

---

## What Changed

Sonnet 5 is positioned as Anthropic's most capable Sonnet to date and the primary agentic workhorse below Opus 4.8. The headline capability shift: it can make plans, choose tools, and run multi-step autonomous workflows at a level that previously required larger and more expensive models.

**SWE-Bench Verified:** 85.2% — up from 79.6% on Sonnet 4.6. That 5.6-point jump on a hard coding benchmark is not incremental. It reflects a model that handles real-world code changes more reliably, not just simpler tasks.

Other published benchmark numbers:

| Benchmark | Sonnet 5 |
|---|---|
| SWE-Bench Verified | 85.2% |
| SWE-Bench Pro | 63.2% |
| SWE-Bench Multilingual | 78.3% |
| Terminal-Bench 2.1 | 80.4% |
| OSWorld-Verified | 81.2% |
| BrowseComp (single-agent) | 84.7% |
| BrowseComp (multi-agent) | 86.6% |
| Humanity's Last Exam with tools | 57.4% |
| USAMO 2026 | 79.5% |

---

## Model Specs

| Spec | Value |
|---|---|
| **Claude API ID** | `claude-sonnet-5` |
| **AWS Bedrock ID** | `anthropic.claude-sonnet-53` |
| **Google Cloud ID** | `claude-sonnet-5` |
| **Context window** | 1M tokens |
| **Max output** | 128K tokens (300K on Batch API with beta header) |
| **Adaptive thinking** | Yes |
| **Extended thinking** | No |
| **Effort default** | `high` (on Claude API and Claude Code) |
| **Knowledge cutoff** | January 2026 |

---

## The Pricing Picture

**Introductory pricing (through August 31, 2026):**

| | Input | Output |
|---|---|---|
| Sonnet 5 | $2/M tokens | $10/M tokens |
| Sonnet 4.6 | $3/M tokens | $15/M tokens |

Sonnet 5 is currently 33% cheaper than Sonnet 4.6 on both dimensions, and it outperforms it on every published benchmark. The migration case is straightforward.

**Standard pricing (from September 1, 2026):**

| | Input | Output |
|---|---|---|
| Sonnet 5 | $3/M tokens | $15/M tokens |

After September 1, Sonnet 5 and Sonnet 4.6 cost the same. There is still no reason to stay on 4.6 — but the urgency to switch before September is real if your workloads are cost-sensitive.

Batch API discount: 50% off standard pricing. On the Message Batches API, `output-300k-2026-03-24` beta header unlocks 300K output tokens per message.

---

## What "Effort: High by Default" Means

Sonnet 5 introduces a behavioral change that Sonnet 4.6 did not have: the `effort` parameter defaults to `high` on both the Claude API and Claude Code. This means Sonnet 5 uses adaptive thinking out of the box — it allocates additional reasoning budget to hard problems without you asking.

The practical effect: slightly higher latency and token usage than a naive comparison to Sonnet 4.6 would suggest. If you are benchmarking costs by swapping the model ID and running the same prompts, you may see Sonnet 5 generating more thinking tokens than Sonnet 4.6 did.

To control this:

```python
# Lower effort for speed-sensitive, simple tasks
response = client.messages.create(
    model="claude-sonnet-5",
    effort="low",   # or "medium"
    ...
)

# Explicit high for complex agentic work (this is already the default)
response = client.messages.create(
    model="claude-sonnet-5",
    effort="high",
    ...
)
```

If your workload is latency-sensitive and the task does not require deep reasoning, set `effort="low"` explicitly. If you are running agents on complex multi-step tasks, leave the default or set `effort="high"`.

---

## When to Use Sonnet 5 vs. Opus 4.8 vs. Fable 5

| Task type | Recommended model |
|---|---|
| Production agents — coding, tool use, multi-step workflows | **Sonnet 5** |
| Maximum coding accuracy, long autonomous sessions, complex refactors | **Opus 4.8** |
| Extended agentic runs (hours not minutes), highest frontier capability | **Fable 5** |
| High-volume, latency-sensitive inference, classification, extraction | **Haiku 4.5** |

Sonnet 5 closes the gap on Opus 4.8 significantly. For most production agent use cases — customer-facing automations, internal workflow tools, CI integrations — Sonnet 5 at $3/M (or $2/M now) will outperform Opus 4.8's cost-effectiveness substantially. Reserve Opus 4.8 for tasks where accuracy matters more than cost and where Sonnet 5 demonstrably falls short in your specific workload.

---

## Safety Changes

Anthropic reports Sonnet 5 is safer than Sonnet 4.6 on all measured dimensions:

- Lower hallucination and sycophancy rates
- Better refusal of clearly malicious requests
- Improved resistance to prompt injection attacks
- Cyber safeguards enabled by default (less restrictive than Fable 5)
- Substantially reduced exploit-development capabilities compared to Opus models

The prompt injection improvement is particularly relevant for agentic builders whose systems expose Claude to untrusted web content or external documents. Sonnet 5 is more robust in those pipelines without requiring additional defensive system prompting.

---

## Deprecation Alert: Claude Opus 4.1 Retires August 5

If any of your systems use `claude-opus-4-1-20250805`, you have 33 days from today to migrate. Opus 4.1 retires August 5, 2026. API calls after that date will fail.

Migrate to `claude-opus-4-8` for equivalent or better performance. Opus 4.1 was substantially more expensive ($15/$75 per MTok) than Opus 4.8 ($5/$25 per MTok), so this migration also cuts inference costs by two-thirds.

---

## Migration Checklist

1. **Update your model ID** from `claude-sonnet-4-6` to `claude-sonnet-5`. The API is backwards-compatible on parameters; no other code changes are required for basic use.

2. **Audit your effort settings.** If you previously relied on Sonnet 4.6's no-reasoning behavior for latency-sensitive paths, add `effort="low"` explicitly for those calls.

3. **Benchmark before September 1.** Introductory pricing runs through August 31. Use that window to validate Sonnet 5 in your workload and lock in 33% savings for the remainder of the summer.

4. **If you are on Opus 4.1, migrate now.** August 5 is the hard deadline. See the [model deprecations page](https://platform.claude.com/docs/en/about-claude/model-deprecations) for details.

5. **Available everywhere.** Sonnet 5 is live on the Claude API, AWS Bedrock (`anthropic.claude-sonnet-53`), Google Cloud Vertex AI, and Microsoft Foundry.

---

*ChatForest covers practical AI builder developments. Research-based: we do not run live API sessions. Model IDs and pricing from [Anthropic's model overview documentation](https://platform.claude.com/docs/en/about-claude/models/overview).*
