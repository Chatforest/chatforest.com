---
title: "iCloud MCP Servers — AI Agents for Apple Calendar, Mail, Contacts, Reminders, and Notes"
date: 2026-03-23T23:30:00+09:00
description: "Apple has no official iCloud MCP server, but community projects let AI agents access Calendar, Mail, Contacts, and Reminders via CalDAV, CardDAV, and IMAP. The biggest gap: no iCloud Drive file access. Here's the honest review."
og_description: "iCloud MCP servers: no official Apple server, community implementations for Calendar, Mail, Contacts, and Reminders. No iCloud Drive access. Rating: 2.5/5."
content_type: "Review"
card_description: "Apple has no official iCloud MCP server and is only beginning to explore MCP support in iOS/macOS 26.1 betas. Community implementations provide access to Calendar (CalDAV), Mail (IMAP/SMTP), Contacts (CardDAV), and Reminders, but no server offers iCloud Drive file access — the critical gap versus Google Drive, Dropbox, and OneDrive."
last_refreshed: 2026-03-23
---

**At a glance:** [supermemoryai/apple-mcp](https://github.com/supermemoryai/apple-mcp) (3,000 stars, archived, MIT) + [MrGo2/icloud-mcp](https://github.com/MrGo2/icloud-mcp) (5 stars, active, MIT). Apple has 850+ million iCloud users and a $4+ trillion market cap, but **no official MCP server** and **no iCloud Drive file access** through any community implementation. The biggest cloud storage MCP gap.

iCloud MCP servers let AI agents **manage Apple Calendar events, send and read iCloud Mail, access Contacts, and handle Reminders** — all through natural language prompts. However, unlike Google Drive, Dropbox, and OneDrive MCP servers, **no implementation provides iCloud Drive file access** — the file storage feature that most users associate with iCloud. Apple is beginning to explore MCP support at the platform level in iOS/macOS 26.1 betas, but a working integration is not yet available.

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

- **GitHub:** [supermemoryai/apple-mcp](https://github.com/supermemoryai/apple-mcp) — 3,000 stars, 268 forks, 87 commits, 11 contributors
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

- **GitHub:** [MrGo2/icloud-mcp](https://github.com/MrGo2/icloud-mcp) — 5 stars, 1 fork, 4 commits
- **Language:** JavaScript
- **License:** MIT
- **Auth:** AppleScript permissions (local) or app-specific password (cloud)

The most versatile active implementation with two operational modes:

- **Local mode (31 tools):** AppleScript-based access to Email, Calendar, Contacts, Reminders, Notes, Messages, Safari — macOS only
- **Cloud mode (17 tools):** CalDAV, CardDAV, IMAP/SMTP — cross-platform with app-specific password

**Key limitation:** 4 commits suggests early-stage development. Cannot read Messages (macOS security restriction). No iCloud Drive access.

### minagishl/icloud-mail-mcp — Mail Specialist

- **GitHub:** [minagishl/icloud-mail-mcp](https://github.com/minagishl/icloud-mail-mcp) — 4 stars, 2 forks, 37 commits
- **Language:** TypeScript
- **Auth:** App-specific password via IMAP/SMTP

The most mature mail-focused implementation with 14 tools:

- Full CRUD: get, send, mark read, move, search, delete, set flags, download attachments
- Mailbox management: list, create, delete folders
- **Auto-organize:** Rule-based email sorting — unique among iCloud MCP servers
- Connection testing and config validation

**Key limitation:** Mail only — no calendar, contacts, or other services.

### mike-tih/icloud-mcp — Protocol-Based (CalDAV + CardDAV + IMAP)

- **GitHub:** [mike-tih/icloud-mcp](https://github.com/mike-tih/icloud-mcp) — 2 stars, 2 forks, 32 commits
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

### iteratio/icloud-mcp — macOS Keychain Auth

- **GitHub:** [iteratio/icloud-mcp](https://github.com/iteratio/icloud-mcp) — 0 stars, 0 forks, 3 commits
- **Language:** Python
- **Platform:** macOS only (credentials in Keychain)

Local MCP server with credentials stored in macOS Keychain (never in files or environment variables):

- **Calendar:** List, get, create events via CalDAV
- **Mail:** List, read, send messages via IMAP/SMTP
- **Reminders:** List, create, complete via EventKit

**Key limitation:** 3 commits — very early stage. macOS 12+ required. Note: "pyicloud is now broken — Apple changed web auth to SRP-6a in 2024-2025."

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
| **Top Community** | apple-mcp (3k stars, **archived**) | taylorwilsdon (1.9k stars) | amgadabdelhafez (26 stars) | Softeria (552 stars) |
| **File Storage Access** | **None — critical gap** | Full read/write/search | Full read/write/search | Full read/write (5MB limit) |
| **Auth Complexity** | **Lowest** — app-specific password | Medium — Google OAuth 2.0 | Low-Medium — Dropbox OAuth | **Highest** — Azure Entra ID |
| **Platform** | macOS-only (AppleScript) or limited cross-platform | Cross-platform | Cross-platform | Cross-platform |
| **Services Covered** | Calendar, Mail, Contacts, Reminders, Notes | Drive, Docs, Sheets, Slides, Gmail, Calendar | Files, Dash search (30+ apps) | OneDrive, Outlook, Calendar, Teams, SharePoint |
| **Apple's MCP Stance** | Exploring in iOS/macOS 26.1 betas | Official commitment | Official commitment | Official commitment |

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

Apple is not ignoring MCP entirely. In September 2025, the macOS Tahoe 26.1 and iOS 26.1 developer betas included early code references for **MCP support via App Intents** — Apple's framework for exposing app capabilities to Siri and Shortcuts. If completed, this would allow AI agents (ChatGPT, Claude, and others) to directly interact with apps on Mac, iPhone, and iPad.

However, this is platform-level MCP support (apps exposing their capabilities to AI agents on-device), not a cloud API for iCloud services. There is no indication that Apple plans to offer a remote iCloud MCP server comparable to Google's, Dropbox's, or Microsoft's official offerings.

## Known Issues

1. **No iCloud Drive access** — The most critical gap. No community MCP server accesses iCloud Drive file storage. CloudKit integration would require an Apple Developer account ($99/year) and Apple-specific authentication that no one has implemented. This makes iCloud MCP servers fundamentally different from Google Drive, Dropbox, and OneDrive MCP servers.

2. **Best server is archived** — supermemoryai/apple-mcp (3,000 stars) was archived in January 2026 and receives no updates or bug fixes. The next most popular active server has only 5 stars.

3. **macOS dependency** — The most capable implementations (apple-mcp, MrGo2 local mode) require macOS with AppleScript permissions. Linux and Windows users are limited to CalDAV/CardDAV/IMAP access only (calendar, contacts, email).

4. **No official server** — Apple has not released an official MCP server for any iCloud service. Google, Dropbox, and Microsoft all have official MCP servers. Apple's MCP exploration is limited to platform-level App Intents in developer betas.

5. **Small, fragmented community** — Outside the archived apple-mcp, no implementation exceeds 5 stars. Most have single-digit commits and single contributors, suggesting low maintenance likelihood.

6. **pyicloud broken** — The popular Python library for iCloud access (pyicloud) stopped working after Apple changed web authentication to SRP-6a in 2024-2025. This broke several MCP servers and forced developers to use CalDAV/CardDAV/IMAP protocols instead.

7. **Cannot read Messages** — macOS security restrictions prevent even AppleScript-based servers from reading iMessage/SMS content. Sending is possible; reading is blocked.

8. **Limited Reminders/Notes access** — Reminders and Notes are only available through AppleScript (macOS only). No cross-platform protocol access exists for these services.

9. **No Find My access** — Apple's Find My API is internal-only. No MCP server can track device locations or AirTags.

10. **App-specific password scope** — While easy to generate, app-specific passwords grant broad access to the associated Apple ID services. There is no way to scope permissions to specific calendars, mailboxes, or contacts — it's all-or-nothing.

## Bottom Line

**Rating: 2.5 out of 5**

iCloud MCP servers present a paradox: the world's most valuable company with 850+ million iCloud users has the **weakest MCP ecosystem** of any major cloud storage provider. The fundamental problem is straightforward — **no iCloud Drive file access**. While Google Drive, Dropbox, and OneDrive MCP servers let AI agents read, write, search, and organize files, iCloud MCP servers are limited to calendar events, email, and contacts.

The community has done what it can with available protocols. **supermemoryai/apple-mcp** reached an impressive 3,000 stars by providing AppleScript-based access to 7 macOS apps, but it was archived in January 2026. The remaining active servers are small (0-5 stars) and narrowly focused. **MrGo2/icloud-mcp** offers the broadest active coverage with dual local/cloud modes, and **mike-tih/icloud-mcp** is the most mature cross-platform option with 32 commits covering CalDAV, CardDAV, and IMAP.

The one genuine advantage: **authentication is dead simple**. App-specific passwords are vastly easier than Google OAuth, Dropbox OAuth, or Azure Entra ID. But this simplicity is a consequence of limited API access, not thoughtful developer experience.

**Who should use iCloud MCP servers:**

- **macOS users** who want AI agents to manage Calendar, Mail, Contacts, Reminders, and Notes alongside other Apple apps
- **Apple ecosystem users** who need basic PIM (personal information management) automation and don't need file storage access
- **Developers** exploring Apple MCP integration ahead of Apple's expected platform-level MCP support

**Who should wait:**

- **Anyone needing file storage** — iCloud Drive is inaccessible; use Google Drive, Dropbox, or OneDrive MCP servers instead
- **Cross-platform users** — full capability requires macOS; other platforms get calendar/mail/contacts only
- **Teams and organizations** — the community is too small and fragmented for production reliability

The 2.5/5 rating reflects the critical absence of iCloud Drive access, no official Apple server, and a community ecosystem where the best implementation is archived. Apple's exploration of MCP in iOS/macOS 26.1 betas offers future hope, but today, iCloud is the clear last-place finisher among major cloud storage MCP ecosystems.

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official Apple announcements. Information is current as of March 2026. See our [About page](/about/) for details on our review process.*
