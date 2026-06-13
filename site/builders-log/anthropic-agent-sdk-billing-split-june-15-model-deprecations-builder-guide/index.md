# Anthropic Agent SDK Billing Split June 15: Two Pools, Two Models Retiring, One Breaking Change

> On June 15, Anthropic separates interactive and Agent SDK usage into independent billing pools, retires claude-sonnet-4-20250514 and claude-opus-4-20250514, and drops temperature/top_p support on Opus 4.7+. Here is what builders need to do before the deadline.


> **Update — June 15, 2026 (post-mortem):** All three changes went live as scheduled. Both model retirements are confirmed — API calls to `claude-sonnet-4-20250514` and `claude-opus-4-20250514` now return hard errors with no automatic fallback. The billing split is live. Two failure modes emerged in the community: (1) builders who missed Anthropic's claim email did not receive their June credit allocation, since credits required a one-time manual claim and were not auto-applied; (2) the simultaneous retirement and billing change created compounded confusion for teams that had deferred preparation, who hit deprecated model errors and unexpected billing behavior at the same time. If you are debugging today, check both: your model ID strings and your credit pool status in the Anthropic Console.

Three things happen on June 15, 2026, that affect builders using Anthropic's Claude:

1. **The billing split** — Agent SDK usage moves into its own credit pool, separate from interactive Claude.
2. **Two model retirements** — `claude-sonnet-4-20250514` and `claude-opus-4-20250514` stop accepting API calls.
3. **A breaking API parameter change** — `temperature`, `top_p`, and `top_k` return 400 errors on Opus 4.7 and later.

This post covers each in detail and ends with a checklist.

---

## The Billing Split

### Before June 15

All Claude usage — the claude.ai website, the Claude Code terminal, Agent SDK runs, `claude -p` scripts, GitHub Actions, and third-party apps like OpenClaw and Zed — drew from a single subscription pool. A Max 20x subscriber paying $200/month could run arbitrarily heavy Agent SDK workloads until the unified cap was hit.

### After June 15

Two independent pools with no cross-pool sharing:

**Interactive pool (unchanged behavior):**
- claude.ai web, desktop, and mobile
- Interactive Claude Code terminal (when you are the human in the loop)
- Claude Cowork

**Agent SDK credit pool (new):**
- Claude Agent SDK (`claude-agent-sdk` Python/TypeScript packages)
- `claude -p` in non-interactive mode
- Claude Code in GitHub Actions
- Third-party apps authenticating via Agent SDK: OpenClaw, Conductor, Zed in agent mode, Jean, T3 Code, and others

### Monthly Credit Amounts

| Plan | Monthly Agent SDK Credit |
|---|---|
| Pro ($20/mo) | $20 |
| Max 5x ($100/mo) | $100 |
| Max 20x ($200/mo) | $200 |
| Team Standard | $20/seat |
| Team Premium | $100/seat |
| Enterprise Standard | No credit included |
| Enterprise Premium | $200/seat |

Credits are billed at standard API list rates. They do not pool across team members. They do not roll over month to month. When exhausted, usage stops by default — unless you explicitly enable an overflow toggle that charges standard API rates beyond the credit amount.

### The Required Claim Action

Credits require a **one-time manual claim before June 15**. They are not automatically applied to your account. After claiming, they auto-refresh monthly. Anthropic has not made this frictionless — you need to navigate to your account settings and claim the credits before the deadline, or you will lose the June allocation.

Check the Anthropic Console billing page to confirm whether you have claimed.

### Why Anthropic Made This Change

Community analysis identified that Max 20x subscribers running heavy Sonnet automation were extracting over $5,800 of API-equivalent value per month on a $200 subscription — an approximately 150x to 175x subsidy. This was not a sustainable unit economics position.

Context worth knowing: this change is the third act in a policy arc. In February 2026, Anthropic banned third-party agents from using subscription credentials entirely. They tightened the ban further in April. In May, they reversed course — reinstating third-party access, but under the metered credit pool rather than the previous flat-rate subsidy. The net result for heavy users is metered access at known rates instead of effectively unlimited access.

---

## Token Budgets Under the New Pools

The credit amounts translate to approximate token budgets at current list pricing:

| Model | Approximate tokens at $200 credit |
|---|---|
| claude-opus-4-7 | ~13.3M tokens |
| claude-sonnet-4-6 | ~22M tokens |
| claude-haiku-4-5 | ~67M tokens |

**Important for Opus 4.7 users:** Opus 4.7 produces 32–47% more tokens than prior Opus versions on identical input text, due to changes in the tokenizer. Your effective throughput is lower than prior Opus models at the same credit amount.

### CI/CD Pipelines Are the High-Risk Case

