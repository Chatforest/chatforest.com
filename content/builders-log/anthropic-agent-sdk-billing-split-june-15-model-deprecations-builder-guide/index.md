---
title: "Anthropic's June 15, 2026 Update: Two Models Retired, Opus 4.7 Breaking Change — and a Billing Split That Got Paused"
date: 2026-06-03
description: "On June 15, 2026, Anthropic retired claude-sonnet-4-20250514 and claude-opus-4-20250514 and made temperature/top_p/top_k return errors on Opus 4.7+. A separate Agent SDK billing pool was announced for the same date but paused before it took effect. Here is what actually changed."
sources_audited: 2026-07-28
content_type: "Builder's Log"
categories: ["Anthropic", "Claude API", "Agent Development", "Model Migration", "Billing"]
tags: ["anthropic", "claude-agent-sdk", "billing", "model-deprecation", "claude-sonnet-4-6", "claude-opus-4-8", "multi-agent", "ci-cd", "token-budget", "api-migration"]
---

> **Update — June 15, 2026 (post-mortem, corrected):** Two of the three changes below went live as scheduled; the billing split did not. Both model retirements are confirmed — API calls to `claude-sonnet-4-20250514` and `claude-opus-4-20250514` now return errors, per [Anthropic's model deprecations page](https://platform.claude.com/docs/en/docs/about-claude/model-deprecations). The `temperature`/`top_p`/`top_k` change on Opus 4.7+ is also confirmed, per the same page's [API parameter deprecations table](https://platform.claude.com/docs/en/docs/about-claude/model-deprecations#api-parameter-deprecations). **The Agent SDK billing split did not launch.** Anthropic's own Help Center confirms it: ["We're pausing the changes to Claude Agent SDK usage described below. For now, nothing has changed: Claude Agent SDK, `claude -p`, and third-party app usage still draw from your subscription's usage limits."](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan) There is no separate credit pool, nothing to claim, and no overflow toggle to configure. If you are debugging today, check only your model ID strings — the billing mechanics below never took effect.

Three things were scheduled to happen on June 15, 2026, that affect builders using Anthropic's Claude — two of them did:

1. **The billing split (paused, did not happen)** — Anthropic [announced](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan) that Agent SDK usage would move into its own credit pool, separate from interactive Claude, then paused the change on June 15 before it took effect.
2. **Two model retirements (happened)** — `claude-sonnet-4-20250514` and `claude-opus-4-20250514` [stopped accepting API calls](https://platform.claude.com/docs/en/docs/about-claude/model-deprecations).
3. **A breaking API parameter change (happened)** — `temperature`, `top_p`, and `top_k` [return 400 errors](https://platform.claude.com/docs/en/docs/about-claude/model-deprecations#api-parameter-deprecations) on Opus 4.7 and later when set to a non-default value.

This post covers each in detail and ends with a checklist. The billing section below describes the plan Anthropic announced and then paused — it is retained for the record, clearly marked, since builders may still encounter references to it.

---

## The Billing Split (Announced, Then Paused — Never Took Effect)

**This entire section describes a plan Anthropic announced and then paused before it launched.** As of June 15, 2026, [Anthropic's Help Center states plainly](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan): "We're pausing the changes to Claude Agent SDK usage described below. For now, nothing has changed." Everything in this section is retained for reference — it is not current billing behavior.

### Before June 15 (and, per the pause, still true today)

All Claude usage — the claude.ai website, the Claude Code terminal, Agent SDK runs, `claude -p` scripts, GitHub Actions, and third-party apps like OpenClaw and Zed — draws from a single subscription pool. A Max 20x subscriber paying $200/month can run Agent SDK workloads against that same $200/month subscription limit, with no separate metering, per the same Help Center article.

### What Anthropic announced for June 15 (paused before taking effect)

Anthropic's plan, as described on the [Agent SDK billing Help Center page](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan), called for two independent pools with no cross-pool sharing:

**Interactive pool (unchanged behavior):**
- claude.ai web, desktop, and mobile
- Interactive Claude Code terminal (when you are the human in the loop)
- Claude Cowork

**Agent SDK credit pool (new):**
- Claude Agent SDK (`claude-agent-sdk` Python/TypeScript packages)
- `claude -p` in non-interactive mode
- Claude Code in GitHub Actions
- Third-party apps authenticating via Agent SDK: OpenClaw, Conductor, Zed in agent mode, Jean, T3 Code, and others

### Monthly Credit Amounts (as announced — never activated)

Per [Anthropic's Agent SDK billing page](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan), the proposed monthly credit was:

| Plan | Monthly Agent SDK Credit (proposed) |
|---|---|
| Pro ($20/mo) | $20 |
| Max 5x ($100/mo) | $100 |
| Max 20x ($200/mo) | $200 |
| Team Standard | $20/seat |
| Team Premium | $100/seat |
| Enterprise Standard | Not eligible |
| Enterprise Premium | $200/seat |

As announced, credits would have billed at standard API list rates, would not have pooled across team members, and would not have rolled over month to month. **None of this is in effect.** There is no credit to claim, no overflow toggle, and nothing to configure in the Console — Agent SDK usage still draws from ordinary subscription limits, per the same Help Center article.

### The Claim Action That Never Applied

The original announcement described a one-time manual claim requirement before credits would activate. Since Anthropic paused the change before June 15, **there is no claim action to take.** If you see older guidance (including earlier versions of this post) telling you to visit the Console and claim credits, that guidance is obsolete — [Anthropic's Help Center](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan) confirms nothing has changed and there is nothing to claim.

### Why Anthropic Proposed This Change

Community cost analyses circulated in the weeks before the announcement arguing that heavy Agent SDK users were drawing far more API-equivalent value than their subscription price. One [widely-cited community breakdown](https://gist.github.com/MagnaCapax/d9177e35b355853f03c730dfcaa693ef) worked two separate scenarios, and they should not be conflated: a Max 20x subscriber running ~30 hours/week of Opus output at 60K tokens/hour, at Opus's $25/MTok output rate, works out to roughly $5,800/month of API-equivalent value on a $200 subscription (about 29x); a much heavier Sonnet-only workload (240–480 hours/week, which the analysis treats as an extreme/automation-farm case) was estimated at 150x–175x, since Sonnet 4.6 is priced about 5x cheaper per token than Opus ($3/$15 vs. $5/$25 per MTok, per [Anthropic's pricing page](https://platform.claude.com/docs/en/about-claude/pricing)). Both scenarios illustrate the same underlying point — subscription rates were not designed to cover sustained programmatic/agentic load — but they are different calculations, not one number.

Context worth knowing: this proposal followed a policy arc. In February 2026, Anthropic [clarified its documentation](https://www.theregister.com/2026/02/20/anthropic_clarifies_ban_third_party_claude_access/) to explicitly prohibit using Free/Pro/Max OAuth credentials in third-party tools, including the Agent SDK. That restriction became actively enforced in April 2026, blocking or rate-limiting third-party agent tools like OpenClaw that had been running on subscription credentials. In May 2026, Anthropic [reversed the enforcement](https://venturebeat.com/technology/anthropic-reinstates-openclaw-and-third-party-agent-usage-on-claude-subscriptions-with-a-catch) and announced the metered Agent SDK credit pool described above as the replacement — which was itself then paused on June 15 before taking effect.

---

## What $200 Buys at Standard API Rates

The credit pool above never launched, so there is no $200 "Agent SDK budget" to spend. But the underlying question — what does $200 of Claude actually buy at list price — still matters for anyone running Agent SDK workloads through a pay-as-you-go API key (which is, and has always been, billed at standard rates regardless of the paused subscription plan). Per [Anthropic's pricing page](https://platform.claude.com/docs/en/about-claude/pricing), current list prices per million tokens (MTok) are:

| Model | Input | Output | $200 buys (input-only) | $200 buys (output-only) |
|---|---|---|---|---|
| claude-opus-4-7 | $5/MTok | $25/MTok | 40M tokens | 8M tokens |
| claude-sonnet-4-6 | $3/MTok | $15/MTok | 66.7M tokens | 13.3M tokens |
| claude-haiku-4-5 | $1/MTok | $5/MTok | 200M tokens | 40M tokens |

Real workloads mix input and output, so the true figure for any given pipeline falls between these two columns depending on how output-heavy the task is.

**Important for Opus 4.7 users:** Opus 4.7 uses an updated tokenizer that can produce more tokens than prior Opus versions for the same input text. Anthropic's own [Opus 4.7 announcement](https://www.anthropic.com/news/claude-opus-4-7) states the tokenizer maps the same input to "roughly 1.0–1.35x" as many tokens depending on content type, and the [pricing page](https://platform.claude.com/docs/en/about-claude/pricing) cites "approximately 30% more tokens for the same text" as the typical case. Either way, your effective throughput per dollar is somewhat lower than on pre-4.7 Opus models for the same input.

### CI/CD Pipelines Are the High-Risk Case for Cost, Regardless of Billing Model

A pipeline that runs an Opus 4.7 agent on every pull request can run up a large API bill quickly on a busy repository. The optimization strategies that matter most:

**Route by complexity.** Use Haiku 4.5 for classification, triage, summarization, and any step where the task complexity does not require a frontier model. Per Anthropic's pricing page, Haiku 4.5 is about 5x cheaper than Opus 4.7 per token on both input ($1 vs. $5/MTok) and output ($5 vs. $25/MTok). Most pipeline steps qualify.

**Token budget caps.** Setting an explicit per-invocation token or turn budget, rather than letting agents run to their natural stopping point, is good practice for controlling API spend regardless of billing model.

**Prompt caching.** For workflows that repeatedly send the same system prompt, tool definitions, or context, Anthropic prices cached-content reads (cache hits) at [0.1x the base input price — a 90% discount](https://platform.claude.com/docs/en/about-claude/pricing#prompt-caching) — versus a 1.25x–2x premium to write the cache in the first place. Realized savings depend on your cache hit rate: one published case study, [ProjectDiscovery](https://projectdiscovery.io/blog/how-we-cut-llm-cost-with-prompt-caching), reported cutting total LLM costs by roughly 59–70% after raising its Anthropic cache hit rate from 7% to 84%.

---

## Model Deprecations on June 15

Two models hit retirement on the same date, after a deprecation notice issued April 14 — Anthropic's policy is to give [at least 60 days' notice](https://platform.claude.com/docs/en/docs/about-claude/model-deprecations#notifications) before retiring a publicly released model, and April 14 to June 15 is 62 days:

| Model Being Retired | Replacement |
|---|---|
| `claude-sonnet-4-20250514` | `claude-sonnet-4-6` |
| `claude-opus-4-20250514` | `claude-opus-4-8` |

This table matches [Anthropic's own model deprecations page](https://platform.claude.com/docs/en/docs/about-claude/model-deprecations), which lists both models' status as "Retired" with an April 14, 2026 deprecation date and June 15, 2026 retirement date, and names these same two replacements.

After June 15, API calls using the old model ID strings fail with errors; per Anthropic's documentation, "Requests to retired models will fail" with no automatic fallback to a successor model.

To find affected code: `grep -r "claude-sonnet-4-20250514\|claude-opus-4-20250514" .` across your repositories. Check environment variables, config files, `.claude/settings.json`, Terraform and Kubernetes configs, and any deployment pipelines that set model IDs.

Anthropic recommends the replacements above for migration, with the sampling-parameter caveat for Opus 4.7+ noted below — see the [migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide) for full details.

---

## Breaking API Change: No More Temperature on Opus 4.7+

`temperature`, `top_p`, and `top_k` are **deprecated for Opus 4.7 and later**, including `claude-opus-4-8`. Per [Anthropic's API parameter deprecations table](https://platform.claude.com/docs/en/docs/about-claude/model-deprecations#api-parameter-deprecations), these parameters "return a 400 error when set to a non-default value on Claude 4.7 and later models."

That "non-default value" qualifier matters: sending the parameters at all is not what triggers the error — sending a non-default value is. The parameters still work normally on older models and on Sonnet/Haiku, which are not covered by this deprecation.

If your code explicitly sets any of these sampling parameters to a non-default value when calling Opus, you must remove or default those parameters before migrating to Opus 4.7 or later. Anthropic's documented recommendation is to omit the parameters entirely and use prompting to guide model behavior instead.

This affects prompting strategies too: use explicit prompt instructions to guide output style, rather than relying on temperature to introduce variation or constrain it.

---

## Action Checklist

**Required actions (these are real):**

- [ ] Grep codebase for `claude-sonnet-4-20250514` and `claude-opus-4-20250514` — update all call sites, both models are retired
- [ ] Review all Opus call sites: remove non-default `temperature`, `top_p`, and `top_k` values before migrating to `claude-opus-4-8`
- [ ] Run the updated model IDs in a test environment to verify no parameter errors

**Not required — the billing plan below was paused:**

- ~~Claim Agent SDK credits in Anthropic Console~~ — there is no credit to claim; [Anthropic paused this change](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan) before June 15
- ~~Decide on overflow billing for the credit pool~~ — there is no separate credit pool to configure

**Cost reduction steps (worth doing regardless of billing model, since API-rate usage is unaffected by the pause):**

- [ ] Audit CI pipeline agent invocations — identify steps suitable for Haiku 4.5 instead of Sonnet or Opus
- [ ] Set per-invocation token budget caps on Agent SDK calls
- [ ] Enable prompt caching for pipeline workloads with shared system prompts or context

~~**If you are on Enterprise Standard with no credit included:** verify whether your enterprise agreement includes Agent SDK access under a separate rate or contract~~ — moot, since the credit pool this referred to was paused before launch.

---

## What the Agent SDK Is

The [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/quickstart) (Python: `pip install claude-agent-sdk`, TypeScript: `npm install @anthropic-ai/claude-agent-sdk`) is a separate package from the Anthropic Client SDK. It gives you the Claude Code agent loop as a programmable library: built-in tools, multi-agent orchestration, MCP integration, session management, and lifecycle hooks.

It is NOT the lower-level `anthropic` Python/JS package. The `anthropic` package requires you to implement tool loops manually; the Agent SDK handles the loop autonomously. Either way, both draw from the same standard API/subscription billing described above — there is no separate credit pool for either, since that plan was paused.

---

## Bottom Line

Of the three changes scheduled for June 15, 2026, two happened and one didn't. The model retirements and the temperature-parameter change are both confirmed on [Anthropic's own documentation](https://platform.claude.com/docs/en/docs/about-claude/model-deprecations): `claude-sonnet-4-20250514` and `claude-opus-4-20250514` are retired (grep-and-replace to fix), and non-default `temperature`/`top_p`/`top_k` values now 400 on Opus 4.7+ (search-and-remove to fix).

The Agent SDK billing split — the change with the biggest structural implications — was announced and then paused by Anthropic before it took effect. [Anthropic's Help Center is explicit](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan) that "nothing has changed": there is no separate credit pool, nothing to claim, and Agent SDK usage still draws from ordinary subscription limits exactly as it did before the announcement. If you're running Agent SDK workloads on a pay-as-you-go API key rather than a subscription, none of this affects your billing either way — you've always paid standard list rates, and routing classification/triage steps to Haiku 4.5 (about 5x cheaper than Opus 4.7 per token) remains the highest-leverage single action for controlling that spend.
