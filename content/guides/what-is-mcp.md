---
title: "What Is MCP? A Developer's Guide to the Model Context Protocol"
date: 2026-03-14T01:06:39+09:00
description: "MCP (Model Context Protocol) lets AI models connect to external tools through a standard interface. Here's what developers need to know."
content_type: "Guide"
card_description: "MCP lets AI models connect to external tools through a standard protocol. Here's what you need to know to start using it."
---

MCP stands for Model Context Protocol. It's an open standard that lets AI models connect to external tools and data sources through a consistent interface. If you've used function calling or tool use with an LLM, MCP is the next step: a standardized way to package, distribute, and connect those tools.

Here's what you need to know.

## The Problem MCP Solves

Every AI tool integration used to be bespoke. Want Claude to read files? Build a custom integration. Want GPT to query a database? Write another one. Want either of them to work with GitHub? Two more.

This doesn't scale. Every combination of AI model + external tool required its own glue code. MCP fixes this by defining a standard protocol. A tool built as an MCP server works with any MCP-compatible client — Claude Desktop, VS Code with Copilot, custom agent frameworks, or anything else that speaks MCP.

**One server, many clients. One client, many servers.** That's the value proposition.

## How It Works (in 60 Seconds)

```
┌──────────────┐     MCP Protocol     ┌──────────────┐
│  MCP Client  │ ◄──────────────────► │  MCP Server  │
│ (Claude, etc)│    JSON-RPC over     │ (filesystem,  │
│              │    stdio or HTTP     │  GitHub, DB)  │
└──────────────┘                      └──────────────┘
```

1. **MCP Server** — A program that exposes tools, resources, or prompts. It might give access to a filesystem, a database, a web API, or anything else.
2. **MCP Client** — The AI application (like Claude Desktop) that connects to servers and makes their tools available to the model.
3. **The Protocol** — JSON-RPC messages over stdio (local servers) or HTTP with SSE (remote servers). The client discovers what tools the server offers, then calls them as needed.

When you add an MCP server to Claude Desktop:
1. Claude Desktop starts the server process
2. The server announces its capabilities (what tools it has)
3. When the AI model decides it needs a tool, Claude Desktop calls the server
4. The server executes the tool and returns results
5. The model incorporates the results into its response

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

The fastest way to try MCP is with Claude Desktop.

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
- **PulseMCP** — The largest community directory with 9,000+ servers listed
- **npm / PyPI** — Many servers are published as packages (`@modelcontextprotocol/server-*` on npm)
- **GitHub** — Search for "mcp-server" to find community-built options

Not all servers are equal. Some are well-maintained reference implementations, others are weekend projects that haven't been updated in months. This is one reason ChatForest exists — to help you figure out which ones are actually worth installing.

## Building Your Own MCP Server

If you can write a function, you can build an MCP server. The official SDKs handle the protocol layer:
- **TypeScript:** `@modelcontextprotocol/sdk`
- **Python:** `mcp`

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

The MCP ecosystem is early. The protocol is stable, the tooling is solid, and the adoption curve is steep. Now is a good time to start building with it.
