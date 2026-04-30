---
title: "Cryptocurrency & DeFi MCP Servers — Ethereum, Solana, Bitcoin, Wallets, DEX Trading, On-Chain Analytics, and More"
date: 2026-03-17T02:00:00+09:00
description: "Cryptocurrency and DeFi MCP servers are giving AI agents direct access to blockchain networks — reading balances, executing swaps, managing wallets, querying DeFi protocols, and"
og_description: "Cryptocurrency & DeFi MCP servers: goat-sdk/goat (985 stars — 200+ onchain actions), coinbase/agentkit (1,200 stars — official Coinbase toolkit + x402 payments), CoinGecko OFFICIAL (475 stars — 15K+ coins), evm-mcp-server (374 stars — 60+ EVM chains), Binance MCP (77 stars — 23 tools WITH trading), deBridge (30 stars — cross-chain swaps 25+ chains). 70+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "Cryptocurrency and DeFi MCP servers for AI-powered blockchain interaction, wallet management, DEX trading, and on-chain analytics. **GOAT remains the largest agentic finance toolkit** — goat-sdk/goat (985 stars, TypeScript, MIT) provides 200+ onchain actions across Ethereum, Solana, Base, and more. Framework-agnostic and wallet-agnostic with Python support added. **Coinbase launches x402 agentic payments** — coinbase/agentkit (1,200 stars, Apache-2.0) now supports OpenAI Agents SDK alongside LangChain, Vercel AI SDK, and MCP. The x402 payment protocol enables AI agents to autonomously pay for APIs and MCP servers with USDC — a new primitive for the agent economy, backed by Coinbase, Cloudflare, and the x402 Foundation. base/base-mcp (347 stars) provides dedicated Base network tools. **THREE MAJOR GAPS FILLED FROM INITIAL REVIEW:** (1) **Centralized exchange trading NOW EXISTS** — TermiX-official/binance-mcp (77 stars, 23 tools) provides spot market orders, TWAP algorithmic trading, portfolio management, and market data. The biggest gap from our March review is closed. (2) **Cross-chain bridge execution NOW EXISTS** — debridge-finance/debridge-mcp (30 stars, MIT, 5 tools) enables cross-chain swaps across 25+ EVM chains and Solana with non-custodial design, 30+ security audits, zero exploits across $20B+ volume. TRON integrated April 2026. (3) **Portfolio tracking NOW EXISTS** — Octav-Labs/octav-api-mcp (MIT, 14 tools) provides portfolio data, transaction history, and NAV reporting across 20+ blockchains. **MARKET DATA GOES OFFICIAL** — CoinGecko launched an official hosted MCP server (475 stars for npm package, 15K+ coins, 1,000+ exchanges, 8M+ tokens via GeckoTerminal) at mcp.api.coingecko.com. CoinMarketCap launched an official hosted MCP (12 tools including technical analysis, on-chain metrics, derivatives data, trending narratives) at mcp.coinmarketcap.com. Crypto.com launched an official hosted MCP at mcp.crypto.com. Three major data providers going official in one cycle is unprecedented. **Solana Foundation launches official MCP** — solana-foundation/solana-mcp-official (79 stars, 121 commits) provides AI-powered developer tools at mcp.solana.com with documentation search, semantic RAG, and account analysis. Helius core-ai (15 stars, MIT, 418 commits, 60+ tools across 14 categories) adds comprehensive Solana infrastructure access. **Hardware wallet security arrives** — szhygulin/vaultpilot-mcp (918 commits, 30+ tools, BSL-1.1) provides hardware-verified DeFi where the AI agent proposes and users approve on their Ledger. Supports 9 chains (Ethereum, Arbitrum, Polygon, Base, Optimism, TRON, Solana, Bitcoin, Litecoin) with Aave V3, Compound V3, Morpho Blue, Uniswap V3, Lido, EigenLayer integration. The security model assumes everything except the hardware wallet may be compromised. **Meme coin trading enters MCP** — noahgsolomon/pumpfun-mcp-server (19 stars, 7 tools) enables AI agents to create, buy, and sell meme tokens on Pump.fun, which exceeded $2B DEX volume in Q1 2026. **BitGo launches institutional MCP** — official documentation-access MCP for institutional custody, but transaction execution not yet available. **EVM coverage grows** — evm-mcp-server (374 stars, 57 commits) covers 60+ networks. web3-mcp expanded to Berachain + UTXO chains (Bitcoin, Litecoin, Dogecoin, Bitcoin Cash) with selective tool activation. **Phantom expands to Bitcoin and Sui** — now covers Solana, Ethereum, Bitcoin, and Sui with scoped permissions. **Remaining gaps narrowing** — derivatives/options/futures trading still absent. No crypto tax reporting. Smart contract audit tooling still limited. But the three biggest gaps from March (exchange trading, cross-chain bridging, portfolio tracking) are all now filled. The category earns 4.5/5 — upgraded from 4/5. The ecosystem transformed from read-heavy/write-light to genuinely actionable. Binance trading fills the biggest gap. deBridge fills the cross-chain gap. CoinGecko, CoinMarketCap, and Crypto.com going official validates the market data layer. VaultPilot's hardware wallet approach addresses the security concern. x402 creates a new payment primitive for agent-to-agent commerce. 50+→70+ servers."
last_refreshed: 2026-04-30
---

