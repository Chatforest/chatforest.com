# Banking & Fintech MCP Servers — Plaid, Adyen, Square, Marqeta, Nymbus, Moody's, Comply, Morningstar, and More

> Banking and fintech MCP servers reviewed: Plaid official remote MCP + community servers, Adyen official (47 stars, alpha), Square official (95 stars, OAuth), Marqeta official (33 tools, card issuance), Nymbus core banking (19 tools, GA April 2026), Moody's Agentic Solutions (600M+ companies, GA May 2026), Comply RegTech (trade pre-clearance + policy guidance, GA May 2026), Revolut X trading (11 tools), Morningstar (200K securities), Bloomberg community, LoanPro, Ramp, BANKSapi PSD2. Rating: 4/5.


Banking and fintech represent some of the highest-stakes use cases for MCP — AI agents that can query account balances, enrich transactions, assess credit risk, and navigate payment APIs must do so with rigorous security and compliance. The ecosystem has moved faster than expected: major players like Plaid, Adyen, Square, Marqeta, Morningstar, and now Nymbus and Moody's all ship official MCP servers. Part of our **[Finance & Business MCP category](/categories/finance-business/)**.

*May 2026 refresh: Added Nymbus (core banking, GA April 2026), Moody's Agentic Solutions (official Anthropic partner, GA May 2026), and Comply (financial services RegTech, GA May 2026).*

