---
title: "The Slack MCP Server — Your Workspace, Accessible to Agents"
date: 2026-03-14T01:06:39+09:00
description: "Slack's official MCP server lets AI agents search messages, send replies, and manage canvases in your workspace. Here's the honest review of what works and what doesn't."
og_description: "Slack's official MCP server lets AI agents search messages, send replies, and manage canvases in your workspace. Here's the honest review."
content_type: "Review"
card_description: "Slack's official MCP server lets AI agents search messages, send replies, and manage canvases. The right way to give agents Slack access."
last_refreshed: 2026-03-14
---

Slack is where work conversations happen. The problem is that those conversations are locked inside Slack — an agent can't search your channels, read a thread, or post an update without some kind of integration. Slack's official MCP server changes that. Generally available since February 28, 2026, it gives AI agents direct, structured access to your workspace through the Model Context Protocol.

**At a glance:** Hosted at `mcp.slack.com` · ~15 curated tools · 50+ partner companies building agents · 25x growth in tool invocations since limited release · Streamable HTTP transport · Confidential OAuth 2.0. Part of our **[Communication & Collaboration MCP category](/categories/communication-collaboration/)**.

This isn't a community wrapper or a bot token hack. It's Slack's own server, hosted at `mcp.slack.com`, using their first-party OAuth. Here's what it's actually like to work with.

## What's New (March 2026 Updates)

Since our initial review, Slack's MCP ecosystem has seen significant movement:

**General availability confirmed (Feb 28).** Both the MCP server and the Real-Time Search (RTS) API graduated from limited release. Slack reports MCP tool invocations and RTS query counts both grew 25x during the preview period. Over 50 partner companies are now building context-aware agents on the platform, including Anthropic, Google, OpenAI, and Perplexity.

**Interactive message composer in Claude.** The MCP server now features a message composer that lets you draft, format, and preview Slack messages directly within Claude — with a live preview of how the message will appear in Slack. Search conversations for context, generate a draft with AI assistance, edit it, and review before sending. This addresses the "fire-and-forget" messaging concern from our original review.

**Expanded OAuth scopes.** The permission model has grown more granular. New scopes include `search:read.files` (file search), `search:read.users` (user search), `canvases:read` (read canvases without write access), and history scopes (`channels:history`, `groups:history`, `mpim:history`, `im:history`) for reading message history. The old single `search:read` scope has been broken into fine-grained `search:read.*` variants.

**Slackbot GA (Jan 13).** Slack launched its own built-in AI agent, Slackbot, for Business+ and Enterprise+ plans. It understands conversations, drafts content, schedules meetings, and connects to Salesforce data. This is Slack's first-party AI play — complementary to, but increasingly competing with, the MCP server's "bring your own AI" model.

**Enterprise search expands.** As of March 2026, Slack's enterprise search now indexes Gmail and Outlook as data sources, with scope approval controls for app permission reviews. This means MCP-connected agents searching Slack may surface results that originally came from email — something to factor into your data governance.

**Agentic marketplace launches.** Slack Marketplace now features AI agents from Claude (Anthropic), ChatGPT (OpenAI), Google Agentspace (Gemini), Perplexity, Notion AI, and Dropbox Dash. The ecosystem is moving from "experiment" to "production."

## What It Does

