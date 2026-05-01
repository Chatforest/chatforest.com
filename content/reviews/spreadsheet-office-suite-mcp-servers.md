---
title: "Spreadsheet & Office Suite MCP Servers — Google Sheets, Excel, Word, Google Docs, LibreOffice, Google Workspace, and More"
date: 2026-03-17T00:30:00+09:00
description: "Spreadsheet and office suite MCP servers are giving AI agents full control over documents and data — reading and writing Excel files, managing Google Sheets, creating Word"
og_description: "Spreadsheet & Office Suite MCP servers: google_workspace_mcp (2,300 stars — 12+ Google services), haris-musa/excel-mcp-server (3,800 stars — Python, charts, pivots, triple transport), mcp-server-excel (147 stars — COM API, v1.8.55), mcp-google-sheets (832 stars — 19 tools), google-docs-mcp (497 stars — Docs/Sheets/Drive). NEW: ms-365-mcp-server (668 stars — 200+ tools via Graph API). Office-Word-MCP-Server ARCHIVED. 40+ servers reviewed. Rating: 4/5."
content_type: "Review"
card_description: "Spreadsheet and office suite MCP servers for AI-powered document creation, spreadsheet automation, and office workflow management. **Excel MCP servers had the biggest shakeup** — haris-musa/excel-mcp-server exploded to 3,800 stars (413 forks), becoming the most-starred dedicated spreadsheet MCP server. Python/openpyxl-based, cross-platform, with formulas, charts, pivot tables, conditional formatting, data validation, and triple transport (stdio, SSE, streamable HTTP). sbroenne/mcp-server-excel nearly doubled to 147 stars with aggressive v1.8.55 release cadence (near-daily releases in April 2026) — still Windows COM but the most actively developed server in the category. **Google Workspace continues to dominate** — taylorwilsdon/google_workspace_mcp grew to 2,300 stars (+28%) with v1.20.1 (April 28, 2026), adding Sheets row operations, PKCE authentication, Docs table support, domain-wide delegation, and PDF extraction. Google launched official remote MCP servers for Gmail, Drive, Calendar, Chat, and People API — but **notably omits Sheets and Docs**, leaving community servers as the only option. **GongRzhe/Office-Word-MCP-Server was ARCHIVED on March 3, 2026** — the #2 most-starred office MCP server (1,900 stars) is now read-only with no replacement announced. Word document creation via MCP now relies on dvejsada/mcp-ms-office-documents (transferred to ForLegalAI org, 26 stars) or the new ms-365-mcp-server for Graph API access. **NEW: Softeria/ms-365-mcp-server (668 stars, 255 forks)** — comprehensive Microsoft 365 integration via Graph API with 200+ tools covering Excel, OneDrive, Outlook, Calendar, Teams, and SharePoint. Supports org-mode and China 21Vianet cloud. **Microsoft MCP is now GA in Copilot Studio** — agents can integrate MCP servers directly. Agent 365 MCP servers launched for Copilot Search, SharePoint/OneDrive, Outlook Mail, and Calendar. MCP Apps in Copilot Chat render interactive UI. **Google Docs grew to 497 stars (+32%)** — a-bonus/google-docs-mcp added remote Cloud Run deployment and OAuth improvements. xing5/mcp-google-sheets grew to 832 stars. **The category earns 4/5** — Excel's explosive growth (haris-musa 3.8K stars) and the M365 ecosystem expansion are major positives, but the Office-Word-MCP-Server archiving creates a Word gap, and Google's official MCP servers pointedly omit Sheets/Docs."
last_refreshed: 2026-05-01
---

Spreadsheet and office suite MCP servers let AI assistants create Word documents, read and write Excel files, manage Google Sheets, edit Google Docs, and automate entire Google Workspace workflows. Instead of manually formatting documents and copying data between spreadsheets, you can have AI agents handle the full office productivity stack through the Model Context Protocol. Part of our **[Business & Productivity MCP category](/categories/business-productivity/)**.

This review covers the **spreadsheet and office suite** ecosystem — Google Sheets, Excel, Microsoft Word, Google Docs, Google Workspace, LibreOffice, and generic spreadsheet tools. For presentation-specific servers, see our [Presentation & Slides review](/reviews/presentation-slides-mcp-servers/). For email servers, see our [Outlook review](/reviews/outlook-mcp-servers/) and [Gmail review](/reviews/gmail-mcp-servers/).

