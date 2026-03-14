---
title: "Google Calendar MCP Server — Multi-Account Calendar Management for AI Assistants"
date: 2026-03-14T22:30:00+09:00
description: "The nspady/google-calendar-mcp server gives AI agents 12 tools for managing Google Calendar — events, scheduling, free/busy queries, multi-account support, and intelligent import from images. Here's the honest review."
og_description: "Google Calendar MCP server: 12 tools for events, scheduling, and availability across multiple Google accounts. OAuth 2.0, npm package, multi-account support. Rating: 4/5."
content_type: "Review"
card_description: "Community-built MCP server for Google Calendar management. 12 tools covering events, scheduling, availability, and multi-account operations. OAuth 2.0, npm package, Docker support."
---

The Google Calendar MCP server by nspady is the leading community implementation for connecting AI assistants to Google Calendar. With 1,000+ GitHub stars and active development (v2.6.1 as of March 2026), it's become the de facto standard — there is no official Google Calendar MCP server, despite Google briefly shipping and then removing MCP support from their Workspace CLI in early March 2026.

The server provides 12 tools covering the full calendar lifecycle: listing calendars, creating and modifying events, searching, checking availability, and managing multiple Google accounts simultaneously. It installs via npm (`@cocal/google-calendar-mcp`) or runs in Docker.

What makes this one stand out: multi-account support with cross-calendar conflict detection, intelligent event import from images and PDFs, and proper OAuth 2.0 authentication. For a community project, the polish level is unusually high.

## What It Does

The server exposes 12 tools across three categories:

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

**Write operations (4 tools):**

| Tool | Description |
|------|-------------|
| `create-event` | Create events with attendees, location, reminders, recurrence |
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

**Active development pace.** 23 releases, 196 commits, v2.6.1 as of March 2026. The maintainer responds to issues and ships fixes regularly. For a community project, this is exceptional longevity.

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

On first run, the server opens a browser for Google OAuth consent. Tokens are stored locally and refreshed automatically — though in test mode (the default for new Google Cloud projects), tokens expire after 7 days and require re-authentication.

**Docker deployment** is also available via docker-compose, supporting both stdio and HTTP modes (port 3000 for the account management interface).

## What's Missing

**Google OAuth setup friction.** This is the biggest barrier. You need a Google Cloud project, OAuth credentials, API enablement, test user configuration, and a credentials JSON file before the server will start. If you've never used Google Cloud Console, budget 15-30 minutes for initial setup. Compare this to [Todoist](/reviews/todoist-mcp-server/) (hosted endpoint, OAuth in-browser) or [Asana](/reviews/asana-mcp-server/) (connect to URL, authorize, done).

**Test mode token expiry.** In Google Cloud's default test mode, OAuth tokens expire every 7 days. The server handles re-authentication by opening a browser, but it's still a recurring annoyance. Publishing your OAuth app to production mode removes this limit but requires Google's review process.

**No hosted/remote option.** This is a local-only server (stdio or local HTTP). You must install Node.js and run it on the same machine as your MCP client. No equivalent of Todoist's `ai.todoist.net/mcp` or Asana's `mcp.asana.com`. For cloud-hosted AI agents or mobile clients, this is a dealbreaker.

