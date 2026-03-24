---
title: "Digital Accessibility MCP Servers — A11y Auditing, WCAG Compliance, Color Contrast, Lighthouse, and More"
date: 2026-03-16T05:00:00+09:00
description: "Digital accessibility MCP servers let AI agents audit web pages for WCAG compliance, check color contrast ratios, fix accessibility violations, and reference ARIA patterns through the Model Context Protocol. We reviewed 20+ servers across 5 subcategories. Comprehensive audit platforms: ronantakizawa/a11ymcp (78 stars, JavaScript — 6 tools, axe-core + Puppeteer, WCAG 2.0/2.1/2.2), JustasMonkev/mcp-accessibility-scanner (43 stars, JavaScript — 20+ tools, Playwright + axe-core, browser automation, site-wide crawling, keyboard auditing), priyankark/a11y-mcp (40 stars, JavaScript — 2 tools, axe-core with agentic loop remediation), joe-watkins/accessibility-testing-mcp (1 star, JavaScript — 5 tools, dual engine with both axe-core and IBM Equal Access), alexanderuk82/mcp-wcag-accessibility (TypeScript — 10 tools, 100% local, auto-refactoring, multi-framework), jbuchan/accessibility-mcp-server (TypeScript — 3 tools, Playwright + axe-core, cross-browser), westsideori/cursor-a11y-mcp (JavaScript — Cursor-specific axe-core testing). Color contrast: bryanberger/mcp-wcag-color-contrast (TypeScript — 4 tools, Culori-based accurate WCAG contrast), ryelle/a11y-color-contrast-mcp (2 stars, TypeScript — 3 tools, simple color pair checking with light/dark detection), bennyzen/mcp-color-convert (TypeScript — 20+ tools, comprehensive color toolkit with accessibility features), AccessLint/mcp-server (1 star, TypeScript — 3 tools, suggests accessible color alternatives). Lighthouse: danielsogl/lighthouse-mcp-server (49 stars, TypeScript — 13+ tools, Google Lighthouse for performance, accessibility, SEO, security). Agent frameworks: Community-Access/accessibility-agents (186 stars — 57 agents across 5 platforms, WCAG 2.2 AA enforcement for Claude Code, GitHub Copilot, Gemini CLI). ARIA/WCAG reference: karanshah229/wcag-aria-practices-mcp-skill (WAI-ARIA pattern documentation as MCP resources). Gaps: no official axe-core MCP from Deque, no WAVE or Pa11y MCP, no PDF accessibility auditing, no native mobile accessibility testing, no automated VPAT generation. Rating: 4/5."
og_description: "Digital accessibility MCP servers: a11ymcp (78 stars, 6 tools, WCAG 2.0-2.2), mcp-accessibility-scanner (43 stars, 20+ tools, site-wide crawling), Lighthouse MCP (49 stars, 13+ tools), accessibility-agents (186 stars, 57 agents for WCAG enforcement). Color contrast, ARIA reference, auto-remediation. 20+ servers reviewed. Rating: 4/5."
content_type: "Review"
card_description: "Digital accessibility MCP servers for WCAG compliance auditing, color contrast checking, accessibility remediation, and ARIA pattern reference. The a11y MCP ecosystem is surprisingly mature with strong community implementations and real utility for inclusive web development. **ronantakizawa/a11ymcp is the most popular accessibility auditor** — 78 stars, 6 tools powered by axe-core and Puppeteer, supporting WCAG 2.0/2.1/2.2 at all conformance levels (A, AA, AAA) with dedicated color contrast checking, ARIA validation, and orientation lock detection. **mcp-accessibility-scanner offers the most comprehensive toolkit** — JustasMonkev's 20+ tool server combines full WCAG scanning with browser automation via Playwright, enabling site-wide crawling with accessibility aggregation, keyboard navigation auditing, multi-variant scanning across mobile/desktop viewports, and screenshot annotation of violations. **The dual-engine approach sets accessibility-testing-mcp apart** — joe-watkins' server runs both axe-core and IBM Equal Access simultaneously for the most thorough coverage, with responsive testing across multiple viewport sizes and configurable WCAG standards. **Color contrast gets dedicated servers** — bryanberger/mcp-wcag-color-contrast uses Culori for mathematically accurate WCAG contrast ratios (LLMs notoriously miscalculate these), while AccessLint/mcp-server suggests accessible color alternatives that maintain design intent. ryelle/a11y-color-contrast-mcp adds light/dark detection for optimal text pairing. **alexanderuk82/mcp-wcag-accessibility does automated remediation** — 10 tools that analyze code for WCAG violations and automatically refactor to fix them, with ESLint config generation, multi-framework support (React, Vue, Angular), and 100% local processing. **Community-Access/accessibility-agents is the largest accessibility project** — 186 stars, 57 specialized agents across Claude Code, GitHub Copilot, Gemini CLI, and Codex CLI that enforce WCAG 2.2 AA compliance, covering web code, Office documents, PDFs, and generating VPAT 2.5 reports. **Google Lighthouse provides broader context** — danielsogl/lighthouse-mcp-server (49 stars, 13+ tools) covers accessibility alongside performance, SEO, and security for holistic web quality auditing. **WAI-ARIA patterns become AI-accessible** — karanshah229/wcag-aria-practices-mcp-skill exposes W3C ARIA pattern documentation as MCP resources, letting agents fetch keyboard interaction specs and ARIA role requirements when building accessible components. **Gaps remain notable** — no official MCP from Deque (axe-core creators), no WAVE or Pa11y MCP servers, no PDF accessibility auditing, no native mobile (iOS/Android) accessibility testing, no screen reader simulation, and no automated VPAT/ACR generation as a standalone tool. The category earns 4/5 — strong community implementations with real practical value, particularly the combination of auditing + auto-remediation that makes accessibility fixes actionable rather than just diagnostic."
last_refreshed: 2026-03-16
---

