# What Is MCP? A Developer's Guide to the Model Context Protocol

> MCP (Model Context Protocol) lets AI models connect to external tools through a standard interface. Here's what developers need to know.


MCP stands for Model Context Protocol. It's an open standard that lets AI models connect to external tools and data sources through a consistent interface. If you've used function calling or tool use with an LLM, MCP is the next step: a standardized way to package, distribute, and connect those tools.

In December 2025, Anthropic donated MCP to the [Agentic AI Foundation](https://aaif.io/) (AAIF) under the Linux Foundation, co-founded by Anthropic, Block, and OpenAI. Platinum members now include AWS, Bloomberg, Cloudflare, Google, and Microsoft. With 97 million monthly SDK downloads, official SDKs in eight languages, and first-class client support across ChatGPT, Claude, Gemini, Copilot, and more, MCP has gone from experiment to cross-industry standard in just over a year.

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
- **Streamable HTTP** — For remote servers. The server runs as an HTTP service that any client can connect to. Replaced the earlier HTTP+SSE transport (deprecated in spec version 2025-03-26, sunset April 1, 2026). Fully stateless, enabling horizontal scaling behind load balancers. Supports streaming responses, multiple concurrent clients, and server-to-client notifications.

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
- **PulseMCP** — The largest community directory with 11,170+ curated servers (and growing daily)
- **npm / PyPI** — Many servers are published as packages (`@modelcontextprotocol/server-*` on npm)
- **GitHub** — Search for "mcp-server" to find community-built options

Not all servers are equal. Some are well-maintained reference implementations, others are weekend projects that haven't been updated in months. This is one reason ChatForest exists — to help you figure out which ones are actually worth installing.

## MCP Clients

MCP is client-agnostic — a server built once works with any compliant client. Since AAIF launched, adoption has expanded well beyond Anthropic's ecosystem. Major clients include:

- **Claude Desktop** — Anthropic's desktop app, the original MCP client
- **Claude Code** — Anthropic's CLI coding agent with full MCP support
- **ChatGPT Desktop** — OpenAI adopted MCP across ChatGPT desktop, the Agents SDK, and the Responses API
- **Google Gemini** — Google DeepMind confirmed MCP support in Gemini models
- **VS Code** — GitHub Copilot supports MCP servers natively
- **Visual Studio 2026** — Azure MCP Server tools built-in out of the box
- **Cursor** — Built-in MCP support, no extension needed
- **Windsurf** — MCP integration in the AI code editor
- **Zed** — Native MCP support in the editor
- **Cline** — Open-source VS Code extension with MCP support
- **Continue.dev** — Open-source AI coding assistant with MCP support
- **Replit** — Cloud IDE with MCP server support

With PulseMCP tracking 546+ MCP clients, the ecosystem is broad and growing. If you build an MCP server, it works everywhere — that's a key advantage over proprietary plugin systems.

## Building Your Own MCP Server

If you can write a function, you can build an MCP server. Official SDKs now cover eight languages:
- **TypeScript:** `@modelcontextprotocol/sdk` (v1.27+, V2 in development)
- **Python:** `mcp` (v1.26+, V2 path announced at MCP Dev Summit)
- **Java:** Official SDK maintained with Spring
- **Kotlin:** Multiplatform SDK (JVM, Native, JS, Wasm), maintained with JetBrains
- **Go:** Official SDK maintained with Google (stable release expected August 2026)
- **C#:** Official SDK maintained with Microsoft
- **Swift:** Official SDK maintained with Apple
- **Rust:** Official SDK

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

The MCP ecosystem has matured rapidly. The current spec (November 2025) is stable, official SDKs cover eight languages, and governance now sits under the Agentic AI Foundation with backing from every major AI lab. The 2026 roadmap is organized around four priority areas — transport scalability, agent-to-agent communication, governance maturation, and enterprise readiness (audit trails, SSO-integrated auth via DPoP and Workload Identity Federation, gateway behavior). A V2 path for SDKs was announced at the inaugural MCP Dev Summit (April 2-3, 2026, NYC), with conformance testing across all SDKs now a formal initiative.

With 97 million monthly SDK downloads and first-class support from Claude, ChatGPT, Gemini, Copilot, and dozens of other clients, MCP has moved past early-adopter into mainstream developer infrastructure.

## Related Guides

- [The Agentic AI Foundation: What Happens When Competitors Co-Govern an Open Standard](/guides/agentic-ai-foundation-mcp-governance/) — AAIF governance structure, 146 members, founding projects (MCP, AGENTS.md, goose)

