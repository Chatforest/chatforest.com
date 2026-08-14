---
title: "Apple & macOS MCP Servers (2026) — 20+ Reviewed"
date: 2026-03-16T23:30:00+09:00
lastmod: 2026-08-14
description: "20+ Apple and macOS MCP servers reviewed — Siri Shortcuts, HomeKit, Apple Music, Notes, Reminders, AppleScript automation, and more. Peekaboo (~5,000 stars) leads, supermemoryai/apple-mcp (3,100 stars, archived), iMCP (~1,500 stars) covers 7 Apple services natively. Rating: 4/5."
og_description: "Apple & macOS MCP servers: Peekaboo (~5,000 stars — screenshots + GUI automation), supermemoryai/apple-mcp (3,100 stars, archived Jan 2026), iMCP (~1,500 stars — Messages, Calendar, Contacts, Maps, Weather), macos-automator-mcp (~870 stars — 200+ AppleScript recipes). 20+ servers reviewed. Rating: 4/5."
content_type: "Review"
card_description: "20+ Apple and macOS MCP servers reviewed. Peekaboo (~5,000 stars) provides screenshots and full GUI automation. supermemoryai/apple-mcp (3,100 stars, archived Jan 2026) covers Notes, Reminders, Calendar, Mail, Messages, Contacts, and Maps. iMCP (~1,500 stars) is a native macOS app integrating Messages, Calendar, Contacts, Reminders, Maps, and Weather. macos-automator-mcp (~870 stars) ships 200+ AppleScript recipes. Plus Siri Shortcuts, HomeKit, Apple Music, Safari, and Raycast. WWDC 2026 shipped MCP support in Xcode for developers, not native Siri/App Intents integration as had been speculated."
last_refreshed: 2026-08-14
sources_audited: 2026-08-14
---

Apple and macOS MCP servers let AI assistants control your Mac — running Siri Shortcuts, managing HomeKit devices, playing Apple Music, reading Notes, setting Reminders, capturing screenshots, and automating virtually any macOS application through AppleScript. Instead of manually switching between apps, you can orchestrate your entire Mac workflow through the Model Context Protocol.

This review covers the **Apple and macOS** ecosystem — comprehensive Apple integration suites, macOS automation via AppleScript/JXA, Siri Shortcuts, HomeKit smart home, Apple Music, Notes & Reminders, Calendar, Safari, screenshots, clipboard, and Raycast. For general browser automation, see our [Playwright review](/reviews/playwright-mcp-server/). For smart home beyond HomeKit, see our [IoT & Smart Home review](/reviews/iot-embedded-mcp-servers/).

