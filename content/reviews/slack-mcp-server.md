---
title: "The Slack MCP Server — Your Workspace, Accessible to Agents"
date: 2026-03-14T01:06:39+09:00
description: "Slack's official MCP server lets AI agents search messages, send replies, and manage canvases in your workspace. Here's the honest review of what works and what doesn't."
og_description: "Slack's official MCP server lets AI agents search messages, send replies, and manage canvases in your workspace. Here's the honest review."
content_type: "Review"
card_description: "Slack's official MCP server lets AI agents search messages, send replies, and manage canvases. The right way to give agents Slack access."
---

Slack is where work conversations happen. The problem is that those conversations are locked inside Slack — an agent can't search your channels, read a thread, or post an update without some kind of integration. Slack's official MCP server changes that. Launched in February 2026, it gives AI agents direct, structured access to your workspace through the Model Context Protocol.

This isn't a community wrapper or a bot token hack. It's Slack's own server, hosted at `mcp.slack.com`, using their first-party OAuth. Here's what it's actually like to work with.

## What It Does

The Slack MCP server provides tools across four categories:

**Search:**
- Search messages across channels, filterable by date, user, and content type
- Search files shared in the workspace
- Find channels by name and description
- Look up users by name, email, or user ID (with partial matching)

**Messaging:**
- Send messages to any conversation — channels, DMs, group DMs
- Read complete message history from channels
- Retrieve full thread conversations
- Draft and preview formatted messages within the AI client

