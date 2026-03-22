---
title: "Event Management & Ticketing MCP Servers — Eventbrite, Ticketmaster, Meetup, Google Calendar, and More"
date: 2026-03-15T20:00:00+09:00
description: "Event management and ticketing MCP servers let AI agents discover live events, manage calendars, create event pages, and automate registration workflows. We found 35+ servers across 6 subcategories. nspady/google-calendar-mcp: 1,100 stars, TypeScript, MIT, 12 tools — multi-account Google Calendar with smart scheduling, free/busy queries, and intelligent import from images/PDFs. delorenj/mcp-server-ticketmaster: 23 stars, TypeScript, MIT, 6 tools — Ticketmaster Discovery API with event/venue/attraction search and dual output formats. Omar-V2/mcp-ical: 278 stars, Python, MIT — natural language macOS Calendar control with recurring events and smart reminders. joshuachestang/eventbrite-mcp-server: 2 stars, JavaScript, MIT, 8 tools — full event lifecycle management with create/update/publish/cancel. PeterShin23/seatgeek-mcp: 3 stars, TypeScript, MIT, 4 tools — event discovery with venue seating layouts and performer recommendations. the-events-calendar/mcp-server: 1 star, TypeScript — official WordPress Events Calendar plugin with unified CRUD for events, venues, organizers, and tickets. Gaps: no official Eventbrite/Ticketmaster/Live Nation servers, no StubHub, no Dice/DICE.fm, no event check-in/badge printing, no virtual event platforms (Hopin/Zoom Events), no catering/vendor management. Rating: 3.5/5."
og_description: "Event management & ticketing MCP servers: Google Calendar (1,100 stars, 12 tools), Ticketmaster (23 stars, event discovery), mcp-ical (278 stars, macOS Calendar), Eventbrite (8 tools, full lifecycle), SeatGeek (4 tools, seating layouts), WordPress Events Calendar (official). 35+ servers across calendaring, ticketing, event platforms, and conference navigation. Rating: 3.5/5."
content_type: "Review"
card_description: "Event management and ticketing MCP servers across calendaring, ticket discovery, event platforms, conference navigation, and community events. The dominant subcategory is **calendaring** — Google Calendar alone has 10+ competing implementations, led by nspady/google-calendar-mcp (1,100 stars, TypeScript, MIT, 12 tools) with multi-account support, smart scheduling, free/busy queries, recurring event handling, and intelligent import from images/PDFs/web links. shade-solutions/calender-mcp takes it further with 60+ tools including analytics, batch operations, working location/focus time, and AI-powered event extraction. Apple Calendar has strong coverage through Omar-V2/mcp-ical (278 stars, Python, MIT) for natural language macOS Calendar control, shadowfax92/apple-calendar-mcp for full CRUD, and somethingwithproof/calendar-mcp for search and management. Microsoft Outlook is served by anoopt/outlook-meetings-scheduler-mcp-server (Microsoft Graph API, attendee discovery) and elyxlz/microsoft-mcp (Outlook + Calendar + OneDrive + Contacts). Calendar-mcp.com provides a hosted iCal (.ics) remote MCP server compatible with any calendar platform. For ticket discovery, delorenj/mcp-server-ticketmaster (23 stars, TypeScript, MIT) is the most popular — 6 tools searching events, venues, and attractions via the Ticketmaster Discovery API with JSON and text output formats. mmmaaatttttt/mcp-live-events (2 stars, Python) focuses specifically on live music events via Ticketmaster, while mochow13/ticketmaster-mcp-server (1 star, TypeScript, ISC) implements Streamable HTTP transport. PeterShin23/seatgeek-mcp (3 stars, TypeScript, MIT, 4 tools) offers event discovery with performer-based recommendations and detailed venue seating layouts including sections and rows — unique in the category. Eventbrite has the most implementations of any event platform: joshuachestang/eventbrite-mcp-server (2 stars, JavaScript, MIT, 8 tools) provides full event lifecycle management — create, list, get, update, publish, cancel events plus venue creation and category listing. vishalsachdev/eventbrite-mcp (2 stars, API Blueprint, MIT) focuses on event listing and analytics with planned attendee management. punkpeye/eventbrite-mcp (1 star, JavaScript, MIT, 4 tools) provides search, details, categories, and venue lookup. Community events are covered by d4nshields/mcp-meetup (0 stars, Python, MIT, 4 tools) integrating Meetup.com with Claude via search, prompt augmentation, recommendations, and OAuth, and ajeetraina/meetup-mcp-server (1 star, JavaScript, MIT) for general Meetup context management. imagineering-cc/events-mcp manages events across both Meetup and Luma via Playwright browser automation — no paid API tiers required. The Events Calendar official MCP server (the-events-calendar/mcp-server, 1 star, TypeScript) bridges WordPress sites running The Events Calendar plugin with AI assistants, providing unified CRUD for events (tribe_events), venues (tribe_venue), organizers (tribe_organizer), and tickets (tribe_rsvp_tickets/tec_tc_ticket) — notable as an official vendor server. the-plus-io/quick-event-mcp (0 stars, JavaScript, proprietary free-to-use) takes a different approach: a hosted remote MCP server that generates complete event landing pages with registration forms, ticket categories, QR code check-in, and email templates for conferences, workshops, parties, meetups, and weddings — the only server that creates event pages from scratch. Conference navigation is a niche but practical subcategory. manu-mishra/reinvent-mcp-2025 (5 stars, JavaScript, MIT, 13 tools) provides intelligent access to all 1,843 AWS re:Invent sessions with fuzzy search, speaker discovery, filtering by level/role/industry/topic/segment, and MessagePack optimization. doozMen/tech-conf-agent (3 stars, Swift, MIT, 6 tools) was built for ServerSide.swift 2025 London with session search, speaker profiles, room finding, and schedule queries backed by SQLite. ajot/event-information-mcp-server (0 stars, Python) uses DigitalOcean's Gradient AI for event discovery with speaker and schedule information. Eventtia has publicly committed to making their enterprise event platform MCP-accessible, describing 'agentic event software' where AI agents handle complex configuration tasks from natural language — potentially the most ambitious commercial approach, though no public server exists yet. Gaps are significant: no official servers from Ticketmaster, Eventbrite, Live Nation, StubHub, Dice, or any major ticketing platform. No virtual event platforms (Hopin, Zoom Events, Airmeet, Gather). No event check-in, badge printing, or attendee management beyond basic listing. No catering, vendor coordination, or event logistics. No venue booking or availability systems. No event analytics or ROI tracking. No volunteer management. No hybrid/virtual event streaming integration. The calendar subcategory is mature and well-served, but the event management and ticketing ecosystem is still early-stage — most servers are thin API wrappers with read-only discovery, and the platforms that would benefit most from MCP integration (Eventbrite, Ticketmaster, Live Nation) haven't released official servers. The category earns 3.5/5 — strong calendaring but underdeveloped event management."
last_refreshed: 2026-03-15
---

