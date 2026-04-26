---
title: "Event Management & Ticketing MCP Servers — Google Official Calendar, Eventbrite, Ticketmaster, Meetup, and More"
date: 2026-03-15T20:00:00+09:00
description: "Event management and ticketing MCP servers let AI agents discover live events, manage calendars, create event pages, and automate registration workflows."
og_description: "Event management & ticketing MCP servers: Google official Calendar MCP (Developer Preview, 8 tools, remote OAuth 2.0), google_workspace_mcp (2,200 stars, 12 Google services), nspady/google-calendar-mcp (1,100 stars, 12 tools), Ticketmaster (24 stars, event discovery), mcp-ical (304 stars, macOS Calendar), Eventbrite (8 tools, full lifecycle), NEW icloud-calendar-mcp (Kotlin/JVM, CalDAV, OWASP compliant), NEW SITCON 2026 conference MCP (10 tools). 35+ servers across calendaring, ticketing, event platforms, and conference navigation. Rating: 3.5/5."
content_type: "Review"
card_description: "Event management and ticketing MCP servers across calendaring, ticket discovery, event platforms, conference navigation, and community events. The biggest development since our original review: **Google launched official remote MCP servers** for Calendar (8 tools), Gmail (10 tools), Drive (7 tools), People API (3 tools), and Chat (2 tools) — available in Developer Preview at `calendarmcp.googleapis.com/mcp/v1` with OAuth 2.0 authentication. This is the first time a major platform has shipped official calendar MCP support. The dominant subcategory remains **calendaring** — Google Calendar alone has 10+ competing community implementations, led by nspady/google-calendar-mcp (1,100 stars, TypeScript, MIT, 12 tools) with multi-account support, smart scheduling, free/busy queries, recurring event handling, and intelligent import from images/PDFs/web links. taylorwilsdon/google_workspace_mcp (2,200 stars, Python, MIT) is the most-starred community server touching calendar — a comprehensive Google Workspace MCP covering 12 services (Gmail, Calendar, Drive, Docs, Sheets, Slides, Forms, Chat, Tasks, Contacts, Apps Script, Search) with OAuth 2.1 multi-user support and tiered tool loading. shade-solutions/calender-mcp takes it further with 60+ tools including analytics, batch operations, working location/focus time, and AI-powered event extraction. Apple Calendar has strong coverage through Omar-V2/mcp-ical (304 stars, Python, MIT) for natural language macOS Calendar control, shadowfax92/apple-calendar-mcp for full CRUD, and somethingwithproof/calendar-mcp for search and management. NEW icloud-calendar-mcp/icloud-calendar-mcp (8 stars, Kotlin/JVM, Apache 2.0) is the first iCloud Calendar MCP server via CalDAV — notable for OWASP MCP Top 10 compliance with 282 dedicated security tests, rate limiting, SSRF protection, audit logging, and ReDoS protection. Microsoft Outlook is served by anoopt/outlook-meetings-scheduler-mcp-server (Microsoft Graph API, attendee discovery) and elyxlz/microsoft-mcp (Outlook + Calendar + OneDrive + Contacts). Calendar-mcp.com provides a hosted iCal (.ics) remote MCP server compatible with any calendar platform. For ticket discovery, delorenj/mcp-server-ticketmaster (24 stars, TypeScript, MIT) is the most popular — 6 tools searching events, venues, and attractions via the Ticketmaster Discovery API with JSON and text output formats. mmmaaatttttt/mcp-live-events (2 stars, Python) focuses specifically on live music events via Ticketmaster, while mochow13/ticketmaster-mcp-server (1 star, TypeScript, ISC) implements Streamable HTTP transport. PeterShin23/seatgeek-mcp (3 stars, TypeScript, MIT, 4 tools) offers event discovery with performer-based recommendations and detailed venue seating layouts including sections and rows — unique in the category. Eventbrite has the most implementations of any event platform: joshuachestang/eventbrite-mcp-server (2 stars, JavaScript, MIT, 8 tools) provides full event lifecycle management — create, list, get, update, publish, cancel events plus venue creation and category listing. vishalsachdev/eventbrite-mcp (2 stars, API Blueprint, MIT) focuses on event listing and analytics with planned attendee management. punkpeye/eventbrite-mcp (1 star, JavaScript, MIT, 4 tools) provides search, details, categories, and venue lookup. Community events are covered by d4nshields/mcp-meetup (0 stars, Python, MIT, 4 tools) integrating Meetup.com with Claude via search, prompt augmentation, recommendations, and OAuth, and ajeetraina/meetup-mcp-server (1 star, JavaScript, MIT) for general Meetup context management. imagineering-cc/events-mcp manages events across both Meetup and Luma via Playwright browser automation — no paid API tiers required. The Events Calendar official MCP server (the-events-calendar/mcp-server, 1 star, TypeScript, 184 commits) bridges WordPress sites running The Events Calendar plugin with AI assistants, providing unified CRUD for events (tribe_events), venues (tribe_venue), organizers (tribe_organizer), and tickets (tribe_rsvp_tickets/tec_tc_ticket) — notable as an official vendor server. the-plus-io/quick-event-mcp (0 stars, JavaScript, proprietary free-to-use) takes a different approach: a hosted remote MCP server that generates complete event landing pages with registration forms, ticket categories, QR code check-in, and email templates for conferences, workshops, parties, meetups, and weddings — the only server that creates event pages from scratch. Conference navigation is a niche but growing subcategory. manu-mishra/reinvent-mcp-2025 (5 stars, JavaScript, MIT, 13 tools) provides intelligent access to all 1,843 AWS re:Invent sessions with fuzzy search, speaker discovery, filtering by level/role/industry/topic/segment, and MessagePack optimization. doozMen/tech-conf-agent (3 stars, Swift, MIT, 6 tools) was built for ServerSide.swift 2025 London with session search, speaker profiles, room finding, and schedule queries backed by SQLite. NEW sitcon-tw/mcp (1 star, TypeScript, Apache-2.0, 10 tools) provides session search, speaker lookup, team member discovery, shareable session URLs, and conference info for SITCON 2026 (Students' Information Technology Conference) — a template for how student/community conferences can be made AI-navigable. ajot/event-information-mcp-server (0 stars, Python) uses DigitalOcean's Gradient AI for event discovery with speaker and schedule information. Eventtia has publicly committed to making their enterprise event platform MCP-accessible, describing 'agentic event software' where AI agents handle complex configuration tasks from natural language — potentially the most ambitious commercial approach, though no public server exists yet. Gaps remain significant but are narrowing on the calendar side: no official servers from Ticketmaster, Eventbrite, Live Nation, StubHub, Dice, or any major ticketing platform. No virtual event platforms (Hopin/RingCentral Events, Zoom Events, Airmeet, Gather). No event check-in, badge printing, or attendee management beyond basic listing. No catering, vendor coordination, or event logistics. No venue booking or availability systems. No event analytics or ROI tracking. No volunteer management. No hybrid/virtual event streaming integration. The category earns 3.5/5 — Google's official Calendar MCP strengthens an already-mature calendaring subcategory, but event management and ticketing remain underdeveloped."
last_refreshed: 2026-04-26
---

