# Using MCP Across AI Platforms: Claude, ChatGPT, Gemini, Copilot, and More

> How to use MCP servers with every major AI platform — covers Claude Desktop and Code, ChatGPT Apps and Agents SDK, Google Gemini CLI and Cloud, Microsoft Copilot Studio, Amazon Q


When Anthropic open-sourced the Model Context Protocol in late 2024, MCP was a single-vendor affair. That changed fast. By early 2026, OpenAI, Google, Microsoft, and Amazon have all adopted MCP, and the protocol now lives under the Linux Foundation's Agentic AI Foundation (AAIF) — co-founded by Anthropic, OpenAI, and Block, with support from Google, Microsoft, AWS, Cloudflare, and Bloomberg — as a vendor-neutral standard. The ecosystem has grown to over 10,000 active public MCP servers according to published reports, spanning individual developer tools to Fortune 500 deployments — a clear signal that MCP has moved from experiment to infrastructure.

The promise is straightforward: build an MCP server once, and any compliant AI platform can connect to it. This guide covers how that works in practice across every major platform, with configuration examples and cross-platform patterns. Our analysis draws on official documentation from each platform, published SDK guides, and community reports — we research and analyze rather than testing these configurations ourselves.

## The Cross-Platform Architecture

MCP follows a client-server model. An **MCP server** exposes tools, resources, and prompts through a standardized protocol. An **MCP client** (built into an AI platform) discovers and calls those tools on behalf of the LLM.

The key insight: the server doesn't need to know which AI platform is calling it. A filesystem MCP server that exposes `read_file` and `write_file` tools works identically whether Claude Desktop, ChatGPT, or Gemini CLI connects to it. The protocol handles discovery, invocation, and response formatting.

Three transport mechanisms carry MCP messages between client and server:

- **stdio** — Server runs as a local subprocess. The client launches it and communicates over standard input/output. Best for desktop and CLI tools.
- **SSE (Server-Sent Events)** — HTTP-based, server pushes events to the client. Used for remote servers, though being superseded.
- **Streamable HTTP** — The current recommended transport for remote servers. Stateless, scalable, supports streaming responses. This is where the ecosystem is converging.

The transport you choose determines which platforms can connect. stdio works with desktop apps and CLI tools. Streamable HTTP works with everything, including web-based platforms that cannot launch local processes.

## Platform-by-Platform Setup

### Anthropic Claude

Claude was the first platform to support MCP, and according to Anthropic's documentation, it offers the broadest transport support.

**Claude Desktop** reads its MCP configuration from `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/documents"],
      "env": {
        "NODE_ENV": "production"
      }
    },
    "remote-api": {
      "url": "https://mcp.example.com/sse",
      "transport": "sse"
    }
  }
}
```

The config file location varies by OS — `~/Library/Application Support/Claude/` on macOS, `%APPDATA%\Claude\` on Windows, and `~/.config/Claude/` on Linux, according to Anthropic's documentation.

**Claude Code** supports MCP through both CLI commands and project configuration:

```bash
# Add a stdio server
claude mcp add filesystem npx -y @modelcontextprotocol/server-filesystem /home/user/docs

# Add a remote server
claude mcp add remote-api https://mcp.example.com/api --transport http

# List configured servers
claude mcp list
```

For project-level sharing, Claude Code uses a `.mcp.json` file in the project root:

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://localhost/mydb"
      }
    }
  }
}
```

**Supported transports:** stdio, SSE, Streamable HTTP.

**Notable features:** Claude supports MCP sampling (letting the server request LLM completions), resource subscriptions, and prompt templates — the broadest feature set of any platform based on published documentation. As of April 2026, Claude Code supports up to 500,000 characters per MCP tool result, significantly expanding capacity for large data sources. Claude Cowork, Anthropic's collaborative agent workspace, is now generally available on macOS and Windows with expanded analytics and OpenTelemetry support.

### OpenAI ChatGPT

