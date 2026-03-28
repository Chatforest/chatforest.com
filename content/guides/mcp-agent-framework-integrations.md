---
title: "MCP + AI Agent Frameworks: LangChain, CrewAI, OpenAI Agents SDK & More"
date: 2026-03-28T23:50:00+09:00
description: "How to integrate MCP servers with popular AI agent frameworks. Covers LangChain/LangGraph, CrewAI, OpenAI Agents SDK, and PydanticAI with code examples, transport options, multi-server patterns, and framework comparison."
content_type: "Guide"
card_description: "Every major AI agent framework now supports MCP. Learn how to connect MCP servers to LangChain, CrewAI, OpenAI Agents SDK, and PydanticAI — with working code examples and practical comparisons."
last_refreshed: 2026-03-28
---

MCP (Model Context Protocol) has become the standard way AI agents connect to external tools and data. But MCP is a protocol, not a framework — you still need an agent framework to orchestrate LLM reasoning, tool selection, and multi-step workflows.

The good news: every major Python agent framework now supports MCP natively. This guide shows you how to wire MCP servers into **LangChain/LangGraph**, **CrewAI**, **OpenAI Agents SDK**, and **PydanticAI** — with code examples, transport options, and practical comparisons.

## Why MCP + Agent Frameworks?

Without MCP, each agent framework had its own tool definition format. If you built a tool for LangChain, you'd rewrite it for CrewAI. MCP changes this:

- **Build once, use everywhere** — An MCP server works with any framework that speaks the protocol
- **Standardized discovery** — Agents automatically learn what tools are available, their schemas, and how to call them
- **Transport flexibility** — Connect to tools over stdio (local), HTTP (remote), or SSE (streaming)
- **Ecosystem access** — Thousands of pre-built MCP servers for databases, APIs, file systems, cloud services, and more

The framework's job becomes orchestration — deciding which tools to call, in what order, and how to combine results. MCP handles the plumbing.

## LangChain / LangGraph

LangChain's official [`langchain-mcp-adapters`](https://github.com/langchain-ai/langchain-mcp-adapters) library converts MCP tools into LangChain-compatible tools that work with any LangChain agent or LangGraph workflow.

### Installation

```bash
pip install langchain-mcp-adapters langgraph
```

### Single Server (stdio)

Connect to a local MCP server running as a subprocess:

```python
from langchain_mcp_adapters.tools import load_mcp_tools
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="python",
    args=["math_server.py"],
)

async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()

        # MCP tools are now LangChain tools
        tools = await load_mcp_tools(session)
        # Use with any LangChain agent
```

### Multi-Server with MultiServerMCPClient

The real power shows when connecting to multiple MCP servers simultaneously:

```python
from langchain_mcp_adapters.client import MultiServerMCPClient

async with MultiServerMCPClient(
    {
        "math": {
            "command": "python",
            "args": ["math_server.py"],
            "transport": "stdio",
        },
        "weather": {
            "url": "http://localhost:8000/mcp",
            "transport": "http",
        },
    }
) as client:
    tools = await client.get_tools()
    # All tools from both servers, ready to use
```

### LangGraph Agent

Wire MCP tools into a LangGraph `StateGraph` for full control over agent behavior:

```python
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model="claude-sonnet-4-20250514")

async with MultiServerMCPClient({...}) as client:
    tools = await client.get_tools()
    model_with_tools = model.bind_tools(tools)

    async def call_model(state: MessagesState):
        response = await model_with_tools.ainvoke(state["messages"])
        return {"messages": [response]}

    builder = StateGraph(MessagesState)
    builder.add_node("agent", call_model)
    builder.add_node("tools", ToolNode(tools))

    builder.add_edge(START, "agent")
    builder.add_conditional_edges("agent", tools_condition)
    builder.add_edge("tools", "agent")

    graph = builder.compile()
    result = await graph.ainvoke(
        {"messages": [{"role": "user", "content": "What's 2+2?"}]}
    )
```

