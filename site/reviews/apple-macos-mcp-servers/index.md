# Apple & macOS MCP Servers (2026) — 30+ Reviewed

> 30+ Apple and macOS MCP servers reviewed — Siri Shortcuts, HomeKit, Apple Music, Notes, Reminders, AppleScript automation, and more. supermemoryai/apple-mcp (3,100 stars, archived) and Peekaboo (3,100 stars) lead. Rating: 4/5.


Apple and macOS MCP servers let AI assistants control your Mac — running Siri Shortcuts, managing HomeKit devices, playing Apple Music, reading Notes, setting Reminders, capturing screenshots, and automating virtually any macOS application through AppleScript. Instead of manually switching between apps, you can orchestrate your entire Mac workflow through the Model Context Protocol.

This review covers the **Apple and macOS** ecosystem — comprehensive Apple integration suites, macOS automation via AppleScript/JXA, Siri Shortcuts, HomeKit smart home, Apple Music, Notes & Reminders, Calendar, Safari, screenshots, clipboard, and Raycast. For general browser automation, see our [Playwright review](/reviews/playwright-mcp-server/). For smart home beyond HomeKit, see our [IoT & Smart Home review](/reviews/iot-embedded-mcp-servers/).

The headline findings: **supermemoryai/apple-mcp ([3,100 stars](https://github.com/supermemoryai/apple-mcp)) covers 8+ Apple apps** in one package — though it was [archived in January 2026](https://glama.ai/mcp/servers/supermemoryai/apple-mcp). **Peekaboo ([3,100 stars](https://github.com/steipete/Peekaboo)) has evolved from a screenshot tool into a [full GUI automation platform](https://www.peekaboo.boo/)**. **macos-automator-mcp ([758 stars](https://github.com/steipete/macos-automator-mcp)) ships 200+ automation recipes**. **Siri Shortcuts provide a bridge to the entire Apple/iOS ecosystem**. **HomeKit has 3+ MCP implementations**. **Apple Music has 4+ independent servers**. AppleScript is the unsung hero — decades old, but it's what makes most of these servers possible.

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

## macOS Automation

### steipete/macos-automator-mcp (Best Automation)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [macos-automator-mcp](https://github.com/steipete/macos-automator-mcp) | 758 | TypeScript | — | 200+ recipes |

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
| [applescript-mcp](https://github.com/joshrutkowski/applescript-mcp) | 376 | TypeScript | — | ~10 |

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
| [mcp-server-siri-shortcuts](https://github.com/dvcrn/mcp-server-siri-shortcuts) | 183 | TypeScript | GPL-3.0 | ~3 |

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
| [HomeClaw](https://github.com/omarshahine/HomeClaw) | 87 | Swift | — | ~10 |

A unified **Mac Catalyst app** providing HomeKit smart home control via MCP — bridges HomeKit (which [lacks a public API](https://github.com/omarshahine/HomeClaw)) through a lightweight menu bar application:

- **Lights** — on/off, brightness, color
- **Locks** — lock/unlock
- **Thermostats** — temperature control
- **Scenes** — create, import, trigger, and delete scenes
- **Window coverings, fans, sensors** — broad device category support
- **Event logging** — query HomeKit activity history with filtering
- **Webhook integration** — external automation pipelines

Compatible with Claude Desktop, Claude Code, and OpenClaw.

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
| [Peekaboo](https://github.com/steipete/Peekaboo) | 3,100 | TypeScript/Swift | — | 10+ |

The **second-most-starred Apple MCP server** — now far more than just screenshots. [Peter Steinberger describes it](https://steipete.me/posts/2025/peekaboo-mcp-lightning-fast-macos-screenshots-for-ai-agents) as giving AI agents "eyes" on your Mac. Version 3 evolved into a [full macOS automation driver](https://www.peekaboo.boo/) — "Think Playwright but for the OS":

- **Screenshot capture** — pixel-accurate window and screen captures via Apple's ScreenCaptureKit, with optional Retina 2x scaling
- **Visual Question Answering** — analyze screenshots using [GPT-5.1, Claude 4.x, Grok 4, Gemini 2.5, or local Ollama models](https://www.pulsemcp.com/servers/steipete-peekaboo)
- **GUI automation** — click, type, scroll, hotkey, menu interaction, window management
- **App and dock control** — launch, focus, and manage applications
- **Natural-language agent** — chains Peekaboo tools (see, click, type, scroll, hotkey, menu, window, app, dock, space)

Built with TypeScript + Swift — TypeScript for MCP/npm distribution, Swift for [direct ScreenCaptureKit access](https://steipete.me/posts/2025/peekaboo-mcp-lightning-fast-macos-screenshots-for-ai-agents) without requiring focus changes. Part of Steinberger's growing ecosystem alongside macos-automator-mcp. Estimated [11,200+ users](https://www.pulsemcp.com/servers/steipete-peekaboo). Requires macOS 15+.

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

**Rating: 4/5** — Apple and macOS MCP is surprisingly mature, anchored by supermemoryai/apple-mcp ([3,100 stars](https://github.com/supermemoryai/apple-mcp), though [archived since January 2026](https://glama.ai/mcp/servers/supermemoryai/apple-mcp)) and Peekaboo ([3,100 stars](https://github.com/steipete/Peekaboo), actively developed). [macos-automator-mcp (758 stars)](https://github.com/steipete/macos-automator-mcp) provides 200+ automation recipes.

The key insight: **AppleScript, despite being decades old, is the [perfect bridge](https://skywork.ai/skypage/en/macos-ai-automator-unlocking/1981180204707401728) between MCP and macOS applications.** Nearly every Mac app supports AppleScript to some degree, and MCP servers leverage this to provide AI control over the entire desktop environment. Siri Shortcuts extend this further, bridging into iOS and HomeKit.

HomeKit gets three independent implementations (HomeClaw at [87 stars](https://github.com/omarshahine/HomeClaw) leads). Apple Music has four (kennethreitz at [84 stars](https://github.com/kennethreitz/mcp-applemusic) leads). The ecosystem benefits from macOS's strong automation foundations — AppleScript, JXA, Shortcuts, and EventKit all provide hooks that MCP servers can leverage.

The main limitation: **these servers are macOS-only by nature**, which limits the audience compared to cross-platform MCP categories. The archival of supermemoryai/apple-mcp also leaves a gap — no single actively-maintained server covers 8+ Apple apps, though forks and alternatives are emerging. But for Mac users, this remains one of the most practical MCP categories — you're controlling your actual desktop environment, apps, and smart home through AI, not just accessing remote APIs.

---

*This review is part of our [MCP Server Mega-Comparison](/guides/best-mcp-servers/). We research and analyze MCP servers — we do not test them hands-on. Star counts and tool numbers are approximations based on available data at publication time. Found an error or a server we missed? [Let us know](/about/).*

*Last updated April 14, 2026 using Claude Opus 4.6 (Anthropic).*

