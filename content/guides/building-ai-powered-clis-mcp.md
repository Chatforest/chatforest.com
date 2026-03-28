---
title: "Building AI-Powered CLIs with MCP: From Terminal Tools to Autonomous Agents"
date: 2026-03-28T23:30:00+09:00
description: "A practical guide to building AI-powered command-line tools using the Model Context Protocol — covering CLI design for agents, MCP client architecture, structured output patterns, and the terminal-first approach that's winning in 2026."
content_type: "Guide"
card_description: "Learn how to build CLI tools that AI agents can use, and how to build terminal-based AI agents powered by MCP."
last_refreshed: 2026-03-28
---

The terminal is having a moment. In 2026, the most capable AI coding tools — Claude Code, Aider, OpenCode, Gemini CLI — all run in the terminal, not in a GUI. Teams that built elaborate graphical interfaces are watching terminal-first agents outperform them on benchmarks and in production. This guide covers both sides of the CLI-AI relationship: how to design CLI tools that agents can use effectively, and how to build your own terminal-based AI agents using the Model Context Protocol. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## Why the Terminal Wins for AI Agents

The shift to terminal-first AI development isn't aesthetic — it's architectural. Terminal agents have concrete advantages:

**Composability.** Unix pipes, environment variables, and file I/O create a natural integration layer. An agent that can run shell commands can use any tool on the system without custom integrations.

**Speed.** No rendering overhead, no UI state to manage, no websocket connections to maintain. A CLI agent can read a file, edit it, run tests, and check results in seconds.

**Parallelism.** Terminal agents can spawn parallel processes trivially. One system reported that dispatching 4 concurrent agents in isolated git worktrees reduced a 4-hour task to 1 hour — something that's awkward to orchestrate through a GUI.

**Reproducibility.** Every action is a command that can be logged, replayed, and audited. No clicking through menus or relying on UI state.

The Claude Code architecture demonstrates this well: a single-threaded master loop that observes, reasons, acts (via tools), and reflects — all orchestrated through the terminal. The entire Unix philosophy of small, composable commands maps naturally to how language models prefer to work.

## Two Sides of CLI + AI

There are two distinct problems in this space, and they're often confused:

1. **Designing CLI tools that AI agents can use** — making your existing tools agent-friendly
2. **Building AI agents that live in the terminal** — creating agentic systems powered by LLMs

Both benefit from MCP, but in different ways. Let's cover each.

---

## Part 1: Designing CLI Tools for AI Agents

If you maintain a CLI tool, AI agents are probably already trying to use it. The question is whether your tool helps or fights them. Research across production agent deployments reveals consistent patterns that separate agent-friendly CLIs from tools that cause agents to loop, hallucinate, or fail.

### The Core Principle: Machine-Readable by Default

Agents don't read your beautifully formatted tables. They parse structured output. The single most impactful change you can make to any CLI tool is adding a `--json` flag:

```bash
# Human-friendly (default)
$ mytool list
NAME        STATUS    CREATED
my-app      running   2026-03-15
test-db     stopped   2026-03-10

# Agent-friendly
$ mytool list --json
[
  {"name": "my-app", "status": "running", "created": "2026-03-15"},
  {"name": "test-db", "status": "stopped", "created": "2026-03-10"}
]
```

The `--json` flag should be a presentation-layer concern only — identical behavior, structured output. This is the pattern that Terraform, GitHub CLI, Docker, and most modern CLIs have adopted.

### Six Rules for Agent-Friendly CLIs

Based on published research and production experience across the industry:

**1. Structured output for every command.** Every command that produces output should support `--json` or `--output json`. Include error responses in the structured format too — an agent that gets a plain-text error message when it expected JSON will struggle to recover.

**2. Deterministic exit codes.** Use meaningful exit codes, not just 0/1. Exit code 2 for invalid arguments, 3 for authentication failures, 4 for not-found errors. Agents use exit codes for control flow before they even parse output.

**3. Schema introspection.** Implement `--help --json` or a `--describe` flag that returns the tool's capabilities as structured data. Agents need to discover what a tool can do without reading documentation. This is effectively what MCP provides at the protocol level.

```bash
$ mytool --describe
{
  "commands": [
    {
      "name": "list",
      "description": "List all resources",
      "flags": [
        {"name": "--status", "type": "string", "enum": ["running", "stopped"]}
      ]
    }
  ]
}
```

