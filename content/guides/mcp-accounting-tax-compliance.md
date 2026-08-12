---
title: "MCP for Accounting — 95+ Integrations (2026)"
date: 2026-03-29T23:30:00+09:00
description: "95+ MCP servers for accounting — QuickBooks, Xero, Sage, NetSuite, tax prep, invoicing, payroll, expense management, and compliance. Which ones are production-ready?"
og_description: "How AI agents connect to accounting tools via MCP. Covers QuickBooks, Xero, Sage Intacct, NetSuite, Zoho Books, tax preparation, and 90+ more integrations."
content_type: "Guide"
card_description: "95+ MCP servers for accounting and finance — QuickBooks, Xero, Sage, NetSuite, tax prep, invoicing, payroll, and compliance. Architecture patterns for AI-powered reconciliation and automated tax filing."
last_refreshed: 2026-08-12
lastmod: 2026-08-12
sources_audited: 2026-08-12
---

Accounting runs on fragmented software. A typical small business might track income in QuickBooks, send invoices through FreshBooks, manage expenses via Brex, run payroll through Gusto, file taxes using country-specific software, reconcile bank accounts through Plaid, and produce financial reports in spreadsheets — each system holding a piece of the financial picture, each requiring manual data transfer between them. The global AI-in-accounting market reached [$10.87 billion in 2026, growing at 44.6% annually toward a projected $68.75 billion by 2031](https://www.mordorintelligence.com/industry-reports/artificial-intelligence-in-accounting-market). The [automated bookkeeping segment alone is growing at 46.1% CAGR](https://www.mordorintelligence.com/industry-reports/artificial-intelligence-in-accounting-market). Among U.S. accountants, [46% now use AI daily, and 81% report measurable productivity gains](https://www.firmofthefuture.com/news/accountant-tech-survey-2025/).

MCP — the Model Context Protocol — provides a standardized way for AI agents to connect to these accounting platforms. Rather than building custom integrations for each tool, MCP-connected agents can query financial data, create journal entries, generate invoices, reconcile transactions, and produce reports through defined tool interfaces. The protocol transforms AI assistants from isolated chatbots into operational accounting tools that can work across bookkeeping, invoicing, tax preparation, payroll, and audit workflows. For an introduction to MCP itself, see our [introduction to MCP](/guides/what-is-mcp/).

The accounting MCP ecosystem is remarkably mature. Six major accounting vendors have shipped official MCP implementations: Intuit/QuickBooks ([351 stars](https://github.com/intuit/quickbooks-online-mcp-server), open source), Xero ([350 stars](https://github.com/XeroAPI/xero-mcp-server), open source), Sage Intacct ([AI Gateway on its developer portal](https://developer.sage.com/intacct/ais/intacct-ai-gateway/latest/intacct-ai-gateway/tools)), Zoho ([15+ app coverage](https://www.zoho.com/blog/books/model-context-protocol-accounting-software.html)), Oracle/NetSuite ([built into platform](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_7200233106.html)), and Microsoft Dynamics 365 ([built into platform](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp)). Stripe's AI toolkit (formerly agent-toolkit) has [1,737 stars](https://github.com/stripe/ai) for payment processing. Community implementations cover everything from plain-text double-entry bookkeeping (Ledger CLI, Beancount, GnuCash) to tax law databases spanning the US, Japan, France, Korea, Portugal, and Denmark. Unified API platforms like CData Connect AI and Unified.to provide broad multi-platform coverage.

This guide is research-based. We survey what MCP servers exist across the accounting and financial compliance landscape, analyze the architecture patterns they enable, and identify where significant gaps remain. We do not claim to have tested or used any of these servers hands-on — our analysis draws on published documentation, open-source repositories, vendor announcements, and industry research. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI. For background on MCP, see our [introduction to MCP](/guides/what-is-mcp/) and the [MCP server directory](/reviews/).

## Why Accounting Needs MCP

Accounting workflows present integration challenges that MCP is architecturally well-suited to address.

**Financial data lives in too many systems.** A single month-end close might require pulling data from a general ledger, bank feeds, payment processors, expense reports, payroll, accounts receivable, and accounts payable — each in a different platform with a different API. An MCP-connected AI agent that can read across all these systems could automate reconciliation workflows that currently take days.

**Bookkeeping is repetitive and rule-driven.** Categorizing transactions, matching invoices to payments, reconciling bank statements, and posting journal entries follow well-defined patterns. These are ideal candidates for AI automation through MCP — agents can read transaction data, apply categorization rules, and write entries back to the general ledger.

**Tax compliance varies dramatically by jurisdiction.** A business operating across borders faces different tax codes, filing deadlines, reporting formats, and regulatory requirements in each country. MCP servers that expose tax law databases and filing APIs let AI agents help navigate multi-jurisdictional compliance without building country-specific integrations from scratch.

**Audit trails must be comprehensive and continuous.** SOX compliance, internal audits, and external audit preparation require documenting what was accessed, what was changed, and why. MCP's structured tool interfaces provide clearer audit trails than ad-hoc API integrations — every agent action is logged with its tool call parameters and results.

**Small businesses need enterprise-grade automation at SMB prices.** The 46.1% CAGR in automated bookkeeping reflects intense demand from businesses too small for dedicated accounting staff but too complex for spreadsheets. MCP-connected agents can bring sophisticated financial automation to businesses using QuickBooks, Xero, or Wave without enterprise software budgets.

## Accounting Platform MCP Servers

The core accounting platforms have the strongest MCP coverage of any vertical we've surveyed, with six major vendors shipping official implementations.

### QuickBooks (Intuit) — Official

Intuit's official QuickBooks Online MCP server is one of the most complete vendor implementations in the MCP ecosystem.

**[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | 351 stars | **Official by Intuit** | OAuth 2.0

According to repository documentation, the official server provides SQL-like queries across Customers, Vendors, Invoices, Bills, Accounts, Items, and Departments. Financial reports include Profit & Loss, Balance Sheet, and Trial Balance. Full CRUD operations cover journal entries, bills, expenses, sales receipts, invoices, deposits, and vendor credits. OAuth 2.0 authentication ensures proper access control.

**[Scottcjn/qb-auto](https://github.com/Scottcjn/qb-auto)** | 48 stars | 8 automation tools

A focused alternative that replaces 50K-token accounting data snapshots with ~200-token targeted extractions — an efficiency-first approach for AI agents working with large QuickBooks datasets.

**[CDataSoftware/quickbooks-mcp-server-by-cdata](https://github.com/CDataSoftware/quickbooks-mcp-server-by-cdata)** | 18 stars | Read-only via CData JDBC

Read-only access to QuickBooks data through CData drivers. Natural language queries without writing SQL. Full CRUD available through the managed CData Connect AI platform.

**Additional community servers:** [nikhilgy/quickbooks-mcp-server](https://github.com/nikhilgy/quickbooks-mcp-server) (10 stars, all public QuickBooks APIs), [aallsbury/qb-time-mcp-server](https://github.com/aallsbury/qb-time-mcp-server) (11 stars, QuickBooks Time API), [laf-rge/quickbooks-mcp](https://github.com/laf-rge/quickbooks-mcp) (11 stars), [vespo92/QBO-MCP-TS](https://github.com/vespo92/QBO-MCP-TS) (3 stars, TypeScript), [LibreChat-AI/quickbooks-online-mcp](https://github.com/LibreChat-AI/quickbooks-online-mcp) (8 stars, Cloudflare Workers with Streamable HTTP/SSE).

### Xero — Official

Xero's official MCP server provides the broadest API coverage of any accounting MCP implementation.

**[XeroAPI/xero-mcp-server](https://github.com/XeroAPI/xero-mcp-server)** | 350 stars | **Official by Xero** | 50+ tools | OAuth 2.0

The [official server's README](https://github.com/XeroAPI/xero-mcp-server) lists 50+ MCP tools/commands covering contacts, chart of accounts, invoices, and other core Xero accounting objects, and points to Xero's full API documentation for complete endpoint coverage. It's the highest-starred official accounting MCP server. Xero also publishes the **[xero-agent-toolkit](https://github.com/XeroAPI/xero-agent-toolkit)** (54 stars) with examples for building AI agents on top of the Xero API.

**[john-zhang-dev/xero-mcp](https://github.com/john-zhang-dev/xero-mcp)** | 21 stars | Community alternative

Community Xero MCP implementation providing an alternative interface.

**[ag2-mcp-servers](https://github.com/ag2-mcp-servers) auto-generated suite:** Five auto-generated servers covering xero-accounting-api, xero-payroll-au-api, xero-bank-feeds-api, xero-assets-api, and xero-files-api. Generated by mcp.ag2.ai for comprehensive Xero API coverage.

### Sage Intacct — Official

**Sage Intacct AI Gateway / MCP Server** | **Official** | [developer.sage.com](https://developer.sage.com/intacct/ais/intacct-ai-gateway/latest/intacct-ai-gateway/tools)

Sage's official MCP implementation ships as an "[AI Gateway](https://www.sage.com/en-us/sage-business-cloud/intacct/product-capabilities/platform/ai-gateway/)" built into Intacct's R2 2026 release, described by Sage as "a single, structured entry point into financial data that requires no custom integration work." It's a read-only, OAuth 2.0-secured REST API accessible via the Model Context Protocol, letting tools like Claude, Microsoft Copilot, and Cursor connect directly to Intacct financial data — see [independent coverage of the R2 2026 rollout](https://www.erpimplementation.eu/en/sage-intacct-ai-gateway-mcp-llm-integration-r2-2026/). It's available through Sage's developer portal rather than open source on GitHub. Sage targets mid-market and enterprise customers where Intacct has strong penetration in accounting firms and growing companies.

**[CDataSoftware/sage-cloud-accounting-mcp-server-by-cdata](https://github.com/CDataSoftware/sage-cloud-accounting-mcp-server-by-cdata)** | Read-only

Read-only access to Sage Cloud Accounting data via CData JDBC drivers.

### Zoho Books — Official

**[Zoho MCP](https://www.zoho.com/mcp/)** | **Official** | [zoho.com/mcp](https://www.zoho.com/mcp/)

Zoho [announced Zia LLM, Zoho AI Agents, and Zoho MCP together on July 17, 2025](https://www.zoho.com/mcp/); the platform connects AI agents to CRM, Books, Desk, and [15+ other Zoho apps](https://www.zoho.com/blog/books/model-context-protocol-accounting-software.html). [Zoho Books MCP](https://www.zoho.com/us/books/help/mcp/zoho-books-mcp.html) is live, with setup documentation covering invoice creation, expense recording, and bank-statement reconciliation via natural-language prompts, and is available as a Claude connector. The cross-app coverage is significant — an AI agent could read a customer record from Zoho CRM, create an invoice in Zoho Books, and send it via Zoho Mail through a single MCP integration layer.

**[kkeeling/zoho-mcp](https://github.com/kkeeling/zoho-mcp)** | 39 stars | Community | Python

Tools for invoices, contacts, expenses, items, and sales orders. The most popular community Zoho MCP server.

**Additional Zoho servers:** [Mgabr90/zoho-mcp-server](https://github.com/Mgabr90/zoho-mcp-server) (2 stars, unified CRM + Books with AnythingLLM), [bu5hm4nn/zoho-bookkeeper-mcp](https://github.com/bu5hm4nn/zoho-bookkeeper-mcp) (bookkeeping workflows with AI agents), [CDataSoftware/zoho-books-mcp-server-by-cdata](https://github.com/CDataSoftware/zoho-books-mcp-server-by-cdata) (read-only), [zoho/analytics-mcp-server](https://github.com/zoho/analytics-mcp-server) (official analytics MCP).

### Oracle NetSuite — Official

**[Oracle NetSuite AI Connector Service](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_7200233106.html)** | **Official** | Built into NetSuite platform

Oracle's official NetSuite documentation confirms NetSuite "has adopted the Model Context Protocol (MCP)" via the AI Connector Service and its **MCP Standard Tools SuiteApp**, which exposes NetSuite data (including SuiteQL access) plus custom tools and MCP Apps to external AI clients under NetSuite's existing role-based permissions.

**[dsvantien/netsuite-mcp-server](https://github.com/dsvantien/netsuite-mcp-server)** | 19 stars | Listed on [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | OAuth 2.0 with PKCE

Community implementation listed on the official MCP servers directory.

**[CDataSoftware/netsuite-mcp-server-by-cdata](https://github.com/CDataSoftware/netsuite-mcp-server-by-cdata)** | 9 stars | Read-only via CData JDBC

**[Improvado](https://improvado.io/mcp/oracle-netsuite)** — Hosted, commercial MCP for NetSuite connecting via NetSuite's SuiteQL API with natural-language queries across financials, operations, and custom records.

### Microsoft Dynamics 365 — Official

**[Dynamics 365 ERP MCP Server](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp)** | **Official by Microsoft**

Microsoft's official MCP implementation for Dynamics 365 covers Finance, Supply Chain, HR, and Project Operations. Per Microsoft's [Use Model Context Protocol for finance and operations apps documentation](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp), it provides three tool categories: Data tools (CRUD operations against data entities), Form tools (navigate ERP forms the way a user would), and Action tools (invoke business-logic classes directly), together exposing "over 650,000 operations across the Dynamics 365 ERP suite" while respecting role-based security. Microsoft's [Dynamics 365 ERP MCP documentation](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/build-agent-mcp) states: "The recommended model for agents using the Dynamics 365 ERP MCP server is Claude Sonnet 4.5. This model provides a better success rate in Copilot Studio over other default models like GPT-4.1."

**[Dynamics 365 ERP Analytics MCP](https://learn.microsoft.com/en-us/dynamics365/finance/business-performance-analytics/erp-analytics-mcp-overview)** | **Official (preview)** | Business Performance Analytics

Covers Record-to-Report, Procure-to-Pay, and Order-to-Cash value chains with analytics-focused MCP tools, per Microsoft's documentation. It's currently a preview feature, requiring Dynamics 365 finance and operations 10.0.38+ and Business performance analytics 2.4.3224+.

### Other Accounting Platforms

**FreshBooks:** [LokiMCPUniverse/freshbooks-mcp-server](https://github.com/LokiMCPUniverse/freshbooks-mcp-server) (2 stars), [GomezMera-IO-LLC/gm-freshbooks-mcp](https://github.com/GomezMera-IO-LLC/gm-freshbooks-mcp), [BusyBee3333/freshbooks-mcp-2026-complete](https://github.com/BusyBee3333/freshbooks-mcp-2026-complete) (100+ tools), [Good-Samaritan-Software-LLC/freshbooks-mcp](https://github.com/Good-Samaritan-Software-LLC/freshbooks-mcp) (full API parity, OAuth2).

**Wave Financial:** [BusyBee3333/wave-mcp-2026-complete](https://github.com/BusyBee3333/wave-mcp-2026-complete) (100+ tools covering invoicing, customers, products, transactions, bills, estimates, taxes, reporting), [vinnividivicci/wave_mcp](https://github.com/vinnividivicci/wave_mcp) (expense tracking, multi-business), [CDataSoftware/wave-financial-mcp-server-by-cdata](https://github.com/CDataSoftware/wave-financial-mcp-server-by-cdata) (read-only).

**Tally ERP:** [dhananjay1405/tally-mcp-server](https://github.com/dhananjay1405/tally-mcp-server) (67 stars, Tally Prime integration), [CDataSoftware/tally-mcp-server-by-cdata](https://github.com/CDataSoftware/tally-mcp-server-by-cdata) (read-only).

**Regional platforms:** [marcusquinn/quickfile-mcp](https://github.com/marcusquinn/quickfile-mcp) (4 stars, QuickFile UK accounting), [samaxbytez/freeagent-mcp](https://github.com/samaxbytez/freeagent-mcp) (FreeAgent for UK sole traders), [klausagnoletti/e-conomic-mcp-server](https://github.com/klausagnoletti/e-conomic-mcp-server) (Danish e-conomic platform), [CDataSoftware/myob-accountright-mcp-server-by-cdata](https://github.com/CDataSoftware/myob-accountright-mcp-server-by-cdata) (Australian MYOB via CData).

## Bookkeeping and Double-Entry Accounting

Beyond cloud accounting platforms, a distinct ecosystem serves accountants and developers who prefer plain-text or open-source bookkeeping tools.

### Plain-Text Accounting

**[minhyeoky/mcp-server-ledger](https://github.com/minhyeoky/mcp-server-ledger)** | 51 stars | Ledger CLI

Exposes the Ledger CLI double-entry accounting system through MCP, providing financial reporting and budget analysis tools. Ledger CLI is popular among technical users who track finances in plain text files under version control — MCP adds an AI query layer on top.

**[vanto/beanquery-mcp](https://github.com/vanto/beanquery-mcp)** | 51 stars | Beancount

BQL (Beancount Query Language) access through MCP. Beancount is a Python-based double-entry bookkeeping system where transactions are stored as plain text. The MCP server allows AI agents to query financial data using BQL.

**[StdioA/beancount-mcp](https://github.com/StdioA/beancount-mcp)** | 11 stars | Beancount query and transaction submission.

### GnuCash

**[ninetails-io/gnucash-mcp](https://github.com/ninetails-io/gnucash-mcp)** | 58 stars | 15 core tools

Read/write access to GnuCash data with 15 core tools plus optional reporting and reconciliation modules. GnuCash is the most widely used open-source desktop accounting application.

### Bookkeeping-Focused Servers

**[vanderheijden86/moneybird-mcp-server](https://github.com/vanderheijden86/moneybird-mcp-server)** | 28 stars | Moneybird (Dutch platform)

AI-powered bookkeeping for the Moneybird platform, popular in the Netherlands for small business accounting.

**[norman-finance/norman-mcp-server](https://github.com/norman-finance/norman-mcp-server)** | 54 stars | European bookkeeping + tax filing

AI-powered bookkeeping and automated tax filing for European entrepreneurs. Combines double-entry bookkeeping with compliance automation.

**[EDSTeam/hakan-accounting-mcp](https://github.com/EDSTeam/hakan-accounting-mcp)** | Swedish compliance, double-entry bookkeeping, financial reporting.

**[youssefaltai/finance-mcp](https://github.com/youssefaltai/finance-mcp)** | Double-entry bookkeeping with 18 tools, PostgreSQL backend.

**[rivradev/recite-mcp](https://github.com/rivradev/recite-mcp)** | Receipt processing with local ledger bookkeeping.

**[AccountantInc/mcp-kiko](https://github.com/AccountantInc/mcp-kiko)** | KikoBooks, 50 tools for accounts, invoices, bills, payments, and journal entries.

## Tax Preparation and Tax Law

Tax preparation is heavily jurisdiction-specific, and the MCP ecosystem reflects this with servers covering US, Japanese, French, Korean, Portuguese, and Danish tax systems.

### United States

**[dma9527/irs-taxpayer-mcp](https://github.com/dma9527/irs-taxpayer-mcp)** | 8 stars | 39 tools

US individual taxpayer tools covering federal and state tax calculations, credits, deductions, and retirement strategies for tax years 2024 and 2025, with full SE tax breakdown (Schedule C profit, SE tax, QBI deduction, quarterly payments). The most comprehensive US-focused tax MCP server.

### Japan

**[kentaroajisaka/tax-law-mcp](https://github.com/kentaroajisaka/tax-law-mcp)** | 94 stars | Japanese tax law

The highest-starred tax MCP server overall. Provides access to Japan's e-Gov API and National Tax Agency administrative circulars. Enables AI agents to look up and reason about Japanese tax regulations.

**[yamayued/houjin-bangou-api-mcp](https://github.com/yamayued/houjin-bangou-api-mcp)** | Japan NTA Corporate Number API.

### Europe

**[norman-finance/norman-mcp-server](https://github.com/norman-finance/norman-mcp-server)** | 54 stars | European bookkeeping + tax filing automation.

**[cornelcroi/french-tax-mcp](https://github.com/cornelcroi/french-tax-mcp)** | 14 stars | French tax calculations and guidance.

**[Bloomidea/saft-mcp](https://github.com/Bloomidea/saft-mcp)** | Portuguese SAF-T (Standard Audit File for Tax) — validate, query, and extract data from SAF-T XML files, which are mandatory for Portuguese tax reporting.

**[srivatsahg/mcp-statistics-denmark](https://github.com/srivatsahg/mcp-statistics-denmark)** | Danish statistical data including tax and income statistics.

### Other Jurisdictions

**[pchuri/korean-capital-gains-tax-mcp](https://github.com/pchuri/korean-capital-gains-tax-mcp)** | 2 stars | Korean capital gains tax calculations for real estate transactions.

**[gama104/GamaMcpServer](https://github.com/gama104/GamaMcpServer)** | Tax-related operations.

### What's Missing in Tax

The tax MCP ecosystem has notable gaps. No MCP servers exist for TurboTax/Intuit tax products, H&R Block, TaxAct, or any major US consumer tax preparation platform. There are no IRS e-filing API MCP servers. Tax preparation for the UK (HMRC), Germany (ELSTER), Canada (CRA), Australia (ATO), or India (Income Tax Department) has no dedicated MCP coverage. Most accountants using professional tax software (Drake, Lacerte, ProConnect, CCH) have no MCP path to integrate AI agents with their existing workflows.

## Invoicing and Accounts Payable/Receivable

Invoicing generates substantial repetitive work — creating invoices, tracking payments, matching receipts, and managing vendor bills. Multiple MCP servers address different parts of this workflow.

**[Aslan11/temporal-invoice-mcp](https://github.com/Aslan11/temporal-invoice-mcp)** | 21 stars | Human-in-the-loop via Temporal

Uses Temporal durable workflows for invoice processing with human approval steps — particularly relevant for accounting where AI-generated invoices may need human review before sending.

**[PromptPartner/bexio-mcp-server](https://github.com/PromptPartner/bexio-mcp-server)** | 27 stars | Swiss accounting (Bexio) | 314 tools

Covers contacts, invoices/sales, banking, projects/time-tracking, accounting, purchasing/expenses, and payroll for the Bexio platform. At 314 tools, this is one of the largest accounting MCP servers.

**[Frihet-io/frihet-mcp](https://github.com/Frihet-io/frihet-mcp)** | 9 stars | 52 tools

Frihet ERP integration covering invoicing, expenses, clients, products, quotes, reports, and tax compliance.

**[Szotasz/billingo-mcp](https://github.com/Szotasz/billingo-mcp)** | 11 stars | Billingo invoicing API v3 — manage invoices, partners, and products.

**[nubiia-dev/mcp-holded](https://github.com/nubiia-dev/mcp-holded)** | 19 stars | Holded Invoice API (formerly published as iamsamuelfraga/mcp-holded; GitHub now redirects to this location).

**[markslorach/invoice-mcp](https://github.com/markslorach/invoice-mcp)** | 11 stars | PDF invoice generation via natural language.

**[Szotasz/nav-online-invoice-mcp](https://github.com/Szotasz/nav-online-invoice-mcp)** | 9 stars | Hungarian NAV Online Invoice API v3.0 — mandatory electronic invoicing for Hungarian businesses.

**[DojoCodingLabs/hacienda-cr](https://github.com/DojoCodingLabs/hacienda-cr)** | 6 stars | Costa Rica electronic invoicing (Hacienda API).

**[Continero/fakturoid-connector](https://github.com/Continero/fakturoid-connector)** | 6 stars | Fakturoid.cz invoice management with Discord notifications.

**[SamDreamsMaker/facturx-mcp](https://github.com/SamDreamsMaker/facturx-mcp)** | Factur-X electronic invoices (EN 16931 standard) with automated tax calculations.

**[MSFT-Innovation-Hub-India/p2p-anomaly-detection-foundry-agent](https://github.com/MSFT-Innovation-Hub-India/p2p-anomaly-detection-foundry-agent)** | 6 stars | Procure-to-pay invoice anomaly detection using Azure AI and GPT-4o vision — flags suspicious patterns in invoice processing.

## Payroll

Payroll MCP servers complement the accounting ecosystem by connecting AI agents to employee compensation systems.

**[check-technologies/mcp-server-check](https://github.com/check-technologies/mcp-server-check)** | 18 stars | Check Payroll API

The most popular dedicated payroll MCP server. Check provides payroll infrastructure as an API — many payroll platforms are built on top of it.

**[rgrz/peoplesoft-mcp](https://github.com/rgrz/peoplesoft-mcp)** | 12 stars | PeopleSoft HCM (HR, Payroll, Benefits).

**[bifrost-mcp/rippling-mcp](https://github.com/bifrost-mcp/rippling-mcp)** | 3 stars | Rippling with 18 tools for employees, departments, leave, and groups.

**[runpayrolla/payrolla-mcp](https://github.com/runpayrolla/payrolla-mcp)** | Payrolla services.

**[Payroll-Engine/PayrollEngine.Mcp.Server](https://github.com/Payroll-Engine/PayrollEngine.Mcp.Server)** | Query and analyze payroll data with natural language.

**Additional payroll-adjacent servers:** [CodeGlide/workday-payroll-api](https://github.com/CodeGlide/workday-payroll-api) (Workday Payroll), [ag2-mcp-servers/xero-payroll-au-api](https://github.com/ag2-mcp-servers/xero-payroll-au-api) (Xero Payroll Australia).

Note: Gusto's official MCP server (7 tools, read-only) is covered in our [HR and recruiting guide](/guides/mcp-hr-recruiting-talent/) but is equally relevant for accounting teams managing payroll data.

## Expense Management

Expense tracking is a critical link between employee spending and the general ledger.

**[campusx-official/expense-tracker-mcp-server](https://github.com/campusx-official/expense-tracker-mcp-server)** | 22 stars | Local expense tracking — a standalone tool for personal or small business expense management.

**[crazyrabbitLTC/mcp-brex-server](https://github.com/crazyrabbitLTC/mcp-brex-server)** | 4 stars | Brex expense tracking

Read-only access to Brex corporate card data with projection and batching capabilities.

**[jageenshukla/claude-skills-mcp-expense-automation](https://github.com/jageenshukla/claude-skills-mcp-expense-automation)** | 4 stars | Automated expense management with PII redaction — important for handling receipt images that may contain sensitive data.

**[expenselm/expenselm-mcp-server](https://github.com/expenselm/expenselm-mcp-server)** | ExpenseLM expense management.

### What's Missing in Expense Management

No MCP servers exist for Expensify, Ramp, Mercury, or most major corporate card platforms. Brex is the only major fintech spend management platform with a community MCP server, and it's read-only. This represents a significant gap — automated expense categorization and policy compliance are high-value AI use cases that lack MCP infrastructure.

## Payments and Billing

**[stripe/ai](https://github.com/stripe/ai)** (formerly stripe/agent-toolkit) | 1,737 stars | **Official by Stripe** | 25 tools

Stripe's official MCP server is one of the most popular in the entire MCP ecosystem. Provides 25 tools in Python and TypeScript for customers, subscriptions, invoices, payment intents, refunds, and product management. Available as a remote MCP at mcp.stripe.com with OAuth authentication. Any accounting workflow involving payment collection, subscription billing, or refund processing can leverage this server.

## Banking and Reconciliation

Bank reconciliation — matching transactions in accounting software against bank statements — is one of the most time-consuming accounting tasks. MCP servers in this category connect to banking data APIs.

**[Plaid Dashboard MCP Server](https://plaid.com/docs/resources/mcp/)** | **Official** | Developer tools integration

Plaid's [official Dashboard MCP server](https://plaid.com/docs/resources/mcp/) offers "production diagnostics and analytics tools, including tools for debugging Items, reviewing Link conversion data, and checking usage metrics" — support diagnostics, Link conversion analytics, and API usage metrics. Plaid notes the server "is under active development" with "limited support" for now. [Plaid connects to 12,000+ financial institutions](https://plaid.com/), making it a natural bridge for bank reconciliation workflows.

**Community Plaid MCP** | .NET | Personal finance

A community implementation exposing Plaid banking APIs for personal finance applications through MCP.

**Xero Bank Feeds API** ([ag2-mcp-servers/xero-bank-feeds-api](https://github.com/ag2-mcp-servers/xero-bank-feeds-api)) provides direct bank feed access through Xero's platform.

## ERP Financial Modules

Enterprise resource planning systems contain the most comprehensive financial data, and several major ERP vendors have shipped official MCP implementations.

### SAP

SAP's MCP ecosystem spans multiple implementation approaches, including community tooling and SAP's own agentic-AI initiatives on SAP BTP — see SAP's own community writeup on [building an agentic AI system with MCP and SAP BTP](https://community.sap.com/t5/technology-blog-posts-by-sap/building-an-agentic-ai-system-with-model-context-protocol-mcp-and-sap-btp/ba-p/14090900).

**[DataZooDE/erpl-adt](https://github.com/DataZooDE/erpl-adt)** | 16 stars | CLI and MCP for SAP ADT REST API.

**[chrbailey/SAP-Transaction-Forensics](https://github.com/chrbailey/SAP-Transaction-Forensics)** | 6 stars | Cross-system forensic pattern discovery for SAP ERP, Salesforce, and NetSuite data, backed by a 2,048-test suite — relevant for fraud detection and compliance auditing.

**[CDataSoftware/sap-erp-mcp-server-by-cdata](https://github.com/CDataSoftware/sap-erp-mcp-server-by-cdata)** | Read-only via CData JDBC.

### Odoo ERP (Accounting Module)

Odoo's open-source ERP includes a comprehensive accounting module, and its MCP ecosystem is the largest among open-source ERPs.

**[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | 365 stars | Standardized resources and tools for data retrieval and manipulation — the most popular open-source ERP MCP server.

**[hachecito/odoo-mcp-improved](https://github.com/hachecito/odoo-mcp-improved)** | 48 stars | Advanced tools specifically for sales, stock, and accounting.

**[yourtechtribe/mcp-odoo-for-finance](https://github.com/yourtechtribe/mcp-odoo-for-finance)** | 14 stars | Specifically designed for Odoo's finance module.

**[jeevanism/odoo-accounting-mcp](https://github.com/jeevanism/odoo-accounting-mcp)** | Experimental, focuses on journal entries for audit workflows.

## Unified Accounting APIs

For organizations that need to connect AI agents across multiple accounting platforms, unified API platforms offer single-integration coverage.

**[NaimGQKC/coa-mapper-mcp](https://github.com/NaimGQKC/coa-mapper-mcp)** | Chart of accounts mapper

Maps charts of accounts between QuickBooks, Xero, Wave, Sage, and FreshBooks. Zero API keys required, works entirely offline. Solves a critical problem: when migrating between accounting platforms or consolidating data from subsidiaries using different systems, chart of accounts mapping is a major bottleneck.

**[Unified.to MCP Server](https://unified.to/mcp)** — Built-in MCP for unified APIs including accounting, providing a single integration point for multiple platforms.

**[CData Connect AI](https://www.cdata.com/connect/ai/)** — Managed MCP platform advertising "270+ connectors," including the CData accounting connectors verified elsewhere in this guide for QuickBooks, Xero, Sage, NetSuite, Wave, MYOB, and SAP (commercial).

## Financial Compliance and Audit

AI agents in accounting must operate within strict compliance frameworks. Several MCP servers address audit and compliance directly.

**[SYNTAAI/sap-security-mcp](https://github.com/SYNTAAI/sap-security-mcp)** | 17 security/compliance tools (10 security tools, 5 Basis tools, 2 report tools) | ERP security analysis and compliance for SAP systems via RFC calls.

**[chrbailey/SAP-Transaction-Forensics](https://github.com/chrbailey/SAP-Transaction-Forensics)** | 6 stars | Cross-system transaction forensics with conformance checking — designed for auditors investigating transaction patterns across SAP, Salesforce, and NetSuite.

**[MSFT-Innovation-Hub-India/p2p-anomaly-detection-foundry-agent](https://github.com/MSFT-Innovation-Hub-India/p2p-anomaly-detection-foundry-agent)** | 6 stars | Procure-to-pay anomaly detection using Azure AI — designed to flag procurement fraud patterns.

**[Impesud/italy-legacy-db-ai-bridge-template](https://github.com/Impesud/italy-legacy-db-ai-bridge-template)** | Italian ERP integration with PII masking and GDPR compliance.

## Time Tracking with Invoicing

Time-based billing connects directly to invoicing and accounts receivable.

**[ianaleck/harvest-mcp-server](https://github.com/ianaleck/harvest-mcp-server)** | 7 stars | 60+ tools | Harvest time tracking plus invoice management — covers the full cycle from time entry to client billing.

**[feamster/paymo-mcp](https://github.com/feamster/paymo-mcp)** | 5 stars | Paymo time tracking plus invoice management.

## Architecture Patterns

MCP servers in accounting enable several powerful architecture patterns. These patterns show how AI agents can orchestrate across multiple accounting tools to automate complex workflows.

### Pattern 1: AI-Powered Reconciliation Engine

```
┌─────────────────────────────────────────────────────┐
│                  AI Reconciliation Agent              │
│                                                       │
│  1. Fetch bank transactions (Plaid/Xero Bank Feeds)  │
│  2. Read GL entries (QuickBooks/Xero/Sage)           │
│  3. Match transactions using rules + AI judgment     │
│  4. Flag unmatched items for human review            │
│  5. Post reconciling entries                         │
│                                                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │   Plaid  │  │QuickBooks│  │  Stripe  │          │
│  │Bank Feeds│  │   GL     │  │ Payments │          │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘          │
│       │              │              │                │
│       └──────────────┼──────────────┘                │
│                      │                                │
│              ┌───────┴────────┐                      │
│              │  Reconciliation│                      │
│              │   Dashboard    │                      │
│              └────────────────┘                      │
└─────────────────────────────────────────────────────┘
```

This pattern connects banking data, the general ledger, and payment processors. The AI agent fetches transactions from all three sources, performs fuzzy matching (handling timing differences, partial payments, and currency conversions), and posts reconciling journal entries. Unmatched items are flagged for human review rather than auto-posted — maintaining the human-in-the-loop principle critical for financial accuracy.

### Pattern 2: Automated Month-End Close

```
┌─────────────────────────────────────────────────────┐
│                Month-End Close Agent                  │
│                                                       │
│  Day 1: Reconcile bank accounts                      │
│  Day 2: Review AP/AR aging                           │
│  Day 3: Post accruals and adjustments                │
│  Day 4: Generate trial balance                       │
│  Day 5: Produce financial statements                 │
│                                                       │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐  │
│  │  Xero   │ │ Stripe  │ │ Payroll │ │ Expense │  │
│  │Acct API │ │Payments │ │ System  │ │ Tracker │  │
│  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘  │
│       │           │           │            │        │
│       └───────────┴───────────┴────────────┘        │
│                       │                              │
│              ┌────────┴────────┐                    │
│              │  Close Checklist│                    │
│              │  (Human Review) │                    │
│              └─────────────────┘                    │
└─────────────────────────────────────────────────────┘
```

Month-end close typically takes 5-10 business days at mid-size companies. This pattern orchestrates an AI agent across accounting, payments, payroll, and expense systems to execute the close checklist — reconciling accounts, reviewing aging reports, posting standard accruals, and generating trial balances. Each step produces artifacts for human review before proceeding to the next.

### Pattern 3: Multi-Jurisdiction Tax Compliance

```
┌─────────────────────────────────────────────────────┐
│             Tax Compliance Agent                      │
│                                                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │ Tax Law  │  │Accounting│  │  Invoice  │          │
│  │ Database │  │ Platform │  │  System   │          │
│  │(JP/FR/US)│  │(Xero/QB) │  │(Factur-X)│          │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘          │
│       │              │              │                │
│       ▼              ▼              ▼                │
│  ┌────────────────────────────────────────┐         │
│  │         Tax Calculation Engine          │         │
│  │  • Look up applicable tax rates         │         │
│  │  • Calculate withholdings               │         │
│  │  • Generate filing-ready reports        │         │
│  │  • Validate against jurisdiction rules  │         │
│  └────────────────────────────────────────┘         │
│                      │                               │
│              ┌───────┴────────┐                     │
│              │  CPA Review &  │                     │
│              │  Filing Action │                     │
│              └────────────────┘                     │
└─────────────────────────────────────────────────────┘
```

This pattern combines jurisdiction-specific tax law MCP servers with accounting platform data and invoicing systems. The AI agent reads transaction data, looks up applicable tax rules, calculates obligations, and generates filing-ready reports — but the actual filing decision remains with a qualified professional. Supports the growing need for multi-country tax compliance as businesses operate globally.

### Pattern 4: Continuous Audit Monitor

```
┌─────────────────────────────────────────────────────┐
│              Continuous Audit Agent                    │
│                                                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │  ERP GL  │  │ AP/AR    │  │ Expense  │          │
│  │(SAP/D365)│  │ Systems  │  │ Reports  │          │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘          │
│       │              │              │                │
│       ▼              ▼              ▼                │
│  ┌────────────────────────────────────────┐         │
│  │        Anomaly Detection Engine         │         │
│  │  • Benford's Law analysis               │         │
│  │  • Duplicate invoice detection          │         │
│  │  • Unusual vendor patterns              │         │
│  │  • Segregation of duties violations     │         │
│  │  • Transaction amount threshold alerts  │         │
│  └────────────────────────────────────────┘         │
│                      │                               │
│              ┌───────┴────────┐                     │
│              │  Audit Alert   │                     │
│              │  Dashboard     │                     │
│              └────────────────┘                     │
└─────────────────────────────────────────────────────┘
```

Traditional audits sample a small percentage of transactions periodically. This pattern enables continuous monitoring — the AI agent queries ERP, accounts payable/receivable, and expense systems in real time, applying statistical analysis (Benford's Law, duplicate detection) and business rule checks (segregation of duties, approval thresholds) to flag potential issues as they occur rather than months later during an audit.

## Regulatory and Compliance Considerations

AI agents in accounting operate in one of the most heavily regulated domains in technology. Several critical factors shape how MCP should be deployed.

### SOX Compliance and AI

The Sarbanes-Oxley Act requires public companies to maintain effective internal controls over financial reporting. AI agents that create, modify, or approve financial transactions are now considered SOX-relevant internal control risks. This means:

- Every MCP tool call touching financial data should be logged immutably
- AI agents should operate with principle of least privilege — read-only access by default, write access only for specific approved workflows
- Human approval gates are required for material transactions
- The shift is from point-in-time audit checks to continuous verification of AI agent behavior

### EU AI Act

The EU AI Act introduces new requirements for AI systems used in financial services, including:

- Transparency requirements — users must know when they're interacting with AI-generated financial documents
- Risk assessment for AI systems that influence financial decisions
- Record-keeping requirements that align well with MCP's structured tool interfaces

### CPA Professional Ethics

Professional-ethics guidance for CPAs, including [AICPA continuing-education material on AI and critical thinking](https://www.aicpa-cima.com/cpe-learning/course/ethics-and-critical-thinking-in-an-ai-world), frames AI as a tool that assists but does not replace professional judgment, skepticism, or ethical reasoning. This has practical implications for MCP deployments:

- AI agents should prepare work products for CPA review, not make final decisions
- Tax return preparation by AI requires qualified professional sign-off
- Audit evidence gathered by AI agents must be independently verifiable
- Client confidentiality rules apply to AI agent access just as they do to human staff

### Data Privacy

Financial records contain highly sensitive personal and business information. GDPR, CCPA, and similar regulations apply to AI agents accessing this data through MCP:

- Role-based access control in MCP servers should match the access policies of the underlying accounting platform
- PII in financial records (names, addresses, bank account numbers, tax IDs) requires appropriate handling
- Data minimization — AI agents should request only the data they need for the specific task
- Cross-border data transfer rules may restrict which MCP servers can access which data

## Comparison Table: Major Accounting Platform MCP Servers

| Platform | Official? | Stars | Tools/Endpoints | Auth | Key Strength |
|----------|-----------|-------|----------------|------|-------------|
| QuickBooks Online | Yes (Intuit) | 351 | SQL-like queries, CRUD, reports | OAuth 2.0 | Most complete SMB accounting MCP |
| Xero | Yes (Xero) | 350 | 50+ tools | OAuth 2.0 | Broadest API coverage |
| Sage Intacct | Yes (Sage) | N/A | REST APIs + AI Gateway | Vendor auth | Mid-market/enterprise focus |
| Zoho Books | Yes (Zoho) | N/A | 15+ app coverage | OAuth 2.0 | Cross-app Zoho integration |
| NetSuite | Yes (Oracle) | N/A | SuiteQL, CRUD, reports | OAuth 2.0 + PKCE | Enterprise role-based security |
| Dynamics 365 | Yes (Microsoft) | N/A | Data/Form/Action tools | Role-based | Enterprise ERP breadth |
| Odoo | Community | 365 | General + finance-specific | Varies | Open-source, customizable |
| Stripe | Yes (Stripe) | 1,737 | 25 tools | OAuth | Payment processing leader |
| Tally ERP | Community | 67 | Data feed to AI | API key | India market leader |
| Bexio | Community | 27 | 314 tools | API key | Swiss market, largest tool count |

## Ecosystem Gaps

Despite strong coverage from major vendors, significant gaps remain.

**Consumer tax preparation:** TurboTax, H&R Block, TaxAct, and all major consumer tax platforms have zero MCP presence. This is a massive market with high automation potential.

**Professional tax software:** Drake Tax, Lacerte, ProConnect Tax, CCH Axcess, and other tools used by professional accounting firms have no MCP servers.

**Tax authority APIs:** No MCP servers exist for IRS e-filing, HMRC (UK), ELSTER (Germany), CRA (Canada), ATO (Australia), or any government tax filing system.

**Expense management:** Expensify, Ramp, Mercury, and most corporate expense platforms are absent. Only Brex has a community server (read-only).

**Accounts payable automation:** Bill.com, Tipalti, Coupa, and AvidXchange — platforms that handle billions in AP transactions — have no MCP presence.

**Audit and GRC platforms:** AuditBoard, Workiva, BlackLine, and FloQast — the platforms that accounting teams actually use for close management, reconciliation, and audit — are entirely absent from the MCP ecosystem.

**Consolidation tools:** No MCP servers exist for multi-entity consolidation platforms — a critical gap for accounting firms and holding companies.

## Getting Started

### For Accountants and Bookkeepers

Start with the official MCP server for your primary accounting platform (QuickBooks, Xero, or Sage). Begin with read-only queries — generating reports, querying transactions, pulling aging reports — before enabling write operations. The Intuit and Xero servers both have strong documentation and OAuth 2.0 security.

### For CFOs and Controllers

Evaluate the month-end close automation pattern. Connect your ERP (Dynamics 365, NetSuite, or SAP) via its official MCP server, add payment data through [Stripe](https://github.com/stripe/ai), and build a close checklist that an AI agent can execute with human review gates at each step.

### For Tax Professionals

Begin with the tax law servers available for your jurisdiction (US: [dma9527/irs-taxpayer-mcp](https://github.com/dma9527/irs-taxpayer-mcp); Japan: [kentaroajisaka/tax-law-mcp](https://github.com/kentaroajisaka/tax-law-mcp); France: [cornelcroi/french-tax-mcp](https://github.com/cornelcroi/french-tax-mcp)). Use them for research and calculation assistance, not filing. Always maintain professional review of AI-assisted tax work.

### For Developers Building Accounting Tools

If you need to support multiple accounting platforms, start with CData Connect AI or Unified.to for broad coverage through a single MCP integration. For deeper single-platform integration, use the official vendor servers. The chart of accounts mapper (NaimGQKC/coa-mapper-mcp) is useful when building cross-platform features.

### For Auditors

The continuous audit monitor pattern (Pattern 4) is the highest-value starting point. Connect to ERP financial data through SAP or Dynamics 365 MCP servers and implement anomaly detection rules. The SAP-Transaction-Forensics server provides a template for cross-system forensic analysis.

### For Small Business Owners

Wave Financial and FreshBooks MCP servers provide free or low-cost entry points. Combine with the [Stripe AI toolkit](https://github.com/stripe/ai) for payment collection and the expense tracker for spending management. Plain-text accounting tools (Ledger CLI, Beancount) offer maximum transparency and version control for technically inclined owners.

## Conclusion

The accounting MCP ecosystem stands out for the depth of official vendor support. Six major accounting platforms — QuickBooks, Xero, Sage, Zoho, NetSuite, and Dynamics 365 — plus Stripe for payments have all shipped official MCP implementations. This level of vendor commitment is rare across MCP verticals and reflects how well-suited accounting workflows are for AI automation: structured data, clear rules, repetitive processes, and high volume.

The ecosystem's gaps mirror the broader accounting software market's fragmentation. Consumer tax software, professional audit platforms, and AP automation tools remain disconnected from the MCP standard. As adoption grows and more accounting workflows move to AI-assisted execution, these gaps represent both market opportunities for MCP server developers and pressure points that will push additional vendors toward official support.

For accounting professionals evaluating MCP, the maturity of official vendor implementations means the integration path is well-defined. Start with your primary platform's official server, establish read-only AI workflows, prove value with reporting and reconciliation, and expand to write operations under appropriate controls. The regulatory landscape — SOX, EU AI Act, CPA ethics — demands careful human oversight, but MCP's structured tool interfaces provide exactly the audit trail framework that compliance requires.
