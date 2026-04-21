# Calendar & Scheduling MCP Servers — Google Calendar, Outlook, Apple Calendar, Cal.com, Calendly, and More

> Calendar and scheduling MCP servers are giving AI assistants direct access to event management, availability checking, and meeting coordination.


Calendar and scheduling MCP servers are giving AI assistants direct access to event management, availability checking, and meeting coordination. Instead of switching between your IDE and a calendar app, these servers let AI agents create events, find free slots, manage attendees, and coordinate schedules — all through the Model Context Protocol.

The landscape spans seven areas: **Google Calendar** (the most implementations), **Microsoft Outlook/365** (including an official server), **Apple/macOS Calendar** (navigating a major archival), **CalDAV/iCloud** (standards-based universal access), **scheduling platforms** (Cal.com, Calendly — both now with official servers), **multi-provider unified** servers, and **task scheduling** automation. Part of our **[Communication & Collaboration](/categories/communication-collaboration/)** and **[Business & Productivity](/categories/business-productivity/)** MCP categories.

## What's New (March–April 2026)

**Calendly shipped an official hosted MCP server** at `mcp.calendly.com`. Fully hosted by Calendly — no self-hosting or local deployment. Uses DCR (RFC 7591) for automatic client registration, so no pre-registered OAuth app or secrets needed. Works on all Calendly plans including free. AI assistants can check/update availability, generate scheduling links, and manage events via natural language.

**apple-mcp (3,000 stars) was archived January 1, 2026.** The most-starred server in this review is now read-only. The project recommends migrating to supermemory MCP at `mcp.supermemory.ai`. Community forks exist (including an enhanced version by Ayaanisthebest), but the original is frozen.

**google_workspace_mcp is the new Google powerhouse.** taylorwilsdon's unified Google Workspace server hit **1,100 stars** — matching google-calendar-mcp — with coverage spanning Gmail, Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Search, and Drive. Native OAuth 2.1 with multi-user support, a persistent workspace-cli tool with encrypted disk-backed token caching, and the only Workspace MCP you can host centrally for an organization.

**Softeria's ms-365-mcp-server surged to 635 stars.** A comprehensive Microsoft 365 server with **90+ tools**, dynamic discovery (keeps initial context small, cuts token usage), multi-account support, and presets for mail, calendar, files, contacts, tasks, OneNote, search, users, and more. MIT license.

**bcharleson released agent-native CLI servers** for both Cal.com (61 tools, full API v2 coverage) and Calendly (40 tools). Every tool has Zod-validated input schemas, structured JSON output, and automatic retry with exponential backoff.

**google-calendar-mcp (nspady) grew to 1,100 stars** (up from 1,000). Still the dedicated Google Calendar leader.

The headline findings: **google-calendar-mcp and google_workspace_mcp are now tied at 1,100 stars** — dedicated vs. comprehensive Google integration. **Calendly joins Microsoft and Cal.com** as vendors with official MCP servers. **apple-mcp's archival** leaves a gap in macOS calendar integration. **Softeria's 90+ tool Microsoft 365 server** rivals the official Microsoft offering. **CalDAV support** means any standards-compliant calendar works with MCP. **No official MCP server exists from Google or Apple.** The strongest practical feature across servers remains mutual free slot detection.

## Google Calendar

### google-calendar-mcp (nspady)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nspady/google-calendar-mcp](https://github.com/nspady/google-calendar-mcp) | 1,100 | TypeScript | MIT | 12 |

The standout dedicated Google Calendar MCP server and one of the most popular MCP servers in any category. Supports **multi-account** connections (work, personal, etc.) with simultaneous querying across all calendars, plus **cross-account conflict detection** that catches overlapping events even across different Google accounts.

The 12 tools cover the full calendar lifecycle: list calendars, list events, search events, create/update/delete events, respond to attendance, check free/busy availability across calendars, and manage accounts. Advanced features include **recurring event modification**, **natural language scheduling** understanding, and **intelligent event import** from images, PDFs, and web links — you can screenshot a conference flyer and have it automatically create calendar events.

The project is actively maintained with a v2.6.1 release (March 2026). This remains the best choice for dedicated Google Calendar MCP integration.

