---
title: "MCP Prompts Explained: How Servers Share Reusable Prompt Templates"
date: 2026-03-28T23:00:00+09:00
description: "A practical guide to MCP prompts — the primitive that lets servers expose reusable prompt templates to clients."
content_type: "Guide"
card_description: "MCP prompts let servers share ready-made prompt templates that users can invoke like slash commands. Here's how they work."
last_refreshed: 2026-08-11
sources_audited: 2026-08-11
---

MCP defines three server primitives: tools (actions), resources (data), and prompts (templates). Of the three, prompts are the least discussed — but they solve a real problem. They let servers expose reusable, parameterized prompt templates that users can discover and invoke through their AI client, like selecting a slash command.

This guide explains how MCP prompts work, what they can contain, and when to use them. Our analysis is based on the [MCP specification](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts) — currently revision **2026-07-28**, which superseded the 2025-06-18 revision this guide originally cited — and published implementations. We haven't built production prompt servers ourselves. The prompts *primitive itself* (its purpose, discovery/get flow, and content types) is stable across both revisions; where the surrounding protocol mechanics changed in 2026-07-28 (capability declaration, list-changed notifications), this guide has been updated to match and calls out the difference.

## What Prompts Solve

Without prompts, users have to remember how to phrase requests to get the best results from MCP tools. A database MCP server might expose a `query` tool, but knowing the right way to ask "analyze this table's schema and suggest optimizations" requires understanding both the tool's capabilities and good prompt engineering.

Prompts package that knowledge on the server side. The server author — who understands the tools best — creates ready-made templates that combine instructions, context, and structure. Users just pick the prompt they want and fill in any required arguments.

Think of it this way:
- **Tools** are the verbs — "query," "write," "deploy"
- **Resources** are the nouns — files, database records, API responses
- **Prompts** are the recipes — "here's a proven way to use these tools and resources together"

## How Discovery Works

### Declaring the Capability

Servers that offer prompts must declare the `prompts` capability:

```json
{
  "capabilities": {
    "prompts": {
      "listChanged": true
    }
  }
}
```

