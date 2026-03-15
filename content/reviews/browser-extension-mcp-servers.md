---
title: "Browser Extension MCP Servers — Chrome DevTools, Browser Automation, Firefox, WebMCP, and More"
date: 2026-03-17T09:00:00+09:00
description: "Browser extension MCP servers let AI agents control, inspect, and automate real browsers through Chrome extensions, DevTools Protocol, and Firefox integration via the Model Context Protocol. We reviewed 15+ servers across 5 subcategories. Official DevTools: ChromeDevTools/chrome-devtools-mcp (28,700 stars, TypeScript — official Google Chrome DevTools MCP with Puppeteer automation, performance tracing, Lighthouse audits, accessibility debugging, memory profiling, network throttling). Chrome extensions: hangwin/mcp-chrome (10,800 stars, TypeScript — Chrome extension MCP using native browser with existing sessions/logins, semantic search, content analysis), AgentDeskAI/browser-tools-mcp (7,100 stars, TypeScript — browser monitoring with WCAG accessibility audits, Lighthouse performance analysis, SEO evaluation, auto-paste to IDE), BrowserMCP/mcp (6,100 stars, TypeScript, Apache-2.0 — Chrome extension for local automation, real browser fingerprint, no bot detection), djyde/browser-mcp (TypeScript — cross-browser extension for Chrome/Edge/Firefox, page markdown, history search, CSS injection). Browser-native protocols: MiguelsPizza/WebMCP (924 stars, TypeScript — MCP-B browser transport protocol, websites as MCP servers, W3C draft standard, Chrome 146 early preview). Firefox: freema/firefox-devtools-mcp (56 stars, TypeScript — Firefox DevTools via WebDriver BiDi, DOM inspection, network monitoring, console capture), eyalzh/browser-control-mcp (250 stars, TypeScript — security-focused Firefox extension with audit log, domain consent, tab management), JediLuke/firefox-mcp-server (TypeScript — 28 tools, multi-session management, WebSocket monitoring, performance metrics via Playwright). DevTools Protocol: lxe/chrome-mcp (42 stars, TypeScript — lightweight CDP-based Chrome control, semantic page info, SSE transport), benjaminr/chrome-devtools-mcp (287 stars, TypeScript — community Chrome DevTools Protocol server with element inspection and console access), Oanakiaja/chrome-extension-bridge-mcp (TypeScript — WebSocket bridge between web pages and MCP servers). Bridge/utility: robhicks/browser-mcp-bridge (TypeScript — comprehensive bridge with debugger attachment, accessibility tree, performance metrics, JavaScript execution). Gaps: no Safari/WebKit MCP server, no cross-browser unified MCP, limited mobile browser support, no browser extension development/testing MCP, no cookie/storage management specialization, WebMCP standard still in early preview. 15+ servers across 5 subcategories. Rating: 4.5/5."
og_description: "Browser extension MCP servers: ChromeDevTools/chrome-devtools-mcp (28,700 stars — official Google DevTools MCP), hangwin/mcp-chrome (10,800 stars — Chrome extension with native browser control), AgentDeskAI/browser-tools-mcp (7,100 stars — monitoring/audits), BrowserMCP/mcp (6,100 stars — local automation), WebMCP (924 stars — W3C browser-native standard). 15+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "Browser extension MCP servers for AI-powered browser control, DevTools debugging, automation, and web inspection across Chrome, Firefox, and emerging browser-native standards. **The official Chrome DevTools MCP** — ChromeDevTools/chrome-devtools-mcp (28,700 stars, TypeScript) is the clear leader, providing coding agents with full Chrome DevTools access via Puppeteer for reliable automation, performance analysis (trace recording and insights), advanced debugging (network requests, screenshots, source-mapped console messages), memory heap snapshot capture for leak debugging, Lighthouse scores for accessibility/SEO/best practices, and browser emulation (dark/light mode, network throttling). Official Google project with rapid development. **Chrome extension pioneer** — hangwin/mcp-chrome (10,800 stars, TypeScript) takes a fundamentally different approach: instead of launching a new browser, it uses your existing Chrome browser as a Chrome extension. This means AI agents inherit your login sessions, cookies, bookmarks, and browser configuration. Features include tab management, content extraction, semantic search across pages, DOM interaction, and screenshot capture. The extension architecture avoids bot detection since it operates within a real user browser session. **Browser monitoring suite** — AgentDeskAI/browser-tools-mcp (7,100 stars, TypeScript) bridges your IDE and browser for development workflows. The Chrome extension captures console logs, network activity, and DOM elements in real time. Includes WCAG-compliant accessibility audits (color contrast, alt text, ARIA attributes, keyboard navigation), Lighthouse-driven performance analysis, SEO evaluation, and auto-paste functionality for screenshots into Cursor IDE. 4.8/5 user rating. **Local-first automation** — BrowserMCP/mcp (6,100 stars, TypeScript, Apache-2.0) is a Chrome extension + MCP server adapted from Playwright MCP to automate your actual browser rather than creating new instances. Fast local automation without network latency, keeps activity private on-device, maintains logged-in sessions, and avoids basic bot detection by using your real browser fingerprint. Works with VS Code, Claude, Cursor, and Windsurf. **Browser-native standard** — MiguelsPizza/WebMCP (924 stars, TypeScript) represents the future of browser-MCP integration. MCP-B is an official extension to the Model Context Protocol for browser environments, enabling websites to expose MCP servers within browser tabs. Websites register tools via navigator.modelContext API, providing deterministic APIs instead of visual/click-based interactions. Available as early preview in Chrome 146 Canary behind a flag. W3C Draft Community Group Report published February 2026, developed jointly by Google and Microsoft engineers. This could eventually make many browser automation MCP servers unnecessary. **Security-focused Firefox control** — eyalzh/browser-control-mcp (250 stars, TypeScript) pairs an MCP server with a Firefox extension that prioritizes safety: local-only connection with shared secret, extension-side audit log for tool calls, tool enable/disable configuration, domain-level consent for content reading, and zero third-party runtime dependencies. Tab management, history access, named tab groups with colors. Available on Firefox Add-ons. **Firefox DevTools via WebDriver BiDi** — freema/firefox-devtools-mcp (56 stars, TypeScript) enables AI assistants to inspect and control Firefox through WebDriver BiDi protocol. Page navigation, DOM inspection, network monitoring, console capture, screenshots, and user input simulation. Used in Mozilla's own Firefox development with Claude Code. Install via npx. Referenced in official Firefox Source Docs. **Firefox multi-session automation** — JediLuke/firefox-mcp-server (TypeScript) provides 28 specialized tools for Firefox automation via Playwright. Isolated browser sessions with independent cookies/storage, concurrent multi-session management, real-time console monitoring, WebSocket traffic capture, network activity monitoring with timing data, and performance metrics (DOM timing, paint events, memory usage). Experimental/vibe-coded project. **Lightweight Chrome CDP control** — lxe/chrome-mcp (42 stars, TypeScript) provides granular Chrome control via Chrome DevTools Protocol without screenshots. Navigate, click coordinates/elements, type text, get semantic page info including interactive elements and text nodes, and query page state (URL, title, scroll position, viewport). SSE transport. Requires Chrome with remote debugging enabled. **Community Chrome DevTools** — benjaminr/chrome-devtools-mcp (287 stars, TypeScript) provides Chrome DevTools Protocol integration for Claude Desktop and Claude Code. Element inspection, console access, and browser automation. Predates the official ChromeDevTools version. **Cross-browser extension** — djyde/browser-mcp (TypeScript) supports Chrome, Edge, and Firefox with a unified extension. Get markdown from the current page, summarize page content, inject CSS (e.g., dark mode), and search browser history. Lightweight multi-browser approach. **WebSocket page bridge** — Oanakiaja/chrome-extension-bridge-mcp (TypeScript) establishes a WebSocket connection between web pages and a local MCP server, exposing the global window object. Useful for interacting with web application state from AI tools. **Comprehensive browser bridge** — robhicks/browser-mcp-bridge (TypeScript) provides full browser content bridging to Claude Code: page content extraction, DOM snapshots with computed styles, JavaScript execution in page context, screenshots, console monitoring, network request tracking, performance metrics, accessibility tree access, debugger attachment/detachment, and multi-tab management. **Gaps remain in several areas** — no Safari or WebKit MCP server exists, leaving Apple's browser ecosystem entirely unserved. No single MCP server provides unified cross-browser automation (Chrome + Firefox + Safari) through a consistent API. Mobile browser MCP support is absent — no servers target Chrome for Android, Safari for iOS, or mobile-specific debugging. No MCP server specializes in browser extension development or testing workflows. Cookie and storage management (localStorage, IndexedDB, sessionStorage) lacks dedicated MCP tooling. The WebMCP standard is still in early preview behind a flag in Chrome 146 Canary — production adoption is likely mid-to-late 2026. No MCP server provides browser performance benchmarking across different browsers for comparison testing."
---