### google_workspace_mcp (taylorwilsdon)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | 1,100 | Python | — | 50+ across services |

**NEW.** The most feature-complete Google Workspace MCP server, covering Gmail, **Calendar**, Docs, Sheets, Slides, Chat, Forms, Tasks, Search, and Drive in a single server. Native **OAuth 2.1** with multi-user support — the only Workspace MCP that can be hosted centrally for an entire organization with encrypted, disk-backed token caching.

Calendar-specific tools include event creation, listing, updating, and deletion with full Google Calendar API access. The breadth-over-depth approach means calendar features match the dedicated servers for core operations while adding seamless cross-service workflows (e.g., "check my calendar, draft a meeting agenda in Docs, and email the attendees"). At 1,100 stars and growing rapidly, this is the natural choice if you already use or plan to use other Google Workspace services through MCP.

### calendar-mcp (deciduus)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [deciduus/calendar-mcp](https://github.com/deciduus/calendar-mcp) | 23 | Python | AGPL-3.0 / Commercial | 12 |

A Python-native alternative with OAuth 2.0 authentication and automatic token management. Matches nspady's server on tool count (12) with a slightly different feature emphasis: **mutual meeting slot detection** across multiple calendars, **daily busyness analysis**, and **attendee response tracking**. The dual AGPL-3.0/Commercial license makes it suitable for both open-source and enterprise use.

The 12 tools split into three groups: calendar management (3 tools), event management (5 tools), and advanced scheduling/analysis (4 tools). The busyness analysis feature is unique — it provides a structured breakdown of how packed a given day is, useful for AI agents making scheduling decisions.

### mcp-google-calendar (guinacio)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [guinacio/mcp-google-calendar](https://github.com/guinacio/mcp-google-calendar) | 9 | Python | MIT | 8 |

A lighter Python implementation focused on core calendar operations. Includes **automatic time conflict detection** when creating events, **recurring event support** using iCalendar RRULE format, and **timezone-aware scheduling** with automatic detection. The 8 tools cover event CRUD, calendar listing, timezone info, current date retrieval, and availability checking.

### Other Google Calendar Implementations

Several additional Google Calendar MCP servers exist with more specialized approaches:

- **shade-solutions/calender-mcp** — Built with Smithery, emphasizes travel time considerations when scheduling
- **markelaugust74/mcp-google-calendar** — Focused implementation for event creation and management
- **surana-mudit/google-calendar-mcp** — Minimal Google Calendar MCP server
- **galacoder/mcp-google-calendar** — Alternative implementation listed on Awesome MCP Servers

Google Calendar has the most MCP server implementations of any calendar platform — at least 6+ on GitHub — reflecting both the platform's dominance in personal/small business calendaring and the accessibility of Google's Calendar API.

## Microsoft Outlook / Microsoft 365

### Microsoft 365 CalendarTools (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [microsoft/mcp — CalendarTools](https://github.com/microsoft/mcp) | 2,800+ (mono-repo) | C# | — | Multiple |

**Official** remote MCP server from Microsoft, part of their MCP catalog. Available as a hosted remote server at `agent365.svc.cloud.microsoft/agents/tenants/{tenant_id}/servers/mcp_CalendarTools`. Provides creating, updating, and deleting events, managing invites, and checking availability — all through Microsoft Graph Calendar APIs. The remote hosting model means no local setup — AI clients connect directly to Microsoft's infrastructure with tenant-scoped authentication.

### ms-365-mcp-server (Softeria)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Softeria/ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server) | 635 | TypeScript | MIT | 90+ |

**NEW.** The most comprehensive community Microsoft 365 MCP server, with **90+ tools** spanning mail, **calendar**, files, contacts, tasks, OneNote, search, users, and more. Key differentiators: **dynamic discovery** that keeps initial context small and cuts token usage (critical for long sessions or cost-sensitive setups), **multi-account support** where a single server instance serves multiple Microsoft accounts with automatic account parameter injection, and configurable **presets** to load only the tool groups you need.

At 635 stars with 246 forks, this has become the go-to community choice for Microsoft 365 integration — offering broader coverage than the official Microsoft server while remaining MIT-licensed and self-hosted.

