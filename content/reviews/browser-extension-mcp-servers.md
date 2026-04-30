---
title: "Browser Extension MCP Servers — Chrome DevTools, Browser Automation, Firefox, Safari, WebMCP, and More"
date: 2026-04-30T09:00:00+09:00
description: "Browser extension MCP servers let AI agents control, inspect, and automate real browsers through Chrome extensions, DevTools Protocol, Firefox, Safari, and WebMCP via the Model Context Protocol."
og_description: "Browser extension MCP servers: ChromeDevTools/chrome-devtools-mcp (37,700 stars — official Google DevTools MCP with 34 tools), hangwin/mcp-chrome (11,400 stars — Chrome extension with native browser control), BrowserMCP/mcp (6,400 stars — local automation), WebMCP (1,100 stars — W3C browser-native standard, accepted as W3C deliverable), achiya-automation/safari-mcp NEW (47 stars — 80 tools filling Safari gap), mozilla/firefox-devtools-mcp (131 stars — now official Mozilla project). 15+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "Browser extension MCP servers for AI-powered browser control, DevTools debugging, automation, and web inspection across Chrome, Firefox, Safari, and emerging browser-native standards. **The official Chrome DevTools MCP** — ChromeDevTools/chrome-devtools-mcp (37,700 stars, TypeScript) is the clear leader, now with 34 tools across 8 categories including input automation (9), navigation (6), emulation (2), performance (3), network (2), debugging (6), extensions (5), and memory (1). Experimental vision with coordinate-based tools, WebMCP debugging support for Chrome 149+, and screencast recording. Official Google project with rapid development (805 commits). **Chrome extension pioneer** — hangwin/mcp-chrome (11,400 stars, TypeScript) takes a fundamentally different approach: instead of launching a new browser, it uses your existing Chrome browser as a Chrome extension. This means AI agents inherit your login sessions, cookies, bookmarks, and browser configuration. 20+ tools including tab management, content extraction, semantic search, DOM interaction, network monitoring, and screenshots. The extension architecture avoids bot detection since it operates within a real user browser session. **Browser monitoring suite DISCONTINUED** — AgentDeskAI/browser-tools-mcp (7,200 stars, TypeScript) has been officially discontinued. The README now states 'THIS PROJECT IS NO LONGER ACTIVE PLEASE USE A DIFFERENT SOLUTION.' Additionally, an OS command injection vulnerability (CWE-78) was reported in April 2026 affecting macOS deployments with autoPaste enabled. Users should migrate to alternatives like chrome-devtools-mcp or mcp-chrome. **Local-first automation** — BrowserMCP/mcp (6,400 stars, TypeScript, Apache-2.0) is a Chrome extension + MCP server adapted from Playwright MCP to automate your actual browser rather than creating new instances. Fast local automation without network latency, keeps activity private on-device, maintains logged-in sessions, and avoids basic bot detection by using your real browser fingerprint. Works with VS Code, Claude, Cursor, and Windsurf. **Browser-native standard advancing** — WebMCP (1,100 stars, TypeScript, AGPL-3.0) has been accepted as a W3C deliverable and is transitioning to official web standard development via the webmachinelearning/webmcp repository. Websites register tools via navigator.modelContext API. Now available in Chrome 146+ Canary and Microsoft Edge 147 (added March 2026). Chrome DevTools MCP integrates WebMCP debugging support for Chrome 149+. The WebMCP-org GitHub organization hosts core packages, examples, and documentation. MCP-B extension is no longer open source. **Safari gap FILLED** — achiya-automation/safari-mcp NEW (47 stars, JavaScript, MIT, 80 tools) provides native Safari browser automation via AppleScript + Swift daemon. 80 tools across 19 categories including navigation, page reading, clicking, form input, screenshots/PDF, scrolling, tabs, JavaScript execution, element inspection, accessibility, drag-and-drop, cookies/storage (10 tools), clipboard, networking (6 tools), and console. ~60% less CPU than Chrome on Apple Silicon, ~5ms latency per command, zero-overhead background operation preserving logins. Framework-aware (React, Vue, Angular, Svelte). The biggest gap from the initial review has been filled. **Safari alternative** — lxman/safari-mcp-server (32 stars, TypeScript, MIT, 9 tools) provides Safari automation via SafariDriver with session management, DevTools access (console, network, performance), screenshots, and JavaScript execution. Less comprehensive than safari-mcp but more DevTools-focused. **Official Mozilla Firefox DevTools** — mozilla/firefox-devtools-mcp (131 stars, TypeScript, MIT, v0.9.2) — the freema/firefox-devtools-mcp project has been adopted by Mozilla and moved to the official mozilla/ GitHub organization. 189 commits. Features page management, snapshot/UID interactions, input handling, network capture, console monitoring, screenshots, script evaluation, privileged context access, WebExtension management, and Firefox preferences control. Claude Code plugin available. Install via npx firefox-devtools-mcp@latest. **Security-focused Firefox control** — eyalzh/browser-control-mcp (277 stars, TypeScript, v1.5.1) pairs an MCP server with a Firefox extension that prioritizes safety: local-only connection with shared secret, extension-side audit log for tool calls, tool enable/disable configuration, domain-level consent for content reading, and zero third-party runtime dependencies. Tab management, history access, named tab groups with colors. Available on Firefox Add-ons. **Firefox multi-session automation** — JediLuke/firefox-mcp-server (TypeScript) provides 28 specialized tools for Firefox automation via Playwright. Isolated browser sessions with independent cookies/storage, concurrent multi-session management, real-time console monitoring, WebSocket traffic capture, network activity monitoring with timing data, and performance metrics (DOM timing, paint events, memory usage). Experimental/vibe-coded project. **Lightweight Chrome CDP control** — lxe/chrome-mcp (47 stars, TypeScript) provides granular Chrome control via Chrome DevTools Protocol without screenshots. Navigate, click coordinates/elements, type text, get semantic page info including interactive elements and text nodes, and query page state (URL, title, scroll position, viewport). SSE transport. Requires Chrome with remote debugging enabled. **Community Chrome DevTools** — benjaminr/chrome-devtools-mcp (296 stars, TypeScript, v1.0.3) provides Chrome DevTools Protocol integration for Claude Desktop and Claude Code. Element inspection, console access, and browser automation. Predates the official ChromeDevTools version. **Cross-browser extension** — djyde/browser-mcp (12 stars, TypeScript) supports Chrome, Edge, and Firefox with a unified extension. Get markdown from the current page, summarize page content, inject CSS (e.g., dark mode), and search browser history. Lightweight multi-browser approach. **WebSocket page bridge** — Oanakiaja/chrome-extension-bridge-mcp (TypeScript) establishes a WebSocket connection between web pages and a local MCP server, exposing the global window object. Useful for interacting with web application state from AI tools. **Comprehensive browser bridge** — robhicks/browser-mcp-bridge (TypeScript) provides full browser content bridging to Claude Code: page content extraction, DOM snapshots with computed styles, JavaScript execution in page context, screenshots, console monitoring, network request tracking, performance metrics, accessibility tree access, debugger attachment/detachment, and multi-tab management. **Remaining gaps** — no unified cross-browser server provides consistent automation across Chrome, Firefox, and Safari through one API. Mobile browser MCP support is absent — no servers target Chrome for Android, Safari for iOS, or mobile-specific debugging. No MCP server specializes in browser extension development or testing workflows. WebMCP is advancing through W3C but not yet production-ready in stable browser releases."
last_refreshed: 2026-04-30
categories: ["/categories/web-search-scraping/"]
---

