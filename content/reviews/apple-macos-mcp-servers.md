---
title: "Apple & macOS MCP Servers — Siri Shortcuts, HomeKit, Apple Music, Notes, Reminders, AppleScript Automation, and More"
date: 2026-03-16T23:30:00+09:00
description: "Apple and macOS MCP servers are turning Macs into AI-controlled workstations — from Siri Shortcuts and HomeKit control to Apple Music playback and AppleScript automation via the Model Context Protocol. We reviewed 30+ servers across 7 subcategories. Comprehensive: supermemoryai/apple-mcp (3,000 stars, TypeScript — Notes, Reminders, Calendar, Contacts, Mail, Messages, Music, Finder with explicit permission requests). macOS Automation: steipete/macos-automator-mcp (709 stars — 200+ AppleScript/JXA recipes, knowledge base, custom skills), joshrutkowski/applescript-mcp (system functions, file management, notifications), peakmojo/applescript-mcp (simple AppleScript execution). Siri Shortcuts: dvcrn/mcp-server-siri-shortcuts (list/open/run Shortcuts), recursechat/mcp-server-apple-shortcuts (safe AI-triggered automation), CaseyRo/mac_shortcuts_mcp (Python-based). HomeKit / Smart Home: somethingwithproof/home-mcp (devices/scenes/automations via Apple Home), jaebinsim/HomeMCP (zero-infrastructure, iOS Shortcuts bridge), omarshahine/HomeClaw (Catalyst app — lights/locks/thermostats/scenes). Apple Music: kennethreitz/mcp-applemusic (play/pause/search/playlists via AppleScript), samwang0723/mcp-applemusic (TypeScript, Express.js), epheterson/mcp-applemusic (REST API, playlist management), pedrocid/music-mcp. Notes & Reminders: karlhepler/apple-mcp (CRUD for Notes + Reminders, folder/list management), mggrim/apple-reminders-mcp-server (18 tools, natural language dates), shadowfax92/apple-reminders-mcp, dbmcco/apple-reminders-mcp. Calendar & Events: FradSer/mcp-server-apple-events (EventKit — Reminders + Calendar), iteratio/icloud-mcp (iCloud Calendar/Mail/Reminders, Keychain credentials). Screenshots & Screen: steipete/Peekaboo (app/system screenshots with optional VQA), jhead/macos-screen-mcp (screenshot + window control). Safari: lxman/safari-mcp-server (AI-controlled Safari browsing). Clipboard: vlad-ds/maccy-clipboard-mcp (Maccy history, text + images). Raycast: ExpertVagabond/raycast-mcp-server (9 tools for Raycast workflow automation). Gaps: no Xcode integration, no macOS system preferences/settings control, no Time Machine backup management, no AirDrop, no Keychain password management MCP, no macOS Automator workflow import. 30+ servers across 7 subcategories. Rating: 4/5."
og_description: "Apple & macOS MCP servers: supermemoryai/apple-mcp (3,000 stars — Notes/Reminders/Calendar/Mail/Music/Finder), macos-automator-mcp (709 stars — 200+ AppleScript recipes), Siri Shortcuts, HomeKit, Apple Music, Peekaboo screenshots. 30+ servers reviewed. Rating: 4/5."
content_type: "Review"
card_description: "Apple and macOS MCP servers for AI-powered Mac automation, Siri Shortcuts, HomeKit smart home control, Apple Music, Notes, Reminders, and more. **supermemoryai/apple-mcp is the standout** — 3,000 stars and growing, it's a comprehensive collection of apple-native tools covering Notes, Reminders, Calendar, Contacts, Mail, Messages, Music, and Finder through the Model Context Protocol. It features explicit access permission requests with clear error messages and step-by-step instructions for granting macOS permissions. Complex multi-app workflows are possible — 'Read my conference notes, find contacts for the people I met, and send them a thank you message.' **macOS automation gets a massive knowledge base** — steipete/macos-automator-mcp (709 stars) transforms your AI assistant into a macOS power user with 200+ pre-built AppleScript and JXA (JavaScript for Automation) recipes. From toggling dark mode to extracting URLs from Safari, the knowledge base can be loaded lazily or eagerly at startup. Custom automation recipes can be added. Published on npm as @steipete/macos-automator-mcp. Created by Peter Steinberger, well-known in the Apple developer community. **Siri Shortcuts bridge the MCP-iOS gap** — dvcrn/mcp-server-siri-shortcuts lets AI assistants list, open, and run macOS Shortcuts directly. recursechat/mcp-server-apple-shortcuts provides safe, controlled Shortcuts execution for AI models. CaseyRo/mac_shortcuts_mcp offers a Python-based alternative. Since Shortcuts can control HomeKit, trigger automations, and interact with hundreds of apps, this effectively gives MCP access to the entire Apple Shortcuts ecosystem. **HomeKit gets multiple MCP implementations** — somethingwithproof/home-mcp controls HomeKit devices, scenes, and automations via Apple Home on macOS. jaebinsim/HomeMCP takes a zero-infrastructure approach using iOS Shortcuts and Apple Intelligence — no local LLM or GPU required. omarshahine/HomeClaw is a unified Catalyst app providing HomeKit control for lights, locks, thermostats, and scenes via MCP, compatible with Claude Desktop, Claude Code, and OpenClaw. **Apple Music has 4+ MCP server implementations** — kennethreitz/mcp-applemusic (experimental, AppleScript-based — play, pause, search, create playlists, browse library) is the most well-known. samwang0723/mcp-applemusic provides TypeScript implementation with Express.js. epheterson/mcp-applemusic manages playlists via the official Apple Music REST API. pedrocid/music-mcp offers another AppleScript-based control option. **Notes and Reminders have dedicated servers** — karlhepler/apple-mcp provides full CRUD operations for both Apple Notes and Reminders with folder/list management, search, and robust error handling (TypeScript + AppleScript). mggrim/apple-reminders-mcp-server is the most feature-rich Reminders server with 18 tools and natural language date parsing. Multiple other Reminders implementations exist from shadowfax92 and dbmcco. FradSer/mcp-server-apple-events provides native EventKit integration covering both Reminders and Calendar. **iCloud integration exists** — iteratio/icloud-mcp provides a local MCP server for iCloud Calendar, Mail, and Reminders with credentials securely stored in the macOS Keychain. **Screenshots and screen control are well-served** — steipete/Peekaboo captures application or system screenshots with optional visual question answering (VQA) through local or remote AI models — excellent for agentic workflows that need to 'see' the screen. jhead/macos-screen-mcp provides screenshot and window control capabilities. **Safari has its own MCP server** — lxman/safari-mcp-server enables AI-controlled Safari browsing, complementing the more common Playwright/Puppeteer-based browser automation. **Clipboard integration exists** — vlad-ds/maccy-clipboard-mcp connects to Maccy clipboard history with search, retrieval, and management for both text and images. **Raycast gets MCP integration** — ExpertVagabond/raycast-mcp-server provides 9 tools for AI-native macOS workflow automation through the popular Raycast launcher. **Major gaps remain** — no Xcode project management or build automation via MCP. No macOS System Settings/Preferences control. No Time Machine backup management. No AirDrop file transfer. No Keychain password retrieval (understandably — security concerns). No macOS Automator workflow import/conversion. No Focus/Do Not Disturb mode control. No disk utility or storage management. No accessibility feature control. No Terminal.app integration beyond standard shell MCP servers. The category earns 4/5 — Apple and macOS MCP is surprisingly mature thanks to the massive supermemoryai/apple-mcp project (3,000 stars) serving as a comprehensive hub and steipete/macos-automator-mcp (709 stars) providing deep automation knowledge. The key insight is that AppleScript, despite being decades old, acts as a powerful bridge between MCP and virtually every macOS application. Siri Shortcuts extend this further into iOS territory. HomeKit gets multiple implementations. Apple Music has 4+ servers. The ecosystem benefits from macOS's strong automation foundations — AppleScript, JXA, Shortcuts, and Automator all provide hooks that MCP servers can leverage. The main weakness is that these servers are macOS-only by nature, limiting the audience. But for Mac users, this is one of the most practical MCP categories — controlling your actual desktop environment, apps, and smart home through AI."
last_refreshed: 2026-03-16
---

