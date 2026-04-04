---
title: "MCP and Anthropic Claude: How Claude Desktop, Claude Code, the Claude API, and the Agent SDK Use the Model Context Protocol"
date: 2026-03-29T14:00:00+09:00
description: "A comprehensive guide to Anthropic's MCP ecosystem — covering Claude Desktop's local servers and MCPB extensions, Claude Code's CLI-native MCP integration, the Claude API's MCP"
content_type: "Guide"
card_description: "Anthropic created MCP and has woven it into every Claude product — Desktop, Code, the API, and the web interface. This guide covers every integration point with configuration examples, SDK details, and practical guidance for choosing the right approach."
last_refreshed: 2026-03-29
---

Anthropic didn't just adopt MCP — they created it. The Model Context Protocol started as an internal Anthropic project, was [open-sourced in November 2024](https://www.anthropic.com/news/model-context-protocol), and has since grown into an industry standard with 97 million monthly SDK downloads and adoption by every major AI platform. In December 2025, Anthropic [donated MCP](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) to the Agentic AI Foundation under the Linux Foundation, establishing open governance while remaining a platinum member and core maintainer.

Because MCP originated at Anthropic, Claude products have the deepest and most mature MCP integration of any AI platform. Claude Desktop was the first consumer AI product to support MCP servers. Claude Code treats MCP as a first-class extension mechanism. The Claude API now offers a native MCP Connector that handles server discovery and tool invocation without requiring developers to build their own MCP client. And Claude.ai's web interface exposes MCP through the Connectors feature, bringing tool integration to the browser.

