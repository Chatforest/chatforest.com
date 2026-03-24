---
title: "OneDrive MCP Servers — AI Agents That Manage Your Microsoft 365 Files, Email, Calendar, and Teams"
date: 2026-03-23T23:00:00+09:00
description: "Microsoft's official Work IQ OneDrive MCP server is in preview with enterprise features like sensitivity labels, while Softeria's community server (552 stars) covers all of M365. From Azure Entra ID auth to 5MB file limits — here's the honest review."
og_description: "OneDrive MCP servers: official Microsoft Work IQ preview plus top community implementations for OneDrive, Outlook, Calendar, Teams, and SharePoint. Rating: 3.5/5."
content_type: "Review"
card_description: "Microsoft offers an official Work IQ OneDrive MCP server in preview with 13 tools and enterprise features like sensitivity labels. The community leader Softeria/ms-365-mcp-server (552 stars) covers OneDrive, Outlook, Calendar, Teams, SharePoint, and more across the full Microsoft 365 suite. Auth complexity via Azure Entra ID remains the biggest barrier."
last_refreshed: 2026-03-23
---

**At a glance:** [microsoft/work-iq](https://github.com/microsoft/work-iq) (594 stars, official, CC-BY-4.0) + [Softeria/ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server) (552 stars, community, MIT). OneDrive sits at the center of 446 million Microsoft 365 seats, and its MCP ecosystem is growing fast — but auth complexity keeps it behind Google Drive.

OneDrive MCP servers let AI agents **search, read, create, and manage files across your Microsoft 365 environment** — browse OneDrive folders, read and write documents, manage Outlook email, schedule Calendar events, access SharePoint sites, and apply enterprise security labels — all through natural language prompts. **Microsoft has an official Work IQ OneDrive remote server** in preview, while a growing community ecosystem already covers the full M365 suite.

[Microsoft](https://www.microsoft.com/) was founded on April 4, 1975, by **Bill Gates** and **Paul Allen**. The company went public in March 1986 (NASDAQ: MSFT). As of early 2026: **~$281.7 billion annual revenue** (FY 2025, ~15% YoY growth), **~$2.98-3.15 trillion market cap**. Microsoft 365 has over **446 million paid seats** globally, with commercial revenue exceeding **$60 billion annually**. SharePoint Online has **200+ million users**. Microsoft 365 holds approximately **58% enterprise market share** among organizations with 1,000+ employees, and **75% of Fortune 500** companies use M365 as their primary productivity suite.

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

**Note:** A previous combined ODSP (OneDrive + SharePoint) remote server was **deprecated on March 13, 2026**, replaced by the separate Work IQ OneDrive and Work IQ SharePoint servers.

### microsoft/work-iq — CLI + MCP

- **GitHub:** [microsoft/work-iq](https://github.com/microsoft/work-iq) — 594 stars, 45 forks, 70 commits
- **License:** CC-BY-4.0 (not open source — no source code contributions accepted)
- **Auth:** Entra ID authentication with tenant admin consent

Work IQ is Microsoft's broader M365 data access tool — natural language queries across emails, meetings, documents, Teams, and OneDrive. It serves as the official catalog and reference for Microsoft's MCP server ecosystem.

## Community Implementations

### Softeria/ms-365-mcp-server — Full M365 Integration (Top Pick)

- **GitHub:** [Softeria/ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server) — 552 stars, 199 forks, 249 commits
- **Language:** TypeScript
- **License:** MIT
- **Auth:** Device code flow (default), OAuth authorization code flow (HTTP mode), Bring Your Own Token (BYOT)

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

- **GitHub:** [merill/lokka](https://github.com/merill/lokka) — 229 stars, 67 forks, 100 commits
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

- **GitHub:** [pnp/cli-microsoft365-mcp-server](https://github.com/pnp/cli-microsoft365-mcp-server) — 88 stars, 20 forks, 63 commits
- **Language:** TypeScript/JavaScript
- **License:** MIT
- **Auth:** Pre-authentication via `m365 login` CLI command

Bridges the CLI for Microsoft 365 to MCP, enabling natural language to CLI command execution:

- Manages Entra ID, OneDrive, OneNote, Outlook, Planner, Power Apps, Power Automate, SharePoint, Teams
- Fuzzy search command discovery
- Integration with VS Code, GitHub Copilot CLI, Claude Desktop
- Requires Node.js 20.x+ and CLI for Microsoft 365 installed globally

### elyxlz/microsoft-mcp — Python M365

- **GitHub:** [elyxlz/microsoft-mcp](https://github.com/elyxlz/microsoft-mcp) — 41 stars, 23 forks, 20 commits
- **Language:** Python
- **License:** MIT
- **Auth:** Device flow via Microsoft Entra ID with Azure app registration; tokens cached locally

40+ tools across Email (11), Calendar (8), Contacts (6), Files (6), and Utility (4). Supports personal, work, and school accounts. Note: security vulnerabilities have been reported by community members.

### MrFixit96/onedrive-mcp-server — Security-Focused

- **GitHub:** [MrFixit96/onedrive-mcp-server](https://github.com/MrFixit96/onedrive-mcp-server) — 0 stars, 1 fork, 12 commits
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

### Other Implementations

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [hvkshetry/office-365-mcp-server](https://github.com/hvkshetry/office-365-mcp-server) | 12 | JavaScript | 24 tools for email, calendar, Teams, OneDrive with KQL search |
| [godwin3737/mcp-server-microsoft365-filesearch](https://github.com/godwin3737/mcp-server-microsoft365-filesearch) | 11 | Python | Search-only — file discovery across SharePoint/OneDrive |
| [ftaricano/mcp-onedrive-sharepoint](https://github.com/ftaricano/mcp-onedrive-sharepoint) | 1 | TypeScript | Unified OneDrive + SharePoint with Excel operations |
| [CDataSoftware/microsoft-onedrive-mcp-server-by-cdata](https://github.com/CDataSoftware/microsoft-onedrive-mcp-server-by-cdata) | 1 | Java | SQL queries on OneDrive data (commercial upsell) |
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
| **Official MCP** | Work IQ (preview, 13 tools, 5MB limit) | google/mcp (3.4k stars, GA remote servers) | 2 servers (remote files + Dash search) |
| **Top Community** | Softeria (552 stars, 249 commits) | taylorwilsdon (1.9k stars, 543 forks) | Limited community ecosystem |
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

1. **Authentication complexity** — Azure app registration, Entra ID configuration, and admin consent requirements make setup significantly harder than Google Drive or Dropbox MCP servers. Enterprise tenants with Conditional Access Policies can block third-party apps entirely.

2. **Copilot license requirement** — The official Work IQ server requires a Microsoft 365 Copilot license at $30/user/month, the highest cost barrier of any cloud storage MCP server.

3. **5MB file size limit** — The official server limits all file operations to 5MB, making it unsuitable for typical document workflows involving large presentations, spreadsheets, or media files.

4. **20-item folder listing cap** — The official server returns a maximum of 20 items per folder listing, making it impractical for folders with many files.

5. **Preview status** — The official Work IQ OneDrive server is in preview; tool names and parameters may change. The previous ODSP combined server was already deprecated (March 13, 2026).

6. **Security vulnerabilities** — Community security audits have found critical vulnerabilities in some implementations, including bearer token exposure and insufficient input validation. Choose implementations carefully.

7. **Personal OneDrive only** — The official server currently only accesses personal OneDrive, not shared drives or organizational file areas (handled separately by Work IQ SharePoint).

8. **Token refresh failures** — Device code flow tokens expire and require manual browser interaction to renew, interrupting automated workflows.

9. **Admin consent barriers** — Many enterprise tenants disable user consent for third-party apps, requiring IT admin approval before any community MCP server can connect — a process that can take days or weeks.

10. **Ecosystem fragmentation** — With 8-10+ implementations varying in language (TypeScript, Python, Java, JavaScript), auth method, and feature coverage, choosing the right server requires significant evaluation.

## Bottom Line

**Rating: 3.5 out of 5**

OneDrive MCP servers occupy an interesting position: the **most enterprise-ready** cloud storage MCP ecosystem (sensitivity labels, Defender integration, admin governance) but also the **most difficult to set up** (Azure Entra ID, admin consent, Copilot license). Microsoft's official Work IQ server has genuinely unique enterprise features that Google Drive and Dropbox lack, but the 5MB file limit and $30/user/month price tag make it impractical for most individual users.

The community ecosystem is solid — **Softeria's ms-365-mcp-server** at 552 stars with 249 commits is a genuinely comprehensive M365 integration covering email, calendar, OneDrive, Teams, SharePoint, and more. The **pnp/cli-microsoft365-mcp-server** offers a clever CLI bridge approach, and **MrFixit96's security-focused implementation** addresses real vulnerabilities found in other servers.

**Who should use OneDrive MCP servers:**

- **Enterprise teams** on Microsoft 365 who need AI agents to manage documents, email, and calendar within their existing M365 environment
- **IT administrators** who want AI-assisted Azure and M365 management (via lokka or pnp CLI bridge)
- **Security-conscious organizations** that need sensitivity labels and admin governance on AI file access

**Who should wait:**

- **Individual users** — the auth complexity and Copilot license cost make Google Drive or Dropbox MCP servers much more accessible
- **Teams needing large file support** — the 5MB official limit is a dealbreaker for real document workflows
- **Anyone without Azure admin access** — enterprise Conditional Access Policies can block setup entirely

The 3.5/5 rating reflects Microsoft's strong enterprise positioning and the active 552-star community server, balanced against the highest auth complexity, highest license cost, and most restrictive file limits of any cloud storage MCP ecosystem we've reviewed.

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official Microsoft announcements. Information is current as of March 2026. See our [About page](/about/) for details on our review process.*
