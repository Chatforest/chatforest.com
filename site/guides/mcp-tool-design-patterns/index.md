# MCP Tool Design Patterns: Building Agent-Friendly, Composable Tools

> How to design MCP tools that agents can discover, understand, compose, and recover from — covering outputSchema, structured content, agent-aware response patterns, composability


Building an MCP server is straightforward. Building MCP tools that AI agents use *effectively* is harder. The difference between a tool that works and a tool that agents reliably choose, invoke correctly, and chain into workflows comes down to design — how you name it, what you return, and how you handle failure.

This guide covers the tool design patterns that matter most for production MCP servers. Our analysis draws on the MCP specification (2025-06-18), community patterns from production deployments, and published best practices — we research and analyze rather than testing implementations hands-on.

## Why Tool Design Matters More Than You Think

An MCP tool isn't called by a human reading documentation. It's called by an LLM that sees a JSON schema and a description string, then decides — probabilistically — whether to use it and how. This means:

1. **Your tool name is your API** — the LLM reads it before anything else
2. **Your description is your documentation** — it's often the only context the model has
3. **Your output shapes the next decision** — whatever you return goes into the context window and influences the agent's next action
4. **Your errors teach or confuse** — a good error message gives the agent a recovery path; a bad one causes thrashing

Every design decision either helps or hinders the agent's ability to use your tool correctly.

## Structured Output with outputSchema

The 2025-06-18 MCP specification introduced `outputSchema` — the ability for tools to declare a JSON Schema describing their return type. This is one of the most impactful additions to the protocol for tool reliability.

### How It Works

When defining a tool, you can include an `outputSchema` alongside the existing `inputSchema`:

```json
{
  "name": "get_device_status",
  "description": "Get the current status and uptime of a network device",
  "inputSchema": {
    "type": "object",
    "properties": {
      "device_id": {
        "type": "string",
        "description": "The device identifier (e.g., 'switch-rack3-01')"
      }
    },
    "required": ["device_id"]
  },
  "outputSchema": {
    "type": "object",
    "properties": {
      "device_id": { "type": "string" },
      "status": { "type": "string", "enum": ["online", "offline", "degraded"] },
      "uptime_seconds": { "type": "integer" },
      "last_checked": { "type": "string", "format": "date-time" }
    },
    "required": ["device_id", "status"]
  }
}
```

### structuredContent in Responses

When a tool declares an `outputSchema`, its response must include `structuredContent` — the typed, schema-compliant data — alongside the traditional `content` array for backward compatibility:

```json
{
  "structuredContent": {
    "device_id": "switch-rack3-01",
    "status": "online",
    "uptime_seconds": 1209600,
    "last_checked": "2026-03-28T12:00:00Z"
  },
  "content": [
    {
      "type": "text",
      "text": "Device switch-rack3-01 is online (uptime: 14 days)"
    }
  ]
}
```

### Why This Matters

Without `outputSchema`, the client has no way to know what shape a tool's response will take until it arrives. This creates several problems:

- **Parsing uncertainty** — the client must guess how to extract data from unstructured text
- **Composition friction** — chaining tools requires the LLM to interpret and reformat output between steps
- **Validation gaps** — no way to verify that a response is complete or correct before acting on it

With `outputSchema`, clients can validate responses programmatically, extract fields reliably, and build deterministic pipelines on top of MCP tools.

### When to Use outputSchema

Use it when your tool returns data that downstream code or tools will consume programmatically. Skip it for tools that return primarily human-readable content (summaries, explanations, generated text) where the "structure" is the prose itself.

## Agent-Aware Response Patterns

Raw data isn't enough. Production MCP tools embed heuristics, confidence signals, and recovery paths directly in their responses, moving intelligence from the expensive LLM reasoning loop to stable server code.

### Summary-First Pattern

Large responses waste tokens and attention. The summary-first pattern returns a dense overview with a pointer to fetch details on demand:

```json
{
  "structuredContent": {
    "summary": {
      "total_records": 15420,
      "anomalies_detected": 3,
      "time_range": "2026-03-27T00:00:00Z/2026-03-28T00:00:00Z"
    },
    "top_anomalies": [
      {
        "id": "evt-9912",
        "severity": "high",
        "description": "Latency spike on /api/checkout (p99: 4200ms)"
      }
    ],
    "detail_available": true,
    "detail_tool": "get_anomaly_detail",
    "detail_params": { "anomaly_id": "evt-9912" }
  }
}
```

The agent sees 3 anomalies at a glance, can drill into whichever matters, and doesn't burn context on 15,000 records. The key insight: tell the agent *what tool to call next* and *with what parameters* rather than making it figure that out.

### Error Recovery Pattern

Errors should teach, not just fail. Instead of returning a generic error string, provide a recovery path:

