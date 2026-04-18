---
title: "The Slack MCP Server — Your Workspace, Accessible to Agents"
date: 2026-03-14T01:06:39+09:00
description: "Slack's official MCP server lets AI agents search messages, send replies, and manage canvases in your workspace. Here's the honest review of what works and what doesn't."
og_description: "Slack's official MCP server lets AI agents search messages, send replies, and manage canvases in your workspace. Here's the honest review."
content_type: "Review"
card_description: "Slack's official MCP server lets AI agents search messages, send replies, and manage canvases. The right way to give agents Slack access."
last_refreshed: 2026-04-18
---

Slack is where work conversations happen. The problem is that those conversations are locked inside Slack — an agent can't search your channels, read a thread, or post an update without some kind of integration. Slack's official MCP server changes that. Generally available since February 28, 2026, it gives AI agents direct, structured access to your workspace through the Model Context Protocol.

**At a glance:** Hosted at `mcp.slack.com` · ~15 curated tools · 50+ partner companies building agents · 25x growth in tool invocations since limited release · Streamable HTTP transport · Confidential OAuth 2.0 (PKCE now supported) · PulseMCP: ~29.1K all-time visitors, ~3.3K weekly, #827 globally. Part of our **[Communication & Collaboration MCP category](/categories/communication-collaboration/)**.

This isn't a community wrapper or a bot token hack. It's Slack's own server, hosted at `mcp.slack.com`, using their first-party OAuth. Here's what it's actually like to work with.

## What's New (April 2026 Updates)

Since our last refresh, Slack's AI platform has seen its most ambitious overhaul since the Salesforce acquisition — reshaping the competitive landscape for the MCP server.

**Slackbot becomes an agentic desktop agent (March 31).** Salesforce unveiled 30+ new AI capabilities for Slackbot, the most sweeping update since the $27.7B acquisition. Slackbot now functions as an **MCP client** — it can connect to and coordinate with any external service that registers an MCP server through Slack's manifest, including Agentforce, Google Workspace, Microsoft 365, Notion, Workday, ServiceNow, and 6,000+ apps in the Salesforce ecosystem. New capabilities include **reusable AI Skills** (define a workflow once, Slackbot learns to run it automatically), **meeting intelligence** (transcribes calls across Zoom, Google Meet, and Huddles with action item extraction), **desktop agent mode** (monitors screen activity, deals, calendar, and habits to surface suggestions proactively), and a **lightweight CRM** built directly into chat. All features run on Anthropic's Claude. This is a massive competitive expansion — Slackbot is no longer just a chat assistant, it's an agent platform.

**Slackbot expands to free and Pro plans (April 2026).** A limited version of Slackbot is now becoming available to users on Slack's free and Pro plans, down from the previous Business+/Enterprise+ restriction. Starting summer 2026, every new Salesforce customer will have Slack automatically provisioned and AI-enabled from day one.

**PKCE support GA (March 30).** OAuth PKCE (Proof Key for Code Exchange) is now generally available for all Slack apps, enabling desktop and mobile clients to authenticate without embedding a `client_secret`. This is a meaningful improvement for custom MCP clients — PKCE-enabled apps are marked as public clients (one-way, irreversible without Slack support). All refresh tokens expire after 30 days for PKCE-enabled apps. Desktop redirects cannot request bot scopes.

**Enterprise search now indexes GitHub issues (April 1).** Slack's enterprise search can now surface GitHub issues alongside messages, files, and email — up to 5 GitHub organizations connectable. Combined with the existing Gmail/Outlook indexing (March 2026), MCP-connected agents searching Slack may now surface results from three external systems. The data governance implications continue to expand.

**Marketplace agent ecosystem grows.** The agentic marketplace now includes Claude, Claude Code, Cursor, Guru, Manus, Perplexity, Read AI, Tembo, Spotter, Alysio GTM, Credal AI, Moveworks, WRITER, Learn Place, Nalvin, Wordsmith, Workleap, and more. The ecosystem has moved firmly from "experiment" to "production."

**send_message reliability issues reported.** Multiple users have reported `slack_send_message` failing with MCP error -32603 (Internal Server Error) while `slack_schedule_message` works correctly on the same channel with the same credentials — suggesting a bug specific to the instant send code path. Separately, after a Claude.ai service outage on April 6, all connectors disconnected and the Slack connector failed to automatically reconnect for some users. These issues are tracked in the Claude Code GitHub repository.

### Earlier updates (still relevant)

**General availability confirmed (Feb 28).** Both the MCP server and the Real-Time Search (RTS) API graduated from limited release. Slack reports MCP tool invocations and RTS query counts both grew 25x during the preview period. Over 50 partner companies are now building context-aware agents on the platform, including Anthropic, Google, OpenAI, and Perplexity.

**Interactive message composer in Claude.** The MCP server features a message composer that lets you draft, format, and preview Slack messages directly within Claude — with a live preview of how the message will appear in Slack. Search conversations for context, generate a draft with AI assistance, edit it, and review before sending.

**Expanded OAuth scopes.** The permission model has grown more granular. New scopes include `search:read.files` (file search), `search:read.users` (user search), `canvases:read` (read canvases without write access), and history scopes (`channels:history`, `groups:history`, `mpim:history`, `im:history`) for reading message history. The old single `search:read` scope has been broken into fine-grained `search:read.*` variants.

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

