---
title: "OpenAI Inline Moderation: One-Call Safety Scores in Responses API and Chat Completions"
date: 2026-07-02
description: "OpenAI added inline moderation to both the Responses API and Chat Completions API on June 4, 2026. Pass a moderation object in your generation request and receive flagged status, per-category scores, and model confidence in the same response."
og_description: "Pass moderation={\"model\": \"omni-moderation-latest\"} to get input and output safety scores alongside your generation — no second API call, no extra latency for standalone requests."
content_type: "Builder's Log"
categories: ["OpenAI", "Safety", "Developer Tools"]
tags: ["openai", "moderation", "responses-api", "chat-completions", "safety", "guardrails", "builder-guide", "june-2026", "api"]
---

OpenAI shipped inline moderation to the Responses API and Chat Completions API on June 4, 2026. You can now receive safety scores for both your input and generated output in a single API call, without routing content through the standalone moderation endpoint separately. Part of our **[Builder's Log](/builders-log/)**.

---

## What Changed

Previously, checking whether a prompt or a model response was safe required two API calls: one to generate, one to moderate. The standalone moderation endpoint (`POST /v1/moderations`) remains available, but it's now optional — you can fold moderation directly into your generation call by passing a `moderation` object at the top level of the request.

This applies to both the Responses API and Chat Completions API.

---

## Responses API

Add `moderation` to any `/v1/responses` request:

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.5",
    input=[{"role": "user", "content": "Explain how vaccines work."}],
    moderation={"model": "omni-moderation-latest"},
)

# Moderation results on input
input_result = response.moderation.input.results[0]
print(input_result.flagged)           # False
print(input_result.categories)        # {hate: False, harassment: False, ...}
print(input_result.category_scores)   # {hate: 0.0001, harassment: 0.0002, ...}

# Moderation results on output
output_result = response.moderation.output.results[0]
print(output_result.flagged)
```

The `response.moderation.input` object contains scores for what the user sent. `response.moderation.output` scores what the model generated. Both are available in the same response object.

---

## Chat Completions API

The same parameter works in Chat Completions:

```python
completion = client.chat.completions.create(
    model="gpt-5.5",
    messages=[{"role": "user", "content": "Explain how vaccines work."}],
    moderation={"model": "omni-moderation-latest"},
)

# Input moderation
input_result = completion.moderation.input.results[0]

# Output moderation — results[i] aligns with choices[i]
output_result = completion.moderation.output.results[0]
print(output_result.flagged)
```

When you request multiple choices (`n=3`), `completion.moderation.output.results[i]` corresponds to `completion.choices[i]`.

---

## Reading Moderation Results

Each result object has three fields:

| Field | Type | Description |
|---|---|---|
| `flagged` | bool | True if any category exceeds its threshold |
| `categories` | dict | Per-category boolean (True = flagged) |
| `category_scores` | dict | Model confidence 0–1 per category |
| `category_applied_input_types` | dict | Which input types each category applies to |

The `flagged` boolean is the fast path for most applications. For logging, routing to human review, or building custom thresholds, use `category_scores` directly — a score of 0.3 on `harassment` may warrant logging even if it doesn't cross the default threshold for `flagged=True`.

Categories include: `hate`, `hate/threatening`, `harassment`, `harassment/threatening`, `self-harm`, `self-harm/intent`, `self-harm/instructions`, `sexual`, `sexual/minors`, `violence`, `violence/graphic`, and `illicit`.

---

## Streaming Behavior

Moderation scores are not part of the streaming delta events. If you stream a response, moderation results arrive as a separate block **after** the full output is available.

```python
stream = client.responses.create(
    model="gpt-5.5",
    input=[{"role": "user", "content": "Tell me about nuclear energy."}],
    moderation={"model": "omni-moderation-latest"},
    stream=True,
)

for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.moderation.completed":
        # Arrives after the final output event
        print("\n\nFlagged:", event.moderation.output.results[0].flagged)
```

This means you cannot gate on moderation results while streaming output. You either stream without gating, or you complete generation first and then evaluate. If real-time blocking matters (e.g., a live voice agent), keep the standalone `/v1/moderations` call in parallel with your generation request.

---

## Tool Calling Coverage

Inline moderation covers tool-call arguments and tool outputs when they appear in conversation content. It does not score:

- Tool names
- Tool descriptions
- Tool schemas
- Response format specifications

If your tools handle sensitive data — medical records, legal documents, personal information — and tool schemas themselves could reveal sensitive patterns, the standalone moderation endpoint gives finer control. For most agents, inline coverage is sufficient.

---

## Cost

The moderation endpoint is free. Adding `moderation` to a generation request does not increase your bill beyond the standard generation cost. There is no per-moderation-call charge, whether you use the inline parameter or the standalone endpoint.

The practical implication: there is no cost reason to skip moderation. The only tradeoff is compute overhead (a small latency increase at response completion) and streaming behavior (results arrive at the end, not in flight).

---

## When to Use Inline vs Standalone

**Use inline moderation when:**
- You want moderation results logged with every response without adding code complexity
- You already use the Responses or Chat Completions API and want the simplest path
- Your use case can tolerate learning about a safety issue after the model has finished generating
- You use non-streaming or can post-process before displaying output to users

**Keep standalone `/v1/moderations` when:**
- You need to check a prompt *before* spending generation tokens on a likely-flagged input
- You need real-time blocking during streaming (fire a moderation call in parallel, cancel the stream if flagged)
- You need to moderate content that isn't part of a generation request (uploaded files, user profiles, form inputs)
- You need the `input_type` breakdown for multimodal content separately from a generation flow

---

## Migration Note

Adding `moderation` to existing generation calls is additive — it doesn't change the model output, the response structure, or any existing fields. You can deploy it to a subset of endpoints first and compare results before rolling out broadly. No beta header is required; inline moderation is generally available as of June 4, 2026.
