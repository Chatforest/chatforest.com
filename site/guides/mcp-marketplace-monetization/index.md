# MCP Server Marketplace & Monetization: How to Publish, Distribute, and Earn from MCP Servers

> A comprehensive guide to MCP server marketplaces, monetization platforms, pricing strategies, and publishing workflows — covering mcp.so, Glama, Smithery, MCPize, Apify, Agent


MCP SDK downloads have reached approximately 97 million per month. Over 11,000 to 17,000+ MCP servers now exist across various registries and directories. Yet according to published reports, fewer than 5% of those servers are monetized in any way. The MCP economy is emerging fast, and the window for early movers is wide open.

This is a research-based guide. We do not claim to have tested, tried, or used any of the platforms described here hands-on. All information is drawn from published documentation, public announcements, community reports, and developer accounts. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

For related context, see our guides on [MCP Registry & Server Discovery](/guides/mcp-registry-server-discovery/), [MCP Authorization & OAuth](/guides/mcp-authorization-oauth/), [MCP Server Security](/guides/mcp-server-security/), [MCP in Production](/guides/mcp-in-production/), [MCP Server Deployment & Hosting](/guides/mcp-server-deployment-hosting/), and [MCP Server Frameworks & SDKs](/guides/mcp-server-frameworks-sdks/).

---

## 1. The Emerging MCP Economy

The numbers paint a clear picture of an ecosystem in rapid expansion:

- **~97 million monthly SDK downloads** with reported 85%+ month-over-month growth
- **11,000–17,000+ MCP servers** listed across various registries and directories
- **Less than 5% monetized** — the vast majority of servers remain free and open source
- **Early revenue signals**: according to published accounts, 21st.dev reportedly hit $10K monthly recurring revenue (MRR) within 6 weeks of launch, with zero marketing spend, using a freemium model (5 free requests, then paid)

This pattern has historical parallels. The early iOS App Store (2008–2010), WordPress plugin ecosystem, and Shopify app marketplace all went through a similar arc: explosive growth in free offerings, followed by a monetization wave as developers discovered demand and platforms built payment infrastructure. MCP appears to be at the inflection point between those two phases.

The opportunity is particularly notable because MCP servers solve concrete automation problems for developers and businesses — they are not speculative or entertainment-focused. Tools that save time and reduce friction tend to monetize well once distribution channels mature.

---

## 2. Discovery Platforms (Free Registries and Directories)

Before monetizing an MCP server, it needs to be discoverable. Several free registries and directories have emerged, each with different strengths. Based on publicly available data:

| Platform | Servers Listed | Key Strength | Notable Feature |
|----------|---------------|--------------|-----------------|
| **mcp.so** | 17,186+ | Largest catalog | Built-in playground for testing servers |
| **Glama** | 12,610+ | Quality focus | Automated security scans, 100+ categories |
| **Smithery** | 7,300+ tools | Developer workflow | CLI install/publish, hosted deployment, analytics |
| **PulseMCP** | 7,600+ | Popularity signals | Official vs. community tags, trending data |
| **Cline MCP Marketplace** | Varies | Distribution reach | GitHub-based submission, reaches millions of Cline users |
| **LobeHub** | Growing | Integrated UX | MCP server marketplace built into the LobeHub platform |

### mcp.so

According to its documentation, mcp.so is the largest MCP server catalog with over 17,186 servers indexed. It provides a playground feature that reportedly allows visitors to test server capabilities directly in the browser. Servers are organized by category and include metadata like GitHub stars, installation instructions, and compatibility information.

### Glama

Glama lists over 12,610 servers across more than 100 categories. Based on published documentation, it differentiates through quality-focused curation, running automated security scans on listed servers. This makes it particularly relevant for enterprise developers who need some assurance about the servers they adopt.

### Smithery

Smithery reports over 7,300 tools and emphasizes the developer workflow. It offers CLI-based publishing (`smithery mcp publish`), hosted deployment options, and analytics dashboards that show how servers are being used. For developers considering monetization, Smithery's analytics can help identify which servers have enough traction to justify paid tiers.

