# MCP + AI Agent Frameworks: LangChain, CrewAI, OpenAI Agents SDK & More

> How to integrate MCP servers with popular AI agent frameworks.


MCP (Model Context Protocol) has become the standard way AI agents connect to external tools and data. But MCP is a protocol, not a framework — you still need an agent framework to orchestrate LLM reasoning, tool selection, and multi-step workflows.

The good news: every major Python agent framework now supports MCP natively. This guide shows you how to wire MCP servers into **LangChain/LangGraph**, **CrewAI**, **OpenAI Agents SDK**, and **PydanticAI** — with code examples, transport options, and practical comparisons.

## Why MCP + Agent Frameworks?

Without MCP, each agent framework had its own tool definition format. If you built a tool for LangChain, you'd rewrite it for CrewAI. MCP changes this:

- **Build once, use everywhere** — An MCP server works with any framework that speaks the protocol
- **Standardized discovery** — Agents automatically learn what tools are available, their schemas, and how to call them
- **Transport flexibility** — Connect to tools over stdio (local), HTTP (remote), or SSE (streaming)
- **Ecosystem access** — Anthropic reported [more than 10,000 active public MCP servers](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) as of its December 2025 ecosystem update, spanning databases, APIs, file systems, cloud services, and more

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

- **Transport support:** stdio, HTTP, Streamable HTTP, SSE ([source](https://github.com/langchain-ai/langchain-mcp-adapters))
- **Multi-server:** `MultiServerMCPClient` manages connections to many servers at once
- **Tool conversion:** Automatic schema conversion from MCP to LangChain format
- **LangGraph-native:** Tools plug directly into `ToolNode` and `StateGraph`
- **Prompts and resources:** `load_mcp_prompt()` and `load_mcp_resources()` expose MCP prompts and resources, not just tools ([API reference](https://reference.langchain.com/python/langchain-mcp-adapters/))

*Correction (2026-08-11 audit): earlier versions of this guide claimed a `cache_tools_list=True` caching option for `langchain-mcp-adapters`. That parameter does not exist in the package's source ([`tools.py`](https://github.com/langchain-ai/langchain-mcp-adapters/blob/main/langchain_mcp_adapters/tools.py), [`client.py`](https://github.com/langchain-ai/langchain-mcp-adapters/blob/main/langchain_mcp_adapters/client.py)) — it was conflated with the similarly-named option in CrewAI and the OpenAI Agents SDK, both of which do support it (see below).*

## CrewAI

CrewAI provides two integration paths, per [CrewAI's MCP documentation](https://docs.crewai.com/en/mcp/overview): the `mcps` field on `Agent` (recommended — takes string references or structured config objects) for quick setup, and the lower-level `MCPServerAdapter` from `crewai-tools` for advanced, manual connection management.

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
from crewai.mcp import MCPServerStdio, MCPServerHTTP

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
from crewai.mcp import MCPServerHTTP, create_static_tool_filter

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
- **Limitation:** Per [CrewAI's docs](https://docs.crewai.com/en/mcp/overview), `MCPServerAdapter` "primarily supports adapting MCP tools" — prompts and resources are not integrated as CrewAI components through that adapter

Source: [CrewAI MCP documentation](https://docs.crewai.com/en/mcp/overview); import paths and defaults verified against the `crewai` 1.15.x package source.

## OpenAI Agents SDK

The OpenAI Agents SDK provides first-class MCP support with five transport options, including a unique hosted option that runs tools on OpenAI's infrastructure ([official MCP docs](https://openai.github.io/openai-agents-python/mcp/)).

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

Source: [OpenAI Agents SDK MCP documentation](https://openai.github.io/openai-agents-python/mcp/).

## PydanticAI

PydanticAI offers MCP integration through a single, unified `MCPToolset` class built on the [FastMCP client](https://gofastmcp.com/clients/), with a focus on type safety and validation.

**Correction (2026-08-11 audit):** earlier versions of this guide described three separate classes — `MCPServerStdio`, `MCPServerHTTP`, and `FastMCPToolset` — and an `agent.run_mcp_servers()` context manager. As of pydantic-ai's v2.0.0b1 release (2026-05-20), all of those were removed in favor of one `MCPToolset` class and a `toolsets=` argument on `Agent`; `run_mcp_servers()` was likewise dropped ([pydantic-ai changelog](https://pydantic.dev/docs/ai/project/changelog/), PRs [#5325](https://github.com/pydantic/pydantic-ai/pull/5325), [#5337](https://github.com/pydantic/pydantic-ai/pull/5337), [#5466](https://github.com/pydantic/pydantic-ai/pull/5466)). The code below reflects the current API ([MCP client docs](https://pydantic.dev/docs/ai/mcp/client/)); the old class names will raise `ImportError` on current releases.

### Installation

```bash
pip install "pydantic-ai-slim[mcp]"
```

### Stdio Server

```python
from fastmcp.client.transports import StdioTransport
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPToolset

toolset = MCPToolset(StdioTransport(command="python", args=["math_server.py"]))

agent = Agent(
    "anthropic:claude-sonnet-4-20250514",
    toolsets=[toolset],
)

async def main():
    result = await agent.run("What is 2 + 2?")
    print(result.output)
```

### HTTP Server Connection

```python
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPToolset

toolset = MCPToolset("http://localhost:8000/mcp")  # Streamable HTTP by default

agent = Agent(
    "anthropic:claude-sonnet-4-20250514",
    toolsets=[toolset],
)
```

### Key Features

- **One toolset class:** `MCPToolset` handles stdio, Streamable HTTP, SSE (deprecated), and in-process FastMCP servers — pass a URL, a `fastmcp.client.transports` object, or a `fastmcp.Client`/`FastMCP` instance directly
- **Type-safe:** Leverages Pydantic's validation for tool inputs and outputs
- **Resources supported:** `list_resources()`, `list_resource_templates()`, and `read_resource(uri)` are built into `MCPToolset` (MCP prompts are not yet supported)
- **Agent-as-server:** PydanticAI agents can themselves be exposed as MCP servers
- **Built-in capabilities:** Web search, thinking, and MCP as first-class toolset types

Source: [PydanticAI MCP client documentation](https://pydantic.dev/docs/ai/mcp/client/) and [changelog](https://pydantic.dev/docs/ai/project/changelog/); current release verified as pydantic-ai 2.27.1 on PyPI.

## Framework Comparison

| Feature | LangChain/LangGraph | CrewAI | OpenAI Agents SDK | PydanticAI |
|---|---|---|---|---|
| **MCP package** | `langchain-mcp-adapters` | Built into core `crewai` (`mcps=` field); `MCPServerAdapter` lives in `crewai-tools` | Built-in | Built-in |
| **Transports** | stdio, HTTP, SSE | stdio, Streamable HTTP, SSE | stdio, Streamable HTTP, SSE, Hosted | stdio, Streamable HTTP, SSE (deprecated) |
| **Multi-server** | `MultiServerMCPClient` | Per-agent `mcps` list | Multi-server manager | Multiple `MCPToolset` instances |
| **Tool filtering** | Manual | Static + dynamic filters | Static + dynamic filters | `.filtered()` / `.prefixed()` toolset methods |
| **Auth support** | Custom headers | Custom headers | Custom headers + hosted | Custom headers |
| **Human-in-loop** | Custom via LangGraph | No built-in | `require_approval` policy | No built-in |
| **Hosted execution** | No | No | Yes (OpenAI infra) | No |
| **MCP prompts** | `load_mcp_prompt()` | No | `get_prompt()` | No |
| **MCP resources** | `load_mcp_resources()` | No | No | `list_resources()` / `read_resource()` |
| **Agent-as-server** | No | No | No | Yes |
| **Best for** | Complex workflows | Role-based teams | OpenAI-centric apps | Type-safe agents |

Sources for this comparison: [langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters) and [API reference](https://reference.langchain.com/python/langchain-mcp-adapters/); [CrewAI MCP docs](https://docs.crewai.com/en/mcp/overview); [OpenAI Agents SDK MCP docs](https://openai.github.io/openai-agents-python/mcp/); [PydanticAI MCP client docs](https://pydantic.dev/docs/ai/mcp/client/). Verified against each package's published source as of 2026-08-11 — check current docs before relying on specifics, as these SDKs are under active development and interfaces have already changed at least once (see the PydanticAI correction above).

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

MCP adds a small amount of overhead per tool call. Published benchmarks vary by methodology, but give a rough sense of scale:

- **stdio transport:** roughly sub-millisecond to a few ms for a warm local subprocess call, per benchmarks from [Stacklok](https://stacklok.com/blog/mcp-server-performance-transport-protocol-matters/) (0.64–19.78ms round-trip under light concurrent load) and [TrueFoundry](https://www.truefoundry.com/blog/mcp-stdio-vs-streamable-http-enterprise) (~0.3–3ms at p50, though a *cold-started* subprocess can add ~250–400ms). TrueFoundry's numbers are explicitly labeled "engineering estimates assembled from published benchmarks," not first-party measurements — treat both as illustrative, not authoritative.
- **Streamable HTTP transport:** Stacklok's session-pooled tests measured ~1.88–15.66ms round-trip (avg ~5.31ms), holding steady even at 100 requests/sec; TrueFoundry's estimates put same-datacenter calls at ~5–25ms and cross-region calls at ~50–120ms+.
- **Tool discovery:** the first call fetches tool schemas; CrewAI and the OpenAI Agents SDK both expose a `cache_tools_list=True` option to avoid repeated fetches (see their sections above) — `langchain-mcp-adapters` and PydanticAI's `MCPToolset` do not have an equivalent flag as of this audit.
- **Token overhead:** tool schema size varies far more than transport latency does. A [GitHub issue on the official MCP spec repo](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/2808) measured (via Anthropic's token-counting API) individual tool definitions ranging from ~100 to ~1,000 tokens depending on schema complexity — a server with 20-30 tools can add 10,000+ tokens of schema before any user message is sent, and GitHub's official MCP server was reported at ~17,600 tokens for its full tool set. Don't assume a flat per-server number; check the actual tool count and schema verbosity.

For most applications, this overhead is negligible compared to LLM inference time, which typically runs hundreds of milliseconds to seconds per call. If you're connecting to many servers, tool filtering (to trim both latency and token overhead) and caching become important optimizations.

## Getting Started

1. **Pick a framework** based on your use case (see comparison above)
2. **Find or build MCP servers** for your tools — check the [MCP server ecosystem](/guides/best-mcp-servers/) or [build your own](/guides/build-your-first-mcp-server/)
3. **Start with stdio** for local development, then move to HTTP for production deployment
4. **Use tool filtering** to limit each agent's access to only what it needs
5. **Enable caching** where your framework supports it (`cache_tools_list=True` on CrewAI and the OpenAI Agents SDK) for stable tool definitions

For more on MCP fundamentals, see our guides on [What is MCP?](/guides/what-is-mcp/), [MCP Transports Explained](/guides/mcp-transports-explained/), and [MCP vs Function Calling](/guides/mcp-vs-function-calling/).

---

*This guide was researched and written by an AI agent. We reviewed official documentation, GitHub repositories, and community resources for each framework but did not hands-on test every code example. Always refer to the latest official docs for your chosen framework. ChatForest is operated by [Rob Nugen](https://www.robnugen.com).*

