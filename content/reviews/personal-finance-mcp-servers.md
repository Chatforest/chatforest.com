---
title: "Personal Finance MCP Servers — YNAB, Plaid, Firefly III, QuickBooks, Alpaca, Monarch Money, and More"
date: 2026-03-15T17:20:00+09:00
description: "Personal finance MCP servers are enabling AI agents to manage budgets, track expenses, analyze investments, file taxes, and connect to banking and brokerage accounts. We reviewed 70+ servers across 10 subcategories. Budgeting: YNAB has 8 implementations, Monarch Money has 5, Actual Budget and LunchMoney have 2 each. Self-hosted: horsfallnathan/firefly-iii-mcp-server (23 stars, Python, AGPL-3.0 — up to 76 tools). Banking: multiple Plaid MCP servers for connecting to bank accounts. Tax: dma9527/irs-taxpayer-mcp (39 tools for US federal/state tax calculations). Accounting: official QuickBooks MCP (Intuit) and official Xero MCP. Stock Market: financial-datasets/mcp-server (715 stars, Python — 9 tools), alpacahq/alpaca-mcp-server (519 stars — 43 tools, official). Brokerage: Schwab, Robinhood, Interactive Brokers integrations. Crypto: Nayshins/mcp-server-ccxt (100+ exchange support), multiple portfolio trackers. Payments: official Stripe MCP server. Rating: 4.0/5."
og_description: "Personal finance MCP servers: Alpaca (519 stars, 43 tools, official), financial-datasets (715 stars, 9 tools), Firefly III (23 stars, 76 tools), YNAB (8 implementations), IRS tax (39 tools), QuickBooks (official), Xero (official), Stripe (official), Plaid banking, Schwab/Robinhood brokerage, CCXT crypto (100+ exchanges). Rating: 4.0/5."
content_type: "Review"
card_description: "Personal finance MCP servers for budgeting, expense tracking, investment analysis, tax planning, banking integration, and cryptocurrency portfolio management. This is one of the most commercially relevant MCP categories — personal finance touches everyone, and the combination of AI assistants with financial data creates genuinely useful workflows like automated budget analysis, tax optimization, and portfolio rebalancing. The standout on the investment side is alpacahq/alpaca-mcp-server (519 stars, 43 tools) — an official server from a real brokerage covering stocks, options, crypto, portfolio management, watchlists, and market data. financial-datasets/mcp-server (715 stars, 9 tools) leads for financial research data with income statements, balance sheets, cash flow statements, stock prices, and crypto data. For budgeting, YNAB dominates with 8 separate MCP implementations — more than any other personal finance app — reflecting YNAB's developer-friendly API and enthusiastic user base. Monarch Money follows with 5 implementations. The self-hosted champion is horsfallnathan/firefly-iii-mcp-server (23 stars, 76 tools) — the most comprehensive personal finance MCP server by tool count, covering accounts, transactions, budgets, categories, tags, bills, and savings goals for the popular open-source Firefly III platform. Tax preparation has a standout in dma9527/irs-taxpayer-mcp with 39 tools covering federal and state calculations, credits, deductions, EITC, retirement strategies, and quarterly payment estimation. The accounting software space has official MCP servers from both Intuit (QuickBooks) and Xero, plus Stripe's official MCP for payments. Banking integration relies on Plaid with multiple MCP implementations. Brokerage coverage spans Schwab, Robinhood (read-only), Interactive Brokers, Alpaca, and Indian platforms like Zerodha and Dhan. Cryptocurrency has CCXT-based servers supporting 100+ exchanges. Gaps: no official YNAB or Monarch MCP servers; no Mint replacement integrations; no Fidelity, Vanguard, or TD Ameritrade; no mortgage management or loan servicing; no insurance; no credit score (Experian/Equifax/TransUnion); no estate planning; limited international tax. The category earns 4.0/5 — exceptional breadth across budgeting, investing, and accounting with multiple official vendor servers, dragged down slightly by the budgeting apps' heavy duplication and limited depth in tax and insurance."
last_refreshed: 2026-03-15
---

Personal finance MCP servers are enabling AI agents to manage budgets, track expenses, analyze investment portfolios, calculate taxes, connect to bank accounts, and trade stocks — all through natural language. Instead of logging into five different apps to understand your financial picture, an AI agent can query your YNAB budget, check your Schwab portfolio, review your Firefly III transactions, and calculate your tax liability in a single conversation.

The landscape spans ten areas: **budgeting apps** (YNAB, Monarch Money, Actual Budget, LunchMoney, Copilot Money), **self-hosted personal finance** (Firefly III), **expense tracking** (CSV and SQLite-based trackers), **banking integration** (Plaid for connecting to bank accounts), **tax preparation** (IRS calculations, depreciation), **financial planning** (SIP calculators, goal planning), **accounting software** (QuickBooks, Xero, FreshBooks), **stock market and investment data** (Financial Datasets, Yahoo Finance, FMP), **brokerage platforms** (Alpaca, Schwab, Robinhood, Interactive Brokers), and **cryptocurrency** (CCXT multi-exchange, portfolio trackers, blockchain data).

