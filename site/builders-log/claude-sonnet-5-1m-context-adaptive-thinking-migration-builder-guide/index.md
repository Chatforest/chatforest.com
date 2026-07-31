# Claude Sonnet 5: 1M Context, Adaptive Thinking by Default, and Three Breaking Changes Every Builder Must Know

> Anthropic's Claude Sonnet 5 launched June 30 as the new Claude Code default. Here's what changed, what breaks, and how to migrate — including the hidden tokenizer cost shift.


Anthropic [shipped Claude Sonnet 5 on June 30, 2026](https://www.anthropic.com/news/claude-sonnet-5). It is now the default model for free and Pro users in Claude Code, and it is available immediately on the API, AWS Bedrock, and Google Cloud Vertex AI, with [Microsoft Foundry support following shortly after launch](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5#availability). The model ID is [`claude-sonnet-5`](https://platform.claude.com/docs/en/release-notes/overview).

Sonnet 5 is a genuine capability upgrade — but it is not a frictionless drop-in. Three behavior changes are breaking, and a new tokenizer creates a hidden cost shift that will surprise builders who assume per-token pricing means per-text cost is the same.

Here is what you need to know before you migrate.

---

## What Changed: The Three Breaking Changes

### 1. Adaptive Thinking Is On by Default

On Claude Sonnet 4.6, requests without a `thinking` field ran without thinking. On Claude Sonnet 5, the same requests now run with [**adaptive thinking**](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5#adaptive-thinking-on-by-default) — the model decides when to reason before answering.

This changes output behavior even if you make zero code changes. Prompts that ran quickly without thinking will now incur thinking tokens. Any `max_tokens` limit you set is a hard cap on **total output** — thinking tokens plus response text — so a limit tuned for 4.6 may truncate your actual response on Sonnet 5.

To restore the old no-thinking behavior, pass explicitly:

```python
thinking = {"type": "disabled"}
```

### 2. Sampling Parameters Return a 400 Error

Setting `temperature`, `top_p`, or `top_k` to a **non-default value** now returns an HTTP 400 error. [This constraint was previously introduced on Claude Opus 4.7](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5#sampling-parameters-not-accepted); it now applies to Sonnet-tier for the first time.

If your code sets any of these parameters, remove them before migrating. The default value (or omitting the parameter entirely) is accepted. Use system prompt instructions to shape model behavior instead.

### 3. Manual Extended Thinking Is Removed

`thinking: {type: "enabled", budget_tokens: N}` was deprecated on Claude Sonnet 4.6. On Sonnet 5, [it returns a 400 error and is gone](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5#manual-extended-thinking-removed). Migrate to adaptive thinking with the effort parameter:

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

Claude Sonnet 5 uses a **new tokenizer**. [The same input text produces approximately **30% more tokens** than on Claude Sonnet 4.6](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5#new-tokenizer); the exact increase depends on the content and workload shape.

[Per-token pricing is unchanged at $3/$15 per million input/output tokens (with $2/$10 introductory pricing through August 31, 2026)](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5#pricing). But because more tokens represent the same text, the cost of an equivalent request can be meaningfully higher than on Sonnet 4.6.

Practical implications:

- **Token counts in `usage` fields will be higher** for the same prompts. Don't reuse cached counts from earlier models.
- **The 1M context window holds less text than before.** The window size itself is unchanged from Sonnet 4.6 — [Claude Sonnet 4.6 already had a 1M-token context window generally available at standard pricing, since March 13, 2026](https://platform.claude.com/docs/en/release-notes/overview) — but each token now covers less text under the new tokenizer, so the same 1M-token window holds less actual text than it did on 4.6.
- **`max_tokens` budgets may truncate.** If you sized output limits close to your expected output length on 4.6, revisit them.

Use the [token counting endpoint](https://platform.claude.com/docs/en/build-with-claude/token-counting) to recount your actual prompts against Sonnet 5 before deploying.

---

## What You Get: Performance

Sonnet 5 narrows the gap to Opus 4.8 significantly at a lower price point. Per [Anthropic's Claude Sonnet 5 System Card (June 30, 2026)](https://www-cdn.anthropic.com/9e6a1044980d8c4ed85669faf9c2a8342e2e9f1e/Claude%20Sonnet%205%20System%20Card.pdf):

| Model | SWE-bench Pro | Per Million Input/Output |
|---|---|---|
| Claude Opus 4.8 | 69.2% | $15 / $75 |
| Claude Sonnet 5 | 63.2% | $3 / $15 (intro: $2 / $10) |
| Claude Sonnet 4.6 | 58.1% | $3 / $15 |

Sonnet 5 also [slightly outperforms Opus 4.8 on the GDPval-AA v2 knowledge-work benchmark (1,618 vs. 1,615)](https://www-cdn.anthropic.com/9e6a1044980d8c4ed85669faf9c2a8342e2e9f1e/Claude%20Sonnet%205%20System%20Card.pdf) — a narrow lead, not a decisive one — and [shows lower rates of hallucination, sycophancy, and other undesirable behaviors compared to Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-5) on Anthropic's automated behavioral audit. It excels at autonomous task completion, finishing complex multi-step work where predecessors stopped midway.

For many agent workloads, Sonnet 5 is now the right default: close to Opus 4.8 capability, at a significantly cheaper price, with the same 1M-token context window Sonnet-tier models have carried since Sonnet 4.6.

---

## Cybersecurity Safeguards

Sonnet 5 is [the **first Sonnet-tier model with real-time cybersecurity safeguards**](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5#cybersecurity-safeguards). Requests involving prohibited or high-risk cybersecurity topics may be refused. These refusals return as HTTP 200 responses with `stop_reason: "refusal"` — not errors — and, separately, [a billing change Anthropic shipped June 2, 2026 means a request refused before any output is generated is not billed at all](https://platform.claude.com/docs/en/release-notes/overview) (a refusal that occurs after partial output has streamed still bills for that output).

If you are building security tooling, test your prompts against Sonnet 5 before migrating. Anthropic recommends Opus 4.8 for legitimate cybersecurity research that needs lighter guardrails, since [Sonnet 5 ships with its cyber safeguards on and no comparable reduced-guardrail option](https://www.anthropic.com/news/claude-sonnet-5) — new at this tier, and may affect workloads that previously ran cleanly on Sonnet 4.6.

---

## Availability

At launch, [Claude Sonnet 5 is available on](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5#availability):

- **Claude API** — all customers
- **AWS** — Claude in Amazon Bedrock (including the `InvokeModel` API) and Claude Platform on AWS
- **Google Cloud** — Vertex AI
- **Microsoft Foundry**

**Not available on:** the legacy "Claude on Amazon Bedrock (Opus 4.6 and earlier)" integration, or Priority Tier (Priority Tier was available on Sonnet 4.6 but is not supported on Sonnet 5).

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

Sonnet 5's launch continues a pattern: Anthropic is pushing Sonnet-class models toward the capability ceiling previously held by Opus, while holding Opus pricing higher and using it to signal frontier capability. [The 1M context window has been standard at Sonnet pricing since Sonnet 4.6](https://platform.claude.com/docs/en/release-notes/overview), and Sonnet 5 carries it forward. Adaptive thinking is now the default behavior, not an opt-in.

For most production agent workloads — coding assistants, document processing, multi-step reasoning pipelines — Sonnet 5 is likely the correct model choice today. The introductory pricing through August 31 makes this an especially good window to migrate and benchmark before standard rates kick in.

Run your prompts through the token counter, fix the three breaking changes, and give your agents 1M context to work with.

---

*Claude Sonnet 5 documentation: [What's New in Sonnet 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5) — Pricing: $2/$10 per million input/output through August 31, 2026; $3/$15 standard.*

