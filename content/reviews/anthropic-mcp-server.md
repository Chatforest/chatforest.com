---
title: "Anthropic MCP Servers — The Company That Created the Model Context Protocol"
date: 2026-03-23T12:00:00+09:00
description: "Anthropic created MCP in November 2024 and maintains the reference servers, SDKs, and specification. Claude Desktop, Claude Code, and Claude.ai are the most mature MCP clients."
og_description: "Anthropic created MCP and maintains reference servers (85.9k stars), Python/TypeScript SDKs (35k+ stars combined), and the most mature MCP client ecosystem. Stainless acquisition, Agent View, Claude Code v2.1.144, 315+ connectors, June 30 spec RC. Rating: 4.5/5."
content_type: "Review"
card_description: "Anthropic created the Model Context Protocol in November 2024 and donated it to the Agentic AI Foundation (Linux Foundation) in December 2025. They maintain 7 reference servers, official Python and TypeScript SDKs, and the most comprehensive MCP client support across Claude.ai (315+ connectors), Claude Desktop (.mcpb extensions), Claude Code (Routines + Channels + Agent View), and the API. Acquired Stainless (May 2026) to strengthen SDK tooling. $30B annualized revenue, $800B valuation offers, potential IPO in October 2026."
last_refreshed: 2026-05-19
---

**At a glance:** [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) (85.9k stars, 10.8k forks, 7 active reference servers) + [Python SDK](https://github.com/modelcontextprotocol/python-sdk) (22.7k stars) + [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) (12.2k stars). Anthropic **invented MCP** in November 2024 and operates the most comprehensive MCP ecosystem: reference servers, official SDKs in 10+ languages, the protocol specification, and the most mature MCP client support across Claude.ai, Claude Desktop, Claude Code, and the API. Part of our **[AI Providers MCP category](/categories/ai-providers/)**.

Anthropic MCP servers provide the **reference implementations** that define how MCP servers should work — file system access, Git operations, web fetching, persistent memory, and sequential reasoning. These aren't wrappers around the Claude API (Anthropic's products ARE the MCP clients). Instead, they're the foundational tools that demonstrate what MCP can do and how to build servers correctly.