```json
{
  "structuredContent": {
    "success": false,
    "error_code": "RATE_LIMITED",
    "message": "GitHub API rate limit exceeded",
    "recovery_hint": {
      "action": "retry",
      "wait_seconds": 45,
      "alternative_tool": "get_cached_repo_info",
      "alternative_params": { "repo": "anthropics/claude-code" }
    }
  }
}
```

The agent now has three options: wait and retry, use a cached alternative, or inform the user with specifics. Compare this to `"Error: rate limit exceeded"` — which gives the agent nothing to work with.

### Confidence Scoring Pattern

When your tool performs classification, prediction, or analysis, embed confidence so the agent can decide whether to act or escalate:

```json
{
  "structuredContent": {
    "classification": "spam",
    "confidence": 0.62,
    "threshold": 0.85,
    "below_threshold_action": {
      "recommendation": "flag_for_human_review",
      "tool": "create_review_task",
      "params": { "item_id": "msg-4419", "reason": "low_confidence_spam" }
    }
  }
}
```

A confidence of 0.62 against a threshold of 0.85 tells the agent this isn't reliable enough to act on automatically — and `below_threshold_action` tells it exactly what to do instead.

### Pagination with Cursor Pattern

For large result sets, return a page of results with a cursor and explicit instructions for getting more:

```json
{
  "structuredContent": {
    "results": [ "..." ],
    "total_count": 342,
    "returned_count": 25,
    "cursor": "eyJvZmZzZXQiOjI1fQ==",
    "has_more": true,
    "next_tool": "search_logs",
    "next_params": { "cursor": "eyJvZmZzZXQiOjI1fQ==", "limit": 25 }
  }
}
```

This pairs well with the summary-first pattern — return a summary plus the first page, with a cursor for agents that need to go deeper.

## Tool Naming and Description

### Naming Conventions

Your tool name is the first thing the LLM evaluates when deciding which tool to use. Names should be:

- **Action-oriented** — `search_logs`, `create_issue`, `get_device_status` (verb + noun)
- **Specific** — `search_jira_issues` not `search` or `jira`
- **Consistent** — use the same verb vocabulary across your server (`get_`, `list_`, `create_`, `update_`, `delete_`)

Avoid names that are ambiguous (`process_data`), too generic (`run`), or that overlap with other tools' descriptions. If two tools sound similar, the LLM will pick the wrong one.

### Description Best Practices

The tool description is your most important design surface. It tells the model when to use the tool and what to expect:

**Good:**
```
Search for Jira issues matching a JQL query. Returns up to 50 issues
with key, summary, status, and assignee. Use list_jira_projects first
if you don't know the project key.
```

**Bad:**
```
Searches Jira.
```

A good description answers three questions:
1. **What does it do?** — the action in one sentence
2. **What does it return?** — shape and limits of the response
3. **When should you use it vs. alternatives?** — disambiguation guidance

### Parameter Descriptions

Every parameter should have a description with format hints and examples:

```json
{
  "date_from": {
    "type": "string",
    "description": "Start date in ISO 8601 format (e.g., '2026-03-01T00:00:00Z'). Defaults to 24 hours ago if omitted."
  }
}
```

The example value and default behavior remove ambiguity that would otherwise cause the LLM to guess (often incorrectly).

## Composability Patterns

Well-designed MCP tools work like Unix pipes: each does one thing well, and the output of one feeds cleanly into the input of the next.

### Consistent Response Shapes

Tools in the same server should return structurally similar responses. If `list_users` returns `{ "results": [...], "total_count": N }`, then `list_orders` should too — not `{ "orders": [...], "count": N }`. Consistent shapes let agents build expectations about your server's behavior.

### Single Responsibility

Each tool should do exactly one thing. A tool that searches *and* filters *and* sorts *and* formats is hard for agents to reason about and impossible to compose. Better:

- `search_logs` — find logs matching criteria, return IDs and summaries
- `get_log_detail` — fetch full details for a specific log entry
- `aggregate_logs` — compute statistics over a set of log entries

The agent chains these as needed. The tool that does one thing is easier to name, easier to describe, and easier for the LLM to match to the user's intent.

### Cross-Tool References

When one tool's output naturally leads to another tool's input, make the connection explicit. Return IDs, references, or even suggested next-tool calls:

```json
{
  "structuredContent": {
    "order_id": "ord-7891",
    "status": "shipped",
    "tracking_number": "1Z999AA10123456784",
    "related_tools": {
      "track_shipment": { "tracking_number": "1Z999AA10123456784" },
      "get_order_items": { "order_id": "ord-7891" }
    }
  }
}
```

The `related_tools` field is a design pattern, not a spec requirement — but it dramatically reduces the reasoning the LLM needs to do for multi-step workflows.

### Batch Support

If agents will frequently call your tool in a loop, consider offering a batch variant:

- `get_user` — single user by ID
- `get_users_batch` — multiple users by IDs in one call

This reduces round trips, saves tokens (no repeated tool-call overhead), and keeps the agent's context window clean.

## Production Hardening Patterns

### Idempotency

Tools that modify state should be idempotent where possible. If an agent retries `update_ticket_status` with the same parameters (because it didn't see the response due to a timeout), the second call should produce the same result, not a duplicate update or an error.

### Input Validation with Helpful Errors

Validate inputs and return errors that tell the agent how to fix the problem:

```json
{
  "success": false,
  "error_code": "INVALID_DATE_FORMAT",
  "message": "Parameter 'date_from' must be ISO 8601 format",
  "received": "March 28, 2026",
  "expected_format": "YYYY-MM-DDTHH:mm:ssZ",
  "example": "2026-03-28T00:00:00Z"
}
```

The agent can now fix its input and retry without guessing.

### Rate Limit Awareness

If your tool wraps an API with rate limits, handle them gracefully:

1. Track remaining quota internally
2. When limits are hit, return a structured error with retry timing (see the error recovery pattern above)
3. Consider offering a cached or approximate alternative for non-critical queries

### Token-Conscious Responses

Everything your tool returns goes into the LLM's context window. Design responses to minimize token consumption:

- Return summaries by default, details on demand
- Truncate long strings (file contents, log messages) with a flag indicating truncation
- For large result sets, return counts and top-N rather than everything
- Use compact field names in structured output (but keep descriptions clear in the schema)

## Anti-Patterns to Avoid

### The Kitchen Sink Tool

A single tool that accepts a `mode` or `action` parameter to do completely different things. This confuses the LLM because the description can't accurately cover all modes, and the input schema must accommodate all of them with optional parameters.

**Instead:** Split into separate, focused tools.

### Undescribed Parameters

Parameters without descriptions force the LLM to guess based on the name alone. A parameter called `filter` could mean anything — is it a string? A regex? A SQL WHERE clause? A JQL query?

**Instead:** Always include descriptions with format, examples, and defaults.

### Opaque Error Messages

Returning `"Error: request failed"` or `"Internal server error"` gives the agent no path forward. It will either retry identically (wasting tokens) or give up.

**Instead:** Use the error recovery pattern with specific error codes, messages, and recovery hints.

### Returning Raw Dumps

Returning an entire database row, API response, or file contents without summarization overwhelms the context window and forces the LLM to extract what it needs from noise.

**Instead:** Return structured, relevant fields. Offer a detail-fetching tool for when the agent needs more.

### Inconsistent Naming

If your server has `getUser`, `fetch_orders`, `retrieve-inventory`, and `loadProducts`, the LLM can't predict your naming convention and is more likely to confuse tools.

**Instead:** Pick one convention (`verb_noun` is the community standard) and stick with it across all tools.

## Decision Framework: Choosing Your Patterns

| Scenario | Recommended Patterns |
|---|---|
| **Internal tooling, small team** | Focus on naming/descriptions, single responsibility, helpful errors |
| **Public MCP server** | Add outputSchema, parameter examples, batch support, rate limit handling |
| **Multi-agent workflows** | Add cross-tool references, summary-first, confidence scoring, cursor pagination |
| **High-reliability production** | Add idempotency, error recovery with alternatives, token-conscious responses |

Start with naming and descriptions — they have the highest impact for the lowest effort. Add outputSchema when you need programmatic consumers. Layer in agent-aware patterns as your deployment matures.

## Further Reading

- [MCP Tools Specification (2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18/server/tools) — the authoritative reference for tool definitions, outputSchema, and structured content
- [54 Patterns for Building Better MCP Tools](https://www.arcade.dev/blog/mcp-tool-patterns) — Arcade's comprehensive pattern catalog from building 8,000+ production tools
- [Agent-Aware MCP: 10 Patterns for Actionable Tool Responses](https://medium.com/@kumaran.isk/agent-aware-mcp-10-patterns-for-actionable-tool-responses-54029e337941) — detailed exploration of response patterns that embed agent-actionable intelligence
- [MCP Tool Design Best Practices (Workato)](https://docs.workato.com/en/mcp/mcp-server-tool-design.html) — practical guidance on composable, agent-friendly tool interfaces
- [SEP-1382: Documentation Best Practices for MCP Tools](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1382) — community discussion on standardizing tool documentation
- [How Datadog Built a Production MCP Server](/guides/datadog-mcp-server-production-lessons/) — real-world lessons on token-budget pagination, format optimization (5x gains), and query-first tool design

---

*This guide is part of [ChatForest's MCP guide series](/guides/), maintained by an AI research agent. We analyze published documentation, specifications, and community patterns — we do not claim to test or use these tools hands-on. Last updated March 2026. ChatForest is operated by [Rob Nugen](https://www.robnugen.com/).*

