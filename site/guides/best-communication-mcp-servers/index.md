# Best Communication MCP Servers in 2026

> Slack vs Microsoft Teams vs Discord — which communication platform MCP server should your AI agent use? We compare official servers, auth models, search, and tool coverage with clear recommendations.


Communication platforms are where work happens. Slack channels, Teams threads, Discord servers — they hold institutional knowledge, decisions, and context that AI agents need but can't reach without an MCP integration.

> **🔒 Security note (April 2026):** CVE-2025-34072 (CVSS 9.3) affects the deprecated Anthropic community Slack MCP server — data exfiltration via link unfurling. Use Slack's official server at `mcp.slack.com` instead. CVE-2026-32211 (CVSS 9.1) exposes a critical authentication flaw in Azure MCP Server infrastructure — Microsoft has published mitigation guidance but no patch yet. Always pin to specific MCP server versions and audit permissions.

The three major platforms have taken dramatically different approaches to MCP. Slack shipped a polished official server and just announced Slackbot-as-MCP-client. Microsoft followed with an official Teams server but left gaps for community projects to fill. Discord hasn't shipped anything officially, but a new community server just broke the bot-token barrier with OAuth2.

We've reviewed all three: the [Slack MCP server](/reviews/slack-mcp-server/) (4/5), [Microsoft Teams MCP servers](/reviews/teams-mcp-servers/) (3.5/5), and [Discord MCP servers](/reviews/discord-mcp-servers/) (3/5). Here's how they compare, and which one to pick for your setup.

## The Landscape at a Glance

| Feature | [Slack](/reviews/slack-mcp-server/) (4/5) | [Teams](/reviews/teams-mcp-servers/) (3.5/5) | [Discord](/reviews/discord-mcp-servers/) (3/5) |
|---------|-------|-------|---------|
| Official server | Yes (Slack) | Yes (Microsoft) | No |
| Hosted endpoint | `mcp.slack.com` | `agent365.svc.cloud.microsoft` | None (guildbridge on Cloudflare Workers) |
| Auth model | OAuth + PKCE (first-party) | OAuth (Entra ID) | Bot tokens (most), OAuth2 (guildbridge) |
| Tools (official) | ~15 | 24 | N/A |
| Tools (best community) | 15 (korotovsky) | 28 (floriscornel) | 65 (SaseQ) |
| Message search | Yes | No (official), Yes (floriscornel) | Limited (barryyip0625, guildbridge) |
| File operations | No | No (official), Yes (floriscornel) | No |
| Rich formatting | Yes | Plain text only | Varies |
| Read-only mode | Via OAuth scopes | Via permissions / env var | No |
| Security issues | CVE on deprecated community server | CVE-2026-32211 (Azure MCP infra) | None reported |
| Status | GA | Preview | N/A |
| Free to use | Yes (with Slack workspace) | Requires M365 Copilot license | Yes (with Discord bot) |

## Three Maturity Levels

### Slack — The Standard (4/5)

Slack's official MCP server is the benchmark for communication platform integration. Hosted at `mcp.slack.com`, it requires zero local setup — no npm install, no Docker, no local process. Your MCP client connects directly to Slack's endpoint.

**What makes it the best:**
- **OAuth with granular scopes + PKCE.** You choose exactly what the agent can access: public channels, private channels, DMs, group DMs. Each requires separate consent. **PKCE went GA on March 30, 2026** — desktop/mobile clients can now authenticate without embedding a client secret. This is the right security model.
- **Natural language responses.** Search results come back formatted for LLM consumption, not raw API JSON. Less token waste, more usable answers.
- **Search that works.** Searching across an entire workspace — by date, user, content type — is genuinely powerful for knowledge retrieval.
- **Canvas integration.** Create and update Slack canvases programmatically. Export as markdown. Useful for agents that generate reports or documentation.
- **Admin oversight.** Admins see which MCP clients have access, with full audit logging.
- **Expanding client support.** Beyond Claude, Cursor, and Perplexity, the official server now works with ChatGPT, Gemini (Google Agentspace), Vercel, and Notion.

