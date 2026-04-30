# Tax & Payroll MCP Servers — IRS Calculations, Tax Filing, VAT Compliance, Payroll Management, and International Tax Law

> Tax and payroll MCP servers let AI agents handle tax calculations, filing, compliance, and payroll management through the Model Context Protocol.


Tax and payroll MCP servers connect AI agents to tax calculations, filing workflows, compliance checks, and workforce management systems. Instead of navigating tax software or payroll platforms manually, these servers let AI assistants compute tax liability, file returns, verify compliance, and query employee data — all through the Model Context Protocol.

This review covers **tax and payroll** — tax calculation engines, filing and compliance tools, international tax law, and payroll/HR integrations. For general accounting platforms (Xero, QuickBooks, Zoho Books, ledger tools), see our [Accounting & Bookkeeping review](/reviews/accounting-bookkeeping-mcp-servers/). For financial markets and trading, see our [Finance & Trading review](/reviews/personal-finance-mcp-servers/) if available.

The headline findings: **One standout US tax server exists** — irs-taxpayer-mcp (6 stars, 44 commits) provides 39 tools covering federal and state tax calculations, retirement strategies, and year-end optimization, all running locally. **Enterprise tax compliance has expanded** — Avalara now ships seven production MCP servers (up from five) and TaxBandits offers natural-language W-9/1099 automation. **The biggest international gap is filled** — durbs182/uk-tax-mcp provides a deterministic HMRC UK tax rule engine with 141 commits covering income tax, capital gains, dividends, pensions, and Scottish rates (TY2025-31). **Japanese tax law surged** — kentaroajisaka/tax-law-mcp reached 80 stars with 14 forks. **Payroll is strengthening** — PeopleSoft HCM MCP provides 41 tools for enterprise HR/payroll/benefits, and finance-calc-mcp adds FICA/FUTA/SUTA payroll tax calculations. **Consumer tax prep is still absent** — no TurboTax, H&R Block, or similar.

---

## US Tax Calculation & Planning