Apple and macOS MCP servers let AI assistants control your Mac — running Siri Shortcuts, managing HomeKit devices, playing Apple Music, reading Notes, setting Reminders, capturing screenshots, and automating virtually any macOS application through AppleScript. Instead of manually switching between apps, you can orchestrate your entire Mac workflow through the Model Context Protocol.

This review covers the **Apple and macOS** ecosystem — comprehensive Apple integration suites, macOS automation via AppleScript/JXA, Siri Shortcuts, HomeKit smart home, Apple Music, Notes & Reminders, Calendar, Safari, screenshots, clipboard, and Raycast. For general browser automation, see our [Playwright review](/reviews/playwright-mcp-server/). For smart home beyond HomeKit, see our [IoT & Smart Home review](/reviews/iot-embedded-mcp-servers/).

The headline findings: **supermemoryai/apple-mcp (3,000 stars) covers 8+ Apple apps** in one package. **macos-automator-mcp (709 stars) ships 200+ automation recipes**. **Siri Shortcuts provide a bridge to the entire Apple/iOS ecosystem**. **HomeKit has 3+ MCP implementations**. **Apple Music has 4+ independent servers**. AppleScript is the unsung hero — decades old, but it's what makes most of these servers possible.

## Comprehensive Apple Integration

### supermemoryai/apple-mcp (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [apple-mcp](https://github.com/supermemoryai/apple-mcp) | 3,000 | TypeScript | — | 20+ |

