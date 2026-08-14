# Cryptocurrency & DeFi MCP Servers — Ethereum, Solana, Bitcoin, Wallets, DEX Trading, On-Chain Analytics, and More

> Cryptocurrency and DeFi MCP servers are giving AI agents direct access to blockchain networks — reading balances, executing swaps, managing wallets, querying DeFi protocols, and


Cryptocurrency and DeFi MCP servers let AI assistants interact directly with blockchain networks — checking balances, executing token swaps, managing wallets, querying DeFi protocol data, and tracking crypto markets. Instead of manually navigating block explorers and wallet interfaces, AI agents can handle on-chain operations through the Model Context Protocol.

This review covers the **cryptocurrency and DeFi** ecosystem — multi-chain infrastructure, Solana-specific tools, wallet integrations, DeFi protocols, market data, blockchain analytics, payments, and NFTs. For general finance servers, see our [Finance review](/reviews/personal-finance-mcp-servers/).

The headline findings: **Three major gaps filled since March** — centralized exchange trading (Binance MCP with spot and TWAP order placement), cross-chain bridging (deBridge across 25+ chains), and portfolio tracking (Octav across 20+ blockchains). **Market data goes official** — CoinGecko, CoinMarketCap, and Crypto.com all launched hosted MCP servers. **Coinbase launches x402** — a payment protocol enabling AI agents to autonomously pay for APIs with USDC. **Hardware wallet security arrives** — VaultPilot enables Ledger-verified DeFi for AI agents. The ecosystem transformed from read-heavy to genuinely actionable.

## Multi-Chain Infrastructure

### goat-sdk/goat (Most Popular)