This guide covers every MCP integration surface across Anthropic's products with configuration examples, SDK details, and architectural guidance. Our analysis draws on [Anthropic's official documentation](https://docs.anthropic.com), the [MCP specification](https://modelcontextprotocol.io), SDK source code, community reports, and published research — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## Anthropic's MCP Timeline

Understanding Anthropic's MCP journey helps explain why their integration is the most mature in the industry:

- **November 2024** — Anthropic [open-sources the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol). Claude Desktop ships as the first consumer MCP client with stdio transport support.
- **Early 2025** — The MCP ecosystem grows rapidly. Third-party MCP servers proliferate. Cursor, Windsurf, and other AI coding tools adopt MCP.
- **March 2025** — [OpenAI adopts MCP](https://techcrunch.com/2025/03/26/openai-adopts-rival-anthropics-standard-for-connecting-ai-models-to-data/), validating it as an industry standard. [Google](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services) and Microsoft follow shortly after.
- **June 2025** — Anthropic launches [Desktop Extensions](https://www.anthropic.com/engineering/desktop-extensions) (originally `.dxt`, later renamed `.mcpb`) for one-click MCP server installation in Claude Desktop.
- **September 2025** — The [official MCP Registry launches in preview](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/). MCPB format replaces DXT (legacy files continue to work).
- **November 2025** — The MCP specification's [third major revision](https://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/) lands, introducing Client ID Metadata Documents and mandatory PKCE S256 for [OAuth 2.1](https://modelcontextprotocol.io/specification/2025-11-25/changelog).
- **December 2025** — Anthropic [donates MCP to the Agentic AI Foundation](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) (AAIF) under the Linux Foundation. OpenAI and Block are [co-founders](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/).
- **January 2026** — Claude.ai web interface [launches pre-built Connectors](https://www.anthropic.com/news/integrations) with 50+ integrations. [Interactive apps](https://techcrunch.com/2026/01/26/anthropic-launches-interactive-claude-apps-including-slack-and-other-workplace-tools/) arrive for Slack, Figma, and more.
- **February 2026** — Claude API [MCP Connector enters public beta](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector) (`mcp-client-2025-11-20`). Free and paid plan users get Connectors access.
- **March 2026** — TypeScript SDK reaches [v1.28.0](https://github.com/modelcontextprotocol/typescript-sdk/releases) with 36,000+ dependent packages. The [2026 MCP Roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) is published.

## The Integration Surfaces

Anthropic's MCP support spans six distinct surfaces, each designed for different workflows:

| Integration Point | Use Case | Transport | MCP Capabilities | Plans |
|---|---|---|---|---|
| **Claude Desktop** | Interactive tool use with local servers | stdio, Streamable HTTP, SSE | Tools, resources, prompts | All plans |
| **Claude Code** | CLI-native coding agent with MCP tools | stdio, Streamable HTTP, SSE | Tools, resources, prompts | All plans |
| **Claude API (MCP Connector)** | Backend API calls with remote MCP servers | Streamable HTTP, SSE (hosted) | Tools only | API access |
| **Claude.ai Web** | Browser-based tool use via Connectors | Streamable HTTP (remote) | Tools | Free (1), paid (unlimited) |
| **Claude Agent SDK** | Building autonomous agents programmatically | stdio, Streamable HTTP | Tools, resources, prompts | API access |
| **MCP SDKs** | Building MCP servers and clients | All transports | Full specification | Open source |

The key architectural distinction: **Claude Desktop** and **Claude Code** can run MCP servers as local child processes (stdio transport), giving them access to your filesystem, databases, and local tools. **Claude.ai web** and the **API MCP Connector** only support remote servers — Anthropic's infrastructure connects to your publicly-exposed MCP server on your behalf. This has significant implications for what's possible and what security considerations apply.

## Claude Desktop: The Original MCP Client

Claude Desktop was the first consumer product to support MCP, and it remains the most full-featured MCP client for interactive use.

### Configuration

MCP servers are configured in `claude_desktop_config.json`:

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Access this file via Claude menu → Settings → Developer tab → "Edit Config."

A typical configuration:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/you/Documents"],
      "env": {}
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_..."
      }
    },
    "remote-server": {
      "url": "https://mcp.example.com/sse",
      "headers": {
        "Authorization": "Bearer token123"
      }
    }
  }
}
```

Each server entry supports:
- **`command` + `args`** — for local stdio servers launched as child processes
- **`url`** — for remote Streamable HTTP or SSE servers
- **`env`** — environment variables passed to local server processes
- **`headers`** — HTTP headers for remote server authentication

Claude Desktop includes a built-in Node.js runtime, so Node-based MCP servers work without a separate Node.js installation.

### Supported Transports

- **stdio** (primary for local servers) — servers run as child processes, communicating over stdin/stdout. This is the most common configuration.
- **Streamable HTTP** (for remote servers) — the recommended remote transport, supporting bidirectional communication.
- **SSE** (legacy remote) — supported but deprecated in favor of Streamable HTTP.

### Approval Flows

All MCP tool actions require explicit user approval. When Claude wants to use a tool, you see an approval popup showing the tool name and parameters. Options include:

- **Allow once** — approve this specific invocation
- **Always approve** — permanently approve this tool (per server)

MCP permissions are granular — each tool must be approved individually; there are no wildcards.

### MCPB Desktop Extensions

For users who don't want to edit JSON config files, Anthropic introduced Desktop Extensions — originally as `.dxt` files (June 2025), later renamed to `.mcpb` (MCP Bundle) in September 2025. Legacy `.dxt` files continue to work.

**Installation is one-click:** download an `.mcpb` file from [desktopextensions.com](https://www.desktopextensions.com/) → double-click → click "Install."

An `.mcpb` file is a ZIP archive containing a `manifest.json` that declares the server's configuration:

```json
{
  "mcpb_version": "1.0",
  "name": "my-mcp-server",
  "version": "1.0.0",
  "description": "Does useful things",
  "author": { "name": "Developer Name" },
  "type": "node",
  "entry_point": "dist/index.js",
  "mcp_config": {
    "transport": "stdio"
  },
  "user_config": {
    "api_key": {
      "type": "string",
      "description": "Your API key",
      "required": true,
      "sensitive": true
    }
  }
}
```

Key MCPB features:
- **Credential security** — fields marked `"sensitive": true` are stored in the OS keychain, not in plaintext config files
- **Template literals** — `${user_config.api_key}` in environment variables are replaced at runtime from keychain values
- **Packaging toolchain** — `npx @anthropic-ai/mcpb init` generates the manifest interactively; `npx @anthropic-ai/mcpb pack` validates and creates the archive
- **Enterprise support** — Group Policy/MDM for pre-installation, publisher blocklists, and private extension directories
- **Three runtime types** — `node`, `python`, and `binary`

### Server Management UI

The "+" button at the bottom of the chat input → "Connectors" shows connected MCP servers and their available tools. The Developer settings panel displays connection status, server logs, and error details for debugging.

On Team and Enterprise plans, workspace owners can manage which desktop extensions are available to team members.

## Claude Code: CLI-Native MCP Integration

[Claude Code](https://docs.anthropic.com/en/docs/claude-code) is Anthropic's command-line AI coding agent. It treats MCP as a first-class extension mechanism — MCP tools appear alongside Claude Code's built-in tools (file editing, terminal access, web search) and can be used in the same agentic workflow.

### Configuration Methods

Claude Code offers three ways to configure MCP servers:

**1. CLI commands** (quickest):
```bash
# Add a local stdio server
claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem /home/user/docs

# Add a remote HTTP server
claude mcp add --transport http my-api https://mcp.example.com/api

# List configured servers
claude mcp list

# Remove a server
claude mcp remove filesystem
```

**2. Direct file editing** (more control):
Edit configuration files directly for complex setups with environment variables and headers.

**3. Project `.mcp.json`** (team sharing):
Place an `.mcp.json` file in the project root. This is checked into version control so the whole team gets the same MCP servers:

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["-y", "mcp-server-postgres", "postgresql://localhost/mydb"]
    },
    "jira": {
      "type": "http",
      "url": "https://mcp.atlassian.com/jira",
      "headers": {
        "Authorization": "Bearer ${JIRA_TOKEN}"
      }
    }
  }
}
```

### Configuration Scopes

Claude Code supports three configuration scopes with clear precedence:

| Scope | Location | Shared? | Precedence |
|---|---|---|---|
| **Local** (default) | `~/.claude.json` (per-project path) | No — private to you | Highest |
| **Project** | `.mcp.json` in project root | Yes — checked into git | Middle |
| **User** | `~/.claude.json` (global) | No — private to you | Lowest |

Local scope takes precedence over project scope, which takes precedence over user scope. If a server is configured both locally and via a Claude.ai connector, the local config wins.

### Environment Variable Expansion

`.mcp.json` supports environment variable expansion with `${VAR}` and `${VAR:-default}` syntax in `command`, `args`, `env`, `url`, and `headers` fields. This keeps secrets out of version control while allowing team-shared configurations.

### Supported Transports

- **stdio** — for local server processes: `claude mcp add --transport stdio <name> -- <command> [args...]`
- **Streamable HTTP** (recommended for remote): `claude mcp add --transport http <name> <url>`
- **SSE** (deprecated): `claude mcp add --transport sse <name> <url>`

### How MCP Tools Work in Claude Code

During a coding session, MCP tools integrate seamlessly with Claude Code's built-in capabilities:

- **Tool discovery** — Claude Code discovers available tools from connected MCP servers at session start. It supports `list_changed` notifications for live capability refresh when servers add or remove tools.
- **Unified tool use** — MCP tools appear alongside built-in tools. Claude Code can use an MCP tool to query a database, then use its built-in file editor to update code based on the results.
- **Permission controls** — Allow, Ask, and Deny rules control which MCP tools Claude Code can use without manual approval. Configurable in settings files.
- **Push messages** — Servers declaring `claude/channel` capability can push messages into sessions (CI results, alerts, deployment status).
- **Output limits** — MCP tool output has a warning threshold at 10,000 tokens, configurable via `MAX_MCP_OUTPUT_TOKENS`.
- **Timeouts** — Startup timeout is configurable via `MCP_TIMEOUT` environment variable.
- **OAuth** — Remote servers requiring authentication are handled via the `/mcp` slash command.
- **Status** — The `/mcp` command within a session shows server connection status.

### CLAUDE.md as Complementary Context

[CLAUDE.md files](/guides/writing-effective-claude-md-files/) provide project-specific instructions and context to Claude Code. They complement MCP by giving Claude knowledge about the project (coding conventions, architecture decisions, deployment procedures) while MCP provides tool access (database queries, API calls, file operations). Together, they let you configure a coding agent that knows your project and can act on it.

## Claude API: The MCP Connector

The [Claude API MCP Connector](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector) lets developers connect to remote MCP servers directly from the Messages API without implementing a separate MCP client. It entered public beta in February 2026.

### How It Works

The API request includes two MCP-specific components:

1. **`mcp_servers`** — an array of server connection details (URL, name, authentication)
2. **`tools`** — includes `mcp_toolset` entries that configure which tools to enable from each server

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    mcp_servers=[
        {
            "type": "url",
            "url": "https://mcp.example.com/api",
            "name": "my-server",
            "authorization_token": "Bearer token123"
        }
    ],
    tools=[
        {
            "type": "mcp_toolset",
            "server_label": "my-server",
            "tool_configuration": {
                "enabled": True
            }
        }
    ],
    messages=[
        {"role": "user", "content": "List all open issues"}
    ],
    extra_headers={
        "anthropic-beta": "mcp-client-2025-11-20"
    }
)
```

### Key Capabilities

- **Multiple servers** — connect to several MCP servers in a single API request
- **Flexible tool filtering** — enable all tools, allowlist specific tools, or denylist unwanted tools per server
- **Deferred loading** — `defer_loading` option for use with Tool Search, so tool descriptions aren't sent to the model upfront
- **OAuth authentication** — Bearer token support for authenticated servers
- **Cache control** — cache control headers supported on toolsets for performance

### Response Types

The MCP Connector introduces two new content block types in API responses:
- **`mcp_tool_use`** — when the model calls an MCP tool
- **`mcp_tool_result`** — the result returned by the MCP server

### Limitations

- **Tools only** — MCP resources, prompts, and sampling are not supported through the Connector
- **Remote servers only** — must be publicly exposed via HTTPS (Streamable HTTP or SSE). Local stdio servers cannot connect directly
- **Not available on Bedrock/Vertex** — only supported on the direct Anthropic API
- **Not eligible for Zero Data Retention** (ZDR)
- **Validation** — every server in `mcp_servers` must be referenced by exactly one toolset, and each server can only be referenced by one toolset

### SDK MCP Helpers

For developers managing their own MCP client connections instead of using the hosted Connector, the SDKs provide helper functions:

**TypeScript SDK:**
```typescript
import { mcpTools, mcpMessages, mcpResourceToContent } from "@anthropic-ai/sdk";

