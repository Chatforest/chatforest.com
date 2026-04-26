# Personal Finance MCP Servers — YNAB, Plaid, Firefly III, QuickBooks, Alpaca, Monarch Money, and More

> Personal finance MCP servers are enabling AI agents to manage budgets, track expenses, analyze investments, file taxes, and connect to banking and brokerage accounts.


Personal finance MCP servers are enabling AI agents to manage budgets, track expenses, analyze investment portfolios, calculate taxes, connect to bank accounts, and trade stocks — all through natural language. Instead of logging into five different apps to understand your financial picture, an AI agent can query your YNAB budget, check your Schwab portfolio, review your Firefly III transactions, and calculate your tax liability in a single conversation.

The landscape spans eleven areas: **budgeting apps** (YNAB, Monarch Money, Actual Budget, LunchMoney, Copilot Money), **self-hosted personal finance** (Firefly III), **expense tracking** (CSV and SQLite-based trackers), **banking integration** (Plaid for connecting to bank accounts, Truthifi for multi-institution aggregation), **tax preparation** (IRS calculations, depreciation), **financial planning** (SIP calculators, goal planning), **accounting software** (QuickBooks, Xero, FreshBooks), **stock market and investment data** (Financial Datasets, Alpha Vantage, EODHD, Yahoo Finance, FMP), **brokerage platforms** (Alpaca, Schwab, Robinhood, Interactive Brokers), **cryptocurrency** (CCXT multi-exchange, altFINS analytics, portfolio trackers, blockchain data), and **payments** (Stripe).

The headline findings: **YNAB now has 10+ MCP implementations** with Jtewen/ynab-mcp (10 stars, 13 tools) emerging as the most featured. **Alpaca shipped V2** — a complete FastMCP rewrite growing to 683 stars and 50+ tools, with Alpaca reporting 4x API trading growth in Q1 2026 driven by AI. **Financial Datasets nearly tripled** to 2,000 stars. **QuickBooks exploded** from ~12 to 180 stars and expanded to 143 tools covering 29 entity types. **Official vendor participation accelerated** — Plaid launched its AI Toolkit, Alpha Vantage and EODHD both released official MCP servers for market data, and Stripe now has 25 tools in its consolidated ai monorepo. **Truthifi emerged** as a commercial MCP aggregator connecting 18,000+ financial institutions including Fidelity, Vanguard, and Schwab. **The crypto space matured** with lazy-dinosaur/ccxt-mcp (82 stars) adding risk management and altFINS launching 150+ pre-computed indicators. **The gap between budgeting duplicates and investment depth remains** but is narrowing as new implementations add differentiated features.

## Budgeting Apps

### YNAB (You Need A Budget)