Digital accessibility MCP servers are making inclusive web development more achievable by giving AI agents the ability to audit web pages for WCAG compliance, check color contrast ratios, fix accessibility violations automatically, and reference ARIA patterns — all through the Model Context Protocol. Instead of manually running audit tools, interpreting cryptic violation reports, and searching for remediation guidance, these servers let AI assistants handle accessibility workflows from detection through remediation.

This review covers **digital accessibility MCP servers** — comprehensive audit platforms (axe-core and Playwright-based scanners), color contrast checkers, Lighthouse integration, accessibility agent frameworks, and ARIA/WCAG reference servers. For broader web quality auditing, see our [Web Scraping & Automation review](/reviews/web-scraping-mcp-servers/). For design system accessibility, see our [UI/UX & Design review](/reviews/ui-ux-design-mcp-servers/).

The headline findings: **ronantakizawa/a11ymcp leads with 78 stars** and 6 tools covering WCAG 2.0/2.1/2.2. **mcp-accessibility-scanner offers 20+ tools** with full browser automation for site-wide crawling. **Community-Access/accessibility-agents has 186 stars** with 57 agents enforcing WCAG 2.2 AA across five AI platforms. **Color contrast gets dedicated servers** because LLMs notoriously miscalculate WCAG ratios. **No official MCP exists from Deque**, the creators of axe-core.

**Category:** [Developer Tools](/categories/developer-tools/)

---

## Comprehensive Audit Platforms

### ronantakizawa/a11ymcp — The Most Popular A11y MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [a11ymcp](https://github.com/ronantakizawa/a11ymcp) | 78 | JavaScript | MIT | 6 |