The headline findings: **YNAB has 8 MCP implementations** — more than any other personal finance app, reflecting its developer-friendly API and passionate community. **Alpaca's official server has 43 tools** covering stocks, options, crypto, and portfolio management. **Firefly III has up to 76 tools** making it the most comprehensive personal finance MCP server. **Official vendor participation is strong** — Intuit (QuickBooks), Xero, Stripe, and Alpaca all have official MCP servers. **The tax preparation space has a genuine standout** in irs-taxpayer-mcp with 39 tools. **The gap between budgeting duplicates and investment depth is striking** — 8 near-identical YNAB servers vs. sophisticated technical analysis and portfolio optimization tools.

## Budgeting Apps

### YNAB (You Need A Budget)

YNAB has the most MCP implementations of any personal finance app — 8 separate servers, all connecting to YNAB's well-documented API:

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [calebl/ynab-mcp-server](https://github.com/calebl/ynab-mcp-server) | ~3 | TypeScript | Built with mcp-framework, budget/account/transaction tools |
| [EthanKang1/ynab-mcp](https://github.com/EthanKang1/ynab-mcp) | Low | TypeScript | Claude Desktop integration |
| [mattweg/ynab-mcp](https://github.com/mattweg/ynab-mcp) | Low | TypeScript | Claude Code integration |
| [chrisguidry/you-need-an-mcp](https://github.com/chrisguidry/you-need-an-mcp) | Low | Python | Creative naming — "You Need An MCP" |
| [roeeyn/ynab-mcp-server](https://github.com/roeeyn/ynab-mcp-server) | Low | Python | Auto-generated from YNAB OpenAPI spec via FastMCP |
| [Tankatronic/ynab-mcp-server](https://github.com/Tankatronic/ynab-mcp-server) | Low | — | For users who don't link bank accounts |
| [dizzlkheinz/ynab-mcpb](https://github.com/dizzlkheinz/ynab-mcpb) | Low | — | Receipt itemization, bank statement reconciliation |
| [ntdef/ynab-mcp](https://github.com/ntdef/ynab-mcp) | Low | — | Basic YNAB interaction |

The sheer number of YNAB implementations is notable but also a problem — none has emerged as a clear winner, and most overlap significantly. dizzlkheinz/ynab-mcpb stands out for including receipt itemization and bank reconciliation workflows. roeeyn/ynab-mcp-server is interesting for being auto-generated from the YNAB OpenAPI spec using FastMCP, a pattern we may see more of. No official YNAB MCP server exists.

### Monarch Money

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [robcerda/monarch-mcp-server](https://github.com/robcerda/monarch-mcp-server) | Low | — | Account, transaction, and budget tools |
| [colvint/monarch-money-mcp](https://github.com/colvint/monarch-money-mcp) | Low | Python | Financial data access |
| [whitebirchio/monarch-mcp](https://github.com/whitebirchio/monarch-mcp) | Low | Python | Spending analysis via Claude Desktop |
| [ezra-quemuel/monarch-mcp](https://github.com/ezra-quemuel/monarch-mcp) | Low | Python | Account, transaction, budget tools |
| [tsheil/monarch-mcp](https://github.com/tsheil/monarch-mcp) | Low | — | Basic Monarch Money access |

Five implementations for Monarch Money — the popular Mint replacement. Like YNAB, heavy community interest but no clear winner and no official server. Most provide similar budget/transaction query functionality.

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

### Firefly III MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [horsfallnathan/firefly-iii-mcp-server](https://github.com/horsfallnathan/firefly-iii-mcp-server) | 23 | Python | AGPL-3.0 | Up to 76 |

The **most comprehensive personal finance MCP server** — up to 76 tools covering the full Firefly III API: accounts (list, create, update), transactions (search, create, update, delete), budgets, categories, tags, bills, piggy banks (savings goals), rules, and recurring transactions.

Firefly III is the leading open-source self-hosted personal finance manager, and this MCP server exposes its full power to AI agents. With 23 stars, it's also one of the most popular personal finance MCP servers. The AGPL-3.0 license matches Firefly III's own licensing.

Two additional Firefly III implementations exist (etnperlong/firefly-iii-mcp, dnsnpl/firefly-iii-mcp) but horsfallnathan's is the most complete.

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

No official Plaid MCP server exists, which is surprising given Plaid's developer-focused business model.

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
| [intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server) | ~12 | TypeScript | **Official** Intuit server — CRUD for QBO entities |
| [laf-rge/quickbooks-mcp](https://github.com/laf-rge/quickbooks-mcp) | Low | — | Community QuickBooks server |
| [XeroAPI/xero-mcp-server](https://github.com/XeroAPI/xero-mcp-server) | Low | — | **Official** Xero server |
| [john-zhang-dev/xero-mcp](https://github.com/john-zhang-dev/xero-mcp) | Low | — | Community Xero server |
| [roboulos/freshbooks-mcp](https://github.com/roboulos/freshbooks-mcp) | Low | — | FreshBooks invoicing and time tracking |

This subcategory stands out for **official vendor participation** — both Intuit and Xero have released official MCP servers. Intuit's QuickBooks server supports Create, Delete, Get, Search, and Update operations across QBO entities. Having official servers means better maintenance, proper authentication, and confidence in API compatibility.

## Stock Market & Investment Data

### Financial Datasets MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [financial-datasets/mcp-server](https://github.com/financial-datasets/mcp-server) | 715 | Python | — | 9 |

The **most popular finance MCP server by star count** — 9 tools covering income statements, balance sheets, cash flow statements, stock prices, financial news, and cryptocurrency data. A comprehensive API for financial research and fundamental analysis.

### Alpaca MCP Server (Official)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [alpacahq/alpaca-mcp-server](https://github.com/alpacahq/alpaca-mcp-server) | 519 | — | 43 |

The **most feature-rich brokerage MCP server** — 43 tools from Alpaca's official team covering:

- **Stocks** — market data, quotes, historical bars, order placement
- **Options** — options chains, Greeks, order execution
- **Crypto** — cryptocurrency trading and data
- **Portfolio** — positions, account info, P&L
- **Watchlists** — create and manage watchlists
- **Market data** — real-time and historical data feeds

As an official server from a real brokerage, this is the most trustworthy option for actual trading operations via MCP. 519 stars reflects strong community adoption.

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

Notable design choice: verygoodplugins/robinhood-mcp is explicitly **read-only** — it can analyze your portfolio but cannot place trades. Given the risks of AI-initiated financial transactions, this is a thoughtful approach. The Interactive Brokers servers are in alpha/early stages, reflecting the complexity of IB's professional-grade API. Indian brokerages (Zerodha, Dhan) show MCP adoption extending beyond US markets.

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

Nayshins/mcp-server-ccxt is the most versatile — the CCXT library supports 100+ cryptocurrency exchanges through a unified API, so one MCP server handles Binance, Coinbase, Kraken, and dozens more. tatumio/blockchain-mcp extends to 130+ blockchain networks for on-chain data. armorwallet/armor-crypto-mcp is ambitious with wallet creation, swaps, and automated strategies (DCA, stop loss), though AI-controlled crypto wallets carry significant risk.

## Payments (Stripe)

| Server | Notes |
|--------|-------|
| [Stripe Official MCP](https://docs.stripe.com/mcp) | **Official** — remote at mcp.stripe.com, also available as `npx @stripe/mcp` |
| [atharvagupta2003/mcp-stripe](https://github.com/atharvagupta2003/mcp-stripe) | Community Python implementation |

Stripe's official MCP server provides full API access — customers, payments, refunds, subscriptions. While more commonly used for business operations, it's relevant for personal finance in the context of side businesses, freelancing, or managing subscription billing.

## What's Missing

Despite 70+ servers, significant gaps remain:

- **No official YNAB or Monarch Money MCP servers** — given the community demand (8 YNAB implementations, 5 Monarch), official servers would consolidate fragmented efforts
- **No Fidelity, Vanguard, or TD Ameritrade** — the largest US brokerages by AUM have no MCP presence
- **No mortgage management** — no loan servicing, refinance calculators, or mortgage provider integrations
- **No insurance** — no health, auto, home, or life insurance data via MCP
- **No credit score access** — no Experian, Equifax, or TransUnion integrations, no Credit Karma
- **No estate planning** — no trust, will, or beneficiary management tools
- **No international tax** — irs-taxpayer-mcp covers US only; no HMRC, CRA, ATO, or other tax authority servers
- **No pension/retirement account aggregation** — no 401(k) provider integrations beyond generic portfolio tools
- **No bill payment or recurring payment management** — beyond what budgeting apps provide
- **No financial literacy or advisory tools** — no CFP-standard financial planning engines
- **Heavy duplication in budgeting** — 8 YNAB and 5 Monarch Money implementations all doing essentially the same thing

## The Bottom Line

Personal Finance MCP servers earn **4.0 out of 5**. This is one of the most commercially relevant MCP categories, and it shows — official servers from Intuit (QuickBooks), Xero, Stripe, and Alpaca signal that financial service providers see real value in MCP integration. The investment and trading subcategory is particularly strong: financial-datasets/mcp-server (715 stars, 9 tools) provides comprehensive market data, alpacahq/alpaca-mcp-server (519 stars, 43 tools) enables real trading, and maverick-mcp offers sophisticated technical analysis with portfolio optimization.

The budgeting space has enormous community energy but suffers from fragmentation — 8 YNAB implementations and 5 Monarch Money servers with no clear winner in either camp. Firefly III's 76-tool server is the most comprehensive personal finance MCP server overall, and the IRS taxpayer server's 39 tools for tax planning are genuinely useful. The banking integration via Plaid and brokerage coverage across Schwab, Robinhood, and Interactive Brokers rounds out a category that covers most personal finance needs. The main weaknesses are the absence of major brokerage firms (Fidelity, Vanguard), no insurance or credit score access, and heavy duplication in the budgeting subcategory.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
