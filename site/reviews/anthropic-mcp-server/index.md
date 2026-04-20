# Anthropic MCP Servers — The Company That Created the Model Context Protocol

> Anthropic created MCP in November 2024 and maintains the reference servers, SDKs, and specification. Claude Desktop, Claude Code, and Claude.ai are the most mature MCP clients.


**At a glance:** [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) (81.8k stars, 10k forks, 7 active reference servers) + [Python SDK](https://github.com/modelcontextprotocol/python-sdk) (22.3k stars) + [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) (11.9k stars). Anthropic **invented MCP** in November 2024 and operates the most comprehensive MCP ecosystem: reference servers, official SDKs in 10+ languages, the protocol specification, and the most mature MCP client support across Claude.ai, Claude Desktop, Claude Code, and the API. Part of our **[AI Providers MCP category](/categories/ai-providers/)**.

Anthropic MCP servers provide the **reference implementations** that define how MCP servers should work — file system access, Git operations, web fetching, persistent memory, and sequential reasoning. These aren't wrappers around the Claude API (Anthropic's products ARE the MCP clients). Instead, they're the foundational tools that demonstrate what MCP can do and how to build servers correctly.

[Anthropic](https://www.anthropic.com/) was founded in 2021 by **Dario Amodei** and **Daniela Amodei**, along with several former OpenAI researchers. As of early 2026: approximately **$19 billion annualized revenue** (up from $9B at end of 2025), **$380 billion valuation** (February 2026 Series G, $30B raised), **300,000+ business customers**, Claude Code alone generating **$2.5 billion annualized revenue**, and approximately **3,000 employees**. Key products include Claude (Opus 4.6, Sonnet 4.6, Haiku 4.5), Claude Code, Claude Desktop, and the Messages/Responses API.

**Architecture note:** Anthropic's MCP role is unique: they are both the **protocol creator** and the **leading MCP client**. Unlike OpenAI (primarily a client), Google (official remote servers), or Microsoft (enterprise MCP servers), Anthropic designed the entire protocol, maintains the specification, provides the SDKs, and built the most capable MCP client implementations. They donated MCP to the [Agentic AI Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) (Linux Foundation) in December 2025, co-founded with OpenAI and Block.

## What It Does

Anthropic maintains 7 active reference servers that demonstrate core MCP capabilities:

### Development Tools

| Server | What It Does |
|--------|-------------|
| Git | Read, search, and manipulate Git repositories — diffs, logs, commits, branches |
| Filesystem | Secure file operations with configurable access controls — read, write, move, search |
| Fetch | Fetch web content and convert to LLM-friendly formats (HTML → Markdown) |

### Reasoning & Memory

| Server | What It Does |
|--------|-------------|
| Memory | Knowledge graph-based persistent memory — entities, relations, observations |
| Sequential Thinking | Dynamic, reflective problem-solving through structured thought sequences |

### Utilities

| Server | What It Does |
|--------|-------------|
| Time | Time and timezone conversion across IANA zones |
| Everything | Reference/test server demonstrating all MCP features — prompts, resources, tools |

### Archived Reference Servers (14)

Anthropic originally maintained 14 additional reference servers that were **archived on May 29, 2025** at [modelcontextprotocol/servers-archived](https://github.com/modelcontextprotocol/servers-archived) (237 stars, 141 forks, 2,572 commits, 21 contributors). These were moved as the ecosystem matured and independent maintainers took over:

| Server | What It Did |
|--------|------------|
| AWS KB Retrieval | Amazon Bedrock knowledge base access |
| Brave Search | Web search via Brave Search API |
| EverArt | AI image generation |
| GitHub | GitHub API operations |
| GitLab | GitLab API operations |
| Google Drive | Google Drive file access |
| Google Maps | Google Maps geocoding and directions |
| PostgreSQL | Database queries with schema inspection |
| Puppeteer | Browser automation |
| Redis | Redis database operations |
| Sentry | Error tracking access |
| Slack | Slack workspace integration |
| SQLite | SQLite database operations |

**No security guarantees** apply to archived servers. They receive no maintenance or bug fixes.

## Anthropic as MCP Client

Anthropic operates the **most comprehensive MCP client ecosystem** — every Claude product supports MCP:

### Claude.ai (Web + Mobile)

- Add MCP servers via Settings → Connectors
- Official **Connectors Directory** with vetted integrations (Asana, Box, Figma, Linear, Slack, etc.)
- Supports read AND write operations
- Available on all Claude.ai plans (Free, Pro, Team, Enterprise)
- **MCP Apps** — interactive UI rendered inside the chat window (project boards, dashboards, canvases)

### Claude Desktop (macOS + Windows)

- Local MCP servers via `claude_desktop_config.json`
- **Desktop Extensions** (.mcpb files) — one-click MCP server installation bundling all dependencies
- Admin controls for Team/Enterprise: enable/disable extensions, upload custom extensions, manage registries
- Anthropic open-sourced the Desktop Extension specification and toolchain

### Claude Code (CLI)

- Configure MCP servers via `.mcp.json` files (project-level or global)
- If logged in with Claude.ai account, Connectors are automatically available
- Supports local stdio servers and remote Streamable HTTP servers
- MCP servers extend Claude Code's capabilities with custom tools

### API (Messages + MCP Connector)

- `mcp_servers` parameter for remote MCP servers accessible via URL
- **MCP Connector** beta — connect to remote servers directly from API calls
- No extra cost for MCP tool calls beyond standard token billing
- Supports Streamable HTTP transport

## MCP SDKs

Anthropic created and maintains the official SDKs that power the entire MCP ecosystem:

### Python SDK

- **GitHub:** [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) — 22.3k stars, 3.2k forks
- **License:** MIT
- **FastMCP** framework for simplified server creation with decorator-based API
- Type-safe context injection, Pydantic validation, progress reporting
- Supports stdio, SSE, and Streamable HTTP transports
- OAuth authentication support
- v2 pre-alpha in development; stable v1.x branch for production

### TypeScript SDK

- **GitHub:** [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) — 11.9k stars, 1.7k forks, 161 contributors, 1,403 commits, 80 releases
- **License:** MIT / Apache 2.0 (dual)
- v1.27.1 (February 2026); v2 pre-alpha on main branch
- Cross-runtime support: Node.js, Bun, Deno
- Framework middleware for Express, Hono, and Node.js HTTP
- Zod v4 for schema validation
- v1.x receiving bug fixes and security updates for 6+ months after v2 ships

### Additional SDKs

Official or community-maintained SDKs also exist for **C#, Go, Java, Kotlin, PHP, Ruby, Rust, and Swift** — making MCP accessible across virtually every major programming language.

## MCP Governance

Anthropic donated MCP to the **Agentic AI Foundation (AAIF)** in December 2025:

| Aspect | Detail |
|--------|--------|
| Foundation | Agentic AI Foundation, directed fund under the Linux Foundation |
| Co-founders | Anthropic, Block, OpenAI |
| Platinum members | Amazon Web Services, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI |
| Donated projects | MCP (Anthropic), goose (Block), AGENTS.md (OpenAI) |
| Governance | Governing Board makes strategic decisions; individual projects maintain technical autonomy |

## Claude API Pricing

| Model | Input (per 1M tokens) | Cached Input | Output (per 1M tokens) | Context Window |
|-------|----------------------|--------------|----------------------|----------------|
| Haiku 4.5 | $1.00 | $0.10 | $5.00 | 200K |
| Sonnet 4.6 | $3.00 | $0.30 | $15.00 | 200K |
| Sonnet 4.6 (>200K input) | $6.00 | $0.60 | $22.50 | 1M |
| Opus 4.6 | $5.00 | $0.50 | $25.00 | 1M |

| Cost Optimization | Discount |
|-------------------|----------|
| Prompt caching (5-min) | Writes 1.25x, reads 0.1x base price |
| Prompt caching (1-hour) | Writes 2x, reads 0.1x base price |
| Batch API | 50% off all models |

**Claude subscriptions:**
- Claude Free — limited access, supports MCP Connectors
- Claude Pro — $20/month
- Claude Team — $25/user/month
- Claude Enterprise — custom pricing
- Claude Code — $20/month (Max: usage-based, ~$100-200/month typical)

**Note:** MCP tool calls incur standard token billing — there's no MCP-specific surcharge. The tool definitions and results count toward your input/output tokens.

## Known Issues

1. **No MCP server wrapping the Claude API** — Anthropic focuses on the client side. There is no official MCP server that lets other AI agents (GPT, Gemini) call Claude via MCP. Community implementations like [mnthe/claude-agent-mcp-server](https://github.com/mnthe/claude-agent-mcp-server) (0 stars, 43 commits, TypeScript) exist but have minimal adoption.

2. **Archived reference servers cause confusion** — The 14 original reference servers (Google Drive, Slack, GitHub, Postgres, etc.) were archived May 2025 with no security guarantees. Tutorials and blog posts still reference them, leading developers to use unmaintained code in production.

3. **Git MCP server security flaws** — Anthropic's official Git reference server was [found to have security vulnerabilities](https://www.techradar.com/pro/security/anthropics-official-git-mcp-server-had-some-worrying-security-flaws-this-is-what-happened-next) that could allow command injection. While addressed, this highlighted the risks of reference servers being treated as production-ready.

4. **Desktop Extension ecosystem is young** — The .mcpb format was introduced recently and the extension ecosystem is still growing. Most MCP servers are still installed manually via config files rather than one-click extensions.

5. **Connector availability varies by plan** — While all Claude.ai plans support MCP Connectors, the Connectors Directory and admin controls differ between Free, Pro, Team, and Enterprise tiers. Some connectors require Team or Enterprise plans.

6. **SDK version fragmentation** — Both Python and TypeScript SDKs have v2 pre-alpha on main branches while v1.x remains the stable production version. Developers must be careful to use the correct branch. Breaking changes expected in v2 (e.g., Zod v4 requirement in TypeScript SDK).

7. **MCP specification still evolving** — New features like MCP Apps, Elicitation (servers requesting structured input mid-task), and the Apps Extension (SEP-1865, co-developed with OpenAI) are being added. Servers built against older spec versions may need updates.

8. **MCP Connector API is beta** — The `mcp_servers` API parameter for remote servers is in beta. Production deployments should monitor for breaking changes in the connector interface.

9. **No centralized MCP server registry by Anthropic** — While Anthropic provides a Connectors Directory for vetted integrations, there's no single Anthropic-run registry of all available MCP servers. Third-party directories (claudemcp.com, PulseMCP, Glama) fill this gap with varying completeness.

10. **AAIF governance is new** — MCP was donated to the Agentic AI Foundation in December 2025. The long-term impact of multi-stakeholder governance (with OpenAI, Google, Microsoft, AWS on the board) on MCP's direction is still unfolding. Anthropic retains technical influence but no longer unilateral control.

## Bottom Line

**Rating: 4.5 out of 5**

Anthropic doesn't just participate in the MCP ecosystem — they **created it**. The Model Context Protocol was designed, specified, and open-sourced by Anthropic in November 2024, and their commitment shows: 81.8k stars on the reference servers repo, 34k+ combined stars on the Python and TypeScript SDKs, 10+ language SDKs, and the most comprehensive MCP client support of any AI company.

On the **client side**, Anthropic is unmatched. Claude.ai Connectors, Claude Desktop with one-click Desktop Extensions, Claude Code with automatic connector sharing, the MCP Connector API, and MCP Apps (interactive UI in chat) represent the deepest MCP integration of any AI platform. Every Claude product speaks MCP natively.

On the **server side**, the 7 active reference servers (Filesystem, Git, Fetch, Memory, Sequential Thinking, Time, Everything) are well-designed demonstrations of MCP capabilities, not production tools. The 14 archived servers (Google Drive, Slack, GitHub, Postgres) have been superseded by independent maintainers and official implementations from the respective service providers.

The 4.5/5 rating reflects Anthropic's unrivaled position as MCP's creator and most committed implementer. The protocol itself is the ecosystem's foundation, the SDKs power thousands of community servers, and Claude's client support is the most comprehensive available. The half-point deduction is for the lack of a Claude API wrapper server (limiting cross-model use), archived reference server confusion, and the still-evolving specification and governance structure.

**Who benefits most from Anthropic's MCP ecosystem:**

- **MCP server developers** — the SDKs, specification, and reference servers are the definitive starting point for building any MCP server
- **Claude users** — Connectors, Desktop Extensions, and Claude Code MCP support provide the richest MCP client experience available
- **Enterprise teams** — Team and Enterprise plans offer admin controls, custom extension registries, and governance tools for MCP at scale

**Who should be cautious:**

- **Developers using archived reference servers** — switch to actively maintained alternatives; the archived versions have no security guarantees
- **Teams building on v2 SDK pre-alpha** — the v1.x branches are the stable choice until v2 officially ships
- **Anyone expecting a Claude API MCP server** — Anthropic builds clients, not a server wrapping their own API; use the API directly or find a community wrapper

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official Anthropic announcements. Information is current as of March 2026. See our [About page](/about/) for details on our review process.*

## Related Guides

- [MCP Apps: How Anthropic and OpenAI Brought Interactive UIs to AI Chat](/guides/mcp-apps-interactive-ui-extension/) — deep dive on MCP Apps (SEP-1865), the interactive UI extension Anthropic co-developed with OpenAI