**4. Accept JSON input.** Humans hate typing nested JSON in the terminal, but agents prefer it. Support both flag-based and JSON-based input:

```bash
# Human style
$ mytool create --name my-app --replicas 3

# Agent style
$ mytool create --json '{"name": "my-app", "replicas": 3}'
```

**5. Idempotent operations.** Agents retry. If `mytool create` fails halfway through and the agent runs it again, the tool should handle the duplicate gracefully — either succeeding silently or returning a clear "already exists" response.

**6. No interactive prompts.** If a command would normally prompt for confirmation, provide a `--yes` or `--force` flag. An agent stuck at a `y/n` prompt is a dead agent. Every interactive path needs a non-interactive alternative.

### When CLI Beats MCP

The debate between [CLI tools and MCP servers for AI agents](/guides/mcp-vs-cli-ai-agents/) has a nuanced answer. CLI tools win when:

- The agent's training data already covers the tool well (git, curl, standard Unix utilities)
- You need zero setup — no server process, no configuration
- Operations are local and fast
- The tool is well-known enough that the model can use it without schema discovery

MCP wins when:

- You need typed schemas and validation before execution
- The tool requires stateful connections (databases, APIs with session tokens)
- You want fine-grained permission control over what the agent can do
- Discovery matters — the agent needs to learn what's available at runtime

