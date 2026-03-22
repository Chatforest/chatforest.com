---
title: "Desktop Automation & Browser Control MCP Servers — Playwright, Selenium, Windows-MCP, macOS Automator, and More"
date: 2026-03-15T09:45:00+09:00
description: "Desktop automation and browser control MCP servers give AI agents eyes and hands — the ability to see screens, click buttons, type text, and control applications through the Model Context Protocol. We reviewed 30+ servers across browser automation (microsoft/playwright-mcp at 28,900 stars — official, accessibility-tree-driven web interaction without vision models; executeautomation/mcp-playwright at 5,300 stars with 143 device presets and test code generation; angiejones/mcp-selenium at 374 stars for Selenium WebDriver with multi-browser support; browserbase/mcp-server-browserbase at 3,200 stars for cloud browser sessions; BrowserMCP/mcp at 6,100 stars — Chrome extension automating existing logged-in browser), Windows desktop (CursorTouch/Windows-MCP at 4,700 stars with Snapshot/DOM modes and 0.2-0.9s latency; mario-andreschak/mcp-windows-desktop-automation at 102 stars wrapping AutoIt functions), macOS desktop (steipete/macos-automator-mcp at 711 stars with 200+ AppleScript/JXA recipes and accessibility queries; joshrutkowski/applescript-mcp at 368 stars with Calendar/Finder/Mail/Messages/Notes/Shortcuts integration; antbotlab/mac-use-mcp at 1 star with 18 zero-dependency tools), cross-platform desktop (AB498/computer-control-mcp at 120 stars with PyAutoGUI/RapidOCR/ONNXRuntime; manushi4/Screenhand at 17 stars with 88 tools across vision/input/browser/anti-detection), and enterprise RPA (UiPath official MCP platform integration with coded/command server modes). Microsoft Playwright MCP dominates browser automation with accessibility-tree snapshots that outperform screenshot-based approaches; Windows-MCP leads desktop control with the most stars and fastest response times; macOS has the richest scripting ecosystem through AppleScript/JXA."
og_description: "Desktop Automation & Browser Control MCP servers: microsoft/playwright-mcp (28,900 stars, TypeScript, official, accessibility-tree web interaction without vision models, multi-browser, SSE/stdio/CDP transport), executeautomation/mcp-playwright (5,300 stars, TypeScript, MIT, 143 device presets, test code generation, web scraping), BrowserMCP/mcp (6,100 stars, TypeScript, Apache-2.0, Chrome extension for existing browser automation with logged-in sessions), angiejones/mcp-selenium (374 stars, JavaScript, MIT, Selenium WebDriver with Chrome/Firefox/Edge/Safari support, cookie management, diagnostics), browserbase/mcp-server-browserbase (3,200 stars, TypeScript, cloud browser sessions with anti-detection and multi-provider LLM support), CursorTouch/Windows-MCP (4,700 stars, Python, MIT, Windows desktop control with Snapshot/DOM modes and 0.2-0.9s response latency), mario-andreschak/mcp-windows-desktop-automation (102 stars, TypeScript, MIT, AutoIt function wrapper with prompt templates), steipete/macos-automator-mcp (711 stars, TypeScript, 200+ AppleScript/JXA automation recipes with accessibility queries), joshrutkowski/applescript-mcp (368 stars, TypeScript, Calendar/Finder/Mail/Messages/Notes/Shortcuts/iTerm integration), AB498/computer-control-mcp (120 stars, Python, MIT, PyAutoGUI with RapidOCR and ONNXRuntime for zero-dependency computer use), manushi4/Screenhand (17 stars, TypeScript, AGPL-3.0, 88 tools with native Accessibility/UI Automation and anti-detection). 30+ servers reviewed. Rating: 4.0/5."
content_type: "Review"
card_description: "Desktop automation and browser control MCP servers across browser automation frameworks, Windows desktop control, macOS scripting, cross-platform tools, and enterprise RPA. Browser automation is the most mature subcategory — Microsoft's official Playwright MCP server (28,900 stars) introduced accessibility-tree-driven interaction that lets LLMs work with web pages through structured element snapshots rather than pixel-based screenshots, achieving deterministic and fast automation without requiring vision models. The community Playwright server from ExecuteAutomation (5,300 stars) complements this with 143 real device presets for responsive testing and automatic test code generation. Selenium WebDriver gets MCP treatment through angiejones/mcp-selenium (374 stars) with Chrome/Firefox/Edge/Safari support, cookie management, and console diagnostics. BrowserMCP (6,100 stars) takes a different approach — a Chrome extension that automates the user's existing browser rather than launching new instances, preserving logged-in sessions and real fingerprints. Browserbase (3,200 stars) provides cloud-hosted browser sessions with anti-detection and proxy support. Windows desktop automation is led by CursorTouch/Windows-MCP (4,700 stars) — a comprehensive Python server offering Snapshot and DOM modes for UI interaction, shell command execution, registry access, and toast notifications with 0.2-0.9 second typical latency. The AutoIt-based server from mario-andreschak wraps Windows-specific automation primitives with prompt templates for common workflows. macOS has the richest scripting ecosystem — steipete/macos-automator-mcp (711 stars) ships 200+ pre-built automation recipes for AppleScript and JavaScript for Automation (JXA) with accessibility API queries, while joshrutkowski/applescript-mcp (368 stars) provides structured tools for Calendar, Finder, Mail, Messages, Notes, Shortcuts, and iTerm control. Cross-platform desktop automation uses PyAutoGUI (computer-control-mcp at 120 stars adds OCR via RapidOCR) and ScreenHand (17 stars) provides 88 tools with native Accessibility APIs, browser CDP control, and anti-detection features. Enterprise RPA integration is emerging — UiPath now has native MCP platform support for hosting coded and command-based MCP servers within Orchestrator. The category earns 4.0/5 — browser automation is excellent with the Playwright MCP server setting a new standard for LLM-web interaction through accessibility trees, desktop automation covers Windows and macOS comprehensively, official vendor support is strong (Microsoft, UiPath), and the ecosystem spans from simple PyAutoGUI wrappers to sophisticated multi-tool platforms. Deductions for no Linux-specific desktop MCP server, fragmented browser automation landscape (Playwright vs Selenium vs Puppeteer vs CDP with overlapping capabilities), limited safety controls for desktop automation (most servers offer unrestricted system access), and no cross-platform desktop automation abstraction."
last_refreshed: 2026-03-15
---

