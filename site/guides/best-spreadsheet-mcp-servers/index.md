# Best Spreadsheet MCP Servers in 2026 — Excel vs Google Sheets vs Airtable vs Smartsheet

> We compared 25+ spreadsheet MCP servers across Excel, Google Sheets, Airtable, Smartsheet, and LibreOffice. Here's which ones are worth using — and which approach fits your workflow.


Spreadsheets are arguably the world's most-used data tool, and connecting AI agents to them is a high-value use case — from financial modeling to data cleaning to automated reporting. The MCP ecosystem has responded with dozens of servers, and the landscape is more nuanced than you'd expect.

The ecosystem splits four ways. **Excel** has the most popular single server ([4,100 stars](https://github.com/haris-musa/excel-mcp-server), Python, works without Excel installed). **Google Sheets** has the most options (10+ repos, from dedicated Sheets servers to full Workspace suites). **Airtable** bridges spreadsheet and database territory with both official and community servers. **Smartsheet** [deprecated its GitHub MCP server](https://github.com/smartsheet-platform/smar-mcp) in favor of a hosted solution (April 2026).

What surprised us most this refresh: **Microsoft now has indirect MCP coverage** through [Arcade's Office 365 integration](https://www.arcade.dev/blog/microsoft-office-365-mcp-servers-launch/) (launched March 13, 2026) — built by Arcade on top of the Microsoft Graph API as a third party, not a Microsoft partnership or first-party server. Meanwhile, Smartsheet deprecated its open-source repo in favor of a hosted MCP endpoint. And the C# Windows server ([sbroenne](https://github.com/sbroenne/mcp-server-excel)) has kept shipping multiple releases a week, reaching v1.10.5 by August 2026 with in-process architecture and window management additions.

**Disclosure:** Our recommendations are based on research — analyzing documentation, GitHub repositories, community feedback, and published benchmarks. We have not hands-on tested every server in this guide.

## At a Glance: Top Picks

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| **Excel (cross-platform)** | [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) | 4,100 | [negokaz/excel-mcp-server](https://github.com/negokaz/excel-mcp-server) (1,006, Go) |
| **Excel (Windows power user)** | [sbroenne/mcp-server-excel](https://github.com/sbroenne/mcp-server-excel) | 435 | — |
| **Excel (cloud/Microsoft 365)** | [Arcade Office 365 MCP](https://www.arcade.dev/blog/microsoft-office-365-mcp-servers-launch) | NEW | — |
| **Google Sheets (full Workspace)** | [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | 2,994 | [xing5/mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) (979, Sheets-only) |
| **Google Sheets (dedicated)** | [xing5/mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) | 979 | [freema/mcp-gsheets](https://github.com/freema/mcp-gsheets) (90, 44 tools) |
| **Airtable** | [domdomegg/airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server) | 455 | [rashidazarang/airtable-mcp](https://github.com/rashidazarang/airtable-mcp) (87, 42 tools) |
| **Smartsheet** | [Smartsheet hosted MCP](https://developers.smartsheet.com/ai-mcp/smartsheet/mcp-server) | Official | [terilios/smartsheet-server](https://github.com/terilios/smartsheet-server) (12, 34 tools) |
| **LibreOffice** | [patrup/mcp-libre](https://github.com/patrup/mcp-libre) | 94 | [WaterPistolAI/libreoffice-mcp](https://github.com/WaterPistolAI/libreoffice-mcp) (23) |

## Excel Servers (Cross-Platform)

These servers manipulate Excel files directly using programming libraries — no Microsoft Excel installation needed. They work on macOS, Linux, and Windows.

### haris-musa/excel-mcp-server — The Winner

**Stars:** 4,100 | **Language:** Python | **License:** MIT | **Last release:** [v0.1.8](https://github.com/haris-musa/excel-mcp-server/releases) (April 12, 2026)

The most popular spreadsheet MCP server of any kind. Uses openpyxl to read, create, and modify Excel files without Microsoft Excel installed.

**What makes it stand out:**
- **25 tools across 10 categories** — workbook operations, data manipulation, formatting, formulas with validation, charts (line, bar, pie, scatter), pivot tables, tables, worksheet operations, range operations, row/column operations
- **Cross-platform** — pure Python means it runs on macOS, Linux, and Windows without any Microsoft software. Perfect for servers and CI/CD
- **Multiple transports** — supports stdio and Streamable HTTP (SSE deprecated). Flexible for desktop apps, web services, and remote deployments
- **Configurable sandbox** — `EXCEL_FILES_PATH` env var restricts file access to a specific directory
- **Highest adoption** — 4,100 stars means bugs get found and fixed. The largest community of any spreadsheet MCP server

**Limitations:**
- File-based approach — can't interact with a running Excel instance, trigger recalculations, or work with Excel add-ins
- Can write formulas but can't evaluate them — results appear when the file is opened in Excel or Sheets
- No IRM/AIP support for encrypted or rights-managed files
- Community-maintained — no Microsoft backing
- Release cadence is modest — [v0.1.8](https://github.com/haris-musa/excel-mcp-server/releases) (April 2026) was the first release since v0.1.7 in August 2025

**Best for:** Most developers. Start here unless you need live Excel integration or advanced features like Power Query.

### negokaz/excel-mcp-server — Go Alternative

**Stars:** 1,006 | **Language:** Go | **License:** MIT | **Last release:** [v0.12.0](https://github.com/negokaz/excel-mcp-server/releases) (July 2025)

A lighter Excel MCP server written in Go. Single binary, no Python or Node.js dependency.

**What makes it stand out:**
- **7 focused tools** — describe_sheets, read_sheet, screen_capture, write_to_sheet, create_table, copy_sheet, format_range
- **Pagination** — handles large spreadsheets with a default 4,000-cell batch size
- **Windows live editing** — on Windows, can interact with a running Excel instance and capture screen shots
- **Multiple formats** — supports XLSX, XLSM, XLTX, XLTM

**Limitations:**
- Fewer tools than haris-musa (7 vs 25) — no charts, pivot tables, or formulas
- Windows-only for live editing features
- Smaller community (1,006 vs 4,100 stars)
- Last release July 2025 — development has slowed

**Best for:** Teams that prefer Go binaries over Python, or need large spreadsheet pagination.

### yzfly/mcp-excel-server — Analysis-Focused

**Stars:** 96 | **Language:** Python | **License:** MIT

An analysis-oriented server that reads multiple tabular formats (XLSX, XLS, CSV, TSV, JSON) and provides statistical analysis and visualization.

**What makes it stand out:**
- **Multi-format** — reads Excel, CSV, TSV, and JSON files with one server
- **Built-in analysis** — statistical operations and data profiling out of the box
- **Visualization** — generates charts from tabular data

**Best for:** Data analysts who work with mixed file formats and need quick stats.

## Excel Servers (Windows / Live Integration)

### sbroenne/mcp-server-excel — Windows Power Users

**Stars:** 435 | **Language:** C# | **License:** MIT | **Last release:** [v1.10.5](https://github.com/sbroenne/mcp-server-excel/releases) (August 7, 2026) | [excelmcpserver.dev](https://excelmcpserver.dev/)

A feature-rich Excel MCP server — but Windows only. Uses COM interop to control live Excel processes, giving access to features no file-based server can match. Stars have grown roughly 4x (103 to 435) since our last review, and the project has shipped several point releases per week through mid-2026.

**What makes it stand out:**
- **23 tools, 210+ operations across 14 command categories** — the broadest operation set of any spreadsheet MCP server
- **In-process service architecture (NEW)** — no separate service process required. Simpler deployment, fewer moving parts
- **Window management tool (NEW)** — 9 operations for Agent Mode, letting AI agents control Excel window state
- **Power Query & M code** — create, edit, and refresh Power Query transformations. No other MCP server supports this
- **DAX measures** — add DAX measures to data models. Unique capability
- **VBA macro execution** — run and manage VBA macros through MCP
- **PivotTables** — full PivotTable creation and manipulation with data connections
- **Enhanced chart formatting (NEW)** — data labels, axis scaling, trendlines
- **Screenshot capture** — capture Excel screenshots for LLM verification of visual output
- **CLI batch mode (NEW)** — execute multiple commands from JSON files
- **Actively maintained** — [v1.10.5](https://github.com/sbroenne/mcp-server-excel/releases) released August 7, 2026, with multiple point releases in the preceding weeks

**Breaking changes in recent releases:**
- Removed `excel_` prefix from all tool names (e.g., `excel_range` → `range`)
- CLI redesigned with 14 unified command categories
- All CLI commands now require explicit `--session` parameters

**Limitations:**
- **Windows only** — requires COM interop with Microsoft Excel 2016+
- **Controls live Excel processes** — not suitable for headless/server environments
- **Heavyweight** — requires full Excel installation plus .NET runtime

**Best for:** Windows power users who need Power Query, DAX, VBA, or PivotTable manipulation. The only option for advanced Excel features, with one of the fastest release cadences of any spreadsheet MCP server we tracked.

### sbraind/excel-mcp-server — macOS Live Integration

**Stars:** 17 | **Language:** TypeScript | **License:** MIT

A smaller server that provides macOS real-time editing via AppleScript integration with running Excel instances.

**What makes it stand out:**
- **34 tools** — read/write, formatting, pivot tables, charts, conditional formatting
- **macOS AppleScript** — interacts with open Excel workbooks on macOS
- **Backup creation** — automatic backups before modifications

**Best for:** macOS users who want live Excel interaction (AppleScript-based).

## Excel via Microsoft 365 (Cloud)

### Arcade Office 365 MCP Servers — NEW

**Launched:** March 13, 2026 | **Type:** Hosted (Arcade platform) | [arcade.dev](https://www.arcade.dev/blog/microsoft-office-365-mcp-servers-launch)

Five integrated MCP servers for Word, Excel, PowerPoint, OneDrive, and SharePoint, [built by Arcade](https://www.arcade.dev/blog/microsoft-office-365-mcp-servers-launch/) on top of the Microsoft Graph API. Arcade's own announcement describes this as a third-party integration, not a Microsoft partnership — it partially closes the gap of "no official Microsoft Excel MCP server" but isn't Microsoft-endorsed.

**What makes it stand out:**
- **Microsoft Graph API integration** — connects to Excel Online / Microsoft 365, not local files
- **Production-grade** — handles binary file formats, session management, concurrent edits
- **OAuth authentication** — proper Microsoft 365 auth flow
- **Excel capabilities** — create workbooks, read cell data, write values and formulas, manage worksheets
- **Full Office suite** — one integration covers Excel, Word, PowerPoint, OneDrive, SharePoint

**Limitations:**
- **Not first-party Microsoft** — built independently by Arcade on the Microsoft Graph API, not published by Microsoft or a confirmed Microsoft partnership
- **Hosted platform** — runs through Arcade's infrastructure, not self-hosted
- **Cloud-only** — requires Microsoft 365 subscription and internet connection
- **Narrower than sbroenne** — no Power Query, DAX, VBA, or PivotTable support yet

**Best for:** Teams using Microsoft 365 who want cloud Excel integration without managing local installations. Complements rather than replaces file-based or live-process servers.

## Google Sheets Servers

Google has not released an official standalone Google Sheets MCP server. Google Cloud [announced official MCP support](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services) on December 10, 2025 — initially for Maps, BigQuery, Compute Engine, and Kubernetes Engine, reaching general availability in March 2026 and [expanding to 50+ managed servers](https://docs.cloud.google.com/mcp/release-notes) by mid-2026. Google Sheets and the rest of Workspace were never part of that rollout. The community continues to fill the gap with excellent options.

### taylorwilsdon/google_workspace_mcp — The Full Suite Winner

**Stars:** 2,994 | **Language:** Python | **License:** MIT | **Last release:** [v1.23.1](https://github.com/taylorwilsdon/google_workspace_mcp/releases) (August 2, 2026)

The most comprehensive Google Workspace MCP server. Covers Sheets alongside Gmail, Drive, Calendar, Docs, Slides, Forms, Tasks, Contacts, and Chat — 10+ Google services in one server.

**What makes it stand out:**
- **Full Workspace coverage** — if you need Sheets access, you probably also need Drive, Gmail, and Calendar. One server covers everything
- **OAuth 2.1** — modern authentication with multi-user bearer token support for organizations
- **Read-only mode** — can restrict the entire server to read-only operations
- **Per-service permissions** — enable only the Google services you need
- **.dxt package** — one-click install for Claude Desktop
- **Structured table support for Sheets (NEW)** — improved Sheets handling with smart chips and tabs rendering
- **2,600+ commits** — heavily maintained, actively developed

**Limitations:**
- Sheets is one module among many — not as deep as dedicated Sheets servers
- Requires Google Cloud project with OAuth credentials (non-trivial setup)
- Large surface area increases potential attack surface
- Python dependency

**Best for:** Anyone who needs Google Sheets plus other Google services. Start here for Workspace access.

### xing5/mcp-google-sheets — The Sheets Specialist

**Stars:** 979 | **Language:** Python | **License:** MIT

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

- **[a-bonus/google-docs-mcp](https://github.com/a-bonus/google-docs-mcp)** (635 stars) — Covers Docs + Sheets + Drive. 34 Sheets-specific tools including formatting, table management, and dropdown validation. TypeScript. Multi-profile auth. New: listDriveFiles and searchDriveFiles tools, remote deployment via Google Cloud Run
- **[mkummer225/google-sheets-mcp](https://github.com/mkummer225/google-sheets-mcp)** (137 stars) — 15 tools covering auth, spreadsheet management, sheet ops, and data manipulation. JavaScript. Minimal but functional
- **[freema/mcp-gsheets](https://github.com/freema/mcp-gsheets)** (90 stars) — 44 tools including charts, conditional formatting, and batch ops. TypeScript
- **[isaacphi/mcp-gdrive](https://github.com/isaacphi/mcp-gdrive)** (284 stars) — Primarily Google Drive, but auto-converts Sheets to CSV. 2 basic Sheets tools. Good for read-only access. Last commit May 2025 — over a year stale
- **[MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite)** (491 stars) — **Does not support Google Sheets** despite the name. Gmail and Calendar only. **⚠️ Has active bugs** — multiple [open issues](https://github.com/MarkusPfundstein/mcp-gsuite/issues) confirm JSON schema validation errors that break Anthropic API compatibility (e.g. [#53](https://github.com/MarkusPfundstein/mcp-gsuite/issues/53)) and a broken `reply_gmail_email` function ([#49](https://github.com/MarkusPfundstein/mcp-gsuite/issues/49)). Consider alternatives

## Airtable Servers

Airtable bridges the gap between spreadsheets and databases. Both official and community MCP servers exist.

### Airtable Official MCP Server

Airtable runs an [official hosted MCP server](https://support.airtable.com/docs/using-the-airtable-mcp-server) at mcp.airtable.com (available through Airtable's platform rather than a standalone GitHub repo). It respects existing Airtable permissions — Commenter/Read-only users get read-only MCP access, per Airtable's own documentation. Compatible with Claude, ChatGPT, Cursor, and other MCP clients.

**Best for:** Teams already on Airtable who want officially supported, permission-respecting access.

### domdomegg/airtable-mcp-server — The Community Winner

**Stars:** 455 | **Language:** TypeScript | **License:** MIT | **Last release:** [v1.14.0](https://github.com/domdomegg/airtable-mcp-server/releases) (July 27, 2026)

The most established community Airtable MCP server, published as the `airtable-mcp-server` npm package.

**What makes it stand out:**
- **18+ tools** — full CRUD, schema inspection, filtering via Airtable formulas, text search, comments
- **npm package** — easy install via `npx airtable-mcp-server`
- **Multiple transports** — stdio (default) and HTTP
- **Write permissions controlled via token scopes** — use Airtable's own permission system

**Limitations:**
- HTTP transport has no built-in authentication — must deploy behind a reverse proxy
- Community-maintained — may lag behind Airtable API changes

**Best for:** Developers who want a quick, well-tested Airtable integration.

### rashidazarang/airtable-mcp — Maximum Features

**Stars:** 87 | **Language:** TypeScript | **Last release:** [v5.1.0](https://github.com/rashidazarang/airtable-mcp/releases) (August 5, 2026)

The most feature-rich Airtable MCP server.

**What makes it stand out:**
- **42 tools across 13 categories** — the broadest Airtable tool surface
- **Governance controls with PII masking** — unique safety feature for regulated environments
- **10 AI-powered prompt templates** — pre-built workflows
- **Webhooks** — event-driven automation support
- **Batch operations** — up to 10 records per batch

**Best for:** Enterprise teams that need governance controls or the broadest possible Airtable coverage.

### Other Airtable Options

- **[felores/airtable-mcp](https://github.com/felores/airtable-mcp)** (75 stars) — 12 tools, staged table building, Claude-optimized prompts, 9 field types. TypeScript

## Smartsheet Servers

### Smartsheet Hosted MCP — Official (NEW)

**Generally available:** March 2026, per [Smartsheet's own announcement](https://www.smartsheet.com/content-center/smartsheet-mcp-server-now-generally-available) (published March 24, 2026) | [developers.smartsheet.com](https://developers.smartsheet.com/ai-mcp/smartsheet/mcp-server)

Smartsheet deprecated its open-source GitHub repo (smartsheet-platform/smar-mcp, deprecated April 2026) in favor of a hosted MCP endpoint integrated directly with the Smartsheet platform. This is now a direct Claude MCP integration.

**What makes it stand out:**
- **Hosted endpoint** — no self-hosting required, connects directly to Smartsheet's infrastructure
- **Official and supported** — first-party Smartsheet integration
- **Replaces smar-mcp** — the GitHub repo now shows a deprecation notice directing users here

**Limitations:**
- **Hosted only** — no self-hosted or open-source option anymore
- Documentation on exact tool count and capabilities still emerging

**Best for:** All Smartsheet users. This is now the officially recommended path.

### smartsheet-platform/smar-mcp — ⚠️ DEPRECATED

**Stars:** 26 | **Language:** TypeScript | **Status:** Deprecated (April 2026)

The original open-source Smartsheet MCP server has been deprecated. The repository directs users to the hosted MCP at developers.smartsheet.com. Included here for reference — if you're using this, migrate to the hosted version.

### terilios/smartsheet-server — More Tools

**Stars:** 12 | **Language:** TypeScript + Python | **License:** MIT

Community server with more tools than the official one.

**What makes it stand out:**
- **34 tools** — more than double the official server
- **Healthcare analytics** — clinical notes, patient feedback analysis (domain-specific)
- **Regex search** — search within sheet data using regular expressions
- **Cross-sheet references** — work across multiple sheets
- **Attachment and discussion management**

**Best for:** Power users who need features the official server doesn't cover, particularly in healthcare.

## LibreOffice Calc Servers

The open-source spreadsheet space has matured, with patrup/mcp-libre emerging as a surprisingly capable option.

### patrup/mcp-libre — The New Leader

**Stars:** 94 | **Language:** Python | **Requirements:** LibreOffice 24.2+, Python 3.12+

An embedded MCP server that runs inside LibreOffice as a native extension. Uses the UNO API directly for 10x faster performance versus external servers.

**What makes it stand out:**
- **50+ format support** — PDF, DOCX, HTML, and more via LibreOffice's converter
- **Native extension** — runs inside LibreOffice for real-time editing of open documents
- **10x faster** — direct UNO API access avoids IPC overhead of external servers
- **Live viewing** — see changes reflected immediately in open documents

**Limitations:** Requires LibreOffice 24.2+ and Python 3.12+. UV package manager needed.

**Best for:** LibreOffice users who want fast, native document manipulation with broad format support.

### WaterPistolAI/libreoffice-mcp

**Stars:** 23 | **Language:** Python

Covers Writer, Calc, Impress, and Draw. Calc tools include get_cell_value, set_cell_value, create_new_sheet, set_cell_formula, create_chart, conditional formatting, and range grouping. Uses OooDev library for improved abstraction.

**Limitations:** Work in progress. Socket-based transport (port 2083), not standard MCP transports.

## Decision Flowchart

**Do you work with Excel files?**

→ **Cross-platform, no Excel needed** → haris-musa/excel-mcp-server (Python, 25 tools)

→ **Go binary, no runtime** → negokaz/excel-mcp-server (Go, 7 tools, pagination)

→ **Windows with Power Query / DAX / VBA** → sbroenne/mcp-server-excel (C#, 210+ operations)

→ **Cloud / Microsoft 365** → Arcade Office 365 MCP (built on Microsoft Graph API, March 2026)

→ **Analysis of CSV/Excel/JSON** → yzfly/mcp-excel-server (multi-format)

**Do you work with Google Sheets?**

→ **Need other Google services too** → taylorwilsdon/google_workspace_mcp (10+ services)

→ **Sheets only, maximum features** → xing5/mcp-google-sheets (19 tools, tool filtering)

→ **Sheets + Docs + Drive** → a-bonus/google-docs-mcp (11 Sheets tools)

→ **Sheets with charts and formatting** → freema/mcp-gsheets (25+ tools)

**Do you work with Airtable?**

→ **Official, permission-respecting** → Airtable Official MCP (mcp.airtable.com)

→ **Community, well-tested** → domdomegg/airtable-mcp-server (18+ tools)

→ **Enterprise with PII masking** → rashidazarang/airtable-mcp (42 tools, governance)

**Do you work with Smartsheet?**

→ **Official (recommended)** → Smartsheet hosted MCP (developers.smartsheet.com, March 2026)

→ **More tools, healthcare focus** → terilios/smartsheet-server (34 tools)

## Four Trends Shaping This Space

### 1. File-based vs. live-process vs. cloud — three fundamentally different approaches

The Excel space has split into three camps. **File-based servers** (haris-musa, negokaz) use libraries like openpyxl to manipulate .xlsx files directly — cross-platform, no Excel needed, but they can't evaluate formulas or interact with running instances. **Live-process servers** (sbroenne for Windows, sbraind for macOS) control actual Excel applications via COM or AppleScript — giving access to Power Query, DAX, VBA, and real-time recalculation, but locking you to a specific OS. **Cloud servers** (Arcade Office 365) connect to Excel Online via Microsoft Graph API — collaborative and always-on, but require internet and a Microsoft 365 subscription. Each approach serves a different use case.

### 2. Vendors are moving from open-source to hosted MCP

The trend is clear: vendors prefer hosted MCP endpoints over open-source repos. Smartsheet deprecated its GitHub repo (smar-mcp) in March 2026, directing users to developers.smartsheet.com. Airtable's official MCP is hosted rather than a standalone repo. Arcade's Office 365 integration is a platform service, not an installable. The advantage for vendors: control over versioning, authentication, and rate limiting. The downside for users: vendor lock-in and no self-hosting option.

### 3. Google is conspicuously absent from Sheets MCP

Google Cloud [announced official MCP support](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services) on December 10, 2025 — initially for Maps, BigQuery, Compute Engine, and Kubernetes Engine, growing to 50+ managed servers by mid-2026. Google Sheets and Workspace were never part of that rollout. Meanwhile, taylorwilsdon's community server has reached nearly 3,000 stars filling that gap. Microsoft at least has indirect coverage through Arcade's third-party Office 365 integration. Google Sheets remains the biggest "official server missing" gap in the spreadsheet MCP space.

### 4. Tool count inflation and context window tradeoffs

Spreadsheet servers are competing on tool count: rashidazarang's Airtable offers 42 tools, freema's Google Sheets offers 44, sbroenne's Excel offers 210+ operations. But more tools mean more context window usage — each tool description consumes tokens. xing5/mcp-google-sheets addressed this with tool filtering, saving ~13K tokens by disabling unused tools. Expect more servers to adopt this pattern as context window efficiency becomes a differentiator.

## What's Missing

- **No official Google Sheets MCP server** — Google announced MCP support in December 2025 (BigQuery, Maps, and infrastructure services), not Sheets or Workspace. Community servers fill the gap but could break on API changes
- **No first-party Microsoft Excel MCP server** — Arcade's Office 365 integration provides coverage as a third party built on Microsoft Graph API, but Microsoft hasn't published an official MCP server under its own org, and there's no confirmed Microsoft partnership. Community options remain excellent
- **No Apple Numbers MCP server** — Apple's spreadsheet is completely absent from the MCP ecosystem
- **Formula evaluation** — file-based Excel servers can write formulas but can't compute results. You get `=SUM(A1:A10)` as text, not the number. Only live-process servers (Windows/macOS) or cloud servers (Arcade) can evaluate
- **Large file handling** — most servers lack strategies for spreadsheets with 100K+ rows. Only negokaz provides pagination (4,000-cell batches)
- **No universal spreadsheet server** — no single server handles Excel + Google Sheets + Airtable. You need separate servers for each platform
- **CSV is underserved** — no well-established, high-star CSV-dedicated MCP server exists. CSV handling is typically a secondary feature of Excel servers
- **No collaborative editing awareness** — no MCP server handles real-time multi-user editing detection or conflict resolution
- **Self-hosted options shrinking** — as vendors move to hosted MCP endpoints (Smartsheet, Airtable), self-hosted and offline options are becoming rarer