Event management and ticketing MCP servers let AI agents discover live events, manage calendars, create event pages, and automate registration workflows. The ecosystem splits sharply: **calendaring is now mature and officially supported** (Google launched official Calendar MCP in Developer Preview), while **ticketing and event management remain early-stage** with mostly read-only API wrappers.

This review covers the **event management and ticketing** vertical — calendar scheduling, ticket discovery, event platforms, community events, and conference navigation. For meeting/video call servers, see our [Communication & Messaging MCP review](/reviews/telecommunications-messaging-mcp-servers/). For restaurant/venue booking, see our [Food & Restaurant MCP review](/reviews/food-restaurant-mcp-servers/).

The headline finding: **Google shipped official Calendar MCP** — a remote MCP server at `calendarmcp.googleapis.com/mcp/v1` with 8 tools and OAuth 2.0 authentication. This is the first major platform to offer official MCP support in this category. Meanwhile, the community side continues to grow, with nspady/google-calendar-mcp holding at 1,100 stars and taylorwilsdon/google_workspace_mcp reaching 2,200 stars. But outside calendaring, no Ticketmaster, Eventbrite, or Live Nation official servers exist.

**Category:** [Business & Productivity](/categories/business-productivity/)

## Calendar & Scheduling

### Google Official Calendar MCP (Developer Preview)