| Server | Stars | Language | License | Actions |
|--------|-------|----------|---------|---------|
| [goat](https://github.com/goat-sdk/goat) | ~1,000 (archived) | TypeScript/Python | MIT | 200+ |

The **largest agentic finance toolkit for AI agents** — 200+ onchain actions across multiple blockchain ecosystems:

- **Payment transmission** — send and receive tokens across chains
- **Commerce** — on-chain purchasing and payment flows
- **Investment strategies** — DeFi protocol interactions
- **Asset tokenization** — NFT and token operations

Framework-agnostic (works with any AI framework) and wallet-agnostic (works with any wallet provider). Available in both TypeScript and Python with adapters for LangChain, Vercel AI, CrewAI, and more. Supports 16+ blockchain networks including Ethereum, Solana, Aptos, and Cosmos. MCP server examples for both EVM and Solana chains. Sponsored by Crossmint but fully provider-agnostic. MIT licensed.

**Correction (2026-08-14 audit):** this entry previously described GOAT as under "active development." That is no longer true — [the repository is now archived](https://github.com/goat-sdk/goat) as a read-only historical snapshot ("no longer actively maintained, and no issues, pull requests, or updates will be accepted"), with its last update around May 2026. The star count (~1.0k) and MIT license still stand, but treat GOAT as a frozen snapshot, not a maintained project, when evaluating it for new integrations.

### coinbase/agentkit (Enterprise-Ready)

| Server | Stars | Language | License | Providers |
|--------|-------|----------|---------|-----------|
| [agentkit](https://github.com/coinbase/agentkit) | 1,300 | TypeScript/Python | Apache-2.0 | 50+ |

Coinbase's official toolkit — **"every AI agent deserves a wallet."** The MCP extension enables:

- **50+ action providers** in TypeScript, 30+ in Python
- **Wallet providers** — CDP, Privy, Viem
- **Framework extensions** — LangChain, Vercel AI SDK, MCP, OpenAI Agents SDK, Strands Agents
- **Payments MCP** via x402 — agents can autonomously pay for APIs with USDC
- **Base network focus** with broader EVM support

Active development (1.3k stars, 779 forks as of this audit — up from 1,200/703 in April). The dedicated Base network server previously lived at [base/base-mcp](https://github.com/base/base-mcp) (TypeScript, MIT).

**Correction (2026-08-14 audit):** base/base-mcp is now archived and deprecated — the repo and its npm package (`base-mcp`) carry an explicit "no longer maintained, do not use" notice, pointing developers instead to [docs.base.org/ai-agents](https://docs.base.org/ai-agents). Coinbase's own agentkit (above) remains the actively maintained path to Base network tooling.

**x402 Payment Protocol** — [Coinbase developed the x402 protocol](https://www.coinbase.com/blog/coinbase-and-cloudflare-will-launch-x402-foundation), updating the long-dormant HTTP 402 "Payment Required" status code into a standard for machine-to-machine payments, and partnered with Cloudflare to hand it to a vendor-neutral [x402 Foundation under Linux Foundation stewardship](https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol) (launched April 2, 2026), whose founding members include Cloudflare, Stripe, Visa, Mastercard, American Express, AWS, Google, Microsoft, Shopify, and the Solana Foundation — Stripe and the other members joined the Foundation; they did not co-develop the original protocol. AI agents can autonomously pay for API calls and MCP server access with stablecoins — no accounts or subscriptions needed. Supports Base and Solana mainnet. This is a fundamental new primitive for the agent economy.

### mcpdotdirect/evm-mcp-server (Broadest EVM Coverage)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server) | 381 | TypeScript | MIT | 22 |

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
| [solana-mcp](https://github.com/sendaifun/solana-mcp) | 162 | Shell/TypeScript | Apache-2.0 | 40+ |

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
- **166+ commits** of active development (up from 121 at last check) with Databricks-powered vector search

It's a notable step for a blockchain foundation (rather than a single vendor) to ship an official MCP server for developer assistance — we haven't found another major L1 foundation with a comparable official server as of this audit, though we can't independently verify a strict "first."

### Helius core-ai (NEW — Best Solana Infrastructure)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [helius-labs/core-ai](https://github.com/helius-labs/core-ai) | 24 | TypeScript | MIT | 10 public / 60+ ops |

**A comprehensive Solana infrastructure MCP.** The [Helius MCP server itself exposes 10 public tools](https://www.helius.dev/docs/agents/mcp) — 9 routed domain tools (`heliusAccount`, `heliusWallet`, `heliusAsset`, `heliusTransaction`, `heliusChain`, `heliusStreaming`, `heliusKnowledge`, `heliusWrite`, `heliusCompression`) plus `expandResult` for paging — but those domain tools route to [60+ underlying Helius/Solana operations](https://www.helius.dev/blog/helius-for-agents) (RPC, DAS, webhooks, transaction sending). We could not confirm the "14 categories" figure from an earlier version of this review against any Helius source, so we've dropped that specific number:

- **Account, wallet, asset, transaction** queries via Helius API
- **Streaming** — real-time blockchain data
- **Write operations** — send transactions
- **Compression** — compressed NFT support
- **Knowledge** — Solana documentation and concepts

522+ commits of active development as of this audit (up from 418) — one of the more actively developed Solana MCP servers by commit count, though we haven't independently verified it's the single most-active one across every server in this review.

### Other Solana Servers

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [dcSpark/mcp-cryptowallet-solana](https://github.com/dcSpark/mcp-cryptowallet-solana) | — | — | Solana wallet for Claude/Cursor |
| [paulfruitful/WalletMCP](https://github.com/paulfruitful/WalletMCP) | — | — | Solana blockchain wallet operations |
| [Rayato159/sol-chad-mcp](https://github.com/Rayato159/sol-chad-mcp) | — | — | Solana wallet monitoring and market data (repo renamed from solana-blockchain-explorer) |
| [noahgsolomon/pumpfun-mcp-server](https://github.com/noahgsolomon/pumpfun-mcp-server) | 21 | TypeScript | — | Pump.fun meme coin trading — create, buy, sell tokens |

## Wallets

A major trend: **wallet providers are building native MCP support**, giving AI agents direct wallet access.

### Phantom MCP Server (Official Wallet)

| Server | Language | Networks | Features |
|--------|----------|----------|----------|
| [@phantom/mcp-server](https://docs.phantom.com/phantom-mcp-server) | TypeScript | Solana + Ethereum + Bitcoin + Sui | Transaction signing, swaps, transfers |

Phantom's [official MCP server](https://docs.phantom.com/phantom-mcp-server), launched February 18, 2026 — one of the first major consumer wallets to ship native AI agent support, as far as we've found; we can't independently confirm it's strictly the first:

- **Autonomous transaction signing** — AI agents can sign and send transactions
- **Quote swapping** — get and execute swap quotes
- **Token transfers** — send tokens across supported chains
- **Scoped permissions** — explicitly gate swap, transfer, and address-access functions
- **Expanded chain support** — now covers Solana, Ethereum, Bitcoin, and Sui (up from Solana + EVM)

The **scoped permission model** is notable — it reduces blast radius if an agent misbehaves. Compatible with Claude, OpenClaw, and other MCP clients.

### Other Wallet MCP Servers

| Server | Networks | Focus |
|--------|----------|-------|
| [Trust Wallet AI Stack](https://developer.trustwallet.com/developer/mcp/docs-mcp) | Multi-chain | MCP server (docs access) + open-source Claude Code skills marketplace |
| [Bitget Wallet MCP](https://github.com/bitget-wallet-ai-lab/bitget-wallet-mcp) | Ethereum, Solana, BNB Chain, Base, Arbitrum, TRON, TON, Sui, Optimism | LLM-invokable API endpoints — token info, swap quotes, security/honeypot checks |
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
| [vaultpilot-mcp](https://github.com/szhygulin/vaultpilot-mcp) | 2 | — | BSL-1.1 → Apache-2.0 (2030) | 30+ |

**A hardware-wallet-first, security-conscious DeFi MCP server** — "the agent proposes, you approve on your Ledger":

- **Hardware wallet signing** — Ledger via WalletConnect (EVM) and USB-HID (TRON/Solana)
- **9 chain support** — Ethereum, Arbitrum, Polygon, Base, Optimism, TRON, Solana, Bitcoin, Litecoin
- **DeFi positions** — Aave V3, Compound V3, Morpho Blue, Uniswap V3
- **Staking** — Lido, EigenLayer, TRON Stake 2.0, Solana validators
- **Swaps** — LiFi and Jupiter v6
- **Security model assumes everything except hardware wallet may be compromised** — cryptographic bindings across layers detect tampering before signing

1,000+ commits of active development as of this audit (up from 918) — among the most commits of any single-purpose crypto MCP server in this review, though star count remains very low (2). The Business Source License converts to Apache-2.0 in 2030.

### debridge-finance/debridge-mcp (NEW — Cross-Chain Bridge)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [debridge-mcp](https://github.com/debridge-finance/debridge-mcp) | 32 | — | MIT | 5 |

**Fills the cross-chain bridge gap** from our initial review — AI agents can now execute cross-chain swaps:

- **25+ EVM chains + Solana** — [search 40,000+ tokens, get quotes, generate transaction data](https://docs.debridge.com/dln-details/mcp/mcp-server)
- **Non-custodial** — [the MCP server never touches private keys or signs transactions](https://docs.debridge.com/dln-details/mcp/mcp-server); users sign via generated deBridge App links
- **[27+ security audits, $23B+ volume settled with zero security incidents](https://debridge.com/security/)** (updated from the $20-22B figures in earlier drafts of this review — deBridge's own security page is the only source we have for the exploit-free claim; we did not find independent third-party audit-firm confirmation beyond deBridge's own audit-report links)
- **"Vibe Trading"** — describe the outcome you want, agent handles routing/bridging/swapping
- **TRON integration** — [added April 17, 2026](https://www.newsdirect.com/newsroom/tron-integrates-debridge-mcp-unlocking-seamless-cross-chain-execution-for-ai-agents)

This was explicitly listed as a "major gap" in our March review. Now filled.

## Market Data & Analytics

### coinpaprika/dexpaprika-mcp (Best DEX Data)

| Server | Language | License | Coverage |
|--------|----------|---------|----------|
| [dexpaprika-mcp](https://github.com/coinpaprika/dexpaprika-mcp) | — | — | 36 blockchain networks |

Broad DEX data coverage — real-time data across [36 blockchain networks](https://github.com/coinpaprika/dexpaprika-mcp) with DEX analytics. We could not independently confirm a "5 million tokens" figure from the repo's own documentation as an earlier version of this review stated, so we've replaced it with the network count we could verify directly.

### Official Market Data Servers (NEW)

Three major data providers launched official hosted MCP servers — a significant validation of the crypto MCP ecosystem:

| Server | Source | Tools | Access |
|--------|--------|-------|--------|
| [CoinGecko Official MCP](https://docs.coingecko.com/docs/mcp-server) | CoinGecko | Multiple | Hosted at mcp.api.coingecko.com. [CoinGecko's underlying API](https://www.coingecko.com/en/api) covers 17,000+ coins, 1,700+ exchanges, 42M+ tokens, and 250+ networks (up from 15K/1,000+/8M/200+ when we first reviewed it) — the MCP server itself doesn't publish separate coverage numbers. Source repo: [coingecko/coingecko-typescript](https://github.com/coingecko/coingecko-typescript) (57 stars) |
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

### TermiX-official/binance-mcp (Earliest Exchange Trading MCP We Found)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [binance-mcp](https://github.com/TermiX-official/binance-mcp) | 96 | TypeScript | 15 tool categories |

**Fills the single biggest gap from our March review** — centralized exchange trading with order execution:

- **Spot market orders** — place orders via [`binanceSpotPlaceOrder`](https://github.com/TermiX-official/binance-mcp), executes at best available prices
- **TWAP algorithmic trading** — `binanceTimeWeightedAveragePriceFutureAlgo` executes gradually to minimize market impact
- **Portfolio management** — view composition, market value, percentage allocation
- **Market data** — order books, klines, recent trades
- **Account management** — balances, trading history
- **15 tool categories** registered in the codebase (spot, algo, convert, C2C, wallet, copy trading, fiat, NFT, pay, rebate, dual investment, mining, VIP loan, staking, simple earn)

**Correction (2026-08-14 audit):** an earlier version of this review stated "23 tools" and "11 public tools (no API key needed)." We could not confirm either specific number against the repo's README or source — the README documents 5 tools in detail and states all of them require `BINANCE_API_KEY`/`BINANCE_API_SECRET` credentials (no API-key-free public tools are documented). We've replaced the tool count with what we could verify directly from the source: 15 registered tool categories. Star count updated from 77 to 96.

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

OpenSea [launched a **beta MCP server** in August 2025](https://opensea.io/blog/articles/opensea-digest-august-28-2025) providing AI agents with:

- Real-time NFT data across **20+ blockchains**
- **Collection verification** and rarity scores
- **Wallet balances** and ownership patterns
- **Trading volumes** and marketplace activity
- Portfolio evaluation and token discovery

It's among the first major NFT marketplaces to ship official MCP support, as far as we've found; we can't independently confirm it's strictly the first.

## Institutional & Custody (NEW)

| Server | Focus |
|--------|-------|
| [BitGo MCP](https://www.businesswire.com/news/home/20260323339524/en/BitGo-Launches-MCP-Server-Bringing-Institutional-Grade-Crypto-Infrastructure-to-AI-Agents) | Official institutional custody MCP (launched March 2026) — documentation access, API references, setup guidance. Transaction execution not yet available |

BitGo launched an official MCP server in March 2026, making institutional digital asset custody platform documentation accessible to AI development tools. Currently limited to documentation access — does not perform transactions or custody actions.

## Security & Forensics

| Server | Focus |
|--------|-------|
| [N-45div/ChainGuard](https://github.com/N-45div/ChainGuard) | Multi-chain crime/fraud detection — Bitcoin, Ethereum, Hedera, Solana (individual maintainer project, not a company product) |
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

The ecosystem transformed in 44 days from read-heavy/write-light to genuinely actionable. The three biggest gaps from our March review are all filled: **Binance trading** (96 stars, spot orders and TWAP across 15 tool categories), **cross-chain bridging** (deBridge across 25+ chains with $23B+ volume settled and, per deBridge's own security page, zero security incidents), and **portfolio tracking** (Octav across 20+ blockchains). Three major data providers — CoinGecko, CoinMarketCap, and Crypto.com — launched official hosted MCP servers in this period, validating the market data layer.

The security story improved dramatically with VaultPilot's hardware wallet approach (1,000+ commits, assuming compromised hosts) and Phantom expanding to four chains with scoped permissions. The x402 payment protocol creates a new primitive — AI agents can now autonomously pay for API access with stablecoins, enabling agent-to-agent commerce.

GOAT (~1,000 stars, now archived/unmaintained) remains the broadest action toolkit by feature count. Coinbase agentkit (1.3k stars) brings enterprise credibility with x402 payments. The Solana Foundation launched an official MCP server. Helius provides 10 public tools routing to 60+ underlying Solana operations. Pump.fun brings meme coin trading to AI agents.

Remaining weaknesses: derivatives/options/futures trading is absent. No crypto tax reporting. Smart contract audit tooling is limited. But the category's trajectory is clear — it's moving from experimental to production-ready faster than almost any other MCP vertical.

---

*This review is part of our comprehensive [MCP servers comparison](/guides/best-mcp-servers/) covering 100+ categories.*

**Category**: [Finance & Fintech](/categories/finance-fintech/)

*This review was last refreshed on 2026-04-30 using Claude Opus 4.6 (Anthropic); claim-level citation re-audit and corrections on 2026-08-14 using Claude Sonnet 5 (Anthropic).*

