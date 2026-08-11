---
title: "What Is MCP? A Developer's Guide to the Model Context Protocol"
date: 2026-03-22T19:00:00+09:00
description: "MCP (Model Context Protocol) lets AI models connect to external tools through a standard interface. Here's what developers need to know."
content_type: "Guide"
card_description: "MCP lets AI models connect to external tools through a standard protocol. Here's what you need to know to start using it."
last_refreshed: 2026-04-05
sources_audited: 2026-08-11
---

MCP stands for Model Context Protocol. It's an open standard that lets AI models connect to external tools and data sources through a consistent interface. If you've used function calling or tool use with an LLM, MCP is the next step: a standardized way to package, distribute, and connect those tools.

In December 2025, Anthropic donated MCP to the [Agentic AI Foundation](https://aaif.io/) (AAIF) under the Linux Foundation, co-founded by Anthropic, Block, and OpenAI. Platinum members include [Anthropic, AWS, Block, Bloomberg, Cloudflare, Google, Microsoft, and OpenAI](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation). With [close to half a billion monthly SDK downloads](https://blog.modelcontextprotocol.io/posts/2026-07-28/) (the TypeScript and Python SDKs have each crossed 1 billion total downloads) and [official SDKs in ten languages](https://modelcontextprotocol.io/docs/sdk), plus first-class client support across ChatGPT, Claude, Gemini, Copilot, and more, MCP has gone from experiment to cross-industry standard in under two years.

Here's what you need to know.

## The Problem MCP Solves

Every AI tool integration used to be bespoke. Want Claude to read files? Build a custom integration. Want GPT to query a database? Write another one. Want either of them to work with GitHub? Two more.

This doesn't scale. Every combination of AI model + external tool required its own glue code. MCP fixes this by defining a standard protocol. A tool built as an MCP server works with any MCP-compatible client — Claude Desktop, VS Code with Copilot, custom agent frameworks, or anything else that speaks MCP.

**One server, many clients. One client, many servers.** That's the value proposition.

## How It Works (in 60 Seconds)

```
┌──────────────┐     MCP Protocol     ┌──────────────┐
│  MCP Client  │ ◄──────────────────► │  MCP Server  │
│ (Claude, VS  │    JSON-RPC over     │ (filesystem,  │
│  Code, etc.) │  stdio or Streamable │  GitHub, DB)  │
│              │        HTTP          │              │
└──────────────┘                      └──────────────┘
```

1. **MCP Server** — A program that exposes tools, resources, or prompts. It might give access to a filesystem, a database, a web API, or anything else.
2. **MCP Client** — The AI application (like Claude Desktop) that connects to servers and makes their tools available to the model.
3. **The Protocol** — JSON-RPC messages over stdio (local servers) or Streamable HTTP (remote servers). The client discovers what tools the server offers, then calls them as needed.

When you add an MCP server to a client like Claude Desktop:
1. The client starts the server process (or connects to a remote server via Streamable HTTP)
2. The server announces its capabilities (what tools it has)
3. When the AI model decides it needs a tool, the client calls the server
4. The server executes the tool and returns results
5. The model incorporates the results into its response

### Transports: Local vs. Remote

MCP supports two transport types:

- **stdio** — For local servers. The client launches the server as a subprocess and communicates via standard input/output. Simple, fast, no network required.
- **Streamable HTTP** — For remote servers. The server runs as an HTTP service that any client can connect to. Replaced the earlier HTTP+SSE transport, which [the spec deprecated starting in revision 2025-03-26](https://blog.fka.dev/blog/2025-06-06-why-mcp-deprecated-sse-and-go-with-streamable-http/) and [still lists as deprecated — not yet removed — under the current 2026-07-28 spec](https://modelcontextprotocol.io/specification/versioning), which keeps deprecated features in place for at least twelve months before they're eligible for removal. The [2026-07-28 revision made the protocol core stateless](https://blog.modelcontextprotocol.io/posts/2026-07-28/), enabling horizontal scaling behind ordinary load balancers. Supports streaming responses, multiple concurrent clients, and server-to-client notifications.

## The Three Things a Server Can Expose

### 1. Tools

Functions the AI can call. "Read this file," "run this SQL query," "create this GitHub issue." Tools are the most common capability.

```json
{
  "name": "read_file",
  "description": "Read the contents of a file",
  "inputSchema": {
    "type": "object",
    "properties": {
      "path": { "type": "string" }
    },
    "required": ["path"]
  }
}
```

### 2. Resources

Data the AI can read (but not execute). Think of these as read-only data sources — a file's contents, a database schema, a configuration. Resources are identified by URIs.

### 3. Prompts

Pre-built prompt templates that the server provides. Less common but useful for servers that want to suggest specific interaction patterns.

## Setting Up Your First MCP Server

The fastest way to try MCP is with Claude Desktop (other clients like VS Code, Cursor, and Windsurf also work — see the clients section below).

**Step 1:** Open your Claude Desktop config file.
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

**Step 2:** Add a server. Here's the filesystem server as an example:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/path/to/allowed/directory"
      ]
    }
  }
}
```

**Step 3:** Restart Claude Desktop. You should see a hammer icon indicating MCP tools are available.

**Step 4:** Ask Claude to do something with files: "List the files in my projects directory" or "Read the contents of package.json."

That's it. You now have an AI agent with file system access.

## Where to Find MCP Servers

The ecosystem is growing fast:
- **Official MCP Registry** — The canonical source, now governed by the Agentic AI Foundation
- **PulseMCP** — The largest community directory, with [22,000+ curated servers](https://www.pulsemcp.com/servers) (and growing daily)
- **npm / PyPI** — Many servers are published as packages (`@modelcontextprotocol/server-*` on npm)
- **GitHub** — Search for "mcp-server" to find community-built options

Not all servers are equal. Some are well-maintained reference implementations, others are weekend projects that haven't been updated in months. This is one reason ChatForest exists — to help you figure out which ones are actually worth installing.

## MCP Clients

MCP is client-agnostic — a server built once works with any compliant client. Since AAIF launched, adoption has expanded well beyond Anthropic's ecosystem. Major clients include (see the [official client directory](https://modelcontextprotocol.io/clients) for the full, ongoing list):

- **Claude Desktop** — Anthropic's desktop app, the original MCP client
- **Claude Code** — Anthropic's CLI coding agent with full MCP support
- **ChatGPT Desktop** — [OpenAI has built MCP into the Responses API, the Agents SDK, and ChatGPT's connectors/developer-mode tooling](https://developers.openai.com/api/docs/guides/tools-connectors-mcp), including [full MCP connectors rolling out to ChatGPT Business, Enterprise, and Edu plans](https://help.openai.com/en/articles/12584461-developer-mode-apps-and-full-mcp-connectors-in-chatgpt-beta)
- **Google Gemini** — [Google DeepMind added native MCP support to the Gemini API and Managed Agents](https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api/)
- **VS Code** — GitHub Copilot supports MCP servers natively
- **Visual Studio 2026** — [Azure MCP Server tools built in out of the box](https://devblogs.microsoft.com/visualstudio/azure-mcp-server-now-built-in-with-visual-studio-2026-a-new-era-for-agentic-workflows/)
- **Cursor** — Built-in MCP support, no extension needed
- **Windsurf** — MCP integration in the AI code editor
- **Zed** — Native MCP support in the editor
- **Cline** — Open-source VS Code extension with MCP support
- **Continue.dev** — Open-source AI coding assistant with MCP support
- **Replit** — [Cloud IDE with an MCP server for building and managing Replit apps](https://docs.replit.com/platforms/mcp-server)

With [PulseMCP tracking 600+ MCP clients](https://www.pulsemcp.com/clients), the ecosystem is broad and growing. If you build an MCP server, it works everywhere — that's a key advantage over proprietary plugin systems.

## Building Your Own MCP Server

If you can write a function, you can build an MCP server. [Official SDKs now cover ten languages](https://modelcontextprotocol.io/docs/sdk):
- **TypeScript:** [`@modelcontextprotocol/client`/`server` v2.0 beta](https://github.com/modelcontextprotocol/typescript-sdk/releases), released July 2026 with support for the 2026-07-28 spec (the earlier `@modelcontextprotocol/sdk` v1 line still ships for 2025-era servers)
- **Python:** [`mcp` v2.0.0](https://pypi.org/project/mcp/), a major rework released July 28, 2026 for the current spec
- **Java:** Official SDK, [maintained in collaboration with the Spring team](https://github.com/modelcontextprotocol/java-sdk)
- **Kotlin:** [Multiplatform SDK (JVM, Native, JS, Wasm), maintained in collaboration with JetBrains](https://github.com/modelcontextprotocol/kotlin-sdk)
- **Go:** [`go-sdk` v1.7.0](https://github.com/modelcontextprotocol/go-sdk/releases), maintained in collaboration with Google, reached stable with full 2026-07-28 spec support in July 2026
- **C#:** [Official SDK maintained in collaboration with Microsoft](https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csharp-sdk/), now at v2.0 implementing the 2026-07-28 revision
- **Swift:** [Official SDK](https://github.com/modelcontextprotocol/swift-sdk)
- **Rust:** Official SDK
- **Ruby:** Official SDK
- **PHP:** Official SDK

A minimal Python MCP server:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-server")

@mcp.tool()
def greet(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()
```

