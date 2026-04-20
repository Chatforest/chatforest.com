# iCloud MCP Servers — Calendar, Mail, Contacts & More

> Apple has no official iCloud MCP server, but community projects let AI agents access Calendar, Mail, Contacts, and Reminders via CalDAV, CardDAV, and IMAP.


**At a glance:** [supermemoryai/apple-mcp](https://github.com/supermemoryai/apple-mcp) (3,100 stars, archived, MIT) + [adamzaidi/icloud-mcp](https://github.com/adamzaidi/icloud-mcp) (65 tools, active, MIT) + [icloud-calendar-mcp](https://github.com/icloud-calendar-mcp/icloud-calendar-mcp) (6 stars, OWASP-compliant, Apache 2.0). Apple has 850+ million iCloud users and a $4+ trillion market cap, but **no official MCP server** and **no iCloud Drive file access** through any community implementation. WWDC 2026 (June 8-12) expected to deliver the first public MCP APIs. The biggest cloud storage MCP gap.

iCloud MCP servers let AI agents **manage Apple Calendar events, send and read iCloud Mail, access Contacts, and handle Reminders** — all through natural language prompts. The community ecosystem has grown significantly, with **9+ implementations** now available — including adamzaidi/icloud-mcp offering 65 tools and icloud-calendar-mcp bringing OWASP MCP Top 10 security compliance. However, unlike Google Drive, Dropbox, and OneDrive MCP servers, **no implementation provides iCloud Drive file access** — the file storage feature that most users associate with iCloud. Apple's WWDC 2026 (June 8-12) is expected to deliver the first public MCP APIs via App Intents, but a working cloud integration is not yet available.

[Apple](https://www.apple.com/) was founded on April 1, 1976, by **Steve Jobs**, **Steve Wozniak**, and **Ronald Wayne**. The company went public in December 1980 (NASDAQ: AAPL). As of early 2026: **~$435.6 billion annual revenue** (twelve months ending December 2025, ~10% YoY growth), **~$4+ trillion market cap** — the world's most valuable public company. iCloud has over **850 million active users**. Apple's Services segment generated **$28.75 billion** in Q4 2025 alone, with iCloud+ subscriptions contributing significantly. The company employs approximately **164,000 full-time workers**.

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

- **GitHub:** [supermemoryai/apple-mcp](https://github.com/supermemoryai/apple-mcp) — 3,100 stars, 272 forks, 87 commits, 11 contributors
- **Language:** TypeScript
- **License:** MIT
- **Status:** **Archived January 2026** — read-only, no longer maintained
- **Platform:** macOS only (uses AppleScript)

The most popular Apple MCP implementation by far, built by Dhravya Shah (Supermemory AI). Provides natural language control of 7 native macOS apps:

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

- **GitHub:** [MrGo2/icloud-mcp](https://github.com/MrGo2/icloud-mcp) — 9 stars, 2 forks, 4 commits
- **Language:** JavaScript
- **License:** MIT
- **Auth:** AppleScript permissions (local) or app-specific password (cloud)

The most versatile active implementation with two operational modes:

- **Local mode (31 tools):** AppleScript-based access to Email, Calendar, Contacts, Reminders, Notes, Messages, Safari — macOS only
- **Cloud mode (17 tools):** CalDAV, CardDAV, IMAP/SMTP — cross-platform with app-specific password

**Key limitation:** 4 commits suggests early-stage development. Cannot read Messages (macOS security restriction). No iCloud Drive access.

### minagishl/icloud-mail-mcp — Mail Specialist

- **GitHub:** [minagishl/icloud-mail-mcp](https://github.com/minagishl/icloud-mail-mcp) — 5 stars, 2 forks, 37 commits
- **Language:** TypeScript
- **Auth:** App-specific password via IMAP/SMTP

The most mature mail-focused implementation with 14 tools:

- Full CRUD: get, send, mark read, move, search, delete, set flags, download attachments
- Mailbox management: list, create, delete folders
- **Auto-organize:** Rule-based email sorting — unique among iCloud MCP servers
- Connection testing and config validation

**Key limitation:** Mail only — no calendar, contacts, or other services.

### mike-tih/icloud-mcp — Protocol-Based (CalDAV + CardDAV + IMAP)

- **GitHub:** [mike-tih/icloud-mcp](https://github.com/mike-tih/icloud-mcp) — 3 stars, 3 forks, 32 commits
- **Language:** Python
- **License:** MIT
- **Auth:** App-specific password via request headers or environment variables

Cross-platform implementation using standard protocols:

- **Calendar:** List, create, update, delete, search events via CalDAV
- **Contacts:** Full CRUD with phone, email, address, organization fields via CardDAV
- **Email:** List, read, search, send, move, delete messages via IMAP/SMTP

**Key limitation:** Python 3.10-3.12 only (3.13+ has dependency issues). Stateless architecture — no session persistence.

### localhost433/icloud-mcp — Calendar Only

- **GitHub:** [localhost433/icloud-mcp](https://github.com/localhost433/icloud-mcp) — 1 star, 1 fork, 11 commits
- **Language:** Python
- **License:** MIT
- **Auth:** App-specific password

HTTP MCP server focused exclusively on iCloud Calendar via CalDAV:

- List calendars, list/create/update/delete events
- Search events and fetch raw ICS data
- Health check endpoint

**Key limitation:** Calendar only. Advanced fields (attendees, alarms, recurrence exceptions) not preserved on update. UID matching within ±3-year window.

### adamzaidi/icloud-mcp — Most Comprehensive (65 Tools)

- **GitHub:** [adamzaidi/icloud-mcp](https://github.com/adamzaidi/icloud-mcp) — 0 stars, 1 fork, 45 commits
- **Language:** JavaScript
- **License:** MIT
- **Auth:** App-specific password via IMAP/SMTP/CalDAV/CardDAV

The **most feature-rich iCloud MCP server** with 65 tools — more than triple any other implementation:

- **Email:** Full CRUD plus reply, forward, drafts, bulk operations (move, delete, archive) with dry-run capability, thread detection via References/In-Reply-To headers, attachment downloading with byte-range fetching for large files
- **Contacts:** Full CardDAV support — create, update, search
- **Calendar:** CalDAV integration with date-range queries
- **Advanced:** Storage analysis, unsubscribe link extraction, automated email routing rules, session logging for multi-step operations, safe move protocol using fingerprinting and verification

**Key advantage:** Cross-platform (Node.js v20+), runs entirely locally with no external data transmission. The depth of email tooling (bulk ops, thread detection, storage analysis) is unmatched.

**Key limitation:** 0 stars — very new, unproven in the community. No Reminders, Notes, or macOS-native app access.

### icloud-calendar-mcp — Security-First (OWASP Compliant)

- **GitHub:** [icloud-calendar-mcp/icloud-calendar-mcp](https://github.com/icloud-calendar-mcp/icloud-calendar-mcp) — 6 stars, 1 fork, 6 commits
- **Language:** Kotlin/JVM
- **License:** Apache 2.0
- **Distribution:** npm, PyPI, MCP Registry

The **most security-focused iCloud MCP server**, explicitly designed around the OWASP MCP Top 10 framework:

- **5 Calendar tools:** List calendars, get events, create, update, delete
- **282 dedicated security tests** covering input validation, rate limiting (60 reads/min, 20 writes/min), credential protection, error sanitization
- **768 total tests** across 30 suites, including adversarial input handling, Unicode security, and ReDoS protection
- RFC 5545 (iCalendar) format compliance

**Key advantage:** The only iCloud MCP server with enterprise-grade security testing. Available across npm, PyPI, and MCP Registry.

**Key limitation:** Calendar only — no mail, contacts, or other services.

### roygabriel/mcp-icloud-calendar — Go with Observability

- **GitHub:** [roygabriel/mcp-icloud-calendar](https://github.com/roygabriel/mcp-icloud-calendar) — 0 stars, 1 fork, 26 commits
- **Language:** Go (1.21+)
- **Auth:** App-specific password

Production-oriented calendar MCP server with enterprise features:

- **5 Calendar tools:** List calendars, search events (with pagination), create, update (partial), delete
- Recurring event expansion into individual occurrences
- Attendee management with role and status tracking
- Prometheus metrics, audit logging, health check endpoints
- Structured JSON logging, configurable timeouts (default 25s), automatic retry with exponential backoff, per-account rate limiting

**Key limitation:** Calendar only. 0 stars — new and unproven.

### Lawiak/icloud-mcp — Docker & Raspberry Pi

- **GitHub:** [Lawiak/icloud-mcp](https://github.com/Lawiak/icloud-mcp) — 0 stars, 0 forks, 24 commits
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
| **Official MCP** | **None** | google/mcp (3.4k stars, GA) | 2 servers (remote + Dash) | Work IQ (preview, 13 tools) |
| **Top Community** | apple-mcp (3.1k stars, **archived**) | taylorwilsdon (1.9k stars) | amgadabdelhafez (26 stars) | Softeria (552 stars) |
| **File Storage Access** | **None — critical gap** | Full read/write/search | Full read/write/search | Full read/write (5MB limit) |
| **Auth Complexity** | **Lowest** — app-specific password | Medium — Google OAuth 2.0 | Low-Medium — Dropbox OAuth | **Highest** — Azure Entra ID |
| **Platform** | macOS-only (AppleScript) or limited cross-platform | Cross-platform | Cross-platform | Cross-platform |
| **Services Covered** | Calendar, Mail, Contacts, Reminders, Notes | Drive, Docs, Sheets, Slides, Gmail, Calendar | Files, Dash search (30+ apps) | OneDrive, Outlook, Calendar, Teams, SharePoint |
| **Apple's MCP Stance** | WWDC 2026 expected to deliver first public APIs | Official commitment | Official commitment | Official commitment |

## iCloud+ Pricing

| Plan | Price | Storage |
|------|-------|---------|
| iCloud (free) | Free | 5 GB |
| iCloud+ 50 GB | $0.99/month | 50 GB |
| iCloud+ 200 GB | $2.99/month | 200 GB |
| iCloud+ 2 TB | $9.99/month | 2 TB |
| iCloud+ 6 TB | $34.99/month | 6 TB |
| iCloud+ 12 TB | $69.99/month | 12 TB |

All paid tiers include iCloud Private Relay, Hide My Email, Custom Email Domain, and Family Sharing (up to 6 people).

**Note:** Pricing is irrelevant to MCP capabilities since no server accesses iCloud Drive storage. Current MCP servers only use Calendar, Mail, and Contacts — features available on all tiers including free.

## Apple's MCP Future

Apple is not ignoring MCP entirely, and the timeline is accelerating. In September 2025, the macOS Tahoe 26.1 and iOS 26.1 developer betas included early code references for **MCP support via App Intents** — Apple's framework for exposing app capabilities to Siri and Shortcuts. If completed, this would allow AI agents (ChatGPT, Claude, and others) to directly interact with apps on Mac, iPhone, and iPad.

**WWDC 2026** (June 8-12) is expected to be the inflection point. Apple has confirmed the conference will spotlight **iOS 27** alongside AI advancements across all platforms. Industry analysts expect the **first public MCP APIs** to arrive at WWDC 2026 via an expanded App Intents framework, though mass adoption is unlikely before iOS 27/macOS 28. A major **Siri overhaul** is also anticipated, with three core components: a planner, a search operator, and a summarizer — all designed to be more context-aware and capable of threading personal context through tasks.

However, this remains platform-level MCP support (apps exposing their capabilities to AI agents on-device), not a cloud API for iCloud services. There is still no indication that Apple plans to offer a remote iCloud MCP server comparable to Google's, Dropbox's, or Microsoft's official offerings.

## Known Issues

1. **No iCloud Drive access** — The most critical gap. No community MCP server accesses iCloud Drive file storage. CloudKit integration would require an Apple Developer account ($99/year) and Apple-specific authentication that no one has implemented. This makes iCloud MCP servers fundamentally different from Google Drive, Dropbox, and OneDrive MCP servers.

2. **Best server is archived** — supermemoryai/apple-mcp (3,100 stars) was archived in January 2026 and receives no updates or bug fixes. The most popular active server (MrGo2/icloud-mcp) has only 9 stars, though adamzaidi/icloud-mcp (65 tools, 45 commits) offers the most comprehensive active implementation.

3. **macOS dependency** — The most capable implementations (apple-mcp, MrGo2 local mode) require macOS with AppleScript permissions. Linux and Windows users are limited to CalDAV/CardDAV/IMAP access only (calendar, contacts, email).

4. **No official server** — Apple has not released an official MCP server for any iCloud service. Google, Dropbox, and Microsoft all have official MCP servers. Apple's first public MCP APIs are expected at WWDC 2026 (June 8-12), but these will be platform-level App Intents, not cloud APIs.

5. **Growing but fragmented community** — Outside the archived apple-mcp, the ecosystem has grown to 9+ implementations, but most have single-digit stars. The community is diversifying (Kotlin, Go, Python, JavaScript, TypeScript) but no single active project has emerged as a clear successor to apple-mcp.

6. **pyicloud broken** — The popular Python library for iCloud access (pyicloud) stopped working after Apple changed web authentication to SRP-6a in 2024-2025. This broke several MCP servers and forced developers to use CalDAV/CardDAV/IMAP protocols instead.

7. **Cannot read Messages** — macOS security restrictions prevent even AppleScript-based servers from reading iMessage/SMS content. Sending is possible; reading is blocked.

8. **Limited Reminders/Notes access** — Reminders and Notes are only available through AppleScript (macOS only). No cross-platform protocol access exists for these services.

9. **No Find My access** — Apple's Find My API is internal-only. No MCP server can track device locations or AirTags.

10. **App-specific password scope** — While easy to generate, app-specific passwords grant broad access to the associated Apple ID services. There is no way to scope permissions to specific calendars, mailboxes, or contacts — it's all-or-nothing.

## Bottom Line

**Rating: 2.5 out of 5**

iCloud MCP servers present a paradox: the world's most valuable company with 850+ million iCloud users has the **weakest MCP ecosystem** of any major cloud storage provider. The fundamental problem is straightforward — **no iCloud Drive file access**. While Google Drive, Dropbox, and OneDrive MCP servers let AI agents read, write, search, and organize files, iCloud MCP servers are limited to calendar events, email, and contacts.

The community has done what it can with available protocols. **supermemoryai/apple-mcp** reached an impressive 3,100 stars by providing AppleScript-based access to 7 macOS apps, but it was archived in January 2026. The active ecosystem has grown significantly since then: **adamzaidi/icloud-mcp** now offers 65 tools with deep email capabilities (thread detection, bulk operations, storage analysis), **icloud-calendar-mcp** brings enterprise-grade OWASP security compliance with 768 tests, and **MrGo2/icloud-mcp** (9 stars) offers the broadest service coverage with dual local/cloud modes.

The one genuine advantage: **authentication is dead simple**. App-specific passwords are vastly easier than Google OAuth, Dropbox OAuth, or Azure Entra ID. But this simplicity is a consequence of limited API access, not thoughtful developer experience.

**Who should use iCloud MCP servers:**

- **macOS users** who want AI agents to manage Calendar, Mail, Contacts, Reminders, and Notes alongside other Apple apps
- **Apple ecosystem users** who need basic PIM (personal information management) automation and don't need file storage access
- **Developers** exploring Apple MCP integration ahead of Apple's expected platform-level MCP support

**Who should wait:**

- **Anyone needing file storage** — iCloud Drive is inaccessible; use Google Drive, Dropbox, or OneDrive MCP servers instead
- **Cross-platform users** — full capability requires macOS; other platforms get calendar/mail/contacts only
- **Teams and organizations** — the community is too small and fragmented for production reliability

The 2.5/5 rating reflects the critical absence of iCloud Drive access, no official Apple server, and a community ecosystem where the best implementation is archived. WWDC 2026 (June 8-12) is expected to deliver Apple's first public MCP APIs, but these will be platform-level App Intents, not cloud iCloud APIs. Today, iCloud remains the clear last-place finisher among major cloud storage MCP ecosystems — though the growing community (9+ implementations) suggests momentum is building.

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official Apple announcements. Information is current as of April 2026. See our [About page](/about/) for details on our review process.*

