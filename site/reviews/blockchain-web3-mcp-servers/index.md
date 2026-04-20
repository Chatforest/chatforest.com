# Blockchain & Web3 MCP Servers — Ethereum, Solana, Bitcoin, Multi-Chain, DeFi, and More

> Blockchain and Web3 MCP servers let AI agents query balances, send transactions, interact with smart contracts, and execute DeFi operations through natural language.


Blockchain and Web3 is one of the largest MCP categories by server count but also one of the most fragmented. AI agents that can query balances, decode transactions, interact with smart contracts, and execute DeFi operations through natural language represent a natural evolution — blockchains are API-native systems with deterministic interfaces, ideal for tool-based interaction. The category spans six areas: **multi-chain platforms** (EVM MCP Server, Tatum, GOAT, Strangelove web3-mcp), **Solana** (official Foundation server, SendAI Agent Kit, openSVM), **Ethereum/EVM wallets and explorers** (dcSpark, Etherscan, Bankless), **Bitcoin** (AbdelStark bitcoin-mcp with Lightning), **DeFi and trading** (defi-trading-mcp, DeFAI), and **market data** (CoinGecko, CoinMarketCap).

The headline finding: **The EVM MCP Server has the strongest multi-network coverage** — 22 tools across 60+ EVM networks with automatic ABI fetching from block explorers and ENS resolution on every address parameter. **GOAT has the broadest onchain action coverage** with 200+ tools spanning DeFi protocols (Uniswap, Jupiter, Orca), NFT marketplaces (OpenSea, MagicEden), prediction markets (Polymarket), and analytics (CoinGecko, BirdEye) across EVM, Solana, and 10+ other chains. **The main gap is safety** — most servers that support write operations (sending transactions, executing trades) have minimal guardrails, making autonomous agent usage risky for anything involving real funds.

## Multi-Chain Platforms

### EVM MCP Server

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [mcpdotdirect/evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server) | 362 | TypeScript | 22 | stdio |

**mcpdotdirect/evm-mcp-server** (362 stars, TypeScript, 94 forks) is the most comprehensive EVM-focused MCP server. Twenty-two tools plus 10 AI-guided prompts covering:

**Blockchain state** — reading balances (native + ERC-20), transaction history, block data, gas prices, and contract storage across 60+ EVM networks (34 mainnets + 26 testnets). Supports Ethereum, Optimism, Arbitrum, Base, Polygon, and dozens more.

**Smart contract interaction** — automatic ABI fetching from Etherscan v2 API across all supported networks, contract read/write operations, and event log querying. This eliminates the manual ABI lookup step that makes smart contract interaction tedious.

**Token operations** — transfers for native tokens, ERC-20, ERC-721 (NFTs), and ERC-1155 (multi-tokens).

**ENS resolution** — all address parameters automatically resolve ENS names, so agents can use human-readable names like `vitalik.eth` instead of raw addresses.

The standout feature is the breadth: 60+ networks from a single server with consistent tooling. Most chain-specific servers cover 1-3 networks. The automatic ABI fetching is genuinely useful — it means the agent can interact with any verified contract without manual setup.

