---
title: "What Is MCP? A Developer's Guide to the Model Context Protocol"
date: 2026-03-22T19:00:00+09:00
description: "MCP (Model Context Protocol) lets AI models connect to external tools through a standard interface. Here's what developers need to know."
content_type: "Guide"
card_description: "MCP lets AI models connect to external tools through a standard protocol. Here's what you need to know to start using it."
last_refreshed: 2026-03-22
---

MCP stands for Model Context Protocol. It's an open standard that lets AI models connect to external tools and data sources through a consistent interface. If you've used function calling or tool use with an LLM, MCP is the next step: a standardized way to package, distribute, and connect those tools.

With 12,000+ servers listed in directories like PulseMCP and official SDKs in seven languages, MCP has gone from experiment to industry standard in just over a year.

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
- **Streamable HTTP** — For remote servers. The server runs as an HTTP service that any client can connect to. Replaced the earlier HTTP+SSE transport (deprecated May 2025, sunset April 2026). Supports streaming responses, multiple concurrent clients, and server-to-client notifications.

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
- **Official MCP Registry** — The canonical source, backed by Anthropic and GitHub
- **PulseMCP** — The largest community directory with 12,370+ servers listed (and growing daily)
- **npm / PyPI** — Many servers are published as packages (`@modelcontextprotocol/server-*` on npm)
- **GitHub** — Search for "mcp-server" to find community-built options

Not all servers are equal. Some are well-maintained reference implementations, others are weekend projects that haven't been updated in months. This is one reason ChatForest exists — to help you figure out which ones are actually worth installing.

## MCP Clients

MCP is client-agnostic — a server built once works with any compliant client. Major clients include:

- **Claude Desktop** — Anthropic's desktop app, the original MCP client
- **Claude Code** — Anthropic's CLI coding agent with full MCP support
- **VS Code** — GitHub Copilot supports MCP servers via extensions
- **Cursor** — Built-in MCP support, no extension needed
- **Windsurf** — MCP integration in the AI code editor
- **Zed** — Native MCP support in the editor
- **Cline** — Open-source VS Code extension with MCP support
- **Continue.dev** — Open-source AI coding assistant with MCP support
- **Replit** — Cloud IDE with MCP server support

If you build an MCP server, it works everywhere. That's a key advantage over proprietary plugin systems.

## Building Your Own MCP Server

If you can write a function, you can build an MCP server. Official SDKs now cover seven languages:
- **TypeScript:** `@modelcontextprotocol/sdk` (v1.27+)
- **Python:** `mcp` (v1.2+)
- **Java:** Official SDK maintained with Spring
- **Kotlin:** Multiplatform SDK (JVM, Native, JS, Wasm), maintained with JetBrains
- **Go:** Official SDK maintained with Google
- **C#:** Official SDK maintained with Microsoft
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

The MCP ecosystem has matured rapidly. The current spec (November 2025) is stable, official SDKs cover seven languages, and the 2026 roadmap focuses on enterprise readiness (audit trails, SSO-integrated auth, gateway behavior) and agent-to-agent communication. With 12,000+ servers already built, adoption has moved past early-adopter into mainstream developer tooling.
