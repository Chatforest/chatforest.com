# The Slack MCP Server — Your Workspace, Accessible to Agents

> Slack's official MCP server lets AI agents search messages, send replies, and manage canvases in your workspace. Here's the honest review of what works and what doesn't.


Slack is where work conversations happen. The problem is that those conversations are locked inside Slack — an agent can't search your channels, read a thread, or post an update without some kind of integration. Slack's official MCP server changes that. [Generally available since February 17, 2026](https://slack.com/blog/news/mcp-real-time-search-api-now-available), it gives AI agents direct, structured access to your workspace through the Model Context Protocol.

**At a glance:** Hosted at [mcp.slack.com](https://mcp.slack.com/mcp) · ~15 curated tools (+5 added May 13: reactions, create channel, list members, list emoji, read files) · 50+ partner companies building agents · 25x growth in tool invocations since limited release · Streamable HTTP transport · Confidential OAuth 2.0 (PKCE now supported) · [PulseMCP](https://www.pulsemcp.com/servers/slack): ~574K all-time visitors, ~56K weekly, #119 overall rank / #49 weekly rank (live figures as of 2026-08-14 — this tracker updates continuously). Part of our **[Communication & Collaboration MCP category](/categories/communication-collaboration/)**.

This isn't a community wrapper or a bot token hack. It's Slack's own server, hosted at `mcp.slack.com`, using their first-party OAuth. Here's what it's actually like to work with.

## What's New (May 2026 Updates)

**Five new tools added (May 13).** Slack's official changelog added five tools to the MCP server, bringing the documented total to ~15:
- **Add reactions** — adds an emoji reaction to a message on behalf of the authenticated user. This directly addresses one of the most commonly cited limitations of the original server.
- **Create a conversation/channel** — creates a new Slack channel, group DM, or IM.
- **List channel members** — retrieves member user IDs for a channel or conversation.
- **List emoji** — returns the custom emoji available in the workspace.
- **Read files** — retrieves metadata and content of files shared in the workspace (complements the existing `search:read.files` scope).

These additions expand the server's utility meaningfully — particularly reactions (previously absent) and channel creation.

**[PulseMCP](https://www.pulsemcp.com/servers/slack) traffic surged, then kept growing.** As of this May refresh, the official Slack MCP server had reached ~73K all-time visitors (up from ~29.1K at the April refresh) with ~10.2K weekly visitors and a weekly rank of #174 (up from #827 in April). By this audit (2026-08-14), those figures have moved further still — see the current snapshot in "At a glance" above. Treat any single number here as a point-in-time reading; the tracker updates continuously.

**Slackbot Skills announced, rolling out (not yet GA).** [Slack's May 13 Feature Drop post](https://slack.com/intl/en-gb/blog/news/slack-feature-drop-april2026) introduced pre-built reusable AI workflows — Daily Priorities, Meeting Prep, Research Synthesis, and Incident Management — for Business+ and Enterprise plans with AI access. The post's own language is "rolling out over the coming weeks," not a hard GA date; we could not confirm April 29 as a GA date from any Slack source and have corrected the framing here. *(Correction, 2026-08-14: an earlier version of this page stated "Slackbot Skills GA (April 29)" — that date and GA status were not supported by Slack's own announcement.)*

**[Today View in beta (announced May 6)](https://slack.com/blog/news/today-daily-briefing).** An AI-powered daily briefing showing priorities, calendar items, and tasks in a dedicated view. Per Slack's own post, it launched for Enterprise plans (with AI access) only; Business+ and Pro access was slated for "this summer."

**Slackbot MCP Client: went GA June 17, 2026.** *(Update, 2026-08-14: as of the May 18 refresh this was still pending; it has since shipped.)* [Slack announced general availability](https://slack.com/blog/news/slackbots-mcp-client) of Slackbot's MCP client, letting Slackbot connect to and coordinate with outside MCP servers and apps — Slack's post cites 20+ partner apps integrated at launch, a smaller figure than the "6,000+ apps via Salesforce AgentExchange" framing floated at the March 31 announcement.

**[korotovsky/slack-mcp-server](https://github.com/korotovsky/slack-mcp-server) v1.3.0 (May 14).** The leading community alternative shipped a significant release: 6 new tools (`saved_list`, `saved_update`, `saved_clear_completed`, `conversations_join`, `conversations_leave`, `channels_me`), stale-while-revalidate caching for large workspaces, native MCP image content for attachments, rate limiting and retry in SearchContext, and multiple bug fixes. Star count rose to 1,600 (+100), open issues dropped from 43 to 22, open PRs from 40 to 8 — a healthier maintenance posture than the April snapshot.

---

## What's New (April 2026 Updates)

Since our last refresh, Slack's AI platform has seen its most ambitious overhaul since the Salesforce acquisition — reshaping the competitive landscape for the MCP server.

**[Slackbot becomes an agentic desktop agent (March 31).](https://techcrunch.com/2026/03/31/salesforce-announces-an-ai-heavy-makeover-for-slack-with-30-new-features/)** Salesforce unveiled 30+ new AI capabilities for Slackbot, the most sweeping update since the [$27.7B acquisition](https://finance.yahoo.com/news/salesforce-completes-slack-acquisition-132247106.html). Slackbot now functions as an **MCP client** — it can connect to and coordinate with any external service that registers an MCP server through Slack's manifest, including Agentforce and other apps in the Salesforce ecosystem (Slack's own MCP client GA post in June, linked above, cites 20+ partner apps at that point — the "6,000+ apps" figure describes the size of the broader Salesforce AppExchange/AgentExchange catalog it can theoretically reach, not apps already connected). New capabilities include **reusable AI Skills** (define a workflow once, Slackbot learns to run it automatically), **meeting intelligence** (transcribes calls with action item extraction), **desktop agent mode** (monitors screen activity, deals, calendar, and habits to surface suggestions proactively), and a **lightweight CRM** built directly into chat — [confirmed by contemporaneous coverage of the same announcement](https://www.salesforceben.com/salesforce-launches-slack-crm-ending-tab-switching-forever/). All features run on Anthropic's Claude. This is a massive competitive expansion — Slackbot is no longer just a chat assistant, it's an agent platform.

**Slackbot expands to free and Pro plans (April 2026).** A limited version of Slackbot began [rolling out to users on Slack's free and Pro plans starting in April](https://venturebeat.com/orchestration/slack-adds-30-ai-features-to-slackbot-its-most-ambitious-update-since-the), down from the previous Business+/Enterprise+ restriction. [Starting June 15, 2026 ("Summer '26" in Salesforce's release naming), every new Salesforce Enterprise/Unlimited org ships with Slack pre-provisioned](https://www.uctoday.com/unified-communications/salesforce-summer-26-slack-is-now-the-default-for-every-new-customer-heres-what-that-changes/) and AI-enabled from day one.

**[PKCE support GA (March 30).](https://docs.slack.dev/changelog/2026/03/30/pkce/)** OAuth PKCE (Proof Key for Code Exchange) is now generally available for all Slack apps, enabling desktop and mobile clients to authenticate without embedding a `client_secret`. This is a meaningful improvement for custom MCP clients — PKCE-enabled apps are marked as public clients (one-way, irreversible without Slack support). Per Slack's changelog, all refresh tokens expire after 30 days for PKCE-enabled apps, and desktop redirects (custom URI schemes and `localhost` redirects) cannot request bot scopes.

**Enterprise search now indexes GitHub issues (April 2026).** [Slack's enterprise search can now surface GitHub issues alongside messages, files, and email](https://slack.com/help/articles/39044407124755-Set-up-and-manage-Slack-enterprise-search) — up to 5 GitHub organizations connectable. Combined with the existing Gmail/Outlook indexing, MCP-connected agents searching Slack may now surface results from three external systems. We could not confirm the specific April 1 date from a primary source and have widened it to "April 2026." The data governance implications continue to expand.

**[Marketplace agent ecosystem grows.](https://slack.com/blog/news/powering-agentic-collaboration)** Per Slack's own agentic-platform post, the marketplace now includes Claude, Claude Code, Cursor, Guru, Manus, Perplexity, Read AI, Tembo, Spotter, Alysio GTM, Credal AI, Moveworks, WRITER, and others. The ecosystem has moved firmly from "experiment" to "production."

**send_message reliability issues reported.** Multiple users have reported `slack_send_message` failing with MCP error -32603 (Internal Server Error) while `slack_schedule_message` works correctly on the same channel with the same credentials — suggesting a bug specific to the instant send code path. This is tracked in [anthropics/claude-code issue #39892](https://github.com/anthropics/claude-code/issues/39892), opened March 27, 2026 and still open as of this audit. Separately, after a Claude.ai service outage on April 6, all connectors disconnected and the Slack connector failed to automatically reconnect for some users.

### Earlier updates (still relevant)

**[General availability confirmed (Feb 17).](https://slack.com/blog/news/mcp-real-time-search-api-now-available)** Both the MCP server and the Real-Time Search (RTS) API graduated from limited release. Slack reports [MCP tool invocations and RTS query counts both grew 25x](https://slack.com/blog/news/mcp-real-time-search-api-now-available) during the preview period. Over 50 partner companies are now building context-aware agents on the platform, including Anthropic, Google, OpenAI, and Perplexity.

**Interactive message composer in Claude.** The MCP server features a message composer that lets you draft, format, and preview Slack messages directly within Claude — with a live preview of how the message will appear in Slack. Search conversations for context, generate a draft with AI assistance, edit it, and review before sending.

**Expanded OAuth scopes.** The permission model has grown more granular. New scopes include `search:read.files` (file search), `search:read.users` (user search), `canvases:read` (read canvases without write access), and history scopes (`channels:history`, `groups:history`, `mpim:history`, `im:history`) for reading message history. The old single `search:read` scope has been broken into fine-grained `search:read.*` variants.

## What It Does

The Slack MCP server provides approximately 15 curated tools across five categories (out of Slack's 200+ API methods), with five new tools added May 13, 2026:

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
- Add emoji reactions to messages *(new May 13)*
- Create new channels, group DMs, or IMs *(new May 13)*
- List channel members *(new May 13)*

**Files:**
- Read file metadata and content shared in the workspace *(new May 13)*

**Canvases:**
- Create and update rich, formatted documents (Slack's canvas feature)
- Read and export canvases as markdown

**Users & Workspace:**
- Access complete user profiles, including custom fields and status
- List custom emoji available in the workspace *(new May 13)*

Unlike the older community `@modelcontextprotocol/server-slack` npm package (which uses a bot token and talks to Slack's regular API), the official server uses confidential OAuth and is purpose-built for LLM consumption. Tool descriptions are designed for agents, and responses come back as natural language rather than raw JSON.

## Setup

This is where the Slack MCP server diverges from most MCP servers we've reviewed. There's no `npx` command. No local process to run. The server is hosted by Slack.

**For supported clients (Claude.ai, Claude Code, Cursor, Perplexity):** These have built-in integration. In Claude Desktop, you add Slack as a remote MCP server pointing to `https://mcp.slack.com/mcp`. The client handles the OAuth flow — you authorize your Slack workspace, grant the scopes you're comfortable with, and you're connected.

**For custom clients:** You need to register a Slack app at api.slack.com, configure OAuth with the right scopes, and handle the token exchange yourself. As of March 30, PKCE is now GA — desktop and mobile clients can authenticate without embedding a `client_secret`, though enabling PKCE permanently marks your app as a public client. Your app must be published to the Slack Marketplace or registered as an internal app — unlisted apps can't access MCP. **Important:** Dynamic Client Registration (DCR) is still not supported. Your app needs a fixed, pre-registered app ID hardcoded into the client. OpenAI Codex users have reported authentication failures specifically because of this — see [openai/codex issue #13200](https://github.com/openai/codex/issues/13200) if you hit "Dynamic client registration not supported" errors.

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

**Only ~15 tools out of 200+ API methods.** The official server covers a curated subset of Slack's capabilities. The May 13 additions (reactions, channel creation, file reads, member listing, emoji) narrowed the gap noticeably. What's still absent: scheduled messages, reminders, pins, bookmarks. Thread creation still only works by replying. For teams that need deeper Slack automation, coverage remains the biggest frustration — though Slack is clearly expanding the set.

**The Marketplace requirement is a barrier for custom clients.** If you're building your own MCP client, your Slack app must be published to the Marketplace or registered as an internal app. You can't just create a quick app for personal use and connect it. This protects workspaces from rogue integrations, but it slows down developers who want to experiment.

**No SSE or Dynamic Client Registration support.** The server only supports Streamable HTTP (JSON-RPC 2.0). If your MCP client uses Server-Sent Events for transport — which some earlier MCP clients do — it won't work. The lack of DCR has caused real pain for OpenAI Codex users trying to connect. PKCE support (GA March 30) helps desktop/mobile clients authenticate without a `client_secret`, but DCR remains absent.

**send_message has reliability issues.** Multiple users report `slack_send_message` failing with MCP error -32603 (Internal Server Error) while `slack_schedule_message` works correctly on the same channel with the same credentials — see [anthropics/claude-code issue #39892](https://github.com/anthropics/claude-code/issues/39892), open since March 27, 2026 and still unresolved as of this audit (2026-08-14). This suggests a bug in the instant send code path. Separately, after a Claude.ai outage on April 6, the Slack connector failed to reconnect automatically for some users, requiring manual re-authorization.

**Rate limits vary by tool and aren't well-documented in practice.** Some tools are Tier 2 (20+ per minute), others Tier 4 (100+ per minute). Search and messaging have "special" rate limits that require checking individual method pages. In practice, a busy agent doing workspace research can bump into the Tier 2 limits on message search. The error messages don't include retry-after headers, so your client is guessing on backoff timing.

**Enterprise search now crosses three external systems.** With Gmail, Outlook, and now GitHub Issues indexing (up to 5 organizations, added April 2026), a search query through the MCP server may surface results from email and code tracking systems. This is powerful but expands the blast radius of a `search:read` scope grant in ways users may not expect. If your organization has enabled cross-system search, review what data sources agents can reach.

**Search scope can surprise users.** If you grant `search:read.private` or `search:read.im`, the agent can search your private conversations. The OAuth consent screen explains this, but in the flow of "just click authorize to get it working," people grant broader access than they intend. Be deliberate about which scopes you authorize.

## Compared to Alternatives

**vs. [korotovsky/slack-mcp-server](https://github.com/korotovsky/slack-mcp-server) (1.8k stars, 354 forks, 29 open issues, 29 open PRs as of 2026-08-14 — GitHub stats change continuously, so treat these as a snapshot):** The most popular community alternative; its README currently claims 30,000+ monthly engineer visitors and 9,000+ active users. Written in Go, supports Stdio, SSE, and HTTP transports. No Marketplace requirement, no permission restrictions, supports DMs, group DMs, GovSlack, and user group management. Has an optional "stealth mode" without app installation. [v1.3.0 (released May 14, 2026)](https://github.com/korotovsky/slack-mcp-server/releases) added 6 new tools (`saved_list`, `saved_update`, `saved_clear_completed`, `conversations_join`, `conversations_leave`, `channels_me`), stale-while-revalidate caching, native image content, and rate-limiting improvements. The downside: raw bot tokens in environment variables, no token refresh, community maintenance only. Good for power users; the official server is better for teams that need guardrails.

**vs. Community Slack MCP server (@modelcontextprotocol/server-slack):** The original reference implementation, now showing its age. Uses a bot token and runs locally. Simpler to set up for personal use (no Marketplace requirement), but lacks the granular OAuth scopes, natural language responses, and audit logging. The official server has clearly surpassed it for production use.

**vs. Slackbot (now available on all plans):** Massively upgraded in March 2026 with 30+ new AI capabilities. Slackbot is now an **MCP client** ([GA June 17, 2026](https://slack.com/blog/news/slackbots-mcp-client), citing 20+ partner apps integrated at launch — a smaller number than the 6,000+ AgentExchange-catalog figure floated at the March announcement), a **desktop agent** that monitors screen activity and proactively surfaces suggestions, and has **reusable AI Skills**, **meeting intelligence** (transcription + action items), and a **lightweight CRM** built into chat. All powered by Anthropic's Claude. A limited version is now available on free and Pro plans (previously Business+/Enterprise+ only). The relationship between Slackbot and the MCP server has shifted: Slackbot is now both a competitor (it provides AI-in-Slack without needing external clients) and a complement (as an MCP client, it can coordinate with MCP servers). If you want a full agentic assistant inside Slack, Slackbot is increasingly the answer. The MCP server's differentiation is now primarily about bringing *your choice* of external AI client to Slack data.

**vs. [Truto Managed MCP](https://truto.one/blog/connect-slack-to-claude-manage-channels-threads-and-users/):** A third-party managed service that dynamically generates tools from Slack's full API documentation (not just the curated 15), per Truto's own description of its approach. Includes automatic token refresh, method-level filtering, and expiring access URLs. The trade-off is routing your data through an external service — not suitable for strict data sovereignty requirements.

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

{{< verdict rating="4" summary="Five new tools in May signals momentum, but Slackbot and the community alternative are both closing in" >}}
The Slack MCP server is showing clearer investment signals through 2026. Five new tools (reactions, channel creation, file reads, member listing, custom emoji) landed May 13, addressing some of the longest-standing gaps, and PulseMCP traffic has grown substantially since — see the current snapshot in "At a glance" above. But the structural constraints remain: ~15 tools out of 200+ API methods, no DCR, the Marketplace registration requirement, and an unresolved `send_message` reliability bug (-32603 error, [tracked in issue #39892](https://github.com/anthropics/claude-code/issues/39892), no confirmed fix as of this audit). Slackbot continues its own expansion — Skills (rolling out), Today View (beta), and an MCP client capability that [reached GA June 17, 2026](https://slack.com/blog/news/slackbots-mcp-client) — narrowing the "use an external AI client to access Slack" value proposition further. On the community side, korotovsky's server remains actively maintained with strong GitHub and PulseMCP traction. The official server is still the right choice for teams prioritizing security, audit logging, and OAuth-first architecture. But Slack needs to keep expanding the tool set or the ceiling will feel increasingly arbitrary. Rating holds at 4/5 — the direction is better than it was, and the 2026 additions count for something.
{{< /verdict >}}

*Disclosure: This review is based on publicly available documentation, GitHub repositories, developer forums, and Slack's official announcements. ChatForest does not test MCP servers hands-on. We research, analyze, and present what we find so you can make informed decisions. Review written and edited using Claude Sonnet 4.6 (Anthropic). Last substantively updated 2026-08-14.*

---

**Sources:** [Slack MCP server (mcp.slack.com)](https://mcp.slack.com/mcp) · [Slack API documentation (api.slack.com)](https://api.slack.com/) · [Slack MCP/RTS GA announcement](https://slack.com/blog/news/mcp-real-time-search-api-now-available) · [Slack May 13 Feature Drop](https://slack.com/intl/en-gb/blog/news/slack-feature-drop-april2026) · [Slackbot MCP client GA announcement](https://slack.com/blog/news/slackbots-mcp-client) · [Today briefing announcement](https://slack.com/blog/news/today-daily-briefing) · [PKCE GA changelog](https://docs.slack.dev/changelog/2026/03/30/pkce/) · [korotovsky/slack-mcp-server community alternative (GitHub)](https://github.com/korotovsky/slack-mcp-server) · [PulseMCP: Slack](https://www.pulsemcp.com/servers/slack) · [anthropics/claude-code #39892 (send_message bug)](https://github.com/anthropics/claude-code/issues/39892) · [openai/codex #13200 (DCR auth failure)](https://github.com/openai/codex/issues/13200)

