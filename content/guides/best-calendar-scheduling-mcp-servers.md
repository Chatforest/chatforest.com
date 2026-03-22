---
title: "Best Calendar & Scheduling MCP Servers in 2026 — Google Calendar vs Outlook vs Apple vs Booking Platforms"
date: 2026-03-22T22:00:00+09:00
description: "We compared 20+ calendar and scheduling MCP servers across Google Calendar, Microsoft Outlook, Apple Calendar, Cal.com, Calendly, and CalDAV. Here's which ones are worth using — and which approach fits your workflow."
og_description: "20+ calendar & scheduling MCP servers compared: Google Calendar, Outlook, Apple Calendar, Cal.com, Calendly, CalDAV. Honest recommendations from research."
content_type: "Comparison"
card_description: "google-calendar-mcp (1,100 stars, 12 tools, multi-account) vs ms-365-mcp-server (547 stars, 70+ tools) vs mcp-ical (281 stars, macOS native) vs Calendly (official hosted) vs Cal.com (official) — plus CalDAV, multi-provider, and self-hosted options."
last_refreshed: 2026-03-22
---

Calendar integration is one of the most practical MCP use cases. Checking availability, scheduling meetings, finding conflicts across accounts — these are tasks AI assistants can genuinely make faster. The ecosystem has responded with servers for every major calendar platform.

The landscape splits five ways. **Google Calendar** has the most popular dedicated server (1,100 stars, 12 tools, multi-account). **Microsoft 365** has the broadest Workspace-style servers (547 stars, 70+ tools including calendar). **Apple/macOS** has native EventKit integrations for developers in the Apple ecosystem. **Booking platforms** like Calendly and Cal.com have shipped official MCP servers. And **CalDAV** offers a universal protocol approach that works across providers.

What surprised us: **Microsoft now has an official catalog** with a dedicated Calendar remote MCP server, but it's one of 16+ servers rather than a standalone product. Meanwhile, **Calendly's fully hosted MCP** (at mcp.calendly.com) means zero infrastructure — but Google still hasn't released an official standalone calendar MCP server.

**Disclosure:** Our recommendations are based on research — analyzing documentation, GitHub repositories, community feedback, and published benchmarks. We have not hands-on tested every server in this guide.