Browser extension MCP servers let AI assistants control, inspect, debug, and automate real browsers through the Model Context Protocol. Instead of writing Puppeteer scripts or clicking through DevTools manually, AI agents can navigate pages, extract content, monitor network traffic, and run accessibility audits conversationally.

This review covers the **browser extension** ecosystem — Chrome DevTools integration, Chrome extension-based automation, Firefox control, browser-native protocols, and DevTools Protocol servers. For related servers, see our [Web Scraping & Crawling review](/reviews/web-scraping-crawling-mcp-servers/) and [Testing & QA review](/reviews/testing-qa-mcp-servers/).

The headline findings: **Chrome DevTools has an official MCP server** (28,700 stars) backed by Google. **Chrome extension-based servers dominate** with three projects over 6,000 stars each. **WebMCP is emerging as a browser-native standard** via W3C, with early preview in Chrome 146.

## Official DevTools

### ChromeDevTools/chrome-devtools-mcp — Official Google Chrome DevTools MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 28,700 | TypeScript | — | 15+ |

The **official MCP server from Google's Chrome DevTools team** — the most popular server in this category by far:

- **Performance analysis** — record traces and extract actionable performance insights
- **Advanced debugging** — analyze network requests, take screenshots, check console messages with source-mapped stack traces
- **Reliable automation** — Puppeteer-based browser control with automatic wait for action results
- **Memory profiling** — heap snapshot capture for memory leak debugging
- **Lighthouse integration** — accessibility, SEO, and best practices audits
- **Browser emulation** — dark/light mode, network throttling options