YNAB has the most MCP implementations of any personal finance app — now 10+ separate servers, all connecting to YNAB's well-documented API:

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [Jtewen/ynab-mcp](https://github.com/Jtewen/ynab-mcp) | 10 | TypeScript | **Most featured** — 13 tools: financial overview, accounts, categories, transactions, scheduled transactions, budgets, payees |
| [calebl/ynab-mcp-server](https://github.com/calebl/ynab-mcp-server) | ~3 | TypeScript | Built with mcp-framework, budget/account/transaction tools |
| [klauern/mcp-ynab](https://github.com/klauern/mcp-ynab) | 6 | Python | Nick Klauer's implementation — 2 tools, clean Python/uv/Taskfile setup |
| [EthanKang1/ynab-mcp](https://github.com/EthanKang1/ynab-mcp) | Low | TypeScript | Claude Desktop integration |
| [mattweg/ynab-mcp](https://github.com/mattweg/ynab-mcp) | Low | TypeScript | Claude Code integration |
| [chrisguidry/you-need-an-mcp](https://github.com/chrisguidry/you-need-an-mcp) | Low | Python | Creative naming — "You Need An MCP" |
| [roeeyn/ynab-mcp-server](https://github.com/roeeyn/ynab-mcp-server) | Low | Python | Auto-generated from YNAB OpenAPI spec via FastMCP |
| [Tankatronic/ynab-mcp-server](https://github.com/Tankatronic/ynab-mcp-server) | Low | — | For users who don't link bank accounts |
| [dizzlkheinz/ynab-mcpb](https://github.com/dizzlkheinz/ynab-mcpb) | Low | — | Receipt itemization, bank statement reconciliation |
| [ntdef/ynab-mcp](https://github.com/ntdef/ynab-mcp) | Low | — | Basic YNAB interaction |

The YNAB MCP landscape has matured since our last review. **Jtewen/ynab-mcp** (10 stars, 13 tools) has emerged as the most comprehensive implementation with tools for financial overview, budget management, scheduled transactions, and payee cleanup. **klauern/mcp-ynab** takes a minimalist approach with just 2 tools but clean Python tooling. dizzlkheinz/ynab-mcpb still stands out for receipt itemization and bank reconciliation. No official YNAB MCP server exists, but community implementations are getting more differentiated rather than just duplicating each other.

### Monarch Money

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [robcerda/monarch-mcp-server](https://github.com/robcerda/monarch-mcp-server) | Low | — | Account, transaction, and budget tools |
| [colvint/monarch-money-mcp](https://github.com/colvint/monarch-money-mcp) | Low | Python | Financial data access |
| [whitebirchio/monarch-mcp](https://github.com/whitebirchio/monarch-mcp) | Low | Python | Spending analysis via Claude Desktop |
| [ezra-quemuel/monarch-mcp](https://github.com/ezra-quemuel/monarch-mcp) | Low | Python | Account, transaction, budget tools |
| [tsheil/monarch-mcp](https://github.com/tsheil/monarch-mcp) | Low | — | Basic Monarch Money access |

Now six implementations for Monarch Money — the popular Mint replacement. **keithah/monarchmoney-ts-mcp** (7 stars) is the standout newcomer with 70+ operations through dynamic SDK method discovery, MCPB bundle format for one-click install, smart context management with verbosity levels, MFA/TOTP support, and AES-256 session encryption. It automatically discovers all MonarchMoney TypeScript SDK functions, so new capabilities appear without code changes. No official Monarch Money MCP server exists, but keithah's implementation is approaching the comprehensiveness of one.

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [keithah/monarchmoney-ts-mcp](https://github.com/keithah/monarchmoney-ts-mcp) | 7 | TypeScript | **Most comprehensive** — 70+ operations, dynamic SDK discovery, MCPB bundle, MFA support |

### Actual Budget

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [s-stefanov/actual-mcp](https://github.com/s-stefanov/actual-mcp) | Low | TypeScript | Account listings, transaction history, create/update transactions |
| [giorgiobrullo/actual-mcp](https://github.com/giorgiobrullo/actual-mcp) | Low | — | Extended features: batch ops, scheduled transactions, transfers |

Two servers for the open-source Actual Budget. giorgiobrullo's fork adds batch operations, budget management, scheduled transactions, and transfer handling — meaningful feature differentiation over the base implementation.

### LunchMoney

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [akutishevsky/lunchmoney-mcp](https://github.com/akutishevsky/lunchmoney-mcp) | Low | Python | Transaction management, budgeting, financial insights |
| [leafeye/lunchmoney-mcp-server](https://github.com/leafeye/lunchmoney-mcp-server) | Low | — | Transaction and budget interaction |

### Other Budgeting/Finance Apps

| Server | Language | Notes |
|--------|----------|-------|
| [ignaciohermosillacornejo/copilot-money-mcp](https://github.com/ignaciohermosillacornejo/copilot-money-mcp) | — | AI-powered queries using Copilot Money local data |
| [jackstein21/tiller-mcp-server](https://github.com/jackstein21/tiller-mcp-server) | — | Query Tiller Money financial data via Google Sheets API |
| [lunchflow/mcp](https://github.com/lunchflow/mcp) | — | Connect to 20,000+ banks in 40+ countries |

lunchflow/mcp is notable for claiming connection to 20,000+ banks across 40+ countries — potentially the broadest banking connectivity of any personal finance MCP server, though details on the underlying API are unclear.

## Self-Hosted Personal Finance (Firefly III)

### Firefly III MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [horsfallnathan/firefly-iii-mcp-server](https://github.com/horsfallnathan/firefly-iii-mcp-server) | ~7 | Python | AGPL-3.0 | Up to 76 |
| [fabianonetto/mcp-server-firefly-iii](https://github.com/fabianonetto/mcp-server-firefly-iii) | 7 | — | — | 66 |

Firefly III now has **two comprehensive MCP servers**. horsfallnathan's original offers up to 76 tools in direct mode (or 3 meta-tools in consolidated mode) covering the full API: accounts, transactions, budgets, categories, tags, bills, piggy banks, rules, and recurring transactions.

**fabianonetto/mcp-server-firefly-iii** (created March 29, 2026) is a newer "professional-grade, AI-agnostic bridge" providing 66 tools with 100% API coverage. It positions itself as a universal bridge for any AI platform supporting MCP, not just Claude Desktop.

Firefly III remains the leading open-source self-hosted personal finance manager. Two additional implementations exist (etnperlong/firefly-iii-mcp, dnsnpl/firefly-iii-mcp) bringing the total to four Firefly III MCP servers.

## Expense Tracking

| Server | Language | Notes |
|--------|----------|-------|
| [Khushi-c-sharma/expense-tracker-mcp-server](https://github.com/Khushi-c-sharma/expense-tracker-mcp-server) | Python | Add, list, filter, summarize expenses via conversation |
| [papihaj/MCP_Servers](https://github.com/papihaj/MCP_Servers) | Python | CSV-based expense tracking with category breakdown and monthly totals |

Basic standalone expense trackers — useful as tutorials or simple personal tools, but not competitive with full budgeting app integrations.

## Banking & Plaid Integration

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [arjabbar/PlaidMCP](https://github.com/arjabbar/PlaidMCP) | Low | C# | Encrypted token storage, .NET implementation |
| [304techmaven/plaid-mcp-server](https://github.com/304techmaven/plaid-mcp-server) | Low | — | Authorization and transaction API access |
| [Harshaan-Chugh/FinAgent-MCP](https://github.com/Harshaan-Chugh/FinAgent-MCP) | Low | — | Plaid banking + Robinhood crypto, evidence tracking |
| [ag2-mcp-servers/the-plaid-api](https://github.com/ag2-mcp-servers/the-plaid-api) | Low | — | Auto-generated from Plaid OpenAPI spec |

Plaid is the standard banking data aggregation layer in the US, and these servers bring that connectivity to AI agents. arjabbar/PlaidMCP is notable for including encrypted token storage — important since Plaid tokens grant access to real bank accounts. FinAgent-MCP combines Plaid with Robinhood for a unified banking + investing view with evidence tracking for recommendations.

**Plaid launched its official AI Toolkit** in 2026, including a Dashboard MCP Server and Sandbox MCP Server with OAuth authentication. However, a critical caveat: the official Dashboard MCP Server provides access to developer integration health and analytics data — it is **not** a gateway to end-user financial data. You cannot use it to see a customer's bank balance or transaction history. The Sandbox MCP Server is for testing and development. So while Plaid now has official MCP presence, the community servers above remain the only path to actual banking data via MCP.

### Truthifi (Multi-Institution Aggregator)

| Server | Notes |
|--------|-------|
| [Truthifi Connect](https://truthifi-connect.ai/) | **Commercial** — connects to 18,000+ financial institutions via OAuth ($79.99/year) |

**The biggest banking integration news** is Truthifi Connect — a commercial MCP server that connects to Fidelity, Vanguard, Schwab, and 18,000+ other financial institutions simultaneously via OAuth. This partially fills the biggest gap from our last review (no Fidelity/Vanguard access). Read-only, no credential sharing, works with both Claude and ChatGPT. The trade-off: it's a paid service at $79.99/year (with 30-day trial), compared to free open-source alternatives that cover fewer institutions.

## Tax Preparation & Planning

### IRS Taxpayer MCP

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [dma9527/irs-taxpayer-mcp](https://github.com/dma9527/irs-taxpayer-mcp) | Low | Node.js | 39 |

The **standout tax server** — 39 tools covering US individual taxpayer needs:

- **Federal tax calculation** — standard/itemized deductions, all filing statuses, AMT
- **State tax calculation** — multi-state support
- **Credits** — EITC (Earned Income Tax Credit), Child Tax Credit, education credits
- **Deductions** — mortgage interest, education, charitable contributions
- **Retirement strategies** — IRA/401(k) contribution optimization, Roth conversion analysis
- **Quarterly payments** — estimated tax calculation for self-employed
- **W-4 optimization** — withholding calculator
- **Mortgage and education benefits** — interest deduction, student loan interest

Supports TY2024 and TY2025. All calculations run locally — no data leaves the machine. This is a genuinely useful tool for tax planning, though it should be used as a planning aid, not as a replacement for professional tax advice.

### Other Tax Servers

| Server | Language | Notes |
|--------|----------|-------|
| [gama104/GamaMcpServer](https://github.com/gama104/GamaMcpServer) | C# | Tax data management with OAuth 2.1 |
| [leecheuk/tax-depreciation-mcp-guide](https://github.com/leecheuk/tax-depreciation-mcp-guide) | — | MACRS depreciation per IRS Publication 946 |

## Financial Planning & Calculators

| Server | Language | Notes |
|--------|----------|-------|
| [MohanPutti/financial-planner-mcp](https://github.com/MohanPutti/financial-planner-mcp) | Node.js | SIP calculation, goal planning, investment strategies (Scripbox algorithms) |
| [aruaru0/finance_calc_go](https://github.com/aruaru0/finance_calc_go) | Go | Financial calculator tools |
| [norman-finance/norman-mcp-server](https://github.com/norman-finance/norman-mcp-server) | — | Invoicing, bookkeeping, client management, tax filing, document generation |

norman-finance/norman-mcp-server blurs the line between personal finance and small business — it includes invoicing, VAT filing, and client management alongside bookkeeping.

## Accounting Software Integration

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server) | 180 | TypeScript | **Official** Intuit server — 143 tools, 29 entity types, 11 reports, 100% test coverage |
| [laf-rge/quickbooks-mcp](https://github.com/laf-rge/quickbooks-mcp) | Low | — | Community QuickBooks server |
| [XeroAPI/xero-mcp-server](https://github.com/XeroAPI/xero-mcp-server) | 257 | — | **Official** Xero server — 49 tools including payroll, timesheets, leave management |
| [john-zhang-dev/xero-mcp](https://github.com/john-zhang-dev/xero-mcp) | Low | — | Community Xero server |
| [roboulos/freshbooks-mcp](https://github.com/roboulos/freshbooks-mcp) | Low | — | FreshBooks invoicing and time tracking |

The accounting subcategory **exploded since our last review**. Intuit's QuickBooks server grew from ~12 to **180 stars** and expanded massively to **143 tools** covering CRUD operations across 29 entity types plus 11 financial reports — with 335 tests at 100% code coverage. This is now one of the most comprehensive official MCP servers in any category. Xero's server grew to **257 stars** with **49 tools** including payroll-specific commands (timesheets, employees, leave management) alongside standard accounting operations. Note: QuickBooks Desktop is being discontinued May 31, 2026, pushing more users to QBO — and this MCP server.

## Stock Market & Investment Data

### Financial Datasets MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [financial-datasets/mcp-server](https://github.com/financial-datasets/mcp-server) | 2,000 | Python | — | 10 |

The **most popular finance MCP server by star count** — nearly tripling from 715 to **2,000 stars** since our last review. Now 10 tools covering income statements, balance sheets, cash flow statements, stock prices (current and historical), financial news, crypto tickers and prices, and stock screening. Authentication now uses OAuth flow — no API key setup required.

### Alpaca MCP Server V2 (Official)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [alpacahq/alpaca-mcp-server](https://github.com/alpacahq/alpaca-mcp-server) | 683 | Python | 50+ |

The **most feature-rich brokerage MCP server**, now in **V2** — a complete rewrite built with FastMCP and OpenAPI. Grew from 519 to **683 stars** (+32%) and from 43 to **50+ tools** across 9 categories:

- **Account & Portfolio** (6 tools) — positions, account info, P&L, activity history
- **Trading/Orders** (9 tools) — market, limit, trailing-stop, bracket, multi-leg options
- **Positions** (5 tools) — open positions, close individual or all
- **Watchlists** (7 tools) — create, update, manage
- **Assets & Market Info** (8 tools) — asset search, market status
- **Stock Data** (9 tools) — real-time quotes, historical bars, snapshots
- **Crypto Data** (8 tools) — crypto quotes, bars, snapshots
- **Options Data** (7 tools) — options chains, Greeks, quotes
- **News** (1 tool) — market and company news

Alpaca reported **4x API trading growth in Q1 2026** driven by AI, with monthly growth rates rising from single digits to ~30%. The V2 rewrite adds toolset filtering via `ALPACA_TOOLSETS` environment variable and paper/live trading support.

### Alpha Vantage MCP (Official)

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [alphavantage/alpha_vantage_mcp](https://github.com/alphavantage/alpha_vantage_mcp) | 129 | — | **Official** — remote at mcp.alphavantage.co, Progressive Tool Discovery |

**New since last review.** Alpha Vantage launched an official MCP server for stocks, forex, crypto, commodities, and built-in technical indicators (RSI, etc.). Notable for **Progressive Tool Discovery** — an optimization that minimizes token consumption while preserving response quality. Free API key required.

### EODHD MCP (Official)

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [EodHistoricalData/EODHD-MCP-Server](https://github.com/EodHistoricalData/EODHD-MCP-Server) | — | — | **Official** — 77 tools, 100+ docs resources, 3 prompt templates |

**New since last review.** EOD Historical Data launched an official MCP with **77 read-only tools** covering stock market data, fundamentals, technical analysis, and macro indicators. Two versions: v1 (API key) and v2 (OAuth 2.0). Also available as `.mcpb` bundle. Major update March 31, 2026.

### Maverick MCP (Technical Analysis)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [wshobson/maverick-mcp](https://github.com/wshobson/maverick-mcp) | Low | Python | 29+ |

Successor to the archived mcp-trader (248 stars). 29+ tools including technical indicators, stock screening, portfolio optimization, and backtesting. The most sophisticated technical analysis MCP server, with moving averages, momentum indicators, volatility measures, and portfolio optimization algorithms.

### Yahoo Finance MCP Servers

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [Alex2Yang97/yahoo-finance-mcp](https://github.com/Alex2Yang97/yahoo-finance-mcp) | Low | Python | Historical prices, company info, financials, options chains, news |
| [narumiruna/yfinance-mcp](https://github.com/narumiruna/yfinance-mcp) | Low | Python | Simple yfinance wrapper |
| [barvhaim/yfinance-mcp-server](https://github.com/barvhaim/yfinance-mcp-server) | Low | Python | Basic Yahoo Finance data |

Multiple Yahoo Finance implementations via the yfinance Python library. Alex2Yang97's is the most comprehensive with options chain data and company financials.

### Other Investment Data Servers

| Server | Language | Notes |
|--------|----------|-------|
| [leogue/stockmcp](https://github.com/leogue/stockmcp) | Python | Real-time stock data, FastAPI-based |
| [sverze/stock-market-mcp-server](https://github.com/sverze/stock-market-mcp-server) | — | Finnhub API integration |
| [cdtait/fmp-mcp-server](https://github.com/cdtait/fmp-mcp-server) | — | Financial Modeling Prep API with prompts and resources |
| [imbenrabi/Financial-Modeling-Prep-MCP-Server](https://github.com/imbenrabi/Financial-Modeling-Prep-MCP-Server) | — | Company fundamentals via FMP |
| [ikhyunAn/MCP_InvestmentPortfolio](https://github.com/ikhyunAn/MCP_InvestmentPortfolio) | — | Portfolio management with real-time prices and recommendations |
| [VoxLink-org/finance-tools-mcp](https://github.com/VoxLink-org/finance-tools-mcp) | — | Investor agent building tools |
| [netanelavr/trading-mcp](https://github.com/netanelavr/trading-mcp) | — | General trading tools |

## Brokerage Platform Integration

| Server | Language | Notes |
|--------|----------|-------|
| [sudowealth/schwab-mcp](https://github.com/sudowealth/schwab-mcp) | TypeScript | Charles Schwab — Cloudflare Workers deployment, account/market data/orders |
| [jkoelker/schwab-mcp](https://github.com/jkoelker/schwab-mcp) | — | "Chat with your portfolio" — Schwab integration |
| [verygoodplugins/robinhood-mcp](https://github.com/verygoodplugins/robinhood-mcp) | Python | **Read-only** Robinhood portfolio research — a safety-conscious design choice |
| [code-rabi/interactive-brokers-mcp](https://github.com/code-rabi/interactive-brokers-mcp) | — | Interactive Brokers — market data, positions, trade placement (Alpha) |
| [rcontesti/IB_MCP](https://github.com/rcontesti/IB_MCP) | — | Interactive Brokers via WEB API |
| [arindhimar/ContextCraft](https://github.com/arindhimar/ContextCraft) | — | Zerodha KiteConnect — live trading, portfolio risk, stock analysis (India) |
| [mayankthole/dhan-mcp-trades](https://github.com/mayankthole/dhan-mcp-trades) | — | Dhan trading platform (India) |
| [laukikk/alpaca-mcp](https://github.com/laukikk/alpaca-mcp) | — | Community Alpaca implementation |

| [trayders/trayd-mcp](https://github.com/trayders/trayd-mcp) | — | — | Robinhood trading — 24-hour extended trading, dual-source quotes |

Notable design choice: verygoodplugins/robinhood-mcp is explicitly **read-only** — it can analyze your portfolio but cannot place trades. In contrast, **trayders/trayd-mcp** (new since last review) goes all-in on trading, supporting 24-hour extended trading limit orders and dual-source quotes (live Robinhood data during market hours, automatic fallback pre-market and overnight). The Interactive Brokers servers are in alpha/early stages. Indian brokerages (Zerodha, Dhan) show MCP adoption extending beyond US markets.

## Cryptocurrency & Blockchain

| Server | Language | Notes |
|--------|----------|-------|
| [Nayshins/mcp-server-ccxt](https://github.com/Nayshins/mcp-server-ccxt) | — | **CCXT library — 100+ exchanges** (Binance, Coinbase, Kraken, etc.), real-time and historical data |
| [kukapay/crypto-portfolio-mcp](https://github.com/kukapay/crypto-portfolio-mcp) | — | Holdings tracking, Binance prices, portfolio allocation charts |
| [kukapay/crypto-orderbook-mcp](https://github.com/kukapay/crypto-orderbook-mcp) | — | Order book depth and imbalance analysis (6 exchanges) |
| [armorwallet/armor-crypto-mcp](https://github.com/armorwallet/armor-crypto-mcp) | — | Wallet creation, swaps, transfers, DCA, stop loss |
| [tatumio/blockchain-mcp](https://github.com/tatumio/blockchain-mcp) | — | Tatum API — read/write across 130+ blockchain networks |
| [rosendolu/crypto-mcp-server](https://github.com/rosendolu/crypto-mcp-server) | — | Multi-exchange trading, arbitrage, technical indicators (MACD/Bollinger/KDJ/EMA) |
| [marcopesani/mcp-server-bitcoin-wallet](https://github.com/marcopesani/mcp-server-bitcoin-wallet) | — | Bitcoin wallet — send/receive BTC |
| [oilst/kraken-mcp](https://github.com/oilst/kraken-mcp) | — | Kraken Pro REST API via FastMCP |
| [truss44/mcp-crypto-price](https://github.com/truss44/mcp-crypto-price) | — | CoinCap API for prices, market trends, historical data |
| [kukapay/crypto-projects-mcp](https://github.com/kukapay/crypto-projects-mcp) | — | Crypto project information and research |

| [lazy-dinosaur/ccxt-mcp](https://github.com/lazy-dinosaur/ccxt-mcp) | 82 | — | **NEW** — CCXT with risk management, position sizing, leverage up to 100x |
| [altFINS MCP](https://altfins.com/crypto-market-and-analytical-data-api/documentation/mcp-server/) | — | — | **NEW commercial** — 150+ pre-computed indicators, 15,000+ coins, 1,000+ exchanges |

The crypto MCP space matured significantly. **lazy-dinosaur/ccxt-mcp** (82 stars) is the most sophisticated new entry — beyond basic CCXT exchange access, it adds performance analytics (win rates, profit factors, consecutive loss analysis), position sizing (capital ratio trading, leverage up to 100x), and risk controls (technical indicator-based stop losses, ATR multiples, daily loss limits). This is the first crypto MCP server to take risk management seriously.

**altFINS** launched a commercial MCP with 150+ pre-computed technical indicators, 7 years of historical data, and 15,000+ coins tracked across 1,000+ exchanges — aimed at algo trading, AI agents, and trading signal platforms.

Nayshins/mcp-server-ccxt remains the original CCXT implementation for broad exchange access. tatumio/blockchain-mcp covers 130+ blockchain networks for on-chain data. armorwallet/armor-crypto-mcp is ambitious with wallet creation, swaps, and automated strategies, though AI-controlled crypto wallets carry significant risk.

## Payments (Stripe)

| Server | Notes |
|--------|-------|
| [Stripe Official MCP](https://docs.stripe.com/mcp) | **Official** — remote at mcp.stripe.com (OAuth) or `npx @stripe/mcp` (API key), 25 tools |
| [atharvagupta2003/mcp-stripe](https://github.com/atharvagupta2003/mcp-stripe) | Community Python implementation |

Stripe's official MCP server now lives in the **stripe/ai monorepo** alongside @stripe/agent-toolkit, @stripe/ai-sdk, and @stripe/token-meter. It provides **25 tools** covering customers, products, prices, invoices, subscriptions, refunds, and searching Stripe's documentation/knowledge base. Connection via hosted remote (OAuth) or local (API key). Relevant for personal finance in the context of side businesses, freelancing, or subscription billing.

## What's Missing

Despite 80+ servers, some significant gaps remain — though several from our last review have been partially addressed:

- **No official YNAB or Monarch Money MCP servers** — community demand keeps growing (10+ YNAB, 6+ Monarch implementations), but still no vendor participation
- **Fidelity/Vanguard only via commercial aggregator** — Truthifi ($79.99/year) fills this gap, but no free/open-source option and no official servers from the largest US brokerages
- **No mortgage management** — no loan servicing, refinance calculators, or mortgage provider integrations
- **No insurance** — no health, auto, home, or life insurance data via MCP
- **No credit score access** — no Experian, Equifax, or TransUnion integrations, no Credit Karma
- **No estate planning** — no trust, will, or beneficiary management tools
- **No international tax** — irs-taxpayer-mcp covers US only; no HMRC, CRA, ATO, or other tax authority servers
- **No pension/retirement account aggregation** — no 401(k) provider integrations beyond generic portfolio tools
- **Plaid official MCP is developer-only** — the official server covers dashboard analytics, not end-user financial data
- **Budgeting duplication persists** — 10+ YNAB servers, though newer entries are more differentiated

## The Bottom Line

Personal Finance MCP servers earn **4.5 out of 5**, up from 4.0 in March. This category matured dramatically in just six weeks. **Official vendor participation accelerated** — Plaid launched its AI Toolkit, Alpha Vantage and EODHD both released official MCP servers, and existing official servers from QuickBooks (now 180 stars, 143 tools) and Xero (257 stars, 49 tools) saw massive growth. **Alpaca's V2 rewrite** (683 stars, 50+ tools) coincided with their reporting 4x API trading growth in Q1 2026. **financial-datasets/mcp-server** nearly tripled to 2,000 stars, making it the most starred finance MCP server.

The budgeting space is finally differentiating — Jtewen/ynab-mcp (13 tools) and keithah/monarchmoney-ts-mcp (70+ operations with dynamic SDK discovery) stand out from the pack. Firefly III added a second comprehensive server. **Truthifi emerged** as the first commercial MCP aggregator covering 18,000+ financial institutions, partially filling the Fidelity/Vanguard gap. The crypto space gained serious risk management tools with lazy-dinosaur/ccxt-mcp and commercial analytics from altFINS.

The remaining weaknesses: no official YNAB or Monarch servers despite massive community demand, Fidelity/Vanguard only via paid aggregator, no insurance or credit score access, Plaid's official MCP only covers developer dashboard analytics not end-user data, and international tax coverage is still US-only. But the trajectory is clearly upward — this is one of the fastest-maturing MCP categories.

**Category**: [Finance & Fintech](/categories/finance-fintech/)

*This review was last edited on 2026-04-27 using Claude Opus 4.6 (Anthropic).*