That's a working MCP server. It exposes one tool (`greet`) that any MCP client can call. The SDK handles all the JSON-RPC communication, capability negotiation, and transport.

We'll cover building MCP servers in depth in future articles.

## What MCP Means for Developers

If you build software, MCP matters for two reasons:

1. **As a user:** MCP servers extend what AI tools can do for you. File access, database queries, API calls, deployment tools — the ecosystem grows with every new server.
2. **As a builder:** Wrapping your API or tool as an MCP server makes it accessible to every AI agent in the ecosystem. It's a distribution channel for your tool's capabilities.

The MCP ecosystem has matured rapidly. The [current spec (2026-07-28) is stable](https://modelcontextprotocol.io/specification/versioning), [official SDKs cover ten languages](https://modelcontextprotocol.io/docs/sdk), and governance now sits under the Agentic AI Foundation with backing from every major AI lab. The [2026 roadmap is organized around four priority areas](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) — transport scalability, agent-to-agent communication, governance maturation, and enterprise readiness (audit trails, SSO-integrated auth via proposals like DPoP and Workload Identity Federation, gateway behavior — these auth proposals are still in review, not yet shipped protocol). SDK maintainers previewed a V2 path at [MCP Dev Summit North America 2026](https://events.linuxfoundation.org/mcp-dev-summit-north-america/) (April 2-3, 2026, NYC — the second Dev Summit, following the inaugural one in San Francisco in May 2025), and [V2 SDKs for TypeScript, Python, Go, and C# shipped July 28, 2026](https://blog.modelcontextprotocol.io/posts/2026-07-28/) alongside conformance testing that's now a formal requirement for spec changes.

With [close to half a billion monthly SDK downloads](https://blog.modelcontextprotocol.io/posts/2026-07-28/) and first-class support from Claude, ChatGPT, Gemini, Copilot, and dozens of other clients, MCP has moved past early-adopter into mainstream developer infrastructure.

## Related Guides

- [The Agentic AI Foundation: What Happens When Competitors Co-Govern an Open Standard](/guides/agentic-ai-foundation-mcp-governance/) — AAIF governance structure, 146 members, founding projects (MCP, AGENTS.md, goose)
