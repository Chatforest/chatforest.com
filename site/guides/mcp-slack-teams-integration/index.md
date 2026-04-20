# MCP with Slack and Teams: Building AI Agents for Workplace Chat

> A practical guide to integrating MCP with Slack and Microsoft Teams — covering MCP servers for both platforms, architecture patterns, security risks (including the data


Workplace chat platforms hold your organization's institutional knowledge — decisions made in threads, context buried in channels, tribal knowledge shared in DMs. AI agents that can read and act in these platforms become genuinely useful: triaging incidents, summarizing channels, answering questions from chat history, and automating routine messages.

MCP (Model Context Protocol) provides a standardized way for AI agents to interact with Slack and Microsoft Teams. Instead of writing custom integrations for each platform, agents discover and call tools through a single protocol. Both Slack and Microsoft now offer official MCP support, and several community servers fill the gaps.

But connecting an AI agent to your workplace chat comes with real security risks — including a data exfiltration vulnerability that got Anthropic's original Slack MCP server archived. This guide covers what's available, how to architect it, and what to watch out for. Our analysis draws on published documentation, security disclosures, and community project data — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## Slack MCP Servers

### Slack's Official MCP Server

Slack released its first-party MCP server in February 2026, after previewing it at Dreamforce in October 2025. This is the production-grade option.

**Endpoint:** `https://mcp.slack.com/mcp` (Streamable HTTP transport)

**What it can do:**

| Category | Capabilities |
|----------|-------------|
| Search | Messages, files, users, public and private channels |
| Messages | Send to any conversation, draft and preview, channel history, thread access |
| Canvases | Create, update, read and export as markdown |
| User data | Full profiles, custom fields, statuses |

**Auth:** Standard Slack OAuth 2.0 with user-level permissions. Only directory-published or internal apps are permitted — unlisted apps are blocked. Admin approval flows are built in.

**Rate limits:** Same tiers as the Slack Web API — Tier 2 (~20/min) for search, Tier 3 (~50/min) for reading, Tier 4 (~100/min) for profiles.

**Key limitation:** It exposes a curated subset of the Slack Web API — roughly 10% of the 200+ available methods. If you need full API coverage, you'll still need the native Slack API.

**Supported MCP clients:** Claude.ai, Claude Code, Perplexity, Cursor — no custom code needed.

### The Archived Reference Server (Don't Use This)

The original `@modelcontextprotocol/server-slack` from Anthropic's MCP project was archived in May 2025 after a critical data exfiltration vulnerability. It exposed 8 tools (list channels, post messages, reply to threads, add reactions, get history, get replies, list users, get profiles) via stdio transport.

**Do not use this server.** It has a known security vulnerability that allows data exfiltration through Slack's link unfurling mechanism. We cover the details in the [Security section](#the-slack-mcp-data-exfiltration-vulnerability) below.

### Community Alternatives

**korotovsky/slack-mcp-server** (Go) is the most popular community option with 9,000+ active users. It offers ~13 tools covering conversations, reactions, attachments, channels, and user groups. Notable features include GovSlack support (routes API calls to slack-gov.com for FedRAMP environments) and a "stealth mode" using browser session cookies — useful for testing but not suitable for production since it bypasses Slack's audit trails.

**AVIMBU/slack-mcp-server** (TypeScript) provides ~8 tools with standard OAuth. **Truto** offers a managed SaaS approach with dynamic tool generation from the full Slack API surface, managed OAuth lifecycle, and method-level filtering.

## Microsoft Teams MCP Servers

### Microsoft's Official Support

Microsoft has taken a multi-pronged approach to MCP in Teams:

**Agent Connectors** (public developer preview) let you register any remote MCP server in the Microsoft 365 app manifest. Teams Channel Agent discovers and invokes the MCP tools. Auth options include OAuth 2.0 via Microsoft's secure vault or no auth for internal tools.

**Teams SDK** has native MCP support (GA in C# and JavaScript, preview in Python). Agents built with the Teams SDK can connect to any MCP server as a tool provider.

**Copilot Studio** supports MCP at general availability, enabling no-code/low-code agent builders to connect MCP servers.

### floriscornel/teams-mcp (Community)

The most comprehensive community Teams server with 25 tools across auth, users, teams, chats, media, and search. Key features:

- **KQL-based search** across all Teams conversations
- **HTML-to-markdown conversion** for LLM consumption
- **Large file upload** via resumable upload sessions (>4 MB)
- **Read-only mode** via `--read-only` flag
- **Automatic OAuth token refresh** with Microsoft Graph

Setup is straightforward: `npx @floriscornel/teams-mcp@latest authenticate`

### InditexTech/mcp-teams-server (Community)

A simpler Python server focused on channel messaging — 5 tools for creating threads, replying, reading messages, and listing members. Limited to a single channel per instance (multi-channel requires multiple server instances). Available as a Docker image.

## Server Comparison

| Aspect | Slack (Official) | Slack (korotovsky) | Teams (Agent Connectors) | Teams (floriscornel) |
|--------|-----------------|-------------------|--------------------------|---------------------|
| Status | GA (Feb 2026) | Active | Public Preview | Active |
| Transport | Streamable HTTP | stdio/SSE/HTTP | HTTPS/WSS | stdio (npx) |
| Tools | Curated subset | ~13 tools | SDK-level | 25 tools |
| Auth | OAuth 2.0 (user-level) | Bot token / session cookies | Azure AD / OAuth vault | Graph OAuth (auto-refresh) |
| Read-only mode | No | No | No | Yes |
| File support | Via canvases | Limited | N/A | Yes (large files) |
| Search | Full (messages, files, users) | Messages | N/A | KQL cross-Teams |
| Audit logging | Built-in | No | Via Azure AD | No |
| Multi-tenant | Per-user scoping | Single workspace | Yes | Yes |

## Architecture Patterns

There are four main patterns for connecting AI agents to workplace chat via MCP.

### Pattern 1: AI Client + MCP Server (Personal Use)

The simplest approach. An AI client like Claude Desktop or Cursor connects to the Slack or Teams MCP server as a tool provider. You ask the AI to search Slack, post a message, or summarize a channel.

```
You → AI Client (MCP Host) → Slack/Teams MCP Server → Platform API
```

Good for personal productivity and ad-hoc queries. The limitation is that it requires a human in the loop — the agent can't react to events on its own.

### Pattern 2: Bot as MCP Client (Team Assistant)

A Slack or Teams bot acts as the MCP client, bridging chat messages to MCP servers. Projects like `tuannvm/slack-mcp-client` and `sooperset/mcp-client-slackbot` implement this pattern.

```
User in Slack → Socket Mode/Events API → Bot Process (MCP Client)
    → LLM Provider (Claude, GPT, etc.)
    → MCP Server(s) (filesystem, database, Kubernetes, etc.)
    → Response back to Slack thread
```

The bot listens via Socket Mode (WebSocket, no public endpoint needed) or the Events API (HTTP webhook). The LLM decides which MCP tools to call based on the user's message. Good for team-wide AI assistants in channels.

### Pattern 3: MCP Gateway (Production Multi-Agent)

For production systems with multiple agents, a centralized MCP Gateway handles all tool connections:

```
Multiple Agents → MCP Gateway → [Slack MCP, Teams MCP, Jira MCP, GitHub MCP, ...]
```

The gateway handles auth, rate limiting, observability, and security policies. It solves the N×M integration problem and provides a single point for audit logging and access control. See our [MCP architecture guide](/guides/mcp-transports-explained/) for more on transport patterns.

### Pattern 4: Slack Official MCP + Real-Time Search

Slack's recommended production pattern combines their MCP server with the Real-time Search (RTS) API:

- **MCP Server:** tool execution (send messages, manage canvases)
- **RTS API:** secure, permission-aware search across conversations, files, and threads
- All actions respect individual user permissions at query time

This is the most enterprise-ready approach for Slack specifically.

### The Event Problem

**MCP is request/response, not event-driven.** This is the most common misunderstanding. MCP tools are invoked by the agent — they don't push events to the agent. For real-time reactive behavior (responding when someone posts in a channel, handling @mentions), you need a separate event listener:

| Platform | Real-Time Options |
|----------|------------------|
| Slack | Socket Mode (WebSocket, no public URL), Events API (HTTP webhook) |
| Teams | Graph API webhook subscriptions |

The typical production pattern: a native event listener detects incoming messages and triggers an MCP-equipped agent to handle them. The agent uses MCP tools for its response actions.

## Real-World Use Cases

### Incident Response

PagerDuty alert fires → AI agent uses Slack MCP to search for related error reports in channels, combines with [Datadog MCP](/guides/best-observability-mcp-servers/) for metrics, synthesizes a situation report, and posts it to the incident channel — all before the on-call engineer has finished reading the page.

### Knowledge Retrieval

Engineers ask questions in natural language. The agent searches across Slack history, threads, and files to find answers that would otherwise require scrolling through months of messages. Combined with Slack's RTS API, searches respect the user's actual workspace permissions.

### Channel Summarization

Summarize what happened in a channel while you were away. Generate weekly project updates grounded in actual conversations. Post wrap-up summaries after incident reviews. This works particularly well because LLMs are good at summarization and Slack MCP servers provide the raw material.

### Cross-Platform Bridging

Build a platform-agnostic agent core with channel-specific adapters for Slack and Teams. An API gateway sits between platform integrations and agent logic for unified auth, rate limiting, and routing. This pattern is especially relevant for organizations running both platforms.

### Meeting and Task Automation

Aggregate action items from meeting threads across channels. Route messages to the right team based on content analysis. Auto-create tickets from Slack conversations. Handle on-call handoffs by summarizing the outgoing shift's activity.

## The Slack MCP Data Exfiltration Vulnerability

This is the most important security lesson in the MCP + workplace chat space. Understanding it helps you evaluate *any* MCP server that handles private data.

In May 2025, researchers discovered that Anthropic's `@modelcontextprotocol/server-slack` could be exploited to steal private data:

1. **Prompt injection:** An attacker embeds malicious instructions in content the AI processes — a Slack message, a document, anything in the context.
2. **Data access:** The compromised agent uses Slack MCP tools to retrieve sensitive data (API keys from channels, private messages, etc.).
3. **Exfiltration:** The agent crafts a hyperlink containing the stolen data as URL parameters and posts it to Slack.
4. **Silent delivery:** Slack's link unfurling automatically sends an HTTP request to the attacker's server, delivering the data with no visible indication in the channel.

Security researcher Simon Willison called this "the lethal trifecta" — an AI agent with tool access, private data, and untrusted input in the same context.

**Timeline:** Reported May 27, 2025 → Anthropic archived the server May 29, 2025 → Public disclosure June 24, 2025.

### Broader Security Risks

The vulnerability illustrates patterns that apply across all MCP + chat integrations:

- **Token mismanagement:** Tokens stored in environment variables or config files with no expiry or rotation. A 2025 OWASP analysis found 43% of publicly available MCP servers contained command injection vulnerabilities.
- **Excessive permissions:** Many MCP tools get unrestricted access. An agent that only needs to read channels shouldn't have permission to post messages or access DMs.
- **Tool chaining for data exfiltration:** An agent reads private data via one tool and sends it externally via another. This is particularly dangerous when the agent processes untrusted content.
- **No method-level filtering:** Most open-source servers expose all tools to all callers with no ability to restrict per-user or per-context.

### How to Mitigate

1. **Use official servers when possible.** Slack's first-party MCP server enforces user-level permissions and includes audit logging.
2. **Scope tokens to minimum permissions.** If the agent only reads, don't grant write permissions. Use Teams' `--read-only` mode.
3. **Never mix untrusted content and private data.** If an agent processes user-submitted content, don't give it access to private channels in the same context.
4. **Deploy an MCP Gateway** with centralized auth, logging, and policy enforcement for production systems.
5. **Use OAuth with expiring tokens** rather than static bot tokens. Rotate regularly.
6. **Monitor tool invocations.** Log every MCP tool call with the requesting user, tool name, and parameters.
7. **Review for prompt injection.** Content from chat messages is untrusted input — treat it accordingly in your agent architecture.

For more on MCP security, see our guides on [MCP server security](/guides/mcp-server-security/) and [MCP attack vectors and defense](/guides/mcp-attack-vectors-defense/).

## MCP vs. Native Bot APIs

MCP doesn't replace native Slack and Teams integrations — it complements them. Understanding when to use each matters.

### When MCP Wins

- **Multi-tool orchestration:** Agent combines Slack + GitHub + Jira + database tools in one workflow through a single protocol
- **LLM-native design:** Tools have machine-readable descriptions that LLMs understand natively
- **Standardized discovery:** Agents find available tools at runtime via `tools/list`
- **Framework ecosystem:** Works with CrewAI, LangChain, Claude SDK, and other [agent frameworks](/guides/mcp-agent-framework-integrations/)

### When Native APIs Win

- **Full API coverage:** 200+ Slack methods vs. ~10% via MCP
- **Real-time events:** Native event subscriptions (Socket Mode, Events API, Graph webhooks) — MCP is request/response only
- **Rich UI:** Full Block Kit (Slack) and Adaptive Cards (Teams) support with interactive elements
- **Deterministic behavior:** Traditional code paths vs. LLM-decided tool selection
- **No LLM costs:** No per-request inference overhead

### The Hybrid Approach (Recommended)

Most production systems combine both:

- **Native bot** for event listening, rich UI rendering, and interactive components
- **MCP** for AI-driven reasoning, tool use, and cross-platform orchestration
- The bot receives events natively, then invokes an LLM with MCP tools for complex tasks

This gives you real-time responsiveness from native APIs and intelligent tool orchestration from MCP.

## Framework Support

How major agent frameworks handle Slack and Teams MCP integration:

| Framework | MCP Support Level | Notes |
|-----------|------------------|-------|
| CrewAI | Native, first-class | Agents declare MCP servers inline; framework handles lifecycle |
| LangChain / LangGraph | Supported | Requires more manual wiring; wraps MCP tools as LangChain tools |
| Claude SDK | First-class | Auto-configures for Slack MCP; OAuth flow built in |
| Composio | Managed connectors | Pre-built Slack/Teams MCP with managed OAuth lifecycle |
| Microsoft 365 Agents Toolkit | Official Teams MCP | Native support for the M365 ecosystem |
| BeeAI Framework | Guide available | Provides MCP Slackbot integration patterns |

The general pattern across frameworks: connect to MCP server → discover tools via `tools/list` → expose to LLM as callable functions → LLM selects and invokes during reasoning → framework handles protocol mechanics.

For a broader framework comparison, see our [agent framework integrations guide](/guides/mcp-agent-framework-integrations/) and [agent SDK comparison](/guides/mcp-agent-sdks-2026/).

## Gotchas and Limitations

### Formatting Is Harder Than It Looks

LLMs generate standard markdown. Slack uses `mrkdwn`, a non-standard variant where `*bold*` works but `**bold**` doesn't. Teams uses Adaptive Cards where markdown only works in `TextBlock` fields. Both platforms silently accept invalid formatting and return 200 OK — your agent thinks it posted a beautifully formatted message, but users see raw markup.

### Rate Limits Hit Fast with AI Agents

AI agents making multiple tool calls per request exhaust rate limits quickly. Slack's tier system and Teams' per-tenant throttling (10,000 requests per 10 seconds per app) apply identically whether the call comes through MCP or the direct API. Implement backoff and batching.

### Message Size Limits

Slack caps messages at 40,000 characters. Teams caps at 28 KB (including Adaptive Card JSON). Agents generating long summaries need chunking strategies.

### Threading Models Differ

Slack threads are identified by `thread_ts` with flat replies. Teams reply chains are nested under channel messages, and 1:1 chats have different threading from channel conversations. A cross-platform agent needs platform-specific thread handling.

### File Handling Varies

The official Slack MCP server handles files through canvases. Most community servers have limited file support. The floriscornel Teams server supports large file uploads (>4 MB via resumable sessions), but the InditexTech server has no file support at all.

### Silent Failures Are Common

Both Slack and Teams APIs may return success (200 OK) while silently dropping invalid content — formatting, attachments, or interactive elements that don't conform to platform requirements. Agents must verify outcomes beyond HTTP status codes.

## Getting Started

### Slack (Quickest Path)

If you're using Claude.ai, Claude Code, Cursor, or Perplexity, Slack's official MCP server works out of the box — install the Slack plugin and authenticate via OAuth. No custom code needed.

For custom agents, register a Slack app, configure the required OAuth scopes (start with `search:read.public` and `channels:history` for read-only access), and point your MCP client at `https://mcp.slack.com/mcp`.

### Teams (Quickest Path)

Install the floriscornel/teams-mcp server via npx:

```
npx @floriscornel/teams-mcp@latest authenticate
```

This walks through the Azure AD OAuth flow. For read-only access, add `--read-only`. For production, use Microsoft's Agent Connectors to register your MCP server in the M365 app manifest.

### Building a Chat Bot with MCP

The Pattern 2 architecture (bot as MCP client) is the most common starting point for team-wide assistants:

1. **Create a Slack/Teams bot** using Bolt (Slack) or the Teams SDK
2. **Listen for events** via Socket Mode (Slack) or Graph webhooks (Teams)
3. **Connect MCP servers** in your bot process — Slack MCP for chat operations, plus any other tools (GitHub, Jira, databases)
4. **Route events to your LLM** with the MCP tools available for reasoning
5. **Post responses** back to the originating thread

Start with read-only access and add write permissions only as needed.

## What's Next

The MCP + workplace chat ecosystem is moving fast:

- **Slack's RTS API** will likely expand, making permission-aware search the default rather than the exception
- **Microsoft's Agent Connectors** are in public preview — expect GA with expanded capabilities
- **MCP Gateway products** are emerging to solve multi-server auth, observability, and policy enforcement
- **Rich formatting support** in MCP servers remains weak — expect improvements as agents become common chat participants

The hybrid pattern — native bot for events and UI, MCP for AI reasoning — is the architecture that will define workplace AI agents in 2026 and beyond. The key is starting with read-only access, understanding the security model, and adding capabilities incrementally.

For related reading, see our guides on [what is MCP](/guides/what-is-mcp/), [MCP server security](/guides/mcp-server-security/), [MCP attack vectors and defense](/guides/mcp-attack-vectors-defense/), [building MCP clients](/guides/building-mcp-clients/), [MCP notifications](/guides/mcp-notifications-explained/), [MCP agent framework integrations](/guides/mcp-agent-framework-integrations/), and [Salesforce's Slack AI Overhaul](/guides/salesforce-slack-mcp-ai-platform/) — how Salesforce is turning Slackbot into an MCP client for 750K+ workspaces.

