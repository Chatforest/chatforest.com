---
title: "OneDrive MCP Servers — AI Agents That Manage Your Microsoft 365 Files, Email, Calendar, and Teams"
date: 2026-03-23T23:00:00+09:00
sources_audited: 2026-08-18
description: "Microsoft's Agent 365 went GA on May 1, 2026. Anthropic's M365 Connector for Claude now gives all Claude users direct OneDrive/M365 access with no Azure app registration. Softeria community server at 915+ stars."
og_description: "OneDrive MCP servers: Anthropic's new M365 Connector removes the auth barrier for Claude users. Agent 365 GA, Work IQ expanding, Softeria at 915+ stars. Rating: 4.0/5."
content_type: "Review"
card_description: "Anthropic's Microsoft 365 Connector for Claude (all plans, free tier included) now gives Claude users direct access to OneDrive, Outlook, Teams, and SharePoint with no Azure app registration — fundamentally lowering the biggest barrier. Agent 365 went GA May 1, 2026. Microsoft/work-iq at 969 stars. Community leader Softeria/ms-365-mcp-server at 915+ stars covers the full M365 suite."
last_refreshed: 2026-08-18
---

**At a glance:** [microsoft/work-iq](https://github.com/microsoft/work-iq) (969 stars, official, MIT-licensed repo — using the hosted Work IQ service itself requires accepting a separate [EULA](https://github.com/microsoft/work-iq/blob/main/NOTICES.TXT)) + [Softeria/ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server) (915+ stars, community, MIT). OneDrive sits at the center of 450 million+ Microsoft 365 seats. **Anthropic's Microsoft 365 Connector** (all Claude plans, no Azure app registration) has dramatically lowered the auth barrier — the biggest knock against this ecosystem in early 2026.

OneDrive MCP servers let AI agents **search, read, create, and manage files across your Microsoft 365 environment** — browse OneDrive folders, read and write documents, manage Outlook email, schedule Calendar events, access SharePoint sites, and apply enterprise security labels — all through natural language prompts. **Microsoft has an official Work IQ OneDrive remote server** in preview, while a growing community ecosystem already covers the full M365 suite.

[Microsoft](https://www.microsoft.com/) was [founded on April 4, 1975](https://en.wikipedia.org/wiki/Microsoft), by **Bill Gates** and **Paul Allen**, and [went public on March 13, 1986](https://en.wikipedia.org/wiki/Microsoft) (NASDAQ: MSFT). Microsoft's [**FY2025 revenue was $281.7 billion, up 15% year-over-year**](https://www.microsoft.com/en-us/investor/earnings/fy-2025-q4/press-release-webcast). Microsoft 365 has over [**450 million paid commercial seats**](https://office365itpros.com/2026/01/30/microsoft-fy26-q2-results/) globally. As of its March 2026 25th-anniversary post, Microsoft says [**SharePoint serves more than 1 billion users each year**](https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/02/sharepoint-at-25-how-microsoft-is-putting-knowledge-to-work-in-the-ai-era/), with over 2 billion files uploaded and 2 million SharePoint sites created every day.

**Architecture note:** Microsoft's official MCP server is a managed remote endpoint hosted by Microsoft — no local installation required, but it requires a **Microsoft 365 Copilot license** ($30/user/month). Community implementations wrap the Microsoft Graph API, using Azure Entra ID (formerly Azure AD) for authentication. Most support device code flow, OAuth 2.0 authorization code flow, or certificate-based auth.

**Category:** [Cloud Storage & File Sync](/categories/cloud-storage-file-sync/)

## What It Does

Between Microsoft's official server and community implementations, OneDrive MCP servers cover five main capability areas:

### File Management

| Capability | What It Does |
|------------|-------------|
| Browse folders | List files and subfolders with metadata (official: max 20 items) |
| Read file content | Download and extract text from documents (official: 5MB limit) |
| Upload files | Create new files in OneDrive (official: 5MB limit) |
| Search files | Full-text search by name or partial name |
| Move/rename/delete | Organize files with eTag concurrency protection |
| Create folders | Create directory structures in OneDrive |
| Sharing | Generate sharing links with role-based access control |

### Enterprise Security (Official Only)

| Capability | What It Does |
|------------|-------------|
| Sensitivity labels | Apply Microsoft Purview sensitivity labels to files |
| eTag concurrency | Prevent overwrite conflicts on rename and delete operations |
| Admin governance | Managed through Microsoft 365 admin center |
| Defender observability | Security monitoring via Microsoft Defender |

### Email & Calendar (Community)

| Capability | What It Does |
|------------|-------------|
| Outlook email | Read, send, search (KQL), and manage email messages |
| Calendar events | Create, update, delete, and query calendar events |
| Teams meetings | Access meeting transcripts and recordings |
| Contacts | Contact management via Microsoft Graph |
| Tasks & Planner | Task creation and project planning |
| Shared mailboxes | Access organizational shared mailboxes |

### Microsoft 365 Integration (Community)

| Capability | What It Does |
|------------|-------------|
| SharePoint | Site discovery, list management, CRUD on list items |
| Excel operations | Workbook metadata, worksheet data, range updates, formulas |
| OneNote | Notebook and page access |
| Teams channels | Channel messaging and management |
| To Do | Task management across Microsoft To Do |
| Power Platform | Power Apps and Power Automate management |

### Azure & Admin (Community)

| Capability | What It Does |
|------------|-------------|
| Microsoft Graph API | Direct Graph API queries for any M365 data |
| Azure Resource Manager | Azure tenant and resource management |
| Entra ID | Security group management, conditional access auditing |
| Intune | Device configuration management |
| Azure cost analysis | Cloud spending analysis |

## Official Microsoft MCP

### Work IQ OneDrive — Remote Server (Preview)

- **Server ID:** `mcp_OneDriveRemoteServer`
- **Type:** Remote MCP server (hosted by Microsoft)
- **Endpoint:** `https://agent365.svc.cloud.microsoft/agents/tenants/{tenant_id}/servers/mcp_OneDriveRemoteServer`
- **Status:** Preview
- **License:** Microsoft 365 Copilot required ($30/user/month)
- **Auth:** Entra ID with delegated user permissions (On-Behalf-Of flow)

**13 tools available:**

| Tool | Purpose |
|------|---------|
| `getOnedrive` | Get drive metadata, quota, and owner info |
| `getFolderChildrenInMyOnedrive` | List top 20 items in a folder |
| `findFileOrFolderInMyDrive` | Search by name or partial name |
| `getFileOrFolderMetadataInMyOnedrive` | Get metadata by item ID |
| `getFileOrFolderMetadataByUrl` | Get metadata from sharing URL |
| `readSmallTextFileFromMyOnedrive` | Download text file (under 5MB) |
| `createSmallTextFileInMyOnedrive` | Upload text file (under 5MB) |
| `createFolderInMyOnedrive` | Create folder |
| `renameFileOrFolderInMyOnedrive` | Rename with eTag concurrency |
| `deleteFileOrFolderInMyOnedrive` | Delete with eTag concurrency |
| `moveSmallFileInMyOnedrive` | Move file (under 5MB) |
| `shareFileOrFolderInMyOnedrive` | Sharing invitations with role-based access |
| `setSensitivityLabelOnFileInMyOnedrive` | Apply sensitivity labels |

**Key limitations:** All file operations limited to **5MB**. Folder listings capped at **20 items**. Personal OneDrive only — no shared drives. Copilot license required. Tool names and parameters may change during preview.

A companion **Work IQ SharePoint** server handles organizational files separately.

**Note:** A previous combined ODSP (OneDrive + SharePoint) remote server has been **deprecated**, replaced by the separate Work IQ OneDrive and Work IQ SharePoint servers described above (confirmed by an [independent MCP-explorer writeup of the Work IQ OneDrive tools](https://www.puntobello.ch/en/nello/mcp365_explorer_onedrive/), which notes OneDrive tools used to be bundled into a combined `mcp_ODSPRemoteServer`).

### microsoft/work-iq — CLI + MCP

- **GitHub:** [microsoft/work-iq](https://github.com/microsoft/work-iq) — 969 stars, 117 forks
- **License:** [MIT](https://github.com/microsoft/work-iq/blob/main/LICENSE) for the repository code; using the packaged Work IQ CLI/service requires accepting a separate EULA (see [NOTICES.TXT](https://github.com/microsoft/work-iq/blob/main/NOTICES.TXT) in the package) — the repo's [CONTRIBUTING guide](https://github.com/microsoft/work-iq/blob/main/CONTRIBUTING.md) does accept pull requests for the plugin/skill definitions
- **Auth:** Entra ID authentication with tenant admin consent

Work IQ is Microsoft's broader M365 data access tool — natural language queries across emails, meetings, documents, Teams, and OneDrive. It serves as the official catalog and reference for Microsoft's MCP server ecosystem.

**Enterprise context:** [Microsoft Agent 365 went GA on **May 1, 2026**](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/) ($15/user/month standalone). The new [**Microsoft 365 E7 "Frontier Suite"**](https://blog.admindroid.com/microsoft365-e7-frontier-suite/) bundles M365 E5, Microsoft 365 Copilot, and Agent 365 at $99/user/month. Work IQ is the intelligence layer underpinning all of it. As of this audit (August 2026), the [Work IQ MCP server remains in **public preview**](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview) per Microsoft's own documentation, which still carries the "preview feature" warning. GitHub Copilot can also connect to Work IQ, extending M365 context into code editors.

## Community Implementations

### Softeria/ms-365-mcp-server — Full M365 Integration (Top Pick)

- **GitHub:** [Softeria/ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server) — 915+ stars, 356+ forks
- **Language:** TypeScript
- **License:** MIT
- **Auth:** Device code flow (default), OAuth authorization code flow (HTTP mode), Bring Your Own Token (BYOT)
- **Latest release:** [v0.144.0 (August 17, 2026)](https://github.com/Softeria/ms-365-mcp-server/releases) — the project resumed frequent releases after the brief Feb–May 2026 slowdown noted in earlier audits of this page; it has shipped well over 100 releases since.

The most comprehensive community implementation, covering the full Microsoft 365 suite:

- **Services:** Email, Calendar, OneDrive, Excel, OneNote, To Do, Planner, Contacts, Search, Teams, SharePoint
- **Multi-cloud:** Supports both Global and China/21Vianet endpoints
- **Multi-account:** Switch between multiple M365 accounts
- **Read-only mode:** Restrict to read-only operations for safety
- **Tool filtering:** Granular access control for which tools are exposed
- **TOON format:** 30-60% token reduction for efficient AI processing
- **Clients:** Claude Desktop, Claude Code, Open WebUI
- **Requires:** Node.js 20+

### merill/lokka — Microsoft Graph & Azure

- **GitHub:** [merill/lokka](https://github.com/merill/lokka) — 290 stars, 80 forks
- **Language:** JavaScript
- **License:** MIT
- **Auth:** Interactive, certificate-based, client secrets, or token-provided

Focused on Microsoft Graph and Azure Resource Manager APIs for admin and security operations:

- Query and manage Azure + M365 tenants via AI
- Security group management, conditional access auditing
- Intune configuration management
- Azure cost analysis
- General Graph API access (including OneDrive)

### pnp/cli-microsoft365-mcp-server — CLI Bridge

- **GitHub:** [pnp/cli-microsoft365-mcp-server](https://github.com/pnp/cli-microsoft365-mcp-server) — 124 stars, 26 forks
- **Language:** TypeScript/JavaScript
- **License:** MIT
- **Auth:** Pre-authentication via `m365 login` CLI command
- **Latest version:** [0.1.23 (July 13, 2026)](https://www.npmjs.com/package/@pnp/cli-microsoft365-mcp-server) per the npm registry (the project does not publish GitHub Releases). Actively maintained — 23 versions shipped since launch.

Bridges the CLI for Microsoft 365 to MCP, enabling natural language to CLI command execution:

- Manages Entra ID, OneDrive, OneNote, Outlook, Planner, Power Apps, Power Automate, SharePoint, Teams
- Fuzzy search command discovery
- Integration with VS Code, GitHub Copilot CLI, Claude Desktop
- Requires Node.js 20.x+ and CLI for Microsoft 365 installed globally

### elyxlz/microsoft-mcp — Python M365

- **GitHub:** [elyxlz/microsoft-mcp](https://github.com/elyxlz/microsoft-mcp) — 54 stars, 39 forks, 20 commits
- **Language:** Python
- **License:** MIT
- **Auth:** Device flow via Microsoft Entra ID with Azure app registration; tokens cached locally

40+ tools across Email (11), Calendar (8), Contacts (6), Files (6), and Utility (4). Supports personal, work, and school accounts. Note: security vulnerabilities have been reported by community members.

### MrFixit96/onedrive-mcp-server — Security-Focused

- **GitHub:** [MrFixit96/onedrive-mcp-server](https://github.com/MrFixit96/onedrive-mcp-server) — 4 stars, 2 forks, 12 commits
- **Language:** Python
- **License:** MIT
- **Auth:** HTTP mode with RFC 9728 Protected Resource Metadata (recommended); MSAL device-code with OS keyring caching (stdio fallback)

Built after a security audit that found 4 critical vulnerabilities in other OneDrive MCP implementations:

- 6 tools: list, metadata, search, upload (resumable for large files), download, sharing
- ~400 lines of core logic with 47 tests
- Dual-transport (stdio + HTTP)
- Bearer token sanitization before reaching language models
- JSON audit logging
- Zero-config auth in HTTP mode
- Works in enterprise tenants that block third-party consent

### Anthropic Microsoft 365 Connector — Built for Claude (NEW, April 2026)

- **Provider:** Anthropic (hosted)
- **Marketplace:** [Microsoft AppSource](https://marketplace.microsoft.com/en-us/product/saas/anthropic.microsoft-365-connector-for-claude)
- **License:** Free (available on all Claude plans including free tier)
- **Auth:** Delegated Microsoft Graph permissions via Microsoft app marketplace — no Azure app registration required

This is the most significant development in the M365 MCP ecosystem since the original Work IQ launch. [**Anthropic built and hosts an official M365 Connector for Claude**](https://claude.com/connectors/microsoft-365) that gives Claude direct access to:

- **OneDrive** — search, read, and manage files across SharePoint and OneDrive
- **Outlook** — read email threads, analyze communication patterns
- **Teams** — search channel discussions and meeting transcripts
- **SharePoint** — access documents across SharePoint sites and libraries

**Why it matters:** Every other OneDrive MCP server requires Azure app registration, Entra ID configuration, or a Copilot license. The Anthropic connector eliminates those barriers — users connect through the Microsoft app marketplace with delegated permissions, and it works on all Claude plans including free. [Available since early April 2026](https://office365itpros.com/2026/04/08/microsoft-365-connector-for-claude/), per independent reporting dated shortly after launch. This effectively resolves **Known Issue #1** (authentication complexity) for Claude.ai users specifically.

**Limitation:** Available for Claude.ai users through the web interface, not as a self-hosted MCP server for programmatic/automated agent use cases.

### Arcade.dev Microsoft 365 MCP Servers — Commercial (NEW, March 13, 2026)

- **Provider:** Arcade.dev (commercial, managed)
- **Coverage:** Word, Excel, PowerPoint, OneDrive, SharePoint — 5 separate MCP servers, 30+ tools
- **Auth:** Managed by Arcade.dev

[Arcade.dev launched five "Optimized MCP servers"](https://www.arcade.dev/blog/microsoft-office-365-mcp-servers-launch/) for the full Microsoft Office surface. Every Word, Excel, PowerPoint, and OneDrive tool also exists in the SharePoint variant (different API surfaces and OAuth scopes). Full read and write access across the suite, designed for complex multi-step agent workflows. Commercial product with [Arcade.dev's catalog infrastructure](https://docs.arcade.dev/en/resources/integrations).

### Other Implementations

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [hvkshetry/office-365-mcp-server](https://github.com/hvkshetry/office-365-mcp-server) | 16 | JavaScript | 24 tools for email, calendar, Teams, OneDrive with KQL search |
| [godwin3737/mcp-server-microsoft365-filesearch](https://github.com/godwin3737/mcp-server-microsoft365-filesearch) | 11 | Python | Search-only — file discovery across SharePoint/OneDrive |
| [ftaricano/mcp-onedrive-sharepoint](https://github.com/ftaricano/mcp-onedrive-sharepoint) | 7 | TypeScript | Unified OneDrive + SharePoint with Excel operations |
| [CDataSoftware/microsoft-onedrive-mcp-server-by-cdata](https://github.com/CDataSoftware/microsoft-onedrive-mcp-server-by-cdata) | 2 | Java | SQL queries on OneDrive data (commercial upsell) |
| [karthik20/onedrive-mcp-server-spring](https://github.com/karthik20/onedrive-mcp-server-spring) | 0 | Java | Spring Boot read-only server |

## Authentication

OneDrive MCP servers have the **most complex authentication setup** of any cloud storage MCP ecosystem:

| Method | Used By | Complexity |
|--------|---------|------------|
| Entra ID + Copilot License | Official Work IQ | Highest — requires $30/user/mo license |
| Azure App Registration + Device Code | Softeria, elyxlz | High — Azure portal setup required |
| Azure App Registration + OAuth 2.0 | hvkshetry, ftaricano | High — redirect URI configuration |
| CLI pre-auth (`m365 login`) | pnp/cli-microsoft365 | Medium — requires global CLI install |
| Certificate-based | lokka | Medium — requires cert generation |
| RFC 9728 Protected Resource Metadata | MrFixit96 | Low — zero-config in HTTP mode |

**Enterprise blockers:** When tenant admins disable "Users can consent to apps" in Entra ID, users see "needs admin approval" errors. Conditional Access Policies can block third-party apps entirely. Two-factor authentication can break device code flows.

## Cloud Storage MCP Comparison

| Dimension | OneDrive | Google Drive | Dropbox |
|-----------|----------|-------------|---------|
| **Official MCP** | Work IQ (preview, 13 tools, 5MB limit) | No dedicated official Drive MCP server — Google/Anthropic's [reference gdrive connector was archived May 29, 2025](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/gdrive) | 2 servers ([remote files + Dash search, open beta since March 2026](https://help.dropbox.com/integrations/set-up-MCP-server)) |
| **Top Community** | [Softeria](https://github.com/Softeria/ms-365-mcp-server) (915+ stars) | [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) (3.0k stars, 945 forks) | Limited community ecosystem |
| **Ecosystem Size** | 8-10 repos | 10+ repos | 5-6 repos |
| **Auth Complexity** | **Highest** — Azure Entra ID, admin consent | Medium — Google OAuth 2.0 | Low-Medium — Dropbox OAuth |
| **Enterprise Features** | **Strongest** — sensitivity labels, Defender, admin governance | High — Workspace admin | Medium — Business plan for Dash |
| **File Size Limits** | 5MB (official) | No hard limit in community servers | No hard limit |
| **License for Official** | M365 Copilot ($30/user/mo) | Free with Google account | Free (core), Business (Dash) |
| **Unique Feature** | Sensitivity labels, Copilot Studio integration | Deep Docs/Sheets/Slides editing | Dash cross-app search (30+ apps) |

## OneDrive Pricing

| Plan | Price | Storage |
|------|-------|---------|
| OneDrive Standalone (Personal) | $1.99/month | 100 GB |
| Microsoft 365 Personal | $9.99/month | 1 TB |
| Microsoft 365 Family (up to 6) | $9.99/month | 1 TB/user |
| OneDrive for Business (Plan 1) | $5/user/month | 1 TB |
| Microsoft 365 Business Basic | $6/user/month | 1 TB |
| Microsoft 365 Business Standard | $12.50/user/month | 1 TB + desktop Office |
| Microsoft 365 Business Premium | $22/user/month | 1 TB + Intune/Defender |
| **M365 Copilot** (required for official MCP) | **$30/user/month** | Add-on to M365 plan |

## Known Issues

1. **Authentication complexity** — Azure app registration, Entra ID configuration, and admin consent requirements make setup significantly harder than Google Drive or Dropbox MCP servers. Enterprise tenants with Conditional Access Policies can block third-party apps entirely. **Partially resolved for Claude.ai users:** The Anthropic M365 Connector (April 2026) eliminates Azure app registration for Claude web users — but programmatic/automated use cases still face the same barriers.

2. **Copilot license requirement** — The official Work IQ server requires a Microsoft 365 Copilot license at $30/user/month, the highest cost barrier of any cloud storage MCP server.

3. **5MB file size limit** — The official server limits all file operations to 5MB, making it unsuitable for typical document workflows involving large presentations, spreadsheets, or media files.

4. **20-item folder listing cap** — The official server returns a maximum of 20 items per folder listing, making it impractical for folders with many files.

5. **Preview status** — The official Work IQ OneDrive MCP server remains in public preview as of May 2026; tool names and parameters may change. The previous ODSP combined server was deprecated March 13, 2026. Agent 365 went GA May 1, 2026 (the broader platform), but Work IQ MCP itself has not been declared GA.

6. **Security vulnerabilities** — Community security audits have found critical vulnerabilities in some implementations, including bearer token exposure and insufficient input validation. Choose implementations carefully.

7. **Personal OneDrive only** — The official server currently only accesses personal OneDrive, not shared drives or organizational file areas (handled separately by Work IQ SharePoint).

8. **Token refresh failures** — Device code flow tokens expire and require manual browser interaction to renew, interrupting automated workflows.

9. **Admin consent barriers** — Many enterprise tenants disable user consent for third-party apps, requiring IT admin approval before any community MCP server can connect — a process that can take days or weeks.

10. **Ecosystem fragmentation** — With 10+ implementations varying in language (TypeScript, Python, Java, JavaScript), auth method, and feature coverage, choosing the right server requires significant evaluation.

11. **Historical note:** an earlier audit of this page (May 2026) flagged a multi-month gap in Softeria/ms-365-mcp-server releases after v0.36.0 (February 8, 2026) as a risk. That gap has since closed — [the project resumed frequent releases and reached v0.144.0 by August 17, 2026](https://github.com/Softeria/ms-365-mcp-server/releases). This is no longer an open concern as of this audit.

## Bottom Line

**Rating: 4.0 out of 5** *(upgraded from 3.5 — May 2026 refresh)*

The OneDrive MCP ecosystem crossed an important threshold in April–May 2026. **Anthropic's Microsoft 365 Connector** eliminates the biggest barrier — Azure app registration and Entra ID complexity — for Claude.ai users. Combined with **Agent 365 going GA (May 1)** and the **M365 E7 Frontier Suite** cementing Work IQ as core enterprise infrastructure, the trajectory has decisively improved.

For individual Claude users, the path is now clear: connect via the Anthropic M365 Connector and get OneDrive, Outlook, Teams, and SharePoint access on any plan, including free. The auth complexity that drove the original 3.5/5 rating no longer applies for this use case.

For programmatic and automated agents, the landscape is also richer: Arcade.dev's commercial M365 MCP servers joined in March 2026, Softeria's community server has grown past 915 stars, and the official Work IQ platform is GA-level committed. The remaining technical limitations (5MB file cap, 20-item folder listing, Copilot license for Work IQ) still exist — but they're limitations of the enterprise tier, not blockers for getting started.

Softeria, the community's top implementation, went quiet for a few months after February 2026 but has since resumed shipping releases at a rapid pace (v0.144.0 as of August 17, 2026) — the earlier concern about the community tier stalling has not materialized.

**Who should use OneDrive MCP servers:**

- **Claude.ai users** — the Anthropic M365 Connector is the immediate answer: free, no setup, works on all plans
- **Enterprise teams** on Microsoft 365 who need AI agents to manage documents, email, and calendar within their existing M365 environment
- **IT administrators** who want AI-assisted Azure and M365 management (via lokka or pnp CLI bridge)
- **Security-conscious organizations** that need sensitivity labels and admin governance on AI file access

**Who should wait:**

- **Teams needing large file support** — the 5MB official limit is still a dealbreaker for real document workflows with Work IQ
- **Anyone needing automated/headless OneDrive access** — community servers still require Azure app setup; the Anthropic connector is Claude.ai-only

The 4.0/5 rating reflects the Anthropic connector removing the primary auth barrier for Claude users, Agent 365 GA solidifying Microsoft's enterprise MCP commitment, and a genuinely expanded set of options from Arcade.dev. The 5MB official limit and Work IQ's continued preview status prevent a higher score.

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official Microsoft announcements. Information was last re-verified in August 2026. See our [About page](/about/) for details on our review process.*