### Outlook Calendar MCP (merajmehrabi)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [merajmehrabi/Outlook_Calendar_MCP](https://github.com/merajmehrabi/Outlook_Calendar_MCP) | 33 | VBScript/JS | MIT | 6 |

A **Windows-only** local implementation that interfaces directly with the Outlook desktop client via VBScript. Tools: `list_events`, `create_event`, `find_free_slots`, `get_attendee_status`, `update_event`, `get_calendars`. The direct desktop integration means it works without Microsoft Graph API credentials — if Outlook is installed and logged in, it works.

The find_free_slots capability is practical for scheduling: the AI agent can identify open windows in your Outlook calendar without you needing to manually check. Requires Node.js, the Outlook desktop app, and VBScript support (mandatory on Windows 11 24H2+).

### Office 365 MCP Server (hvkshetry)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [hvkshetry/office-365-mcp-server](https://github.com/hvkshetry/office-365-mcp-server) | 12 | JavaScript | MIT | 24 |

A comprehensive Microsoft 365 integration with 24 consolidated tools spanning email, **calendar**, Teams, OneDrive/SharePoint, contacts, Planner, To Do, groups, and directory services — all through the Graph API. Calendar-specific capabilities include listing, creating, updating, and deleting events plus finding available time slots. The consolidation approach means one server replaces what would otherwise be 5–6 separate MCP servers.

### Other Outlook/M365 Implementations

- **ryaker/outlook-mcp** — Connects Claude with M365 via Graph API and Power Automate API with calendar event management
- **XenoXilus/outlook-mcp** — Email, calendar, and SharePoint integration through Graph API
- **elyxlz/microsoft-mcp** — Minimal, powerful server for Graph API covering Outlook, Calendar, and OneDrive
- **ampcome-mcps/outlook-mcp** — Comprehensive email, contact, calendar, and folder management
- **kacase/mcp-outlook** — Calendar events, scheduling, email reading and sending via Graph API
- **anoopt/outlook-meetings-scheduler-mcp-server** — Focused specifically on meeting scheduling with attendee support

Microsoft Outlook has at least 8 MCP server implementations — second only to Google Calendar in quantity. The official Microsoft server elevates this category significantly.

## Apple / macOS Calendar

