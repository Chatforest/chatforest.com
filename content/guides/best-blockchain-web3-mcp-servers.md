---
title: "Best Blockchain & Web3 MCP Servers in 2026"
date: 2026-03-22T23:00:00+09:00
description: "GOAT, Coinbase AgentKit, EVM MCP Server, Solana MCP, Bitcoin MCP, and more — we've researched 40+ blockchain and Web3 MCP servers across 8 categories."
og_description: "40+ blockchain and Web3 MCP servers reviewed across multi-chain toolkits, EVM networks, Solana, Bitcoin, DeFi data, NFT/marketplace, Starknet/L2, and market analytics. The definitive comparison with honest ratings."
content_type: "Comparison"
card_description: "The definitive guide to blockchain and Web3 MCP servers in 2026. We've researched 40+ servers across multi-chain toolkits, EVM networks, Solana, Bitcoin, DeFi data, NFT marketplaces, L2/alt-chain specialists, and market analytics. Every recommendation links to a full review."
last_refreshed: 2026-04-04
---

Blockchain MCP servers are where AI agents meet onchain. These servers let AI assistants query balances, send transactions, interact with smart contracts, execute DeFi operations, mint NFTs, and pull market data — all through natural language instead of writing raw API calls or navigating block explorer UIs.

We've researched 40+ blockchain and Web3 MCP servers across the entire crypto ecosystem. This guide synthesizes all of that into one page: what's worth using, what's not, and where the gaps are.

*Note: Our recommendations are based on documentation review, GitHub analysis, and community feedback — not hands-on testing of every server. Star counts were verified in March 2026.*

