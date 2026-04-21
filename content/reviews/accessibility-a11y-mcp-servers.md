---
title: "Accessibility & a11y MCP Servers — Axe-Core, WCAG Auditing, Color Contrast, BrowserStack, and More"
date: 2026-03-15T12:55:00+09:00
description: "Accessibility and a11y MCP servers are enabling AI-powered WCAG compliance testing and remediation. We reviewed 25+ servers across 7 subcategories."
og_description: "Accessibility MCP servers: Deque axe MCP (official, 2 tools, paid), a11ymcp (83 stars, 6 tools, axe-core), mcp-accessibility-scanner (48 stars, 15+ tools, Playwright), BrowserStack MCP (136 stars, 20+ tools), WCAG reference server (20 tools), color contrast checkers, and 79 accessibility agents. Rating: 3.5/5."
content_type: "Review"
card_description: "Accessibility and a11y MCP servers for WCAG compliance testing, color contrast checking, code remediation, and enterprise accessibility scanning. The biggest development since March 2026: **Deque launched an official axe MCP Server** (dequelabs/axe-mcp-server-public) — the company behind axe-core that powers nearly every community scanner now has its own 2-tool server (analyze + remediate) integrated with Claude, Copilot, and Cursor. It requires a paid Axe DevTools for Web subscription. The community leader is ronantakizawa/a11ymcp (83 stars, 6,000+ downloads) with 6 tools covering URL testing, HTML snippet testing, rule exploration, color contrast, ARIA validation, and orientation lock detection. JustasMonkev's mcp-accessibility-scanner (48 stars, 193 commits) goes further with Playwright-powered multi-page crawling, keyboard navigation testing, and matrix scanning — the most comprehensive free scanner available. A new WCAG reference server (joe-watkins/wcag-mcp, 7 stars, 20 tools) provides comprehensive access to all 87 WCAG 2.2 success criteria, 400+ techniques, and 101 glossary terms — useful for AI agents that need to understand the standards, not just scan for violations. joe-watkins/accessibility-testing-mcp adds dual-engine testing (axe-core + IBM Equal Access). BrowserStack's official MCP server (136 stars) includes accessibility scanning powered by Spectra with AI-generated code fixes, though it requires a paid license. The Community-Access/accessibility-agents project (236 stars, v4.5.0) has grown to 79 specialized agents across 8 teams and 5 platforms — the most ambitious accessibility-AI project in the ecosystem. The category earns 3.5/5 — excellent tooling depth for web page auditing with Deque now officially in the MCP space, but gaps remain: no native mobile accessibility testing (iOS VoiceOver, Android TalkBack), no PDF/document accessibility remediation via MCP, no screen reader simulation, and no VPAT/ACR report generation."
last_refreshed: 2026-04-21
---

Accessibility MCP servers are bringing automated WCAG compliance testing directly into AI coding workflows. Instead of switching to browser DevTools or running manual audits, these servers let AI agents scan pages for violations, check color contrast ratios, validate ARIA attributes, and even refactor code to fix accessibility issues — all through the Model Context Protocol.

The landscape now spans seven areas: **full-page auditing** (axe-core-powered scanners), **WCAG reference & knowledge** (guideline lookup tools), **color contrast checking** (dedicated contrast ratio tools), **WCAG analysis & remediation** (code-level fixing), **enterprise integration** (Deque, BrowserStack), **color blindness simulation** (visual impairment previews), and **dual-engine testing** (multiple accessibility engines).

The headline findings: **Deque — the company behind axe-core — has launched an official MCP server** (dequelabs/axe-mcp-server-public), with 2 tools (analyze + remediate) that work with Claude, Copilot, and Cursor. This is the single most important development in the category: the upstream engine provider now competes directly with the community servers that use its library. However, it requires a paid Axe DevTools for Web subscription. **Three competing free axe-core scanners** still dominate open-source adoption — ronantakizawa/a11ymcp (83 stars, 6,000+ downloads), JustasMonkev's mcp-accessibility-scanner (48 stars, 193 commits, 15+ tools), and priyankark/a11y-mcp (40 stars). **The most capable free scanner is JustasMonkev's**, with Playwright-based multi-page crawling, keyboard navigation testing, and matrix scanning across viewport variants. **A new WCAG reference server** (joe-watkins/wcag-mcp, 7 stars, 20 tools) gives AI agents comprehensive access to WCAG 2.2 guidelines, techniques, and glossary — enabling agents to understand the standards, not just detect violations. **The Community-Access/accessibility-agents project has surged** to 236 stars with 79 agents across 8 teams — the most ambitious accessibility-AI project in the ecosystem. **The biggest gap is still what's missing**: no mobile accessibility testing (VoiceOver, TalkBack), no PDF/document accessibility remediation, no screen reader emulation, and no VPAT/ACR generation.

