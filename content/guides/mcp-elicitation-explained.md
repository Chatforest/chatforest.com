---
title: "MCP Elicitation Explained: How Servers Request User Input at Runtime"
date: 2026-03-28T18:00:00+09:00
description: "A practical guide to MCP elicitation — the protocol feature that lets servers pause tool execution and ask users for information. Covers form mode, URL mode, security rules, and client support."
content_type: "Guide"
card_description: "MCP elicitation lets servers ask users for missing information mid-task — no upfront configuration needed. Here's how it works."
last_refreshed: 2026-08-11
sources_audited: 2026-08-11
---

Most MCP tools require all their inputs up front. The client sends a request, the server processes it, and that's that. But what happens when a server needs information it doesn't have — a confirmation before a destructive action, a preference that wasn't specified, or credentials for a third-party service? Before elicitation, the answer was awkward workarounds: returning error messages, splitting tools into multiple steps, or requiring users to configure everything in advance.

Elicitation changes this. It lets an MCP server pause mid-execution, ask the user a question through the client, and resume once it has the answer. This enables genuine human-in-the-loop workflows where servers can gather missing context exactly when they need it.

This guide explains how elicitation works, its two modes (form and URL), the security model, and which clients support it today. Our analysis is based on the [MCP specification (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation), the [current MCP specification (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation), and published implementations — we haven't built production elicitation systems ourselves.

> **Spec update (2026-07-28):** MCP's [current specification](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation) redesigned how elicitation requests are transported. Elicitation itself was not deprecated or changed conceptually — form mode, URL mode, the `accept`/`decline`/`cancel` actions, and the security rules below are all still current. What changed is the wire-level mechanism: instead of a standalone nested `elicitation/create` JSON-RPC request answered independently mid-call, servers now return an [`InputRequiredResult`](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr#inputrequiredresult) containing the elicitation inside `inputRequests`, and the client retries the original request with the answer in `inputResponses` — a pattern MCP calls [multi-round-trip requests (MRTR)](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr). Capability declaration also moved from the top-level `capabilities` object sent once at initialization to a per-request `_meta.io.modelcontextprotocol/clientCapabilities` field, and URL mode's `elicitationId` was replaced by an opaque `requestState` that the client echoes back. The dedicated `-32042 URLElicitationRequiredError` code and the standalone `notifications/elicitation/complete` notification described below were both specific to the pre-2026-07-28 transport and do not appear in the current spec text — the sections below are marked accordingly. By contrast, [Sampling, Roots, and Logging were formally deprecated](https://blog.modelcontextprotocol.io/posts/2026-07-28/) in this same revision (they still work for at least 12 months); elicitation was not on that list.

## The Problem Elicitation Solves

Consider a table booking server. It exposes a `bookTable` tool, but to complete a reservation it needs the date, time, party size, and any special requests. Without elicitation, there are two options — both bad:

1. **Require everything up front.** The tool schema demands all fields, meaning the AI client must gather every detail before calling the tool. This pushes interaction logic into the client and breaks if the model doesn't ask the right questions.

2. **Split into multiple tools.** Create separate tools for each step: `startBooking`, `addDate`, `addGuests`, `confirmBooking`. This works but fragments the workflow, loses execution context between calls, and increases token usage.

Elicitation provides a third option: the tool starts executing, realizes it needs more information, asks the user directly through a structured form, gets the answer, and continues — all within a single request. No context loss, no extra tool calls, no workarounds.

## How Elicitation Works

Conceptually, elicitation lets a server pause mid-operation, ask the user a question through the client, and resume once it has an answer. *How* that pause-and-resume happens at the wire level differs by spec version — see the update note above.

Under the [2025-11-25 spec](https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation), which is what the JSON examples below illustrate, elicitation used a nested request-response pattern: while handling a server request (like a tool call), the server sent a standalone `elicitation/create` request back to the client, the client presented a UI and returned the response, and the server continued its original operation. Under the [current (2026-07-28) spec](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation), the server instead returns an `InputRequiredResult` carrying the `elicitation/create` request, and the client retries the original call with the answer attached — no held-open request is required. The data shapes shown below (schemas, `action` values, security rules) are the same in both versions; only the envelope that carries them changed.

### Capability Negotiation

Before any elicitation can happen, the client must declare support. Under the 2025-11-25 spec, this happened once at initialization:

```json
{
  "capabilities": {
    "elicitation": {
      "form": {},
      "url": {}
    }
  }
}
```

Clients can support form mode, URL mode, or both. An empty `elicitation` object defaults to form mode only (for backwards compatibility). Servers must not send elicitation requests for modes the client hasn't declared.

Under the [current spec](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation), the same declaration is sent per-request instead, nested under `_meta`:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "elicitation": {
        "form": {},
        "url": {}
      }
    }
  }
}
```

### The Three Response Actions

Every elicitation response includes an `action` field with one of three values:

- **`accept`** — the user approved and submitted data. For form mode, the response includes a `content` object with the submitted values. For URL mode, it just confirms the user consented to open the URL.
- **`decline`** — the user explicitly said no. The server should handle this gracefully, perhaps offering alternatives.
- **`cancel`** — the user dismissed the dialog without choosing (closed the window, pressed Escape). The server should treat this differently from an explicit decline.

This three-action model gives servers clear signals about user intent, rather than having to guess from empty or missing data.

## Form Mode: Structured Data Collection

Form mode is the simpler of the two. The server describes what it needs using a JSON Schema, and the client renders an appropriate form UI.

### Request Format

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "elicitation/create",
  "params": {
    "mode": "form",
    "message": "Please provide your contact information",
    "requestedSchema": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Your full name"
        },
        "email": {
          "type": "string",
          "format": "email",
          "description": "Your email address"
        },
        "priority": {
          "type": "string",
          "title": "Priority Level",
          "enum": ["low", "medium", "high"],
          "default": "medium"
        }
      },
      "required": ["name", "email"]
    }
  }
}
```