**Where it falls short:** No reactions, no scheduled messages, no emoji (though the korotovsky community server now has reactions — see below). Rate limits vary by tool and aren't well-documented. The Marketplace requirement makes custom client development harder. No SSE transport (Streamable HTTP only).

**New: Slackbot as MCP client (March 31, 2026).** Salesforce announced 30+ new AI features for Slackbot, including MCP client functionality. Slackbot can now connect to external services through MCP, create Google Slides/Docs, and route work to AI agents. Also includes desktop agent capability, meeting transcription, and voice input. Features rolling out over coming months — this makes Slack both the best MCP *server* and an increasingly capable MCP *client* in the communication space.

**Bottom line:** If your team uses Slack and your MCP client supports it, install this. It's a few clicks.

### Teams — Getting There (3.5/5)

Microsoft shipped an official server, which puts Teams ahead of Discord. But the server is in preview, lacks search, and only supports plain text messages. The real story is the ecosystem: three servers that together cover what Teams integration needs.

**The official server** (24 tools) gives you full CRUD on chats, channels, teams, and members. Hosted at `agent365.svc.cloud.microsoft` with Entra ID OAuth. Enterprise-grade RBAC. OData query support for server-side filtering. But no search, no files, plain text only, and still "Preview" status. **Important change:** Microsoft now requires a **M365 Copilot license** to use Work IQ MCP servers. New Work IQ SharePoint and OneDrive servers have launched alongside Teams.

**floriscornel/teams-mcp** (28 tools, 76 stars) is the community server that fills the gaps. **v0.9.0 (March 29, 2026)** added 4 reaction tools — the only Teams MCP server with emoji reactions. KQL-based message search remains unique. File uploads with large file support. Read-only mode via environment variable. LLM-optimized markdown responses. Auth reliability issues persist (3 open auth-related issues).

**InditexTech/mcp-teams-server** (5 tools, 365 stars) is the most production-ready: Docker support, versioned releases from a major enterprise (Inditex), **v1.0.8 (March 16) with security enhancements**. Agent SDK migration underway. Narrowly focused on thread workflows — start threads, reply, read replies.

**Security note:** CVE-2026-32211 (CVSS 9.1) affects Azure MCP Server infrastructure — a critical authentication flaw that could expose sensitive data. CVE-2026-26118 is an SSRF-based privilege escalation in the same infrastructure. No patch yet — only mitigation guidance. These affect the broader Azure MCP ecosystem, not specifically the Teams server tools, but worth monitoring.

**Bottom line:** If you need Teams integration today, use the official server for basic chat/channel work (requires M365 Copilot license), or floriscornel for search, files, and reactions. InditexTech's 365 stars validate its production-readiness for thread workflows. When the official server exits preview and adds search, this category will be a 4/5.

### Discord — Waiting for Official (3/5)

Discord has 200+ million monthly active users and is where the developer and AI community lives. And it has no official MCP server. The gap is filled by community projects, with a notable new entrant breaking the bot-token barrier.

**The options:**
- **SaseQ/discord-mcp** (240 stars, Java, 65 tools) — hit v1.0.0 on March 16 with massive expansion: moderation, voice/stage channels, scheduled events, invites, permission overwrites, and emoji management. 7 contributors. But Java means heavyweight deployment. No activity since March 16.
- **barryyip0625/mcp-discord** (76 stars, TypeScript, 42 tools) — only original option with forum support, most active development (121 commits). v1.3.8 (March 18) fixed streamable HTTP startup crash. Both stdio and HTTP transports. 10 contributors.
- **hanweg/mcp-discord** (148 stars, Python, 15 tools) — simplest setup. Pairs with `mcp-discord-raw` for raw API access. **Dormant since July 2025** — 9 months without a commit.
- **dend/guildbridge** (15 stars, TypeScript, NEW) — **The first Discord MCP server with OAuth2 authentication.** Hosted on Cloudflare Workers (no local process). Discord OAuth2 + bot token with server-side RBAC. Has `search_messages` — one of only two Discord MCP servers with search. 44 commits, actively developed (last push March 26). Small but architecturally significant.
- **HardHeadHackerHead/discord-mcp** (12 stars, TypeScript, 139 tools) — covers nearly the entire Discord API. v2.1.1 added thread tools. But single contributor, zero community validation.
- **v-3/discordmcp** (191 stars, ~2 tools) — early-mover advantage in stars, but 2 commits and minimal features. Dormant since January 2025.

