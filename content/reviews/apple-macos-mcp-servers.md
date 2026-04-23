---
title: "Apple & macOS MCP Servers (2026) — 30+ Reviewed"
date: 2026-03-16T23:30:00+09:00
lastmod: 2026-04-24
description: "30+ Apple and macOS MCP servers reviewed — Siri Shortcuts, HomeKit, Apple Music, Notes, Reminders, AppleScript automation, and more. Peekaboo (3,200 stars) leads, supermemoryai/apple-mcp (3,100 stars, archived), iMCP (1,400 stars) covers 7 Apple services natively. Rating: 4/5."
og_description: "Apple & macOS MCP servers: Peekaboo (3,200 stars — screenshots + GUI automation), supermemoryai/apple-mcp (3,100 stars, archived Jan 2026), iMCP (1,400 stars — Messages, Calendar, Contacts, Maps, Weather), macos-automator-mcp (767 stars — 200+ AppleScript recipes). 30+ servers reviewed. Rating: 4/5."
content_type: "Review"
card_description: "30+ Apple and macOS MCP servers reviewed. Peekaboo (3,200 stars) provides screenshots and full GUI automation. supermemoryai/apple-mcp (3,100 stars, archived Jan 2026) covers Notes, Reminders, Calendar, Mail, Music, and Finder. iMCP (1,400 stars) is a native macOS app integrating Messages, Calendar, Contacts, Reminders, Maps, and Weather. macos-automator-mcp (767 stars) ships 200+ AppleScript recipes. Plus Siri Shortcuts, HomeKit, Apple Music, Safari, and Raycast. macOS Tahoe 26.1 beta hints at native Apple MCP support via App Intents."
last_refreshed: 2026-04-24
---

Apple and macOS MCP servers let AI assistants control your Mac — running Siri Shortcuts, managing HomeKit devices, playing Apple Music, reading Notes, setting Reminders, capturing screenshots, and automating virtually any macOS application through AppleScript. Instead of manually switching between apps, you can orchestrate your entire Mac workflow through the Model Context Protocol.

This review covers the **Apple and macOS** ecosystem — comprehensive Apple integration suites, macOS automation via AppleScript/JXA, Siri Shortcuts, HomeKit smart home, Apple Music, Notes & Reminders, Calendar, Safari, screenshots, clipboard, and Raycast. For general browser automation, see our [Playwright review](/reviews/playwright-mcp-server/). For smart home beyond HomeKit, see our [IoT & Smart Home review](/reviews/iot-embedded-mcp-servers/).

