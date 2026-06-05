# GPT-5.2 Retires June 5: What Builders Get When They Switch to GPT-5.4

> GPT-5.2 Thinking is retired on June 5, 2026. The migration is a one-line model name change — but the upgrade brings three capabilities that matter: native computer-use, 1M-token context, and Tool Search, which cuts token usage 47% on MCP-heavy workloads.


GPT-5.2 Thinking retires on June 5, 2026. If you have production code that calls `gpt-5.2` or `gpt-5.2-thinking`, you have four days to update the model name before your requests start failing.

The migration is a single-line change. But this is a good time to understand what GPT-5.4 actually offers that GPT-5.2 did not — because three of those features directly affect how builders structure agent pipelines.

---

## The One-Line Migration

Change the model string:

```python
# Before
response = client.responses.create(
    model="gpt-5.2-thinking",
    ...
)

# After
response = client.responses.create(
    model="gpt-5.4",
    ...
)
```

That is the minimum viable migration. GPT-5.4 is backward-compatible with the Responses API surface that GPT-5.2 used. Existing prompts, tool definitions, and structured output schemas work without modification.

If you are still on the older Chat Completions API format, GPT-5.4 also supports that path, but OpenAI has signaled that new capabilities (Tool Search in particular) require the Responses API. The migration to `client.responses.create()` is worth doing in the same pass.

---

## What GPT-5.4 Adds

GPT-5.4 was released on March 5, 2026, as OpenAI's first general-purpose model with three capabilities that did not exist in GPT-5.2:

- **Native computer-use** — the model can interact with a desktop through screenshots, control the mouse and keyboard, and generate Playwright scripts for browser automation
- **1M-token context** — standard context is 272K tokens; API and Codex users can configure up to 1M tokens
- **Tool Search** — a new mechanism for handling large tool inventories without loading every definition into the prompt

The benchmarks are also better: GPT-5.4 beats human experts on OSWorld desktop-automation tasks and shows measurable improvements on coding and reasoning benchmarks. But for most migration decisions, the three structural capabilities above matter more than raw scores.

---

## Native Computer-Use

GPT-5.4 is the first general-purpose OpenAI model that can operate a desktop. Previous computer-use capability was confined to specialized models or required the Operator product. With GPT-5.4, you can build agents that:

- Take a screenshot and reason about what is on screen
- Issue mouse and keyboard events directly
- Write and execute Playwright code for browser automation
- Operate across applications (not just the browser)

The model accepts screenshots as image inputs and outputs structured actions: `{"type": "mouse_click", "x": 412, "y": 208}` or `{"type": "key", "key": "ctrl+c"}`. It can also generate and run Playwright scripts autonomously when the browser automation path is preferred over raw input events.

This is relevant even for builders who do not intend to ship a computer-use product. Several agent frameworks now use computer-use as a fallback for tools that do not have an API — the model can click through a legacy web interface or fill in a form that lacks a programmatic endpoint. GPT-5.4 makes this pattern available at standard API pricing without a specialized model swap.

---

## 1M-Token Context

The standard context window is 272K tokens. For most tasks, that is more than enough.

The 1M-token option is designed for long-horizon agents that need to plan, execute, and verify across a much larger scope: entire codebases, regulatory document review, multi-session conversation replay, or reasoning across many retrieved documents simultaneously.

The pricing structure reflects the cost:

| Context range | Input price | Output price |
|---|---|---|
| 0 – 272K tokens | $2.50 / MTok | $15.00 / MTok |
| 272K – 1M tokens | $5.00 / MTok | $15.00 / MTok |

The 1M window is not a free upgrade. For most production workloads, staying within 272K at standard pricing is the right call. The extended context makes economic sense when the task genuinely cannot be decomposed — or when the cost of multiple round-trips and retrieval errors exceeds the token price delta.

---

## Tool Search

Tool Search is the most novel addition for builders who work with MCP or large tool inventories.