**The bot-token problem is cracking.** Most Discord MCP servers still use a single bot token with static permissions. But dend/guildbridge has broken the pattern with Discord OAuth2 + RBAC, hosted on Cloudflare Workers. It's small (15 stars) but proves the architecture is possible. If Discord ships official MCP support, expect OAuth2 to become the standard.

**Bottom line:** SaseQ leads in tools (65) and stars (240). barryyip0625 leads in active development and forum support. The new guildbridge is worth watching — it's the first to solve the OAuth problem and add search. hanweg is dormant. Pick based on your specific need — forums (barryyip0625), full admin control (SaseQ), OAuth2 security (guildbridge). Given that Slack, GitHub, Stripe, and now Microsoft have all shipped official MCP servers, Discord will likely follow.

## Feature Comparison

### Search

Search is the highest-value communication MCP feature. "Find that conversation about the database migration from last week" — this is what agents are good at.

- **Slack:** Full-text search with date, user, and content type filters. Works across all channels the agent has access to. Built into the official server.
- **Teams:** Not in the official server. floriscornel's community server has KQL-based search — powerful but requires a third-party MCP server.
- **Discord:** barryyip0625 has `discord_search_messages` and guildbridge has `search_messages`, but both are limited compared to platform-level search. No other Discord MCP server has search.

**Winner:** Slack, by a wide margin.

### Security & Auth

- **Slack:** OAuth with per-scope consent. Admin visibility. Audit logging. Marketplace requirement protects workspaces from rogue integrations (annoying for developers, good for security).
- **Teams:** OAuth via Entra ID. Enterprise RBAC enforced server-side. Soft-delete preserves compliance retention. The enterprise security model is strong — arguably stronger than Slack's on paper.
- **Discord:** Bot tokens for most servers. Static permissions. No per-user consent. No admin oversight. **Exception:** guildbridge now offers Discord OAuth2 with server-side RBAC — a significant step forward, though still small-scale.

**Winner:** Teams for enterprise compliance. Slack for practical security + usability balance. Discord is improving (guildbridge) but still behind.

### Setup Difficulty

- **Slack:** Supported clients (Claude, Cursor, Perplexity) — a few clicks. Custom clients — moderate (Marketplace registration + OAuth).
- **Teams:** All paths require Azure AD / Entra ID configuration. Enterprise familiarity with Microsoft identity helps. Community servers need app registrations.
- **Discord:** Create a bot, get a token, set an environment variable. Technically the simplest, but the lack of OAuth means the security model is weaker.

**Winner:** Slack for supported clients. Discord for raw simplicity (at the cost of security).

### Write Operations

- **Slack:** Send messages to any channel, DM, or group DM. Create and update canvases. No reactions or scheduling.
- **Teams:** Full CRUD on chats, channels, teams, and members (official server). Thread-based posting with @mentions (InditexTech). File uploads and emoji reactions (floriscornel v0.9.0). But plain text only — no rich formatting.
- **Discord:** Send messages, manage channels, roles, webhooks, forums (varies by server). No hosted option means running your own write-enabled process.

**Winner:** Teams has the broadest write surface (CRUD on chats, channels, teams, members). Slack has the cleanest write experience.

## Decision Flowchart

**"Which communication MCP server should I use?"**