Works with Gemini, Claude, Cursor, and Copilot. Includes accessibility debugging skills. Rapid development with official Google backing.

### benjaminr/chrome-devtools-mcp — Community Chrome DevTools

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chrome-devtools-mcp](https://github.com/benjaminr/chrome-devtools-mcp) | 287 | TypeScript | — | 10+ |

**Community-built Chrome DevTools Protocol integration** that predates the official version. Element inspection, console access, and browser automation. Integrates with Claude Desktop and Claude Code. Useful as an alternative if you want a lighter-weight DevTools integration.

## Chrome Extensions

### hangwin/mcp-chrome — Chrome Extension Browser Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-chrome](https://github.com/hangwin/mcp-chrome) | 10,800 | TypeScript | — | 10+ |

**The most popular Chrome extension MCP server** — uses your actual daily browser instead of launching a new instance:

- **Native browser sessions** — inherits your login state, cookies, bookmarks, and browser configuration
- **Tab management** — open, close, switch, and list browser tabs
- **Content extraction** — get page content, extract text, read DOM elements
- **Semantic search** — search across page content using semantic matching
- **DOM interaction** — click elements, fill forms, interact with page components
- **Screenshots** — capture visible page content

The extension architecture is a key differentiator: because it runs inside your real Chrome browser, it avoids bot detection entirely. AI agents see exactly what you see, with all your authenticated sessions intact.

### AgentDeskAI/browser-tools-mcp — Browser Monitoring & Auditing

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [browser-tools-mcp](https://github.com/AgentDeskAI/browser-tools-mcp) | 7,100 | TypeScript | — | 15+ |

**Development-focused browser monitoring** that bridges your IDE and browser:

- **Console capture** — real-time console logs, errors, and warnings sent to your IDE
- **Network monitoring** — HTTP request/response tracking with timing data
- **Accessibility audits** — WCAG-compliant checks for color contrast, missing alt text, keyboard navigation traps, ARIA attributes
- **Performance analysis** — Lighthouse-driven analysis of render-blocking resources, DOM size, unoptimized images
- **SEO evaluation** — on-page SEO factors (metadata, headings, link structure) with improvement suggestions
- **Auto-paste** — screenshots automatically pasted into Cursor IDE

4.8/5 user rating. Three-component architecture: Chrome extension + browser-tools-server + MCP server for IDE integration.

### BrowserMCP/mcp — Local Browser Automation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [BrowserMCP/mcp](https://github.com/BrowserMCP/mcp) | 6,100 | TypeScript | Apache-2.0 | 10+ |

**Adapted from Playwright MCP to automate your actual browser** rather than creating new instances:

- **Local-first** — fast automation without network latency
- **Privacy-preserving** — all activity stays on your device
- **Session reuse** — maintains logged-in sessions across interactions
- **Anti-detection** — uses your real browser fingerprint, avoiding basic bot detection and CAPTCHAs
- **Multi-client** — works with VS Code, Claude, Cursor, and Windsurf

Apache-2.0 licensed. The approach of automating the user's existing browser (rather than a headless instance) is increasingly popular in this space.

### djyde/browser-mcp — Cross-Browser Extension

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [browser-mcp](https://github.com/djyde/browser-mcp) | — | TypeScript | — | 4 |

**Lightweight cross-browser extension** supporting Chrome, Edge, and Firefox:

- Get markdown from the current page
- Summarize page content
- Inject CSS styles (e.g., switch to dark mode)
- Search browser history

Simple but effective for basic browser interaction across multiple browsers.

## Browser-Native Protocol

### MiguelsPizza/WebMCP — MCP-B Browser Transport Standard

| Server | Stars | Language | License | Status |
|--------|-------|----------|---------|--------|
| [WebMCP](https://github.com/MiguelsPizza/WebMCP) | 924 | TypeScript | — | Early Preview |

**The future of browser-MCP integration** — an official extension to the Model Context Protocol for browser environments:

- **Websites as MCP servers** — web apps register tools via `navigator.modelContext` API
- **Deterministic APIs** — structured tool calls replace visual/click-based interactions
- **W3C standardization** — Draft Community Group Report published February 2026
- **Chrome 146 early preview** — available behind the "WebMCP for testing" flag in Canary
- **Co-developed by Google and Microsoft** — strong industry backing

WebMCP (also called MCP-B) enables intra-browser communication between AI agents and web applications. Instead of scraping or automating clicks, websites expose callable tools directly. This could eventually make many browser automation MCP servers unnecessary — if a website exposes its own MCP tools, there's no need for an external extension to control it.

Production adoption expected mid-to-late 2026. Not a replacement for Anthropic's MCP (which uses JSON-RPC for client-server communication) — WebMCP operates entirely client-side within the browser.

## Firefox

### eyalzh/browser-control-mcp — Security-Focused Firefox Extension

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [browser-control-mcp](https://github.com/eyalzh/browser-control-mcp) | 250 | TypeScript | — | 10+ |

**The most security-conscious browser MCP server** — designed for safe use with your personal browser:

- **Local-only connection** — shared secret between MCP server and extension
- **Audit log** — extension-side log of all tool calls for accountability
- **Tool control** — enable/disable individual tools from the extension settings
- **Domain consent** — reading webpage content requires user consent per domain
- **Zero dependencies** — no runtime third-party dependencies in the extension
- **Tab management** — open, close, list tabs; create named tab groups with colors; reorder tabs
- **History access** — search browsing history

Available on [Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/browser-control-mcp/). Still experimental — use with caution.

### freema/firefox-devtools-mcp — Firefox DevTools via WebDriver BiDi

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [firefox-devtools-mcp](https://github.com/freema/firefox-devtools-mcp) | 56 | TypeScript | — | 10+ |

**Firefox DevTools integration via WebDriver BiDi** (Selenium WebDriver):

- Page navigation and DOM inspection
- Network monitoring and console capture
- Screenshots and user input simulation
- Firefox MOZ_LOG system for detailed debug output
- Snapshot/UID-based interactions

Used in Mozilla's own Firefox development with Claude Code — referenced in [official Firefox Source Docs](https://firefox-source-docs.mozilla.org/ai-agent-tools/firefox-devtools-mcp.html). Install via `npx firefox-devtools-mcp@latest`. Requires Node.js 20.19+ and Firefox 100+. Also available via Docker.

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
| [chrome-mcp](https://github.com/lxe/chrome-mcp) | 42 | TypeScript | — | SSE |

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

The browser extension MCP ecosystem has some notable gaps:

- **No Safari or WebKit MCP server** — Apple's browser is entirely unserved, leaving a gap for iOS and macOS development workflows
- **No unified cross-browser server** — no single MCP server provides consistent automation across Chrome, Firefox, and Safari through one API
- **No mobile browser support** — no servers target Chrome for Android, Safari for iOS, or mobile-specific debugging scenarios
- **No extension development MCP** — no server assists with browser extension development, testing, or debugging workflows
- **No dedicated storage management** — cookie, localStorage, IndexedDB, and sessionStorage management lacks specialized MCP tooling
- **WebMCP still in early preview** — available only behind a flag in Chrome 146 Canary; production adoption expected mid-to-late 2026
- **No cross-browser performance comparison** — no server enables benchmarking page performance across different browsers

## The Bottom Line

**Rating: 4.5/5** — Browser extension MCP servers are one of the strongest categories in the MCP ecosystem. The official Chrome DevTools MCP (28,700 stars) provides production-quality debugging and automation backed by Google. Three Chrome extension projects (mcp-chrome, browser-tools-mcp, BrowserMCP) each exceed 6,000 stars, reflecting massive developer interest in AI-controlled browsers.

The category's real strength is diversity of approaches: DevTools Protocol for debugging, Chrome extensions for session-aware automation, Firefox extensions for security-conscious browsing, and the emerging WebMCP standard for browser-native tool exposure. WebMCP in particular could reshape how AI agents interact with websites — instead of automating clicks, websites will expose structured tools directly.

Firefox has solid coverage with three dedicated servers, including one referenced in Mozilla's own documentation. The main gaps are Safari (zero coverage) and mobile browsers. For developers building AI-assisted workflows that involve browser interaction, this category offers mature, well-maintained options today.
