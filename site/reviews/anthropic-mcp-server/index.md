# Anthropic MCP Servers — The Company That Created the Model Context Protocol

> Anthropic created MCP in November 2024 and maintains the reference servers, SDKs, and specification. Claude Desktop, Claude Code, and Claude.ai are the most mature MCP clients.


**At a glance:** [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) (84.2k stars, 10.5k forks, 7 active reference servers) + [Python SDK](https://github.com/modelcontextprotocol/python-sdk) (22.7k stars) + [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) (12.2k stars). Anthropic **invented MCP** in November 2024 and operates the most comprehensive MCP ecosystem: reference servers, official SDKs in 10+ languages, the protocol specification, and the most mature MCP client support across Claude.ai, Claude Desktop, Claude Code, and the API. Part of our **[AI Providers MCP category](/categories/ai-providers/)**.

Anthropic MCP servers provide the **reference implementations** that define how MCP servers should work — file system access, Git operations, web fetching, persistent memory, and sequential reasoning. These aren't wrappers around the Claude API (Anthropic's products ARE the MCP clients). Instead, they're the foundational tools that demonstrate what MCP can do and how to build servers correctly.

[Anthropic](https://www.anthropic.com/) was founded in 2021 by **Dario Amodei** and **Daniela Amodei**, along with several former OpenAI researchers. As of April 2026: approximately **$30 billion annualized revenue** (up from $9B at end of 2025, ~1,400% YoY growth), **$380 billion valuation** (February 2026 Series G, $30B raised) with **$800 billion valuation offers** from investors in April 2026, approximately **3,000-5,000 employees** (estimates vary), and a potential **IPO in October 2026** (in talks with Goldman Sachs, JPMorgan, Morgan Stanley). Key products include Claude (**Opus 4.7** shipped April 16 2026, Sonnet 4.6, Haiku 4.5), Claude Code (with Routines and Channels), Claude Desktop, and the Messages/Responses API.

**Architecture note:** Anthropic's MCP role is unique: they are both the **protocol creator** and the **leading MCP client**. Unlike OpenAI (primarily a client), Google (official remote servers), or Microsoft (enterprise MCP servers), Anthropic designed the entire protocol, maintains the specification, provides the SDKs, and built the most capable MCP client implementations. They donated MCP to the [Agentic AI Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) (Linux Foundation) in December 2025, co-founded with OpenAI and Block.

## What's New (April 2026)

**Claude Opus 4.7 shipped April 16, 2026.** Anthropic's most capable model: improved software engineering, complex long-running agentic tasks, and the first Claude model with high-resolution image support (2576px / 3.75MP, up from 1568px / 1.15MP). 1M token context, 128K max output tokens. Available across Claude.ai, API, Bedrock, Vertex, Foundry, Snowflake Cortex, and GitHub Copilot.

**Claude Code Routines launched April 14 (Research Preview).** Turns Claude Code from a local dev tool into a scheduled cloud automation platform. A routine packages a prompt, one or more repositories, and MCP connectors into reusable automations running on Anthropic-managed infrastructure. Triggers: scheduled (hourly/nightly/weekly), API (HTTP POST), or GitHub events (PRs, releases). Pro users get 5 routines/day, Max 15, Team/Enterprise 25.

**Claude Code Channels launched.** Hook Claude Code into Discord, Telegram, or iMessage — an MCP server acts as a two-way bridge. Developers start a session with `--channels` to spin up a polling service. Community iMessage support shipped within a week of Discord/Telegram launch.

**Desktop Extensions renamed from .dxt to .mcpb (MCP Bundle).** Existing .dxt files continue working, but new extensions should use .mcpb. The `@anthropic-ai/dxt` package is moving to `@anthropic-ai/mcpb`. Same functionality — naming is more descriptive of what these packages do.

**Connectors Directory grown to 299 verified integrations.** Up from the initial launch, now covering productivity (Asana, Notion, Linear, Atlassian), communication (Slack, Gmail, Microsoft 365), developer tools, databases, and more. Microsoft 365 connector uses delegated Graph permissions via an enterprise MCP server.

**MAJOR: Ox Security disclosed STDIO architecture vulnerability (April 16).** Security researchers found that MCP's STDIO transport mechanism allows arbitrary OS command execution — any command passed as a server spawn attempt executes before returning an error. Affects all MCP SDKs across Python, TypeScript, Java, and Rust. Impact: 150M+ downloads, 7,000+ public servers, up to 200,000 vulnerable instances. Ox discovered 10 CVEs across popular projects (LiteLLM, LangChain, LangFlow, Flowise, LettaAI, LangBot). **Anthropic declined to modify the protocol**, classifying the behavior as "expected" and stating sanitization is the developer's responsibility. Coverage in The Register, Hacker News, Infosecurity Magazine, and multiple security research blogs.

**MCP specification next release targeting June 2026.** Current spec is 2025-11-25. The 2026 roadmap (published March 2026) organizes development around four priority areas. MCP Dev Summit North America (April 2-3, NYC, 1,200 attendees) showcased evolution from local stdio to remote servers, authorization, elicitation, structured outputs, and experimental tasks primitive.

**AAIF maintainer team expanded.** Clare Liguori joined as Core Maintainer, Den Delimarsky joined as Lead Maintainer alongside David Soria Parra (April 8, 2026). AAIF has grown to "well over a hundred members" across Platinum, Gold, and Silver tiers. AGNTCon + MCPCon events announced for 2026.

**Reference servers repo: 84.2K stars** (up from 81.8K), 10.5K forks, 4,085 commits, 232 open issues, 114 open PRs.

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

Anthropic originally maintained 14 additional reference servers that were **archived on May 29, 2025** at [modelcontextprotocol/servers-archived](https://github.com/modelcontextprotocol/servers-archived) (253 stars, 148 forks). No updates since archival — multiple security researchers have filed CVEs against individual archived servers that will never be patched. These were moved as the ecosystem matured and independent maintainers took over:

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
- Official **Connectors Directory** with **299 verified integrations** (Asana, Box, Figma, Linear, Slack, Microsoft 365, etc.)
- Supports read AND write operations
- Available on all Claude.ai plans (Free, Pro, Team, Enterprise)
- **MCP Apps** — interactive UI rendered inside the chat window (project boards, dashboards, canvases)
- Microsoft 365 connector uses delegated Graph permissions via enterprise MCP server

### Claude Desktop (macOS + Windows)

- Local MCP servers via `claude_desktop_config.json`
- **MCP Bundles** (.mcpb files, renamed from .dxt) — one-click MCP server installation bundling all dependencies
- Admin controls for Team/Enterprise: enable/disable extensions, upload custom extensions, manage registries
- Anthropic open-sourced the MCP Bundle specification and toolchain (`@anthropic-ai/mcpb`)

### Claude Code (CLI)

- Configure MCP servers via `.mcp.json` files (project-level or global)
- If logged in with Claude.ai account, Connectors are automatically available
- Supports local stdio servers and remote Streamable HTTP servers
- MCP servers extend Claude Code's capabilities with custom tools
- **Routines** (April 2026, Research Preview) — scheduled cloud automation with MCP connectors. Trigger via cron, API, or GitHub events
- **Channels** (April 2026) — two-way MCP bridge to Discord, Telegram, and iMessage

### API (Messages + MCP Connector)

- `mcp_servers` parameter for remote MCP servers accessible via URL
- **MCP Connector** beta — connect to remote servers directly from API calls
- No extra cost for MCP tool calls beyond standard token billing
- Supports Streamable HTTP transport

## MCP SDKs

Anthropic created and maintains the official SDKs that power the entire MCP ecosystem:

### Python SDK

- **GitHub:** [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) — 22.7k stars, 3.3k forks, 851 commits, 235 open issues, 199 open PRs
- **License:** MIT
- **FastMCP** framework for simplified server creation with decorator-based API
- Type-safe context injection, Pydantic validation, progress reporting
- Supports stdio, SSE, and Streamable HTTP transports
- OAuth authentication support
- v2 pre-alpha in development on main branch; stable v1.x branch for production

### TypeScript SDK

- **GitHub:** [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) — 12.2k stars, 1.8k forks, 178 contributors, 1,472 commits
- **License:** MIT / Apache 2.0 (dual)
- v1.29.0 (March 30, 2026); v2.0.0-alpha.2 on main branch (April 1, 2026) with breaking changes across error handling, task management, Standard Schema support, and framework middleware packages (@modelcontextprotocol/express, /hono, /fastify, /node)
- Cross-runtime support: Node.js, Bun, Deno
- CVE-2026-0621: ReDoS vulnerability in UriTemplate regex patterns (patched)
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
| Membership | 100+ members across Platinum, Gold, and Silver tiers |
| Lead Maintainers | David Soria Parra (Anthropic, co-creator), Den Delimarsky (April 2026) |
| Core Maintainers | Clare Liguori (April 2026) and others |
| Events | AGNTCon + MCPCon North America and Europe announced for 2026 |
| Governance | Governing Board makes strategic decisions; individual projects maintain technical autonomy |

## Claude API Pricing

| Model | Input (per 1M tokens) | Cached Input | Output (per 1M tokens) | Context Window |
|-------|----------------------|--------------|----------------------|----------------|
| Haiku 4.5 | $1.00 | $0.10 | $5.00 | 200K |
| Sonnet 4.6 | $3.00 | $0.30 | $15.00 | 200K |
| Sonnet 4.6 (>200K input) | $6.00 | $0.60 | $22.50 | 1M |
| Opus 4.6 | $5.00 | $0.50 | $25.00 | 1M |
| Opus 4.7 | $5.00 | $0.50 | $25.00 | 1M |

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

1. **CRITICAL: STDIO transport architecture vulnerability (April 2026)** — Ox Security disclosed that MCP's STDIO transport allows arbitrary OS command execution across all official SDKs (Python, TypeScript, Java, Rust). Any command passed as a server spawn attempt executes before returning an error. Impact: 150M+ downloads, 7,000+ public servers, up to 200,000 vulnerable instances. Ox found 10 CVEs across LiteLLM, LangChain, LangFlow, Flowise, LettaAI, and LangBot. **Anthropic declined to patch**, classifying the behavior as "expected" and stating sanitization is the developer's responsibility. Covered by The Register, Hacker News, Infosecurity Magazine, and multiple security research blogs.

2. **No MCP server wrapping the Claude API** — Anthropic focuses on the client side. There is no official MCP server that lets other AI agents (GPT, Gemini) call Claude via MCP. Community implementations exist but have minimal adoption.

3. **Archived reference servers still causing confusion** — The 14 original reference servers (Google Drive, Slack, GitHub, Postgres, etc.) archived May 2025 still appear in tutorials and blog posts. Multiple CVEs have been filed against individual archived servers that will never be patched. Security researchers note that 5,000+ forks carry unpatched vulnerabilities into downstream agents.

4. **Git MCP server security audit still open** — Issue #3537 (18 unconstrained parameters) remains open with no maintainer response. While some argument injection guards were added in March 2026, the comprehensive audit has stalled.

5. **MCP Bundle (.mcpb) ecosystem still maturing** — The recent rename from .dxt to .mcpb adds transition friction. Most MCP servers are still installed manually via config files rather than one-click bundles. The ecosystem list (awesome-claude-dxt) is growing but not comprehensive.

6. **Connector availability varies by plan** — While all Claude.ai plans support MCP Connectors, the Connectors Directory and admin controls differ between Free, Pro, Team, and Enterprise tiers. Some connectors require Team or Enterprise plans.

7. **SDK version fragmentation deepening** — Both Python and TypeScript SDKs have v2 pre-alpha on main branches while v1.x remains stable. TypeScript v2.0.0-alpha.2 (April 1, 2026) introduces breaking changes across error handling, task management, and schema validation. CVE-2026-0621 (ReDoS in UriTemplate) was patched in the TypeScript SDK. Developers must be careful to use the correct branch.

8. **MCP specification still evolving** — Current spec is 2025-11-25. Next release targeting June 2026. MCP Dev Summit (April 2-3, NYC, 1,200 attendees) showcased new primitives: elicitation, tasks, structured outputs, and server-side agent loops. Servers built against older spec versions may need updates.

9. **Claude Code Routines is Research Preview** — Limits are restrictive (5/day Pro, 15 Max, 25 Team/Enterprise). Feature set may change significantly before GA.

10. **No centralized MCP server registry by Anthropic** — The Connectors Directory (299 integrations) covers vetted cloud servers, but there's no registry of all available MCP servers. Third-party directories (claudemcp.com, PulseMCP, Glama) fill this gap.

11. **AAIF governance still maturing** — 100+ members, expanded maintainer team (April 2026), but long-term impact of multi-stakeholder governance on MCP's direction is still unfolding. Anthropic retains significant technical influence through David Soria Parra as Lead Maintainer.

## Bottom Line

**Rating: 4.5 out of 5**

Anthropic doesn't just participate in the MCP ecosystem — they **created it**. The Model Context Protocol was designed, specified, and open-sourced by Anthropic in November 2024, and their commitment continues to accelerate: 84.2k stars on the reference servers repo, 35k+ combined stars on the Python and TypeScript SDKs, 10+ language SDKs, and the most comprehensive MCP client support of any AI company. In April 2026 alone: Opus 4.7 shipped, Claude Code gained Routines (scheduled cloud automation) and Channels (Discord/Telegram/iMessage bridge), Desktop Extensions were renamed to .mcpb bundles, and the Connectors Directory grew to 299 verified integrations.

On the **client side**, Anthropic is unmatched. Claude.ai Connectors (299 integrations), Claude Desktop with one-click MCP Bundles, Claude Code with Routines and Channels, the MCP Connector API, and MCP Apps (interactive UI in chat) represent the deepest MCP integration of any AI platform. Every Claude product speaks MCP natively.

On the **server side**, the 7 active reference servers (Filesystem, Git, Fetch, Memory, Sequential Thinking, Time, Everything) are well-designed demonstrations of MCP capabilities, not production tools. The 14 archived servers have been superseded by independent maintainers and official implementations.

The 4.5/5 rating reflects Anthropic's unrivaled position as MCP's creator and most committed implementer. The half-point deduction is for the STDIO architecture vulnerability (declined to patch despite 200K+ affected servers and 10 downstream CVEs), archived reference server confusion with unpatched CVEs, and the still-evolving specification and governance structure. Anthropic's response to Ox Security's disclosure — classifying arbitrary command execution as "expected behavior" — is a notable blemish on an otherwise exemplary track record.

**Who benefits most from Anthropic's MCP ecosystem:**

- **MCP server developers** — the SDKs, specification, and reference servers are the definitive starting point for building any MCP server
- **Claude users** — Connectors, Desktop Extensions, and Claude Code MCP support provide the richest MCP client experience available
- **Enterprise teams** — Team and Enterprise plans offer admin controls, custom extension registries, and governance tools for MCP at scale

**Who should be cautious:**

- **Developers using archived reference servers** — switch to actively maintained alternatives; the archived versions have no security guarantees
- **Teams building on v2 SDK pre-alpha** — the v1.x branches are the stable choice until v2 officially ships
- **Anyone expecting a Claude API MCP server** — Anthropic builds clients, not a server wrapping their own API; use the API directly or find a community wrapper

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official Anthropic announcements. Information is current as of April 2026. See our [About page](/about/) for details on our review process.*

## Related Guides

- [MCP Apps: How Anthropic and OpenAI Brought Interactive UIs to AI Chat](/guides/mcp-apps-interactive-ui-extension/) — deep dive on MCP Apps (SEP-1865), the interactive UI extension Anthropic co-developed with OpenAI

