---
title: "Microsoft Teams MCP Servers — Official at Last, Community Got There First"
date: 2026-03-22T17:00:00+09:00
description: "Microsoft now has an official Teams MCP server with 25 tools for chats, channels, and members. Two community servers were there first. Here's how they compare and which one to pick."
og_description: "Microsoft now has an official Teams MCP server. Two community alternatives preceded it. Here's how they compare and which to pick."
content_type: "Review"
card_description: "Microsoft's official Work IQ Teams server brings 25 tools for chats, channels, and members. Two community servers offer different approaches. A landscape review."
last_refreshed: 2026-05-20
sources_audited: 2026-08-15
---

[Microsoft Teams has 320 million monthly active users](https://techcommunity.microsoft.com/discussions/microsoftteams/teams-grows-to-320-million-monthly-active-users/3964746) (as of Q1 FY2024; most recent official figure disclosed). It's the default communication tool in enterprise environments — the place where decisions get made, meetings get scheduled, and institutional knowledge goes to die in unread channels.

Unlike Discord (which still has [no official MCP server](/reviews/discord-mcp-servers/)), Microsoft shipped one. The official Work IQ Teams server, rebranded under Microsoft's "Work IQ" intelligence layer, now lives in its own dedicated repo — [microsoft/work-iq](https://github.com/microsoft/work-iq) (967 stars as of August 2026) — having graduated from the broader [microsoft/mcp](https://github.com/microsoft/mcp) catalog (3,569 stars). It provides 25 tools ([full reference](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-teams-tools)) for full CRUD operations on chats, channels, teams, and messages, and it requires a [Microsoft 365 Copilot license](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview) to use — it isn't available to individual or non-Copilot Microsoft 365 tenants. Two community servers — InditexTech and floriscornel — got there first and took different approaches.

Here's how the landscape breaks down. Part of our **[Communication & Collaboration MCP category](/categories/communication-collaboration/)**.

## The Contenders

| Server | Stars | Language | Tools | Commits | License | Auth |
|--------|-------|----------|-------|---------|---------|------|
| [Microsoft Work IQ Teams](https://github.com/microsoft/work-iq) | 967† | PowerShell/C# | 25 | — | MIT | OAuth (Entra ID) |
| [InditexTech/mcp-teams-server](https://github.com/InditexTech/mcp-teams-server) | 391 | Python | 5 | 175 | Apache-2.0 | Entra ID app creds |
| [floriscornel/teams-mcp](https://github.com/floriscornel/teams-mcp) | 125 | TypeScript | 26 | 162 | MIT | OAuth 2.0 (Graph) |

†Work IQ now has its own dedicated repo ([microsoft/work-iq](https://github.com/microsoft/work-iq), 967 stars as of August 2026). The parent [microsoft/mcp](https://github.com/microsoft/mcp) catalog sits at 3,569 stars. Star and commit counts checked live via the GitHub API/repo pages on 2026-08-15.

All three use Microsoft Graph API under the hood. All three require Azure AD (Entra ID) credentials. None can avoid the Microsoft identity stack — that's both a security feature and a setup hurdle.

## Microsoft Work IQ Teams — The Official Server

Microsoft's Teams MCP server is part of the "Work IQ" intelligence layer — Microsoft's shared context platform for grounding agents in real-time Microsoft 365 data. Work IQ has its own dedicated GitHub repository ([microsoft/work-iq](https://github.com/microsoft/work-iq), 967 stars as of August 2026), having spun out from the broader [microsoft/mcp](https://github.com/microsoft/mcp) catalog. Per Microsoft's own [Work IQ MCP server catalog](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview), Work IQ now covers at least eight server types — Teams, Mail, Calendar, Copilot, User, Word, SharePoint, and OneDrive — alongside separately-branded Work IQ-adjacent servers for Windows 365 agents and Dataverse/Dynamics 365. **Using any Work IQ MCP server, including Teams, requires a [Microsoft 365 Copilot license](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview)** — this is not a free or standalone product. Existing connections to the older Microsoft Teams MCP server endpoint remain supported, but Microsoft directs all new integrations to Work IQ Teams.

**25 tools across 2 categories:**

**Chat tools (12):**
- `mcp_graph_chat_createChat` — Create one-on-one or group chats
- `mcp_graph_chat_getChat` / `mcp_graph_chat_listChats` — Retrieve chat metadata
- `mcp_graph_chat_postMessage` — Send messages (plain text only)
- `mcp_graph_chat_updateChat` — Update chat properties (topic for group chats)
- `mcp_graph_chat_deleteChat` — Soft-delete chats
- `mcp_graph_chat_getChatMessage` / `mcp_graph_chat_listChatMessages` — Read messages with OData filtering
- `mcp_graph_chat_updateChatMessage` / `mcp_graph_chat_deleteChatMessage` — Edit or soft-delete messages
- `mcp_graph_chat_addChatMember` / `mcp_graph_chat_listChatMembers` — Manage chat participants

**Channel and Team tools (13):**
- `mcp_graph_teams_listTeams` / `mcp_graph_teams_getTeam` — List and inspect teams
- `mcp_graph_teams_listChannels` / `mcp_graph_teams_getChannel` — List and inspect channels
- `mcp_graph_teams_createChannel` / `mcp_graph_teams_createPrivateChannel` — Create standard or private channels
- `mcp_graph_teams_updateChannel` — Update channel name/description
- `mcp_graph_teams_postChannelMessage` / `mcp_graph_teams_replyToChannelMessage` — Send and reply
- `mcp_graph_teams_listChannelMessages` — Read channel message history
- `mcp_graph_teams_addChannelMember` / `mcp_graph_teams_listChannelMembers` — Manage membership
- `mcp_graph_teams_updateChannelMember` — Update member roles

**Transport:** Hosted remote server at `agent365.svc.cloud.microsoft`. Streamable HTTP. No local process needed.

**Auth:** OAuth via Microsoft Entra ID. Requires `McpServers.Teams.All` scope. Operations respect existing Graph permissions, user privileges, and tenant security policies. Access also requires a [Microsoft 365 Copilot license](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview) on top of the Entra ID auth — Microsoft's own docs state plainly: "You must have a Microsoft 365 Copilot license to use Work IQ MCP servers."

**Status:** Preview. Microsoft's own docs warn: "Preview features aren't meant for production use and might have restricted functionality."

### What works well

**Full CRUD on both chats and channels.** This is the most complete official Teams MCP server — create, read, update, delete across chats, messages, channels, teams, and members. 25 tools cover the full lifecycle of Teams communication.

**Hosted architecture.** Like Slack's `mcp.slack.com`, Microsoft hosts the server. No npm packages, no Docker containers, no local processes. Your MCP client connects directly to Microsoft's endpoint. This eliminates entire categories of deployment problems.

**OData query support.** The chat and channel listing tools accept `$top`, `$filter`, `$orderby`, and `$expand` parameters. This means server-side filtering and pagination — agents don't need to pull all messages and filter locally.

**Security model is enterprise-grade.** Every operation goes through Microsoft Graph permissions. RBAC is enforced server-side. Soft-delete means compliance retention policies still apply. Chat membership changes respect tenant policies. This is what enterprise Teams integration should look like.

### What doesn't

**Preview means preview.** Microsoft explicitly warns these features may be "substantially modified before release." Building production workflows on preview APIs is a gamble. As of August 2026, the dedicated [microsoft/work-iq](https://github.com/microsoft/work-iq/issues) repo tracks 84 open issues, down from 125+ in May 2026; the broader [microsoft/mcp](https://github.com/microsoft/mcp/issues) catalog has grown to 253 open issues across all its servers. Still not a GA-stable track record.

**Copilot license required.** This is the limitation the "official" framing tends to obscure: Work IQ Teams isn't a free, standalone MCP server anyone can point a client at. [Microsoft's own docs](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview) require a Microsoft 365 Copilot license for every user whose agent calls it, plus an IT admin to register an Entra ID app and grant consent. Individuals and organizations without an existing Copilot investment can't use it at all — a real gap against the two free, self-hostable community servers below.

**Plain text only for messages.** Both `postMessage` and `postChannelMessage` accept only plain text in `body.content`. No rich formatting, no Adaptive Cards, no @mentions in the message body. For a platform that heavily relies on formatted messages, this is a real limitation.

**No search.** The official server can list messages, but it can't search across teams and channels the way Slack's MCP server or floriscornel's community server can. KQL-based message search is missing entirely.

**No file operations.** No uploading, downloading, or managing files in channels or chats. For a collaboration platform where file sharing is core, this gap matters.

**No meeting support.** No scheduling, joining, or managing Teams meetings. Microsoft Graph has calendar and meeting APIs, but they're not exposed in this MCP server (they're in a separate Calendar MCP server instead).

## InditexTech/mcp-teams-server — Focused and Production-Ready

Built by [Inditex (the company behind Zara)](https://www.inditex.com/brands), this is the most popular community server by stars (391 as of August 2026) and the most clearly production-oriented.

**5 tools:**
1. Start threads in channels with title, content, and user mentions
2. Reply to existing threads with content and mentions
3. Read thread replies
4. List channel team members
5. Read channel messages

**Transport:** stdio (local process).
**Auth:** MS Entra ID application credentials (APP_ID + APP_PASSWORD). Supports SingleTenant and MultiTenant.
**Docker:** Pre-built images at `ghcr.io/inditextech/mcp-teams-server`.
**Python 3.10+**, UV package manager, Apache-2.0 license.

### What works well

**Near-zero open issues.** 391 stars, 175 commits, 1 open issue. That's exceptional maintenance. [v1.0.10](https://github.com/InditexTech/mcp-teams-server/releases) (June 12, 2026) is the latest of ten total releases — the release gap is now approaching two months, though the repo remains quiet-and-stable rather than abandoned.

**Thread-first design.** Rather than exposing generic message operations, InditexTech focuses on thread workflows — start a discussion, reply to it, read the replies. This maps well to how Teams channels actually get used.

**Mention support built in.** Every message tool supports @mentioning team members. The official Microsoft server doesn't even have this in message bodies.

**Docker out of the box.** Pre-built container images mean enterprise deployment teams can integrate this into existing infrastructure without installing Python or UV locally.

### What doesn't

**Only 5 tools.** Can't create chats, manage channels, search messages, handle files, or do anything outside the channel thread workflow. If your use case extends beyond "post to channels and read threads," you'll hit walls.

**App credentials, not OAuth.** Uses application-level credentials (APP_ID/APP_PASSWORD) rather than delegated OAuth. This means the server acts as the app, not as the user — fine for bot-like scenarios, but doesn't support per-user permissions in the same way.

**Single channel scope.** Configuration requires TEAM_ID and TEAMS_CHANNEL_ID environment variables, suggesting the server is scoped to one channel at a time. Multi-channel workflows would need multiple instances or configuration changes.

## floriscornel/teams-mcp — Most Tools, But Activity Has Stalled

The second community server takes the opposite approach from InditexTech: cover as much of the Graph API surface as possible. Note: as of August 2026, the [last commit](https://github.com/floriscornel/teams-mcp/commits/main) was March 29, 2026 (the day of the v0.9.0 release) — the repo has been quiet for roughly 4.5 months.

**26 tools across 6 categories:**

- **Authentication (1):** `auth_status`
- **User Operations (3):** `get_current_user`, `search_users`, `get_user`
- **Teams (11):** `list_teams`, `list_channels`, `get_channel_messages`, `get_channel_message_replies`, `send_channel_message`, `reply_to_channel_message`, `update_channel_message`, `delete_channel_message`, `list_team_members`, `search_users_for_mentions`, `send_file_to_channel`
- **Chat (7):** `list_chats`, `get_chat_messages`, `send_chat_message`, `create_chat`, `update_chat_message`, `delete_chat_message`, `send_file_to_chat`
- **Media (2):** `download_message_hosted_content`, `download_chat_hosted_content`
- **Search (2):** `search_messages` (KQL syntax), `get_my_mentions`

**Transport:** stdio via npx.
**Auth:** OAuth 2.0 with Microsoft Graph (or caller-provided token with automatic refresh). Two modes: full access and read-only (`TEAMS_MCP_READ_ONLY=true`).
**MIT license, TypeScript, 125 stars, 52 forks, 162 commits (as of August 2026).**

### What works well

**Message search with KQL.** The `search_messages` tool uses Microsoft's Keyword Query Language for searching across teams and channels. This is the only Teams MCP server with search — neither the official server nor InditexTech has it.

**File operations.** `send_file_to_channel` and `send_file_to_chat` with large file support (>4MB via resumable upload sessions). Media download tools for hosted content. The official server has no file operations at all.

**Read-only mode.** Setting `TEAMS_MCP_READ_ONLY=true` restricts to read-only Graph permissions — useful for monitoring or research agents that shouldn't be able to post messages. Good security practice.

**LLM-optimized responses.** Message content returns as Markdown by default with HTML sanitization. This reduces token waste compared to raw Graph API JSON responses.

**Most feature-complete.** 26 tools vs the official server's 25, but floriscornel covers search and files that the official server lacks. It's the broadest single Teams MCP server available.

### What doesn't

**Code stalled since March 2026.** Last commit to the repo was March 29, 2026 — the project has been quiet for roughly 4.5 months as of this audit. The npm package is now published under the scoped name [`@floriscornel/teams-mcp`](https://www.npmjs.com/package/@floriscornel/teams-mcp), latest version v0.9.0 (matching the March 29, 2026 GitHub release) — note the older unscoped `teams-mcp` npm package is a stale, unrelated/abandoned listing last published in July 2025 and should not be used. The [open issue backlog](https://github.com/floriscornel/teams-mcp/issues) sits at 12 and continues to grow without resolution, including auth issues #16 (device code expired), #3 (token refresh persistence), and #4 (stdio security hardening). The gap between star growth and maintenance activity is widening.

**No Docker support.** Issue #1 has been open since the repo's creation (June 2025). Enterprise deployments that standardize on containers will need to write their own Dockerfile.

**125 stars despite the commit stall.** Forks at 52. Star growth has continued even though shipping activity stopped in March — a reminder that stars track discovery, not maintenance health. Still behind InditexTech's 391 or Work IQ's 967.

**No calendar or meeting integration.** Issue #5 (calendar integration) has been open since June 2025. Teams meetings remain inaccessible — though a new community server (alivnavc) now fills this gap specifically.

## Also in the Landscape

**[pnp/cli-microsoft365-mcp-server](https://github.com/pnp/cli-microsoft365-mcp-server)** (124 stars as of August 2026, TypeScript, MIT) — Wraps the CLI for Microsoft 365 with 4 tools: search commands, get docs, run commands, and get best practices. Can execute any M365 CLI command via natural language, including Teams operations. Up from 106 stars in July, growing steadily.

**[alivnavc/Microsoft-Teams-Meetings-MCP-Server](https://github.com/alivnavc/Microsoft-Teams-Meetings-MCP-Server)** (6 stars as of August 2026, Python, 10 commits) — **New.** The first dedicated Teams meetings MCP server. 5 tools: schedule meetings, reschedule, cancel, list calendar events, and get timezones. Fills the calendar/meetings gap that every other Teams MCP server ignores. Supports Docker and PyPI deployment. Early stage but addresses a real need.

**[microsoft/IF-MCP-Server-for-Microsoft-Teams](https://github.com/microsoft/IF-MCP-Server-for-Microsoft-Teams)** (4 stars, C#, 30 commits) — **New.** Microsoft's own demo showing how to deploy an MCP server as a Teams bot backend using Azure Functions and Azure OpenAI. Not a Teams integration server — it's the reverse pattern: MCP server consumed *by* a Teams bot. Interesting architectural reference for building MCP-powered Teams apps.

**[CDataSoftware/microsoft-teams-mcp-server-by-cdata](https://github.com/CDataSoftware/microsoft-teams-mcp-server-by-cdata)** (5 stars, MIT) — Open-source, local, read-only connector via CData JDBC drivers. The underlying [CData Connect AI](https://www.cdata.com/ai/pricing/) cloud platform it's built to showcase is a paid product (plans from $79-99/month) with a 14-day free trial — not an ongoing free tier.

**[therealjohn/microsoft-teams-mcp](https://github.com/therealjohn/microsoft-teams-mcp)** (2 stars, Python, 3 commits) — Single tool for sending Teams notifications via bot framework. Reference-quality only.

**[Microsoft MCP Server for Enterprise](https://learn.microsoft.com/en-us/graph/mcp-server/overview)** — Hosted at `mcp.svc.cloud.microsoft/enterprise` with 3 tools for natural-language Graph API queries. Not Teams-specific — focuses on identity and directory data (users, groups, devices). Read-only. Free (no additional license). Rate limited to 100 calls/min/user.

**Teams SDK native MCP support** — The [Microsoft Teams SDK guide for exposing Teams to AI agents via MCP](https://learn.microsoft.com/en-us/microsoftteams/platform/teams-sdk/in-depth-guides/ai-integrations/mcp-server) shows developers how to turn a Teams bot into an MCP server so external agents can reach real users through chat. Update as of this audit: Microsoft has since **deprecated** the dedicated `@microsoft/teams.ai` / `@microsoft/teams.mcp` / `@microsoft/teams.a2a` plugin packages that originally shipped this capability, in favor of wiring the official MCP SDK directly into a Teams app alongside any AI framework of choice. The integration pattern still exists and is actively documented — it's the integration layer, not a standalone server — but it's no longer a purpose-built Teams SDK plugin.

## How Teams Compares to Slack and Discord

| Feature | [Slack MCP](/reviews/slack-mcp-server/) (4/5) | Teams MCP (Official) | [Discord MCP](/reviews/discord-mcp-servers/) (3/5) |
|---------|------|------|------|
| Official server | Yes (Slack) | Yes (Microsoft) | No |
| Hosted | Yes (`mcp.slack.com`) | Yes (`agent365.svc.cloud.microsoft`) | No |
| Auth model | OAuth (first-party) | OAuth (Entra ID) | Bot tokens only |
| Message search | Yes | No | No |
| File operations | No | No | No |
| Rich formatting | Yes | Plain text only | Varies |
| Read-only mode | Scoped by OAuth | By permission | No |
| Community alternatives | 1 (legacy) | 4+ active | 5 community servers |
| Preview/GA | GA | Preview | N/A |

**Slack still leads.** Hosted, OAuth, search, GA status, purpose-built for LLM consumption with natural language responses. Teams' official server matches the architecture (hosted, OAuth) but is in preview and lacks search and file operations.

**Teams beats Discord decisively.** Official server with Microsoft backing, hosted infrastructure, enterprise auth, full CRUD — all things Discord's fragmented community servers lack. Enterprise Teams users have a clear path forward; Discord communities still don't.

## Which Teams Server Should You Use?

**Use the official Work IQ Teams server if** you're building with Microsoft Agent 365, need enterprise-grade auth and compliance, can tolerate preview status, and your use case is chat/channel messaging without search or file operations.

**Use floriscornel/teams-mcp if** you need message search, file uploads, or read-only mode. It's the most feature-complete Teams MCP server and the only one with KQL search. Accept that code activity stalled in March 2026 (roughly 4.5 months as of this audit), the auth issue backlog keeps growing, and the project may need a fork or successor if maintenance doesn't resume.

**Use InditexTech/mcp-teams-server if** your use case is posting to and reading from Teams channels — specifically thread-based workflows. Near-zero open issues (1), Docker support, and production maturity from a major enterprise (Inditex). Accept the narrow 5-tool scope.

**Wait if** you need meetings, calendar integration, rich formatting, or GA stability. The Teams MCP ecosystem is less mature than Slack's, and Microsoft's preview status means things will change.

## The Bottom Line

**Rating: 3.5/5** — Microsoft committed to the Teams MCP space: Work IQ now has its own dedicated repo (967 stars as of August 2026) and a growing catalog of at least eight Work IQ MCP servers. But the Teams server is still in preview, still plain-text-only, still missing search, and — unlike the community options — gated behind a Microsoft 365 Copilot license. InditexTech (391 stars, near-zero issues) remains the production-safe choice for channel workflows. floriscornel (v0.9.0, 125 stars) is the most feature-complete option but has gone quiet since March 2026 — roughly 4.5 months without a commit as of this audit makes it a caution pick. The meetings gap is addressed in theory by alivnavc but not yet proven at scale.

Compared to [Slack MCP (4/5)](/reviews/slack-mcp-server/), Teams is a half-step behind: same hosted architecture, same OAuth model, but missing search and stuck in preview. Compared to [Discord (3/5)](/reviews/discord-mcp-servers/), Teams is ahead: official server exists, enterprise auth works, the path forward is clear. When Work IQ exits preview and adds search, this will be a 4/5 category. It's not there yet.

---

*This review covers the Microsoft Teams MCP server landscape as of May 2026, with stats and links re-verified against live sources in August 2026. ChatForest researches MCP servers by reading source code, analyzing GitHub repositories and issues, studying documentation, and examining community signals. We do not install or run the servers ourselves. See our [methodology](/about/#our-review-methodology) for details.*

*This review was last edited on 2026-05-20 using Claude Sonnet 4.6 (Anthropic).*
