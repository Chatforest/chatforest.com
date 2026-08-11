# MCP Server Marketplace & Monetization: How to Publish, Distribute, and Earn from MCP Servers

> A comprehensive guide to MCP server marketplaces, monetization platforms, pricing strategies, and publishing workflows — covering mcp.so, Glama, Smithery, MCPize, Apify, and Agent Bazaar.


MCP SDK downloads [reached approximately 97 million per month](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation), combined across the Python and TypeScript SDKs, according to Anthropic's own count. MCP servers now number in the tens of thousands across the major registries and directories — the leading catalogs range from roughly 14,000 to over 70,000 listings depending on how each one counts (see the per-registry figures in Section 2). Most of those servers remain free and open source. The MCP economy is emerging fast, and the window for early movers is wide open.

This is a research-based guide. We do not claim to have tested, tried, or used any of the platforms described here hands-on. All information is drawn from published documentation, public announcements, community reports, and developer accounts. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

For related context, see our guides on [MCP Registry & Server Discovery](/guides/mcp-registry-server-discovery/), [MCP Authorization & OAuth](/guides/mcp-authorization-oauth/), [MCP Server Security](/guides/mcp-server-security/), [MCP in Production](/guides/mcp-in-production/), [MCP Server Deployment & Hosting](/guides/mcp-server-deployment-hosting/), and [MCP Server Frameworks & SDKs](/guides/mcp-server-frameworks-sdks/).

---

## 1. The Emerging MCP Economy

The numbers paint a clear picture of an ecosystem in rapid expansion:

