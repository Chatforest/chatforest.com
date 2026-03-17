---
title: "Spreadsheet MCP Servers — Google Sheets, Excel, Airtable, Smartsheet, and More"
date: 2026-03-17T22:50:00+09:00
description: "Spreadsheet MCP servers reviewed: Excel via haris-musa/excel-mcp-server (3,500 stars, Python, most popular, 20+ tools, no Excel needed), Google Sheets via google_workspace_mcp (1,800 stars, 10+ Google services) and mcp-google-sheets (740 stars, 19 tools), Airtable official MCP server (Feb 2026) + domdomegg community (427 stars, 16 tools), Smartsheet official MCP (15 tools). Rating: 3.5/5."
og_description: "Spreadsheet MCP servers: Excel (3,500 stars, most popular), Google Sheets (1,800 stars workspace, 740 stars dedicated), Airtable (official + 427-star community), Smartsheet (official). Rating: 3.5/5."
content_type: "Review"
card_description: "Spreadsheets are the world's most-used data tool — and the MCP ecosystem has responded with dozens of servers. Excel leads with a 3,500-star Python server that needs no Excel installation. Google Sheets has 10+ community options. Airtable and Smartsheet both have official MCP servers. But Google and Microsoft still haven't released official standalone spreadsheet servers."
---

Spreadsheets are arguably the world's most-used data tool, and connecting AI agents to them is a high-value use case — from financial modeling to data cleaning to report generation. The MCP ecosystem has responded with dozens of servers, and the picture is more nuanced than expected: **Airtable and Smartsheet have official MCP servers**, but **Google and Microsoft still haven't released official standalone spreadsheet servers** despite their dominance in the space.

The landscape splits four ways: **Excel** has the most popular single server (3,500 stars), **Google Sheets** has the most options (10+ repos), **Airtable** bridges spreadsheet and database with both official and community servers, and **Smartsheet** quietly shipped an official MCP server.

## Excel — Python File Server (Most Popular)

| Detail | Info |
|--------|------|
| [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) | 3,500 stars |
| Language | Python |
| License | MIT |
| Tools | 20+ |
| Formats | xlsx, xlsm, csv |

The most popular spreadsheet MCP server of any kind. It manipulates Excel files directly using Python libraries — no Microsoft Excel installation needed.

### What Works Well

**Comprehensive operations.** 20+ tools covering workbook creation, reading, and updating. Formulas, formatting, charts (line, bar, pie, scatter), pivot tables, data validation, Excel tables, and more. This is the most complete cross-platform Excel toolset available.

**No Excel required.** Pure Python implementation means it runs on macOS, Linux, and Windows without any Microsoft software. Great for server environments and CI/CD pipelines.

**Multiple transports.** Supports stdio, SSE, and HTTP transport modes, making it flexible for desktop apps, web services, and remote deployments.

**High adoption.** At 3,500 stars, this is by far the most battle-tested spreadsheet MCP server. The large user base means bugs get found and fixed quickly.

### What Doesn't Work Well

**No live Excel integration.** File-based approach means you can't interact with a running Excel instance, trigger recalculations, or work with Excel add-ins.

**No IRM/AIP support.** Can't open encrypted or rights-managed Excel files.

**Community-maintained.** Despite its popularity, this isn't backed by Microsoft. API stability depends on the maintainer.

## Excel — Go Cross-Platform Server