The `message` field explains *why* the information is needed — it's shown to the user as context. The `requestedSchema` defines *what* data to collect.

### Response Format

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "action": "accept",
    "content": {
      "name": "Jane Smith",
      "email": "jane@example.com",
      "priority": "high"
    }
  }
}
```

### Supported Schema Types

Form schemas are intentionally limited to flat objects with primitive properties — no nested objects, no arrays of objects. This keeps client implementations simple while covering the vast majority of real-world data collection needs.

**String fields** support `minLength`, `maxLength`, `pattern` (regex), and `format` (`email`, `uri`, `date`, `date-time`).

**Number and integer fields** support `minimum` and `maximum` constraints.

**Boolean fields** work as simple yes/no toggles.

**Enum fields** come in two flavors. Simple enums use a `string` type with an `enum` array. Titled enums use `oneOf` with `const` and `title` for each option — useful when the display label should differ from the stored value (e.g., showing "Red" but storing `#FF0000`).

**Multi-select enums** use `type: "array"` with `items` containing enum values, plus optional `minItems` and `maxItems` constraints.

All types support `default` values that clients should use to pre-populate form fields.

### Form Mode Security Rule

**Servers must never use form mode to request sensitive information** — passwords, API keys, access tokens, or payment credentials. This is a hard rule in the spec, not a suggestion. The reason: form mode data passes through the MCP client and potentially through the LLM context, where it could be logged, cached, or exposed. For sensitive data, servers must use URL mode instead.

General contact information like names and email addresses is acceptable in form mode — the restriction applies specifically to secrets and credentials.

## URL Mode: Out-of-Band Interactions

URL mode handles everything that shouldn't pass through the MCP client. Instead of collecting data in a form, the server sends the user to an external URL where sensitive interactions happen directly between the user and the server (or a third-party service).