### dma9527/irs-taxpayer-mcp — 39 Tools for Federal/State Tax

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [irs-taxpayer-mcp](https://github.com/dma9527/irs-taxpayer-mcp) | 6 | TypeScript | MIT | 39 |

**The most comprehensive individual tax MCP server in the ecosystem.** Provides 39 tools for US individual taxpayers covering the full federal and state tax landscape:

- **Federal tax calculations** — bracket breakdown, AMT (Alternative Minimum Tax), NIIT (3.8% Net Investment Income Tax), Additional Medicare Tax (0.9%), QBI deduction, self-employment tax, capital gains
- **Credits and deductions** — Child Tax Credit, standard vs. itemized deduction analysis, SALT cap handling
- **Retirement planning** — 401k maxing, HSA contributions, Roth conversion strategies, traditional vs. Roth IRA analysis
- **Year-end optimization** — personalized recommendations including tax-loss harvesting, charitable bunching, income timing, deduction acceleration
- **State tax** — multi-state tax calculations

Supports TY2024 and TY2025 including the **One Big Beautiful Bill Act** (OBBB Act) with updated bracket adjustments and SALT cap changes. All calculations run locally — no data leaves the machine. Published as an npm package for easy installation.

This is a genuinely useful tool for tax planning conversations — an AI assistant with this server can model "what if I max my 401k?" or "should I do a Roth conversion this year?" with real numbers. Documentation available in English, Chinese, Spanish, and Japanese.

### FellowTraveler/finance-calc-mcp — Payroll Tax & Business Calculations

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [finance-calc-mcp](https://github.com/FellowTraveler/finance-calc-mcp) | — | Python | MIT | 10+ |

**The first MCP server to provide employer-side payroll tax calculations** — fills a gap that existed since the category's inception. Provides both an MCP server and CLI for financial calculations:

- **Payroll summaries** — FICA (Social Security + Medicare), FUTA, and SUTA calculations for employer payroll cost estimation
- **Federal income tax** — 2024 US bracket-by-bracket breakdowns for all filing statuses
- **Self-employment tax** — Social Security, Medicare, and additional Medicare surtax
- **Business tools** — gross margin, profit, markup, loan amortization, break-even analysis, depreciation schedules (straight-line and double-declining)

Single-command install via `uvx` — no cloning required. Integrates with Claude Desktop and other MCP clients. Created March 2026.

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
| [Avalara MCP Servers](https://developer.avalara.com/mcp-servers/) ([GitHub](https://github.com/avadev/mcp)) | 2 | — | Commercial | Multiple |

**Seven production MCP servers** from Avalara, the enterprise tax compliance leader (expanded from five):

- **AvaTax** — real-time tax calculation, transaction management, nexus handling, compliance data
- **Returns** — tax returns management, filing calendars, compliance deadlines via the Global Returns API
- **E-Invoicing and Live Reporting** — international e-invoicing compliance
- **Tax Registrations and Business Licenses** — registration management across jurisdictions
- **Exemption Certificate Management** — certificate storage and validation
- **Cross Border Trade** *(new)* — duty calculations, trade and tariff content libraries, import trade restrictions
- **Tax Content** *(new)* — access to Avalara's regularly updated tax content database

All servers use OAuth 2.1 authorization. Avalara's MCP servers act as AI-ready guides to their APIs, exposing machine-readable descriptions of each service. This is enterprise tax infrastructure — transaction-level tax calculation across thousands of jurisdictions, automated filing, and compliance monitoring. Not for individual tax prep, but for businesses that need to collect and remit sales tax, VAT, or GST at scale.

### norman-finance/norman-mcp-server — German Tax Filing + Bookkeeping

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [norman-mcp-server](https://github.com/norman-finance/norman-mcp-server) | 44 | Python | MIT | 10 skills |

**Surged from 8 to 44 stars** — the fastest-growing server in this category. Connects accounting, invoicing, and VAT filing directly to Claude, Cursor, ChatGPT, and OpenClaw:

- **Invoicing** — create, send, and track invoices including recurring and ZUGFeRD e-invoices
- **Bookkeeping** — categorize transactions, match receipts, verify entries
- **Tax filing** — generate Finanzamt previews, file VAT returns, track deadlines
- **Company overview** — balance, revenue, and financial health at a glance
- **Documents** — upload and attach receipts, invoices, and supporting files
- **10 ready-to-use skills** — financial overviews, invoice creation, client management, tax reporting, transaction categorization, receipt discovery via Gmail, payment reminders, expense analysis, deduction identification, monthly reconciliation

Now at v0.1.7 with 169 commits. OAuth 2.1 authentication. Supports local stdio, remote HTTP, and containerized deployment. Currently in **beta**. The German-market focus (Finanzamt, ZUGFeRD e-invoicing) fills a gap — most tax MCP servers target the US market.

---

## International Tax

### durbs182/uk-tax-mcp — HMRC UK Tax Rule Engine

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [uk-tax-mcp](https://github.com/durbs182/uk-tax-mcp) | — | Python | Private (NxLap Ltd) | 8 |

**Fills the single biggest international gap from our initial review.** A deterministic, auditable HMRC UK tax rule engine exposed via MCP — AI agents call tax computation tools rather than performing calculations themselves:

- **Income tax** — standard rUK and Scottish rates with all bands
- **Capital gains tax** — by asset type
- **Dividend tax** — with tax-free allowance calculations
- **Savings interest tax** — personal savings allowance
- **Pension taxation** — including UFPLS (Uncrystallised Funds Pension Lump Sum)
- **State Pension** — calculation tools
- **Tax years 2025-26 through 2030-31** — forward-looking coverage for both rUK and Scotland jurisdictions

The architecture is notably rigorous — six-layer design (AST schema, evaluator engine, DSL compiler, rule registry, validation pipeline, MCP server), `decimal.Decimal` arithmetic to prevent floating-point errors, SHA-256 hashing for rule reproducibility, and a mandatory human review gate before publication. All rules require HMRC source citations. No Turing-complete rules (no loops or recursion) — this is a deterministic calculator, not a programmable engine.

141 commits with 86/86 worked examples covering all published rules. Created April 2026.

### CSOAI-ORG/tax-calculator-ai-mcp — Multi-Country Tax Calculator

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tax-calculator-ai-mcp](https://github.com/CSOAI-ORG/tax-calculator-ai-mcp) | — | Python | MIT | 5 |

A **multi-country tax calculator** covering UK and US income tax, EU VAT, UK corporation tax, and capital gains tax:

- **Income tax** — progressive bracket calculations for UK and US
- **VAT** — EU/UK country-specific rates with standard, reduced, and zero rate types
- **Corporation tax** — UK rates with marginal relief
- **Capital gains tax** — UK calculations by asset classification
- **Tax deadlines** — UK and US jurisdiction deadlines

Free tier allows 15 calls/day. Available via pip and MCP registry. Created April 2026. The EU VAT coverage partially fills a gap — while not a full VAT OSS/IOSS implementation, it provides basic rate calculations across EU countries.

### kentaroajisaka/tax-law-mcp — Japanese Tax Statutes and Rulings

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tax-law-mcp](https://github.com/kentaroajisaka/tax-law-mcp) | 80 | TypeScript | — | Multiple |

**Surged to 80 stars with 14 forks** — proving strong demand for jurisdiction-specific tax law MCP servers. An MCP server for **Japanese tax law** that pulls directly from official government sources:

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

### rgrz/peoplesoft-mcp — PeopleSoft HCM (41 Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [peoplesoft-mcp](https://github.com/rgrz/peoplesoft-mcp) | 7 | Python | MIT | 41 |

**The most comprehensive enterprise HRIS/payroll MCP server.** Enables AI assistants to query and understand PeopleSoft HCM databases with 41 semantic tools across all major modules:

- **HR** (5 tools) — employee lookup, job history, department analysis, organizational hierarchy
- **Payroll** (5 tools) — calculation results, processing status, year-to-date balances, payment details
- **Benefits** (4 tools) — elections, dependents, beneficiaries
- **Performance** (3 tools) — reviews and search
- **PeopleTools** (18 tools) — record definitions, PeopleCode, SQL objects, introspection
- **Schema** (5 tools) — table descriptions, translate values, indexes
- **Direct Query** (1 tool) — custom SQL execution

Direct Oracle database access without JDBC. Built-in effective dating support and PeopleTools introspection. Four embedded resources provide guidance on PeopleSoft concepts, schema organization, query patterns, and architecture. Created February 2026.

### rocketsciencegg/rippling-mcp-server — Rippling HR & Payroll

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rippling-mcp-server](https://github.com/rocketsciencegg/rippling-mcp-server) | 3 | TypeScript | — | 5+ |

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

The tax and payroll MCP space has narrowed its gaps but significant ones remain:

- **Consumer tax prep** — no TurboTax, H&R Block, or FreeTaxUSA MCP servers
- **Direct payroll platform servers** — no ADP or Paychex MCP servers (only aggregator access through Merge); a Gusto MCP exists but is early-stage
- ~~**UK tax** — no HMRC self-assessment~~ **FILLED** — durbs182/uk-tax-mcp provides deterministic HMRC tax calculations
- **EU VAT** — basic rate calculations exist (tax-calculator-ai-mcp) but no full VAT OSS (One Stop Shop) or IOSS (Import One Stop Shop) servers
- **Canadian tax** — no CRA (Canada Revenue Agency) integration
- **Australian tax** — no ATO (Australian Taxation Office) integration
- ~~**Payroll tax engines**~~ **PARTIALLY FILLED** — finance-calc-mcp provides FICA, FUTA, and SUTA calculations
- **W-2 generation** — no MCP server for preparing and filing W-2 forms (TaxBandits handles W-2 but through their commercial API)
- **Benefits administration** — PeopleSoft covers benefit elections but no standalone 401k, health insurance, or FSA/HSA administration servers
- **Tax document OCR** — no tax-specific document parsing (general OCR MCP servers exist but none optimized for W-2s, 1099s, or K-1s)

---

## Bottom Line

The tax and payroll MCP category earns **4 out of 5** — up from 3.5 in the initial review.

**What works well:** irs-taxpayer-mcp remains the standout — 39 tools for US individual tax planning, all running locally. Avalara has expanded to seven enterprise servers including cross-border trade and tax content. The **biggest improvement** is international: durbs182/uk-tax-mcp fills the HMRC gap with a rigorous, deterministic UK tax engine (141 commits, 86 worked examples, SHA-256 reproducibility), and kentaroajisaka/tax-law-mcp surged to 80 stars proving demand for jurisdiction-specific servers. Norman's 44-star growth validates German tax/VAT automation. TaxBandits continues to lead commercial filing.

**What's improved:** Three major gaps from the initial review are now filled or partially filled — UK HMRC tax (fully filled), payroll tax calculations with FICA/FUTA/SUTA (finance-calc-mcp), and EU VAT rate calculations (tax-calculator-ai-mcp). PeopleSoft HCM adds enterprise-grade HRIS/payroll with 41 tools covering HR, payroll, benefits, and performance.

**What needs work:** Consumer tax prep (TurboTax/H&R Block) remains absent. No major payroll platform has an official MCP server — access still comes through aggregators (Merge) or limited platform-specific servers (Rippling, PeopleSoft). Canada (CRA) and Australia (ATO) have no coverage. Benefits administration and W-2 generation remain underserved.

**Who benefits today:** US taxpayers doing tax planning (irs-taxpayer-mcp), UK taxpayers calculating income tax/CGT/dividends/pensions (uk-tax-mcp), German entrepreneurs managing VAT and bookkeeping (Norman), businesses needing enterprise tax compliance (Avalara's seven servers), firms filing volume 1099s (TaxBandits), enterprises on PeopleSoft HCM (peoplesoft-mcp), companies using Merge's 70+ HRIS integrations, Japanese tax professionals (tax-law-mcp), and Indian businesses with GST/e-Invoice needs (rocketlang).

**Category**: [Finance & Fintech](/categories/finance-fintech/)

*This review was refreshed on 2026-04-30 using Claude Opus 4.6 (Anthropic). Initial review: 2026-03-16.*

