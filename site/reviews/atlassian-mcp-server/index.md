# Atlassian MCP Server — Jira and Confluence Access for AI Agents

> Atlassian's official Rovo MCP server connects AI agents to Jira, Confluence, and Compass. We review the cloud-hosted server and the community alternative with 6x the stars.


Jira and Confluence are the backbone of project management and documentation at thousands of companies. The problem is obvious: AI agents can't see your sprint board, can't search your knowledge base, and can't create tickets from conversation context without some kind of bridge.

Atlassian launched their official Rovo MCP Server in May 2025, hosted at `mcp.atlassian.com`. It [reached general availability on February 4, 2026](https://www.atlassian.com/blog/announcements/atlassian-rovo-mcp-ga), and gives AI agents structured access to Jira, Confluence, Compass, and now Jira Service Management through OAuth 2.1. But here's the twist — a community server with 6x the GitHub stars may actually be the better choice for many teams.

**At a glance:** [955 GitHub stars, 119 forks](https://github.com/atlassian/atlassian-mcp-server), 46+ tools across 6 product areas (now including Bitbucket Cloud), [~960 all-time PulseMCP visitors, global rank #9,228](https://www.pulsemcp.com/servers/atlassian), GA since Feb 4 2026, SSE transport sunset June 30 2026

**Category:** [Developer Tools](/categories/developer-tools/)

## The Official Server

**Repository:** [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server)
**Stars:** 955 | **Forks:** 119 | **Commits:** 108 | **Contributors:** 14 ([live repo stats](https://github.com/atlassian/atlassian-mcp-server), checked 2026-08-12)
**Language:** JavaScript, Python | **License:** Apache 2.0

The Atlassian Rovo MCP Server is cloud-hosted — there's nothing to install, no local process to manage. You point your MCP client at `https://mcp.atlassian.com/v1/mcp` and complete an OAuth 2.1 consent flow in your browser. All actions respect your existing Jira and Confluence permissions. This is the right architecture.

### What It Does

The server supports six Atlassian product areas with 46+ tools:

**Jira:**
- Search issues with JQL ("Find all open bugs in Project Alpha")
- Create, update, and transition issues
- Add comments and work logs
- Bulk issue creation from specs or meeting notes

**Confluence:**
- Search pages with CQL
- Read, create, and update pages
- Summarize content
- Navigate spaces

**Compass:**
- Create service components from repositories
- Query service dependencies
- Bulk import components and custom fields from CSV/JSON

**Jira Service Management:**
- Query alerts and incidents
- View on-call schedules
- Handle escalations

**Bitbucket Cloud (new — April 2026):**
- Browse workspaces and repositories
- Create, approve, merge, and comment on pull requests
- Manage branches, access files, and create commits
- Monitor pipelines and track deployments
- Manage environments

**Cross-product:**
- Link Jira tickets to Confluence pages
- Fetch documentation linked to Compass components
- Rovo Search across all connected products

### Setup

For supported clients (Claude, ChatGPT, GitHub Copilot CLI, Gemini CLI, VS Code, Amazon Quick Suite), setup is straightforward — add the server endpoint and complete the OAuth flow. The app auto-installs on first authorization (no Marketplace installation needed).

For local or custom clients, you'll need Node.js v18+ to run the `mcp-remote` proxy that bridges stdio transport to the remote HTTPS endpoint.

**API token authentication** is available for headless or long-running setups, but requires an organization admin to enable it first and uses scoped Rovo MCP tokens rather than standard Atlassian API tokens.

### Rate Limits

| Plan | Limit |
|------|-------|
| Free | 500 calls/hour |
| Standard | 1,000 calls/hour |
| Premium/Enterprise | 1,000 base + 20 per user (up to 10,000/hour max) |

These limits are per-organization, not per-user. For most teams, the Standard tier's 1,000 calls/hour should be sufficient. Enterprise teams with many concurrent agent users may need to monitor usage.

## What's New (May 2026 Update)

**Teamwork Graph opens to external agents at Team '26.** Atlassian's annual user conference (May 2026) introduced two major additions to the MCP ecosystem:

**Teamwork Graph MCP tools (open beta).** Two new tools — `getTeamworkGraphContext` and `getTeamworkGraphObject` — extend the Rovo MCP server with graph-aware queries. The pair works as a discover-then-fetch pattern: the context tool surfaces what's connected and relevant; the object tool retrieves a specific node in full detail. Unlike standard MCP tool calls that return raw data, these tools operate against Atlassian's Teamwork Graph, [a connected knowledge store with over 150 billion objects and relationships](https://www.atlassian.com/blog/company-news/teamwork-graph-team-26) spanning Jira issues, Confluence pages, deployments, third-party integrations (GitHub, Google Docs, Figma), and team relationships. [Atlassian benchmarks show graph-grounded responses are 44% more accurate while using 48% fewer tokens](https://www.atlassian.com/blog/company-news/teamwork-graph-team-26) than equivalent calls that retrieve raw data and let the model sort it out. Authentication is unified — a single credential spanning all connected Atlassian apps and linked tools.

**Teamwork Graph CLI (open beta).** [A companion command-line interface with 300+ commands](https://www.atlassian.com/blog/company-news/teamwork-graph-team-26) lets coding agents — specifically called out: Claude Code, Cursor, and Codex — query and modify graph context directly from the terminal. The CLI supports both read and write operations, meaning agents can update work items and create relationships, not just query them. Atlassian designed the CLI for token efficiency: structured commands return targeted context rather than large data dumps, which aligns with how agentic coding workflows consume context. Use case highlighted at the conference: incident response agents that pull a unified view of related Jira issues, past deployments, and historical remediation steps in a single query.

**Why this matters for MCP users.** The standard Rovo MCP server (46+ tools, cloud-hosted, OAuth 2.1) connects AI agents to Jira and Confluence operations. The Teamwork Graph layer adds a different kind of access: relationship traversal across the full data model, not just individual record operations. An agent looking up "all Jira issues connected to this Confluence page that also have related GitHub PRs from the last sprint" previously required multiple round trips; the graph tools aim to answer that in one. This doesn't replace the existing tools — it extends them.

**Current status:** Both the Teamwork Graph MCP tools and the CLI are in open beta as of Team '26. Production-readiness and rate limit behavior under graph queries have not been independently assessed.

## What's New (April 2026 Update)

**Bitbucket Cloud support added (April 8, 2026).** The biggest feature addition since GA — AI clients can now browse repositories, create commits, manage pull requests, and monitor pipelines through the same MCP connection that serves Jira and Confluence. This brings the server to six product areas. However, Bitbucket tools currently require API token authentication only; OAuth support is not yet available for these tools, creating an inconsistency with the OAuth 2.1 flow used for Jira and Confluence.

**Rovo platform expanding rapidly around the MCP server.** [Rovo Studio entered open beta](https://community.atlassian.com/forums/Atlassian-AI-Rovo-articles/The-new-unified-AI-building-experience-for-Rovo-Studio-is-now-in/ba-p/3208776) as a unified, no-code AI workflow builder. [Rovo Skills — pre-built guidance for common Jira, Confluence, and JSM tasks — went live for all Rovo Chat customers](https://community.atlassian.com/forums/Atlassian-AI-Rovo-articles/Rovo-Skills-are-now-available/ba-p/3208133). [Rovo agents can now connect to MCP-enabled third-party apps](https://www.atlassian.com/blog/announcements/rovo-mcp-gallery) such as Figma, Intercom, Box, and Canva to pull context and take action without custom integration code. (We could not independently confirm the "Rovo Service GA" and "verified agent badge" claims from the earlier version of this review, so we've cut them here.)

**Open issues climbed back up: 38 → 52 (as of April 2026).** The downward trend we noted last review had reversed. Fourteen new issues since March, including a critical [duplicate-creation bug (#132)](https://github.com/atlassian/atlassian-mcp-server/issues/132) where `createJiraIssue` consistently creates two identical tickets per call — also affecting `createComment`. Multiple users confirmed this with financial impact from wasted API quotas. **As of this audit (August 2026), [the repository shows 73 open issues](https://github.com/atlassian/atlassian-mcp-server/issues?q=is%3Aissue+is%3Aopen)** — the climb has continued, though (see "Where It Falls Short" below) many of the specific bugs cited in this review's April snapshot have since been closed.

**Admin controls switched from allowlist to blocklist.** Organization admins can now choose which apps shouldn't have access to Rovo features, replacing the previous allowlist approach with a blocklist model.

**PulseMCP traffic declining (April 2026 snapshot).** The official server dropped from ~16.7K to ~14.4K all-time visitors, weekly visitors fell from ~697 to ~530, and global ranking slipped from #1,184 to #1,431. Meanwhile, the community alternative surged to 3.4M all-time visitors. **Re-checked for this audit (August 2026):** [PulseMCP now shows the official server](https://www.pulsemcp.com/servers/atlassian) at ~960 all-time visitors (global rank #9,228) and [the community server](https://www.pulsemcp.com/servers/sooperset-atlassian) at ~995K all-time visitors (global rank #75). Both figures have moved dramatically since April in ways a simple traffic decline doesn't explain — this likely reflects a change in PulseMCP's estimation methodology rather than a literal ~15x usage swing. Treat PulseMCP's exact numbers as directional estimates, not precise measurements.

## What's New (March 2026 Update)

**[Rovo MCP Server reached GA on February 4, 2026.](https://www.atlassian.com/blog/announcements/atlassian-rovo-mcp-ga)** The server is now officially generally available with enterprise-grade security, audit logging, and admin controls. Atlassian reports that [nearly 40% of monthly active users are enterprise customers](https://www.atlassian.com/blog/announcements/atlassian-rovo-mcp-ga).

**Agents in Jira open beta (February 24).** [Atlassian introduced AI agents directly inside Jira](https://www.atlassian.com/blog/rovo/ai-agents-in-jira) — you can assign work to Rovo agents and MCP-enabled third-party agents, @mention agents in issue comments for iterative collaboration, and embed agents into Jira workflows. Agents respect existing project permissions, audit trails, and approval flows. This complements MCP: MCP lets your external agents reach into Jira, while Agents in Jira lets Atlassian's agents work natively inside your boards.

**ChatGPT connector with writeback.** Atlassian launched a [dedicated Rovo MCP Connector for ChatGPT](https://www.atlassian.com/blog/announcements/atlassian-rovo-mcp-connector-chatgpt) — described in Atlassian's own announcement as "among the first MCP connectors with writeback support." [The ecosystem now spans 20+ MCP connectors](https://www.atlassian.com/blog/announcements/atlassian-rovo-mcp-connector-chatgpt) including Figma, HubSpot, and Lovable.

**Azure SRE Agent integration (February 25).** [Microsoft published official documentation for connecting Atlassian Rovo MCP to Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/get-started-with-atlassian-rovo-mcp-server-in-azure-sre-agent/4497122) via Streamable HTTP transport. This validates the server for enterprise DevOps workflows — SRE teams can query Jira issues, view on-call schedules, and manage incidents through Azure's AI agent platform.

**Jira Service Management tools added.** The server now covers five product areas (up from three): Jira, Confluence, Compass, Jira Service Management (alerts, on-call, escalations), and cross-product Rovo Search. Tool count documented at 46+ via Azure integration docs.

**Search regression fixed.** [Issue #70](https://github.com/atlassian/atlassian-mcp-server/issues/70) (deprecated `/rest/api/3/search` endpoint returning empty results) was closed on March 15. The remote server already uses the new `/rest/api/3/search/jql` endpoint — the bug only affected the old Docker stdio version that Atlassian no longer supports. This removes the biggest blocker from our previous review.

**Open issues dropped from 57 to 38.** Atlassian closed 19 issues since our last review, a meaningful cleanup. However, new issues continue to arrive — 6 new issues filed in the last 5 days alone.

**SSE transport deprecated.** The `/v1/sse` endpoint is deprecated in favor of `/v1/mcp` (Streamable HTTP). SSE remains available for backward compatibility until June 30, 2026.

**New pagination bug (since fixed).** [Issue #118](https://github.com/atlassian/atlassian-mcp-server/issues/118) (filed March 20) reported that `searchJiraIssuesUsingJql` silently dropped results beyond `maxResults` — no `nextPageToken`, no pagination metadata, incorrect totals, a regression likely tied to the `/search/jql` migration. As of this audit (August 2026) the issue is closed — see the update in "Where It Falls Short" below.

## What Works Well

**Cloud-hosted with OAuth 2.1 is the gold standard.** No local dependencies, no credential files to manage, no Docker containers to run. The server handles scaling, uptime, and transport. This is how production MCP servers should work.

**Permission-aware by design.** [Every action respects the user's existing Jira, Confluence, and Compass roles](https://support.atlassian.com/atlassian-rovo-mcp-server/docs/getting-started-with-the-atlassian-remote-mcp-server/). If you can't see a project in Jira, your agent can't either. IP allowlisting is also honored if your organization uses it.

**Audit logging.** [MCP usage logs give admins visibility into how AI is interacting with Jira and Confluence, for audit, compliance, and governance needs](https://www.atlassian.com/blog/announcements/atlassian-rovo-mcp-ga). For compliance-heavy environments, this is critical — you can trace what every agent did, when, and on whose behalf.

**Free for all Atlassian Cloud customers.** No additional cost beyond your existing Atlassian subscription. The rate limits scale with your plan tier, but the MCP server itself adds no per-user or per-call charges.

**Admin controls are comprehensive.** Organization admins can manage, monitor, and revoke MCP access through the Connected Apps interface. Domain and IP controls let you restrict which external AI tools can connect. Individual users can revoke their own authorization independently.

**AGENTS.md integration.** You can configure default project keys, space IDs, and cloud IDs in AGENTS.md to reduce discovery tool calls and save tokens — a thoughtful touch for reducing per-query costs.

## Where It Falls Short

**73 open issues as of this audit (August 2026)** — [live count](https://github.com/atlassian/atlassian-mcp-server/issues?q=is%3Aissue+is%3Aopen), up from the 52 we reported in April and 38 in March. But re-checking each specific bug cited in earlier versions of this review against the live tracker shows most of those individual bugs have actually been closed — the issue count keeps climbing on new reports, not because these particular ones lingered:

- **Duplicate creation bug — still open.** [Issue #132](https://github.com/atlassian/atlassian-mcp-server/issues/132) (filed March 31, still open as of August 2026) reports that `createJiraIssue` consistently creates two identical tickets for every single call — duplicates a few milliseconds apart. Also affects `createComment`. Multiple users confirmed, with financial impact from wasted API quotas. This remains the most damaging bug open on the tracker.
- **Pagination bug — fixed.** [Issue #118](https://github.com/atlassian/atlassian-mcp-server/issues/118) (filed March 20), which reported that JQL search silently dropped results beyond `maxResults`, is now closed.
- **ADF conversion failures — partially fixed.** Of the three issues previously cited here, [#42](https://github.com/atlassian/atlassian-mcp-server/issues/42) and [#104](https://github.com/atlassian/atlassian-mcp-server/issues/104) (both about `editJiraIssue` rejecting valid ADF markdown conversions) are now closed. [#101](https://github.com/atlassian/atlassian-mcp-server/issues/101) (custom field values must be Atlassian Document objects) remains open.
- **Content loss during Confluence edits — mostly fixed.** [Issue #60](https://github.com/atlassian/atlassian-mcp-server/issues/60) (general rich-content loss on edit) and [#53](https://github.com/atlassian/atlassian-mcp-server/issues/53) (HTML `<details>` tags escaped) are now closed. [#54](https://github.com/atlassian/atlassian-mcp-server/issues/54) (inline comment anchors stripped on `updateConfluencePage`) remains open.
- **Large page handling — still open.** [Issue #106](https://github.com/atlassian/atlassian-mcp-server/issues/106) reports `updateConfluencePage`/`createConfluencePage` being unusable for large pages (40-70KB ADF bodies), with no partial-update mechanism.
- **Authentication — mostly fixed, one client still affected.** Of the three client auth issues previously cited, [#137](https://github.com/atlassian/atlassian-mcp-server/issues/137) (Cursor OAuth 404) and [#116](https://github.com/atlassian/atlassian-mcp-server/issues/116) (Gemini CLI PKCE failure) are now closed. [#108](https://github.com/atlassian/atlassian-mcp-server/issues/108) (VS Code "Internal Server Error" / "We couldn't verify your access") remains open.
- **Jira mentions broken in ChatGPT — still open.** [Issue #136](https://github.com/atlassian/atlassian-mcp-server/issues/136) reports that mentions don't work when adding comments via the Atlassian MCP App in ChatGPT — ironic given the ChatGPT connector was a headline GA feature.

**Cloud-only with no Data Center support.** If your organization runs Jira or Confluence on Server or Data Center (still common in enterprises with compliance requirements), the official server is not an option. This is a significant gap.

**No self-hosted deployment.** You can't run this server behind your firewall. All data flows through `mcp.atlassian.com` on Cloudflare infrastructure. For organizations with strict data residency requirements, this may be a non-starter.

**The README doesn't list actual tools.** Unlike every other MCP server we've reviewed, the official documentation describes workflows ("Find all open bugs") rather than listing actual tool names and parameters. You discover the tools only after connecting. This makes it harder to evaluate capabilities before setup.

**No file attachments.** [Issue #47](https://github.com/atlassian/atlassian-mcp-server/issues/47) and [#63](https://github.com/atlassian/atlassian-mcp-server/issues/63) — both still open as of this audit — request the ability to attach files to Jira issues, a common workflow that's missing.

## The Community Alternative

**Repository:** [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian)
**Stars:** 5,732 | **Forks:** 1,308 | **Commits:** 695+ | **Contributors:** 100+ ([live repo stats](https://github.com/sooperset/mcp-atlassian), checked 2026-08-12)
**Language:** Python | **License:** MIT
**Latest release:** [v0.23.0 (July 18, 2026)](https://github.com/sooperset/mcp-atlassian/releases) | **Total releases:** 73+
**PulseMCP:** [global rank #75, ~995K all-time visitors](https://www.pulsemcp.com/servers/sooperset-atlassian) (checked 2026-08-12)

The community server from sooperset has **6x the GitHub stars** of the official server (5,732 vs 955) and, per current PulseMCP figures, far more estimated traffic (~995K vs ~960 all-time visitors). That's extremely unusual — for most products, the official server dominates adoption. Here's why the community version leads:

**72 tools vs. 46+ tools.** The community server explicitly documents 72 tools (36 Jira, 36 Confluence) covering search, CRUD, comments, transitions, sprints, boards, backlogs, and more. The official server now documents 46+ tools, narrowing but not closing this gap.

**Server/Data Center support.** Works with Jira Server/Data Center v8.14+ and Confluence Server/Data Center v6.0+ — the feature the official server refuses to support.

**Multiple auth methods.** API tokens for Cloud, Personal Access Tokens for Server/Data Center, OAuth 2.0, and as of v0.21.0, OAuth 2.0 with Dynamic Client Registration for Data Center instances.

**SSE and Streamable HTTP transport.** Supports remote hosting with multi-user capabilities, not just stdio. v0.21.0 added Basic Auth multi-user support for MCP gateway scenarios.

**Self-hosted.** Install via `uvx`, Docker, `pip`, or from source. Your data stays behind your firewall.

**Active development.** 695+ commits, 73+ releases, 100+ contributors ([live repo stats](https://github.com/sooperset/mcp-atlassian), checked 2026-08-12) — rapid iteration with 1-2 week release cadence.

**v0.21.1 highlights (April 10):** Fixed critical startup crash caused by `fakeredis 2.35.0` dependency break, added `include_content` flag to Confluence create/update operations to skip echoing full page bodies, new `confluence_get_space_page_tree` tool for discovering page hierarchies, and Helm chart enhancements with OAuth proxy and client storage configuration.

**v0.21.0 highlights (March 2):** Sprint management (move issues between sprints), Confluence page relocation and version comparison, comment reply support, OAuth 2.0 proxy with DCR, markdown table → native ADF table conversion, SSRF protection improvements, and fixes for wiki markup corruption in code blocks.

**But it has its own problems:** [131 open issues and 50 open PRs as of this audit](https://github.com/sooperset/mcp-atlassian/issues) (down from 171/85 reported in April — a real cleanup, not stagnation). It's community-maintained with no corporate backing. No hosted remote option (you manage the infrastructure). And it requires Python and its dependency chain.

## Other Community Servers

| Server | Stars (checked 2026-08-12) | Focus | Notable |
|--------|-------|-------|---------|
| [aashari/mcp-server-atlassian-jira](https://github.com/aashari/mcp-server-atlassian-jira) | 72 | Jira-only | 5 generic HTTP tools (GET/POST/PUT/PATCH/DELETE), TOON format reduces tokens 30-60% |
| [xuanxt/atlassian-mcp](https://github.com/xuanxt/atlassian-mcp) | 6 | Jira + Confluence | 51 tools, npm + Docker, sprints and boards |
| [b1ff/atlassian-dc-mcp](https://github.com/b1ff/atlassian-dc-mcp) | 86 | Data Center | Bitbucket + Confluence + Jira for DC version |
| [nguyenvanduocit/jira-mcp](https://github.com/nguyenvanduocit/jira-mcp) | 96 | Jira | Go-based, sprint planning + workflow transitions |

The aashari server takes an interesting approach: instead of wrapping individual Jira operations into specific tools, it exposes five generic HTTP methods that map directly to Jira's REST API. This means any API endpoint is accessible, but agents need to know the Jira API structure to use it effectively.

## Security Considerations

[Atlassian's README includes an unusually candid security warning](https://github.com/atlassian/atlassian-mcp-server#readme): LLMs are vulnerable to prompt injection and tool poisoning attacks. They explicitly recommend:

- Use least privilege and scoped tokens
- Review high-impact changes before confirming
- Monitor audit logs for unusual activity
- Only use trusted MCP clients and servers

This transparency is commendable, but the warnings highlight a real risk: an agent with Jira write access could create, modify, or transition issues based on injected prompts. The official server's permission model mitigates this (you can't exceed your own access), but doesn't prevent an agent from taking unintended actions within your permission scope.

The community server (sooperset) has its own `SECURITY.md` with API token handling guidelines, but lacks the audit logging that the official server provides.

## Who Should Use Which

**Use the official Atlassian server if:**
- You're on Atlassian Cloud and want zero-install setup
- Audit logging and admin controls matter for compliance
- Your workflows are primarily read-heavy (search, summarize, navigate)
- You're using a supported client (Claude, ChatGPT, Copilot CLI, VS Code)

**Use sooperset/mcp-atlassian if:**
- You need Server/Data Center support
- You need self-hosted deployment behind a firewall
- You need the full 72-tool surface area
- You want a battle-tested server with rapid release cadence
- Write operations (creating/editing issues and pages) are central to your workflow

**Use aashari/mcp-server-atlassian-jira if:**
- You want maximum API coverage with minimal tool overhead
- Your agents can navigate Jira's REST API structure
- Token efficiency is critical (TOON format)

**Consider [Azure DevOps MCP Server](/reviews/azure-devops-mcp-server/) instead if:**
- Your team uses Azure DevOps rather than Jira for work items, sprints, and backlogs
- Both platforms cover similar project management workflows; the right choice depends on where your organization already lives. Azure DevOps MCP (3.5/5, 1.6K stars) offers 9 tool domains, WIQL queries, and local + remote deployment — with a critical unpatched CVE to weigh. Jira's MCP ecosystem is more mature but fragmented across official and community servers.

## The Verdict

**Rating: 3.5 / 5** — for the official Atlassian Rovo MCP server.

The Rovo platform story is impressive. Bitbucket Cloud support (April 8) brings the server to six product areas. Rovo Studio entered open beta. The Skills Library provides pre-built agent capabilities. Rovo agents now connect to third-party apps via MCP natively. Atlassian is building a comprehensive agentic platform around Jira and Confluence, and the architecture remains the gold standard: cloud-hosted, OAuth 2.1, permission-aware, audit-logged, free with your subscription.

But the MCP server's execution has struggled to keep up with the platform's ambitions. Open issues climbed from 38 to 52 by April, and [stand at 73 as of this audit](https://github.com/atlassian/atlassian-mcp-server/issues?q=is%3Aissue+is%3Aopen) — though re-checking the specific bugs cited in this review shows Atlassian has closed most of them since April (pagination, two of three ADF conversion bugs, most of the Confluence content-loss reports, Cursor and Gemini CLI auth). The duplicate-creation bug ([#132](https://github.com/atlassian/atlassian-mcp-server/issues/132)) — where every `createJiraIssue` call silently creates two identical tickets — remains open and is still the most damaging reliability issue we've seen on any MCP server. VS Code auth ([#108](https://github.com/atlassian/atlassian-mcp-server/issues/108)) is still broken. The ChatGPT connector's own mention feature still doesn't work ([#136](https://github.com/atlassian/atlassian-mcp-server/issues/136)). Bitbucket tools lack OAuth support, inconsistent with the rest of the server. These aren't edge cases — they affect core workflows.

The community server (sooperset) continues to pull ahead on GitHub stars: [5,732 vs. 955 (6x)](https://github.com/sooperset/mcp-atlassian). PulseMCP's estimated-traffic numbers for both servers have shifted enough since April that we're not confident treating them as a precise comparison (see the April 2026 Update section above); directionally, PulseMCP still ranks the community server far above the official one. Its v0.23.0 release (July 2026) continued the pace set by v0.21.1's startup-crash fix and page-hierarchy tool. Both servers are still working through issue backlogs (73 official, 131 community as of this audit), but the community server ships fixes faster with a 1-2 week release cadence.

We're holding the rating at 3.5/5. The platform expansion is genuine, and Atlassian has closed most of the specific reliability bugs this review flagged in April — but the duplicate-creation bug alone should still give any team pause before using write operations, and it remains open as of this audit. Atlassian needs to fix the duplication, finish stabilizing authentication across clients, and ship OAuth for Bitbucket tools before the rating can improve.

**May 2026 note:** Team '26's Teamwork Graph additions are promising — the 44%/48% accuracy and token claims are significant if they hold at scale, and the CLI designed for Claude Code and Cursor signals that Atlassian is treating coding agents as first-class users. But both the Graph MCP tools and CLI are in open beta, and independent benchmarking against the published numbers hasn't happened yet. If the graph-grounded queries prove reliable in practice, the productivity argument for the official server gets stronger. Watch for open beta feedback over summer 2026.

---

*This review is based on research conducted in March–May 2026, analyzing the GitHub repositories, official documentation, Atlassian blog announcements, Atlassian Community forums, Microsoft Azure documentation, PulseMCP data, open issues, Team '26 conference materials, and community feedback. Stats and issue statuses were re-verified against live sources on 2026-08-12. ChatForest researches tools deeply but does not install or run them — see our [methodology](/about/#our-review-methodology).*

*This review was last edited on 2026-05-17 using Claude Sonnet 4.6 (Anthropic).*