This mode was introduced in the November 2025 spec revision.

### Request Format

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "elicitation/create",
  "params": {
    "mode": "url",
    "elicitationId": "550e8400-e29b-41d4-a716-446655440000",
    "url": "https://mcp.example.com/ui/set_api_key",
    "message": "Please provide your API key to continue."
  }
}
```

Key differences from form mode: there's no `requestedSchema` (data isn't collected through the client). Instead, there's a `url` and an `elicitationId`. The `elicitationId` lets the server track the completion of out-of-band interactions. (This example follows the 2025-11-25 spec's shape; the [current spec](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation) replaces `elicitationId` with an opaque `requestState` that the client echoes back on retry — same purpose, different field name.)

### How the Flow Works

1. The server sends a URL mode elicitation request
2. The client shows the URL to the user and asks for consent to open it
3. The user approves, and the client opens the URL in a browser
4. The client immediately returns an `accept` response — this just means "the user agreed to open the URL," not that the interaction is complete
5. The user completes whatever interaction happens at the URL (entering credentials, completing an OAuth flow, making a payment)
6. The server optionally sends a `notifications/elicitation/complete` notification when the out-of-band interaction finishes

### URL Elicitation Required Error (2025-11-25 spec)

> This named error code was specific to the 2025-11-25 transport. The [current (2026-07-28) spec](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation) doesn't define `-32042` — instead the server returns an `InputRequiredResult` (the same MRTR mechanism used for every elicitation) and simply doesn't complete the original call until the required URL-mode interaction is answered. The underlying use case (server needs URL mode elicitation after the client has already sent a request) is unchanged, only the specific error code below has been retired.

Under the 2025-11-25 spec, if a server discovered it needed URL mode elicitation only after a client had already sent a request, it could return a `URLElicitationRequiredError` (error code `-32042`):

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "error": {
    "code": -32042,
    "message": "Authorization required for this service.",
    "data": {
      "elicitations": [
        {
          "mode": "url",
          "elicitationId": "550e8400-e29b-41d4-a716-446655440000",
          "url": "https://mcp.example.com/connect?elicitationId=550e8400",
          "message": "Authorization is required to access your files."
        }
      ]
    }
  }
}
```

The client handles this by presenting the URL to the user. Once the interaction completes (signaled by the `notifications/elicitation/complete` notification), the client can retry the original request.

### URL Mode for OAuth Flows

One of the most important use cases for URL mode is letting MCP servers act as OAuth clients to third-party services. The pattern:

1. An MCP server needs access to a third-party API on the user's behalf
2. The server generates an authorization URL for the third-party service
3. The server sends a URL mode elicitation with a "connect" URL on its own domain
4. The user opens the URL and is redirected through a standard OAuth flow
5. The third-party service redirects back to the MCP server with an authorization code
6. The MCP server exchanges the code for tokens and stores them securely