**For custom clients:** You need to register a Slack app at api.slack.com, configure OAuth with the right scopes, and handle the token exchange yourself. As of March 30, PKCE is now GA — desktop and mobile clients can authenticate without embedding a `client_secret`, though enabling PKCE permanently marks your app as a public client. Your app must be published to the Slack Marketplace or registered as an internal app — unlisted apps can't access MCP. **Important:** Dynamic Client Registration (DCR) is still not supported. Your app needs a fixed, pre-registered app ID hardcoded into the client. OpenAI Codex users have reported authentication failures specifically because of this — check GitHub issue #13200 if you hit "Dynamic client registration not supported" errors.

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

**No SSE or Dynamic Client Registration support.** The server only supports Streamable HTTP (JSON-RPC 2.0). If your MCP client uses Server-Sent Events for transport — which some earlier MCP clients do — it won't work. The lack of DCR has caused real pain for OpenAI Codex users trying to connect. PKCE support (GA March 30) helps desktop/mobile clients authenticate without a `client_secret`, but DCR remains absent.

**send_message has reliability issues.** Multiple users report `slack_send_message` failing with MCP error -32603 (Internal Server Error) while `slack_schedule_message` works correctly on the same channel with the same credentials. This suggests a bug in the instant send code path. Separately, after a Claude.ai outage on April 6, the Slack connector failed to reconnect automatically for some users, requiring manual re-authorization.

**Rate limits vary by tool and aren't well-documented in practice.** Some tools are Tier 2 (20+ per minute), others Tier 4 (100+ per minute). Search and messaging have "special" rate limits that require checking individual method pages. In practice, a busy agent doing workspace research can bump into the Tier 2 limits on message search. The error messages don't include retry-after headers, so your client is guessing on backoff timing.

**Enterprise search now crosses three external systems.** With Gmail, Outlook, and now GitHub Issues indexing (up to 5 organizations, added April 2026), a search query through the MCP server may surface results from email and code tracking systems. This is powerful but expands the blast radius of a `search:read` scope grant in ways users may not expect. If your organization has enabled cross-system search, review what data sources agents can reach.

**Search scope can surprise users.** If you grant `search:read.private` or `search:read.im`, the agent can search your private conversations. The OAuth consent screen explains this, but in the flow of "just click authorize to get it working," people grant broader access than they intend. Be deliberate about which scopes you authorize.

## Compared to Alternatives

**vs. korotovsky/slack-mcp-server (1,500 stars, 293 forks):** The most popular community alternative, now claiming 30,000+ monthly engineer visitors and 9,000+ active users. Written in Go, supports Stdio, SSE, and HTTP transports. No Marketplace requirement, no permission restrictions, supports DMs, group DMs, GovSlack, and user group management. Has an optional "stealth mode" without app installation. PulseMCP: ~305K all-time visitors, ~3.5K weekly, #143 globally — significantly outpacing the official server's #827 ranking. The downside: raw bot tokens in environment variables, no token refresh, community maintenance only. 43 open issues and 40 open PRs suggest active development but also growing maintenance load. Good for power users; the official server is better for teams that need guardrails.

**vs. Community Slack MCP server (@modelcontextprotocol/server-slack):** The original reference implementation, now showing its age. Uses a bot token and runs locally. Simpler to set up for personal use (no Marketplace requirement), but lacks the granular OAuth scopes, natural language responses, and audit logging. The official server has clearly surpassed it for production use.

**vs. Slackbot (now available on all plans):** Massively upgraded in March 2026 with 30+ new AI capabilities. Slackbot is now an **MCP client** that can connect to 6,000+ apps, a **desktop agent** that monitors screen activity and proactively surfaces suggestions, and has **reusable AI Skills**, **meeting intelligence** (transcription + action items across Zoom/Meet/Huddles), and a **lightweight CRM** built into chat. All powered by Anthropic's Claude. A limited version is now available on free and Pro plans (previously Business+/Enterprise+ only). The relationship between Slackbot and the MCP server has shifted: Slackbot is now both a competitor (it provides AI-in-Slack without needing external clients) and a complement (as an MCP client, it can coordinate with MCP servers). If you want a full agentic assistant inside Slack, Slackbot is increasingly the answer. The MCP server's differentiation is now primarily about bringing *your choice* of external AI client to Slack data.

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
- Slackbot already covers your needs (now available on all plans, including free and Pro)

{{< verdict rating="4" summary="Still the right integration for external AI clients, but Slackbot is closing the gap fast" >}}
The Slack MCP server remains production-proven and well-architected — PKCE support, granular OAuth scopes, and 50+ partner companies confirm Slack's commitment. But the competitive landscape shifted dramatically in late March. Slackbot's 30+ feature upgrade transformed it from a basic assistant into an agentic desktop agent with MCP client capabilities, meeting intelligence, reusable AI Skills, and a lightweight CRM — and it's now available on free and Pro plans. The MCP server's value proposition has narrowed: it's for teams that want to bring *their choice* of external AI client (Claude, Cursor, Perplexity) to Slack data rather than using Slack's built-in AI. That's still a legitimate use case, especially for multi-tool workflows. But the gaps remain real — only ~15 out of 200+ API methods, no DCR, the Marketplace requirement, and now a `send_message` reliability bug. The community alternative (korotovsky, 1,500 stars, PulseMCP #143 vs. official #827) continues to outpace the official server in adoption. Rating holds at 4/5 — the architecture is sound and the integration works, but Slack needs to either expand the tool set or explain why 15 tools is the ceiling.
{{< /verdict >}}

*Disclosure: This review is based on publicly available documentation, GitHub repositories, developer forums, and Slack's official announcements. ChatForest does not test MCP servers hands-on. We research, analyze, and present what we find so you can make informed decisions. Review written and edited using Claude Opus 4.6 (Anthropic). Last updated 2026-04-18.*
