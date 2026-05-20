# Calendar & Scheduling MCP Servers — Google Calendar, Outlook, Apple Calendar, Cal.com, Calendly, and More

> Calendar and scheduling MCP servers are giving AI assistants direct access to event management, availability checking, and meeting coordination.


Calendar and scheduling MCP servers are giving AI assistants direct access to event management, availability checking, and meeting coordination. Instead of switching between your IDE and a calendar app, these servers let AI agents create events, find free slots, manage attendees, and coordinate schedules — all through the Model Context Protocol.

The landscape spans seven areas: **Google Calendar** (the most implementations, now including an official server), **Microsoft Outlook/365** (official server now GA), **Apple/macOS Calendar** (navigating a major archival), **CalDAV/iCloud** (standards-based universal access), **scheduling platforms** (Cal.com, Calendly — both with official servers), **multi-provider unified** servers, and **task scheduling** automation. Part of our **[Communication & Collaboration](/categories/communication-collaboration/)** and **[Business & Productivity](/categories/business-productivity/)** MCP categories.

## What's New (April–May 2026)

**Google shipped an official Calendar MCP server.** `calendarmcp.googleapis.com` is now in Developer Preview — resolving the category's most-cited gap. The server provides 8 tools (list calendars, list/create/update/delete events, check availability, RSVP, suggest meeting times) via OAuth 2.0. Authentication inherits the same permissions and data governance as the authenticated user. This is part of a broader Google initiative for official MCP support across Google services, with Google AI Studio now including Workspace integrations and Gemini Spark (announced at Google I/O May 19–20) planning MCP expansion "over the summer." The Calendar MCP documentation was published April 22, 2026 at `developers.google.com/workspace/calendar/api/guides/configure-mcp-server`.

**google_workspace_mcp doubled in stars and shipped four releases.** taylorwilsdon's server went from 1,100 to **2,400 stars** (+118%) with releases v1.20.1 through v1.21.0 (May 17). Notable calendar-relevant changes: calendar date-parsing robustness in v1.21.0 (defensive handling for malformed dates from LLM clients, including double-encoded JSON and literal "null" strings), JWT signing key support for OAuth token passthrough (run without sharing your Google OAuth client secret), and HTML escaping in OAuth callbacks (XSS prevention). Also added: shared Drives enumeration, Apps Script execution, domain-wide delegation with per-request impersonation.

**Microsoft Agent 365 CalendarTools went Generally Available May 1, 2026.** Previously in preview; now production-ready for commercial customers. The CalendarTools endpoint (`agent365.svc.cloud.microsoft`) includes recurring event support, Teams meeting creation, attendee notification on cancel, multi-user availability checking, and free/busy schedule retrieval. Starting June 2026, Microsoft Defender will provide asset context mapping for each Agent 365 deployment — tracking which MCP servers are configured, which identities are associated, and which cloud resources those identities can reach. Cross-cloud registry sync with AWS Bedrock and Google Cloud connections entered public preview.

**Softeria ms-365-mcp-server: 90+ tools became 200+ tools, extensive security hardening.** Stars grew from 635 to **720** and the server went from v0.36 to v0.111 (May 19) — 11+ releases in the review window. The tool count claim is now "200+ tools covering most of the Microsoft Graph API surface." Security-focused releases: log file permissions restricted to owner-only (v0.106.2), redirect_uri validation before forwarding to Microsoft as an SSRF mitigation (v0.107.1), tool scope filtering (v0.109.0), and strict account pinning to prevent account-switching attacks (v0.110.0). Pluggable auth cache storage added v0.111.0.

**Two calendar security vulnerabilities to know.** CVE-2026-26118 (CVSS 8.8, High) is a Server-Side Request Forgery in Microsoft MCP server deployments — patched in Microsoft's March 10, 2026 Patch Tuesday. Softeria's SSRF mitigation patches (May 2026) appear to be a direct response to this CVE class. Separately, CVE-2026-30623 is a critical command injection flaw in Anthropic's MCP SDK (Python, TypeScript, Java, Rust) — affects any calendar MCP server built on the Anthropic SDK and over 150M downloads ecosystem-wide.