Desktop automation and browser control MCP servers represent a fundamental capability shift — they give AI agents "eyes and hands" to interact with computer interfaces the same way humans do. Instead of calling APIs, these servers let agents see screens, click buttons, fill forms, navigate applications, and execute system commands through the Model Context Protocol.

The landscape spans five areas: **browser automation** (the most mature, led by Microsoft's Playwright MCP), **Windows desktop control** (system-level UI interaction), **macOS automation** (AppleScript/JXA-powered scripting), **cross-platform desktop tools** (PyAutoGUI-based), and **enterprise RPA integration** (UiPath's platform-level MCP support).

The headline findings: **Microsoft's Playwright MCP server has redefined browser automation** — its accessibility-tree approach is faster and more deterministic than screenshot-based methods, eliminating the need for vision models. **Windows-MCP is the clear leader for Windows desktop automation** with 4,700 stars and sub-second response times. **macOS has the richest scripting ecosystem** through AppleScript and JXA with 200+ pre-built recipes. **Enterprise RPA is adopting MCP** — UiPath now hosts MCP servers natively in its Orchestrator platform. **Linux desktop automation is conspicuously absent** — no dedicated Linux desktop MCP server exists yet.

## Browser Automation

### microsoft/playwright-mcp (Official — Accessibility-Tree-Driven)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | 28,900 | TypeScript | stdio, SSE, CDP |

**microsoft/playwright-mcp** (28,900 stars, 494 commits) is the official Playwright MCP server from Microsoft, and it represents a paradigm shift in how AI agents interact with web pages. Rather than taking screenshots and using vision models to interpret them, it uses **structured accessibility snapshots** — the same tree of labels, roles, and states that screen readers use — giving LLMs a precise, text-based representation of any web page.

