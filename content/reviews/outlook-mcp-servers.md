---
title: "Outlook MCP Servers — Microsoft's Enterprise Email Meets the Agent Era"
date: 2026-03-15T02:00:00+09:00
description: "Outlook MCP servers let AI agents read, search, send, and manage Microsoft 365 email."
og_description: "Outlook MCP servers: Microsoft's official Work IQ Mail, Softeria's ms-365-mcp-server (639 stars, v0.85.0, 200+ tools), and 8+ community options. Rating: 3.5/5."
content_type: "Review"
card_description: "Outlook MCP servers — from Microsoft's official Work IQ Mail to community Graph API wrappers. Let agents manage enterprise email. Softeria now at 200+ tools covering full M365. Licensing paywall tightening."
last_refreshed: 2026-04-22
lastmod: 2026-04-22T18:00:00+09:00
---

If [Gmail MCP servers](/reviews/gmail-mcp-servers/) deal with personal inboxes, Outlook MCP servers deal with corporate ones. Microsoft 365 mail sits behind Entra ID, compliance policies, Data Loss Prevention rules, and IT admin controls. That's the whole point — and it's what makes the MCP integration story more complicated than Gmail's.

The good news: Microsoft shipped official MCP servers for Outlook Mail and Calendar as part of their Work IQ platform. The bad news: they require a Microsoft 365 Copilot license (~$30/user/month) and are still in preview — and as of April 15, 2026, Microsoft pulled back Copilot Chat access from M365 apps for large enterprise users without the full Copilot license, making the paywall even more relevant. Community servers fill the gap for everyone else — and Softeria's ms-365-mcp-server has exploded to 200+ tools and v0.85.0. Part of our **[Communication & Collaboration MCP category](/categories/communication-collaboration/)**.

## The Landscape