A pipeline that runs an Opus 4.7 agent on every pull request can exhaust $200 of credit within days on a busy repository. The optimization strategies that matter most:

**Route by complexity.** Use Haiku 4.5 for classification, triage, summarization, and any step where the task complexity does not require a frontier model. Haiku is approximately 15x cheaper than Opus 4.7 per token. Most pipeline steps qualify.

**Token budget caps.** The Agent SDK supports per-session token limits. Set an explicit budget for each invocation rather than letting agents run to their natural stopping point. This is good practice regardless of billing model; it becomes essential under per-credit metering.

**Prompt caching.** For workflows that repeatedly send the same system prompt, tool definitions, or context, prompt caching reduces input token costs by 70–90% on cached content. The Agent SDK's session resume (`session_id`) parameter preserves context across runs, enabling cache reuse across pipeline invocations on the same repository.

---

## Model Deprecations on June 15

Two models hit retirement on the same date, after a 60-day deprecation notice issued April 14:

| Model Being Retired | Replacement |
|---|---|
| `claude-sonnet-4-20250514` | `claude-sonnet-4-6` |
| `claude-opus-4-20250514` | `claude-opus-4-8` |

After June 15, API calls using the old model ID strings will fail with errors. There is no automatic fallback.

To find affected code: `grep -r "claude-sonnet-4-20250514\|claude-opus-4-20250514" .` across your repositories. Check environment variables, config files, `.claude/settings.json`, Terraform and Kubernetes configs, and any deployment pipelines that set model IDs.

Both replacements are drop-in compatible at the API interface level, with the caveat for Opus 4.7+ noted below.

---

## Breaking API Change: No More Temperature on Opus 4.7+

`temperature`, `top_p`, and `top_k` are **deprecated for Opus 4.7 and later**, including `claude-opus-4-8`.

Sending these parameters to Opus 4.7+ returns an HTTP 400 error. The parameters still work on older models and on Sonnet/Haiku.

If your code explicitly sets any of these sampling parameters when calling Opus, you must remove those parameters before migrating to Opus 4.7 or later. The Agent SDK type definitions still accept these parameters (for backward compatibility with older models), but passing them on newer Opus models is a runtime error, not a compile-time error.

This affects prompting strategies too: use explicit prompt instructions to guide output style, rather than relying on temperature to introduce variation or constrain it.

---

## Action Checklist

**Before June 15 — required actions:**

- [ ] Claim Agent SDK credits in Anthropic Console (one-time action, auto-refreshes afterward)
- [ ] Decide whether to enable overflow billing for the credit pool, or let it hard-stop
- [ ] Grep codebase for `claude-sonnet-4-20250514` and `claude-opus-4-20250514` — update all call sites
- [ ] Review all Opus call sites: remove `temperature`, `top_p`, and `top_k` parameters if present before migrating to `claude-opus-4-8`
- [ ] Run the updated model IDs in a test environment against the Responses API to verify no parameter errors

**Cost reduction steps (do after migration is stable):**

- [ ] Audit CI pipeline agent invocations — identify steps suitable for Haiku 4.5 instead of Sonnet or Opus
- [ ] Set per-session token budget caps on Agent SDK calls
- [ ] Enable prompt caching for pipeline workloads with shared system prompts or context

**If you are on Enterprise Standard with no credit included:**
- [ ] Verify whether your enterprise agreement includes Agent SDK access under a separate rate or contract — contact Anthropic support to confirm before June 15

---

## What the Agent SDK Is

The Claude Agent SDK (Python: `pip install claude-agent-sdk`, TypeScript: `npm install @anthropic-ai/claude-agent-sdk`) is a separate package from the Anthropic Client SDK. It gives you the Claude Code agent loop as a programmable library: built-in tools, multi-agent via `AgentDefinition`, MCP integration, session management, and lifecycle hooks.

It is NOT the lower-level `anthropic` Python/JS package. The `anthropic` package requires you to implement tool loops manually. The Agent SDK handles the loop autonomously. If your code imports only `anthropic` and calls `client.messages.create()` directly, it draws from standard API billing, not the credit pool.

---

## Bottom Line

The billing split, the model retirements, and the temperature parameter removal all land on June 15. The model update is a grep-and-replace. The temperature fix is a search-and-remove. Claiming credits requires a one-time visit to the Console.

The structural change is the billing split. For interactive users, nothing changes. For builders running automated pipelines or multi-agent workflows against Claude, every invocation now draws from a finite monthly credit at API list prices. The credit amounts are real — $200 of Sonnet 4.6 covers roughly 22M tokens — but they are not infinite. Routing classification and triage steps to Haiku 4.5 is the highest-leverage single action for extending that budget.