| Server | Transport | Auth | Tools |
|--------|-----------|------|-------|
| [calendarmcp.googleapis.com](https://developers.google.com/workspace/calendar/api/guides/configure-mcp-server) | Remote HTTP | OAuth 2.0 | 8 |

**The biggest development in this category since our original review.** Google launched an official remote MCP server for Calendar as part of the Google Workspace Developer Preview Program. Tools include:

- **create_event** / **update_event** / **delete_event** — full event lifecycle
- **get_event** / **list_events** / **list_calendars** — read operations
- **respond_to_event** — accept/decline invitations
- **suggest_time** — AI-powered scheduling suggestions

The server lives at `https://calendarmcp.googleapis.com/mcp/v1` and works with Gemini CLI, Claude, and any MCP-compatible client. It inherits the user's existing Google Workspace permissions and data governance controls — no separate authorization model needed.

Google also launched official MCP servers for **Gmail** (10 tools), **Google Drive** (7 tools), **People API** (3 tools), and **Google Chat** (2 tools) as part of the same Workspace MCP initiative. This makes Google the first major productivity platform to ship official MCP across multiple services.

### Google Calendar MCP (Community)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nspady/google-calendar-mcp](https://github.com/nspady/google-calendar-mcp) | 1,100 | TypeScript | MIT | 12 |

The **most popular community calendar MCP server** and one of the highest-starred in this entire review. Features:

- **Multi-account** — connect multiple Google accounts simultaneously
- **Multi-calendar** — manage events across different calendars
- **Smart scheduling** — detect overlapping events across accounts
- **Free/busy queries** — check availability before scheduling
- **Recurring events** — modify single instances or entire series
- **Intelligent import** — extract calendar data from images, PDFs, and web links
- **RSVP control** — accept/decline/tentative with per-instance granularity

The intelligent import feature is particularly useful — paste a screenshot of a conference schedule and it creates calendar events automatically.

### Google Workspace MCP (Community)

| Server | Stars | Language | License | Services |
|--------|-------|----------|---------|----------|
| [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | 2,200 | Python | MIT | 12 |

The **most-starred community server touching Google Calendar** — though it's a comprehensive Workspace MCP, not calendar-specific. Covers Gmail, Calendar, Drive, Docs, Sheets, Slides, Forms, Chat, Tasks, Contacts, Apps Script, and Custom Search. Features OAuth 2.1 multi-user support, tiered tool loading (core/extended/complete), read-only mode, and stateless container-friendly deployment. If you need calendar plus other Google services from a single MCP server, this is the leading option.

### shade-solutions/calender-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [shade-solutions/calender-mcp](https://github.com/shade-solutions/calender-mcp) | 1 | TypeScript | — | 60+ |

The **most feature-rich calendar MCP server by tool count.** Built on Smithery with 60+ tools across 8 categories:

- **Basic operations** — CRUD, colors, settings, ACLs
- **Event management** — quick add, move between calendars, instances
- **Advanced scheduling** — working location, out-of-office, focus time, appointment slots, optimal time finding
- **Analytics** — time analysis, meeting effectiveness, calendar utilization, event categorization
- **Batch operations** — bulk create/delete/update, duplicate series, search-and-replace
- **Integration** — export to formats, AI event extraction from text, travel time blocking, conflict detection

The analytics tools are unique in the calendar space — no other server offers meeting effectiveness scoring or calendar utilization reports.

### Additional Google Calendar Implementations

At least 8 more Google Calendar MCP servers exist:

- **guinacio/mcp-google-calendar** — scheduling and availability checking
- **deciduus/calendar-mcp** — Python-based, natural language operations
- **markelaugust74/mcp-google-calendar** — event creation via Claude
- **feamster/calendar-mcp** — Google Calendar MCP server
- **surana-mudit/google-calendar-mcp** — another community implementation
- **KhurramDevOps/Google_Calender_MCP** — automation and synchronization

The duplication pattern is extreme — Google Calendar may have more MCP implementations than any other single API.

### Apple Calendar / macOS

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Omar-V2/mcp-ical](https://github.com/Omar-V2/mcp-ical) | 304 | Python | MIT | ~5 |

The **most popular Apple Calendar MCP server.** Uses PyObjC to interact directly with macOS Calendar (not iCloud API), supporting:

- Natural language event creation ("lunch with Alex next Tuesday at noon")
- Custom calendar selection
- Smart reminders
- Recurring events
- Schedule queries

Two additional Apple Calendar implementations exist: **shadowfax92/apple-calendar-mcp** for full CRUD via standardized MCP interface, and **somethingwithproof/calendar-mcp** for search and management.

### iCloud Calendar (CalDAV)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [icloud-calendar-mcp/icloud-calendar-mcp](https://github.com/icloud-calendar-mcp/icloud-calendar-mcp) | 8 | Kotlin/JVM | Apache 2.0 | 5 |

The **first iCloud Calendar MCP server via CalDAV** — works with any CalDAV-compatible calendar, not just Apple's. The standout feature is security: built with **OWASP MCP Top 10 compliance** and 282 dedicated security tests covering credential protection, input validation with SSRF protection, rate limiting (60 reads/min, 20 writes/min), ReDoS protection, and audit logging for all mutations. Available on npm, PyPI, and as a standalone JAR.

### Microsoft Outlook

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [anoopt/outlook-meetings-scheduler-mcp-server](https://github.com/anoopt/outlook-meetings-scheduler-mcp-server) | — | TypeScript | — | ~3 |

Schedules meetings in Microsoft Outlook via **Microsoft Graph API** with attendee email discovery and calendar event creation. Requires configurable authentication.

**elyxlz/microsoft-mcp** provides a broader Microsoft Graph integration covering Outlook, Calendar, OneDrive, and Contacts in a single minimal server.

**merajmehrabi/Outlook_Calendar_MCP** takes a local approach — accesses the Windows Outlook desktop application directly (Windows only).

### iCal / Cross-Platform

**calendar-mcp.com** offers a hosted iCal (.ics) remote MCP server compatible with any calendar that supports the iCal standard — works with Apple Calendar, Outlook, Google Calendar, and others without platform-specific API integration.

## Ticket Discovery & Live Events

### Ticketmaster MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [delorenj/mcp-server-ticketmaster](https://github.com/delorenj/mcp-server-ticketmaster) | 24 | TypeScript | MIT | 6 |

The **most popular ticketing MCP server.** Searches events, venues, and attractions via the Ticketmaster Discovery API with:

- Keyword and date range filtering
- Location-based search
- Venue discovery
- Attraction classification
- **Dual output** — JSON for programmatic use, text for human readability
- Pricing, images, and ticket URLs

Two additional Ticketmaster implementations exist:
- **mmmaaatttttt/mcp-live-events** (2 stars, Python) — focused specifically on live music events with LLM-optimized response formatting
- **mochow13/ticketmaster-mcp-server** (1 star, TypeScript, ISC) — notable for implementing **Streamable HTTP transport** via Express.js, making it accessible without stdio

### SeatGeek MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [PeterShin23/seatgeek-mcp](https://github.com/PeterShin23/seatgeek-mcp) | 3 | TypeScript | MIT | 4 |

The only secondary ticket marketplace MCP server. Unique features:

- **find_events** — search by performer, location, date, or venue
- **find_event_recommendations** — personalized event suggestions
- **find_performer_recommendations** — discover similar performers
- **retrieve_event_venue_information** — detailed seating layouts including sections and rows

The **venue seating layout** tool is unique in the category — no other event MCP server provides section-level venue information.

## Event Platforms

### Eventbrite

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [joshuachestang/eventbrite-mcp-server](https://github.com/joshuachestang/eventbrite-mcp-server) | 2 | JavaScript | MIT | 8 |

The **most complete Eventbrite implementation** with full event lifecycle management:

- `create_event` / `update_event` / `publish_event` / `cancel_event`
- `list_events` / `get_event`
- `create_venue`
- `list_categories`

This is one of the few event MCP servers that supports **write operations** — most are read-only discovery tools.

Two additional Eventbrite implementations:
- **vishalsachdev/eventbrite-mcp** (2 stars, API Blueprint, MIT) — event listing with planned analytics and attendee management
- **punkpeye/eventbrite-mcp** (1 star, JavaScript, MIT, 4 tools) — search, details, categories, and venue lookup

### The Events Calendar (WordPress)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [the-events-calendar/mcp-server](https://github.com/the-events-calendar/mcp-server) | 1 | TypeScript | — | ~8 |

An **official vendor server** — The Events Calendar WordPress plugin team built this MCP bridge. Provides unified CRUD operations for:

- **Events** (tribe_events)
- **Venues** (tribe_venue)
- **Organizers** (tribe_organizer)
- **Tickets** (tribe_rsvp_tickets or tec_tc_ticket)

Requires a WordPress site running The Events Calendar plugin with an Application Password. Supports installation across Claude Desktop, Cursor, VS Code, Windsurf, and more.

### Quick Event MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [the-plus-io/quick-event-mcp](https://github.com/the-plus-io/quick-event-mcp) | 0 | JavaScript | Proprietary (free) | 1 |

A **remote MCP server** (no local installation) that generates complete event pages from a single `create_event` tool call:

- Professional landing pages with hero sections and speaker info
- Registration forms tailored to event type
- Ticket categories with capacity controls
- Confirmation and reminder email templates
- QR code check-in functionality
- Supports conferences, workshops, parties, meetups, weddings, galas, seminars
- Bilingual (English/German)

The only server that creates **entire event pages from scratch** — unique in the category.

## Community Events

### Meetup MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [d4nshields/mcp-meetup](https://github.com/d4nshields/mcp-meetup) | 0 | Python | MIT | 4 |

Integrates Meetup.com with Claude for intelligent event discovery:

- `search_meetup_events` — find events by topic/location
- `augment_prompt_with_events` — enrich prompts with event context
- `get_event_recommendations` — AI-powered suggestions
- `get_oauth_url` — OAuth authentication

**ajeetraina/meetup-mcp-server** (1 star, JavaScript, MIT) provides general Meetup context management and session tracking.

### Events MCP (Meetup + Luma)

**imagineering-cc/events-mcp** manages events across both **Meetup and Luma** via Playwright browser automation — no paid API tiers required. This is a pragmatic approach: rather than using official APIs (which can be expensive or limited), it automates the browser directly.

## Conference Navigation

### AWS re:Invent Session Navigator

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [manu-mishra/reinvent-mcp-2025](https://github.com/manu-mishra/reinvent-mcp-2025) | 5 | JavaScript | MIT | 13 |

The **most sophisticated conference MCP server.** Provides intelligent access to all 1,843 AWS re:Invent 2025 sessions:

- **search_sessions** / **search_speakers** / **get_session_details**
- Filter by **5 difficulty levels**, **19 job roles**, **19 industries**, **18 topics**, **53 areas of interest**, **10 segments**, **4 session formats**
- Fuzzy matching for flexible queries
- Speaker discovery with session mapping
- MessagePack optimization for sub-second startup
- Pagination support for large result sets

A template for how conference organizers could make their events AI-navigable.

### Tech Conference Agent

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [doozMen/tech-conf-agent](https://github.com/doozMen/tech-conf-agent) | 3 | Swift | MIT | 6 |

Built for **ServerSide.swift 2025 London** — a rare Swift 6.2 MCP implementation with actor-based concurrency. Tools include session listing/searching, speaker profiles, room finding, and schedule queries backed by SQLite with 27+ speaker profiles.

### SITCON 2026 Conference MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sitcon-tw/mcp](https://github.com/sitcon-tw/mcp) | 1 | TypeScript | Apache 2.0 | 10 |

A **student/community conference MCP server** built for SITCON 2026 (Students' Information Technology Conference). Provides:

- **Session tools** — search sessions by title/description/tags/speaker, generate shareable session URLs
- **Speaker tools** — lookup by ID or name
- **Team tools** — search members by team, name, or description/links
- **Conference info** — theme, Code of Conduct, SITCON mission

A good template for how smaller conferences can make their events AI-navigable without building complex infrastructure.

### Event Information MCP

**ajot/event-information-mcp-server** (0 stars, Python) uses DigitalOcean's Gradient AI platform for event discovery with speaker information and schedule management. Supports remote deployment on DigitalOcean App Platform.

## Commercial & Enterprise

**Eventtia** has publicly committed to making their enterprise event platform MCP-accessible, describing "agentic event software" where organizers state outcomes in natural language ("set up registration for 500 VIPs with tiered pricing, approval workflows, and custom badge printing") and AI agents handle configuration. No public server exists yet, but Eventtia's framing — "the competitive question changes from 'which platform has the best interface?' to 'which platform exposes the richest capabilities to agents?'" — signals where the industry is heading.

## What's Missing

The calendar gap has narrowed significantly with Google's official MCP, but event management and ticketing gaps remain substantial:

- **No official ticketing platform servers** — Ticketmaster, Eventbrite, Live Nation, StubHub, Dice, AXS — none have released official MCP servers
- **No virtual event platforms** — Hopin (now RingCentral Events), Zoom Events, Airmeet, Gather, Run The World — zero MCP presence
- **No event check-in** — no badge printing, no attendee scanning, no door management (beyond quick-event-mcp's QR codes)
- **No event logistics** — no catering management, vendor coordination, floor plan tools, or A/V management
- **No venue booking** — no availability systems, room reservation, or space management
- **No event analytics** — no ROI tracking, attendee engagement scoring, or post-event reporting
- **No volunteer management** — no shift scheduling, role assignment, or communication
- **No hybrid event tools** — no streaming integration, virtual/in-person bridging, or breakout room management
- **No festival/multi-day management** — no stage scheduling, artist management, or multi-venue coordination

## The Bottom Line

The event management and ticketing MCP ecosystem remains **split**: calendaring is now officially supported by Google (Developer Preview, 8 tools, remote MCP) alongside mature community options (nspady at 1,100 stars, google_workspace_mcp at 2,200 stars, mcp-ical at 304 stars, plus iCloud Calendar via CalDAV). But event management proper is still early-stage. Most ticketing servers are thin read-only wrappers around discovery APIs. The few write-capable servers (joshuachestang's Eventbrite, The Events Calendar) are promising but low-traction.

The biggest remaining opportunity: **official MCP servers from major ticketing platforms.** Eventbrite alone processes billions of dollars in ticket sales — an official MCP server enabling agents to create events, manage attendees, and track sales would be immediately useful. Eventtia's "agentic event software" vision points the way, but the industry hasn't followed yet.

**Rating: 3.5 / 5** — Google's official Calendar MCP is a landmark, but it strengthens an already-mature subcategory. Ticketing, event logistics, and virtual events remain wide open.

*This review was last edited on 2026-04-26 using Claude Opus 4.6 (Anthropic).*