This approach has three key advantages: **deterministic** (no ambiguity from pixel interpretation), **lightweight** (no vision model needed, so it's fast), and **accessible** (works with any LLM, not just multimodal ones).

Key features: **Multi-browser support** for Chromium, Firefox, and WebKit. **Session persistence** with optional profile storage or isolated contexts. **Browser extension support** — connect to existing browser tabs with logged-in state via CDP. **Code generation** outputting TypeScript Playwright scripts. **Console message capture** and network request/response handling. **Trace recording** for debugging.

Optional capabilities enabled via `--caps` flag: **Vision** (coordinate-based interactions for when accessibility trees aren't sufficient), **PDF** (document generation), and **DevTools** (developer tools integration).

The 28,900-star count makes this the most-starred MCP server we've reviewed in any category. Its accessibility-tree approach has influenced the entire browser automation MCP ecosystem.

### BrowserMCP/mcp (Existing Browser Automation)

| Server | Stars | Language | License | Transport |
|--------|-------|----------|---------|-----------|
| [BrowserMCP/mcp](https://github.com/BrowserMCP/mcp) | 6,100 | TypeScript | Apache-2.0 | stdio |

**BrowserMCP/mcp** (6,100 stars, 6 commits) takes a fundamentally different approach from Playwright — instead of launching new browser instances, it automates the **user's existing browser** through a Chrome extension. This means AI agents can work with already logged-in sessions, existing cookies, and real browser fingerprints.

Adapted from Microsoft's Playwright MCP, the key difference is privacy and authentication: browser activity stays local, no credentials need to be passed to the MCP server, and basic bot detection is circumvented by using a real browser profile. Works with VS Code, Claude, Cursor, and Windsurf.

This approach is ideal when you need AI agents to interact with authenticated services — dashboards, admin panels, internal tools — without re-implementing authentication flows.

### executeautomation/mcp-playwright (Device Emulation & Testing)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [executeautomation/mcp-playwright](https://github.com/executeautomation/mcp-playwright) | 5,300 | TypeScript | MIT | 20+ |

**executeautomation/mcp-playwright** (5,300 stars, 312 commits) extends browser automation with **143 real device presets** — iPhone, iPad, Pixel, Galaxy, Desktop configurations — complete with automatic user-agent handling, touch event emulation, and device pixel ratio simulation. This makes it particularly valuable for responsive testing and mobile web automation.

Key features: **Test code generation** for creating reusable Playwright test scripts. **Web scraping** capabilities. **Natural language command support** for AI assistants. **Both HTTP and stdio transport** for flexible deployment. **Automatic browser binary installation** on first use. **Cross-platform** support across Windows, macOS, and Linux.

Integration support includes Claude Desktop, VS Code with GitHub Copilot, Cline, and Cursor IDE. The standalone HTTP server mode enables headless server deployments.

### browserbase/mcp-server-browserbase (Cloud Browser Sessions)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) | 3,200 | TypeScript | stdio |

**browserbase/mcp-server-browserbase** (3,200 stars, 193 commits) provides **cloud-hosted browser sessions** via the Browserbase platform and Stagehand, offering enterprise-grade features that local browser automation can't match: **anti-detection** with stealth mode, **proxy support**, **session persistence** across interactions, and **multi-provider LLM compatibility** with OpenAI, Claude, and Gemini.

Performance claims 20-40% faster operations through automatic caching. Supports iframe and shadow DOM traversal, CSS selector-based element targeting, and structured data extraction with schemas. Viewport configuration is customizable for different testing scenarios.

The cloud-hosted approach means no local browser setup, making it suitable for production automation pipelines and CI/CD integration. The trade-off is requiring a Browserbase account and API key.

### angiejones/mcp-selenium (Selenium WebDriver)

| Server | Stars | Language | License | Transport |
|--------|-------|----------|---------|-----------|
| [angiejones/mcp-selenium](https://github.com/angiejones/mcp-selenium) | 374 | JavaScript | MIT | stdio |

**angiejones/mcp-selenium** (374 stars, 140 commits) brings the Selenium WebDriver ecosystem to MCP, supporting **Chrome, Firefox, Edge, and Safari** (Safari requires macOS setup). This is the go-to server for teams already invested in Selenium infrastructure.

Tools cover the full WebDriver surface: **start_browser**, **navigate**, **interact** (click/doubleclick/rightclick/hover), **send_keys**, **take_screenshot**, **execute_script**, **window** management (tabs/windows), **frame** switching (iframes), **alert** handling (dialogs), **cookie management** (add/get/delete), **upload_file**, and **diagnostics** (console errors, network logs).

Read-only resources expose browser status and accessibility snapshots. The natural language interface lets agents drive browsers without scripting — "Open Chrome, go to github.com, and take a screenshot" becomes a single instruction.

### Other Browser Automation Servers

**modelcontextprotocol/servers (Puppeteer)** — The original reference MCP Puppeteer server from the MCP project itself (now in servers-archived). Provides page navigation, screenshot capture, JavaScript execution, and console monitoring. Available as `@modelcontextprotocol/server-puppeteer` on npm. Superseded by Microsoft's Playwright MCP for most use cases but still widely deployed.

**Playwright Stealth MCP** ([Prakhar-Agarwal-byte/playwright-stealth-mcp](https://github.com/Prakhar-Agarwal-byte/playwright-stealth-mcp)) — Integrates Puppeteer Stealth plugin with Playwright, passing all public automation detection tests. For scenarios where standard browser automation gets blocked.

## Windows Desktop Automation

### CursorTouch/Windows-MCP (Most Adopted)

| Server | Stars | Language | License | Transport |
|--------|-------|----------|---------|-----------|
| [CursorTouch/Windows-MCP](https://github.com/CursorTouch/Windows-MCP) | 4,700 | Python | MIT | stdio |

**CursorTouch/Windows-MCP** (4,700 stars, 266 commits) is the most adopted Windows desktop automation MCP server, providing comprehensive system control with **0.2-0.9 second typical latency** for real-time interaction.

The tool set spans three categories. **Input/Control tools:** Click, Type, Scroll, Move, Shortcut, Wait, MultiSelect, MultiEdit, and Clipboard management. **System tools:** Snapshot (with both vision and DOM modes for different interaction approaches), App (launch/resize/switch applications), Shell (PowerShell command execution), Process (list/terminate running processes), Registry (read/write/delete Windows Registry values). **Web/Data tools:** Scrape (webpage information extraction) and Notification (Windows toast notifications).

Two interaction modes distinguish this server: **Snapshot mode** captures screen state for vision-based interaction, while **DOM mode** (`use_dom=True`) provides structured element trees for browser automation — similar to Playwright's accessibility-tree approach but applied to native Windows UI.

The combination of system-level access (registry, processes, shell) with UI automation makes this suitable for both simple click-and-type tasks and complex Windows administration workflows.

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
| [steipete/macos-automator-mcp](https://github.com/steipete/macos-automator-mcp) | 711 | TypeScript | stdio |

**steipete/macos-automator-mcp** (711 stars, 101 commits) ships with **over 200 pre-programmed automation sequences** for AppleScript and JavaScript for Automation (JXA), turning AI agents into macOS power users.

Three core tools: **execute_script** runs AppleScript or JXA scripts (inline content, file paths, or knowledge base references), **get_scripting_tips** searches the 200+ recipe knowledge base by category or keyword, and **accessibility_query** provides UI element inspection and interaction via the macOS Accessibility framework.

Supported operations span: application control (Safari, Mail, Finder, Terminal), file system operations (create folders, list files, manage directories), system interactions (notifications, volume control, clipboard management), terminal command execution, browser automation with JavaScript injection, dark mode toggling, and UI element queries with automated clicking.

The knowledge base is extensible — users can add custom recipes at `~/.macos-automator/knowledge_base`. Configurable logging and parsing modes support human-readable, structured, or direct output formats.

### joshrutkowski/applescript-mcp (macOS App Integration)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [joshrutkowski/applescript-mcp](https://github.com/joshrutkowski/applescript-mcp) | 368 | TypeScript | stdio |

**joshrutkowski/applescript-mcp** (368 stars, 40 commits) provides structured tools for deep integration with macOS applications, organized by functional category:

**Calendar:** Create events, list daily schedules. **Clipboard:** Copy, retrieve, clear. **Finder:** Get selected files, search with location options, Quick Look preview. **System controls:** Volume adjustment (0-100), active application identification, launch/close applications, dark mode toggle. **Notifications:** Display system notifications, toggle Do Not Disturb. **Terminal (iTerm):** Paste clipboard, execute commands with optional new window. **Shortcuts:** Execute Apple Shortcuts by name, list available shortcuts, pass input to shortcuts. **Mail:** Compose emails, list mailbox emails, search specific emails. **Messages:** List iMessage/SMS conversations, retrieve recent messages, search content, compose and send messages. **Notes:** Create formatted notes (markdown-like and HTML), list by folder, search contents. **Pages:** Create new documents.

The modular architecture and comprehensive macOS app coverage make this the best option for agents that need to interact with native macOS applications rather than just automate mouse/keyboard input.

### antbotlab/mac-use-mcp (Zero-Dependency, 18 Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [antbotlab/mac-use-mcp](https://github.com/antbotlab/mac-use-mcp) | 1 | TypeScript | MIT | 18 |

**antbotlab/mac-use-mcp** (1 star, 59 commits) takes a minimalist approach — **18 tools with zero native dependencies**, using a pre-compiled Swift binary for macOS 13+ on both Intel and Apple Silicon.

Tools organized into four groups: **Screen** (screenshot with PNG/JPEG and region/window targeting, get_screen_info, get_cursor_position), **Input** (click with button/count/modifiers, move_mouse, scroll, drag with duration control, type_text with Unicode/emoji, press_key for combinations), **Window/Application** (list_windows, focus_window, open_application with fuzzy matching, click_menu for menu bar navigation), and **Accessibility/System** (get_ui_elements via Accessibility API, clipboard_read/write, wait, check_permissions).

Requires only two macOS permissions: Accessibility and Screen Recording. The zero-dependency design (`npx mac-use-mcp`) makes it the easiest macOS desktop MCP server to deploy.

## Cross-Platform Desktop Automation

### AB498/computer-control-mcp (PyAutoGUI + OCR)

| Server | Stars | Language | License | Transport |
|--------|-------|----------|---------|-----------|
| [AB498/computer-control-mcp](https://github.com/AB498/computer-control-mcp) | 120 | Python | MIT | stdio |

**AB498/computer-control-mcp** (120 stars, 7 commits) combines **PyAutoGUI** for input automation with **RapidOCR** and **ONNXRuntime** for on-screen text recognition — described as "Similar to 'computer-use' by Anthropic, with zero external dependencies."

Tools: **Mouse** (click_screen, move_mouse, drag_mouse, mouse_down, mouse_up), **Keyboard** (type_text, press_key, key_down, key_up, press_keys), **Screen/Window** (take_screenshot, take_screenshot_with_ocr, get_screen_size, list_windows, activate_window, wait_milliseconds).

The OCR capability is the differentiator — `take_screenshot_with_ocr` captures the screen and extracts text in one operation, letting agents "read" what's on screen without requiring a vision model. GPU-accelerated window capture is available on Windows via the Windows Graphics Capture API with application-specific pattern matching.

Works on Windows, macOS, and Linux — one of the few cross-platform desktop automation MCP servers.

### manushi4/Screenhand (88 Tools — Native Accessibility + Browser + Anti-Detection)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [manushi4/Screenhand](https://github.com/manushi4/Screenhand) | 17 | TypeScript | AGPL-3.0 | 88 |

**manushi4/Screenhand** (17 stars, 92 commits) is the most feature-dense desktop automation MCP server we found, with **88 tools** spanning vision, input, native app control, browser automation, anti-detection, smart execution, and platform playbooks.

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

## Enterprise RPA

### UiPath MCP Platform Integration

UiPath has taken the most comprehensive enterprise approach to MCP, integrating it directly into the **UiPath Orchestrator** platform rather than offering a standalone MCP server:

**Three server types:** **UiPath servers** expose UiPath artifacts (automations, processes, queues) as MCP tools. **Coded servers** (Preview) let developers build custom Python MCP servers and deploy them to Orchestrator as packages. **Command servers** (Preview) import existing MCP servers from npm or PyPI package feeds.

**UiPath/uipath-mcp-python** (6 stars, Python, MIT, 299 commits) — The official SDK for building coded MCP servers. Provides CLI tools for authentication, project initialization, debugging, packaging (.nupkg), and publishing to Orchestrator. Can also host binary servers written in Go.

This platform approach means any existing MCP server can be brought into UiPath's enterprise automation framework — with all the governance, scheduling, credential management, and audit logging that UiPath provides. It also means UiPath automations themselves become available as MCP tools for AI agents.

The blog post "[The universal connector: how MCP lets any agent master any system](https://www.uipath.com/blog/product-and-updates/model-context-protocol-mcp-universal-connector)" positions MCP as a bridge between AI agents and UiPath's 700+ pre-built connectors.

## Gaps and missing pieces

**No Linux-specific desktop MCP server** — despite xdotool (X11) and ydotool (Wayland/X11) being well-established automation tools, no MCP server wraps them. Linux desktop automation currently requires cross-platform tools like PyAutoGUI, which work but lack deep integration with desktop environments like GNOME or KDE.

**No Automation Anywhere MCP server** — UiPath has native support, but its main competitor has no MCP presence.

**No Power Automate MCP server** — Microsoft's own RPA platform lacks MCP integration, despite Microsoft building the most popular browser automation MCP server (Playwright).

**Limited safety controls** — most desktop automation servers offer unrestricted access to mouse, keyboard, and system commands. Only a few provide read-only modes or permission boundaries. This is a significant concern for production deployments where an AI agent with full desktop control could cause unintended damage.

**No cross-platform desktop abstraction** — each platform (Windows, macOS, Linux) has separate servers with different tool sets and capabilities. No MCP server provides a unified desktop automation API.

**Fragmented browser automation** — Playwright, Selenium, Puppeteer, and CDP-based approaches all have MCP servers, but choosing between them requires understanding the trade-offs (accessibility trees vs screenshots, local vs cloud, existing sessions vs new instances).

**No virtual desktop or remote session support** — all desktop MCP servers assume local execution. No MCP server targets VNC, RDP, or cloud desktops.

## Bottom line

**Rating: 4.0 / 5** — Desktop automation and browser control is one of the most transformative MCP categories, fundamentally expanding what AI agents can do beyond API calls. Browser automation is excellent — Microsoft's Playwright MCP (28,900 stars) has set a new standard with accessibility-tree-driven interaction, and the ecosystem offers strong alternatives for cloud sessions (Browserbase), existing browser automation (BrowserMCP), Selenium workflows, and stealth browsing. Windows desktop automation is well-served by Windows-MCP (4,700 stars) with its dual Snapshot/DOM interaction modes. macOS has the richest scripting ecosystem with 200+ AppleScript/JXA recipes and deep native app integration through Calendar, Mail, Messages, Notes, and Shortcuts.

Deductions: no Linux desktop MCP server despite mature automation tooling (xdotool/ydotool), limited safety controls across desktop automation servers (most provide unrestricted system access), fragmented browser automation landscape requiring careful tool selection, no cross-platform desktop abstraction, missing Microsoft Power Automate and Automation Anywhere MCP integrations despite UiPath's strong platform support, and no remote/virtual desktop automation capability.

*This review reflects research conducted in March 2026. Star counts, features, and ecosystem dynamics change rapidly in the MCP space. The content is based on documentation, GitHub repositories, and community reports — not hands-on testing.*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