**Category:** [Developer Tools](/categories/developer-tools/)

---

## Full-Page Auditing

### a11ymcp (ronantakizawa)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ronantakizawa/a11ymcp](https://github.com/ronantakizawa/a11ymcp) | 83 | JavaScript | MIT | 6 |

The most popular free accessibility MCP server, with **6,000+ downloads** and a **#20 ranking on ProductHunt**. Uses axe-core and Puppeteer to provide six distinct tools. 87 commits. Verified on MseeP.ai and listed in the Glama.ai MCP registry.

- **test_accessibility** — scan any public URL with customizable viewport dimensions
- **test_html_string** — test raw HTML snippets without deploying
- **get_rules** — explore axe-core's full rule catalog
- **check_color_contrast** — verify foreground/background color pairs against WCAG thresholds
- **check_aria_attributes** — validate ARIA usage in HTML markup
- **check_orientation_lock** — detect orientation restrictions that violate WCAG 1.3.4

Supports WCAG 2.0, 2.1, and 2.2 testing. The HTML string testing is particularly useful for AI coding assistants — test generated markup before it reaches a browser.

### mcp-accessibility-scanner (JustasMonkev)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [JustasMonkev/mcp-accessibility-scanner](https://github.com/JustasMonkev/mcp-accessibility-scanner) | 48 | JavaScript | — | 15+ |

The **most comprehensive free accessibility scanner** in the MCP ecosystem. Built on Playwright (not Puppeteer), which enables richer browser automation and persistent sessions. Now at 193 commits (+20% since March), indicating active, ongoing development.

Core scanning tools:
- **scan_page** — WCAG compliance checks across 2.0/2.1/2.2 at A/AA/AAA levels
- **audit_site** — multi-page crawling with aggregated violation reporting
- **scan_page_matrix** — variant comparison across mobile, desktop, zoom, and reduced-motion configurations
- **audit_keyboard** — real keyboard navigation testing (not just static analysis)

Plus full browser automation: navigate, click, type, hover, drag, select, take screenshots, save PDFs, manage tabs, and resize viewports.

The matrix scanning feature is unique — it tests the same page across multiple viewport/motion configurations in a single call, catching responsive design accessibility regressions.

### a11y-mcp (priyankark)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [priyankark/a11y-mcp](https://github.com/priyankark/a11y-mcp) | 40 | JavaScript | MPL-2.0 | 2 |

A simpler, focused approach with just two tools:

- **audit_webpage** — detailed accessibility audit with optional HTML snippet extraction and WCAG standard filtering
- **get_summary** — summarize accessibility issues on a page

Designed explicitly for **agentic loops** — audit a page, get violations, let the AI fix them, re-audit. Compatible with Amp, Cline, Cursor, and GitHub Copilot. The MPL-2.0 license (rather than MIT) is worth noting for commercial integrations.

### cursor-a11y-mcp (westsideori)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [westsideori/cursor-a11y-mcp](https://github.com/westsideori/cursor-a11y-mcp) | 2 | JavaScript | MIT | 1 |

A single-tool server purpose-built for Cursor IDE integration. Provides comprehensive accessibility testing via axe-core and Puppeteer with detailed violation reports including impact levels, descriptions, help documentation, affected HTML elements, and failure summaries. Straightforward but limited compared to the multi-tool alternatives.

## Color Contrast Checking

Three dedicated servers solve the specific problem that **LLMs cannot accurately calculate WCAG contrast ratios** from training data — they need to run the actual WCAG contrast algorithm.

### a11y-color-contrast-mcp (ryelle)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ryelle/a11y-color-contrast-mcp](https://github.com/ryelle/a11y-color-contrast-mcp) | 2 | TypeScript | MIT | 3 |

Three focused tools: **get color contrast** (calculate WCAG ratio between two colors), **are colors accessible** (test against WCAG thresholds), and **use light or dark** (determine optimal text color for a given background). Clean, single-purpose design.

### mcp-wcag-color-contrast (bryanberger)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bryanberger/mcp-wcag-color-contrast](https://github.com/bryanberger/mcp-wcag-color-contrast) | 0 | TypeScript | MIT | 4 |

Built with Bun and the Culori color library. Includes **batch_contrast** for analyzing multiple color pairs simultaneously — useful for design system audits where you need to check an entire palette. Also provides luminance calculation and specific WCAG level compliance checking.

### AccessLint MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [accesslint/mcp-server](https://github.com/accesslint/mcp-server) | 1 | TypeScript | MIT | 3 |

From AccessLint, an established accessibility linting company. Uniquely includes **suggest_accessible_color** — given a color pair that fails WCAG, it proposes alternative colors that would pass. Also provides contrast ratio calculation and detailed color pair analysis for WCAG 2.1. Designed for integration with both Claude Desktop and the AccessLint marketplace plugin.

