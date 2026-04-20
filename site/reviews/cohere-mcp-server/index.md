# Cohere MCP Server — Enterprise AI's North Star Meets the Model Context Protocol

> Cohere has no standalone MCP server — instead, their North AI agent platform consumes MCP servers via built-in connectors and custom tool integration, with a North MCP Python SDK


**At a glance:** Cohere has **no official MCP server** wrapping its API. Instead, MCP integration lives inside [North](https://cohere.com/north), Cohere's enterprise AI agent platform, which can consume any MCP server as a custom tool. Cohere publishes [north-mcp-python-sdk](https://github.com/cohere-ai/north-mcp-python-sdk) (11 stars, MIT) for building authenticated MCP servers that work with North. Community servers are minimal: one community Cohere API wrapper exists but has been removed from GitHub. Part of our **[AI Providers MCP category](/categories/ai-providers/)**.

Cohere is the **enterprise-focused AI company** that built its reputation on retrieval-augmented generation (RAG) and multilingual models. Rather than publishing MCP servers or building broad MCP client support, Cohere channels MCP through North — a low-code enterprise agent platform where MCP is one of several tool integration options alongside built-in connectors.

[Cohere](https://cohere.com/) was founded in 2019 by **Aidan Gomez** (co-inventor of the Transformer architecture), **Ivan Zhang**, and **Nick Frosst** (ex-Google Brain). Headquartered in Toronto with offices in San Francisco, Palo Alto, London, and New York. As of early 2026: approximately **$240 million ARR** (surpassing $200M target per February 2026 investor memo), **$7 billion valuation** (September 2025 Series D second close), approximately **$1.54 billion total funding** across 7 rounds (investors include Radical Ventures, Inovia Capital, NVIDIA, AMD Ventures, PSP Investments, Salesforce Ventures), approximately **450–842 employees** (sources vary). Cohere is **not a member of the AAIF** at any tier.

**Architecture note:** Cohere's MCP strategy is the **most enterprise-locked** of any major AI provider. Where Google published 24+ official MCP servers and Anthropic created the protocol, Cohere treats MCP as a connector layer inside North — accessible to North enterprise customers but not to the broader developer ecosystem. There is no official Cohere API MCP server for use with Claude Desktop, Cursor, or other MCP clients.

## What It Does

### North as MCP Client

[North](https://cohere.com/north), Cohere's AI agent platform (GA August 2025), integrates with MCP servers as custom tools for enterprise agents:

| Connector Type | Services |
|---------------|----------|
| Built-in | Gmail, Slack, Salesforce, Outlook, Linear, SharePoint |
| Custom MCP | Any MCP server via StreamableHTTP transport |
| Agent coordination | Agent-to-agent workflows within North |

**Key capabilities:**
- Agents built in **Agent Studio** (low-code UI + API) can connect to any MCP server
- MCP is treated as one tool type alongside built-in connectors and custom functions
- Enterprise security: GDPR, SOC-2 Type II, ISO 27001, ISO 42001 compliant
- Deployment options: SaaS, VPC, on-premises, and air-gapped environments
- North uses **StreamableHTTP transport only** (SSE deprecated in their implementation)

### North MCP Python SDK

Cohere publishes an official SDK for building MCP servers that authenticate with North:

| Aspect | Detail |
|--------|--------|
| GitHub | [cohere-ai/north-mcp-python-sdk](https://github.com/cohere-ai/north-mcp-python-sdk) — 11 stars, 7 forks, 46 commits, 5 releases (latest v0.3.0), MIT |
| Language | Python 3.11+ |
| Created | May 2025 |
| Transport | StreamableHTTP only |
| Key features | Server secret protection, user OAuth token access, user identity from IdP, debug mode |
| Install | `uv pip install git+ssh://git@github.com/cohere-ai/north-mcp-python-sdk.git` |

This SDK extends the base MCP Python SDK with North-specific authentication. It is designed for **building MCP servers that integrate with North**, not for general-purpose use with other MCP clients.

### No Official Cohere API MCP Server

A search of the `cohere-ai` GitHub organization (57 public repos) finds **no MCP server wrapping the Cohere API**. The only MCP-related repos are the North MCP Python SDK and a fork of [mcp-atlassian](https://github.com/cohere-ai/mcp-atlassian) (for internal Confluence/Jira use). Developers who want to use Cohere models via MCP from Claude Desktop, Cursor, or other MCP clients have **no official path**.

## Community Servers

### Third-Party MCP Integrations

| Platform | What it does |
|----------|-------------|
| [Zapier Cohere AI MCP](https://zapier.com/mcp/cohere-ai) | Connect Cohere actions to any MCP-compatible tool via Zapier |
| [viaSocket MCP](https://viasocket.com/mcp/cohere-ai) | Cohere AI actions accessible via MCP through viaSocket |
| [Pipedream MCP](https://mcp.pipedream.com/app/cohere_platform) | Cohere platform actions as MCP server via Pipedream |

These are **platform-mediated wrappers** — they expose Cohere API actions through their respective automation platforms, not standalone MCP servers. No community-built standalone Cohere API MCP server with significant adoption exists on GitHub.

## Cohere Model Pricing

All API pricing per 1 million tokens:

### Command Models (Chat / Agents)

| Model | Parameters | Context | Max Output | Input | Output |
|-------|-----------|---------|------------|-------|--------|
| Command A | 111B | 256K | 8K | $2.50 | $10.00 |
| Command A Reasoning | N/A | 256K | 32K | $2.50 | $10.00 |
| Command A Vision | N/A | 128K | 8K | $2.50 | $10.00 |
| Command A Translate | N/A | 8K | 8K | $2.50 | $10.00 |
| Command R+ (08-2024) | N/A | 128K | 4K | $2.50 | $10.00 |
| Command R (08-2024) | N/A | 128K | 4K | $0.15 | $0.60 |
| Command R7B (12-2024) | 7B | 128K | 4K | $0.04 | $0.15 |

### Embed Models

| Model | Dimensions | Context | Price per 1M tokens |
|-------|-----------|---------|-------------------|
| Embed v4.0 | 256–1536 | 128K | Usage-based |
| Embed English v3.0 | 1024 | 512 | Usage-based |
| Embed Multilingual v3.0 | 1024 | 512 | Usage-based |

### Rerank Models

| Model | Context | Price per 1K searches |
|-------|---------|---------------------|
| Rerank v4.0 Pro | 32K | Usage-based |
| Rerank v4.0 Fast | 32K | Usage-based |
| Rerank v3.5 | 4K | Usage-based |

### Open Research Models

| Model | Parameters | Context | License | Price |
|-------|-----------|---------|---------|-------|
| Aya Expanse 32B | 32B | 128K | Apache 2.0 | Free (self-hosted) |
| Aya Vision 32B | 32B | 16K | Apache 2.0 | Free (self-hosted) |

**Key point:** Cohere's Command R7B at **$0.04/$0.15** per million tokens is competitive for lightweight tasks. Command A at $2.50/$10.00 is priced at the premium tier, comparable to GPT-4o and Claude Sonnet. The Aya research models are **Apache 2.0 open-weight** but are not Cohere's primary commercial offerings.

### North Platform Plans

| Plan | Price | Key Features |
|------|-------|-------------|
| North | Contact sales | Agent Studio, built-in connectors, MCP support, enterprise security |
| API | Pay-per-token | Direct model access, no North platform features |

North pricing is not public — enterprises must request a demo.

## AI Provider MCP Comparison

| Feature | Cohere | Anthropic | Google | OpenAI | Meta/Llama | Hugging Face | Mistral | AWS Bedrock |
|---------|--------|-----------|--------|--------|------------|-------------|---------|-------------|
| Official MCP server | No | No (reference servers) | Yes (3.4k stars) | No | No | Yes (210 stars) | No | Yes (8.5k stars, 68 servers) |
| Server approach | North-only client | Reference implementations | Managed + open-source | Client only | Client only (Llama Stack) | Hub access + Gradio | Client only | monorepo (68 servers) |
| MCP client | Yes (North only) | Yes (all Claude products) | Yes (Gemini CLI, SDKs) | Yes (ChatGPT, Agents SDK) | Yes (Llama Stack) | No | Yes (Le Chat, Agents API) | Yes (Q Developer, AgentCore) |
| AAIF member | No | Yes (Platinum, co-founder) | Yes (Platinum) | Yes (Platinum, co-founder) | No | No | Yes (Silver) | Yes (Platinum) |
| Unique strength | Enterprise RAG + sovereignty | Created the protocol | Most official servers (24+) | 900M+ weekly users | Fully free models | 1M+ models, Gradio-as-MCP | Open-weight + EU sovereignty | 68 official servers |
| Open-weight models | Some (Aya, Apache 2.0) | No | Some (Gemma) | No | Yes (Llama license) | Platform (hosts all) | Yes (Apache 2.0, 3B-675B) | No (hosts others) |
| Free tier | No (API is pay-per-use) | Yes (limited Claude) | Yes (Flash models) | Yes (limited ChatGPT) | Yes (all models free) | Yes (full Hub access) | Yes (Le Chat Free) | No (cloud billing required) |

## Known Issues

1. **No official Cohere API MCP server** — Developers who want to use Cohere models (Command A, Command R+, Command R7B) as MCP tools from Claude Desktop, Cursor, or Windsurf have no official server. No community wrapper has gained traction either.

2. **MCP locked inside North** — MCP integration is only available through North, Cohere's enterprise platform. There's no MCP support in the raw Cohere API, Python SDK (`cohere-python`), or any standalone developer tool. This limits MCP access to North enterprise customers.

3. **Not an AAIF member** — Cohere is absent from the Agentic AI Foundation at every tier (Platinum, Gold, Silver). This means zero influence over MCP protocol governance as the standard evolves under the Linux Foundation.

4. **North MCP SDK has minimal adoption** — The north-mcp-python-sdk has 11 stars and 7 forks. Compare this to Anthropic's MCP Python SDK (22.3k stars) or TypeScript SDK (11.9k stars). The SDK is North-specific, limiting its appeal to the broader MCP developer community.

5. **Enterprise sales process blocks access** — North requires a sales conversation; there's no self-serve plan. Developers who want to experiment with Cohere's MCP integration cannot do so without enterprise engagement.

6. **StreamableHTTP only** — North's MCP implementation only supports StreamableHTTP transport. SSE is deprecated in their implementation, and stdio is not supported. This limits compatibility with MCP servers that only offer stdio transport.

7. **No free tier** — Cohere offers no free API tier (unlike OpenAI, Google, Mistral, and Meta). The cheapest option is Command R7B at $0.04/M input tokens via the API, but this doesn't include North or MCP features.

8. **Cohere Toolkit ecosystem is small** — The cohere-toolkit (3.2k stars) is the most popular open-source project but has no MCP integration. The overall GitHub ecosystem is modest compared to competitors.

9. **Aya open-weight models lag behind** — While Cohere publishes Aya Expanse 32B and Aya Vision 32B under Apache 2.0, these are research-grade 32B models — not competitive with Mistral's 675B open-weight frontier model or Meta's Llama 4 Scout/Maverick.

10. **Revenue and scale gap** — At $240M ARR, Cohere is significantly smaller than Anthropic (~$19B annualized), Google ($402B revenue), AWS ($128B), or even Mistral (EUR 300M ARR). This affects long-term investment capacity in MCP ecosystem development.

## Bottom Line

**Rating: 2.5 out of 5**

Cohere brings a **strong enterprise AI platform** but the **weakest MCP ecosystem** of any major AI provider we've reviewed. North's ability to consume MCP servers is useful for enterprises already on the platform, and the North MCP Python SDK provides a path for building authenticated MCP servers. But that's where it ends.

The fundamental issue is **MCP is locked inside North's enterprise walls**. There is no Cohere API MCP server, no MCP support in the standard Python/TypeScript SDKs, no free tier to experiment with, and no AAIF membership to influence the protocol's direction. A developer who wants to wire Cohere models into the broader MCP ecosystem — using them from Claude Desktop, Cursor, or any other MCP client — has no official path.

Cohere's **enterprise positioning** makes this somewhat intentional. They're building for Fortune 500 companies that want private, sovereign AI deployments with agent capabilities — not for individual developers exploring MCP tooling. North's built-in connectors (Gmail, Slack, Salesforce, Outlook, Linear, SharePoint) plus custom MCP support serve that enterprise audience.

The **2.5/5 rating** reflects Cohere's strong models and enterprise platform offset by the thinnest MCP ecosystem we've reviewed: no official API server, North-only MCP access, 11-star SDK, no AAIF membership, no free tier, and no community adoption. Every other AI provider in our series — even those without official MCP servers — offers broader MCP accessibility.

**Who benefits most from Cohere's MCP ecosystem:**

- **North enterprise customers** — if you're already on North, MCP integration provides a clean way to connect agents to external tools and data sources
- **Enterprise developers building for North** — the North MCP Python SDK offers authenticated server development with OAuth and identity provider integration
- **Organizations needing sovereign AI** — Cohere's VPC and air-gapped deployment options with MCP tool connectivity serve regulated industries

**Who should be cautious:**

- **Individual developers** — there's no way to use Cohere models as MCP tools from standard MCP clients; North requires enterprise sales engagement
- **MCP ecosystem builders** — Cohere's MCP investment is entirely North-locked; building for Cohere's MCP means building for North's specific implementation
- **Anyone expecting open MCP participation** — without AAIF membership, Cohere has no seat at the table shaping MCP's future as an open standard

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official Cohere announcements. Information is current as of March 2026. See our [About page](/about/) for details on our review process.*

