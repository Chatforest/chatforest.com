# Anthropic Cache Diagnostics Beta: Find Exactly Why Your Prompt Cache Missed

> Anthropic's cache diagnostics beta adds a cache_miss_reason field to API responses. Pass your previous response ID and get a machine-readable explanation of exactly where your prompt prefix diverged.


Prompt caching cuts Claude API costs by up to 90% on repeated context — but only when the beginning of your prompt is byte-for-byte identical across turns. Until now, the only signal that a cache miss occurred was `usage.cache_read_input_tokens` dropping to zero. No reason. No location. No path to a fix.

Anthropic's **cache diagnostics beta**, launched May 13, 2026, closes that gap. Pass the `id` of your previous response on the next request and the API tells you exactly what changed: the model, the system prompt, the tools, or the message history. You can fix the root cause instead of guessing.

---

## The problem cache diagnostics solves

Prompt caching requires the *beginning* of your prompt to be byte-for-byte identical to a recent request. A single invisible difference invalidates everything after it:

- A timestamp or request ID interpolated into the system prompt
- Tools returned in a different order (JSON serialization order is not guaranteed in all languages)
- A router or fallback silently switching models between turns
- Assistant history echoed back with whitespace differences or re-serialized tool calls

Before cache diagnostics, you could tell a miss happened. You couldn't tell why. The only remediation was manual diff-and-compare.

---

## How to opt in

Include the beta header `cache-diagnosis-2026-04-07` on every request. On the first turn, pass `diagnostics.previous_message_id: null` to opt in without a prior message. On subsequent turns, pass the `id` from the previous response.

```python
import anthropic

client = anthropic.Anthropic()

SYSTEM = "You are an assistant working through a large document. <document>...</document>"

# Turn 1 — opt in, no prior message to compare
r1 = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    cache_control={"type": "ephemeral"},
    system=SYSTEM,
    messages=[{"role": "user", "content": "Summarize section 1."}],
    diagnostics={"previous_message_id": None},
    betas=["cache-diagnosis-2026-04-07"],
)

# Turn 2 — reference the previous response id
r2 = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    cache_control={"type": "ephemeral"},
    system=SYSTEM,
    messages=[
        {"role": "user", "content": "Summarize section 1."},
        {"role": "assistant", "content": r1.content},
        {"role": "user", "content": "Now summarize section 2."},
    ],
    diagnostics={"previous_message_id": r1.id},
    betas=["cache-diagnosis-2026-04-07"],
)

if r2.diagnostics is None:
    print("No divergence detected — prefix is stable.")
elif r2.diagnostics.cache_miss_reason is None:
    print("Comparison still running — check next turn.")
else:
    print(f"Cache miss: {r2.diagnostics.cache_miss_reason.type}")
```

The `diagnostics` object appears on the response `Message`. For streaming, it arrives on the `message_start` event.

---

## What you get back

The `diagnostics` field has four possible states:

| Value | Meaning |
|---|---|
| field absent | Beta header was missing, or `diagnostics` wasn't passed |
| `null` | First turn (`previous_message_id: null`), or comparison found no divergence |
| `{"cache_miss_reason": null}` | Comparison still running — check the next turn |
| `{"cache_miss_reason": {...}}` | Divergence found — type tells you where |

When there's a miss, the response looks like this:

```json
{
  "diagnostics": {
    "cache_miss_reason": {
      "type": "system_changed",
      "cache_missed_input_tokens": 41850
    }
  }
}
```

`cache_missed_input_tokens` estimates how many input tokens fell after the divergence point. It's a magnitude indicator, not a billing number — use it to gauge the cost impact, not to reconcile invoices.

---

## The six miss reason types

The API reports the **earliest** divergence only. Fix the first one before hunting for the next.

### `system_changed`

The `system` parameter differs between turns. This is the most common cause in practice. A timestamp, request UUID, or session ID is being interpolated into the system prompt.

**Fix:** Make the system prompt a byte-stable constant. Move dynamic values — user names, current time, session identifiers — into the first `user` message *after* your `cache_control` breakpoint.

```python
# Bad: timestamp invalidates cache every minute
system = f"Today is {datetime.now().strftime('%Y-%m-%d %H:%M')}. You are..."

# Good: dynamic context goes in the user turn, not the system prompt
system = "You are an assistant. Today's context follows in the user message."
messages = [{"role": "user", "content": f"Today is {today}. Now: {user_query}"}]
```

### `tools_changed`

The `tools` array differs. Tools were added, removed, reordered, or their `input_schema` JSON was serialized differently between requests.

**Fix:** Send the same tool list on every turn in a fixed order. Deterministically serialize tool schemas — sort JSON object keys before sending.