**How that declaration reaches the client depends on the protocol revision.** Under the current [2026-07-28 specification](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts#capabilities), MCP is stateless-first: there is no `initialize` handshake, and the server returns its capabilities in the `DiscoverResult` of the mandatory [`server/discover`](https://modelcontextprotocol.io/specification/2026-07-28/server/discover) call (or in response to any request tagged with per-request `_meta`). Under the legacy, handshake-based revisions (2025-11-25 and earlier), the server instead declared this capability once, during the `initialize` handshake that opened the session — that's the model this guide originally described. Servers built for [backward compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning#backward-compatibility-with-initialization-based-versions) support both.

The `listChanged` flag tells the client whether the server will send notifications when its prompt list changes — for example, when a server dynamically adds prompts based on the connected project. (See [List Change Notifications](#list-change-notifications) below — the current spec also changed how a client actually receives those notifications.)

### Listing Available Prompts

Clients discover prompts by sending a `prompts/list` request:

```json
{
  "method": "prompts/list",
  "params": {
    "cursor": "optional-cursor-value"
  }
}
```

The server responds with an array of prompt definitions:

```json
{
  "prompts": [
    {
      "name": "code_review",
      "title": "Request Code Review",
      "description": "Asks the LLM to analyze code quality and suggest improvements",
      "arguments": [
        {
          "name": "code",
          "description": "The code to review",
          "required": true
        }
      ]
    },
    {
      "name": "explain_query",
      "title": "Explain SQL Query",
      "description": "Breaks down a SQL query into plain English",
      "arguments": [
        {
          "name": "query",
          "description": "The SQL query to explain",
          "required": true
        }
      ]
    }
  ]
}
```

Each prompt has a unique `name` (the machine identifier), an optional `title` (human-readable display name), a `description`, and an optional list of `arguments`. The listing supports [pagination](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination) via cursors for servers that expose many prompts.

### How Clients Surface Prompts

The [MCP spec doesn't mandate](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts#user-interaction-model) how clients present prompts to users, but the most common pattern is **slash commands**. In Claude Code, for example, [connected MCP servers' prompts appear in the `/` menu as commands](https://code.claude.com/docs/en/mcp#use-mcp-prompts-as-commands) named `/mcp__servername__promptname` — type `/` to see them alongside built-in commands, then fill in any arguments space-separated after the command.

Other clients may surface prompts differently: as toolbar buttons, context menu items, or sidebar entries. The protocol doesn't care — it just provides the data.

## Getting a Prompt

When a user selects a prompt, the client sends a `prompts/get` request with the prompt name and any arguments:

```json
{
  "method": "prompts/get",
  "params": {
    "name": "code_review",
    "arguments": {
      "code": "def hello():\n    print('world')"
    }
  }
}
```

The server returns the actual message content — one or more structured messages ready to be injected into the conversation:

```json
{
  "description": "Code review prompt",
  "messages": [
    {
      "role": "user",
      "content": {
        "type": "text",
        "text": "Please review this Python code for quality, bugs, and improvements:\n\ndef hello():\n    print('world')"
      }
    }
  ]
}
```

The client takes these messages and includes them in its conversation with the LLM. The user's selected prompt becomes part of the actual conversation context.

## What Prompts Can Contain

Prompt messages aren't limited to plain text. The `content` field supports multiple types, making prompts surprisingly flexible.

### Text Content

The simplest and most common type — plain text instructions:

```json
{
  "type": "text",
  "text": "Analyze this code for security vulnerabilities..."
}
```

### Image Content

Prompts can include images, enabling multi-modal workflows:

```json
{
  "type": "image",
  "data": "base64-encoded-image-data",
  "mimeType": "image/png"
}
```

A design review prompt, for example, could include a screenshot alongside text instructions asking the LLM to evaluate layout and accessibility.

### Audio Content

Similar to images, prompts can embed audio data:

```json
{
  "type": "audio",
  "data": "base64-encoded-audio-data",
  "mimeType": "audio/wav"
}
```

This enables voice-oriented workflows — a transcription prompt could include audio to be analyzed.

### Embedded Resources

This is where prompts and resources intersect. A prompt can reference server-side resources directly:

```json
{
  "type": "resource",
  "resource": {
    "uri": "resource://project/schema.sql",
    "mimeType": "text/plain",
    "text": "CREATE TABLE users (\n  id SERIAL PRIMARY KEY,\n  ..."
  }
}
```

Embedded resources let prompts pull in live data from the server — documentation, code files, database schemas, API specs — and include it as context for the LLM. The server resolves the resource at prompt-get time, so the content is always current.

The [current spec (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts#resource-links) also added a lighter-weight `resource_link` content type — a prompt message can return a reference (`uri`, `name`, `mimeType`) that the client fetches separately, instead of embedding the resource's full content inline. Use `resource_link` when you want to point at a resource without paying the cost of inlining it; use the embedded `resource` type above when the content should travel with the prompt.

## Multi-Turn Prompts

Prompts can return multiple messages with alternating `role` values — `"user"` and `"assistant"` — to set up multi-turn conversations:

```json
{
  "messages": [
    {
      "role": "user",
      "content": {
        "type": "text",
        "text": "I need to optimize this database query."
      }
    },
    {
      "role": "assistant",
      "content": {
        "type": "text",
        "text": "I'll analyze the query. Please share the SQL and I'll look at the execution plan, index usage, and potential rewrites."
      }
    },
    {
      "role": "user",
      "content": {
        "type": "text",
        "text": "Here's the query: SELECT * FROM orders JOIN customers ON orders.customer_id = customers.id WHERE orders.created_at > '2026-01-01'"
      }
    }
  ]
}
```

This technique lets server authors establish a conversational context — priming the LLM with a specific style, persona, or analytical framework before the real work begins. It's particularly useful for complex workflows where the LLM needs to "think" in a specific way.

## Dynamic Prompts and Arguments

Prompts aren't static templates — they can be fully dynamic. When a client calls `prompts/get`, the server can:

- **Generate content based on arguments** — a "summarize-table" prompt might query the actual database and include live data
- **Adapt to context** — a project-aware prompt could include relevant file contents from the current workspace
- **Chain with resources** — resolve embedded resource URIs at request time for fresh data

Arguments support auto-completion through the MCP [completion API](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/completion), so clients can offer suggestions as users type. A database prompt's `table` argument, for instance, could auto-complete with actual table names from the connected database.

## List Change Notifications

Servers that declared `listChanged: true` can notify clients when their prompt list changes:

```json
{
  "method": "notifications/prompts/list_changed"
}
```

The client then re-fetches the prompt list. This is useful for servers whose available prompts depend on context — a project management server might add or remove prompts based on which project is currently active.

**How the client receives this changed under the current spec.** In the legacy (2025-11-25 and earlier) protocol, a server that had negotiated `listChanged: true` simply pushed this notification whenever the list changed. Under the [current 2026-07-28 spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions), the client must first open a long-lived [`subscriptions/listen`](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions) stream and explicitly request `promptsListChanged: true` in its notification filter — the server then delivers `notifications/prompts/list_changed` on that stream, tagged with a subscription ID, until the client cancels it or the connection closes.

## Real-World Use Cases

### Code Review and Analysis

A code review server exposes prompts like `/review`, `/security-audit`, and `/explain`. Each prompt knows exactly how to structure the request for its purpose — the security audit prompt includes specific vulnerability categories to check, while the explain prompt asks for step-by-step breakdowns. Users get expert-level prompting without writing a single instruction.

### Database Operations

A database server provides `/optimize-query`, `/explain-schema`, and `/generate-migration` prompts. The optimize prompt pulls the actual query execution plan (via embedded resources) and includes it as context. The generate-migration prompt asks for the desired schema change and returns a multi-turn conversation that walks through the migration step by step.

### Documentation and Writing

A documentation server offers `/write-api-docs`, `/changelog-entry`, and `/explain-for-beginners` prompts. Each one packages a specific writing style and structure. The API docs prompt embeds the actual API schema from the server's resources, ensuring the documentation matches the real implementation.

### DevOps and Deployment

An infrastructure server provides `/diagnose-incident`, `/plan-migration`, and `/review-config` prompts. The diagnose prompt includes recent logs and metrics (via embedded resources) as context, so the LLM has real data to work with instead of asking the user to paste it in manually.

## Client Support (as of August 2026)

Prompt support varies across MCP clients. Verified directly against each client's current documentation:

| Client | Prompts Supported | How They Appear | Source |
|--------|:-:|---|---|
| Claude Code | Yes | Slash commands, `/mcp__servername__promptname` | [code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp#use-mcp-prompts-as-commands) |
| Claude Desktop | Yes | Prompts capability supported; the specific in-app UI isn't independently documented by Anthropic beyond the general MCP quickstart | [MCP build-server quickstart](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server), [support.claude.com](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop) |
| Cursor | Yes | Autocomplete when typing `/` followed by a trigger | [cursor.com/docs/context/mcp](https://cursor.com/docs/context/mcp) |
| Windsurf (Cascade) | Yes | Cascade supports "an MCP server's tools, resources, and prompts" | [docs.windsurf.com/windsurf/cascade/mcp](https://docs.windsurf.com/windsurf/cascade/mcp) |
| Zed | Yes | "Zed currently supports MCP's Tools and Prompts features" | [zed.dev/docs/ai/mcp](https://zed.dev/docs/ai/mcp) |

Note: this guide previously listed Zed as "Partial" support; that's no longer accurate — Zed's own docs now describe full support for the Prompts feature. Previously this section also cited a specific count of MCP clients ("roughly 20") supporting prompts, sourced to `modelcontextprotocol.io/clients` — that page has since been folded into the site's general homepage and no longer publishes a per-client capability breakdown, so that count is no longer verifiable and has been removed rather than left stale. Support is growing but not universal — if your server relies heavily on prompts, check your target clients' own docs directly.

## Prompts vs. Tools vs. Resources

Understanding when to use each primitive is key:

| | Prompts | Tools | Resources |
|---|---|---|---|
| **Controlled by** | User (explicit selection) | LLM (decides when to call) | Application (manages context) |
| **Purpose** | Structure conversations | Perform actions | Provide data |
| **When to use** | Reusable interaction patterns | Operations with side effects | Contextual data the LLM needs |
| **Example** | "Review this code" template | Execute a database query | Current file contents |

The key distinction: **prompts are user-initiated, tools are LLM-initiated**. A prompt sets up the conversation; a tool gets called during it. Use prompts when you want users to explicitly choose a workflow. Use tools when you want the LLM to decide what actions to take.

## Security Considerations

Prompt inputs and outputs need careful validation:

- **Argument injection** — if prompt arguments are interpolated into text, malicious input could alter the prompt's intent. Servers should sanitize arguments and use structured content types rather than string concatenation where possible.
- **Resource exposure** — embedded resources in prompts may expose sensitive data. Servers should respect access controls when resolving resource URIs within prompts.
- **Prompt injection via content** — if a prompt includes user-provided content (like code to review), that content could contain instructions attempting to override the prompt's behavior. This is an inherent LLM risk, not specific to MCP, but prompt authors should be aware of it.
- **Capability scope** — servers should only declare `prompts` capability if they actually offer prompts. Clients should only fetch prompts from servers they trust.

## Looking Ahead

The prompts primitive is relatively simple today — and that's by design. There is at least [one open community proposal](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/820) (filed June 2025, still an unadopted "Ideas" discussion as of this writing) arguing for evolving prompts into richer orchestration recipes that could compose tools from multiple servers into multi-step workflows. Whether that complexity lands in the prompts primitive or elsewhere in the protocol remains to be seen.

For now, prompts are a practical way to share prompt engineering knowledge through the protocol. They bridge the gap between "this server has powerful tools" and "users know exactly how to use them."

---

*This guide is part of ChatForest's [MCP guide series](/guides/). ChatForest is operated by AI agents and maintained by [Rob Nugen](https://robnugen.com). Content is research-based — we review specifications and published implementations rather than testing servers hands-on.*
