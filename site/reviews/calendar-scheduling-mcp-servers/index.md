# Calendar & Scheduling MCP Servers — Google Calendar, Outlook, Apple Calendar, Cal.com, Calendly, and More

> Calendar and scheduling MCP servers are giving AI assistants direct access to event management, availability checking, and meeting coordination.


Calendar and scheduling MCP servers are giving AI assistants direct access to event management, availability checking, and meeting coordination. Instead of switching between your IDE and a calendar app, these servers let AI agents create events, find free slots, manage attendees, and coordinate schedules — all through the Model Context Protocol.

The landscape spans seven areas: **Google Calendar** (the most implementations), **Microsoft Outlook/365** (including an official server), **Apple/macOS Calendar** (with the highest-starred server), **CalDAV/iCloud** (standards-based universal access), **scheduling platforms** (Cal.com, Calendly), **multi-provider unified** servers, and **task scheduling** automation. Part of our **[Communication & Collaboration](/categories/communication-collaboration/)** and **[Business & Productivity](/categories/business-productivity/)** MCP categories.

The headline findings: **google-calendar-mcp leads with 1,000 stars** and 12 tools including multi-account support and cross-account conflict detection — one of the highest-starred servers in any MCP category. **Microsoft has shipped an official remote MCP server** for 365 Calendar through Graph API. **apple-mcp is the most-starred server touching calendar** at 3,000 stars, though calendar is one of seven app integrations. **Cal.com has an official MCP server** with 9 booking management tools. **CalDAV support** means any standards-compliant calendar (Nextcloud, Radicale, Baikal, iCloud) works with MCP. **No official MCP server exists from Google or Apple** despite Google Calendar being the most-integrated platform. **AI-native scheduling platforms** (Clockwise, Reclaim, Motion) have minimal MCP presence. **The strongest practical feature** across servers is mutual free slot detection — AI can find meeting times across multiple calendars without human back-and-forth.

## Google Calendar

### google-calendar-mcp (nspady)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nspady/google-calendar-mcp](https://github.com/nspady/google-calendar-mcp) | 1,000 | TypeScript | MIT | 12 |

The standout Google Calendar MCP server and one of the most popular MCP servers in any category. Supports **multi-account** connections (work, personal, etc.) with simultaneous querying across all calendars, plus **cross-account conflict detection** that catches overlapping events even across different Google accounts.

The 12 tools cover the full calendar lifecycle: list calendars, list events, search events, create/update/delete events, respond to attendance, check free/busy availability across calendars, and manage accounts. Advanced features include **recurring event modification**, **natural language scheduling** understanding, and **intelligent event import** from images, PDFs, and web links — you can screenshot a conference flyer and have it automatically create calendar events.

The project is actively maintained with 197 commits and a v2.6.1 release (March 2026). This is the Google Calendar MCP server to use unless you have specific needs that require a different approach.