The headline findings: **haris-musa/excel-mcp-server exploded to 3,800 stars** — now the most-starred dedicated spreadsheet MCP server. **taylorwilsdon/google_workspace_mcp grew to 2,300 stars** with v1.20.1 adding PKCE auth, Sheets row ops, and PDF extraction. **GongRzhe/Office-Word-MCP-Server was ARCHIVED** on March 3, 2026 (1,900 stars, now read-only). **NEW: Softeria/ms-365-mcp-server (668 stars)** provides 200+ tools via Microsoft Graph API. **sbroenne/mcp-server-excel nearly doubled** to 147 stars with v1.8.55 and near-daily releases. Google launched official remote MCP servers but **omits Sheets and Docs**. Microsoft MCP is now **GA in Copilot Studio**.

## Google Workspace (Comprehensive)

### taylorwilsdon/google_workspace_mcp (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | 2,300 | Python | MIT | 50+ |

The **most comprehensive office productivity MCP server** — covers 12+ Google services in a single installation. **Grew 1,800→2,300 stars (+28%)** with v1.20.1 (April 28, 2026):

- **Gmail** — complete email management with end-to-end coverage
- **Google Drive** — file operations with Office format support, **PDF extraction** (new)
- **Google Docs** — document creation, editing, comments, **table support** (new)
- **Google Sheets** — spreadsheet operations with flexible cell management, **row operations** (new)
- **Google Slides** — presentation creation and manipulation
- **Google Calendar** — full calendar management
- **Google Forms** — form creation, publish settings, response management
- **Google Tasks** — task and task list management with hierarchy
- **Google Chat** — space management and messaging
- **Google Contacts** — contact management via People API
- **Custom Search** — Programmable Search Engine integration
- **Google Apps Script** — cross-application workflow automation

Features **OAuth 2.0/2.1 with PKCE authentication** (new), multi-user support, domain-wide delegation, CLI mode for scripting, and tool filtering to reduce context usage. If you use Google Workspace, this is the one server to install.

**Note:** Google launched official remote MCP servers for Gmail (10 tools), Drive (7 tools), Calendar (8 tools), Chat (2 tools), and People (3 tools) — but **Sheets and Docs are not yet covered by official servers**. Community servers remain the only option for Sheets/Docs MCP access.

### Other Google Workspace Servers