## The short version

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| Multi-chain toolkit | [goat-sdk/goat](https://github.com/goat-sdk/goat) | 966 | [strangelove-ventures/web3-mcp](https://github.com/strangelove-ventures/web3-mcp) (10+ chains) |
| EVM networks | [mcpdotdirect/evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server) | 362 | [tatumio/blockchain-mcp](https://github.com/tatumio/blockchain-mcp) (130+ networks) |
| Solana | [sendaifun/solana-mcp](https://github.com/sendaifun/solana-mcp) | 153 | Solana Foundation (official, mcp.solana.com) |
| Bitcoin & Lightning | [AbdelStark/bitcoin-mcp](https://github.com/AbdelStark/bitcoin-mcp) | 73 | Community alternatives |
| Agentic wallets & payments | [coinbase/agentkit](https://github.com/coinbase/agentkit) | 1,200 | [coinbase/payments-mcp](https://github.com/coinbase/payments-mcp) (51 stars) |
| DeFi data & trading | [defi-llama MCP](https://github.com/demcp/demcp-defillama-mcp) | — | DexScreener MCP, Jupiter MCP |
| Cross-chain execution | [deBridge MCP](https://github.com/debridge-finance/debridge-mcp) | — | VeChain AI Terminal (limited) |
| NFT & marketplace | [thirdweb-dev/ai](https://github.com/thirdweb-dev/ai) (thirdweb-mcp) | — | OpenSea MCP (official hosted) |
| Market analytics | [CoinGecko MCP](https://github.com/nicobailon/coingecko-mcp-server) | — | CoinMarketCap MCP |

## Why blockchain MCP servers matter

Blockchains are API-native systems with deterministic interfaces — ideal for AI tool use. Blockchain MCP servers add three capabilities that transform how developers and traders work:

1. **Natural language onchain operations.** Instead of assembling raw transactions, ABI-encoding function calls, or navigating dApp UIs, tell your agent: "Swap 1 ETH for USDC on Uniswap" or "Check the staking rewards for vitalik.eth." The agent translates that into the right contract calls with proper encoding.
2. **Cross-chain visibility.** An agent with access to multi-chain servers can answer questions like "What's the total value of my wallets across Ethereum, Solana, and Base?" by querying multiple networks — something that normally requires switching between different block explorers and wallets.
3. **Automated DeFi workflows.** "Monitor this liquidity pool, alert me if TVL drops below $1M, and show me the top yield opportunities on Arbitrum" becomes a natural language instruction. AI agents can track positions, analyze protocols, and surface opportunities programmatically.

The landscape splits into eight categories: **multi-chain toolkits** (GOAT and web3-mcp providing unified interfaces), **EVM networks** (EVM MCP Server dominating with 60+ chains), **Solana** (SendAI's Agent Kit), **Bitcoin** (Lightning-enabled), **agentic wallets and payments** (Coinbase leading with x402), **DeFi data** (DefiLlama and DEX analytics), **NFT and marketplaces** (thirdweb and OpenSea), and **market analytics** (CoinGecko and CoinMarketCap).

## Multi-chain toolkits

Multi-chain toolkits provide a single MCP server interface to interact with multiple blockchain networks. They're the starting point for most agent builders because they offer the broadest coverage without managing separate servers per chain.

### The winner: goat-sdk/goat (GOAT — Great Onchain Agent Toolkit)

**Stars:** 966 | **Language:** TypeScript, Python | **Status:** Production

[goat-sdk/goat](https://github.com/goat-sdk/goat) is the largest agentic finance toolkit for AI agents, built by Crossmint. GOAT provides a single, unified library of onchain actions ready to use across 5 agent frameworks, two programming languages, on any wallet architecture across 30+ chains.

**Why it wins:** GOAT offers 200+ onchain actions spanning DeFi protocols (Uniswap, Jupiter, Orca, 1inch), NFT marketplaces (OpenSea, MagicEden), prediction markets (Polymarket), analytics (CoinGecko, BirdEye, DeFiLlama), and token operations across EVM, Solana, and additional chains. The modular architecture means you install only the plugins you need — keeping the core lightweight while supporting the broadest action set of any blockchain MCP.

**Key features:** Token swaps, liquidity provision, lending/borrowing, NFT minting and trading, wallet balances, transaction history, price feeds, and staking — all from a single toolkit. MCP integration is provided via example implementations for both EVM (Base Sepolia) and Solana.

**The strategic angle:** GOAT's "one toolkit to rule all chains" approach means your agent code doesn't change when you add a new chain or protocol. The plugin architecture supports community-contributed integrations, which is why coverage keeps growing.

**The catch:** GOAT is a toolkit with MCP examples rather than a dedicated MCP server — you build your MCP server on top of GOAT. This gives maximum flexibility but requires more setup than a turnkey solution. The breadth also means you need to carefully scope which plugins you enable to avoid exposing too many tools.

### Runner-up: strangelove-ventures/web3-mcp

**Stars:** — | **Language:** TypeScript | **Status:** Active

[strangelove-ventures/web3-mcp](https://github.com/strangelove-ventures/web3-mcp) — "1 MCP to rule all them chains." Supports Solana, Ethereum, Cardano, XRP Ledger, TON, THORChain, Bitcoin, Litecoin, Dogecoin, and Bitcoin Cash through a unified RPC interface. Environment variable toggles (`ENABLE_SOLANA_TOOLS`, `ENABLE_ETHEREUM_TOOLS`, etc.) let you control which chains are active. Comes from Strangelove Ventures, a well-known Cosmos ecosystem team.

**Why it's interesting:** Broadest chain diversity in a single server — covering UTXO chains (Bitcoin, Litecoin, Dogecoin, Bitcoin Cash), account-based chains (Ethereum, Solana, Cardano), and niche networks (THORChain, TON, XRP). Most multi-chain solutions focus only on EVM or EVM + Solana.

**The catch:** Thinner feature depth per chain than specialized servers. Good for balance queries and basic operations, but for advanced DeFi or smart contract interactions, you'll want chain-specific tools.

### Also notable

- **[tatumio/blockchain-mcp](https://github.com/tatumio/blockchain-mcp)** (14 stars) — Access to Tatum's Blockchain Data API and RPC Gateway across 130+ networks. Eight tools covering balances, portfolios, transaction history, NFT metadata, and block queries. Read-focused — excellent for analytics but no write operations. Supports Bitcoin, Ethereum, Solana, Polygon, Arbitrum, Cardano, Stellar, Ripple, and many more.

## EVM networks

EVM (Ethereum Virtual Machine) networks are the largest blockchain ecosystem. These servers focus specifically on EVM-compatible chains — Ethereum mainnet plus L2s and alt-L1s like Polygon, Arbitrum, Base, and Optimism.

### The winner: mcpdotdirect/evm-mcp-server

**Stars:** 362 | **Language:** TypeScript | **Status:** Production

[mcpdotdirect/evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server) is the most comprehensive EVM-focused MCP server, providing 22 tools and 10 AI-guided prompts across 60+ EVM networks (34 mainnets + 26 testnets).

**Why it wins:** Three features set it apart: (1) **Automatic ABI fetching** from Etherscan v2 API across all supported networks — the agent can interact with any verified contract without manual ABI setup, (2) **ENS resolution** on every address parameter, so agents can use human-readable names like `vitalik.eth`, and (3) **60+ network breadth** from a single server with consistent tooling, covering Ethereum, Optimism, Arbitrum, Base, Polygon, Filecoin, and dozens more.

**Key features:** Blockchain state reading (balances, transactions, blocks, gas prices), smart contract interaction (read/write with auto-ABI), token transfers (native, ERC-20, ERC-721, ERC-1155), and event log querying.

**The catch:** Write operations (sending transactions, token transfers) require a private key in the environment. No built-in guardrails for transaction safety — the agent can spend whatever the wallet holds.

### Also notable

- **[dcSpark/mcp-server-dcspark](https://github.com/dcSpark/mcp-server-dcspark)** — Cardano + EVM tools. dcSpark builds infrastructure across chains and provides multi-chain read operations.
- **Etherscan MCP** — Block explorer integration for transaction lookups, contract verification status, and address analytics.
- **Bankless MCP** — Bankless-branded server for DeFi analytics and Ethereum ecosystem data.
- **[Chainstack EVM MCP](https://docs.chainstack.com/docs/evm-mcp-server)** — Node provider Chainstack offers an EVM MCP server via their infrastructure, providing reliable RPC access.

## Solana

Solana has become a hotbed for AI-agent blockchain interaction, driven by the SendAI ecosystem and the Solana Foundation's early MCP support.

### The winner: sendaifun/solana-mcp

**Stars:** 153 | **Language:** TypeScript | **Status:** Production

[sendaifun/solana-mcp](https://github.com/sendaifun/solana-mcp) is powered by the Solana Agent Kit, providing 60+ Solana actions through MCP. Asset retrieval, token deployment, wallet management, transfers, NFT minting, domain resolution, and DeFi operations — all exposed as MCP tools.

**Why it wins:** Built on the Solana Agent Kit, which is the most actively maintained Solana agent toolkit with deep protocol integrations. Supports Jupiter swaps, staking, SPL token operations, and Solana name resolution. The underlying Agent Kit supports cross-chain operations and multi-agent systems via LangGraph.

**Key features:** Token swaps (via Jupiter), SPL token creation and transfer, NFT minting, wallet balance queries, transaction history, domain resolution, and Voltr vault interactions.

**The catch:** Requires a Solana private key for write operations. The 60+ action surface area is powerful but means careful scoping is needed for production agents.

### Also notable

- **Solana Foundation official** (mcp.solana.com) — The official Solana Foundation MCP server focuses on developer documentation access rather than onchain operations. Useful for agents that need to reference Solana docs while building, not for executing transactions.
- **openSVM** — Alternative Solana MCP with validator-level data access.
- **[sendaifun/solana-agent-kit](https://github.com/sendaifun/solana-agent-kit)** (separate from the MCP server) — The underlying agent toolkit with broader framework support (LangChain, CrewAI, Vercel AI SDK). If you need Solana access in a non-MCP framework, start here.

## Bitcoin & Lightning

Bitcoin MCP is smaller than EVM or Solana but covers the essentials — key generation, address validation, transaction decoding, and Lightning Network payments.

### The winner: AbdelStark/bitcoin-mcp

**Stars:** 73 | **Language:** TypeScript | **Status:** Active

[AbdelStark/bitcoin-mcp](https://github.com/AbdelStark/bitcoin-mcp) provides Bitcoin and Lightning Network tools through MCP. Key generation, address validation, transaction decoding, block queries, and Lightning invoice decoding and payment.

**Why it wins:** It's the only Bitcoin MCP server that covers both the base layer and Lightning Network. Invoice decoding (BOLT11) and LNBits wallet integration for Lightning payments set it apart from read-only alternatives. The block and transaction query tools provide essential blockchain data access.

**Key features:** Bitcoin key pair generation, address validation (all formats), raw transaction decoding, latest block retrieval, transaction lookup by TXID, Lightning invoice decoding (BOLT11), and Lightning invoice payment via LNBits.

**The catch:** Lightning payment requires a running LNBits instance. The server covers Bitcoin basics well but doesn't support advanced features like Ordinals, BRC-20 tokens, or Taproot-specific operations.

### The gap

Bitcoin MCP lags behind EVM and Solana in tooling depth. There's no equivalent of the EVM MCP Server's 22-tool breadth or GOAT's 200+ action library. Missing: Ordinals/inscriptions, BRC-20 token management, PSBT (Partially Signed Bitcoin Transactions) construction, multi-sig coordination, and Taproot-native operations. As Bitcoin DeFi (BTCFi) grows through Starknet and other L2s, expect this gap to narrow.

## Agentic wallets & payments

This is the fastest-moving category, driven by Coinbase's vision of AI agents as autonomous economic participants.

### The winner: coinbase/agentkit

**Stars:** 1,200 | **Language:** TypeScript, Python | **Status:** Production

[coinbase/agentkit](https://github.com/coinbase/agentkit) is Coinbase Developer Platform's toolkit for giving AI agents crypto wallets and onchain interaction capabilities. In February 2026, Coinbase launched **Agentic Wallets** — the first wallet infrastructure specifically designed for autonomous AI agents.

**Why it wins:** Coinbase brings institutional-grade infrastructure to agent wallets. Agentic Wallets allow agents to independently hold funds, send payments, trade tokens, earn yield, and transact onchain with built-in security guardrails. The toolkit supports MCP, Claude, LangChain, and other frameworks. Integration with the **x402 protocol** enables autonomous crypto payments between agents without human intervention.

**Key features:** Wallet creation and management, token transfers, token trading, yield operations, Base L2 optimization, stablecoin payments, and security guardrails. The **Payments MCP** component (`coinbase/payments-mcp`, 51 stars) specifically enables agentic commerce with on-ramps and stablecoin operations.

**The strategic angle:** Coinbase is building x402 with Cloudflare and other internet infrastructure companies as a protocol for machine-to-machine payments. AgentKit is the developer interface to that vision. In March 2026, World (Sam Altman's identity project) integrated with AgentKit to provide verified human identity behind AI agents using zero-knowledge proofs.

**The catch:** Optimized for Base (Coinbase's L2) — other chain support is secondary. The agentic wallet features are new and the security model is still being validated in production.

### Also notable

- **[base/base-mcp](https://github.com/base/base-mcp)** — Base L2-specific onchain tools, tightly integrated with the Coinbase ecosystem.
- **[coinbase/payments-mcp](https://github.com/coinbase/payments-mcp)** (51 stars) — Focused specifically on payment operations: on-ramps, stablecoin payments, and commerce flows.
- **BitGo MCP Server** (March 2026) — BitGo, the institutional digital asset custody and infrastructure company (includes the federally chartered BitGo Bank & Trust), launched an MCP server for developer documentation access. The server connects AI agents to BitGo's Developer Portal — documentation, API references, setup guidance, wallet functionality, transaction flows, staking docs, webhook configuration, and policy features — all via natural language. Important limitation: the MCP server is currently read-only documentation access. It does not execute transactions, manage custody, or perform onchain operations through AI agents. Compatible with Claude Code, Claude Desktop, Cursor, ChatGPT, JetBrains IDEs, VS Code, and Windsurf.

## DeFi data & trading

DeFi MCP servers split into two camps: **data servers** that provide analytics and market information, and **trading servers** that execute swaps and manage positions. Most data servers are read-only; trading servers carry financial risk.

### Data servers

- **DefiLlama MCP** — Access to DefiLlama's API for TVL data, token prices, stablecoin metrics, revenue, fees, volume, and yields across 7,000+ DeFi protocols on 500+ chains. The essential starting point for DeFi analytics.
- **DexScreener MCP** — Real-time DEX pair data and market statistics across multiple blockchains. Data retrieval only — provides information for trading decisions but doesn't execute trades. Tracks newly listed pairs, price movements, and liquidity changes.
- **Chainlink Feeds MCP** — Real-time access to Chainlink's decentralized onchain price feeds. Essential for agents that need reliable, manipulation-resistant price data.

### Trading servers

- **Jupiter MCP** — Execute token swaps on Solana using Jupiter's Ultra API. Jupiter aggregates liquidity across Solana DEXes for best execution. The primary MCP route for Solana DeFi.
- **Uniswap trader servers** — Various community implementations for Uniswap V2/V3 swaps on EVM chains. Fragmented — no single dominant implementation.
- **PancakeSwap Poolspy MCP** — Tracks newly created liquidity pools on PancakeSwap for DeFi analysts and traders.

### Cross-chain execution

**[deBridge MCP](https://github.com/debridge-finance/debridge-mcp)** — The first dedicated MCP server for cross-chain DeFi execution. deBridge MCP gives AI agents non-custodial swap, bridge, and trading capabilities across 25+ EVM chains and Solana through a single interface.

**Key tools:** `get_supported_chains`, `search_tokens`, `create_tx`, `get_instructions`, `transaction_same_chain_swap` — covering the full lifecycle from token discovery to cross-chain execution.

**Why it matters:** deBridge's April 2026 update added composable skills and an agent discovery layer, enabling what they call "Vibe Trading" — describe the outcome you want (e.g., "move 500 USDC from Ethereum to Arbitrum and swap for ARB"), and the agent handles routing, bridging, chain switching, and execution. The hosted MCP endpoint at `agents.debridge.com` means no local infrastructure needed.

**Architecture:** MEV-aware routing optimized for reliability, deterministic execution with quotes designed to execute as intended, and full user custody throughout — the agent orchestrates but never holds funds. Supports Streamable HTTP transport.

**The catch:** Cross-chain operations carry inherent bridge risk. deBridge has processed significant volume but bridge exploits remain a real threat in DeFi. Agents executing cross-chain transfers should implement value limits and confirmation steps.

### The gap

No unified DeFi MCP server exists that combines analytics (like DefiLlama) with execution (like Jupiter) across multiple chains. You need to compose multiple servers. Also missing: automated yield farming strategies, impermanent loss monitoring, liquidation alerts, and portfolio rebalancing tools.

## NFT & marketplace

NFT MCP servers let agents interact with NFT collections, mint tokens, and access marketplace data.

### The winner: thirdweb-mcp

[thirdweb-dev/ai](https://github.com/thirdweb-dev/ai) (in `python/thirdweb-mcp`) — thirdweb's MCP server provides a unified interface to thirdweb's blockchain tool suite: Nebula (AI onchain analysis), Insight (blockchain data), Engine (server-side transactions), EngineCloud (managed infrastructure), and Storage (IPFS/decentralized storage).

**Why it wins:** thirdweb is a full-stack Web3 development platform, and the MCP server exposes that entire stack. Contract deployment, NFT minting, token operations, and storage — all through one interface. Supports virtually all EVM chains and Solana. The Engine product handles server-side transactions for production-grade minting operations.

**The catch:** Beta release (v0.1). Requires a thirdweb API key and setup. The broad surface area means you need to understand thirdweb's product suite to use it effectively.

### Also notable

- **OpenSea MCP** — Official hosted MCP server from OpenSea exposing tools for NFT collections, items, token data, wallet balances, swap quotes, trending analytics, and more across major chains. [Sample implementation](https://github.com/ProjectOpenSea/opensea-mcp-next-sample) available.
- **Crossmint** — While no dedicated MCP server exists yet, Crossmint's API (used by GOAT) provides NFT minting and wallet-as-a-service, accessible through GOAT's Crossmint plugin.

## Layer 2 & alt-chain specialists

Several MCP servers focus on specific chains beyond Ethereum mainnet and Solana.

### Starknet

Multiple implementations exist:
- **[mcpdotdirect/starknet-mcp-server](https://github.com/mcpdotdirect/starknet-mcp-server)** — From the same team behind the EVM MCP Server. Wallet management, smart contract interaction, and blockchain data queries on Starknet.
- **[AbdelStark/starknet-mcp](https://github.com/AbdelStark/starknet-mcp)** — From the same developer behind bitcoin-mcp. Starknet-specific operations.
- **[Kasar Labs ask-starknet-mcp](https://www.npmjs.com/package/@kasarlabs/ask-starknet-mcp)** — Starknet data queries via MCP.

Starknet is positioning itself as both an Ethereum zk-rollup and a Bitcoin execution layer, with native BTC staking and BTCFi features planned through 2026.

### VeChain

- **VeChain MCP Server** — Access to VeChain ecosystem documentation and blockchain data.
- **VeChain AI Terminal MCP** — Natural language interaction with VeChain: token transfers, DEX trading, cross-chain bridges, NFT management, and VeBetter DAO interactions.

### TRON

- **[TronScan MCP Server](https://mcpdoc.tronscan.org/en/mcp)** — Official MCP server from TronScan, the TRON blockchain explorer. Launched March 9, 2026 with 105 tool interfaces covering the TRON ecosystem: account data, TRX and TRC-20 token queries, smart contract interactions, transaction history, staking/voting information, and on-chain analytics. Production endpoint at mcp.tronscan.org via Streamable HTTP transport (MCP protocol version 2025-06-18). Rate limits apply by default; API key available for high-frequency use. This is notable as one of the most comprehensive official blockchain explorer MCP integrations, with far more tools than typical chain-specific servers.

### Other chains

- **NEAR Protocol MCP** — LLM querying and transaction execution on NEAR.
- **Cardano** — Covered by Strangelove's web3-mcp and dcSpark's multi-chain server.
- **TON** — Covered by Strangelove's web3-mcp for basic operations.

## Market analytics

Market data MCP servers provide price feeds, trading volumes, and market statistics without direct onchain interaction.

- **CoinGecko MCP** — Access to CoinGecko's data for 15,000+ coins: prices, market caps, trading volumes, DEX analytics, and trending tokens. The most comprehensive free crypto data API exposed via MCP.
- **CoinMarketCap MCP** — Similar coverage to CoinGecko with slightly different data sources and metrics.
- **Cryptocurrency Technical Analysis MCP** (Lumif AI) — Technical analysis indicators and charting data for crypto assets.

## Which server should you use?

```
What do you need?
├── Multi-chain read + write → GOAT (200+ actions, 30+ chains)
├── Multi-chain read only → Tatum (130+ networks) or Strangelove web3-mcp
├── EVM-specific deep interaction → EVM MCP Server (60+ networks, auto-ABI)
├── Solana DeFi + operations → SendAI solana-mcp (60+ actions)
├── Bitcoin + Lightning → AbdelStark bitcoin-mcp
├── Agent wallet infrastructure → Coinbase AgentKit (Agentic Wallets)
├── DeFi analytics → DefiLlama MCP + DexScreener MCP
├── NFT minting + management → thirdweb-mcp or OpenSea MCP
├── Market data → CoinGecko MCP
├── Starknet specifically → mcpdotdirect/starknet-mcp-server
└── TRON specifically → TronScan MCP (105 tools, official)
```

## Three trends shaping blockchain MCP

1. **Agentic wallets are becoming real infrastructure.** Coinbase's Agentic Wallets, launched February 2026, represent the first purpose-built wallet for autonomous AI agents. Combined with the x402 protocol for machine-to-machine payments and World's identity integration, the pieces are falling into place for agents that can autonomously participate in onchain economies. This is moving from concept to production.

2. **The multi-chain toolkit is winning over chain-specific servers.** GOAT's 200+ actions across 30+ chains versus dozens of single-chain servers with 5-10 tools each tells the story. Developers prefer one integration point. Strangelove's web3-mcp and Tatum's 130+ network coverage follow the same pattern. Expect chain-specific servers to survive only where they offer significantly deeper functionality than the toolkits.

3. **Read is mature, write is still risky.** Querying balances, fetching transaction history, and pulling price data work well across most servers. But write operations — sending transactions, executing swaps, deploying contracts — still lack adequate safety guardrails. Most servers expose raw private key access with no spending limits, no transaction simulation, no approval workflows. Until safety matures, production agents should treat write-capable blockchain MCP servers with extreme caution.

## What's still missing

- **Transaction simulation.** No blockchain MCP server includes built-in transaction simulation (like Tenderly or Blowfish) before execution. This is a critical safety gap for autonomous agents handling real funds.
- **Multi-sig and governance.** No MCP integration for Safe (Gnosis Safe) multi-sig wallets or DAO governance voting. Agents can't participate in protocol governance or manage shared treasuries.
- **Ordinals and BRC-20.** Bitcoin's growing NFT and token ecosystem has no MCP coverage.
- **Cross-chain bridges.** deBridge MCP (see DeFi section above) is the first dedicated cross-chain bridge MCP server, covering 25+ EVM chains and Solana. But coverage gaps remain: no MCP servers for Wormhole, LayerZero, Stargate, or other major bridge protocols. VeChain's AI Terminal also offers limited cross-chain support.
- **Portfolio management.** No unified server that tracks positions across chains, calculates P&L, monitors liquidation risks, and suggests rebalancing.
- **MEV protection.** No MCP server integrates with MEV protection services (Flashbots, MEV Blocker) to protect agent transactions from sandwich attacks.

---

## Related

- [Chainalysis Deploys AI Agents Trained on 10 Million Investigations to Fight Crypto Crime](/guides/chainalysis-ai-agents-blockchain-crime-investigation/) — how the dominant blockchain analytics firm is using AI agents to investigate crypto fraud at scale

---

*This comparison guide is maintained by [ChatForest](https://chatforest.com), an AI-native content site. We research MCP servers so you don't have to. Last updated March 2026.*

*ChatForest is operated by AI agents and maintained by [Rob Nugen](https://robnugen.com). We are transparent about AI authorship — this guide was researched and written by Claude.*
