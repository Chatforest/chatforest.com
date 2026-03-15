---
title: "Spreadsheet & Office Suite MCP Servers — Google Sheets, Excel, Word, Google Docs, LibreOffice, Google Workspace, and More"
date: 2026-03-17T00:30:00+09:00
description: "Spreadsheet and office suite MCP servers are giving AI agents full control over documents and data — reading and writing Excel files, managing Google Sheets, creating Word documents, editing Google Docs, and automating entire Google Workspace workflows via the Model Context Protocol. We reviewed 35+ servers across 6 subcategories. Google Sheets: xing5/mcp-google-sheets (737 stars, Python — 19 tools, multi-auth, zero-install via uvx), mkummer225/google-sheets-mcp (Google Sheets connector), domdomegg/google-sheets-mcp (read/write/manage), shionhonda/mcp-gsheet (list/read/write), freema/mcp-gsheets (Claude Code compatible), isaacphi/mcp-gdrive (Drive + Sheets combined), ajaysmb/gsheets-mcp (auto-formatting + charts), kazz187/mcp-google-spreadsheet. Excel: negokaz/excel-mcp-server (878 stars, Go — 7 tools, formula support, live editing on Windows, screenshot capture), sbroenne/mcp-server-excel (76 stars, C# — 25 tools, 225+ operations, COM API — Power Query, DAX, VBA, PivotTables, Charts), haris-musa/excel-mcp-server (Python, comprehensive manipulation), yzfly/mcp-excel-server (natural language interaction), guillehr2/Excel-MCP-Server-Master (XLSX/XLSM without Excel installed), ArchimedesCrypto/excel-reader-mcp (SheetJS, chunked reading). Microsoft Word: GongRzhe/Office-Word-MCP-Server (1,700 stars, Python — document creation/reading/manipulation, tables, images, formatting, PDF conversion, protection, footnotes, comments), dvejsada/mcp-ms-office-documents (18 stars, MIT — PowerPoint, Word, Excel, HTML email generation, cloud storage integration, Docker). Google Docs & Workspace: taylorwilsdon/google_workspace_mcp (1,800 stars, Python, MIT — 12+ services: Gmail, Drive, Docs, Sheets, Slides, Calendar, Forms, Tasks, Chat, Contacts, Search, Apps Script), a-bonus/google-docs-mcp (377 stars, TypeScript, MIT — Docs/Sheets/Drive with formatting, comments, templates), ngs/google-mcp-server (multi-account, Calendar/Drive/Gmail/Sheets/Docs/Slides), MarkusPfundstein/mcp-gsuite (GSuite interaction). LibreOffice: WaterPistolAI/libreoffice-mcp (17 stars, Python — Writer/Calc/Impress/Draw/Base, charts, formulas), patrup/mcp-libre (embedded MCP in LibreOffice, native integration), harshithb3304/libre-office-mcp (Python, document bridge). Generic Spreadsheet: PSU3D0/spreadsheet-mcp (39 stars, Rust — token-efficient, formula recalculation engine, batch operations, diff detection). Microsoft Official: microsoft/mcp (2,800 stars, C# — Azure MCP + Fabric MCP, catalog of official Microsoft MCP servers). Full Office Automation: OfficeMCP/OfficeMCP (63 stars, Python — Word/Excel/Outlook/PowerPoint/Access/OneNote/Visio/Project via COM). Gaps: no real-time collaborative editing, no OneDrive MCP, no Notion-to-Office bridge, no spreadsheet visualization/charting-only server, no Apple Numbers, no WPS Office, no conflict resolution for concurrent edits. 35+ servers across 6 subcategories. Rating: 4/5."
og_description: "Spreadsheet & Office Suite MCP servers: google_workspace_mcp (1,800 stars — 12+ Google services), Office-Word-MCP-Server (1,700 stars — full Word automation), excel-mcp-server (878 stars — Go, formulas, screenshots), mcp-google-sheets (737 stars — 19 tools), google-docs-mcp (377 stars — Docs/Sheets/Drive). 35+ servers reviewed. Rating: 4/5."
content_type: "Review"
card_description: "Spreadsheet and office suite MCP servers for AI-powered document creation, spreadsheet automation, and office workflow management. **Google Workspace gets a comprehensive 1,800-star server** — taylorwilsdon/google_workspace_mcp (MIT, Python) covers Gmail, Drive, Docs, Sheets, Slides, Calendar, Forms, Tasks, Chat, Contacts, Custom Search, and Apps Script in a single MCP server. OAuth 2.0/2.1 authentication with multi-user support, CLI mode for scripting, and tool filtering to reduce context usage. This is the most complete office productivity MCP server available — one server to control your entire Google Workspace. **Microsoft Word has the second most-starred office MCP server** — GongRzhe/Office-Word-MCP-Server (1,700 stars, Python) provides rich document manipulation: create documents, insert headings/paragraphs/tables/images/page breaks, format text (bold, italic, underline, colors, fonts), manage tables (cell shading, merging, alignment, padding, column width), search and replace, document protection with passwords and digital signatures, comment extraction, PDF conversion, footnotes/endnotes, and document merging. It uses python-docx under the hood, so no Microsoft Office installation required. **Google Sheets is the most-contested subcategory** — 8+ independent MCP server implementations compete for the same use case. xing5/mcp-google-sheets (737 stars, Python) leads with 19 tools covering list/create/read/write/search/share/batch operations, 4 authentication methods (Service Account, OAuth 2.0, direct credentials, Application Default), and zero-install deployment via uvx. mkummer225/google-sheets-mcp, domdomegg/google-sheets-mcp, shionhonda/mcp-gsheet, freema/mcp-gsheets, isaacphi/mcp-gdrive, ajaysmb/gsheets-mcp, and kazz187/mcp-google-spreadsheet all offer overlapping functionality. The fragmentation means users have choices, but also means no single implementation has consolidated community effort. **Excel MCP servers split between file-based and COM-based approaches** — negokaz/excel-mcp-server (878 stars, Go, MIT) works cross-platform by reading/writing XLSX files directly — 7 tools for describing sheets, reading data with pagination, writing cells, creating tables, copying sheets, formatting ranges, and capturing screenshots (Windows only). sbroenne/mcp-server-excel (76 stars, C#, MIT) takes the opposite approach — it controls a live Excel application through COM API on Windows, providing 25 tools with 225+ operations covering Power Query, DAX measures, VBA macros, PivotTables, Charts, Slicers, Conditional Formatting, Named Ranges, Data Connections, and calculation mode control. If you need Power Query or PivotTables, this is the only option. haris-musa/excel-mcp-server, yzfly/mcp-excel-server, guillehr2/Excel-MCP-Server-Master, and ArchimedesCrypto/excel-reader-mcp provide additional Python and TypeScript alternatives. **Google Docs gets dedicated coverage** — a-bonus/google-docs-mcp (377 stars, TypeScript, MIT) provides full Google Docs API access including document reading (plain text, JSON, markdown), text insertion and styling (bold, italic, colors, fonts, links), paragraph formatting, tables, images, page breaks, multi-tab documents, and comment management (create, reply, resolve, delete). Also covers Google Sheets (ranges, formatting, dropdowns, named tables) and Google Drive (search, create, move, copy, rename). **The multi-document generation server is worth noting** — dvejsada/mcp-ms-office-documents (18 stars, MIT, Python) generates PowerPoint, Word, Excel, and HTML email files from a single MCP server. Supports dynamic templates with {{placeholder}} syntax, formula support in spreadsheets, cloud storage integration (AWS S3, Google Cloud Storage, Azure Blob, MinIO), time-limited download links, Docker deployment, and optional API key authentication. Ideal for automated report generation workflows. **LibreOffice gets MCP adapters** — WaterPistolAI/libreoffice-mcp (17 stars, Python) is the most comprehensive, supporting Writer, Calc, Impress, Draw, and Base with charts, conditional formatting, macros, and form controls. It requires LibreOffice running with a socket connection. patrup/mcp-libre provides native embedded MCP integration directly within LibreOffice. harshithb3304/libre-office-mcp offers another Python bridge. **Generic spreadsheet tools exist** — PSU3D0/spreadsheet-mcp (39 stars, Rust) is designed specifically for LLM agents with token-efficient dense JSON encoding, a native formula recalculation engine (Formualizer), batch operations, diff detection between workbook versions, and deterministic pagination. Supports .xlsx/.xlsm read+write and .xls/.xlsb discovery. Slim Docker image at 15MB. **OfficeMCP automates the full Microsoft Office suite** — OfficeMCP/OfficeMCP (63 stars, Python) controls Word, Excel, Outlook, PowerPoint, Access, OneNote, Publisher, Visio, and Project via Windows COM interface. Also supports WPS Office. Windows-only by nature. Includes demo modes, text-to-speech, and Python code execution within the server context. **Microsoft's official MCP catalog exists** — microsoft/mcp (2,800 stars, C#) provides Azure MCP Server and Microsoft Fabric MCP Server, with pointers to additional official servers for Azure DevOps, AKS, Microsoft 365, and more. This is the official Microsoft entry point for MCP. **Major gaps remain** — no real-time collaborative editing through MCP (Google Docs collaboration is view/edit, not live co-authoring). No OneDrive-specific MCP server (Drive operations are covered by workspace servers). No Notion-to-Office format bridge. No Apple Numbers MCP server. No WPS Office standalone MCP (OfficeMCP covers it via COM on Windows). No spreadsheet-only visualization/charting server (charts exist within broader servers). No conflict resolution for concurrent multi-agent edits to the same document. The category earns 4/5 — the spreadsheet and office suite MCP ecosystem is genuinely strong. Google Workspace gets the best single-server coverage at 1,800 stars with 12+ services. Word document creation is mature at 1,700 stars. Google Sheets has the most competitive subcategory with 8+ implementations. Excel splits intelligently between cross-platform file manipulation and Windows-native COM automation. LibreOffice has working adapters. The main weakness is fragmentation — rather than one great Google Sheets server, there are 8 adequate ones. But the category covers the core office productivity workflow well: create documents, manage spreadsheets, automate workspace operations."
---

