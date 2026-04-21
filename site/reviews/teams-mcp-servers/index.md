# Microsoft Teams MCP Servers — Official at Last, Community Got There First

> Microsoft now has an official Teams MCP server with 24 tools for chats, channels, and members. Two community servers were there first. Here's how they compare and which one to pick.


Microsoft Teams has 320 million monthly active users. It's the default communication tool in enterprise environments — the place where decisions get made, meetings get scheduled, and institutional knowledge goes to die in unread channels.

Unlike Discord (which still has [no official MCP server](/reviews/discord-mcp-servers/)), Microsoft shipped one. The official Work IQ Teams server, now rebranded under Microsoft's "Work IQ" intelligence layer and part of the [microsoft/mcp](https://github.com/microsoft/mcp) catalog (3,000 stars across all Microsoft MCP servers), provides 24 tools for full CRUD operations on chats, channels, teams, and messages. Two community servers — InditexTech and floriscornel — got there first and took different approaches.

Here's how the landscape breaks down. Part of our **[Communication & Collaboration MCP category](/categories/communication-collaboration/)**.

## The Contenders

| Server | Stars | Language | Tools | Commits | License | Auth |
|--------|-------|----------|-------|---------|---------|------|
| [Microsoft Work IQ Teams](https://github.com/microsoft/mcp) | 3,000* | C# | 24 | 1,681* | — | OAuth (Entra ID) |
| [InditexTech/mcp-teams-server](https://github.com/InditexTech/mcp-teams-server) | 368 | Python | 5 | 145 | Apache-2.0 | Entra ID app creds |
| [floriscornel/teams-mcp](https://github.com/floriscornel/teams-mcp) | 87 | TypeScript | 26 | 162 | MIT | OAuth 2.0 (Graph) |

*Stars and commits are for the entire microsoft/mcp catalog, not the Teams server alone.

All three use Microsoft Graph API under the hood. All three require Azure AD (Entra ID) credentials. None can avoid the Microsoft identity stack — that's both a security feature and a setup hurdle.

## Microsoft Work IQ Teams — The Official Server

Microsoft's own Teams MCP server is part of the broader "Microsoft Agent 365" platform and the [microsoft/mcp](https://github.com/microsoft/mcp) catalog alongside servers for Mail, Calendar, Copilot Chat, Azure DevOps, Fabric, and more. As of April 2026, Microsoft has consolidated its MCP branding under "Work IQ" — the intelligence layer that grounds Microsoft 365 Copilot and agents in real-time shared context. Existing connections to the older Microsoft Teams MCP server remain supported, but Microsoft directs all new integrations to Work IQ Teams.

**24 tools across 2 categories:**

**Chat tools (12):**
- `mcp_graph_chat_createChat` — Create one-on-one or group chats
- `mcp_graph_chat_getChat` / `mcp_graph_chat_listChats` — Retrieve chat metadata
- `mcp_graph_chat_postMessage` — Send messages (plain text only)
- `mcp_graph_chat_updateChat` — Update chat properties (topic for group chats)
- `mcp_graph_chat_deleteChat` — Soft-delete chats
- `mcp_graph_chat_getChatMessage` / `mcp_graph_chat_listChatMessages` — Read messages with OData filtering
- `mcp_graph_chat_updateChatMessage` / `mcp_graph_chat_deleteChatMessage` — Edit or soft-delete messages
- `mcp_graph_chat_addChatMember` / `mcp_graph_chat_listChatMembers` — Manage chat participants

**Channel and Team tools (12):**
- `mcp_graph_teams_listTeams` / `mcp_graph_teams_getTeam` — List and inspect teams
- `mcp_graph_teams_listChannels` / `mcp_graph_teams_getChannel` — List and inspect channels
- `mcp_graph_teams_createChannel` / `mcp_graph_teams_createPrivateChannel` — Create standard or private channels
- `mcp_graph_teams_updateChannel` — Update channel name/description
- `mcp_graph_teams_postChannelMessage` / `mcp_graph_teams_replyToChannelMessage` — Send and reply
- `mcp_graph_teams_listChannelMessages` — Read channel message history
- `mcp_graph_teams_addChannelMember` / `mcp_graph_teams_listChannelMembers` — Manage membership
- `mcp_graph_teams_updateChannelMember` — Update member roles

**Transport:** Hosted remote server at `agent365.svc.cloud.microsoft`. Streamable HTTP. No local process needed.

**Auth:** OAuth via Microsoft Entra ID. Requires `McpServers.Teams.All` scope. Operations respect existing Graph permissions, user privileges, and tenant security policies.

**Status:** Preview. Microsoft's own docs warn: "Preview features aren't meant for production use and might have restricted functionality."

### What works well

**Full CRUD on both chats and channels.** This is the most complete official Teams MCP server — create, read, update, delete across chats, messages, channels, teams, and members. 24 tools cover the full lifecycle of Teams communication.

**Hosted architecture.** Like Slack's `mcp.slack.com`, Microsoft hosts the server. No npm packages, no Docker containers, no local processes. Your MCP client connects directly to Microsoft's endpoint. This eliminates entire categories of deployment problems.

**OData query support.** The chat and channel listing tools accept `$top`, `$filter`, `$orderby`, and `$expand` parameters. This means server-side filtering and pagination — agents don't need to pull all messages and filter locally.

**Security model is enterprise-grade.** Every operation goes through Microsoft Graph permissions. RBAC is enforced server-side. Soft-delete means compliance retention policies still apply. Chat membership changes respect tenant policies. This is what enterprise Teams integration should look like.

### What doesn't

**Preview means preview.** Microsoft explicitly warns these features may be "substantially modified before release." Building production workflows on preview APIs is a gamble. The microsoft/mcp repo has 207 open issues across all its servers (down slightly from 214 in March, suggesting some triage but no major cleanup).

**Plain text only for messages.** Both `postMessage` and `postChannelMessage` accept only plain text in `body.content`. No rich formatting, no Adaptive Cards, no @mentions in the message body. For a platform that heavily relies on formatted messages, this is a real limitation.

**No search.** The official server can list messages, but it can't search across teams and channels the way Slack's MCP server or floriscornel's community server can. KQL-based message search is missing entirely.

**No file operations.** No uploading, downloading, or managing files in channels or chats. For a collaboration platform where file sharing is core, this gap matters.

**No meeting support.** No scheduling, joining, or managing Teams meetings. Microsoft Graph has calendar and meeting APIs, but they're not exposed in this MCP server (they're in a separate Calendar MCP server instead).

## InditexTech/mcp-teams-server — Focused and Production-Ready

Built by Inditex (the company behind Zara), this is the most popular community server by stars (368) and the most clearly production-oriented.

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

**Near-zero open issues.** 368 stars, 145 commits, 1 open issue. That's exceptional maintenance. The v1.0.8 release (March 2026) continues a steady cadence of versioned releases (9 total).

**Thread-first design.** Rather than exposing generic message operations, InditexTech focuses on thread workflows — start a discussion, reply to it, read the replies. This maps well to how Teams channels actually get used.

**Mention support built in.** Every message tool supports @mentioning team members. The official Microsoft server doesn't even have this in message bodies.

**Docker out of the box.** Pre-built container images mean enterprise deployment teams can integrate this into existing infrastructure without installing Python or UV locally.

### What doesn't

**Only 5 tools.** Can't create chats, manage channels, search messages, handle files, or do anything outside the channel thread workflow. If your use case extends beyond "post to channels and read threads," you'll hit walls.

**App credentials, not OAuth.** Uses application-level credentials (APP_ID/APP_PASSWORD) rather than delegated OAuth. This means the server acts as the app, not as the user — fine for bot-like scenarios, but doesn't support per-user permissions in the same way.

**Single channel scope.** Configuration requires TEAM_ID and TEAMS_CHANNEL_ID environment variables, suggesting the server is scoped to one channel at a time. Multi-channel workflows would need multiple instances or configuration changes.

## floriscornel/teams-mcp — Most Tools, Broadest Coverage

The second community server takes the opposite approach from InditexTech: cover as much of the Graph API surface as possible.

**26 tools across 6 categories:**

- **Authentication (1):** `auth_status`
- **User Operations (3):** `get_current_user`, `search_users`, `get_user`
- **Teams (11):** `list_teams`, `list_channels`, `get_channel_messages`, `get_channel_message_replies`, `send_channel_message`, `reply_to_channel_message`, `update_channel_message`, `delete_channel_message`, `list_team_members`, `search_users_for_mentions`, `send_file_to_channel`
- **Chat (7):** `list_chats`, `get_chat_messages`, `send_chat_message`, `create_chat`, `update_chat_message`, `delete_chat_message`, `send_file_to_chat`
- **Media (2):** `download_message_hosted_content`, `download_chat_hosted_content`
- **Search (2):** `search_messages` (KQL syntax), `get_my_mentions`

**Transport:** stdio via npx.
**Auth:** OAuth 2.0 with Microsoft Graph (or caller-provided token with automatic refresh). Two modes: full access and read-only (`TEAMS_MCP_READ_ONLY=true`).
**MIT license, TypeScript, 87 stars, 41 forks, 162 commits.**

### What works well

**Message search with KQL.** The `search_messages` tool uses Microsoft's Keyword Query Language for searching across teams and channels. This is the only Teams MCP server with search — neither the official server nor InditexTech has it.

**File operations.** `send_file_to_channel` and `send_file_to_chat` with large file support (>4MB via resumable upload sessions). Media download tools for hosted content. The official server has no file operations at all.

**Read-only mode.** Setting `TEAMS_MCP_READ_ONLY=true` restricts to read-only Graph permissions — useful for monitoring or research agents that shouldn't be able to post messages. Good security practice.

**LLM-optimized responses.** Message content returns as Markdown by default with HTML sanitization. This reduces token waste compared to raw Graph API JSON responses.

**Most feature-complete.** 25 tools vs the official server's 24, but floriscornel covers search and files that the official server lacks. It's the broadest single Teams MCP server available.

### What doesn't

**11 open issues including auth problems.** Issue count grew from 8 to 11. Issue #16 (device code expired during auth), #3 (token refresh persistence), and #4 (stdio security hardening) remain open. For an OAuth-based server, auth reliability is critical, and the growing issue backlog suggests maintenance isn't keeping pace with adoption.

**No Docker support.** Issue #1 has been open since the repo's creation (June 2025). Enterprise deployments that standardize on containers will need to write their own Dockerfile.

**87 stars — growing fast but still niche.** Up 38% from 63 in March, with forks jumping from 32 to 41. PulseMCP shows 14.7K all-time visitors and 702 weekly (#1,442 globally). Adoption is accelerating but still well behind InditexTech's 368 or the microsoft/mcp catalog's 3,000.

**No calendar or meeting integration.** Issue #5 (calendar integration) has been open since June 2025. Teams meetings remain inaccessible — though a new community server (alivnavc) now fills this gap specifically.

## Also in the Landscape

**[pnp/cli-microsoft365-mcp-server](https://github.com/pnp/cli-microsoft365-mcp-server)** (101 stars, TypeScript, MIT) — Wraps the CLI for Microsoft 365 with 4 tools: search commands, get docs, run commands, and get best practices. Can execute any M365 CLI command via natural language, including Teams operations. Up from 87 stars and 3 tools in March — growing steadily with GitHub Copilot integration support.

**[alivnavc/Microsoft-Teams-Meetings-MCP-Server](https://github.com/alivnavc/Microsoft-Teams-Meetings-MCP-Server)** (4 stars, Python, 10 commits) — **New.** The first dedicated Teams meetings MCP server. 5 tools: schedule meetings, reschedule, cancel, list calendar events, and get timezones. Fills the calendar/meetings gap that every other Teams MCP server ignores. Supports Docker and PyPI deployment. Early stage but addresses a real need.

**[microsoft/IF-MCP-Server-for-Microsoft-Teams](https://github.com/microsoft/IF-MCP-Server-for-Microsoft-Teams)** (4 stars, C#, 30 commits) — **New.** Microsoft's own demo showing how to deploy an MCP server as a Teams bot backend using Azure Functions and Azure OpenAI. Not a Teams integration server — it's the reverse pattern: MCP server consumed *by* a Teams bot. Interesting architectural reference for building MCP-powered Teams apps.

**[CDataSoftware/microsoft-teams-mcp-server-by-cdata](https://github.com/CDataSoftware/microsoft-teams-mcp-server-by-cdata)** — Read-only access via CData JDBC drivers. Commercial product (CData Connect AI) with a free read-only tier.

**[therealjohn/microsoft-teams-mcp](https://github.com/therealjohn/microsoft-teams-mcp)** (2 stars, Python, 3 commits) — Single tool for sending Teams notifications via bot framework. Reference-quality only.

**[Microsoft MCP Server for Enterprise](https://learn.microsoft.com/en-us/graph/mcp-server/overview)** — Hosted at `mcp.svc.cloud.microsoft/enterprise` with 3 tools for natural-language Graph API queries. Not Teams-specific — focuses on identity and directory data (users, groups, devices). Read-only. Free (no additional license). Rate limited to 100 calls/min/user.

**Teams SDK native MCP support** — As of April 2026, the [Microsoft Teams SDK](https://learn.microsoft.com/en-us/microsoftteams/platform/teams-sdk/in-depth-guides/ai/mcp/mcp-server) has optional packages supporting MCP as both server and client, allowing developers to expose MCP tools directly from Teams apps or consume MCP servers within them. This is the integration layer, not a standalone server — but it signals Microsoft embedding MCP deeply into the Teams developer platform.

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

**Use floriscornel/teams-mcp if** you need message search, file uploads, or read-only mode. It's the most feature-complete Teams MCP server and the only one with KQL search. Accept that it's community-maintained with 87 stars and a growing backlog of auth issues (11 open).

**Use InditexTech/mcp-teams-server if** your use case is posting to and reading from Teams channels — specifically thread-based workflows. Zero open issues, Docker support, and production maturity from a major enterprise (Inditex). Accept the narrow 5-tool scope.

**Wait if** you need meetings, calendar integration, rich formatting, or GA stability. The Teams MCP ecosystem is less mature than Slack's, and Microsoft's preview status means things will change.

## The Bottom Line

**Rating: 3.5/5** — Microsoft did the right thing shipping an official hosted Teams MCP server with 24 tools, enterprise auth, and full CRUD for chats and channels. The Work IQ rebranding and Teams SDK native MCP support show Microsoft is embedding MCP deeply into the platform — but the server itself is still in preview, still lacks search and file operations, and still only supports plain text messages. The community servers fill real gaps — floriscornel adds search and files (now 87 stars, up 38%), InditexTech adds production polish and Docker (368 stars, still near-zero issues), and a new meetings server from alivnavc addresses the calendar blind spot. Together they cover what Teams integration needs, but no single server nails it yet.

Compared to [Slack MCP (4/5)](/reviews/slack-mcp-server/), Teams is a half-step behind: same hosted architecture, same OAuth model, but missing search and stuck in preview. Compared to [Discord (3/5)](/reviews/discord-mcp-servers/), Teams is ahead: official server exists, enterprise auth works, the path forward is clear. When the official server exits preview and adds search, this will be a 4/5 category. It's not there yet.

---

*This review covers the Microsoft Teams MCP server landscape as of April 2026. ChatForest researches MCP servers by reading source code, analyzing GitHub repositories and issues, studying documentation, and examining community signals. We do not install or run the servers ourselves. See our [methodology](/about/#our-review-methodology) for details.*

*This review was last edited on 2026-04-21 using Claude Opus 4.6 (Anthropic).*