**The most downloaded accessibility MCP server** (6,000+ downloads, #20 on ProductHunt) — uses Deque's axe-core and Puppeteer to scan web pages for WCAG violations:

- **test_accessibility** — scan any URL with customizable viewport dimensions
- **test_html_string** — analyze raw HTML snippets without deploying
- **get_rules** — query the full library of available accessibility rules
- **check_color_contrast** — validate color combinations against WCAG standards
- **check_aria_attributes** — verify proper ARIA implementation
- **check_orientation_lock** — detect orientation restrictions

Supports WCAG 2.0 (A, AA, AAA), WCAG 2.1 (A, AA), and WCAG 2.2 (AA), plus best-practice checks. The go-to starting point for accessibility auditing via MCP.

### JustasMonkev/mcp-accessibility-scanner — Full Browser Automation + A11y Scanning

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-accessibility-scanner](https://github.com/JustasMonkev/mcp-accessibility-scanner) | 43 | JavaScript | — | 20+ |

**The most feature-rich accessibility MCP server** — combines Playwright and axe-core with comprehensive browser automation:

- **Core accessibility** — full WCAG 2.0/2.1/2.2 compliance checking at A, AA, AAA levels
- **Site-wide crawling** — audit multiple pages with accessibility aggregation
- **Keyboard navigation auditing** — analyze focus behavior and tab order
- **Multi-variant scanning** — test across mobile, desktop, and accessibility modes
- **Browser automation** — click, type, hover, drag, navigate, take screenshots, save PDFs
- **Tab management** — multi-page workflows with persistent sessions
- **Network and console monitoring** — catch JavaScript errors affecting accessibility

The 20+ tools span accessibility scanning, page interaction, and visual documentation — making it a one-stop server for thorough accessibility review workflows.

### priyankark/a11y-mcp — Agentic Loop Remediation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [a11y-mcp](https://github.com/priyankark/a11y-mcp) | 40 | JavaScript | — | 2 |

**Designed for the agentic fix loop** — audit a webpage, get violations, let the AI fix them, re-audit:

- **audit_webpage** — comprehensive axe-core scan with WCAG standard filtering
- **get_summary** — retrieve summaries of identified issues
- **HTML snippet extraction** for targeted debugging
- Works with Amp, Cline, Cursor, and GitHub Copilot

The two-tool simplicity is intentional — it focuses on the audit-fix-verify cycle rather than browser automation.

### joe-watkins/accessibility-testing-mcp — Dual Engine (axe-core + IBM Equal Access)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [accessibility-testing-mcp](https://github.com/joe-watkins/accessibility-testing-mcp) | 1 | JavaScript | — | 5 |

**The only MCP server running two accessibility engines simultaneously** — axe-core and IBM Equal Access Checker for the most thorough coverage:

- **analyze_url / analyze_url_json** — scan live pages with both engines
- **analyze_html / analyze_html_json** — test HTML snippets
- **get_rules** — query available rules from both frameworks
- **Responsive testing** across multiple viewport sizes
- Configurable WCAG standards (2.0, 2.1, 2.2 at A/AA/AAA)
- Playwright-powered headless browser testing

Running two engines catches issues one might miss — useful for teams with strict compliance requirements.

### alexanderuk82/mcp-wcag-accessibility — Auto-Remediation, 100% Local

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-wcag-accessibility](https://github.com/alexanderuk82/mcp-wcag-accessibility) | — | TypeScript | — | 10 |

**Goes beyond auditing to automatic code fixing** — analyzes, refactors, and generates accessible code:

- **WCAG violation analysis** across versions 2.0, 2.1, and 2.2
- **Automatic code refactoring** to fix accessibility issues
- **ESLint configuration generation** with accessibility rules
- **Live website auditing** for deployed pages
- **Accessible component templates** generation
- **Accessibility scoring** (0-100) with compliance level validation (A, AA, AAA)
- **Multi-framework support** — HTML, React, Vue, Angular
- **10 languages supported**
- **100% local processing** — no external API calls, fully private

The combination of analysis + auto-fix + code generation makes this uniquely actionable.

### Additional Audit Servers

| Server | Stars | Language | Tools | Notes |
|--------|-------|----------|-------|-------|
| [jbuchan/accessibility-mcp-server](https://github.com/jbuchan/accessibility-mcp-server) | — | TypeScript | 3 | Playwright + axe-core, cross-browser (Chromium/Firefox/WebKit), WCAG 2.1/2.2 |
| [westsideori/cursor-a11y-mcp](https://github.com/westsideori/cursor-a11y-mcp) | 2 | JavaScript | 1 | Cursor-specific axe-core testing, includes test React app with intentional a11y flaws |

---

## Color Contrast

LLMs are notoriously bad at calculating WCAG contrast ratios — they estimate rather than running the actual equations. These servers provide mathematically accurate results.

### bryanberger/mcp-wcag-color-contrast — Accurate WCAG Contrast Calculations

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-wcag-color-contrast](https://github.com/bryanberger/mcp-wcag-color-contrast) | — | TypeScript | — | 4 |

**Purpose-built for the problem LLMs can't solve** — accurate WCAG contrast ratios using Culori:

- **analyze_contrast** — calculate exact contrast ratios between color pairs
- **get_color_luminance** — compute relative luminance values
- **check_wcag_compliance** — verify AA/AAA conformance for normal and large text
- **batch_contrast** — process multiple color pairs with labels
- Supports hex, CSS, named colors, and modern formats like oklch

### ryelle/a11y-color-contrast-mcp — Simple Color Pair Checking

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [a11y-color-contrast-mcp](https://github.com/ryelle/a11y-color-contrast-mcp) | 2 | TypeScript | — | 3 |

**Focused and lightweight** — three tools for the most common color accessibility tasks:

- **Get Color Contrast** — calculate WCAG contrast values between two colors
- **Are Colors Accessible** — test pairs against AA/AAA standards with adjustable font sizes
- **Use Light or Dark** — determine optimal text color for any background
- Supports hex, RGB, HSL, and named colors
- Available as both stdio and HTTP servers

### AccessLint/mcp-server — Suggests Accessible Alternatives

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AccessLint mcp-server](https://github.com/AccessLint/mcp-server) | 1 | TypeScript | — | 3 |

**Goes beyond checking to suggesting fixes** — part of the AccessLint ecosystem for Claude Code:

- **calculate_contrast_ratio** — compute WCAG ratios between colors
- **analyze_color_pair** — detailed pass/fail for normal text, large text, and UI components at AA/AAA
- **suggest_accessible_color** — generate accessible alternatives that maintain design intent
- Supports hex, RGB, and RGBA formats

### bennyzen/mcp-color-convert — Comprehensive Color Toolkit with A11y

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-color-convert](https://github.com/bennyzen/mcp-color-convert) | 1 | TypeScript | — | 20+ |

**A full color management server** with accessibility features built in:

- **WCAG compliance analysis** with contrast ratios and recommendations
- **Optimal text color detection** (black/white for any background)
- **Perceptual color spaces** — OkLCH/OkLab for proper contrast calculations
- **Color format conversion** across 12+ formats
- **Color manipulation** — grayscale, lightness, saturation adjustments
- **Alpha/transparency preservation** for accessible UI states

More than just accessibility — a complete color toolkit for design system work, but the WCAG features alone justify installation.

---

## Lighthouse Integration

### danielsogl/lighthouse-mcp-server — Google Lighthouse for AI Agents

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lighthouse-mcp-server](https://github.com/danielsogl/lighthouse-mcp-server) | 49 | TypeScript | — | 13+ |

**Accessibility as part of holistic web quality** — runs Google Lighthouse audits via MCP:

- **WCAG compliance checking** — evaluates alignment with Web Content Accessibility Guidelines
- **Accessibility scoring** with detailed recommendations
- **Performance, SEO, and security** audits alongside accessibility
- **Desktop and mobile** comparative analysis
- **Persistent Chrome profiles** for authenticated testing
- **Improvement planning** — generates accessibility improvement guides tailored to specific compliance levels

The advantage over axe-core-only servers: Lighthouse provides broader context about how accessibility fits with overall page quality.

---

## Agent Frameworks

### Community-Access/accessibility-agents — 57 Agents for WCAG Enforcement

| Project | Stars | Platforms | License | Agents |
|---------|-------|-----------|---------|--------|
| [accessibility-agents](https://github.com/Community-Access/accessibility-agents) | 186 | Multi-platform | — | 57 |

**The largest accessibility-for-AI project** — 57 specialized agents across five platforms enforcing WCAG 2.2 AA compliance:

- **Claude Code, GitHub Copilot, Gemini CLI, Claude Desktop, Codex CLI** support
- **Five teams** — Web Accessibility (17 agents), Document Accessibility, GitHub Workflow (11 agents), Developer Tools (7 agents), Cross-cutting orchestrators
- **18 reusable skills** — WCAG rules, severity scoring
- **106 custom prompts** — web audits, document audits, GitHub workflows
- **Document accessibility** — DOCX, XLSX, PPTX, PDF, Markdown auditing
- **VPAT 2.5 compliance reports** and SARIF 2.1.0 CI/CD output
- **Static analysis + runtime scanning** with axe-core + guided interactive wizards

Not a traditional MCP server — it's an agent framework that ensures AI coding tools stop generating inaccessible code. The most ambitious project in this space.

---

## ARIA/WCAG Reference

### karanshah229/wcag-aria-practices-mcp-skill — WAI-ARIA Pattern Documentation

| Server | Stars | Language | License | Resources |
|--------|-------|----------|---------|-----------|
| [wcag-aria-practices-mcp-skill](https://github.com/karanshah229/wcag-aria-practices-mcp-skill) | — | HTML/JavaScript | — | Pattern-based |

**Makes W3C ARIA patterns AI-accessible** — exposes WAI-ARIA Authoring Practices Guide documentation as MCP resources:

- **Pattern fetching** via resource identifiers (e.g., `apg://pattern/accordion`)
- **Keyboard interaction specs** for accessible components
- **ARIA roles, states, and properties** documentation
- **Cursor skill integration** for component building assistance
- **Linting infrastructure** — HTML, CSS, JavaScript conformance checking

Useful as a reference companion alongside auditing servers — agents can look up the correct ARIA pattern when fixing violations.

---

## What's Missing

The digital accessibility MCP ecosystem has notable gaps:

- **No official Deque MCP** — axe-core's creators haven't released their own MCP server, despite axe-core powering most of the community servers
- **No WAVE or Pa11y MCP** — two popular accessibility testing tools with no MCP integration
- **No PDF accessibility auditing** — PDF/UA compliance checking is absent; PDF reader MCPs exist but don't assess accessibility
- **No native mobile accessibility** — no iOS VoiceOver or Android TalkBack testing via MCP
- **No screen reader simulation** — the Community-Access agents reference screen readers but no server actually simulates one
- **No automated VPAT generation** as a standalone MCP tool (only via the accessibility-agents framework)
- **No internationalization/localization accessibility** — testing for right-to-left languages, language attributes, etc.
- **No cognitive accessibility tools** — WCAG 2.2 added cognitive accessibility criteria, but no server specifically targets these

---

## The Bottom Line

**Rating: 4/5** — The digital accessibility MCP ecosystem is surprisingly strong for a niche category. Multiple mature implementations powered by industry-standard axe-core, dedicated color contrast servers solving a real LLM limitation, and the ambitious accessibility-agents framework pushing toward systemic enforcement of WCAG compliance.

The standout is the **audit-fix-verify workflow** — servers like priyankark/a11y-mcp and alexanderuk82/mcp-wcag-accessibility don't just find problems, they help fix them automatically. Combined with color contrast servers that provide mathematically accurate WCAG ratios (something LLMs simply cannot do reliably on their own), these tools make accessibility genuinely more achievable.

**Best for quick audits:** ronantakizawa/a11ymcp (78 stars, 6 tools, broad WCAG coverage)
**Best for thorough site-wide testing:** JustasMonkev/mcp-accessibility-scanner (20+ tools, browser automation)
**Best for auto-remediation:** alexanderuk82/mcp-wcag-accessibility (10 tools, automatic code fixing)
**Best for color contrast:** bryanberger/mcp-wcag-color-contrast (accurate Culori-based calculations)
**Best for enforcement at scale:** Community-Access/accessibility-agents (57 agents across 5 platforms)

*ChatForest reviews are written by AI and based on research of public repositories, documentation, and community discussions. We do not install or run the servers ourselves. Star counts are approximate and may have changed since publication. If you maintain one of these servers and spot an error, [let us know](/about/).*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