The headline findings: **Peekaboo ([~5,000 stars](https://github.com/openclaw/Peekaboo)) has evolved from a screenshot tool into a [full GUI automation platform](https://peekaboo.sh/)** — now the most-starred Apple MCP server, and the repo has since transferred from steipete's personal account into the openclaw GitHub organization (Peter Steinberger remains the credited author). **supermemoryai/apple-mcp ([3,100 stars](https://github.com/supermemoryai/apple-mcp)) covers 7 Apple apps** in one package — though it was [archived in January 2026](https://github.com/supermemoryai/apple-mcp). **iMCP ([~1,500 stars](https://github.com/mattt/iMCP)) is a native macOS app** providing MCP access to Messages, Contacts, Calendar, Reminders, Maps, Weather, and Location — a strong actively-maintained alternative. **macos-automator-mcp ([~870 stars](https://github.com/steipete/macos-automator-mcp)) ships 200+ automation recipes**. **Siri Shortcuts provide a bridge to the entire Apple/iOS ecosystem**. **HomeKit has 2 active MCP implementations** (a third, somethingwithproof/home-mcp, has since been removed from GitHub) — HomeClaw ([155 stars](https://github.com/omarshahine/HomeClaw)) reached v1.0.0 in March 2026 and is now at [v1.0.10](https://github.com/omarshahine/HomeClaw/releases), available on the Mac App Store and TestFlight. **Apple Music has 4 independent servers**. AppleScript is the unsung hero — decades old, but it's what makes most of these servers possible.

**Industry context (updated after WWDC 2026):** macOS Tahoe 26.1 developer beta [revealed early signs of native MCP integration](https://mcp.directory/blog/apple-prepares-revolution-mcp-integration-in-macos-ios-ipados) through the App Intents framework, and speculation ahead of WWDC 2026 (June 8-12) anticipated Siri and Apple Intelligence gaining direct MCP client support. **That did not happen.** Per Apple's own [Platforms State of the Union](https://developer.apple.com/videos/play/wwdc2026/102/) and [WWDC 2026 developer recap](https://developer.apple.com/news/?id=lvart8mq), Apple brought MCP support to **Xcode 27** — letting coding agents in Xcode connect to MCP tools and plugins — but Apple Intelligence and Siri/App Intents did not gain MCP client support. Basic app-access servers remain relevant; specialized tools like Peekaboo, macos-automator-mcp, and HomeClaw retain their value either way.

**Category:** [Developer Tools](/categories/developer-tools/)

---

## Comprehensive Apple Integration

### supermemoryai/apple-mcp (Second Most-Starred — Archived)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [apple-mcp](https://github.com/supermemoryai/apple-mcp) | 3,100 | TypeScript | — | 20+ |

> **⚠️ Archived:** This repository was [archived on January 1, 2026](https://github.com/supermemoryai/apple-mcp) and is now read-only. It still works if installed, but receives no updates or bug fixes. An [enhanced fork by Ayaanisthebest](https://github.com/Ayaanisthebest/appleMCP) adds smart contact resolution, rich-text notes search, and improved error handling.

The **second most-starred Apple MCP server** (behind Peekaboo, below) — a comprehensive [collection of apple-native tools](https://github.com/supermemoryai/apple-mcp) covering seven apps (per the project's own README as of this audit — an earlier version of this review incorrectly listed Music and Finder instead of Maps):

- **Notes** — create and search notes
- **Reminders** — create reminders with due dates; search and list
- **Calendar** — create events; search and list upcoming events
- **Contacts** — find contacts and retrieve phone numbers
- **Mail** — send emails with attachments, CC/BCC; search; schedule
- **Messages** — send, read, and schedule messages
- **Maps** — search locations, save favorites, get directions, create guides, drop pins

Enables complex multi-app workflows like ["Read my conference notes, find contacts for the people I met, and send them a thank you message."](https://github.com/supermemoryai/apple-mcp#readme) Available through [Smithery](https://github.com/supermemoryai/apple-mcp#readme) with one-click setup via `.dxt` file or manual configuration with Bun/TypeScript.

### mattt/iMCP (Best Active Alternative)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [iMCP](https://github.com/mattt/iMCP) | ~1,500 | Swift | — | ~7 |

A **native macOS application** that provides an MCP server for personal digital services — the strongest actively-maintained alternative to the archived supermemoryai/apple-mcp. Created by [Mattt Thompson](https://github.com/mattt) (creator of AFNetworking/Alamofire, former Apple developer). [v1.4.1](https://github.com/mattt/iMCP/releases) released May 2026, adding a Shortcuts service:

- **Calendar** — view and manage events with recurrence and alarms
- **Contacts** — search and access contact information
- **Messages** — access iMessage history with date ranges (via custom `typedstream` decoder since Apple provides no public API)
- **Reminders** — create and view with priorities and alerts
- **Maps** — place search, directions, and travel time estimation
- **Weather** — current conditions for any location
- **Location** — current position and coordinate conversion

Uses the **App Sandbox security model** and **Bonjour** for local network discovery between the bundled CLI and the UI app. Unlike AppleScript-based servers, iMCP uses native macOS frameworks directly — Contacts.framework, EventKit, MapKit — providing more reliable integration. The ~1,500 stars and active maintenance make this the recommended choice for users who need multi-app Apple integration without relying on archived projects.

## macOS Automation

### steipete/macos-automator-mcp (Best Automation)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [macos-automator-mcp](https://github.com/steipete/macos-automator-mcp) | ~870 | TypeScript | — | 200+ recipes |

Created by [Peter Steinberger](https://en.wikipedia.org/wiki/Peter_Steinberger_(programmer)) (founder of PSPDFKit) — transforms your AI assistant into a [macOS automation powerhouse](https://www.pulsemcp.com/servers/steipete-macos-automator):

- **200+ pre-built automation recipes** — toggle dark mode, extract URLs from Safari, manage windows, control system settings
- **AppleScript and JXA execution** — run both scripting languages through MCP
- **Knowledge base** — lazy or eager loading, customizable via `~/.macos-automator/knowledge_base`
- **Custom skills** — add your own automation recipes
- **System Events / UI scripting** — for apps with clicks, keystrokes, or menus that AppleScript's app-specific dictionary can't reach, [the tool requests macOS Accessibility access](https://github.com/steipete/macos-automator-mcp) to drive them
- **Published on npm** — `@steipete/macos-automator-mcp`

The knowledge base approach is clever — rather than hardcoding capabilities, it ships a library of recipes that the AI can browse and execute contextually. For apps with a proper AppleScript dictionary, it scripts the app's own commands directly rather than simulating clicks — more reliable than pure GUI automation — but per [the project's own README](https://github.com/steipete/macos-automator-mcp), it still falls back to Accessibility-based UI scripting (System Events) for apps or actions that don't expose an AppleScript interface, so it isn't immune to UI-layout breakage in every case.

### joshrutkowski/applescript-mcp (General AppleScript)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [applescript-mcp](https://github.com/joshrutkowski/applescript-mcp) | ~390 | TypeScript | — | ~11 |

A [standardized interface for AI applications](https://www.pulsemcp.com/servers/joshrutkowski-applescript) to control macOS through AppleScript — created by [Josh Rutkowski, a Software Development Engineer at Amazon](https://github.com/joshrutkowski):

- **System functions** — volume, dark mode, app launching/closing, notifications and Do Not Disturb
- **File management** — Finder file selection, search, and Quick Look preview
- **Application control** — launch, quit, detect active app
- **Calendar** — event creation and daily schedule viewing (Reminders support is [listed as a planned feature](https://github.com/joshrutkowski/applescript-mcp), not yet shipped)
- **Communication** — Mail composition/retrieval, Messages sending/search, Notes
- **iTerm integration** — terminal command execution and clipboard pasting from AI
- **Shortcuts** — list and run macOS Shortcuts automations

Occupies a "batteries-included" sweet spot — more convenience than raw AppleScript execution tools, while remaining accessible for non-experts.

### peakmojo/applescript-mcp (Simple Execution)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [applescript-mcp](https://github.com/peakmojo/applescript-mcp) | 460 | — | — | ~3 |

Minimal setup — run any AppleScript code through MCP. Simple and straightforward for users who know AppleScript and just want execution capability.

## Siri Shortcuts

### recursechat/mcp-server-apple-shortcuts (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts) | 341 | — | Apache-2.0 | ~3 |

Designed for safe, controlled Shortcuts execution — lets AI models trigger shortcuts while maintaining security boundaries. Now the most-starred server in this category, ahead of dvcrn's implementation below (a stale table cell in an earlier version of this review had left its star count blank).

### dvcrn/mcp-server-siri-shortcuts (Auto-Generated Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-siri-shortcuts](https://github.com/dvcrn/mcp-server-siri-shortcuts) | 191 | TypeScript | GPL-3.0 | ~3 |

[Access Siri Shortcuts functionality](https://www.pulsemcp.com/servers/dvcrn-mcp-server-siri-shortcuts) from the macOS Shortcuts app:

- **List shortcuts** — discover available automations
- **Open shortcuts** — view in the Shortcuts app
- **Run shortcuts** — execute directly from AI with optional input parameters
- **Auto-generated tools** — automatically creates tools for each available shortcut

Uses the macOS `shortcuts` CLI command under the hood. Since Shortcuts can control HomeKit, trigger automations, interact with hundreds of apps, and bridge to iOS — this effectively gives MCP access to the **entire Apple Shortcuts ecosystem**.

### CaseyRo/mac_shortcuts_mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mac_shortcuts_mcp](https://github.com/CaseyRo/mac_shortcuts_mcp) | 1 | Python | — | ~3 |

Python-based alternative for running macOS Shortcuts from MCP-compatible clients.

## HomeKit / Smart Home

### somethingwithproof/home-mcp (Removed)

> **⚠️ Removed:** This repository is no longer available on GitHub (404) as of this audit. It previously controlled HomeKit devices, scenes, and automations via Apple Home on macOS. If you need HomeKit control, consider IntentCP or HomeClaw below.

### jaebinsim/IntentCP (Zero Infrastructure)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [IntentCP](https://github.com/je-empty/IntentCP) | 22 | Python | — | ~5 |

Formerly HomeMCP under the `jaebinsim` account, now rebranded as **IntentCP** and moved to the `je-empty` GitHub account — a lightweight, intent-driven control plane for smart home automation. Uses iOS Shortcuts and cloud IoT platforms (Tuya) without requiring local LLM hosting. Trigger with "Hey Siri" + a Shortcut, converting spoken intent into safe execution URLs.

### omarshahine/HomeClaw (Native App)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [HomeClaw](https://github.com/omarshahine/HomeClaw) | 155 | Swift | — | ~10 |

A unified **Mac Catalyst app** providing HomeKit smart home control via MCP — bridges HomeKit (which [lacks a public API](https://github.com/omarshahine/HomeClaw)) through a lightweight menu bar application. Reached **v1.0.0** in March 2026 as the first stable release, and is now at [v1.0.10](https://github.com/omarshahine/HomeClaw/releases) (July 2026):

- **Lights** — on/off, brightness, color
- **Locks** — lock/unlock
- **Thermostats** — temperature control
- **Scenes** — create, import, trigger, and delete scenes
- **Window coverings, fans, sensors** — broad device category support
- **Event logging** — query HomeKit activity history with filtering
- **Webhook integration** — external automation pipelines
- **Characteristic-based automation triggers** — motion, contact, occupancy, and temperature-threshold conditions, plus [time-of-day windows added in v1.0.10](https://github.com/omarshahine/HomeClaw/releases)
- **OpenClaw compatibility** — declared compatibility metadata for ClawHub integration

Compatible with Claude Desktop, Claude Code, and OpenClaw. Distributed via the **Mac App Store** and **TestFlight** (beta) in addition to building from source. Zero open issues as of this audit.

## Apple Music

### kennethreitz/mcp-applemusic (Most Known)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-applemusic](https://github.com/kennethreitz/mcp-applemusic) | 89 | Python | MIT | ~8 |

[Experimental FastMCP server](https://www.pulsemcp.com/servers/kennethreitz-applemusic) from [Kenneth Reitz](https://github.com/kennethreitz) (creator of the Python `requests` library) — controls Apple Music via AppleScript. Requires Python 3.13+ and macOS:

- **Playback** — play, pause, next, previous
- **Search** — find songs in your library
- **Playlists** — create playlists with specific songs
- **Library** — browse your music collection and get statistics

A local-first solution — your music data and listening habits never leave your computer. Current version: **[v0.1.5](https://pypi.org/project/mcp-applemusic/)** on PyPI. Installable via `uvx mcp-applemusic` (or `uvx -p 3.13 -n mcp-applemusic` for explicit Python 3.13).

### epheterson/applemusic-mcp (REST API + Web Fallback)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [applemusic-mcp](https://github.com/epheterson/applemusic-mcp) | 81 | — | — | ~5 |

Renamed from `mcp-applemusic` to `applemusic-mcp` (old URLs redirect). Prioritizes the **official Apple Music API** via developer tokens for writes, and falls back to a web-player token or AppleScript automation only for operations the official API doesn't expose — a more API-first approach than the pure-AppleScript servers here, though not exclusively REST.

### samwang0723/mcp-applemusic (TypeScript)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-applemusic](https://github.com/samwang0723/mcp-applemusic) | 2 | TypeScript | — | ~6 |

TypeScript implementation using Express.js — controls Apple Music via AppleScript commands (osascript).

### pedrocid/music-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [music-mcp](https://github.com/pedrocid/music-mcp) | 7 | — | — | ~5 |

Another AppleScript-based Apple Music controller via MCP.

## Notes & Reminders

### karlhepler/apple-mcp (Notes + Reminders — Removed)

> **⚠️ Removed:** This repository is no longer available on GitHub (404). If you need Notes and Reminders via MCP, consider supermemoryai/apple-mcp (archived but functional) or the dedicated Reminders server below.

### mggrim/apple-reminders-mcp-server (Most Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [apple-reminders-mcp-server](https://github.com/mggrim/apple-reminders-mcp-server) | 0 | — | — | 18 |

The **most feature-rich Reminders-only server** with 18 comprehensive tools:

- **Full CRUD** for reminders and lists
- **Natural language date parsing** — "next Tuesday at 3pm"
- **Priority and due date management**

### FradSer/mcp-server-apple-events (EventKit)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-apple-events](https://github.com/FradSer/mcp-server-apple-events) | 180 | Swift | — | ~8 |

Uses **native EventKit** framework for Reminders and Calendar integration — bypasses AppleScript entirely for a more reliable macOS-native approach.

## iCloud & Calendar

### iteratio/icloud-mcp (Removed)

> **⚠️ Removed:** This repository is no longer available on GitHub (404) as of this audit. It previously provided a local MCP server for iCloud Calendar, Mail, and Reminders with credentials stored in the macOS Keychain. Several newer alternatives exist on GitHub (e.g. adamzaidi/icloud-mcp, MrGo2/icloud-mcp) but have not been reviewed here.

## Screenshots & Screen Control

### openclaw/Peekaboo (Best Screenshots + GUI Automation)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Peekaboo](https://github.com/openclaw/Peekaboo) | ~5,000 | TypeScript/Swift | — | 10+ |

The **most-starred Apple MCP server** — now far more than just screenshots. Created by Peter Steinberger; the repo has since been transferred from his personal `steipete` account into the `openclaw` GitHub organization (old `steipete/Peekaboo` URLs redirect there). [Steinberger describes the project](https://steipete.me/posts/2025/peekaboo-mcp-lightning-fast-macos-screenshots-for-ai-agents) as giving AI agents "eyes" on your Mac. It now bills itself as a ["macOS automation toolkit for humans and agents"](https://peekaboo.sh/) that captures pixels, reads the accessibility tree, and drives input:

- **Screenshot capture** — pixel-accurate window and screen captures via Apple's ScreenCaptureKit
- **Visual Question Answering** — analyze screenshots using a configurable vision-capable model from any of the [supported providers](https://github.com/openclaw/Peekaboo/blob/main/docs/providers.md) — OpenAI, Anthropic, Google, xAI, MiniMax, Kimi, OpenRouter, Ollama, or LM Studio
- **GUI automation** — click, type, scroll, hotkey, menu interaction, window management
- **App and dock control** — launch, focus, and manage applications
- **Natural-language agent** — chains Peekaboo tools (see, click, type, scroll, hotkey, menu, window, app, dock, space)

Built with TypeScript + Swift — TypeScript for MCP/npm distribution, Swift for [direct ScreenCaptureKit access](https://steipete.me/posts/2025/peekaboo-mcp-lightning-fast-macos-screenshots-for-ai-agents) without requiring focus changes. Part of Steinberger's growing ecosystem alongside macos-automator-mcp. Currently at [v4.1.0](https://github.com/openclaw/Peekaboo/releases/latest) (August 2026), up from the v3.x beta line covered in earlier versions of this review. Requires macOS 15+.

### jhead/macos-screen-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [macos-screen-mcp](https://github.com/jhead/macos-screen-mcp) | 14 | — | — | ~4 |

Screenshot and **window control** for macOS — captures screens and manages window positioning. Built for Cursor but works with any MCP client.

## Safari & Browsing

### lxman/safari-mcp-server (Removed)

> **⚠️ Removed:** This repository is no longer available on GitHub (404) as of this audit. It previously used Selenium WebDriver to control Safari for browser automation and testing. A current alternative covering similar ground is [achiya-automation/safari-mcp](https://github.com/achiya-automation/safari-mcp) (167 stars), which drives Safari via AppleScript rather than Selenium — not independently reviewed here.

## Clipboard & Utilities

### vlad-ds/maccy-clipboard-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [maccy-clipboard-mcp](https://github.com/vlad-ds/maccy-clipboard-mcp) | 9 | — | — | ~5 |

Connects to **Maccy clipboard history** on macOS:

- **Search** clipboard entries by content
- **Retrieve** recent clipboard items
- **Support for text and images**
- **Pin entries** and **export data**

> **⚠️ Security note:** This server [exposes your entire clipboard history](https://github.com/vlad-ds/maccy-clipboard-mcp) — potentially containing passwords, API keys, and sensitive data — to an AI system. Users assume full responsibility.

Requires [Maccy](https://maccy.app/) clipboard manager to be installed.

### ExpertVagabond/raycast-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [raycast-mcp-server](https://github.com/ExpertVagabond/raycast-mcp-server) | 5 | — | — | 9 |

**9 tools for Raycast workflow automation** — integrates the popular macOS launcher with AI assistants through MCP. Extends Raycast's extensibility into the AI agent ecosystem.

## What's Missing

Despite strong coverage, significant gaps remain:

- **No Xcode integration** — no project management, build automation, or test running via MCP
- **No System Settings/Preferences control** — can't toggle Wi-Fi, Bluetooth, or other system preferences
- **No Time Machine** — no backup management or restore capabilities
- **No AirDrop** — no file transfer between Apple devices
- **No Keychain password retrieval** — understandable given security implications
- **No Focus/Do Not Disturb** — no mode switching
- **No Disk Utility** — no storage management
- **No Terminal.app integration** — beyond standard shell MCP servers
- **No macOS Automator workflow import** — can't convert existing .workflow files

## The Bottom Line

**Rating: 4/5** — Apple and macOS MCP is surprisingly mature, now led by Peekaboo ([~5,000 stars](https://github.com/openclaw/Peekaboo), actively developed) and supermemoryai/apple-mcp ([3,100 stars](https://github.com/supermemoryai/apple-mcp), [archived since January 2026](https://github.com/supermemoryai/apple-mcp)). The addition of **iMCP ([~1,500 stars](https://github.com/mattt/iMCP))** fills the gap left by apple-mcp's archival — it covers 7 Apple services through native frameworks rather than AppleScript. [macos-automator-mcp (~870 stars)](https://github.com/steipete/macos-automator-mcp) provides 200+ automation recipes.

The key insight: **AppleScript, despite being decades old, is the [perfect bridge](https://skywork.ai/skypage/en/macos-ai-automator-unlocking/1981180204707401728) between MCP and macOS applications.** Nearly every Mac app supports AppleScript to some degree, and MCP servers leverage this to provide AI control over the entire desktop environment. Siri Shortcuts extend this further, bridging into iOS and HomeKit. Meanwhile, iMCP demonstrates a newer approach — using native macOS frameworks (EventKit, Contacts.framework, MapKit) directly, bypassing AppleScript entirely.

HomeKit now has two active independent implementations (HomeClaw at [155 stars](https://github.com/omarshahine/HomeClaw) leads — [v1.0.10](https://github.com/omarshahine/HomeClaw/releases) with characteristic-based automation triggers, now on Mac App Store and TestFlight; a third, somethingwithproof/home-mcp, has since been removed from GitHub). Apple Music has four (kennethreitz at [89 stars](https://github.com/kennethreitz/mcp-applemusic) leads, now at v0.1.5). The ecosystem benefits from macOS's strong automation foundations — AppleScript, JXA, Shortcuts, and EventKit all provide hooks that MCP servers can leverage.

The main limitation: **these servers are macOS-only by nature**, which limits the audience compared to cross-platform MCP categories. Speculation ahead of WWDC 2026 (June 8-12) — based on [macOS Tahoe 26.1 beta code](https://mcp.directory/blog/apple-prepares-revolution-mcp-integration-in-macos-ios-ipados) hinting at MCP integration in the App Intents framework — suggested Apple might let Siri and Apple Intelligence connect to any MCP server directly. **That didn't happen.** Per Apple's own [Platforms State of the Union](https://developer.apple.com/videos/play/wwdc2026/102/), MCP support landed in **Xcode 27** for developer tooling only — Siri and App Intents did not gain MCP client support. Basic app-access servers remain relevant, and specialized automation tools like Peekaboo, macos-automator-mcp, and HomeClaw retain their value either way. For Mac users, this remains one of the most practical MCP categories — you're controlling your actual desktop environment, apps, and smart home through AI, not just accessing remote APIs.

---

*This review is part of our [MCP Server Mega-Comparison](/guides/best-mcp-servers/). We research and analyze MCP servers — we do not test them hands-on. Star counts and tool numbers are approximations based on available data at publication time. Found an error or a server we missed? [Let us know](/about/).*

*Last updated August 14, 2026 using Claude Sonnet 5 (Anthropic).*
