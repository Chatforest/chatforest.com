---
title: "Spreadsheet MCP Servers — Google Sheets, Excel, Airtable, and More"
date: 2026-03-17T22:50:00+09:00
description: "Spreadsheet MCP servers reviewed: Google Sheets via google_workspace_mcp (1,800 stars, Python, MIT, 10+ Google services) and mcp-google-sheets (740 stars, 19 dedicated tools), Excel via negokaz/excel-mcp-server (883 stars, Go, cross-platform, 7 tools) and sbroenne/mcp-server-excel (81 stars, C#, Windows COM, 25 tools/230 operations), Airtable via domdomegg/airtable-mcp-server (427 stars, TypeScript, 16 tools). No official Google or Microsoft standalone spreadsheet MCP servers yet. Rating: 3.5/5."
og_description: "Spreadsheet MCP servers: Google Sheets (1,800 stars workspace, 740 stars dedicated), Excel (883 stars cross-platform, 81 stars COM automation), Airtable (427 stars, 16 tools). All community-built. Rating: 3.5/5."
content_type: "Review"
card_description: "Spreadsheets are the world's most-used data tool — and the MCP ecosystem has responded with dozens of community servers, though no official standalone servers from Google or Microsoft yet. Google Sheets has the most options, led by a 1,800-star workspace server and a 740-star dedicated Sheets server. Excel has strong cross-platform and Windows COM options. Airtable leads the structured-data space with a 427-star TypeScript server offering 16 tools."
---

Spreadsheets are arguably the world's most-used data tool, and connecting AI agents to them is a high-value use case — from financial modeling to data cleaning to report generation. The MCP ecosystem has responded with dozens of community-built servers, but notably **no official standalone spreadsheet MCP servers** from Google or Microsoft yet.

The landscape splits three ways: **Google Sheets** has the most MCP server options (10+ repos), **Excel** has both cross-platform file-based and Windows COM automation approaches, and **Airtable** occupies the structured-data middle ground between spreadsheet and database.

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

## Google Sheets — Dedicated Server

| Detail | Info |
|--------|------|
| [xing5/mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) | 740 stars |
| Language | Python |
| License | MIT |
| Tools | 19 |

A dedicated Google Sheets MCP server focused entirely on spreadsheet operations.

### What Works Well

**Deep Sheets coverage.** 19 tools covering CRUD operations, batch updates, sheet management, sharing, and chart creation. This is more spreadsheet-specific depth than the workspace server offers.

**Flexible authentication.** Supports service accounts (recommended for automation), OAuth 2.0, and Application Default Credentials. Service accounts are the right choice for server-to-server automation without user interaction.

**Zero-install deployment.** Run with `uvx mcp-google-sheets@latest` — no manual installation required.

**Tool filtering.** Context window optimization lets you disable tools you don't need, reducing token consumption from ~13,000 tokens for the full tool set to only what you've enabled.

### What Doesn't Work Well

**Community-maintained.** Not backed by Google. API changes or breaking updates depend on community response time.

**No real-time collaboration awareness.** Unlike the Google Sheets web UI, the MCP server doesn't surface who else is editing or provide conflict resolution for simultaneous edits.

## Other Google Sheets Options

Several other community servers exist:

- **[shionhonda/mcp-gsheet](https://github.com/shionhonda/mcp-gsheet)** — Lightweight MCP server for basic read/write operations on Google Sheets. Good for simple use cases.
- **[freema/mcp-gsheets](https://github.com/freema/mcp-gsheets)** — Read, write, and manage Google Sheets from Claude Desktop or Claude Code.
- **[distrihub/mcp-google-workspace](https://github.com/distrihub/mcp-google-workspace)** — A Rust-based Google Drive and Sheets MCP server, notable for using Rust in a space dominated by Python and TypeScript.
- **[a-bonus/google-docs-mcp](https://github.com/a-bonus/google-docs-mcp)** — Google Docs, Sheets, and Drive access with direct formatting and editing capabilities.

## Excel — Cross-Platform File Server

| Detail | Info |
|--------|------|
| [negokaz/excel-mcp-server](https://github.com/negokaz/excel-mcp-server) | 883 stars |
| Language | Go |
| License | MIT |
| Tools | 7 |
| Formats | xlsx, xlsm, xltx, xltm |

The most popular Excel MCP server takes a file-based approach — it reads and writes Excel files directly without requiring Microsoft Excel to be installed.

### What Works Well

**Cross-platform.** Written in Go, runs on macOS, Linux, and Windows. No Microsoft Excel installation needed — it manipulates .xlsx files directly using Go libraries.

**Formula support.** Reads and writes both values and formulas, not just static data. This is critical for financial models and analytical spreadsheets.

**Pagination.** Large spreadsheets are handled with pagination support, preventing context window overflow.

**Screenshot capability.** On Windows, can capture live screenshots of Excel sheets for visual verification by the AI agent.

### What Doesn't Work Well

**Limited tool count.** Only 7 tools means complex operations (conditional formatting, pivot tables, macros) aren't natively supported. You're limited to reading, writing, creating tables, copying sheets, and basic formatting.

**No live Excel integration.** The file-based approach means you can't interact with a running Excel instance (except on Windows). If you need to trigger recalculations or interact with Excel add-ins, this won't work.

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

**Requires Excel license.** You need Microsoft Excel installed and licensed. Not suitable for server environments or CI/CD pipelines.

**Lower adoption.** 81 stars indicates a smaller user base and potentially less battle-testing than the cross-platform alternative.

## Other Excel Options

- **[yzfly/mcp-excel-server](https://github.com/yzfly/mcp-excel-server)** — Python-based, emphasizes natural language interaction with Excel files including visualization and analysis.
- **[haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server)** — Python, file-based manipulation without needing Excel installed.
- **[Softeria/ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server)** — Microsoft 365 integration via Graph API, includes Excel as one of several services.
- **[OfficeMCP/ExcelMCP](https://github.com/OfficeMCP/ExcelMCP)** — Another Windows COM-based server for controlling Excel via MCP.

**Notable absence:** Microsoft's [official MCP catalog](https://github.com/microsoft/mcp) (2,800 stars) includes Azure, Fabric, DevOps, and many Microsoft 365 services — but no dedicated Excel MCP server. The Microsoft 365 Mail, Calendar, and User servers exist, but spreadsheet support through official channels is still missing.

## Airtable

| Detail | Info |
|--------|------|
| [domdomegg/airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server) | 427 stars |
| Language | TypeScript |
| License | MIT |
| Tools | 16 |

The leading Airtable MCP server provides comprehensive access to Airtable's structured data platform.

### What Works Well

**Full CRUD plus schema management.** 16 tools covering record operations (list, search, get, create, update, delete), schema management (list bases, describe tables, create/update tables and fields), and comments. This covers most of what you'd want to do with Airtable programmatically.

**HTTP transport.** Supports HTTP transport mode for remote MCP clients, not just stdio. This makes it usable in server-side deployments, not just desktop apps.

**Formula-based filtering.** Uses Airtable's native formula syntax for record filtering, which is powerful for users already familiar with the platform.

**Optional write scopes.** Write operations can be selectively enabled or disabled, letting you deploy a read-only version for safety.

### What Doesn't Work Well

**Not official.** Airtable hasn't released their own MCP server. Community maintenance means potential lag on API changes.

**No automation/webhook management.** You can manage records and schema, but can't create or modify Airtable Automations or manage webhooks through this server.

## Other Airtable Options

- **[felores/airtable-mcp](https://github.com/felores/airtable-mcp)** (72 stars, JavaScript, MIT) — 10 tools with staged table building capabilities and LLM-optimized system prompts.
- **[rashidazarang/airtable-mcp](https://github.com/rashidazarang/airtable-mcp)** — Full CRUD, schema management, record comments, webhooks, batch operations, and AI-powered analytics.
- **[sulaiman013/AIRTABLE-MCP](https://github.com/sulaiman013/AIRTABLE-MCP)** — Emphasizes natural language interaction with intelligent filtering and aggregation.

## What About Notion?

Notion's database features make it a spreadsheet alternative for many teams. The [official Notion MCP server](https://github.com/makenotion/notion-mcp-server) (~2,500 stars) provides access to Notion databases, pages, and blocks. If your "spreadsheet" workflow is actually structured data in Notion, the official server is well-maintained and popular.

## The Big Picture

| Platform | Top Server | Stars | Tools | Official? |
|----------|-----------|-------|-------|-----------|
| Google Sheets (workspace) | taylorwilsdon/google_workspace_mcp | 1,800 | 10+ services | No |
| Google Sheets (dedicated) | xing5/mcp-google-sheets | 740 | 19 | No |
| Excel (cross-platform) | negokaz/excel-mcp-server | 883 | 7 | No |
| Excel (Windows COM) | sbroenne/mcp-server-excel | 81 | 25 / 230 ops | No |
| Airtable | domdomegg/airtable-mcp-server | 427 | 16 | No |
| Notion | makenotion/notion-mcp-server | ~2,500 | Official | Yes |

## Who Should Use These

**Google Sheets users** have the best selection — the workspace server (1,800 stars) is mature and well-tested, and the dedicated server (740 stars, 19 tools) goes deeper on spreadsheet-specific operations. Choose based on whether you need just Sheets or the full Google Workspace suite.

**Excel users** face a fork in the road: the Go-based cross-platform server (883 stars) works everywhere but is limited to 7 tools and file-based operations. The C# COM server (81 stars) offers vastly deeper automation (230 operations) but locks you into Windows with a live Excel installation.

**Airtable users** have a solid option in the 427-star TypeScript server with 16 tools covering records, schema, and comments.

**The gap:** Neither Google nor Microsoft offers an official standalone spreadsheet MCP server. Google's ecosystem relies entirely on community servers, and Microsoft's official MCP catalog skips Excel entirely despite covering many other Microsoft 365 services. Notion is the only platform in this space with an official MCP server.

## Rating: 3.5 / 5

The spreadsheet MCP ecosystem is **broad but unofficial**. There are plenty of servers to choose from — Google Sheets alone has 10+ options — but the lack of vendor backing means API compatibility, security updates, and long-term maintenance all depend on community volunteers. The Google Sheets workspace server (1,800 stars) and the cross-platform Excel server (883 stars) have enough adoption to inspire confidence, but this is a category where official support from Google and Microsoft would make a significant difference. Airtable and Notion round out the structured-data options, with Notion being the only platform offering an official server.
