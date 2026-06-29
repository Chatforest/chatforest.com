# OpenAI Assistants API Sunset: August 26, 2026 Is the Hard Deadline — Here Is How to Migrate

> On August 26, 2026, every call to /v1/assistants, /v1/threads, and /v1/runs returns an error. No grace period. No extension. The Responses API is the replacement. This guide covers what breaks, what changes architecturally, and how to migrate before the deadline.


On **August 26, 2026**, OpenAI will shut down the Assistants API. Every call to `/v1/assistants`, `/v1/threads`, and `/v1/runs` will return an error. There is no degraded mode, no grace period, and no announced extension.

Today is June 28, 2026. That leaves 59 days. Migrations involving staging environments, re-implementing tool calls, and coordinating deploys tend to take three to four weeks. The safe internal deadline is **mid-July**.

---

## What Gets Shut Off

The Assistants API introduced three core abstractions:

- **Assistants** — persistent objects holding a system prompt, model, and tool configuration
- **Threads** — server-side conversation history managed by OpenAI
- **Runs** — execution jobs that process a thread with an assistant and return results

After August 26, API calls to `/v1/beta/assistants`, `/v1/beta/threads`, and `/v1/beta/threads/{id}/runs` return HTTP errors. Threads stored on OpenAI's servers are no longer readable. There is no automated tool to export or migrate existing Threads — if you have data there you need to keep, extract it now.

Third-party integrations are also affected. Zapier deprecated all ChatGPT (OpenAI) steps using the Assistants API on the same timeline — any Zaps built on Assistants steps will fail on August 26.

---

## What the Responses API Is

The Responses API is OpenAI's unified successor to both the Assistants API and the Chat Completions API. It replaces Assistants for stateful agent-style workloads and is the recommended interface for all new projects using GPT-5.5 and newer models.

Where the Assistants API abstracted conversation state into Threads and Runs that OpenAI managed invisibly, the Responses API makes state explicit. You send input items — a list of messages, tool results, or content blocks — and receive output items back. Multi-turn state is handled either by passing `store: true` and referencing the prior response by ID, or by maintaining conversation history yourself and replaying it with each request.

The Responses API also ships capabilities that the Assistants API never supported:

- **Deep research** — long multi-step web research runs managed by the API
- **Computer use** — browser and desktop control
- **Remote MCPs** — connect to external MCP servers directly from the API call
- **Background Mode** — submit a long-running request and poll asynchronously rather than holding a connection open

---

## Architecture Change: Assistants vs. Responses

The Assistants API is opaque by design. The state machine — queuing messages into a Thread, creating a Run, polling the Run status, retrieving output messages — all happens inside OpenAI's infrastructure. You do not see the full conversation on each request; you see only what the API surfaces.

The Responses API is transparent. You own the input. Each API call is self-contained: either you pass the full conversation as a list of input items, or you pass a `previous_response_id` that points to a stored prior response and send only the new message.

This means:
- **Debugging is easier**: the full input to any generation is visible in your code
- **Caching is more efficient**: OpenAI reports 40–80% better cache utilization compared to Chat Completions in internal benchmarks
- **Reasoning models work better**: the Responses API is the recommended interface for GPT-5.2 Pro's extended reasoning modes

---

## Code Migration

### Simple request (stateless)

**Assistants API (deprecated):**

```python
# Four separate API calls to produce one AI response
assistant = client.beta.assistants.create(
    name="Support Agent",
    instructions="You are a helpful support agent.",
    model="gpt-5.5",
    tools=[{"type": "function", "function": {...}}],
)
thread = client.beta.threads.create()
client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="How do I reset my password?",
)
run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id,
)
messages = client.beta.threads.messages.list(thread_id=thread.id)
```

**Responses API (replacement):**

```python
response = openai.responses.create(
    model="gpt-5.5",
    instructions="You are a helpful support agent.",
    input=[{"role": "user", "content": "How do I reset my password?"}],
)
print(response.output_text)
```

### Multi-turn conversation (server-side state)

Pass `store=True` on the first turn. Each subsequent turn references the prior response by ID — OpenAI maintains the context server-side.