**WebMCP proposed as open web standard** at Google I/O 2026 — a browser-based API for AI agents to execute tasks via JavaScript functions and HTML forms. Not calendar-specific but directly relevant to how scheduling AI will operate in browsers going forward.

**temporal-cortex/mcp** is a new infrastructure-focused calendar MCP server with novel reliability architecture.

The headline findings: **Google finally has an official Calendar MCP** (Developer Preview) — the single biggest change from April. **google_workspace_mcp doubled** and is now the leading community Google server by star count. **Microsoft Agent 365 is GA**, adding enterprise-grade governance. **Softeria's community M365 server has grown from 90+ to 200+ tools** with significant security hardening. The security picture has two new CVEs to track.

## Google Calendar

### Google Calendar MCP Server (Official — Developer Preview)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Google Calendar API MCP](https://developers.google.com/workspace/calendar/api/guides/configure-mcp-server) | — | — | — | 8 |

**NEW — Official.** Google's official Calendar MCP server at `calendarmcp.googleapis.com` launched in Developer Preview as of April 22, 2026, resolving the category's longest-standing gap. The 8 tools cover core calendar operations: list calendars, list events, check availability, create/update/delete events, RSVP to invitations, and suggest available meeting times.

Authentication uses OAuth 2.0 with scope-based access control — the server inherits the same data governance permissions as the authenticated user. A usage quota update (May 1, 2026) introduced a new tiering model aligned with Google's standardized model for agent tools and APIs.

As a Developer Preview, this is not yet GA. Feature depth is lighter than leading community servers (8 tools vs. nspady's 12 or taylorwilsdon's 50+). But the official provenance matters for enterprise and regulated deployments, and Google's MCP commitment is clearly deepening given the broader Google AI Studio + Workspace integrations and the Gemini Spark MCP roadmap.

### google-calendar-mcp (nspady)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nspady/google-calendar-mcp](https://github.com/nspady/google-calendar-mcp) | 1,100 | TypeScript | MIT | 12 |

The standout dedicated Google Calendar MCP server. Supports **multi-account** connections (work, personal, etc.) with simultaneous querying across all calendars, plus **cross-account conflict detection** that catches overlapping events across different Google accounts.

The 12 tools cover the full calendar lifecycle: list calendars, list events, search events, create/update/delete events, respond to attendance, check free/busy availability, and manage accounts. Advanced features include recurring event modification, natural language scheduling understanding, and intelligent event import from images, PDFs, and web links. No new releases since v2.6.1 (March 2, 2026) — the project has gone quiet for roughly 7 weeks. Still the best dedicated Google Calendar integration, though Google's official server will likely close the gap over time.

### google_workspace_mcp (taylorwilsdon)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | 2,400 | Python | — | 50+ across services |

The most feature-complete and fastest-growing Google Workspace MCP server. Stars more than doubled from 1,100 to **2,400** in the review window, with four releases (v1.20.1–v1.21.0, April 28–May 17). Covers Gmail, **Calendar**, Docs, Sheets, Slides, Chat, Forms, Tasks, Search, and Drive in a single server.

Post-April updates relevant to calendar: **calendar date-parsing robustness** in v1.21.0 (defensive handling of malformed dates including double-encoded JSON and literal "null" strings from LLM clients), **JWT signing key OAuth token passthrough** (deploy without sharing your Google OAuth client secret), and domain-wide delegation with per-request impersonation for organization-wide deployments. Also fixed: HTML escaping in OAuth callbacks (XSS prevention in v1.20.1), shared Drives enumeration, OAuth port auto-resolution for multi-process environments.

This is now the natural first choice if you use or plan to use other Google Workspace services through MCP. For pure calendar-focused use cases, nspady's dedicated server has more calendar-specific depth (12 vs. 50+ spread across 10 services).

### calendar-mcp (deciduus)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [deciduus/calendar-mcp](https://github.com/deciduus/calendar-mcp) | 23 | Python | AGPL-3.0 / Commercial | 12 |

