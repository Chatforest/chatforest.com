---
title: "Building A2A Agents: A Practical Guide to Agent-to-Agent Communication"
date: 2026-03-28T19:00:00+09:00
description: "How to build agents that discover and communicate with each other using the A2A protocol — covering Agent Cards, task lifecycle, streaming, multi-turn conversations, MCP"
content_type: "Guide"
card_description: "MCP connects agents to tools. A2A connects agents to each other. This guide walks through building agents that can discover, negotiate, and collaborate using the A2A protocol."
last_refreshed: 2026-03-28
---

You've built an AI agent that can call tools via [MCP](/guides/what-is-mcp/). Now you want it to collaborate with *other* agents — a research agent that gathers data, a writing agent that drafts content, a review agent that checks quality. Each agent is an independent service with its own capabilities. How do they find each other? How do they exchange tasks and results?

That's what the [A2A (Agent-to-Agent) protocol](https://a2a-protocol.org/) solves. Created by Google in April 2025 and donated to the Linux Foundation in June 2025, A2A standardizes agent discovery, task delegation, and result exchange. As of March 2026, it's backed by 100+ companies, governed by the Linux Foundation alongside MCP, and supported by stable SDKs in five languages.

This guide covers how to actually build A2A agents. For a higher-level comparison of MCP and A2A, see our [MCP vs A2A protocol comparison](/guides/mcp-vs-a2a-protocol-comparison/). For multi-agent architecture patterns, see our [multi-agent architectures guide](/guides/mcp-multi-agent-architectures/).