### PulseMCP

PulseMCP lists over 7,600 servers and stands out for its popularity signals — it tags servers as "official" or "community" and surfaces trending data. This can help developers understand which niches are underserved and where demand exists.

### Cline MCP Marketplace

The Cline marketplace uses a GitHub-based submission process where developers open an issue with their repository URL and a 400x400 PNG logo. According to published criteria, submissions are reviewed for community adoption, security practices, and overall quality. Acceptance provides access to millions of Cline users — a significant distribution channel.

### LobeHub

LobeHub integrates an MCP server marketplace directly into its platform, providing another discovery surface for server developers. Based on documentation, it is a growing marketplace that benefits from LobeHub's existing user base.

For a deeper look at the official MCP Registry and how programmatic discovery works, see our [MCP Registry & Server Discovery guide](/guides/mcp-registry-server-discovery/).

---

## 3. Monetization Platforms (Paid Distribution)

A growing set of platforms now handle the hard parts of monetization — billing, hosting, access control, and payouts — so developers can focus on building servers.

### MCPize

According to published documentation, MCPize offers an **85% revenue share** to developers (15% platform fee). The platform reportedly handles hosting, SSL, payment processing, and distribution. Key features based on documentation:

- Stripe-based payouts
- MRR tracking dashboard
- 1,000+ servers listed
- Python and TypeScript SDKs for integration
- Developers set their own pricing

MCPize appears designed as a turnkey monetization layer: wrap an existing MCP server with their SDK, deploy via CLI, set a price, and the platform handles the rest.

### Apify

Apify reports over 36,000 active developers and 130,000+ monthly signups on its platform. Based on documentation, it uses a **pay-per-event model** built around its `Actor.charge()` API — developers define billable events (a scrape completed, data returned, etc.) and Apify handles metering and billing.

Notable aspects based on published reports:

- Partner distribution through Make, n8n, Zapier, and Gumloop integrations
- Template-based development workflow
- At least one developer has publicly reported earning $2,000+/month through the platform
- MCP servers can be published as Apify Actors

### dotMCP

dotMCP, based on its documentation, focuses on converting existing APIs into MCP servers. It reportedly supports importing from OpenAPI specs, GraphQL schemas, and Postman collections, with auto-generation of MCP server wrappers. Features described in documentation include:

- Server tunneling for self-hosted servers
- Visual builder for non-developers
- Distribution to Claude and Cursor clients
- API import from multiple formats

This approach targets developers who already have APIs and want to reach the MCP ecosystem without rewriting their server logic.

### Agent Bazaar

Agent Bazaar describes itself as building an **open billing standard** for MCP. Based on published specifications, it offers:

- **Per-call metering** with sub-cent (microcent) precision
- **HMAC-SHA256 signed receipts** for cryptographic billing verification
- **Trust scores** for servers and clients
- **82% revenue share** (18% platform fee)

The open billing standard is particularly notable — if adopted broadly, it could reduce the fragmentation that currently exists across monetization platforms. Developers would implement one billing interface and reach multiple marketplaces.

### Nevermined

Nevermined provides **payment infrastructure** rather than a full marketplace. According to documentation, it supports multiple payment protocols:

- **x402** — HTTP-native payment protocol
- **A2A** (Agent-to-Agent) payments
- **AP2** protocol support
- **Fiat payments** via Stripe (USDC, USDT, ETH also supported)
- **Cryptographic verification** of payment transactions

A published case study reports that Valory reduced billing deployment time from 6 weeks to 6 hours using Nevermined's infrastructure. This platform targets developers who want payment capabilities without a specific marketplace — useful for self-distributed servers or multi-platform strategies.

---

## 4. DIY Monetization (Self-Hosted Billing)

Not every developer wants to use a platform. For those who prefer full control, several approaches exist.

### Moesif

