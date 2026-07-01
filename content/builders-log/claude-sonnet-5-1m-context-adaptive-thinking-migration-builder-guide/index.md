---
title: "Claude Sonnet 5: 1M Context, Adaptive Thinking by Default, and Three Breaking Changes Every Builder Must Know"
date: 2026-07-01
description: "Anthropic's Claude Sonnet 5 launched June 30 as the new Claude Code default. Here's what changed, what breaks, and how to migrate — including the hidden tokenizer cost shift."
tags: ["anthropic", "claude", "claude-code", "api", "migration", "builders-log"]
slug: claude-sonnet-5-1m-context-adaptive-thinking-migration-builder-guide
---

Anthropic shipped Claude Sonnet 5 on June 30, 2026. It is now the default model for free and Pro users in Claude Code, and it is available immediately on the API, AWS Bedrock, Google Cloud Vertex AI, and Microsoft Foundry (preview). The model ID is `claude-sonnet-5`.

Sonnet 5 is a genuine capability upgrade — but it is not a frictionless drop-in. Three behavior changes are breaking, and a new tokenizer creates a hidden cost shift that will surprise builders who assume per-token pricing means per-text cost is the same.

Here is what you need to know before you migrate.

---

## What Changed: The Three Breaking Changes

### 1. Adaptive Thinking Is On by Default

On Claude Sonnet 4.6, requests without a `thinking` field ran without thinking. On Claude Sonnet 5, the same requests now run with **adaptive thinking** — the model decides when to reason before answering.

This changes output behavior even if you make zero code changes. Prompts that ran quickly without thinking will now incur thinking tokens. Any `max_tokens` limit you set is a hard cap on **total output** — thinking tokens plus response text — so a limit tuned for 4.6 may truncate your actual response on Sonnet 5.

To restore the old no-thinking behavior, pass explicitly:

```python
thinking = {"type": "disabled"}
```

### 2. Sampling Parameters Return a 400 Error

Setting `temperature`, `top_p`, or `top_k` to a **non-default value** now returns an HTTP 400 error. This constraint was introduced for Opus-class models earlier in 2026; it now applies to Sonnet-tier for the first time.

If your code sets any of these parameters, remove them before migrating. The default value (or omitting the parameter entirely) is accepted. Use system prompt instructions to shape model behavior instead.

### 3. Manual Extended Thinking Is Removed

`thinking: {type: "enabled", budget_tokens: N}` was deprecated on Claude Sonnet 4.6. On Sonnet 5, it returns a 400 error and is gone. Migrate to adaptive thinking with the effort parameter:

```python
# Not supported (returns 400)
thinking = {"type": "enabled", "budget_tokens": 32000}

# Use this instead
thinking = {"type": "adaptive"}
# or with effort level:
# effort = "high"
```

---

## The Hidden Cost Change: New Tokenizer

Claude Sonnet 5 uses a **new tokenizer**. The same input text produces approximately **30% more tokens** than on Claude Sonnet 4.6.

Per-token pricing is unchanged at $3/$15 per million input/output tokens (with $2/$10 introductory pricing through August 31, 2026). But because more tokens represent the same text, the cost of an equivalent request can be meaningfully higher than on Sonnet 4.6.

Practical implications:

- **Token counts in `usage` fields will be higher** for the same prompts. Don't reuse cached counts from earlier models.
- **The 1M context window holds less text than before.** The window is nominally larger (1M vs 200k on 4.6), but each token covers less text, so available text capacity doesn't scale linearly with the token number.
- **`max_tokens` budgets may truncate.** If you sized output limits close to your expected output length on 4.6, revisit them.

Use the [token counting endpoint](https://platform.claude.com/docs/en/build-with-claude/token-counting) to recount your actual prompts against Sonnet 5 before deploying.

---

## What You Get: Performance

Sonnet 5 narrows the gap to Opus 4.8 significantly at a lower price point:

| Model | Agentic Coding | Per Million Input/Output |
|---|---|---|
| Claude Opus 4.8 | 69.2% | $15 / $75 |
| Claude Sonnet 5 | 63.2% | $3 / $15 (intro: $2 / $10) |
| Claude Sonnet 4.6 | 58.1% | $3 / $15 |

Sonnet 5 also slightly outperforms Opus 4.8 on knowledge work benchmarks and shows lower rates of hallucination and deceptive behavior compared to Sonnet 4.6. It excels at autonomous task completion, finishing complex multi-step work where predecessors stopped midway.

For many agent workloads, Sonnet 5 is now the right default: close to Opus 4.8 capability, significantly cheaper, with the 1M context window that previously required a larger model.

---

## Cybersecurity Safeguards

Sonnet 5 is the **first Sonnet-tier model with real-time cybersecurity safeguards**. Requests involving prohibited or high-risk cybersecurity topics may be refused. These refusals return as HTTP 200 responses with `stop_reason: "refusal"` — not errors — which is consistent with the billing change Anthropic made recently (no charge on refusals without output).

If you are building security tooling, test your prompts against Sonnet 5 before migrating. Sonnet 5's safeguards are less strict than Opus 4.8's for certain tasks, but they are new at this tier and may affect workloads that previously ran cleanly on Sonnet 4.6.

---

## Availability

At launch, Claude Sonnet 5 is available on:

- **Claude API** — all customers
- **AWS** — Amazon Bedrock (new surface) and Claude Platform on AWS
- **Google Cloud** — Vertex AI
- **Microsoft Foundry** — preview

**Not available on:** Amazon Bedrock legacy (the `InvokeModel` and `Converse` APIs) or Priority Tier (Tier was available on Sonnet 4.6 but is not supported on Sonnet 5).

---

## Migration Checklist

1. **Update model ID:** `claude-sonnet-4-6` → `claude-sonnet-5`
2. **Remove sampling parameters:** delete any `temperature`, `top_p`, or `top_k` settings
3. **Migrate extended thinking:** replace `thinking: {type: "enabled", budget_tokens: N}` with `thinking: {type: "adaptive"}`
4. **Recount token budgets:** use the token counting API; expect ~30% more tokens for same text
5. **Revisit `max_tokens` limits:** adaptive thinking now consumes from the same budget as response text
6. **Test cybersecurity-adjacent workloads:** new safeguards may refuse prompts that ran on 4.6

If you want thinking off entirely, pass `thinking: {type: "disabled"}` explicitly.

---

## The Bigger Picture

Sonnet 5's launch continues a pattern: Anthropic is pushing Sonnet-class models toward the capability ceiling previously held by Opus, while holding Opus pricing higher and using it to signal frontier capability. The 1M context window is now standard at Sonnet pricing. Adaptive thinking is now the default behavior, not an opt-in.

For most production agent workloads — coding assistants, document processing, multi-step reasoning pipelines — Sonnet 5 is likely the correct model choice today. The introductory pricing through August 31 makes this an especially good window to migrate and benchmark before standard rates kick in.

Run your prompts through the token counter, fix the three breaking changes, and give your agents 1M context to work with.

---

*Claude Sonnet 5 documentation: [What's New in Sonnet 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5) — Pricing: $2/$10 per million input/output through August 31, 2026; $3/$15 standard.*
