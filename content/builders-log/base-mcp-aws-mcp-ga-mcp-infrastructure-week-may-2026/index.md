---
title: "MCP Goes Infrastructure: Base Brings Agents Onchain, AWS Opens the Full Cloud API"
date: 2026-05-28
description: "Two launches last week redefined what MCP is for. Base MCP lets any Claude or ChatGPT session execute DeFi transactions via a non-custodial smart wallet. AWS MCP Server hit GA with 15,000+ API operations and full IAM governance. Here's what builders can do with both."
tags: ["mcp", "coinbase", "aws", "defi", "web3", "infrastructure", "ai-agents", "blockchain", "cloud"]
---

## The Week MCP Stopped Being a Dev Tool

For most of 2025, the Model Context Protocol was a developer convenience — a cleaner way to connect Claude or Cursor to your database, your GitHub repo, your local filesystem. Powerful, but still in the "workflow accelerator" category.

Last week changed the framing.

On May 26, Coinbase's Base network launched Base MCP, enabling any MCP-compatible AI client to send ETH, swap tokens, and execute DeFi positions onchain — with a non-custodial smart wallet and human review before anything touches the blockchain.

A few weeks earlier, on May 6, Amazon Web Services promoted its MCP server to general availability, giving AI agents standardized access to all 15,000+ AWS API operations with IAM-based governance and CloudTrail audit logging.

These are not incremental developer conveniences. One connects AI agents to global financial rails. The other connects them to the world's largest cloud platform with enterprise-grade access controls. Both chose MCP as the interface standard. That choice matters.

---

## Base MCP: AI Agents Go Onchain

Base is the Ethereum Layer-2 network incubated by Coinbase — fast, low-fee, and one of the most actively developed L2s. On May 26, it launched an MCP server that connects Base smart wallets to any MCP-compatible AI client: Claude, ChatGPT, Cursor, Codex.

**What it can do:**

- Send native ETH
- Transfer ERC-20 tokens
- Batch smart contract calls into a single transaction
- Swap tokens via Uniswap
- Lend or borrow via Morpho and Moonwell
- Trade perpetuals via Avantis
- Send micropayments via the x402 protocol using USDC

These are not simulated actions. They are real blockchain transactions.

**How the security model works:**

This is the part worth slowing down on. Base MCP is non-custodial, meaning the MCP server never touches private keys. The flow is:

1. You instruct an AI client in natural language: "swap 0.1 ETH for USDC"
2. The AI constructs a transaction intent and sends it to Base MCP
3. Base MCP creates a pending request stored in the user's Base Account
4. You review the pending request in the Base App on your device
5. You sign and broadcast — or reject

The AI cannot execute anything autonomously. Every transaction requires human review and explicit sign-off before it reaches the chain. This architecture makes Base MCP safer than it sounds from the headline, and sets a model for how AI-initiated financial transactions should be structured while fully autonomous agents are still being debated.

---

## The x402 Angle: Agent Pays Agent

The micropayments capability is the most underreported detail in the launch coverage.

Base MCP implements the x402 protocol, a payment standard co-developed by Coinbase and Cloudflare that enables HTTP-native payments using USDC on Base. The core idea: an AI agent making an HTTP request can include payment automatically as part of the request, without separate payment flows or human approval for each small transaction.

In practice, this means:

- An AI agent can pay an API for data it retrieves, per call, in real time
- One agent can pay another agent for compute or services, denominated in USDC
- Payment and request become the same round-trip

This is the "agent economy" pattern that has been discussed theoretically for two years. Base MCP is one of the first production deployments where the plumbing actually exists.

For builders thinking about monetizing agents or building agent-native services, x402 + Base MCP is the closest thing to a live standard right now.

---

## AWS MCP Server GA: The Full Cloud API, Agent-Accessible

On May 6, AWS promoted its MCP server from preview (first shown at re:Invent 2025) to general availability. The scope expansion is significant: preview covered a subset of services; GA covers everything.

**API coverage:** The `call_aws` tool can invoke any of AWS's 15,000+ API operations — including long-running async jobs and file upload operations. If your IAM credentials can do it, the agent can do it.

**The three core tools agents get:**

