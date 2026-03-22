---
title: "Best Spreadsheet MCP Servers in 2026 — Excel vs Google Sheets vs Airtable vs Smartsheet"
date: 2026-03-22T18:00:00+09:00
description: "We compared 25+ spreadsheet MCP servers across Excel, Google Sheets, Airtable, Smartsheet, and LibreOffice. Here's which ones are worth using — and which approach fits your workflow."
og_description: "25+ spreadsheet MCP servers compared: Excel, Google Sheets, Airtable, Smartsheet, LibreOffice. Honest recommendations from research."
content_type: "Comparison"
card_description: "excel-mcp-server (3,500 stars, Python, cross-platform) vs google_workspace_mcp (1,900 stars, full suite) vs Airtable (official + 429-star community) vs Smartsheet (official, 15 tools) — plus Go, C#, and LibreOffice options."
last_refreshed: 2026-03-22
---

Spreadsheets are arguably the world's most-used data tool, and connecting AI agents to them is a high-value use case — from financial modeling to data cleaning to automated reporting. The MCP ecosystem has responded with dozens of servers, and the landscape is more nuanced than you'd expect.

The ecosystem splits four ways. **Excel** has the most popular single server (3,500 stars, Python, works without Excel installed). **Google Sheets** has the most options (10+ repos, from dedicated Sheets servers to full Workspace suites). **Airtable** bridges spreadsheet and database territory with both official and community servers. **Smartsheet** quietly shipped an official MCP server with safety controls.

What surprised us: **Airtable has an official MCP server** (launched February 2026), but Google and Microsoft still haven't released official standalone spreadsheet servers. Meanwhile, a C# Windows server controls live Excel processes for Power Query, DAX, and VBA — features no file-based server can touch.

**Disclosure:** Our recommendations are based on research — analyzing documentation, GitHub repositories, community feedback, and published benchmarks. We have not hands-on tested every server in this guide.