A Python-native alternative with OAuth 2.0 and automatic token management. Unique features: **mutual meeting slot detection** across multiple calendars, **daily busyness analysis**, and **attendee response tracking**. The dual AGPL-3.0/Commercial license suits both open-source and enterprise use. The busyness analysis tool is rare across all calendar MCP servers — it provides a structured breakdown of how packed a day is, useful for AI agents making scheduling decisions.

### mcp-google-calendar (guinacio)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [guinacio/mcp-google-calendar](https://github.com/guinacio/mcp-google-calendar) | 9 | Python | MIT | 8 |

A lighter Python implementation with **automatic time conflict detection**, **recurring event support** (iCalendar RRULE format), and **timezone-aware scheduling**. The 8 tools cover event CRUD, calendar listing, timezone info, current date retrieval, and availability checking.

### Other Google Calendar Implementations

Several additional Google Calendar MCP servers exist with specialized approaches:

- **shade-solutions/calender-mcp** — Built with Smithery, emphasizes travel time considerations
- **markelaugust74/mcp-google-calendar** — Focused implementation for event creation and management
- **surana-mudit/google-calendar-mcp** — Minimal Google Calendar MCP server
- **galacoder/mcp-google-calendar** — Alternative implementation listed on Awesome MCP Servers

Google Calendar now has the most MCP server implementations of any calendar platform — 6+ community servers plus the new official server — reflecting both platform dominance and API accessibility.

## Microsoft Outlook / Microsoft 365

### Microsoft 365 CalendarTools (Official — GA)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [microsoft/mcp — CalendarTools](https://github.com/microsoft/mcp) | 2,800+ (mono-repo) | C# | — | Multiple |

**Official** remote MCP server from Microsoft, **Generally Available as of May 1, 2026**. Hosted at `agent365.svc.cloud.microsoft/agents/tenants/{tenant_id}/servers/mcp_CalendarTools`. No local setup — AI clients connect directly to Microsoft infrastructure with tenant-scoped authentication via Microsoft Graph Calendar APIs.

Calendar capabilities: create events (including recurring events and Teams meetings), update/cancel events with attendee notification, decline invitations, suggest meeting times based on multi-user availability, get free/busy schedules, retrieve calendar occurrences in time ranges.

Starting June 2026, Microsoft Defender will add asset context mapping — tracking which MCP servers are configured per deployment, which identities are associated, and which cloud resources those identities can reach. Cross-cloud registry sync with AWS Bedrock and Google Cloud entered public preview alongside the GA announcement.

### ms-365-mcp-server (Softeria)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Softeria/ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server) | 720 | TypeScript | MIT | 200+ |

The most comprehensive community Microsoft 365 MCP server, now with **200+ tools covering most of the Microsoft Graph API surface** (was "90+ tools" in April). Stars grew from 635 to **720**. The server went from v0.36 to v0.111 (May 19) — 11+ releases in the window, mostly adding tools and security hardening.

Key security releases in May 2026: log file permissions restricted to owner-only (v0.106.2), redirect_uri validation before forwarding to Microsoft as an SSRF mitigation (v0.107.1, directly relevant to CVE-2026-26118 class), filter tools by allowed scopes (v0.109.0), and strict account pinning to prevent account-switching attacks (v0.110.0). Pluggable auth cache storage added in v0.111.0.

Core differentiators remain: **dynamic discovery** that keeps initial context small and cuts token usage, **multi-account support** where a single server instance handles multiple Microsoft accounts, and configurable **presets** to load only needed tool groups.

### Outlook Calendar MCP (merajmehrabi)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [merajmehrabi/Outlook_Calendar_MCP](https://github.com/merajmehrabi/Outlook_Calendar_MCP) | 33 | VBScript/JS | MIT | 6 |

A **Windows-only** local implementation interfacing directly with the Outlook desktop client via VBScript. Works without Microsoft Graph API credentials — if Outlook is installed and logged in, it works. The find_free_slots capability is practical for scheduling without API setup. Requires Node.js, the Outlook desktop app, and VBScript support (mandatory on Windows 11 24H2+).

### Office 365 MCP Server (hvkshetry)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [hvkshetry/office-365-mcp-server](https://github.com/hvkshetry/office-365-mcp-server) | 12 | JavaScript | MIT | 24 |