```python
# First turn
response = openai.responses.create(
    model="gpt-5.5",
    store=True,
    instructions="You are a helpful support agent.",
    input=[{"role": "user", "content": "How do I reset my password?"}],
)

# Second turn — only send the new message
response = openai.responses.create(
    model="gpt-5.5",
    store=True,
    previous_response_id=response.id,
    input=[{"role": "user", "content": "What if I don't get the email?"}],
)
```

### Built-in tools

The Responses API includes tools that previously required custom function definitions in the Assistants API:

```python
response = openai.responses.create(
    model="gpt-5.5",
    tools=[
        {"type": "web_search_preview"},
        {"type": "file_search", "vector_store_ids": ["vs_abc123"]},
    ],
    input=[{"role": "user", "content": "What changed in the Responses API last week?"}],
)
```

Available built-in tools: `web_search_preview`, `file_search`, `computer_use_preview`, `code_interpreter`, and remote MCPs via `mcp` type entries.

### Reasoning effort

For workloads on GPT-5.2 Pro or other reasoning-capable models, `reasoning_effort` controls depth vs. speed:

```python
response = openai.responses.create(
    model="gpt-5.2-pro",
    reasoning={"effort": "high"},  # options: none, minimal, low, medium, high, xhigh
    input=[{"role": "user", "content": "Analyze this architecture for failure modes."}],
)
```

### Background Mode

For long-running tasks where holding an HTTP connection open is impractical:

```python
response = openai.responses.create(
    model="gpt-5.2-pro",
    background=True,
    input=[{"role": "user", "content": "Research and summarize the top 20 MCP servers."}],
)
# response.status == "queued" — poll until "completed"
while response.status not in ("completed", "failed", "cancelled"):
    import time; time.sleep(5)
    response = openai.responses.retrieve(response.id)
```

Background Mode is not Zero Data Retention (ZDR) compatible — responses are stored for ~10 minutes to enable polling.

---

## What Does Not Migrate Automatically

**Threads.** OpenAI has no automated export or migration tool for stored Thread data. If you have multi-turn conversation history in Threads that needs to be preserved — for support history, user session context, or compliance — write an export job now that reads the Thread messages via the Assistants API and stores them in your own database. Do this before August 26.

**Assistant objects.** Any logic encoded in a saved Assistant (system prompt, tool list, model choice) must be moved into your application code. There is no equivalent of a persistent server-side Assistant object in the Responses API — you supply `instructions` and `tools` on each call.

**Run logic.** Assistants API Runs handle tool call loops automatically. In the Responses API, tool call loops are explicit: when the response contains a tool call, you execute it and send the result back as a new input item. This gives you more control but requires re-implementing any custom orchestration logic.

---

## Performance Impact

OpenAI's internal benchmarks for the Responses API compared to Chat Completions:

| Metric | Improvement |
|---|---|
| Cache hit rate | 40–80% better |
| SWE-bench (same prompt) | +3% |

Reasoning model performance specifically improves because the Responses API was designed around the way reasoning models use context — the input structure maps more cleanly to how these models accumulate and reference prior outputs.

---

## Migration Checklist

1. **Audit for Assistants API usage**: grep for `beta.assistants`, `beta.threads`, `beta.runs`, and `/v1/beta/threads` in your codebase and infrastructure configs
2. **Export Thread data**: use the Assistants API to read and store any conversation history you need to preserve — do this before August 26
3. **Port system prompts and tool lists**: move logic from saved Assistant objects into your application code
4. **Migrate to Responses API**: use `store: True` + `previous_response_id` for multi-turn, or manage conversation history in your own state store
5. **Re-implement tool call loops**: if your Assistants workflow used function calling, update the loop to handle Responses API tool call items explicitly
6. **Update Zapier or no-code integrations**: rebuild any Zaps that used Assistants API steps using the Responses API actions
7. **Test before August 26**: run your workloads against the Responses API in staging and confirm behavior before the deadline

---

## Timeline

| Date | Event |
|---|---|
| August 26, 2025 | Assistants API deprecation announced |
| August 26, 2026 | Assistants API shutdown — `/v1/beta/assistants`, `/v1/beta/threads`, `/v1/beta/runs` return errors |
| August 26, 2026 | Stored Threads become inaccessible |

59 days from today. The Responses API is production-ready now. Migration is not a future consideration — it is the current task.

