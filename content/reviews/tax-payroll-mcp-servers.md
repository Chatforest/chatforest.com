---
title: "Tax & Payroll MCP Servers — IRS Calculations, Tax Filing, VAT Compliance, Payroll Management, and International Tax Law"
date: 2026-03-16T19:00:00+09:00
description: "Tax and payroll MCP servers let AI agents handle tax calculations, filing, compliance, and payroll management through the Model Context Protocol. We reviewed 15+ servers across 5 subcategories. US tax calculation (3 servers): dma9527/irs-taxpayer-mcp (TypeScript — 39 tools for federal/state tax calculations, credits, deductions, retirement strategies, TY2024+TY2025 with OBBB Act, all calculations local), gama104/GamaMcpServer (8 stars, C# — 30 capabilities including 9 tools, 18 resources, 3 prompts, OAuth 2.1 security, supports 1040/Schedule A/C for 2023-2025), jayanta8509/TAX_MCP (Python — LangChain + MySQL tax client management, Redis memory, GPT-4o-mini, dual client types). Tax filing & compliance (3 servers): TaxBandits Remote MCP Server (commercial — natural language W-9/1099 automation, IRS e-filing, compliance validation), Avalara MCP Servers (commercial — AvaTax calculation, Returns filing, E-Invoicing, Tax Registrations, Exemption Certificates), norman-finance/norman-mcp-server (8 stars, TypeScript — invoicing, bookkeeping, VAT filing, Finanzamt previews, German tax compliance). International tax (3 servers): kentaroajisaka/tax-law-mcp (TypeScript — Japanese tax law via e-Gov API, NTA administrative circulars, 1,950 tax ruling cases), ag2-mcp-servers/income-tax-department (Python — India PAN API from APISetuGov, auto-generated), rocketlang/mcp-tools (TypeScript — 282 India-first MCP tools including GST, e-Invoice, GSTR-3B, VAHAN, container tracking). Payroll & HR (3 servers): rocketsciencegg/rippling-mcp-server (TypeScript — Rippling HR/payroll, worker search, headcount snapshots, compensation summaries, org structure), merge-api/merge-mcp (Python — unified API for 70+ HRIS/payroll integrations including ADP, BambooHR, Workday, Paylocity), payroll-mcp-server (TypeScript + Express — salary management AI model interaction). Charity & nonprofit (1 server): briancasteel/charity-mcp-server (TypeScript — IRS charity database lookup, EIN verification, tax-deductible status, 14 prompt templates). Gaps: no TurboTax/H&R Block consumer tax prep, no ADP/Gusto/Paychex direct MCP servers, no UK HMRC self-assessment, no EU VAT OSS/IOSS, no Canadian CRA, no Australian ATO, no payroll tax calculation engines, no W-2 preparation, no 401k/benefits administration, no tax document OCR/parsing. Rating: 3.5/5."
og_description: "Tax & payroll MCP servers: irs-taxpayer-mcp (39 tools, local US tax calculations), Avalara (enterprise tax compliance), TaxBandits (W-9/1099 automation), Rippling (HR/payroll), Merge (70+ HRIS integrations), Japanese tax law, India GST tools. 15+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "Tax and payroll MCP servers for tax calculation, filing, compliance, and workforce management through AI assistants. This category is distinct from [Accounting & Bookkeeping](/reviews/accounting-bookkeeping-mcp-servers/) — that review covers general ledger platforms (Xero, QuickBooks, Zoho); this review covers tax-specific calculation, filing, compliance, and payroll/HR tools. **The US tax calculation space has a standout server** — dma9527/irs-taxpayer-mcp provides 39 tools covering federal/state brackets, AMT, NIIT, QBI deductions, SE tax, capital gains, CTC, and year-end optimization strategies (401k maxing, HSA, Roth conversion, tax-loss harvesting, charitable bunching), all running locally with no data leaving the machine. It supports TY2024 and TY2025 including the One Big Beautiful Bill Act. **Enterprise tax compliance is well-served** — Avalara ships five MCP servers (AvaTax, Returns, E-Invoicing, Tax Registrations, Exemption Certificates) and TaxBandits provides a remote MCP server for W-9/1099 automation with natural language commands. **International tax is emerging** — kentaroajisaka/tax-law-mcp provides direct access to Japanese tax statutes via the e-Gov API with 1,950 ruling cases, while rocketlang/mcp-tools offers 282 India-first tools including GST, e-Invoice, and GSTR-3B. **Payroll integration exists through aggregators** — merge-api/merge-mcp wraps 70+ HRIS/payroll platforms (ADP, BambooHR, Workday, Paylocity) through a unified API, and rocketsciencegg/rippling-mcp-server provides direct Rippling HR/payroll access. **Major gaps remain** — no consumer tax prep (TurboTax, H&R Block), no direct ADP or Gusto MCP servers, no UK HMRC, no Canadian CRA, no Australian ATO, no EU VAT OSS/IOSS, no payroll tax calculation engines, no W-2 generation, no benefits administration. The category earns 3.5/5 — irs-taxpayer-mcp is genuinely impressive for individual US tax planning, and enterprise tools from Avalara and TaxBandits bring production credibility, but payroll remains underserved and international coverage is sparse."
last_refreshed: 2026-03-16
---