**Canvases:**
- Create and update rich, formatted documents (Slack's canvas feature)
- Export canvases as markdown

**Users:**
- Access complete user profiles, including custom fields and status

Unlike the older community `@modelcontextprotocol/server-slack` npm package (which uses a bot token and talks to Slack's regular API), the official server uses confidential OAuth and is purpose-built for LLM consumption. Tool descriptions are designed for agents, and responses come back as natural language rather than raw JSON.

## Setup

This is where the Slack MCP server diverges from most MCP servers we've reviewed. There's no `npx` command. No local process to run. The server is hosted by Slack.

**For supported clients (Claude.ai, Claude Code, Cursor, Perplexity):** These have built-in integration. In Claude Desktop, you add Slack as a remote MCP server pointing to `https://mcp.slack.com/mcp`. The client handles the OAuth flow — you authorize your Slack workspace, grant the scopes you're comfortable with, and you're connected.

**For custom clients:** You need to register a Slack app at api.slack.com, configure confidential OAuth with the right scopes, and handle the token exchange yourself. Your app must be published to the Slack Marketplace or registered as an internal app — unlisted apps can't access MCP.

**Required OAuth scopes** depend on what you want to do:
- `search:read.public` — Search public channels (required baseline)
- `search:read.private` — Search private channels (requires user consent)
- `search:read.im` — Search DMs (requires user consent)
- `search:read.mpim` — Search group DMs (requires user consent)
- `chat:write` — Send messages
- `canvases:write` — Create/update canvases
- `users:read` — Look up user profiles

**Setup difficulty: Easy for supported clients, moderate for custom builds.** If you're using Claude Desktop or Cursor, it's a few clicks. If you're building your own MCP client, budget time for Slack app registration and OAuth configuration.

## What Works Well

**Search is genuinely powerful.** Searching across an entire Slack workspace from within an AI conversation is a significant capability. "Find that thread where the team discussed the database migration last week" — that actually works. Date and user filters keep results focused. This alone justifies the integration for most teams.

**Granular privacy controls are done right.** The scope model is smart. Public channel search is the baseline, but accessing DMs or private channels requires explicit user consent through separate scopes. This is a meaningful upgrade from the old bot-token approach where a single token could access everything the bot was invited to. Admins can see and manage which MCP clients have access, with full audit logging.

**Natural language responses save context.** When you search for messages, the server returns results formatted for LLM consumption, not raw API JSON. This means less parsing overhead, fewer tokens wasted on structural data, and more usable answers in the conversation. It's a small thing that makes a noticeable difference in practice.

**Canvas integration opens up document workflows.** Being able to create and update canvases from an agent means you can generate reports, meeting summaries, or documentation and publish them directly where your team works — inside Slack. Export-as-markdown is a nice touch for agents that need to process canvas content.

**No local server to manage.** The server runs at `mcp.slack.com`. No npm install, no Docker, no Node.js version drama. It just works. This is how hosted MCP servers should operate.

## What Doesn't Work Well

**The Marketplace requirement is a barrier for custom clients.** If you're building your own MCP client, your Slack app must be published to the Marketplace or registered as an internal app. You can't just create a quick app for personal use and connect it. This protects workspaces from rogue integrations, but it slows down developers who want to experiment.

**No SSE support.** The server only supports Streamable HTTP (JSON-RPC 2.0). If your MCP client uses Server-Sent Events for transport — which some earlier MCP clients do — it won't work. Not a dealbreaker for modern clients, but worth knowing if you're working with older tooling.

**Rate limits vary by tool and aren't well-documented in practice.** Some tools are Tier 2 (20+ per minute), others Tier 4 (100+ per minute). In practice, a busy agent doing workspace research can bump into the Tier 2 limits on message search. The error messages don't include retry-after headers, so your client is guessing on backoff timing.

**Message sending is powerful but risky.** An agent with `chat:write` can post to any channel. There's no "draft and confirm" gate in the MCP protocol itself — that depends on your AI client's implementation. If your client auto-approves tool calls, an agent could fire off messages without human review. Use client-side approval prompts for any agent with write access to Slack.

**No reactions, no emoji, no scheduling.** You can read and send messages, but you can't add reactions, set reminders, or schedule messages. For a "full Slack access" integration, these gaps are noticeable. Thread creation works, but only by replying — you can't pin or bookmark messages either.

**Search scope can surprise users.** If you grant `search:read.private` or `search:read.im`, the agent can search your private conversations. The OAuth consent screen explains this, but in the flow of "just click authorize to get it working," people grant broader access than they intend. Be deliberate about which scopes you authorize.

## Compared to Alternatives

**vs. Community Slack MCP server (@modelcontextprotocol/server-slack):** The community server uses a bot token and runs locally. It's simpler to set up for personal use (no Marketplace requirement), but lacks the granular OAuth scopes, natural language responses, and audit logging. Use the official server for team/production use; the community server for quick personal experiments.

**vs. korotovsky/slack-mcp-server:** This third-party server has no permission requirements and supports DMs, group DMs, and GovSlack. It's more permissive and flexible, but that flexibility comes with less security. Good for power users who know what they're doing; the official server is better for teams that need guardrails.

**vs. Slack's native Agentforce/AI integrations:** Slack has been building first-party AI features (agent actions, AI-powered search). The MCP server is for bringing your own AI client — Claude, Cursor, Perplexity — rather than using Slack's built-in AI. They're complementary, not competitive.

## Who Should Use This

**Yes, use it if:**
- Your team lives in Slack and you want your AI agent to search workspace knowledge
- You use a supported MCP client (Claude, Cursor, Perplexity) and want easy setup
- You need an agent to post updates, summaries, or reports to channels
- Workspace security and admin oversight are important to you
- You want to create or update canvases programmatically

**Skip it if:**
- You just need a quick personal Slack bot (use the community server or a bot token)
- Your MCP client doesn't support Streamable HTTP transport
- You need reactions, scheduled messages, or other Slack features beyond search/send/canvases
- You're building a custom client and don't want to deal with Marketplace registration

{{< verdict rating="4" summary="The right way to give agents Slack access" >}}
The Slack MCP server is a solid first-party integration that gets the security model right. Granular OAuth scopes, admin oversight, audit logging, and natural language responses — Slack clearly thought about what "agent access to your workspace" should look like. The gaps are real (no reactions, no scheduling, Marketplace requirement for custom clients), but the core value — searching your workspace and posting messages from an AI agent — works well. If your team uses Slack and you're using a supported AI client, this is a straightforward install that immediately makes your agent more useful.
{{< /verdict >}}