### calendar-mcp (deciduus)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [deciduus/calendar-mcp](https://github.com/deciduus/calendar-mcp) | 25 | Python | AGPL-3.0 / Commercial | 12 |

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
| [microsoft/mcp — CalendarTools](https://github.com/microsoft/mcp) | 2,800 (mono-repo) | C# | — | Multiple |

**Official** remote MCP server from Microsoft, part of their MCP catalog (2,800 stars across all servers). Available as a hosted remote server at `agent365.svc.cloud.microsoft/agents/tenants/{tenant_id}/servers/mcp_CalendarTools`. Provides creating, updating, and deleting events, managing invites, and checking availability — all through Microsoft Graph Calendar APIs.

This is significant: Microsoft is one of the first major productivity vendors to ship an official MCP server for calendar operations. The remote hosting model means no local setup — AI clients connect directly to Microsoft's infrastructure with tenant-scoped authentication.

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

### apple-mcp (supermemoryai)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [supermemoryai/apple-mcp](https://github.com/supermemoryai/apple-mcp) | 3,000 | TypeScript | MIT | 7 app integrations |

The most-starred server in this review — though calendar is one of seven Apple-native app integrations (Messages, Notes, Contacts, Mail, Reminders, **Calendar**, Maps). Calendar capabilities include creating events, searching events, and viewing upcoming schedule. The standout feature is **command chaining** across apps: "check my calendar for tomorrow, find the attendees in my contacts, and send them a reminder via Messages."

At 3,000 stars, this is one of the most popular MCP servers period. The breadth-over-depth approach means calendar features are solid but not as comprehensive as dedicated calendar servers.

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
| [dominik1001/caldav-mcp](https://github.com/dominik1001/caldav-mcp) | 56 | TypeScript | MIT | 4 |

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

Community alternatives exist from **Danielpeter-99/calcom-mcp** (FastMCP implementation) and **mumunha/cal_dot_com_mcpserver** (3 stars).

### Calendly MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [universal-mcp/calendly](https://github.com/universal-mcp/calendly) | — | — | — | Multiple |
| [meamitpatil/calendly-mcp-server](https://lobehub.com/mcp/meamitpatil-calendly-mcp-server) | — | — | — | Multiple |

A Universal MCP server for the Calendly scheduling platform, providing tools to retrieve user information, list events, manage invitees, and cancel events. Requires API key or OAuth credential configuration. A second community implementation is available on LobeHub. Neither is official from Calendly.

### When2Meet MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [joyce-yuan/when2meet-mcp](https://github.com/joyce-yuan/when2meet-mcp) | — | — | — | Multiple |

A creative integration that lets AI assistants fill out When2Meet availability polls. Features include automatic event detail extraction from When2Meet URLs, **natural language availability specification** ("I'm free Monday through Wednesday afternoons"), and automated availability marking. This solves a genuine pain point — When2Meet's grid interface is tedious to fill out manually.

## Multi-Provider Unified Servers

### calendar-mcp (MarimerLLC)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MarimerLLC/calendar-mcp](https://github.com/MarimerLLC/calendar-mcp) | 7 | C# | MIT | 14 |

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

- **No official Google Calendar MCP server** — despite having the most community implementations, Google hasn't shipped an official server (though google-calendar-mcp at 1,000 stars fills this gap well)
- **No official Apple Calendar MCP server** — apple-mcp is community-built despite being wildly popular
- **AI-native scheduling platforms** — Clockwise reportedly introduced an MCP server in September 2025 but it's not publicly available on GitHub; Reclaim and Motion have minimal or no MCP presence
- **Group scheduling** — no Doodle MCP server exists; When2Meet is covered but with limited adoption
- **Enterprise scheduling** — no Kronos/UKG, Deputy, or workforce management scheduling servers
- **Room/resource booking** — no dedicated meeting room or resource booking MCP servers
- **Calendar analytics** — few servers provide insights beyond basic event data (deciduus's busyness analysis is a rare exception)

## Bottom Line

**Rating: 4.0 / 5** — Calendar and scheduling is one of the strongest MCP categories. The ecosystem benefits from calendar management being a natural fit for AI assistants — asking "when am I free next Tuesday?" or "schedule a 30-minute meeting with the team" is exactly the kind of task where AI adds clear value.

The **Google Calendar** tier is excellent, led by nspady's 1,000-star server with features like cross-account conflict detection and event import from images. The **Microsoft** tier is elevated by an official remote MCP server from Microsoft itself. **Apple Calendar** has the most-starred server in the review (apple-mcp at 3,000 stars) plus a strong dedicated option in mcp-ical. **CalDAV** provides universal standards-based access. **Cal.com** has shipped an official server.

The 4.0 rating reflects the strong breadth (every major calendar platform is covered), high community engagement (multiple servers above 100 stars), vendor participation (Microsoft and Cal.com official servers), and practical AI-native features (natural language scheduling, mutual free slot detection, intelligent event import). The gap to 4.5 is the absence of official servers from Google and Apple, limited AI scheduling platform integration, and the lack of group scheduling and calendar analytics tooling.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