**12 tools is modest.** Compared to [Asana](/reviews/asana-mcp-server/) (44 tools) or [Todoist](/reviews/todoist-mcp-server/) (28+ tools), the tool count is smaller. But Google Calendar's data model is simpler — events, calendars, and availability. The 12 tools cover the API surface well. What's absent: no direct attendee management tool (it's part of create/update), no calendar creation or deletion, no shared calendar permission management, and no integration with Google Meet (meeting links must be added manually).

**No Google Workspace admin features.** The server works with individual Google accounts. It doesn't support Google Workspace domain-wide delegation, admin-level calendar management, or room/resource booking. Enterprise deployments managing shared calendars at scale will need more than this.

**Port requirements.** The OAuth flow uses ports 3500-3505 for the local redirect. If those ports are blocked (corporate firewalls, containerized environments), authentication fails. A `USE_MANUAL_AUTH=true` fallback exists for environments where localhost isn't accessible.

## No Official Google MCP Server (Yet)

Google's relationship with MCP is complicated. In early March 2026, Google released an open-source Workspace CLI (`@googleworkspace/cli`) that included a built-in MCP server covering Drive, Gmail, Calendar, Docs, and Sheets. Two days later, they deleted all 1,151 lines of MCP code in a breaking change, pivoting to CLI-based integration with structured JSON output instead.

This leaves the community implementations as the only option for Google Calendar MCP integration. The nspady server has emerged as the clear leader — 1,000+ stars, active maintenance, comprehensive features. But it means there's no guarantee of long-term API stability that comes with an official first-party server.

**taylorwilsdon/google_workspace_mcp** (1,800 stars, Python, MIT) covers Gmail, Drive, Calendar, Docs, Sheets, Slides, Forms, Tasks, Contacts, and Chat in a single server. If you need Google Calendar alongside other Workspace services, this all-in-one option may be more practical than running separate MCP servers.

## Community Alternatives

**guinacio/mcp-google-calendar** (9 stars, Python, MIT) — Python implementation with event management, availability checking, timezone support, recurring events, and conflict detection. OAuth 2.0. Smaller community but clean Python codebase for Python-first teams.

**deciduus/calendar-mcp** (25 stars, Python, AGPL-3.0/Commercial) — Python server with agentic features: mutual availability detection across attendees, busyness analysis, FastAPI-based REST API. Dual-licensed. Best choice if you need automated meeting scheduling that considers all participants' availability.

**Composio, Zapier, viaSocket** — Platform-hosted Google Calendar MCP servers that handle OAuth and hosting for you. Trade-off: vendor lock-in, potential costs, and dependency on a third-party platform for calendar access.

## How It Compares

**vs. [Todoist MCP](/reviews/todoist-mcp-server/) (4/5):** Different tools entirely. Todoist is task management with projects, labels, and assignments. Google Calendar is time-based scheduling with events and availability. Many users will want both — tasks in Todoist, meetings in Google Calendar.

**vs. [Asana MCP](/reviews/asana-mcp-server/) (4/5):** Asana is project management; Google Calendar is time management. Asana has calendar-like features (due dates, time periods) but no event scheduling or availability queries. Google Calendar has no task hierarchy or project structure. Complementary, not competing.

**vs. taylorwilsdon/google_workspace_mcp:** The all-in-one Workspace server covers Calendar alongside Gmail, Drive, Docs, and more — but the calendar tools may be less specialized. nspady's server is calendar-focused with features like image import and multi-account that the broader server may lack. Choose based on whether you need just Calendar or the full Workspace suite.

## The Bottom Line

The Google Calendar MCP server fills an obvious gap: connecting AI assistants to the world's most popular calendar. The multi-account support with cross-calendar conflict detection is genuinely useful — checking availability across work and personal calendars in natural language is the kind of thing that makes MCP compelling.

The OAuth setup friction is real but one-time. Once configured, the server is reliable and actively maintained. The 12-tool set covers the Google Calendar API surface well, and features like image-based event import go beyond what you'd expect from a community project.

The absence of an official Google MCP server means this community implementation carries the ecosystem. At 1,000+ stars with 23 releases, it has the community validation to justify that trust. But it also means no guaranteed long-term support — you're dependent on a community maintainer, not a Google SLA.

For anyone using Google Calendar who wants their AI assistant to manage scheduling, check availability, and handle events across accounts, this is the server to use. The setup tax is the price of Google's OAuth requirements, not a limitation of the server itself.

**Rating: 4/5** — The best Google Calendar MCP server available, with multi-account support and active maintenance. OAuth setup complexity and the lack of an official Google server keep it from 4.5.

---
