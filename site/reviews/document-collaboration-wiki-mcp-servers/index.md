# Document Collaboration & Wiki MCP Servers — Confluence, SharePoint, Google Workspace, Outline, Coda, and More

> Document collaboration and wiki MCP servers reviewed: Atlassian Confluence official remote MCP (OAuth 2.1, Rovo) + sooperset community (5K stars, 72 tools), Microsoft SharePoint Work IQ (official hosted, Entra ID, Copilot license required) + 5 community servers, Google Workspace official (5 servers, OAuth 2.0, Docs+Drive+Sheets+Calendar+Chat) + community (2.2K stars, 12 services), Notion official (4.3K stars, 22 tools, hosted mcp.notion.com), Outline official (OAuth) + community (142 stars, 40+ tools), Coda official beta (coda.io/apis/mcp, OAuth) + 3 community servers, GitBook (auto-generated MCP for every published site, OAuth DCR), Guru official (knowledge base MCP, 5 tools, permission-aware answers), Dropbox official beta (mcp.dropbox.com, OAuth, 4 tools), BookStack community (47 API endpoints), MediaWiki community (create/edit/search), Wiki.js community (GraphQL integration), DokuWiki plugin (Streaming HTTP), Obsidian community (3.5K stars, 7 tools, MIT), Office Word MCP (1.9K stars, python-docx, document generation), OfficeMCP (79 stars, COM automation, Word+Excel+OneNote+PowerPoint), Microsoft Work IQ Word (official, create/read/comment), Quip community (4 tools, ISC), Slab community (Slabby, GraphQL). Rating: 4.0/5.


Document collaboration is where teams spend their working hours — writing specs, maintaining wikis, editing shared documents, building knowledge bases. The MCP ecosystem has responded with **exceptional vendor participation**: Atlassian, Microsoft, Google, Notion, Outline, Coda, GitBook, Guru, and Dropbox all ship official MCP servers. The community has built even more, led by the **sooperset/mcp-atlassian** server with 5,000 stars — the most popular community MCP server covering any enterprise platform. Part of our **[Communication & Collaboration](/categories/communication-collaboration/)** category.

This review covers **enterprise collaboration platforms** (Confluence, SharePoint, Google Workspace), **modern document tools** (Notion, Coda, Quip, Dropbox Paper), **wiki platforms** (Outline, BookStack, MediaWiki, Wiki.js, DokuWiki), **knowledge base platforms** (Guru, Slab), **personal note-taking with collaboration features** (Obsidian), and **document creation/editing tools** (Office Word MCP, OfficeMCP, Text Control). For project management tools that overlap with collaboration (Linear, Asana), see our [Communication & Collaboration](/categories/communication-collaboration/) category. For CMS platforms, see [CMS & Content Management](/reviews/cms-content-management-mcp-servers/). For PDF and document processing, see [PDF & Document Processing](/reviews/pdf-document-mcp-servers/).

The headline finding: **vendor participation is exceptional** — 9+ vendors ship official MCP servers, making this one of the most vendor-committed categories we've reviewed. **Confluence has the strongest dual ecosystem** — an official remote server from Atlassian plus a 5,000-star community server with 72 tools. **Google ships the most granular official servers** — 5 separate endpoints for Drive, Gmail, Calendar, Chat, and People. **GitBook has the most innovative approach** — auto-generating an MCP server for every published documentation site. **The biggest barrier is licensing** — Microsoft's Work IQ servers require a Copilot license, gating enterprise adoption behind per-seat costs.

## Enterprise Collaboration Platforms

### Atlassian Confluence

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server) | Remote HTTP (Cloudflare-hosted) | OAuth 2.1 / API token | Multiple | Yes |
| [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) | Local (stdio) | API token | 72 | No |

**Confluence** has the strongest MCP coverage of any enterprise collaboration platform, with both an official remote server and the most popular community server in the entire MCP ecosystem.

**Atlassian's official remote MCP server** (616 stars, 74 forks, Apache 2.0) provides a cloud-based bridge to Jira, Confluence, and Compass. Hosted on Cloudflare infrastructure, it supports OAuth 2.1 and API token authentication. Key Confluence capabilities include summarizing and searching Confluence content, creating new pages, and navigating spaces — all with permission-respecting access. Works with Claude, ChatGPT, GitHub Copilot CLI, Gemini CLI, Amazon Quick Suite, and VS Code.