The Slack MCP server provides approximately 15 curated tools across four categories (out of Slack's 200+ API methods):

**Search:**
- Search messages across channels, filterable by date, user, and content type
- Search files shared in the workspace
- Find channels by name and description
- Look up users by name, email, or user ID (with partial matching)

**Messaging:**
- Send messages to any conversation — channels, DMs, group DMs
- Read complete message history from channels
- Retrieve full thread conversations
- Draft and preview formatted messages within the AI client (with live preview in Claude)

**Canvases:**
- Create and update rich, formatted documents (Slack's canvas feature)
- Read and export canvases as markdown

**Users:**
- Access complete user profiles, including custom fields and status

Unlike the older community `@modelcontextprotocol/server-slack` npm package (which uses a bot token and talks to Slack's regular API), the official server uses confidential OAuth and is purpose-built for LLM consumption. Tool descriptions are designed for agents, and responses come back as natural language rather than raw JSON.

## Setup

This is where the Slack MCP server diverges from most MCP servers we've reviewed. There's no `npx` command. No local process to run. The server is hosted by Slack.

**For supported clients (Claude.ai, Claude Code, Cursor, Perplexity):** These have built-in integration. In Claude Desktop, you add Slack as a remote MCP server pointing to `https://mcp.slack.com/mcp`. The client handles the OAuth flow — you authorize your Slack workspace, grant the scopes you're comfortable with, and you're connected.

**For custom clients:** You need to register a Slack app at api.slack.com, configure confidential OAuth with the right scopes, and handle the token exchange yourself. Your app must be published to the Slack Marketplace or registered as an internal app — unlisted apps can't access MCP. **Important:** Dynamic Client Registration (DCR) is not supported. Your app needs a fixed, pre-registered app ID hardcoded into the client. OpenAI Codex users have reported authentication failures specifically because of this — check GitHub issue #13200 if you hit "Dynamic client registration not supported" errors.

**Required OAuth scopes** depend on what you want to do:
- `search:read.public` — Search public channels (required baseline)
- `search:read.private` — Search private channels (requires user consent)
- `search:read.im` — Search DMs (requires user consent)
- `search:read.mpim` — Search group DMs (requires user consent)
- `search:read.files` — Search files
- `search:read.users` — Search users
- `channels:history`, `groups:history`, `mpim:history`, `im:history` — Read message history
- `chat:write` — Send messages
- `canvases:read` — Read canvases
- `canvases:write` — Create/update canvases
- `users:read`, `users:read.email` — Look up user profiles

**Setup difficulty: Easy for supported clients, moderate for custom builds.** If you're using Claude Desktop or Cursor, it's a few clicks. If you're building your own MCP client, budget time for Slack app registration and OAuth configuration.

## What Works Well

**Search is genuinely powerful.** Searching across an entire Slack workspace from within an AI conversation is a significant capability. "Find that thread where the team discussed the database migration last week" — that actually works. Date and user filters keep results focused. This alone justifies the integration for most teams.

**Granular privacy controls are done right.** The scope model has gotten even more granular since launch. Public channel search is the baseline, but accessing DMs, private channels, files, or message history each requires its own explicit scope. This is a meaningful upgrade from the old bot-token approach where a single token could access everything the bot was invited to. Admins can see and manage which MCP clients have access, with full audit logging.

**Natural language responses save context.** When you search for messages, the server returns results formatted for LLM consumption, not raw API JSON. This means less parsing overhead, fewer tokens wasted on structural data, and more usable answers in the conversation. It's a small thing that makes a noticeable difference in practice.

**The message composer changes the writing workflow.** The interactive composer in Claude — with live preview, formatting controls, and search-for-context built in — turns "agent sends a message" from a risky fire-and-forget into a collaborative drafting process. This is a real improvement over the raw `chat:write` tool call.

**Canvas integration opens up document workflows.** Being able to create, read, and update canvases from an agent means you can generate reports, meeting summaries, or documentation and publish them directly where your team works — inside Slack. The new `canvases:read` scope means you can give an agent read-only access without write risk.

**No local server to manage.** The server runs at `mcp.slack.com`. No npm install, no Docker, no Node.js version drama. It just works. This is how hosted MCP servers should operate.

## What Doesn't Work Well

**Only ~15 tools out of 200+ API methods.** The official server covers a curated subset of Slack's capabilities. No reactions, no emoji, no scheduled messages, no reminders, no pins, no bookmarks. Thread creation only works by replying. For teams that need deeper Slack automation, this coverage gap is the biggest frustration.

**The Marketplace requirement is a barrier for custom clients.** If you're building your own MCP client, your Slack app must be published to the Marketplace or registered as an internal app. You can't just create a quick app for personal use and connect it. This protects workspaces from rogue integrations, but it slows down developers who want to experiment.

**No SSE or Dynamic Client Registration support.** The server only supports Streamable HTTP (JSON-RPC 2.0). If your MCP client uses Server-Sent Events for transport — which some earlier MCP clients do — it won't work. The lack of DCR has caused real pain for OpenAI Codex users trying to connect. Not dealbreakers for the four supported clients, but a meaningful gap for the broader MCP ecosystem.

**Rate limits vary by tool and aren't well-documented in practice.** Some tools are Tier 2 (20+ per minute), others Tier 4 (100+ per minute). Search and messaging have "special" rate limits that require checking individual method pages. In practice, a busy agent doing workspace research can bump into the Tier 2 limits on message search. The error messages don't include retry-after headers, so your client is guessing on backoff timing.

**Enterprise search now crosses system boundaries.** With Gmail and Outlook indexing, a search query through the MCP server may surface results from email systems. This is powerful but expands the blast radius of a `search:read` scope grant in ways users may not expect. If your organization has enabled cross-system search, review what data sources agents can reach.

**Search scope can surprise users.** If you grant `search:read.private` or `search:read.im`, the agent can search your private conversations. The OAuth consent screen explains this, but in the flow of "just click authorize to get it working," people grant broader access than they intend. Be deliberate about which scopes you authorize.

## Compared to Alternatives

**vs. korotovsky/slack-mcp-server (1,300+ stars):** The most popular community alternative. Written in Go, supports Stdio, SSE, and HTTP transports. No Marketplace requirement, no permission restrictions, supports DMs, group DMs, and GovSlack. Has an optional "stealth mode" without app installation. The downside: raw bot tokens in environment variables, no token refresh, community maintenance only. Research suggests 43% of publicly available MCP servers contain command injection vulnerabilities — weigh flexibility against security. Good for power users; the official server is better for teams that need guardrails.

**vs. Community Slack MCP server (@modelcontextprotocol/server-slack):** The original reference implementation, now showing its age. Uses a bot token and runs locally. Simpler to set up for personal use (no Marketplace requirement), but lacks the granular OAuth scopes, natural language responses, and audit logging. The official server has clearly surpassed it for production use.

**vs. Slackbot (Business+/Enterprise+):** Slack's own built-in AI agent, GA since January 2026. It understands conversations, drafts content, schedules meetings, and connects to Salesforce data. If your team is already on Business+ or Enterprise+ and you want a "just works" AI in Slack without configuring external clients, Slackbot is the zero-setup option. The MCP server is for bringing your own AI client (Claude, Cursor, Perplexity) rather than using Slack's built-in AI. They're complementary — Slackbot for Slack-native AI, MCP for external agent access.

**vs. Truto Managed MCP:** A third-party managed service that dynamically generates tools from Slack's full API documentation (not just the curated 15). Includes automatic token refresh, method-level filtering, and expiring access URLs. The trade-off is routing your data through an external service — not suitable for strict data sovereignty requirements.

## Who Should Use This

**Yes, use it if:**
- Your team lives in Slack and you want your AI agent to search workspace knowledge
- You use a supported MCP client (Claude, Cursor, Perplexity) and want easy setup
- You need an agent to post updates, summaries, or reports to channels
- Workspace security, admin oversight, and audit logging are important to you
- You want to create or update canvases programmatically
- The interactive message composer workflow appeals to you (Claude users)

**Skip it if:**
- You just need a quick personal Slack bot (use korotovsky's server or a bot token)
- Your MCP client doesn't support Streamable HTTP transport or requires DCR
- You need reactions, scheduled messages, pins, or other Slack features beyond the curated 15 tools
- You're building a custom client and don't want to deal with Marketplace registration
- You're on a Business+ plan and Slackbot already covers your needs

{{< verdict rating="4" summary="The right way to give agents Slack access — now with proof at scale" >}}
The Slack MCP server has matured from a promising launch to a production-proven platform. The 25x growth in tool invocations, 50+ partner companies, and the interactive message composer in Claude show real momentum. The expanded OAuth scopes give finer-grained control, and the GA status means Slack is committed to this as infrastructure, not an experiment. The gaps remain real — only 15 out of 200+ API methods, no DCR support, and the Marketplace requirement still frustrates developers. But with Slackbot handling the "built-in AI" use case and the MCP server handling "bring your own agent," Slack now has a coherent two-track AI strategy. If your team uses Slack and you're using a supported AI client, this is the integration to start with.
{{< /verdict >}}

*Disclosure: This review is based on publicly available documentation, GitHub repositories, developer forums, and Slack's official announcements. ChatForest does not test MCP servers hands-on. We research, analyze, and present what we find so you can make informed decisions. Review written and edited using Claude Opus 4.6 (Anthropic). Last updated 2026-03-20.*
