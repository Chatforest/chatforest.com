---
title: "Apple & macOS MCP Servers (2026) — 30+ Reviewed"
date: 2026-03-16T23:30:00+09:00
description: "30+ Apple and macOS MCP servers reviewed — Siri Shortcuts, HomeKit, Apple Music, Notes, Reminders, AppleScript automation, and more. supermemoryai/apple-mcp (3,000 stars) leads the pack. Rating: 4/5."
og_description: "Apple & macOS MCP servers: supermemoryai/apple-mcp (3,000 stars — Notes/Reminders/Calendar/Mail/Music/Finder), macos-automator-mcp (709 stars — 200+ AppleScript recipes), Siri Shortcuts, HomeKit, Apple Music, Peekaboo screenshots. 30+ servers reviewed. Rating: 4/5."
content_type: "Review"
card_description: "30+ Apple and macOS MCP servers reviewed. supermemoryai/apple-mcp (3,000 stars) covers Notes, Reminders, Calendar, Mail, Music, and Finder. macos-automator-mcp (709 stars) ships 200+ AppleScript recipes. Plus Siri Shortcuts, HomeKit, Apple Music, Safari, screenshots, and Raycast integration."
last_refreshed: 2026-03-16
---

Apple and macOS MCP servers let AI assistants control your Mac — running Siri Shortcuts, managing HomeKit devices, playing Apple Music, reading Notes, setting Reminders, capturing screenshots, and automating virtually any macOS application through AppleScript. Instead of manually switching between apps, you can orchestrate your entire Mac workflow through the Model Context Protocol.

This review covers the **Apple and macOS** ecosystem — comprehensive Apple integration suites, macOS automation via AppleScript/JXA, Siri Shortcuts, HomeKit smart home, Apple Music, Notes & Reminders, Calendar, Safari, screenshots, clipboard, and Raycast. For general browser automation, see our [Playwright review](/reviews/playwright-mcp-server/). For smart home beyond HomeKit, see our [IoT & Smart Home review](/reviews/iot-embedded-mcp-servers/).

The headline findings: **supermemoryai/apple-mcp (3,000 stars) covers 8+ Apple apps** in one package. **macos-automator-mcp (709 stars) ships 200+ automation recipes**. **Siri Shortcuts provide a bridge to the entire Apple/iOS ecosystem**. **HomeKit has 3+ MCP implementations**. **Apple Music has 4+ independent servers**. AppleScript is the unsung hero — decades old, but it's what makes most of these servers possible.

**Category:** [Developer Tools](/categories/developer-tools/)

---

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

*This review is part of our [MCP Server Mega-Comparison](/guides/best-mcp-servers/). We research and analyze MCP servers — we do not test them hands-on. Star counts and tool numbers are approximations based on available data at publication time. Found an error or a server we missed? [Let us know](/about/).*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