// Convert MCP tools to Claude API tools
const tools = mcpTools(mcpToolList, mcpClient);

// Convert MCP prompt messages to API format
const messages = mcpMessages(mcpPromptMessages);

// Convert MCP resource to content block
const content = mcpResourceToContent(resource);
```

**Python SDK (v0.84.0+):**
```python
from anthropic.mcp import mcp_tool, async_mcp_tool, mcp_message

# Convert MCP Tool + ClientSession into a BetaFunctionTool
tool = mcp_tool(mcp_tool_definition, mcp_session)

# Async variant
tool = await async_mcp_tool(mcp_tool_definition, mcp_session)

# Convert MCP prompt messages to API format
messages = mcp_message(prompt_message)
```

These helpers bridge any MCP server to the Claude API without the hosted Connector, giving developers full control over the MCP client lifecycle.

## Claude.ai Web: Connectors

MCP is available in Claude's web interface through the [Connectors](https://support.anthropic.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) feature, bringing tool integration to the browser.

### Availability

- **Free plan** — one custom connector
- **Pro, Max, Team, Enterprise** — unlimited connectors
- Feature remains in beta

### Pre-Built Connectors

The Connectors Directory features **50+ curated integrations** spanning productivity, communication, design, engineering, finance, and healthcare. As of January 2026, some connectors support interactive apps — rendering live interfaces for Slack, Figma, Canva, Asana, and more directly inside Claude conversations.

### Custom Connectors

Paid plan users can add custom connectors:
1. Go to Settings → Connectors → "Add custom connector"
2. Enter a name and MCP server URL
3. Configure OAuth credentials in Advanced settings if needed

### Team and Enterprise

Workspace owners add connectors at the organization level via Organization settings → Connectors. Individual team members then authenticate through their personal Settings → Connectors page.

### Per-Conversation Activation

Connectors are enabled per-conversation using the "+" button in the chat interface → "Connectors" to toggle specific integrations on or off. This gives you control over which tools are available in each conversation.

### Security

Custom connectors connect to arbitrary, unverified services. Anthropic warns users to only connect to trusted servers. Pre-built connectors in the directory undergo Anthropic's review process.

## The Official MCP SDKs

Anthropic maintains the two official MCP SDKs that implement the full specification. These are the foundation on which MCP servers and clients are built.

### TypeScript SDK (`@modelcontextprotocol/sdk`)

- **Latest version:** 1.28.0 (March 25, 2026)
- **Install:** `npm install @modelcontextprotocol/sdk`
- **GitHub:** [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)
- **Dependents:** 36,000+ packages on npm

Key features:
- Full MCP specification implementation
- Server and client classes
- All transports (stdio, SSE, Streamable HTTP)
- Zod schema integration for type-safe tool definitions
- OAuth authentication support
- Conformance testing suite

### Python SDK (`mcp` package)

- **Latest version:** 1.26.0 (January 24, 2026)
- **Install:** `pip install mcp` or `uv add "mcp[cli]"`
- **GitHub:** [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)

Key features:
- Full MCP specification implementation
- **FastMCP** high-level API built into the SDK
- All transports (stdio, SSE, Streamable HTTP)
- Async-first design

### FastMCP

[FastMCP](https://gofastmcp.com) is a high-level Python framework for building MCP servers quickly. The core FastMCP API is built into the official Python SDK, while the standalone FastMCP package (maintained by Prefect/Jlowin) extends it further:

- **FastMCP 3.0** (January 2026) added component versioning, granular authorization, OpenTelemetry instrumentation, multiple provider types (FileSystem, Skills, OpenAPI), hot reload, and custom providers
- Currently at version **3.1.1**
- Claims to power approximately 70% of MCP servers across all languages

### Combined SDK Downloads

Anthropic reported **97 million monthly SDK downloads** across the Python and TypeScript SDKs as of December 2025, with 4,750% growth since launch.

## Claude Agent SDK

The [Claude Agent SDK](https://docs.anthropic.com/en/docs/agent-sdk/overview) gives developers programmatic access to the same tools, agent loop, and context management that power Claude Code. It's available in both Python and TypeScript.

- **Python:** `claude-agent-sdk-python` (v0.1.48 on PyPI)
- **TypeScript:** `claude-agent-sdk-typescript` (v0.2.71 on npm)

### Native MCP Integration

The Agent SDK supports MCP natively:
- **In-process MCP servers** — run an MCP server within the same process as your agent
- **External MCP servers** — connect to remote or local MCP servers using any supported transport
- **Full MCP capabilities** — tools, resources, and prompts are all accessible

This means you can build autonomous agents that leverage the full MCP ecosystem — connecting to databases, APIs, file systems, and any other MCP-enabled service — with the same agentic capabilities that Claude Code uses internally.

## Anthropic's Role in MCP Governance

### The Agentic AI Foundation

On December 9, 2025, Anthropic donated MCP to the **Agentic AI Foundation (AAIF)** under the Linux Foundation. This was a deliberate move toward open governance — ensuring that no single company controls the protocol.

**Co-founders:** Anthropic, Block, and OpenAI

**Platinum members:** Amazon Web Services, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, and OpenAI

**100+ total members** across the foundation

Three projects were contributed at launch:
1. **Model Context Protocol (MCP)** — by Anthropic
2. **Goose** — by Block (open-source AI agent)
3. **AGENTS.md** — by OpenAI

### Governance Model

The AAIF Governing Board handles strategic decisions, budget, and member recruitment. Individual projects like MCP maintain **full technical autonomy** — maintainers continue to control the specification, review contributions, and make technical decisions independently. This is the standard Linux Foundation model (similar to how Kubernetes operates under the CNCF).

### MCP Dev Summit

The [first MCP Dev Summit North America](/guides/mcp-dev-summit-2026-guide/) took place **April 2–3, 2026** in New York City, featuring 95+ sessions from Anthropic, OpenAI, Microsoft, Docker, Bloomberg, and major enterprise adopters. Key topics included SDK V2 roadmap, authentication standardization, and cross-platform interoperability.

## The 2026 MCP Roadmap

Anthropic published the [2026 MCP Roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) on March 9, 2026, outlining four priority areas:

### 1. Transport Evolution and Scalability
- Evolving Streamable HTTP for **stateless horizontal scaling** (no sticky sessions or distributed stores)
- Session creation, resumption, and migration for transparent server restarts and scale-out
- A cookie-like mechanism being explored to decouple session state from transport
- **Server Cards** — a `.well-known` metadata format for capability discovery without connecting
- No new official transports this cycle

### 2. Agent Communication
- Refining the **Tasks primitive** (SEP-1686) for managing long-running operations
- Retry semantics for transient failures
- Expiry policies for result retention

### 3. Governance Maturation
- Documented contributor ladder
- Delegation model allowing Working Groups to accept domain-specific SEPs
- Reducing Core Maintainer bottlenecks

### 4. Enterprise Readiness
- Audit trails, SSO-integrated authentication, gateway behavior, configuration portability
- Prioritizing extensions over core spec changes
- Security SEPs: DPoP (SEP-1932) and Workload Identity Federation (SEP-1933)

**Timeline:** The goal is to finalize SEPs in Q1 2026 for inclusion in the next spec release, tentatively slated for **June 2026**.

## Choosing the Right Integration Point

### For Individual Developers

**Start with Claude Desktop** if you want to try MCP servers interactively. Install servers from [desktopextensions.com](https://www.desktopextensions.com/) with one click, or configure custom servers in `claude_desktop_config.json`. This is the lowest-friction way to experience MCP.

**Use Claude Code** if you're a developer who works in the terminal. Claude Code's MCP integration lets you extend your AI coding agent with project-specific tools — database access, API clients, deployment tools — through a simple `.mcp.json` file that the whole team can share.

### For Application Developers

**Use the Claude API MCP Connector** if you want the simplest path to connecting Claude to remote MCP servers in production. Anthropic manages the MCP client connection — you just provide the server URL and authentication. The trade-off: tools only (no resources or prompts), and remote servers must be publicly accessible.

**Use the SDK MCP helpers** if you need full control over the MCP client lifecycle, want to connect to local stdio servers, or need MCP capabilities beyond tools (resources, prompts). You manage the MCP connection yourself and bridge it to the Claude API through the helper functions.

**Use the Claude Agent SDK** if you're building autonomous agents that need the same capabilities as Claude Code — agentic loops, tool use, context management — with native MCP support. This is the right choice for production agent systems.

### For MCP Server Builders

**Use the TypeScript SDK** (`@modelcontextprotocol/sdk`) or **Python SDK** (`mcp`) to build MCP servers. For Python, the built-in FastMCP API provides a high-level decorator-based interface for rapid development:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-server")

@mcp.tool()
def search_docs(query: str) -> str:
    """Search documentation for relevant information."""
    # Your implementation here
    return results
```