Tax and payroll MCP servers connect AI agents to tax calculations, filing workflows, compliance checks, and workforce management systems. Instead of navigating tax software or payroll platforms manually, these servers let AI assistants compute tax liability, file returns, verify compliance, and query employee data — all through the Model Context Protocol.

This review covers **tax and payroll** — tax calculation engines, filing and compliance tools, international tax law, and payroll/HR integrations. For general accounting platforms (Xero, QuickBooks, Zoho Books, ledger tools), see our [Accounting & Bookkeeping review](/reviews/accounting-bookkeeping-mcp-servers/). For financial markets and trading, see our [Finance & Trading review](/reviews/finance-trading-mcp-servers/) if available.

The headline findings: **One standout US tax server exists** — irs-taxpayer-mcp provides 39 tools covering federal and state tax calculations, retirement strategies, and year-end optimization, all running locally. **Enterprise tax compliance has arrived** — Avalara ships five production MCP servers and TaxBandits offers natural-language W-9/1099 automation. **Payroll access comes through aggregators** — Merge wraps 70+ HRIS/payroll platforms, while Rippling has a direct MCP server. **International coverage is thin** — only Japan and India have dedicated tax law servers. **Consumer tax prep is absent** — no TurboTax, H&R Block, or similar.

---

## US Tax Calculation & Planning

