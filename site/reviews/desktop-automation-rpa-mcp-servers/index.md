# Desktop Automation & Browser Control MCP Servers — Playwright, Selenium, Windows-MCP, macOS Automator, and More

> Desktop automation and browser control MCP servers give AI agents eyes and hands — the ability to see screens, click buttons, type text, and control applications through the Model Context Protocol.


Desktop automation and browser control MCP servers represent a fundamental capability shift — they give AI agents "eyes and hands" to interact with computer interfaces the same way humans do. Instead of calling APIs, these servers let agents see screens, click buttons, fill forms, navigate applications, and execute system commands through the Model Context Protocol.

The landscape spans six areas: **browser automation** (the most mature, led by Microsoft's Playwright MCP), **Windows desktop control** (system-level UI interaction), **macOS automation** (AppleScript/JXA-powered scripting), **Linux desktop automation** (newly emerging), **cross-platform desktop tools** (PyAutoGUI-based and Docker-virtualized), and **enterprise RPA integration** (UiPath, Power Apps, and Automation Anywhere).

The headline findings, updated as of this August 2026 audit: **Google's [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) hit [v1.0.0 on May 18, 2026](https://github.com/ChromeDevTools/chrome-devtools-mcp/releases/tag/v1.0.0)** — now 49,175 stars, the most-starred MCP server in the browser automation category and **#3 on [PulseMCP globally](https://www.pulsemcp.com/servers/chrome-devtools)** (1.6 million weekly visitors, 44 million all-time). **Microsoft's [Playwright MCP](https://github.com/microsoft/playwright-mcp) server** — now 36,128 stars — is **#2 on [PulseMCP globally](https://www.pulsemcp.com/servers/microsoft-playwright)** by traffic, with 76.9 million all-time visitors and 5.5 million weekly, still ahead of ChromeDevTools MCP on raw traffic despite the lower star count. v0.0.71–v0.0.75 added drag-and-drop, network response body access, multi-tab Chrome extension management, and **the server is now published to the official MCP Registry on every release**. **[Windows-MCP](https://github.com/CursorTouch/Windows-MCP) hit v0.8.0** (May 19) with a **critical CVE security fix** ([CVE-2026-48989](https://nvd.nist.gov/vuln/detail/CVE-2026-48989) / [GHSA-vrxg-gm77-7q5g](https://github.com/advisories/GHSA-vrxg-gm77-7q5g), v0.7.5) patching HTTP wildcard CORS that allowed unauthenticated cross-origin access to the PowerShell tool; it has since shipped v0.8.5 and now stands at 6,750 stars with 2M+ Claude Desktop Extension users. v0.8.0 added Firefox IAccessible2/MSAA fallback, stateless-http transport, Win32 glow overlay feedback, and Raspberry Pi support. **The Linux gap is closing further** — tine grew to 20 stars (v0.1.0 alpha, GNOME Wayland), GhostDesk to 146 stars (30 tools), and **[isac322/kwin-mcp](https://github.com/isac322/kwin-mcp) (40 stars) brings 30-tool KDE Plasma 6 Wayland automation** — the first KDE-specific desktop MCP server. **[iFurySt/open-browser-use](https://github.com/iFurySt/open-browser-use) (235 stars)** launched as an open-source multi-SDK alternative to Codex's Browser Use capability. **Several community servers have gone dormant, and one has been archived outright** — [BrowserMCP](https://github.com/BrowserMCP/mcp) (no commits since April 2025), [executeautomation/mcp-playwright](https://github.com/executeautomation/mcp-playwright) (dormant since Dec 2025), [joshrutkowski/applescript-mcp](https://github.com/joshrutkowski/applescript-mcp) (dormant since April 2025), and [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase), which Browserbase archived on July 20, 2026 in favor of its hosted MCP endpoint.

## Browser Automation

### microsoft/playwright-mcp (Official — Accessibility-Tree-Driven)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | 36,128 | TypeScript | stdio, SSE, CDP |

**microsoft/playwright-mcp** (36,128 stars) is the official Playwright MCP server from Microsoft and ranks **#2 globally by traffic on [PulseMCP](https://www.pulsemcp.com/servers/microsoft-playwright)** with 76.9 million all-time visitors and 5.5 million weekly. It uses **structured accessibility snapshots** — the same tree of labels, roles, and states that screen readers use — giving LLMs a precise, text-based representation of any web page without vision models.

This approach has three key advantages: **deterministic** (no ambiguity from pixel interpretation), **lightweight** (no vision model needed, so it's fast), and **accessible** (works with any LLM, not just multimodal ones).

Key features: **Multi-browser support** for Chromium, Firefox, and WebKit. **Session persistence** with optional profile storage or isolated contexts. **Browser extension support** — connect to existing browser tabs with logged-in state via CDP. **Code generation** outputting TypeScript Playwright scripts. **Console message capture** and network request/response handling. **Trace recording** for debugging.

Optional capabilities enabled via `--caps` flag: **Vision** (coordinate-based interactions for when accessibility trees aren't sufficient), **PDF** (document generation), and **DevTools** (developer tools integration).

**What's new (April–May 2026):** Five rapid releases in the window. **v0.0.71** (April 27) — new `browser_drop` tool for drag-and-drop operations; `browser_network_requests` gains `responseBody` and `responseHeaders` with binary body handling. **v0.0.72** (April 30) — `browser_network_requests` returns a numbered list; new `browser_network_request` fetches individual request details; `browser_run_code` renamed to `browser_run_code_unsafe` to signal danger. **v0.0.73** (May 1) — **now published to the official MCP Registry on every release** (the authoritative registry for MCP servers); bug fixes for extension channel and executablePath resolution. **v0.0.74** (May 6) — Chrome extension now supports managing multiple tabs; `browser_take_screenshot` skips base64 data when a filename is provided; auto-recovery when remote browser disconnects mid-session. **v0.0.75** (May 7) — bug fix: serialize shared browser launch in `--isolated` mode; fix CDP command forwarding in extension mode.

Notable open issues: #1565 (browser fails to launch after 2-8 days uptime), #1539 (click timeout on resolved elements), #1530 (named session management request), #1466 (GNAP: git-native multi-agent browser coordination).

The accessibility-tree approach has influenced the entire browser automation MCP ecosystem. Its [PulseMCP](https://www.pulsemcp.com/servers/microsoft-playwright) traffic lead (5.5M weekly) remains despite the ChromeDevTools MCP (below) having a higher star count.

### ChromeDevTools/chrome-devtools-mcp (Official Google — CDP-Powered, v1.0.0 GA)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 49,175 | TypeScript | stdio |

**ChromeDevTools/chrome-devtools-mcp** (49,175 stars) is the **official Google Chrome DevTools team's MCP server**, maintained under the ChromeDevTools GitHub organization. It is currently the **most-starred MCP server in the browser automation category** and **[#3 on PulseMCP globally](https://www.pulsemcp.com/servers/chrome-devtools)** (#4 this week) with approximately 1.6 million weekly visitors and 44 million all-time. On May 18, 2026, it **hit [v1.0.0](https://github.com/ChromeDevTools/chrome-devtools-mcp/releases/tag/v1.0.0)** — the first major stable release, signaling production readiness. As of this audit the latest release is v1.7.0 (August 10, 2026).

Where Playwright MCP abstracts the browser through accessibility trees, chrome-devtools-mcp exposes the **Chrome DevTools Protocol (CDP) directly** as MCP tools. This gives agents raw access to the full CDP surface: DOM inspection, network monitoring, JavaScript execution in any frame, performance profiling, storage management, and device emulation — the same APIs used by browser developer tools.

**Five releases shipped in the April–May 2026 window:** v0.23.0 (April 22) through v1.0.1 (May 18). v1.0.0 added navigation URL reporting after page-navigating actions, `filePath` support in `evaluate_script`, improved geolocation emulation, and better error reporting for unknown tool arguments. v1.0.1 followed immediately with stability fixes.

The CDP-native approach means agents can perform operations that accessibility trees don't expose well: intercepting and modifying network requests, reading raw DOM with full attribute access, running arbitrary JavaScript across iframes, and accessing browser internals (cookies, storage, service workers) at the protocol level. This complements rather than replaces Playwright MCP — the two servers suit different use cases.

### BrowserMCP/mcp (Existing Browser Automation)

| Server | Stars | Language | License | Transport |
|--------|-------|----------|---------|-----------|
| [BrowserMCP/mcp](https://github.com/BrowserMCP/mcp) | 6,965 | TypeScript | Apache-2.0 | stdio |

**BrowserMCP/mcp** (6,965 stars, 6 commits) takes a fundamentally different approach from Playwright — instead of launching new browser instances, it automates the **user's existing browser** through a Chrome extension. This means AI agents can work with already logged-in sessions, existing cookies, and real browser fingerprints.

Adapted from Microsoft's Playwright MCP, the key difference is privacy and authentication: browser activity stays local, no credentials need to be passed to the MCP server, and basic bot detection is circumvented by using a real browser profile. Works with VS Code, Claude, Cursor, and Windsurf.

**⚠ Stagnation warning:** The [GitHub repository](https://github.com/BrowserMCP/mcp/commits/main) has had no commits since April 2025 — over a year with zero code activity despite 130+ open issues. The star count continues to grow (6,527→6,965) on reputation alone, but active maintenance has ceased. Consider [Pilot](https://github.com/TacosyHorchata/Pilot) (32 stars, March 2026) as a newer alternative offering the same Chrome extension + real browser approach.

### executeautomation/mcp-playwright (Device Emulation & Testing)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [executeautomation/mcp-playwright](https://github.com/executeautomation/mcp-playwright) | 5,633 | TypeScript | MIT | 20+ |

**executeautomation/mcp-playwright** (5,633 stars, 312 commits) extends browser automation with **143 real device presets** — iPhone, iPad, Pixel, Galaxy, Desktop configurations — complete with automatic user-agent handling, touch event emulation, and device pixel ratio simulation. This makes it particularly valuable for responsive testing and mobile web automation.

Key features: **Test code generation** for creating reusable Playwright test scripts. **Web scraping** capabilities. **Natural language command support** for AI assistants. **Both HTTP and stdio transport** for flexible deployment. **Automatic browser binary installation** on first use. **Cross-platform** support across Windows, macOS, and Linux.

Integration support includes Claude Desktop, VS Code with GitHub Copilot, Cline, and Cursor IDE. The standalone HTTP server mode enables headless server deployments.

**⚠ Dormant since December 2025:** No commits or releases in over 8 months as of this audit. Stars still growing (5,524→5,633) but the project appears unmaintained.

### browserbase/mcp-server-browserbase (Cloud Browser Sessions — Archived)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) | 3,411 | TypeScript | stdio |

**⚠ Archived July 20, 2026:** Browserbase [archived this repository](https://github.com/browserbase/mcp-server-browserbase) — GitHub shows the standard "archived by the owner… now read-only" banner, and the README states it "is archived and no longer maintained. It was originally published as a reference implementation and is retained for historical purposes." Browserbase now directs users to its **hosted MCP endpoint** at `mcp.browserbase.com` instead of self-hosting this server.

**browserbase/mcp-server-browserbase** (3,411 stars, 198 commits, frozen at archival) provided **cloud-hosted browser sessions** via the Browserbase platform and Stagehand, offering enterprise-grade features that local browser automation can't match: **anti-detection** with stealth mode, **proxy support**, **session persistence** across interactions, and **multi-provider LLM compatibility** with OpenAI, Claude, and Gemini.

Performance claims 20-40% faster operations through automatic caching. Supports iframe and shadow DOM traversal, CSS selector-based element targeting, and structured data extraction with schemas. Viewport configuration is customizable for different testing scenarios.

**Final state before archival:** **v3.0.0** (March 31, 2026) was the last release — all tools renamed to shorter names (e.g., `browserbase_session_create` → `start`), package renamed to `@browserbasehq/mcp`, and the hosted MCP endpoint launched (defaults to Gemini 2.5 Flash Lite, configurable). The underlying **[Stagehand](https://github.com/browserbase/stagehand)** automation library (23.9k stars) remains actively developed independent of this repo's archival.

The cloud-hosted approach means no local browser setup, making it suitable for production automation pipelines and CI/CD integration. With the self-hosted server archived, the hosted endpoint (requiring a Browserbase account and API key) is now the only supported path.

### angiejones/mcp-selenium (Selenium WebDriver)

| Server | Stars | Language | License | Transport |
|--------|-------|----------|---------|-----------|
| [angiejones/mcp-selenium](https://github.com/angiejones/mcp-selenium) | 424 | JavaScript | MIT | stdio |

**angiejones/mcp-selenium** (424 stars, 140 commits) brings the Selenium WebDriver ecosystem to MCP, supporting **Chrome, Firefox, Edge, and Safari** (Safari requires macOS setup). This is the go-to server for teams already invested in Selenium infrastructure.

Tools cover the full WebDriver surface: **start_browser**, **navigate**, **interact** (click/doubleclick/rightclick/hover), **send_keys**, **take_screenshot**, **execute_script**, **window** management (tabs/windows), **frame** switching (iframes), **alert** handling (dialogs), **cookie management** (add/get/delete), **upload_file**, and **diagnostics** (console errors, network logs).

Read-only resources expose browser status and accessibility snapshots. The natural language interface lets agents drive browsers without scripting — "Open Chrome, go to github.com, and take a screenshot" becomes a single instruction.

### Other Browser Automation Servers

**modelcontextprotocol/servers (Puppeteer)** — The original reference MCP Puppeteer server from the MCP project itself (now in servers-archived). Provides page navigation, screenshot capture, JavaScript execution, and console monitoring. Available as `@modelcontextprotocol/server-puppeteer` on npm. Superseded by Microsoft's Playwright MCP for most use cases but still widely deployed.

**Playwright Stealth MCP** ([Prakhar-Agarwal-byte/playwright-stealth-mcp](https://github.com/Prakhar-Agarwal-byte/playwright-stealth-mcp)) — Integrates Puppeteer Stealth plugin with Playwright, passing all public automation detection tests. For scenarios where standard browser automation gets blocked.

## Windows Desktop Automation

### CursorTouch/Windows-MCP (Most Adopted)

| Server | Stars | Language | License | Transport |
|--------|-------|----------|---------|-----------|
| [CursorTouch/Windows-MCP](https://github.com/CursorTouch/Windows-MCP) | 6,750 | Python | MIT | stdio |

**CursorTouch/Windows-MCP** (6,750 stars) is the most adopted and most actively developed Windows desktop automation MCP server, providing comprehensive system control with **0.2-0.9 second typical latency** for real-time interaction.

The tool set spans three categories. **Input/Control tools:** Click, Type, Scroll, Move, Shortcut, Wait, MultiSelect, MultiEdit, and Clipboard management. **System tools:** Snapshot (with both vision and DOM modes for different interaction approaches), App (launch/resize/switch applications), Shell (PowerShell command execution), Process (list/terminate running processes), Registry (read/write/delete Windows Registry values). **Web/Data tools:** Scrape (webpage information extraction) and Notification (Windows toast notifications).

Two interaction modes distinguish this server: **Snapshot mode** captures screen state for vision-based interaction, while **DOM mode** (`use_dom=True`) provides structured element trees for browser automation — similar to Playwright's accessibility-tree approach but applied to native Windows UI.

**What's new (April–May 2026):** Three significant releases — **v0.7.4** (April 23): performance fix eliminating double-caching of COM tree nodes (halving COM calls per node), fixed PowerShell Tool missing environment variables, MCP config update for Claude Desktop Windows Store. **v0.7.5** (May 14): **critical security patch for [CVE-2026-48989](https://nvd.nist.gov/vuln/detail/CVE-2026-48989) ([GHSA-vrxg-gm77-7q5g](https://github.com/advisories/GHSA-vrxg-gm77-7q5g), CVSS 8.9 High)** — HTTP transports were emitting `Access-Control-Allow-Origin: *` unconditionally, allowing any cross-origin page to open unauthenticated MCP sessions and invoke the PowerShell tool (remote code execution risk). Fix: no wildcard CORS by default, new `--cors-origins` opt-in flag, DNS rebinding protection via TrustedHostMiddleware. **v0.8.0** (May 19): Firefox IAccessible2/MSAA fallback for DOM extraction (cross-browser accessibility), `--stateless-http` support for streamable-http transport, screenshot capture with Win32 glow overlay feedback, Raspberry Pi integration, Authlib CVE-2026-44681 security patch. The project has since shipped **v0.8.2** (WaitFor condition waits) and **[v0.8.5](https://github.com/CursorTouch/Windows-MCP/releases)** (Aug 1 — protocol/stdout stability, multi-monitor handling), the latest release as of this audit.

The [README](https://github.com/CursorTouch/Windows-MCP/blob/main/README.md) now reports **2M+ users** via Claude Desktop Extensions — the first Windows desktop MCP server to claim that scale (self-reported by the maintainer, not independently audited). The combination of system-level access (registry, processes, shell) with UI automation makes this suitable for both simple click-and-type tasks and complex Windows administration workflows. CursorTouch also maintains **[MacOS-MCP](https://github.com/CursorTouch/MacOS-MCP)** (147 stars) — a lightweight macOS computer use server, extending their cross-platform ambitions.

### mario-andreschak/mcp-windows-desktop-automation (AutoIt-Based)

| Server | Stars | Language | License | Transport |
|--------|-------|----------|---------|-----------|
| [mario-andreschak/mcp-windows-desktop-automation](https://github.com/mario-andreschak/mcp-windows-desktop-automation) | 113 | TypeScript | MIT | stdio, WebSocket |

**mario-andreschak/mcp-windows-desktop-automation** (113 stars, 4 commits) wraps **AutoIt functions** — the venerable Windows automation toolkit — as MCP tools. AutoIt has decades of community automation scripts, and this server makes them accessible to AI agents.

Tool categories: **Mouse operations** (movement, clicking, dragging), **Keyboard functions** (keystroke sending, clipboard management), **Window management** (location, activation, closure, resizing), **UI control interaction** (button clicks, text field manipulation), **Process control** (starting, stopping, monitoring applications), and **System functions** (shutdown, sleep commands).

Also provides resources (file access, screenshot capture) and **prompt templates** for common automation scenarios: window discovery, form completion, repetitive task scripting, and conditional waiting. Supports both stdio and WebSocket transports.

The 4-commit count suggests this is more of a wrapper than a deeply developed project, but the AutoIt foundation provides battle-tested Windows automation primitives.

## macOS Desktop Automation

### steipete/macos-automator-mcp (200+ Recipes)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [steipete/macos-automator-mcp](https://github.com/steipete/macos-automator-mcp) | 869 | TypeScript | stdio |

**steipete/macos-automator-mcp** (869 stars) ships with **over 200 pre-programmed automation sequences** for AppleScript and JavaScript for Automation (JXA), turning AI agents into macOS power users.

Three core tools: **execute_script** runs AppleScript or JXA scripts (inline content, file paths, or knowledge base references), **get_scripting_tips** searches the 200+ recipe knowledge base by category or keyword, and **accessibility_query** provides UI element inspection and interaction via the macOS Accessibility framework.

Supported operations span: application control (Safari, Mail, Finder, Terminal), file system operations (create folders, list files, manage directories), system interactions (notifications, volume control, clipboard management), terminal command execution, browser automation with JavaScript injection, dark mode toggling, and UI element queries with automated clicking.

The knowledge base is extensible — users can add custom recipes at `~/.macos-automator/knowledge_base`. Configurable logging and parsing modes support human-readable, structured, or direct output formats.

### joshrutkowski/applescript-mcp (macOS App Integration)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [joshrutkowski/applescript-mcp](https://github.com/joshrutkowski/applescript-mcp) | 392 | TypeScript | stdio |

**joshrutkowski/applescript-mcp** (392 stars, 40 commits — [dormant since April 2025](https://github.com/joshrutkowski/applescript-mcp/commits/main)) provides structured tools for deep integration with macOS applications, organized by functional category:

**Calendar:** Create events, list daily schedules. **Clipboard:** Copy, retrieve, clear. **Finder:** Get selected files, search with location options, Quick Look preview. **System controls:** Volume adjustment (0-100), active application identification, launch/close applications, dark mode toggle. **Notifications:** Display system notifications, toggle Do Not Disturb. **Terminal (iTerm):** Paste clipboard, execute commands with optional new window. **Shortcuts:** Execute Apple Shortcuts by name, list available shortcuts, pass input to shortcuts. **Mail:** Compose emails, list mailbox emails, search specific emails. **Messages:** List iMessage/SMS conversations, retrieve recent messages, search content, compose and send messages. **Notes:** Create formatted notes (markdown-like and HTML), list by folder, search contents. **Pages:** Create new documents.

The modular architecture and comprehensive macOS app coverage make this the best option for agents that need to interact with native macOS applications rather than just automate mouse/keyboard input.

### antbotlab/mac-use-mcp (Zero-Dependency, 18 Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [antbotlab/mac-use-mcp](https://github.com/antbotlab/mac-use-mcp) | 5 | TypeScript | MIT | 18 |

**antbotlab/mac-use-mcp** (5 stars, 59 commits) takes a minimalist approach — **18 tools with zero native dependencies**, using a pre-compiled Swift binary for macOS 13+ on both Intel and Apple Silicon.

Tools organized into four groups: **Screen** (screenshot with PNG/JPEG and region/window targeting, get_screen_info, get_cursor_position), **Input** (click with button/count/modifiers, move_mouse, scroll, drag with duration control, type_text with Unicode/emoji, press_key for combinations), **Window/Application** (list_windows, focus_window, open_application with fuzzy matching, click_menu for menu bar navigation), and **Accessibility/System** (get_ui_elements via Accessibility API, clipboard_read/write, wait, check_permissions).

Requires only two macOS permissions: Accessibility and Screen Recording. The zero-dependency design (`npx mac-use-mcp`) makes it the easiest macOS desktop MCP server to deploy.

## Linux Desktop Automation (NEW)

The Linux desktop gap — flagged in our original review as "conspicuously absent" — is now being actively addressed across all three major desktop environments: GNOME, KDE, and Docker-virtualized.

### GhostDesk (Docker Virtual Linux Desktop)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [YV17labs/GhostDesk](https://github.com/YV17labs/GhostDesk) | 146 | Python | stdio |

**YV17labs/GhostDesk** (146 stars, 247 commits) provides a **full virtual Linux desktop inside Docker** for AI agents. Now with 30 tools covering screenshots (WebP/PNG), mouse control, keyboard input, UI reading, clipboard, application launch and monitoring. Human-like input patterns help bypass bot detection. Supports self-hosted models (Qwen family) and frontier LLMs.

The Docker isolation is both a strength (sandboxed, reproducible, no risk to host) and a limitation (can't interact with the user's actual desktop). Best suited for automated workflows, testing, and agent research rather than personal desktop automation.

### smythp/tine (GNOME Wayland)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [smythp/tine](https://github.com/smythp/tine) | 20 | Python | stdio |

**smythp/tine** (20 stars, v0.1.0 alpha) is a dedicated **GNOME Wayland** desktop automation server for AI agents. Three reading modes: AT-SPI2 accessibility tree, labeled coordinate grid overlay, optional OCR. Uses kernel-level event injection via `/dev/uinput` (no Wayland portals required). Post-click tree hashing detects "silent misses." Tested on GNOME 49 / Arch Linux.

### isac322/kwin-mcp (KDE Plasma 6 Wayland)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [isac322/kwin-mcp](https://github.com/isac322/kwin-mcp) | 40 | — | stdio |

**isac322/kwin-mcp** (40 stars, created February 2026) is the **first KDE-specific desktop MCP server** — a significant gap filler given KDE Plasma's substantial Linux market share. Provides **30 tools** for KDE Plasma 6 Wayland desktop automation. This, combined with tine (GNOME) and GhostDesk (Docker), means the major Linux desktop environments now all have MCP coverage.

### Other Linux Servers

**[asattelmaier/gnome-ui-mcp](https://github.com/asattelmaier/gnome-ui-mcp)** (1 star, first listed May 14, 2026) — GNOME Wayland automation via AT-SPI element discovery and Mutter remote desktop input. Listed on PulseMCP.

**[kurojs/wayland-mcp](https://github.com/kurojs/wayland-mcp)** (6 stars, first listed May 15, 2026) — Wayland-native MCP server.

**[nordbyte/PeekabooX](https://github.com/nordbyte/PeekabooX)** (9 stars, first listed May 18, 2026) — Linux AI operator toolkit with screen capture and accessibility tree access.

**[vito1317/linux-control-mcp](https://github.com/vito1317/linux-control-mcp)** (0 stars, April 2026) — X11-based Linux desktop control (mouse, keyboard, window, accessibility, screenshot, animations).

## Cross-Platform Desktop Automation

### AB498/computer-control-mcp (PyAutoGUI + OCR)

| Server | Stars | Language | License | Transport |
|--------|-------|----------|---------|-----------|
| [AB498/computer-control-mcp](https://github.com/AB498/computer-control-mcp) | 158 | Python | MIT | stdio |

**AB498/computer-control-mcp** (158 stars, 7 commits) combines **PyAutoGUI** for input automation with **RapidOCR** and **ONNXRuntime** for on-screen text recognition — described as "Similar to 'computer-use' by Anthropic, with zero external dependencies."

Tools: **Mouse** (click_screen, move_mouse, drag_mouse, mouse_down, mouse_up), **Keyboard** (type_text, press_key, key_down, key_up, press_keys), **Screen/Window** (take_screenshot, take_screenshot_with_ocr, get_screen_size, list_windows, activate_window, wait_milliseconds).

The OCR capability is the differentiator — `take_screenshot_with_ocr` captures the screen and extracts text in one operation, letting agents "read" what's on screen without requiring a vision model. GPU-accelerated window capture is available on Windows via the Windows Graphics Capture API with application-specific pattern matching.

Works on Windows, macOS, and Linux — one of the few cross-platform desktop automation MCP servers.

### manushi4/Screenhand (88 Tools — Native Accessibility + Browser + Anti-Detection)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [manushi4/Screenhand](https://github.com/manushi4/Screenhand) | 11 | TypeScript | AGPL-3.0 | 88 |

**manushi4/Screenhand** (11 stars, 134 commits) is the most feature-dense desktop automation MCP server we found, with **88 tools** spanning vision, input, native app control, browser automation, anti-detection, smart execution, and platform playbooks.

**Vision & Input** (3 tools): screenshot, screenshot_file, ocr. **App Control** (9 tools): apps, windows, focus, launch, ui_tree, ui_find, ui_press, ui_set_value, menu_click. **Keyboard & Mouse** (6 tools): click, click_text, type_text, key, drag, scroll. **Browser Control** (9 tools): browser_tabs, browser_open, browser_navigate, browser_js, browser_dom, browser_click, browser_type, browser_wait, browser_page_info. **Anti-Detection** (3 tools): browser_stealth, browser_fill_form, browser_human_click. **Smart Execution** (8 tools): execution_plan, click_with_fallback, type_with_fallback, read_with_fallback, locate_with_fallback, select_with_fallback, scroll_with_fallback, wait_for_state. **Platform Playbooks** (6 tools): platform_guide, playbook_preflight, playbook_record, export_playbook, platform_explore, platform_learn.

Uses native Accessibility APIs (macOS) and UI Automation (Windows) rather than pixel-based approaches. Chrome DevTools Protocol for browser control. Performance claims ~50ms for native UI actions and ~10ms for Chrome browser operations.

Also ships 13 Claude Code skills (automate-app, post-social, run-campaign, edit-video, design-figma) and 5 specialized agents (marketing, design, QA, scraper, orchestrator). The AGPL-3.0 license may limit commercial use.

### lksrz/mcp-desktop-pro (Multi-Action Chaining)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [lksrz/mcp-desktop-pro](https://github.com/lksrz/mcp-desktop-pro) | 6 | JavaScript | stdio |

**lksrz/mcp-desktop-pro** (6 stars, 49 commits) — a fork of tanob/mcp-desktop-automation — focuses on **multi-action chaining** with timing and error handling. The `multiple_desktop_actions` tool lets agents sequence mouse moves, clicks, and keyboard inputs with inter-action delays and configurable error handling.

Key technical decisions: **aggressive image compression** (50% scaling, WebP quality 15, max 300KB) to keep screenshot payloads within LLM context limits. **Window-relative coordinate transformation** for precise UI targeting. **Retina display automatic scaling** for macOS. **Visual debugging** with cursor position overlay on screenshots.

### Other Cross-Platform Servers

**[hetaoBackend/mcp-pyautogui-server](https://github.com/hetaoBackend/mcp-pyautogui-server)** (46 stars, Python, MIT) — PyAutoGUI wrapper with Docker support, cross-platform mouse/keyboard/screenshot/image-location capabilities. **[hathibelagal-dev/mcp-pyautogui](https://github.com/hathibelagal-dev/mcp-pyautogui)** (20 stars) — Another PyAutoGUI MCP server implementation. **[tanob/mcp-desktop-automation](https://github.com/tanob/mcp-desktop-automation)** (33 stars) — RobotJS-based server (Node.js), the parent project of mcp-desktop-pro.

### New Entrants (March–April 2026)

**[Touchpoint-Labs/Touchpoint](https://github.com/Touchpoint-Labs/Touchpoint)** (44 stars, March 2026) — Cross-platform accessibility API with MCP server. Gives agents "eyes and hands" on any desktop via accessibility APIs rather than vision.

**[ForrestKim42/llm-app-exploration](https://github.com/ForrestKim42/llm-app-exploration)** (23 stars, April 2026) — Accessibility-first pattern for LLM agents to explore and control any app (mobile or desktop) without vision models.

**[dklymentiev/screenbox](https://github.com/dklymentiev/screenbox)** (20 stars, March 2026) — Real virtual desktops for AI agents. MCP-native, self-hosted, fully isolated.

**[RavaniRoshan/winscript-mcp](https://github.com/RavaniRoshan/winscript-mcp)** (8 stars, April 2026, "WinScript MCP") — Windows-native automation API as MCP server. **59 tools** for UI control, Office integration, and workflow recording. Bills itself as "AppleScript for Windows."

**[anomalous3/ahk-mcp](https://github.com/anomalous3/ahk-mcp)** (8 stars, April 2026) — AutoHotkey v2 + UI Automation as token-efficient computer use for AI agents.

**[anaisbetts/mcp-computer-use](https://github.com/anaisbetts/mcp-computer-use)** (15 stars, April 2026) — MCP server implementing the OpenAI CUA (Computer-Using Agent) spec for desktop. Written in Rust. Cross-platform: Windows Capture, libwayshot for Linux/Wayland, ScreenCaptureKit for macOS 14+. Action schemas match the CUA spec exactly (click, double-click, scroll, type, wait, keypress, drag, screenshot).

**[iFurySt/open-browser-use](https://github.com/iFurySt/open-browser-use)** (235 stars, April 24, 2026) — Open-source multi-SDK alternative to Codex's Browser Use feature. Available as JS/TS SDK, Python SDK, Go SDK, CLI, and MCP server. Platform-neutral browser automation. v0.1.39 (May 17, 2026) at last check. Describes itself as "open-source alternative to the Chrome Browser Use capability recently shipped in Codex.app."

**[VersoXBT/desktop-pilot-mcp](https://github.com/VersoXBT/desktop-pilot-mcp)** (10 stars, April 2026) — macOS app automation via Accessibility API, AppleScript, CGEvent. Claims 30-100x faster than screenshot-based computer use (vendor claim, not independently benchmarked by this review).

**[TacosyHorchata/Pilot](https://github.com/TacosyHorchata/Pilot)** (32 stars, March 2026) — Chrome extension + MCP server for AI agents to control a tab in the user's real browser with existing sessions and logins. A newer alternative to BrowserMCP.

## Enterprise RPA

### UiPath MCP Platform Integration

UiPath has taken the most comprehensive enterprise approach to MCP, integrating it directly into the **UiPath Orchestrator** platform rather than offering a standalone MCP server:

**Three server types:** **UiPath servers** expose UiPath artifacts (automations, processes, queues) as MCP tools. **Coded servers** (Preview) let developers build custom Python MCP servers and deploy them to Orchestrator as packages. **Command servers** (Preview) import existing MCP servers from npm or PyPI package feeds.

**[UiPath/uipath-mcp-python](https://github.com/UiPath/uipath-mcp-python)** (11 stars, Python, MIT, 306 commits) — The official SDK for building coded MCP servers. Provides CLI tools for authentication, project initialization, debugging, packaging (.nupkg), and publishing to Orchestrator. Can also host binary servers written in Go.

**What's new:** **v0.2.0** (April 3, 2026) added **Streamable HTTP transport** for MCP servers and bumped minimum dependency versions (uipath≥2.10.40, uipath-runtime≥0.10.0).

This platform approach means any existing MCP server can be brought into UiPath's enterprise automation framework — with all the governance, scheduling, credential management, and audit logging that UiPath provides. It also means UiPath automations themselves become available as MCP tools for AI agents.

The blog post "[The universal connector: how MCP lets any agent master any system](https://www.uipath.com/blog/product-and-updates/model-context-protocol-mcp-universal-connector)" positions MCP as a bridge between AI agents and UiPath's [pre-built connector catalog](https://docs.uipath.com/integration-service/automation-cloud/latest/user-guide/introduction) (UiPath's own docs describe it as "a large and growing catalog" without publishing an exact count).

### Automation Anywhere (NEW — Limited MCP Support)

Automation Anywhere can now expose automations as an MCP server for external clients (Copilot Studio, Claude). However, **AI Agent Studio cannot yet act as an MCP client** — an Automation Anywhere team member [confirmed in the company's own community forum on March 10, 2026](https://community.automationanywhere.com/developers-forum-36/can-ai-agent-studio-connect-to-external-custom-mcp-servers-as-a-client-91236) that this "is not currently implemented," suggesting REST web service calls from a custom automation as a workaround. Community-built servers exist ([VankProgrammingAndDesign/aa-mcp-server](https://github.com/VankProgrammingAndDesign/aa-mcp-server)) but have zero stars.

This puts Automation Anywhere significantly behind UiPath on MCP adoption. The one-way support (MCP server only, no client) limits the integration story.

### Microsoft Power Platform (NEW — Public Preview)

**[Power Apps MCP Server](https://www.microsoft.com/en-us/power-platform/blog/power-apps/public-preview-power-apps-mcp-and-enhanced-agent-feed-for-your-business-applications/)** entered **public preview on February 11, 2026**, per Microsoft's own Power Platform blog, letting agents automate repetitive app tasks with human review and approval through a task-centric "enhanced agent feed." This is Microsoft's entry into the RPA-meets-MCP space — significant given that Microsoft also builds the most popular browser automation MCP server (Playwright).

Power Automate does not have an official first-party MCP server yet, but community alternatives exist ([Cliveo/Power-Platform-MCP](https://github.com/Cliveo/Power-Platform-MCP), 7 stars, for Dataverse + Power Automate integration).

## Gaps and missing pieces

**Linux desktop still maturing** — tine (GNOME), kwin-mcp (KDE), and GhostDesk (Docker) now cover all three major Linux desktop configurations. Coverage has improved significantly from "conspicuously absent" to multi-environment. xdotool (X11) and ydotool (Wayland) remain unwrapped as dedicated MCP servers, but the practical gaps are smaller.

**Dormant or discontinued community servers** — BrowserMCP (6,965 stars, no commits since April 2025), executeautomation/mcp-playwright (5,633 stars, dormant since Dec 2025), and joshrutkowski/applescript-mcp (392 stars, dormant since April 2025) have large star counts but no maintenance. browserbase/mcp-server-browserbase goes further: Browserbase [archived it outright on July 20, 2026](https://github.com/browserbase/mcp-server-browserbase), pushing users to its hosted endpoint instead. Users relying on these servers may face unpatched issues.

**Limited safety controls** — most desktop automation servers offer unrestricted access to mouse, keyboard, and system commands. Only a few provide read-only modes or permission boundaries. Playwright added file system restrictions and origin controls by default, but desktop automation servers generally lag on security.

**No cross-platform desktop abstraction** — each platform (Windows, macOS, Linux) has separate servers with different tool sets and capabilities. CursorTouch is expanding cross-platform (Windows-MCP + MacOS-MCP) but they're still separate tools.

**Fragmented browser automation** — Playwright, Selenium, Puppeteer, and CDP-based approaches all have MCP servers, but choosing between them requires understanding the trade-offs (accessibility trees vs screenshots, local vs cloud, existing sessions vs new instances).

**Power Automate still missing official MCP** — Microsoft's own RPA platform lacks first-party MCP integration, despite Microsoft building the most popular browser automation MCP server (Playwright) and Power Apps MCP entering public preview.

**Virtual desktop support emerging** — GhostDesk and screenbox provide Docker-based virtual desktops, but VNC/RDP-based remote session automation via MCP is still absent.

## Bottom line

**Rating: 4.5 / 5** — Desktop automation and browser control has reached a new level of maturity. The browser automation subcategory now has **two official servers from major tech companies** hitting major milestones: Google's ChromeDevTools/chrome-devtools-mcp (49,175 stars, v1.0.0 GA May 18, #3 on PulseMCP) and Microsoft's Playwright MCP (36,128 stars, #2 on PulseMCP globally, 76.9M all-time visitors, now in the official MCP Registry). These two servers take complementary approaches — accessibility trees vs. CDP — and together provide comprehensive browser automation coverage. Windows-MCP (6,750 stars, v0.8.5, 2M+ users) is actively patching security CVEs and shipping major features. Linux desktop support now spans GNOME (tine), KDE (kwin-mcp), and Docker-virtualized (GhostDesk) environments.

Deductions: several high-profile community servers remain dormant (BrowserMCP and executeautomation — combined 12,500+ stars with no maintenance) and Browserbase's self-hosted server was archived outright, limited safety controls across most desktop automation servers (Windows-MCP just patched a severe CORS CVE, highlighting the risk), Power Automate still missing official MCP, and no true cross-platform desktop abstraction exists.

## Further Reading

- [Holo3: How a 10B-Parameter Open Model Beat GPT-5.4 and Opus 4.6 at Controlling Desktops](/guides/holo3-desktop-agent-osworld-record/) — H Company's open-source model scores 78.85% on OSWorld, offering a visual understanding approach to desktop automation that complements MCP tool-calling

*This review reflects research conducted in March–May 2026, with a claim-level citation re-audit and stats refresh in August 2026. Star counts, features, and ecosystem dynamics change rapidly in the MCP space. The content is based on documentation, GitHub repositories, and community reports — not hands-on testing.*

**Category**: [Business & Productivity](/categories/business-productivity/)

*This review was last edited on 2026-08-14 using Claude Sonnet 5 (Anthropic).*

