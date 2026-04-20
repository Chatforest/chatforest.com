# MCP and OpenAI: How ChatGPT, the Agents SDK, Codex, and the Responses API Use the Model Context Protocol

> A comprehensive guide to OpenAI's MCP integration — covering the Responses API's hosted MCP tool, the Agents SDK (Python and TypeScript) with MCPServerStdio and


When Sam Altman [announced](https://x.com/OpenAIDevs/status/1904957755829481737) in March 2025 that "people love MCP and we are excited to add support across our products," it marked a turning point. The Model Context Protocol — created by Anthropic and open-sourced in late 2024 — went from a single-vendor experiment to an industry standard overnight. OpenAI's adoption meant that the two largest AI labs were now backing the same tool integration protocol.

Since that announcement, OpenAI has woven MCP into every layer of their platform: the **Responses API** for backend integrations, the **Agents SDK** for building autonomous agents, **ChatGPT Developer Mode** for interactive tool use, the **Apps SDK** for building interactive UIs inside ChatGPT, and **Codex** for AI-assisted coding. Each integration point serves a different use case, and understanding which one to use — and how — is essential for developers building on the OpenAI platform.

This guide covers all of OpenAI's MCP integration surfaces with practical code examples, security considerations, and architectural guidance. Our analysis draws on [OpenAI's official documentation](https://developers.openai.com/api/docs/mcp), the [Agents SDK source code](https://github.com/openai/openai-agents-python), community reports, and published security research — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## OpenAI's MCP Adoption Timeline

Understanding when and how OpenAI adopted MCP helps explain the current state of their integrations:

- **November 2024** — Anthropic open-sources MCP. Most teams, including OpenAI, take a wait-and-see approach.
- **March 2025** — OpenAI officially adopts MCP. Support lands first in the Agents SDK (immediately available), with the Responses API and ChatGPT desktop support announced as coming soon. OpenAI joins the MCP steering committee.
- **May 2025** — ChatGPT begins testing MCP integration. Microsoft and GitHub join the MCP steering committee at Build 2025.
- **June 2025** — The Responses API adds remote MCP server support with the `type: "mcp"` tool configuration.
- **September 2025** — ChatGPT Developer Mode launches in beta with full MCP support, including write actions. Previously, MCP connectors in ChatGPT were read-only.
- **November 2025** — ChatGPT Apps (formerly "connectors") become available on all paid plans. The MCP Apps UI standard is proposed.
- **December 2025** — Anthropic donates MCP to the Agentic AI Foundation (AAIF) under the Linux Foundation. OpenAI is a co-founder alongside Anthropic and Block.
- **January 2026** — MCP Apps UI standard matures. ChatGPT, Claude, Goose, and VS Code ship support.
- **March 2026** — OpenAI's Agents SDK TypeScript version ships with full MCP support. Codex adds MCP shortcuts. The steering committee reaches early consensus on making MCP fully stateless, targeting June 2026.

## The Five Integration Points

OpenAI's MCP support spans five distinct surfaces, each designed for different developer workflows:

| Integration Point | Use Case | Transport | Language | MCP Capabilities |
|---|---|---|---|---|
| **Responses API** | Backend API calls with MCP tools | Streamable HTTP (hosted) | Any (REST API) | Tools only |
| **Agents SDK (Python)** | Building autonomous agents | stdio, Streamable HTTP, hosted | Python | Tools, resources, prompts |
| **Agents SDK (TypeScript)** | Building agents in JS/TS | stdio, Streamable HTTP, hosted | TypeScript | Tools, resources, prompts |
| **ChatGPT Developer Mode** | Interactive tool use in ChatGPT | Streamable HTTP | N/A (UI-based) | Tools (read + write) |
| **Apps SDK** | Interactive UIs inside ChatGPT | Streamable HTTP | TypeScript | Tools + UI rendering |
| **Codex** | AI-assisted coding with MCP tools | stdio, Streamable HTTP | N/A (product) | Tools, resources |

The key distinction: the **Responses API** and **hosted MCP tools** run server-side — OpenAI's infrastructure connects to your remote MCP server on your behalf. The **Agents SDK** with stdio runs client-side — your code launches and manages the MCP server process locally. This architectural difference has significant implications for security, latency, and deployment.

## The Responses API: MCP in API Calls

The [Responses API](https://developers.openai.com/api/docs/guides/tools-connectors-mcp) is OpenAI's primary API for building agentic applications. It replaced the older Chat Completions API for tool-use scenarios and supports MCP servers as a built-in tool type.

### How It Works

Instead of manually defining function schemas for each tool, you point the Responses API at a remote MCP server. The API discovers the server's available tools, passes them to the model, and handles tool invocation automatically:

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    tools=[
        {
            "type": "mcp",
            "server_label": "my_server",
            "server_url": "https://mcp.example.com/sse",
            "require_approval": "never",
        }
    ],
    input="What files are in the project root?",
)

print(response.output_text)
```

The `type: "mcp"` tool configuration tells the Responses API to treat this as a remote MCP server rather than a traditional function call. The API connects to the server URL, discovers available tools via the MCP protocol, and presents them to the model alongside any other tools you've configured.

### Key Parameters

- **`server_label`** — A human-readable name for the server. Used in logging and the model's tool descriptions.
- **`server_url`** — The URL of your remote MCP server. Must support Streamable HTTP or SSE transport.
- **`require_approval`** — Controls whether tool calls need explicit approval before execution. Options:
  - `"never"` — Tools execute automatically. Use only for trusted, read-only servers.
  - `"always"` — Every tool call pauses for approval. Safest for write operations.
  - A list of specific tool names that require approval, with all others auto-approved.
- **`headers`** — Optional HTTP headers sent with each request (e.g., authorization tokens).

### Tool Approval Flow

Each MCP tool invocation produces an `mcp_tool_call` item in the response. When approval is required, the stream pauses and returns the tool call details for inspection. Your code can examine the tool name, arguments, and decide whether to approve:

```python
response = client.responses.create(
    model="gpt-4.1",
    tools=[
        {
            "type": "mcp",
            "server_label": "database",
            "server_url": "https://mcp.example.com/db",
            "require_approval": "always",
        }
    ],
    input="Delete all inactive users from the database",
)

# Check for pending approvals in the response
for item in response.output:
    if item.type == "mcp_approval_request":
        # Inspect the tool call before approving
        print(f"Tool: {item.name}")
        print(f"Arguments: {item.arguments}")
        # Approve or deny based on your logic
```

### Multiple MCP Servers

You can attach multiple remote MCP servers to a single Responses API call. The model sees all tools from all servers and can chain calls across them:

```python
response = client.responses.create(
    model="gpt-4.1",
    tools=[
        {
            "type": "mcp",
            "server_label": "filesystem",
            "server_url": "https://mcp.example.com/files",
            "require_approval": "never",
        },
        {
            "type": "mcp",
            "server_label": "database",
            "server_url": "https://mcp.example.com/db",
            "require_approval": "always",
        },
    ],
    input="Read the config file and update the database settings accordingly",
)
```

### Model Support

The MCP tool type works with GPT-4o series, GPT-4.1 series, and o-series reasoning models (o3, o4-mini). As of March 2026, GPT-5.3-Codex is also supported for Codex-specific workflows.

### Limitations

- **Remote only** — The Responses API can only connect to remote MCP servers over HTTP. You cannot use stdio (local process) servers directly. If you need local servers, use the Agents SDK.
- **Tools only** — The Responses API's MCP integration supports tools but not MCP resources or prompts. For full MCP feature support, use the Agents SDK.
- **OpenAI-hosted connection** — OpenAI's servers connect to your MCP server, which means your server must be publicly accessible (or accessible to OpenAI's infrastructure). This has security implications — see the [security section](#security-considerations) below.

## The Agents SDK: Full MCP for Agent Builders

The [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) is an open-source framework for building multi-agent workflows. It provides the most complete MCP integration in OpenAI's ecosystem, supporting all three transport types and the full range of MCP capabilities.

### Python SDK

The Python SDK (`openai-agents-python`) was the first to ship MCP support in March 2025. Install it with MCP extras:

```bash
pip install 'openai-agents[mcp]'
```

#### MCPServerStdio: Local Servers

Use `MCPServerStdio` when your MCP server runs as a local process. The SDK handles launching, communication, and cleanup:

```python
import asyncio
from agents import Agent, Runner
from agents.mcp import MCPServerStdio

async def main():
    async with MCPServerStdio(
        name="Filesystem Server",
        params={
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-filesystem", "/tmp/data"],
        },
    ) as server:
        agent = Agent(
            name="File Assistant",
            instructions="Help the user manage files in /tmp/data.",
            mcp_servers=[server],
        )

        result = await Runner.run(agent, "List all files in the directory")
        print(result.final_output)

asyncio.run(main())
```

The `MCPServerStdio` context manager starts the server process on enter and cleanly shuts it down on exit. The agent automatically discovers all tools exposed by the server and uses them during execution.

#### MCPServerStreamableHttp: Remote Servers

For remote MCP servers, use `MCPServerStreamableHttp`:

```python
from agents.mcp import MCPServerStreamableHttp

async with MCPServerStreamableHttp(
    name="Remote API Server",
    params={
        "url": "https://mcp.example.com/mcp",
        "headers": {"Authorization": f"Bearer {token}"},
        "timeout": 10,
    },
    cache_tools_list=True,
    max_retry_attempts=3,
) as server:
    agent = Agent(
        name="API Assistant",
        instructions="Use the API tools to help the user.",
        mcp_servers=[server],
    )
    result = await Runner.run(agent, "Search for recent orders")
    print(result.final_output)
```

Key parameters for `MCPServerStreamableHttp`:

- **`cache_tools_list`** — Cache the tool list to avoid re-fetching on every agent turn. Set to `True` for servers with a stable tool set.
- **`max_retry_attempts`** and **`retry_backoff_seconds_base`** — Automatic retries with exponential backoff for `list_tools()` and `call_tool()` operations.

#### HostedMCPTool: OpenAI-Hosted Connections

For remote servers where you want OpenAI to manage the connection (same as the Responses API approach), use `HostedMCPTool`:

```python
from agents import Agent, HostedMCPTool, Runner

agent = Agent(
    name="Assistant",
    tools=[
        HostedMCPTool(
            tool_config={
                "type": "mcp",
                "server_label": "gitmcp",
                "server_url": "https://gitmcp.io/openai/codex",
                "require_approval": "never",
            }
        )
    ],
)

result = await Runner.run(agent, "What language is this repository written in?")
```

The difference from `MCPServerStreamableHttp`: with `HostedMCPTool`, OpenAI's servers connect to the MCP server. With `MCPServerStreamableHttp`, your agent process connects directly. Choose based on whether you want the connection managed server-side (hosted) or client-side (direct).

#### Tool Approval Callbacks

For fine-grained control over which tools can execute, provide an approval callback:

```python
from agents import MCPToolApprovalFunctionResult, MCPToolApprovalRequest

SAFE_TOOLS = {"read_file", "list_directory", "search"}

def approve_tool(request: MCPToolApprovalRequest) -> MCPToolApprovalFunctionResult:
    if request.data.name in SAFE_TOOLS:
        return {"approve": True}
    return {"approve": False, "reason": "This tool requires human review"}

agent = Agent(
    name="Cautious Assistant",
    tools=[
        HostedMCPTool(
            tool_config={
                "type": "mcp",
                "server_label": "database",
                "server_url": "https://mcp.example.com/db",
                "require_approval": "always",
            },
            on_approval_request=approve_tool,
        )
    ],
)
```

### TypeScript SDK

The [TypeScript SDK](https://github.com/openai/openai-agents-js) (`@openai/agents`) shipped with full MCP support and mirrors the Python SDK's API:

```typescript
import { Agent, run } from "@openai/agents";
import { MCPServerStreamableHttp } from "@openai/agents/mcp";

const server = new MCPServerStreamableHttp({
  name: "Remote Server",
  url: "https://mcp.example.com/mcp",
  headers: { Authorization: `Bearer ${token}` },
});

await server.connect();

const agent = new Agent({
  name: "Assistant",
  instructions: "Use the MCP tools to help the user.",
  mcpServers: [server],
});

const result = await run(agent, "Search for recent orders");
console.log(result.finalOutput);

await server.close();
```

The TypeScript SDK supports the same three server types:
- **`MCPServerStdio`** — Local process servers
- **`MCPServerStreamableHttp`** — Direct remote connections
- **`HostedMCPTool`** — OpenAI-managed remote connections

Both SDKs include built-in tracing for debugging agent workflows, including MCP tool calls.

## ChatGPT Developer Mode: Interactive MCP

[ChatGPT Developer Mode](https://help.openai.com/en/articles/12584461-developer-mode-apps-and-full-mcp-connectors-in-chatgpt-beta) launched in September 2025 as a beta feature that turns ChatGPT into a full MCP client with read **and** write capabilities.

### What Changed

Before Developer Mode, ChatGPT's MCP integrations (called "connectors") were limited to read-only operations — search, fetch, and query. Developer Mode removes that restriction, enabling write actions like updating databases, sending messages, creating records, and triggering workflows.

### How to Use It

1. **Enable Developer Mode** — Available to Pro, Plus, Business, Enterprise, and Education accounts on the web.
2. **Add an MCP Server** — Register a remote MCP server by providing its URL and any required authentication.
3. **Use Tools in Conversation** — ChatGPT discovers the server's tools and offers them during conversation.

### Safety Controls

ChatGPT displays an explicit confirmation modal before executing any write or modify operation. Users can expand the tool call details to inspect the full JSON payload, including inputs and expected outputs, before approving.

This is important: the safety model relies on ChatGPT correctly identifying which operations are destructive. As OpenAI's own documentation [acknowledges](https://help.openai.com/en/articles/12584461-developer-mode-apps-and-full-mcp-connectors-in-chatgpt-beta), the AI's reasoning can make mistakes — potentially misclassifying harmful operations as benign. Developer Mode is intended for developers who understand how to safely configure and test their MCP servers.

### What You Can Build

With full MCP support, ChatGPT becomes a conversational interface to any system that has an MCP server:

- **Project management** — "Create a new sprint in Jira and move these tickets into it"
- **Database operations** — "Show me all users who signed up last week, then update their tier to premium"
- **Communication** — "Draft a Slack message to the engineering channel about today's deployment"
- **E-commerce** — "Check inventory for product X and update the price to $29.99"

The key advantage over the Responses API: Developer Mode provides a visual, interactive interface where users can inspect and approve each operation. The disadvantage: it's not programmable — you cannot automate workflows through Developer Mode the way you can through the API.

## The Apps SDK: Interactive UIs Inside ChatGPT

The [Apps SDK](https://developers.openai.com/apps-sdk/quickstart) extends MCP by adding UI capabilities. Instead of just exposing tools, an MCP server built with the Apps SDK can render interactive widgets inside ChatGPT's conversation interface.

### Architecture

Apps SDK applications have two layers:

1. **MCP Server** — The backend that exposes tools, just like any MCP server.
2. **UI Widget** — A web component (HTML/CSS/JS, any framework) that renders inside an iframe in ChatGPT. The widget communicates with ChatGPT via the MCP Apps UI bridge — JSON-RPC messages over `postMessage`.

UI resources are pre-declared in the MCP server manifest. OpenAI reviews assets before publication and uses the declarations for caching.

### Cross-Client Compatibility

The MCP Apps standard is not ChatGPT-specific. Since the spec was proposed in November 2025, Claude, Goose, and VS Code have also shipped support. An app built with the Apps SDK works across all MCP Apps-compatible clients without client-specific code — a significant advantage for developers building tools that need to work across AI platforms.

### When to Use It

Use the Apps SDK when your tool needs:
- **Visual output** — Charts, tables, forms, maps
- **User interaction** — Buttons, inputs, dropdowns
- **Rich feedback** — Progress indicators, previews, confirmations
- **Cross-platform reach** — One UI that works in ChatGPT, Claude, VS Code, and more

For tools that only need text-based input and output, a standard MCP server (without the Apps SDK) is simpler.

## Codex: MCP for AI-Assisted Coding

[OpenAI Codex](https://openai.com/codex/) uses MCP to connect AI coding agents to external tools and context providers. This is particularly useful for connecting to remotely hosted systems like Figma, Linear, GitHub, or internal knowledge services.

### MCP in Codex

Codex supports MCP servers through both stdio (local) and Streamable HTTP (remote) transports. Recent 2026 updates added MCP shortcuts in the composer — including install keyword suggestions and an MCP server submenu in the "Add context" menu — making it easier to discover and connect to MCP servers.

### Codex + Agents SDK

By exposing the Codex CLI as an MCP server and orchestrating it with the Agents SDK, developers can build deterministic, reviewable coding workflows:

```python
from agents import Agent, Runner
from agents.mcp import MCPServerStdio

# Connect to Codex as an MCP server
async with MCPServerStdio(
    name="Codex",
    params={
        "command": "codex",
        "args": ["--mcp"],
    },
) as codex_server:
    agent = Agent(
        name="Code Reviewer",
        instructions="Review pull requests using Codex.",
        mcp_servers=[codex_server],
    )
    result = await Runner.run(agent, "Review PR #42 for security issues")
```

This pattern scales from a single agent to a complete software delivery pipeline, with each step reviewable and auditable.

### AGENTS.md

OpenAI's AGENTS.md standard — a simple instruction file developers can add to a repository to tell AI coding tools how to behave — works alongside MCP. While MCP provides the tools (file access, build systems, test runners), AGENTS.md provides the context (coding standards, review criteria, deployment procedures). Together they give Codex (and other coding agents) both the capability and the guidance to work effectively on a codebase.

## Security Considerations

OpenAI's MCP integration introduces specific security concerns that developers should understand and mitigate.

### The Hosted Connection Model

When using the Responses API or `HostedMCPTool`, OpenAI's servers connect to your MCP server on your behalf. This means:

- **Your MCP server must be publicly accessible** (or at least accessible to OpenAI's infrastructure)
- **Data flows through OpenAI** — tool inputs and outputs pass through OpenAI's servers before reaching your MCP server
- **Authentication tokens are sent to OpenAI** — if your server requires authentication, the tokens are included in the API request to OpenAI

For sensitive operations, consider using `MCPServerStreamableHttp` (direct connection) instead of `HostedMCPTool`, so your agent process connects directly to the MCP server without routing through OpenAI.

### Approval Controls

OpenAI provides three levels of tool approval:

1. **`require_approval: "never"`** — Auto-approve all tool calls. Only use for trusted, read-only servers.
2. **`require_approval: "always"`** — Every call needs approval. Safest for write operations.
3. **Selective approval** — Specify which tools require approval by name. Balance safety with usability.

In the Agents SDK, the approval callback pattern (shown above) enables programmatic approval decisions — allowing you to build allowlists, check argument patterns, or escalate to human review.

### Known Risks

Security researchers have identified several risk categories specific to OpenAI's MCP integration:

- **Prompt injection via tool responses** — A malicious MCP server can embed instructions in tool responses that manipulate the model's behavior. OpenAI's models have defenses against this, but it remains an active research area.
- **Unintended data exposure** — The model may send more data to an MCP server than the user intended. For example, if the conversation contains sensitive information and the model decides to include it in a tool call argument.
- **Malicious MCP servers** — Connecting to untrusted MCP servers exposes your workflow to potential data exfiltration, prompt injection, and destructive actions. OpenAI recommends connecting only to servers hosted by trusted providers (e.g., Stripe's official MCP server at `mcp.stripe.com` rather than a third-party Stripe MCP server).
- **Write action misclassification** — In ChatGPT Developer Mode, the safety model can make mistakes about which operations are destructive. Always inspect tool call payloads before approving write operations.

For a comprehensive treatment of MCP security risks and mitigations, see our [MCP attack vectors guide](/guides/mcp-attack-vectors-defense/) and [server security guide](/guides/mcp-server-security/).

### Recommendations

1. **Start with `require_approval: "always"`** for any MCP server that performs write operations
2. **Use official first-party MCP servers** when available (e.g., Stripe, Shopify, Twilio host their own servers)
3. **Audit tool call logs** — Enable tracing in the Agents SDK to monitor what tools are being called and with what arguments
4. **Keep MCP servers narrowly scoped** — A server that can only read from one database table is less risky than one with full database access
5. **Use direct connections for sensitive data** — Prefer `MCPServerStreamableHttp` over `HostedMCPTool` when data shouldn't route through OpenAI

## Choosing the Right Integration

### Use the Responses API when:
- You're building a backend service that needs MCP tools
- You want OpenAI to manage the MCP connection
- You only need tool calling (not resources or prompts)
- Your MCP servers are remote and publicly accessible

### Use the Agents SDK when:
- You're building autonomous agents with multi-step reasoning
- You need local MCP servers (stdio transport)
- You need full MCP capabilities (tools + resources + prompts)
- You want direct connections to MCP servers (no routing through OpenAI)
- You need programmatic tool approval logic

### Use ChatGPT Developer Mode when:
- You want an interactive, visual interface for MCP tools
- You need human-in-the-loop approval for write operations
- You're prototyping or testing MCP server integrations
- Your users are developers who understand the risks

### Use the Apps SDK when:
- Your tool needs interactive UI (charts, forms, previews)
- You want cross-platform reach (ChatGPT + Claude + VS Code)
- You're building a product for ChatGPT's 800+ million user base

### Use Codex MCP when:
- You need AI coding agents to access external context
- You want to connect Codex to project management, design, or documentation tools
- You're building automated coding pipelines with the Agents SDK

## OpenAI and the Future of MCP

OpenAI is not just adopting MCP — they're actively shaping its future. As a co-founder of the Agentic AI Foundation and a member of the MCP steering committee, OpenAI has influence over the protocol's direction.

### Stateless MCP

The steering committee has reached early consensus on making MCP a fully stateless protocol, with the specification change targeted for June 2026. This aligns with OpenAI's Responses API architecture, which is already essentially stateless — each API call is independent. The shift benefits cloud-native deployments and horizontal scaling, both priorities for OpenAI's infrastructure.

### MCP Apps

OpenAI's Apps SDK pushes MCP beyond tool calling into interactive UIs. The MCP Apps standard — with its iframe-based rendering, JSON-RPC bridge, and cross-client compatibility — represents a vision where MCP servers aren't just backends but full-stack applications. Whether this vision gains traction across the ecosystem depends on adoption by other MCP clients.

### AGENTS.md and Skills

Alongside MCP, OpenAI is pushing AGENTS.md as a complementary standard for AI agent configuration. While MCP answers "what can the agent do?" (tools), AGENTS.md answers "how should the agent behave?" (instructions). The combination gives coding agents like Codex a complete framework for working on codebases.

## Conclusion

OpenAI's MCP adoption is comprehensive. From the Responses API (for backend integrations) to ChatGPT Developer Mode (for interactive use) to the Agents SDK (for autonomous agents) to the Apps SDK (for interactive UIs), every major OpenAI product surface now speaks MCP.

The practical implication: if you build an MCP server, it works with both Claude and ChatGPT. If you build an MCP Apps UI, it works in both Claude and ChatGPT's interfaces. The protocol-level interoperability that MCP promises is becoming reality, and OpenAI's full commitment — as a steering committee member, AAIF co-founder, and active contributor — makes that interoperability durable.

For developers getting started, the Agents SDK is the most flexible entry point. It supports all transport types, all MCP capabilities, and gives you full control over the connection and approval flow. The Responses API is simpler for backend-only use cases. ChatGPT Developer Mode is best for prototyping and human-in-the-loop workflows. And the Apps SDK is the path forward if you need interactive UIs that work across AI platforms.

## Related Guides

- [What Is MCP?](/guides/what-is-mcp/) — The fundamentals of the Model Context Protocol
- [Using MCP Across AI Platforms](/guides/mcp-across-ai-platforms/) — How MCP works in Claude, Gemini, Copilot, and more
- [MCP Agent Framework Integrations](/guides/mcp-agent-framework-integrations/) — LangChain, CrewAI, PydanticAI MCP integration
- [MCP Transports Explained](/guides/mcp-transports-explained/) — stdio, SSE, and Streamable HTTP in depth
- [MCP Server Security](/guides/mcp-server-security/) — Securing your MCP servers
- [MCP Attack Vectors & Defense](/guides/mcp-attack-vectors-defense/) — Security threats and mitigations
- [MCP Authentication & OAuth 2.1](/guides/mcp-authentication-oauth/) — Authorization flows for MCP servers
- [Building MCP Clients](/guides/building-mcp-clients/) — How to build your own MCP client
- [The MCP Ecosystem in 2026](/guides/mcp-ecosystem-2026-state-of-the-standard/) — State of the standard