[Anthropic](https://www.anthropic.com/) was founded in 2021 by **Dario Amodei** and **Daniela Amodei**, along with several former OpenAI researchers. As of May 2026: approximately **$30 billion annualized revenue** (up from $9B at end of 2025, ~1,400% YoY growth), **$380 billion valuation** (February 2026 Series G, $30B raised) with **$800 billion valuation offers** from investors, approximately **3,000-5,000 employees** (estimates vary), and a potential **IPO in October 2026** (in talks with Goldman Sachs, JPMorgan, Morgan Stanley). Key products include Claude (**Opus 4.7** shipped April 16 2026, Sonnet 4.6, Haiku 4.5), Claude Code (with Routines, Channels, and Agent View), Claude Desktop, and the Messages/Responses API. **Acquired Stainless** (May 18, 2026) to strengthen SDK tooling.

**Architecture note:** Anthropic's MCP role is unique: they are both the **protocol creator** and the **leading MCP client**. Unlike OpenAI (primarily a client), Google (official remote servers), or Microsoft (enterprise MCP servers), Anthropic designed the entire protocol, maintains the specification, provides the SDKs, and built the most capable MCP client implementations. They donated MCP to the [Agentic AI Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) (Linux Foundation) in December 2025, co-founded with OpenAI and Block.

## What's New (May 2026)

**Stainless acquired May 18, 2026.** Anthropic acquired Stainless, a NYC-based startup (founded 2022) that automates creation and maintenance of language SDKs. Stainless was previously used by OpenAI, Google, and Cloudflare. Financial terms undisclosed. Strategic rationale: Stainless directly strengthens Anthropic's SDK tooling pipeline — including the MCP Python and TypeScript SDKs. Reported by TechCrunch.

**Claude Code v2.1.144 (May 19).** The Claude Code CLI advanced from v2.1.91 to v2.1.144 across the month (~53 releases). MCP-relevant highlights: v2.1.132 (May 6) fixed unbounded memory growth (10GB+) with stdio MCP servers; v2.1.136 (May 8) added MCP server persistence fixes and OAuth refresh token handling; v2.1.117 (April 22) enabled concurrent MCP server connection on startup (default on, up to 67% faster `/resume`).

**Agent View launched May 11 (Research Preview).** New `claude agents` command in Claude Code provides a centralized dashboard for all running Claude Code sessions. Sessions are accessible from the browser with shareable session URLs.

**Claude for Small Business (May 13).** 15 ready-to-run agentic workflows via new MCP connectors to QuickBooks, PayPal, HubSpot, Canva, DocuSign, Google Workspace, and Microsoft 365. Available via claude.ai.

**Claude for Creative Work (April 28).** Eight new MCP-powered creative connectors added: Ableton, Adobe Creative Cloud (50+ tools), Affinity by Canva, Autodesk Fusion, Blender, Resolume Arena/Wire, SketchUp, and Splice. Available via claude.ai.

**Connectors Directory: 315+ verified integrations** (estimated), up from 299 at last review. Two major connector waves (Creative Work, Small Business) added ~23+ confirmed integrations.

**MCP specification: June 30 RC coming.** PR #2750 filed May 19 — "Blog: 2026-06-30 specification release candidate." Headline change is a **stateless transport rework** (self-contained `tools/call` requests, simplified HTTP flow). Also in scope: MCP Apps primitive, Tasks primitive, Extensions framework (preventing future breaking changes to core), Authorization changes, Governance framework with conformance requirements. 22 SEPs in scope; 131 open issues, 107 open PRs in the spec repo.

**Python SDK v1.27.1 (May 8).** Pydantic 2.13 compatibility fix, `httpx` restricted to `<1.0.0`, OAuth client metadata handling improvements.

**Legacy model deprecation.** `claude-sonnet-4-20250514` and `claude-opus-4-20250514` (original Claude 4 generation) deprecated and retiring June 15, 2026. Current lineup: Opus 4.7, Sonnet 4.6, Haiku 4.5.

**Claude Mythos Preview (Project Glasswing, April 7).** Invitation-only cybersecurity model that Anthropic claims "can surpass all but the most skilled humans at finding and exploiting software vulnerabilities." Has identified thousands of critical flaws in major operating systems and browsers. Partners: AWS, Apple, Cisco, Google, Microsoft. Anthropic committed $100M in usage credits to 40+ critical infrastructure organizations and $4M to open-source security organizations. Not publicly available.

**Gates Foundation $200M commitment (May 14).** Four-year grant, Claude credits, and technical support across global health, education, and economic mobility.

**Reference servers repo: 85,913 stars** (up from 84,200 — +1,700 stars), 10,752 forks, 4,102 commits, 279 open issues, 203 open PRs.

---

## What's New (April 2026)

**Claude Opus 4.7 shipped April 16, 2026.** Anthropic's most capable model: improved software engineering, complex long-running agentic tasks, and the first Claude model with high-resolution image support (2576px / 3.75MP, up from 1568px / 1.15MP). 1M token context, 128K max output tokens. Available across Claude.ai, API, Bedrock, Vertex, Foundry, Snowflake Cortex, and GitHub Copilot.

**Claude Code Routines launched April 14 (Research Preview).** Turns Claude Code from a local dev tool into a scheduled cloud automation platform. A routine packages a prompt, one or more repositories, and MCP connectors into reusable automations running on Anthropic-managed infrastructure. Triggers: scheduled (hourly/nightly/weekly), API (HTTP POST), or GitHub events (PRs, releases). Pro users get 5 routines/day, Max 15, Team/Enterprise 25.

**Claude Code Channels launched.** Hook Claude Code into Discord, Telegram, or iMessage — an MCP server acts as a two-way bridge. Developers start a session with `--channels` to spin up a polling service. Community iMessage support shipped within a week of Discord/Telegram launch.

**Desktop Extensions renamed from .dxt to .mcpb (MCP Bundle).** Existing .dxt files continue working, but new extensions should use .mcpb. The `@anthropic-ai/dxt` package is moving to `@anthropic-ai/mcpb`. Same functionality — naming is more descriptive of what these packages do.

**Connectors Directory grown to 315+ verified integrations.** Up from the initial launch, now covering productivity (Asana, Notion, Linear, Atlassian), communication (Slack, Gmail, Microsoft 365), developer tools, databases, creative tools (Blender, Adobe Creative Cloud, SketchUp, Autodesk Fusion), and small business tools (QuickBooks, PayPal, HubSpot, DocuSign). Microsoft 365 connector uses delegated Graph permissions via an enterprise MCP server.

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
- Official **Connectors Directory** with **315+ verified integrations** (Asana, Box, Figma, Linear, Slack, Microsoft 365, Blender, Adobe CC, QuickBooks, HubSpot, etc.)
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
- **Routines** (April 2026, Research Preview) — scheduled cloud automation with MCP connectors. Three trigger types: cron, HTTP POST API endpoint, or GitHub events (PR open/close, releases). Managed at `claude.ai/code/routines` or via `/schedule` CLI command
- **Channels** (April 2026) — two-way MCP bridge to Discord, Telegram, and iMessage
- **Agent View** (May 11, Research Preview) — `claude agents` command provides a centralized dashboard for all running sessions; shareable session URLs

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

1. **CRITICAL: STDIO transport architecture vulnerability (April 2026)** — Ox Security disclosed that MCP's STDIO transport allows arbitrary OS command execution across all official SDKs (Python, TypeScript, Java, Rust). Any command passed as a server spawn attempt executes before returning an error. Impact: 150M+ downloads, 7,000+ public servers, up to 200,000 vulnerable instances. Ox found 10 CVEs across LiteLLM, LangChain, LangFlow, Flowise, LettaAI, and LangBot. **Anthropic declined to patch**, classifying the behavior as "expected" and stating sanitization is the developer's responsibility. Covered by The Register, Hacker News, Infosecurity Magazine, and multiple security research blogs. **Update (May 2026):** SEP-2692 ("Stdio process lifetime") is now in active review in the MCP spec repo — this SEP directly addresses STDIO process management. No resolution yet. Claude Code v2.1.132 (May 6) separately fixed unbounded memory growth (10GB+) with stdio MCP servers.

2. **No MCP server wrapping the Claude API** — Anthropic focuses on the client side. There is no official MCP server that lets other AI agents (GPT, Gemini) call Claude via MCP. Community implementations exist but have minimal adoption.

3. **Archived reference servers still causing confusion** — The 14 original reference servers (Google Drive, Slack, GitHub, Postgres, etc.) archived May 2025 still appear in tutorials and blog posts. Multiple CVEs have been filed against individual archived servers that will never be patched. Security researchers note that 5,000+ forks carry unpatched vulnerabilities into downstream agents.

4. **Git MCP server security audit still open** — Issue #3537 (18 unconstrained parameters) remains open with no maintainer response. While some argument injection guards were added in March 2026, the comprehensive audit has stalled.

5. **MCP Bundle (.mcpb) ecosystem still maturing** — The recent rename from .dxt to .mcpb adds transition friction. Most MCP servers are still installed manually via config files rather than one-click bundles. The ecosystem list (awesome-claude-dxt) is growing but not comprehensive.

6. **Connector availability varies by plan** — While all Claude.ai plans support MCP Connectors, the Connectors Directory and admin controls differ between Free, Pro, Team, and Enterprise tiers. Some connectors require Team or Enterprise plans.

7. **SDK version fragmentation deepening** — Both Python and TypeScript SDKs have v2 pre-alpha on main branches while v1.x remains stable. TypeScript v2.0.0-alpha.2 (April 1, 2026) introduces breaking changes across error handling, task management, and schema validation. CVE-2026-0621 (ReDoS in UriTemplate) was patched in the TypeScript SDK. Developers must be careful to use the correct branch.

8. **MCP specification still evolving** — Current spec is 2025-11-25. **June 30 RC confirmed** (PR #2750, May 19): stateless transport rework is the headline change, plus MCP Apps and Tasks primitives, Extensions framework, Authorization changes, and a new Governance Framework with conformance requirements. 22 SEPs in scope. Servers built against the 2025-11-25 spec may need updates when the RC ships.

9. **Claude Code Routines is Research Preview** — Limits are restrictive (5/day Pro, 15 Max, 25 Team/Enterprise). Feature set may change significantly before GA.

10. **No centralized MCP server registry by Anthropic** — The Connectors Directory (299 integrations) covers vetted cloud servers, but there's no registry of all available MCP servers. Third-party directories (claudemcp.com, PulseMCP, Glama) fill this gap.

11. **AAIF governance still maturing** — 100+ members, expanded maintainer team (April 2026), but long-term impact of multi-stakeholder governance on MCP's direction is still unfolding. Anthropic retains significant technical influence through David Soria Parra as Lead Maintainer.

## Bottom Line

**Rating: 4.5 out of 5**

Anthropic doesn't just participate in the MCP ecosystem — they **created it**. The Model Context Protocol was designed, specified, and open-sourced by Anthropic in November 2024, and their commitment continues to accelerate: 85.9k stars on the reference servers repo, 35k+ combined stars on the Python and TypeScript SDKs, 10+ language SDKs, and the most comprehensive MCP client support of any AI company. Since April 2026: Opus 4.7 shipped, Claude Code gained Routines (scheduled cloud automation), Channels (Discord/Telegram/iMessage bridge), and Agent View (centralized agent dashboard), the Connectors Directory grew to 315+ verified integrations across creative and small business categories, and Anthropic acquired Stainless (May 18) to strengthen SDK tooling.

On the **client side**, Anthropic is unmatched. Claude.ai Connectors (315+ integrations), Claude Desktop with one-click MCP Bundles, Claude Code with Routines, Channels, and Agent View, the MCP Connector API, and MCP Apps (interactive UI in chat) represent the deepest MCP integration of any AI platform. Every Claude product speaks MCP natively.

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

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official Anthropic announcements. Information is current as of May 2026. See our [About page](/about/) for details on our review process.*

## Related Guides

- [MCP Apps: How Anthropic and OpenAI Brought Interactive UIs to AI Chat](/guides/mcp-apps-interactive-ui-extension/) — deep dive on MCP Apps (SEP-1865), the interactive UI extension Anthropic co-developed with OpenAI
