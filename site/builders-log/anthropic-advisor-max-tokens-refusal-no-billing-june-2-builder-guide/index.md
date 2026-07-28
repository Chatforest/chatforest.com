# Anthropic June 2: Advisor max_tokens Cap and Free Zero-Output Refusals

> Two billing improvements shipped June 2, 2026: cap advisor token spend with tools[].max_tokens (2048 recommended — 7x reduction, near-zero truncation), and zero charge when stop_reason: 'refusal' arrives before Claude generates any output.


Two changes shipped to the Claude API on [June 2, 2026](https://platform.claude.com/docs/en/release-notes/api#june-2-2026), both affecting cost. The first gives builders a hard ceiling on advisor token spend. The second removes charges for requests that never produce output.

## Advisor tool: `max_tokens` per call

The [advisor tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool) was introduced in April 2026 beta ([our earlier write-up](/builders-log/anthropic-advisor-tool-opus-sonnet-haiku-cost-intelligence-tradeoff/)). Quick recap: a cheap executor model (Sonnet or Haiku) runs the full workflow and calls an Opus advisor mid-generation for strategic guidance. One API call, no separate orchestration layer.

The June 2 addition is a [`max_tokens` parameter on the tool definition itself](https://platform.claude.com/docs/en/release-notes/api#june-2-2026).

### The problem it solves

The top-level `max_tokens` in a Messages request caps executor output only. It has no effect on the advisor model's sub-inference. [Advisor output is typically 400–700 text tokens or 1,400–1,800 tokens including thinking](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#usage-and-billing) — but without a cap, that's variable and unbounded. For cost-sensitive workloads where the advisor's guidance doesn't need to be exhaustive, that variability is the largest line item per agentic turn.

### How to set it

Add `max_tokens` to the tool definition, not the top-level request ([capping advisor output](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#capping-advisor-output)):

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,                        # executor output cap (unchanged)
    betas=["advisor-tool-2026-03-01"],
    tools=[
        {
            "type": "advisor_20260301",
            "name": "advisor",
            "model": "claude-opus-4-8",
            "max_tokens": 2048,             # NEW: caps advisor (thinking + text)
        }
    ],
    messages=[{"role": "user", "content": your_task}]
)
```

[The cap applies to the advisor's total output — thinking plus text — per call. It is not shared across multiple advisor calls in the same request. Minimum value is 1024. Setting it above the advisor model's own output cap returns a 400 error.](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#capping-advisor-output)

### What happens when the cap is hit

The advisor result block carries `stop_reason: "max_tokens"` when truncated, and [the API appends a literal notice to the advice text](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#capping-advisor-output) so the executor sees it:

```json
{
  "type": "advisor_tool_result",
  "tool_use_id": "srvtoolu_abc123",
  "content": {
    "type": "advisor_result",
    "text": "Use a channel-based coordination pattern. The tricky part is\n\n[Advisor output truncated at max_tokens=2048.]",
    "stop_reason": "max_tokens"
  }
}
```

When the advisor finishes cleanly, `stop_reason` is `"end_turn"`. When you don't set `max_tokens` at all, the field is omitted entirely. Branch on it to decide whether to raise the cap or let the executor proceed with partial guidance.

### What to set it to

[Anthropic's benchmarks on a hard reasoning task (n = 40 per configuration)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#capping-advisor-output):

| `max_tokens` setting | Mean advisor output | Truncation rate |
|---|---|---|
| Unset (default) | ~4,200–5,900 tokens | n/a |
| 2048 | ~630–840 tokens | ~0% |
| 1024 | ~370–480 tokens | ~10% |

**Recommended starting point: 2048.** Roughly 7× reduction in mean advisor output with near-zero truncation and no detectable quality degradation. At 1024 you get roughly 10× reduction but around 10% of calls get cut mid-thought. (These figures are specific to a hard-reasoning benchmark — a heavier workload than the 1,400–1,800 "typical" tokens quoted above — so use the ratios, not the absolute counts, to size savings on lighter workloads.) Validate on your own workload — the right number depends on how much the advisor needs to reason to be useful.

### Prompt-based vs. hard ceiling

There are two ways to trim advisor output:

**Soft request (prompt-based):** Add a line in the user message addressed directly to the advisor:
```
(Advisor: please keep your guidance under 80 words — I need a focused starting point, not a comprehensive plan.)
```
[The advisor sees your system prompt and user messages as quoted context, so instructions addressed to it are followed reliably.](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#trimming-advisor-output-length)

**Hard ceiling (`max_tokens`):** Guarantees a bound for cost and latency regardless of how the advisor reasons.

You can use both. The soft approach biases toward brevity; the hard ceiling ensures you never exceed budget even if the advisor decides a long reasoning chain is justified.

---

## Refusals before output: no longer billed

The second June 2 change is simpler but meaningfully affects high-throughput integrations.

### What changed

When a Claude API request returns `stop_reason: "refusal"` and Claude has not generated any output, [**you are not billed**](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals#reset-context-after-refusal) for that request. [Usage counts that appear in the response are informational only — they are not charged.](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#what-a-refusal-looks-like)

If Claude generates output before the refusal, you are billed for that request at the normal rate — [a mid-stream refusal bills the input tokens and the output already streamed](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#what-a-refusal-looks-like). The billing distinction is whether any output was produced, not whether the stop reason was refusal.

### Context on refusal types

The `stop_reason: "refusal"` path is triggered by streaming safety classifiers — not by the model deciding to decline, and not by input validation failures (which return 400 errors). Anthropic's docs describe [three refusal types](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals#current-refusal-types):

| Mechanism | Response format | Billing |
|---|---|---|
| Streaming classifier refusal (no output) | 200, `stop_reason: "refusal"` | **No charge** (as of June 2) |
| Streaming classifier refusal (output before refusal) | 200, `stop_reason: "refusal"` | Billed for tokens produced |
| Input / copyright validation failure | [400 error](https://platform.claude.com/docs/en/api/errors#http-errors) | [No `usage` object is returned with an error response](https://platform.claude.com/docs/en/api/errors#error-shapes) |
| Model-generated refusal | 200, standard text response | [Billed at standard per-token rates](https://platform.claude.com/docs/en/about-claude/pricing#model-pricing) like any other completion |

### Detecting refusals

[Refusals are 200 responses, not errors. Monitoring built only on HTTP error rates will not surface them.](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals#migration-notes) Track `stop_reason` independently.

**Non-streaming:**
```python
response = client.messages.create(...)
if response.stop_reason == "refusal":
    # reset conversation context before retrying
    messages = []
```

**Streaming:**
```python
with client.messages.stream(...) as stream:
    for event in stream:
        if event.type == "message_delta":
            if event.delta.stop_reason == "refusal":
                messages = []   # reset context
                break
```

[After any refusal, reset the conversation context before the next turn. Attempting to continue without resetting results in continued refusals.](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals#reset-context-after-refusal) Retrying on the same model also tends to re-refuse — use the [refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback) page to route to a different Claude model instead.

### Batch API note

In [Message Batches](https://platform.claude.com/docs/en/build-with-claude/batch-processing), [a refused request returns as a **succeeded** result with `stop_reason: "refusal"` — not as an errored result](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#refusals-in-message-batches). Filter on stop reason after iterating results, not on the result status field.

### Migration notes for existing integrations

If you already handle refusals, no API changes are needed. The billing behavior changed server-side; the response format is the same. If you were eating refusal costs in a high-volume pipeline and had built no mitigation because the frequency was manageable, the June 2 change makes the economics better without requiring any code changes. If you want to redirect refused requests to a fallback model, the [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback) page covers server-side fallback and SDK middleware approaches.

---

Both changes shipped on June 2, 2026. No beta headers are required for the refusal billing change. The advisor `max_tokens` parameter requires the existing `advisor-tool-2026-03-01` beta header.