- [**~97 million monthly SDK downloads**](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) — the Python and TypeScript SDKs combined, per Anthropic
- **Tens of thousands of MCP servers** listed across registries — for example, [Glama indexes 71,000+](https://glama.ai/mcp/servers) and [PulseMCP tracks 22,000+](https://www.pulsemcp.com/servers) as of August 2026 (registries use different counting methods; see Section 2 for the full breakdown)
- **Most servers remain free and open source** — no registry publishes a reliable, sourced figure for what share is monetized, so we don't cite one here
- **Early revenue signals**: on Apify — one of the paid-distribution platforms covered below — [developer payouts have reportedly reached $1.4 million in a single recent month](https://apify.com/mcp/developers), evidence that real money is already moving through MCP-adjacent monetization platforms

This pattern has historical parallels. The early iOS App Store (2008–2010), WordPress plugin ecosystem, and Shopify app marketplace all went through a similar arc: explosive growth in free offerings, followed by a monetization wave as developers discovered demand and platforms built payment infrastructure. MCP appears to be at the inflection point between those two phases.

The opportunity is particularly notable because MCP servers solve concrete automation problems for developers and businesses — they are not speculative or entertainment-focused. Tools that save time and reduce friction tend to monetize well once distribution channels mature.

---

## 2. Discovery Platforms (Free Registries and Directories)

Before monetizing an MCP server, it needs to be discoverable. Several free registries and directories have emerged, each with different strengths. Based on publicly available data:

| Platform | Servers Listed | Key Strength | Notable Feature |
|----------|---------------|--------------|-----------------|
| **[mcp.so](https://mcp.so)** | Large catalog (site does not publish a stable count we could verify) | Broad catalog | [Built-in playground](https://mcp.so/playground) for testing servers |
| **[Glama](https://glama.ai/mcp/servers)** | 71,000+ | Quality focus | [Automated security scans](https://glama.ai/mcp/servers), [85 categories](https://glama.ai/mcp/categories) |
| **[Smithery](https://smithery.ai)** | 14,240+ tools | Developer workflow | CLI install/publish, hosted deployment, observability |
| **[PulseMCP](https://www.pulsemcp.com/servers)** | 22,000+ | Popularity signals | Official vs. community tags, trending data |
| **[Cline MCP Marketplace](https://github.com/cline/mcp-marketplace)** | Varies | Distribution reach | GitHub-based submission; [Cline's VS Code extension has 4.9M+ installs](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev) |
| **[LobeHub](https://lobehub.com/mcp)** | 10,000+ tools | Integrated UX | MCP server marketplace built into the LobeHub platform |

### mcp.so

[mcp.so](https://mcp.so) is one of the broader MCP server catalogs, organized by category with metadata like GitHub stars, installation instructions, and compatibility information. It provides a [playground](https://mcp.so/playground) that lets visitors test server capabilities directly in the browser. Note: mcp.so's total server count is not independently verifiable as of this audit (the site blocks automated fetches), so we don't repeat a specific figure here.

### Glama

[Glama](https://glama.ai/mcp/servers) lists over 71,000 MCP servers and hosted connectors across [85 categories](https://glama.ai/mcp/categories) as of August 2026. It differentiates through quality-focused curation: Glama [runs regular codebase and documentation scans](https://glama.ai/mcp/categories) to check that servers work as expected and flag obvious security issues, and assigns each server a quality score. This makes it particularly relevant for developers who need some assurance about the servers they adopt.

### Smithery

[Smithery](https://smithery.ai) lists over 14,240 MCPs and emphasizes the developer workflow. It offers CLI-based publishing (`smithery mcp publish <url> -n <org>/<name>`, [documented here](https://smithery.ai/docs/concepts/cli)), [hosted/remote deployment on Smithery's infrastructure](https://smithery.ai/docs/build), and built-in usage observability. For developers considering monetization, Smithery's usage data can help identify which servers have enough traction to justify paid tiers.

### PulseMCP

[PulseMCP](https://www.pulsemcp.com/servers) lists over 22,000 servers and stands out for its popularity signals — it tags servers as official, "Anthropic Reference," or community, and offers "Most Popular (All Time / This Month / This Week)" sorts along with estimated weekly visitor counts per server. This can help developers understand which niches are underserved and where demand exists.

### Cline MCP Marketplace

The [Cline marketplace](https://github.com/cline/mcp-marketplace) uses a GitHub-based submission process where developers open an issue with their repository URL and a 400×400 PNG logo. Per the [official submission guidelines](https://github.com/cline/mcp-marketplace/blob/main/README.md), submissions are reviewed for community adoption, developer credibility, project maturity, and security considerations. Cline's VS Code extension itself has [passed 4.9 million installs](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev) on the Visual Studio Marketplace, giving accepted servers meaningful distribution reach.

### LobeHub

[LobeHub](https://lobehub.com/mcp) integrates an MCP server marketplace directly into its platform, listing over 10,000 tools as of this audit. It provides another discovery surface for server developers, benefiting from LobeHub's existing user base.

For a deeper look at the official MCP Registry and how programmatic discovery works, see our [MCP Registry & Server Discovery guide](/guides/mcp-registry-server-discovery/).

---

## 3. Monetization Platforms (Paid Distribution)

A growing set of platforms now handle the hard parts of monetization — billing, hosting, access control, and payouts — so developers can focus on building servers.

### MCPize

According to [MCPize's own developer documentation](https://mcpize.com/developers/monetize-mcp-servers), the platform offers an **80% revenue share** to developers (20% platform fee). It handles hosting, SSL, payment processing, and distribution. Key features per that page and the [MCPize homepage](https://mcpize.com):

- [Direct Stripe Connect payouts](https://mcpize.com/developers/monetize-mcp-servers), paid out monthly on the 1st
- MRR tracking dashboard ("daily, weekly, monthly MCP server revenue" plus "MRR trends")
- 950+ servers listed, from 450+ publishing developers, per the MCPize homepage
- Python and TypeScript SDKs for integration
- Developers set their own pricing

MCPize is designed as a turnkey monetization layer: wrap an existing MCP server with their SDK, deploy via CLI, set a price, and the platform handles the rest.

### Apify

Apify [reports 36,000+ monthly developers and 130,000+ monthly signups](https://apify.com/mcp/developers) on its platform. It uses a **pay-per-event model** built around its `Actor.charge()` API — developers define billable events (a scrape completed, data returned, etc.) and Apify handles metering and billing.

Notable aspects, per the [same Apify page](https://apify.com/mcp/developers):

- Partner distribution through Make, n8n, Zapier, and Gumloop integrations
- Template-based development workflow
- Apify [reports $1.4 million paid out to developers in a recent month](https://apify.com/mcp/developers), and highlights a developer testimonial reporting over $2,000/month in earnings from the Apify Store
- MCP servers can be published as Apify Actors

### dotMCP

[dotMCP](https://dotmcp.io) focuses on converting existing APIs into MCP servers. Per its own site, it supports importing from OpenAPI 3.x specs, GraphQL schemas, and Postman collections, with auto-generation of MCP server wrappers. Features confirmed on [dotmcp.io](https://dotmcp.io):

- Server tunneling for self-hosted/local servers, via a tunnel daemon
- Visual builder for defining tools and handlers without code
- Distribution to Claude, Cursor, and other AI applications
- API import from OpenAPI, GraphQL, and Postman

This approach targets developers who already have APIs and want to reach the MCP ecosystem without rewriting their server logic. (Note: the `.com` version of this domain is now a parked/for-sale page; the live product is at `dotmcp.io`.)

### Agent Bazaar

Agent Bazaar is an **open billing standard** for MCP, with a reference implementation hosted at [noui.bot](https://noui.bot/). Per the [published MCP Billing Spec v1](https://noui.bot/specs/mcp-billing-v1) and the [noui.bot Agent Bazaar product page](https://noui.bot/), it offers:

- **Per-call metering** with sub-cent (microcent) precision
- **HMAC-SHA256 signed receipts** for cryptographic billing verification
- **Trust scores** — a composite of verification, reliability, and dispute history
- **90% revenue share** (10% platform fee) for providers, per the current noui.bot pricing

The open billing standard is particularly notable — if adopted broadly, it could reduce the fragmentation that currently exists across monetization platforms. Developers would implement one billing interface and reach multiple marketplaces.

### Nevermined

[Nevermined](https://nevermined.ai) provides **payment infrastructure** rather than a full marketplace. (Its domain moved from `nevermined.io` to `nevermined.ai`.) According to its site, it supports multiple payment protocols:

- **x402** — HTTP-native payment protocol
- **A2A** (Google's Agent-to-Agent) payments
- **AP2** (Agent Payments Protocol) support
- **Fiat payments** via Stripe and PayPal Braintree
- **Crypto settlement** via Coinbase Commerce (USDC, USDT, ETH)
- **Cryptographic verification** of payment transactions

A [published Nevermined case study](https://nevermined.ai/blog/mcp-monetization-ai-agents) reports that Valory cut deployment time for the payments and billing infrastructure behind its Olas AI agent marketplace from 6 weeks to 6 hours using Nevermined. This is a single-source claim from Nevermined's own marketing content (echoed by a Valory executive quote on the same page), not independently audited — treat the specific "6 weeks to 6 hours" figure as Nevermined's and Valory's own characterization. This platform targets developers who want payment capabilities without a specific marketplace — useful for self-distributed servers or multi-platform strategies.

---

## 4. DIY Monetization (Self-Hosted Billing)

Not every developer wants to use a platform. For those who prefer full control, several approaches exist.

### Moesif

According to [Moesif's own MCP-focused blog post](https://www.moesif.com/blog/api-strategy/model-context-protocol/Monetizing-MCP-Model-Context-Protocol-Servers-With-Moesif/), Moesif provides **usage analytics and billing that can be applied to MCP servers**. It meters JSON-RPC requests at the protocol level and integrates with billing providers. Key capabilities per that post:

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
| **Freemium** | Broad-appeal tools, developer adoption | [21st MCP](https://21st.dev/mcp) (free search/publish, capped daily installs; paid credits for AI generation) | Organic discovery, low friction, viral growth | Most users never pay; need volume |
| **Per-Call / Usage-Based** | Commodity functions, variable-cost operations | Apify `Actor.charge()` | Fair to users, scales with value | Revenue unpredictable; hard to forecast |
| **Subscription / Tiered** | Consistent-use tools, enterprise users | Monthly plans with request limits | Predictable revenue, simpler billing | May overshoot or undershoot value |
| **Outcome-Based** | High-value results (lead gen, data enrichment) | Charge only on successful results | Aligns incentives perfectly | Complex to define "success"; disputes |
| **Credit-Based** | Multi-tool platforms, variable operations | Prepaid credits consumed per call | Upfront revenue, flexible allocation | Users may feel "nickel-and-dimed" |
| **Hybrid** | Mature products, enterprise customers | Base subscription + usage overages | Predictable base + usage upside | Complex pricing; harder to communicate |

### Key Observations from Published Data

- **Freemium with low free tiers** appears to be a common early monetization pattern among MCP tool builders — we could not independently verify specific revenue figures claimed for individual freemium MCP servers, so we don't cite one here.
- **Per-call pricing** works well on platforms like Apify where the cost of each operation is variable and the value is easily attributable to a single call.
- **Subscription models** are more common for tools used daily or integrated into workflows, where predictable billing matters more than precise usage alignment.
- **Outcome-based pricing** is the highest-margin model but requires careful definition of what constitutes a successful outcome and robust tracking to verify it.

---

## 6. Publishing Your First MCP Server

Here is a practical walkthrough for getting an MCP server listed on major platforms, based on their published documentation.

### Smithery

Per [Smithery's CLI documentation](https://smithery.ai/docs/concepts/cli), the publishing workflow is:

```
smithery mcp publish "https://your-server-url" -n your-org/your-server-name
```

The CLI handles registration, metadata collection, and deployment. Smithery also supports [hosted/remote deployment](https://smithery.ai/docs/build), where the platform runs the server on its own infrastructure.

### Cline MCP Marketplace

Per the [official submission guidelines](https://github.com/cline/mcp-marketplace/blob/main/README.md):

1. Open a GitHub issue on the [Cline MCP Marketplace repository](https://github.com/cline/mcp-marketplace)
2. Include your repository URL
3. Include a 400×400 PNG logo
4. The review process evaluates: community adoption, developer credibility, project maturity, and security considerations
5. Accepted servers appear in the Cline marketplace

**Tip**: Per the same guidelines, a well-written README is usually sufficient, but including an optional `llms-install.md` file is recommended for servers with complex setup requirements (specific configuration, API credentials, etc.) — it helps AI coding assistants guide users through installation.

### MCPize

Per [MCPize's developer documentation](https://mcpize.com/developers/monetize-mcp-servers), the workflow is:

1. Install the MCPize SDK (Python or TypeScript)
2. Wrap your MCP server with MCPize's billing middleware
3. Deploy via CLI
4. Set pricing in the MCPize dashboard
5. The platform handles hosting, SSL, billing, and payouts

### Apify

Per [Apify's MCP developer page](https://apify.com/mcp/developers):

1. Start from an Apify Actor template
2. Implement your MCP server logic
3. Add billing events using `Actor.charge()` for billable operations
4. Publish to the Apify Store
5. The platform handles distribution, billing, and partner integrations

### Best Practices for Publishing

Our own recommendations, informed by the platform documentation cited throughout this guide:

- **README quality matters**: A clear, well-structured README with usage examples significantly improves adoption. Document every tool, resource, and prompt your server exposes.
- **Include `llms-install.md`**: This file helps AI coding assistants guide users through installation for servers with complex setup. It is specifically called out in [Cline's marketplace submission guidelines](https://github.com/cline/mcp-marketplace/blob/main/README.md).
- **Use a valid open-source license**: Most registries require or strongly prefer servers with a recognized license (MIT, Apache 2.0, etc.).
- **Security review**: Before publishing, review your server for common vulnerabilities. See our [MCP Server Security guide](/guides/mcp-server-security/) for a checklist.
- **Test across clients**: Servers that work reliably across Claude Desktop, Cursor, and other MCP clients tend to get better reviews and adoption — verify compatibility before publishing rather than assuming it.
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

[21st MCP](https://21st.dev/mcp), for example, keeps search, publishing, and management free but caps installs at two per day and gates its AI-generation features behind paid credits — a tight limit designed to force quick evaluation rather than casual, indefinite free use.

### Consider Outcome-Based Pricing for High-Value Tools

If your server produces high-value results (lead enrichment, code generation, data transformation), consider charging per successful outcome rather than per call. This aligns your revenue with the value you deliver and reduces friction for users.

### Use Analytics Before Setting Prices

If your server is already free and has users, instrument it with analytics before introducing pricing. Understanding usage patterns — which tools are called most, how often, by how many unique users — informs pricing decisions. Both [Smithery](https://smithery.ai) (built-in usage observability) and [Moesif](https://www.moesif.com/blog/api-strategy/model-context-protocol/Monetizing-MCP-Model-Context-Protocol-Servers-With-Moesif/) (JSON-RPC-level metering) offer analytics that can serve this purpose.

### A/B Test When Possible

Where a platform supports experimenting with different price points, that's the most reliable way to find the optimal price. Even without built-in support, you can test manually by adjusting prices over time and measuring conversion and churn.

---

## 8. Ecosystem Table

A consolidated view of the MCP marketplace and monetization ecosystem, based on published documentation:

| Platform | Type | Servers Listed | Revenue Share | Key Feature | URL |
|----------|------|---------------|---------------|-------------|-----|
| **mcp.so** | Discovery | Large (unverified count) | N/A (free) | Broad catalog, playground | mcp.so |
| **Glama** | Discovery | 71,000+ | N/A (free) | Automated security scans | glama.ai |
| **PulseMCP** | Discovery | 22,000+ | N/A (free) | Popularity signals, trending | pulsemcp.com |
| **Smithery** | Discovery + Hosting | 14,240+ | N/A (free) | CLI publish, hosted deployment | smithery.ai |
| **Cline Marketplace** | Discovery | Varies | N/A (free) | Access to Cline's 4.9M+ VS Code installs | GitHub-based (github.com/cline/mcp-marketplace) |
| **LobeHub** | Discovery | 10,000+ | N/A (free) | Integrated platform | lobehub.com |
| **MCPize** | Monetization | 950+ | 80% developer | Turnkey billing + hosting | mcpize.com |
| **Apify** | Monetization | Part of 36K+ monthly developers | Pay-per-event | Partner distribution (Make, n8n, Zapier) | apify.com |
| **dotMCP** | Monetization | Growing | Varies | API import, auto-generation | dotmcp.io |
| **Agent Bazaar** | Monetization | Growing | 90% developer | Open billing standard, microcent metering | noui.bot |
| **Nevermined** | Payment Infra | N/A (infra layer) | Varies | x402, crypto + fiat, cryptographic verification | nevermined.ai |
| **Moesif** | DIY Billing | N/A (analytics layer) | N/A | JSON-RPC metering, Stripe/Chargebee/Zuora integration | moesif.com |

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

