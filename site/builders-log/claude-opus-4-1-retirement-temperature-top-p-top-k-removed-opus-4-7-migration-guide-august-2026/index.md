# Claude Opus 4.1 Retires August 5 — 10 Breaking Changes to Fix Before You Upgrade

> Anthropic retired temperature, top_p, and top_k on Opus 4.7+ and Sonnet 5. If you set any of them to a non-default value, you'll get a 400 error today. Here's the full migration checklist for Opus 4.1 → Opus 4.8.


Anthropic has deprecated `temperature`, `top_p`, and `top_k` on Claude Opus 4.7 and later. If you call those models with any of those parameters set to a **non-default value**, the API returns a `400` error immediately — no fallback, no warning, just a hard failure. This applies to Opus 4.7, Opus 4.8, Sonnet 5, Fable 5, and Mythos 5.

Separately, Claude Opus 4.1 (`claude-opus-4-1-20250805`) was deprecated June 5, 2026 and **retires August 5, 2026**. After that date, requests to that model ID return errors. If you haven't migrated yet, you have five weeks. The migration path from Opus 4.1 to Opus 4.8 spans ten breaking changes, some of which restructure your API call significantly.

---

## The immediate issue: sampling parameters are gone

Anthropic's reasoning models — Opus 4.7+, Sonnet 5, Fable 5, Mythos 5 — use adaptive thinking internally. Externally exposed sampling controls (`temperature`, `top_p`, `top_k`) no longer apply, so Anthropic removed them rather than silently ignore them.

**If you call Opus 4.7, Opus 4.8, or Sonnet 5 with `temperature`, `top_p`, or `top_k` set to any non-default value, you get a 400 error.**

```python
# This breaks on Opus 4.7+ and Sonnet 5
response = client.messages.create(
    model="claude-opus-4-8",
    temperature=0.7,   # 400 error
    top_p=0.9,         # 400 error
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
)

# Fix: omit all three
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
)
```

The guidance from Anthropic is to use prompting to guide model behavior instead. Phrases like "respond concisely" or "vary your phrasing" do what `temperature` adjustments used to do for most use cases.

If you're on Opus 4.6 or Sonnet 4.6 and using `temperature`, you're fine — those models still accept it. But if you plan to upgrade to Opus 4.7+, Sonnet 5, or any later model, remove the parameters first and test before promoting to production.

---

## Opus 4.1 retirement: August 5, 2026

| Model | Deprecated | Retires | Replace with |
|---|---|---|---|
| `claude-opus-4-1-20250805` | June 5, 2026 | **August 5, 2026** | `claude-opus-4-8` |

After August 5, any request to `claude-opus-4-1-20250805` returns an error. The recommended replacement is `claude-opus-4-8`. Pricing stays the same: $5 per million input tokens, $25 per million output tokens.

If you have production workloads on Opus 4.1, five weeks is enough time — but the migration isn't just a model ID swap. There are ten breaking changes stacked between Opus 4.1 and Opus 4.7+.

---

## Ten breaking changes: Opus 4.1 → Opus 4.8

Work through these in order. Each one that doesn't apply to your codebase, skip and move on.

### 1. Remove sampling parameters

Already covered above. Remove `temperature`, `top_p`, and `top_k` from every call targeting Opus 4.7+. This is the most likely to cause a silent regression if you're testing against a different model than your production call uses.

### 2. Replace extended thinking with adaptive thinking + effort

The `thinking` block syntax changed:

```python
# Before (Opus 4.1 style)
response = client.messages.create(
    model="claude-opus-4-1-20250805",
    thinking={"type": "enabled", "budget_tokens": 32000},
    max_tokens=16000,
    messages=[...]
)

# After (Opus 4.7+)
response = client.messages.create(
    model="claude-opus-4-8",
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},
    max_tokens=16000,
    messages=[...]
)
```

The `effort` parameter controls how much the model reasons. Valid values are `"low"`, `"medium"`, `"high"`, and `"max"`. If you omit `output_config` entirely, the model defaults to adaptive thinking at its own judgment. The `budget_tokens` field is not valid on Opus 4.7+.

### 3. Update tool versions

Two built-in tools changed IDs:

| Before | After |
|---|---|
| `text_editor_20250124` | `text_editor_20250728` |
| `code_execution` | `code_execution_20250825` |

Also: the `undo_edit` command was removed from the text editor tool. If your tool-use code calls `undo_edit`, remove those calls — the model won't find the command.

### 4. Handle two new stop reasons

Opus 4.7+ can return two stop reasons that don't exist on Opus 4.1:

- `stop_reason: "refusal"` — the model declined to complete the request. The response will also include `stop_details.category` with a refusal category string.
- `stop_reason: "model_context_window_exceeded"` — the context window was hit mid-generation.

If your code assumes `stop_reason` is always `"end_turn"`, `"max_tokens"`, or `"stop_sequence"`, add branches for these two. Unhandled stop reasons typically surface as silent empty outputs or downstream parsing errors.

```python
match response.stop_reason:
    case "end_turn":
        # normal completion
    case "max_tokens":
        # handle truncation
    case "refusal":
        category = response.stop_details.category
        # log and handle refusal
    case "model_context_window_exceeded":
        # chunk your input or raise
```

### 5. Remove assistant message prefills

Opus 4.7+ returns a `400` error if you pass a trailing assistant turn in `messages` (a "prefill"). This pattern was common for steering output format:

```python
# Before — worked on Opus 4.1
messages = [
    {"role": "user", "content": "List three items."},
    {"role": "assistant", "content": "1."},  # prefill
]

# After — use output_config.format instead
response = client.messages.create(
    model="claude-opus-4-8",
    output_config={"format": {"type": "json_schema", "json_schema": {...}}},
    messages=[{"role": "user", "content": "List three items."}]
)
```

Use `output_config.format` for structured outputs. For plain text formatting, use explicit instructions in the user turn.

### 6. Migrate `output_format` to `output_config.format`

If you used the `output_format` parameter for structured output (JSON schema), it has moved:

```python
# Before
output_format={"type": "json_schema", "json_schema": my_schema}

# After
output_config={"format": {"type": "json_schema", "json_schema": my_schema}}
```

The `output_format` key is no longer accepted.

### 7. Remove legacy beta headers

Remove these from your `extra_headers` or `anthropic_beta` parameter — they either do nothing or cause errors on Opus 4.7+:

- `token-efficient-tools-2025-02-19`
- `output-128k-2025-02-19`
- `interleaved-thinking-2025-05-14`
- `effort-2025-11-24`

### 8. Verify tool string parameter handling

The model's behavior on trailing newlines in tool result strings changed between Opus 4.1 and Opus 4.7. If you have tests that assert exact string equality on tool parameters, run them against Opus 4.7+ before deploying — you may see newline differences that break downstream parsing.

### 9. Re-baseline tokenization

Opus 4.7+ uses a new tokenizer that produces **roughly 30% more tokens** than Opus 4.1 on the same input text. This has two practical effects:

- **Cost increases.** A prompt that was 1,000 tokens on Opus 4.1 may be ~1,300 tokens on Opus 4.8. Re-run your cost estimates.
- **`max_tokens` headroom.** If you set `max_tokens` close to the context window limit, prompts that fit before may now exceed it. Audit your largest prompts.

### 10. Handle Sonnet 5 introductory pricing window (if relevant)

If you're also migrating Sonnet workloads: Claude Sonnet 5 is on introductory pricing of $2 per million input / $10 per million output through August 31, 2026. Standard pricing ($3/$15) takes effect September 1. If you're running cost models, account for the step-up.

---

## Migration checklist

```
[ ] Remove temperature, top_p, top_k from all API calls targeting Opus 4.7+
[ ] Replace extended thinking syntax (budget_tokens → adaptive + effort)
[ ] Update built-in tool IDs (text_editor, code_execution)
[ ] Remove undo_edit command usage
[ ] Add handlers for "refusal" and "model_context_window_exceeded" stop reasons
[ ] Remove assistant message prefills; switch to output_config.format
[ ] Migrate output_format → output_config.format
[ ] Remove legacy beta headers
[ ] Audit tool result string parsing for trailing newline behavior
[ ] Re-baseline token counts and max_tokens values (~30% increase)
[ ] Update model ID to claude-opus-4-8
[ ] Run integration tests against Opus 4.8 in staging before August 5
```

---

## What to do now

If you're on Opus 4.1: the retirement date is August 5. Start with the `temperature` removal first since that's the only change that causes immediate 400 errors on Opus 4.7+ in production. The others surface as incorrect behavior or test failures.

If you're already on Opus 4.6 and planning to upgrade to Opus 4.7+: only the temperature change and the extended thinking syntax change apply to you — the others were introduced in the 4.1 → 4.6 window.

Anthropic's official model deprecation list and migration guide are at `platform.claude.com/docs/en/about-claude/model-deprecations` and `platform.claude.com/docs/en/about-claude/models/migration-guide`.