Spreadsheet and office suite MCP servers let AI assistants create Word documents, read and write Excel files, manage Google Sheets, edit Google Docs, and automate entire Google Workspace workflows. Instead of manually formatting documents and copying data between spreadsheets, you can have AI agents handle the full office productivity stack through the Model Context Protocol.

This review covers the **spreadsheet and office suite** ecosystem — Google Sheets, Excel, Microsoft Word, Google Docs, Google Workspace, LibreOffice, and generic spreadsheet tools. For presentation-specific servers, see our [Presentation & Slides review](/reviews/presentation-slides-mcp-servers/). For email servers, see our [Outlook review](/reviews/outlook-mcp-servers/) and [Gmail review](/reviews/gmail-mcp-server/).

The headline findings: **taylorwilsdon/google_workspace_mcp (1,800 stars) covers 12+ Google services** in one server. **GongRzhe/Office-Word-MCP-Server (1,700 stars) provides rich Word document automation**. **Google Sheets has 8+ competing implementations** — the most contested subcategory. **Excel splits between cross-platform file tools and Windows COM automation**. The Microsoft official MCP catalog at 2,800 stars provides the entry point for Azure and Fabric.

## Google Workspace (Comprehensive)

### taylorwilsdon/google_workspace_mcp (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | 1,800 | Python | MIT | 50+ |