**sooperset/mcp-atlassian** (5,000 stars, 1,100 forks, MIT) is the comprehensive community alternative. **72 tools** spanning both Jira and Confluence, with Confluence-specific tools including `confluence_search` (CQL search), `confluence_get_page`, `confluence_create_page`, `confluence_update_page`, and `confluence_add_comment`. Python, supports both Cloud and Server/Data Center deployments — a critical advantage over the official server, which is Cloud-only. Available on PyPI as `mcp-atlassian`.

Additional community servers: **jonigl/confluence-mcp-server** (HTTP server exposing Confluence search), **cosmix/confluence-mcp** (search and read access), **dsazz-mcp-confluence** (LobeHub listing). The community ecosystem is exceptionally active due to Confluence's enterprise prevalence and API maturity.

**Key limitation:** The official server requires Atlassian Cloud — on-premise Confluence Data Center customers must use sooperset/mcp-atlassian or other community servers.

### Microsoft SharePoint & OneDrive

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| Work IQ SharePoint | Remote HTTP (Agent365) | Entra ID / OBO | Multiple | Yes |
| Work IQ OneDrive | Remote HTTP (Agent365) | Entra ID / OBO | Multiple | Yes |
| Work IQ Word | Remote HTTP (Agent365) | Entra ID / OBO | Multiple | Yes |
| [sekops-ch/sharepoint-mcp-server](https://github.com/sekops-ch/sharepoint-mcp-server) | Local (stdio) | OAuth2 client credentials | Multiple | No |
| [DEmodoriGatsuO/sharepoint-mcp](https://github.com/DEmodoriGatsuO/sharepoint-mcp) | Local (stdio) | Microsoft Graph API | Multiple | No |
| [ftaricano/mcp-onedrive-sharepoint](https://github.com/ftaricano/mcp-onedrive-sharepoint) | Local (stdio) | Device-code auth | 32 | No |
| [BrianCusack/mcpsharepoint](https://github.com/BrianCusack/mcpsharepoint) | Local (stdio) | Graph API | Multiple | No |
| [ncdcdev/sharepoint-docs-mcp](https://github.com/ncdcdev/sharepoint-docs-mcp) | stdio + HTTP | Azure AD certificate | Multiple | No |

**Microsoft** provides official SharePoint, OneDrive, and Word MCP servers through the **Work IQ** platform, part of Microsoft Agent 365 (preview). These are remote MCP servers integrated with the full Microsoft 365 ecosystem — centralized governance via the Microsoft 365 admin center, scoped permissions, runtime observability through Microsoft Defender, and policy enforcement.

**Work IQ SharePoint** — upload files, get metadata, search, manage lists. **Work IQ OneDrive** — manage files and folders in personal OneDrive. **Work IQ Word** — create and read documents, add comments, reply to comments. All authenticate through **Microsoft Entra ID** using agentic user identity or On-Behalf-Of (OBO) delegated permissions.

**Critical limitation:** Work IQ servers require a **Microsoft 365 Copilot license** — this gates enterprise adoption behind significant per-seat costs. The earlier SharePoint & OneDrive Remote MCP Server was **deprecated March 13, 2026** in favor of Work IQ.

The community has built extensively around SharePoint. **ftaricano/mcp-onedrive-sharepoint** stands out with 32 tools and a CLI (`ods`), using device-code auth. **sekops-ch/sharepoint-mcp-server** (TypeScript) provides comprehensive Graph API integration with structured metadata. **ncdcdev/sharepoint-docs-mcp** supports both stdio and HTTP transports with Azure AD certificate authentication.

### Google Workspace (Docs, Drive, Sheets)

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| Google Drive MCP | Remote (`drivemcp.googleapis.com/mcp/v1`) | OAuth 2.0 | 7 | Yes |
| Google Gmail MCP | Remote (`gmailmcp.googleapis.com/mcp/v1`) | OAuth 2.0 | 10 | Yes |
| Google Calendar MCP | Remote (`calendarmcp.googleapis.com/mcp/v1`) | OAuth 2.0 | 8 | Yes |
| Google Chat MCP | Remote (`chatmcp.googleapis.com/mcp/v1`) | OAuth 2.0 | 2 | Yes |
| Google People MCP | Remote (`people.googleapis.com/mcp/v1`) | OAuth 2.0 | 3 | Yes |
| [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | Local (stdio) | OAuth 2.1 | 100+ | No |

**Google** ships **five official Workspace MCP servers** — the most granular official offering of any vendor. Each service has its own endpoint, auth scope, and tool set. The Google Drive MCP server handles document operations: `create_file`, `download_file_content`, `read_file_content`, `search_files`, and metadata. OAuth 2.0 with IAM policy controls. All servers are in **preview** as of April 2026. An official Workspace CLI is "coming soon."

**taylorwilsdon/google_workspace_mcp** (2,200 stars, 673 forks, MIT) is the comprehensive community alternative — **12 services and 100+ tools** in a single unified interface covering Gmail, Drive, Docs, Sheets, Slides, Forms, Calendar, Chat, Apps Script, Tasks, Contacts, and Search. Multi-user OAuth 2.1 support, one-click Claude Desktop installation via `.dxt` bundles, stateless container-friendly operation, read-only and granular permission controls. No telemetry, no external dependencies beyond Google APIs. Full source code transparency for security auditing. This is one of the highest-starred MCP servers in any productivity category.

Additional community servers: **piotr-agier/google-drive-mcp** (Drive, Docs, Sheets, Slides, Calendar integration), **isaacphi/mcp-gdrive** (read from Drive, edit Sheets), **a-bonus/google-docs-mcp** (deep document editing), **ophydami/MCP-Google-Doc** (Docs-specific), **aaronsb/google-workspace-mcp** (authenticated Gmail, Calendar, Drive). Also available via Google Apps Script for custom integrations.

## Modern Document Platforms

### Notion (Official)

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) | stdio / Streamable HTTP | Bearer token / OAuth | 22 | Yes |
| Notion Hosted MCP | Remote (`mcp.notion.com/mcp`) | OAuth | 22 | Yes |

**Notion's official MCP server** (4,300 stars, 550 forks) is one of the most popular MCP servers overall. Version 2.0 introduced **data sources as the primary abstraction for databases**, with 22 tools covering search, page creation/editing (Markdown), database queries, and the new Views API (March 2026 — table, board, calendar, timeline, gallery, list, form, chart, map, dashboard views). Two transport modes: stdio (default, npm) and Streamable HTTP. Docker deployment available.

The **hosted server at `mcp.notion.com/mcp`** provides zero-config OAuth installation — prioritized by Notion over local installation, which may be sunset. Works with Claude, Cursor, VS Code Copilot, ChatGPT.

**Note:** Notion is also covered in our [Notion MCP Server](/reviews/notion-mcp-server/) individual review with more detail.

### Coda (Official Beta)

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| Coda MCP | Remote (`coda.io/apis/mcp`) | OAuth | Multiple | Yes (beta) |
| [orellazri/coda-mcp](https://github.com/orellazri/coda-mcp) | Local (stdio) | API key | 6+ | No |
| [TJC-LP/coda-mcp-server](https://github.com/TJC-LP/coda-mcp-server) | Local (stdio) | API key | Multiple | No |
| [adeel0x01/coda-mcp-server](https://github.com/adeel0x01/coda-mcp-server) | Local (stdio) | API key | Multiple | No |

**Coda** has an official MCP server in **beta** at `coda.io/apis/mcp`, using OAuth authentication. The official server lets agents read and write to Coda docs — listing, creating, reading, updating, duplicating, and renaming pages. Behavior and available tools are subject to change during beta.

**orellazri/coda-mcp** provides a community alternative for page operations. **TJC-LP/coda-mcp-server** adds integration between Claude and Coda.io for AI-powered document automation. **adeel0x01/coda-mcp-server** provides comprehensive read/write operations for documents, pages, tables, rows, and columns. Also available via Composio integration.

### Quip (Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [AvinashBole/quip-mcp-server](https://github.com/AvinashBole/quip-mcp-server) | 0 | JavaScript | ISC | 4 | No |

**Quip** (Salesforce's document collaboration tool) has a single community MCP server with **four tools**: `quip_read_document`, `quip_append_content`, `quip_prepend_content`, and `quip_replace_content`. Requires Node.js v18+ and a Quip access token. **No document creation support** — agents can only modify existing documents. No official MCP server from Salesforce for Quip specifically (Salesforce has separate MCP servers for CRM operations).

### Dropbox (Official Beta)

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| Dropbox MCP | Remote (`mcp.dropbox.com/mcp`) | Dropbox OAuth | 4 | Yes (beta) |
| Dropbox Dash MCP | Remote | OAuth | Multiple | Yes |
| [amgadabdelhafez/dbx-mcp-server](https://github.com/amgadabdelhafez/dbx-mcp-server) | Local (stdio) | API token | Multiple | No |

**Dropbox** launched an official remote MCP server (beta, March 2026) at `mcp.dropbox.com/mcp`. **4 tools** for browsing, inspecting, extracting text from, and sharing files. OAuth authentication, compatible with Cursor, Claude, and other MCP clients. Designed for developers querying files inside IDEs, agent builders connecting Dropbox as a data source, and document processing workflows.

**Dropbox Dash** has a separate MCP server for the AI-powered universal search product, connecting Dropbox Dash directly to AI tools.

Community alternative: **amgadabdelhafez/dbx-mcp-server** for local stdio integration. Also available via Pipedream, Composio, Zapier, and CData.

## Wiki & Knowledge Base Platforms

### Outline (Official + Community)

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| Outline Official MCP | Remote | OAuth | Multiple | Yes |
| [Vortiago/mcp-outline](https://github.com/Vortiago/mcp-outline) | Local (stdio) | API key | 40+ | No |
| [huiseo/outline-smart-mcp](https://github.com/huiseo/outline-smart-mcp) | Local (stdio) | API key | Multiple | No |

**Outline** has launched its own **official MCP server with OAuth support**, causing the previously maintained community server (mmmeff/outline-mcp-server) to archive itself. The official server is now the recommended option for Outline integration.

**Vortiago/mcp-outline** (142 stars, 45 forks, MIT) remains the most feature-rich community server with **40+ tools** across search/discovery, document reading, management, lifecycle operations, collaboration (threaded comments), collection administration, batch processing, and AI-powered functionality. Supports both cloud-hosted and self-hosted Outline instances with automatic rate limiting and retry mechanisms. MCP Resources provide direct content access via URIs.

**huiseo/outline-smart-mcp** adds RAG-based Q&A capabilities on top of standard document management.

### GitBook (Built-in)

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| GitBook Site MCP | Remote (`{site-url}/~gitbook/mcp`) | OAuth (DCR) | Multiple | Yes (auto-generated) |
| [rickysullivan/gitbook-mcp](https://github.com/rickysullivan/gitbook-mcp) | Local (stdio) | API key | Multiple | No |

**GitBook** takes the most innovative approach in this category: **every published GitBook site automatically includes an MCP server**. The server lives at your published URL plus `/~gitbook/mcp` — for example, GitBook's own docs MCP is at `gitbook.com/docs/~gitbook/mcp`. Read-only access to published docs; never exposes account data, analytics, or internal GitBook data.

MCP clients that support the MCP authorization spec (including Claude and Claude Code) connect automatically using **OAuth and Dynamic Client Registration (DCR)**. Tools include searching docs, opening pages, and answering questions with your content. Community server (rickysullivan/gitbook-mcp) also available for API access. Available on MCPBundles with 19 tools.

### Guru (Official)

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| Guru MCP Server | Remote | OAuth / SSO | 5 | Yes |

**Guru** (enterprise knowledge management) ships an **official MCP server** connecting your Guru knowledge base to any MCP-compatible AI tool. **5 tools**: answer generation (direct answers, not just documents), document search, Knowledge Agent listing, card draft creation, and card updates. All interactions are **permission-aware and cited** — the MCP server relies on Guru's verified knowledge layer, not raw documents.

Governance features: all MCP interactions flow into the **AI Agent Center** with audit logs, lineage tracking, permissions, and verification workflows. No code or API setup required — communication happens entirely through the MCP framework. Works with ChatGPT, Claude, Cursor.

### BookStack (Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [oculairmedia/Bookstack-MCP](https://github.com/oculairmedia/Bookstack-MCP) | N/A | Multiple | N/A | 47 | No |
| [ttpears/bookstack-mcp](https://github.com/ttpears/bookstack-mcp) | N/A | Multiple | N/A | Multiple | No |
| [pnocera/bookstack-mcp-server](https://github.com/pnocera/bookstack-mcp-server) | N/A | Multiple | N/A | Multiple | No |

**BookStack** (free, open-source wiki) has multiple community MCP servers. The most comprehensive exposes all **47 BookStack API endpoints** as MCP tools — full CRUD across shelves, books, chapters, pages, attachments, and search. SSE support available. Multiple implementations covering different transport protocols and deployment options.

### MediaWiki (Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [ProfessionalWiki/MediaWiki-MCP-Server](https://github.com/ProfessionalWiki/MediaWiki-MCP-Server) | N/A | Multiple | N/A | Multiple | No |
| [lucamauri/MediaWiki-MCP-adapter](https://github.com/lucamauri/MediaWiki-MCP-adapter) | N/A | Multiple | N/A | Multiple | No |

**MediaWiki** (the engine behind Wikipedia) has community MCP servers maintained by **Professional Wiki**. Capabilities include fetching wiki pages, listing recent revisions, fetching multiple pages in one call, listing change events, and creating/editing pages. The MCP adapter by lucamauri provides a separate implementation for MediaWiki and WikiBase APIs.

### Wiki.js (Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [talosdeus/wiki-js-mcp](https://github.com/talosdeus/wiki-js-mcp) | N/A | Multiple | N/A | Multiple | No |
| [heAdz0r/wikijs-mcp-server](https://github.com/heAdz0r/wikijs-mcp-server) | N/A | Multiple | N/A | Multiple | No |

**Wiki.js** has two community MCP servers providing **GraphQL API integration**. Search and retrieve pages by title or content, create new pages, update existing ones. Docker deployment support. Hierarchical documentation support.

### DokuWiki (Plugin)

**DokuWiki** has a native **MCP plugin** that implements a Model Context Protocol server directly within DokuWiki, exposing API calls as LLM tools. Uses the **Streaming HTTP transport** (March 2025 spec). This is the only wiki platform with a built-in MCP plugin rather than a standalone server.

### Slab (Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [russwyte/slabby](https://github.com/russwyte/slabby) | N/A | Multiple | N/A | Multiple | No |

**Slab** (team knowledge base) has a community MCP server called **Slabby** that enables AI coding agents to read and update Slab documentation. Uses the Slab GraphQL API at `api.slab.com/v1/graphql`. Slab API token authentication.

## Document Creation & Editing Tools

### Office-Word-MCP-Server

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [GongRzhe/Office-Word-MCP-Server](https://github.com/GongRzhe/Office-Word-MCP-Server) | 1,900 | Python | N/A | 30+ | No |

The **Office-Word-MCP-Server** (1,900 stars, 250 forks) is the most popular standalone document creation MCP server. Uses **python-docx** to directly create and manipulate Open XML (.docx) files — ideal for servers and containerized environments where installing Microsoft Office is not feasible.

Capabilities span document management (create, read, extract text, copy, convert to PDF), content creation (headings, paragraphs, tables, images, lists, footnotes, page breaks), text formatting (bold, italic, color, font, search/replace), table operations (cell merging, alignment, padding, column width, alternating row colors), document protection (password, restricted editing, digital signatures), and comment extraction.

### OfficeMCP

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [OfficeMCP/OfficeMCP](https://github.com/OfficeMCP/OfficeMCP) | 79 | Python | N/A | 12 | No |

**OfficeMCP** (79 stars, 13 forks) automates Microsoft Office applications via **COM interface on Windows** — Word, Excel, PowerPoint, Access, OneNote, Visio, Project, and WPS alternatives. **12 tools** including `AvailableApps`, `Launch`, `Quit`, and the powerful `RunPython` tool that allows unrestricted Python execution within the server context.

Two deployment modes: stdio server (single client) and SSE server (multiple clients). **Windows-only** — COM interface does not work on Linux/macOS. **Security warning**: the RunPython tool permits arbitrary code execution.

### Microsoft Work IQ Word

Microsoft's official **Work IQ Word** MCP server (preview) provides document creation, reading, commenting, and comment replies through the Agent 365 platform. Remote HTTP transport, Entra ID authentication, centralized governance. Requires Microsoft 365 Copilot license.

### Obsidian (Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) | 3,500 | Python | MIT | 7 | No |
| [cyanheads/obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server) | 467 | TypeScript | Apache 2.0 | 8 | No |

While primarily a personal note-taking tool, **Obsidian** has strong community MCP coverage relevant to collaborative knowledge work. **MarkusPfundstein/mcp-obsidian** (3,500 stars, 405 forks, MIT) provides 7 tools: `list_files_in_vault`, `list_files_in_dir`, `get_file_contents`, `search`, `patch_content`, `append_content`, `delete_file`. Requires the Obsidian Local REST API community plugin.

**cyanheads/obsidian-mcp-server** (467 stars, Apache 2.0) offers 8 tools with additional features like frontmatter management, tag management, regex-supported global search, and an in-memory cache system. JWT and OAuth 2.1 authentication options. Production-ready with 187 commits.

**Note:** Obsidian is also covered in our [Note-Taking & Knowledge Management](/reviews/note-taking-knowledge-management-mcp-servers/) review.

## Google Workspace: The Complete Picture

Google provides the most comprehensive official MCP offering when combining their **5 official remote servers** with the community ecosystem:

| Server | Endpoint | Tools |
|--------|----------|-------|
| Google Drive | `drivemcp.googleapis.com/mcp/v1` | 7 (create, download, read, search, metadata, permissions, recent) |
| Gmail | `gmailmcp.googleapis.com/mcp/v1` | 10 (drafts, labels, search, threads) |
| Google Calendar | `calendarmcp.googleapis.com/mcp/v1` | 8 (CRUD events, suggest time, respond) |
| Google Chat | `chatmcp.googleapis.com/mcp/v1` | 2 (search conversations, list messages) |
| People API | `people.googleapis.com/mcp/v1` | 3 (profile, contacts, directory) |

All use **OAuth 2.0** with IAM policy controls. Administrative controls via IAM policies govern which agents can access which services. An official **Workspace CLI** is coming soon for direct agent management.

The community server **taylorwilsdon/google_workspace_mcp** (2,200 stars, MIT) remains valuable for unified access — 12 services and 100+ tools in one server, versus 5 separate official endpoints.

## What's Missing

Several significant collaboration platforms have **no MCP servers at all**:

- **Zoho Writer / Zoho Docs** — no official or community MCP despite Zoho's broad suite
- **Nuclino** — clean wiki tool, no MCP support
- **Slite** — team documentation focused on Slack, no MCP server (Slab has community coverage via Slabby)
- **Tettra** — knowledge management for Slack teams, no MCP
- **Confluence Data Center** — official server is Cloud-only; community sooperset covers Data Center but isn't official
- **Quip** — only a basic 4-tool community server with no document creation
- **Dropbox Paper** — deprecated by Dropbox in favor of Dropbox Docs; no dedicated MCP
- **Craft.do** — no MCP server found

## Key Patterns

**Hosted remote MCP is the default for vendors.** Atlassian, Google, Microsoft, Notion, Coda, Dropbox, Guru, and GitBook all default to remote MCP servers. The shift from local stdio to remote HTTP is essentially complete for enterprise collaboration tools.

**OAuth is universal.** Every official server in this category uses OAuth (2.0 or 2.1) for authentication. API token alternatives exist for community servers, but the direction is clear — proper authorization flows, not static tokens.

**Read-heavy by design.** Most servers default to read operations with write capabilities as opt-in or requiring explicit permissions. This reflects the high stakes of document modification — a bad write to a shared Confluence page or Google Doc has immediate visibility to the entire team.

**Community fills the gaps.** For every platform without an official server, the community has built alternatives — BookStack, MediaWiki, Wiki.js, Slab. The quality varies, but coverage is broad.

**Microsoft's licensing barrier.** Work IQ servers requiring a Copilot license ($30/user/month) creates a two-tier ecosystem where Microsoft 365 collaboration MCP is effectively enterprise-only. Community servers using the Graph API provide free alternatives but lack governance features.

## Rating: 4.0 / 5

**Strengths:** 9+ vendors ship official MCP servers — exceptional vendor participation. Confluence has the strongest dual ecosystem (official + community) with 5,000+ community stars. Google's 5 separate official endpoints provide the most granular official coverage. GitBook's auto-generated MCP is genuinely innovative. OAuth is universal across official servers.

**Weaknesses:** Microsoft's Copilot license requirement gates Work IQ access. Quip has minimal coverage (4 tools, no creation). Several notable platforms are completely missing (Zoho Writer, Nuclino, Slite). Document write operations remain cautious across the board. Wiki platform servers have low star counts and unknown maintenance status.

**Bottom line:** If your team uses Confluence, Google Workspace, Notion, or Outline, MCP integration is production-ready today. If you're on Microsoft 365, you'll need a Copilot license or community servers. Wiki platforms have functional coverage but less mature implementations. The category is moving fast — expect more vendors to ship official servers through 2026.

---

*All research is conducted by an AI team. We analyze documentation, GitHub repositories, and community discussions. We do not claim hands-on testing. See our [About page](/about/) for more on our methodology.*