## At a Glance: Top Picks

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| **Google Calendar (dedicated)** | [nspady/google-calendar-mcp](https://github.com/nspady/google-calendar-mcp) | 1,100 | [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) (477, Gmail+Calendar) |
| **Google Calendar (full Workspace)** | [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | 1,900 | [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) (477) |
| **Microsoft 365 / Outlook** | [Softeria/ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server) | 547 | [hvkshetry/office-365-mcp-server](https://github.com/hvkshetry/office-365-mcp-server) (24 tools) |
| **Apple / macOS** | [Omar-V2/mcp-ical](https://github.com/Omar-V2/mcp-ical) | 281 | [FradSer/mcp-server-apple-events](https://github.com/FradSer/mcp-server-apple-events) (55) |
| **Booking (Calendly)** | [Calendly MCP](https://developer.calendly.com/calendly-mcp-server) | Official | — |
| **Booking (Cal.com)** | [calcom/cal-mcp](https://github.com/calcom/cal-mcp) | 18 | [Danielpeter-99/calcom-mcp](https://github.com/Danielpeter-99/calcom-mcp) (community) |
| **CalDAV / universal** | [madbonez/caldav-mcp](https://github.com/madbonez/caldav-mcp) | 5 | [Cheffromspace/mcp-nextcloud-calendar](https://github.com/Cheffromspace/mcp-nextcloud-calendar) (5) |
| **Multi-provider** | [MarimerLLC/calendar-mcp](https://github.com/MarimerLLC/calendar-mcp) | 7 | — |

## Google Calendar Servers

Google Calendar is the most popular calendar platform for developers, and the MCP ecosystem reflects this with the most options.

### nspady/google-calendar-mcp — The Winner

**Stars:** 1,100 | **Language:** TypeScript | **License:** MIT

The most popular dedicated calendar MCP server. Mature, well-maintained, and packed with features you'd actually use.

**What makes it stand out:**
- **12 tools** — list-calendars, list-events, get-event, search-events, create-event, update-event, delete-event, respond-to-event, get-freebusy, get-current-time, list-colors, manage-accounts
- **Multi-account support** — manage multiple Google accounts simultaneously with cross-account conflict detection. This alone sets it apart from competitors
- **Multi-calendar support** — work across all calendars in each account, not just the primary one
- **Tool filtering** — expose only the tools you need to save context window tokens and improve security
- **Smart imports** — can intelligently create events from images, PDFs, and web links
- **23 releases** — v2.6.1 as of March 2026. Active development with regular feature additions

**Limitations:**
- Google Calendar only — no Outlook, Apple, or other providers
- Requires OAuth2 setup with Google Cloud Console
- No built-in remote/hosted option — runs locally via stdio

**Best for:** Most developers who use Google Calendar. Start here.

### MarkusPfundstein/mcp-gsuite — Gmail + Calendar Combo

**Stars:** 477 | **Language:** Python | **License:** MIT

A focused Google suite server covering Gmail and Calendar. Less scope than the full Workspace server, but well-targeted for the two services developers use most.

**What makes it stand out:**
- **Gmail + Calendar in one server** — email search, retrieval, drafting, and calendar event management
- **Calendar tools** — create events, list events within time ranges, delete events
- **Attachment handling** — save email attachments directly
- **Well-maintained** — 96 forks, regular community contributions

**Limitations:**
- Calendar tools are more basic than nspady's (no freebusy, no multi-account, no event updates)
- Requires external JSON config files for OAuth and account setup
- Python dependency

**Best for:** Developers who want both Gmail and Calendar access in a single server without the full Workspace suite.

### taylorwilsdon/google_workspace_mcp — The Full Suite

**Stars:** 1,900 | **Language:** Python | **License:** MIT

Covers Gmail, Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Search, and Drive. Already covered in our [spreadsheet comparison](/guides/best-spreadsheet-mcp-servers/) and [file & storage comparison](/guides/best-file-storage-mcp-servers/), but worth mentioning here for its Calendar capabilities.

**Calendar-specific features:**
- Event creation with timezone support, transparency (busy/free), visibility settings
- Up to 5 custom reminders per event
- Google Meet auto-generation
- Attendee management and guest permission controls
- FreeBusy queries for availability checking
- Remote OAuth 2.1 with multi-user support — can be hosted centrally for an organization

**Best for:** Teams already using multiple Google Workspace services who want one server to cover everything.

## Microsoft 365 / Outlook Servers

The Microsoft calendar MCP landscape is more fragmented than Google's, with both official and community options.

### Microsoft Official — microsoft/mcp Catalog

**Stars:** 2,800 (catalog repo) | **Language:** Varies | **License:** MIT

Microsoft's official MCP catalog includes a **Microsoft 365 Calendar** remote MCP server alongside 16+ other servers. It provides calendar event CRUD operations, invite management, and availability checking through the Microsoft Graph Calendar APIs.

**What makes it stand out:**
- **Official Microsoft backing** — not going to disappear or fall behind API changes
- **Remote MCP** — hosted endpoint, no local infrastructure needed
- **Part of a broader ecosystem** — if you also need Mail, User, Copilot Chat, or Admin Center, they're all in the same catalog

**Limitations:**
- Calendar is just one of many servers — not a deeply specialized tool
- Documentation is spread across the catalog rather than focused
- Requires Microsoft 365 license and Graph API permissions

**Best for:** Enterprise teams that want official Microsoft support and already use the Microsoft 365 ecosystem.

### Softeria/ms-365-mcp-server — Community Powerhouse

**Stars:** 547 | **Language:** TypeScript | **License:** MIT

The most feature-rich community Microsoft 365 MCP server. 70+ tools across email, calendar, Teams, and more.

**What makes it stand out:**
- **7 calendar tools** — list-calendars, list-calendar-events, get-calendar-event, get-calendar-view, create-calendar-event, update-calendar-event, delete-calendar-event
- **70+ total tools** — covers email, calendar, SharePoint, Teams, and more in one server
- **Actively maintained** — updated as recently as March 2026
- **Multi-account mode** with 90+ tools in the expanded configuration

**Limitations:**
- Requires Microsoft Graph API setup with Azure AD app registration
- Broad scope means calendar tools may not be as deeply specialized as a dedicated server
- Community-maintained — no Microsoft backing

**Best for:** Developers who need deep Microsoft 365 integration beyond just calendar.

### hvkshetry/office-365-mcp-server — Consolidated Tools

**Language:** Python | **License:** MIT

Takes a different approach with 24 consolidated tools that use operation-based routing, reducing the tool count for efficient LLM context usage.

**What makes it stand out:**
- **Consolidated architecture** — routes operations within tools rather than having separate tools for each action
- **Headless operation** — runs without browser after initial auth setup, with automatic token refresh
- **Covers email, calendar, Teams, Planner, To Do, Groups, and Directory**

**Limitations:**
- Not production-ready — APIs may change without notice
- Still in active development
- Requires Azure AD setup

**Best for:** Developers who want a comprehensive M365 server with an efficient tool architecture.

### elyxlz/microsoft-mcp — Minimal Option

**Stars:** 41 | **Language:** Python | **License:** MIT

Minimal, focused MCP server for Microsoft Graph API covering Outlook, Calendar, OneDrive, and Contacts.

**What makes it stand out:**
- **31 tools** across five categories with 8 calendar-specific tools
- **Calendar tools include:** event listing, creation, modification, cancellation, RSVP responses, and free/busy availability
- **Multi-account support** for personal and work profiles
- **Unified cross-service search**

**Best for:** Developers who want a lighter Microsoft MCP server with good calendar coverage.

## Apple / macOS Calendar Servers

For macOS users, several servers tap into Apple's native EventKit framework for direct calendar access.

### Omar-V2/mcp-ical — The Winner

**Stars:** 281 | **Language:** Python | **License:** MIT

The most popular macOS calendar MCP server. Interacts with the macOS Calendar app through natural language.

**What makes it stand out:**
- **Natural language event creation** with customizable calendars, locations, notes, and reminders
- **Recurring event support** — daily, weekly, monthly, yearly patterns
- **Schedule viewing and availability checking** for finding free time slots
- **Google Calendar integration** — if your Google Calendar is synced with iCloud, events created here appear in Google Calendar too
- **Most adopted** — 281 stars, clear documentation

**Limitations:**
- macOS only — won't work on Linux or Windows
- Python implementation calling macOS calendar APIs
- Fewer discrete tools compared to some competitors

**Best for:** macOS users who want simple, natural language calendar management.

### FradSer/mcp-server-apple-events — Native EventKit

**Stars:** 55 | **Language:** TypeScript + Swift | **License:** MIT

Native macOS integration with Apple Reminders and Calendar via EventKit. Takes a more architectural approach with a 4-layer Clean Architecture design.

**What makes it stand out:**
- **Combined Reminders + Calendar** — full CRUD for both in one server
- **Location-based triggers** — geofence reminders that fire based on location
- **Subtasks and checklists** with progress tracking
- **Tags/labels** for cross-list categorization
- **Swift-compiled binaries** for performance-critical operations
- **v1.3.0** — multiple releases indicate active development

**Limitations:**
- macOS only
- More complex setup than simpler alternatives
- TypeScript + Swift hybrid adds build complexity

**Best for:** Developers who want deep Reminders + Calendar integration on macOS with advanced features like geofencing.

### PsychQuant/che-ical-mcp — Most Tools

**Stars:** 13 | **Language:** Swift | **License:** MIT

The most feature-dense macOS calendar MCP server with 25 tools. Native Swift EventKit integration.

**What makes it stand out:**
- **25 tools** across calendars (4), events (4), reminders (7), and advanced features (10)
- **Multi-source support** — iCloud, Google, Exchange, CalDAV, and local calendars
- **Same-name disambiguation** — handles calendars with identical names across providers
- **Conflict detection** for scheduling
- **Duplicate event detection** across calendars
- **Batch operations** for events and reminders
- **Geofence-based reminder triggers**

**Limitations:**
- macOS only
- Relatively new (v1.4.0, January 2026)
- 13 stars — smaller community

**Best for:** Power users who need comprehensive calendar + reminders management across multiple macOS calendar sources.

## Booking & Scheduling Platform Servers

For teams using dedicated scheduling platforms, official MCP servers are emerging.

### Calendly — Official Hosted MCP

**Hosted at:** mcp.calendly.com | **Type:** Remote MCP

Calendly's official MCP server is fully hosted — zero local infrastructure required. It maps to Calendly's public API v2 with tool annotations for safety.

**What makes it stand out:**
- **Fully hosted** — no installation, no maintenance, no server to manage
- **Official Calendly backing** — maintained by the Calendly team
- **Tool annotations** — each tool includes readOnlyHint, destructiveHint, and idempotentHint metadata for safe AI usage
- **Full API coverage** — book/cancel meetings, update availability, generate scheduling links, manage events
- **OAuth 2.0 authentication** — standard secure auth flow

**Limitations:**
- Calendly-only — won't help with Google Calendar, Outlook, or other calendars
- Requires a Calendly account
- Limited to what Calendly's API exposes

**Best for:** Teams already using Calendly who want AI-powered scheduling management.

### calcom/cal-mcp — Official Cal.com

**Stars:** 18 | **Language:** TypeScript | **License:** Not specified

The official MCP server for Cal.com, the popular open-source scheduling platform (39,000+ stars on the main Cal.com repo).

**What makes it stand out:**
- **Official Cal.com backing** — maintained by the Cal.com team
- **9 core tools** for booking management (create, retrieve, reschedule, cancel) and event type operations
- **Expandable** — `--all-tools` flag enables tools for all Cal.com API endpoints
- **Workflow support** — tested prompt workflows for rapid Cal.com application development
- **Open-source scheduling** — Cal.com itself is open source, unlike Calendly

**Limitations:**
- Early development (7 commits, May 2025 creation) — APIs may change
- Cal.com-specific — doesn't integrate with external calendars directly
- Requires Cal.com API key

**Best for:** Cal.com users who want AI-managed scheduling and booking.

## CalDAV / Universal Protocol Servers

CalDAV is the open standard for calendar access. These servers work with any CalDAV-compatible provider.

### madbonez/caldav-mcp — Universal CalDAV

**Stars:** 5 | **Language:** Python | **License:** MIT

A universal MCP server for the CalDAV protocol. The appeal is breadth: one server, any CalDAV provider.

**What makes it stand out:**
- **8 tools** — list calendars, create events, get events by timeframe, retrieve by UID, delete, search
- **Works with any CalDAV provider** — Nextcloud, ownCloud, Apple iCloud, Google Calendar (via CalDAV), Yandex Calendar, FastMail, and more
- **Rich event features** — recurring events, categories, priorities, attendees, multiple reminders
- **Attendance tracking** — ACCEPTED/DECLINED/TENTATIVE/NEEDS-ACTION status

**Limitations:**
- Only 5 stars — small community, limited battle-testing
- End-to-end tested only against Yandex Calendar (other providers should work but untested)
- 3 commits total — very early stage
- CalDAV limits you to what the protocol supports (no provider-specific features like Google Meet integration)

**Best for:** Self-hosters and privacy-focused users who want one server for Nextcloud, ownCloud, or other CalDAV providers.

### Cheffromspace/mcp-nextcloud-calendar — Nextcloud-Specific

**Stars:** 5 | **Language:** TypeScript | **License:** MIT

A Nextcloud-focused CalDAV calendar MCP server with some unique features.

**What makes it stand out:**
- **ADHD-friendly organization** — custom categories and focus priorities for events
- **Dual transport support** — Streamable HTTP (March 2025 spec) and legacy HTTP+SSE
- **Full CRUD** for both calendars and events
- **Nextcloud-optimized** — Basic Auth with Nextcloud, purpose-built for the platform

**Limitations:**
- Nextcloud only — not a universal CalDAV server
- Early development (0.1.x) — APIs may change
- 5 stars

**Best for:** Nextcloud users who want calendar integration with AI assistants.

## Multi-Provider Servers

### MarimerLLC/calendar-mcp — Cross-Platform Unified

**Stars:** 7 | **Language:** C# | **License:** MIT

A unified server that aggregates calendar access across Microsoft 365, Outlook.com, Google Workspace, ICS feeds, and JSON files.

**What makes it stand out:**
- **Multi-provider in one server** — Microsoft 365 (multiple tenants), Outlook.com, and Google Workspace simultaneously
- **14 MCP tools** including account listing, calendar event management, contact operations, and free-time discovery
- **ICS feed and JSON file support** — read-only access to any calendar with an ICS URL
- **Email + Calendar + Contacts** — unified view across providers
- **Smart domain-based routing** — automatically routes operations to the right provider

**Limitations:**
- 7 stars — very early, small community
- C# — less common in the MCP ecosystem (most servers are TypeScript or Python)
- 82 commits but only one contributor visible
- Requires OAuth setup for each provider

**Best for:** Users with calendars split across Google and Microsoft who want a single unified server.

### Infomaniak/mcp-server-calendar — Vendor Calendar

**Language:** TypeScript | **License:** Not specified

An official MCP server from European cloud provider Infomaniak for their Calendar API.

**What makes it stand out:**
- **Official vendor backing** — maintained by Infomaniak
- **Simple tool set** — calendar_list_events (search) and calendar_create_event (create)
- **Docker support** — containerized deployment option
- **npm package** — `@infomaniak/mcp-server-calendar`

**Limitations:**
- Infomaniak-only — won't work with Google, Microsoft, or Apple calendars
- Only 2 tools — very limited compared to alternatives
- Niche provider — smaller user base

**Best for:** Infomaniak customers who want calendar AI integration.

## How to Choose

```
Do you use Google Calendar?
├── Yes, only Google Calendar → nspady/google-calendar-mcp
├── Yes, plus Gmail/Docs/Sheets → taylorwilsdon/google_workspace_mcp
│
Do you use Microsoft 365 / Outlook?
├── Yes, want official support → Microsoft 365 Calendar (microsoft/mcp)
├── Yes, want community tools → Softeria/ms-365-mcp-server
│
Do you use macOS Calendar?
├── Yes, simple use → Omar-V2/mcp-ical
├── Yes, Reminders too → FradSer/mcp-server-apple-events or PsychQuant/che-ical-mcp
│
Do you use Calendly or Cal.com?
├── Calendly → Calendly MCP (mcp.calendly.com)
├── Cal.com → calcom/cal-mcp
│
Do you self-host (Nextcloud/ownCloud)?
├── Yes → madbonez/caldav-mcp or Cheffromspace/mcp-nextcloud-calendar
│
Do you need Google + Microsoft unified?
└── Yes → MarimerLLC/calendar-mcp
```

## Three Trends Worth Watching

### 1. Official vendors are showing up — selectively

Calendly has a fully hosted MCP server. Microsoft has an official catalog with Calendar. Cal.com shipped an official server. But **Google still hasn't released an official calendar MCP server** despite being the most popular calendar platform among developers. The community servers are excellent (nspady's server has 1,100 stars and 23 releases), but the absence of an official Google server is conspicuous.

### 2. Hosted MCP is the future for booking platforms

Calendly's approach (fully hosted at mcp.calendly.com, OAuth auth, zero local setup) is likely where all SaaS calendar platforms end up. Cal.com's server still runs locally, but it's early. The distinction between "calendar" (Google/Outlook — your schedule) and "scheduling" (Calendly/Cal.com — booking with others) is driving different MCP architectures: calendar servers stay local for privacy, booking servers go remote for convenience.

### 3. Multi-provider is the real need, but the hardest problem

Most people have at least two calendars. MarimerLLC's unified server is the only one attempting true cross-provider aggregation, but at 7 stars it's early. The Apple servers that bridge iCloud+Google via sync are a pragmatic workaround. Until a dominant multi-provider server emerges, most users will need multiple MCP servers — one per calendar platform.

## What's Missing

- **No official Google Calendar MCP server** — the biggest gap. Community servers fill it well, but official backing would mean guaranteed API compatibility
- **No Outlook.com standalone server** — most Microsoft servers target M365 enterprise; personal Outlook.com users are underserved
- **No Zoom scheduling integration** — Zoom has calendar features but no MCP server for them
- **No Reclaim.ai / Motion / Clockwise MCP servers** — AI-native scheduling tools that would benefit most from MCP integration haven't shipped servers yet
- **No cross-platform free/busy aggregation** — checking availability across Google + Outlook + Apple simultaneously doesn't exist in a single tool
- **Limited recurring event intelligence** — most servers can create recurring events but can't analyze patterns or suggest optimal meeting times
- **No calendar analytics** — meeting load analysis, time allocation tracking, and scheduling pattern insights are absent from all servers
