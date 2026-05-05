---
title: "mcp-use — The Open-Source MCP Client Library That Connects Any LLM to Any MCP Server"
date: 2026-05-05T25:00:00+09:00
description: "mcp-use reviewed: an MIT-licensed Python and TypeScript framework that lets any LangChain-compatible LLM connect to any MCP server in ~6 lines of code. 9.9K stars. Rating: 4.0/5."
og_description: "mcp-use (9.9K stars, MIT, Python + TypeScript): connect any LangChain-compatible LLM — OpenAI, Claude, Gemini, Groq — to any MCP server in ~6 lines of Python. MCPAgent orchestrates tool-calling loops; MCPClient manages multi-server configs; LangChainAdapter converts MCP schemas to callable tools. Three transports: stdio, SSE, WebSocket. Optional E2B sandbox isolation. Started as Pietro Zullo's pure Python client (March 2025), now a fullstack framework under Manufact. Rating: 4.0/5."
content_type: "Review"
card_description: "mcp-use (9.9K stars, v1.7.0, MIT, Python + TypeScript) is the open-source MCP client library that makes programmatic LLM-to-MCP connections simple. Where servers like Playwright MCP or GitHub MCP expose tools to AI assistants, mcp-use is the plumbing on the client side that lets you build those connections yourself — outside of Claude Desktop or any managed client. Six lines of Python: import MCPAgent and MCPClient, point to an MCP server config, attach an LLM, call run(). The MCPAgent handles the ReAct loop; the MCPClient manages server lifecycle; the LangChainAdapter converts MCP tool schemas into callable LangChain tools. Supports OpenAI (GPT-4o), Anthropic (Claude 3.5+), Google (Gemini), Groq, and any other LangChain-compatible model with function-calling. Three transports: stdio (local subprocess), HTTP/SSE (remote), WebSocket. Multi-server configs with optional vector-based tool discovery. E2B sandbox integration for isolated cloud execution. Tool restrictions at the agent level (block file_system, shell, network). Grew from Pietro Zullo's personal Python library (March 2025, pietrozullo/mcp-use) to a fullstack framework now under the mcp-use/Manufact organization, with TypeScript tooling, React-based MCP Apps, and a production deployment platform. The Python pip library remains the most immediately useful piece for developers building MCP-powered agents programmatically. Part of our **Developer Tools** category. Rating: 4.0/5."
last_refreshed: 2026-05-05
categories: ["/categories/developer-tools/"]
---

Every MCP server review on this site covers the server side of the equation: tools exposed, capabilities offered, deployment options. mcp-use sits on the other side — it is what you use to **consume** those MCP servers programmatically, from your own code, with your own choice of LLM.

