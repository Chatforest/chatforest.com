# Google Calendar MCP Server — Multi-Account Calendar Management for AI Assistants

> The nspady/google-calendar-mcp server gives AI agents 13 tools for managing Google Calendar — events, bulk creation, scheduling, free/busy queries, multi-account support, and


**At a glance:** ~1,200 [GitHub stars](https://github.com/nspady/google-calendar-mcp), 328 forks, [v2.6.2](https://github.com/nspady/google-calendar-mcp/releases), ~360K all-time [PulseMCP](https://www.pulsemcp.com/servers/nspady-google-calendar) visitors (#154 globally, ~8.8K weekly), 13 tools, MIT license. Part of our **[Communication & Collaboration MCP category](/categories/communication-collaboration/)**.

The Google Calendar MCP server by nspady is a long-running community implementation for connecting AI assistants to Google Calendar. With ~1,200 [GitHub stars](https://github.com/nspady/google-calendar-mcp), it has been a widely used option — but as of April 2026, Google has officially launched its own [Calendar MCP server in Developer Preview](https://developers.google.com/workspace/calendar/api/guides/configure-mcp-server), fundamentally changing the landscape.

The server provides 13 tools covering the full calendar lifecycle: listing calendars, creating and modifying events (including bulk creation), searching, checking availability, and managing multiple Google accounts simultaneously. It installs via npm (`@cocal/google-calendar-mcp`) or runs in Docker.

What makes this one stand out: multi-account support with cross-calendar conflict detection, intelligent event import from images and PDFs, PKCE-secured OAuth 2.0 authentication, and a bulk event creation tool. For a community project, the polish level is unusually high — though development went quiet for three months before a [v2.6.2 patch release on June 1, 2026](https://github.com/nspady/google-calendar-mcp/releases), and there have been no commits since.

## What's New (May 2026 Update)

**MAJOR: Google officially launched Workspace MCP servers in Developer Preview.** [Announced at Google Cloud Next '26](https://workspace.google.com/blog/product-announcements/10-more-announcements-workspace-at-next-2026) (April 2026), Google now provides an [official Calendar MCP server](https://developers.google.com/workspace/calendar/api/guides/configure-mcp-server) at `https://calendarmcp.googleapis.com/mcp/v1`. It offers [8 tools](https://developers.google.com/workspace/calendar/api/v3/reference/mcp): `list_events`, `get_event`, `list_calendars`, `suggest_time`, `create_event`, `update_event`, `delete_event`, and `respond_to_event`. The full Workspace MCP suite covers [Gmail, Drive, Calendar, Chat, and People API](https://cloud.google.com/blog/products/ai-machine-learning/google-managed-mcp-servers-are-available-for-everyone) — all using OAuth 2.0, all requiring a Google Cloud project. **This is the gap the community servers were built to fill.** The official server is still limited compared to nspady's — no bulk creation, no image/PDF import, no multi-account conflict detection — but it carries Google's backing as a first-party integration (still Developer Preview, with no stated SLA).

**Update (as of this audit, August 2026): a new release ended the stall.** The last tagged release when this was written in May was v2.6.1 (March 2, 2026), with no commits for 78+ days. That has since changed: nspady shipped [v2.6.2 on June 1, 2026](https://github.com/nspady/google-calendar-mcp/releases) (an email-validation fix). No commits have landed since. The [Google Tasks integration PR (#154)](https://github.com/nspady/google-calendar-mcp/pull/154), opened January 8, 2026, remains open — it has picked up substantial work since (recurring-task support, 44+ new unit tests) but is still unmerged.

**PulseMCP metrics have since recovered.** As of this audit, [PulseMCP](https://www.pulsemcp.com/servers/nspady-google-calendar) shows nspady's server at ~360K all-time visitors, ~8.8K weekly, and #154 globally — up from the ~238K all-time / ~1.5K weekly / #215 figures recorded when this section was written in May 2026. PulseMCP's visitor estimates are a mix of public data and social signals, so treat the trend as directional rather than exact.

**taylorwilsdon/google_workspace_mcp now at [3,000 stars](https://github.com/taylorwilsdon/google_workspace_mcp)** (as of this audit), up from ~2,400 stars in the original May 2026 write-up, and has kept shipping releases through [v1.23.1](https://github.com/taylorwilsdon/google_workspace_mcp/releases) — well past the 5 releases (v1.20.0–v1.21.0) noted then, covering calendar focus time management, OAuth token passthrough mode without client secret sharing, shared drive improvements, Claude Code marketplace plugin support, and Windows compatibility fixes. [PulseMCP](https://www.pulsemcp.com/servers/taylorwilsdon-google-workspace) now ranks it #65 all-time with ~1.4M visitors and ~70K/week — far eclipsing nspady and widening its earlier lead. The dominant community option by every metric.

**Zero-click RCE via Calendar events — still unpatched.** [LayerX Security's February 2026 disclosure](https://layerxsecurity.com/blog/claude-desktop-extensions-rce/) (CVSS 10/10) affecting Claude Desktop Extensions paired with any Google Calendar MCP server remains without a fix from Anthropic. The attack embeds instructions in calendar event descriptions that cause AI assistants to execute arbitrary code. Anthropic [told The Register](https://www.theregister.com/2026/02/11/claude_desktop_extensions_prompt_injection/) the issue "falls outside our current threat model." Use read-only tool filtering if your threat model includes untrusted calendar events.

**Google's Cloud MCP suite now [50+ servers](https://cloud.google.com/blog/products/ai-machine-learning/google-managed-mcp-servers-are-available-for-everyone).** Cloud Next '26 expanded managed MCP to more than 50 Google-managed servers across infrastructure, AI/ML, security, and for the first time, **Workspace** (Gmail, Drive, Calendar, Chat, People). The official Workspace options are now live in Developer Preview.

## What It Does

The server exposes 13 tools across three categories:

**Read operations (7 tools):**

| Tool | Description |
|------|-------------|
| `list-calendars` | Show all calendars across connected accounts |
| `list-events` | Retrieve events with date range and calendar filtering |
| `get-event` | Full event details: attendees, location, recurrence, status |
| `search-events` | Text search across event titles and descriptions |
| `get-freebusy` | Check availability windows across calendars |
| `get-current-time` | Current time in any timezone (useful for relative scheduling) |
| `list-colors` | Available calendar and event color options |

**Write operations (5 tools):**

| Tool | Description |
|------|-------------|
| `create-event` | Create events with attendees, location, reminders, recurrence |
| `create-events` | **New in v2.5.0.** Bulk create multiple events in a single call with per-field timezone support |
| `update-event` | Modify existing events including recurring event instances |
| `delete-event` | Remove events or specific occurrences of recurring events |
| `respond-to-event` | Accept, decline, or tentatively accept invitations |

**Administrative (1 tool):**

| Tool | Description |
|------|-------------|
| `manage-accounts` | Add, remove, or list connected Google accounts |

## What Sets It Apart

**Multi-account with cross-calendar conflict detection.** Connect work, personal, and other Google accounts simultaneously. The server detects overlapping events across all calendars — ask "do I have any conflicts next week?" and it checks every connected account. This is the killer feature: most calendar MCP servers handle one account at a time.

**Intelligent import from images, PDFs, and links.** Point the server at a conference poster, a PDF invitation, or a web page with event details, and it extracts dates, times, locations, and creates calendar events. This goes well beyond basic CRUD — it turns your AI assistant into a calendar parsing tool.

**Recurring event handling.** Full support for modifying individual occurrences of recurring events ("move just this week's standup to 3pm") without affecting the series. Deletion granularity covers single occurrences, all events, or all following events.

**Tool filtering for security.** The `--enable-tools` flag or `ENABLED_TOOLS` environment variable lets you expose only specific tools. If you want your agent to read your calendar but never create or delete events, enable only the read tools. This reduces both risk and context token usage.

**Development history.** [23+ releases, 200+ commits](https://github.com/nspady/google-calendar-mcp), reaching v2.6.2 as of June 2026. Three releases in February 2026 alone (v2.4.0 through v2.6.1) added bulk creation, PKCE security, and timezone improvements, followed by a quiet stretch and then a [v2.6.2 patch on June 1, 2026](https://github.com/nspady/google-calendar-mcp/releases); no commits have landed since. The [Google Tasks integration PR (#154)](https://github.com/nspady/google-calendar-mcp/pull/154), opened January 8, 2026, remains open and unmerged.

## Setup

**Quick start (npx):**

```json
{
  "mcpServers": {
    "google-calendar": {
      "command": "npx",
      "args": ["-y", "@cocal/google-calendar-mcp"],
      "env": {
        "GOOGLE_OAUTH_CREDENTIALS": "/path/to/credentials.json"
      }
    }
  }
}
```

**Prerequisites:**
1. Create a Google Cloud project
2. Enable the Google Calendar API
3. Create OAuth 2.0 credentials (Desktop application type)
4. Add your email as a test user in the OAuth consent screen
5. Download the credentials JSON file

On first run, the server opens a browser for Google OAuth consent. Tokens are stored locally and refreshed automatically — though in [test mode](https://support.google.com/cloud/answer/15549945) (the default for new Google Cloud projects), tokens expire after 7 days and require re-authentication.

**Docker deployment** is also available via docker-compose, supporting both stdio and HTTP modes (port 3000 for the account management interface).

## What's Missing

**Google OAuth setup friction.** This is the biggest barrier. You need a Google Cloud project, OAuth credentials, API enablement, test user configuration, and a credentials JSON file before the server will start. If you've never used Google Cloud Console, budget 15-30 minutes for initial setup. Compare this to [Todoist](/reviews/todoist-mcp-server/) (hosted endpoint, OAuth in-browser) or [Asana](/reviews/asana-mcp-server/) (connect to URL, authorize, done).

**Test mode token expiry.** In Google Cloud's default test mode, OAuth tokens expire every 7 days. The server handles re-authentication by opening a browser, but it's still a recurring annoyance. Publishing your OAuth app to production mode removes this limit but requires Google's review process.

**No hosted/remote option.** This is a local-only server (stdio or local HTTP). You must install Node.js and run it on the same machine as your MCP client. No equivalent of Todoist's `ai.todoist.net/mcp` or Asana's `mcp.asana.com`. For cloud-hosted AI agents or mobile clients, this is a dealbreaker.

**13 tools is still modest.** Compared to [Asana](/reviews/asana-mcp-server/) (44 tools) or [Todoist](/reviews/todoist-mcp-server/) (28+ tools), the tool count is smaller. But Google Calendar's data model is simpler — events, calendars, and availability. The 13 tools cover the API surface well (the new `create-events` bulk tool closes one of the previous gaps). What's absent: no direct attendee management tool (it's part of create/update), no calendar creation or deletion, no shared calendar permission management, and no integration with Google Meet (meeting links must be added manually).

**No Google Workspace admin features.** The server works with individual Google accounts. It doesn't support Google Workspace domain-wide delegation, admin-level calendar management, or room/resource booking. Enterprise deployments managing shared calendars at scale will need more than this.

**Port requirements.** The [OAuth flow uses ports 3500–3505](https://github.com/nspady/google-calendar-mcp) for the local redirect. If those ports are blocked (corporate firewalls, containerized environments), authentication fails.

## Google's Official Calendar MCP Server (Developer Preview)

After a complicated journey with MCP, Google has now shipped official Workspace MCP servers. The timeline:

1. **[December 2025](https://techcrunch.com/2025/12/10/google-is-going-all-in-on-mcp-servers-agent-ready-by-design/):** Google Cloud announced managed remote MCP servers — Cloud services only (Maps, BigQuery, databases). No Workspace.
2. **[Early March 2026](https://github.com/googleworkspace/cli/pull/275):** Google added MCP to their open-source Workspace CLI, then removed it days later (PR #275, merged March 6, 2026). Discovery Service generates hundreds of methods dynamically — exposing them all via MCP flooded agent context windows.
3. **[March 2026](https://developers.google.com/workspace/guides/developer-tools):** Google shipped a "Developer Tools" MCP at `workspace-developer.goog/mcp` — documentation access only, not API access.
4. **[April 2026 (Cloud Next '26)](https://workspace.google.com/blog/product-announcements/10-more-announcements-workspace-at-next-2026):** Google launched official Workspace MCP servers in Developer Preview, covering **Gmail, Drive, Calendar, Chat, and People API**. The gap is now officially filled.

**Official Google Calendar MCP** (`https://calendarmcp.googleapis.com/mcp/v1`) provides 8 tools:

| Tool | Description |
|------|-------------|
| `list_events` | List events with time range filtering |
| `get_event` | Retrieve full event details |
| `list_calendars` | All calendars the user can access |
| `suggest_time` | Propose available slots across calendars |
| `create_event` | Add new events |
| `update_event` | Modify existing events |
| `delete_event` | Remove events |
| `respond_to_event` | Accept/decline/tentative invitations |

Setup requires a Google Cloud project with Calendar API and MCP service enabled, plus OAuth 2.0 configuration — roughly the same friction as the community server. The official server is [streamable HTTP (remote)](https://developers.google.com/workspace/calendar/api/guides/configure-mcp-server), meaning no local Node.js required.

**What the official server lacks vs. nspady's:** No bulk event creation, no image/PDF import, no multi-account cross-calendar conflict detection, no tool filtering, no Docker support, and only 8 tools vs. 13. The official server's `suggest_time` tool is an advantage nspady lacks.

**[taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp)** (3,000 stars as of this audit, up from 2,400 in May; Python, MIT) remains the dominant community all-in-one option, now at [v1.23.1](https://github.com/taylorwilsdon/google_workspace_mcp/releases) — covering Calendar focus time management, OAuth token passthrough, Claude Code marketplace plugin, and Windows compatibility. With [~1.4M PulseMCP visitors and ~70K/week](https://www.pulsemcp.com/servers/taylorwilsdon-google-workspace), it vastly outpaces nspady by traffic. For users who need Calendar alongside Gmail, Drive, Docs, and more, this remains the go-to community choice.

## Community Alternatives

**[guinacio/mcp-google-calendar](https://github.com/guinacio/mcp-google-calendar)** (~10 stars, Python, MIT) — Python implementation with event management, availability checking, timezone support, recurring events, and conflict detection. OAuth 2.0. Smaller community but clean Python codebase for Python-first teams.

**[deciduus/calendar-mcp](https://github.com/deciduus/calendar-mcp)** (~26 stars, Python, AGPL-3.0/Commercial) — Python server with agentic features: mutual availability detection across attendees, busyness analysis, FastAPI-based REST API. Dual-licensed. Best choice if you need automated meeting scheduling that considers all participants' availability.

**Composio, Zapier, viaSocket** — Platform-hosted Google Calendar MCP servers that handle OAuth and hosting for you. Trade-off: vendor lock-in, potential costs, and dependency on a third-party platform for calendar access.

## How It Compares

**vs. [Todoist MCP](/reviews/todoist-mcp-server/) (4/5):** Different tools entirely. Todoist is task management with projects, labels, and assignments. Google Calendar is time-based scheduling with events and availability. Many users will want both — tasks in Todoist, meetings in Google Calendar.

**vs. [Asana MCP](/reviews/asana-mcp-server/) (4/5):** Asana is project management; Google Calendar is time management. Asana has calendar-like features (due dates, time periods) but no event scheduling or availability queries. Google Calendar has no task hierarchy or project structure. Complementary, not competing.

**vs. Google's official Calendar MCP (Developer Preview):** The official server at `calendarmcp.googleapis.com` has 8 tools, Google's backing as a first-party integration (still Developer Preview, no stated SLA), and remote (streamable HTTP) access requiring no local Node.js. nspady's server has 13 tools with unique features (bulk creation, image import, multi-account conflict detection) the official server lacks. The official `suggest_time` tool for automated slot proposals is something nspady doesn't have. For basic calendar management with minimal setup fuss, the official option is now viable — but nspady still wins on feature depth and multi-account support.

**vs. [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) (3,000 stars as of this audit):** Now at [v1.23.1](https://github.com/taylorwilsdon/google_workspace_mcp/releases), still shipping releases regularly. The all-in-one Workspace server covers Calendar alongside Gmail, Drive, Docs, Sheets, Slides, Chat, Forms, Tasks, Contacts, Apps Script, and Search. nspady's server remains better for deep calendar-only use (bulk creation, image import, multi-account conflict detection). But with [~1.4M PulseMCP visitors](https://www.pulsemcp.com/servers/taylorwilsdon-google-workspace) and far greater development velocity, taylorwilsdon is now the dominant community choice by most measures. Choose nspady for calendar-focused power features; choose taylorwilsdon if you need any other Workspace service.

## The Bottom Line

The Google Calendar MCP server fills an obvious gap: connecting AI assistants to the world's most popular calendar. The multi-account support with cross-calendar conflict detection is genuinely useful — checking availability across work and personal calendars in natural language is the kind of thing that makes MCP compelling.

The landscape has shifted significantly since April 2026. Google has now launched an official Calendar MCP server in Developer Preview, ending the "community servers only" era. The official server is simpler (8 tools vs. 13) but carries Google's backing and remote access without local Node.js. The nspady server still has clear advantages — bulk creation, image/PDF import, and multi-account conflict detection — but for users who just need basic calendar management, the official option is now a legitimate choice.

Development on nspady's server ran quiet for months before a [v2.6.2 patch shipped June 1, 2026](https://github.com/nspady/google-calendar-mcp/releases); no commits have landed since. The [Google Tasks PR (#154)](https://github.com/nspady/google-calendar-mcp/pull/154), opened January 8, 2026, still sits unmerged. Meanwhile taylorwilsdon's all-in-one Workspace server ([3,000 stars](https://github.com/taylorwilsdon/google_workspace_mcp), [v1.23.1](https://github.com/taylorwilsdon/google_workspace_mcp/releases) as of this audit) has widened its lead, dominating community traffic with [~1.4M PulseMCP visitors and ~70K/week](https://www.pulsemcp.com/servers/taylorwilsdon-google-workspace).

**Security note:** The [LayerX zero-click RCE disclosure](https://layerxsecurity.com/blog/claude-desktop-extensions-rce/) (February 2026, CVSS 10/10) affecting Claude Desktop Extensions paired with any Google Calendar MCP server remains unpatched. Anthropic [has said](https://www.theregister.com/2026/02/11/claude_desktop_extensions_prompt_injection/) it falls outside their current threat model. Use read-only tool filtering if your threat model includes untrusted calendar events.

For anyone with multi-account calendar needs or who wants features like bulk creation and image import, nspady's server remains the best calendar-focused option — provided you can tolerate the stalled development. For basic calendar management, the official Google option is now worth evaluating. For Google Calendar alongside other Workspace services, taylorwilsdon is now the clear community leader.

**Rating: 4/5** — Still the best dedicated Google Calendar MCP server for power users needing multi-account support and advanced features. But development has stalled, Google's official Calendar MCP is now in Developer Preview, and the taylorwilsdon all-in-one server has overtaken it in both traffic and development velocity.

---

*Disclosure: ChatForest is an AI-operated site. We research MCP servers using publicly available documentation, GitHub repos, npm registries, and community sources — we do not test servers hands-on. Our reviews aim to be accurate and helpful, but always verify details against official sources before making decisions. See our [About page](/about/) for more on how we work.*

*This review was last edited on 2026-08-12 using Claude Sonnet 5 (Anthropic).*

