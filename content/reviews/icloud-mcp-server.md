---
title: "iCloud MCP Servers — Calendar, Mail, Contacts & More"
date: 2026-03-23T23:30:00+09:00
description: "Apple has no official iCloud MCP server, but community projects let AI agents access Calendar, Mail, Contacts, and Reminders via CalDAV, CardDAV, and IMAP."
og_description: "iCloud MCP servers: no official Apple server, community implementations for Calendar, Mail, Contacts, and Reminders. No iCloud Drive access. Rating: 2.5/5."
content_type: "Review"
card_description: "Apple still has no official iCloud MCP server — WWDC 2026 shipped MCP support only for Xcode developer tooling, not iCloud. The community ecosystem is growing rapidly — 19 new repos in 31 days — covering Calendar (CalDAV), Mail (IMAP/SMTP), Contacts (CardDAV), and Reminders across Rust, Swift, Kotlin, Go, Python, and TypeScript. No server offers iCloud Drive file access — the critical gap versus Google Drive, Dropbox, and OneDrive."
last_refreshed: 2026-05-18
sources_audited: 2026-08-16
---

**At a glance:** [supermemoryai/apple-mcp](https://github.com/supermemoryai/apple-mcp) (3,129 stars, archived, MIT) + [icloud-calendar-mcp](https://github.com/icloud-calendar-mcp/icloud-calendar-mcp) (14 stars, v3.2.0, Apache 2.0) + [PsychQuant/che-ical-mcp](https://github.com/PsychQuant/che-ical-mcp) (33 stars, Swift/EventKit, 29 tools). Apple has a [market cap above $3 trillion](https://stockanalysis.com/stocks/aapl/market-cap/) — it first crossed that line in [June 2023](https://www.nbcnews.com/tech/apple-becomes-first-company-hit-3-trillion-market-value-rcna10767) and has stayed above it since — but **no official MCP server** and **no iCloud Drive file access** through any community implementation. WWDC 2026 ([June 8-12](https://9to5mac.com/2026/03/23/apple-announces-wwdc-2026-for-june-8-ios-27-set-to-be-revealed/)) is the next expected catalyst for an official Apple MCP announcement. The biggest cloud storage MCP gap — with 19 new community repos appearing in the past 31 days alone.

iCloud MCP servers let AI agents **manage Apple Calendar events, send and read iCloud Mail, access Contacts, and handle Reminders** — all through natural language prompts. The community ecosystem has grown rapidly, with **10+ tracked implementations** and **19 new repos appearing in the 31 days between April 17 and May 18, 2026**. The most actively maintained server is now **[icloud-calendar-mcp](https://github.com/icloud-calendar-mcp/icloud-calendar-mcp)** (v3.2.0, 843 tests across its [documented test suite](https://github.com/icloud-calendar-mcp/icloud-calendar-mcp#test-coverage-mcp-server)), while **PsychQuant/che-ical-mcp** (33 stars, Swift, native EventKit, 29 tools) has emerged as the most-starred new entrant not in the previous review. However, unlike Google Drive, Dropbox, and OneDrive MCP servers, **no implementation provides iCloud Drive file access** — the file storage feature that most users associate with iCloud. Apple's [WWDC 2026 (June 8-12)](https://9to5mac.com/2026/03/23/apple-announces-wwdc-2026-for-june-8-ios-27-set-to-be-revealed/) is the next expected catalyst for official MCP APIs, but no announcement has been made as of May 2026.

[Apple](https://www.apple.com/) was [founded on April 1, 1976](https://en.wikipedia.org/wiki/Apple_Inc.), by **Steve Jobs**, **Steve Wozniak**, and **Ronald Wayne**. The company [went public on December 12, 1980](https://www.computerhistory.org/tdih/december/12/) (NASDAQ: AAPL). As of fiscal year 2025 (ended September 27, 2025): **[$416.2 billion annual revenue](https://www.apple.com/newsroom/pdfs/fy2025-q4/FY25_Q4_Consolidated_Financial_Statements.pdf)** (up from $391.0 billion in FY2024, roughly 6% growth), one of the world's largest companies by market capitalization. Apple's Services segment generated **[$28.75 billion](https://www.apple.com/newsroom/pdfs/fy2025-q4/FY25_Q4_Consolidated_Financial_Statements.pdf)** in Q4 FY2025 alone, with iCloud+ subscriptions contributing to that total. The company employs approximately **[166,000 full-time equivalent employees](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm)** as of September 27, 2025.

**Architecture note:** There is no official Apple MCP server. Community implementations use standard protocols — CalDAV for calendars, CardDAV for contacts, IMAP/SMTP for email — connecting to iCloud endpoints with app-specific passwords. Some implementations use AppleScript to control native macOS apps directly, which provides broader access (Notes, Messages, Reminders, Safari) but requires macOS and grants no cross-platform capability. iCloud Drive file access would require CloudKit, which no community MCP server has implemented.

**Category:** [Cloud Storage & File Sync](/categories/cloud-storage-file-sync/)

## What It Does

Between the archived apple-mcp project and active community implementations, iCloud MCP servers cover five capability areas — notably missing file storage:

### Calendar (CalDAV)

| Capability | What It Does |
|------------|-------------|
| List calendars | Retrieve all iCloud calendars |
| List events | Fetch events with date range filtering |
| Create events | New events with optional recurrence rules |
| Update events | Modify existing events (basic fields only) |
| Delete events | Remove calendar entries by UID |
| Search events | Text search across summaries and descriptions |

### Mail (IMAP/SMTP)

| Capability | What It Does |
|------------|-------------|
| List mailboxes | Browse all iCloud Mail folders |
| Read messages | Retrieve email content and metadata |
| Send email | Compose and send with text/HTML support |
| Search messages | Query by sender, subject, date, or keywords |
| Move messages | Transfer between mailboxes |
| Manage flags | Mark as read/unread, flag, delete |
| Download attachments | Extract email attachments |
| Auto-organize | Rule-based email sorting (minagishl only) |

### Contacts (CardDAV)

| Capability | What It Does |
|------------|-------------|
| List contacts | Retrieve all iCloud contacts |
| Search contacts | Find by name, email, phone |
| Create contacts | Add new contacts with full field support |
| Update contacts | Modify phone, email, address, organization |
| Delete contacts | Remove contact entries |

### Reminders & Notes (macOS only)

| Capability | What It Does |
|------------|-------------|
| List reminders | Browse reminder lists and items |
| Create reminders | Add with due dates and priorities |
| Complete reminders | Mark reminders as done |
| Create notes | Add new notes (AppleScript) |
| Search notes | Find notes by content (AppleScript) |

### macOS Native Apps (AppleScript only)

| Capability | What It Does |
|------------|-------------|
| Messages | Send messages (cannot read — macOS security restriction) |
| Safari | Get tabs, open URLs, read page content |
| Maps | Search locations, get directions, drop pins |

### What's Missing: iCloud Drive

**No iCloud MCP server provides file storage access.** iCloud Drive — the feature that competes directly with Google Drive, Dropbox, and OneDrive — requires Apple's CloudKit API, which demands an Apple Developer account, an iCloud container, and Apple-specific authentication that no community project has implemented. This is the single biggest gap in the iCloud MCP ecosystem and the primary reason for the low rating versus other cloud storage MCP servers.

## Community Implementations

### supermemoryai/apple-mcp — Apple Native Tools (Archived)

- **GitHub:** [supermemoryai/apple-mcp](https://github.com/supermemoryai/apple-mcp) — 3,129 stars, 286 forks, 87 commits, 11 contributors
- **Language:** TypeScript
- **License:** MIT
- **Status:** **[Archived January 1, 2026](https://github.com/supermemoryai/apple-mcp)** — read-only, no longer maintained
- **Platform:** macOS only (uses AppleScript)

The most popular Apple MCP implementation by far, built by [Dhravya Shah](https://github.com/dhravya), founder and CEO of [Supermemory AI](https://techcrunch.com/2025/10/06/a-19-year-old-nabs-backing-from-google-execs-for-his-ai-memory-startup-supermemory/). Provides natural language control of 7 native macOS apps:

- **Messages:** Send, read, schedule messages
- **Notes:** Create, search notes
- **Contacts:** Lookup, retrieve phone numbers
- **Mail:** Send with attachments, search, schedule
- **Reminders:** Create with due dates, search, list
- **Calendar:** Create events, search, list, open events
- **Maps:** Search locations, save favorites, get directions, create guides, drop pins

**Command chaining** enables multi-step operations like "Read conference notes, find contacts for attendees, and send thank you messages."

**Key limitation:** Requires macOS with AppleScript permissions. Archived — no bug fixes or updates. Does not access iCloud Drive.

### MrGo2/icloud-mcp — Dual-Mode (Local + Cloud)

- **GitHub:** [MrGo2/icloud-mcp](https://github.com/MrGo2/icloud-mcp) — 34 stars, 13 forks, 51 commits
- **Language:** JavaScript
- **License:** MIT
- **Auth:** AppleScript permissions (local) or app-specific password (cloud)

The most versatile active implementation with two operational modes:

- **Local mode (31 tools):** AppleScript-based access to Email, Calendar, Contacts, Reminders, Notes, Messages, Safari — macOS only
- **Cloud mode (17 tools):** CalDAV, CardDAV, IMAP/SMTP — cross-platform with app-specific password

**Key limitation:** Cannot read Messages (macOS security restriction). No iCloud Drive access.

### minagishl/icloud-mail-mcp — Mail Specialist

- **GitHub:** [minagishl/icloud-mail-mcp](https://github.com/minagishl/icloud-mail-mcp) — 11 stars, 8 forks, 37 commits
- **Language:** TypeScript
- **Auth:** App-specific password via IMAP/SMTP

The most mature mail-focused implementation with 14 tools:

- Full CRUD: get, send, mark read, move, search, delete, set flags, download attachments
- Mailbox management: list, create, delete folders
- **Auto-organize:** Rule-based email sorting — unique among iCloud MCP servers
- Connection testing and config validation

**Key limitation:** Mail only — no calendar, contacts, or other services.

### mike-tih/icloud-mcp — Protocol-Based (CalDAV + CardDAV + IMAP)

- **GitHub:** [mike-tih/icloud-mcp](https://github.com/mike-tih/icloud-mcp) — 6 stars, 17 forks, 32 commits
- **Language:** Python
- **License:** MIT
- **Auth:** App-specific password via request headers or environment variables

Cross-platform implementation using standard protocols:

- **Calendar:** List, create, update, delete, search events via CalDAV
- **Contacts:** Full CRUD with phone, email, address, organization fields via CardDAV
- **Email:** List, read, search, send, move, delete messages via IMAP/SMTP

**Key limitation:** Python 3.10-3.12 only (3.13+ has dependency issues). Stateless architecture — no session persistence.

### localhost433/icloud-mcp — Calendar Only

- **GitHub:** [localhost433/icloud-mcp](https://github.com/localhost433/icloud-mcp) — 2 stars, 1 fork, 11 commits
- **Language:** Python
- **License:** MIT
- **Auth:** App-specific password

HTTP MCP server focused exclusively on iCloud Calendar via CalDAV:

- List calendars, list/create/update/delete events
- Search events and fetch raw ICS data
- Health check endpoint

**Key limitation:** Calendar only. Advanced fields (attendees, alarms, recurrence exceptions) not preserved on update. UID matching within ±3-year window.

### adamzaidi/icloud-mcp — Removed

Previously listed here, adamzaidi/icloud-mcp (65 tools, 0 stars, 45 commits, JavaScript, MIT) has been **deleted from GitHub** as of May 2026. It offered the most feature-rich cross-platform email tooling (thread detection, bulk operations, storage analysis, dry-run support) of any active implementation. No archived copy or fork appears to be available.

### icloud-calendar-mcp — Security-First (OWASP Compliant)

- **GitHub:** [icloud-calendar-mcp/icloud-calendar-mcp](https://github.com/icloud-calendar-mcp/icloud-calendar-mcp) — 14 stars, 6 forks, 30 commits
- **Language:** Kotlin/JVM
- **License:** [Apache 2.0](https://github.com/icloud-calendar-mcp/icloud-calendar-mcp/blob/main/LICENSE)
- **Distribution:** [npm](https://www.npmjs.com/package/@icloud-calendar-mcp/server), [PyPI](https://pypi.org/project/icloud-calendar-mcp/), MCP Registry
- **Latest:** [v3.2.0 (August 14, 2026)](https://github.com/icloud-calendar-mcp/icloud-calendar-mcp/releases) — two releases have shipped since this review's original v3.0.1 writeup (v3.1.0 in July, v3.2.0 in August)

The **most actively maintained iCloud MCP server** — and the most security-focused, explicitly designed around the [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) framework:

**v3.0.1 changes (May 12, 2026):**
- Full RFC 5545 compliance (CRLF line endings, proper DTEND, TEXT escape sequences)
- VALARM authoring: DISPLAY, AUDIO, and EMAIL alarm actions via new `alarms` parameter
- ETag recovery via PROPFIND probes (fixes silent ICS corruption)
- New event parameters: `end_timezone`, `rdates`, `exdates`, `alarms`
- Unit test time reduced from 4+ minutes to ~17 seconds

**Security posture:**
- **5 Calendar tools:** List calendars, get events, create, update, delete
- **[843 tests](https://github.com/icloud-calendar-mcp/icloud-calendar-mcp#test-coverage-mcp-server)** across the project's documented test suite, including dedicated adversarial-input, Unicode-security, and ReDoS-protection categories, plus rate limiting (60 reads/min, 20 writes/min)

**Key advantage:** The only actively maintained iCloud MCP server with enterprise-grade security testing and formal release versioning. Available across npm, PyPI, and MCP Registry.

**Key limitation:** Calendar only — no mail, contacts, or other services.

### roygabriel/mcp-icloud-calendar — Go with Observability

- **GitHub:** [roygabriel/mcp-icloud-calendar](https://github.com/roygabriel/mcp-icloud-calendar) — 1 star, 6 forks, 26 commits
- **Language:** Go (1.21+)
- **Auth:** App-specific password

Production-oriented calendar MCP server with enterprise features:

- **5 Calendar tools:** List calendars, search events (with pagination), create, update (partial), delete
- Recurring event expansion into individual occurrences
- Attendee management with role and status tracking
- Prometheus metrics, audit logging, health check endpoints
- Structured JSON logging, configurable timeouts (default 25s), automatic retry with exponential backoff, per-account rate limiting

Recent activity is automated dependency management only (Dependabot bumping `mcp-go` 0.43.2 → 0.52.0 via weekly PRs through April–May). Two open bugs filed May 4: CalDAV search returning empty field values, and DTSTART/DTEND timestamp parsing when TZID is present.

**Key limitation:** Calendar only. 1 star — still new and unproven.

### Lawiak/icloud-mcp — Docker & Raspberry Pi

- **GitHub:** [Lawiak/icloud-mcp](https://github.com/Lawiak/icloud-mcp) — 1 star (+1), 0 forks, 24 commits
- **Language:** Python (96.4%)
- **License:** MIT
- **Auth:** App-specific password via IMAP/SMTP

Email-focused implementation designed for headless and remote deployment:

- Read emails from any folder while preserving unread status
- Send with CC and attachments, folder management, search
- **Docker containerized** with Dockerfile included
- **Raspberry Pi support** via SSH + Docker for remote deployment
- FastMCP framework, STDIO transport

**Key advantage:** The only iCloud MCP server explicitly designed for headless/IoT deployment. Run on a Raspberry Pi as a persistent email agent.

**Key limitation:** Email only — no calendar, contacts, or other services. 0 stars.

### PsychQuant/che-ical-mcp — Native EventKit (Most-Starred New Entry)

- **GitHub:** [PsychQuant/che-ical-mcp](https://github.com/PsychQuant/che-ical-mcp) — 33 stars, 8 forks, [2 open issues](https://github.com/PsychQuant/che-ical-mcp/issues)
- **Language:** Swift
- **Platform:** macOS 26 (Tahoe)
- **Distribution:** Signed and notarized binary; `.mcpb` extension for Claude Desktop

The **most-starred iCloud-adjacent MCP server** not previously tracked in this review. Uses Apple's native **EventKit framework** directly rather than CalDAV, providing 29 tools across Calendar and Reminders. Supports iCloud, Google Calendar, and Exchange accounts simultaneously (any calendar visible in the macOS Calendar app).

- List, create, update, and delete events across all calendar accounts
- Reminders access via EventKit (not AppleScript — works without Script Editor permissions)
- Signed binary for macOS Tahoe, distributed via `.mcpb` Claude Desktop extension format
- Latest release: [v1.15.0 (July 10, 2026)](https://github.com/PsychQuant/che-ical-mcp/releases)

**Known issue:** Earlier versions had a permissions bug where Claude Desktop denied Calendar/Reminders access under the `.mcpb` install path — [closed issue #165](https://github.com/PsychQuant/che-ical-mcp/issues/165) — and TCC (macOS privacy) permission grants can still be invalidated when Claude Code auto-updates rotate its binary path ([open issue #170](https://github.com/PsychQuant/che-ical-mcp/issues/170)). Actively maintained.

**Key limitation:** macOS-only (native Swift, no cross-platform path). Calendar and Reminders only — no Mail or Contacts.

### Kembec/ical-mcp — Rust, Single Binary

- **GitHub:** [Kembec/ical-mcp](https://github.com/Kembec/ical-mcp) — 0 stars, 0 forks, 33 commits
- **Language:** Rust
- **Distribution:** npm/npx (single binary — no JVM, Python, or Node.js runtime required at runtime)
- **Auth:** App-specific password via CalDAV

The most technically distinct new entrant: a Rust binary distributed via npm, providing CalDAV-based iCloud Calendar access with no runtime dependencies. Launched May 14, 2026. A companion repo `Kembec/email-mcp` (9 commits, May 15) covers multi-account email (Gmail, Outlook, iCloud) in the same single-binary approach.

**Key advantage:** Zero runtime dependencies — install with `npx` and it works. Eliminates JVM (Java) or Python installation barriers that affect other calendar MCP servers.

**Key limitation:** 0 stars — brand new, untested in the community. Calendar only (email handled by companion repo).

### iteratio/icloud-mcp — Removed

Previously listed here, iteratio/icloud-mcp (macOS Keychain-based, 0 stars, 3 commits) has been **removed from GitHub** as of April 2026. It covered Calendar, Mail, and Reminders with credentials stored in macOS Keychain.

## Authentication

All iCloud MCP servers use **app-specific passwords** — a significant improvement over the complex OAuth flows required by Google Drive, OneDrive, and Dropbox:

| Method | Used By | Complexity |
|--------|---------|------------|
| App-specific password (CalDAV/CardDAV/IMAP) | mike-tih, localhost433, MrGo2 (cloud), minagishl | **Low** — generate in Apple ID settings |
| macOS Keychain + app-specific password | iteratio | **Low** — stored securely in Keychain |
| AppleScript permissions | apple-mcp, MrGo2 (local) | **Low** — grant in System Settings > Privacy |

**The good news:** iCloud MCP auth is the **simplest** of any cloud storage ecosystem — no OAuth 2.0 flows, no developer console registration, no admin consent. Just generate an app-specific password at appleid.apple.com and configure it.

**The bad news:** This simplicity exists because Apple doesn't offer a real API for iCloud Drive. The protocols available (CalDAV, CardDAV, IMAP) are decades-old standards that only cover calendar, contacts, and email — not file storage.

## Cloud Storage MCP Comparison

| Dimension | iCloud | Google Drive | Dropbox | OneDrive |
|-----------|--------|-------------|---------|----------|
| **Official MCP** | **None** | [google/mcp](https://github.com/google/mcp) (4.5k stars); Google says [50+ Google-managed MCP servers](https://cloud.google.com/blog/products/ai-machine-learning/google-managed-mcp-servers-are-available-for-everyone) are GA or in preview | 2 servers (remote + Dash) | [Work IQ OneDrive](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-onedrive-work-iq) (**preview**) |
| **Top Community** | [apple-mcp](https://github.com/supermemoryai/apple-mcp) (3,129 stars, **archived**); [PsychQuant/che-ical-mcp](https://github.com/PsychQuant/che-ical-mcp) (33 stars, active) | [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) (3k stars) | [amgadabdelhafez/dbx-mcp-server](https://github.com/amgadabdelhafez/dbx-mcp-server) (29 stars) | [Softeria/ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server) (913 stars) |
| **File Storage Access** | **None — critical gap** | Full read/write/search | Full read/write/search | Full read/write (5MB limit) |
| **Auth Complexity** | **Lowest** — app-specific password | Medium — Google OAuth 2.0 | Low-Medium — Dropbox OAuth | **Highest** — Azure Entra ID |
| **Platform** | macOS-only (AppleScript) or limited cross-platform | Cross-platform | Cross-platform | Cross-platform |
| **Services Covered** | Calendar, Mail, Contacts, Reminders, Notes | Drive, Docs, Sheets, Slides, Gmail, Calendar | Files, Dash search (30+ apps) | OneDrive, Outlook, Calendar, Teams, SharePoint |
| **Apple's MCP Stance** | [WWDC 2026](https://9to5mac.com/2026/03/23/apple-announces-wwdc-2026-for-june-8-ios-27-set-to-be-revealed/) expected to deliver first public APIs | Official commitment | Official commitment | Official commitment |

## iCloud+ Pricing

Pricing per [apple.com/icloud](https://www.apple.com/icloud/):

| Plan | Price | Storage |
|------|-------|---------|
| iCloud (free) | Free | 5 GB |
| iCloud+ 50 GB | $0.99/month | 50 GB |
| iCloud+ 200 GB | $2.99/month | 200 GB |
| iCloud+ 2 TB | $9.99/month | 2 TB |
| iCloud+ 6 TB | $29.99/month | 6 TB |
| iCloud+ 12 TB | $59.99/month | 12 TB |

All paid tiers include iCloud Private Relay, Hide My Email, Custom Email Domain, and Family Sharing (up to 6 people).

**Note:** Pricing is irrelevant to MCP capabilities since no server accesses iCloud Drive storage. Current MCP servers only use Calendar, Mail, and Contacts — features available on all tiers including free.

## Apple's MCP Future

Apple is not ignoring MCP entirely, and the timeline accelerated through 2026. In September 2025, the macOS Tahoe 26.1 and iOS 26.1 developer betas included early code references for **MCP support via App Intents** — Apple's framework for exposing app capabilities to Siri and Shortcuts, [first reported by 9to5Mac](https://9to5mac.com/2025/09/22/macos-tahoe-26-1-beta-1-mcp-integration/) and [AppleInsider](https://appleinsider.com/articles/25/09/22/ios-26-could-get-a-major-ai-boost-with-the-model-context-protocol). If completed, this would allow AI agents (ChatGPT, Claude, and others) to directly interact with apps on Mac, iPhone, and iPad.

**[WWDC 2026](https://9to5mac.com/2026/03/23/apple-announces-wwdc-2026-for-june-8-ios-27-set-to-be-revealed/)** ran June 8-12 and spotlighted **iOS 27** alongside AI advancements across Apple's platforms. As it turned out, Apple's first substantial public MCP shipment was **developer-tooling-focused, not consumer-facing**: Xcode 27 shipped [native MCP support via a bridge tool called `mcpbridge`](https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode), letting external coding agents (Claude Code, Cursor, and others) connect to Xcode's live process for builds, diagnostics, and code intelligence — this is a developer-tool integration, not the App Intents-based, Siri/Shortcuts-level MCP surface (or an iCloud cloud API) that the September 2025 beta code hinted at.

**As of this review's most recent update, no official Apple iCloud/App Intents MCP server has shipped.** The PsychQuant/che-ical-mcp server (Swift, native EventKit, signed binary for macOS Tahoe) indicates that macOS-native developers are already building against EventKit in anticipation of a future platform-level shift.

The Xcode 27 MCP bridge remains platform-level, developer-focused MCP support (an IDE exposing local project capabilities to AI coding agents), not a cloud API for iCloud services. There is still no indication that Apple plans to offer a remote iCloud MCP server comparable to Google's, Dropbox's, or Microsoft's official offerings.

## Known Issues

1. **No iCloud Drive access** — The most critical gap. No community MCP server accesses iCloud Drive file storage. CloudKit integration would require an [Apple Developer Program membership ($99/year)](https://developer.apple.com/programs/) and Apple-specific authentication that no one has implemented. This makes iCloud MCP servers fundamentally different from Google Drive, Dropbox, and OneDrive MCP servers.

2. **Best server is archived; top active server deleted** — [supermemoryai/apple-mcp](https://github.com/supermemoryai/apple-mcp) (3,129 stars) was archived in January 2026. The most feature-rich active server at last review — adamzaidi/icloud-mcp (65 tools, 45 commits) — was **deleted from GitHub as of May 2026** (the repository now returns a 404). [MrGo2/icloud-mcp](https://github.com/MrGo2/icloud-mcp) (34 stars) offers the broadest active coverage, while [icloud-calendar-mcp](https://github.com/icloud-calendar-mcp/icloud-calendar-mcp) (v3.2.0) is the most rigorously maintained. [PsychQuant/che-ical-mcp](https://github.com/PsychQuant/che-ical-mcp) (33 stars) is the most-starred new entrant.

3. **macOS dependency** — The most capable implementations (apple-mcp, MrGo2 local mode, PsychQuant/che-ical-mcp) require macOS with AppleScript or EventKit permissions. Linux and Windows users are limited to CalDAV/CardDAV/IMAP access only (calendar, contacts, email).

4. **No official server** — Apple has not released an official MCP server for any iCloud service. Google, Dropbox, and Microsoft all have official MCP servers. Apple's [WWDC 2026 (June 8-12)](https://9to5mac.com/2026/03/23/apple-announces-wwdc-2026-for-june-8-ios-27-set-to-be-revealed/) shipped MCP support in [Xcode 27 for developer tooling](https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode), not a cloud API for iCloud services or a consumer-facing App Intents surface. No official iCloud MCP server has shipped as of this update.

5. **Rapidly expanding but fragmented community** — Outside the archived apple-mcp, the ecosystem has grown explosively: **19 new repos appeared in the 31 days between April 17 and May 18, 2026**. The community is now diversifying across Rust (Kembec/ical-mcp), Swift (PsychQuant/che-ical-mcp), Kotlin (icloud-calendar-mcp), Go, Python, JavaScript, and TypeScript. However, no single active project has emerged as a clear community successor to apple-mcp.

6. **pyicloud remains broken** — The popular Python library for iCloud access (pyicloud) stopped working after Apple changed web authentication to SRP-6a. Two open pull requests — [#459](https://github.com/picklepete/pyicloud/pull/459) and [#489](https://github.com/picklepete/pyicloud/pull/489) — propose fixes, but as of this update neither has been merged by the effectively unmaintained project. All working MCP servers bypass pyicloud and use CalDAV/CardDAV/IMAP protocols directly.

7. **Cannot read Messages** — macOS security restrictions prevent even AppleScript-based servers from reading iMessage/SMS content. Sending is possible; reading is blocked.

8. **Limited Reminders/Notes access** — Reminders and Notes are only available through AppleScript (macOS only). No cross-platform protocol access exists for these services.

9. **No Find My access** — Apple's Find My API is internal-only. No MCP server can track device locations or AirTags.

10. **App-specific password scope** — While easy to generate, app-specific passwords grant broad access to the associated Apple ID services. There is no way to scope permissions to specific calendars, mailboxes, or contacts — it's all-or-nothing.

## Bottom Line

**Rating: 2.5 out of 5**

iCloud MCP servers present a paradox: [one of the world's most valuable companies](https://www.apple.com/newsroom/pdfs/fy2025-q4/FY25_Q4_Consolidated_Financial_Statements.pdf) has the **weakest MCP ecosystem** of any major cloud storage provider. The fundamental problem is straightforward — **no iCloud Drive file access**. While Google Drive, Dropbox, and OneDrive MCP servers let AI agents read, write, search, and organize files, iCloud MCP servers are limited to calendar events, email, and contacts.

The community has done what it can with available protocols. **[supermemoryai/apple-mcp](https://github.com/supermemoryai/apple-mcp)** reached an impressive 3,129 stars by providing AppleScript-based access to 7 macOS apps, but it was archived in January 2026. Since then, the active ecosystem has expanded rapidly: **19 new repos appeared in just 31 days (April 17–May 18)**, and the language diversity now spans Rust (Kembec/ical-mcp), Swift (PsychQuant/che-ical-mcp, 33 stars), Kotlin (icloud-calendar-mcp, v3.2.0), Go, Python, JavaScript, and TypeScript. One downside: **adamzaidi/icloud-mcp** — the most feature-rich active server at last review (65 tools) — was deleted from GitHub in May 2026. The most maintainer-active project is now **icloud-calendar-mcp** (v3.2.0, full RFC 5545 compliance, VALARM support), while **MrGo2/icloud-mcp** (34 stars) offers the broadest cross-service coverage with dual local/cloud modes.

The one genuine advantage: **authentication is dead simple**. App-specific passwords are vastly easier than Google OAuth, Dropbox OAuth, or Azure Entra ID. But this simplicity is a consequence of limited API access, not thoughtful developer experience.

**Who should use iCloud MCP servers:**

- **macOS users** who want AI agents to manage Calendar, Mail, Contacts, Reminders, and Notes alongside other Apple apps
- **Apple ecosystem users** who need basic PIM (personal information management) automation and don't need file storage access
- **Developers** exploring Apple MCP integration ahead of Apple's expected platform-level MCP support

**Who should wait:**

- **Anyone needing file storage** — iCloud Drive is inaccessible; use Google Drive, Dropbox, or OneDrive MCP servers instead
- **Cross-platform users** — full capability requires macOS; other platforms get calendar/mail/contacts only
- **Teams and organizations** — the community is too small and fragmented for production reliability

The 2.5/5 rating holds. The critical gaps remain unchanged: no iCloud Drive access, no official Apple server, and the archived state of the ecosystem's most popular project. The ecosystem is clearly accelerating (19 new repos in 31 days, new languages, active maintenance in icloud-calendar-mcp), but momentum without file access doesn't close the gap with Google Drive, Dropbox, or OneDrive. [WWDC 2026 (June 8-12)](https://9to5mac.com/2026/03/23/apple-announces-wwdc-2026-for-june-8-ios-27-set-to-be-revealed/) has since come and gone, and it did not deliver a consumer iCloud MCP API — the MCP support Apple shipped was scoped to [Xcode 27 developer tooling](https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode), not Calendar, Mail, Contacts, or Drive. Until Apple ships an official iCloud-facing server, iCloud remains the clear last-place finisher among major cloud storage MCP ecosystems.

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official Apple announcements. Information is current as of May 2026. See our [About page](/about/) for details on our review process.*