At **9.9K stars** with an MIT license and active development through May 2026, mcp-use is the most widely adopted open-source MCP client library in the Python ecosystem. Its core proposition is simple: connect any LangChain-compatible LLM to any MCP server, with the glue code reduced to about six lines. Part of our **[Developer Tools category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Repo** | [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use) |
| **Stars** | ~9,900 |
| **Forks** | 1,267 |
| **License** | MIT |
| **Language** | TypeScript (Python fully supported) |
| **Python version** | 1.7.0 (March 17, 2026) |
| **Author** | Pietro Zullo (@pietrozullo) / Manufact |
| **Created** | March 28, 2025 |
| **Open Issues** | 72 |
| **Install** | `pip install mcp-use` |
| **Python** | 3.11+ |

---

## What It Does

When you configure Claude Desktop or Claude Code to use an MCP server, the client side — session management, transport negotiation, tool-call routing, retry logic — is handled for you. mcp-use exposes that client layer as a Python library, so you can build the same kind of MCP-connected agent in your own code.

The three-component model:

**MCPClient** manages connections to one or more MCP servers. You initialize it with a config dict or JSON file that describes each server — which transport to use, what command to spawn (stdio) or what URL to connect to (SSE, WebSocket). The client handles session lifecycle, capability negotiation, and keeps connections alive across multiple agent turns.

**LangChainAdapter** converts the tool schemas that MCP servers expose (JSON Schema format) into `BaseTool` objects that LangChain's LLM integrations can call. This is the translation layer — MCP speaks JSON-RPC, LangChain speaks tool-use APIs, the adapter bridges them without you having to handle either protocol directly.

**MCPAgent** is the orchestrator. It wraps an LLM and an MCPClient, then runs a ReAct-style loop: query arrives → LLM decides which tool to call → MCPClient executes the call → result goes back to LLM → loop continues until the task is done or `max_steps` is reached.

The result: a working MCP-connected agent in roughly this structure:

```python
from mcp_use import MCPAgent, MCPClient
from langchain_anthropic import ChatAnthropic

client = MCPClient.from_dict({
    "mcpServers": {
        "playwright": {
            "command": "npx",
            "args": ["@playwright/mcp@latest"]
        }
    }
})

agent = MCPAgent(
    llm=ChatAnthropic(model="claude-opus-4-6"),
    client=client,
    max_steps=15
)

result = await agent.run("Find the current price of NVIDIA stock")
print(result)
```

That is the entire MCP client stack — transport management, session negotiation, tool-call serialization, result parsing — handled by the library.

---

## Supported LLMs

Any LangChain-compatible model with function-calling capability:

| Provider | Package |
|----------|---------|
| Anthropic (Claude 3.5+, Claude 4.x) | `langchain-anthropic` |
| OpenAI (GPT-4o, o1, o3) | `langchain-openai` |
| Google (Gemini 1.5+, 2.0) | `langchain-google-genai` |
| Groq | `langchain-groq` |
| Meta Llama (via providers) | LangChain integrations |

The critical constraint: the model must support function calling / tool use. Models that generate only text completions cannot drive the tool-call loop.

---

## Key Features

### Multi-server Configurations

One MCPClient can manage connections to multiple MCP servers simultaneously. The agent dispatches tool calls to the right server based on tool names. With `use_server_manager=True` (requires `pip install "mcp-use[search]"`), the library uses vector embeddings (`fastembed`) to automatically select the best server for each query — useful when you have a large collection of servers and want the LLM to focus on semantics rather than tool catalog management.

### Three Transport Types

| Transport | When to use |
|-----------|-------------|
| **stdio** | Local MCP servers spawned as subprocesses — Claude Desktop's default model |
| **HTTP/SSE** | Remote servers via Server-Sent Events; persistent connections |
| **WebSocket** | Real-time bidirectional remote connections |

Config format signals the transport: `command`/`args` → stdio; `url` → SSE; `ws_url` → WebSocket.

### E2B Sandbox Integration

`pip install "mcp-use[e2b]"` adds a `SandboxConnector` that runs MCP servers inside isolated E2B cloud environments rather than as local subprocesses. This matters for security-sensitive deployments: the MCP server's process has no access to your local filesystem, shell, or network. Requires an E2B API key (paid service). The Code Execution Mode extension lets the LLM write and execute Python in E2B while retaining access to MCP tools — combining code generation with tool use in an isolated runtime.

### Tool Restrictions

```python
agent = MCPAgent(
    llm=llm,
    client=client,
    disallowed_tools=["file_system", "network", "shell"]
)
```

Block specific tools or tool categories at the agent level, independent of what the MCP server exposes. Useful for building agents that can use read-only tools from a server that also exposes write operations.

### Streaming Output

```python
async for chunk in agent.stream("Summarize the last 10 issues in this repo"):
    print(chunk)
```

Step-by-step visibility into the ReAct loop — see each tool call and result as it happens rather than waiting for the full run to complete.

---

## From Python Client to Fullstack Framework

mcp-use started as `pietrozullo/mcp-use` — Pietro Zullo's personal Python library, published to PyPI in late March 2025. By the time it hit 9K+ stars, it had been transferred to the `mcp-use` organization and was growing into something larger.

The current `mcp-use/mcp-use` repo now has two distinct halves:

**Python (pip install mcp-use)** — the MCPAgent/MCPClient library described above. This is what most Python developers care about. Version 1.7.0, stable, actively maintained.

**TypeScript (@mcp-use/cli, @mcp-use/inspector, mcp-use npm)** — a server-building toolkit with hot-reload development, a web-based MCP inspector at `inspector.mcp-use.com`, 13 application templates (Chart Builder, Diagram Builder, Maps Explorer, etc.), and React-based MCP Apps that render interactive UIs inside conversations. This is the direction the organization is building toward, with production deployment via [Manufact](https://manufact.com) MCP Cloud.

For the purposes of this review, the Python library is the primary subject — it is the piece that directly complements the MCP servers we review on this site.

---

## What mcp-use Is Not

**Not an MCP server framework.** Creating MCP servers in Python is marked "coming soon" — the server tooling is TypeScript-only currently. For Python MCP server development, see [FastMCP](/reviews/mcp-server-frameworks-sdks/) or the [official Python SDK](https://github.com/modelcontextprotocol/python-sdk).

**Not a standalone solution.** mcp-use requires LangChain as a dependency. You are not getting a minimal library — you are bringing in LangChain's full dependency tree. For teams already using LangChain, this is free; for teams that aren't, it's a significant additional dependency.

**Not model-agnostic without LangChain.** The MCPAgent and LangChainAdapter are built on LangChain's tool-calling abstractions. There is no native OpenAI SDK path or Anthropic SDK path — both go through LangChain providers. This is not a blocker (LangChain's Anthropic integration wraps the same Claude APIs), but it is a coupling to be aware of.

---

## Comparison: mcp-use vs. langchain-mcp-adapters

The official [langchain-ai/langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters) project provides the core MCP-to-LangChain translation layer that mcp-use builds on. The difference is orchestration: langchain-mcp-adapters gives you the adapter; mcp-use adds MCPAgent (the ReAct loop), multi-server management, E2B sandbox support, streaming, and tool restrictions on top.

If you need a thin, official adapter and plan to build your own agent loop, langchain-mcp-adapters is the primitive. If you want a working agent framework with batteries included, mcp-use adds the pieces that make it runnable.

---

## Limitations

1. **LangChain coupling** — the full LangChain dependency tree comes with the library.
2. **Python server creation not yet available** — you cannot create MCP servers in Python using this library.
3. **Tool-calling LLMs only** — models without function-calling support will not work; this excludes many smaller or older models.
4. **Resource cleanup required** — use `manage_connector=True` in `run()` or call `agent.close()` to avoid connection leaks.
5. **E2B requires a paid API key** — sandboxed execution is not free; budget accordingly for production deployments.
6. **TypeScript tooling not mirrored in Python** — MCP Apps, the inspector, the CLI with hot reload — these are TypeScript-only features not available to Python library users.

---

## Who Should Use This

**MCP-use is well-suited for:**
- Developers building agents that need to call multiple MCP servers from code rather than from Claude Desktop
- Teams already using LangChain who want to add MCP server connectivity
- Prototyping autonomous agents that mix web search (Playwright, Firecrawl), data sources (databases, APIs), and file operations via MCP
- Projects where you want to choose the LLM independently (Claude, GPT-4o, Gemini) and want a single client library that works with all of them

**Less suited for:**
- Teams that want a minimal library without LangChain dependency overhead
- Projects that need to create MCP servers in Python (use FastMCP instead)
- Production deployments where you want full control of the agent loop (you may want to implement the loop yourself with langchain-mcp-adapters as the primitive)

---

## Verdict

mcp-use is the most practical open-source solution for programmatic MCP client development in Python. Its 9.9K stars and active maintenance reflect genuine usefulness — it solves a real problem (all the glue code between LLM and MCP server) in a well-designed way. The LangChain coupling is the main caveat; whether that's a problem depends entirely on your stack. The TypeScript side of the project is evolving toward a broader framework, but the Python pip library delivers its core promise reliably today.

**Rating: 4.0/5** — 9.9K stars, MIT license, broad LLM support, solid multi-server and transport coverage. One point deducted for LangChain coupling and Python/TypeScript feature parity gap; another half-point for the "coming soon" state of Python server creation.

---

*ChatForest researches MCP servers and tools without hands-on testing. Star counts and version numbers reflect data collected around the publication date and may have changed.*