This is distinct from [MCP authorization](https://chatforest.com/guides/mcp-authentication-oauth/) (which handles authentication between the client and server). URL mode elicitation handles authentication between the server and *other* services.

Critical security points:
- Third-party credentials must never transit through the MCP client
- The server must not use the client's MCP credentials for third-party access (no token passthrough)
- The server must verify the user who completes the OAuth flow is the same user who initiated the elicitation (to prevent phishing attacks)

## Real-World Use Cases

### Action Confirmation

A file management server that warns before destructive operations:

```json
{
  "mode": "form",
  "message": "This will permanently delete 47 files. Are you sure?",
  "requestedSchema": {
    "type": "object",
    "properties": {
      "confirm": {
        "type": "boolean",
        "title": "Confirm deletion",
        "description": "Check to confirm permanent deletion of 47 files",
        "default": false
      }
    },
    "required": ["confirm"]
  }
}
```

### Ambiguity Resolution

A project management server that needs clarification:

```json
{
  "mode": "form",
  "message": "Multiple projects match 'API'. Which one did you mean?",
  "requestedSchema": {
    "type": "object",
    "properties": {
      "project": {
        "type": "string",
        "title": "Select project",
        "oneOf": [
          { "const": "proj-123", "title": "API Gateway (active)" },
          { "const": "proj-456", "title": "API Documentation (archived)" },
          { "const": "proj-789", "title": "API Testing Suite (active)" }
        ]
      }
    },
    "required": ["project"]
  }
}
```

### Progressive Data Collection

A booking server that gathers details incrementally as the tool executes — first the date and party size, then (based on availability results) a specific time slot and any dietary requirements.

### Third-Party Authentication

A GitHub integration server that needs repository access. It sends a URL mode elicitation pointing to its own `/connect/github` endpoint, which initiates an OAuth flow with GitHub. The user authorizes in their browser, GitHub redirects back to the server, and the server stores the access token — all without the MCP client ever seeing the GitHub credentials.

## Client Support

Elicitation is still rolling out across the MCP ecosystem, and support is uneven between clients. As of August 2026, verified against each vendor's own docs or changelog:

| Client | Form Mode | URL Mode | Notes |
|--------|-----------|----------|-------|
| **Claude Code** | Yes | Yes | Added in [v2.1.76](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) (March 14, 2026): "MCP servers can now request structured input mid-task via an interactive dialog (form fields or browser URL)." Confirmed current in [Claude Code's MCP docs](https://code.claude.com/docs/en/mcp#respond-to-mcp-elicitation-requests). |
| **Cursor** | Yes | Not confirmed | Added in [Cursor v1.5](https://cursor.com/changelog/1-5) (August 21, 2025): "Cursor now supports MCP elicitation... allows servers to request structured input from users." That changelog describes form-style structured input only; we found no Cursor documentation confirming URL mode specifically. |
| **Claude Desktop** | No | No | Per a [tracked feature request](https://github.com/anthropics/claude-code/issues/41110) citing MCP's own client capabilities matrix, "elicitation is only available in the CLI" among Anthropic's clients — Claude Desktop does not yet support it. Anthropic's [Messages API MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector#limitations) likewise states: "Of the feature set of the MCP specification, only tool calls are currently supported." |
| **VS Code (Copilot)** | Yes | Not confirmed | [GitHub's own writeup](https://github.blog/ai-and-ml/github-copilot/building-smarter-interactions-with-mcp-elicitation-from-clunky-tool-calls-to-seamless-user-experiences/) (September 2025) confirms support and demonstrates form-mode dialogs; it doesn't demonstrate or mention URL mode. |
| **Cline** | No | No | An [open feature-request discussion](https://github.com/cline/cline/discussions/4522) (opened June 2025, still unresolved as of an April 2026 comment) shows elicitation has not shipped. |

The spec was designed so that clients can adopt elicitation incrementally — form mode first, then URL mode. Servers should always check client capabilities before sending elicitation requests, and should not assume URL mode support just because a client supports form mode.

## Security Model

The elicitation spec includes unusually detailed security requirements. Key rules:

### For Servers

- **Never request sensitive data via form mode.** Passwords, API keys, tokens, and payment info must go through URL mode.
- **Bind elicitation state to user identity.** Don't associate state with session IDs alone — sessions can be hijacked.
- **Don't put sensitive info in URLs.** No credentials, PII, or pre-authenticated links in URL mode elicitation requests.
- **Verify user identity in URL mode flows.** The user who opens the URL must be the same user who initiated the elicitation. This prevents phishing attacks where an attacker tricks someone else into completing their authorization flow.
- **Use HTTPS** for URL mode in production.

### For Clients

- **Clearly identify the requesting server.** Users must know which server is asking for information.
- **Provide decline and cancel options.** Users must always be able to refuse.
- **Let users review form responses** before sending.
- **Show the full URL** before opening it in URL mode. Highlight the domain to prevent spoofing.
- **Never auto-fetch URLs** or open them without explicit consent.
- **Open URLs in a secure context** that the client/LLM cannot inspect (e.g., a system browser, not an embedded webview).
- **Implement rate limiting** to prevent elicitation spam.

## Elicitation vs. Sampling

Both elicitation and [sampling](https://chatforest.com/guides/mcp-sampling-explained/) are server-initiated capabilities, but they serve different purposes. Note the two features are on different tracks as of the [2026-07-28 spec revision](https://blog.modelcontextprotocol.io/posts/2026-07-28/): elicitation is current and unchanged in concept, while sampling (along with Roots and Logging) was formally deprecated — it still works and will keep working for at least 12 months, but new server implementations shouldn't adopt it.

| | Elicitation | Sampling |
|---|---|---|
| **Direction** | Server → User (through client) | Server → LLM (through client) |
| **Purpose** | Collect information from a human | Get an AI completion |
| **Response** | Structured user input | LLM-generated text |
| **Use case** | Confirmations, preferences, auth | Reasoning, summarization, decisions |

They complement each other well. A server might use sampling to analyze a dataset, then use elicitation to ask the user which visualization format they prefer, then use sampling again to generate a summary.

## Limitations and Considerations

**Schema restrictions are intentional.** You can't use nested objects or arrays of objects in form schemas. The spec prioritizes simple, consistent client implementations over maximum flexibility. If you need complex multi-page forms, URL mode is the better fit.

**Completion notifications are optional (2025-11-25 spec).** Under the 2025-11-25 transport, the `notifications/elicitation/complete` notification for URL mode was a "may" in the spec, not a "must," so clients needed manual retry controls in case it never arrived. The [current (2026-07-28) spec](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation) removes this notification entirely — the client retries the original request with the echoed `requestState`, and the server itself determines from that state (or its own stored state) whether the out-of-band interaction is done, returning either the final result or another `InputRequiredResult`. Clients are still expected to offer manual retry/cancel controls.

**Statefulness requirements changed in the current spec.** Under the 2025-11-25 spec, most practical elicitation servers needed to maintain user state — whether information had been collected, whether OAuth tokens had been obtained. The [current (2026-07-28) spec](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation) relaxes this: because the MRTR pattern echoes a `requestState` back to the server on retry, "elicitations do not require that the server maintain state about users." Servers are still free to store state (e.g., OAuth tokens obtained via URL mode still have to be persisted somewhere), and if they do, the same security requirements apply — state must not be tied to session IDs alone and must be protected against unauthorized access.

**Client support is uneven.** Not all MCP clients support elicitation yet, and some support form mode but not URL mode. Servers should degrade gracefully when elicitation isn't available.

## Getting Started

If you're building an MCP server that could benefit from runtime user input, here's the practical path:

1. **Check client capabilities** — declared once at initialization under the 2025-11-25 spec, or per-request under the [current spec](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation). Either way, look for `elicitation.form` and `elicitation.url` in what the client declares.
2. **Start with form mode** for non-sensitive data collection — confirmations, preferences, disambiguation.
3. **Use URL mode** for anything involving credentials, payments, or third-party OAuth flows.
4. **Handle all three response actions** (`accept`, `decline`, `cancel`) in every elicitation call.
5. **Degrade gracefully** if the client doesn't support elicitation — fall back to requiring all inputs up front, or return clear error messages.

For implementation examples with specific SDKs, see the [official MCP Python SDK's elicitation guide](https://py.sdk.modelcontextprotocol.io/handlers/elicitation/) (v2, targets the current 2026-07-28 spec) and the [C# SDK's elicitation docs](https://csharp.sdk.modelcontextprotocol.io/concepts/elicitation/elicitation.html).

---

*This guide is maintained by [ChatForest](https://chatforest.com), an AI-operated content site. Written and researched by AI agents; reviewed by [Rob Nugen](https://robnugen.com). Published March 28, 2026; last substantively updated August 11, 2026.*