The **most starred Apple MCP server by far** — a comprehensive collection of apple-native tools covering multiple apps:

- **Notes** — create, read, search, and manage notes and folders
- **Reminders** — full CRUD for reminders and lists
- **Calendar** — event creation, retrieval, and management
- **Contacts** — search and retrieve contact information
- **Mail** — read and compose emails
- **Messages** — send and read iMessages
- **Music** — control Apple Music playback
- **Finder** — file and folder operations

Features an **explicit access request system** — all modules request permissions before attempting operations, with clear error messages and step-by-step instructions for granting access in System Settings. Enables complex multi-app workflows like "Read my conference notes, find contacts for the people I met, and send them a thank you message."

## macOS Automation

### steipete/macos-automator-mcp (Best Automation)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [macos-automator-mcp](https://github.com/steipete/macos-automator-mcp) | 709 | TypeScript | — | 200+ recipes |

Created by Peter Steinberger (well-known Apple developer) — transforms your AI assistant into a macOS automation powerhouse:

- **200+ pre-built automation recipes** — toggle dark mode, extract URLs from Safari, manage windows, control system settings
- **AppleScript and JXA execution** — run both scripting languages through MCP
- **Knowledge base** — lazy or eager loading, customizable via `~/.macos-automator/knowledge_base`
- **Custom skills** — add your own automation recipes
- **Published on npm** — `@steipete/macos-automator-mcp`

The knowledge base approach is clever — rather than hardcoding capabilities, it ships a library of recipes that the AI can browse and execute contextually.

### joshrutkowski/applescript-mcp (General AppleScript)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [applescript-mcp](https://github.com/joshrutkowski/applescript-mcp) | — | TypeScript | — | ~10 |

A standardized interface for AI applications to control macOS through AppleScript:

- **System functions** — volume, brightness, notifications
- **File management** — Finder operations
- **Application control** — launch, quit, interact with apps

Good for general-purpose macOS scripting without the recipe-based approach.

### peakmojo/applescript-mcp (Simple Execution)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [applescript-mcp](https://github.com/peakmojo/applescript-mcp) | — | — | — | ~3 |

Minimal setup — run any AppleScript code through MCP. Simple and straightforward for users who know AppleScript and just want execution capability.

## Siri Shortcuts

### dvcrn/mcp-server-siri-shortcuts (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-siri-shortcuts](https://github.com/dvcrn/mcp-server-siri-shortcuts) | — | TypeScript | — | ~3 |

Access Siri Shortcuts functionality from the macOS Shortcuts app:

- **List shortcuts** — discover available automations
- **Open shortcuts** — view in the Shortcuts app
- **Run shortcuts** — execute directly from AI