According to its documentation, Moesif provides **usage analytics and billing specifically designed for MCP servers**. It meters JSON-RPC requests at the protocol level and integrates with billing providers. Key capabilities based on documentation:

- Meters individual MCP tool calls and JSON-RPC requests
- Integrates with Stripe, Chargebee, and Zuora for billing
- Supports multiple pricing models: per-call, hybrid (subscription + overages), and outcome-based
- Provides usage analytics dashboards

### OAuth 2.1 + API Keys

For access control, the MCP specification supports OAuth 2.1 authorization flows. Developers can gate access to their servers using standard OAuth patterns, issuing API keys or tokens tied to billing tiers. See our [MCP Authorization & OAuth guide](/guides/mcp-authorization-oauth/) for implementation details.

### Rate Limiting Per Tier

A common DIY pattern involves implementing rate limiting that varies by tier:

- **Free tier**: 10–50 requests/day
- **Basic tier**: 1,000 requests/day
- **Pro tier**: 10,000+ requests/day or unlimited

Rate limits can be enforced at the server level using standard middleware, with tier information derived from the OAuth token or API key.

### Build Your Own with Stripe Metered Billing

For full control, developers can integrate Stripe's metered billing directly:

1. Create Stripe products and prices with metered billing
2. Track usage per API key in your MCP server
3. Report usage to Stripe at regular intervals
4. Stripe handles invoicing and collection

This approach offers maximum flexibility but requires more development work. It makes sense for servers with complex pricing models or those distributed across multiple channels.

For security considerations when implementing billing and access control, see our [MCP Server Security guide](/guides/mcp-server-security/).

---

## 5. Business Models Comparison

Based on documented examples and published reports from the MCP ecosystem:

| Model | Best For | Example | Pros | Cons |
|-------|----------|---------|------|------|
| **Freemium** | Broad-appeal tools, developer adoption | 21st.dev (5 free reqs, ~6% conversion reported) | Organic discovery, low friction, viral growth | Most users never pay; need volume |
| **Per-Call / Usage-Based** | Commodity functions, variable-cost operations | Apify `Actor.charge()` | Fair to users, scales with value | Revenue unpredictable; hard to forecast |
| **Subscription / Tiered** | Consistent-use tools, enterprise users | Monthly plans with request limits | Predictable revenue, simpler billing | May overshoot or undershoot value |
| **Outcome-Based** | High-value results (lead gen, data enrichment) | Charge only on successful results | Aligns incentives perfectly | Complex to define "success"; disputes |
| **Credit-Based** | Multi-tool platforms, variable operations | Prepaid credits consumed per call | Upfront revenue, flexible allocation | Users may feel "nickel-and-dimed" |
| **Hybrid** | Mature products, enterprise customers | Base subscription + usage overages | Predictable base + usage upside | Complex pricing; harder to communicate |

### Key Observations from Published Data

- **Freemium with low free tiers** appears to be the most successful early monetization pattern. The reported ~6% conversion rate at 21st.dev (with only 5 free requests) suggests that developers are willing to pay when the tool delivers clear value quickly.
- **Per-call pricing** works well on platforms like Apify where the cost of each operation is variable and the value is easily attributable to a single call.
- **Subscription models** are more common for tools used daily or integrated into workflows, where predictable billing matters more than precise usage alignment.
- **Outcome-based pricing** is the highest-margin model but requires careful definition of what constitutes a successful outcome and robust tracking to verify it.

---

## 6. Publishing Your First MCP Server

Here is a practical walkthrough for getting an MCP server listed on major platforms, based on their published documentation.

### Smithery

According to Smithery's documentation, the publishing workflow is:

```
smithery mcp publish "https://your-server-url" -n your-org/your-server-name
```

The CLI handles registration, metadata collection, and deployment. Smithery reportedly also supports hosted deployment, where the platform runs the server on your behalf.

### Cline MCP Marketplace

Based on published submission guidelines:

1. Open a GitHub issue on the Cline MCP Marketplace repository
2. Include your repository URL
3. Include a 400x400 PNG logo
4. The review process evaluates: community adoption, security practices, code quality, and overall usefulness
5. Accepted servers appear in the Cline marketplace, reaching its user base

