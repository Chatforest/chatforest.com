# Anthropic MCP Servers — The Company That Created the Model Context Protocol

> Anthropic created MCP in November 2024 and maintains the reference servers, SDKs, and specification. Claude Desktop, Claude Code, and Claude.ai are the most mature MCP clients.


**At a glance:** [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) (89.6k stars, 11.4k forks, 7 active reference servers) + [Python SDK](https://github.com/modelcontextprotocol/python-sdk) (24.0k stars) + [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) (13.2k stars) — star/fork counts checked live against GitHub on 2026-08-14; they climb continuously, so treat as directional. Anthropic **invented MCP** in November 2024 and operates the most comprehensive MCP ecosystem: reference servers, official SDKs in 10+ languages, the protocol specification, and the most mature MCP client support across Claude.ai, Claude Desktop, Claude Code, and the API. Part of our **[AI Providers MCP category](/categories/ai-providers/)**.

Anthropic MCP servers provide the **reference implementations** that define how MCP servers should work — file system access, Git operations, web fetching, persistent memory, and sequential reasoning. These aren't wrappers around the Claude API (Anthropic's products ARE the MCP clients). Instead, they're the foundational tools that demonstrate what MCP can do and how to build servers correctly.

[Anthropic](https://www.anthropic.com/) was **[founded in 2021](https://techcrunch.com/2021/05/28/anthropic-is-the-new-ai-research-outfit-from-openais-dario-amodei-and-it-has-124m-to-burn/)** by **Dario Amodei** and **Daniela Amodei**, along with several former OpenAI researchers. Financial trajectory through 2026: **[$30 billion annualized revenue run rate (ARR)](https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth)** in early April 2026 (up from approximately $9B ARR at end of 2025), then **[$47 billion ARR by late May 2026](https://www.anthropic.com/news/series-h)**; **[$380 billion valuation](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation)** (February 2026 Series G, $30B raised), followed by **[$800 billion valuation offers](https://www.bloomberg.com/news/articles/2026-04-14/anthropic-attracts-investor-offers-at-a-800-billion-valuation)** from investors that Anthropic initially declined (April 2026), then a **[$65 billion Series H at a $965 billion post-money valuation](https://www.anthropic.com/news/series-h)** (closed May 28, 2026, led by Altimeter Capital, Dragoneer, Greenoaks, and Sequoia Capital). Headcount is not officially disclosed by Anthropic; the most recent reported figure is **[approximately 2,300 employees as of December 2025](https://fortune.com/article/anthropic-ceo-dario-amodei-openai-chatgpt-artificial-intelligence-safety-donald-trump/)** (Fortune), up from under 200 in late 2023 — third-party estimate trackers put mid-2026 headcount higher but Anthropic has not confirmed a figure. Anthropic has also **[filed confidentially for an IPO targeting an October 2026 Nasdaq listing](https://www.techtimes.com/articles/317845/20260605/anthropic-ipo-picks-goldman-sachs-morgan-stanley-jpmorgan-revenue-accounting-question-looms.htm)** (Goldman Sachs, JPMorgan, and Morgan Stanley selected as lead underwriters in June 2026). Key products include Claude (**[Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)** shipped April 16 2026, Sonnet 4.6, Haiku 4.5), Claude Code (with Routines, Channels, and Agent View), Claude Desktop, and the Messages/Responses API. **Acquired Stainless** (May 18, 2026) to strengthen SDK tooling.

**Architecture note:** Anthropic's MCP role is unique: they are both the **protocol creator** and the **leading MCP client**. Unlike OpenAI (primarily a client), Google (official remote servers), or Microsoft (enterprise MCP servers), Anthropic designed the entire protocol, maintains the specification, provides the SDKs, and built the most capable MCP client implementations. They donated MCP to the [Agentic AI Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) (Linux Foundation) in December 2025, co-founded with OpenAI and Block.

## What's New (May 2026)

**[Stainless acquired May 18, 2026](https://www.anthropic.com/news/anthropic-acquires-stainless).** Anthropic acquired Stainless, a NYC-based startup (founded 2022) that automates creation and maintenance of language SDKs. Stainless was previously used by OpenAI, Google, and Cloudflare. Financial terms undisclosed. Strategic rationale: Stainless directly strengthens Anthropic's SDK tooling pipeline — including the MCP Python and TypeScript SDKs. Reported by TechCrunch.

**Claude Code v2.1.144 (May 19).** The Claude Code CLI advanced from v2.1.91 to v2.1.144 across the month. MCP-relevant highlights per the **[Claude Code changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)**: v2.1.132 (May 6) fixed unbounded memory growth (10GB+ RSS) when a stdio MCP server writes non-protocol data to stdout, plus retry-and-report handling when an MCP server connects but fails `tools/list`; v2.1.136 (May 8) shipped MCP server stability fixes. We could not independently confirm the specific "OAuth refresh token handling" and "67% faster `/resume`" details attributed to v2.1.136 and v2.1.117 in earlier drafts of this review against the public changelog, so those specifics have been removed — flagged for follow-up rather than left unverified.

**[Agent View launched May 11](https://claude.com/blog/agent-view-in-claude-code) (Research Preview).** New `claude agents` command in Claude Code provides a centralized dashboard for all running Claude Code sessions, available to Pro/Max/Team/Enterprise and API users. Sessions are accessible from the browser with shareable session URLs.

**[Claude for Small Business (May 13)](https://www.anthropic.com/news/claude-for-small-business).** 15 ready-to-run agentic workflows via new MCP connectors to QuickBooks, PayPal, HubSpot, Canva, DocuSign, Google Workspace, Microsoft 365, and Slack, delivered through Claude Cowork. Available via claude.ai.

**[Claude for Creative Work (April 28)](https://www.anthropic.com/news/claude-for-creative-work).** Nine new MCP-powered creative connectors: Ableton, Adobe Creative Cloud (50+ tools), Affinity by Canva, Autodesk Fusion, Blender, Resolume Arena and Wire, SketchUp, and Splice. Available via claude.ai.

**[Connectors Directory](https://claude.com/docs/connectors/directory) growing.** Anthropic does not publish an official integration count; third-party trackers put the directory in the low-to-mid 300s in May 2026, climbing past 400 by mid-2026 — treat any specific number as a rough, fast-moving estimate rather than an Anthropic-confirmed figure.

**MCP specification: release candidate in progress.** **[PR #2750](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2750)**, filed May 19 by MCP lead maintainer Den Delimarsky, originally titled "Blog: 2026-06-30 specification release candidate"; the target date was later pushed to 2026-07-28 (the PR was updated and merged under that title on May 22). Headline change is a **stateless transport rework** (self-contained `tools/call` requests, simplified HTTP flow). Also in scope: MCP Apps primitive, Tasks primitive, Extensions framework (preventing future breaking changes to core), Authorization changes, Governance framework with conformance requirements. 22 SEPs in scope.

**[Python SDK v1.27.1 (May 8)](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.27.1).** Pydantic 2.13 compatibility fix, `httpx` restricted to `<1.0.0`, and a fix coercing empty-string optional URL fields to `None` in `OAuthClientMetadata`.

**Legacy model deprecation.** **[`claude-sonnet-4-20250514` and `claude-opus-4-20250514`](https://platform.claude.com/docs/en/about-claude/model-deprecations)** (original Claude 4 generation) retired June 15, 2026. Current lineup at review time: Opus 4.7, Sonnet 4.6, Haiku 4.5 (Anthropic has since shipped newer models; see Anthropic's own model page for the current lineup).

**[Claude Mythos Preview (Project Glasswing, April 7)](https://www.anthropic.com/glasswing).** Invitation-only cybersecurity model that Anthropic's own announcement says "can surpass all but the most skilled humans at finding and exploiting software vulnerabilities" and has "already found thousands of high-severity vulnerabilities, including some in every major operating system and web browser." Partners include AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks. Anthropic committed up to $100M in usage credits across 40+ organizations and $4M in direct donations to open-source security organizations (Alpha-Omega/OpenSSF via the Linux Foundation, and the Apache Software Foundation). Not publicly available.

**[Gates Foundation $200M commitment (May 14)](https://www.anthropic.com/news/gates-foundation-partnership).** Four-year blended commitment (grants, Claude credits, and technical support) across global health, education, and economic mobility.

**Reference servers repo: 85,913 stars** (up from 84,200 — +1,700 stars), 10,752 forks, 4,102 commits, 279 open issues, 203 open PRs, per **[the repo's public stats](https://github.com/modelcontextprotocol/servers)** as of this review's original May 2026 snapshot — see the "At a glance" line above for the current count checked at audit time.

---

## What's New (April 2026)

**[Claude Opus 4.7 shipped April 16, 2026](https://www.anthropic.com/news/claude-opus-4-7).** Anthropic's most capable model at the time: improved software engineering and complex long-running agentic tasks, plus higher-resolution vision — Anthropic's own announcement says it "can accept images up to 2,576 pixels on the long edge (~3.75 megapixels), more than three times as many as prior Claude models." 1M token context. Available across Claude.ai, the API, Amazon Bedrock, Google Cloud Vertex AI, and Microsoft Foundry (we could not confirm Snowflake Cortex or GitHub Copilot availability from Anthropic's own announcement, so those two have been removed from this line).

**[Claude Code Routines launched April 14](https://claude.com/blog/introducing-routines-in-claude-code) (Research Preview).** Turns Claude Code from a local dev tool into a scheduled cloud automation platform. A routine packages a prompt, one or more repositories, and MCP connectors into reusable automations running on Anthropic-managed infrastructure. Triggers: scheduled, API (HTTP POST), or GitHub events (PRs, releases). Pro users get 5 routines/day, Max 15, Team/Enterprise 25.

**Claude Code Channels launched March 20, 2026** (not April, despite this recap's original placement here — corrected on the 2026-08-14 audit pass). Hook Claude Code into Discord or Telegram, with iMessage (macOS) added roughly a week later, on March 26. An MCP server acts as a two-way bridge between the chat platform and a local Claude Code session.

**Desktop Extensions renamed from .dxt to .mcpb (MCP Bundle)** — this happened in **[late 2025](https://blog.modelcontextprotocol.io/posts/2025-11-20-adopting-mcpb/)** (the MCP project's own blog post is dated November 21, 2025), not April 2026; kept in this recap for continuity but the date has been corrected on the 2026-08-14 audit pass. Existing .dxt files continue working, but new extensions should use .mcpb. The `@anthropic-ai/dxt` package moved to `@anthropic-ai/mcpb`. Same functionality — naming is more descriptive of what these packages do.

**Connectors Directory growing** — up from the initial launch, now covering productivity (Asana, Notion, Linear, Atlassian), communication (Slack, Gmail, Microsoft 365), developer tools, databases, creative tools (Blender, Adobe Creative Cloud, SketchUp, Autodesk Fusion), and small business tools (QuickBooks, PayPal, HubSpot, DocuSign) per **[Anthropic's Connectors Directory docs](https://claude.com/docs/connectors/directory)**. Anthropic does not publish a running total, so no specific count is asserted here (see the May 2026 note above on why the "315+" figure from earlier drafts of this review has been removed). Microsoft 365 connector uses delegated Graph permissions via an enterprise MCP server.

**MAJOR: Ox Security disclosed STDIO architecture vulnerability (April 16).** Security researchers found that MCP's STDIO transport mechanism allows arbitrary OS command execution — any command passed as a server spawn attempt executes before returning an error. Affects all MCP SDKs across Python, TypeScript, Java, and Rust. Impact per **[Ox Security's report](https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/)**, corroborated by **[The Register's independent coverage](https://www.theregister.com/2026/04/16/anthropic_mcp_design_flaw/)**: 150M+ downloads, 7,000+ public servers, up to 200,000 vulnerable instances. Ox's report lists 10 CVEs across GPT Researcher, LiteLLM, Agent Zero, Fay Framework, Bisheng, Langchain-Chatchat, Jaaz, Upsonic, Windsurf, and DocsGPT — **an earlier draft of this review misattributed these to "LangChain, LangFlow, Flowise, LettaAI, and LangBot," which do not appear in Ox's CVE list; corrected on the 2026-08-14 audit pass.** **Anthropic declined to modify the protocol**, with Ox's report quoting Anthropic as citing the behavior as "expected" and stating sanitization is the developer's responsibility; The Register's separate reporting corroborates that Anthropic confirmed the behavior as intentional during coordinated disclosure in January 2026.

**MCP specification next release targeting mid-to-late 2026.** Current stable spec is 2025-11-25. See the "release candidate in progress" note above (May 2026) for how the target date moved from June 30 to July 28, 2026.

**[AAIF maintainer team expanded](https://blog.modelcontextprotocol.io/posts/2026-04-08-maintainer-update/).** Clare Liguori (AWS) joined as Core Maintainer, Den Delimarsky (Anthropic) joined as Lead Maintainer alongside David Soria Parra (April 8, 2026). AAIF membership has grown quickly — **[from roughly 146 organizations in April 2026 to 247 by August 2026](https://www.linuxfoundation.org/press/agentic-ai-foundation-welcomes-97-new-members)** across Platinum, Gold, Silver, and Associate tiers, so any specific count should be treated as a snapshot, not a stable figure.

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

### Archived Reference Servers (13)

Anthropic originally maintained 13 additional reference servers that were **archived on May 29, 2025** at **[modelcontextprotocol/servers-archived](https://github.com/modelcontextprotocol/servers-archived)** (294 stars, 166 forks as of 2026-08-14; a prior version of this review said 14 servers and cited stale 253/148 counts — corrected on the 2026-08-14 audit pass against the **[current README of the main servers repo](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/README.md)**, which lists exactly these 13 as archived). No updates since archival. Most notably, the archived **SQLite MCP server** had a SQL-injection flaw that was forked 5,000+ times before archival and that Anthropic has said it will not patch because the repo is out of scope post-archival, per **[Trend Micro's research](https://www.trendmicro.com/en_us/research/25/f/why-a-classic-mcp-server-vulnerability-can-undermine-your-entire-ai-agent.html)** and **[The Register's coverage](https://www.theregister.com/2025/06/25/anthropic_sql_injection_flaw_unfixed/)** — see Known Issue #3 below. These were moved as the ecosystem matured and independent maintainers took over:

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
- Official **[Connectors Directory](https://claude.com/docs/connectors/directory)** covering hundreds of verified and community integrations (Asana, Box, Figma, Linear, Slack, Microsoft 365, Blender, Adobe CC, QuickBooks, HubSpot, etc.) — Anthropic does not publish an exact count
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
- **[Routines](https://claude.com/blog/introducing-routines-in-claude-code)** (April 14 2026, Research Preview) — scheduled cloud automation with MCP connectors. Three trigger types: scheduled cadence, HTTP POST API endpoint, or GitHub events (PR open/close, releases)
- **Channels** (launched March 20, 2026, not April — see the "What's New (April 2026)" note above) — two-way MCP bridge to Discord and Telegram, with iMessage added March 26
- **[Agent View](https://claude.com/blog/agent-view-in-claude-code)** (May 11, Research Preview) — `claude agents` command provides a centralized dashboard for all running sessions; shareable session URLs

### API (Messages + MCP Connector)

- `mcp_servers` parameter for remote MCP servers accessible via URL
- **MCP Connector** beta — connect to remote servers directly from API calls
- No extra cost for MCP tool calls beyond standard token billing
- Supports Streamable HTTP transport

## MCP SDKs

Anthropic created and maintains the official SDKs that power the entire MCP ecosystem:

### Python SDK

- **GitHub:** [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) — 24.0k stars, 3.8k forks (checked live 2026-08-14; was 22.7k/3.3k at the review's original May 2026 snapshot)
- **License:** MIT
- **FastMCP** framework for simplified server creation with decorator-based API
- Type-safe context injection, Pydantic validation, progress reporting
- Supports stdio, SSE, and Streamable HTTP transports
- OAuth authentication support
- v2 pre-alpha in development on main branch (as of the May 2026 snapshot); stable v1.x branch for production

### TypeScript SDK

- **GitHub:** [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) — 13.2k stars, 2.1k forks (checked live 2026-08-14; was 12.2k/1.8k at the review's original May 2026 snapshot)
- **License:** MIT / Apache 2.0 (dual)
- v1.29.0 (March 30, 2026); v2.0.0-alpha.2 on main branch (April 1, 2026) with breaking changes across error handling, task management, Standard Schema support, and framework middleware packages (@modelcontextprotocol/express, /hono, /fastify, /node) — as of this audit (August 2026) the v2 line has since moved to beta targeting the 2026-07-28 spec, per the **[MCP blog's SDK-beta post](https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/)**
- Cross-runtime support: Node.js, Bun, Deno
- **[CVE-2026-0621](https://github.com/advisories/GHSA-8r9q-7v3j-jr4g)**: ReDoS vulnerability in the `UriTemplate` class's handling of RFC 6570 exploded array patterns (affected versions up to and including 1.25.1; patched in 1.25.2)
- v1.x receiving bug fixes and security updates for at least 6 months after v2's stable release

### Additional SDKs

Official or community-maintained SDKs also exist for **C#, Go, Java, Kotlin, PHP, Ruby, Rust, and Swift** — making MCP accessible across virtually every major programming language.

## MCP Governance

Anthropic donated MCP to the **[Agentic AI Foundation (AAIF)](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation)** in December 2025 (announced December 9, 2025):

| Aspect | Detail |
|--------|--------|
| Foundation | Agentic AI Foundation, directed fund under the Linux Foundation |
| Co-founders | Anthropic, Block, OpenAI |
| Platinum members | Amazon Web Services, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI |
| Donated projects | MCP (Anthropic), goose (Block), AGENTS.md (OpenAI) |
| Membership | **[247 member organizations as of August 2026](https://www.linuxfoundation.org/press/agentic-ai-foundation-welcomes-97-new-members)** across Platinum, Gold, Silver, and Associate tiers — up from ~146 in April 2026; grows quickly enough that any snapshot count goes stale within weeks |
| Lead Maintainers | David Soria Parra (Anthropic, MCP co-creator), **[Den Delimarsky](https://blog.modelcontextprotocol.io/posts/2026-04-08-maintainer-update/)** (Anthropic, promoted April 2026) |
| Core Maintainers | Clare Liguori (AWS, added April 2026) and others |
| Events | **[AGNTCon + MCPCon Europe (Sept 17–18, Amsterdam) and North America (Oct 22–23, San Jose)](https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-global-2026-events-program-anchored-by-agntcon-mcpcon-north-america-and-europe)** |
| Governance | Governing Board makes strategic decisions; individual projects maintain technical autonomy |

## Claude API Pricing

Per **[Anthropic's current model-pricing table](https://platform.claude.com/docs/en/about-claude/pricing)** (checked live 2026-08-14):

| Model | Input (per 1M tokens) | Cached Input (read) | Output (per 1M tokens) | Context Window |
|-------|----------------------|--------------|----------------------|----------------|
| Haiku 4.5 | $1.00 | $0.10 | $5.00 | 200K |
| Sonnet 4.6 | $3.00 | $0.30 | $15.00 | 1M |
| Opus 4.6 | $5.00 | $0.50 | $25.00 | 1M |
| Opus 4.7 | $5.00 | $0.50 | $25.00 | 1M |

A prior version of this table listed a "Sonnet 4.6 (>200K input)" row at $6.00/$0.60/$22.50 — Anthropic's current pricing docs state that "Claude 4.6 and later models... include the full 1M token context window at standard pricing" with no long-context premium tier, so that row was inaccurate and has been removed on the 2026-08-14 audit pass.

| Cost Optimization | Discount |
|-------------------|----------|
| Prompt caching (5-min) | Writes 1.25x, reads 0.1x base price |
| Prompt caching (1-hour) | Writes 2x, reads 0.1x base price |
| Batch API | 50% off all models |

**[Claude subscriptions](https://claude.com/pricing)** (checked live 2026-08-14):
- Claude Free — limited access, supports MCP Connectors
- Claude Pro — $20/month billed monthly ($17/month billed annually)
- Claude Team — $25/seat/month billed monthly for the standard seat ($20/seat/month billed annually); a $100–125/seat/month Premium seat tier also exists
- Claude Enterprise — seat price plus usage at API rates; custom terms
- Claude Code — included with Pro/Max; Max plans start at $100/month

**Note:** MCP tool calls incur standard token billing — there's no MCP-specific surcharge. The tool definitions and results count toward your input/output tokens.

## Known Issues

1. **CRITICAL: STDIO transport architecture vulnerability (April 2026)** — **[Ox Security disclosed](https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/)**, corroborated by **[The Register](https://www.theregister.com/2026/04/16/anthropic_mcp_design_flaw/)**, that MCP's STDIO transport allows arbitrary OS command execution across all official SDKs (Python, TypeScript, Java, Rust). Any command passed as a server spawn attempt executes before returning an error. Impact: 150M+ downloads, 7,000+ public servers, up to 200,000 vulnerable instances. Ox's report lists 10 CVEs across GPT Researcher, LiteLLM, Agent Zero, Fay Framework, Bisheng, Langchain-Chatchat, Jaaz, Upsonic, Windsurf, and DocsGPT — **corrected on the 2026-08-14 audit pass; an earlier draft of this review misattributed these CVEs to a different set of projects (LangChain, LangFlow, Flowise, LettaAI, LangBot) that do not appear in Ox's own CVE table.** **Anthropic declined to patch**, classifying the behavior as "expected" and stating sanitization is the developer's responsibility. Covered by The Register and Hacker News (we could not independently confirm Infosecurity Magazine coverage, so that attribution has been removed). **Update (May 2026):** **[SEP-2692](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2692)** ("Stdio process lifetime") is a documentation-only SEP clarifying that stdio server processes should persist for the life of the host application — it does not itself change runtime behavior or resolve the underlying command-execution issue. No resolution yet. Claude Code v2.1.132 (May 6) separately fixed unbounded memory growth (10GB+) with stdio MCP servers, per the **[Claude Code changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)**.

2. **No MCP server wrapping the Claude API** — Anthropic focuses on the client side. There is no official MCP server that lets other AI agents (GPT, Gemini) call Claude via MCP. Community implementations exist but have minimal adoption.

3. **Archived reference servers still causing confusion** — The 13 original reference servers (Google Drive, Slack, GitHub, Postgres, etc.) archived May 2025 still appear in tutorials and blog posts. Most notably, the archived **SQLite MCP server** has a SQL-injection vulnerability that was forked over 5,000 times before archival; per **[Trend Micro's research](https://www.trendmicro.com/en_us/research/25/f/why-a-classic-mcp-server-vulnerability-can-undermine-your-entire-ai-agent.html)**, Anthropic's position is that because the repo is archived, the flaw is "out of scope" and will not be patched, so it persists in every downstream fork. A prior version of this review generalized this into an unsourced "5,000+ forks" claim about the whole archived-servers batch; corrected on the 2026-08-14 audit pass to attribute it specifically to the SQLite server, which is what the source actually documents.

4. **Git MCP server security history** — **[Issue #3537](https://github.com/modelcontextprotocol/servers/issues/3537)** ("Security Audit: Unconstrained string parameters across all official servers," filed March 12, 2026) flags 18 unconstrained string parameters in the Git server and remains open with no maintainer response as of this audit. Separately, **[CVE-2025-68144](https://github.com/advisories/GHSA-9xwc-hfwc-8w59)** — an argument-injection flaw in the `git_diff` and `git_checkout` tools that let flag-like arguments overwrite arbitrary files — was fixed in `mcp-server-git` 2025.12.18 (December 2025), following disclosure by Cyata Security; a prior version of this review dated that fix to "March 2026," which does not match the public record and has been corrected.

5. **MCP Bundle (.mcpb) ecosystem still maturing** — The recent rename from .dxt to .mcpb adds transition friction. Most MCP servers are still installed manually via config files rather than one-click bundles. The ecosystem list (awesome-claude-dxt) is growing but not comprehensive.

6. **Connector availability varies by plan** — While all Claude.ai plans support MCP Connectors, the Connectors Directory and admin controls differ between Free, Pro, Team, and Enterprise tiers. Some connectors require Team or Enterprise plans.

7. **SDK version fragmentation deepening** — At the review's May 2026 snapshot, both Python and TypeScript SDKs had v2 pre-alpha on main branches while v1.x remained stable; TypeScript v2.0.0-alpha.2 (April 1, 2026) introduced breaking changes across error handling, task management, and schema validation. **[CVE-2026-0621](https://github.com/advisories/GHSA-8r9q-7v3j-jr4g)** (ReDoS in `UriTemplate`) was patched in TypeScript SDK 1.25.2. As of this audit (August 2026), TypeScript SDK v2 has since moved to **[beta](https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/)** targeting the 2026-07-28 spec. Developers must be careful to use the correct branch.

8. **MCP specification still evolving** — Current stable spec is 2025-11-25. A release-candidate PR was filed May 19 (**[#2750](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2750)**) originally targeting June 30, 2026; the target later moved to **July 28, 2026**, under which it was merged May 22. Headline change is the stateless transport rework, plus MCP Apps and Tasks primitives, Extensions framework, Authorization changes, and a new Governance Framework with conformance requirements. 22 SEPs in scope. Servers built against the 2025-11-25 spec may need updates when the RC ships.

9. **Claude Code Routines is Research Preview** — Limits are restrictive (5/day Pro, 15 Max, 25 Team/Enterprise), per **[Anthropic's own announcement](https://claude.com/blog/introducing-routines-in-claude-code)**. Feature set may change significantly before GA.

10. **No centralized MCP server registry by Anthropic** — The **[Connectors Directory](https://claude.com/docs/connectors/directory)** covers vetted cloud servers, but there's no registry of all available MCP servers and no published count of directory entries. Third-party directories (claudemcp.com, PulseMCP, Glama) fill this gap.

11. **AAIF governance still maturing** — **[247 member organizations as of August 2026](https://www.linuxfoundation.org/press/agentic-ai-foundation-welcomes-97-new-members)**, expanded maintainer team (April 2026), but long-term impact of multi-stakeholder governance on MCP's direction is still unfolding. Anthropic retains significant technical influence through David Soria Parra as Lead Maintainer.

## Bottom Line

**Rating: 4.5 out of 5**

Anthropic doesn't just participate in the MCP ecosystem — they **created it**. The Model Context Protocol was designed, specified, and open-sourced by Anthropic in November 2024, and their commitment continues to accelerate: 89.6k stars on the reference servers repo, 37k+ combined stars on the Python and TypeScript SDKs, 10+ language SDKs, and the most comprehensive MCP client support of any AI company. Since April 2026: Opus 4.7 shipped, Claude Code gained Routines (scheduled cloud automation), Channels (Discord/Telegram bridge, added March 2026), and Agent View (centralized agent dashboard), the Connectors Directory grew across creative and small business categories, and Anthropic acquired Stainless (May 18) to strengthen SDK tooling.

On the **client side**, Anthropic is unmatched. Claude.ai Connectors, Claude Desktop with one-click MCP Bundles, Claude Code with Routines, Channels, and Agent View, the MCP Connector API, and MCP Apps (interactive UI in chat) represent the deepest MCP integration of any AI platform. Every Claude product speaks MCP natively.

On the **server side**, the 7 active reference servers (Filesystem, Git, Fetch, Memory, Sequential Thinking, Time, Everything) are well-designed demonstrations of MCP capabilities, not production tools. The 13 archived servers have been superseded by independent maintainers and official implementations.

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

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official Anthropic announcements. The bulk of this review reflects Anthropic's product and MCP-ecosystem state as of May 2026; a claim-by-claim citation audit on 2026-08-14 corrected several errors and refreshed fast-moving figures (GitHub star/fork counts, funding/valuation, AAIF membership) but did not re-report every dated item forward to August 2026 — see inline notes where a figure or date was corrected. See our [About page](/about/) for details on our review process.*

## Related Guides

- [MCP Apps: How Anthropic and OpenAI Brought Interactive UIs to AI Chat](/guides/mcp-apps-interactive-ui-extension/) — deep dive on MCP Apps (SEP-1865), the interactive UI extension Anthropic co-developed with OpenAI

