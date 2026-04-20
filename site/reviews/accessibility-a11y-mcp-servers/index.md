# Accessibility & a11y MCP Servers — Axe-Core, WCAG Auditing, Color Contrast, BrowserStack, and More

> Accessibility and a11y MCP servers are enabling AI-powered WCAG compliance testing and remediation. We reviewed 20+ servers across 5 subcategories.


Accessibility MCP servers are bringing automated WCAG compliance testing directly into AI coding workflows. Instead of switching to browser DevTools or running manual audits, these servers let AI agents scan pages for violations, check color contrast ratios, validate ARIA attributes, and even refactor code to fix accessibility issues — all through the Model Context Protocol.

The landscape spans five areas: **full-page auditing** (axe-core-powered scanners), **color contrast checking** (dedicated contrast ratio tools), **WCAG analysis & remediation** (code-level fixing), **enterprise integration** (BrowserStack), and **color blindness simulation** (visual impairment previews).

The headline findings: **Three competing axe-core scanners** dominate the category — ronantakizawa/a11ymcp (78 stars, 5,000+ downloads), JustasMonkev's mcp-accessibility-scanner (43 stars, 15+ tools), and priyankark/a11y-mcp (40 stars). All three use the same underlying engine (Deque's axe-core, also used by Google Lighthouse and Microsoft Accessibility Insights) but differ in scope and tool design. **The most capable scanner is JustasMonkev's**, with Playwright-based multi-page crawling, keyboard navigation testing, and matrix scanning across viewport variants. **BrowserStack is the only major vendor** with accessibility in its official MCP server (130 stars) — powered by Spectra with AI-generated code fixes, but requires a paid license. **Three dedicated color contrast servers** exist for precise WCAG ratio checking — solving the real problem that LLMs hallucinate contrast ratios when calculating them from training data alone. **The biggest gap is what's missing**: no mobile accessibility testing (VoiceOver, TalkBack), no PDF/document accessibility remediation, no screen reader emulation, and no accessibility management platform integrations.

**Category:** [Developer Tools](/categories/developer-tools/)

---

## Full-Page Auditing

### a11ymcp (ronantakizawa)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ronantakizawa/a11ymcp](https://github.com/ronantakizawa/a11ymcp) | 78 | JavaScript | MIT | 6 |

The most popular accessibility MCP server, with **5,000+ downloads** and a **#20 ranking on ProductHunt**. Uses axe-core and Puppeteer to provide six distinct tools:

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
| [JustasMonkev/mcp-accessibility-scanner](https://github.com/JustasMonkev/mcp-accessibility-scanner) | 43 | JavaScript | — | 15+ |

The **most comprehensive accessibility scanner** in the MCP ecosystem. Built on Playwright (not Puppeteer), which enables richer browser automation and persistent sessions.

Core scanning tools:
- **scan_page** — WCAG compliance checks across 2.0/2.1/2.2 at A/AA/AAA levels
- **audit_site** — multi-page crawling with aggregated violation reporting
- **scan_page_matrix** — variant comparison across mobile, desktop, zoom, and reduced-motion configurations
- **audit_keyboard** — real keyboard navigation testing (not just static analysis)

Plus full browser automation: navigate, click, type, hover, drag, select, take screenshots, save PDFs, manage tabs, and resize viewports. The 161 commits suggest active, ongoing development.

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

## Enterprise & IDE Integration

### BrowserStack MCP Server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [browserstack/mcp-server](https://github.com/browserstack/mcp-server) | 130 | TypeScript | — | 20+ |

BrowserStack's official MCP server includes accessibility as part of a broader testing suite (Live, App Live, Automate, screenshots). The accessibility tools:

- **runAccessibilityScan** — automated WCAG/ADA compliance scanning with support for both public and local URLs (automatic tunnel management for private dev environments)
- **accessibilityExpert** — expert guidance on WCAG guidelines, usability, and accessibility best practices

Powered by **Spectra™**, BrowserStack's accessibility engine. The key differentiator: it analyzes violations in context, aligns fixes with your design system, and suggests **production-ready code** — not just violation reports. AI-generated contextual code fixes directly in the IDE.

**Requires a BrowserStack Accessibility license** — this is not a free tool. Available on AWS Marketplace. The 130 stars and 457 commits indicate substantial investment and active maintenance. For teams already using BrowserStack, adding accessibility scanning to their AI workflow is straightforward.

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
| [Community-Access/accessibility-agents](https://github.com/Community-Access/accessibility-agents) | 186 | MIT | 57+ |

Not an MCP server, but the **most ambitious accessibility-AI project** in the ecosystem. Provides 57+ specialized agents organized into five teams:

- **Web Accessibility** — 17 agents enforcing WCAG 2.2 AA standards
- **Document Accessibility** — agents for DOCX, XLSX, PPTX, PDF, EPUB, and Markdown
- **GitHub Workflow** — 11 agents for CI/CD accessibility checks
- **Developer Tools** — 7 agents for Python, wxPython, desktop accessibility, and NVDA addon development
- **Cross-cutting** — orchestrators and coordinators

Works with Claude Code, GitHub Copilot, Gemini CLI, Claude Desktop, and Codex CLI. The document accessibility team is particularly notable — it fills a gap that no MCP server currently addresses. At 186 stars, it has more community traction than any individual accessibility MCP server.

## What's Missing

The accessibility MCP ecosystem has notable gaps:

- **Mobile accessibility** — no VoiceOver (iOS) or TalkBack (Android) testing servers
- **PDF/document accessibility** — no MCP server for PDF remediation, alt-text generation, or document structure validation (the Community-Access agents project partially addresses this)
- **Screen reader emulation** — no server simulates actual screen reader output (NVDA, JAWS, VoiceOver)
- **VPAT/ACR generation** — no automated Voluntary Product Accessibility Template creation
- **Accessibility management platforms** — no integrations with Level Access, Deque (beyond axe-core), eSSENTIAL Accessibility, or UserWay
- **Cognitive accessibility** — no tools for readability analysis, plain language checking, or cognitive load assessment (WCAG 2.1 Level AAA)
- **Automated remediation at scale** — individual page fixes work, but no server handles site-wide remediation campaigns

## The Bottom Line

**Rating: 3.5 / 5** — The accessibility MCP category has surprisingly strong tooling for web page auditing, with three competing axe-core scanners (78, 43, and 40 stars respectively) and BrowserStack providing enterprise-grade coverage. The "audit → fix → re-audit" agentic loop is well-supported. Color contrast checking is thoroughly covered by three dedicated servers solving the real problem of LLM contrast hallucination. The WCAG remediation tools (particularly alexanderuk82's 10-tool server) and the Community-Access agents project (186 stars, 57+ agents) show strong community investment in making AI coding tools produce accessible code by default.

The deductions come from the ecosystem's narrow focus on web page auditing — mobile accessibility, document remediation, screen reader testing, and enterprise platform integrations are all absent. The category also suffers from fragmentation: 10+ servers doing variations of the same axe-core scan, rather than one comprehensive solution. Still, for web developers who want AI assistants that catch and fix WCAG violations during coding, the tooling is genuinely useful today.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