| Detail | Info |
|--------|------|
| [negokaz/excel-mcp-server](https://github.com/negokaz/excel-mcp-server) | 883 stars |
| Language | Go |
| License | MIT |
| Tools | 7 |
| Formats | xlsx, xlsm, xltx, xltm |

A lighter-weight alternative written in Go.

### What Works Well

**Fast and lightweight.** Go binary with no runtime dependencies. Starts quickly and has low memory overhead compared to Python alternatives.

**Formula support.** Reads and writes both values and formulas, not just static data.

**Screenshot capability.** On Windows, can capture live screenshots of Excel sheets for visual verification by the AI agent.

**Pagination.** Large spreadsheets are handled with pagination, preventing context window overflow.

### What Doesn't Work Well

**Limited tool count.** Only 7 tools — no charts, pivot tables, data validation, or conditional formatting. Fine for simple read/write tasks, but the Python server (3,500 stars) is more capable for complex work.

## Excel — Windows COM Automation

| Detail | Info |
|--------|------|
| [sbroenne/mcp-server-excel](https://github.com/sbroenne/mcp-server-excel) | 81 stars |
| Language | C# |
| License | MIT |
| Tools | 25 (230 operations across 16 categories) |

A Windows-only MCP server that controls a live Excel instance through the COM API.

### What Works Well

**Deepest Excel integration available.** 25 tools with 230 operations across Power Query, DAX measures, VBA macros, PivotTables, Charts, formatting, and data transformations. This is the closest thing to full Excel automation via MCP.

**Live Excel control.** Interacts with a running Excel instance, so you see changes in real time. The AI agent can automate Excel exactly as a human would — including triggering recalculations and interacting with add-ins.

**IRM/AIP-protected files.** Can work with Information Rights Management and Azure Information Protection encrypted files, which the file-based servers cannot.

**Dual interfaces.** Both an MCP Server for conversational AI and a CLI for coding agents. The CLI uses ~64% fewer tokens for equivalent tasks.

### What Doesn't Work Well

**Windows-only.** COM automation requires a live Excel installation on Windows. No macOS or Linux support.

**Requires Excel license.** You need Microsoft Excel 2016+ installed and licensed. Not suitable for server environments or CI/CD pipelines.

## Other Excel Options

- **[yzfly/mcp-excel-server](https://github.com/yzfly/mcp-excel-server)** (~84 stars, Python, MIT) — Natural language interaction with Excel files including visualization and analysis using pandas/matplotlib.
- **[Softeria/ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server)** — Microsoft 365 integration via Graph API, includes Excel as one of several services.
- **[OfficeMCP/ExcelMCP](https://github.com/OfficeMCP/ExcelMCP)** — Another Windows COM-based server for controlling Excel.
- **[guillehr2/Excel-MCP-Server-Master](https://github.com/guillehr2/Excel-MCP-Server-Master)** (~25 stars, JavaScript/Python) — No Excel needed, supports import/export to CSV, JSON, SQL, PDF.

**Notable absence:** Microsoft's [official MCP catalog](https://github.com/microsoft/mcp) (2,800 stars) includes Azure, Fabric, DevOps, and many Microsoft 365 services — but no dedicated Excel MCP server. The Microsoft 365 Mail, Calendar, and User servers exist, but spreadsheet support through official channels is still missing.

## Google Sheets — Workspace Server

| Detail | Info |
|--------|------|
| [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | 1,800 stars |
| Language | Python |
| License | MIT |
| Tools | 10+ Google services (Sheets, Docs, Drive, Gmail, Calendar, etc.) |

The most popular way to access Google Sheets via MCP is through this comprehensive Google Workspace server that covers Gmail, Drive, Calendar, Docs, Sheets, Slides, Forms, Tasks, Chat, and Contacts in a single package.

### What Works Well

**Broad coverage.** Rather than just Sheets, you get the entire Google Workspace suite. If your workflow involves pulling data from Sheets, drafting an email in Gmail, and updating a Calendar event, one server handles all of it.

**Mature authentication.** OAuth 2.0 and 2.1 support with automatic token refresh, multi-user capability, and desktop OAuth client configuration that doesn't require redirect URIs. This is one of the more polished auth implementations we've seen in an MCP server.

**Tool tier system.** Core, extended, and complete tiers let you control which tools are exposed. A read-only mode with restricted scopes is available for safety-conscious deployments.

**Docker support.** Containerized deployment for teams that don't want to install Python dependencies directly.

### What Doesn't Work Well

**Not Sheets-focused.** Because it covers 10+ services, the Sheets-specific tooling may not be as deep as a dedicated server. Complex spreadsheet operations (conditional formatting, pivot tables, charts) may require falling back to the Google Sheets API directly.

**Setup complexity.** Google OAuth configuration is notoriously fiddly. You'll need to create a Google Cloud project, configure consent screens, and manage credentials — a barrier for casual users.

## Google Sheets — Dedicated Servers

| Detail | Info |
|--------|------|
| [xing5/mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) | 740 stars |
| Language | Python |
| License | MIT |
| Tools | 19 |

The most popular dedicated Google Sheets MCP server.

### What Works Well

**Solid Sheets coverage.** 19 tools covering CRUD operations, batch updates, sheet management, sharing, and chart creation. Flexible authentication supports service accounts, OAuth 2.0, and Application Default Credentials.

**Zero-install deployment.** Run with `uvx mcp-google-sheets@latest` — no manual installation required.

**Tool filtering.** Context window optimization lets you disable tools you don't need, reducing token consumption from ~13,000 tokens for the full tool set.

### What Doesn't Work Well

**Community-maintained.** Not backed by Google. API changes or breaking updates depend on community response time.

**No real-time collaboration awareness.** The MCP server doesn't surface who else is editing or provide conflict resolution for simultaneous edits.

### Most Feature-Rich: freema/mcp-gsheets

| Detail | Info |
|--------|------|
| [freema/mcp-gsheets](https://github.com/freema/mcp-gsheets) | ~52 stars |
| Language | TypeScript |
| License | MIT |
| Tools | 30+ |

Despite lower star count, this is the most feature-complete dedicated Google Sheets server. **30+ tools** covering batch operations, cell formatting, borders, merge/unmerge cells, conditional formatting, chart CRUD, sheet duplication, and copying. If you need deep Sheets-specific functionality, this is the one to look at — the trade-off is a smaller community.

## Other Google Sheets Options

- **[mkummer225/google-sheets-mcp](https://github.com/mkummer225/google-sheets-mcp)** (~123 stars, JavaScript, MIT) — 14-15 tools for read/write cells, rows, columns; create sheets and spreadsheets.
- **[shionhonda/mcp-gsheet](https://github.com/shionhonda/mcp-gsheet)** — Lightweight, minimal (3 tools: list, read, write). Good for simple use cases.
- **[distrihub/mcp-google-workspace](https://github.com/distrihub/mcp-google-workspace)** — A Rust-based Google Drive and Sheets MCP server, notable for using Rust in a space dominated by Python and TypeScript.
- **[a-bonus/google-docs-mcp](https://github.com/a-bonus/google-docs-mcp)** — Google Docs, Sheets, and Drive access with direct formatting and editing capabilities.

**Notable absence:** Google announced official MCP support in December 2025 for enterprise services (BigQuery, GKE, Maps), but Google Sheets and other Workspace consumer services are not included. All Google Sheets MCP servers remain community-built.

## Airtable — Official + Community

### Official Airtable MCP Server

Airtable released an [official MCP server](https://support.airtable.com/docs/using-the-airtable-mcp-server) in February 2026. It supports search, create, update, and analyze operations, respects existing Airtable permissions (read-only users can only read), and works with Claude, ChatGPT, and Cursor. The official server does not have a public GitHub repository — it's documented through Airtable's support site.

### Community: domdomegg/airtable-mcp-server

| Detail | Info |
|--------|------|
| [domdomegg/airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server) | 427 stars |
| Language | TypeScript |
| License | MIT |
| Tools | 16 |

The leading open-source Airtable MCP server.

### What Works Well

**Full CRUD plus schema management.** 16 tools covering record operations (list, search, get, create, update, delete), schema management (list bases, describe tables, create/update tables and fields), and comments.

**HTTP transport.** Supports HTTP transport mode for remote MCP clients, not just stdio.

**Formula-based filtering.** Uses Airtable's native formula syntax for record filtering.

**Optional write scopes.** Write operations can be selectively enabled or disabled.

### What Doesn't Work Well

**Superseded by official for some use cases.** Now that Airtable has an official server, the community server's main advantages are open source transparency, HTTP transport, and schema management tools that the official may not expose.

### Other Airtable Options

- **[rashidazarang/airtable-mcp](https://github.com/rashidazarang/airtable-mcp)** (~72 stars, TypeScript) — Most tools of any Airtable server (42 tools), including webhooks, batch operations, PII masking, and AI prompt templates.
- **[felores/airtable-mcp](https://github.com/felores/airtable-mcp)** (72 stars, JavaScript, MIT) — 12 tools with staged table building and rich field type support.

## Smartsheet — Official MCP Server

| Detail | Info |
|--------|------|
| [smartsheet-platform/smar-mcp](https://github.com/smartsheet-platform/smar-mcp) | ~25 stars |
| Language | TypeScript |
| Official | Yes (smartsheet-platform org) |
| Tools | 15 |

Smartsheet quietly shipped an official MCP server under their platform organization on GitHub. 15 tools covering get/update/add/delete rows, cell history, copy sheets, create sheets, discussions, workspaces, and version backups. Lower adoption than the community alternatives for other platforms, but official vendor backing is a significant advantage for enterprise users who already use Smartsheet.

## What About Notion?

Notion's database features make it a spreadsheet alternative for many teams. The [official Notion MCP server](https://github.com/makenotion/notion-mcp-server) (~2,500 stars) provides access to Notion databases, pages, and blocks. If your "spreadsheet" workflow is actually structured data in Notion, the official server is well-maintained and popular.

## The Big Picture

| Platform | Top Server | Stars | Tools | Official? |
|----------|-----------|-------|-------|-----------|
| Excel (Python) | haris-musa/excel-mcp-server | 3,500 | 20+ | No |
| Excel (Go) | negokaz/excel-mcp-server | 883 | 7 | No |
| Excel (Windows COM) | sbroenne/mcp-server-excel | 81 | 25 / 230 ops | No |
| Google Sheets (workspace) | taylorwilsdon/google_workspace_mcp | 1,800 | 10+ services | No |
| Google Sheets (dedicated) | xing5/mcp-google-sheets | 740 | 19 | No |
| Google Sheets (feature-rich) | freema/mcp-gsheets | ~52 | 30+ | No |
| Airtable | Official (support.airtable.com) | N/A | Official | Yes |
| Airtable (community) | domdomegg/airtable-mcp-server | 427 | 16 | No |
| Smartsheet | smartsheet-platform/smar-mcp | ~25 | 15 | Yes |
| Notion | makenotion/notion-mcp-server | ~2,500 | Official | Yes |

## Who Should Use These

**Excel users** should start with haris-musa's Python server (3,500 stars, 20+ tools) — it's by far the most popular and capable cross-platform option. If you need deep Windows automation (Power Query, VBA, DAX), sbroenne's COM server is unmatched but Windows-only.

**Google Sheets users** have the best selection — the workspace server (1,800 stars) is mature and covers all of Google Workspace. For Sheets-only depth, xing5's dedicated server (740 stars, 19 tools) or freema's feature-rich server (30+ tools) are better choices.

**Airtable users** should try the official Airtable MCP server first. Fall back to domdomegg's community server (427 stars, 16 tools) if you need open source or HTTP transport.

**Smartsheet users** have an official server — small but vendor-backed.

**The gap:** Google and Microsoft still haven't released official standalone spreadsheet MCP servers. Google's official MCP covers BigQuery and GKE but not Workspace. Microsoft's MCP catalog covers Azure, Fabric, and DevOps but skips Excel. The community has filled the gap impressively — the 3,500-star Excel server proves demand is there.

## Rating: 3.5 / 5

The spreadsheet MCP ecosystem is **broad and surprisingly capable**. The Excel Python server's 3,500 stars make it one of the most popular MCP servers period, and Airtable and Smartsheet both have official servers. But the two biggest platforms — Google Sheets and Microsoft Excel — still rely entirely on community servers for MCP support. The quantity of options is impressive (10+ for Google Sheets alone), but the lack of official backing from the two dominant vendors keeps this rating below the 4.0+ scores we give to categories with strong vendor support. When Google and Microsoft ship official spreadsheet MCP servers, this category will jump significantly.