Browser extension MCP servers let AI assistants control, inspect, debug, and automate real browsers through the Model Context Protocol. Instead of writing Puppeteer scripts or clicking through DevTools manually, AI agents can navigate pages, extract content, monitor network traffic, and run accessibility audits conversationally.

This review covers the **browser extension** ecosystem — Chrome DevTools integration, Chrome extension-based automation, Firefox control, browser-native protocols, and DevTools Protocol servers. For related servers, see our [Web Scraping & Crawling review](/reviews/web-scraping-crawling-mcp-servers/) and [Testing & QA review](/reviews/testing-qa-mcp-servers/).

The headline findings: **Chrome DevTools has an official MCP server** (37,700 stars) backed by Google, now with 34 tools and WebMCP debugging support. **The Safari gap has been filled** — achiya-automation/safari-mcp provides 80 native tools via AppleScript. **firefox-devtools-mcp is now an official Mozilla project** at 131 stars. **AgentDeskAI/browser-tools-mcp has been discontinued** (command injection vulnerability + project ended). **WebMCP has been accepted as a W3C deliverable**, now available in Edge 147 alongside Chrome.

## Official DevTools

### ChromeDevTools/chrome-devtools-mcp — Official Google Chrome DevTools MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 37,700 | TypeScript | — | 34 |

