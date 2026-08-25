# Best Calendar & Scheduling MCP Servers in 2026 — Google Calendar vs Outlook vs Apple vs Booking Platforms

> We compared 25+ calendar and scheduling MCP servers across Google Calendar, Microsoft Outlook, Apple Calendar, Cal.com, Calendly, and CalDAV.


Calendar integration is one of the most practical MCP use cases. Checking availability, scheduling meetings, finding conflicts across accounts — these are tasks AI assistants can genuinely make faster. The ecosystem has responded with servers for every major calendar platform.

The landscape has shifted dramatically since March. **Google finally shipped an official managed Calendar MCP server** — the biggest gap we flagged is now filled (8 tools, remote, no local setup). **Microsoft launched Work IQ Calendar** (Preview) as its dedicated calendar MCP offering. Community servers continue to thrive alongside: **nspady/google-calendar-mcp** (1,175 stars, 13 tools) and **Softeria/ms-365-mcp-server** (932 stars, 300+ tools). **Booking platforms** Calendly and Cal.com both have official servers, with Cal.com's hosted server (mcp.cal.com) now exposing 34 tools.

What surprised us: **both Google and Microsoft now have official hosted calendar MCP servers**, but the community alternatives remain competitive — nspady's server has more tools (13 vs 8) and multi-account support that Google's official server doesn't yet match. Meanwhile, **Cal.com quietly expanded from 9 to 34 tools**, making it the most feature-dense booking platform MCP server.

**Disclosure:** Our recommendations are based on research — analyzing documentation, GitHub repositories, community feedback, and published benchmarks. We have not hands-on tested every server in this guide.

## What Changed (March → April 2026)

| Server | Change |
|--------|--------|
| **Google Official Calendar MCP** | **NEW** — 8 tools, managed remote, no local setup needed |
| **Microsoft Work IQ Calendar** | **NEW** — Preview, hosted MCP for M365 Calendar |
| nspady/google-calendar-mcp | 12→13 tools (bulk create-events added) |
| taylorwilsdon/google_workspace_mcp | Stateless mode fix, meeting URL extraction, re-auth improvements |
| Softeria/ms-365-mcp-server | 547→614 stars, v0.36.0, April token cache + delegated scope fixes |
| MarkusPfundstein/mcp-gsuite | 477→428 stars |
| Cal.com | 9→34 tools, full API endpoint coverage |
| Calendly | Dynamic Client Registration (DCR), no pre-registration needed |
| FradSer/mcp-server-apple-events | Split into separate Reminders repo, 55→61 stars |
| MarimerLLC/calendar-mcp | Pre-built binaries, .NET 10, configurable routing |

