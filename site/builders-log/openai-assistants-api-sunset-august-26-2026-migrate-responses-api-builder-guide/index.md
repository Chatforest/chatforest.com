# OpenAI Assistants API Sunset: August 26, 2026 Is the Hard Deadline — Here Is How to Migrate

> On August 26, 2026, every call to /v1/assistants, /v1/threads, and /v1/runs returns an error. No grace period. No extension. The Responses API is the replacement. This guide covers what breaks, what changes architecturally, and how to migrate before the deadline.


On **August 26, 2026**, [OpenAI will shut down the Assistants API.](https://community.openai.com/t/assistants-api-beta-deprecation-august-26-2026-sunset/1354666) Every call to `/v1/assistants`, `/v1/threads`, and `/v1/runs` will return an error. There is no degraded mode, no grace period, and [no announced extension](https://developers.openai.com/api/docs/deprecations).

Today is June 28, 2026. That leaves 59 days. Migrations involving staging environments, re-implementing tool calls, and coordinating deploys tend to take three to four weeks. The safe internal deadline is **mid-July**.

---

## What Gets Shut Off

The Assistants API introduced three core abstractions:

- **Assistants** — persistent objects holding a system prompt, model, and tool configuration
- **Threads** — server-side conversation history managed by OpenAI
- **Runs** — execution jobs that process a thread with an assistant and return results

After August 26, API calls to `/v1/beta/assistants`, `/v1/beta/threads`, and `/v1/beta/threads/{id}/runs` return HTTP errors, so Threads stored on OpenAI's servers become unreachable through the API. [OpenAI's own migration guide is explicit that there is no automated tool to export or migrate existing Threads](https://developers.openai.com/api/docs/assistants/migration) — "We will not provide an automated tool for migrating Threads to Conversations" — so if you have data there you need to keep, extract it now.

Third-party integrations are also affected. [Zapier has deprecated the ChatGPT (OpenAI) actions and searches built on the Assistants API](https://help.zapier.com/hc/en-us/articles/44865998484365-Important-update-ChatGPT-users-OpenAI-Assistants-API-deprecation) — Create Assistant, Find Assistant, Find or Create Assistant, and Upload File (when used with assistants) — and those Zaps stop working on August 26, 2026 unless rebuilt. One exception: Zaps using "Conversation With Assistant (Legacy)" are auto-migrated by Zapier to a new Responses-API-backed Conversation action, though left disabled pending your review; every other Assistants-based action requires a manual rebuild.

---

## What the Responses API Is

The Responses API is OpenAI's unified successor to both the Assistants API and the Chat Completions API. [OpenAI recommends it for reasoning, tool-calling, and multi-turn workflows going forward](https://developers.openai.com/api/docs/guides/latest-model), and its [own writeup on the design](https://developers.openai.com/blog/responses-api) frames it as the simpler, more flexible replacement for both older APIs.

[OpenAI's Assistants migration guide](https://developers.openai.com/api/docs/assistants/migration) maps the old abstractions onto new ones directly:

| Legacy (Assistants API) | Replacement (Responses API) |
|---|---|
| Assistants | Prompts |
| Threads | Conversations |
| Runs | Responses |
| Run steps | Items |

Where the Assistants API abstracted conversation state into Threads and Runs that OpenAI managed invisibly, the Responses API makes state explicit. You send input items — a list of messages, tool results, or content blocks — and receive output items back. [Multi-turn state can be handled](https://developers.openai.com/api/docs/guides/migrate-to-responses) by passing `store: true` and referencing the prior response by ID, by attaching a `conversation` object (the direct, richer replacement for Threads — it stores message and tool-call items rather than just messages), or by maintaining conversation history yourself and replaying it with each request.

The Responses API also ships capabilities that the Assistants API never supported:

- **[Deep research](https://developers.openai.com/api/docs/guides/deep-research)** — long multi-step web research runs managed by the API
- **[Computer use](https://developers.openai.com/api/docs/guides/tools)** — browser and desktop control
- **[Remote MCPs](https://developers.openai.com/api/docs/guides/tools-connectors-mcp)** — connect to external MCP servers directly from the API call
- **[Background Mode](https://developers.openai.com/api/docs/guides/background)** — submit a long-running request and poll asynchronously rather than holding a connection open

---

## Architecture Change: Assistants vs. Responses

The Assistants API is opaque by design. The state machine — queuing messages into a Thread, creating a Run, polling the Run status, retrieving output messages — all happens inside OpenAI's infrastructure. You do not see the full conversation on each request; you see only what the API surfaces.

The Responses API is transparent. You own the input. Each API call is self-contained: either you pass the full conversation as a list of input items, or you pass a `previous_response_id` that points to a stored prior response and send only the new message.

This means:
- **Debugging is easier**: the full input to any generation is visible in your code
- **Caching is more efficient**: [OpenAI reports 40–80% better cache utilization compared to Chat Completions in internal benchmarks](https://developers.openai.com/blog/responses-api)
- **Reasoning models work better**: [reasoning is preserved across turns in the Responses API but dropped between calls in Chat Completions](https://developers.openai.com/cookbook/examples/responses_api/reasoning_items) — OpenAI's own benchmark shows a 3% SWE-bench improvement for the same prompt and setup when reasoning items are carried forward. [GPT-5.2 Pro, a reasoning-heavy model, is available only through the Responses API](https://developers.openai.com/api/docs/models/gpt-5.2-pro)

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

For reasoning-capable models, the [`reasoning.effort` parameter](https://developers.openai.com/api/docs/guides/reasoning) controls depth vs. speed. The full range across models is `none, minimal, low, medium, high, xhigh, max`, but [each model supports only a subset](https://developers.openai.com/api/docs/models/gpt-5.2-pro) — GPT-5.2 Pro specifically supports only `medium`, `high`, and `xhigh`:

```python
response = openai.responses.create(
    model="gpt-5.2-pro",
    reasoning={"effort": "high"},  # gpt-5.2-pro supports: medium, high, xhigh
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

[Background Mode is not compatible with strict Zero Data Retention (ZDR) — response data is stored for roughly 10 minutes to enable polling](https://developers.openai.com/api/docs/guides/background), which conflicts with a no-retention requirement. GPT-5.2 Pro requests specifically can take several minutes, which is why OpenAI recommends background mode for that model.

---

## What Does Not Migrate Automatically

**Threads.** [OpenAI's migration guide states plainly that it will not provide an automated tool for migrating Threads to Conversations](https://developers.openai.com/api/docs/assistants/migration). If you have multi-turn conversation history in Threads that needs to be preserved — for support history, user session context, or compliance — write an export job now that reads the Thread messages via the Assistants API (`openai.beta.threads.messages.list`) and either creates a matching `Conversation` object (`openai.conversations.create`) or stores the data in your own database. Do this before August 26.

**Assistant objects.** This is *not* a total loss the way it first appears: [OpenAI's migration guide introduces "Prompts" as the direct, dashboard-managed replacement for Assistant objects](https://developers.openai.com/api/docs/assistants/migration) — a Prompt bundles model, tools, and instructions, is versionable, and is referenced by ID (`prompt={"id": "..."}`) instead of being recreated on every call. Prompts are created in the dashboard, not the API, so you can't script the conversion — but you don't have to hardcode instructions and tools into application code just to preserve a reusable, centrally managed configuration. If you skip Prompts, the fallback is what this article originally implied: supply `instructions` and `tools` directly on each `responses.create()` call.

**Run logic.** Assistants API Runs handle tool call loops automatically. In the Responses API, tool call loops are explicit: when the response contains a tool call, you execute it and send the result back as a new input item. This gives you more control but requires re-implementing any custom orchestration logic.

---

## Performance Impact

OpenAI's own internal benchmarks for the Responses API compared to Chat Completions:

| Metric | Improvement | Source |
|---|---|---|
| Cache hit rate | 40–80% better | [Why we built the Responses API](https://developers.openai.com/blog/responses-api) |
| SWE-bench (same prompt/setup, reasoning items preserved) | +3% | [Better performance from reasoning models using the Responses API](https://developers.openai.com/cookbook/examples/responses_api/reasoning_items) |

Reasoning model performance specifically improves because [the Responses API preserves reasoning state across turns, while Chat Completions drops it between calls](https://developers.openai.com/cookbook/examples/responses_api/reasoning_items) — the model doesn't have to redo work it already did on the previous turn.

---

## Migration Checklist

1. **Audit for Assistants API usage**: grep for `beta.assistants`, `beta.threads`, `beta.runs`, and `/v1/beta/threads` in your codebase and infrastructure configs
2. **Export Thread data**: use the Assistants API to read and store any conversation history you need to preserve — do this before August 26
3. **Port system prompts and tool lists**: either recreate each saved Assistant as a [Prompt object](https://developers.openai.com/api/docs/assistants/migration) in the OpenAI dashboard and reference it by ID, or move the logic directly into your application code
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