| Server | Stars | Language | Mail Tools | Auth | License |
|--------|-------|----------|------------|------|---------|
| [Microsoft Work IQ Mail](https://github.com/microsoft/mcp) | 3,000* | C# | 10 | OAuth (Entra ID) | — |
| [Softeria/ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server) | 639 | TypeScript | 200+ (all M365) | OAuth / Device Code / BYOT | MIT |
| [ryaker/outlook-mcp](https://github.com/ryaker/outlook-mcp) | 345 | JavaScript | 27+ | OAuth (Graph) | — |
| [merill/lokka](https://github.com/merill/lokka) | 239 | TypeScript | via Graph | OAuth (multiple modes) | MIT |
| [pnp/cli-microsoft365-mcp-server](https://github.com/pnp/cli-microsoft365-mcp-server) | 52 | TypeScript | via CLI | M365 login | MIT |
| [XenoXilus/outlook-mcp](https://github.com/XenoXilus/outlook-mcp) | 22 | JavaScript | Email+Calendar+SharePoint | OAuth (Graph) | — |
| [ampcome-mcps/outlook-mcp](https://github.com/ampcome-mcps/outlook-mcp) | 1 | Python | 26 | Nango + Graph | MIT |
| [Abhishek-Aditya-bs/Outlook-MCP-Server](https://github.com/Abhishek-Aditya-bs/Outlook-MCP-Server) | 1 | Python | 2 | Windows COM | MIT |

\*Stars for the entire microsoft/mcp catalog, not the Mail server alone.

Every server in this ecosystem uses Microsoft Graph API — except one (Abhishek's, which uses local Outlook COM). That means every one requires Azure AD / Entra ID credentials. No shortcuts, no API keys, no personal access tokens. This is a feature for enterprise security teams and a hurdle for individual developers.

## Microsoft Work IQ Mail — The Official Server

Microsoft's own Mail MCP server is part of the broader [Work IQ](https://github.com/microsoft/work-iq) platform (751 stars, up from 564) and the [microsoft/mcp](https://github.com/microsoft/mcp) catalog (3,000 stars across all Microsoft MCP servers, up from 2,800). It ships alongside Work IQ servers for Calendar, Teams, Copilot Chat, SharePoint, and more. In March 2026, Microsoft launched **MCP Apps** — agents can now bring rich HTML-based UI experiences directly into Microsoft 365 Copilot chat, grounded in Work IQ organizational context. A new **workiq-productivity** plugin adds read-only email triage and meeting cost analysis.

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

**Copilot license required — and the paywall is tightening.** You need a Microsoft 365 Copilot license to use Work IQ MCP servers. At ~$30/user/month, this immediately prices out individual developers, small teams, and anyone who just wants Outlook MCP access without the full Copilot suite. **As of April 15, 2026, Microsoft pulled back Copilot Chat access from M365 apps (Word, Excel, PowerPoint, OneNote) for large enterprise users without the full Copilot license** — reinforcing the premium boundary rather than relaxing it. The community servers exist largely because of this paywall.

**Preview means preview.** Just like the Teams server, Microsoft warns this may be "substantially modified before release." Building production email workflows on preview APIs is risky.

**No folder management.** You can't list folders, create folders, or move messages between folders. For users who rely on folder-based email organization, this is a gap.

**No attachment handling.** The tools can send emails and search attachments, but there's no dedicated tool for downloading or uploading attachments. This limits agent use cases around file extraction from emails.

**No contact integration.** Reading or managing Outlook contacts requires a separate server. The Mail server is strictly mail.

## Softeria/ms-365-mcp-server — The Community Standard

[ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server) (639 stars, up from 530; 370 commits, up from 243; MIT license) is the most popular community Outlook MCP server by a wide margin — and it's been on a tear. Since March 2026, Softeria has shipped **49 releases** (v0.36.0 → v0.85.0), expanding from a solid M365 wrapper into a comprehensive **200+ tool** platform covering virtually the entire Microsoft Graph API surface. PulseMCP: 203K all-time visitors, 23.7K weekly, #203 globally (#79 weekly).

**Supported services:**

- **Email** — list, send, delete, create drafts, reply, reply-all, move messages
- **Calendar** — manage events, delta sync, calendar event actions (new in v0.82.0)
- **OneDrive** — file upload/download, folder operations, search (v0.75.0)
- **Excel** — worksheet and range operations
- **OneNote** — notebook and page management, site-scoped notebooks
- **Tasks** — To Do and Planner task management
- **Contacts** — Outlook contact operations
- **User Profile & Search** — directory and user queries
- **Groups** — create/update/delete, member/owner management (new in v0.84.0)
- **Places** — rooms, room lists (new in v0.77.0)
- **Virtual Events** — webinar endpoints (new in v0.73.0)
- **Trending Insights** — trending documents (new in v0.81.0)

**With `--org-mode` flag (organizational accounts):**
- Teams & Chats (including create-chat in v0.85.0), SharePoint, Online Meetings (transcripts/recordings), Shared Mailboxes, User Management

**Install:** `npx @softeria/ms-365-mcp-server`

**Auth:** Three modes — Device Code Flow (interactive, with token caching), OAuth Authorization Code (for HTTP transport, now with OAuth 2.1 and dynamic client registration), or Bring Your Own Token (for CI/CD or automated systems).

### What works well

**Breadth that no single Microsoft server matches.** One NPX command gives you email, calendar, files, tasks, contacts, Excel, OneNote, groups, places, virtual events, and more. Microsoft's approach splits these across separate Work IQ servers, each requiring its own setup. Softeria unifies them — now with 200+ tools.

**TOON output format.** The experimental "Token-Oriented Object Notation" reduces token usage by 30-60% compared to standard JSON. For LLM integrations where every token costs money, this is a meaningful optimization that no other Outlook MCP server offers.

**BM25 tool discovery (v0.79.6).** With 200+ tools, loading them all wastes context. Softeria added BM25 search-based discovery and `get-tool-schema` — agents find relevant tools by description instead of loading everything. Combined with preset categories (mail, calendar, files, personal, work, excel, contacts, tasks, onenote, search, users, all), this elegantly solves the context bloat problem that tool sprawl creates.

**Multi-account support.** A single server instance can manage multiple Microsoft 365 accounts simultaneously. Switch between personal and work accounts without reconfiguring.

**Read-only mode.** Start with `--read-only` to restrict all operations to safe reads. Useful for testing or building agents that should never modify data. Tool filtering adds another layer — you can expose only specific tools to specific agents.

**Security hardening (April 2026).** PKCE store size bounded to prevent memory exhaustion, default CORS restricted from wildcard to localhost, log directory moved to user home with secure permissions, pagination memory limits, and startup validation for `--enabled-tools` regex. This is the kind of production-grade security work most community servers skip.

**No Copilot license required.** Uses standard Microsoft Graph API permissions. Any Microsoft 365 account (including free personal accounts for some features) can authenticate.

### What doesn't

**15 open issues, some significant.** #400: `create-draft-email` broken in app-token (OAuth) mode — missing POST endpoint for `/users/:userId/messages`. #375: OAuth callback fails due to random ephemeral port not registered as redirect URI. #336: server-side 401 retry silently consumes refresh token without returning new one to client. Active development means active bugs, and authentication edge cases remain the dominant category.

**Rapid release pace creates integration risk.** 49 releases in 38 days means the API surface changes fast. If you pin a version, you miss security fixes; if you don't, you may get breaking changes. Enterprise teams that need stability may find this cadence uncomfortable.

**Node.js 20+ recommended.** Works with Node.js 14+ but with dependency warnings. The recommended version is higher than what many systems run.

## ryaker/outlook-mcp — Outlook + OneDrive + Power Automate

[outlook-mcp](https://github.com/ryaker/outlook-mcp) (345 stars, up from 278; 78 commits) connects Outlook with OneDrive and Power Automate — a combination few other servers offer. Recent work includes HTML email sanitization to prevent prompt injection attacks — a security concern that's increasingly relevant as agents interact with untrusted email content.

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

[Lokka](https://github.com/merill/lokka) (239 stars, up from 228; 100 commits; MIT license) takes a different approach: instead of wrapping specific Microsoft services into dedicated tools, it exposes the Microsoft Graph API itself as an MCP tool.

**4 tools:**
1. `lokka-microsoft` — Call any Microsoft Graph or Azure API endpoint
2. `set-access-token` — Manage authentication tokens dynamically
3. `get-auth-status` — Check authentication status
4. `add-graph-permission` — Request additional Graph API scopes interactively (new)

**Why this matters:** Rather than "search emails" as a tool, Lokka's approach is "call any Graph API endpoint." Your agent constructs the Graph API query (`/me/messages?$search="subject:invoice"`) and Lokka executes it. This means every Graph API capability is available, including ones that purpose-built servers haven't implemented yet.

**Auth:** Four modes — interactive auth (personal or custom app), app-only auth (certificate or client secret), client-provided tokens, and API version control (beta vs. v1.0).

### When to consider it

Lokka is best for users who already know the Microsoft Graph API and want maximum flexibility. It's the opposite of Softeria's approach — instead of many purpose-built tools, you get one tool that can do anything. The tradeoff is that your agent needs to know how to construct Graph API queries, which means more complex prompts and more room for errors.

It's also strong for **Azure management** tasks — subscriptions, billing, resource management — that pure Outlook servers don't touch.

## Also in the Landscape

**[pnp/cli-microsoft365-mcp-server](https://github.com/pnp/cli-microsoft365-mcp-server)** (52 stars, MIT) — Wraps the CLI for Microsoft 365 as an MCP server. If you already use `m365` CLI commands, this gives your agent the same capabilities. SharePoint, Teams, Planner, and more. Different philosophy from Softeria — this delegates to an established CLI rather than calling Graph API directly.

**[XenoXilus/outlook-mcp](https://github.com/XenoXilus/outlook-mcp)** (22 stars, 31 commits) — Email, calendar, and SharePoint integration with Office document parsing (PDF, Word, PowerPoint, Excel). Automatic handling of large files exceeding MCP limits. v1.0.1 (January 2026). Lower adoption but the document parsing angle is unique.

**[nsakki55/outlook-mcp](https://github.com/nsakki55/outlook-mcp)** — Auth Code + PKCE flow, no client secret needed. Connects directly to Microsoft Graph API. Useful for scenarios where you can't store a client secret.

**[Abhishek-Aditya-bs/Outlook-MCP-Server](https://github.com/Abhishek-Aditya-bs/Outlook-MCP-Server)** — The only server that uses **local Outlook COM** instead of Graph API. Windows-only, requires Outlook desktop installed, uses pywin32 to access mailboxes directly. Two tools: check mailbox access and search email chains. Useful if you need to access local Outlook data without cloud connectivity, but the Windows-only + local Outlook requirement limits its audience severely.

**[ampcome-mcps/outlook-mcp](https://github.com/ampcome-mcps/outlook-mcp)** (1 star, MIT) — 26 tools covering email, contacts, calendar, and folders through Graph API. Uses Nango for credential management (no direct token storage). Comprehensive tool count but minimal adoption and community validation.

**[merajmehrabi/Outlook_Calendar_MCP](https://github.com/merajmehrabi/Outlook_Calendar_MCP)** — Windows-only calendar MCP server using local Outlook COM. Read and manage calendar events from the desktop app. Same limitations as the Abhishek server — Windows + local Outlook required.

**[kacase/mcp-outlook](https://github.com/kacase/mcp-outlook)** — Another Graph API wrapper for Outlook. Calendar events, email reading, message sending. Lower adoption.

**[microsoft/work-iq](https://github.com/microsoft/work-iq) CLI** (751 stars, up from 564) — Not an MCP server per se, but a CLI/plugin for GitHub Copilot that queries Microsoft 365 data using natural language. Now includes a **workiq-productivity** plugin with read-only email triage and meeting cost analysis. Requires Entra ID admin consent. Interesting for Copilot users, but not a general-purpose MCP server.

## How Outlook Compares to Gmail

| Feature | [Gmail MCP](/reviews/gmail-mcp-servers/) (3.5/5) | Outlook MCP (Official) | Outlook MCP (Softeria) |
|---------|------|------|------|
| Official server | Google Workspace MCP | Work IQ Mail | N/A |
| Hosted | Yes (`workspace-developer.goog`) | Yes (Work IQ) | No (local npx) |
| Auth model | OAuth | OAuth (Entra ID) | OAuth 2.1 / Device Code / BYOT |
| Message search | Gmail query syntax | KQL search | Via Graph API |
| Folder management | Label management | No | Yes |
| Attachment handling | Limited | No | Via OneDrive tools |
| Calendar bundled | Separate server | Separate Work IQ server | Yes (with delta sync) |
| License cost | Free (Google account) | Copilot license (~$30/mo) | Free (M365 account) |
| Community standard | taylorwilsdon (1,700 stars) | N/A | Softeria (639 stars) |
| Services covered | Gmail + 11 Google services | Mail only | 200+ tools across M365 |
| Tool discovery | N/A | N/A | BM25 search + presets |

**Gmail is more accessible.** No paid license requirement for MCP access, stronger community ecosystem (1,700-star dominant server vs 530), and Google's own endpoint works without Copilot licensing.

**Outlook has deeper enterprise integration.** Entra ID auth, compliance policy enforcement, tenant-level controls, DLP rules — the enterprise security infrastructure around Outlook is more mature. If your organization already has Microsoft 365 Copilot licenses, the official server is the obvious choice.

**Both have the same fundamental risk.** Email is sensitive data. Whether it's Gmail or Outlook, giving an agent send permissions deserves serious thought. Both ecosystems have the same gap: no official reference server from the MCP project (modelcontextprotocol/servers).

## Which Outlook Server Should You Use?

**Use Work IQ Mail if** your organization has Microsoft 365 Copilot licenses and you want official, hosted, Microsoft-supported email MCP access with KQL search. Accept preview status and the limited 10-tool scope.

**Use Softeria/ms-365-mcp-server if** you want the broadest Microsoft 365 coverage from a single server, don't have Copilot licenses, or need features like BM25 tool discovery, TOON token optimization, multi-account support, or read-only mode. This is the community standard for a reason — 639 stars, 200+ tools, 49 releases in 38 days, MIT license.

**Use ryaker/outlook-mcp if** you need Power Automate integration alongside email and calendar. The workflow automation angle is unique. Accept the more complex setup and local token storage.

**Use merill/lokka if** you know the Microsoft Graph API and want maximum flexibility. One tool that can do anything the API supports. Not for beginners.

**Wait if** you need GA-quality stability from Microsoft. The official servers are in preview and will change. If your workflow can't tolerate API modifications, the community servers (especially Softeria) are more stable bets despite not having Microsoft's backing.

## The Bottom Line

**Rating: 3.5/5** — The official/community split remains the defining characteristic of this ecosystem. Microsoft's Work IQ Mail server has hosted architecture, KQL search, and enterprise-grade auth — but the Copilot license requirement (~$30/user/month) creates a paywall that's getting tighter, not looser. The April 15, 2026 rollback of Copilot Chat access for large enterprise users signals that Microsoft is reinforcing premium boundaries, not relaxing them.

Softeria's ms-365-mcp-server (639 stars, 200+ tools, v0.85.0) has emerged as one of the most comprehensive community MCP servers in the entire ecosystem — not just for Outlook, but for M365 overall. The 49 releases since March 2026 added groups management, virtual events, places, trending insights, BM25 tool discovery, and significant security hardening. The rapid pace is both a strength (features ship fast) and a concern (integration stability). ryaker's Power Automate integration (345 stars) and lokka's raw Graph API access (239 stars) fill distinct niches.

The ecosystem is less mature than [Gmail's](/reviews/gmail-mcp-servers/) (no 1,700-star dominant server, no free official endpoint) but more coherent than [Teams'](/reviews/teams-mcp-servers/). The gap between Softeria (639 stars, accelerating) and Gmail's taylorwilsdon (1,700 stars) is narrowing — if Softeria maintains this pace, it could challenge for parity by mid-2026. When Microsoft removes the Copilot license requirement or exits preview, this category moves to 4/5. The enterprise security infrastructure is already there; it's the accessibility that's holding it back.

---

*This review covers the Microsoft Outlook MCP server landscape as of April 2026. ChatForest researches MCP servers by reading source code, analyzing GitHub repositories and issues, studying documentation, and examining community signals. We do not install or run the servers ourselves. See our [methodology](/about/#our-review-methodology) for details.*

*This review was last edited on 2026-04-22 using Claude Opus 4.6 (Anthropic).*