The pragmatic answer for 2026: **use both**. Expose common operations as CLI commands, and wrap complex workflows as MCP tools. The [Claude Code architecture](https://code.claude.com/docs/en/how-claude-code-works) does exactly this — it has dedicated tools for file operations and search, but also shells out to arbitrary commands when needed.

---

## Part 2: Building Terminal AI Agents with MCP

Now let's flip the perspective. Instead of making tools for agents, let's build an agent that lives in the terminal and uses MCP to connect to tools.

### Architecture of a Terminal Agent

Every terminal AI agent follows the same core loop:

```
┌──────────────────────────────────────────┐
│  1. READ    — Accept user input          │
│  2. THINK   — Send to LLM with context   │
│  3. ACT     — Execute tool calls         │
│  4. DISPLAY — Show results to user       │
│  └──── Loop until task complete ─────────┘
```

The key architectural decisions are:

- **How tools are discovered and invoked** (MCP vs. direct API calls vs. shell commands)
- **How context is managed** (what goes into the LLM prompt, what gets summarized or dropped)
- **How the agent decides when to stop** (natural termination vs. explicit signals)

### MCP Client Integration

MCP gives your terminal agent a standardized way to discover and use tools. Instead of hardcoding tool definitions, your agent connects to MCP servers that expose their capabilities at runtime.

A minimal MCP client in Python using the official SDK:

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def connect_to_server(command: str, args: list[str]):
    """Connect to an MCP server and discover its tools."""
    server_params = StdioServerParameters(
        command=command,
        args=args
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Discover available tools
            tools = await session.list_tools()
            for tool in tools.tools:
                print(f"Tool: {tool.name} — {tool.description}")

            # Call a tool
            result = await session.call_tool(
                "tool_name",
                arguments={"key": "value"}
            )
            return result
```

In TypeScript with the official SDK:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["path/to/server.js"]
});

const client = new Client({ name: "my-cli-agent", version: "1.0.0" });
await client.connect(transport);

// Discover tools
const { tools } = await client.listTools();

// Call a tool
const result = await client.callTool({
  name: "search_files",
  arguments: { query: "TODO", path: "./src" }
});
```

For a complete walkthrough of building MCP clients, see our guide on [building MCP clients](/guides/building-mcp-clients/).

### The Agentic Loop with Tool Use

The core of any terminal agent is the loop that sends messages to the LLM, detects tool calls in the response, executes them, and feeds results back. Here's the pattern:

```python
async def agent_loop(user_message: str, mcp_session, llm_client):
    """Core agentic loop — runs until the model stops calling tools."""
    messages = [{"role": "user", "content": user_message}]

    # Convert MCP tools to the format the LLM expects
    available_tools = await mcp_session.list_tools()
    tool_definitions = [
        {
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.inputSchema
        }
        for tool in available_tools.tools
    ]

    while True:
        # Send to LLM
        response = llm_client.messages.create(
            model="claude-sonnet-4-6-20250514",
            messages=messages,
            tools=tool_definitions,
            max_tokens=4096
        )

        # Check if the model wants to use tools
        tool_calls = [b for b in response.content if b.type == "tool_use"]

        if not tool_calls:
            # Model responded with text — we're done
            text = next(b.text for b in response.content if b.type == "text")
            print(text)
            break

        # Execute each tool call via MCP
        messages.append({"role": "assistant", "content": response.content})

        tool_results = []
        for call in tool_calls:
            result = await mcp_session.call_tool(
                call.name,
                arguments=call.input
            )
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": call.id,
                "content": result.content
            })

        messages.append({"role": "user", "content": tool_results})
```

This is the same pattern used by Claude Code, Aider, and every other terminal agent — the differences are in the details of context management, error handling, and user interaction.

### Managing Context in the Terminal

Terminal agents face a unique context challenge. Every tool call result adds to the conversation, and context windows fill up fast. Production terminal agents use several strategies:

**Sliding window.** Drop the oldest messages when approaching the context limit. Simple but loses early context that might matter.

**Summarization.** Periodically compress the conversation history into a summary. Claude Code does this automatically — it compresses prior messages as the conversation approaches context limits.

**Selective inclusion.** Only include tool results that are relevant to the current task. If the agent read 20 files but only 3 are relevant, summarize or drop the rest.

**Tiered context.** Keep a persistent system prompt (project context, rules, capabilities) separate from the ephemeral conversation. The system prompt stays; conversation messages get managed. This is the pattern behind [CLAUDE.md files](/guides/writing-effective-claude-md-files/) — persistent context that survives conversation compression.

### Connecting Multiple MCP Servers

Real-world terminal agents connect to multiple MCP servers simultaneously — a file system server, a database server, a search server, and so on. The pattern is to connect to all servers at startup and merge their tool lists:

```python
async def connect_all_servers(server_configs: list[dict]):
    """Connect to multiple MCP servers and aggregate tools."""
    all_tools = []
    sessions = {}

    for config in server_configs:
        session = await connect_to_server(
            config["command"],
            config["args"]
        )
        tools = await session.list_tools()

        # Namespace tools to avoid collisions
        for tool in tools.tools:
            namespaced_name = f"{config['name']}__{tool.name}"
            all_tools.append({
                "name": namespaced_name,
                "description": f"[{config['name']}] {tool.description}",
                "input_schema": tool.inputSchema
            })
            sessions[namespaced_name] = session

    return all_tools, sessions
```

Tool namespacing prevents collisions when multiple servers expose tools with the same name. This is a solved problem in frameworks like [mcp-agent](https://github.com/lastmile-ai/mcp-agent) and the [Claude Agent SDK](/guides/mcp-agent-sdks-2026/).

### Error Handling in the Loop

Terminal agents need robust error handling because tools fail regularly — network timeouts, permission errors, rate limits, malformed responses. The key patterns:

**Retry with backoff** for transient failures (network errors, rate limits). But cap retries — an agent stuck in a retry loop burns tokens and time.

**Graceful degradation.** If a tool fails, tell the model what happened and let it adapt. The model might find an alternative approach:

```python
try:
    result = await mcp_session.call_tool(call.name, arguments=call.input)
except Exception as e:
    result = f"Tool '{call.name}' failed: {str(e)}. Try an alternative approach."
```

**Timeout enforcement.** Set timeouts on every tool call. A tool that hangs indefinitely will block the entire agent loop. For guidance on handling long-running operations, see our guide on [MCP async tasks](/guides/mcp-async-tasks-long-running/).

---

## Part 3: Production Patterns

### Structured Output from Your Agent

Your terminal agent should itself support structured output — the same principle that applies to CLI tools applies to your agent:

```bash
# Interactive mode (human-friendly)
$ myagent "find all TODO comments in src/"
Found 12 TODO comments across 8 files:
  src/auth.py:42 — TODO: Add rate limiting
  src/db.py:15 — TODO: Connection pooling
  ...

# Pipe mode (machine-friendly)
$ myagent --json "find all TODO comments in src/"
{
  "results": [
    {"file": "src/auth.py", "line": 42, "text": "TODO: Add rate limiting"},
    {"file": "src/db.py", "line": 15, "text": "TODO: Connection pooling"}
  ],
  "total": 12
}
```

Detect whether stdout is a TTY to automatically switch between modes, or use an explicit flag.

### Permission Models

Terminal agents that can run arbitrary commands need permission guardrails. The dominant patterns in 2026:

**Allowlist.** Define which tools/commands the agent can use freely. Everything else requires confirmation. This is the Claude Code model — read operations are auto-approved, writes need user confirmation.

**Tiered permissions.** Read-only operations run automatically. Mutations require confirmation. Destructive operations (delete, force-push) require explicit opt-in.

**Sandboxing.** Run tool calls in a restricted environment — a container, a chroot, or a dedicated user with limited permissions. This is essential for agents that execute user-provided or model-generated code.

For deep coverage of security considerations, see our guides on [MCP server security](/guides/mcp-server-security/) and [MCP attack vectors and defense](/guides/mcp-attack-vectors-defense/).

### Observability

You can't debug what you can't see. Production terminal agents need:

- **Full conversation logging.** Every message sent to and received from the LLM, with timestamps.
- **Tool call tracing.** Input, output, duration, and exit status for every tool invocation.
- **Token counting.** Track input and output tokens per request to monitor costs.
- **Session recording.** The ability to replay an entire agent session for debugging.

These map directly to the patterns covered in our [MCP logging and observability guide](/guides/mcp-logging-observability/). The key insight: log at the harness level (your agent code), not inside individual tools.

### Cost Control

Terminal agents can burn through API credits fast. A complex coding task might require 50+ LLM calls with large context windows. Practical cost controls:

- **Set token budgets** per task or session. Kill the loop if the budget is exceeded.
- **Use cheaper models for simple steps.** Route tool-result summarization to a faster, cheaper model.
- **Cache tool results.** If the agent reads the same file twice, serve it from cache.
- **Minimize context.** Every token in the prompt costs money. Aggressive context management isn't just about fitting in the window — it's about cost.

For detailed strategies, see our [MCP cost optimization guide](/guides/mcp-cost-optimization/).

---

## Frameworks vs. Building from Scratch

You don't have to build everything yourself. Several frameworks handle the plumbing of terminal agent development:

| Framework | Language | MCP Support | Best For |
|-----------|----------|-------------|----------|
| [Claude Agent SDK](/guides/mcp-agent-sdks-2026/) | Python | Native | Building on Claude models |
| [mcp-agent](https://github.com/lastmile-ai/mcp-agent) | Python | Native | Multi-server orchestration |
| [LangGraph](/guides/mcp-agent-framework-integrations/) | Python | Via integration | Complex state machines |
| [Mastra](https://mastra.ai) | TypeScript | Native | TypeScript-first agents |
| [Pydantic AI](https://ai.pydantic.dev) | Python | Via integration | Type-safe tool definitions |

The trade-off is always the same: frameworks save time on boilerplate but constrain your architecture. For a simple terminal agent with 2-3 MCP servers, building from scratch with the official SDK gives you more control. For complex multi-agent systems, a framework handles orchestration patterns you'd otherwise reinvent.

See our [framework integration guide](/guides/mcp-agent-framework-integrations/) for detailed comparisons.

## The Bigger Picture

The convergence of CLI tools and AI agents is reshaping how software gets built. The Unix philosophy — small tools, structured data, composable pipelines — turns out to be an excellent fit for AI agent architectures. MCP formalizes what Unix pipes did informally: a standard protocol for tools to expose capabilities and for agents to discover and use them.

The practical takeaway: if you maintain CLI tools, add `--json` output and schema introspection. If you're building AI agents, start in the terminal — it's faster to iterate, easier to debug, and the resulting agents are more capable than their GUI counterparts. And use MCP to connect the pieces, because the ecosystem of available servers is [growing fast](/guides/best-mcp-servers/).

## Further Reading

- [What Is MCP?](/guides/what-is-mcp/) — foundational concepts
- [MCP vs CLI for AI Agents](/guides/mcp-vs-cli-ai-agents/) — the full debate
- [Building MCP Clients](/guides/building-mcp-clients/) — complete client tutorial
- [Build Your First MCP Server](/guides/build-your-first-mcp-server/) — server-side walkthrough
- [MCP Tool Design Patterns](/guides/mcp-tool-design-patterns/) — designing effective tools
- [MCP Transports Explained](/guides/mcp-transports-explained/) — stdio, HTTP, and when to use each
- [How to Build an AI Agent](/guides/how-to-build-ai-agent/) — broader agent architecture guide
- [AI Coding Assistants Compared](/guides/ai-coding-assistants-compared/) — the tools using these patterns
- [MCP Server Frameworks and SDKs](/guides/mcp-server-frameworks-sdks/) — official and community SDKs