```python
import json

def stable_tool(tool_dict):
    return json.loads(json.dumps(tool_dict, sort_keys=True))

tools = [stable_tool(t) for t in my_tools]
```

### `model_changed`

The `model` parameter is different. A router, A/B test, or fallback logic selected a different model. The prompt cache is per-model — there is no cross-model cache sharing.

**Fix:** Hold the model constant within a cached conversation. If you need a fallback, treat the fallback turn as a fresh cache start.

### `messages_changed`

The model, system, and tools all match, but something earlier in `messages` was altered rather than appended to. Typical causes: conversation history was truncated, assistant turns were re-serialized differently, or `tool_result` blocks weren't echoed back verbatim.

**Fix:** Treat history as append-only. Echo assistant `content` and tool results back exactly as received — don't re-serialize, don't edit earlier turns.

### `previous_message_not_found`

No fingerprint exists for the supplied `previous_message_id`. This is not evidence that your request changed — it means the API can't compare. Common causes: the prior request didn't include the beta header, it came from a different workspace, or too much time passed.

**Fix:** Include the beta header on every turn, keep consecutive turns reasonably close together, and verify you're using the same API key workspace.

### `unavailable`

Diagnostics couldn't produce a result. This covers: non-`*_changed` parameter differences (`tool_choice`, `thinking`, `context_management`, active beta headers), very long conversations where the divergence is beyond the comparison horizon, and transient conditions.

If you see this persistently after checking the obvious suspects, consult the [prompt caching troubleshooting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#troubleshooting-common-issues).

---

## Combining diagnostics with usage

`diagnostics` answers "did my request change?" while `usage.cache_read_input_tokens` answers "did the cache hit?" Use both together:

| Diagnostics | Cache read tokens | What it means |
|---|---|---|
| `null` | High | Working correctly — prefix is stable and the cache hit |
| `null` | Low or zero | Request matches but the cache entry expired — shorten turn gaps or use the 1-hour TTL option |
| `*_changed` | Low or zero | Your bug — the request changed; fix the cause |
| `*_changed` | High | Change happened late in the prompt; an earlier `cache_control` breakpoint still hit — worth fixing but low priority |

---

## Threading through a conversation loop

For multi-turn conversations, carry the previous response `id` forward on every turn:

```python
messages = []
prev_id = None

for user_msg in ["Summarize section 1.", "Now section 2.", "Now section 3."]:
    messages.append({"role": "user", "content": user_msg})

    r = client.beta.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        cache_control={"type": "ephemeral"},
        system=SYSTEM,
        messages=messages,
        diagnostics={"previous_message_id": prev_id},
        betas=["cache-diagnosis-2026-04-07"],
    )

    if r.diagnostics and r.diagnostics.cache_miss_reason:
        reason = r.diagnostics.cache_miss_reason
        print(f"Turn miss: {reason.type} (~{reason.cache_missed_input_tokens:,} tokens lost)")

    messages.append({"role": "assistant", "content": r.content})
    prev_id = r.id
```

The first turn always returns `diagnostics: null` — there's nothing to compare against. Diagnostics become meaningful from turn 2 onward.

---

## Current limitations

- **Beta:** Field names and semantics may change before GA.
- **Claude API only:** Not available on Amazon Bedrock or Google Cloud Vertex AI.
- **Fingerprints expire:** Run diagnostic comparisons between closely spaced requests; if too much time passes, you'll get `previous_message_not_found`.
- **Same workspace:** The previous request must be from the same organization and workspace as the current one.
- **First divergence only:** The API reports the earliest divergence point. Fix it, then re-run — later divergences may be hidden behind the first.
- **ZDR eligible:** Fingerprints contain only cryptographic hashes and token-count estimates — no raw prompt content is stored.

---

## Who should use this

Cache diagnostics is targeted at builders who:

- **Are spending on cache writes that aren't hitting** — you see cache creation tokens going up but reads not following. `cache_missed_input_tokens` tells you how much prefix you're burning per miss.
- **Run agentic loops** — multi-step workflows where tool calls inject dynamic content that can silently break the stable prefix.
- **Are migrating between models** — if your code has any routing or fallback logic, `model_changed` will surface it immediately.
- **Are using third-party SDKs or wrappers** — framework layers sometimes re-serialize tool schemas or reorder messages. Diagnostics finds this without needing to instrument the framework.

Enable the beta header in staging, run your workflow, and check the `cache_miss_reason` on turn 2+. Even one `system_changed` fix on a large system prompt can eliminate thousands of dollars per month in unnecessary cache write costs.

---

*Cache diagnostics is in public beta as of May 13, 2026. Feature details sourced from the [official Anthropic API documentation](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics).*