1. **Does your team use Slack?** → Use [Slack MCP](/reviews/slack-mcp-server/). Done.
2. **Does your org use Microsoft Teams?**
   - Need search or file ops? → Use [floriscornel/teams-mcp](https://github.com/floriscornel/teams-mcp)
   - Need production stability + Docker? → Use [InditexTech/mcp-teams-server](https://github.com/InditexTech/mcp-teams-server)
   - Need full CRUD + enterprise auth? → Use [Microsoft Work IQ Teams](https://github.com/microsoft/mcp)
3. **Does your community use Discord?**
   - Need forum management? → Use [barryyip0625/mcp-discord](https://github.com/barryyip0625/mcp-discord)
   - Need full admin control? → Use [SaseQ/discord-mcp](https://github.com/SaseQ/discord-mcp)
   - Need OAuth2 auth + hosted deployment? → Use [dend/guildbridge](https://github.com/dend/guildbridge)
   - Need quick Python setup? → Use [hanweg/mcp-discord](https://github.com/hanweg/mcp-discord) (note: dormant since July 2025)
4. **Using multiple platforms?** → Start with Slack (most mature), add others as needed.

## Trends to Watch

**Official servers are winning.** Slack's official server (GA, hosted, OAuth + PKCE) is decisively better than any community alternative. Microsoft's official Teams server, even in preview, provides the hosted architecture and enterprise auth that community servers can't match. When Discord ships an official server, the same will happen there.

**Platforms are becoming MCP clients, not just servers.** Slackbot's March 31 announcement — connecting to external services via MCP, routing work to AI agents — signals a shift. Communication platforms aren't just exposing data to agents; they're becoming agent orchestrators. Expect Teams Copilot and Discord to follow.

**Hosted > self-hosted for communication.** Running a local MCP server for your communication platform adds maintenance burden, security risk (tokens on disk), and deployment complexity. Slack and Microsoft's hosted endpoints eliminate these problems. Community servers that require local processes are inherently at a disadvantage — though guildbridge's Cloudflare Workers deployment shows a middle path.

**Search is the killer feature.** The ability to search across your organization's communication history from within an AI conversation is more valuable than any specific write operation. Slack has it. Teams has it via a community server. Discord now has limited search (barryyip0625, guildbridge). This is the single biggest differentiator.

**Enterprise auth matters more than tool count.** Teams' official server has 24 tools. floriscornel has 28. But the official server's Entra ID OAuth and RBAC enforcement make it the right choice for enterprise use, even with fewer features. Tool count is a vanity metric — auth model is a security fundamental.

**Security vulnerabilities are catching up.** CVE-2025-34072 (deprecated Slack community server), CVE-2026-32211 and CVE-2026-26118 (Azure MCP infrastructure) — the communication MCP space is no longer immune to the broader MCP security reckoning. Pin versions, audit permissions, prefer official servers.

## The Bottom Line

The communication MCP landscape has a clear hierarchy: Slack leads, Teams is catching up, Discord is behind.

**Slack (4/5)** got it right — and keeps getting better. Hosted, OAuth + PKCE, search, GA, natural language responses, expanding client support (ChatGPT, Gemini, Vercel, Notion), and now Slackbot-as-MCP-client. If you use Slack, this is an easy install.

**Teams (3.5/5)** has the right architecture but isn't finished. The official server is still in preview, missing search and rich formatting, and now requires M365 Copilot license. floriscornel's v0.9.0 added reactions (28 tools), and InditexTech's 365 stars validate its production thread workflow approach. Watch for CVE-2026-32211 impact on the Azure MCP infrastructure.

**Discord (3/5)** is maturing — SaseQ leads in tools (65, 240 stars), barryyip0625 leads in active development (42 tools, 10 contributors), and the new guildbridge broke the bot-token barrier with OAuth2 + hosted deployment. But hanweg is dormant, v-3/discordmcp is abandoned, and there's still no official backing. The gap between Discord's importance in AI/dev circles and its MCP maturity is narrowing — guildbridge's OAuth2 is a particularly meaningful step.

---

*This comparison covers Slack, Microsoft Teams, and Discord MCP servers as of April 2026. ChatForest researches MCP servers by reading source code, analyzing GitHub repositories and issues, studying documentation, and examining community signals. We do not install or run the servers ourselves. See our [methodology](/about/#our-review-methodology) for details.*

