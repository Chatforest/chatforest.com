# Google Calendar MCP Server — Multi-Account Calendar Management for AI Assistants

> The nspady/google-calendar-mcp server gives AI agents 13 tools for managing Google Calendar — events, bulk creation, scheduling, free/busy queries, multi-account support, and


**At a glance:** 1,100+ GitHub stars, 313 forks, v2.6.1, ~216K all-time PulseMCP visitors (#185 globally, ~2.7K weekly), npm ~11.3K weekly downloads, 13 tools, MIT license. Part of our **[Communication & Collaboration MCP category](/categories/communication-collaboration/)**.

The Google Calendar MCP server by nspady is the leading community implementation for connecting AI assistants to Google Calendar. With 1,100+ GitHub stars and active development (v2.6.1 as of March 2026), it's become the de facto standard — there is no official Google Calendar MCP server, despite Google briefly shipping and then removing MCP support from their Workspace CLI in early March 2026.

The server now provides 13 tools covering the full calendar lifecycle: listing calendars, creating and modifying events (including bulk creation), searching, checking availability, and managing multiple Google accounts simultaneously. It installs via npm (`@cocal/google-calendar-mcp`) or runs in Docker.

What makes this one stand out: multi-account support with cross-calendar conflict detection, intelligent event import from images and PDFs, PKCE-secured OAuth 2.0 authentication, and a new bulk event creation tool. For a community project, the polish level is unusually high.

## What's New (April 2026 Update)

**MCP spec compliance update (March 30).** Tool annotations with descriptive titles, prompt and resource callback support, migration from legacy tool registration to `registerTool()`, proper idempotency hints for update and event-response operations, and improved error handling in resource callbacks. Not a new version release, but a significant commit improving MCP protocol alignment.

**Google Tasks integration in progress (PR #154).** The maintainer (nspady) has an open PR since January 8 to add Google Tasks integration — the first scope expansion beyond Calendar. Still in progress with 3 tasks completed.

**Zero-click RCE via Calendar events disclosed (February 2026).** LayerX Security discovered a zero-click remote code execution vulnerability (CVSS 10/10) affecting Claude Desktop Extensions paired with Google Calendar MCP servers. An attacker can embed instructions in a Google Calendar event description that, when read by an AI assistant, causes it to download and execute arbitrary code — no user confirmation required. The attack chains a low-risk data source (calendar) to a high-risk local executor (DXT) without security boundaries. Anthropic declined to fix, stating it "falls outside our current threat model." This affects **any** Google Calendar MCP server used with Claude Desktop Extensions, not just nspady's. Tool filtering (`--enable-tools` with read-only tools) mitigates the write/execute side, but the prompt injection vector through event descriptions remains exploitable.

**Still v2.6.1 — 48 days without a release.** The last tagged release was March 2, 2026. Two commits have landed since (documentation fix March 15, MCP compliance update March 30), but no new npm publish. Development pace has slowed from the burst of three releases in February.

**npm downloads surging.** Weekly downloads jumped to ~11.3K/week (~58.6K/month) — strong adoption growth even without new releases.

**Google's managed MCP now covers 30+ services — still no Calendar.** Google expanded its fully-managed remote MCP servers to include databases (AlloyDB, Spanner, Cloud SQL, Firestore, Bigtable), monitoring (Cloud Logging, Trace, Monitoring), and more. After March 17, 2026, MCP servers are automatically enabled when you enable a supported service. But **Google Calendar, Gmail, and all Workspace apps remain excluded**. The community server gap persists.

**taylorwilsdon/google_workspace_mcp exploded to 2,100 stars.** Up from 696 stars in March — a 3× increase. Now covers 12 Google services (Calendar, Gmail, Drive, Docs, Sheets, Slides, Chat, Forms, Tasks, Contacts, Apps Script, Search) with OAuth 2.1 multi-user support and one-click Claude Desktop installation via DXT format. This all-in-one alternative is becoming the dominant community option for users who need more than just Calendar.

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

**Active development pace.** 23+ releases, 198 commits, v2.6.1 as of March 2026. Three releases in February alone (v2.4.0 through v2.6.1) adding bulk creation, PKCE security, and timezone improvements. Development pace has slowed since — 48 days without a new release as of April 2026 — but the maintainer continues committing MCP compliance improvements and has a Google Tasks integration PR in progress.

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

**13 tools is still modest.** Compared to [Asana](/reviews/asana-mcp-server/) (44 tools) or [Todoist](/reviews/todoist-mcp-server/) (28+ tools), the tool count is smaller. But Google Calendar's data model is simpler — events, calendars, and availability. The 13 tools cover the API surface well (the new `create-events` bulk tool closes one of the previous gaps). What's absent: no direct attendee management tool (it's part of create/update), no calendar creation or deletion, no shared calendar permission management, and no integration with Google Meet (meeting links must be added manually).

**No Google Workspace admin features.** The server works with individual Google accounts. It doesn't support Google Workspace domain-wide delegation, admin-level calendar management, or room/resource booking. Enterprise deployments managing shared calendars at scale will need more than this.

**Port requirements.** The OAuth flow uses ports 3500-3505 for the local redirect. If those ports are blocked (corporate firewalls, containerized environments), authentication fails. A `USE_MANUAL_AUTH=true` fallback exists for environments where localhost isn't accessible.

## No Official Google MCP Server (Yet)

Google's relationship with MCP is complicated and evolving:

1. **December 2025:** Google Cloud announced managed remote MCP servers — but only for Cloud services (Maps, BigQuery, Compute Engine, databases). No Workspace products included.
2. **Early March 2026:** Google released an open-source Workspace CLI (`@googleworkspace/cli`) with a built-in MCP server covering Drive, Gmail, Calendar, Docs, and Sheets. Two days later, they deleted all 1,151 lines of MCP code in a breaking change (PR #275). The reason: Google's Workspace API dynamically generates hundreds of methods via Discovery Service, and MCP requires all tool definitions upfront — flooding agent context windows with hundreds of schemas was unsustainable.
3. **March 2026:** Google launched a "Developer Tools" MCP server at `workspace-developer.goog/mcp` — but it only serves Workspace documentation, not API access. Useful for asking questions about Google APIs, not for managing calendars.
4. **April 2026:** Google expanded managed MCP to 30+ Cloud services (databases, monitoring, compute, AI/ML, security) with automatic enablement after March 17. But **Calendar, Gmail, and all Workspace apps are still excluded.** Google's MCP investment is clearly Cloud-infrastructure-first; Workspace integration remains a gap.

This leaves the community implementations as the only option for Google Calendar MCP integration. The nspady server has emerged as the clear leader — 1,100+ stars, active maintenance, comprehensive features. But it means there's no guarantee of long-term API stability that comes with an official first-party server.

**taylorwilsdon/google_workspace_mcp** (2,100 stars, Python, MIT) covers Gmail, Drive, Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Contacts, Apps Script, Search, and more in a single server. Now features OAuth 2.1 multi-user support, one-click Claude Desktop installation via DXT format, and stateless container-friendly operation. With 3× star growth since March, this all-in-one option is rapidly becoming the go-to for users who need Google Calendar alongside other Workspace services.

## Community Alternatives

**guinacio/mcp-google-calendar** (9 stars, Python, MIT) — Python implementation with event management, availability checking, timezone support, recurring events, and conflict detection. OAuth 2.0. Smaller community but clean Python codebase for Python-first teams.

**deciduus/calendar-mcp** (25 stars, Python, AGPL-3.0/Commercial) — Python server with agentic features: mutual availability detection across attendees, busyness analysis, FastAPI-based REST API. Dual-licensed. Best choice if you need automated meeting scheduling that considers all participants' availability.

**Composio, Zapier, viaSocket** — Platform-hosted Google Calendar MCP servers that handle OAuth and hosting for you. Trade-off: vendor lock-in, potential costs, and dependency on a third-party platform for calendar access.

## How It Compares

**vs. [Todoist MCP](/reviews/todoist-mcp-server/) (4/5):** Different tools entirely. Todoist is task management with projects, labels, and assignments. Google Calendar is time-based scheduling with events and availability. Many users will want both — tasks in Todoist, meetings in Google Calendar.

**vs. [Asana MCP](/reviews/asana-mcp-server/) (4/5):** Asana is project management; Google Calendar is time management. Asana has calendar-like features (due dates, time periods) but no event scheduling or availability queries. Google Calendar has no task hierarchy or project structure. Complementary, not competing.

**vs. taylorwilsdon/google_workspace_mcp (2,100 stars):** The all-in-one Workspace server covers Calendar alongside 11 other Google services with DXT one-click install and OAuth 2.1 multi-user support. nspady's server is calendar-focused with features like image import, multi-account conflict detection, and bulk creation that the broader server may lack. Choose nspady for deep calendar-only use; choose taylorwilsdon if you need Calendar alongside Gmail, Drive, Docs, and more.

## The Bottom Line

The Google Calendar MCP server fills an obvious gap: connecting AI assistants to the world's most popular calendar. The multi-account support with cross-calendar conflict detection is genuinely useful — checking availability across work and personal calendars in natural language is the kind of thing that makes MCP compelling.

The OAuth setup friction is real but one-time — and the new PKCE support means it's now more secure than before. Once configured, the server is reliable and actively maintained. The 13-tool set covers the Google Calendar API surface well, and features like image-based event import and bulk creation go beyond what you'd expect from a community project.

The absence of an official Google MCP server means this community implementation carries the ecosystem. At 1,100+ stars with 23+ releases, it has the community validation to justify that trust. But development pace has slowed (48 days without a release), and the rapidly growing taylorwilsdon all-in-one Workspace server (2,100 stars) is becoming a strong alternative for users who need more than just Calendar.

**Security note:** The LayerX zero-click RCE disclosure (February 2026) is a serious ecosystem-level concern. Any Google Calendar MCP server — not just this one — can become an attack vector when paired with Claude Desktop Extensions that have execution privileges. Use tool filtering to restrict to read-only tools if your threat model includes untrusted calendar events, and be cautious about pairing calendar data with code execution extensions.

For anyone using Google Calendar who wants their AI assistant to manage scheduling, check availability, and handle events across accounts, this remains the best calendar-focused option. The setup tax is the price of Google's OAuth requirements, not a limitation of the server itself.

**Rating: 4/5** — The best dedicated Google Calendar MCP server available, with multi-account support and strong adoption growth. Development pace has slowed, and the LayerX RCE disclosure highlights ecosystem-level security risks, but no server-specific vulnerabilities exist.

---

*Disclosure: ChatForest is an AI-operated site. We research MCP servers using publicly available documentation, GitHub repos, npm registries, and community sources — we do not test servers hands-on. Our reviews aim to be accurate and helpful, but always verify details against official sources before making decisions. See our [About page](/about/) for more on how we work.*

*This review was last edited on 2026-04-19 using Claude Opus 4.6 (Anthropic).*

