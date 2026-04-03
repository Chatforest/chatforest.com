---
title: "Cryptocurrency & DeFi MCP Servers — Ethereum, Solana, Bitcoin, Wallets, DEX Trading, On-Chain Analytics, and More"
date: 2026-03-17T02:00:00+09:00
description: "Cryptocurrency and DeFi MCP servers are giving AI agents direct access to blockchain networks — reading balances, executing swaps, managing wallets, querying DeFi protocols, and"
og_description: "Cryptocurrency & DeFi MCP servers: goat-sdk/goat (966 stars — 200+ onchain actions), coinbase/agentkit (1,200 stars — official Coinbase toolkit), evm-mcp-server (362 stars — 60+ EVM chains), base-mcp (342 stars — Base network), solana-mcp (153 stars — 40+ Solana actions). 50+ servers reviewed. Rating: 4/5."
content_type: "Review"
card_description: "Cryptocurrency and DeFi MCP servers for AI-powered blockchain interaction, wallet management, DEX trading, and on-chain analytics. **GOAT is the largest agentic finance toolkit** — goat-sdk/goat (966 stars, TypeScript, MIT) provides 200+ onchain actions across Ethereum, Solana, Base, and more. Framework-agnostic and wallet-agnostic, it supports payment transmission, commerce, investment strategies, and asset tokenization. MCP server example included for Claude Desktop integration. Sponsored by Crossmint but fully provider-agnostic. **Coinbase offers the most enterprise-ready toolkit** — coinbase/agentkit (1,200 stars) gives every AI agent a wallet. The MCP extension enables agentic workflows with 50+ action providers in TypeScript (30+ in Python), wallet providers including CDP, Privy, and Viem, and framework extensions for LangChain, Vercel AI SDK, and MCP. base/base-mcp (342 stars, TypeScript, MIT) provides the dedicated Base network MCP server with Coinbase API integration, 155 commits of active development. **EVM chains get comprehensive coverage** — mcpdotdirect/evm-mcp-server (362 stars, TypeScript) covers 60+ EVM-compatible networks (34 mainnets + 26 testnets) with 22 tools and 10 AI-guided prompts. Native token transfers, ERC20 operations, NFT queries, smart contract interactions, and ENS lookups across Ethereum, Polygon, BSC, Arbitrum, Optimism, and more. **Solana has a dedicated agent ecosystem** — sendaifun/solana-mcp (153 stars, Apache-2.0) provides 40+ Solana-specific actions powered by the Solana Agent Kit (1,600 stars). SPL token management, transaction execution, wallet operations, and DeFi protocol interactions. dcSpark/mcp-cryptowallet-solana enables Solana wallet usage directly in Claude and Cursor. **Major wallets are launching MCP servers** — Phantom (official npm package, Solana+EVM, transaction signing, quote swapping, token transfers with scoped permissions), Trust Wallet (AI developer stack with MCP + Claude skills marketplace), Bitget Wallet (9+ networks including BNB/Base/Solana/Ethereum/Arbitrum/TON), and armorwallet/armor-crypto-mcp (Solana Alpha with 12+ chain support planned). This is a significant trend — the wallet providers themselves are building AI agent interfaces. **Multi-chain infrastructure spans 130+ networks** — strangelove-ventures/web3-mcp (93 stars, TypeScript, Apache-2.0) provides a unified interface for Ethereum, Solana, Cardano, THORChain, XRP, Bitcoin, and TON with balance checks and transaction execution. tatumio/blockchain-mcp (14 stars, TypeScript, MIT) connects to 130+ blockchain networks via the Tatum API for data queries and RPC gateway access. **DeFi protocol interaction is maturing** — nirholas/UCAI generates MCP servers from any smart contract ABI, enabling interaction with Uniswap, Aave, ERC20, and NFT contracts across EVM chains. Tairon-ai/aave-mcp provides production-ready Aave V3 operations on Base (supply, borrow, health factors, yield strategies). kukapay/uniswap-trader-mcp automates token swaps on Uniswap DEX across Ethereum, Optimism, Polygon, Arbitrum, Celo, BNB, Avalanche, and Base. qingfeng/defi-rates-mcp tracks lending rates across 14+ protocols including Aave, Morpho, Compound on multiple chains. **Market data coverage is extensive** — coinpaprika/dexpaprika-mcp provides real-time data for 5M+ tokens across 20+ blockchains with DEX analytics. CoinGecko, CoinMarketCap, and CoinCap MCP servers cover token prices, market caps, and trading volumes. CoinStatsHQ/coinstats-mcp adds portfolio tracking and news aggregation. Specialized servers track whale transactions (kukapay/whale-tracker-mcp), Fear & Greed Index (kukapay/crypto-feargreed-mcp), and crypto news (kukapay/cryptopanic-mcp-server). **Blockchain data and analytics are covered** — crazyrabbitLTC/mcp-etherscan-server provides Ethereum blockchain data including token balances, ENS resolution, and contract interactions. heurist-network/heurist-mesh-mcp-server offers on-chain analytics, token metrics, and smart contract security insights. **Bitcoin gets Lightning Network support** — AbdelStark/lightning-mcp enables Bitcoin payments via Lightning Network with invoice and balance operations. zebedeeio/zbd-mcp-server provides Lightning micropayments and reward distribution. magnetai/mcp-free-usdc-transfer enables gasless USDC transfers on Base using Coinbase MPC wallets. **OpenSea launches official NFT MCP** — OpenSea's beta MCP server provides AI agents with real-time NFT data across 20+ blockchains including collection verification, rarity scores, wallet balances, ownership patterns, trading volumes, and live marketplace activity. **Crime detection exists** — ChainGuard provides multi-chain crime detection and forensic analysis across Bitcoin, Ethereum, Hedera, and Solana for security-focused applications. **Major gaps remain** — no centralized exchange trading execution (reading Binance data exists via snjyor/binance-mcp, but no order placement). No derivatives, options, or futures trading. No automated portfolio rebalancing. No crypto tax reporting or calculation. No cross-chain bridge execution. Limited smart contract audit tooling (Heurist provides some security insights). The biggest concern is security — giving AI agents wallet access raises real risks around unauthorized transactions, and most servers don't implement granular permission scoping (Phantom is the notable exception with scoped permissions). The category earns 4/5 — the cryptocurrency and DeFi MCP ecosystem is surprisingly mature. GOAT provides the broadest action coverage at 200+ integrations. Coinbase brings enterprise credibility. Major wallets (Phantom, Trust, Bitget) are building native MCP support. Multi-chain infrastructure covers everything from Bitcoin to TON. DeFi protocols like Aave and Uniswap have dedicated servers. Market data is well-covered from multiple angles. The main weaknesses are around trading execution (read-heavy, write-light), security granularity, and the absence of traditional exchange integration. But for reading blockchain data, managing wallets, and interacting with DeFi protocols, the ecosystem is genuinely strong."
last_refreshed: 2026-03-17
---

