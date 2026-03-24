---
title: "Outlook MCP Servers — Microsoft's Enterprise Email Meets the Agent Era"
date: 2026-03-15T02:00:00+09:00
description: "Outlook MCP servers let AI agents read, search, send, and manage Microsoft 365 email. We reviewed the landscape: Microsoft's official Work IQ server, the dominant community option (530 stars), and 5+ alternatives. Here's what works and what requires a Copilot license."
og_description: "Outlook MCP servers: Microsoft's official Work IQ Mail, Softeria's ms-365-mcp-server (530 stars), and 5+ community options. Rating: 3.5/5."
content_type: "Review"
card_description: "Outlook MCP servers — from Microsoft's official Work IQ Mail to community Graph API wrappers. Let agents manage enterprise email. The licensing requirements are significant."
last_refreshed: 2026-03-15
---

If [Gmail MCP servers](/reviews/gmail-mcp-servers/) deal with personal inboxes, Outlook MCP servers deal with corporate ones. Microsoft 365 mail sits behind Entra ID, compliance policies, Data Loss Prevention rules, and IT admin controls. That's the whole point — and it's what makes the MCP integration story more complicated than Gmail's.

The good news: Microsoft shipped official MCP servers for Outlook Mail and Calendar as part of their Work IQ platform. The bad news: they require a Microsoft 365 Copilot license (~$30/user/month) and are still in preview. Community servers fill the gap for everyone else. Part of our **[Communication & Collaboration MCP category](/categories/communication-collaboration/)**.

## The Landscape