For distribution, consider [MCPB packaging](/guides/mcp-server-packaging-distribution/) for Claude Desktop users, npm/PyPI for developers, or Docker for enterprise deployments.

## Comparison: Anthropic vs. OpenAI MCP Integration

For developers choosing between platforms or building cross-platform MCP servers, here's how Anthropic's MCP support compares to [OpenAI's](/guides/mcp-openai-integration/):

| Aspect | Anthropic (Claude) | OpenAI |
|---|---|---|
| **MCP history** | Created and open-sourced MCP | Adopted March 2025 |
| **Local server support** | Yes (Desktop + Code via stdio) | Yes (Agents SDK via stdio) |
| **Remote server support** | Yes (all products) | Yes (all products) |
| **API-level MCP** | MCP Connector (public beta) | Responses API (GA) |
| **Consumer MCP** | Claude Desktop, Claude.ai web | ChatGPT Developer Mode |
| **One-click install** | MCPB extensions | N/A |
| **Agent SDK** | Claude Agent SDK (native MCP) | OpenAI Agents SDK (native MCP) |
| **MCP capabilities** | Tools, resources, prompts (Desktop/Code) | Tools, resources, prompts (Agents SDK) |
| **API MCP capabilities** | Tools only (Connector) | Tools only (Responses API) |
| **Interactive UI** | Connectors with apps | Apps SDK with iframe |
| **Governance role** | Creator, AAIF platinum member | AAIF co-founder, platinum member |

Both platforms now offer comprehensive MCP support. Anthropic's advantage is depth and maturity — they've been iterating on MCP integration since November 2024. OpenAI's advantage is breadth — their Agents SDK and Responses API reached general availability faster.

## Security Considerations

MCP integration across Claude products raises several security considerations:

### Local Servers (Desktop + Code)
- **Process isolation** — stdio servers run as child processes with the same permissions as the parent application. A compromised server has access to everything the user does.
- **Config file security** — `claude_desktop_config.json` and `.mcp.json` may contain API keys and tokens. MCPB's keychain integration addresses this for Desktop Extensions, but manual configurations still risk plaintext secrets.
- **Supply chain** — installing MCP servers via npm/pip carries the same supply chain risks as any package installation. Prefer servers from verified publishers and the official registry.

### Remote Servers (API Connector + Web Connectors)
- **Data exposure** — remote MCP servers receive the context of your conversation. Only connect to servers you trust.
- **Authentication** — use OAuth 2.1 or Bearer tokens for remote server authentication. See our [MCP Authentication & OAuth 2.1 guide](/guides/mcp-authentication-oauth/) for details.
- **Network security** — remote servers must be exposed over HTTPS. Ensure TLS is properly configured.

### Team Environments
- **Project `.mcp.json`** — servers in project config files are shared with the team. Claude Code prompts for approval before using project-scoped servers, preventing supply chain attacks through version control.
- **Enterprise controls** — Team and Enterprise plans support managed connector policies, publisher blocklists, and private extension directories.

For a deeper dive into MCP security, see our guides on [MCP server security](/guides/mcp-server-security/) and [MCP attack vectors and defense](/guides/mcp-attack-vectors-defense/).

## What's Next

MCP is Anthropic's bet on an open standard for AI tool integration, and they're backing it with deep integration across every product. The June 2026 spec release — with stateless HTTP, Server Cards, and enhanced agent communication — will shape the next phase. The Agentic AI Foundation's governance ensures that MCP's evolution reflects the needs of the broader ecosystem, not just one company.

For developers building on Claude, MCP is already the primary extension mechanism. Whether you're connecting Claude Desktop to a local database, giving Claude Code access to your deployment pipeline, or building production agents with the Claude API, MCP provides the standard interface. The question isn't whether to adopt MCP — it's which integration point fits your workflow.

**Related guides:**
- [What Is MCP?](/guides/what-is-mcp/) — Protocol fundamentals
- [MCP and OpenAI](/guides/mcp-openai-integration/) — OpenAI's MCP integration for comparison
- [Writing Effective CLAUDE.md Files](/guides/writing-effective-claude-md-files/) — Complementary context for Claude Code
- [MCP Server Packaging & Distribution](/guides/mcp-server-packaging-distribution/) — Publishing servers for Claude users
- [MCP Authentication & OAuth 2.1](/guides/mcp-authentication-oauth/) — Security for remote MCP servers
- [MCP Server Security](/guides/mcp-server-security/) — Hardening MCP deployments
- [MCP Clients Comparison](/guides/mcp-clients-comparison/) — How Claude compares to other MCP clients
- [Building MCP Clients](/guides/building-mcp-clients/) — Building your own MCP client
- [MCP Server Frameworks & SDKs](/guides/mcp-server-frameworks-sdks/) — Choosing the right SDK