### apple-mcp (supermemoryai) — ARCHIVED

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [supermemoryai/apple-mcp](https://github.com/supermemoryai/apple-mcp) | 3,000 | TypeScript | MIT | 7 app integrations |

**Archived January 1, 2026.** The most-starred server in this review is now read-only — no bug fixes, no security updates, no new features. Calendar was one of seven Apple-native app integrations (Messages, Notes, Contacts, Mail, Reminders, **Calendar**, Maps). The project recommends migrating to **supermemory MCP** at `mcp.supermemory.ai`. Community forks exist, including an enhanced version by Ayaanisthebest, and iCloud-based alternatives (MrGo2/icloud-mcp with dual local/cloud modes, mike-tih/icloud-mcp with CalDAV/CardDAV/IMAP coverage).

At 3,000 stars, the brand still has significant visibility, but the archival leaves a notable gap in macOS-native calendar integration via MCP.

### mcp-ical (Omar-V2)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Omar-V2/mcp-ical](https://github.com/Omar-V2/mcp-ical) | 278 | Python | MIT | Multiple |

The most popular **dedicated** macOS Calendar MCP server. Uses PyObjC to interface directly with macOS Calendar (EventKit), enabling natural language interaction: "What's my schedule for next week?" or "Add a lunch meeting with Sarah tomorrow at noon."

Features include event creation with location, notes, reminders, and recurring patterns; smart schedule querying and availability checking; intelligent event updates; and **multi-calendar support** including Google Calendar accounts synced through macOS Calendar. The Python + PyObjC approach means it accesses the same calendar data as the native Calendar app without needing separate API credentials.

### Other Apple Calendar Implementations

- **somethingwithproof/calendar-mcp** — MCP server for Apple Calendar on macOS with full event lifecycle
- **shadowfax92/apple-calendar-mcp** — macOS Calendar access through EventKit with AI model integration

## CalDAV / iCloud Calendar

### caldav-mcp (dominik1001)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dominik1001/caldav-mcp](https://github.com/dominik1001/caldav-mcp) | 57 | TypeScript | MIT | 4 |

The universal calendar server — **any CalDAV-compliant calendar** works with this single MCP server. That means Nextcloud, Radicale, Baikal, iCloud, FastMail, Synology Calendar, and dozens more. The 4 tools (`create-event`, `list-events`, `delete-event`, `list-calendars`) are simple but cover the essential operations.

The CalDAV approach is strategically important: instead of needing a separate MCP server for each calendar provider, this single server works with any that implements the CalDAV standard. For self-hosted calendar users, this is the obvious choice.

### iCloud Calendar MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [localhost433/icloud-mcp](https://github.com/localhost433/icloud-mcp) | — | — | — | Multiple |
| [rgabriel/mcp-icloud-calendar](https://lobehub.com/mcp/rgabriel-mcp-icloud-calendar) | — | — | — | Multiple |

Two implementations targeting iCloud Calendar specifically via the CalDAV protocol. **icloud-mcp** provides HTTP MCP server with list/read/create/update/delete operations using an iCloud app-specific password. **mcp-icloud-calendar** connects to Apple iCloud Calendar for similar operations. Both require generating an app-specific password through Apple ID settings.

## Scheduling Platforms

### Cal.com MCP Server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [calcom/cal-mcp](https://github.com/calcom/cal-mcp) | 18 | TypeScript | — | 9 |

**Official** MCP server from Cal.com, the open-source scheduling platform. The 9 core tools cover the booking lifecycle: `getBooking`, `getBookings`, `createBooking`, `rescheduleBooking`, `cancelBooking`, `getEventTypes`, `getEventTypeById`, `updateEventType`, `deleteEventType`. An `--all-tools` flag exposes additional Cal.com API endpoints.

This is notable as Cal.com is one of very few scheduling platforms to ship an official MCP server. The project is under active development with "rapid changes" and "frequent modifications" noted in the docs. Supports integration with Claude Desktop, Cursor, and Windsurf.

Community alternatives include **Danielpeter-99/calcom-mcp** (FastMCP implementation), **mumunha/cal_dot_com_mcpserver** (3 stars), and the new **bcharleson/calcom-cli** — an agent-native CLI with **61 tools** covering the full Cal.com API v2 (bookings, event types, schedules, slots, calendars, webhooks, profile, out-of-office, teams, conferencing, destination calendars, selected calendars, and Stripe). Every tool has Zod-validated input schemas, structured JSON output, and automatic retry with exponential backoff on rate limits.

### Calendly MCP Server (Official)

| Server | Stars | Type | License | Tools |
|--------|-------|------|---------|-------|
| [Calendly MCP](https://developer.calendly.com/calendly-mcp-server) | — | Hosted | — | Multiple |

**Official** hosted MCP server from Calendly at `mcp.calendly.com`. **No self-hosting or local deployment** — Calendly runs the infrastructure. Authentication uses **DCR (RFC 7591)** for automatic client registration, meaning no pre-registered OAuth app or secrets needed in your MCP client config. Works on **all Calendly plans including free**.

AI assistants can check and update availability, generate scheduling links, manage scheduled events, and more via natural language. This is a significant shift — Calendly is now one of the first scheduling platforms with a fully hosted, zero-config official MCP server.

Community alternatives remain available: **universal-mcp/calendly** (API key/OAuth), **bcharleson/calendly-cli** (agent-native with **40 tools** covering authentication, scheduling, availability, webhooks, routing forms, groups, and data compliance — Zod-validated, with automatic retry), and several others on LobeHub and GitHub.

### When2Meet MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [joyce-yuan/when2meet-mcp](https://github.com/joyce-yuan/when2meet-mcp) | — | — | — | Multiple |

A creative integration that lets AI assistants fill out When2Meet availability polls. Features include automatic event detail extraction from When2Meet URLs, **natural language availability specification** ("I'm free Monday through Wednesday afternoons"), and automated availability marking. This solves a genuine pain point — When2Meet's grid interface is tedious to fill out manually.

## Multi-Provider Unified Servers

### calendar-mcp (MarimerLLC)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MarimerLLC/calendar-mcp](https://github.com/MarimerLLC/calendar-mcp) | 10 | C# | MIT | 14 |

A unified MCP server that aggregates **Microsoft 365, Outlook.com, Google Workspace, ICS feeds, and JSON calendar files** into a single interface. The 14 tools span account listing, email operations, calendar management, contact handling, and availability checking across all connected providers.

The key value proposition: instead of configuring separate MCP servers for your work (M365), personal (Google), and subscription (ICS) calendars, this single server provides a unified view. Supports both local stdio and containerized HTTP deployment.

## Task Scheduling

### scheduler-mcp (PhialsBasement)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [PhialsBasement/scheduler-mcp](https://github.com/PhialsBasement/scheduler-mcp) | 54 | Python | MIT | 12 |

Not a calendar server but a **task automation scheduler** built on MCP. Uses cron expressions to schedule shell commands, API calls, AI content generation tasks, and desktop notifications. The 12 tools cover task management (list, get, add, update, remove, enable/disable, run immediately) and monitoring (execution history, server info).

Four task types are supported: **command tasks** (shell commands), **API tasks** (HTTP requests), **AI tasks** (content generation), and **reminder tasks** (desktop notifications with sound). Cross-platform support across Windows, macOS, and Linux. This is useful for AI agents that need to schedule recurring operations rather than calendar events.

## What's Missing

The calendar MCP ecosystem has notable gaps:

- **No official Google Calendar MCP server** — despite having the most community implementations (and now two 1,100-star servers), Google hasn't shipped an official server
- **No official Apple Calendar MCP server** — and the community flagship (apple-mcp, 3,000 stars) was archived January 2026, leaving macOS calendar users with fewer maintained options (mcp-ical, community forks, iCloud-based alternatives)
- **AI-native scheduling platforms** — Clockwise reportedly introduced an MCP server in September 2025 but it's not publicly available on GitHub; Reclaim and Motion have minimal or no MCP presence
- **Group scheduling** — no Doodle MCP server exists; When2Meet is covered but with limited adoption
- **Enterprise scheduling** — no Kronos/UKG, Deputy, or workforce management scheduling servers
- **Room/resource booking** — no dedicated meeting room or resource booking MCP servers
- **Calendar analytics** — few servers provide insights beyond basic event data (deciduus's busyness analysis is a rare exception)

## Bottom Line

**Rating: 4.0 / 5** — Calendar and scheduling remains one of the strongest MCP categories. The ecosystem benefits from calendar management being a natural fit for AI assistants — asking "when am I free next Tuesday?" or "schedule a 30-minute meeting with the team" is exactly the kind of task where AI adds clear value.

The **Google Calendar** tier is excellent, now with two 1,100-star servers: nspady's dedicated server (cross-account conflict detection, event import from images) and taylorwilsdon's comprehensive Google Workspace server (OAuth 2.1, multi-user, 10+ Google services). The **Microsoft** tier has expanded with both an official remote server and Softeria's 635-star community server (90+ tools, dynamic discovery, multi-account). **Apple Calendar** took a hit — apple-mcp (3,000 stars) was archived January 2026, though mcp-ical and iCloud-based alternatives continue. **CalDAV** provides universal standards-based access. **Scheduling platforms** saw the biggest gains: **Calendly shipped an official hosted MCP server** (zero-config, all plans including free), joining Microsoft and Cal.com as vendors with official servers. bcharleson's agent-native CLIs add deep API coverage for both Cal.com (61 tools) and Calendly (40 tools).

The 4.0 rating reflects strong breadth (every major calendar platform is covered), growing vendor participation (now Microsoft, Calendly, and Cal.com with official servers), high community engagement (multiple servers above 500 stars), and practical AI-native features. The gap to 4.5 remains: no official servers from Google or Apple, apple-mcp's archival narrows macOS options, AI scheduling platforms (Clockwise, Reclaim, Motion) still lack MCP presence, and group scheduling/calendar analytics tooling is thin.

*This review was last edited on 2026-04-22 using Claude Opus 4.6 (Anthropic).*

