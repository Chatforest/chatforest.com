---
title: "The Notion MCP Server — Your Workspace in Your Agent's Hands (Both Versions)"
date: 2026-03-14T03:33:50+09:00
description: "Notion offers two official MCP servers: a hosted OAuth-based remote server and an open-source local server via npm. Together they give AI agents full read/write access to your Notion workspace — pages, databases, comments, search. But the local server is being sunsetted, v2.0 broke every existing workflow, and OAuth tokens expire three times a week. Here's the honest review."
og_description: "Notion's official MCP server gives AI agents workspace access with 18+ tools. Two versions (hosted OAuth + local npm), strong capabilities, but a sunsetting local server and v2.0 breaking changes create real friction. Rating: 3.5/5."
content_type: "Review"
card_description: "Notion's official MCP server for AI-powered workspace access. Two versions — hosted OAuth remote server and local npm package. 18+ tools for pages, databases, comments, and search. Strong concept but v2.0 breaking changes, OAuth token expiry issues, and the local server being sunsetted create friction."
---

Notion is the productivity tool that half the tech industry runs on. Wikis, project trackers, meeting notes, documentation — if your team uses Notion, the data sitting in those pages is some of the most valuable context an AI agent could access.

The [official Notion MCP server](https://github.com/makenotion/notion-mcp-server) gives agents that access. Read pages, create documents, query databases, add comments, search your workspace — all through MCP tools. With ~4,000 GitHub stars, 499 forks, and broad client support (Claude Desktop, Cursor, VS Code Copilot, ChatGPT), it has real adoption.

But there's a twist: Notion actually offers *two* MCP servers, and they're diverging fast. The **hosted remote server** at `mcp.notion.com` uses OAuth and requires zero local setup. The **local open-source server** (`@notionhq/notion-mcp-server` on npm) uses integration tokens and runs on your machine. Notion has explicitly stated they're prioritizing the hosted version and [may sunset the local server](https://github.com/makenotion/notion-mcp-server). Issues and pull requests on the GitHub repo are not actively monitored.

This is the first productivity/knowledge management tool we've reviewed, and it reveals a recurring pattern in the MCP ecosystem: first-party vendors are moving from local servers to hosted remote servers with OAuth. Sentry did it. Slack did it. Now Notion is doing it. The question is whether the hosted version is ready to be the only option.

## What It Does

The Notion MCP server provides 18 tools across five capability areas:

### Pages
- **`notion-create-pages`** — Create one or more pages with properties, content (in Notion-flavored Markdown), icons, and cover images. Can target a specific parent page or database, or create private pages.
- **`notion-update-page`** — Update page properties, content, icon, or cover. Supports applying database templates.
- **`notion-move-pages`** — Move pages or databases to a new parent location.
- **`notion-duplicate-page`** — Duplicate a page within the workspace. Completes asynchronously.
- **`notion-fetch`** — Retrieve page content by URL or ID, returned as Notion-flavored Markdown. Also handles databases and data sources.

### Databases (Data Sources)
- **`notion-create-database`** — Create a new database with specified properties and an initial view.
- **`notion-update-data-source`** — Update data source properties, name, description, or attributes.
- **`notion-create-view`** — Create database views: table, board, list, calendar, timeline, gallery, form, chart, map, or dashboard.
- **`notion-update-view`** — Modify view configuration including filters, sorts, and display settings.
- **`notion-query-data-sources`** — Query across multiple data sources with structured summaries. **Requires Enterprise plan with Notion AI.**
- **`notion-query-database-view`** — Query using a pre-defined view's filters and sorts. **Requires Business+ plan with Notion AI.**

### Search & Discovery
- **`notion-search`** — Search across your Notion workspace. With a Notion AI plan, also searches connected tools (Slack, Google Drive, Jira). Rate-limited to 30 requests/minute.

### Comments
- **`notion-create-comment`** — Add page-level or block-level comments, including discussion replies.
- **`notion-get-comments`** — List all comments and discussions on a page, including resolved threads.

### Workspace Info
- **`notion-get-teams`** — List teams/teamspaces in the workspace.
- **`notion-get-users`** — List all workspace users.
- **`notion-get-user`** — Get a specific user's details.
- **`notion-get-self`** — Get information about the bot user and workspace.

The tool count is solid. Compared to other first-party MCP servers we've reviewed, Notion's coverage is among the most comprehensive — only Sentry (with ~20 tools) is comparable.

## Setup

### Hosted Remote Server (Recommended)

The hosted server at `mcp.notion.com` is Notion's preferred path:

**Claude Desktop / Cursor / VS Code:**
```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "MCP_TRANSPORT": "streamable-http",
        "MCP_URL": "https://mcp.notion.com/mcp"
      }
    }
  }
}
```

You'll be redirected to authorize via OAuth in your browser. No integration token needed — the server manages sessions and stores the API token from the OAuth exchange. Your Notion workspace permissions are reflected in what the agent can access.

### Local Server (May Be Sunsetted)

For the local server, you need an internal integration token:

1. Create an integration at [notion.so/profile/integrations](https://www.notion.so/profile/integrations)
2. Grant the integration access to specific pages and databases (click "…" → "Connections" → add your integration on each page)
3. Configure your MCP client:

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "OPENAPI_MCP_HEADERS": "{\"Authorization\": \"Bearer ntn_YOUR_TOKEN\", \"Notion-Version\": \"2025-09-03\"}"
      }
    }
  }
}
```

Also available via Docker (`docker pull ghcr.io/makenotion/notion-mcp-server`).

The local setup has more friction — creating the integration, copying the token, manually granting page access — but gives you full control over what the agent can see.

## What Works

**Notion-flavored Markdown is genuinely clever.** Notion's API returns deeply nested JSON with block hierarchies, property schemas, and metadata. The MCP server compresses all of this into a Markdown dialect that preserves Notion-specific features (callouts, columns, toggles, databases) while dramatically reducing token consumption. This is the same approach Notion uses for their hosted server, and it's measurably more efficient than raw API responses.

**The tool design is agent-friendly.** Tools like `notion-create-pages` accept content in Markdown rather than forcing agents to construct Notion's block JSON. This is a deliberate design choice — agents are good at generating Markdown, terrible at constructing deeply nested property objects. The hosted server's tools were rewritten specifically for conversational AI workflows.

**Search across connected tools is powerful (with Notion AI).** If you're on a Notion AI plan, the search tool queries not just your Notion workspace but connected Slack channels, Google Drive files, and Jira tickets. For agents doing research across an organization's knowledge, this is genuinely valuable.

**View creation covers every layout type.** The `notion-create-view` tool supports 10 different view types including charts, maps, and dashboards. This is more comprehensive than most users would expect from an MCP integration.

**OAuth on the hosted server is the right model.** One-click authorization, no tokens on disk, permissions inherited from your Notion workspace. Like Sentry's `mcp.sentry.dev`, this is what first-party MCP integration should look like.

## What Doesn't Work

**The local server is being abandoned.** Notion's README explicitly warns: "We may sunset this local MCP server repository in the future. Issues and pull requests are not actively monitored." This isn't subtle deprecation — it's a clear signal. If you build workflows on the local server, plan for migration.

**v2.0.0 broke every existing workflow.** The migration to Notion API 2025-09-03 renamed "databases" to "data sources" across the entire tool surface. `post-database-query` → gone. `update-a-database` → gone. `create-a-database` → gone. `database_id` parameters → `data_source_id`. Any existing prompts, scripts, or agent configurations referencing the old terminology stopped working. The conceptual rename is Notion's API decision, but the MCP server passed the breaking change through without a migration path.

**OAuth tokens expire too frequently.** [Issue #225](https://github.com/makenotion/notion-mcp-server/issues/225) reports OAuth tokens requiring re-authentication 3+ times per week. For a tool meant to be always-on in your development workflow, frequent auth interruptions defeat the purpose.

**JSON serialization bugs break operations.** A [reported bug](https://github.com/anthropics/claude-code/issues/25865) shows that MCP framework serialization passes JSON object parameters as strings, causing Zod validation failures. This means `notion-update-page`, `notion-move-pages`, and `notion-create-pages` can fail silently in certain clients (Claude Code's Cowork mode specifically). The bug is in the client-server interaction layer, making it hard for either side to fix independently.

**Page connection is manual and tedious.** Creating a Notion integration doesn't give it access to your workspace. You must manually go into each page or database, click "…" → "Connections," and add your integration. For large workspaces with hundreds of pages, this is impractical. The hosted OAuth server inherits your workspace permissions, which is better, but the local server requires this manual step.

**Two premium tools are paywalled behind Notion AI.** `notion-query-data-sources` requires Enterprise with Notion AI. `notion-query-database-view` requires Business+ with Notion AI. These are the most powerful query tools — cross-database structured queries and view-based filtering. Without them, you're limited to basic search and individual page fetches.

**Rate limits are tight for agents.** 180 requests/minute general, 30 requests/minute for search. An agent doing a thorough workspace exploration — searching, fetching pages, reading databases — can hit the search limit in under a minute. There's no built-in rate limit handling or backoff in the server.

**No file uploads.** You can't attach images or files through the MCP server. Notion says it's on the roadmap, but today the server is text-only for content creation.

**Transcription blocks are blocked.** Notion's API returns a 400 error for transcription blocks (AI meeting notes). If your agent tries to read a page with meeting transcriptions, those sections come back empty.

**Cannot delete databases.** An intentional safety limit — the API supports deletion but the MCP server blocks it. Reasonable, but worth knowing if you're expecting full CRUD.

## The Two-Server Problem

The elephant in the room is that Notion is running two MCP servers simultaneously, and they're not equivalent:

| Feature | Hosted (mcp.notion.com) | Local (@notionhq/notion-mcp-server) |
|---------|------------------------|--------------------------------------|
| Auth | OAuth 2.0 (one-click) | Integration token (manual) |
| Setup | Zero-install | npx or Docker |
| Page access | Inherits workspace permissions | Manual per-page connection |
| Token optimization | Notion-flavored Markdown | Standard API responses |
| Active support | Yes | "May be sunsetted" |
| Offline use | No | Yes |
| Self-hosted | No | Yes |
| Enterprise controls | Notion-managed | You manage |

For individual developers and small teams, the hosted server is clearly better. But for enterprises that need self-hosted deployments, audit logs, or network-level controls, the local server's deprecation is a problem with no announced replacement.

## Alternatives

**[suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server)** — The most popular community alternative (~49K estimated downloads). Adds optional per-request Markdown conversion for token optimization. Active development. If the official local server is sunsetted, this becomes the de facto open-source option.

**[awkoy/notion-mcp-server](https://github.com/awkoy/notion-mcp-server)** — A production-ready community implementation with a complete tool set. More actively maintained than the official local server's GitHub suggests.

**[NotionMCP Light](https://skywork.ai/skypage/en/notion-ai-workflow-guide/1978343041038721024)** — Lighter-weight alternative focused on Markdown document workflows (technical docs, blog drafts, meeting notes). Trades feature coverage for efficiency and lower token costs.

**Notion's own API directly** — If you're building custom tooling, the [Notion SDK](https://github.com/makenotion/notion-sdk-js) gives you full API access without the MCP abstraction layer. More work to set up, but no MCP server bugs or limitations.

**Obsidian + local file MCP** — For personal knowledge management that doesn't need Notion's collaboration features, Obsidian with a filesystem MCP server gives agents access to your notes with zero API calls, no rate limits, and no authentication. Different trade-off entirely.

## Who Should Use It

**Use the hosted server if:**
- Your team already uses Notion as a primary knowledge base
- You want agents to draft documents, update project trackers, or query databases
- You're on a Notion AI plan (unlocks the best query tools)
- You use Claude Desktop, Cursor, or another MCP client that supports OAuth

**Use the local server (while it lasts) if:**
- You need self-hosted deployment for compliance or security reasons
- You need offline access to Notion through your agent
- You want to run it in a controlled enterprise environment

**Skip it if:**
- You're not already a Notion user — this server extends Notion, it doesn't replace it
- You need stable, long-term tooling — the ecosystem is in flux (v2.0 breaking changes, local server sunsetting)
- You need file upload or meeting transcription access
- You're on Notion's free plan and want advanced query capabilities

{{< verdict rating="3.5" summary="The right idea executed in transition — powerful workspace access, but the two-server split and v2.0 breaking changes create real friction" >}}
The Notion MCP server gives AI agents meaningful access to one of the most widely-used productivity platforms. 18 tools covering pages, databases, comments, search, and workspace management is comprehensive coverage. The Notion-flavored Markdown approach is genuinely clever — reducing token consumption while preserving Notion-specific features. And the hosted server's OAuth model is the direction all first-party MCP servers should follow.

The 3.5 rating reflects the transition pains. The local server is being sunsetted with no enterprise-ready replacement announced. v2.0.0 broke every existing workflow with the databases-to-data-sources rename. OAuth tokens expire too frequently. JSON serialization bugs cause silent failures in certain clients. Two of the most powerful query tools are locked behind premium Notion AI plans. And the rate limits (especially 30 searches/minute) are tight for agents doing real workspace exploration.

Notion is clearly investing in MCP — the hosted server architecture is sophisticated, and the tool design shows AI-first thinking. But today, you're adopting a platform in the middle of a migration from one architecture (local, token-based) to another (hosted, OAuth-based). If you're a Notion-heavy team and willing to ride out the transition, this is worth setting up. If you need stability, wait for the dust to settle.
{{< /verdict >}}