## WCAG Analysis & Remediation

### mcp-wcag-accessibility (alexanderuk82)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [alexanderuk82/mcp-wcag-accessibility](https://github.com/alexanderuk82/mcp-wcag-accessibility) | 0 | TypeScript | MIT | 10 |

The most ambitious remediation-focused server with **10 tools** spanning analysis, fixing, and documentation:

- **analyze_accessibility** — comprehensive WCAG audit
- **refactor_for_wcag** — automatic code refactoring to fix violations
- **validate_compliance** — check against specific WCAG levels
- **get_documentation** — retrieve relevant WCAG guidelines
- **annotate_code** — add accessibility annotations
- **accessibility_score** — generate an accessibility score
- **generate_component** — create accessible component templates
- **eslint_config** — generate ESLint configurations for accessibility rules
- **live_url_audit** — audit live URLs
- **wcag_github_sync** — sync with WCAG GitHub repository

Supports **multi-framework analysis** across HTML, React, Vue, and Angular. Available in 10 languages. The ESLint config generation is a practical touch — bake accessibility rules into the project's linting pipeline rather than relying solely on runtime audits. Runs 100% locally with no external API dependencies.

## Enterprise & Vendor Integration

### Deque axe MCP Server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dequelabs/axe-mcp-server-public](https://github.com/dequelabs/axe-mcp-server-public) | 3 | — | Proprietary | 2 |

**The most significant addition to the category since our original review.** Deque — the company that builds axe-core, the engine powering nearly every community accessibility MCP server — now has its own official MCP server with two tools:

- **analyze** — scan pages for accessibility violations using the full axe engine
- **remediate** — AI-powered code fixes for detected violations

Integrates with **Claude, GitHub Copilot, Cursor**, and any MCP-compatible AI coding agent. Included in Deque's Axe DevTools for Web bundle at no additional cost for existing customers. First announced at Axe-con 2025, now generally available.

**Requires a paid Axe DevTools for Web subscription** and an API key from axe.deque.com. This is the first time the upstream engine provider has entered the MCP space directly — creating an interesting dynamic where the community servers use Deque's open-source axe-core library for free, while Deque's own server adds proprietary remediation intelligence on top. Only 3 stars and 7 commits so far, suggesting early-stage adoption.

### BrowserStack MCP Server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [browserstack/mcp-server](https://github.com/browserstack/mcp-server) | 136 | TypeScript | — | 20+ |

BrowserStack's official MCP server includes accessibility as part of a broader testing suite (Live, App Live, Automate, screenshots). Now at 469 commits. The accessibility tools:

- **runAccessibilityScan** — automated WCAG/ADA compliance scanning with support for both public and local URLs (automatic tunnel management for private dev environments)
- **accessibilityExpert** — expert guidance on WCAG guidelines, usability, and accessibility best practices

Powered by **Spectra™**, BrowserStack's accessibility engine. The key differentiator: it analyzes violations in context, aligns fixes with your design system, and suggests **production-ready code** — not just violation reports. AI-generated contextual code fixes directly in the IDE.

**Requires a BrowserStack Accessibility license** — this is not a free tool. Available on AWS Marketplace. For teams already using BrowserStack, adding accessibility scanning to their AI workflow is straightforward.

## WCAG Reference & Knowledge

### wcag-mcp (joe-watkins)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [joe-watkins/wcag-mcp](https://github.com/joe-watkins/wcag-mcp) | 7 | JavaScript | MIT | 20 |

A **new addition** that fills a different niche: instead of scanning pages for violations, this server gives AI agents comprehensive access to the **WCAG 2.2 specification itself**. 20 tools spanning four categories:

- **Core WCAG tools** (9) — look up success criteria, filter by level/principle, search guidelines
- **Technique resources** (5) — browse 400+ WCAG techniques with applicability details
- **Glossary functions** (3) — access 101 WCAG glossary definitions
- **Enhanced context** (3) — get Understanding documentation for any success criterion

Covers all 87 success criteria across the four WCAG principles (Perceivable, Operable, Understandable, Robust) and 13 guidelines. Works locally via stdio and remotely through Netlify Functions.

This is genuinely useful for AI coding agents: rather than just detecting violations, an agent can look up the relevant WCAG guideline, understand the technique, and make an informed fix — combining well with any of the scanning servers above.

### accessibility-testing-mcp (joe-watkins)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [joe-watkins/accessibility-testing-mcp](https://github.com/joe-watkins/accessibility-testing-mcp) | 1 | JavaScript | MIT | 5 |

A **dual-engine accessibility testing server** that runs both **axe-core and IBM Equal Access** — the first MCP server to offer multiple accessibility testing engines in a single package. Five tools:

- **analyze_url / analyze_url_json** — test live URLs with either or both engines
- **analyze_html / analyze_html_json** — test HTML snippets
- **get_rules** — explore available rules