Event management and ticketing MCP servers let AI agents discover live events, manage calendars, create event pages, and automate registration workflows. The ecosystem splits sharply: **calendaring is mature** (Google Calendar alone has 10+ MCP implementations), while **ticketing and event management are early-stage** with mostly read-only API wrappers.

This review covers the **event management and ticketing** vertical — calendar scheduling, ticket discovery, event platforms, community events, and conference navigation. For meeting/video call servers, see our [Communication & Messaging MCP review](/reviews/communication-messaging-mcp-servers/). For restaurant/venue booking, see our [Food & Restaurant MCP review](/reviews/food-restaurant-mcp-servers/).

The headline finding: **calendaring dominates**, with Google Calendar's nspady/google-calendar-mcp reaching 1,100 stars. But outside calendaring, the category lacks the official vendor participation seen in other verticals — no Ticketmaster, Eventbrite, or Live Nation official servers exist.

## Calendar & Scheduling

### Google Calendar MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nspady/google-calendar-mcp](https://github.com/nspady/google-calendar-mcp) | 1,100 | TypeScript | MIT | 12 |

The **most popular calendar MCP server** and one of the highest-starred in this entire review. Features:

- **Multi-account** — connect multiple Google accounts simultaneously
- **Multi-calendar** — manage events across different calendars
- **Smart scheduling** — detect overlapping events across accounts
- **Free/busy queries** — check availability before scheduling
- **Recurring events** — modify single instances or entire series
- **Intelligent import** — extract calendar data from images, PDFs, and web links
- **RSVP control** — accept/decline/tentative with per-instance granularity