### Tatum Blockchain MCP

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [tatumio/blockchain-mcp](https://github.com/tatumio/blockchain-mcp) | 14 | TypeScript | 8+ | stdio |

**tatumio/blockchain-mcp** (14 stars, TypeScript, MIT) provides access to the Tatum Blockchain Data API and RPC Gateway across 130+ networks including Bitcoin, Ethereum, Solana, Polygon, Arbitrum, Base, and Avalanche. Tools include `get_wallet_balance_by_time`, `get_wallet_portfolio`, `get_transaction_history`, `get_metadata` (NFT/multitoken), `get_owners`, `check_owner`, `get_tokens`, and `get_block_by_time`.

The 130+ network count is the highest of any blockchain MCP server, but Tatum is primarily a read-only data API — you can query blockchain state comprehensively but can't send transactions. This makes it safe for analytics and monitoring but not useful for agents that need to execute operations. Requires a Tatum API key (free tier available).

### GOAT (Great Onchain Agent Toolkit)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [goat-sdk/goat](https://github.com/goat-sdk/goat) | 398 | TypeScript | 200+ | stdio |

**goat-sdk/goat** (398 stars, TypeScript, MIT) is the leading agentic finance toolkit. Rather than a single MCP server, GOAT is a modular framework where you install only the plugins you need. Over 200 onchain actions across:

**DeFi** — Uniswap, Jupiter, KIM, Orca, and more for swaps and liquidity. **Minting** — OpenSea, MagicEden for NFT operations. **Betting** — Polymarket for prediction market interaction. **Analytics** — CoinGecko, BirdEye, Allora for market data and price feeds.

Chain support spans EVM (Base, Polygon, Mode, Sei), Solana, Aptos, Chromia, Fuel, Sui, Starknet, Zilliqa, and more. The MCP adapter (`@goat-sdk/adapter-model-context-protocol`) wraps any combination of GOAT plugins into an MCP server compatible with Claude Desktop.

The design philosophy is right — keep the core minimal, let users compose their toolset. The tradeoff is complexity: setting up GOAT requires choosing chains, wallets, and plugins, which is more involved than single-purpose servers. But for agents that need broad cross-chain DeFi capabilities, nothing else comes close.

### Strangelove web3-mcp

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [strangelove-ventures/web3-mcp](https://github.com/strangelove-ventures/web3-mcp) | — | TypeScript | varies | stdio |

**strangelove-ventures/web3-mcp** is a unified MCP server for interacting with multiple blockchains — Solana, Ethereum, THORChain, XRP Ledger, TON, Cardano, and UTXO chains (Bitcoin, Litecoin, Dogecoin, Bitcoin Cash). Configuration via environment variables: `ENABLE_SOLANA_TOOLS`, `ENABLE_ETHEREUM_TOOLS`, `ENABLE_CARDANO_TOOLS`, `ENABLE_BITCOIN_TOOLS`, etc.

The standout feature is non-EVM chain support — Cardano, XRP Ledger, and TON are rarely covered by other MCP servers. Cross-chain swap and quote capabilities where supported (via THORChain). Strangelove Ventures is known in the Cosmos/IBC ecosystem, lending credibility to the cross-chain functionality.

## Solana

### Solana Foundation (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [solana-foundation/solana-mcp-official](https://github.com/solana-foundation/solana-mcp-official) | 42 | TypeScript | docs | HTTP |

**solana-foundation/solana-mcp-official** (42 stars) is the official Solana Developer MCP, hosted at mcp.solana.com. Unlike most blockchain MCP servers, this is a **documentation server** — it serves up-to-date Solana ecosystem documentation to AI agents and IDE assistants (Cursor, Windsurf, Claude CLI). The purpose is helping developers build on Solana, not interacting with the blockchain directly. Uses Vercel's `@vercel/mcp-adapter` for dual endpoint support (mcp.solana.com/mcp and mcp.solana.com/sse).

This is a developer experience play, not a blockchain interaction tool. Valuable if you're building Solana applications; not useful if you want an agent to read/write onchain data.

### SendAI Solana MCP (Agent Kit)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [sendaifun/solana-mcp](https://github.com/sendaifun/solana-mcp) | 139 | TypeScript | 11 | stdio |

**sendaifun/solana-mcp** (139 stars, TypeScript) extends Claude's capabilities with Solana blockchain interaction, powered by the Solana Agent Kit. Eleven tools: `GET_ASSET` (token info), `DEPLOY_TOKEN` (deploy new tokens), `GET_PRICE` (price feeds), `WALLET_ADDRESS`, `BALANCE`, `TRANSFER`, `MINT_NFT`, `TRADE` (token swaps), `REQUEST_FUNDS` (devnet faucet), `RESOLVE_DOMAIN` (Solana domain names), `GET_TPS` (network performance).

This is the most practical Solana MCP server for agents that need to execute operations. The Agent Kit (sendaifun/solana-agent-kit, separate repo) supports 40+ protocol actions and growing. The MCP server exposes the most common ones. Note: operations like `DEPLOY_TOKEN`, `TRANSFER`, and `TRADE` involve real funds on mainnet — use with extreme caution.

### openSVM Solana MCP Server

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [openSVM/solana-mcp-server](https://github.com/openSVM/solana-mcp-server) | 33 | Rust | RPC methods | stdio, HTTP |

**openSVM/solana-mcp-server** (33 stars, Rust) provides comprehensive access to Solana RPC methods — querying account data, managing tokens, and analyzing transactions. Built in Rust for performance. Supports both stdio transport and HTTP JSON-RPC mode. Multi-network support and flexible deployment options (Docker, Kubernetes, AWS Lambda, Google Cloud Functions, Vercel Edge, Netlify).

The deployment flexibility is notable — one-liner scripts for every major platform. This is primarily a read-focused server exposing standard Solana RPC methods through MCP, making it useful for monitoring and analysis rather than transaction execution.

## Ethereum/EVM Wallets and Explorers

### dcSpark Crypto Wallet EVM

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [dcSpark/mcp-cryptowallet-evm](https://github.com/dcSpark/mcp-cryptowallet-evm) | 8 | TypeScript | 10+ | stdio |

**dcSpark/mcp-cryptowallet-evm** (8 stars, TypeScript, MIT) provides wallet operations via ethers.js v5 — `wallet_create_random`, `wallet_from_private_key`, `wallet_from_mnemonic`, `wallet_from_encrypted_json`, plus balance checking, transaction sending, and smart contract interaction.

This is a wallet-focused server rather than a blockchain data server. It handles key generation and transaction signing. Low adoption (8 stars) but functional for basic EVM wallet operations.

### Etherscan MCP Server

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [crazyrabbitLTC/mcp-etherscan-server](https://github.com/crazyrabbitLTC/mcp-etherscan-server) | 26 | TypeScript | 6 | stdio |

**crazyrabbitLTC/mcp-etherscan-server** (26 stars, TypeScript, MIT) provides Ethereum blockchain data through Etherscan's API. Six tools: check ETH balance, view transaction history, track ERC-20 transfers, fetch contract ABIs, monitor gas prices, and resolve ENS names. Created by Dennison Bertram (CEO of Tally.xyz, former OpenZeppelin Developer Advocate).

Focused and well-built for its scope, but the EVM MCP Server (above) covers Etherscan data access plus much more across 60+ networks. This is useful if you only need Ethereum mainnet and want a lightweight server.

## Bitcoin

### Bitcoin & Lightning MCP

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [AbdelStark/bitcoin-mcp](https://github.com/AbdelStark/bitcoin-mcp) | 73 | Rust | 5+ | stdio |

**AbdelStark/bitcoin-mcp** (73 stars, Rust) enables AI models to interact with Bitcoin and Lightning Network. Key tools: **key generation** (create Bitcoin key pairs with address, public key, and WIF private key), **address validation** (check address correctness), **transaction decoding** (parse raw transactions into human-readable format), plus Lightning Network support including **invoice decoding** and **payment** capabilities.

This is the most capable Bitcoin-focused MCP server. Lightning Network support is unique — no other blockchain MCP server handles L2 payment channels. The Rust implementation is a good fit for cryptographic operations. AbdelStark also maintains a separate `lightning-mcp` repository focused specifically on Lightning.

## DeFi and Trading

### DeFi Trading Agent MCP

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [edkdev/defi-trading-mcp](https://github.com/edkdev/defi-trading-mcp) | 39 | TypeScript | 10+ | stdio |

**edkdev/defi-trading-mcp** (39 stars, TypeScript) transforms AI into an autonomous crypto trading agent with real-time market analysis, portfolio management, and trade execution across 17+ blockchains including Ethereum, Polygon, BSC, Arbitrum, Optimism, Base, Avalanche, Worldchain, Berachain, Blast, Linea, Scroll, Mantle, Ink, and MonadTestnet.

**Important safety warning:** autonomous trading agents executing real trades with real funds is inherently high-risk. This server is better suited for monitoring, analysis, and paper trading than unsupervised live trading. There's no mention of transaction limits, confirmation steps, or emergency stop mechanisms.

### DeFAI MCP (BNB Chain)

DeFAI MCP is an AI-powered DeFi agent for BNB Chain with yield optimization, cross-DEX arbitrage, and delta-neutral strategies, using ERC-4337 account abstraction for gasless transactions. It was the first on-chain DeFi MCP server specifically targeting BNB Chain. Early-stage but architecturally interesting for its account abstraction approach.

## Market Data

### CoinGecko MCP (Official)

CoinGecko provides an official MCP server offering real-time market data with aggregated prices, market cap, and trading volume for 15,000+ coins across 1,000+ exchanges. Capabilities include onchain DEX price and liquidity data, trending coins, new token listings, top gainers/losers, and popular NFT collections. This is the strongest market data source — CoinGecko's data coverage is industry-standard.

### CoinMarketCap MCP Servers

Multiple community CoinMarketCap MCP servers exist: **longmans/coin_api_mcp** provides cryptocurrency listings and quotes. **shinzo-labs/coinmarketcap-mcp** is another implementation. **szcharlesji/crypto-mcp** offers tools for listings, quotes, ID mappings, metadata, global metrics, and exchange information. All require CoinMarketCap API keys (free tier available).

## Also notable

**Bankless Onchain** — query onchain data including ERC-20 tokens, transaction history, and smart contract state. **kukapay/chainlist-mcp** — gives AI agents fast access to verified EVM chain information (RPC URLs, chain IDs, explorers, native tokens). **magnetai/mcp-free-usdc-transfer** — send USDC on Base for free using Coinbase CDP's MPC wallet technology. **SettleMint MCP** — enterprise blockchain platform integration for smart contract management, deployment, and blockchain network interaction. **OpenSea MCP** — official hosted server for NFT operations, token swaps, collection analytics, and wallet management across major chains. **BitGo MCP Server** (March 2026) — documentation-access MCP server from the institutional digital asset custody company BitGo (federally chartered BitGo Bank & Trust). Connects AI agents to BitGo's Developer Portal for wallet functionality, transaction flows, staking docs, webhooks, and policy features via natural language. Read-only — does not execute transactions or manage custody. **royyannick/awesome-blockchain-mcps** — a curated awesome-list specifically for blockchain and crypto MCP servers.

## The bigger picture

Blockchain and Web3 is a large but uneven MCP category. The **read side is strong** — between EVM MCP Server (60+ networks), Tatum (130+ networks), and CoinGecko (15,000+ coins), agents can access virtually any blockchain data. The **write side is risky** — servers like SendAI's Solana MCP and defi-trading-mcp enable real transaction execution, but safety controls are minimal. There's no standardized way to limit transaction amounts, require confirmation, or prevent agents from draining wallets.

The fragmentation is notable. Rather than a few comprehensive servers, the space has dozens of chain-specific and protocol-specific tools. GOAT's modular approach is the right architecture for this — compose what you need rather than running one massive server. But it requires more setup knowledge than other MCP categories.

**Who should use these:** Developers building blockchain analytics tools, portfolio trackers, or blockchain-aware AI assistants. For read-only use cases (querying balances, analyzing transactions, monitoring prices), these servers are practical today. For write operations (sending transactions, executing trades), proceed with extreme caution — preferably on testnets first.

**Rating: 3.5/5** — Strong data access coverage across most major chains, an active community ecosystem, and good diversity of approaches. Loses points for fragmentation (no single server covers everything well), minimal safety controls on write operations, and the inherent risk of connecting AI agents to financial systems. The category will mature significantly as MCP security patterns (OAuth 2.1, permission scopes, transaction limits) become standard.

**Category**: [Finance & Fintech](/categories/finance-fintech/)

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

