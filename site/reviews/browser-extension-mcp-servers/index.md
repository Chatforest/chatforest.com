# Browser Extension MCP Servers — Chrome DevTools, Browser Automation, Firefox, WebMCP, and More

> Browser extension MCP servers let AI agents control, inspect, and automate real browsers through Chrome extensions, DevTools Protocol, and Firefox integration via the Model Context Protocol.


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

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