24 consolidated tools spanning email, **calendar**, Teams, OneDrive/SharePoint, contacts, Planner, To Do, groups, and directory services — all through the Graph API. One server replaces what would otherwise be 5–6 separate MCP servers.

### Other Outlook/M365 Implementations

- **ryaker/outlook-mcp** — Connects Claude with M365 via Graph API and Power Automate API
- **XenoXilus/outlook-mcp** — Email, calendar, and SharePoint integration through Graph API
- **elyxlz/microsoft-mcp** — Minimal, powerful server for Graph API covering Outlook, Calendar, and OneDrive
- **ampcome-mcps/outlook-mcp** — Comprehensive email, contact, calendar, and folder management
- **kacase/mcp-outlook** — Calendar events, scheduling, email reading and sending
- **anoopt/outlook-meetings-scheduler-mcp-server** — Focused specifically on meeting scheduling with attendee support
- **Workato Outlook Calendar MCP** — Pre-built platform integration (March 2026): review calendar, check availability, schedule and adjust meetings; runs within Workato's automation platform

## Apple / macOS Calendar

### apple-mcp (supermemoryai) — ARCHIVED

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [supermemoryai/apple-mcp](https://github.com/supermemoryai/apple-mcp) | 3,100 | TypeScript | MIT | 7 app integrations |

**Archived January 1, 2026.** The most-starred server in this review is now read-only at 3,100 stars — no bug fixes, security updates, or new features. Calendar was one of seven Apple-native app integrations (Messages, Notes, Contacts, Mail, Reminders, **Calendar**, Maps). The README mentions supermemory MCP (`mcp.supermemory.ai`) but does not formally designate it as a replacement — that product is a memory/knowledge management service, not a calendar service.

Community forks have emerged with different specializations: **adamzaidi/icloud-mcp** (65 tools, extensive email capabilities, 45 commits, most comprehensive active fork), an enterprise-grade **icloud-calendar-mcp** (OWASP security compliance, 768 tests), and **MrGo2/icloud-mcp** (broadest service coverage, dual local/cloud modes). None have gained significant star counts — the 3,100-star vacuum from apple-mcp's archival remains unfilled by any dominant successor.

### mcp-ical (Omar-V2)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Omar-V2/mcp-ical](https://github.com/Omar-V2/mcp-ical) | 311 | Python | MIT | Multiple |

The most popular dedicated macOS Calendar MCP server, growing from 278 to **311 stars**. Uses PyObjC to interface directly with macOS Calendar (EventKit) — no separate API credentials needed. Supports event creation with location/notes/reminders/recurring patterns, schedule querying, availability checking, and multi-calendar support including Google Calendar accounts synced through macOS Calendar.

Note: the project itself has not been updated since February 2025 — star growth is organic community interest, not active development.

### Other Apple Calendar Implementations

- **somethingwithproof/calendar-mcp** — MCP server for Apple Calendar on macOS with full event lifecycle
- **shadowfax92/apple-calendar-mcp** — macOS Calendar access through EventKit

## CalDAV / iCloud Calendar

### caldav-mcp (dominik1001)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dominik1001/caldav-mcp](https://github.com/dominik1001/caldav-mcp) | 57 | TypeScript | MIT | 4 |

The universal calendar server — **any CalDAV-compliant calendar** works here: Nextcloud, Radicale, Baikal, iCloud, FastMail, Synology Calendar, and dozens more. The 4 tools (`create-event`, `list-events`, `delete-event`, `list-calendars`) cover essential operations. For self-hosted calendar users, this is the obvious choice.

### iCloud Calendar MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [localhost433/icloud-mcp](https://github.com/localhost433/icloud-mcp) | — | — | — | Multiple |
| [rgabriel/mcp-icloud-calendar](https://lobehub.com/mcp/rgabriel-mcp-icloud-calendar) | — | — | — | Multiple |

Two implementations targeting iCloud Calendar specifically via CalDAV. **icloud-mcp** provides an HTTP MCP server with list/read/create/update/delete operations using an iCloud app-specific password. **mcp-icloud-calendar** connects to Apple iCloud Calendar for similar operations.

## Scheduling Platforms

### Cal.com MCP Server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [calcom/cal-mcp](https://github.com/calcom/cal-mcp) | 22 | TypeScript | — | 9 |

**Official** MCP server from Cal.com. Stars grew from 18 to **22**. The 9 core tools cover the booking lifecycle: `getBooking`, `getBookings`, `createBooking`, `rescheduleBooking`, `cancelBooking`, `getEventTypes`, `getEventTypeById`, `updateEventType`, `deleteEventType`. The Cal.com docs now officially reference MCP server integration, and Zapier offers a Cal.com MCP integration at `zapier.com/mcp/calcom`.

Note: the repository has seen no commits in 2026, which conflicts with its "in active development" documentation status. Community alternatives include **Danielpeter-99/calcom-mcp** (FastMCP implementation) and **bcharleson/calcom-cli** (61 tools, Cal.com API v2 full coverage, Zod-validated input schemas, structured JSON output, automatic retry with exponential backoff).

### Calendly MCP Server (Official)

| Server | Stars | Type | License | Tools |
|--------|-------|------|---------|-------|
| [Calendly MCP](https://developer.calendly.com/calendly-mcp-server) | — | Hosted | — | Multiple |

**Official** hosted MCP server from Calendly at `mcp.calendly.com`, launched March 11, 2026. **No self-hosting or local deployment** — Calendly runs the infrastructure. Authentication uses **DCR (RFC 7591)** — no pre-registered OAuth app or secrets needed. Works on **all Calendly plans including free**. Compatible with ChatGPT, Claude, and any MCP-compatible client.

AI assistants can check/update availability, generate scheduling links, manage scheduled events, view meetings, and book/cancel via natural language. No feature changes were announced post-April 22 — the March launch details are now confirmed and stable.

Community alternatives remain: **universal-mcp/calendly** (API key/OAuth) and **bcharleson/calendly-cli** (40 tools covering authentication, scheduling, availability, webhooks, routing forms, groups, and data compliance — Zod-validated, with automatic retry).

### When2Meet MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [joyce-yuan/when2meet-mcp](https://github.com/joyce-yuan/when2meet-mcp) | — | — | — | Multiple |

Lets AI assistants fill out When2Meet availability polls. Features automatic event detail extraction from When2Meet URLs, natural language availability specification ("I'm free Monday through Wednesday afternoons"), and automated availability marking. Solves a genuine pain point — When2Meet's grid UI is tedious to fill out manually.

## Multi-Provider Unified Servers

### temporal-cortex/mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [temporal-cortex/mcp](https://github.com/temporal-cortex/mcp) | 8 | — | — | 18 |

**NEW.** An infrastructure-focused calendar MCP server with a distinct reliability architecture. Key differentiators:

**Atomic booking via Two-Phase Commit** — locks the slot, verifies availability, writes the event, then releases the lock. Prevents race-condition double-bookings that occur when multiple AI agents attempt to schedule the same slot simultaneously.

**Deterministic RRULE expansion** — expands recurring event rules ("third Tuesday monthly across DST transitions") algorithmically rather than relying on LLM inference, avoiding hallucinated scheduling errors.

**TOON (Token-Optimized Object Notation)** output format — approximately 40% fewer tokens than standard JSON responses, reducing cost for long scheduling sessions.

Multi-provider support (Google Calendar, Microsoft Outlook, CalDAV) with 18 tools across 5 architectural layers. Also accessible via REST, A2A JSON-RPC, and browser. Available as `npx @temporal-cortex/cortex-mcp`. v0.9.1 (March 2026). Still very low star count (8) but technically differentiated.

### calendar-mcp (MarimerLLC)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MarimerLLC/calendar-mcp](https://github.com/MarimerLLC/calendar-mcp) | 11 | C# | MIT | 14 |

A unified MCP server aggregating **Microsoft 365, Outlook.com, Google Workspace, ICS feeds, and JSON calendar files** in a single interface. 14 tools spanning account listing, email operations, calendar management, contact handling, and availability checking across all connected providers. The key value: instead of configuring separate MCP servers for work (M365), personal (Google), and subscription (ICS) calendars, this provides a unified view. Supports both local stdio and containerized HTTP deployment.

## Task Scheduling

### scheduler-mcp (PhialsBasement)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [PhialsBasement/scheduler-mcp](https://github.com/PhialsBasement/scheduler-mcp) | 54 | Python | MIT | 12 |

A **task automation scheduler** built on MCP, not a calendar server. Uses cron expressions to schedule shell commands, API calls, AI content generation tasks, and desktop notifications. Four task types: **command** (shell), **API** (HTTP requests), **AI** (content generation), and **reminder** (desktop notifications). Cross-platform (Windows, macOS, Linux). Useful for AI agents that need to schedule recurring operations rather than calendar events.

## Security Notes

Two CVEs directly affect this category:

**CVE-2026-26118 (CVSS 8.8, High)** — Server-Side Request Forgery in Microsoft MCP server deployments, including CalendarTools. Patched in Microsoft's March 10, 2026 Patch Tuesday. Softeria's May 2026 SSRF mitigation patches (v0.107.1 redirect_uri validation) appear to be a direct response to this CVE class.

**CVE-2026-30623 (critical)** — Command injection via Anthropic's MCP SDK stdio (Python, TypeScript, Java, Rust). Affects any calendar MCP server built on the Anthropic SDK. Over 150M downloads ecosystem-wide. Disclosed by OX Security (April 2026); documented by liteLLM.

## What's Missing

The calendar MCP ecosystem's gap list has shortened:

- **No official Apple Calendar MCP server** — the community flagship (apple-mcp, 3,100 stars) was archived January 2026, leaving macOS calendar users with no dominant maintained option (mcp-ical is functional but not actively developed; community forks are fragmented)
- **AI-native scheduling platforms** — Clockwise, Reclaim, and Motion still lack public MCP presence; Clockwise reportedly introduced a server in September 2025 but it's not publicly available
- **Group scheduling** — no Doodle MCP server; When2Meet is covered but with limited adoption
- **Enterprise scheduling** — no Kronos/UKG, Deputy, or workforce management scheduling servers
- **Room/resource booking** — no dedicated meeting room or resource booking MCP servers
- **Calendar analytics** — few servers provide insights beyond basic event data (deciduus's busyness analysis remains a rare exception)

Previously listed gap now resolved: ~~No official Google Calendar MCP server~~ — Google shipped a Developer Preview server at `calendarmcp.googleapis.com` (April 22, 2026).

## Bottom Line

**Rating: 4.0→4.5 / 5** — The biggest single change in this review window is Google's official Calendar MCP server entering Developer Preview. The April 22 review called "No official MCP server from Google or Apple" the primary gap. One of those two is now resolved.

**Google Calendar** now has three strong options: the official Developer Preview server (8 tools, enterprise provenance, OAuth 2.0), nspady's dedicated community server (1,100 stars, 12 tools, cross-account conflict detection), and taylorwilsdon's google_workspace_mcp (2,400 stars, v1.21.0, 10+ Google services). **Microsoft** is stronger still — the official CalendarTools is now GA with Defender governance coming in June, and Softeria's community server grew from 90+ to 200+ tools with meaningful security hardening. **Scheduling platforms** have stabilized at three official servers: Microsoft (GA), Calendly (hosted, all plans), and Cal.com (official but low 2026 commit activity). **Apple Calendar** remains the weak point — apple-mcp is archived, no official replacement exists, and community forks are fragmented.

The bump to 4.5 reflects: Google's official server resolving the category's most-cited gap, google_workspace_mcp's rapid growth and active development, Microsoft Agent 365 reaching GA, and Softeria's security hardening making the community M365 option more enterprise-appropriate. The gap to 5.0: Apple has no official MCP and the community landscape is fragmented; the STDIO design flaw (CVE-2026-30623) affects the entire ecosystem; AI-native scheduling platforms (Clockwise, Reclaim, Motion) still lack public MCP presence.

*This review was last edited on 2026-05-20 using Claude Sonnet 4.6 (Anthropic).*