Since Shortcuts can control HomeKit, trigger automations, interact with hundreds of apps, and bridge to iOS — this effectively gives MCP access to the **entire Apple Shortcuts ecosystem**.

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

### jaebinsim/HomeMCP (Zero Infrastructure)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [HomeMCP](https://github.com/jaebinsim/HomeMCP) | — | — | — | ~5 |

**Zero-infrastructure smart home orchestrator** — uses iOS Shortcuts and Apple Intelligence. No local LLM or GPU required. A creative approach that bridges the MCP world to HomeKit through Shortcuts as the intermediary.

### omarshahine/HomeClaw (Native App)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [HomeClaw](https://github.com/omarshahine/HomeClaw) | — | Swift | — | ~10 |

A unified **Catalyst app** providing HomeKit smart home control via MCP:

- **Lights** — on/off, brightness, color
- **Locks** — lock/unlock
- **Thermostats** — temperature control
- **Scenes** — activate HomeKit scenes

Compatible with Claude Desktop, Claude Code, and OpenClaw.

## Apple Music

### kennethreitz/mcp-applemusic (Most Known)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-applemusic](https://github.com/kennethreitz/mcp-applemusic) | — | Python | — | ~8 |

Experimental FastMCP server from Kenneth Reitz (creator of `requests`) — controls Apple Music via AppleScript:

- **Playback** — play, pause, next, previous
- **Search** — find songs in your library
- **Playlists** — create playlists with specific songs
- **Library** — browse your music collection

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

### karlhepler/apple-mcp (Notes + Reminders)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [apple-mcp](https://github.com/karlhepler/apple-mcp) | — | TypeScript | — | ~12 |

Focused server for **Apple Notes and Reminders** with full CRUD:

- **Notes** — create, read, update, delete, search across folders
- **Reminders** — create, complete, delete, list management
- **Folder/list management** — organize notes and reminders
- **Search** — find content across all notes

Built with TypeScript and AppleScript. Good alternative to supermemoryai/apple-mcp if you only need Notes and Reminders.

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

### steipete/Peekaboo (Best Screenshots)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Peekaboo](https://github.com/steipete/Peekaboo) | — | Swift | — | ~5 |

A macOS CLI and optional MCP server for **AI-powered screen capture**:

- **Application screenshots** — capture specific app windows
- **System screenshots** — capture the entire screen
- **Visual Question Answering (VQA)** — ask questions about captured screenshots using local or remote AI models

Excellent for agentic workflows where the AI needs to "see" what's on screen.

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
| [maccy-clipboard-mcp](https://github.com/vlad-ds/maccy-clipboard-mcp) | — | — | — | ~5 |

Connects to **Maccy clipboard history** on macOS:

- **Search** clipboard entries by content
- **Retrieve** recent clipboard items
- **Support for text and images**

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

**Rating: 4/5** — Apple and macOS MCP is surprisingly mature, anchored by supermemoryai/apple-mcp (3,000 stars) covering 8+ apps in one package and steipete/macos-automator-mcp (709 stars) providing 200+ automation recipes.

The key insight: **AppleScript, despite being decades old, is the perfect bridge between MCP and macOS applications.** Nearly every Mac app supports AppleScript to some degree, and MCP servers leverage this to provide AI control over the entire desktop environment. Siri Shortcuts extend this further, bridging into iOS and HomeKit.

HomeKit gets three independent implementations. Apple Music has four. Notes and Reminders have multiple dedicated servers. The ecosystem benefits from macOS's strong automation foundations — AppleScript, JXA, Shortcuts, and EventKit all provide hooks that MCP servers can leverage.

The main limitation: **these servers are macOS-only by nature**, which limits the audience compared to cross-platform MCP categories. But for Mac users, this is one of the most practical MCP categories — you're controlling your actual desktop environment, apps, and smart home through AI, not just accessing remote APIs.

---

*This review is part of our [MCP Server Mega-Comparison](/guides/best-mcp-servers/). We research and analyze MCP servers — we do not test them hands-on. Star counts and tool numbers are approximations based on available data at publication time. Found an error or a server we missed? [Let us know](/contact/).*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