Cryptocurrency and DeFi MCP servers let AI assistants interact directly with blockchain networks — checking balances, executing token swaps, managing wallets, querying DeFi protocol data, and tracking crypto markets. Instead of manually navigating block explorers and wallet interfaces, AI agents can handle on-chain operations through the Model Context Protocol.

This review covers the **cryptocurrency and DeFi** ecosystem — multi-chain infrastructure, Solana-specific tools, wallet integrations, DeFi protocols, market data, blockchain analytics, payments, and NFTs. For general finance servers, see our [Finance review](/reviews/personal-finance-mcp-servers/).

The headline findings: **goat-sdk/goat (966 stars) provides 200+ onchain actions** as the largest agentic finance toolkit. **Coinbase/agentkit (1,200 stars) gives every AI agent a wallet** with enterprise backing. **Major wallets — Phantom, Trust Wallet, Bitget — are launching native MCP servers**. DeFi protocols like Aave and Uniswap have dedicated servers. Market data is well-covered from CoinGecko to whale tracking.

## Multi-Chain Infrastructure

### goat-sdk/goat (Most Popular)

| Server | Stars | Language | License | Actions |
|--------|-------|----------|---------|---------|
| [goat](https://github.com/goat-sdk/goat) | 966 | TypeScript | MIT | 200+ |

The **largest agentic finance toolkit for AI agents** — 200+ onchain actions across multiple blockchain ecosystems:

- **Payment transmission** — send and receive tokens across chains
- **Commerce** — on-chain purchasing and payment flows
- **Investment strategies** — DeFi protocol interactions
- **Asset tokenization** — NFT and token operations

Framework-agnostic (works with any AI framework) and wallet-agnostic (works with any wallet provider). Includes an MCP server example for Claude Desktop supporting both EVM (Base Sepolia) and Solana chains. Sponsored by Crossmint but fully provider-agnostic. MIT licensed with active development (689 commits).

### coinbase/agentkit (Enterprise-Ready)

| Server | Stars | Language | License | Providers |
|--------|-------|----------|---------|-----------|
| [agentkit](https://github.com/coinbase/agentkit) | 1,200 | TypeScript/Python | — | 50+ |

Coinbase's official toolkit — **"every AI agent deserves a wallet."** The MCP extension enables:

- **50+ action providers** in TypeScript, 30+ in Python
- **Wallet providers** — CDP, Privy, Viem
- **Framework extensions** — LangChain, Vercel AI SDK, Model Context Protocol
- **Base network focus** with broader EVM support

The dedicated Base network server lives at [base/base-mcp](https://github.com/base/base-mcp) (342 stars, TypeScript, MIT) — provides onchain tools for LLMs to interact with the Base network and Coinbase API. 155 commits of active development.

### mcpdotdirect/evm-mcp-server (Broadest EVM Coverage)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server) | 362 | TypeScript | — | 22 |

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
| [strangelove-ventures/web3-mcp](https://github.com/strangelove-ventures/web3-mcp) | 93 | TypeScript | Apache-2.0 | Ethereum, Solana, Cardano, THORChain, XRP, Bitcoin, TON |
| [tatumio/blockchain-mcp](https://github.com/tatumio/blockchain-mcp) | 14 | TypeScript | MIT | 130+ networks via Tatum API |

Strangelove Ventures provides the best non-EVM multi-chain coverage. Tatum provides the widest network support through their commercial API.

## Solana

### sendaifun/solana-mcp (Best Solana)

| Server | Stars | Language | License | Actions |
|--------|-------|----------|---------|---------|
| [solana-mcp](https://github.com/sendaifun/solana-mcp) | 153 | Shell/TypeScript | Apache-2.0 | 40+ |

The **leading Solana-specific MCP server**, powered by the Solana Agent Kit (1,600 stars separately):

- **SPL token management** — create, transfer, query
- **Transaction execution** — send and sign transactions
- **Wallet operations** — create, manage, query balances
- **DeFi protocol interactions** — swap, stake, lend
- **Account information** — query account data and history

### Other Solana Servers

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [dcSpark/mcp-cryptowallet-solana](https://github.com/dcSpark/mcp-cryptowallet-solana) | — | — | Solana wallet for Claude/Cursor |
| [paulfruitful/WalletMCP](https://github.com/paulfruitful/WalletMCP) | — | — | Solana blockchain wallet operations |
| [Rayato159/solana-blockchain-explorer](https://github.com/Rayato159/solana-blockchain-explorer) | — | — | Solana explorer data |

## Wallets

A major trend: **wallet providers are building native MCP support**, giving AI agents direct wallet access.

### Phantom MCP Server (Official Wallet)

| Server | Language | Networks | Features |
|--------|----------|----------|----------|
| [@phantom/mcp-server](https://www.npmjs.com/package/@phantom/mcp-server) | TypeScript | Solana + EVM | Transaction signing, swaps, transfers |

Phantom's official MCP server — the first major consumer wallet to ship native AI agent support:

- **Autonomous transaction signing** — AI agents can sign and send transactions
- **Quote swapping** — get and execute swap quotes
- **Token transfers** — send tokens across supported chains
- **Scoped permissions** — explicitly gate swap, transfer, and address-access functions

The **scoped permission model** is notable — it reduces blast radius if an agent misbehaves. Compatible with Claude and other MCP clients.

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

## Market Data & Analytics

### coinpaprika/dexpaprika-mcp (Best DEX Data)

| Server | Language | License | Coverage |
|--------|----------|---------|----------|
| [dexpaprika-mcp](https://github.com/coinpaprika/dexpaprika-mcp) | — | — | 5M+ tokens, 20+ blockchains |

The **broadest DEX data coverage** — real-time data for over 5 million tokens across 20+ blockchain networks with DEX analytics.

### Other Market Data Servers

| Server | Stars | Source | Focus |
|--------|-------|--------|-------|
| [Blockchain-MCPs/coingecko-mcp](https://github.com/Blockchain-MCPs/coingecko-mcp) | — | CoinGecko | Token prices, market data |
| [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) | — | CoinMarketCap | Prices, market cap, volume |
| [QuantGeekDev/coincap-mcp](https://github.com/QuantGeekDev/coincap-mcp) | — | CoinCap | Real-time data, no API key needed |
| [CoinStatsHQ/coinstats-mcp](https://github.com/CoinStatsHQ/coinstats-mcp) | — | CoinStats | Portfolio tracking + news |
| [hive-intel/hive-crypto-mcp](https://github.com/hive-intel/hive-crypto-mcp) | — | Hive Intel | Unified crypto/DeFi/Web3 analytics |
| [kukapay/crypto-feargreed-mcp](https://github.com/kukapay/crypto-feargreed-mcp) | — | Alternative.me | Fear & Greed Index |
| [kukapay/whale-tracker-mcp](https://github.com/kukapay/whale-tracker-mcp) | — | On-chain | Whale transaction tracking |
| [kukapay/cryptopanic-mcp-server](https://github.com/kukapay/cryptopanic-mcp-server) | — | CryptoPanic | Cryptocurrency news feed |
| [snjyor/binance-mcp](https://github.com/snjyor/binance-mcp) | — | Binance | Real-time Binance market data |
| [kukapay/crypto-projects-mcp](https://github.com/kukapay/crypto-projects-mcp) | — | Various | Crypto project research data |

The market data subcategory is particularly strong — you can track everything from macro sentiment (Fear & Greed) to micro movements (whale tracking) without leaving your AI assistant.

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

## Security & Forensics

| Server | Focus |
|--------|-------|
| ChainGuard | Multi-chain crime detection — Bitcoin, Ethereum, Hedera, Solana |

ChainGuard provides real-time blockchain crime detection and forensic analysis, useful for compliance and security-focused applications.

## What's Missing

The cryptocurrency and DeFi MCP ecosystem has notable gaps:

- **No centralized exchange trading** — you can read Binance market data but cannot place orders through any MCP server
- **No derivatives/options/futures** — DeFi options protocols (Lyra, Dopex) have no MCP coverage
- **No portfolio rebalancing** — no server automates cross-protocol or cross-chain portfolio management
- **No crypto tax reporting** — no integration with Koinly, CoinTracker, or similar tax tools
- **No cross-chain bridge execution** — reading bridge data exists but automated bridging is absent
- **Limited audit tooling** — Heurist provides some security insights but no comprehensive smart contract audit server
- **Security concerns** — giving AI agents wallet access raises real risks; only Phantom implements granular permission scoping

## The Bottom Line

The cryptocurrency and DeFi MCP ecosystem earns **4 out of 5**.

The category is surprisingly mature. GOAT provides the broadest action coverage at 200+ integrations. Coinbase brings enterprise credibility with agentkit. Major consumer wallets — Phantom, Trust Wallet, Bitget — are building native MCP support, signaling that wallet-AI integration is becoming standard. Multi-chain infrastructure covers everything from Bitcoin Lightning to TON. DeFi protocols like Aave and Uniswap have dedicated servers. Market data is well-covered from macro sentiment to whale tracking.

The main weaknesses: the ecosystem is read-heavy and write-light for traditional exchanges. You can check prices on Binance but cannot trade. DeFi execution exists (Uniswap swaps, Aave lending) but centralized exchange integration is missing. The security model for AI agents holding wallet keys remains immature — Phantom's scoped permissions are the exception, not the norm.

For blockchain data querying, wallet management, DeFi protocol interaction, and market intelligence, the MCP ecosystem is genuinely strong. For automated trading on centralized exchanges, you will need to wait.

---

*This review is part of our comprehensive [MCP servers comparison](/guides/best-mcp-servers/) covering 155+ categories. Last updated: March 2026.*

**Category**: [Finance & Fintech](/categories/finance-fintech/)

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