The **official MCP server from Google's Chrome DevTools team** — the most popular server in this category by far, with 805 commits and 2,300 forks:

- **34 tools across 8 categories** — input automation (9 tools), navigation (6), emulation (2), performance (3), network (2), debugging (6), extensions (5), memory (1)
- **Performance analysis** — record traces and extract actionable performance insights
- **Advanced debugging** — analyze network requests, take screenshots, check console messages with source-mapped stack traces
- **Reliable automation** — Puppeteer-based browser control with automatic wait for action results
- **Memory profiling** — heap snapshot capture for memory leak debugging
- **Experimental vision** — coordinate-based tools like click_at(x,y) and screencast recording (requires ffmpeg)
- **WebMCP debugging** — supports debugging WebMCP tools in Chrome 149+ with `--experimentalWebmcp` flag
- **Browser emulation** — dark/light mode, network throttling options

Works with Gemini, Claude, Cursor, and Copilot. Includes accessibility debugging skills. Rapid development with official Google backing.

### benjaminr/chrome-devtools-mcp — Community Chrome DevTools

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chrome-devtools-mcp](https://github.com/benjaminr/chrome-devtools-mcp) | 296 | TypeScript | — | 10+ |

**Community-built Chrome DevTools Protocol integration** that predates the official version. Element inspection, console access, and browser automation. Integrates with Claude Desktop and Claude Code. v1.0.3 released. Useful as an alternative if you want a lighter-weight DevTools integration.

## Chrome Extensions

### hangwin/mcp-chrome — Chrome Extension Browser Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-chrome](https://github.com/hangwin/mcp-chrome) | 11,400 | TypeScript | — | 20+ |

**The most popular Chrome extension MCP server** — uses your actual daily browser instead of launching a new instance (192 commits, 1,000 forks):

- **Native browser sessions** — inherits your login state, cookies, bookmarks, and browser configuration
- **Tab management** — open, close, switch, and list browser tabs
- **Content extraction** — get page content, extract text, read DOM elements
- **Semantic search** — AI-powered semantic search across browser tabs
- **DOM interaction** — click elements, fill forms, interact with page components
- **Screenshots** — advanced capture with element targeting and full-page support
- **Network monitoring** — WebRequest and debugger APIs with response body capture

The extension architecture is a key differentiator: because it runs inside your real Chrome browser, it avoids bot detection entirely. AI agents see exactly what you see, with all your authenticated sessions intact.

### AgentDeskAI/browser-tools-mcp — DISCONTINUED

| Server | Stars | Language | License | Status |
|--------|-------|----------|---------|--------|
| [browser-tools-mcp](https://github.com/AgentDeskAI/browser-tools-mcp) | 7,200 | TypeScript | — | **Discontinued** |

**⚠️ This project has been officially discontinued.** The README now states: "THIS PROJECT IS NO LONGER ACTIVE PLEASE USE A DIFFERENT SOLUTION FOR THIS."

Additionally, an **OS command injection vulnerability** (CWE-78) was reported in April 2026. The flaw allows attacker-controlled path data to be interpolated into a shell command via `osascript` without escaping, enabling arbitrary OS command execution on macOS deployments where autoPaste is enabled. The vulnerability was not patched before the project was discontinued.

Previously offered development-focused browser monitoring bridging IDE and browser — console capture, network monitoring, Lighthouse-driven accessibility/performance/SEO audits, and auto-paste screenshots into Cursor. Users should migrate to alternatives like chrome-devtools-mcp or mcp-chrome.

### BrowserMCP/mcp — Local Browser Automation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [BrowserMCP/mcp](https://github.com/BrowserMCP/mcp) | 6,400 | TypeScript | Apache-2.0 | 10+ |

**Adapted from Playwright MCP to automate your actual browser** rather than creating new instances:

- **Local-first** — fast automation without network latency
- **Privacy-preserving** — all activity stays on your device
- **Session reuse** — maintains logged-in sessions across interactions
- **Anti-detection** — uses your real browser fingerprint, avoiding basic bot detection and CAPTCHAs
- **Multi-client** — works with VS Code, Claude, Cursor, and Windsurf

Apache-2.0 licensed. 494 forks. The approach of automating the user's existing browser (rather than a headless instance) is increasingly popular in this space.

### djyde/browser-mcp — Cross-Browser Extension

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [browser-mcp](https://github.com/djyde/browser-mcp) | 12 | TypeScript | — | 4 |

**Lightweight cross-browser extension** supporting Chrome, Edge, and Firefox:

- Get markdown from the current page
- Summarize page content
- Inject CSS styles (e.g., switch to dark mode)
- Search browser history

Simple but effective for basic browser interaction across multiple browsers.

## Browser-Native Protocol

### WebMCP — W3C Browser-Native Standard

| Server | Stars | Language | License | Status |
|--------|-------|----------|---------|--------|
| [WebMCP](https://github.com/MiguelsPizza/WebMCP) | 1,100 | TypeScript | AGPL-3.0 | W3C Deliverable |

**Accepted as a W3C deliverable** and transitioning to official web standard development via the [webmachinelearning/webmcp](https://github.com/webmachinelearning/webmcp) repository:

- **Websites as MCP servers** — web apps register tools via `navigator.modelContext` API
- **W3C accepted** — formally accepted as a W3C Community Group deliverable, advancing beyond draft status
- **Multi-browser support** — available in Chrome 146+ Canary and Microsoft Edge 147 (added March 2026)
- **Chrome DevTools integration** — WebMCP debugging support in Chrome 149+ via `--experimentalWebmcp` flag
- **WebMCP DevTools extension** — dedicated Chrome Web Store extension for inspecting, testing, and monitoring WebMCP tools
- **WebMCP-org** — GitHub organization created with core packages, examples, documentation, and userscripts
- **Co-developed by Google and Microsoft** — strong industry backing

The original MiguelsPizza/WebMCP repository (164 commits, 75 forks) is now maintained for historical reference — the MCP-B extension is no longer open source. Active development has moved to the W3C Community Group. WebMCP could eventually make many browser automation MCP servers unnecessary — if a website exposes its own MCP tools, there's no need for an external extension to control it.

Production adoption expected second half of 2026. Not a replacement for Anthropic's MCP (which uses JSON-RPC for client-server communication) — WebMCP operates entirely client-side within the browser.

## Safari

### achiya-automation/safari-mcp — Native Safari Browser Automation (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [safari-mcp](https://github.com/achiya-automation/safari-mcp) | 47 | JavaScript | MIT | 80 |

**Fills the biggest gap from the initial review** — the first comprehensive Safari MCP server, providing native macOS browser automation via AppleScript + Swift daemon:

- **80 tools across 19 categories** — navigation (4), page reading (3), clicking (5), form input (7), screenshots/PDF (3), scrolling (3), tab management (4), wait functions (2), JavaScript execution (1), element inspection (4), accessibility (1), drag-and-drop (1), file operations (2), dialogs (2), device emulation (2), cookies/storage (10), clipboard (2), networking (6), console (4)
- **Native WebKit performance** — ~60% less CPU than Chrome on Apple Silicon, ~5ms latency per command vs ~80ms for alternatives
- **Zero overhead** — runs in background, preserves existing logins and sessions
- **Framework-aware** — compatibility with React, Vue, Angular, and Svelte
- **Drop-in replacement** — positioned as alternative to Chrome DevTools MCP for macOS users

Requires macOS with Safari, Node.js 18+, and Safari Developer settings enabled. Install via `npx safari-mcp`.

### lxman/safari-mcp-server — Safari DevTools Access (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [safari-mcp-server](https://github.com/lxman/safari-mcp-server) | 32 | TypeScript | MIT | 9 |

**Safari automation via SafariDriver** — less comprehensive than safari-mcp but more DevTools-focused:

- Session management (start, control, manage Safari sessions)
- Developer tools access (console logs, network logs, performance metrics)
- Screenshot capture and DOM element inspection
- JavaScript execution within browser context
- Multi-session management support

Requires macOS, Node.js 18+, Safari 10+, and SafariDriver authorization via admin privileges.

## Firefox

### mozilla/firefox-devtools-mcp — Official Mozilla Firefox DevTools

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [firefox-devtools-mcp](https://github.com/mozilla/firefox-devtools-mcp) | 131 | TypeScript | MIT | 15+ |

**Now an official Mozilla project** — the freema/firefox-devtools-mcp project has been adopted by Mozilla and moved to the `mozilla/` GitHub organization. 189 commits, 30 forks, v0.9.2:

- **Page management** — navigation, DOM inspection, snapshot/UID-based interactions
- **Input handling** — user input simulation and form interaction
- **Network capture** — request monitoring and analysis
- **Console monitoring** — real-time console message capture
- **Screenshots** — page and element capture
- **Script evaluation** — JavaScript execution in page context
- **Privileged context access** — Firefox-specific advanced features
- **WebExtension management** — manage Firefox extensions
- **Firefox preferences** — control Firefox configuration settings
- **Claude Code plugin** — installable plugin with commands, skills, and agents

Install via `npx firefox-devtools-mcp@latest`. Requires Node.js 20.19+ and Firefox 100+. Referenced in [official Firefox Source Docs](https://firefox-source-docs.mozilla.org/ai-agent-tools/firefox-devtools-mcp.html).

### eyalzh/browser-control-mcp — Security-Focused Firefox Extension

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [browser-control-mcp](https://github.com/eyalzh/browser-control-mcp) | 277 | TypeScript | — | 10+ |

**The most security-conscious browser MCP server** — designed for safe use with your personal browser (72 commits, 62 forks, v1.5.1):

- **Local-only connection** — shared secret between MCP server and extension
- **Audit log** — extension-side log of all tool calls for accountability
- **Tool control** — enable/disable individual tools from the extension settings
- **Domain consent** — reading webpage content requires user consent per domain
- **Zero dependencies** — no runtime third-party dependencies in the extension
- **Tab management** — open, close, list tabs; create named tab groups with colors; reorder tabs
- **History access** — search browsing history

Available on [Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/browser-control-mcp/).

### JediLuke/firefox-mcp-server — Multi-Session Firefox Automation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [firefox-mcp-server](https://github.com/JediLuke/firefox-mcp-server) | — | TypeScript | — | 28 |

**28 specialized tools for Firefox automation** via Playwright:

- **Isolated sessions** — independent cookies and storage per session
- **Concurrent operations** — manage multiple browser sessions simultaneously
- **Real-time monitoring** — console output, WebSocket traffic, network activity with timing data
- **Performance metrics** — DOM timing, paint events, and memory usage tracking

Self-described as "fully vibe-coded" and experimental. Requires Node.js 18+ and Playwright-installed Firefox. Tool names optimized for LLM discovery.

## DevTools Protocol & Bridges

### lxe/chrome-mcp — Lightweight Chrome CDP Control

| Server | Stars | Language | License | Transport |
|--------|-------|----------|---------|-----------|
| [chrome-mcp](https://github.com/lxe/chrome-mcp) | 47 | TypeScript | — | SSE |

**Granular Chrome control via Chrome DevTools Protocol** without screenshots:

- Navigate to URLs
- Click at coordinates or by element index
- Type text at current focus
- Get semantic page info — interactive elements, text nodes
- Query page state — URL, title, scroll position, viewport size

SSE transport. Requires Bun (recommended) or Node.js 14+ and Chrome with remote debugging enabled.

### Oanakiaja/chrome-extension-bridge-mcp — WebSocket Page Bridge

| Server | Stars | Language | License | Type |
|--------|-------|----------|---------|------|
| [chrome-extension-bridge-mcp](https://github.com/Oanakiaja/chrome-extension-bridge-mcp) | — | TypeScript | — | Bridge |

**WebSocket bridge between web pages and a local MCP server.** The Chrome extension connects to pages and exposes the global `window` object, allowing AI tools to interact with web application state and execute functions. Useful for accessing client-side application logic that isn't exposed via the page's public API.

### robhicks/browser-mcp-bridge — Comprehensive Browser Bridge

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [browser-mcp-bridge](https://github.com/robhicks/browser-mcp-bridge) | — | TypeScript | — | 12+ |

**Full browser content bridging to Claude Code:**

- Page content extraction — HTML, text, metadata, and page structure
- DOM snapshots with computed styles
- JavaScript execution in page context
- Screenshot capture
- Console message monitoring
- Network request tracking with performance metrics
- Accessibility tree access
- Debugger attachment and detachment
- Multi-tab management

Custom DevTools panel for advanced inspection. Designed specifically for Claude Code integration.

## What's Missing

The browser extension MCP ecosystem has narrowed its gaps significantly but some remain:

- **No unified cross-browser server** — no single MCP server provides consistent automation across Chrome, Firefox, and Safari through one API
- **No mobile browser support** — no servers target Chrome for Android, Safari for iOS, or mobile-specific debugging scenarios
- **No extension development MCP** — no server assists with browser extension development, testing, or debugging workflows
- **WebMCP not yet in stable releases** — available in Chrome Canary and Edge 147 behind flags; production adoption expected second half of 2026
- **browser-tools-mcp gap** — the discontinuation of browser-tools-mcp (7,200 stars) leaves a gap in IDE-integrated browser monitoring, though chrome-devtools-mcp and mcp-chrome largely cover the same capabilities

## The Bottom Line

**Rating: 4.5/5** — Browser extension MCP servers remain one of the strongest categories in the MCP ecosystem. The official Chrome DevTools MCP has surged to 37,700 stars (+31%) with 34 tools and WebMCP debugging support. The category has undergone significant structural changes since the initial review.

**Three major developments define this refresh:** First, the **Safari gap has been filled** — achiya-automation/safari-mcp provides 80 native tools via AppleScript with ~60% less CPU than Chrome on Apple Silicon, addressing the single biggest gap from the initial review. Second, **firefox-devtools-mcp has been adopted by Mozilla** as an official project, growing from 56 to 131 stars with v0.9.2 and a Claude Code plugin. Third, **AgentDeskAI/browser-tools-mcp has been discontinued** after an unpatched OS command injection vulnerability — a cautionary tale about security in browser automation.

**WebMCP is advancing rapidly** — accepted as a W3C deliverable, now available in Edge 147 alongside Chrome, with Chrome DevTools MCP adding WebMCP debugging support for Chrome 149+. The standard is moving from "interesting experiment" to "browser platform feature."

The remaining gaps are unified cross-browser automation and mobile browser support. For developers building AI-assisted browser workflows, the ecosystem offers mature options across Chrome, Firefox, and now Safari.

*This review was last refreshed on 2026-04-30 using Claude Opus 4.6 (Anthropic).*
