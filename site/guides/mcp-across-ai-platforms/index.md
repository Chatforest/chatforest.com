# Using MCP Across AI Platforms: Claude, ChatGPT, Gemini, Copilot, and More

> How to use MCP servers with every major AI platform — covers Claude Desktop and Code, ChatGPT Apps and Agents SDK, Google Gemini CLI and Cloud, Microsoft Copilot Studio, Amazon Q


When [Anthropic open-sourced the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) in November 2024, MCP was a single-vendor affair. That changed fast. OpenAI, Google, Microsoft, and Amazon have all adopted MCP, and in December 2025 the protocol moved under the Linux Foundation's [Agentic AI Foundation (AAIF)](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/) — a directed fund [co-founded by Anthropic, Block, and OpenAI, with support from Google, Microsoft, AWS, Cloudflare, and Bloomberg](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) — as a vendor-neutral standard. At the time of that move, Anthropic [reported over 10,000 active MCP servers and 97 million monthly SDK downloads](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/), spanning individual developer tools to enterprise deployments — a clear signal that MCP has moved from experiment to infrastructure.

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

Claude was the first platform to support MCP — Anthropic created and open-sourced the protocol — and [Anthropic's documentation](https://code.claude.com/docs/en/mcp) describes broad transport support across its products.

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

The config file location varies by OS — `~/Library/Application Support/Claude/` on macOS and `%APPDATA%\Claude\` on Windows, per [Anthropic's MCP quickstart documentation](https://modelcontextprotocol.io/quickstart/user). Claude Desktop reached Linux (Ubuntu/Debian) as an [official beta in June 2026](https://support.claude.com/en/articles/10065433-install-claude-desktop), using `~/.config/Claude/`.

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

**Notable features:** Claude supports resource subscriptions and prompt templates. Note that [MCP sampling and logging (client primitives that let a server request LLM completions or send log messages) were marked deprecated in the protocol's 2026-07-28 specification revision](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture) — new server implementations are directed to integrate with LLM provider APIs directly instead, though many existing servers still implement the older pattern. On the output side, [Claude Code's default MCP output limit is 25,000 tokens (configurable via `MAX_MCP_OUTPUT_TOKENS`), and individual tools can raise their own result-size ceiling up to a hard cap of 500,000 characters](https://code.claude.com/docs/en/mcp) by declaring `_meta["anthropic/maxResultSizeChars"]` in their tool definition — useful for tools that return large but necessary output like full database schemas. [Claude Cowork](https://claude.com/product/cowork), Anthropic's agentic desktop workspace, launched in [research preview on macOS for Max subscribers in January 2026](https://techcrunch.com/2026/01/12/anthropics-new-cowork-tool-offers-claude-code-without-the-code/) and reached [Windows with full feature parity in February 2026](https://www.unite.ai/anthropic-brings-claude-cowork-to-windows-with-full-feature-parity/).

### OpenAI ChatGPT

[OpenAI announced MCP support in March 2025](https://x.com/OpenAIDevs/status/1904957755829481737), starting with the Agents SDK immediately and flagging ChatGPT desktop and Responses API support as "coming soon" — [confirmed by contemporaneous reporting](https://techcrunch.com/2025/03/26/openai-adopts-rival-anthropics-standard-for-connecting-ai-models-to-data/). Remote MCP servers followed in the [Responses API in May 2025](https://openai.com/index/new-tools-and-features-in-the-responses-api/), with ChatGPT's own connector UI rolling out afterward through 2025 and into 2026. ChatGPT's MCP implementation is remote-first — a meaningful architectural difference from Claude's local-first approach.

**ChatGPT Apps via MCP** allow developers to register remote MCP servers through the OpenAI platform. Users can then add these servers to their ChatGPT sessions. According to [OpenAI's help center documentation](https://help.openai.com/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt):

- ChatGPT connects only to remote HTTPS MCP servers via SSE or Streamable HTTP, with OAuth-based authentication
- Custom MCP connectors (via Developer Mode) are available on Plus, Pro, Business, Enterprise, and Edu plans — not the free tier
- Full read+write tool access is in beta and is scoped by workspace admin settings on Business/Enterprise/Edu plans

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

**OpenAI Responses API** [includes native support for remote MCP servers](https://openai.com/index/new-tools-and-features-in-the-responses-api/), allowing developers to connect models to any MCP server with just a few lines of code. Per [OpenAI's API documentation](https://developers.openai.com/api/docs/guides/tools-connectors-mcp), there is no separate fee for the MCP tool itself — usage is billed at the model's standard input/output token rates. The **Realtime API** also [supports MCP by passing a remote server URL into the session configuration](https://developers.openai.com/api/docs/guides/realtime-mcp).

**MCP Connectors** — [OpenAI has rolled out a catalog of partner-built MCP connectors reviewed by OpenAI](https://help.openai.com/en/articles/11391654-chatgpt-business-release-notes), including Amplitude, Fireflies, Vercel, Monday.com, Stripe, and Hex, with Atlassian Rovo (Jira, Confluence) added separately. These are available to Enterprise, Edu, Business, Pro, and Plus customers.

**Notable features:** A built-in OAuth flow means users authenticate with MCP servers through ChatGPT's UI rather than manually managing API keys — accessible for non-technical users, but limited to remote servers only. [Company knowledge / Developer Mode supports custom MCP connectors](https://help.openai.com/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt) with search/fetch tool functionality.

**Key limitation:** No stdio support means ChatGPT cannot connect to local MCP servers. If your server only speaks stdio, you will need to wrap it with an HTTP transport layer or use a gateway like `mcp-proxy` or `supergateway`.

### Google Gemini

Google adopted MCP across multiple products through 2025-2026. The [Gemini CLI's own docs](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md) offer the most direct MCP configuration reference.

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

**Gemini Cloud and Enterprise** support MCP through custom data store configurations, allowing organizations to connect Gemini to internal tools and databases via MCP servers, per [Google Cloud's grounding documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-your-search-api).

**Gemini SDK (Python/JS)** [includes built-in MCP support](https://ai.google.dev/gemini-api/docs/function-calling), allowing developers to build agents that connect to MCP servers programmatically — the SDK can automatically execute an MCP tool call the model generates and feed the result back in a follow-up request:

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

**Gemini API/SDK native MCP** — The [Python and JavaScript client SDKs automatically execute MCP tool calls](https://ai.google.dev/gemini-api/docs/function-calling) the model generates and loop the result back to the model, reducing the boilerplate of wiring MCP into a custom agent loop. One caveat worth noting: Google's own docs state that [the Gemini API does not support combining a built-in search tool (like Google Search grounding) with custom function declarations in the same request](https://ai.google.dev/gemini-api/docs/google-search) — so MCP tools and Search grounding are not simultaneously active in a single call.

**Managed MCP servers** — Google has released [more than 50 fully managed remote MCP servers, generally available or in preview](https://cloud.google.com/blog/products/ai-machine-learning/google-managed-mcp-servers-are-available-for-everyone), spanning Cloud Run, Google Cloud Storage, AlloyDB, Cloud SQL, Spanner, Pub/Sub, BigQuery, GKE, and more, plus a separate [Looker-managed MCP server currently in preview](https://docs.cloud.google.com/looker/docs/mcp).

**Notable features:** Per the [Gemini CLI's documentation](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md), it supports environment variable interpolation in config files using `${VAR_NAME}` syntax.

### Microsoft Copilot

Microsoft has integrated MCP across its Copilot product line. [MCP integration in Copilot Studio reached general availability on May 29, 2025](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/model-context-protocol-mcp-is-now-generally-available-in-microsoft-copilot-studio/), per Microsoft's own announcement.

**Copilot Studio** provides a wizard-based setup for connecting MCP servers:

1. Navigate to Actions in Copilot Studio
2. Select "Add an MCP Server"
3. Enter the server URL (Streamable HTTP endpoint)
4. Configure authentication (OAuth 2.1, API key, or none)
5. Copilot Studio dynamically discovers available tools from the server

**VS Code Copilot** uses an [`mcp.json` configuration file](https://code.visualstudio.com/docs/agent-customization/mcp-servers) (typically in `.vscode/mcp.json`):

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

**GitHub Copilot Chat** [supports MCP servers configured manually or installed through the GitHub MCP Registry](https://docs.github.com/copilot/customizing-copilot/using-model-context-protocol/extending-copilot-chat-with-mcp), and **Microsoft 365 Copilot** [enables MCP through declarative agent configurations](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/build-mcp-plugins), which Microsoft says reached general availability in that product.

**Supported transports:** stdio (VS Code only), SSE, Streamable HTTP.

**Notable features:** Dynamic tool and resource discovery is emphasized across all Copilot products — when you connect an MCP server, Copilot automatically detects what tools are available and presents them contextually. Copilot Studio also supports connecting multiple MCP servers simultaneously, with the platform routing requests to the appropriate server based on tool descriptions. As of [April 2026, Copilot Studio's MCP integration includes enhanced tracing and analytics that show which MCP server and specific tool was invoked at runtime](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/new-and-improved-agent-governance-intelligent-workflows-and-connected-app-experiences/), improving debugging and observability. Separately, [MCP Apps — a cross-vendor extension co-developed with OpenAI that lets MCP servers return interactive UI components — became available in Microsoft 365 Copilot chat](https://devblogs.microsoft.com/microsoft365dev/mcp-apps-now-available-in-copilot-chat/) in 2026.

### Amazon Q Developer

Amazon integrated MCP into Q Developer across CLI and cloud environments. [AWS's Bedrock AgentCore documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html) covers both local development and cloud-scale deployment.

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

**Amazon Bedrock AgentCore** provides [managed MCP server hosting](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html). This allows organizations to deploy MCP servers as stateful services within AWS infrastructure, with support for:

- Automatic scaling across requests
- Session persistence for stateful interactions
- Integration with AWS IAM for authentication
- [Stateful MCP features available in 14 AWS regions as of the March 2026 launch](https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-bedrock-agentcore-runtime-stateful-mcp/) — AgentCore's overall regional footprint has continued to expand since ([São Paulo added in May 2026](https://aws.amazon.com/about-aws/whats-new/2026/05/agentcore-sao-paulo-region/) and [four more regions added mid-2026](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-four-additional-regions/)), so check AWS's current region table for the up-to-date count

**Supported transports:** stdio, SSE, Streamable HTTP.

**Notable features:** [AWS documentation describes Q Developer's MCP support for elicitation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/mcp-stateful-features.html) (servers can request additional input from users mid-interaction), sampling (servers can request LLM completions), and progress notifications (servers can report task progress back to the client) — note that sampling and logging were marked deprecated in the MCP protocol's 2026-07-28 specification revision, though AWS's stateful-MCP feature set (built to the prior spec) still documents them. The Bedrock AgentCore integration also means MCP servers can be deployed once and accessed by multiple agents and applications.

**Recent additions (March-April 2026):** [Bedrock AgentCore Runtime added stateful MCP server features](https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-bedrock-agentcore-runtime-stateful-mcp/) — elicitation, sampling, and progress notifications alongside existing resource, prompt, and tool support. AgentCore also [added AG-UI (Agent-User Interaction) protocol support](https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-bedrock-agentcore-runtime-ag-ui-protocol) for real-time agent experiences; AG-UI standardizes how agents communicate with user-facing interfaces, distinct from the separate [A2A (Agent2Agent) protocol](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/) that AgentCore uses for agent-to-agent communication. The [**AWS Agent Registry** (preview)](https://aws.amazon.com/blogs/machine-learning/the-future-of-managing-agents-at-scale-aws-agent-registry-now-in-preview/) provides a private, governed catalog for discovering agents, tools, skills, and MCP servers within an organization, accessible via console, CLI, SDK, or a native MCP endpoint.

## Platform Comparison

| Platform | Config Format | Transports | Auth | Local Servers | Remote Servers | Notable Feature |
|----------|--------------|------------|------|---------------|----------------|-----------------|
| Claude Desktop | JSON config file | stdio, SSE, HTTP | Env vars, headers | Yes | Yes | Broadest MCP feature support |
| Claude Code | CLI + .mcp.json | stdio, SSE, HTTP | Env vars, headers | Yes | Yes | Project-level sharing via .mcp.json |
| ChatGPT | Platform registration | SSE, HTTP | OAuth | No | Yes | Built-in user-facing OAuth flow |
| OpenAI Responses API | API code | SSE, HTTP | OAuth, headers | No | Yes | Native MCP in API, no extra tool fee |
| OpenAI Agents SDK | Python code | SSE, HTTP | Headers, OAuth | No | Yes | Programmatic agent composition |
| Gemini CLI | settings.json | stdio, SSE, HTTP | Env vars, OAuth | Yes | Yes | Env var interpolation in config |
| Gemini Cloud | Cloud console | SSE, HTTP | Google IAM, OAuth | No | Yes | Enterprise data store integration |
| Copilot Studio | Wizard UI | SSE, HTTP | OAuth 2.1, API key | No | Yes | Dynamic tool discovery UI |
| VS Code Copilot | mcp.json | stdio, SSE, HTTP | Env vars, headers | Yes | Yes | Workspace-scoped config |
| Amazon Q CLI | JSON config | stdio, SSE, HTTP | Env vars, IAM | Yes | Yes | Elicitation and sampling support |
| Bedrock AgentCore | AWS console/SDK | SSE, HTTP | AWS IAM | No | Yes | Managed stateful MCP hosting |

## Cross-Platform Configuration Tips

If you are building MCP servers intended for broad compatibility, several patterns emerge from the documentation across platforms.

**Design for Streamable HTTP first.** stdio works well for local desktop and CLI clients, but web platforms like ChatGPT and Copilot Studio cannot launch local processes. Building your server with Streamable HTTP as the primary transport ensures it works everywhere. You can add stdio as a secondary transport for local development convenience.

**Implement OAuth for authentication.** ChatGPT requires OAuth-based authentication for its connectors, Copilot Studio supports OAuth 2.1 natively, and [the MCP authorization specification requires OAuth 2.1 with PKCE](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) for remote servers — implementing the full OAuth 2.1 authorization code flow with PKCE gives the broadest compatibility.

**Write clear, specific tool descriptions.** Every platform uses tool descriptions for discovery and routing. According to documentation from multiple vendors, vague descriptions like "manages data" lead to poor tool selection by the AI. Specific descriptions like "Creates a new row in a PostgreSQL database table, accepting column names and values as parameters" help every platform route requests correctly.

**Test with MCP Inspector before deploying.** The [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) is an interactive debugging tool that lets you connect to any MCP server and verify its tools, resources, and prompts work correctly. According to the MCP project documentation, running `npx @modelcontextprotocol/inspector` launches a web UI for testing servers before connecting them to any platform.

**Use environment variables for secrets.** All platforms that support local servers allow environment variable injection in configuration files. Never hardcode API keys, database credentials, or tokens in MCP config files — use `env` blocks or platform-specific variable syntax instead.

**Consider Docker for portable deployment.** Packaging MCP servers as Docker containers solves dependency management across platforms. See our [guide to running MCP servers in Docker](/guides/mcp-docker-containers/) for detailed patterns.

## Common Pitfalls

**stdio servers won't work with web platforms.** This is the most common source of confusion based on community reports. If you build a server that only speaks stdio, it will work with Claude Desktop, Claude Code, Gemini CLI, VS Code Copilot, and Amazon Q CLI — but not with ChatGPT, Copilot Studio, or any cloud-hosted platform. Tools like `mcp-proxy` and `supergateway` can bridge this gap by wrapping a stdio server with an HTTP transport.

**Auth requirements differ significantly.** ChatGPT requires OAuth-based authentication with specific redirect URI patterns for its connectors. Copilot Studio supports OAuth 2.1 and API keys. Claude Desktop typically uses environment variables for API keys. Amazon Q in AWS uses IAM roles. If you are building a server for multiple platforms, you may need to support multiple authentication methods.

**Tool naming conventions may cause issues.** The [MCP specification (SEP-986) permits tool names 1–64 characters using alphanumerics, underscores, dashes, dots, and slashes](https://modelcontextprotocol.io/seps/986-specify-format-for-tool-names) — it doesn't mandate lowercase-with-underscores, but that pattern (e.g., `read_file`) is the de facto convention across reference implementations and the Python/JS SDKs. Some platforms may handle camelCase or other conventions differently, so sticking to the common convention avoids surprises.

**Rate limits vary by platform and plan.** Each platform imposes its own limits on how frequently MCP tools can be called. Enterprise plans typically offer higher limits. According to published documentation, these limits apply on top of any rate limits your MCP server itself enforces — a tool call must pass both the platform's limits and the server's limits.

**Config file locations are platform-specific.** Each platform stores its MCP configuration in a different location. When troubleshooting connection issues, verify you are editing the correct config file for the platform you are using.

## What's Coming

The MCP ecosystem continues to evolve rapidly. The official [2026 MCP Roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) identifies four strategic priority areas, and the maintainer team recently expanded — [Den Delimarsky (Anthropic) was promoted to Lead Maintainer alongside David Soria Parra, and Clare Liguori (AWS) joined as Core Maintainer](https://blog.modelcontextprotocol.io/posts/2026-04-08-maintainer-update/).

**Transport evolution** — The roadmap prioritizes improving Streamable HTTP for horizontal scaling and stateless operation, rather than adding new transports. A standard metadata format via `.well-known` endpoints is planned for capability discovery without requiring live connections — addressing a key pain point for enterprises operating at scale.

**Agent communication** — Building on the experimental [Tasks feature (SEP-1686)](https://modelcontextprotocol.io/seps/1686-tasks), the focus is production-readiness: retry semantics for transient failures and expiry policies for result retention. Note this is distinct from AG-UI (Agent-User Interaction) and A2A (Agent2Agent) — separate protocols, not part of MCP itself, that AWS Bedrock AgentCore [also supports](https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-bedrock-agentcore-runtime-ag-ui-protocol) for agent-to-UI and agent-to-agent communication respectively.

**MCP Apps** — An emerging pattern where MCP servers can return UI components (not just data) for rendering in client applications, [now live in Microsoft 365 Copilot chat](https://devblogs.microsoft.com/microsoft365dev/mcp-apps-now-available-in-copilot-chat/) among other clients.

**Multimodal support** — The MCP specification is expanding to support image, audio, and video data in tool inputs and outputs. Several platforms have indicated support for multimodal MCP in their roadmaps.

**Enterprise readiness** — Audit trails, SSO-integrated auth, gateway behavior, and configuration portability are the main enterprise pain points identified in the [roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/). The roadmap indicates most solutions will ship as extensions rather than core protocol changes, to avoid burdening all users. Managed MCP hosting from Google Cloud and AWS Bedrock AgentCore is already addressing some of these needs.

**Governance maturation** — A Contributor Ladder is being developed to define progression from community participant to lead maintainer, and Working Groups are being empowered to review domain-specific SEPs independently. The [first MCP Dev Summit North America took place in New York City (April 2-3, 2026) with over 95 sessions](https://events.linuxfoundation.org/2026/02/24/agentic-ai-foundation-unveils-mcp-dev-summit-north-america-2026-schedule/), and MCP Dev Summit Europe is scheduled for Amsterdam (September 17-18, 2026).

## Conclusion

MCP has matured from a single-vendor protocol into the industry standard for connecting AI systems to tools and data. With adoption from Anthropic, OpenAI, Google, Microsoft, and Amazon — and governance under the Linux Foundation — building MCP servers represents a stable investment.

The practical reality matches the promise: a well-built MCP server with Streamable HTTP transport and OAuth 2.1 authentication works across all major platforms today. The configuration differs per platform, but the server code stays the same. For teams building AI-powered tools and integrations, MCP eliminates the need to build separate integrations for each AI vendor.

Start with one server, one transport (Streamable HTTP), and one platform. Once it works, adding additional platforms is a configuration exercise — not a development project.

---

*This guide is part of [ChatForest's MCP resource library](/guides/). ChatForest is an AI-native content site — our guides are researched and written by AI, reviewed for accuracy by [Rob Nugen](https://www.robnugen.com/). Last refreshed: April 2026.*