Our analysis draws on the [A2A specification](https://a2a-protocol.org/latest/specification/), official SDK documentation, published implementation examples, and the [a2a-samples repository](https://github.com/a2aproject/a2a-samples) — we research and analyze rather than building these systems ourselves.

## Why A2A Exists

Before A2A, connecting agents meant custom integration for every pair. Agent A calls Agent B's REST API directly. Agent C uses a message queue. Agent D expects a webhook. Each connection is bespoke, and adding a new agent means writing new integration code for every existing agent it needs to talk to.

A2A replaces this with a standard protocol. Every A2A agent:
- **Publishes an Agent Card** describing what it can do
- **Accepts tasks** through a standard API
- **Reports progress** through a standard lifecycle
- **Returns results** as structured artifacts

The relationship between MCP and A2A is straightforward: **MCP is vertical (agent-to-tool), A2A is horizontal (agent-to-agent)**. An agent might use MCP to query a database, then use A2A to send those results to another agent for analysis. Both protocols are now under Linux Foundation governance, and they're designed to work together.

## Core Concepts

### Agent Cards

Every A2A agent publishes a JSON document — its Agent Card — at `/.well-known/agent.json`. This is how agents discover each other. An Agent Card describes identity, capabilities, skills, endpoints, and security requirements:

```json
{
  "name": "Research Agent",
  "description": "Searches the web and synthesizes findings into structured reports",
  "version": "1.0.0",
  "icon_url": "https://example.com/research-icon.png",
  "provider": {
    "organization": "Example Corp",
    "url": "https://example.com"
  },
  "supported_interfaces": [
    {
      "protocol_binding": "JSONRPC",
      "url": "https://research.example.com/a2a"
    }
  ],
  "capabilities": {
    "streaming": true,
    "pushNotifications": true,
    "multiTurn": true,
    "extendedAgentCard": false
  },
  "skills": [
    {
      "id": "web_research",
      "name": "Web Research",
      "description": "Searches the web for a given topic and returns a structured summary",
      "tags": ["research", "search", "summarization"],
      "examples": ["Research the latest trends in AI agent frameworks"],
      "input_modes": ["text"],
      "output_modes": ["text"]
    }
  ],
  "securitySchemes": [
    {
      "type": "oauth2",
      "flows": {
        "clientCredentials": {
          "tokenUrl": "https://auth.example.com/token",
          "scopes": {
            "research:read": "Execute research queries"
          }
        }
      }
    }
  ]
}
```

The `skills` array is particularly important. Each skill describes a specific capability with input/output modes, tags for categorization, and example prompts. Client agents use these to determine whether a remote agent can handle their request.

The `capabilities` object declares what interaction patterns the agent supports — streaming responses, push notifications for long-running tasks, and multi-turn conversations.

### Tasks

Tasks are the fundamental unit of work in A2A. When a client agent sends a request, the server creates a Task and manages it through a defined lifecycle:

```
submitted → working → completed
                   → failed
                   → canceled
                   → input_required → (client responds) → working → ...
                   → auth_required → (client authenticates) → working → ...
```

Each task has:
- **`id`** — server-generated unique identifier
- **`contextId`** — groups related tasks in a conversation
- **`status`** — current lifecycle state
- **`messages`** — conversation history between client and server
- **`artifacts`** — generated outputs (files, data, text)

The `input_required` state is what enables multi-turn interactions. When an agent needs clarification, it transitions the task to `input_required`, and the client responds with additional messages using the same `taskId` and `contextId`.

### Messages and Parts

Messages carry the actual content exchanged between agents. Each message has a `role` ("user" for client, "agent" for server) and contains one or more Parts:

- **TextPart** — plain text content
- **DataPart** — structured JSON data
- **FilePart** — binary content or file URI references

This flexible structure means agents can exchange anything from simple text to complex structured data to file attachments — all within the same protocol.

### Artifacts

Artifacts are the tangible outputs of a completed task. While messages represent the conversation, artifacts represent the deliverables. An artifact includes an `id`, `mediaType`, and one or more Parts containing the actual content.

For example, a code review agent might return:
- An artifact with `mediaType: "text/markdown"` containing the review summary
- An artifact with `mediaType: "application/json"` containing structured findings

## Building Your First A2A Agent

### SDK Setup

A2A has stable SDKs in five languages:

| Language | Package | Install |
|----------|---------|---------|
| Python | `a2a-sdk` | `pip install a2a-sdk` |
| TypeScript | `@a2a-js/sdk` | `npm install @a2a-js/sdk` |
| Go | `a2a-go` | `go get github.com/a2aproject/a2a-go` |
| Java | `a2a-java` | Maven dependency |
| .NET | `A2A` | `dotnet add package A2A` |

The Python SDK offers extras for specific needs:

```bash
pip install a2a-sdk[http-server]     # HTTP server support
pip install a2a-sdk[grpc]            # gRPC support
pip install a2a-sdk[telemetry]       # OpenTelemetry tracing
pip install a2a-sdk[all]             # Everything
```

### Creating an A2A Server (Python)

Here's the structure of a basic A2A agent server:

```python
from a2a.types import AgentCard, AgentSkill, AgentCapabilities, AgentInterface

# 1. Define the Agent Card
skill = AgentSkill(
    id="summarize",
    name="Text Summarization",
    description="Summarizes long text into concise bullet points",
    tags=["summarization", "text"],
    examples=["Summarize this article about quantum computing"],
    input_modes=["text"],
    output_modes=["text"],
)

agent_card = AgentCard(
    name="Summarizer Agent",
    description="Summarizes text into concise bullet points",
    version="1.0.0",
    default_input_modes=["text"],
    default_output_modes=["text"],
    capabilities=AgentCapabilities(
        streaming=True,
        extended_agent_card=False,
    ),
    supported_interfaces=[
        AgentInterface(
            protocol_binding="JSONRPC",
            url="http://localhost:8000",
        )
    ],
    skills=[skill],
)

# 2. Implement the task handler
# The handler receives messages and returns responses
# through the task lifecycle (working → completed)

# 3. Start the server
# The SDK handles JSON-RPC routing, task state management,
# and Agent Card serving at /.well-known/agent.json
```

The key implementation work is in the task handler — the logic that processes incoming messages, manages task state transitions, and produces artifacts. The SDK handles protocol details like JSON-RPC routing and Agent Card serving.

### Creating an A2A Client

A client agent discovers and communicates with server agents:

```python
# 1. Discover agent by fetching its Agent Card
# GET https://summarizer.example.com/.well-known/agent.json

# 2. Check capabilities and skills
# Does this agent support streaming? Multi-turn?
# Does it have a skill matching our needs?

# 3. Send a message to create a task
# POST https://summarizer.example.com/messages
# {
#   "message": {
#     "role": "user",
#     "parts": [{"text": "Summarize this: ..."}]
#   }
# }

# 4. Receive task with status and artifacts
# The response includes a Task object with the current
# status, messages, and any generated artifacts
```

### Interaction Patterns

A2A supports multiple execution modes:

**Blocking (synchronous)** — the client waits for the task to reach a terminal state:
```
Client → SendMessage → waits → receives completed Task
```

**Non-blocking** — the client gets an immediate response and checks back later:
```
Client → SendMessage (returnImmediately: true) → receives Task in "working" state
Client → GetTask(taskId) → polls for completion
```

**Streaming (SSE)** — the client receives real-time updates via Server-Sent Events:
```
Client → SendStreamingMessage → receives SSE stream
  ← TaskStatusUpdateEvent (working)
  ← Message (partial result)
  ← TaskArtifactUpdateEvent (artifact ready)
  ← TaskStatusUpdateEvent (completed)
```

**Push notifications** — for long-running tasks where the client disconnects:
```
Client → SendMessage + PushNotificationConfig (webhookUrl)
... time passes ...
Server → POST to webhookUrl with TaskStatusUpdateEvent
```

## Multi-Turn Conversations

Real agent collaboration often requires back-and-forth. A2A handles this through the `contextId` and `input_required` state:

```
Client: "Analyze this dataset" (new contextId assigned by server)
  → Task created: {id: "task-1", contextId: "ctx-1", status: "working"}

Server: "I found 3 anomalies. Should I focus on outliers or trends?"
  → Task updated: {id: "task-1", status: "input_required"}

Client: "Focus on outliers" (same taskId and contextId)
  → Task updated: {id: "task-1", status: "working"}

Server: [generates analysis artifact]
  → Task updated: {id: "task-1", status: "completed", artifacts: [...]}
```

The `contextId` groups related tasks, so if the client later asks "Now analyze the trends too," the server can reference the original conversation context.

## A2A + MCP: The Complete Architecture

The most powerful multi-agent systems use both protocols. Here's how they fit together:

```
┌──────────────────────────────────────────────────┐
│                  User / Application               │
└─────────────────────┬────────────────────────────┘
                      │ A2A
                      ▼
┌──────────────────────────────────────────────────┐
│              Coordinator Agent                    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │ MCP:     │  │ MCP:     │  │ MCP:     │      │
│  │ Database │  │ Calendar │  │ Email    │      │
│  └──────────┘  └──────────┘  └──────────┘      │
└────────┬──────────────────────────┬──────────────┘
         │ A2A                      │ A2A
         ▼                          ▼
┌─────────────────┐      ┌─────────────────┐
│ Research Agent   │      │ Writing Agent    │
│  ┌──────────┐   │      │  ┌──────────┐   │
│  │ MCP:     │   │      │  │ MCP:     │   │
│  │ Web      │   │      │  │ File     │   │
│  │ Search   │   │      │  │ System   │   │
│  └──────────┘   │      │  └──────────┘   │
└─────────────────┘      └─────────────────┘
```

Each layer serves a distinct purpose:
- **A2A** handles discovery, task delegation, and result exchange between agents
- **MCP** gives each agent access to its specific tools and data sources

### MCP-A2A Bridge Pattern

You can also bridge the two protocols — an MCP server that wraps an A2A client. This lets MCP-native hosts (like Claude Desktop) interact with A2A agents as if they were MCP tools:

```
Claude Desktop → MCP Client → Bridge MCP Server → A2A Client → Remote A2A Agent
```

The bridge MCP server translates MCP tool calls into A2A messages and returns A2A artifacts as MCP tool results. This means existing MCP-compatible applications gain access to the entire A2A ecosystem without protocol changes.

### When to Use Which

| Scenario | Protocol | Why |
|----------|----------|-----|
| Agent queries a database | MCP | Tool invocation — vertical relationship |
| Agent asks another agent to analyze data | A2A | Agent collaboration — horizontal relationship |
| Agent reads a file from disk | MCP | Resource access — vertical relationship |
| Agent delegates a subtask to a specialist | A2A | Task delegation — horizontal relationship |
| Agent calls a REST API | MCP | Tool invocation with API wrapper |
| Two agents negotiate a plan | A2A | Multi-turn collaboration |
| Agent needs LLM completion from host | MCP (sampling) | Host-provided capability |
| Agent routes work to best-fit agent | A2A | Discovery via Agent Cards + delegation |

## Protocol Details

### Transport Options

A2A spec 0.3 supports three protocol bindings:

**JSON-RPC** — the original and most widely supported binding. Methods include:
- `a2a.sendMessage` — initiate or continue interaction
- `a2a.sendStreamingMessage` — with SSE streaming
- `a2a.getTask` — retrieve task state
- `a2a.listTasks` — enumerate tasks with cursor-based pagination
- `a2a.cancelTask` — request task cancellation
- `a2a.subscribeToTask` — stream updates for an existing task

**HTTP/REST** — added for broader compatibility:
```
POST   /messages              (SendMessage)
POST   /messages:stream       (SendStreamingMessage)
GET    /tasks/{taskId}        (GetTask)
GET    /tasks                 (ListTasks)
POST   /tasks/{taskId}:cancel (CancelTask)
GET    /tasks/{taskId}:subscribe (SubscribeToTask)
```

**gRPC** — added in spec 0.3 for high-performance scenarios. The normative source is now `spec/a2a.proto` (Protocol Buffers), and the gRPC binding maps directly to the same operations.

### Agent Card Signing

Spec 0.3 introduced Agent Card signing for authenticity verification. The `signature` field in an Agent Card lets clients verify that the card was published by the claimed provider — important in enterprise environments where agents must verify each other's identity before exchanging sensitive data.

### Error Handling

A2A defines typed errors for common failure modes:

- `TaskNotFoundError` — referenced task doesn't exist
- `TaskNotCancelableError` — task is in a terminal state
- `PushNotificationNotSupportedError` — agent doesn't support push
- `UnsupportedOperationError` — requested operation not implemented
- `ContentTypeNotSupportedError` — media type mismatch
- `InvalidAgentResponseError` — malformed response
- `VersionNotSupportedError` — spec version mismatch

Each error includes a machine-readable code, human-readable message, and optional details object. This is significantly more structured than raw HTTP error codes, making it easier to build resilient client agents that can recover gracefully.

## Real-World Scenarios

### Travel Planning

A coordinator agent receives "Plan a 5-day trip to Tokyo." It:

1. Fetches the Agent Card from a Weather Agent at `weather-agent.example.com/.well-known/agent.json`
2. Sends an A2A task: "Get the 5-day forecast for Tokyo"
3. Fetches the Agent Card from an Activities Agent
4. Sends an A2A task: "Recommend outdoor activities in Tokyo" with the weather data as context
5. Combines results into a trip plan

Each specialist agent operates independently — it might use MCP tools internally (weather APIs, activity databases) but the coordination happens through A2A tasks.

### Enterprise Workflow

A customer service agent receives "My order hasn't arrived." It:

1. Discovers available agents via Agent Cards (logistics, billing, returns)
2. Delegates to the Logistics Agent: "Track order #12345"
3. The Logistics Agent transitions to `input_required`: "Which shipment — the order was split into 2 packages"
4. The customer service agent responds with the customer's preference
5. The Logistics Agent completes with tracking details as an artifact
6. The customer service agent synthesizes and responds to the customer

The `input_required` state enables genuine collaboration, not just one-shot delegation.

### Code Review Pipeline

A review coordinator receives a pull request and orchestrates:

1. **Security Agent** — scans for vulnerabilities (uses MCP tools: static analysis, dependency checker)
2. **Style Agent** — checks code style compliance (uses MCP tools: linter, formatter)
3. **Logic Agent** — reviews business logic (uses MCP tools: test runner, documentation)

All three tasks run in parallel. The coordinator waits for all to complete, then merges artifacts into a consolidated review. If any agent transitions to `input_required`, the coordinator provides context from the other agents' findings.

## Production Considerations

### Authentication and Security

A2A uses standard HTTP authentication mechanisms declared in Agent Cards:

- **OAuth 2.0** — client credentials flow for service-to-service communication
- **OpenID Connect** — when agent identity verification is required
- **API keys** — for simpler setups
- **mTLS** — for zero-trust environments

Credentials travel in HTTP headers, not in protocol payloads. Per-skill OAuth scopes enable fine-grained authorization — a client might have permission to use an agent's "search" skill but not its "admin" skill.

HTTPS is mandatory for production. TLS 1.2+ with strong cipher suites is expected. Consider certificate pinning for critical inter-agent communication.

### Observability

The Python SDK includes an OpenTelemetry extra (`a2a-sdk[telemetry]`) for distributed tracing. W3C trace context headers propagate across agent boundaries, giving you end-to-end visibility into multi-agent workflows.

Key observability practices:
- **Structured logging** with `taskId`, `contextId`, and trace context in every log entry
- **Metrics** on request rates, error rates, and latency per agent and per skill
- **Audit logging** for sensitive operations (data access, external API calls)

### Scaling and Performance

- **Cursor-based pagination** for `listTasks` — `pageToken`/`nextPageToken` pattern, page sizes 1-100
- **Streaming** reduces latency for large responses — the client starts processing before the full response is ready
- **Push notifications** eliminate polling for long-running tasks
- **gRPC binding** (spec 0.3) provides better performance for high-throughput scenarios with Protocol Buffer serialization

### Version Management

A2A uses an `A2A-Version` header for version negotiation. Agents should handle `VersionNotSupportedError` gracefully and include deprecation timelines when evolving their Agent Cards.

### Extended Agent Cards

For agents with sensitive capability details, A2A supports extended Agent Cards — a separate, authenticated endpoint with detailed information not in the public card. The public card sets `capabilities.extendedAgentCard: true` to signal availability.

## The Broader Ecosystem

A2A doesn't exist in isolation. The current agent protocol landscape:

| Protocol | Focus | Governance | Status |
|----------|-------|------------|--------|
| [MCP](/guides/what-is-mcp/) | Agent-to-tool | Linux Foundation (AAIF) | Mature, widely adopted |
| A2A | Agent-to-agent | Linux Foundation | Stable, growing adoption |
| [AGENTS.md](/guides/agentic-web-agents-md-llms-txt/) | Agent discovery on websites | Community | Rapidly adopted (60k+ repos) |
| [llms.txt](/guides/agentic-web-agents-md-llms-txt/) | LLM-readable site summaries | Community | Growing adoption |

IBM's Agent Communication Protocol (ACP) merged into A2A in August 2025, consolidating the agent-to-agent space. The Linux Foundation's Agentic AI Foundation (AAIF), co-founded by OpenAI, Anthropic, Google, Microsoft, AWS, and Block in December 2025, now governs both MCP and provides the broader context for A2A's governance.

Framework support is broad. The [a2a-samples repository](https://github.com/a2aproject/a2a-samples) includes examples for LangGraph, CrewAI, Google ADK, and Semantic Kernel agents exposed as A2A servers.

## Getting Started

If you're ready to build A2A agents, here's a practical path:

1. **Start with the Python SDK** — `pip install a2a-sdk[http-server]` and work through the [a2a-samples](https://github.com/a2aproject/a2a-samples) examples
2. **Build a simple server agent** — define an Agent Card, implement a task handler, serve it locally
3. **Build a client agent** — discover the server agent's card, send messages, handle task lifecycle
4. **Add streaming** — upgrade to `sendStreamingMessage` for real-time updates
5. **Integrate with MCP** — give your agent MCP tools for actual capabilities, A2A for coordination
6. **Harden for production** — add authentication, observability, error handling

For agents that also need MCP capabilities, see our guides on [building your first MCP server](/guides/build-your-first-mcp-server/), [MCP tool design patterns](/guides/mcp-tool-design-patterns/), and [MCP in production](/guides/mcp-in-production/).

## Related Guides

- [A2A Protocol Hits v1.0](/guides/a2a-protocol-v1-production-ready/) — What changed in the first production-ready release (gRPC, signed Agent Cards, multi-tenancy)
- [MCP vs A2A Protocol Comparison](/guides/mcp-vs-a2a-protocol-comparison/) — Understanding the two protocols shaping AI agent infrastructure
- [AI Agent Protocol Stack 2026](/guides/ai-agent-protocol-stack-2026/) — How MCP, A2A, and four other protocols layer together
- [Conway: Anthropic's Always-On Agent Platform](/guides/anthropic-conway-always-on-agent-platform/) — Anthropic's persistent agent runtime with webhooks, extensions, and always-on operation

---

*This guide is part of the [ChatForest MCP guide series](/guides/), maintained by [Rob Nugen](https://www.robnugen.com/) and AI collaborators. Last updated March 28, 2026.*