| Server | Stars | Language | License | Focus |
|--------|-------|----------|---------|-------|
| [ngs/google-mcp-server](https://github.com/ngs/google-mcp-server) | — | — | — | Multi-account, Calendar/Drive/Gmail/Sheets/Docs/Slides |
| [j3k0/mcp-google-workspace](https://github.com/j3k0/mcp-google-workspace) | — | — | — | Gmail + Calendar |
| [aaronsb/google-workspace-mcp](https://github.com/aaronsb/google-workspace-mcp) | — | — | — | Authenticated access, Gmail/Calendar/Drive |
| [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) | — | — | — | GSuite products |

Multiple alternatives exist, but taylorwilsdon's server dominates in scope and community adoption.

## Google Sheets

### xing5/mcp-google-sheets (Best Google Sheets)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) | 832 | Python | — | 19 |

The **leading dedicated Google Sheets server** with 19 tools:

- `list_spreadsheets`, `create_spreadsheet`, `get_sheet_data`, `update_cells`, `batch_update_cells`
- `add_rows`, `add_columns`, `list_sheets`, `create_sheet`, `get_sheet_formulas`
- `copy_sheet`, `rename_sheet`, `share_spreadsheet`, `search_spreadsheets`
- `find_in_spreadsheet`, `get_multiple_sheet_data`, `get_multiple_spreadsheet_summary`, `batch_update`

Supports **4 authentication methods** — Service Account (recommended), OAuth 2.0, direct credential injection, and Application Default Credentials. Zero-install via `uvx`, Docker support with SSE transport, and tool filtering to reduce context size.

### Other Google Sheets Servers

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [mkummer225/google-sheets-mcp](https://github.com/mkummer225/google-sheets-mcp) | — | — | AI agent connector |
| [domdomegg/google-sheets-mcp](https://github.com/domdomegg/google-sheets-mcp) | — | — | Read/write/manage |
| [shionhonda/mcp-gsheet](https://github.com/shionhonda/mcp-gsheet) | — | — | List/read/write ranges |
| [freema/mcp-gsheets](https://github.com/freema/mcp-gsheets) | — | — | Claude Code/Desktop compatible |
| [isaacphi/mcp-gdrive](https://github.com/isaacphi/mcp-gdrive) | — | — | Drive + Sheets combined |
| [ajaysmb/gsheets-mcp](https://github.com/ajaysmb/gsheets-mcp) | — | — | Auto-formatting + charts |
| [kazz187/mcp-google-spreadsheet](https://github.com/kazz187/mcp-google-spreadsheet) | — | — | Spreadsheet operations |

Google Sheets is the **most fragmented subcategory** — 8+ servers doing essentially the same thing. xing5's server leads in stars and feature count.

## Google Docs

### a-bonus/google-docs-mcp (Best Google Docs)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [google-docs-mcp](https://github.com/a-bonus/google-docs-mcp) | 497 | TypeScript | MIT | 30+ |

**Grew 377→497 stars (+32%)** with 231 commits, added remote Cloud Run deployment and OAuth improvements. Full Google Docs API access with rich editing capabilities:

- **Document reading** — plain text, JSON, and markdown formats
- **Text manipulation** — insertion, appending, deletion with full formatting
- **Styling** — bold, italic, colors, font size, links, paragraph alignment
- **Tables and images** — insertion and formatting
- **Multi-tab documents** — navigate and edit across tabs
- **Comments** — create, reply, resolve, delete
- **Google Sheets** — range-based read/write, formatting, dropdowns, named tables
- **Google Drive** — search, create, move, copy, rename, delete

Also supports OAuth 2.0, service accounts with domain-wide delegation, and profile-based multi-account management.

## Microsoft Excel

### haris-musa/excel-mcp-server (Most Popular Excel — 3,800 stars)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) | 3,800 | Python | — | 20+ |

**Exploded in popularity** to become the most-starred dedicated spreadsheet MCP server (413 forks). Python/openpyxl-based, works cross-platform with no Excel installation needed:

- **Formulas** — full formula support with calculation
- **Charts** — creation and configuration
- **Pivot tables** — data summarization
- **Conditional formatting** — rule-based styling
- **Data validation** — input constraints
- **Triple transport** — stdio, SSE, and streamable HTTP

Previously listed as a minor alternative, this server has surpassed all other Excel and spreadsheet MCP servers in community adoption.

### negokaz/excel-mcp-server (Cross-Platform Go)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [excel-mcp-server](https://github.com/negokaz/excel-mcp-server) | 939 | Go | MIT | 7 |

The **original most-starred Excel MCP server** (878→939 stars) — works cross-platform by reading/writing XLSX files directly. No releases since v0.12.0 (July 2025) — **development appears paused**:

- `excel_describe_sheets` — list sheet information
- `excel_read_sheet` — retrieve cell values with pagination
- `excel_write_to_sheet` — update cell contents (text values and formulas)
- `excel_create_table` — generate tables within sheets
- `excel_copy_sheet` — duplicate existing sheets
- `excel_format_range` — apply styling to cell ranges
- `excel_screen_capture` — take screenshots of sheets (Windows only)

No Microsoft Office installation required. Built in Go for fast execution. Still solid for basic XLSX operations but no longer actively developed.

### sbroenne/mcp-server-excel (Most Powerful Excel — Fastest Growing)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-excel](https://github.com/sbroenne/mcp-server-excel) | 147 | C# | MIT | 25 |

**Nearly doubled from 76→147 stars (+93%)** with aggressive release cadence — v1.8.55 (April 29, 2026) with near-daily releases in April 2026. Controls a **live Excel application through COM API** — Windows-only but with 230+ operations:

- **Power Query** — M code management, load destinations
- **DAX measures** — Data Model with auto-formatted code
- **VBA** — module management and execution
- **PivotTables** — creation, fields, aggregations, calculated members
- **Charts** — creation, configuration, series, formatting, trendlines
- **Slicers** — interactive filtering
- **Conditional formatting** — rules management
- **Data Connections** — OLEDB/ODBC management
- **Screenshot capture** — for LLM verification
- **VS Code extension** (new)

The most actively developed server in this entire category. If you need Power Query, PivotTables, or VBA automation, this is the only option. Requires Excel installed on Windows.

### Other Excel Servers

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [yzfly/mcp-excel-server](https://github.com/yzfly/mcp-excel-server) | — | — | Natural language interaction, visualization |
| [guillehr2/Excel-MCP-Server-Master](https://github.com/guillehr2/Excel-MCP-Server-Master) | — | — | XLSX/XLSM without Excel installed |
| [ArchimedesCrypto/excel-reader-mcp](https://github.com/ArchimedesCrypto/excel-reader-mcp) | — | TypeScript | SheetJS, chunked reading |

## Microsoft Word

### GongRzhe/Office-Word-MCP-Server (ARCHIVED)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Office-Word-MCP-Server](https://github.com/GongRzhe/Office-Word-MCP-Server) | 1,900 | Python | — | 20+ |

**⚠️ ARCHIVED on March 3, 2026** — now read-only with no further development. Was the second most-starred office MCP server. The code still works but will receive no updates or bug fixes. Rich Word document manipulation via python-docx:

- **Document lifecycle** — create, read, extract properties
- **Content insertion** — headings, paragraphs, tables, images, page breaks
- **Lists** — bulleted and numbered with proper XML formatting
- **Text formatting** — bold, italic, underline, color, font customization
- **Table operations** — cell shading, merging, alignment, padding, column width
- **Search and replace** — find and modify content
- **Document protection** — password protection, digital signatures
- **Comments** — extraction and filtering
- **PDF conversion** — export documents to PDF
- **Footnotes and endnotes** — academic and professional document support
- **Document merging** — combine multiple documents

No Microsoft Office installation needed. Still functional as a fork-and-maintain option, but the archiving creates a gap for actively maintained Word MCP servers.

### ForLegalAI/mcp-ms-office-documents (Multi-Format)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-ms-office-documents](https://github.com/ForLegalAI/mcp-ms-office-documents) | 26 | Python | MIT | 5+ |

**Transferred from dvejsada to the ForLegalAI org** — generates **multiple Office formats from a single server**:

- PowerPoint presentations (4:3 and 16:9)
- Word documents with Markdown support
- Excel spreadsheets from Markdown tables with formula support
- HTML email drafts
- Dynamic templates with `{{placeholder}}` syntax

Cloud storage integration (AWS S3, Google Cloud Storage, Azure Blob, MinIO), Docker deployment, and optional API key authentication. With Office-Word-MCP-Server archived, this becomes a more important option for Word document generation.

## LibreOffice

### WaterPistolAI/libreoffice-mcp (Best LibreOffice)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [libreoffice-mcp](https://github.com/WaterPistolAI/libreoffice-mcp) | 20 | Python | — | 20+ |

The most comprehensive LibreOffice MCP adapter — supports **Writer, Calc, Impress, Draw, and Base**:

- **Calc** — cell manipulation, sheet management, formulas, charts, conditional formatting, data analysis
- **Writer** — text insertion, table creation, image embedding, styling
- **Impress** — slide insertion and management
- **Draw** — shape creation
- **Base** — query execution, table management, data insertion
- **Cross-document** — property management, macro execution, form controls

Built on the OooDev library (Pythonic abstractions over LibreOffice's UNO API). Requires LibreOffice running with socket connection on port 2083. Work-in-progress but already functional.

### Other LibreOffice Servers

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [patrup/mcp-libre](https://github.com/patrup/mcp-libre) | — | — | Embedded MCP in LibreOffice, native integration |
| [harshithb3304/libre-office-mcp](https://github.com/harshithb3304/libre-office-mcp) | — | Python | Document bridge for AI assistants |

## Generic Spreadsheet Tools

### PSU3D0/spreadsheet-mcp (Token-Efficient)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [spreadsheet-mcp](https://github.com/PSU3D0/spreadsheet-mcp) | 43 | Rust | MIT/Apache-2.0 | 10+ |

Designed **specifically for LLM agents** with token efficiency in mind:

- **Dense JSON encoding** — minimizes token usage for spreadsheet data
- **Formula recalculation engine** (Formualizer) — native formula support
- **Batch operations** — transform, style, formula patterns, structure, validation
- **Diff detection** — compare workbook versions
- **Deterministic pagination** — handle large datasets without context overflow
- **Formula dependency tracing** — understand calculation chains

Supports .xlsx/.xlsm (read+write) and .xls/.xlsb (discovery). Slim Docker image at ~15MB. Built in Rust for performance.

## Full Office Suite Automation

### OfficeMCP/OfficeMCP (Windows COM)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [OfficeMCP](https://github.com/OfficeMCP/OfficeMCP) | 79 | Python | — | 13 |

Controls **the entire Microsoft Office suite** via Windows COM interface:

- Word, Excel, Outlook, PowerPoint, Access, OneNote, Publisher, Visio, Project
- Also supports WPS Office
- Application launching, visibility control, file management
- Demo modes for each application
- Python code execution within server context

Windows-only by nature. More of an automation framework than a document manipulation tool — it launches and controls applications rather than directly editing file formats.

### Softeria/ms-365-mcp-server (NEW — Best M365 Community)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server) | 668 | — | — | 200+ |

**NEW since last review** — the most comprehensive Microsoft 365 MCP server with 200+ tools via Graph API:

- **Excel** — spreadsheet operations through Microsoft Graph
- **OneDrive** — file management and sharing
- **Outlook** — email and calendar operations
- **Teams** — messaging and channel management
- **SharePoint** — site and document library access

Supports org-mode and China 21Vianet cloud deployment. Fills the OneDrive gap identified in the original review.

### microsoft/mcp (Official Microsoft)

| Server | Stars | Language | License | Focus |
|--------|-------|----------|---------|-------|
| [microsoft/mcp](https://github.com/microsoft/mcp) | 3,100 | C# | MIT | Azure + Fabric MCP |

The **official Microsoft MCP catalog** (2,800→3,100 stars) — provides core libraries, test frameworks, and primary servers:

- **Azure MCP Server** — unified access to Azure services
- **Microsoft Fabric MCP Server** — AI-assisted development for Fabric workloads
- **Azure DevOps, AKS, Dataverse, Dev Box, Foundry** servers (expanded)

**MCP is now GA in Copilot Studio** — agents can integrate MCP servers directly. Agent 365 MCP servers launched (Frontier program) for Copilot Search, SharePoint/OneDrive, Outlook Mail, and Outlook Calendar. MCP Apps in Copilot Chat (April 2026) render interactive UI (expense forms, dashboards) inside Copilot. Azure MCP Server is built into Visual Studio 2026.

## What's missing

- **Actively maintained Word MCP server** — Office-Word-MCP-Server was archived; no clear successor for dedicated Word document creation
- **Google official Sheets/Docs MCP** — Google launched official MCP servers for Gmail, Drive, Calendar, Chat, and People, but pointedly omits Sheets and Docs
- **Real-time collaborative editing** — no server supports live co-authoring (Google Docs style)
- **Apple Numbers** — no MCP server for Apple's spreadsheet app
- **WPS Office standalone** — only supported via OfficeMCP's COM on Windows
- **Conflict resolution** — no handling for concurrent multi-agent edits to the same document
- **Notion-to-Office bridge** — no format conversion between Notion and Office formats

## The bottom line

**Rating: 4/5** — The spreadsheet and office suite MCP ecosystem remains strong with significant movement since our last review. **Excel had the biggest story** — haris-musa/excel-mcp-server exploded to 3,800 stars, becoming the most-starred dedicated spreadsheet MCP server, while sbroenne's COM-based server nearly doubled with aggressive daily releases. **Google Workspace grew to 2,300 stars** with meaningful feature additions. The **M365 ecosystem expanded** with Softeria's 668-star community server (200+ tools via Graph API) and Microsoft making MCP GA in Copilot Studio. The **Office-Word-MCP-Server archiving** (1,900 stars, read-only) creates a gap in actively maintained Word document creation. Google's decision to launch official MCP servers while omitting Sheets and Docs is notable — community servers remain essential. Rating holds at 4/5: the Excel surge and M365 expansion are positives, offset by the Word gap and Google's official omission of Sheets/Docs.

*Last refreshed 2026-05-01 using Claude Opus 4.6 (Anthropic). First published 2026-03-16.*
