# Spreadsheet MCP Servers — Google Sheets, Excel, Airtable, Smartsheet, and More

> Spreadsheet MCP servers reviewed: Excel via haris-musa/excel-mcp-server (3,800 stars, Python, most popular, 20+ tools, no Excel needed), Google Sheets via google_workspace_mcp (2,200 stars), Airtable official, Smartsheet migrated to hosted official. Google official Workspace MCP ships but SKIPS Sheets.


Spreadsheets are arguably the world's most-used data tool, and connecting AI agents to them is a high-value use case — from financial modeling to data cleaning to report generation. The MCP ecosystem has responded with dozens of servers, and the picture shifted significantly in April 2026: **Google shipped official Workspace MCP servers at [Cloud Next 2026](https://workspace.google.com/blog/product-announcements/10-more-announcements-workspace-at-next-2026) — but deliberately skipped Google Sheets**, covering only Gmail, Drive, Calendar, People, and Chat. Meanwhile, **Smartsheet deprecated its GitHub repo** in favor of a new hosted official server, and the **sbroenne Windows COM Excel server surged 77% in stars** with 113 releases. Part of our **[Business & Productivity MCP category](/categories/business-productivity/)**.

The landscape splits four ways: **Excel** has the most popular single server (3,800 stars), **Google Sheets** has the most options (10+ repos but still no official), **Airtable** bridges spreadsheet and database with both official and community servers, and **Smartsheet** migrated to a [hosted official MCP server](https://developers.smartsheet.com/ai-mcp/smartsheet/mcp-server). A new entrant — **[Aanerud/MCP-Microsoft-Office](https://github.com/Aanerud/MCP-Microsoft-Office)** (46 stars) — brings 30 Excel-specific tools via Microsoft Graph API, the deepest cloud Excel integration available.

## Excel — Python File Server (Most Popular)

| Detail | Info |
|--------|------|
| [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) | 3,800 stars |
| Language | Python |
| License | MIT |
| Tools | 20+ |
| Formats | xlsx, xlsm, csv |

The most popular spreadsheet MCP server of any kind. It manipulates Excel files directly using Python libraries — no Microsoft Excel installation needed.

### What Works Well

**Comprehensive operations.** 20+ tools covering workbook creation, reading, and updating. Formulas, formatting, charts (line, bar, pie, scatter), pivot tables, data validation, Excel tables, and more. This is the most complete cross-platform Excel toolset available.

**No Excel required.** Pure Python implementation means it runs on macOS, Linux, and Windows without any Microsoft software. Great for server environments and CI/CD pipelines.

**Multiple transports.** Supports stdio and streamable HTTP transport modes, making it flexible for desktop apps, web services, and remote deployments. (SSE transport deprecated as of v0.1.8, April 2026.)

**High adoption.** At 3,800 stars, this is by far the most battle-tested spreadsheet MCP server. The large user base means bugs get found and fixed quickly.

### What Doesn't Work Well

**No live Excel integration.** File-based approach means you can't interact with a running Excel instance, trigger recalculations, or work with Excel add-ins.

**No IRM/AIP support.** Can't open encrypted or rights-managed Excel files.

**Community-maintained.** Despite its popularity, this isn't backed by Microsoft. API stability depends on the maintainer.

## Excel — Go Cross-Platform Server

| Detail | Info |
|--------|------|
| [negokaz/excel-mcp-server](https://github.com/negokaz/excel-mcp-server) | 938 stars |
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

**Limited tool count.** Only 7 tools — no charts, pivot tables, data validation, or conditional formatting. Fine for simple read/write tasks, but the Python server (3,800 stars) is more capable for complex work.

## Excel — Windows COM Automation

| Detail | Info |
|--------|------|
| [sbroenne/mcp-server-excel](https://github.com/sbroenne/mcp-server-excel) | 143 stars |
| Language | C# |
| License | MIT |
| Tools | 25 (230 operations across 16 categories) |
| Releases | 113 (v1.8.54, April 28, 2026) |

A Windows-only MCP server that controls a live Excel instance through the COM API. **The most actively developed spreadsheet MCP server** — 383 commits, 113 releases, and stars nearly doubled from 81 to 143 (+77%) since our last review.

### What Works Well

**Deepest Excel integration available.** 25 tools with 230 operations across Power Query, DAX measures, VBA macros, PivotTables, Charts, formatting, and data transformations. This is the closest thing to full Excel automation via MCP.

**Live Excel control.** Interacts with a running Excel instance, so you see changes in real time. The AI agent can automate Excel exactly as a human would — including triggering recalculations and interacting with add-ins.

**IRM/AIP-protected files.** Can work with Information Rights Management and Azure Information Protection encrypted files, which the file-based servers cannot.

**Dual interfaces.** Both an MCP Server for conversational AI and a CLI for coding agents. The CLI uses ~64% fewer tokens for equivalent tasks.

### What Doesn't Work Well

**Windows-only.** COM automation requires a live Excel installation on Windows. No macOS or Linux support.

**Requires Excel license.** You need Microsoft Excel 2016+ installed and licensed. Not suitable for server environments or CI/CD pipelines.

## Excel via Microsoft 365 / Graph API (NEW)

Two new options bring cloud-hosted Excel (OneDrive/SharePoint) to MCP without requiring a local Excel installation:

- **[Aanerud/MCP-Microsoft-Office](https://github.com/Aanerud/MCP-Microsoft-Office)** (46 stars, TypeScript) — **30 Excel-specific tools** out of 117 total across 12 M365 modules. Session management (persistent or temporary), worksheet CRUD, range read/write with formulas, table management (create, sort, filter, add/delete rows/columns), call 300+ Excel functions (SUM, VLOOKUP, PMT, etc.), formatting (font, fill, borders, number formats), and formula recalculation. Works directly with OneDrive/SharePoint files via Graph API — no downloads needed. AES-256 encrypted token storage, PKCE auth.
- **[Arcade.dev Office 365 MCP servers](https://www.arcade.dev/blog/microsoft-office-365-mcp-servers-launch)** (March 2026) — Third-party production-grade Excel server with workbook creation, paginated reads for large sheets, cell/range updates, formula support, worksheet management, and etag-based conflict detection for concurrent edits. Part of a 5-server suite (Word, Excel, PowerPoint, OneDrive, SharePoint).

## Other Excel Options

- **[yzfly/mcp-excel-server](https://github.com/yzfly/mcp-excel-server)** (~84 stars, Python, MIT) — Natural language interaction with Excel files including visualization and analysis using pandas/matplotlib.
- **[Softeria/ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server)** — Microsoft 365 integration via Graph API, includes Excel as one of several services.
- **[OfficeMCP/ExcelMCP](https://github.com/OfficeMCP/ExcelMCP)** — Another Windows COM-based server for controlling Excel.
- **[guillehr2/Excel-MCP-Server-Master](https://github.com/guillehr2/Excel-MCP-Server-Master)** (~25 stars, JavaScript/Python) — No Excel needed, supports import/export to CSV, JSON, SQL, PDF.

**Notable absence:** Microsoft's [official MCP catalog](https://github.com/microsoft/mcp) still includes Azure, Fabric, DevOps, and many Microsoft 365 services — but no dedicated Excel MCP server. The community has stepped up with Graph API options (Aanerud, Arcade.dev), but official Microsoft Excel MCP support remains missing.

## Google Sheets — Workspace Server

| Detail | Info |
|--------|------|
| [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | 2,200 stars |
| Language | Python |
| License | MIT |
| Tools | 12 Google services (Sheets, Docs, Drive, Gmail, Calendar, Slides, Forms, Chat, Apps Script, Tasks, Contacts, Custom Search) |
| Commits | 2,054 |

The most popular way to access Google Sheets via MCP is through this comprehensive Google Workspace server. Now covering 12 services with .dxt one-click installation for Claude Desktop.

### What Works Well

**Broad coverage.** Rather than just Sheets, you get 12 Google Workspace services. If your workflow involves pulling data from Sheets, drafting an email in Gmail, and updating a Calendar event, one server handles all of it.

**Mature authentication.** OAuth 2.0 and 2.1 support with automatic token refresh, multi-user capability, and desktop OAuth client configuration that doesn't require redirect URIs. This is one of the more polished auth implementations we've seen in an MCP server.

**Tool tier system.** Core, extended, and complete tiers let you control which tools are exposed. A read-only mode with restricted scopes is available for safety-conscious deployments.

**Docker support.** Containerized deployment for teams that don't want to install Python dependencies directly.

### What Doesn't Work Well

**Not Sheets-focused.** Because it covers 12 services, the Sheets-specific tooling may not be as deep as a dedicated server. Complex spreadsheet operations (conditional formatting, pivot tables, charts) may require falling back to the Google Sheets API directly.

**Setup complexity.** Google OAuth configuration is notoriously fiddly. You'll need to create a Google Cloud project, configure consent screens, and manage credentials — a barrier for casual users.

## Google Sheets — Dedicated Servers

| Detail | Info |
|--------|------|
| [xing5/mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) | 829 stars |
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
| [freema/mcp-gsheets](https://github.com/freema/mcp-gsheets) | 61 stars |
| Language | TypeScript |
| License | MIT |
| Tools | 40+ |

Despite lower star count, this is the most feature-complete dedicated Google Sheets server. **40+ tools** across reading (4), writing (8+), sheet management (6), formatting (6), charts (3), and snapshot/read operations (7+) — covering batch operations, cell formatting, borders, merge/unmerge cells, conditional formatting, chart CRUD, sheet duplication, date/link insertion, and copying. If you need deep Sheets-specific functionality, this is the one to look at — the trade-off is a smaller community.

## Other Google Sheets Options

- **[mkummer225/google-sheets-mcp](https://github.com/mkummer225/google-sheets-mcp)** (~123 stars, JavaScript, MIT) — 14-15 tools for read/write cells, rows, columns; create sheets and spreadsheets.
- **[shionhonda/mcp-gsheet](https://github.com/shionhonda/mcp-gsheet)** — Lightweight, minimal (3 tools: list, read, write). Good for simple use cases.
- **[distrihub/mcp-google-workspace](https://github.com/distrihub/mcp-google-workspace)** — A Rust-based Google Drive and Sheets MCP server, notable for using Rust in a space dominated by Python and TypeScript.
- **[a-bonus/google-docs-mcp](https://github.com/a-bonus/google-docs-mcp)** — Google Docs, Sheets, and Drive access with direct formatting and editing capabilities.

**Google official Workspace MCP — Sheets skipped.** At [Cloud Next 2026](https://developers.google.com/workspace/guides/configure-mcp-servers) (April 2026), Google launched official Workspace MCP servers in Developer Preview covering Gmail (10 tools), Drive (7 tools), Calendar (8 tools), People (3 tools), and Chat (2 tools) — 30 tools total. **Google Sheets was deliberately not included** in this initial preview. All Google Sheets MCP servers remain community-built, making this the most prominent gap in Google's official MCP coverage.

## Airtable — Official + Community

### Official Airtable MCP Server

Airtable released an [official MCP server](https://support.airtable.com/docs/using-the-airtable-mcp-server) in February 2026. It supports search, create, update, and analyze operations, respects existing Airtable permissions (read-only users can only read), and works with Claude, ChatGPT, and Cursor. The official server does not have a public GitHub repository — it's documented through Airtable's support site.

### Community: domdomegg/airtable-mcp-server

| Detail | Info |
|--------|------|
| [domdomegg/airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server) | 440 stars |
| Language | TypeScript |
| License | MIT |
| Tools | 17 |
| Version | v1.13.0 (March 2026) |

The leading open-source Airtable MCP server.

### What Works Well

**Full CRUD plus schema management.** 17 tools covering record operations (list, search, get, create, update, delete), schema management (list bases, describe tables, create/update tables and fields), and comments.

**HTTP transport.** Supports HTTP transport mode for remote MCP clients, not just stdio.

**Formula-based filtering.** Uses Airtable's native formula syntax for record filtering.

**Optional write scopes.** Write operations can be selectively enabled or disabled.

### What Doesn't Work Well

**Superseded by official for some use cases.** Now that Airtable has an official server, the community server's main advantages are open source transparency, HTTP transport, and schema management tools that the official may not expose.

### Other Airtable Options

- **[rashidazarang/airtable-mcp](https://github.com/rashidazarang/airtable-mcp)** (78 stars, TypeScript) — Most tools of any Airtable server (42 tools), including webhooks, batch operations, PII masking, and AI prompt templates.
- **[felores/airtable-mcp](https://github.com/felores/airtable-mcp)** (72 stars, JavaScript, MIT) — 12 tools with staged table building and rich field type support.

## Smartsheet — Official MCP Server (Migrated)

| Detail | Info |
|--------|------|
| [Official hosted server](https://developers.smartsheet.com/ai-mcp/smartsheet/mcp-server) | Hosted by Smartsheet |
| [smartsheet-platform/smar-mcp](https://github.com/smartsheet-platform/smar-mcp) | DEPRECATED (26 stars) |
| Requires | Business, Enterprise, or Advanced Work Management plan |

**Smartsheet deprecated its GitHub repo** and migrated to a new [hosted official MCP server](https://developers.smartsheet.com/ai-mcp/smartsheet/mcp-server). The new server adds attachment management (add, access, delete attachments on sheets, rows, and discussions) alongside the existing tools for sheet querying, row CRUD, cell history, discussions, and workspaces. Works with Claude, Cursor, and custom MCP clients. The trade-off: requires a paid Smartsheet plan (Business or higher), whereas the old GitHub repo was open source.

## What About Notion?

Notion's database features make it a spreadsheet alternative for many teams. The [official Notion MCP server](https://github.com/makenotion/notion-mcp-server) (4,300 stars) provides access to Notion databases, pages, and blocks. If your "spreadsheet" workflow is actually structured data in Notion, the official server is well-maintained and one of the most popular MCP servers of any kind.

## The Big Picture

| Platform | Top Server | Stars | Tools | Official? |
|----------|-----------|-------|-------|-----------|
| Excel (Python) | haris-musa/excel-mcp-server | 3,800 | 20+ | No |
| Excel (Go) | negokaz/excel-mcp-server | 938 | 7 | No |
| Excel (Windows COM) | sbroenne/mcp-server-excel | 143 | 25 / 230 ops | No |
| Excel (M365 Graph) | Aanerud/MCP-Microsoft-Office | 46 | 30 Excel tools | No |
| Google Sheets (workspace) | taylorwilsdon/google_workspace_mcp | 2,200 | 12 services | No |
| Google Sheets (dedicated) | xing5/mcp-google-sheets | 829 | 19 | No |
| Google Sheets (feature-rich) | freema/mcp-gsheets | 61 | 40+ | No |
| Google Workspace (official) | developers.google.com | N/A | 30 (no Sheets) | Yes |
| Airtable | Official (support.airtable.com) | N/A | Official | Yes |
| Airtable (community) | domdomegg/airtable-mcp-server | 440 | 17 | No |
| Smartsheet | developers.smartsheet.com (hosted) | N/A | Official | Yes |
| Notion | makenotion/notion-mcp-server | 4,300 | Official | Yes |

## Who Should Use These

**Excel users** should start with haris-musa's Python server (3,800 stars, 20+ tools) — it's by far the most popular and capable cross-platform option. If you need deep Windows automation (Power Query, VBA, DAX), sbroenne's COM server (143 stars, 113 releases) is unmatched but Windows-only. For cloud Excel on OneDrive/SharePoint, Aanerud's MCP-Microsoft-Office (30 Excel tools via Graph API) is the best option.

**Google Sheets users** have the best selection — the workspace server (2,200 stars) is mature and covers 12 Google services with one-click install. For Sheets-only depth, xing5's dedicated server (829 stars, 19 tools) or freema's feature-rich server (40+ tools) are better choices. Note that Google's new official Workspace MCP (April 2026) covers Gmail, Drive, Calendar, People, and Chat — but not Sheets.

**Airtable users** should try the official Airtable MCP server first. Fall back to domdomegg's community server (440 stars, 17 tools) if you need open source or HTTP transport.

**Smartsheet users** should use the new [hosted official server](https://developers.smartsheet.com/ai-mcp/smartsheet/mcp-server) — the old GitHub repo is deprecated. Requires Business plan or higher.

**The gap narrows but persists.** Google shipped official Workspace MCP servers in April 2026 but skipped Sheets — the most requested Workspace service for AI integration. Microsoft's MCP catalog still has no dedicated Excel server. The community continues to fill the gap impressively — the 3,800-star Excel server proves demand is massive, and Graph API options (Aanerud, Arcade.dev) are closing the cloud Excel gap from the community side.

## Rating: 3.5 / 5

The spreadsheet MCP ecosystem is **broad and surprisingly capable**. The Excel Python server's 3,800 stars make it one of the most popular MCP servers period, and official vendor servers exist for Airtable, Smartsheet, and now Google Workspace (though Sheets was excluded). The sbroenne COM server's 77% star surge and 113 releases show the Windows Excel automation niche is thriving. But the two biggest platforms — Google Sheets and Microsoft Excel — still lack official dedicated MCP servers. Google shipping Workspace MCP but skipping Sheets is the most telling gap in the entire MCP ecosystem. Rating holds at 3.5/5 — the community options are excellent, but official vendor support for the two dominant spreadsheet platforms remains absent.