- `call_aws` — execute any AWS API operation with the agent's existing IAM credentials
- `search_documentation` and `read_documentation` — retrieve current AWS documentation at query time, so agents work from up-to-date API signatures rather than training-data knowledge

- Sandboxed Python execution — agents can write and run multi-step Python scripts against AWS services, isolated from the local filesystem and shell

The documentation retrieval tool is underrated. AI agents hallucinate AWS API parameters because their training data contains outdated documentation. AWS MCP fetches current docs at inference time, meaning the agent constructs API calls from what the API actually looks like today, not what it looked like in 2024.

**IAM governance: why enterprises care**

The AWS MCP server does not introduce a new permission system. It uses standard IAM policies and Service Control Policies — the same governance model your infrastructure team already manages.

This means:
- Read-only agents are trivially configured: standard IAM boundary policies apply
- Audit trails are automatic: CloudTrail logs every API call the agent makes, with timing, parameters, and outcome
- CloudWatch metrics surface agent activity in your existing dashboards
- No separate MCP-specific permission layer to learn, audit, or explain to security teams

For teams building AI-driven infrastructure automation — and especially for anyone operating in regulated industries — this is the first cloud AI agent interface that doesn't require a new security conversation with your compliance team.

**Current availability:** US East (Northern Virginia) and EU (Frankfurt). No additional charge for the MCP server; you pay for the underlying AWS operations the agent uses.

---

## Five Builder Implications

**1. MCP is becoming the default integration layer for non-LLM systems.**
Both Base and AWS are large, complex platforms with established API surfaces. Both chose MCP over a proprietary agent SDK. This is further evidence — alongside Google's MCP support and the Atlassian Teamwork Graph integration — that the 97M monthly SDK download figure is driving adoption outside the pure AI-tools space. If you're building agent integrations, MCP compatibility is becoming table stakes.

**2. The non-custodial agent wallet pattern is the one to study.**
Base MCP's security model — AI constructs intent, human reviews and signs — is the right architecture for AI-initiated financial actions during the current regulatory moment. Fully autonomous agent transactions face unresolved legal and custodial questions in most jurisdictions. The "pending request + human sign-off" pattern lets you ship now without betting on regulatory outcomes.

**3. x402 is worth a prototype.**
The agent-pays-agent micropayment pattern enabled by x402 and Base MCP has been waiting for a production implementation. If you're building an API-native service that agents might call — data feeds, compute, verification services — testing USDC micropayments on Base is now feasible without writing wallet infrastructure from scratch.

**4. AWS MCP changes the case for AI infrastructure agents.**
Before GA, building an AI agent that manages AWS resources required either: writing bespoke AWS SDK calls into a custom tool layer, or accepting hallucinated API parameters. AWS MCP GA closes both gaps. Teams running CloudOps, cost optimization, or infrastructure provisioning workflows now have a sanctioned, audited interface that doesn't require custom integration work.

**5. The sandboxed Python execution in AWS MCP is a sleeper feature.**
The ability for an agent to write and execute multi-step Python code against AWS APIs — inside a sandbox, without shell access — enables reasoning patterns that single API calls can't support. An agent can retrieve data from S3, transform it with Pandas, call an API, evaluate the result, and act conditionally — all within one reasoning turn. This moves AWS MCP closer to a general-purpose cloud operations agent rather than a wrapper around the CLI.

---

## The Broader Pattern

In the first 18 months of MCP's existence, adoption was concentrated in developer tooling: file systems, code repositories, databases, productivity apps. The infrastructure that builders use to build.

What's changed is the category of system connecting to MCP. Coinbase Base is a global financial settlement layer. AWS is the compute backbone for roughly a third of the internet. These systems are not attaching to MCP because their developers like the protocol. They are attaching because the agent use cases — autonomous portfolio management, AI-driven cloud operations — have enough demand that not supporting MCP means losing developer relevance.

The protocol is crossing from "developer convenience" to "infrastructure standard." The next question is which regulated industries — financial services, healthcare, government — attach next, and what the compliance story looks like when they do.

---

*Chatforest covers AI infrastructure, model releases, and builder tooling. This article is based on public launch announcements, documentation, and coverage from CoinDesk, The Block, InfoQ, Fortune, and the AWS blog. We research rather than hands-on test the tools we cover.*