| Server | Stars | Language | Mail Tools | Auth | License |
|--------|-------|----------|------------|------|---------|
| [Microsoft Work IQ Mail](https://github.com/microsoft/mcp) | 2,800* | C# | 10 | OAuth (Entra ID) | — |
| [Softeria/ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server) | 530 | TypeScript | 6+ | OAuth / Device Code | MIT |
| [ryaker/outlook-mcp](https://github.com/ryaker/outlook-mcp) | 278 | TypeScript | 6+ | OAuth (Graph) | — |
| [merill/lokka](https://github.com/merill/lokka) | 228 | TypeScript | via Graph | OAuth (multiple modes) | MIT |
| [ampcome-mcps/outlook-mcp](https://github.com/ampcome-mcps/outlook-mcp) | 1 | Python | 26 | Nango + Graph | MIT |
| [Abhishek-Aditya-bs/Outlook-MCP-Server](https://github.com/Abhishek-Aditya-bs/Outlook-MCP-Server) | 1 | Python | 2 | Windows COM | MIT |

\*Stars for the entire microsoft/mcp catalog, not the Mail server alone.

Every server in this ecosystem uses Microsoft Graph API — except one (Abhishek's, which uses local Outlook COM). That means every one requires Azure AD / Entra ID credentials. No shortcuts, no API keys, no personal access tokens. This is a feature for enterprise security teams and a hurdle for individual developers.

## Microsoft Work IQ Mail — The Official Server

Microsoft's own Mail MCP server is part of the broader [Work IQ](https://github.com/microsoft/work-iq) platform and the [microsoft/mcp](https://github.com/microsoft/mcp) catalog (2,800 stars across all Microsoft MCP servers). It ships alongside Work IQ servers for Calendar, Teams, Copilot Chat, SharePoint, and more.

**10 tools:**

| Tool | What it does |
|------|-------------|
| `createMessage` | Create a draft email (HTML or plain text) |
| `sendMail` | Send email with To/CC/BCC recipients |
| `sendDraft` | Send an existing draft by ID |
| `getMessage` | Retrieve a single message by ID |
| `listSent` | List messages in sent items |
| `searchMessages` | KQL-style search across subject, body, attachments |
| `reply` | Reply to an existing message |
| `replyAll` | Reply-all to an existing message |
| `updateMessage` | Update subject, body, categories, importance |
| `deleteMessage` | Delete a message with optional ETag concurrency |

**Transport:** Hosted remote server. No local process needed — your MCP client connects directly to Microsoft's infrastructure.

**Auth:** OAuth via Microsoft Entra ID. Operations respect existing Graph permissions, user privileges, and tenant security policies.

**Status:** Preview. Microsoft's docs explicitly state: "Preview features aren't meant for production use and might have restricted functionality."

### What works well

**KQL search is the standout.** The `searchMessages` tool uses Microsoft Graph Search API with Keyword Query Language. You can search across subject, body, and attachments with the same query syntax Outlook users already know. This is something [Gmail's community servers](/reviews/gmail-mcp-servers/) also offer, but having it in an official server with first-party indexing is a step up.

**Full email lifecycle.** Create drafts, update them, send them, reply, reply-all, delete — the 10 tools cover the complete email workflow. The draft-then-send pattern (`createMessage` → `sendDraft`) is useful for agents that should compose but not send without confirmation.

**Hosted architecture.** Like the [Work IQ Teams server](/reviews/teams-mcp-servers/), Microsoft hosts this. No npm packages to install, no Docker containers, no local token files. This eliminates deployment friction and means Microsoft handles updates.

**ETag concurrency control.** The `updateMessage` and `deleteMessage` tools support `If-Match` headers for optimistic concurrency. This prevents race conditions when multiple agents or users modify the same message — an enterprise-grade detail that community servers typically skip.

### What doesn't

**Copilot license required.** You need a Microsoft 365 Copilot license to use Work IQ MCP servers. At ~$30/user/month, this immediately prices out individual developers, small teams, and anyone who just wants Outlook MCP access without the full Copilot suite. The community servers exist largely because of this paywall.

**Preview means preview.** Just like the Teams server, Microsoft warns this may be "substantially modified before release." Building production email workflows on preview APIs is risky.

**No folder management.** You can't list folders, create folders, or move messages between folders. For users who rely on folder-based email organization, this is a gap.

**No attachment handling.** The tools can send emails and search attachments, but there's no dedicated tool for downloading or uploading attachments. This limits agent use cases around file extraction from emails.

**No contact integration.** Reading or managing Outlook contacts requires a separate server. The Mail server is strictly mail.

## Softeria/ms-365-mcp-server — The Community Standard

[ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server) (530 stars, 243 commits, MIT license) is the most popular community Outlook MCP server by a wide margin. Unlike Microsoft's mail-only server, Softeria covers the full Microsoft 365 suite through a single server.

**Supported services:**

- **Email** — list, send, delete, create drafts, move messages
- **Calendar** — manage events and calendar views
- **OneDrive** — file upload/download, folder operations
- **Excel** — worksheet and range operations
- **OneNote** — notebook and page management
- **Tasks** — To Do and Planner task management
- **Contacts** — Outlook contact operations
- **User Profile & Search** — directory and user queries

**With `--org-mode` flag (organizational accounts):**
- Teams & Chats, SharePoint, Online Meetings (transcripts/recordings), Shared Mailboxes, User Management

**Install:** `npx @softeria/ms-365-mcp-server`

**Auth:** Three modes — Device Code Flow (interactive, with token caching), OAuth Authorization Code (for HTTP transport), or Bring Your Own Token (for CI/CD or automated systems).

### What works well

**Breadth that no single Microsoft server matches.** One NPX command gives you email, calendar, files, tasks, contacts, Excel, OneNote, and more. Microsoft's approach splits these across separate Work IQ servers, each requiring its own setup. Softeria unifies them.

**TOON output format.** The experimental "Token-Oriented Object Notation" reduces token usage by 30-60% compared to standard JSON. For LLM integrations where every token costs money, this is a meaningful optimization that no other Outlook MCP server offers.

**Multi-account support.** A single server instance can manage multiple Microsoft 365 accounts simultaneously. Switch between personal and work accounts without reconfiguring.

**Read-only mode.** Start with `--read-only` to restrict all operations to safe reads. Useful for testing or building agents that should never modify data. Tool filtering adds another layer — you can expose only specific tools to specific agents.

**No Copilot license required.** Uses standard Microsoft Graph API permissions. Any Microsoft 365 account (including free personal accounts for some features) can authenticate.

### What doesn't

**13 open issues.** Active development means active bugs. Some issues relate to authentication edge cases and token refresh — the same category of problems that plague most Graph API integrations.

**Tool sprawl.** Covering 8+ Microsoft services means dozens of tools. If you only need email, you're loading calendar, OneDrive, Excel, and OneNote tools into your agent's context. The `--tools` flag mitigates this, but the default is everything.

**Node.js 20+ recommended.** Works with Node.js 14+ but with dependency warnings. The recommended version is higher than what many systems run.

## ryaker/outlook-mcp — Outlook + OneDrive + Power Automate

[outlook-mcp](https://github.com/ryaker/outlook-mcp) (278 stars, 74 commits) connects Outlook with OneDrive and Power Automate — a combination no other server offers.

**Covers three services:**

- **Outlook** — email list/search/send/read, calendar events, folder management, mail rules
- **OneDrive** — file upload/download, search, sharing
- **Power Automate** — list flows, trigger flows, view run history

**Auth:** OAuth 2.0 through Microsoft Graph. Tokens stored locally at `~/.outlook-mcp-tokens.json`.

**Setup:** Register an Azure app, configure permissions, run the auth server on port 3333, authenticate via browser.

### What works well

**Power Automate integration is unique.** No other Outlook MCP server connects to Power Automate. An agent that can read emails, process them, and trigger automation flows creates workflow possibilities that pure email servers can't match.

**Folder management and mail rules.** Unlike the official Work IQ server, ryaker supports creating folders, moving messages between folders, and managing Outlook mail rules. These are basic Outlook features that the official server lacks.

**Calendar included.** Accept/decline invitations, create events — calendar operations are bundled alongside email, which matches how Outlook users actually work.

### What doesn't

**Local token storage.** Tokens at `~/.outlook-mcp-tokens.json` are a security concern. Any process with file system access can read them. Softeria's approach of using OS credential stores is more secure.

**Complex setup.** Azure Portal app registration → environment variables → auth server → browser auth → Claude Desktop config. Five steps before your first email read. Community servers for other platforms (like Slack) have gotten this down to two.

**No license specified.** The repository doesn't clearly state its license. For enterprise use, this is a blocker — legal teams won't approve unlicensed dependencies.

## merill/lokka — The Graph API Swiss Army Knife

[Lokka](https://github.com/merill/lokka) (228 stars, MIT license) takes a different approach: instead of wrapping specific Microsoft services into dedicated tools, it exposes the Microsoft Graph API itself as an MCP tool.

**3 tools:**
1. `lokka-microsoft` — Call any Microsoft Graph or Azure API endpoint
2. `set-access-token` — Manage authentication tokens dynamically
3. `get-auth-status` — Check authentication status

**Why this matters:** Rather than "search emails" as a tool, Lokka's approach is "call any Graph API endpoint." Your agent constructs the Graph API query (`/me/messages?$search="subject:invoice"`) and Lokka executes it. This means every Graph API capability is available, including ones that purpose-built servers haven't implemented yet.

**Auth:** Four modes — interactive auth (personal or custom app), app-only auth (certificate or client secret), client-provided tokens, and API version control (beta vs. v1.0).

### When to consider it

Lokka is best for users who already know the Microsoft Graph API and want maximum flexibility. It's the opposite of Softeria's approach — instead of many purpose-built tools, you get one tool that can do anything. The tradeoff is that your agent needs to know how to construct Graph API queries, which means more complex prompts and more room for errors.

It's also strong for **Azure management** tasks — subscriptions, billing, resource management — that pure Outlook servers don't touch.

## Also in the Landscape

**[Abhishek-Aditya-bs/Outlook-MCP-Server](https://github.com/Abhishek-Aditya-bs/Outlook-MCP-Server)** — The only server that uses **local Outlook COM** instead of Graph API. Windows-only, requires Outlook desktop installed, uses pywin32 to access mailboxes directly. Two tools: check mailbox access and search email chains. Useful if you need to access local Outlook data without cloud connectivity, but the Windows-only + local Outlook requirement limits its audience severely.

**[ampcome-mcps/outlook-mcp](https://github.com/ampcome-mcps/outlook-mcp)** (1 star, MIT) — 26 tools covering email, contacts, calendar, and folders through Graph API. Uses Nango for credential management (no direct token storage). Comprehensive tool count but minimal adoption and community validation.

**[merajmehrabi/Outlook_Calendar_MCP](https://github.com/merajmehrabi/Outlook_Calendar_MCP)** — Windows-only calendar MCP server using local Outlook COM. Read and manage calendar events from the desktop app. Same limitations as the Abhishek server — Windows + local Outlook required.

**[kacase/mcp-outlook](https://github.com/kacase/mcp-outlook)** — Another Graph API wrapper for Outlook. Calendar events, email reading, message sending. Lower adoption.

**[microsoft/work-iq](https://github.com/microsoft/work-iq) CLI** (564 stars) — Not an MCP server per se, but a CLI/plugin for GitHub Copilot that queries Microsoft 365 data using natural language. "What's on my calendar tomorrow?" style queries. Requires Entra ID admin consent. Interesting for Copilot users, but not a general-purpose MCP server.

## How Outlook Compares to Gmail

| Feature | [Gmail MCP](/reviews/gmail-mcp-servers/) (3.5/5) | Outlook MCP (Official) | Outlook MCP (Softeria) |
|---------|------|------|------|
| Official server | Google Workspace MCP | Work IQ Mail | N/A |
| Hosted | Yes (`workspace-developer.goog`) | Yes (Work IQ) | No (local npx) |
| Auth model | OAuth | OAuth (Entra ID) | OAuth / Device Code / BYOT |
| Message search | Gmail query syntax | KQL search | Via Graph API |
| Folder management | Label management | No | Yes |
| Attachment handling | Limited | No | Via OneDrive tools |
| Calendar bundled | Separate server | Separate Work IQ server | Yes |
| License cost | Free (Google account) | Copilot license (~$30/mo) | Free (M365 account) |
| Community standard | taylorwilsdon (1,700 stars) | N/A | Softeria (530 stars) |
| Services covered | Gmail + 11 Google services | Mail only | 8+ M365 services |

**Gmail is more accessible.** No paid license requirement for MCP access, stronger community ecosystem (1,700-star dominant server vs 530), and Google's own endpoint works without Copilot licensing.

**Outlook has deeper enterprise integration.** Entra ID auth, compliance policy enforcement, tenant-level controls, DLP rules — the enterprise security infrastructure around Outlook is more mature. If your organization already has Microsoft 365 Copilot licenses, the official server is the obvious choice.

**Both have the same fundamental risk.** Email is sensitive data. Whether it's Gmail or Outlook, giving an agent send permissions deserves serious thought. Both ecosystems have the same gap: no official reference server from the MCP project (modelcontextprotocol/servers).

## Which Outlook Server Should You Use?

**Use Work IQ Mail if** your organization has Microsoft 365 Copilot licenses and you want official, hosted, Microsoft-supported email MCP access with KQL search. Accept preview status and the limited 10-tool scope.

**Use Softeria/ms-365-mcp-server if** you want the broadest Microsoft 365 coverage from a single server, don't have Copilot licenses, or need features like TOON token optimization, multi-account support, or read-only mode. This is the community standard for a reason — 530 stars, active maintenance, MIT license.

**Use ryaker/outlook-mcp if** you need Power Automate integration alongside email and calendar. The workflow automation angle is unique. Accept the more complex setup and local token storage.

**Use merill/lokka if** you know the Microsoft Graph API and want maximum flexibility. One tool that can do anything the API supports. Not for beginners.

**Wait if** you need GA-quality stability from Microsoft. The official servers are in preview and will change. If your workflow can't tolerate API modifications, the community servers (especially Softeria) are more stable bets despite not having Microsoft's backing.

## The Bottom Line

**Rating: 3.5/5** — Microsoft did the right thing shipping official Work IQ MCP servers for Outlook Mail and Calendar, with hosted architecture, KQL search, and enterprise-grade auth. But the Copilot license requirement creates a paywall that pushes most users to community alternatives. Softeria's ms-365-mcp-server (530 stars) fills that gap admirably — covering 8+ Microsoft services from a single install with no Copilot license needed, three auth modes, and a token-optimized output format.

The ecosystem is less mature than [Gmail's](/reviews/gmail-mcp-servers/) (no 1,700-star dominant server, no free official endpoint) but more coherent than [Teams'](/reviews/teams-mcp-servers/) — you have a clear decision tree between official (if you have licenses) and community (if you don't). When Microsoft removes the Copilot license requirement or exits preview, this category moves to 4/5. The enterprise security infrastructure is already there; it's the accessibility that's holding it back.

---

*This review covers the Microsoft Outlook MCP server landscape as of March 2026. ChatForest researches MCP servers by reading source code, analyzing GitHub repositories and issues, studying documentation, and examining community signals. We do not install or run the servers ourselves. See our [methodology](/about/#our-review-methodology) for details.*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
