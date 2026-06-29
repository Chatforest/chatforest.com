# Claude Opus 4.7 Fast Mode Deprecated: What Changes on July 24, and How to Migrate

> Anthropic deprecated fast mode for Claude Opus 4.7 on June 25, 2026, with removal on July 24. After that date, speed: "fast" on Opus 4.7 returns an error — no silent fallback. Opus 4.8 fast mode is the direct replacement, at 3x lower price.


Anthropic deprecated **fast mode for Claude Opus 4.7** on June 25, 2026. Removal is scheduled for **July 24, 2026**. After that date, any API request to `claude-opus-4-7` with `speed: "fast"` will return an error — it will not silently fall back to standard Opus 4.7 or to any other model.

The migration is one line of code, and it comes with a price cut: Opus 4.8 fast mode costs $10/$50 per million tokens input/output, versus $30/$150 on Opus 4.7 fast mode. That is a 3x reduction.

---

## What Fast Mode Actually Does

Fast mode is a premium runtime option that trades higher per-token price for up to 2.5x higher output tokens per second. You enable it by setting `speed: "fast"` alongside the `fast-mode-2026-02-01` beta header.

The use cases it fits: real-time streaming interfaces where latency per token matters more than cost, multi-agent pipelines where a fast synthesis step unblocks downstream work, and any workload where a human is waiting on the response.

---

## The Breaking Change on July 24

This is a hard removal, not a deprecation warning:

- Before July 24: `speed: "fast"` on Opus 4.7 continues to work
- After July 24: `speed: "fast"` on Opus 4.7 returns an **error**
- After July 24: there is **no automatic fallback** to standard Opus 4.7

If your production code calls `claude-opus-4-7` with `speed: "fast"` and you have not migrated, you will see request failures starting July 24.

This also applies to Claude Code workflows that use the `--fast` flag if they are pinned to an Opus 4.7 model ID.

---

## The Migration

Change the model ID and nothing else. The beta header and `speed` parameter syntax are identical on Opus 4.8.

**Before:**

```python
response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    speed="fast",
    betas=["fast-mode-2026-02-01"],
    messages=[{"role": "user", "content": "..."}],
)
```

**After:**

```python
response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    speed="fast",
    betas=["fast-mode-2026-02-01"],
    messages=[{"role": "user", "content": "..."}],
)
```

One change: `claude-opus-4-7` → `claude-opus-4-8`.

**Note:** Fast mode on Opus 4.8 is currently a research preview. If you do not already have access, contact your Anthropic account manager to enable it on your account before July 24.

---

## Pricing Comparison

| Configuration | Input (per M) | Output (per M) |
|---|---|---|
| Opus 4.7 standard | $15 | $75 |
| Opus 4.7 fast (deprecated) | $30 | $150 |
| Opus 4.8 standard | $15 | $75 |
| **Opus 4.8 fast (replacement)** | **$10** | **$50** |

Opus 4.8 fast mode is actually cheaper than Opus 4.8 standard on input, and cheaper than Opus 4.7 standard on output. The pricing model on Opus 4.8 was restructured when fast mode shipped with the May 28 release — the fast mode premium was absorbed into the overall price reduction.

For a workload running 100M output tokens per month on Opus 4.7 fast, the switch to Opus 4.8 fast drops monthly output cost from $15,000 to $5,000.

---

## What Opus 4.8 Adds Beyond Speed

Migration is not purely a defensive move. Opus 4.8 (released May 28, 2026) ships additional capabilities that Opus 4.7 does not have:

- **Dynamic Workflows**: the model can pause mid-generation to invoke tools and resume, rather than generating a tool call and stopping
- **1M token default context**: context window raised from 200K on Opus 4.7
- **Effort control**: `thinking_effort` parameter lets you trade reasoning depth for speed on non-fast requests
- **Near-Mythos alignment**: Opus 4.8 was trained with Constitutional AI iteration that brings its refusal calibration closer to Mythos 5's profile

If your existing Opus 4.7 fast workloads are simple generation tasks, you likely will not need Dynamic Workflows immediately. But the context increase alone may open routing decisions that were not available on 4.7.

---

## Checklist Before July 24

1. **Audit API calls**: grep your codebase for `claude-opus-4-7` to find all call sites; separately grep for `fast-mode-2026-02-01` to find any non-Opus 4.7 calls that use fast mode
2. **Confirm Opus 4.8 fast access**: if you do not see `fast-mode-2026-02-01` working on Opus 4.8 in your account, contact your account manager now — the research preview is not automatically enabled
3. **Update model ID**: one-line change per call site
4. **Update cost estimates**: your fast-mode budget should decrease by roughly 3x; update forecasting if it is in your billing model
5. **Test before deadline**: run your staging workload on Opus 4.8 fast before July 24 to catch any behavioral differences

---

## Timeline

| Date | Event |
|---|---|
| June 25, 2026 | Fast mode on Opus 4.7 deprecated |
| July 24, 2026 | Fast mode on Opus 4.7 removed; `speed: "fast"` returns error |

That is 26 days from today. The migration itself takes minutes. The lead time is for testing, access confirmation, and updating downstream cost tracking.