The IBM Equal Access engine catches some issues that axe-core misses (and vice versa), making this useful for teams wanting broader coverage. Multi-viewport testing supported. 21 commits.

## Color Blindness Simulation

### mcp-web-a11y (bilhasry-deriv)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bilhasry-deriv/mcp-web-a11y](https://github.com/bilhasry-deriv/mcp-web-a11y) | 4 | JavaScript | MIT | 2 |

Combines accessibility auditing with **color blindness simulation** — a unique pairing in the MCP ecosystem. Two tools:

- **check_accessibility** — standard axe-core WCAG scanning
- **simulate_colorblind** — renders pages through color matrices simulating protanopia (red-blind), deuteranopia (green-blind), and tritanopia (blue-blind)

The simulation feature generates screenshots showing how the page appears to users with different types of color vision deficiency. Useful for catching issues that pass automated contrast checks but still create problems for color-blind users — like using color alone to convey meaning (WCAG 1.4.1).

## Related: Accessibility Agents

### Community-Access/accessibility-agents

| Project | Stars | License | Agents |
|---------|-------|---------|--------|
| [Community-Access/accessibility-agents](https://github.com/Community-Access/accessibility-agents) | 236 | MIT | 79 |

Not an MCP server, but the **most ambitious accessibility-AI project** in the ecosystem — and it has surged from 186 to 236 stars (+27%) since March. Now at **v4.5.0** with **79 specialized agents** (up from 57+) organized into **eight teams** across **five platforms**:

- **Web Accessibility** — agents enforcing WCAG 2.2 AA standards
- **Document Accessibility** — agents for DOCX, XLSX, PPTX, PDF, EPUB, and Markdown
- **GitHub Workflow** — agents for CI/CD accessibility checks
- **Developer Tools** — agents for Python, wxPython, desktop accessibility, and NVDA addon development
- **Education & Standards** — new team for accessibility training and standards awareness
- Additional cross-cutting orchestrators and coordinators

Works with Claude Code, GitHub Copilot (VS Code and CLI), Gemini CLI, Claude Desktop, and Codex CLI. VS Code 1.113 compatibility improvements include "MCP across agent types" that bridges servers into Copilot CLI and Claude agents. 268 commits. The project notably emphasizes that "AI and automated tools are not perfect — they cannot replace testing with real screen readers."

At 236 stars, it has significantly more community traction than any individual accessibility MCP server.

## What's Missing

The accessibility MCP ecosystem has notable gaps:

- **Mobile accessibility** — no VoiceOver (iOS) or TalkBack (Android) testing servers
- **PDF/document accessibility** — no MCP server for PDF remediation, alt-text generation, or document structure validation (the Community-Access agents project partially addresses this)
- **Screen reader emulation** — no server simulates actual screen reader output (NVDA, JAWS, VoiceOver)
- **VPAT/ACR generation** — no automated Voluntary Product Accessibility Template creation
- **Accessibility management platforms** — no integrations with Level Access, eSSENTIAL Accessibility, or UserWay (Deque now has an official MCP server, but it requires a paid subscription)
- **Cognitive accessibility** — no tools for readability analysis, plain language checking, or cognitive load assessment (WCAG 2.1 Level AAA)
- **Automated remediation at scale** — individual page fixes work, but no server handles site-wide remediation campaigns

## The Bottom Line

**Rating: 3.5 / 5** — The accessibility MCP category continues to show strong tooling for web page auditing. The biggest development since March: **Deque — the company behind axe-core — launched an official MCP server** with analyze + remediate tools, making it the first upstream engine provider to enter the MCP accessibility space directly. However, it requires a paid subscription, so the free community scanners (a11ymcp at 83 stars, mcp-accessibility-scanner at 48 stars with 193 commits) remain the workhorses for most developers. A new WCAG reference server (joe-watkins/wcag-mcp, 20 tools) fills a knowledge gap by giving AI agents access to the full WCAG 2.2 specification. The Community-Access/accessibility-agents project surged to 236 stars with 79 agents across 8 teams — increasingly the go-to for comprehensive accessibility-AI workflows.

The rating holds at 3.5/5 rather than improving because the fundamental gaps remain unchanged: no mobile accessibility testing (VoiceOver, TalkBack), no PDF/document accessibility remediation via MCP, no screen reader emulation, and no VPAT/ACR generation. The category still suffers from fragmentation — 10+ servers doing variations of the same axe-core scan rather than one comprehensive solution. Deque's entry is positive signal but behind a paywall, and dual-engine testing (axe-core + IBM Equal Access) is only available in one low-visibility server. For web developers who want AI assistants that catch and fix WCAG violations during coding, the tooling is genuinely useful and getting more vendor attention.

*This review was last edited on 2026-04-21 using Claude Opus 4.6 (Anthropic).*