Cryptocurrency and DeFi MCP servers let AI assistants interact directly with blockchain networks — checking balances, executing token swaps, managing wallets, querying DeFi protocol data, and tracking crypto markets. Instead of manually navigating block explorers and wallet interfaces, AI agents can handle on-chain operations through the Model Context Protocol.

This review covers the **cryptocurrency and DeFi** ecosystem — multi-chain infrastructure, Solana-specific tools, wallet integrations, DeFi protocols, market data, blockchain analytics, payments, and NFTs. For general finance servers, see our [Finance review](/reviews/personal-finance-mcp-servers/).

The headline findings: **Three major gaps filled since March** — centralized exchange trading (Binance MCP with 23 tools including order placement), cross-chain bridging (deBridge across 25+ chains), and portfolio tracking (Octav across 20+ blockchains). **Market data goes official** — CoinGecko, CoinMarketCap, and Crypto.com all launched hosted MCP servers. **Coinbase launches x402** — a payment protocol enabling AI agents to autonomously pay for APIs with USDC. **Hardware wallet security arrives** — VaultPilot enables Ledger-verified DeFi for AI agents. The ecosystem transformed from read-heavy to genuinely actionable.

## Multi-Chain Infrastructure

### goat-sdk/goat (Most Popular)

| Server | Stars | Language | License | Actions |
|--------|-------|----------|---------|---------|
| [goat](https://github.com/goat-sdk/goat) | 985 | TypeScript/Python | MIT | 200+ |

The **largest agentic finance toolkit for AI agents** — 200+ onchain actions across multiple blockchain ecosystems:

- **Payment transmission** — send and receive tokens across chains
- **Commerce** — on-chain purchasing and payment flows
- **Investment strategies** — DeFi protocol interactions
- **Asset tokenization** — NFT and token operations

Framework-agnostic (works with any AI framework) and wallet-agnostic (works with any wallet provider). Now available in both TypeScript and Python with adapters for LangChain, Vercel AI, CrewAI, and more. Supports 16+ blockchain networks including Ethereum, Solana, Aptos, and Cosmos. MCP server examples for both EVM and Solana chains. Sponsored by Crossmint but fully provider-agnostic. MIT licensed with active development (689 commits, 294 forks).

### coinbase/agentkit (Enterprise-Ready)

| Server | Stars | Language | License | Providers |
|--------|-------|----------|---------|-----------|
| [agentkit](https://github.com/coinbase/agentkit) | 1,200 | TypeScript/Python | Apache-2.0 | 50+ |

Coinbase's official toolkit — **"every AI agent deserves a wallet."** The MCP extension enables:

- **50+ action providers** in TypeScript, 30+ in Python
- **Wallet providers** — CDP, Privy, Viem
- **Framework extensions** — LangChain, Vercel AI SDK, MCP, OpenAI Agents SDK, Strands Agents
- **Payments MCP** via x402 — agents can autonomously pay for APIs with USDC
- **Base network focus** with broader EVM support

Active development with 517 commits and 703 forks. The dedicated Base network server lives at [base/base-mcp](https://github.com/base/base-mcp) (347 stars, TypeScript, MIT) — provides onchain tools for LLMs to interact with the Base network and Coinbase API.

**x402 Payment Protocol** — Coinbase co-launched the x402 standard (with Cloudflare and the x402 Foundation) enabling machine-to-machine payments using the HTTP 402 "Payment Required" status code. AI agents can autonomously pay for API calls and MCP server access with stablecoins — no accounts or subscriptions needed. Supports Base and Solana mainnet. This is a fundamental new primitive for the agent economy.

### mcpdotdirect/evm-mcp-server (Broadest EVM Coverage)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server) | 374 | TypeScript | — | 22 |

The **most comprehensive EVM server** — covers 60+ EVM-compatible networks (34 mainnets + 26 testnets):

- **Native token transfers** and balance queries
- **ERC20 operations** — transfers, approvals, balances
- **NFT queries** — ownership, metadata
- **Smart contract interactions** — read and write
- **ENS lookups** — name resolution
- **10 AI-guided prompts** for common workflows

Supports Ethereum, Polygon, BSC, Arbitrum, Optimism, Base, Avalanche, and dozens more through a unified interface.

### Other Multi-Chain Servers

| Server | Stars | Language | License | Chains |
|--------|-------|----------|---------|--------|
| [strangelove-ventures/web3-mcp](https://github.com/strangelove-ventures/web3-mcp) | 93 | TypeScript | Apache-2.0 | Ethereum, Solana, Cardano, THORChain, XRP, Bitcoin, TON, Berachain + UTXO chains |
| [tatumio/blockchain-mcp](https://github.com/tatumio/blockchain-mcp) | 14 | TypeScript | MIT | 130+ networks via Tatum API |

Strangelove Ventures expanded to include Berachain and UTXO chains (Bitcoin, Litecoin, Dogecoin, Bitcoin Cash) with a notable selective tool activation feature — environment flags let you enable only the chains you need, reducing attack surface. Tatum provides the widest network support through their commercial API.

## Solana

### sendaifun/solana-mcp (Best Solana)

| Server | Stars | Language | License | Actions |
|--------|-------|----------|---------|---------|
| [solana-mcp](https://github.com/sendaifun/solana-mcp) | 157 | Shell/TypeScript | Apache-2.0 | 40+ |

The **leading Solana-specific MCP server**, powered by the Solana Agent Kit (1,600 stars separately):

- **SPL token management** — create, transfer, query
- **Transaction execution** — send and sign transactions
- **Wallet operations** — create, manage, query balances
- **DeFi protocol interactions** — swap, stake, lend
- **Account information** — query account data and history

### Solana Foundation Official MCP (NEW)

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [solana-foundation/solana-mcp-official](https://github.com/solana-foundation/solana-mcp-official) | 79 | TypeScript | Official Solana developer tools |

The **Solana Foundation launched an official MCP server** at [mcp.solana.com](https://mcp.solana.com) — AI-powered developer tools with:

- **Semantic RAG** — Solana_Expert__Ask_For_Help and Solana_Documentation_Search tools
- **Canonical spec retrieval** — list_sections and get_documentation tools
- **Hosted endpoint** — available via Streamable HTTP at mcp.solana.com/mcp
- **121 commits** of active development with Databricks-powered vector search

This is the first major blockchain foundation to ship an official MCP server for developer assistance.

### Helius core-ai (NEW — Best Solana Infrastructure)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [helius-labs/core-ai](https://github.com/helius-labs/core-ai) | 15 | TypeScript | MIT | 60+ |

**The most comprehensive Solana infrastructure MCP** — 60+ tools across 14 categories:

- **Account, wallet, asset, transaction** queries via Helius API
- **Streaming** — real-time blockchain data
- **Write operations** — send transactions
- **Compression** — compressed NFT support
- **Knowledge** — Solana documentation and concepts

418 commits of active development — the most actively developed Solana MCP server by commit count.

### Other Solana Servers

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [dcSpark/mcp-cryptowallet-solana](https://github.com/dcSpark/mcp-cryptowallet-solana) | — | — | Solana wallet for Claude/Cursor |
| [paulfruitful/WalletMCP](https://github.com/paulfruitful/WalletMCP) | — | — | Solana blockchain wallet operations |
| [Rayato159/solana-blockchain-explorer](https://github.com/Rayato159/solana-blockchain-explorer) | — | — | Solana explorer data |
| [noahgsolomon/pumpfun-mcp-server](https://github.com/noahgsolomon/pumpfun-mcp-server) | 19 | TypeScript | — | Pump.fun meme coin trading — create, buy, sell tokens |

## Wallets

A major trend: **wallet providers are building native MCP support**, giving AI agents direct wallet access.

### Phantom MCP Server (Official Wallet)

| Server | Language | Networks | Features |
|--------|----------|----------|----------|
| [@phantom/mcp-server](https://www.npmjs.com/package/@phantom/mcp-server) | TypeScript | Solana + Ethereum + Bitcoin + Sui | Transaction signing, swaps, transfers |

Phantom's official MCP server — the first major consumer wallet to ship native AI agent support (launched February 2026):

- **Autonomous transaction signing** — AI agents can sign and send transactions
- **Quote swapping** — get and execute swap quotes
- **Token transfers** — send tokens across supported chains
- **Scoped permissions** — explicitly gate swap, transfer, and address-access functions
- **Expanded chain support** — now covers Solana, Ethereum, Bitcoin, and Sui (up from Solana + EVM)

The **scoped permission model** is notable — it reduces blast radius if an agent misbehaves. Compatible with Claude, OpenClaw, and other MCP clients.

### Other Wallet MCP Servers

| Server | Networks | Focus |
|--------|----------|-------|
| Trust Wallet AI Stack | Multi-chain | MCP server + Claude skills marketplace |
| Bitget Wallet MCP | BNB, Base, Solana, Ethereum, Arbitrum, TON, Tron, Sui, Optimism | LLM-invokable API endpoints |
| [armorwallet/armor-crypto-mcp](https://github.com/armorwallet/armor-crypto-mcp) | Solana (Alpha), 12+ planned | Swaps, transfers, DCA, stop loss, take profit |

Trust Wallet and Bitget represent enterprise wallet providers entering the AI agent space. Armor focuses on strategic trading features like DCA and stop-loss.

## DeFi Protocols

### nirholas/UCAI (Universal Contract AI Interface)

| Server | Language | License | Focus |
|--------|----------|---------|-------|
| [UCAI](https://github.com/nirholas/UCAI) | Python | — | ABI-to-MCP generator |

The **most versatile DeFi approach** — generates MCP servers from any smart contract ABI:

- **Uniswap** — DEX interactions
- **Aave** — lending/borrowing
- **ERC20** — token operations
- **NFTs** — minting and management
- Works across **Ethereum, Polygon, Arbitrum, Base** and other EVM chains
- **Transaction simulation** before execution

Rather than building separate servers for each protocol, UCAI lets you point at any contract ABI and generate tools automatically.

### Protocol-Specific Servers

| Server | Stars | Language | Protocol | Focus |
|--------|-------|----------|----------|-------|
| [Tairon-ai/aave-mcp](https://github.com/Tairon-ai/aave-mcp) | — | — | Aave V3 | Supply, borrow, health factors, yield strategies (Base) |
| [kukapay/uniswap-trader-mcp](https://github.com/kukapay/uniswap-trader-mcp) | — | — | Uniswap | Automated token swaps on 8+ chains |
| [qingfeng/defi-rates-mcp](https://github.com/qingfeng/defi-rates-mcp) | — | — | Multi-protocol | Lending rates across 14+ protocols (Aave, Morpho, Compound) |

Aave V3 gets production-ready coverage on Base. Uniswap gets multi-chain swap automation. DeFi rates comparison spans 14+ protocols across Ethereum, Arbitrum, Base, BSC, and Solana.

### szhygulin/vaultpilot-mcp (NEW — Hardware-Verified DeFi)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vaultpilot-mcp](https://github.com/szhygulin/vaultpilot-mcp) | 3 | — | BSL-1.1 → Apache-2.0 (2030) | 30+ |

**The most security-conscious DeFi MCP server** — "the agent proposes, you approve on your Ledger":

- **Hardware wallet signing** — Ledger via WalletConnect (EVM) and USB-HID (TRON/Solana)
- **9 chain support** — Ethereum, Arbitrum, Polygon, Base, Optimism, TRON, Solana, Bitcoin, Litecoin
- **DeFi positions** — Aave V3, Compound V3, Morpho Blue, Uniswap V3
- **Staking** — Lido, EigenLayer, TRON Stake 2.0, Solana validators
- **Swaps** — LiFi and Jupiter v6
- **Security model assumes everything except hardware wallet may be compromised** — cryptographic bindings across layers detect tampering before signing

918 commits of active development — by far the most commits of any single-purpose crypto MCP server. The Business Source License converts to Apache-2.0 in 2030.

### debridge-finance/debridge-mcp (NEW — Cross-Chain Bridge)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [debridge-mcp](https://github.com/debridge-finance/debridge-mcp) | 30 | — | MIT | 5 |

**Fills the cross-chain bridge gap** from our initial review — AI agents can now execute cross-chain swaps:

- **25+ EVM chains + Solana** — search 40,000+ tokens, get quotes, generate transaction data
- **Non-custodial** — MCP server never touches private keys; users sign via generated deBridge App links
- **30+ security audits, zero exploits** across $20B+ processed volume
- **"Vibe Trading"** — describe the outcome you want, agent handles routing/bridging/swapping
- **TRON integration** — added April 2026

This was explicitly listed as a "major gap" in our March review. Now filled.

## Market Data & Analytics

### coinpaprika/dexpaprika-mcp (Best DEX Data)

| Server | Language | License | Coverage |
|--------|----------|---------|----------|
| [dexpaprika-mcp](https://github.com/coinpaprika/dexpaprika-mcp) | — | — | 5M+ tokens, 20+ blockchains |

The **broadest DEX data coverage** — real-time data for over 5 million tokens across 20+ blockchain networks with DEX analytics.

### Official Market Data Servers (NEW)

Three major data providers launched official hosted MCP servers — a significant validation of the crypto MCP ecosystem:

| Server | Source | Tools | Access |
|--------|--------|-------|--------|
| [CoinGecko Official MCP](https://docs.coingecko.com/docs/mcp-server) | CoinGecko | Multiple | Hosted at mcp.api.coingecko.com — 15K+ coins, 1,000+ exchanges, 8M+ tokens via GeckoTerminal, onchain analytics across 200+ networks. NPM: @coingecko/coingecko-mcp (475 stars) |
| [CoinMarketCap Official MCP](https://coinmarketcap.com/api/mcp/) | CoinMarketCap | 12 | Hosted at mcp.coinmarketcap.com — market quotes, technical analysis, on-chain metrics, derivatives data, trending narratives, macro events, news, semantic search. Streamable HTTP, no install needed |
| [Crypto.com Official MCP](https://mcp.crypto.com/docs) | Crypto.com | Multiple | Hosted at mcp.crypto.com — real-time market data, read-only, public data only |

### Other Market Data Servers

| Server | Stars | Source | Focus |
|--------|-------|--------|-------|
| [Blockchain-MCPs/coingecko-mcp](https://github.com/Blockchain-MCPs/coingecko-mcp) | — | CoinGecko | Token prices, market data (community) |
| [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) | — | CoinMarketCap | Prices, market cap, volume (community) |
| [QuantGeekDev/coincap-mcp](https://github.com/QuantGeekDev/coincap-mcp) | — | CoinCap | Real-time data, no API key needed |
| [CoinStatsHQ/coinstats-mcp](https://github.com/CoinStatsHQ/coinstats-mcp) | — | CoinStats | Portfolio tracking + news |
| [hive-intel/hive-crypto-mcp](https://github.com/hive-intel/hive-crypto-mcp) | — | Hive Intel | Unified crypto/DeFi/Web3 analytics |
| [kukapay/crypto-feargreed-mcp](https://github.com/kukapay/crypto-feargreed-mcp) | — | Alternative.me | Fear & Greed Index |
| [kukapay/whale-tracker-mcp](https://github.com/kukapay/whale-tracker-mcp) | — | On-chain | Whale transaction tracking |
| [kukapay/cryptopanic-mcp-server](https://github.com/kukapay/cryptopanic-mcp-server) | — | CryptoPanic | Cryptocurrency news feed |
| [kukapay/crypto-projects-mcp](https://github.com/kukapay/crypto-projects-mcp) | — | Various | Crypto project research data |
| [ymylive/coin-mcp](https://github.com/ymylive/coin-mcp) | — | Multi-source | 49 tools across CoinGecko, CCXT, DefiLlama, DexScreener — RSI, MACD, Bollinger, 8 prompt templates |

The market data subcategory transformed with three official vendor launches. You can now access institutional-grade data from CoinGecko, CoinMarketCap, and Crypto.com without third-party intermediaries.

## Centralized Exchange Trading (NEW — Gap Filled)

### TermiX-official/binance-mcp (First Exchange Trading MCP)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [binance-mcp](https://github.com/TermiX-official/binance-mcp) | 77 | TypeScript | 23 |

**Fills the single biggest gap from our March review** — centralized exchange trading with order execution:

- **Spot market orders** — place orders via `binanceSpotPlaceOrder`, executes at best available prices
- **TWAP algorithmic trading** — `binanceTimeWeightedAveragePriceFutureAlgo` executes gradually to minimize market impact
- **Portfolio management** — view composition, market value, percentage allocation
- **Market data** — 11 public tools (no API key needed) for order books, klines, recent trades
- **Account management** — balances, trading history

This was explicitly listed as "the biggest gap" in our initial review (reading Binance data existed but no order placement). Now the gap is closed — AI agents can execute trades on Binance through MCP.

## Portfolio Tracking (NEW — Gap Filled)

### Octav-Labs/octav-api-mcp

| Server | Language | License | Tools |
|--------|----------|---------|-------|
| [octav-api-mcp](https://github.com/Octav-Labs/octav-api-mcp) | TypeScript | MIT | 14 |

**Fills the portfolio tracking gap** — DeFi-focused portfolio intelligence across 20+ blockchains:

- **Complete portfolio** including wallet holdings and DeFi protocol positions
- **Total NAV** in specified currency
- **Token distribution** aggregated across all chains
- **Transaction history** with filtering and pagination
- **Historical snapshots** for any past date

Supports Ethereum, Solana, Arbitrum, Base, Polygon, Optimism, BNB Chain, Avalanche, and many more.

## Blockchain Data & Analytics

| Server | Stars | Focus |
|--------|-------|-------|
| [crazyrabbitLTC/mcp-etherscan-server](https://github.com/crazyrabbitLTC/mcp-etherscan-server) | — | Ethereum — balances, ENS resolution, contracts, transactions |
| [heurist-network/heurist-mesh-mcp-server](https://github.com/heurist-network/heurist-mesh-mcp-server) | — | On-chain analytics, token metrics, smart contract security |
| [marctheshark3/ergo-mcp](https://github.com/marctheshark3/ergo-mcp) | — | Ergo blockchain — transaction history, address forensics |

Etherscan provides the most familiar interface for Ethereum developers. Heurist adds security insights for smart contract analysis.

## Payments

| Server | Stars | Focus |
|--------|-------|-------|
| [AbdelStark/lightning-mcp](https://github.com/AbdelStark/lightning-mcp) | — | Bitcoin Lightning Network — invoices, balances, payments |
| [zebedeeio/zbd-mcp-server](https://github.com/zebedeeio/zbd-mcp-server) | — | Lightning micropayments and reward distribution |
| [magnetai/mcp-free-usdc-transfer](https://github.com/magnetai/mcp-free-usdc-transfer) | — | Gasless USDC transfers on Base via Coinbase MPC wallets |

Lightning Network gets two implementations for Bitcoin micropayments. The gasless USDC server on Base is notable for removing the gas fee barrier entirely.

## NFTs

### OpenSea MCP (Official)

OpenSea launched a **beta MCP server** in August 2025 providing AI agents with:

- Real-time NFT data across **20+ blockchains**
- **Collection verification** and rarity scores
- **Wallet balances** and ownership patterns
- **Trading volumes** and marketplace activity
- Portfolio evaluation and token discovery

This is the first major NFT marketplace to ship official MCP support.

## Institutional & Custody (NEW)

| Server | Focus |
|--------|-------|
| [BitGo MCP](https://www.bitgo.com/) | Official institutional custody MCP — documentation access, API references, setup guidance. Transaction execution not yet available |

BitGo launched an official MCP server in March 2026, making institutional digital asset custody platform documentation accessible to AI development tools. Currently limited to documentation access — does not perform transactions or custody actions.

## Security & Forensics

| Server | Focus |
|--------|-------|
| ChainGuard | Multi-chain crime detection — Bitcoin, Ethereum, Hedera, Solana |
| [szhygulin/vaultpilot-mcp](https://github.com/szhygulin/vaultpilot-mcp) | Hardware-verified DeFi — Ledger signing, assumes compromised host |

ChainGuard provides real-time blockchain crime detection and forensic analysis. VaultPilot introduces the most sophisticated security model — assuming everything except the hardware wallet is compromised, with cryptographic bindings across layers.

## What's Missing

Three major gaps from our March review are now filled (exchange trading, cross-chain bridging, portfolio tracking). Remaining gaps:

- **No derivatives/options/futures** — DeFi options protocols (Lyra, Dopex) have no MCP coverage; Binance TWAP exists but no full derivatives support
- **No automated portfolio rebalancing** — Octav provides tracking but not automated rebalancing across protocols/chains
- **No crypto tax reporting** — no integration with Koinly, CoinTracker, or similar tax tools
- **Limited smart contract audit tooling** — Heurist provides some security insights but no comprehensive audit server
- **Security improving but not solved** — VaultPilot's hardware wallet approach is a major step forward, Phantom has scoped permissions, but most servers still lack granular permission models

## The Bottom Line

The cryptocurrency and DeFi MCP ecosystem earns **4.5 out of 5** — upgraded from 4/5 in March.

The ecosystem transformed in 44 days from read-heavy/write-light to genuinely actionable. The three biggest gaps from our March review are all filled: **Binance trading** (77 stars, 23 tools with spot orders and TWAP), **cross-chain bridging** (deBridge across 25+ chains with $20B+ volume and zero exploits), and **portfolio tracking** (Octav across 20+ blockchains). Three major data providers — CoinGecko, CoinMarketCap, and Crypto.com — launched official hosted MCP servers in this period, validating the market data layer.

The security story improved dramatically with VaultPilot's hardware wallet approach (918 commits, assuming compromised hosts) and Phantom expanding to four chains with scoped permissions. The x402 payment protocol creates a new primitive — AI agents can now autonomously pay for API access with stablecoins, enabling agent-to-agent commerce.

GOAT (985 stars) remains the broadest action toolkit. Coinbase agentkit (1,200 stars) brings enterprise credibility with x402 payments. The Solana Foundation launched an official MCP server. Helius provides 60+ tools for Solana infrastructure. Pump.fun brings meme coin trading to AI agents.

Remaining weaknesses: derivatives/options/futures trading is absent. No crypto tax reporting. Smart contract audit tooling is limited. But the category's trajectory is clear — it's moving from experimental to production-ready faster than almost any other MCP vertical.

---

*This review is part of our comprehensive [MCP servers comparison](/guides/best-mcp-servers/) covering 155+ categories. Last updated: April 2026.*

**Category**: [Finance & Fintech](/categories/finance-fintech/)

*This review was last refreshed on 2026-04-30 using Claude Opus 4.6 (Anthropic).*
