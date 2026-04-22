---
title: "Desktop Automation & Browser Control MCP Servers — Playwright, Selenium, Windows-MCP, macOS Automator, and More"
date: 2026-03-15T09:45:00+09:00
description: "Desktop automation and browser control MCP servers give AI agents eyes and hands — the ability to see screens, click buttons, type text, and control applications through the Model Context Protocol."
og_description: "Desktop Automation & Browser Control MCP servers: microsoft/playwright-mcp (31,200 stars, TypeScript, official, accessibility-tree web interaction without vision models, multi-browser, PulseMCP #1 globally with 42.4M all-time visitors), CursorTouch/Windows-MCP (5,260 stars, Python, MIT, v0.7.1, +203 commits, DXCam screenshot backend, MSIX/UWP app launch), BrowserMCP/mcp (6,377 stars, TypeScript, Apache-2.0, Chrome extension for existing browser sessions — stagnant, no commits in 1 year), executeautomation/mcp-playwright (5,455 stars, TypeScript, MIT, 143 device presets — dormant since Dec 2025), browserbase/mcp-server-browserbase (3,277 stars, TypeScript, v3.0.0 breaking tool rename, hosted MCP at mcp.browserbase.com), NEW: GhostDesk (44 stars, Docker virtual Linux desktop for AI agents, 25+ tools), NEW: tine (10 stars, first GNOME Wayland desktop automation MCP), NEW: WinScript MCP (9 stars, 59 tools, Windows-native AppleScript equivalent), NEW: Pilot (31 stars, Chrome extension + MCP for real browser control), Power Apps MCP Server public preview (1,100+ enterprise systems), Automation Anywhere limited MCP support. Linux gap partially closing. 40+ servers reviewed. Rating: 4.0/5."
content_type: "Review"
card_description: "Desktop automation and browser control MCP servers across browser automation frameworks, Windows desktop control, macOS scripting, cross-platform tools, and enterprise RPA. Browser automation is the most mature subcategory — Microsoft's official Playwright MCP server (31,200 stars, PulseMCP #1 globally with 42.4M all-time visitors) continues to define accessibility-tree-driven web interaction for LLMs. The server hit v0.0.70 with Playwright 1.59 adding browser.bind() for shared browser instances and page.screencast for annotated video receipts. A Chrome Web Store extension 'Playwright MCP Bridge' now available. ExecuteAutomation's community Playwright server (5,455 stars) appears dormant since Dec 2025. BrowserMCP (6,377 stars) has had no commits in over a year — stagnant. Browserbase (3,277 stars) shipped v3.0.0 with breaking tool name changes and a hosted MCP endpoint at mcp.browserbase.com. New browser entrant Pilot (31 stars) offers Chrome extension + MCP for real browser control with logged-in sessions. Windows desktop automation is led by CursorTouch/Windows-MCP (5,260 stars, +203 commits since March) — the most actively developed server in this category, now at v0.7.1 with DXCam screenshot backend, MSIX/UWP app launch support, and UIAutomation hang fixes. New entrant WinScript MCP (9 stars, 59 tools) bills itself as 'AppleScript for Windows.' macOS has the richest scripting ecosystem — steipete/macos-automator-mcp (762 stars) ships 200+ recipes, CursorTouch launched MacOS-MCP (18 stars) for lightweight computer use, and desktop-pilot-mcp claims 30-100x faster than screenshot-based approaches. The Linux gap is finally closing — GhostDesk (44 stars) provides a full virtual Linux desktop in Docker for AI agents (25+ tools), tine (10 stars) is the first GNOME Wayland desktop automation MCP server using AT-SPI2, and gnome-ui-mcp brings Mutter remote desktop input. Enterprise RPA expanded — UiPath's official SDK shipped v0.2.0 with Streamable HTTP transport, Power Apps MCP Server entered public preview connecting to 1,100+ enterprise systems, and Automation Anywhere added limited MCP server capability. OpenAI Codex shipped desktop computer use (April 16) with broad MCP support. The category holds at 4.0/5 — browser automation is dominant with Playwright MCP as the undisputed #1 globally, Windows-MCP is thriving, the Linux gap is partially closing, and enterprise RPA is expanding. Deductions for dormant community servers (BrowserMCP, executeautomation), still-fragmented browser automation landscape, limited safety controls, and Linux desktop support still thin compared to Windows/macOS."
last_refreshed: 2026-04-22
---