This review covers **open banking and account aggregation** (Plaid, TrueLayer, multi-provider), **payment processing** (Adyen, Square, Ramp), **banking-as-a-service** (Marqeta), **core banking** (Nymbus), **credit and risk intelligence** (Moody's), **financial market data** (Morningstar, Bloomberg, EODHD, Financial Datasets), **neobank and challenger bank** integrations (Revolut, Mercury), **lending and credit** (LoanPro, Carrington Labs), **KYC, AML & compliance** (Comply, iDenfy, Kyonis), and **transaction enrichment** (Ntropy). For cryptocurrency and DeFi, see our [Cryptocurrency & DeFi MCP Servers](/reviews/cryptocurrency-defi-mcp-servers/) review. For payment-specific servers like Stripe and PayPal, see our dedicated [Stripe MCP Server](/reviews/stripe-mcp-server/) and [PayPal MCP Server](/reviews/paypal-mcp-server/) reviews.

The headline finding: **read-only design dominates** — most financial MCP servers deliberately exclude write operations to minimize risk. **Plaid leads open banking** with an official remote MCP server and multiple community implementations. **Payment processors are all-in** with Adyen, Square, and Marqeta shipping official servers. **Core banking has arrived** — Nymbus ships 19 tools for real banking operations. **Moody's brings credit intelligence to Claude natively** as an official Anthropic partner covering 600M+ companies. **Security patterns are maturing** with OAuth 2.1, encrypted token storage, PII exclusion, and audit logging now standard.

## Open Banking & Account Aggregation

Open banking MCP servers connect AI agents to bank accounts, transactions, and balances through regulated APIs. This is the most active sub-category, with both official and community implementations.

### Plaid Ecosystem

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| Plaid Dashboard MCP | Remote | Python | MIT | Dashboard + sandbox | Yes |
| PlaidMCP (arjabbar) | — | C# / .NET | — | 8+ tools | No |
| bank-mcp (elcukro) | — | TypeScript | — | 3 tools, 4 providers | No |
| 304techmaven/plaid-mcp | — | TypeScript | — | Auth + transactions | No |

**Plaid's official MCP** is a remote server at `api.dashboard.plaid.com/mcp` using Streamable HTTP transport. It provides integration health monitoring, API usage metrics, Link conversion rate optimization, and support diagnostics — focused on the **developer dashboard** rather than end-user banking data. The companion [plaid/ai-coding-toolkit](https://github.com/plaid/ai-coding-toolkit) (MIT, Python) provides sandbox tools like `get_mock_data_prompt`, `search_documentation`, and `get_sandbox_access_token`. Published on PyPI as `mcp-server-plaid`. Authentication uses OAuth Bearer tokens via Plaid Dashboard authorization, preserving all existing security standards.

**PlaidMCP** (arjabbar, C# / .NET) is the standout community implementation. It offers **AES-GCM 256-bit encrypted token storage** at rest, uses secure `item_ref` aliases instead of raw access tokens, and provides configurable ephemeral or persistent storage. Tools include Link token creation, public token exchange, account listing, balance retrieval, and transaction sync with cursor-based pagination.

**bank-mcp** (elcukro, TypeScript) is a multi-provider aggregator supporting **Plaid, Teller, Enable Banking, and Tink** — covering 15,000+ institutions across the US and Europe. Deliberately read-only with only `listAccounts`, `listTransactions`, and `getBalance`. Runs as a stdio process with **no HTTP server, no open port, and no network attack surface**. Only 4 runtime dependencies. Credentials are never logged, and no data leaves the local machine. Plaid provides 104 sub-categories with confidence scores; Tink covers 3,400+ European banks; Enable Banking uses PSD2; Teller uses mTLS with a free tier of 100 live connections.

### TrueLayer (Experimental)

**TrueLayer** has experimental MCP integration documented at docs.truelayer.com but **explicitly states it is NOT officially supported or maintained**. Tools include `get_accounts`, `get_transactions`, and notably `create-truelayer-payout` — one of the few banking MCP servers with a **write operation that initiates real payments**. This carries significant security implications. Community implementation at tkom04/openbankingmcp.

### BANKSapi (Commercial, PSD2-Licensed)

**BANKSapi** (banksapi.de) is a German fintech offering a commercial MCP server with **PSD2 AIS and PIS licensing from BaFin**. Covers 3,000+ providers (99% of German bank accounts, credit cards, custody accounts, loans). ISO 27001 certified, GDPR-compliant, hosted in high-security German data centers. Model-agnostic — works with local or hosted LLMs. Not open source.

### E2E MCP Gateway (Middle East)

**E2E MCP** (e2emcp.com) provides a federated gateway for UAE, KSA, and Bahrain, compliant with CBUAE Open Finance framework. Manages compliance, encryption, and local data residency. Does not require users to be licensed payment providers.

### openbanking-mcp (Demo)

**openbanking-mcp** (collinsrj, TypeScript) is an educational demo showing how Open Banking account and transaction data can be exposed via MCP resources using RFC 6570 URI Templates.

## Payment Processing

Payment MCP servers let AI agents interact with checkout, order management, and merchant services APIs.

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| Adyen MCP | ~47 | TypeScript | MIT | Checkout + Management + webhooks | Yes (alpha) |
| Square MCP | ~95 | TypeScript | — | Full API ecosystem | Yes |
| Ramp MCP | Remote | — | — | Expense + cards + approvals | Yes |

**Adyen** ([adyen/adyen-mcp](https://github.com/Adyen/adyen-mcp), 47 stars, MIT, TypeScript) is in alpha but already functional. Covers Checkout API and Management API with tools for webhook configuration, merchant management, and onboarding links. Available on npm as `@adyen/mcp`. Key feature: **natural language to API call translation** (e.g., "Refund order #12345").

**Square** ([square/square-mcp-server](https://github.com/square/square-mcp-server), 95 stars, TypeScript) provides the full Square API ecosystem — payments, orders, inventory, and customer management. Auto-generated from OpenAPI specs. Supports remote MCP with OAuth (recommended) or local with ACCESS_TOKEN. Block has been integrating MCP across its fintech stack.

**Ramp** (mcp.ramp.com, hosted) is an official MCP server for corporate expense management. Tools cover expense completion (memos, receipts, categories, trips), **card management** (lock/unlock, activate, generate agent card credentials), spend analysis, transaction auditing, and approval management. Every write is recorded in Ramp's Audit Log, and access respects each user's role permissions.

## Banking-as-a-Service

### Marqeta

**Marqeta** ([marqeta/marqeta-mcp](https://github.com/marqeta/marqeta-mcp)) ships an official MCP server with **33 tools across 7 service categories**: issue virtual cards, set spend/velocity controls, create and submit disputes, retrieve transaction details, and flag anomalies. Generated from OpenAPI specifications. This is one of the **highest-risk financial MCP servers** — it can issue cards and manage disputes on live financial infrastructure. Authentication via environment variables (`MARQETA_API_URL`, `MARQETA_USERNAME`, `MARQETA_PASSWORD`, `MARQETA_PROGRAM_SHORT_CODE`).

A companion community server, **marqeta-diva-mcp** (zvika-finally), focuses on data insights, visualization, and analytics.

## Core Banking

Core banking MCP servers give AI agents access to account systems, customer records, and money movement within banking institutions. This was a notable gap in the financial MCP ecosystem until mid-2026.

| Server | Language | Tools | Focus | Official |
|--------|----------|-------|-------|----------|
| Nymbus MCP Server | Closed/hosted | 19 tools | Core banking operations | Yes |

**Nymbus** (GA April 9, 2026) is one of the **first MCP servers purpose-built for core banking operations**, addressing AI agent integration with banking core systems — a gap previously noted across the entire financial MCP ecosystem. Nymbus serves community banks, credit unions, and fintech brands running on the Nymbus Banking Platform.

**19 tools** cover four operational areas: **customer lookup** (find accounts, retrieve customer profiles), **account management** (view account details, balances, transaction history), **money movement** (initiate and review transfers), and **debit card controls** (freeze/unfreeze, manage card status). Each institution controls which tools are enabled, which user roles can access them, and where additional approval is required before an operation executes.

**Security architecture**: Token-based authentication, role-based access controls, **PII masking in logs** (transaction descriptions and customer data are scrubbed before logging), encrypted connections, and full audit logging of all AI agent actions. The design replaces per-tool custom integrations typical with legacy core systems — instead of each AI tool requiring its own integration with the core, Nymbus's MCP provides a single standardized connection layer.

No public GitHub repo; closed commercial product bundled with the Nymbus Banking Platform. Institutions must be on the Nymbus platform to access it.

## Financial Market Data

Financial data MCP servers provide stock prices, ratings, research, and analytics to AI agents.

| Server | Stars | Language | Coverage | Tools | Official |
|--------|-------|----------|----------|-------|----------|
| Moody's Agentic Solutions | — | Hosted | 600M+ companies | Credit + compliance | Yes (Anthropic partner) |
| Morningstar MCP | ~19 | Python | 200K+ securities | 2 main | Yes |
| blpapi-mcp | — | — | Bloomberg Terminal | 18 tools | No |
| EODHD MCP | — | — | Global markets | 77 tools | Semi-official |
| Financial Datasets | — | Python | US stocks | 5 categories | Yes |
| FinanceKit MCP | — | — | Stocks + crypto | 17 tools | No |

**Moody's Agentic Solutions** (api.moodys.com/genai-ready-data/m1/mcp, GA May 5, 2026) is an official Anthropic partner product available natively in **Claude Desktop, Claude.ai, and Claude Enterprise**. It covers **600+ million public and private companies** through Moody's proprietary credit ratings and data. Two primary workflow categories: **credit analysis** (memo generation, peer comparisons, scorecard assessments) and **compliance workflows** (entity profiling, ownership structure mapping, adverse media screening, sanctions checks). Authentication uses MCP OAuth spec — users log in via Moody's credentials, and outputs are rendered as **interactive reports inline within Claude**, eliminating system-switching. No public GitHub repo; commercial product requiring a Moody's account. The Anthropic partnership, announced alongside the launch, positions this as a major signal that financial institutions will invest in Claude-native MCP tools.

**Morningstar** ([Morningstar/morningstar-mcp-server](https://github.com/Morningstar/morningstar-mcp-server), 19 stars, MIT, Python) provides two main tools: `Datapoint` (market cap, ratings, fair value, closing price, total return, economic moat, EPS, NAV, fund size, sector, domicile) and `Articles` (editorial content, methodologies, thematic research, investment strategies). Covers **200,000+ global securities**. Integrated with Claude, ChatGPT, Copilot Studio, and Microsoft Foundry. Requires a licensed Morningstar account. Note: the GitHub repo is archived — development has moved to Morningstar's internal hosting.

**blpapi-mcp** (djsamseng, community) wraps the Bloomberg Terminal API with **18 financial data tools** covering market data, bulk data, technical analysis, screening, and calendars. **Requires a running Bloomberg Terminal** (BBComm accessible). Bloomberg has committed to MCP internally but has not released a public official server. Integrates with Cursor, Claude Code, and Aider.

**EODHD** provides **77 read-only tools**, 100+ documentation resources, and 3 prompt templates (`analyze_stock`, `compare_stocks`, `market_overview`). Community implementations at Enlavan/EODHD_MCP_server and tradermonty/eodhd-mcp-server. V2 supports OAuth authentication.

**Financial Datasets** ([financial-datasets/mcp-server](https://github.com/financial-datasets/mcp-server), Python) covers stock prices (OHLCV), income statements, balance sheets, cash flow statements, and stock screening with metric/ratio filters. Uses **OAuth 2.1** — no API key needed for interactive clients like Claude.

**FinanceKit MCP** (vdalhambra, community) offers **17 tools** including stock quotes, technical analysis (RSI, MACD, Bollinger Bands, ADX, Stochastic, ATR, OBV), crypto data via CoinGecko, risk metrics, options chains, earnings calendar, and portfolio analysis. No API keys required for stocks and crypto — technical indicators calculated locally.

**FinMCP** (Finance-LLMs, MIT) provides a deep research engine with multi-market integration (Indian NSE/BSE + global via Yahoo Finance), trading platform integration (Upstox), and specialized financial document analysis. Multi-provider AI support via NVIDIA, OpenAI, and Fireworks AI.

## Neobank & Challenger Bank Integrations

| Server | Language | Focus | Official |
|--------|----------|-------|----------|
| Revolut X Trading | — | Trading data, 11 tools | Yes |
| revolut-mcp (jeff-nasseri) | — | Personal banking | No |
| Mercury banking (multiple) | Python/TS | Business banking | No |
| mono-mcp (sin4ch) | — | Nigerian banking, 12 tools | No |

**Revolut X** ([revolut-engineering/revolut-x-api](https://github.com/revolut-engineering/revolut-x-api)) is an official MCP server from Revolut Engineering with **11 tool files** covering market data, account management, orders, monitoring, and grid strategy backtests. **Read-only by design** — cannot place, modify, or cancel orders. In beta. Notable: two engineers reportedly built a working trading system in 30 minutes using this server.

**Mercury** has three community-built MCP servers: jbdamask/mcp-mercury-banking (Python, read-only, tested with Claude Desktop), dragonkhoi/mercury-mcp (lightweight API bridge), and klodr/mercury-invoicing-mcp (adds full Invoicing API support including recurring invoices). None are official Mercury products.

**Mono Banking MCP** (sin4ch/mono-mcp) provides **12 tools plus webhook support** for Nigerian banking operations via the Mono Open Banking API. Uses FastMCP with async httpx and SQLAlchemy webhook storage.

No MCP servers found from **Chime, N26, Monzo, or Starling**.

## Lending & Credit

| Server | Language | Focus | Official |
|--------|----------|-------|----------|
| LoanPro MCP | Go | Loan servicing | Yes |
| Carrington Labs | — | Credit risk scoring | Yes (commercial) |

**LoanPro** ([MiloCreditPlatform/loanpro-mcp-server](https://github.com/milocreditplatform/loanpro-mcp-server), Go) is an official server with modular packages for loan operations, customer operations, and payment operations. Supports HTTP, SSE, and stdio transports. **Read-only access** to financial data with compliance guardrails enforced programmatically and full audit trail for both human and AI agent actions. Positioning: "Onboard a new servicing employee instantly."

**Carrington Labs** (carringtonlabs.com/mcp-server, commercial) provides **deterministic credit risk assessments** — not probabilistic — with Cashflow Score, Credit Risk Model outputs, and explainability. Returns only a unique record ID and model outputs, **never personally identifiable information**. Score plus key factor explanations meet Equal Credit Opportunity Act requirements. Announced November 2025, broader availability expected.

## KYC, AML & Compliance

| Server | Focus | Customers | Official |
|--------|-------|-----------|----------|
| Comply (ComplyAI) | Trade pre-clearance + policy guidance + compliance briefings | 5,000+ financial firms | Yes |
| iDenfy MCP | Documentation access (KYC/KYB/AML) | — | Yes |
| Kyonis Compliance | KYC verification + AML screening | — | Yes |
| Sardine | Fraud detection AI assistant | — | Yes (internal) |

**Comply** (comply.com, GA May 2026) is the **first enterprise-grade MCP server for financial services compliance** according to Comply's positioning. Comply serves 5,000+ financial firms with trade surveillance, personal account dealing, and policy management tools — the MCP server extends those capabilities to AI agents.

Three launch use cases: **trade pre-clearance agents** (employees submit pre-clearance requests via any MCP-compatible AI tool; compliance officers approve or deny with automated audit logs), **policy guidance agents** (AI agents answer firm-specific compliance questions sourced from the firm's own approved policies, surfaceable via Teams, Slack, or any connected AI client), and **morning briefing agents** (daily compliance summary covering open pre-clearance requests, outstanding certification gaps, and regulatory alerts). **No developer required** — compliance officers configure and deploy their own agents without code.

Compatible orchestrators: Claude, Microsoft Copilot, and ChatGPT. No public GitHub repo; commercial product available through Comply's enterprise platform.

**iDenfy** (documentation.idenfy.com/resources/mcp, launched April 2026) is a **documentation-access MCP server** — it searches iDenfy's live docs and returns API field names, endpoints, and working code examples. It **cannot trigger verification flows, access live data, dashboard, sessions, API keys, or customer data**. Free for all developers. Covers KYC, KYB, and AML products.

**Kyonis Compliance** (listed on PulseMCP) provides KYC verification, AML sanctions screening, and due diligence checks via the Kyonis API.

**Sardine** (sardine.ai) uses MCP internally for a fraud detection AI assistant covering device intelligence, behavior biometrics, and ML fraud detection across onboarding, login, and payments with real-time transaction interdiction in hundreds of milliseconds. Not publicly available as a standalone MCP server.

## Transaction Enrichment

**Ntropy** ([ntropy-network/ntropy-mcp](https://github.com/ntropy-network/ntropy-mcp), MIT) enriches raw transaction data with **95%+ merchant identification and categorization** on both business and consumer data. Tools include `check_connection`, transaction enrichment (with parameters for description, date, amount, entry type, currency, country), and account holder management. Requires an external Ntropy API key.

## Security Patterns Across Financial MCP Servers

Financial MCP servers have developed distinct security patterns worth noting:

- **Read-only by default**: bank-mcp, Revolut X, Mercury, LoanPro, and most data servers deliberately exclude write operations. The few servers with write access (TrueLayer payouts, Marqeta card issuance, Ramp expense management) carry elevated risk profiles.
- **PII exclusion**: Carrington Labs returns only record IDs and model outputs, never personally identifiable information. This pattern should be standard for credit and lending MCP servers.
- **Encrypted token storage**: PlaidMCP uses AES-GCM 256-bit encryption at rest with alias-based token references.
- **OAuth 2.0/2.1**: Becoming the standard authentication method for remote financial MCP servers (Plaid, Square, Financial Datasets, EODHD v2).
- **Stdio-only transport**: bank-mcp and others prefer stdio to eliminate network attack surface entirely.
- **Audit logging**: Ramp and LoanPro record every AI agent action in audit trails.
- **Sandbox-first development**: Plaid, TrueLayer, and Revolut mandate sandbox environments before production access.

## What's Missing

- **Core banking tier-1 vendors**: Nymbus (community banks, credit unions) now ships 19 tools, but Thought Machine, Mambu, Temenos, FIS, and Fiserv — which serve the world's largest banks — still offer no MCP integration.
- **Major neobanks**: Beyond Revolut, no MCP servers from Chime, N26, Monzo, Starling, or SoFi.
- **Full Bloomberg access**: The community blpapi-mcp wrapper requires a Bloomberg Terminal license. No public Bloomberg MCP server exists.
- **LSEG/Refinitiv**: Has partnered with Microsoft and Anthropic for managed MCP access but offers no self-hostable public server.
- **PSD3-specific servers**: PSD3 is still in legislative process; no MCP servers target it yet.
- **Crypto banking**: While we cover crypto in our [Cryptocurrency & DeFi](/reviews/cryptocurrency-defi-mcp-servers/) review, there are no MCP servers bridging traditional banking with stablecoin or CBDC operations.
- **Dedicated fraud prevention**: Sardine's MCP is internal-only. No public MCP servers for Featurespace, Feedzai, or other fraud platforms.

## Rating: 4 / 5

The banking and fintech MCP ecosystem has matured significantly. Official servers from Plaid, Adyen, Square, Marqeta, Morningstar, Ramp, LoanPro, Nymbus, Moody's, and Comply represent genuine institutional commitment across every major financial services sub-category. The three May 2026 additions resolve the two most significant gaps in the April review: Nymbus breaks open core banking (19 tools, GA), and Comply brings enterprise compliance workflows to financial AI agents for the first time.

The remaining gaps — tier-1 core banking vendors (Temenos, FIS, Fiserv), major neobanks (Chime, Monzo), and public Bloomberg access — are real but increasingly narrow. Security patterns are now standard: read-only defaults, PII exclusion, OAuth 2.1, and full audit logging appear across virtually all financial MCP servers. The ecosystem's progress from the January 2026 baseline to May 2026 represents one of the fastest category maturity arcs in the broader MCP server landscape.