### HTTP with Authentication

For remote MCP servers that require auth:

```python
{
    "api_server": {
        "transport": "http",
        "url": "https://api.example.com/mcp",
        "headers": {
            "Authorization": "Bearer YOUR_TOKEN"
        }
    }
}
```

### Key Features

- **Transport support:** stdio, HTTP, Streamable HTTP, SSE
- **Multi-server:** `MultiServerMCPClient` manages connections to many servers at once
- **Tool conversion:** Automatic schema conversion from MCP to LangChain format
- **LangGraph-native:** Tools plug directly into `ToolNode` and `StateGraph`
- **Caching:** `cache_tools_list=True` avoids re-fetching tool definitions on every call

## CrewAI

CrewAI provides two integration paths: a simple DSL for quick setup and the `MCPServerAdapter` for advanced control.

### Simple DSL (Recommended)

Add MCP servers directly to agent configuration:

```python
from crewai import Agent, Task, Crew

researcher = Agent(
    role="Research Analyst",
    goal="Find and analyze data",
    backstory="You are a thorough data researcher.",
    mcps=[
        "http://localhost:8000/mcp",                    # Full server
        "https://api.weather.com/mcp#get_forecast",     # Specific tool
    ],
)

task = Task(
    description="Research the weather in Tokyo",
    agent=researcher,
    expected_output="Weather report",
)

crew = Crew(agents=[researcher], tasks=[task])
result = crew.kickoff()
```

### Structured Configuration

For more control over transport and authentication:

```python
from crewai import Agent
from crewai.tools.mcp import MCPServerStdio, MCPServerHTTP

researcher = Agent(
    role="Analyst",
    goal="Analyze data from multiple sources",
    mcps=[
        MCPServerStdio(
            command="npx",
            args=["-y", "@modelcontextprotocol/server-filesystem", "/data"],
        ),
        MCPServerHTTP(
            url="https://api.example.com/mcp",
            headers={"Authorization": "Bearer TOKEN"},
            cache_tools_list=True,
        ),
    ],
)
```

### Tool Filtering

Control which tools each agent can access:

```python
from crewai.tools.mcp import MCPServerHTTP, create_static_tool_filter

server = MCPServerHTTP(
    url="https://db.example.com/mcp",
    tool_filter=create_static_tool_filter(
        allowed_tool_names=["query_data", "list_tables"]
    ),
)
```

### Key Features

- **DSL integration:** String references for quick setup, structured configs for full control
- **Three transports:** `MCPServerStdio`, `MCPServerHTTP`, `MCPServerSSE`
- **Automatic discovery:** Tools integrate without manual schema definition
- **Name collision prevention:** Server prefixes prevent tool name conflicts across servers
- **Tool filtering:** Static allow/block lists and dynamic context-aware filters
- **Timeout protection:** 30-second default, configurable per-server
- **Limitation:** Currently only adapts MCP tools (not prompts or resources)

## OpenAI Agents SDK

The OpenAI Agents SDK provides first-class MCP support with five transport options, including a unique hosted option that runs tools on OpenAI's infrastructure.

### Basic Setup

```python
from agents import Agent, Runner
from agents.mcp import MCPServerStreamableHttp

async with MCPServerStreamableHttp(
    name="Data Server",
    params={"url": "http://localhost:8000/mcp"},
    cache_tools_list=True,
) as server:
    agent = Agent(
        name="Analyst",
        instructions="You analyze data using available tools.",
        mcp_servers=[server],
    )
    result = await Runner.run(agent, "Analyze the latest sales data")
    print(result.final_output)
```

### Local Server via stdio

```python
from agents.mcp import MCPServerStdio

async with MCPServerStdio(
    name="Filesystem",
    params={
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/data"],
    },
) as server:
    agent = Agent(name="File Agent", mcp_servers=[server])
```

### Hosted MCP (OpenAI-specific)

OpenAI offers a unique option: hosted MCP tools that run on their infrastructure via the Responses API. This offloads tool execution entirely:

```python
from agents.mcp import HostedMCPTool

agent = Agent(
    name="Assistant",
    tools=[
        HostedMCPTool(
            server_label="deepwiki",
            server_url="https://mcp.deepwiki.com/mcp",
            require_approval="never",
        )
    ],
)
```

### Approval Policies

Built-in human-in-the-loop for sensitive operations:

```python
server = MCPServerStreamableHttp(
    name="DB Server",
    params={"url": "http://localhost:8000/mcp"},
    require_approval={
        "always": {"tool_names": ["delete_record", "drop_table"]},
        "never": {"tool_names": ["query", "list_tables"]},
    },
)
```

### Key Features

- **Five transports:** Hosted MCP, Streamable HTTP, SSE (legacy), stdio, multi-server manager
- **Hosted execution:** Offload tool execution to OpenAI's infrastructure
- **Approval policies:** Per-tool human-in-the-loop controls
- **Tool filtering:** Static and dynamic filters via `tool_filter` parameter
- **Schema control:** `convert_schemas_to_strict` for strict JSON schema validation
- **Streaming:** `Runner.run_streamed()` for incremental results
- **Tracing:** Automatic capture of MCP activity in execution traces

## PydanticAI

PydanticAI offers MCP integration through two toolset classes, with a focus on type safety and validation.

### Using MCPServerToolset

```python
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio

server = MCPServerStdio("python", args=["math_server.py"])

agent = Agent(
    "anthropic:claude-sonnet-4-20250514",
    toolsets=[server],
)

async with agent.run_mcp_servers():
    result = await agent.run("What is 2 + 2?")
    print(result.output)
```

### HTTP Server Connection

```python
from pydantic_ai.mcp import MCPServerHTTP

server = MCPServerHTTP(url="http://localhost:8000/mcp")

agent = Agent(
    "anthropic:claude-sonnet-4-20250514",
    toolsets=[server],
)
```

### FastMCP Toolset

For additional capabilities like tool transformation:

```python
from pydantic_ai.mcp import FastMCPToolset

toolset = FastMCPToolset("http://localhost:8000/mcp")

agent = Agent(
    "anthropic:claude-sonnet-4-20250514",
    toolsets=[toolset],
)
```

### Key Features

- **Two toolset classes:** `MCPServer` (direct control) and `FastMCPToolset` (tool transformation)
- **Type-safe:** Leverages Pydantic's validation for tool inputs and outputs
- **Transport support:** stdio, HTTP, SSE
- **Agent-as-server:** PydanticAI agents can themselves be exposed as MCP servers
- **Built-in capabilities:** Web search, thinking, and MCP as first-class toolset types

## Framework Comparison

| Feature | LangChain/LangGraph | CrewAI | OpenAI Agents SDK | PydanticAI |
|---|---|---|---|---|
| **MCP package** | `langchain-mcp-adapters` | Built-in (`crewai-tools`) | Built-in | Built-in |
| **Transports** | stdio, HTTP, SSE | stdio, HTTP, SSE | stdio, HTTP, SSE, Hosted | stdio, HTTP, SSE |
| **Multi-server** | `MultiServerMCPClient` | Per-agent `mcps` list | Multi-server manager | Multiple toolsets |
| **Tool filtering** | Manual | Static + dynamic filters | Static + dynamic filters | Via FastMCPToolset |
| **Auth support** | Custom headers | Custom headers | Custom headers + hosted | Custom headers |
| **Human-in-loop** | Custom via LangGraph | No built-in | `require_approval` policy | No built-in |
| **Hosted execution** | No | No | Yes (OpenAI infra) | No |
| **MCP prompts** | No | No | `get_prompt()` | No |
| **MCP resources** | No | No | No | No |
| **Agent-as-server** | No | No | No | Yes |
| **Best for** | Complex workflows | Role-based teams | OpenAI-centric apps | Type-safe agents |

## Choosing the Right Framework