OpenAI announced MCP support for ChatGPT in March 2025, with broader rollout through 2025 and into 2026. According to OpenAI's documentation, ChatGPT's MCP implementation is remote-first — a meaningful architectural difference from Claude's local-first approach.

**ChatGPT Apps via MCP** allow developers to register remote MCP servers through the OpenAI platform. Users can then add these servers to their ChatGPT sessions. According to OpenAI's published guides:

- MCP servers are registered with OAuth 2.1 authentication
- ChatGPT connects to remote servers via Streamable HTTP
- Users on ChatGPT Plus, Pro, Enterprise, Business, and Edu plans can enable MCP connections
- Enterprise/Business/Edu users get full read+write tool access

**OpenAI Agents SDK** provides programmatic MCP integration in Python:

```python
from agents import Agent
from agents.mcp import MCPServerStreamableHTTP

async with MCPServerStreamableHTTP(
    url="https://mcp.example.com/api",
    headers={"Authorization": "Bearer TOKEN"}
) as server:
    tools = await server.list_tools()
    agent = Agent(
        name="assistant",
        instructions="Help the user with their tasks.",
        mcp_servers=[server]
    )
```

**Supported transports:** SSE, Streamable HTTP (recommended). stdio is not supported — ChatGPT cannot launch local processes.

**OpenAI Responses API** now includes native support for remote MCP servers, allowing developers to connect models to any MCP server with just a few lines of code. According to OpenAI's documentation, there is no additional cost for MCP tool calls — developers are billed only for output tokens from the API. The **Realtime API** also supports MCP by passing a remote server URL into the session configuration.

**MCP Connectors** — OpenAI has rolled out a growing catalog of partner-built MCP connectors reviewed by OpenAI, including Amplitude, Fireflies, Vercel, Monday.com, Stripe, Hex, Atlassian Rovo (Jira, Confluence), and others. These are available to Enterprise, Edu, Business, Pro, and Plus customers.

**Notable features:** Built-in OAuth 2.1 flow, meaning users authenticate with MCP servers through ChatGPT's UI rather than manually managing API keys. According to OpenAI's documentation, this makes ChatGPT's MCP support more accessible for non-technical users but limits it to remote servers only. Company knowledge now supports custom MCP connectors with search/fetch functionality.

**Key limitation:** No stdio support means ChatGPT cannot connect to local MCP servers. If your server only speaks stdio, you will need to wrap it with an HTTP transport layer or use a gateway like `mcp-proxy` or `supergateway`.

### Google Gemini

Google adopted MCP across multiple products through 2025-2026. According to Google's documentation, the Gemini CLI offers the most direct MCP configuration.

**Gemini CLI** reads MCP configuration from `settings.json`:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/docs"]
    },
    "remote-search": {
      "url": "https://mcp.example.com/search",
      "transport": "sse",
      "headers": {
        "Authorization": "Bearer ${SEARCH_API_KEY}"
      }
    }
  }
}
```

Gemini CLI also supports management commands:

```bash
gemini mcp add my-server -- npx -y @modelcontextprotocol/server-filesystem /path
gemini mcp list
gemini mcp remove my-server
```

**Gemini Cloud and Enterprise** support MCP through custom data store configurations, allowing organizations to connect Gemini to internal tools and databases via MCP servers. According to Google Cloud documentation, this includes support for OAuth 2.0 authentication for remote servers.

**Gemini SDK (Python/JS)** includes experimental MCP integration, allowing developers to build agents that connect to MCP servers programmatically:

```python
from google import genai
from google.genai import types

client = genai.Client()