### dma9527/irs-taxpayer-mcp — 39 Tools for Federal/State Tax

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [irs-taxpayer-mcp](https://github.com/dma9527/irs-taxpayer-mcp) | — | TypeScript | — | 39 |

**The most comprehensive individual tax MCP server in the ecosystem.** Provides 39 tools for US individual taxpayers covering the full federal and state tax landscape:

- **Federal tax calculations** — bracket breakdown, AMT (Alternative Minimum Tax), NIIT (3.8% Net Investment Income Tax), Additional Medicare Tax (0.9%), QBI deduction, self-employment tax, capital gains
- **Credits and deductions** — Child Tax Credit, standard vs. itemized deduction analysis, SALT cap handling
- **Retirement planning** — 401k maxing, HSA contributions, Roth conversion strategies, traditional vs. Roth IRA analysis
- **Year-end optimization** — personalized recommendations including tax-loss harvesting, charitable bunching, income timing, deduction acceleration
- **State tax** — multi-state tax calculations

Supports TY2024 and TY2025 including the **One Big Beautiful Bill Act** (OBBB Act) with updated bracket adjustments and SALT cap changes. All calculations run locally — no data leaves the machine. Published as an npm package for easy installation.

This is a genuinely useful tool for tax planning conversations — an AI assistant with this server can model "what if I max my 401k?" or "should I do a Roth conversion this year?" with real numbers.

### gama104/GamaMcpServer — Production-Ready C# Tax Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [GamaMcpServer](https://github.com/gama104/GamaMcpServer) | 8 | C# | — | 9 tools, 18 resources, 3 prompts |

A **production-ready MCP server** built in C# for tax-related operations. Validated against the MCP 2025-03-26 specification with 30 total capabilities:

- **9 tools** for tax data management
- **18 resources** for tax form data (1040, Schedule A, Schedule C for years 2023-2025)
- **3 prompts** for guided tax workflows
- **OAuth 2.1 security** with user-scoped data access

The C# implementation is unusual in the MCP ecosystem (most servers are TypeScript or Python), which makes it notable for .NET shops. The OAuth 2.1 integration suggests a multi-user production orientation rather than a local-only tool.

### jayanta8509/TAX_MCP — AI Tax Client Management

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [TAX_MCP](https://github.com/jayanta8509/TAX_MCP) | — | Python | — | Multiple |

An **AI-powered tax management system** that combines LangChain, MCP, and a MySQL database for tax client workflows:

- **Context awareness** — remembers previous interactions, tax forms discussed, and client details using Redis (12-hour TTL)
- **Privacy focused** — built-in rules prevent leaking internal Client IDs or reference types
- **Dual client support** — handles both "Company" and "Individual" client types with dynamic schema mapping
- **LLM-powered queries** — uses GPT-4o-mini via LangChain to convert natural language into database operations

More of a tax practice management tool than a calculator — designed for tax professionals managing multiple clients rather than individuals doing their own taxes. Requires Redis, MySQL, and an OpenAI API key.

---

## Tax Filing & Compliance

### TaxBandits Remote MCP Server — Natural Language IRS Filing

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [TaxBandits MCP](https://developer.taxbandits.com/docs/mcp/) | — | — | Commercial | Multiple |

**TaxBandits' remote MCP server** brings a new paradigm to tax form processing — issue plain-language commands and the system handles compliance, validation, and IRS transmission:

- **W-9 automation** — collect W-9 forms via email, text, secure URL, or Drop-in UI
- **1099 processing** — generate, validate, and e-file 1099-NEC, 1099-MISC, and other variants ("Generate 1099-NEC forms for all contractors who earned $600+ in 2024")
- **IRS e-filing** — direct submission with all compliance checks and validations
- **Additional forms** — W-2, 940, 941, 941 Schedule R, 1095, 1042-S
- **Recipient copies** — automated distribution of tax documents

This is a **commercial, hosted MCP server** — it connects to TaxBandits' existing API infrastructure. The natural-language interface sits on top of their battle-tested e-filing platform. Best suited for businesses and accounting firms handling volume filings.

### Avalara MCP Servers — Enterprise Tax Compliance Suite

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Avalara MCP Servers](https://developer.avalara.com/mcp-servers/) | — | — | Commercial | Multiple |

**Five production MCP servers** from Avalara, the enterprise tax compliance leader:

- **AvaTax** — real-time tax calculation, transaction management, nexus handling, compliance data
- **Returns** — tax returns management, filing calendars, compliance deadlines via the Global Returns API
- **E-Invoicing and Live Reporting** — international e-invoicing compliance
- **Tax Registrations and Business Licenses** — registration management across jurisdictions
- **Exemption Certificate Management** — certificate storage and validation

Avalara's MCP servers act as AI-ready guides to their APIs, exposing machine-readable descriptions of each service. This is enterprise tax infrastructure — transaction-level tax calculation across thousands of jurisdictions, automated filing, and compliance monitoring. Not for individual tax prep, but for businesses that need to collect and remit sales tax, VAT, or GST at scale.

### norman-finance/norman-mcp-server — German Tax Filing + Bookkeeping

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [norman-mcp-server](https://github.com/norman-finance/norman-mcp-server) | 8 | TypeScript | — | Multiple |

**Connects accounting, invoicing, and VAT filing** directly to Claude, Cursor, and any MCP-compatible AI:

- **Invoicing** — create, send, and track invoices including recurring and ZUGFeRD e-invoices
- **Bookkeeping** — categorize transactions, match receipts, verify entries
- **Tax filing** — generate Finanzamt previews, file VAT returns, track deadlines
- **Company overview** — balance, revenue, and financial health at a glance
- **Documents** — upload and attach receipts, invoices, and supporting files

Currently in **beta**. The German-market focus (Finanzamt, ZUGFeRD e-invoicing) fills a gap — most tax MCP servers target the US market. Norman bridges the gap between accounting and tax compliance for German businesses.

---

## International Tax

### kentaroajisaka/tax-law-mcp — Japanese Tax Statutes and Rulings

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tax-law-mcp](https://github.com/kentaroajisaka/tax-law-mcp) | — | TypeScript | — | Multiple |

An MCP server for **Japanese tax law** that pulls directly from official government sources:

- **e-Gov Law API v2** — retrieves Japanese tax law provisions in Markdown format
- **NTA administrative circulars** (通達) — National Tax Agency interpretive guidance
- **1,950 tax ruling cases** from the National Tax Appeals Bureau (kfs.go.jp)
- **Keyword cross-law search** — search across multiple tax statutes simultaneously
- **Table of contents** for administrative circular navigation
- **Hardcoded law IDs** for Income Tax Law, Corporate Tax Law, Consumption Tax Law, and other major statutes

Handles Shift_JIS encoding for NTA and Appeals Bureau content. Also provides REST API endpoints for use with Custom GPT and other AI tools. This is a genuinely useful tool for preventing AI hallucination in Japanese tax queries — it grounds responses in actual statute text rather than training data.

### ag2-mcp-servers/income-tax-department — India PAN API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [income-tax-department](https://github.com/ag2-mcp-servers/income-tax-department) | — | Python | — | Auto-generated |

An **auto-generated MCP server** wrapping India's PAN (Permanent Account Number) API from the government's API portal (apisetu.gov.in). Created by AG2's MCP builder — minimal manual curation. Useful as a bridge to Indian tax infrastructure but limited in scope to PAN verification.

### rocketlang/mcp-tools — 282 India-First MCP Tools

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-tools](https://github.com/rocketlang/mcp-tools) | — | TypeScript | MIT | 282 |

A **massive India-first MCP toolkit** with 282 tools covering tax, logistics, and government services:

- **GST compliance** — verification and calculations
- **e-Invoice** — India's electronic invoicing system integration
- **GSTR-3B reporting** — monthly GST return filing
- **VAHAN** — vehicle registration data
- **FASTag** — electronic toll collection
- **Container tracking, fleet management, banking**

Part of the ANKR Platform — India's AI-native enterprise operating system. The breadth is impressive (282 tools), though tax-specific tools are a subset of the total. This is the most comprehensive India-market MCP offering by a wide margin.

---

## Payroll & HR

### rocketsciencegg/rippling-mcp-server — Rippling HR & Payroll

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rippling-mcp-server](https://github.com/rocketsciencegg/rippling-mcp-server) | — | TypeScript | — | 5+ |

An MCP server for **Rippling** — one of the leading HR/payroll platforms:

- **search_workers** — search employees by name or email, returns name, title, department, manager, location, compensation
- **get_headcount_snapshot** — headcount by department and location, employment type breakdown, recent hires/departures (30-day window)
- **get_compensation_summary** — total cash compensation aggregated by department with min/max/avg ranges
- **get_org_structure** — department hierarchy, teams, manager names, direct report counts
- **get_worker_details** — full worker profile with compensation, level, and location

Clean, focused tool design — each tool returns shaped, useful data rather than raw API dumps. Good for HR analytics queries like "who reports to Sarah?" or "what's the average compensation in engineering?"

### merge-api/merge-mcp — Unified API for 70+ HRIS/Payroll Platforms

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [merge-mcp](https://github.com/merge-api/merge-mcp) | — | Python | — | Multiple |

Merge's MCP server provides a **single integration point for 70+ HRIS and payroll platforms**, including ADP, BambooHR, Workday, Paylocity, UKG Pro, Gusto, Justworks, and HRWorks:

- **Employee data** — profiles, employment history, titles, departments
- **Payroll runs** — employee pay statements for specific payroll periods
- **Company data** — organizational information from the HRIS
- **Employments** — position and compensation details

The power of Merge is abstraction — instead of building separate MCP integrations for ADP, Gusto, and Workday, you connect once through Merge and get access to all of them. Requires a Merge API key and account token. Tools depend on your enabled API category and scopes.

### payroll-mcp-server — Salary Management

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| payroll-mcp-server | — | TypeScript + Express | — | Multiple |

A **salary management MCP server** providing standard interfaces for interacting with payroll AI models. Built with TypeScript and Express, it exposes payroll management functionality for AI model interaction. Limited documentation available — appears to be an early-stage project.

---

## Charity & Nonprofit Tax

### briancasteel/charity-mcp-server — IRS Charity Verification

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [charity-mcp-server](https://github.com/briancasteel/charity-mcp-server) | — | TypeScript | — | 4 |

An **enterprise-grade MCP server** for charity and nonprofit organization data from the IRS database:

- **EIN lookup** — detailed information about any charity using their Tax ID, including official name, location, tax status, classification codes
- **Organization search** — search charities by name, city, or state with pagination and filtering
- **Tax-deductible verification** — quickly verify if an organization qualifies as a tax-deductible public charity
- **14 prompt templates** — guided charity verification workflows customizable by organization type

Useful for donors verifying tax-deductible status, nonprofits checking their own IRS records, or accountants confirming charitable contribution eligibility. Claims 100% implementation of all planned features with full type safety.

---

## What's Missing

The tax and payroll MCP space has significant gaps:

- **Consumer tax prep** — no TurboTax, H&R Block, or FreeTaxUSA MCP servers
- **Direct payroll platform servers** — no ADP, Gusto, or Paychex MCP servers (only aggregator access through Merge)
- **UK tax** — no HMRC self-assessment, no MTD (Making Tax Digital) MCP integration
- **EU VAT** — no VAT OSS (One Stop Shop) or IOSS (Import One Stop Shop) servers
- **Canadian tax** — no CRA (Canada Revenue Agency) integration
- **Australian tax** — no ATO (Australian Taxation Office) integration
- **Payroll tax engines** — no servers for calculating employer-side payroll taxes (FICA, FUTA, SUTA)
- **W-2 generation** — no MCP server for preparing and filing W-2 forms
- **Benefits administration** — no 401k, health insurance, or FSA/HSA administration servers
- **Tax document OCR** — no servers for parsing W-2s, 1099s, K-1s, or other tax documents from images/PDFs

---

## Bottom Line

The tax and payroll MCP category earns **3.5 out of 5**.

**What works well:** irs-taxpayer-mcp is genuinely impressive — 39 tools covering the full federal and state tax landscape with retirement optimization and year-end planning, all running locally with no data leakage. Avalara's five-server enterprise suite brings production tax compliance to MCP. TaxBandits makes W-9/1099 filing conversational. Japan's tax-law-mcp grounds AI responses in actual statute text.

**What needs work:** Payroll is the weakest link — no major payroll platform has an official MCP server, and access comes only through aggregators (Merge) or one platform-specific server (Rippling). International tax coverage is sparse — only Japan and India have dedicated servers, leaving the UK, EU, Canada, and Australia completely unserved. Consumer tax prep (the TurboTax/H&R Block experience) doesn't exist in MCP form. And there's no bridge between tax calculation and actual filing for individuals.

**Who benefits today:** US taxpayers doing tax planning (irs-taxpayer-mcp), businesses needing automated tax compliance (Avalara), firms filing volume 1099s (TaxBandits), companies using Rippling or platforms accessible through Merge (payroll queries), and Japanese tax professionals (tax-law-mcp). Everyone else is waiting.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
