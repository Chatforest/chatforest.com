# Gemini's June 8 Hard Cutoff: Everything That Breaks and How to Fix It

> Google's Gemini Interactions API removes the legacy outputs schema on June 8, 2026 — 8 days from now. Here's exactly what breaks across text, streaming, function calling, and multimodal, with before/after migration code for each.


Eight days.

That is how long Google is giving builders to migrate off the legacy Gemini Interactions API schema before it stops working entirely. On **June 8, 2026**, Google removes the `outputs` array from Gemini API responses — permanently. No opt-out. No pinned version escape hatch. If your code touches `interaction.outputs`, it breaks.

This is not a soft deprecation with a long tail. The timeline moved fast: the new schema became the default on May 26 (already live), and the legacy format disappears June 8. That is a 13-day window from default flip to hard removal. Most teams have not acted yet.

Here is what breaks, why, and exactly how to fix it.

---

## The Timeline

| Date | What Changed |
|------|-------------|
| May 7, 2026 | New `steps` schema available; SDK 2.0.0 released |
| May 26, 2026 | New schema becomes default for all requests |
| **June 8, 2026** | Legacy `outputs` schema permanently removed |

If you have not upgraded your SDK or migrated your response-parsing code, the May 26 switch may already be causing silent failures in staging. The June 8 date is when production breaks.

---

## The Core Change: `outputs` → `steps`

The fundamental restructuring is this: Gemini API responses used to return a flat `outputs` array containing only the model's generated content. Now they return a `steps` array — a complete execution timeline of everything that happened during the request.

**Legacy response (breaks June 8):**
```json
{
  "outputs": [
    { "type": "text", "text": "Here is the answer..." }
  ]
}
```

**New response (required after June 8):**
```json
{
  "steps": [
    {
      "type": "user_input",
      "content": [{ "type": "text", "text": "Tell me a joke." }]
    },
    {
      "type": "model_output",
      "content": [{ "type": "text", "text": "Here is the answer..." }]
    }
  ]
}
```

The `steps` array can also include `thought` steps, `function_call` steps, `function_result` steps, `google_search_call` steps, and `google_search_result` steps — making the full execution chain visible and inspectable.

**Why Google did this:** The old `outputs` array only gave you the end result. The new `steps` timeline gives you the full trace: what the model thought, what tools it called, what results came back, and what it generated. For agentic workloads, this is table stakes. For simple text generation, it's a structural change you have to handle.

---

## SDK Version Requirement

This is the fastest fix for most builders:

| SDK Version | Schema Received |
|-------------|----------------|
| Python SDK ≥ 2.0.0 | New `steps` schema (with convenience properties) |
| Python SDK 1.x.x | Legacy `outputs` until June 8, then breaks |
| JavaScript SDK ≥ 2.0.0 | New `steps` schema (with convenience properties) |
| JavaScript SDK 1.x.x | Legacy `outputs` until June 8, then breaks |

**Upgrade command:**
```bash
pip install --upgrade google-genai  # Python
npm install @google/genai@latest    # Node.js
```

After upgrading, the SDK exposes convenience properties that handle the `steps` traversal for you:

```python
# After SDK 2.0.0 upgrade — works immediately
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Summarize this document."
)
print(interaction.output_text)   # convenience property — no steps traversal needed
print(interaction.output_image)  # if image was generated
print(interaction.output_audio)  # if audio was generated
```

The convenience properties are the fast path. If you only need the final output, upgrading the SDK and switching to `interaction.output_text` instead of `interaction.outputs[-1].text` is the entire migration.

If you do need to inspect the steps themselves (for tracing, debugging, or agentic workflows), read on.

---

## Five Areas That Break

### 1. Basic Text Generation

**Before (breaks June 8):**
```python
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Tell me about agentic AI."
)
text = interaction.outputs[-1].text
```

**After:**
```python
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Tell me about agentic AI."
)
text = interaction.output_text  # SDK convenience property
```

If you need to walk the steps manually:
```python
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

---

### 2. Streaming

Streaming has the most invasive change. The SSE event structure is completely different.

**Before (breaks June 8):**
```python
with client.interactions.stream(...) as stream:
    for event in stream:
        if event.type == "content.delta":
            print(event.delta, end="")
```

**After:**
```python
with client.interactions.stream(...) as stream:
    for event in stream:
        if event.type == "step.delta":
            if hasattr(event, "text_delta"):
                print(event.text_delta, end="")
```

New streaming events to handle:

| Event | Meaning |
|-------|---------|
| `interaction.created` | New interaction started |
| `step.start` | A step is beginning (type indicates which) |
| `step.delta` | Incremental content within a step |
| `step.stop` | Step completed |
| `interaction.completed` | All steps done |

Builders with custom streaming parsers need to rewrite their event handlers. The `content.delta` event type does not exist in the new schema.

---

### 3. Function Calling

Function calling has changed from embedded outputs to discrete step types.

**Before (breaks June 8):**
```python
response = client.interactions.create(
    model="gemini-3.5-flash",
    input="What's the weather in Tokyo?",
    tools=[weather_tool]
)
# Tool calls were embedded in outputs
tool_calls = [o for o in response.outputs if o.type == "tool_call"]
```

**After:**
```python
response = client.interactions.create(
    model="gemini-3.5-flash",
    input="What's the weather in Tokyo?",
    tools=[weather_tool]
)
# Check if action is required
if response.status == "requires_action":
    for step in response.steps:
        if step.type == "function_call":
            # Execute function_call.name with function_call.arguments
            result = execute_function(step.function_call)
            # Submit result back
            response = client.interactions.submit_tool_outputs(
                interaction_id=response.id,
                tool_outputs=[{"step_id": step.id, "output": result}]
            )