Desktop automation and browser control MCP servers represent a fundamental capability shift — they give AI agents "eyes and hands" to interact with computer interfaces the same way humans do. Instead of calling APIs, these servers let agents see screens, click buttons, fill forms, navigate applications, and execute system commands through the Model Context Protocol.

The landscape spans six areas: **browser automation** (the most mature, led by Microsoft's Playwright MCP), **Windows desktop control** (system-level UI interaction), **macOS automation** (AppleScript/JXA-powered scripting), **Linux desktop automation** (newly emerging), **cross-platform desktop tools** (PyAutoGUI-based and Docker-virtualized), and **enterprise RPA integration** (UiPath, Power Apps, and Automation Anywhere).

The headline findings: **Microsoft's Playwright MCP server is the #1 MCP server globally** — 31,200 stars, 42.4 million PulseMCP visitors all-time, and Playwright 1.59's browser.bind() and page.screencast expand what agents can do. **Windows-MCP is thriving** with 5,260 stars and +203 commits since March, shipping v0.7.1 with DXCam screenshots and UWP app support. **The Linux gap is finally closing** — GhostDesk (44 stars) provides virtual Linux desktops in Docker, tine (10 stars) is the first GNOME Wayland MCP server, and gnome-ui-mcp adds Mutter remote input. **Enterprise RPA is expanding** — UiPath shipped SDK v0.2.0, Power Apps MCP Server entered public preview (1,100+ enterprise systems), and Automation Anywhere added limited MCP support. **OpenAI Codex shipped desktop computer use** (April 16) with MCP support, entering the space as a competitor. **Several community servers have gone dormant** — BrowserMCP (no commits in over a year), executeautomation/mcp-playwright (dormant since Dec 2025), and joshrutkowski/applescript-mcp (dormant since April 2025).

## Browser Automation

### microsoft/playwright-mcp (Official — Accessibility-Tree-Driven)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | 31,200 | TypeScript | stdio, SSE, CDP |

**microsoft/playwright-mcp** (31,200 stars, 527 commits) is the official Playwright MCP server from Microsoft and the **#1 MCP server globally on PulseMCP** with 42.4 million all-time visitors and 2.5 million weekly. It uses **structured accessibility snapshots** — the same tree of labels, roles, and states that screen readers use — giving LLMs a precise, text-based representation of any web page without vision models.

This approach has three key advantages: **deterministic** (no ambiguity from pixel interpretation), **lightweight** (no vision model needed, so it's fast), and **accessible** (works with any LLM, not just multimodal ones).

Key features: **Multi-browser support** for Chromium, Firefox, and WebKit. **Session persistence** with optional profile storage or isolated contexts. **Browser extension support** — connect to existing browser tabs with logged-in state via CDP. **Code generation** outputting TypeScript Playwright scripts. **Console message capture** and network request/response handling. **Trace recording** for debugging.

Optional capabilities enabled via `--caps` flag: **Vision** (coordinate-based interactions for when accessibility trees aren't sufficient), **PDF** (document generation), and **DevTools** (developer tools integration).

**What's new (March–April 2026):** v0.0.70 (April 1) is a maintenance release built from the Playwright 1.59 branch point. v0.0.69 (March 30) added network offline mode toggle, expanded mouse click options (button, count, delay), network request inspection with filtering, plain CSS and text selector support alongside aria-ref handles, and a **Chrome Web Store extension** ("Playwright MCP Bridge"). Playwright 1.59 itself added `browser.bind()` for sharing one browser across MCP/CLI/clients and `page.screencast` for annotated video receipts with action highlights and chapter titles. A new **token-efficient CLI mode** ("SKILLS") was added, favored by coding agents. File system restrictions and origin controls are now enabled **by default** for security.

Notable open issues: #1565 (browser fails to launch after 2-8 days uptime), #1539 (click timeout on resolved elements), #1530 (named session management request), #1466 (GNAP: git-native multi-agent browser coordination).

The 31,200-star count makes this the most-starred MCP server in any category. Its accessibility-tree approach has influenced the entire browser automation MCP ecosystem.

### BrowserMCP/mcp (Existing Browser Automation)

| Server | Stars | Language | License | Transport |
|--------|-------|----------|---------|-----------|
| [BrowserMCP/mcp](https://github.com/BrowserMCP/mcp) | 6,377 | TypeScript | Apache-2.0 | stdio |

**BrowserMCP/mcp** (6,377 stars, 6 commits) takes a fundamentally different approach from Playwright — instead of launching new browser instances, it automates the **user's existing browser** through a Chrome extension. This means AI agents can work with already logged-in sessions, existing cookies, and real browser fingerprints.

Adapted from Microsoft's Playwright MCP, the key difference is privacy and authentication: browser activity stays local, no credentials need to be passed to the MCP server, and basic bot detection is circumvented by using a real browser profile. Works with VS Code, Claude, Cursor, and Windsurf.

**⚠ Stagnation warning:** The GitHub repository has had no commits since April 2024 — over two years with zero code activity despite 130+ open issues. The star count continues to grow (6,100→6,377) on reputation alone, but active maintenance has ceased. Consider [Pilot](https://github.com/TacosyHorchata/Pilot) (31 stars, March 2026) as a newer alternative offering the same Chrome extension + real browser approach.

### executeautomation/mcp-playwright (Device Emulation & Testing)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [executeautomation/mcp-playwright](https://github.com/executeautomation/mcp-playwright) | 5,455 | TypeScript | MIT | 20+ |

**executeautomation/mcp-playwright** (5,455 stars, 312 commits) extends browser automation with **143 real device presets** — iPhone, iPad, Pixel, Galaxy, Desktop configurations — complete with automatic user-agent handling, touch event emulation, and device pixel ratio simulation. This makes it particularly valuable for responsive testing and mobile web automation.

Key features: **Test code generation** for creating reusable Playwright test scripts. **Web scraping** capabilities. **Natural language command support** for AI assistants. **Both HTTP and stdio transport** for flexible deployment. **Automatic browser binary installation** on first use. **Cross-platform** support across Windows, macOS, and Linux.

Integration support includes Claude Desktop, VS Code with GitHub Copilot, Cline, and Cursor IDE. The standalone HTTP server mode enables headless server deployments.

**⚠ Dormant since December 2025:** No commits or releases in over 4 months. Stars still growing (5,300→5,455) but the project appears unmaintained.

### browserbase/mcp-server-browserbase (Cloud Browser Sessions)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) | 3,277 | TypeScript | stdio |

**browserbase/mcp-server-browserbase** (3,277 stars, 198 commits) provides **cloud-hosted browser sessions** via the Browserbase platform and Stagehand, offering enterprise-grade features that local browser automation can't match: **anti-detection** with stealth mode, **proxy support**, **session persistence** across interactions, and **multi-provider LLM compatibility** with OpenAI, Claude, and Gemini.

Performance claims 20-40% faster operations through automatic caching. Supports iframe and shadow DOM traversal, CSS selector-based element targeting, and structured data extraction with schemas. Viewport configuration is customizable for different testing scenarios.

**What's new:** **v3.0.0** (March 31, 2026) is a **breaking release** — all tools renamed to shorter names (e.g., `browserbase_session_create` → `start`), package renamed to `@browserbasehq/mcp`, and a **hosted MCP endpoint** launched at mcp.browserbase.com for remote access without local installation.

The cloud-hosted approach means no local browser setup, making it suitable for production automation pipelines and CI/CD integration. The trade-off is requiring a Browserbase account and API key.

### angiejones/mcp-selenium (Selenium WebDriver)

| Server | Stars | Language | License | Transport |
|--------|-------|----------|---------|-----------|
| [angiejones/mcp-selenium](https://github.com/angiejones/mcp-selenium) | 389 | JavaScript | MIT | stdio |

**angiejones/mcp-selenium** (389 stars, 140 commits) brings the Selenium WebDriver ecosystem to MCP, supporting **Chrome, Firefox, Edge, and Safari** (Safari requires macOS setup). This is the go-to server for teams already invested in Selenium infrastructure.

Tools cover the full WebDriver surface: **start_browser**, **navigate**, **interact** (click/doubleclick/rightclick/hover), **send_keys**, **take_screenshot**, **execute_script**, **window** management (tabs/windows), **frame** switching (iframes), **alert** handling (dialogs), **cookie management** (add/get/delete), **upload_file**, and **diagnostics** (console errors, network logs).

Read-only resources expose browser status and accessibility snapshots. The natural language interface lets agents drive browsers without scripting — "Open Chrome, go to github.com, and take a screenshot" becomes a single instruction.

### Other Browser Automation Servers

**modelcontextprotocol/servers (Puppeteer)** — The original reference MCP Puppeteer server from the MCP project itself (now in servers-archived). Provides page navigation, screenshot capture, JavaScript execution, and console monitoring. Available as `@modelcontextprotocol/server-puppeteer` on npm. Superseded by Microsoft's Playwright MCP for most use cases but still widely deployed.

**Playwright Stealth MCP** ([Prakhar-Agarwal-byte/playwright-stealth-mcp](https://github.com/Prakhar-Agarwal-byte/playwright-stealth-mcp)) — Integrates Puppeteer Stealth plugin with Playwright, passing all public automation detection tests. For scenarios where standard browser automation gets blocked.

## Windows Desktop Automation

### CursorTouch/Windows-MCP (Most Adopted)

| Server | Stars | Language | License | Transport |
|--------|-------|----------|---------|-----------|
| [CursorTouch/Windows-MCP](https://github.com/CursorTouch/Windows-MCP) | 5,260 | Python | MIT | stdio |

**CursorTouch/Windows-MCP** (5,260 stars, 469 commits) is the most adopted and most actively developed Windows desktop automation MCP server, providing comprehensive system control with **0.2-0.9 second typical latency** for real-time interaction.

The tool set spans three categories. **Input/Control tools:** Click, Type, Scroll, Move, Shortcut, Wait, MultiSelect, MultiEdit, and Clipboard management. **System tools:** Snapshot (with both vision and DOM modes for different interaction approaches), App (launch/resize/switch applications), Shell (PowerShell command execution), Process (list/terminate running processes), Registry (read/write/delete Windows Registry values). **Web/Data tools:** Scrape (webpage information extraction) and Notification (Windows toast notifications).

Two interaction modes distinguish this server: **Snapshot mode** captures screen state for vision-based interaction, while **DOM mode** (`use_dom=True`) provides structured element trees for browser automation — similar to Playwright's accessibility-tree approach but applied to native Windows UI.

**What's new (March–April 2026):** Three releases in rapid succession — v0.7.1 (March 29), v0.7.0 (March 17), v0.6.9 (March 13). **+203 commits** since our last review, making this the most actively developed server in the category. New features include: **DXCam screenshot backend** for faster screen capture, **MSIX/UWP app launch support**, PowerShell executor refactor, UIAutomation hang fix, keyboard focus fix on window switching, Dependabot integration for security, and configurable screenshot scaling via environment variable.

The combination of system-level access (registry, processes, shell) with UI automation makes this suitable for both simple click-and-type tasks and complex Windows administration workflows. CursorTouch also launched **[MacOS-MCP](https://github.com/CursorTouch/MacOS-MCP)** (18 stars) — a lightweight macOS computer use server, extending their cross-platform ambitions.

### mario-andreschak/mcp-windows-desktop-automation (AutoIt-Based)

| Server | Stars | Language | License | Transport |
|--------|-------|----------|---------|-----------|
| [mario-andreschak/mcp-windows-desktop-automation](https://github.com/mario-andreschak/mcp-windows-desktop-automation) | 102 | TypeScript | MIT | stdio, WebSocket |

**mario-andreschak/mcp-windows-desktop-automation** (102 stars, 4 commits) wraps **AutoIt functions** — the venerable Windows automation toolkit — as MCP tools. AutoIt has decades of community automation scripts, and this server makes them accessible to AI agents.

Tool categories: **Mouse operations** (movement, clicking, dragging), **Keyboard functions** (keystroke sending, clipboard management), **Window management** (location, activation, closure, resizing), **UI control interaction** (button clicks, text field manipulation), **Process control** (starting, stopping, monitoring applications), and **System functions** (shutdown, sleep commands).

Also provides resources (file access, screenshot capture) and **prompt templates** for common automation scenarios: window discovery, form completion, repetitive task scripting, and conditional waiting. Supports both stdio and WebSocket transports.

The 4-commit count suggests this is more of a wrapper than a deeply developed project, but the AutoIt foundation provides battle-tested Windows automation primitives.

## macOS Desktop Automation

### steipete/macos-automator-mcp (200+ Recipes)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [steipete/macos-automator-mcp](https://github.com/steipete/macos-automator-mcp) | 762 | TypeScript | stdio |

**steipete/macos-automator-mcp** (762 stars, 101 commits) ships with **over 200 pre-programmed automation sequences** for AppleScript and JavaScript for Automation (JXA), turning AI agents into macOS power users.

Three core tools: **execute_script** runs AppleScript or JXA scripts (inline content, file paths, or knowledge base references), **get_scripting_tips** searches the 200+ recipe knowledge base by category or keyword, and **accessibility_query** provides UI element inspection and interaction via the macOS Accessibility framework.

Supported operations span: application control (Safari, Mail, Finder, Terminal), file system operations (create folders, list files, manage directories), system interactions (notifications, volume control, clipboard management), terminal command execution, browser automation with JavaScript injection, dark mode toggling, and UI element queries with automated clicking.

The knowledge base is extensible — users can add custom recipes at `~/.macos-automator/knowledge_base`. Configurable logging and parsing modes support human-readable, structured, or direct output formats.

### joshrutkowski/applescript-mcp (macOS App Integration)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [joshrutkowski/applescript-mcp](https://github.com/joshrutkowski/applescript-mcp) | 379 | TypeScript | stdio |

**joshrutkowski/applescript-mcp** (379 stars, 40 commits — dormant since April 2025) provides structured tools for deep integration with macOS applications, organized by functional category:

**Calendar:** Create events, list daily schedules. **Clipboard:** Copy, retrieve, clear. **Finder:** Get selected files, search with location options, Quick Look preview. **System controls:** Volume adjustment (0-100), active application identification, launch/close applications, dark mode toggle. **Notifications:** Display system notifications, toggle Do Not Disturb. **Terminal (iTerm):** Paste clipboard, execute commands with optional new window. **Shortcuts:** Execute Apple Shortcuts by name, list available shortcuts, pass input to shortcuts. **Mail:** Compose emails, list mailbox emails, search specific emails. **Messages:** List iMessage/SMS conversations, retrieve recent messages, search content, compose and send messages. **Notes:** Create formatted notes (markdown-like and HTML), list by folder, search contents. **Pages:** Create new documents.

The modular architecture and comprehensive macOS app coverage make this the best option for agents that need to interact with native macOS applications rather than just automate mouse/keyboard input.

### antbotlab/mac-use-mcp (Zero-Dependency, 18 Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [antbotlab/mac-use-mcp](https://github.com/antbotlab/mac-use-mcp) | 1 | TypeScript | MIT | 18 |

**antbotlab/mac-use-mcp** (1 star, 59 commits) takes a minimalist approach — **18 tools with zero native dependencies**, using a pre-compiled Swift binary for macOS 13+ on both Intel and Apple Silicon.

Tools organized into four groups: **Screen** (screenshot with PNG/JPEG and region/window targeting, get_screen_info, get_cursor_position), **Input** (click with button/count/modifiers, move_mouse, scroll, drag with duration control, type_text with Unicode/emoji, press_key for combinations), **Window/Application** (list_windows, focus_window, open_application with fuzzy matching, click_menu for menu bar navigation), and **Accessibility/System** (get_ui_elements via Accessibility API, clipboard_read/write, wait, check_permissions).

Requires only two macOS permissions: Accessibility and Screen Recording. The zero-dependency design (`npx mac-use-mcp`) makes it the easiest macOS desktop MCP server to deploy.

## Linux Desktop Automation (NEW)

The Linux desktop gap — flagged in our original review as "conspicuously absent" — is now being addressed by several new projects.

### GhostDesk (Docker Virtual Linux Desktop)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [YV17labs/GhostDesk](https://github.com/YV17labs/GhostDesk) | 44 | Python | stdio |

**YV17labs/GhostDesk** (44 stars, March 2026) takes a different approach to the Linux desktop problem — instead of wrapping native Linux desktop APIs, it provides a **full virtual Linux desktop inside Docker** for AI agents. 25+ tools cover screenshots, mouse control, keyboard input, UI reading, clipboard, and shell access. Human-like input patterns help bypass bot detection. Works with any MCP client.

The Docker isolation is both a strength (sandboxed, reproducible, no risk to host) and a limitation (can't interact with the user's actual desktop). Best suited for automated workflows, testing, and agent research rather than personal desktop automation.

### smythp/tine (GNOME Wayland — First Native Linux MCP)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [smythp/tine](https://github.com/smythp/tine) | 10 | Python | stdio |

**smythp/tine** (10 stars, April 2026) is the first dedicated **GNOME Wayland** desktop automation MCP server. CLI-first, using AT-SPI2 (Assistive Technology Service Provider Interface) for accessibility-based UI interaction — no portals, no consent dialogs. This is the Linux equivalent of macOS Accessibility API access.

### Other Linux Servers

**asattelmaier/gnome-ui-mcp** (1 star, March 2026) — GNOME Wayland automation via AT-SPI element discovery and Mutter remote desktop input. Listed on PulseMCP.

**vito1317/linux-control-mcp** (0 stars, April 2026) — X11-based Linux desktop control (mouse, keyboard, window, accessibility, screenshot, animations).

## Cross-Platform Desktop Automation

### AB498/computer-control-mcp (PyAutoGUI + OCR)

| Server | Stars | Language | License | Transport |
|--------|-------|----------|---------|-----------|
| [AB498/computer-control-mcp](https://github.com/AB498/computer-control-mcp) | 137 | Python | MIT | stdio |

**AB498/computer-control-mcp** (137 stars, 7 commits) combines **PyAutoGUI** for input automation with **RapidOCR** and **ONNXRuntime** for on-screen text recognition — described as "Similar to 'computer-use' by Anthropic, with zero external dependencies."

Tools: **Mouse** (click_screen, move_mouse, drag_mouse, mouse_down, mouse_up), **Keyboard** (type_text, press_key, key_down, key_up, press_keys), **Screen/Window** (take_screenshot, take_screenshot_with_ocr, get_screen_size, list_windows, activate_window, wait_milliseconds).

The OCR capability is the differentiator — `take_screenshot_with_ocr` captures the screen and extracts text in one operation, letting agents "read" what's on screen without requiring a vision model. GPU-accelerated window capture is available on Windows via the Windows Graphics Capture API with application-specific pattern matching.

Works on Windows, macOS, and Linux — one of the few cross-platform desktop automation MCP servers.

### manushi4/Screenhand (88 Tools — Native Accessibility + Browser + Anti-Detection)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [manushi4/Screenhand](https://github.com/manushi4/Screenhand) | 2 | TypeScript | AGPL-3.0 | 88 |

**manushi4/Screenhand** (2 stars, 134 commits) is the most feature-dense desktop automation MCP server we found, with **88 tools** spanning vision, input, native app control, browser automation, anti-detection, smart execution, and platform playbooks.

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

**hetaoBackend/mcp-pyautogui-server** (41 stars, Python, MIT) — PyAutoGUI wrapper with Docker support, cross-platform mouse/keyboard/screenshot/image-location capabilities. **hathibelagal-dev/mcp-pyautogui** — Another PyAutoGUI MCP server implementation. **tanob/mcp-desktop-automation** — RobotJS-based server (Node.js), the parent project of mcp-desktop-pro.

### New Entrants (March–April 2026)

**Touchpoint-Labs/Touchpoint** (28 stars, March 2026) — Cross-platform accessibility API with MCP server. Gives agents "eyes and hands" on any desktop via accessibility APIs rather than vision.

**ForrestKim42/llm-app-exploration** (23 stars, April 2026) — Accessibility-first pattern for LLM agents to explore and control any app (mobile or desktop) without vision models.

**dklymentiev/screenbox** (17 stars, March 2026) — Real virtual desktops for AI agents. MCP-native, self-hosted, fully isolated.

**RavaniRoshan/winscript-mcp** (9 stars, April 2026, "WinScript MCP") — Windows-native automation API as MCP server. **59 tools** for UI control, Office integration, and workflow recording. Bills itself as "AppleScript for Windows." ~1.8K weekly visitors on PulseMCP.

**anomalous3/ahk-mcp** (6 stars, April 2026) — AutoHotkey v2 + UI Automation as token-efficient computer use for AI agents.

**anaisbetts/mcp-computer-use** (9 stars, April 2026) — MCP server implementing OpenAI CUA (Computer-Using Agent) for desktop. Written in Rust.

**VersoXBT/desktop-pilot-mcp** (8 stars, April 2026) — macOS app automation via Accessibility API, AppleScript, CGEvent. Claims 30-100x faster than screenshot-based computer use.

**TacosyHorchata/Pilot** (31 stars, March 2026) — Chrome extension + MCP server for AI agents to control a tab in the user's real browser with existing sessions and logins. A newer, actively maintained alternative to BrowserMCP.

## Enterprise RPA

### UiPath MCP Platform Integration

UiPath has taken the most comprehensive enterprise approach to MCP, integrating it directly into the **UiPath Orchestrator** platform rather than offering a standalone MCP server:

**Three server types:** **UiPath servers** expose UiPath artifacts (automations, processes, queues) as MCP tools. **Coded servers** (Preview) let developers build custom Python MCP servers and deploy them to Orchestrator as packages. **Command servers** (Preview) import existing MCP servers from npm or PyPI package feeds.

**UiPath/uipath-mcp-python** (8 stars, Python, MIT, 306 commits) — The official SDK for building coded MCP servers. Provides CLI tools for authentication, project initialization, debugging, packaging (.nupkg), and publishing to Orchestrator. Can also host binary servers written in Go.

**What's new:** **v0.2.0** (April 3, 2026) added **Streamable HTTP transport** for MCP servers and bumped minimum dependency versions (uipath≥2.10.40, uipath-runtime≥0.10.0). Active development — last updated April 21.

This platform approach means any existing MCP server can be brought into UiPath's enterprise automation framework — with all the governance, scheduling, credential management, and audit logging that UiPath provides. It also means UiPath automations themselves become available as MCP tools for AI agents.

The blog post "[The universal connector: how MCP lets any agent master any system](https://www.uipath.com/blog/product-and-updates/model-context-protocol-mcp-universal-connector)" positions MCP as a bridge between AI agents and UiPath's 700+ pre-built connectors.

### Automation Anywhere (NEW — Limited MCP Support)

Automation Anywhere can now expose automations as an MCP server for external clients (Copilot Studio, Claude). However, **AI Agent Studio cannot yet act as an MCP client** — confirmed as of March 2026 community forums. Community-built servers exist (VankProgrammingAndDesign/aa-mcp-server) but have zero stars.

This puts Automation Anywhere significantly behind UiPath on MCP adoption. The one-way support (MCP server only, no client) limits the integration story.

### Microsoft Power Platform (NEW — Public Preview)

**Power Apps MCP Server** entered **public preview in April 2026**, letting agents connect to **1,100+ enterprise systems** with no code. This is Microsoft's entry into the RPA-meets-MCP space — significant given that Microsoft also builds the most popular browser automation MCP server (Playwright).

Power Automate does not have an official first-party MCP server yet, but community alternatives exist (Cliveo/Power-Platform-MCP for Dataverse + Power Automate integration).

## Gaps and missing pieces

**Linux desktop support still thin** — The gap is partially closing with tine (GNOME Wayland), gnome-ui-mcp, and GhostDesk (Docker virtual desktop), but coverage remains far behind Windows and macOS. No KDE-specific server exists. No MCP server wraps ydotool (Wayland) or xdotool (X11) directly.

**Dormant community servers** — BrowserMCP (6,377 stars, no commits in over a year), executeautomation/mcp-playwright (5,455 stars, dormant since Dec 2025), and joshrutkowski/applescript-mcp (379 stars, dormant since April 2025) have large star counts but no maintenance. Users relying on these servers may face unpatched issues.

**Limited safety controls** — most desktop automation servers offer unrestricted access to mouse, keyboard, and system commands. Only a few provide read-only modes or permission boundaries. Playwright added file system restrictions and origin controls by default, but desktop automation servers generally lag on security.

**No cross-platform desktop abstraction** — each platform (Windows, macOS, Linux) has separate servers with different tool sets and capabilities. CursorTouch is expanding cross-platform (Windows-MCP + MacOS-MCP) but they're still separate tools.

**Fragmented browser automation** — Playwright, Selenium, Puppeteer, and CDP-based approaches all have MCP servers, but choosing between them requires understanding the trade-offs (accessibility trees vs screenshots, local vs cloud, existing sessions vs new instances).

**Power Automate still missing official MCP** — Microsoft's own RPA platform lacks first-party MCP integration, despite Microsoft building the most popular browser automation MCP server (Playwright) and Power Apps MCP entering public preview.

**Virtual desktop support emerging** — GhostDesk and screenbox provide Docker-based virtual desktops, but VNC/RDP-based remote session automation via MCP is still absent.

## Bottom line

**Rating: 4.0 / 5** — Desktop automation and browser control remains one of the most transformative MCP categories. Microsoft's Playwright MCP (31,200 stars, PulseMCP #1 globally) continues to dominate browser automation with its accessibility-tree approach, now enhanced by Playwright 1.59's browser.bind() and screencast capabilities. Windows-MCP (5,260 stars, +203 commits) is thriving with v0.7.1 adding DXCam screenshots and UWP app support. The Linux gap is finally closing — GhostDesk (44 stars) provides Docker virtual desktops and tine is the first GNOME Wayland MCP server. Enterprise RPA expanded with UiPath SDK v0.2.0, Power Apps MCP public preview (1,100+ systems), and Automation Anywhere's limited entry. OpenAI Codex shipping desktop computer use with MCP support marks a significant competitive development.

Deductions: several high-profile community servers have gone dormant (BrowserMCP, executeautomation — combined 11,800+ stars with no maintenance), Linux desktop support still thin compared to Windows/macOS, limited safety controls across desktop automation servers (Playwright improving with default origin restrictions, but most provide unrestricted system access), fragmented browser automation landscape, Power Automate still missing official MCP despite Power Apps entering preview, and no cross-platform desktop abstraction.

## Further Reading

- [Holo3: How a 10B-Parameter Open Model Beat GPT-5.4 and Opus 4.6 at Controlling Desktops](/guides/holo3-desktop-agent-osworld-record/) — H Company's open-source model scores 78.85% on OSWorld, offering a visual understanding approach to desktop automation that complements MCP tool-calling

*This review reflects research conducted in March–April 2026. Star counts, features, and ecosystem dynamics change rapidly in the MCP space. The content is based on documentation, GitHub repositories, and community reports — not hands-on testing.*

**Category**: [Business & Productivity](/categories/business-productivity/)

*This review was last edited on 2026-04-22 using Claude Opus 4.6 (Anthropic).*