The intelligent import feature is particularly useful — paste a screenshot of a conference schedule and it creates calendar events automatically.

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
| [Omar-V2/mcp-ical](https://github.com/Omar-V2/mcp-ical) | 278 | Python | MIT | ~5 |

The **most popular Apple Calendar MCP server.** Uses PyObjC to interact directly with macOS Calendar (not iCloud API), supporting:

- Natural language event creation ("lunch with Alex next Tuesday at noon")
- Custom calendar selection
- Smart reminders
- Recurring events
- Schedule queries

Two additional Apple Calendar implementations exist: **shadowfax92/apple-calendar-mcp** for full CRUD via standardized MCP interface, and **somethingwithproof/calendar-mcp** for search and management.

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
| [delorenj/mcp-server-ticketmaster](https://github.com/delorenj/mcp-server-ticketmaster) | 23 | TypeScript | MIT | 6 |

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

### Event Information MCP

**ajot/event-information-mcp-server** (0 stars, Python) uses DigitalOcean's Gradient AI platform for event discovery with speaker information and schedule management. Supports remote deployment on DigitalOcean App Platform.

## Commercial & Enterprise

**Eventtia** has publicly committed to making their enterprise event platform MCP-accessible, describing "agentic event software" where organizers state outcomes in natural language ("set up registration for 500 VIPs with tiered pricing, approval workflows, and custom badge printing") and AI agents handle configuration. No public server exists yet, but Eventtia's framing — "the competitive question changes from 'which platform has the best interface?' to 'which platform exposes the richest capabilities to agents?'" — signals where the industry is heading.

## What's Missing

The gaps in this category are substantial:

- **No official platform servers** — Ticketmaster, Eventbrite, Live Nation, StubHub, Dice, AXS — none have released official MCP servers
- **No virtual event platforms** — Hopin, Zoom Events, Airmeet, Gather, Run The World — zero MCP presence
- **No event check-in** — no badge printing, no attendee scanning, no door management (beyond quick-event-mcp's QR codes)
- **No event logistics** — no catering management, vendor coordination, floor plan tools, or A/V management
- **No venue booking** — no availability systems, room reservation, or space management
- **No event analytics** — no ROI tracking, attendee engagement scoring, or post-event reporting
- **No volunteer management** — no shift scheduling, role assignment, or communication
- **No hybrid event tools** — no streaming integration, virtual/in-person bridging, or breakout room management
- **No festival/multi-day management** — no stage scheduling, artist management, or multi-venue coordination

## The Bottom Line

The event management and ticketing MCP ecosystem is **split personality**: calendaring is genuinely mature (Google Calendar at 1,100 stars, Apple Calendar at 278 stars, multiple Outlook implementations), but event management proper is early-stage. Most ticketing servers are thin read-only wrappers around discovery APIs. The few write-capable servers (joshuachestang's Eventbrite, The Events Calendar) are promising but low-traction.

The biggest opportunity is clear: **official MCP servers from major event platforms.** Eventbrite alone processes billions of dollars in ticket sales — an official MCP server enabling agents to create events, manage attendees, and track sales would be immediately useful. Eventtia's "agentic event software" vision points the way, but the industry hasn't followed yet.

**Rating: 3.5 / 5** — strong calendaring, early-stage event management, significant gaps in ticketing and logistics.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