```

The key difference: the interaction status is now `"requires_action"` when tool execution is needed, matching the OpenAI Assistants API pattern. Tool calls and results appear as separate, typed steps in the timeline.

---

### 4. Stateful Conversations (Multi-turn)

Multi-turn conversation handling changes significantly — actually for the better.

**Before (breaks June 8):**
```python
# Manually maintain history array
history = []
for user_message in conversation:
    history.append({"role": "user", "parts": [user_message]})
    response = client.generate_content(
        model="gemini-3.5-flash",
        contents=history
    )
    history.append({"role": "model", "parts": [response.outputs[-1].text]})
```

**After:**
```python
# Server-side state management via previous_interaction_id
first_response = client.interactions.create(
    model="gemini-3.5-flash",
    input="My name is Alex. Remember that."
)

second_response = client.interactions.create(
    model="gemini-3.5-flash",
    input="What's my name?",
    previous_interaction_id=first_response.id  # server manages history
)
print(second_response.output_text)  # "Your name is Alex."
```

Google manages conversation state server-side. Interactions are retained for 55 days on paid tier, 1 day on free tier. This eliminates the manual history-array pattern entirely — a real simplification if you adopt it.

Note: If you were passing the `steps` array manually in the `input` field of subsequent requests (as described in early migration docs), the cleaner path is `previous_interaction_id`.

---

### 5. Multimodal and Structured Output

Two additional schema changes affect multimodal and structured output builders:

**`response_format` is now an array (multimodal):**
```python
# Before
response = client.interactions.create(
    model="gemini-3.5-flash",
    input="Describe this image and generate a caption image.",
    response_format={"type": "text"}  # single object
)

# After
response = client.interactions.create(
    model="gemini-3.5-flash",
    input="Describe this image and generate a caption image.",
    response_format=[{"type": "text"}, {"type": "image"}]  # array
)
```

**`response_mime_type` removed; `response_format` used for JSON:**
```python
# Before
response = client.interactions.create(
    model="gemini-3.5-flash",
    input="Extract the names from this text.",
    generation_config={"response_mime_type": "application/json"}
)

# After
response = client.interactions.create(
    model="gemini-3.5-flash",
    input="Extract the names from this text.",
    response_format={"type": "json_object"}  # or json_schema with schema
)
```

**`image_config` moves from `generation_config` to `response_format`:**
```python
# Before
response = client.interactions.create(
    model="gemini-3.5-flash",
    input="Generate an image of a forest.",
    generation_config={"image_config": {"aspect_ratio": "16:9"}}
)

# After
response = client.interactions.create(
    model="gemini-3.5-flash",
    input="Generate an image of a forest.",
    response_format={"type": "image", "image_config": {"aspect_ratio": "16:9"}}
)
```

---

## Server-Side Tools: Search and Code Execution

If you use Google Search or Code Execution as built-in tools, their results now appear as typed steps:

```python
response = client.interactions.create(
    model="gemini-3.5-flash",
    input="What are today's top AI headlines?",
    tools=[{"google_search": {}}]
)

for step in response.steps:
    if step.type == "google_search_call":
        print(f"Searched: {step.query}")
    elif step.type == "google_search_result":
        print(f"Found: {step.results}")
    elif step.type == "model_output":
        print(f"Answer: {step.content[0].text}")
```

Citations now appear inline as content annotations rather than as a separate citations field. Builders who parse `response.citations` will need to update to `step.content[n].annotations` for the model output step.

---

## How to Know If You're Affected

Run this grep against your codebase:

```bash
# Python
grep -rn "\.outputs\[" . --include="*.py"
grep -rn "\.outputs\[-1\]" . --include="*.py"
grep -rn "response_mime_type" . --include="*.py"
grep -rn "content\.delta" . --include="*.py"
grep -rn "generation_config.*image_config" . --include="*.py"

# JavaScript
grep -rn "\.outputs\[" . --include="*.ts" --include="*.js"
grep -rn "responseMimeType" . --include="*.ts" --include="*.js"
grep -rn "content\.delta" . --include="*.ts" --include="*.js"
```

Each match is a migration point. If you find zero matches and you're on SDK 2.0.0+, you are already compliant. If you are on SDK 1.x and have zero matches, you may still have silent failures after May 26 that become hard failures on June 8.

---

## The One-Day Migration Path

For most builders, this is the sequence:

1. **Upgrade SDK** — `pip install --upgrade google-genai` / `npm install @google/genai@latest`
2. **Replace `outputs[-1].text`** with `output_text` across your codebase
3. **Rewrite streaming handlers** — swap `content.delta` for `step.delta`
4. **Update function calling** — check for `requires_action` status, handle `function_call` steps
5. **Fix `response_mime_type`** — replace with `response_format` object
6. **Fix `image_config`** — move from `generation_config` to `response_format`
7. **Test multi-turn flows** — consider switching to `previous_interaction_id` server-side state

Steps 1 and 2 cover 80% of affected codebases. Steps 3–7 apply to builders using advanced features.

The new schema is genuinely better — the execution timeline is more useful than a flat outputs array, and server-side conversation state is simpler than manual history management. The migration is worth doing even if the deadline were further out.

It is not. Eight days.

---

*Google's official migration guide is at [ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026). SDK upgrade docs at [ai.google.dev/gemini-api/docs/migrate-to-interactions](https://ai.google.dev/gemini-api/docs/migrate-to-interactions).*