The **most comprehensive office productivity MCP server** — covers 12+ Google services in a single installation:

- **Gmail** — complete email management with end-to-end coverage
- **Google Drive** — file operations with Office format support
- **Google Docs** — document creation, editing, and comments
- **Google Sheets** — spreadsheet operations with flexible cell management
- **Google Slides** — presentation creation and manipulation
- **Google Calendar** — full calendar management
- **Google Forms** — form creation, publish settings, response management
- **Google Tasks** — task and task list management with hierarchy
- **Google Chat** — space management and messaging
- **Google Contacts** — contact management via People API
- **Custom Search** — Programmable Search Engine integration
- **Google Apps Script** — cross-application workflow automation

Features **OAuth 2.0/2.1 with multi-user support**, CLI mode for scripting, and tool filtering to reduce context usage. If you use Google Workspace, this is the one server to install.

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
| [mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) | 737 | Python | — | 19 |

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
| [google-docs-mcp](https://github.com/a-bonus/google-docs-mcp) | 377 | TypeScript | MIT | 30+ |

Full Google Docs API access with rich editing capabilities:

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

### negokaz/excel-mcp-server (Most Popular Excel)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [excel-mcp-server](https://github.com/negokaz/excel-mcp-server) | 878 | Go | MIT | 7 |

The **most starred Excel MCP server** — works cross-platform by reading/writing XLSX files directly:

- `excel_describe_sheets` — list sheet information
- `excel_read_sheet` — retrieve cell values with pagination
- `excel_write_to_sheet` — update cell contents (text values and formulas)
- `excel_create_table` — generate tables within sheets
- `excel_copy_sheet` — duplicate existing sheets
- `excel_format_range` — apply styling to cell ranges
- `excel_screen_capture` — take screenshots of sheets (Windows only)

No Microsoft Office installation required. Built in Go for fast execution.

### sbroenne/mcp-server-excel (Most Powerful Excel)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-excel](https://github.com/sbroenne/mcp-server-excel) | 76 | C# | MIT | 25 |

Controls a **live Excel application through COM API** — Windows-only but with 225+ operations:

- **Power Query** — M code management, load destinations
- **DAX measures** — Data Model with auto-formatted code
- **VBA** — module management and execution
- **PivotTables** — creation, fields, aggregations, calculated members
- **Charts** — creation, configuration, series, formatting, trendlines
- **Slicers** — interactive filtering
- **Conditional formatting** — rules management
- **Data Connections** — OLEDB/ODBC management
- **Screenshot capture** — for LLM verification

If you need Power Query, PivotTables, or VBA automation, this is the only option. Requires Excel installed on Windows.

### Other Excel Servers

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) | — | Python | Comprehensive manipulation |
| [yzfly/mcp-excel-server](https://github.com/yzfly/mcp-excel-server) | — | — | Natural language interaction, visualization |
| [guillehr2/Excel-MCP-Server-Master](https://github.com/guillehr2/Excel-MCP-Server-Master) | — | — | XLSX/XLSM without Excel installed |
| [ArchimedesCrypto/excel-reader-mcp](https://github.com/ArchimedesCrypto/excel-reader-mcp) | — | TypeScript | SheetJS, chunked reading |

## Microsoft Word

### GongRzhe/Office-Word-MCP-Server (Best Word)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Office-Word-MCP-Server](https://github.com/GongRzhe/Office-Word-MCP-Server) | 1,700 | Python | — | 20+ |

The **second most-starred office MCP server** — rich Word document manipulation:

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

Uses python-docx — no Microsoft Office installation needed.

### dvejsada/mcp-ms-office-documents (Multi-Format)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-ms-office-documents](https://github.com/dvejsada/mcp-ms-office-documents) | 18 | Python | MIT | 5+ |

Generates **multiple Office formats from a single server**:

- PowerPoint presentations (4:3 and 16:9)
- Word documents with Markdown support
- Excel spreadsheets from Markdown tables with formula support
- HTML email drafts
- Dynamic templates with `{{placeholder}}` syntax

Cloud storage integration (AWS S3, Google Cloud Storage, Azure Blob, MinIO), Docker deployment, and optional API key authentication. Good for automated report generation pipelines.

## LibreOffice

### WaterPistolAI/libreoffice-mcp (Best LibreOffice)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [libreoffice-mcp](https://github.com/WaterPistolAI/libreoffice-mcp) | 17 | Python | — | 20+ |

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
| [spreadsheet-mcp](https://github.com/PSU3D0/spreadsheet-mcp) | 39 | Rust | MIT/Apache-2.0 | 10+ |

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
| [OfficeMCP](https://github.com/OfficeMCP/OfficeMCP) | 63 | Python | — | 13 |

Controls **the entire Microsoft Office suite** via Windows COM interface:

- Word, Excel, Outlook, PowerPoint, Access, OneNote, Publisher, Visio, Project
- Also supports WPS Office
- Application launching, visibility control, file management
- Demo modes for each application
- Python code execution within server context

Windows-only by nature. More of an automation framework than a document manipulation tool — it launches and controls applications rather than directly editing file formats.

### microsoft/mcp (Official Microsoft)

| Server | Stars | Language | License | Focus |
|--------|-------|----------|---------|-------|
| [microsoft/mcp](https://github.com/microsoft/mcp) | 2,800 | C# | MIT | Azure + Fabric MCP |

The **official Microsoft MCP catalog** — provides core libraries, test frameworks, and two primary servers:

- **Azure MCP Server** — unified access to Azure services
- **Microsoft Fabric MCP Server** — AI-assisted development for Fabric workloads

Links to additional official Microsoft MCP servers for Azure DevOps, AKS, Microsoft 365, and data analytics platforms. This is Microsoft's entry point into the MCP ecosystem.

## What's missing

- **Real-time collaborative editing** — no server supports live co-authoring (Google Docs style)
- **OneDrive** — no dedicated MCP server (workspace servers cover Drive operations)
- **Apple Numbers** — no MCP server for Apple's spreadsheet app
- **WPS Office standalone** — only supported via OfficeMCP's COM on Windows
- **Conflict resolution** — no handling for concurrent multi-agent edits to the same document
- **Spreadsheet visualization** — no charting-only server (charts exist within broader servers)
- **Notion-to-Office bridge** — no format conversion between Notion and Office formats

## The bottom line

**Rating: 4/5** — The spreadsheet and office suite MCP ecosystem is genuinely strong. Google Workspace gets the best single-server coverage (1,800 stars, 12+ services). Word document creation is mature (1,700 stars). Google Sheets has the most competitive subcategory with 8+ implementations. Excel splits intelligently between cross-platform file manipulation (Go, 878 stars) and Windows-native COM automation (C#, 225+ operations). LibreOffice has working adapters. The Microsoft official catalog provides the institutional backing. The main weakness is fragmentation — rather than consolidating effort into one great Google Sheets server, the community has built 8 adequate ones. But the category covers the core office productivity workflow well: create documents, manage spreadsheets, automate workspace operations. If you use Google Workspace, install taylorwilsdon's server. If you work with Excel files, negokaz's Go server works everywhere. If you need Word documents, GongRzhe's server doesn't even need Office installed.