The headline findings: **Peekaboo ([3,200 stars](https://github.com/steipete/Peekaboo)) has evolved from a screenshot tool into a [full GUI automation platform](https://www.peekaboo.boo/)** — now the most-starred Apple MCP server. **supermemoryai/apple-mcp ([3,100 stars](https://github.com/supermemoryai/apple-mcp)) covers 8+ Apple apps** in one package — though it was [archived in January 2026](https://glama.ai/mcp/servers/supermemoryai/apple-mcp). **iMCP ([1,400 stars](https://github.com/mattt/iMCP)) is a native macOS app** providing MCP access to Messages, Contacts, Calendar, Reminders, Maps, Weather, and Location — a strong actively-maintained alternative. **macos-automator-mcp ([767 stars](https://github.com/steipete/macos-automator-mcp)) ships 200+ automation recipes**. **Siri Shortcuts provide a bridge to the entire Apple/iOS ecosystem**. **HomeKit has 3+ MCP implementations** — HomeClaw ([96 stars](https://github.com/omarshahine/HomeClaw)) reached v1.0.0 with characteristic-based automation triggers. **Apple Music has 4+ independent servers**. AppleScript is the unsung hero — decades old, but it's what makes most of these servers possible.

**Industry context:** macOS Tahoe 26.1 developer beta [revealed early signs of native MCP integration](https://mcp.directory/blog/apple-prepares-revolution-mcp-integration-in-macos-ios-ipados) through the App Intents framework — potentially allowing Siri, Shortcuts, and Spotlight to act as MCP clients. First public APIs are possible by WWDC 2026, with mass adoption no earlier than iOS 27/macOS 28. If realized, this would make many third-party MCP servers redundant for basic Apple app access.

**Category:** [Developer Tools](/categories/developer-tools/)

---

## Comprehensive Apple Integration

### supermemoryai/apple-mcp (Most Popular — Archived)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [apple-mcp](https://github.com/supermemoryai/apple-mcp) | 3,100 | TypeScript | — | 20+ |

> **⚠️ Archived:** This repository was [archived on January 1, 2026](https://glama.ai/mcp/servers/supermemoryai/apple-mcp) and is now read-only. It still works if installed, but receives no updates or bug fixes. An [enhanced fork by Ayaanisthebest](https://skywork.ai/skypage/en/mac-superpowers-apple-ecosystem/1981262794550333440) adds smart features, rich text support, and improved error handling.

The **most starred Apple MCP server** — a comprehensive [collection of apple-native tools](https://playbooks.com/mcp/supermemoryai/apple-mcp) covering multiple apps:

- **Notes** — create, read, search, and manage notes and folders
- **Reminders** — full CRUD for reminders and lists
- **Calendar** — event creation, retrieval, and management
- **Contacts** — search and retrieve contact information
- **Mail** — read and compose emails
- **Messages** — send and read iMessages
- **Music** — control Apple Music playback
- **Finder** — file and folder operations

Features an **explicit access request system** — all modules request permissions before attempting operations, with clear error messages and step-by-step instructions for granting access in System Settings. Enables complex multi-app workflows like ["Read my conference notes, find contacts for the people I met, and send them a thank you message."](https://skywork.ai/skypage/en/mac-superpowers-apple-ecosystem/1981262794550333440) Available through [Smithery](https://glama.ai/mcp/servers/supermemoryai/apple-mcp) with one-click setup via `.dxt` file or manual configuration with Bun/TypeScript.

### mattt/iMCP (Best Active Alternative)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [iMCP](https://github.com/mattt/iMCP) | 1,400 | Swift | — | ~7 |

A **native macOS application** that provides an MCP server for personal digital services — the strongest actively-maintained alternative to the archived supermemoryai/apple-mcp. Created by [Mattt Thompson](https://github.com/mattt) (creator of AFNetworking/Alamofire, former Apple developer). v1.4.0 released January 2026:

- **Calendar** — view and manage events with recurrence and alarms
- **Contacts** — search and access contact information
- **Messages** — access iMessage history with date ranges (via custom `typedstream` decoder since Apple provides no public API)
- **Reminders** — create and view with priorities and alerts
- **Maps** — place search, directions, and travel time estimation
- **Weather** — current conditions for any location
- **Location** — current position and coordinate conversion

Uses the **App Sandbox security model** and **Bonjour** for local network discovery between the bundled CLI and the UI app. Unlike AppleScript-based servers, iMCP uses native macOS frameworks directly — Contacts.framework, EventKit, MapKit — providing more reliable integration. The 1,400 stars and active maintenance make this the recommended choice for users who need multi-app Apple integration without relying on archived projects.

## macOS Automation

### steipete/macos-automator-mcp (Best Automation)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [macos-automator-mcp](https://github.com/steipete/macos-automator-mcp) | 767 | TypeScript | — | 200+ recipes |

Created by [Peter Steinberger](https://steipete.me/) (ex-founder of PSPDFKit) — transforms your AI assistant into a [macOS automation powerhouse](https://www.pulsemcp.com/servers/steipete-macos-automator):

- **200+ pre-built automation recipes** — toggle dark mode, extract URLs from Safari, manage windows, control system settings
- **AppleScript and JXA execution** — run both scripting languages through MCP
- **Knowledge base** — lazy or eager loading, customizable via `~/.macos-automator/knowledge_base`
- **Custom skills** — add your own automation recipes
- **Accessibility API querying** — [inspect and interact with UI elements](https://skywork.ai/skypage/en/macos-ai-automator-unlocking/1981180204707401728) across applications
- **Published on npm** — `@steipete/macos-automator-mcp`

The knowledge base approach is clever — rather than hardcoding capabilities, it ships a library of recipes that the AI can browse and execute contextually. Unlike GUI/accessibility-based approaches, it ["calls the application's internal API"](https://skywork.ai/skypage/en/macos-ai-automator-unlocking/1981180204707401728) for surgical precision — it doesn't fail because a UI element moved.

### joshrutkowski/applescript-mcp (General AppleScript)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [applescript-mcp](https://github.com/joshrutkowski/applescript-mcp) | 379 | TypeScript | — | ~10 |

A [standardized interface for AI applications](https://www.pulsemcp.com/servers/joshrutkowski-applescript) to control macOS through AppleScript — created by [Josh Rutkowski, a Software Development Engineer at Amazon](https://skywork.ai/skypage/en/macos-ai-applescript/1980507376320815104):

- **System functions** — volume, brightness, dark mode, notifications
- **File management** — Finder operations, file search, Quick Look
- **Application control** — launch, quit, interact with apps
- **Calendar & Reminders** — event creation and management
- **Communication** — Mail composition, Messages sending, contact searching
- **iTerm integration** — terminal command execution from AI

Occupies the ["batteries-included" sweet spot](https://skywork.ai/skypage/en/macos-ai-applescript/1980507376320815104) — more convenience than raw AppleScript execution tools, while remaining accessible for non-experts.

### peakmojo/applescript-mcp (Simple Execution)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [applescript-mcp](https://github.com/peakmojo/applescript-mcp) | — | — | — | ~3 |

Minimal setup — run any AppleScript code through MCP. Simple and straightforward for users who know AppleScript and just want execution capability.

## Siri Shortcuts

### dvcrn/mcp-server-siri-shortcuts (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-siri-shortcuts](https://github.com/dvcrn/mcp-server-siri-shortcuts) | 184 | TypeScript | GPL-3.0 | ~3 |

[Access Siri Shortcuts functionality](https://www.pulsemcp.com/servers/dvcrn-mcp-server-siri-shortcuts) from the macOS Shortcuts app:

- **List shortcuts** — discover available automations
- **Open shortcuts** — view in the Shortcuts app
- **Run shortcuts** — execute directly from AI with optional input parameters
- **Auto-generated tools** — automatically creates tools for each available shortcut

Uses the macOS `shortcuts` CLI command under the hood. Since Shortcuts can control HomeKit, trigger automations, interact with hundreds of apps, and bridge to iOS — this effectively gives MCP access to the **entire Apple Shortcuts ecosystem**.

### recursechat/mcp-server-apple-shortcuts

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts) | — | — | — | ~3 |

Designed for safe, controlled Shortcuts execution — lets AI models trigger shortcuts while maintaining security boundaries.

### CaseyRo/mac_shortcuts_mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mac_shortcuts_mcp](https://github.com/CaseyRo/mac_shortcuts_mcp) | — | Python | — | ~3 |

Python-based alternative for running macOS Shortcuts from MCP-compatible clients.

## HomeKit / Smart Home

### somethingwithproof/home-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [home-mcp](https://github.com/somethingwithproof/home-mcp) | — | — | — | ~5 |

Controls HomeKit devices, scenes, and automations via Apple Home on macOS:

- **Device control** — lights, switches, sensors
- **Scene activation** — trigger predefined HomeKit scenes
- **Automation management** — view and control automations

Works best when combined with Shortcuts that control your HomeKit devices, since Apple Home has limited AppleScript support.

### jaebinsim/IntentCP (Zero Infrastructure)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [IntentCP](https://github.com/jaebinsim/HomeMCP) | 20 | Python | — | ~5 |

Formerly HomeMCP, now rebranded as **IntentCP** — a lightweight, intent-driven control plane for smart home automation. Uses iOS Shortcuts and cloud IoT platforms (Tuya) without requiring local LLM hosting. Trigger with "Hey Siri" + a Shortcut, converting spoken intent into safe execution URLs.

### omarshahine/HomeClaw (Native App)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [HomeClaw](https://github.com/omarshahine/HomeClaw) | 96 | Swift | — | ~10 |

A unified **Mac Catalyst app** providing HomeKit smart home control via MCP — bridges HomeKit (which [lacks a public API](https://github.com/omarshahine/HomeClaw)) through a lightweight menu bar application. Reached **v1.0.0** (March 2026) as the first stable release:

- **Lights** — on/off, brightness, color
- **Locks** — lock/unlock
- **Thermostats** — temperature control
- **Scenes** — create, import, trigger, and delete scenes
- **Window coverings, fans, sensors** — broad device category support
- **Event logging** — query HomeKit activity history with filtering
- **Webhook integration** — external automation pipelines
- **Characteristic-based automation triggers** — motion sensors, contact sensors, occupancy detectors, and temperature thresholds (build 136, April 2026)
- **OpenClaw compatibility** — declared compatibility metadata for ClawHub integration

Compatible with Claude Desktop, Claude Code, and OpenClaw. Fixed TCC crash on macOS 26.4. Zero open issues.

## Apple Music

### kennethreitz/mcp-applemusic (Most Known)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-applemusic](https://github.com/kennethreitz/mcp-applemusic) | 84 | Python | MIT | ~8 |

[Experimental FastMCP server](https://www.pulsemcp.com/servers/kennethreitz-applemusic) from Kenneth Reitz (creator of `requests`) — controls Apple Music via AppleScript. Requires [Python 3.13+ and macOS](https://skywork.ai/skypage/en/apple-music-mcp-server-guide/1977608435765022720):

- **Playback** — play, pause, next, previous
- **Search** — find songs in your library
- **Playlists** — create playlists with specific songs
- **Library** — browse your music collection and get statistics

A local-first solution — [your music data and listening habits never leave your computer](https://skywork.ai/skypage/en/apple-music-mcp-server-guide/1977608435765022720). Installable via `uvx -p 3.13 -n mcp-applemusic`.

### epheterson/mcp-applemusic (REST API)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-applemusic](https://github.com/epheterson/mcp-applemusic) | — | — | — | ~5 |

Uses the **official Apple Music REST API** rather than AppleScript — manages playlists and library access. Better for programmatic playlist management.

### samwang0723/mcp-applemusic (TypeScript)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-applemusic](https://github.com/samwang0723/mcp-applemusic) | — | TypeScript | — | ~6 |

TypeScript implementation using Express.js — controls Apple Music via AppleScript commands (osascript).

### pedrocid/music-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [music-mcp](https://github.com/pedrocid/music-mcp) | — | — | — | ~5 |

Another AppleScript-based Apple Music controller via MCP.

## Notes & Reminders

### karlhepler/apple-mcp (Notes + Reminders — Removed)

> **⚠️ Removed:** This repository is no longer available on GitHub (404). If you need Notes and Reminders via MCP, consider supermemoryai/apple-mcp (archived but functional) or the dedicated Reminders server below.

### mggrim/apple-reminders-mcp-server (Most Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [apple-reminders-mcp-server](https://github.com/mggrim/apple-reminders-mcp-server) | — | — | — | 18 |

The **most feature-rich Reminders-only server** with 18 comprehensive tools:

- **Full CRUD** for reminders and lists
- **Natural language date parsing** — "next Tuesday at 3pm"
- **Priority and due date management**

### FradSer/mcp-server-apple-events (EventKit)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-apple-events](https://github.com/FradSer/mcp-server-apple-events) | — | Swift | — | ~8 |

Uses **native EventKit** framework for Reminders and Calendar integration — bypasses AppleScript entirely for a more reliable macOS-native approach.

## iCloud & Calendar

### iteratio/icloud-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [icloud-mcp](https://github.com/iteratio/icloud-mcp) | — | — | — | ~6 |

Local MCP server for **iCloud Calendar, Mail, and Reminders** with credentials securely stored in the macOS Keychain. Works with iCloud accounts rather than requiring direct app access.

## Screenshots & Screen Control

### steipete/Peekaboo (Best Screenshots + GUI Automation)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Peekaboo](https://github.com/steipete/Peekaboo) | 3,200 | TypeScript/Swift | — | 10+ |

The **most-starred Apple MCP server** — now far more than just screenshots. [Peter Steinberger describes it](https://steipete.me/posts/2025/peekaboo-mcp-lightning-fast-macos-screenshots-for-ai-agents) as giving AI agents "eyes" on your Mac. Version 3 evolved into a [full macOS automation driver](https://www.peekaboo.boo/) — "Think Playwright but for the OS":

- **Screenshot capture** — pixel-accurate window and screen captures via Apple's ScreenCaptureKit, with optional Retina 2x scaling
- **Visual Question Answering** — analyze screenshots using [GPT-5.1, Claude 4.x, Grok 4, Gemini 2.5, or local Ollama models](https://www.pulsemcp.com/servers/steipete-peekaboo)
- **GUI automation** — click, type, scroll, hotkey, menu interaction, window management
- **App and dock control** — launch, focus, and manage applications
- **Natural-language agent** — chains Peekaboo tools (see, click, type, scroll, hotkey, menu, window, app, dock, space)

Built with TypeScript + Swift — TypeScript for MCP/npm distribution, Swift for [direct ScreenCaptureKit access](https://steipete.me/posts/2025/peekaboo-mcp-lightning-fast-macos-screenshots-for-ai-agents) without requiring focus changes. Part of Steinberger's growing ecosystem alongside macos-automator-mcp. Estimated [11,300+ users](https://www.pulsemcp.com/servers/steipete-peekaboo). Recent development (March 2026): updated MCP runtime for swift-sdk 0.12, improved ScreenCaptureKit window capture on macOS 15. Currently on v3.0.0-beta4 with 17 open issues. Requires macOS 15+.

### jhead/macos-screen-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [macos-screen-mcp](https://github.com/jhead/macos-screen-mcp) | — | — | — | ~4 |

Screenshot and **window control** for macOS — captures screens and manages window positioning. Built for Cursor but works with any MCP client.

## Safari & Browsing

### lxman/safari-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [safari-mcp-server](https://github.com/lxman/safari-mcp-server) | — | Node.js | — | ~5 |

AI-controlled Safari browsing — a Mac-native alternative to Playwright or Puppeteer. Uses Safari's built-in automation capabilities rather than requiring Chromium.

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
| [raycast-mcp-server](https://github.com/ExpertVagabond/raycast-mcp-server) | — | — | — | 9 |

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

**Rating: 4/5** — Apple and macOS MCP is surprisingly mature, now led by Peekaboo ([3,200 stars](https://github.com/steipete/Peekaboo), actively developed) and supermemoryai/apple-mcp ([3,100 stars](https://github.com/supermemoryai/apple-mcp), [archived since January 2026](https://glama.ai/mcp/servers/supermemoryai/apple-mcp)). The addition of **iMCP ([1,400 stars](https://github.com/mattt/iMCP))** fills the gap left by apple-mcp's archival — it covers 7 Apple services through native frameworks rather than AppleScript. [macos-automator-mcp (767 stars)](https://github.com/steipete/macos-automator-mcp) provides 200+ automation recipes.

The key insight: **AppleScript, despite being decades old, is the [perfect bridge](https://skywork.ai/skypage/en/macos-ai-automator-unlocking/1981180204707401728) between MCP and macOS applications.** Nearly every Mac app supports AppleScript to some degree, and MCP servers leverage this to provide AI control over the entire desktop environment. Siri Shortcuts extend this further, bridging into iOS and HomeKit. Meanwhile, iMCP demonstrates a newer approach — using native macOS frameworks (EventKit, Contacts.framework, MapKit) directly, bypassing AppleScript entirely.

HomeKit gets three independent implementations (HomeClaw at [96 stars](https://github.com/omarshahine/HomeClaw) leads — now at v1.0.0 with characteristic-based automation triggers for motion sensors and temperature thresholds). Apple Music has four (kennethreitz at [84 stars](https://github.com/kennethreitz/mcp-applemusic) leads). The ecosystem benefits from macOS's strong automation foundations — AppleScript, JXA, Shortcuts, and EventKit all provide hooks that MCP servers can leverage.

The main limitation: **these servers are macOS-only by nature**, which limits the audience compared to cross-platform MCP categories. But Apple may be about to change the game entirely — [macOS Tahoe 26.1 beta code](https://mcp.directory/blog/apple-prepares-revolution-mcp-integration-in-macos-ios-ipados) reveals early MCP integration through the App Intents framework, with possible public APIs by WWDC 2026. If Apple ships native MCP support, basic app access servers would become redundant — but specialized automation tools like Peekaboo, macos-automator-mcp, and HomeClaw would retain their value. For Mac users, this remains one of the most practical MCP categories — you're controlling your actual desktop environment, apps, and smart home through AI, not just accessing remote APIs.

---

*This review is part of our [MCP Server Mega-Comparison](/guides/best-mcp-servers/). We research and analyze MCP servers — we do not test them hands-on. Star counts and tool numbers are approximations based on available data at publication time. Found an error or a server we missed? [Let us know](/about/).*

*Last updated April 24, 2026 using Claude Opus 4.6 (Anthropic).*