# Connect to MCP tools through Gemini's tool configuration
tools = types.Tool(mcp_servers=[
    types.MCPServer(url="https://mcp.example.com/api")
])
```

**Supported transports:** stdio (CLI only), SSE, Streamable HTTP.

**Gemini API/SDK native MCP** — As of March-April 2026, MCP tool calls and built-in function calling can be combined in a single Gemini API request. According to Google's documentation, this allows grounding Gemini in internal data via MCP while keeping Google Search grounding active simultaneously, and the combined call is more token-efficient than two separate requests.

**Managed MCP servers** — Google released fully managed remote MCP servers for its services, providing a unified MCP layer across Google and Google Cloud services. According to Google Cloud documentation, additional services are rolling out through 2026, including Cloud Run, Cloud Storage, AlloyDB, Cloud SQL, Spanner, Looker, and Pub/Sub.

**Notable features:** According to published documentation, Gemini CLI supports environment variable interpolation in config files using `${VAR_NAME}` syntax, and the Cloud integration supports Google's existing IAM authentication alongside OAuth 2.0.

### Microsoft Copilot

Microsoft has integrated MCP across its Copilot product line. According to Microsoft's documentation, MCP support reached general availability in Copilot Studio in early 2025.

**Copilot Studio** provides a wizard-based setup for connecting MCP servers:

1. Navigate to Actions in Copilot Studio
2. Select "Add an MCP Server"
3. Enter the server URL (Streamable HTTP endpoint)
4. Configure authentication (OAuth 2.1, API key, or none)
5. Copilot Studio dynamically discovers available tools from the server

**VS Code Copilot** uses an `mcp.json` configuration file (typically in `.vscode/mcp.json`):

```json
{
  "servers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "${workspaceFolder}"]
    },
    "remote-tools": {
      "url": "https://mcp.example.com/api",
      "transport": "http"
    }
  }
}
```

**GitHub Copilot Chat** supports MCP through extensions, and **Microsoft 365 Copilot** enables MCP through declarative agent configurations, according to Microsoft's published guides.

**Supported transports:** stdio (VS Code only), SSE, Streamable HTTP.

**Notable features:** Dynamic tool and resource discovery is emphasized across all Copilot products — when you connect an MCP server, Copilot automatically detects what tools are available and presents them contextually. Copilot Studio also supports connecting multiple MCP servers simultaneously, with the platform routing requests to the appropriate server based on tool descriptions. As of early 2026, Copilot Studio's MCP integration includes enhanced tracing and analytics tools that show which MCP server and specific tool was invoked at runtime, improving debugging and observability. Microsoft's MCP Apps SDK has also expanded how agents connect to external work applications across the broader ecosystem.

### Amazon Q Developer

Amazon integrated MCP into Q Developer across CLI and cloud environments. According to AWS documentation, the integration supports both local development and cloud-scale deployment.

**Q Developer CLI** supports MCP configuration for local and remote servers:

```json
{
  "mcpServers": {
    "aws-docs": {
      "command": "npx",
      "args": ["-y", "@aws/mcp-server-aws-docs"]
    },
    "cdk-server": {
      "command": "npx",
      "args": ["-y", "@aws/mcp-server-cdk-explorer"],
      "env": {
        "AWS_PROFILE": "dev"
      }
    }
  }
}
```

**Amazon Bedrock AgentCore** provides managed MCP server hosting, according to AWS documentation. This allows organizations to deploy MCP servers as stateful services within AWS infrastructure, with support for:

- Automatic scaling across requests
- Session persistence for stateful interactions
- Integration with AWS IAM for authentication
- Availability across 14 AWS regions

**Supported transports:** stdio, SSE, Streamable HTTP.

**Notable features:** According to AWS's published documentation, Q Developer supports MCP elicitation (servers can request additional input from users mid-interaction), sampling (servers can request LLM completions), and progress notifications (servers can report task progress back to the client). The Bedrock AgentCore integration also means MCP servers can be deployed once and accessed by multiple agents and applications.

**Recent additions (March-April 2026):** Bedrock AgentCore Runtime now supports stateful MCP server features, including elicitation, sampling, and progress notifications alongside existing resource, prompt, and tool support — available across 14 AWS regions. AgentCore also added AG-UI (Agent-User Interaction) protocol support for real-time agent experiences, complementing MCP and A2A. The new **AWS Agent Registry** (preview) provides a private, governed catalog for discovering agents, tools, skills, and MCP servers within an organization, accessible via console, CLI, SDK, or as an MCP server queryable from IDEs.

## Platform Comparison

| Platform | Config Format | Transports | Auth | Local Servers | Remote Servers | Notable Feature |
|----------|--------------|------------|------|---------------|----------------|-----------------|
| Claude Desktop | JSON config file | stdio, SSE, HTTP | Env vars, headers | Yes | Yes | Broadest MCP feature support |
| Claude Code | CLI + .mcp.json | stdio, SSE, HTTP | Env vars, headers | Yes | Yes | Project-level sharing via .mcp.json |
| ChatGPT | Platform registration | SSE, HTTP | OAuth 2.1 | No | Yes | Built-in user-facing OAuth flow |
| OpenAI Responses API | API code | SSE, HTTP | OAuth, headers | No | Yes | Native MCP in API, no extra cost |
| OpenAI Agents SDK | Python code | SSE, HTTP | Headers, OAuth | No | Yes | Programmatic agent composition |
| Gemini CLI | settings.json | stdio, SSE, HTTP | Env vars, OAuth 2.0 | Yes | Yes | Env var interpolation in config |
| Gemini Cloud | Cloud console | SSE, HTTP | Google IAM, OAuth | No | Yes | Enterprise data store integration |
| Copilot Studio | Wizard UI | SSE, HTTP | OAuth 2.1, API key | No | Yes | Dynamic tool discovery UI |
| VS Code Copilot | mcp.json | stdio, SSE, HTTP | Env vars, headers | Yes | Yes | Workspace-scoped config |
| Amazon Q CLI | JSON config | stdio, SSE, HTTP | Env vars, IAM | Yes | Yes | Elicitation and sampling support |
| Bedrock AgentCore | AWS console/SDK | SSE, HTTP | AWS IAM | No | Yes | Managed stateful MCP hosting |

## Cross-Platform Configuration Tips

If you are building MCP servers intended for broad compatibility, several patterns emerge from the documentation across platforms.

**Design for Streamable HTTP first.** stdio works well for local desktop and CLI clients, but web platforms like ChatGPT and Copilot Studio cannot launch local processes. Building your server with Streamable HTTP as the primary transport ensures it works everywhere. You can add stdio as a secondary transport for local development convenience.

**Implement OAuth 2.1 for authentication.** ChatGPT requires OAuth 2.1, Copilot Studio supports it natively, and the MCP specification recommends it for remote servers. According to the MCP auth specification, servers should implement the full OAuth 2.1 authorization code flow with PKCE for maximum compatibility.

**Write clear, specific tool descriptions.** Every platform uses tool descriptions for discovery and routing. According to documentation from multiple vendors, vague descriptions like "manages data" lead to poor tool selection by the AI. Specific descriptions like "Creates a new row in a PostgreSQL database table, accepting column names and values as parameters" help every platform route requests correctly.

**Test with MCP Inspector before deploying.** The [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) is an interactive debugging tool that lets you connect to any MCP server and verify its tools, resources, and prompts work correctly. According to the MCP project documentation, running `npx @modelcontextprotocol/inspector` launches a web UI for testing servers before connecting them to any platform.

**Use environment variables for secrets.** All platforms that support local servers allow environment variable injection in configuration files. Never hardcode API keys, database credentials, or tokens in MCP config files — use `env` blocks or platform-specific variable syntax instead.

**Consider Docker for portable deployment.** Packaging MCP servers as Docker containers solves dependency management across platforms. See our [guide to running MCP servers in Docker](/guides/mcp-docker-containers/) for detailed patterns.

## Common Pitfalls

**stdio servers won't work with web platforms.** This is the most common source of confusion based on community reports. If you build a server that only speaks stdio, it will work with Claude Desktop, Claude Code, Gemini CLI, VS Code Copilot, and Amazon Q CLI — but not with ChatGPT, Copilot Studio, or any cloud-hosted platform. Tools like `mcp-proxy` and `supergateway` can bridge this gap by wrapping a stdio server with an HTTP transport.

**Auth requirements differ significantly.** ChatGPT requires OAuth 2.1 with specific redirect URI patterns. Copilot Studio supports OAuth 2.1 and API keys. Claude Desktop typically uses environment variables for API keys. Amazon Q in AWS uses IAM roles. If you are building a server for multiple platforms, you may need to support multiple authentication methods.

**Tool naming conventions may cause issues.** According to the MCP specification, tool names should use lowercase with underscores (e.g., `read_file`). Some platforms may handle camelCase or other conventions differently. Sticking to the specification's naming convention avoids surprises.

**Rate limits vary by platform and plan.** Each platform imposes its own limits on how frequently MCP tools can be called. Enterprise plans typically offer higher limits. According to published documentation, these limits apply on top of any rate limits your MCP server itself enforces — a tool call must pass both the platform's limits and the server's limits.

**Config file locations are platform-specific.** Each platform stores its MCP configuration in a different location. When troubleshooting connection issues, verify you are editing the correct config file for the platform you are using.

## What's Coming

The MCP ecosystem continues to evolve rapidly. The official [2026 MCP Roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) identifies four strategic priority areas, and the maintainer team recently expanded — Den Delimarsky (Anthropic) was promoted to Lead Maintainer alongside David Soria Parra, and Clare Liguori (AWS) joined as Core Maintainer.

**Transport evolution** — The roadmap prioritizes improving Streamable HTTP for horizontal scaling and stateless operation, rather than adding new transports. A standard metadata format via `.well-known` endpoints is planned for capability discovery without requiring live connections — addressing a key pain point for enterprises operating at scale.

**Agent communication** — Building on the experimental Tasks feature (SEP-1686), the focus is production-readiness: retry semantics for transient failures and expiry policies for result retention. The AG-UI (Agent-to-Agent) protocol, already supported by AWS Bedrock AgentCore, complements MCP by standardizing how agents communicate with user interfaces and each other.

**MCP Apps** — An emerging pattern where MCP servers can return UI components (not just data) for rendering in client applications. According to MCP specification discussions, this would allow servers to provide rich interactive interfaces alongside their tools.

**Multimodal support** — The MCP specification is expanding to support image, audio, and video data in tool inputs and outputs. Several platforms have indicated support for multimodal MCP in their roadmaps.

**Enterprise readiness** — Audit trails, SSO-integrated auth, gateway behavior, and configuration portability are the main enterprise pain points identified in the roadmap. According to the MCP team, most solutions will ship as extensions rather than core protocol changes, to avoid burdening all users. Managed MCP hosting from Google Cloud and AWS Bedrock AgentCore is already addressing some of these needs.

**Governance maturation** — A Contributor Ladder is being developed to define progression from community participant to lead maintainer, and Working Groups are being empowered to review domain-specific SEPs independently. The first MCP Dev Summit North America took place in New York City (April 2-3, 2026) with over 95 sessions, and MCP Dev Summit Europe is scheduled for Amsterdam (September 17-18, 2026).

## Conclusion

MCP has matured from a single-vendor protocol into the industry standard for connecting AI systems to tools and data. With adoption from Anthropic, OpenAI, Google, Microsoft, and Amazon — and governance under the Linux Foundation — building MCP servers represents a stable investment.

The practical reality matches the promise: a well-built MCP server with Streamable HTTP transport and OAuth 2.1 authentication works across all major platforms today. The configuration differs per platform, but the server code stays the same. For teams building AI-powered tools and integrations, MCP eliminates the need to build separate integrations for each AI vendor.

Start with one server, one transport (Streamable HTTP), and one platform. Once it works, adding additional platforms is a configuration exercise — not a development project.

---

*This guide is part of [ChatForest's MCP resource library](/guides/). ChatForest is an AI-native content site — our guides are researched and written by AI, reviewed for accuracy by [Rob Nugen](https://www.robnugen.com/). Last refreshed: April 2026.*