**Tip**: According to community reports, including an `llms-install.md` file in your repository improves the chances of acceptance and makes installation smoother for Cline users.

### MCPize

Based on MCPize documentation, the workflow is:

1. Install the MCPize SDK (Python or TypeScript)
2. Wrap your MCP server with MCPize's billing middleware
3. Deploy via CLI
4. Set pricing in the MCPize dashboard
5. The platform handles hosting, SSL, billing, and payouts

### Apify

According to Apify's documentation:

1. Start from an Apify Actor template
2. Implement your MCP server logic
3. Add billing events using `Actor.charge()` for billable operations
4. Publish to the Apify Store
5. The platform handles distribution, billing, and partner integrations

### Best Practices for Publishing

Based on documentation and community discussions across platforms:

- **README quality matters**: A clear, well-structured README with usage examples significantly improves adoption. Document every tool, resource, and prompt your server exposes.
- **Include `llms-install.md`**: This file helps AI coding assistants guide users through installation. It is specifically recommended for Cline marketplace submissions.
- **Use a valid open-source license**: Most registries require or strongly prefer servers with a recognized license (MIT, Apache 2.0, etc.).
- **Security review**: Before publishing, review your server for common vulnerabilities. See our [MCP Server Security guide](/guides/mcp-server-security/) for a checklist.
- **Test across clients**: Based on community reports, servers that work reliably across Claude Desktop, Cursor, and other MCP clients get better reviews and adoption.
- **Include a server card**: The official MCP Registry uses server cards for metadata. Including one makes your server compatible with programmatic discovery. See our [MCP Registry & Server Discovery guide](/guides/mcp-registry-server-discovery/) for the format.

---

## 7. Pricing Strategy

Setting the right price for an MCP server is as much art as science. Based on patterns observed across the ecosystem and published developer accounts:

### Research the Market First

Before setting a price, look at what comparable servers charge. Check the monetization platforms listed in this guide — many show pricing publicly. If your server does something similar to an existing paid server, that gives you a baseline.

### Price on Value, Not Time

A server that saves a developer 2 hours per day is worth far more than the hours it took to build. Focus on the problem being solved and the value of the outcome, not the cost of development.

### Start with a Generous Free Tier

Based on published patterns, a generous free tier drives organic discovery. The key is making the free tier useful enough to demonstrate value but limited enough to create upgrade pressure:

- **Too generous**: Users never hit the limit, no conversion
- **Too stingy**: Users cannot evaluate the server, no adoption
- **Right-sized**: Users experience the value, hit the limit during real work, and convert

The reported 5-free-requests model at 21st.dev is aggressive but reportedly effective — it forces quick evaluation and decision.

### Consider Outcome-Based Pricing for High-Value Tools

If your server produces high-value results (lead enrichment, code generation, data transformation), consider charging per successful outcome rather than per call. This aligns your revenue with the value you deliver and reduces friction for users.

### Use Analytics Before Setting Prices

If your server is already free and has users, instrument it with analytics before introducing pricing. Understanding usage patterns — which tools are called most, how often, by how many unique users — informs pricing decisions. Smithery and Moesif both reportedly offer analytics for this purpose.

### A/B Test When Possible

Some platforms reportedly support A/B testing different price points. If available, this is the most reliable way to find the optimal price. Even without platform support, you can test by adjusting prices over time and measuring conversion and churn.

---

## 8. Ecosystem Table

A consolidated view of the MCP marketplace and monetization ecosystem, based on published documentation:

| Platform | Type | Servers Listed | Revenue Share | Key Feature | URL |
|----------|------|---------------|---------------|-------------|-----|
| **mcp.so** | Discovery | 17,186+ | N/A (free) | Largest catalog, playground | mcp.so |
| **Glama** | Discovery | 12,610+ | N/A (free) | Automated security scans | glama.ai |
| **PulseMCP** | Discovery | 7,600+ | N/A (free) | Popularity signals, trending | pulsemcp.com |
| **Smithery** | Discovery + Hosting | 7,300+ | N/A (free) | CLI publish, hosted deployment | smithery.ai |
| **Cline Marketplace** | Discovery | Varies | N/A (free) | Access to Cline user base | GitHub-based |
| **LobeHub** | Discovery | Growing | N/A (free) | Integrated platform | lobehub.com |
| **MCPize** | Monetization | 1,000+ | 85% developer | Turnkey billing + hosting | mcpize.com |
| **Apify** | Monetization | Part of 36K+ actors | Pay-per-event | Partner distribution (Make, n8n, Zapier) | apify.com |
| **dotMCP** | Monetization | Growing | Varies | API import, auto-generation | dotmcp.com |
| **Agent Bazaar** | Monetization | Growing | 82% developer | Open billing standard, microcent metering | agentbazaar.ai |
| **Nevermined** | Payment Infra | N/A (infra layer) | Varies | x402, crypto + fiat, cryptographic verification | nevermined.io |
| **Moesif** | DIY Billing | N/A (analytics layer) | N/A | JSON-RPC metering, Stripe/Chargebee integration | moesif.com |

---

## 9. What's Next for the MCP Economy

Based on published roadmaps, community discussions, and observable trends:

### Open Billing Standards

Agent Bazaar's open billing specification is an early attempt to standardize how MCP servers charge for their services. If a standard billing protocol gains adoption — similar to how OAuth standardized authorization — it would significantly reduce the integration burden for developers and allow servers to be monetized across multiple marketplaces simultaneously. This is likely the single most important development to watch.

### Enterprise Features in MCP 2026

The MCP specification continues to evolve, and enterprise-oriented features (better authentication, audit logging, tenant isolation) create the foundation for higher-value monetization. Enterprise customers pay more and churn less, but they require features that many current servers lack. See our [MCP in Production guide](/guides/mcp-in-production/) for current enterprise patterns.

### Crypto and Micropayment Rails

Nevermined's support for x402 (HTTP-native payments), USDC/USDT, and cryptographic verification represents an emerging pattern. Micropayments have historically failed in consumer contexts but may work for machine-to-machine transactions where the friction of traditional payment rails is a real barrier. Agent-to-agent payments — where one AI agent pays another for services — are a particularly interesting frontier.

### Consolidation and Maturity

The current landscape has many small players across discovery and monetization. Historical patterns from app stores and SaaS marketplaces suggest eventual consolidation, where a few dominant platforms capture most of the market. Developers who establish presence across multiple platforms now position themselves well regardless of which platforms emerge as winners.

### From Free to Paid

As the ecosystem matures, the percentage of monetized servers will grow. Developers who build free servers today with usage analytics instrumented from the start will be best positioned to introduce pricing when the time is right. The data from free usage — which tools are most valuable, how often they are used, who the power users are — is the foundation for effective monetization.

---

## Summary

The MCP server marketplace is in its early innings. Discovery platforms are maturing, monetization infrastructure is emerging, and business model patterns are becoming clearer. For developers considering building commercial MCP servers, the key takeaways based on published data:

1. **List everywhere**: Register on multiple discovery platforms (mcp.so, Glama, Smithery, PulseMCP) to maximize visibility.
2. **Start free, add analytics**: Launch free, instrument usage, and let data guide monetization decisions.
3. **Choose your monetization path**: Platform-managed (MCPize, Apify) for simplicity, or DIY (Moesif + Stripe) for control.
4. **Price on value**: The most successful MCP monetization examples focus on the value delivered, not the cost of infrastructure.
5. **Watch the standards**: Open billing standards and payment protocols will shape which platforms win.

For deployment and hosting considerations, see our [MCP Server Deployment & Hosting guide](/guides/mcp-server-deployment-hosting/). For framework selection, see our [MCP Server Frameworks & SDKs guide](/guides/mcp-server-frameworks-sdks/).