## At a Glance: Top Picks

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| **Excel (cross-platform)** | [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) | 3,500 | [negokaz/excel-mcp-server](https://github.com/negokaz/excel-mcp-server) (891, Go) |
| **Excel (Windows power user)** | [sbroenne/mcp-server-excel](https://github.com/sbroenne/mcp-server-excel) | 88 | — |
| **Google Sheets (full Workspace)** | [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | 1,900 | [xing5/mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) (753, Sheets-only) |
| **Google Sheets (dedicated)** | [xing5/mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) | 753 | [freema/mcp-gsheets](https://github.com/freema/mcp-gsheets) (52, 25+ tools) |
| **Airtable** | [domdomegg/airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server) | 429 | [rashidazarang/airtable-mcp](https://github.com/rashidazarang/airtable-mcp) (73, 42 tools) |
| **Smartsheet** | [smartsheet-platform/smar-mcp](https://github.com/smartsheet-platform/smar-mcp) | 25 | [terilios/smartsheet-server](https://github.com/terilios/smartsheet-server) (10, 34 tools) |
| **LibreOffice** | [WaterPistolAI/libreoffice-mcp](https://github.com/WaterPistolAI/libreoffice-mcp) | 17 | [patrup/mcp-libre](https://github.com/patrup/mcp-libre) (embedded) |

## Excel Servers (Cross-Platform)

These servers manipulate Excel files directly using programming libraries — no Microsoft Excel installation needed. They work on macOS, Linux, and Windows.

### haris-musa/excel-mcp-server — The Winner

**Stars:** 3,500 | **Language:** Python | **License:** MIT

The most popular spreadsheet MCP server of any kind. Uses openpyxl to read, create, and modify Excel files without Microsoft Excel installed.

**What makes it stand out:**
- **25 tools across 10 categories** — workbook operations, data manipulation, formatting, formulas with validation, charts (line, bar, pie, scatter), pivot tables, tables, worksheet operations, range operations, row/column operations
- **Cross-platform** — pure Python means it runs on macOS, Linux, and Windows without any Microsoft software. Perfect for servers and CI/CD
- **Multiple transports** — supports stdio and Streamable HTTP (SSE deprecated). Flexible for desktop apps, web services, and remote deployments
- **Configurable sandbox** — `EXCEL_FILES_PATH` env var restricts file access to a specific directory
- **Highest adoption** — 3,500 stars means bugs get found and fixed. The largest community of any spreadsheet MCP server

**Limitations:**
- File-based approach — can't interact with a running Excel instance, trigger recalculations, or work with Excel add-ins
- Can write formulas but can't evaluate them — results appear when the file is opened in Excel or Sheets
- No IRM/AIP support for encrypted or rights-managed files
- Community-maintained — no Microsoft backing

**Best for:** Most developers. Start here unless you need live Excel integration or advanced features like Power Query.

### negokaz/excel-mcp-server — Go Alternative

**Stars:** 891 | **Language:** Go | **License:** MIT

A lighter Excel MCP server written in Go. Single binary, no Python or Node.js dependency.

**What makes it stand out:**
- **7 focused tools** — describe_sheets, read_sheet, screen_capture, write_to_sheet, create_table, copy_sheet, format_range
- **Pagination** — handles large spreadsheets with a default 4,000-cell batch size
- **Windows live editing** — on Windows, can interact with a running Excel instance and capture screen shots
- **Multiple formats** — supports XLSX, XLSM, XLTX, XLTM

**Limitations:**
- Fewer tools than haris-musa (7 vs 25) — no charts, pivot tables, or formulas
- Windows-only for live editing features
- Smaller community (891 vs 3,500 stars)

**Best for:** Teams that prefer Go binaries over Python, or need large spreadsheet pagination.

### yzfly/mcp-excel-server — Analysis-Focused

**Stars:** 85 | **Language:** Python | **License:** MIT

An analysis-oriented server that reads multiple tabular formats (XLSX, XLS, CSV, TSV, JSON) and provides statistical analysis and visualization.

**What makes it stand out:**
- **Multi-format** — reads Excel, CSV, TSV, and JSON files with one server
- **Built-in analysis** — statistical operations and data profiling out of the box
- **Visualization** — generates charts from tabular data

**Best for:** Data analysts who work with mixed file formats and need quick stats.

## Excel Servers (Windows / Live Integration)

### sbroenne/mcp-server-excel — Windows Power Users

**Stars:** 88 | **Language:** C# | **License:** MIT

The most feature-rich Excel MCP server — but Windows only. Uses COM interop to control live Excel processes, giving access to features no file-based server can match.

**What makes it stand out:**
- **25 tools, 230 operations** — the broadest operation set of any spreadsheet MCP server
- **Power Query & M code** — create, edit, and refresh Power Query transformations. No other MCP server supports this
- **DAX measures** — add DAX measures to data models. Unique capability
- **VBA macro execution** — run and manage VBA macros through MCP
- **PivotTables** — full PivotTable creation and manipulation with data connections
- **Screenshot capture** — capture Excel screenshots for LLM verification of visual output
- **Data connections** — OLEDB/ODBC connections for external data
- **Actively maintained** — v1.8.32 released March 20, 2026

**Limitations:**
- **Windows only** — requires COM interop with Microsoft Excel 2016+
- **Controls live Excel processes** — not suitable for headless/server environments
- **Heavyweight** — requires full Excel installation plus .NET runtime

**Best for:** Windows power users who need Power Query, DAX, VBA, or PivotTable manipulation. The only option for advanced Excel features.

### sbraind/excel-mcp-server — macOS Live Integration

**Stars:** ~5 | **Language:** TypeScript | **License:** MIT

A smaller server that provides macOS real-time editing via AppleScript integration with running Excel instances.

**What makes it stand out:**
- **34 tools** — read/write, formatting, pivot tables, charts, conditional formatting
- **macOS AppleScript** — interacts with open Excel workbooks on macOS
- **Backup creation** — automatic backups before modifications

**Best for:** macOS users who want live Excel interaction (AppleScript-based).

## Google Sheets Servers

Google has not released an official standalone Google Sheets MCP server. The community has filled the gap with excellent options ranging from full Workspace suites to Sheets-dedicated servers.

### taylorwilsdon/google_workspace_mcp — The Full Suite Winner

**Stars:** 1,900 | **Language:** Python | **License:** MIT

The most comprehensive Google Workspace MCP server. Covers Sheets alongside Gmail, Drive, Calendar, Docs, Slides, Forms, Tasks, Contacts, and Chat — 10+ Google services in one server.

**What makes it stand out:**
- **Full Workspace coverage** — if you need Sheets access, you probably also need Drive, Gmail, and Calendar. One server covers everything
- **OAuth 2.1** — modern authentication with multi-user bearer token support for organizations
- **Read-only mode** — can restrict the entire server to read-only operations
- **Per-service permissions** — enable only the Google services you need
- **.dxt package** — one-click install for Claude Desktop
- **1,654 commits** — heavily maintained, actively developed

**Limitations:**
- Sheets is one module among many — not as deep as dedicated Sheets servers
- Requires Google Cloud project with OAuth credentials (non-trivial setup)
- Large surface area increases potential attack surface
- Python dependency

**Best for:** Anyone who needs Google Sheets plus other Google services. Start here for Workspace access.

### xing5/mcp-google-sheets — The Sheets Specialist

**Stars:** 753 | **Language:** Python | **License:** MIT

The most feature-rich Google Sheets-only MCP server. Focused entirely on Sheets operations.

**What makes it stand out:**
- **19 tools** — full CRUD, batch operations, formatting, sharing permissions
- **Tool filtering** — disable unused tools to save ~13K tokens of context window. Unique optimization
- **Flexible auth** — supports Service Accounts (headless), OAuth 2.0 (interactive), and credential injection (CI/CD)
- **Docker support** — containerized deployment available
- **Batch operations** — efficient multi-cell/multi-row updates

**Limitations:**
- Sheets only — no Gmail, Calendar, or Drive integration
- Smaller community than google_workspace_mcp

**Best for:** Teams that only need Google Sheets access and want maximum depth. The tool filtering feature is valuable for context-window-constrained clients.

### Other Google Sheets Options

- **[a-bonus/google-docs-mcp](https://github.com/a-bonus/google-docs-mcp)** (398 stars) — Covers Docs + Sheets + Drive. 11 Sheets-specific tools including formatting, table management, and dropdown validation. TypeScript. Multi-profile auth
- **[mkummer225/google-sheets-mcp](https://github.com/mkummer225/google-sheets-mcp)** (127 stars) — 15 tools covering auth, spreadsheet management, sheet ops, and data manipulation. JavaScript
- **[freema/mcp-gsheets](https://github.com/freema/mcp-gsheets)** (52 stars) — 25+ tools including charts, conditional formatting, and batch ops. Production-ready with full test coverage. TypeScript
- **[isaacphi/mcp-gdrive](https://github.com/isaacphi/mcp-gdrive)** (272 stars) — Primarily Google Drive, but auto-converts Sheets to CSV. 2 basic Sheets tools. Good for read-only access
- **[MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite)** (485 stars) — **Does not support Google Sheets** despite the name. Gmail and Calendar only. Included here because the name is misleading

## Airtable Servers

Airtable bridges the gap between spreadsheets and databases. Both official and community MCP servers exist.

### Airtable Official MCP Server

Launched **February 11, 2026**. Respects existing Airtable permissions — read-only users get read-only MCP access. Compatible with Claude, ChatGPT, Cursor, and other MCP clients. Available through Airtable's platform rather than a standalone GitHub repo.

**Best for:** Teams already on Airtable who want officially supported, permission-respecting access.

### domdomegg/airtable-mcp-server — The Community Winner

**Stars:** 429 | **Language:** TypeScript | **License:** MIT

The most established community Airtable MCP server, published as the `airtable-mcp-server` npm package.

**What makes it stand out:**
- **16 tools** — full CRUD, schema inspection, filtering via Airtable formulas, text search, comments
- **npm package** — easy install via `npx airtable-mcp-server`
- **Multiple transports** — stdio (default) and HTTP
- **Write permissions controlled via token scopes** — use Airtable's own permission system

**Limitations:**
- HTTP transport has no built-in authentication — must deploy behind a reverse proxy
- Community-maintained — may lag behind Airtable API changes

**Best for:** Developers who want a quick, well-tested Airtable integration.

### rashidazarang/airtable-mcp — Maximum Features

**Stars:** 73 | **Language:** TypeScript

The most feature-rich Airtable MCP server.

**What makes it stand out:**
- **42 tools across 13 categories** — the broadest Airtable tool surface
- **Governance controls with PII masking** — unique safety feature for regulated environments
- **10 AI-powered prompt templates** — pre-built workflows
- **Webhooks** — event-driven automation support
- **Batch operations** — up to 10 records per batch

**Best for:** Enterprise teams that need governance controls or the broadest possible Airtable coverage.

### Other Airtable Options

- **[felores/airtable-mcp](https://github.com/felores/airtable-mcp)** (72 stars) — 10 tools, staged table building, Claude-optimized prompts, 9 field types. JavaScript

## Smartsheet Servers

### smartsheet-platform/smar-mcp — Official

**Stars:** 25 | **Language:** TypeScript | **Official**

The official Smartsheet MCP server from the smartsheet-platform organization.

**What makes it stand out:**
- **15 tools** — sheet CRUD, cell history, version backups at specific timestamps, workspace/folder management
- **Safety controls** — delete operations require explicit `ALLOW_DELETE_TOOLS` env var
- **Version backups** — snapshot a sheet at a specific timestamp. Unique among spreadsheet servers
- **Official support** — backed by Smartsheet

**Limitations:**
- ~60+ Smartsheet API endpoints remain unimplemented
- Last significant activity April 2025 — unclear maintenance cadence

**Best for:** Smartsheet users who want officially supported, safety-gated access.

### terilios/smartsheet-server — More Tools

**Stars:** 10 | **Language:** TypeScript + Python | **License:** MIT

Community server with more tools than the official one.

**What makes it stand out:**
- **34 tools** — more than double the official server
- **Healthcare analytics** — clinical notes, patient feedback analysis (domain-specific)
- **Regex search** — search within sheet data using regular expressions
- **Cross-sheet references** — work across multiple sheets
- **Attachment and discussion management**

**Best for:** Power users who need features the official server doesn't cover, particularly in healthcare.

## LibreOffice Calc Servers

The open-source spreadsheet space is early-stage, with no production-ready option yet.

### WaterPistolAI/libreoffice-mcp

**Stars:** 17 | **Language:** Python

Covers Writer, Calc, Impress, and Draw. Calc tools include get_cell_value, set_cell_value, create_new_sheet, set_cell_formula, create_chart, conditional formatting, and range grouping.

**Limitations:** Work in progress. Socket-based transport (port 2083), not standard MCP transports.

### patrup/mcp-libre — Embedded Approach

An embedded MCP server that runs inside LibreOffice as an extension. 10x faster than external servers because it uses the UNO API directly. Real-time editing of open documents.

**Best for:** LibreOffice users willing to experiment with an early-stage embedded approach.

## Decision Flowchart

**Do you work with Excel files?**

→ **Cross-platform, no Excel needed** → haris-musa/excel-mcp-server (Python, 25 tools)

→ **Go binary, no runtime** → negokaz/excel-mcp-server (Go, 7 tools, pagination)

→ **Windows with Power Query / DAX / VBA** → sbroenne/mcp-server-excel (C#, 230 operations)

→ **Analysis of CSV/Excel/JSON** → yzfly/mcp-excel-server (multi-format)

**Do you work with Google Sheets?**

→ **Need other Google services too** → taylorwilsdon/google_workspace_mcp (10+ services)

→ **Sheets only, maximum features** → xing5/mcp-google-sheets (19 tools, tool filtering)

→ **Sheets + Docs + Drive** → a-bonus/google-docs-mcp (11 Sheets tools)

→ **Sheets with charts and formatting** → freema/mcp-gsheets (25+ tools)

**Do you work with Airtable?**

→ **Official, permission-respecting** → Airtable Official MCP (February 2026)

→ **Community, well-tested** → domdomegg/airtable-mcp-server (16 tools)

→ **Enterprise with PII masking** → rashidazarang/airtable-mcp (42 tools, governance)

**Do you work with Smartsheet?**

→ **Official with safety controls** → smartsheet-platform/smar-mcp (delete gating)

→ **More tools, healthcare focus** → terilios/smartsheet-server (34 tools)

## Three Trends Shaping This Space

### 1. File-based vs. live-process — two fundamentally different approaches

The Excel space has split into two camps. File-based servers (haris-musa, negokaz) use libraries like openpyxl to manipulate .xlsx files directly — cross-platform, no Excel needed, but they can't evaluate formulas or interact with running instances. Live-process servers (sbroenne for Windows, sbraind for macOS) control actual Excel applications via COM or AppleScript — giving access to Power Query, DAX, VBA, and real-time recalculation, but locking you to a specific OS. Neither approach is wrong; they serve completely different use cases.

### 2. Official vendors are showing up (selectively)

Airtable launched its official MCP server in February 2026. Smartsheet has had one since early 2025. But Google hasn't released a standalone Sheets server (despite taylorwilsdon's community server handling 1,900 stars worth of demand), and Microsoft hasn't released an official Excel MCP server (leaving community projects to fill the gap). The pattern: smaller platforms with more to gain from AI integration ship official servers faster than incumbents.

### 3. Tool count inflation and context window tradeoffs

Spreadsheet servers are competing on tool count: rashidazarang's Airtable offers 42 tools, freema's Google Sheets offers 25+, sbroenne's Excel offers 230 operations. But more tools mean more context window usage — each tool description consumes tokens. xing5/mcp-google-sheets addressed this with tool filtering, saving ~13K tokens by disabling unused tools. Expect more servers to adopt this pattern as context window efficiency becomes a differentiator.

## What's Missing

- **No official Google Sheets MCP server** — Google hasn't shipped one despite massive demand. Community servers fill the gap but could break on API changes
- **No official Microsoft Excel MCP server** — the world's most-used spreadsheet has no vendor-backed MCP server. Community options are excellent but unofficial
- **No Apple Numbers MCP server** — Apple's spreadsheet is completely absent from the MCP ecosystem
- **Formula evaluation** — file-based Excel servers can write formulas but can't compute results. You get `=SUM(A1:A10)` as text, not the number. Only live-process servers (Windows/macOS) can evaluate
- **No Excel Online / Microsoft 365 MCP** — no server connects to the cloud version of Excel via Microsoft Graph API for collaborative editing
- **Large file handling** — most servers lack strategies for spreadsheets with 100K+ rows. Only negokaz provides pagination (4,000-cell batches)
- **No universal spreadsheet server** — no single server handles Excel + Google Sheets + Airtable. You need separate servers for each platform
- **CSV is underserved** — no well-established, high-star CSV-dedicated MCP server exists. CSV handling is typically a secondary feature of Excel servers
- **No collaborative editing awareness** — no MCP server handles real-time multi-user editing detection or conflict resolution