The problem it solves: as agents connect to more MCP servers, the combined token cost of loading every tool definition into every request becomes significant. A cluster of 36 MCP servers may carry tens of thousands of tokens of tool definitions before the first user message is processed.

OpenAI evaluated Tool Search against 250 tasks from Scale's MCP Atlas benchmark with all 36 MCP servers enabled. The result: **47% fewer tokens consumed**, with no accuracy loss compared to loading full definitions upfront.

### How It Works

Instead of sending every tool definition in the `tools` array, you declare a list of available tools and add `{"type": "tool_search"}` to the array. The model receives lightweight descriptors (name, a short summary) for all tools, then fetches the full definition of a tool only when it decides to use it.

```python
response = client.responses.create(
    model="gpt-5.4",
    tools=[
        {"type": "tool_search"},      # enable dynamic tool lookup
        {"type": "mcp", "server_label": "github", "server_url": "..."},
        {"type": "mcp", "server_label": "linear", "server_url": "..."},
        {"type": "mcp", "server_label": "slack", "server_url": "..."},
        # ... more MCP servers
    ],
    input="Triage the open GitHub issues from this sprint and post a summary to #eng-standup"
)
```

The API handles the tool lookup internally. When the model decides it needs the `create_issue` tool from the GitHub MCP server, it fetches the full schema for that tool and appends it to the context at that moment. Tools the model does not need never consume tokens.

Only `gpt-5.4` and `gpt-5.4-pro` support `tool_search`. It requires the Responses API — it is not available via Chat Completions.

### When Tool Search Matters

Tool Search is high-value when:
- You connect four or more MCP servers simultaneously
- Your MCP servers expose large numbers of tools (tens or hundreds per server)
- Your agent queries are narrowly scoped relative to the full tool inventory (the agent only needs 2–3 tools per task, but 36 servers are registered)

Tool Search has minimal benefit when:
- You have a small, fixed tool set (< 10 tools, all definitions under 2K tokens combined)
- Your tasks genuinely use most available tools in each request
- You need deterministic, reproducible token counts for billing estimation

---

## GPT-5.4 Pro

`gpt-5.4-pro` is also available. OpenAI's documentation describes it as targeting "maximum performance on complex tasks." Pricing is higher — check the OpenAI API pricing page for current rates, as Pro pricing has been updated since release. Use `gpt-5.4` as the default unless you have a task where `gpt-5.4` measurably underperforms and the Pro price delta is justified by the outcome difference.

---

## Pricing Summary

| Model | Standard input | Output | Extended context |
|---|---|---|---|
| gpt-5.4 | $2.50 / MTok | $15.00 / MTok | $5.00 / MTok (272K–1M) |
| gpt-5.2 (retiring) | N/A after June 5 | — | — |

---

## Builder Action Checklist

**Before June 5 (retirement deadline):**

- [ ] Search your codebase for `gpt-5.2` and `gpt-5.2-thinking` model strings
- [ ] Replace with `gpt-5.4` in all production call sites
- [ ] Run a smoke test against the Responses API if you are migrating from Chat Completions at the same time
- [ ] Update any hardcoded model references in environment variables or config files

**Optional GPT-5.4 upgrades (do after migration is stable):**

- [ ] If you have 4+ MCP servers registered: add `{"type": "tool_search"}` to your tools array and measure token reduction on your actual workload
- [ ] If you have tasks that would benefit from > 272K context: test against 1M token window, compare cost against decomposition alternatives
- [ ] If you have any legacy-UI automation tasks (apps without APIs): evaluate native computer-use as a replacement for your current brittle workarounds

---

## Bottom Line

GPT-5.2 Thinking stops accepting requests on June 5. Updating the model name takes five minutes. Leaving it until June 5 risks a production outage over a trivial change.

Once you have migrated, Tool Search is the feature most likely to reduce your monthly bill if you run MCP-heavy agents — 47% token reduction on MCP Atlas is not a marginal improvement. It requires no prompt changes, no architecture changes, and no additional API surface to learn. It is a one-line addition to your tools array that pays for itself on any workload where the model uses a small fraction of registered tools per request.