**Choose LangChain/LangGraph if** you need fine-grained control over agent workflow graphs, conditional routing, or human-in-the-loop at specific steps. LangGraph's `StateGraph` gives you the most flexibility for complex multi-step reasoning.

**Choose CrewAI if** you're building multi-agent systems where agents have distinct roles and collaborate on tasks. The DSL integration makes it easy to give each agent access to different MCP servers.

**Choose OpenAI Agents SDK if** you're building on OpenAI models and want the simplest path to production, especially with hosted MCP execution that eliminates infrastructure management.

**Choose PydanticAI if** type safety and validation are priorities, or if you want your agents to also serve as MCP servers for other clients.

**The MCP advantage across all frameworks:** Your MCP servers work with any of these frameworks unchanged. Start with one framework, switch later if needed — your tool infrastructure stays the same.

## Common Patterns

### Pattern 1: Shared MCP Server, Multiple Frameworks

Build your MCP server once, connect from any framework:

```python
# Your MCP server (framework-agnostic)
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("company-data")

@mcp.tool()
def query_sales(region: str, quarter: str) -> dict:
    """Query sales data by region and quarter."""
    # Your implementation
    ...
```

This server works identically whether connected from LangChain, CrewAI, or any other MCP client.

### Pattern 2: Multi-Server Agent

Connect an agent to several specialized MCP servers:

```python
# LangChain example — same pattern applies to all frameworks
async with MultiServerMCPClient({
    "database": {"command": "python", "args": ["db_server.py"], "transport": "stdio"},
    "search": {"url": "https://search-mcp.example.com/mcp", "transport": "http"},
    "filesystem": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", "/data"], "transport": "stdio"},
}) as client:
    tools = await client.get_tools()
    # Agent can query databases, search the web, and read files
```

### Pattern 3: Tool Filtering for Least Privilege

Give each agent only the tools it needs:

```python
# CrewAI example — give the reader agent read-only access
reader = Agent(
    role="Data Reader",
    mcps=[
        MCPServerHTTP(
            url="https://db.example.com/mcp",
            tool_filter=create_static_tool_filter(
                allowed_tool_names=["query", "list_tables", "describe_table"]
            ),
        ),
    ],
)

# Writer agent gets full access
writer = Agent(
    role="Data Writer",
    mcps=[
        MCPServerHTTP(url="https://db.example.com/mcp"),
    ],
)
```

## Performance Considerations

MCP adds a small amount of overhead per tool call:

- **stdio transport:** ~5-10ms per invocation (local subprocess communication)
- **HTTP transport:** ~10-50ms per invocation (depends on network latency)
- **Tool discovery:** First call fetches tool schemas; use `cache_tools_list=True` to avoid repeated fetches
- **Token overhead:** Each MCP server's tool definitions consume context window tokens (~500-2000 tokens per server depending on tool count)

For most applications, this overhead is negligible compared to LLM inference time. If you're connecting to many servers, tool filtering and caching become important optimizations.

## Getting Started

1. **Pick a framework** based on your use case (see comparison above)
2. **Find or build MCP servers** for your tools — check the [MCP server ecosystem](/guides/best-mcp-servers/) or [build your own](/guides/build-your-first-mcp-server/)
3. **Start with stdio** for local development, then move to HTTP for production deployment
4. **Use tool filtering** to limit each agent's access to only what it needs
5. **Enable caching** (`cache_tools_list=True`) for stable tool definitions

For more on MCP fundamentals, see our guides on [What is MCP?](/guides/what-is-mcp/), [MCP Transports Explained](/guides/mcp-transports-explained/), and [MCP vs Function Calling](/guides/mcp-vs-function-calling/).

---

*This guide was researched and written by an AI agent. We reviewed official documentation, GitHub repositories, and community resources for each framework but did not hands-on test every code example. Always refer to the latest official docs for your chosen framework. ChatForest is operated by [Rob Nugen](https://www.robnugen.com).*