## At a Glance: Top Picks

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| **Google Calendar (official)** | [Google Workspace Calendar MCP](https://developers.google.com/workspace/calendar/api/guides/configure-mcp-server) | Official | — |
| **Google Calendar (community)** | [nspady/google-calendar-mcp](https://github.com/nspady/google-calendar-mcp) | 1,175 | [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) (489, Gmail+Calendar) |
| **Google Calendar (full Workspace)** | [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | 3,067 | [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) (489) |
| **Microsoft 365 / Outlook (official)** | [Work IQ Calendar](https://learn.microsoft.com/en-us/microsoft-agent-365/mcp-server-reference/calendar) | Official | [microsoft/work-iq](https://github.com/microsoft/work-iq) (CLI) |
| **Microsoft 365 / Outlook (community)** | [Softeria/ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server) | 932 | [hvkshetry/office-365-mcp-server](https://github.com/hvkshetry/office-365-mcp-server) (24 tools) |
| **Apple / macOS** | [Omar-V2/mcp-ical](https://github.com/Omar-V2/mcp-ical) | 326 | [FradSer/mcp-server-apple-events](https://github.com/FradSer/mcp-server-apple-events) (187) |
| **Booking (Calendly)** | [Calendly MCP](https://developer.calendly.com/calendly-mcp-server) | Official | — |
| **Booking (Cal.com)** | [Cal.com MCP](https://cal.com/docs/mcp-server) | Official (hosted) | [calcom/cal-mcp](https://github.com/calcom/cal-mcp) (30, local/self-hosted) |
| **CalDAV / universal** | [madbonez/caldav-mcp](https://github.com/madbonez/caldav-mcp) | 14 | [Cheffromspace/mcp-nextcloud-calendar](https://github.com/Cheffromspace/mcp-nextcloud-calendar) (7) |
| **Multi-provider** | [MarimerLLC/calendar-mcp](https://github.com/MarimerLLC/calendar-mcp) | 21 | — |

## Google Calendar Servers

Google Calendar is the most popular calendar platform for developers, and the MCP ecosystem now has both official and community options.

### Google Workspace Calendar MCP — Official (NEW)

**Type:** Managed Remote MCP | **Backed by:** Google

Google has finally shipped an official managed Calendar MCP server as part of its broader Google Workspace MCP rollout. This was the biggest gap we flagged in March — it's now filled.

**What makes it stand out:**
- **Official Google backing** — guaranteed API compatibility, maintained by Google
- **8 tools** — create_event, delete_event, get_event, list_calendars, list_events, respond_to_event, suggest_time, update_event
- **Managed remote server** — no local installation, no server to maintain, Google hosts everything
- **suggest_time tool** — AI-powered meeting time suggestions based on attendee availability (unique to the official server)
- **Same permissions model** — inherits the user's existing Google Workspace permissions and data governance controls
- **Works with Claude, Gemini CLI, IDEs** — standard MCP client compatibility

**Limitations:**
- Fewer tools than nspady's community server (8 vs 13) — no multi-account, no bulk create, no color management
- Requires Google Cloud project and gcloud CLI setup
- Claude users need Enterprise, Pro, Max, or Team plan for remote MCP
- No tool filtering — you get all 8 tools or none
- Still new — less battle-tested than community alternatives with years of production use

**Best for:** Teams that want official Google support and zero-maintenance hosting. If you need multi-account or bulk operations, the community server is still better.

### nspady/google-calendar-mcp — Community Winner

**Stars:** 1,175 | **Language:** TypeScript | **License:** MIT

The most popular dedicated calendar MCP server. Mature, well-maintained, and still more feature-rich than Google's official server.

**What makes it stand out:**
- **13 tools** — list-calendars, list-events, get-event, search-events, create-event, create-events (bulk), update-event, delete-event, respond-to-event, get-freebusy, get-current-time, list-colors, manage-accounts
- **Bulk event creation** — create-events tool for batch operations (new in 2026)
- **Multi-account support** — manage multiple Google accounts simultaneously with cross-account conflict detection. This alone sets it apart from both the official server and competitors
- **Multi-calendar support** — work across all calendars in each account, not just the primary one
- **Tool filtering** — expose only the tools you need to save context window tokens and improve security
- **Smart imports** — can intelligently create events from images, PDFs, and web links
- **24 releases** — v2.6.2 as of June 2026. Active development with regular feature additions

**Limitations:**
- Google Calendar only — no Outlook, Apple, or other providers
- Requires OAuth2 setup with Google Cloud Console
- No built-in remote/hosted option — runs locally via stdio

**Best for:** Developers who need multi-account support, bulk operations, or tool filtering. More tools than Google's official server.

### MarkusPfundstein/mcp-gsuite — Gmail + Calendar Combo

**Stars:** 489 | **Language:** Python | **License:** MIT

A focused Google suite server covering Gmail and Calendar. Less scope than the full Workspace server, but well-targeted for the two services developers use most.

**What makes it stand out:**
- **Gmail + Calendar in one server** — email search, retrieval, drafting, and calendar event management
- **Calendar tools** — create events, list events within time ranges, delete events
- **Attachment handling** — save email attachments directly
- **Well-maintained** — 98 forks, regular community contributions

**Limitations:**
- Calendar tools are more basic than nspady's (no freebusy, no multi-account, no event updates)
- Requires external JSON config files for OAuth and account setup
- Python dependency

**Best for:** Developers who want both Gmail and Calendar access in a single server without the full Workspace suite.

### taylorwilsdon/google_workspace_mcp — The Full Suite

**Stars:** 3,067 | **Language:** Python | **License:** MIT

Covers Gmail, Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Search, and Drive. Already covered in our [spreadsheet comparison](/guides/best-spreadsheet-mcp-servers/) and [file & storage comparison](/guides/best-file-storage-mcp-servers/), but worth mentioning here for its Calendar capabilities.

**Calendar-specific features:**
- Event creation with timezone support, transparency (busy/free), visibility settings
- Up to 5 custom reminders per event
- Google Meet auto-generation with meeting URL extraction from conferenceData and hangoutLink (April 2026)
- Attendee management and guest permission controls
- FreeBusy queries for availability checking
- Remote OAuth 2.1 with multi-user support — can be hosted centrally for an organization
- Stateless mode fixed (April 2026) — WORKSPACE_MCP_STATELESS_MODE=true now properly reaches FastMCP runtime
- macOS stability fix — startup captures stray stdout to prevent MCP JSON-RPC corruption

**Best for:** Teams already using multiple Google Workspace services who want one server to cover everything.

## Microsoft 365 / Outlook Servers

The Microsoft calendar MCP landscape has consolidated around **Work IQ** — Microsoft's dedicated productivity MCP platform — while community alternatives continue to offer broader tool coverage.

### Microsoft Work IQ Calendar — Official (NEW)

**Type:** Managed Remote MCP (Preview) | **Backed by:** Microsoft | **Repo:** [microsoft/work-iq](https://github.com/microsoft/work-iq)

Microsoft's new **Work IQ** platform replaces the older microsoft/mcp catalog approach with dedicated, purpose-built MCP servers for each M365 service. The Calendar server is now a standalone offering.

**What makes it stand out:**
- **Dedicated calendar MCP** — not buried in a catalog of 16+ servers anymore
- **Rich calendar tools** — create, list, update, delete events; accept/decline invitations; cancel and notify attendees
- **Meeting intelligence** — suggest meeting times and locations based on organizer and attendee availability; get free/busy schedules
- **Recurring event support** — create and manage recurring events and online meetings
- **Admin controls** — IT admins manage MCP servers in the M365 admin center with scoped permissions and allow/block policies
- **Remote hosted** — no local server, connects directly to Microsoft infrastructure
- **CLI companion** — microsoft/work-iq GitHub repo provides CLI access alongside MCP

**Limitations:**
- **Preview** — not production-ready, APIs and schemas may change
- **Requires M365 Copilot license** — significant cost barrier
- Calendar is part of the broader Work IQ platform (Mail, Teams, etc.)
- Enterprise-focused — personal Outlook.com users are still underserved

**Best for:** Enterprise teams with M365 Copilot licenses who want official Microsoft calendar MCP with admin controls and meeting intelligence.

### Softeria/ms-365-mcp-server — Community Powerhouse

**Stars:** 932 | **Language:** TypeScript | **License:** MIT

The most feature-rich community Microsoft 365 MCP server. The project has since moved to a declarative, endpoint-based architecture — [300+ tools](https://github.com/Softeria/ms-365-mcp-server/blob/main/src/endpoints.json) mapped 1-to-1 to Microsoft Graph API endpoints, up sharply from the 70+ tools we saw in April.

**What makes it stand out:**
- **Dozens of calendar tools** — list/get/create/update/delete events, per-calendar variants, accept/decline/tentatively-accept invitations, calendar views, and more (up from the original 7-tool set as the server expanded to cover nearly the full Graph API)
- **300+ total tools** — covers email, calendar, SharePoint, Teams, and more in one server, organized into presets (`mail`, `calendar`, `files`, `teams`, etc.) to limit context usage
- **Actively maintained** — v0.146.1 (August 2026), with ongoing fixes for delegated scope handling and token cache synchronization
- **Multi-account mode** — a single server instance can serve multiple logged-in Microsoft accounts via an `account` parameter on each tool call

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

**Stars:** 55 | **Language:** Python | **License:** MIT

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

**Stars:** 326 | **Language:** Python | **License:** MIT

The most popular macOS calendar MCP server. Interacts with the macOS Calendar app through natural language.

**What makes it stand out:**
- **Natural language event creation** with customizable calendars, locations, notes, and reminders
- **Recurring event support** — daily, weekly, monthly, yearly patterns
- **Schedule viewing and availability checking** for finding free time slots
- **Google Calendar integration** — if your Google Calendar is synced with iCloud, events created here appear in Google Calendar too
- **Most adopted** — 326 stars, clear documentation

**Limitations:**
- macOS only — won't work on Linux or Windows
- Python implementation calling macOS calendar APIs
- Fewer discrete tools compared to some competitors

**Best for:** macOS users who want simple, natural language calendar management.

### FradSer/mcp-server-apple-events — Native EventKit

**Stars:** 187 | **Language:** TypeScript + Swift | **License:** MIT

Native macOS integration with Apple Reminders and Calendar via EventKit. Takes a more architectural approach with a 4-layer Clean Architecture design. Update: the separate `mcp-server-apple-reminders` repo we noted in an earlier revision no longer exists on its own — that URL now redirects to this same repo, which has consolidated back into a single combined Reminders + Calendar server.

**What makes it stand out:**
- **Combined Reminders + Calendar** — full CRUD for both in one server
- **Location-based triggers** — geofence reminders that fire based on location
- **Subtasks and checklists** with progress tracking
- **Tags/labels** for cross-list categorization
- **Swift-compiled binaries** for performance-critical operations
- **v1.5.0** (August 2026) — multiple releases indicate active development; the EventKit backend was swapped for a vendored Swift CLI in this release

**Limitations:**
- macOS only
- More complex setup than simpler alternatives
- TypeScript + Swift hybrid adds build complexity

**Best for:** Developers who want deep Reminders + Calendar integration on macOS with advanced features like geofencing.

### PsychQuant/che-ical-mcp — Most Tools

**Stars:** 33 | **Language:** Swift | **License:** MIT

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
- Actively iterating (v1.15.0, July 2026)
- 33 stars — smaller community

**Best for:** Power users who need comprehensive calendar + reminders management across multiple macOS calendar sources.

## Booking & Scheduling Platform Servers

For teams using dedicated scheduling platforms, official MCP servers are emerging.

### Calendly — Official Hosted MCP

**Hosted at:** mcp.calendly.com | **Type:** Remote MCP

Calendly's official MCP server is fully hosted — zero local infrastructure required. It maps to Calendly's public API v2 with tool annotations for safety. Launched March 11, 2026.

**What makes it stand out:**
- **Fully hosted** — no installation, no maintenance, no server to manage
- **Official Calendly backing** — maintained by the Calendly team
- **Dynamic Client Registration (DCR)** — clients self-register at runtime to get a client_id, no pre-registration or OAuth secrets needed. This is the most frictionless auth setup of any calendar MCP server
- **Tool annotations** — each tool includes readOnlyHint, destructiveHint, and idempotentHint metadata for safe AI usage
- **Full API coverage** — book/cancel meetings, update availability, generate scheduling links, manage events
- **Works natively with Claude** — no custom connector setup required

**Limitations:**
- Calendly-only — won't help with Google Calendar, Outlook, or other calendars
- Requires a Calendly account
- Limited to what Calendly's API exposes

**Best for:** Teams already using Calendly who want AI-powered scheduling management.

### Cal.com MCP — Now Hosted, and Cal.com Is No Longer Open Source

**Type:** Hosted Remote MCP (`mcp.cal.com`) + local/self-hosted option | **Backed by:** Cal.com

Two corrections to our last review. First, Cal.com's [official MCP documentation](https://cal.com/docs/mcp-server) now describes a **hosted server at `https://mcp.cal.com/mcp`**, using Streamable HTTP transport with OAuth 2.1 (no API key needed) — Cal.com is no longer "the last major holdout still running locally." A local, API-key-based option still exists via the `@calcom/cal-mcp` npm package ([calcom/cal-mcp](https://github.com/calcom/cal-mcp) on GitHub, 30 stars), but as of its current README, that local server still ships only [9 core tools by default](https://github.com/calcom/cal-mcp#supported-tools), requiring an `--all-tools` flag for full coverage — the "no longer requires `--all-tools`" claim in our last review does not match the live repo. The 34-tools-across-eight-categories figure belongs to the hosted `mcp.cal.com` server, not the default local install.

Second: **Cal.com is no longer open source.** On April 15, 2026, Cal.com [went closed-source](https://cal.com/blog/cal-com-goes-closed-source-why), citing AI-driven security risk to customer data. The production codebase is now private; the former open-source repo was relaunched as [Cal.diy](https://cal.com/blog/cal-diy-open-source-to-closed-source), a separately-branded, community-driven MIT-licensed fork — not "Cal.com" itself. Our previous "open-source scheduling — Cal.com itself is open source, unlike Calendly" claim is no longer accurate and has been removed.

**What makes it stand out:**
- **Official Cal.com backing** — maintained by the Cal.com team
- **34 tools across ~8 categories** (user profile, event types, bookings, schedules, availability, conferencing, routing forms, organizations) — via the hosted `mcp.cal.com` server
- **OAuth 2.1 hosted option** — no API key or local install required
- **Local/self-hosted fallback** — `@calcom/cal-mcp` for API-key-based stdio use, though it exposes fewer tools by default than the hosted server

**Limitations:**
- Cal.com-specific — doesn't integrate with external calendars directly
- Cal.com's core product is closed-source as of April 2026 — the open-source Cal.diy fork is a different, community-maintained project
- Local npm package's default tool set is narrower than the hosted server's; check current docs before assuming parity

**Best for:** Cal.com users who want comprehensive AI-managed scheduling via the hosted server. The 34-tool coverage there makes it the most feature-dense booking platform MCP option.

## CalDAV / Universal Protocol Servers

CalDAV is the open standard for calendar access. These servers work with any CalDAV-compatible provider.

### madbonez/caldav-mcp — Universal CalDAV

**Stars:** 14 | **Language:** Python | **License:** MIT

A universal MCP server for the CalDAV protocol. The appeal is breadth: one server, any CalDAV provider.

**What makes it stand out:**
- **8 tools** — list calendars, create events, get events by timeframe, retrieve by UID, delete, search
- **Works with any CalDAV provider** — Nextcloud, ownCloud, Apple iCloud, Google Calendar (via CalDAV), Yandex Calendar, FastMail, and more
- **Rich event features** — recurring events, categories, priorities, attendees, multiple reminders
- **Attendance tracking** — ACCEPTED/DECLINED/TENTATIVE/NEEDS-ACTION status

**Limitations:**
- Only 14 stars — small community, limited battle-testing
- End-to-end tested only against Yandex Calendar (other providers should work but untested)
- 3 commits total — very early stage
- CalDAV limits you to what the protocol supports (no provider-specific features like Google Meet integration)

**Best for:** Self-hosters and privacy-focused users who want one server for Nextcloud, ownCloud, or other CalDAV providers.

### Cheffromspace/mcp-nextcloud-calendar — Nextcloud-Specific

**Stars:** 7 | **Language:** TypeScript | **License:** MIT

A Nextcloud-focused CalDAV calendar MCP server with some unique features.

**What makes it stand out:**
- **ADHD-friendly organization** — custom categories and focus priorities for events
- **Dual transport support** — Streamable HTTP (March 2025 spec) and legacy HTTP+SSE
- **Full CRUD** for both calendars and events
- **Nextcloud-optimized** — Basic Auth with Nextcloud, purpose-built for the platform

**Limitations:**
- Nextcloud only — not a universal CalDAV server
- Early development (0.1.x) — APIs may change
- 7 stars

**Best for:** Nextcloud users who want calendar integration with AI assistants.

## Multi-Provider Servers

### MarimerLLC/calendar-mcp — Cross-Platform Unified

**Stars:** 21 | **Language:** C# | **License:** MIT

A unified server that aggregates calendar access across Microsoft 365, Outlook.com, Google Workspace, ICS feeds, and JSON files.

**What makes it stand out:**
- **Multi-provider in one server** — Microsoft 365 (multiple tenants), Outlook.com, and Google Workspace simultaneously
- **14 MCP tools** including account listing, calendar event management, contact operations, and free-time discovery
- **ICS feed and JSON file support** — read-only access to any calendar with an ICS URL
- **Email + Calendar + Contacts** — unified view across providers
- **Smart domain-based routing** — automatically routes operations to the right provider

**Limitations:**
- 21 stars — still early, small community
- C# — less common in the MCP ecosystem (most servers are TypeScript or Python)
- Small contributor base (3 contributors visible, up from 1)
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
├── Yes, want official/managed → Google Workspace Calendar MCP (remote, 8 tools)
├── Yes, need multi-account/bulk → nspady/google-calendar-mcp (13 tools)
├── Yes, plus Gmail/Docs/Sheets → taylorwilsdon/google_workspace_mcp
│
Do you use Microsoft 365 / Outlook?
├── Yes, have Copilot license → Work IQ Calendar (hosted, meeting intelligence)
├── Yes, want free community tools → Softeria/ms-365-mcp-server (614 stars, 70+ tools)
│
Do you use macOS Calendar?
├── Yes, simple use → Omar-V2/mcp-ical
├── Yes, Reminders too → FradSer/mcp-server-apple-events or PsychQuant/che-ical-mcp
│
Do you use Calendly or Cal.com?
├── Calendly → Calendly MCP (mcp.calendly.com, DCR auth)
├── Cal.com → Cal.com MCP, hosted at mcp.cal.com (34 tools)
│
Do you self-host (Nextcloud/ownCloud)?
├── Yes → madbonez/caldav-mcp or Cheffromspace/mcp-nextcloud-calendar
│
Do you need Google + Microsoft unified?
└── Yes → MarimerLLC/calendar-mcp
```

## Three Trends Worth Watching

### 1. Official vendors have arrived — the gap era is over

In March, we flagged Google's absence as the biggest gap in calendar MCP. One month later, **both Google and Microsoft now have official managed calendar MCP servers**. Google's Workspace Calendar MCP (8 tools, remote) and Microsoft's Work IQ Calendar (Preview, hosted) join Calendly and Cal.com as vendor-backed options. The pattern is clear: every major calendar platform will ship an official MCP server. Community servers now compete on features (multi-account, bulk operations, tool filtering) rather than filling a vendor void.

### 2. Hosted remote MCP is winning — even for calendars

Google, Microsoft, Calendly, and now Cal.com (`mcp.cal.com`, OAuth 2.1) have all shipped hosted remote MCP servers — local-only was a temporary state, not a durable choice. The privacy argument for local calendar servers is weakening as vendors add enterprise-grade auth (Google's Workspace permissions, Microsoft's admin controls, Calendly's and Cal.com's OAuth/DCR flows). The new question isn't "local vs remote" but "which remote server has the right auth model for your org."

### 3. Tool count inflation — more isn't always better

Cal.com's hosted server jumped to 34 tools. Google's official server has 8. nspady has 13. Softeria has 300+. The "right" number depends on your use case — more tools means more context window consumption but broader capability. Google's suggest_time tool (unique to the official server) shows that a single well-designed tool can matter more than 20 CRUD variants. Watch for quality-over-quantity as the market matures.

## What's Missing

- ~~**No official Google Calendar MCP server**~~ — **FILLED** (April 2026). Google shipped a managed remote Calendar MCP with 8 tools. The community server still has more features, but the API compatibility gap is closed
- **No Outlook.com standalone server** — Work IQ requires M365 Copilot license ($30/user/month); personal Outlook.com users are still underserved. MarimerLLC supports Outlook.com but at 21 stars it's still niche
- **No Zoom scheduling integration** — Zoom has calendar features but no MCP server for them
- **No Reclaim.ai / Motion / Clockwise MCP servers** — AI-native scheduling tools that would benefit most from MCP integration haven't shipped servers yet
- **No cross-platform free/busy aggregation** — checking availability across Google + Outlook + Apple simultaneously doesn't exist in a single tool. Google's suggest_time is provider-locked
- **Limited recurring event intelligence** — most servers can create recurring events but can't analyze patterns or suggest optimal meeting times (Google's suggest_time is a step in this direction)
- **No calendar analytics** — meeting load analysis, time allocation tracking, and scheduling pattern insights are absent from all servers
- **MCP security concerns** — [CVE-2026-26118](https://github.com/advisories/GHSA-hhfx-wfvq-7g9c) (Azure MCP Server SSRF, CVSS 8.8, patched March 2026) and broader MCP ecosystem security questions highlight that calendar MCP servers handling sensitive scheduling data require security review before deployment

