---
title: "Insurance & InsurTech MCP Servers — Policy Management, Claims Processing, Underwriting Intelligence, and Compliance"
date: 2026-03-15T23:55:00+09:00
description: "Insurance and InsurTech MCP servers are a surprisingly active and commercially-backed category with 18+ servers across 7 subcategories."
og_description: "Insurance & InsurTech MCP servers: Sure MCP (first to enable AI agents to quote, bind, service policies), Root Platform MCP (official, v1.3.22), Socotra MCP (most mature, enterprise-grade, now GA), Fenris MCP (insurance data layer, consumer/property/vehicle intelligence), Apify Underwriting Intelligence (8 actors, multi-peril scoring), EIOPA Insurance MCP (7 tools, Solvency II, DORA), US_Compliance_MCP v2.0 (50 regulations, 2,079 sections). 18+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "Insurance and InsurTech MCP servers for AI-powered policy management, claims processing, underwriting intelligence, and regulatory compliance. This is a surprisingly active category with strong commercial backing — now featuring three major commercial platforms. **Sure launches first full-lifecycle insurance MCP** — Sure's MCP capability enables AI agents to autonomously quote, bind, and service insurance policies across all supported lines and carriers. Beta partners report 95% reduction in quote-to-bind time and 80% decrease in customer service response times. Available for enterprise clients and developer partners. **Root Platform MCP actively maintained at v1.3.22** — Root Insurance's @rootplatform/mcp-server (TypeScript, MIT) provides comprehensive tools for creating quotes, managing policies, and handling complete insurance workflows. Updated within the past week on npm. **Socotra MCP now GA for all customers** — Socotra's commercial MCP server is now generally available to all customers and select partners across all insurance lines and geographic markets. Added VS Code support alongside Claude and Cursor. 10-minute setup. Enterprise security with full audit trails. **Fenris MCP Server launches as insurance data layer** — Fenris (March 2026) provides AI agents with real-time consumer, property, vehicle, and predictive intelligence data, supporting intake, quoting, underwriting triage, lead routing, and renewal outreach. Compatible with Claude, ChatGPT, Gemini. **Underwriting intelligence gets multi-peril scoring** — the Apify Insurance Underwriting Intelligence MCP wraps 8 specialized actors for property & casualty risk assessment with climate trajectory modeling across 5, 10, and 25-year horizons. **European insurance regulation gets MCP coverage** — NEW eiopa-insurance-mcp (TypeScript, BSL-1.1, 7 tools) provides structured access to 185 EIOPA publications covering Solvency II, DORA for insurance, and IORP II. **US compliance expands to v2.0** — US_Compliance_MCP now covers 50 US regulations with 2,079 sections and 135 definitions, with automated regulation change monitoring. ComplianceCow cow-mcp reaches 11 stars with 271 commits. **Claims processing reaches AI-native quality** — ClaimsProcessingAssistant-MCP provides AI-powered document analysis with Supabase and Redis. insurance-ai-mcp-server offers enterprise Kafka-based claim orchestration. **Major gaps remain** — no actuarial modeling or pricing engines, no reinsurance platforms (Swiss Re, Munich Re), no catastrophe modeling (RMS, AIR, CoreLogic), no agency management systems (Applied Epic, Vertafore), no claims adjudication engines (Guidewire, Duck Creek). The category holds at 3.5/5 — impressive commercial investment from Sure, Root, Socotra, and Fenris, but the computational backbone of insurance (actuarial, reinsurance, cat modeling) remains completely absent."
last_refreshed: 2026-04-28
---

Insurance and InsurTech MCP servers let AI assistants manage policies, process claims, assess underwriting risk, and navigate regulatory compliance. Instead of logging into separate policy administration systems, claims platforms, and compliance databases, these servers let AI agents handle insurance workflows through the Model Context Protocol.

*This review was originally published on 2026-03-15 and last refreshed on 2026-04-28.*

This review covers the **insurance and InsurTech** vertical — policy platforms, claims processing, underwriting intelligence, insurance connectors, compliance, and document processing. For healthcare-adjacent insurance servers, see our [Healthcare MCP review](/reviews/healthcare-medical-mcp-servers/). For financial services broadly, see our [Finance MCP review](/reviews/personal-finance-mcp-servers/).

The headline findings: **Sure enables AI agents to autonomously quote, bind, and service policies** with reported 95% faster quote-to-bind times. **Root Platform stays actively maintained at v1.3.22** and **Socotra goes GA for all customers** with VS Code support. **Fenris launches as the insurance data layer** for AI agents. **European insurance regulation gets MCP coverage** via EIOPA guidelines MCP. **US compliance scales to 50 regulations** with automated monitoring. **Actuarial modeling, reinsurance, and catastrophe modeling are still completely missing.**

**Category:** [Finance & Fintech](/categories/finance-fintech/)

## Policy Platforms

### Root Platform MCP (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [@rootplatform/mcp-server](https://www.npmjs.com/package/@rootplatform/mcp-server) | — | TypeScript | MIT | Multiple |

The **official MCP server from Root Insurance**, a leading InsurTech platform:

- **Quote creation** — generate insurance quotes programmatically through AI agents
- **Policy management** — create, modify, and manage insurance policies
- **Full insurance workflows** — end-to-end policy lifecycle through natural language
- **Dual environments** — sandbox for testing, production for live operations

Install via npm with your Root API key. Now at **v1.3.22** and actively maintained (updated within the past week). This is significant because Root is a publicly-traded InsurTech company — this isn't a demo but a commercially-backed interface to real insurance operations. The MIT license means you can inspect and extend the integration.

### Socotra MCP (Commercial)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Socotra MCP](https://docs.socotra.com/aiGuide/mcpServer/mcpServerOverview.html) | — | — | Commercial | Full lifecycle |

Described as **"the most mature MCP server in the insurance industry"** — Socotra's commercial offering covers the full insurance lifecycle:

- **Policy administration** — product configuration, policy creation, endorsements, renewals
- **Claims management** — FNOL, investigation, adjudication, payment
- **Billing** — invoicing, payment processing, accounting
- **Enterprise security** — capability-scoped authentication, encrypted agent sessions, policy-aware authorization
- **Full audit trail** — every AI action is logged and traceable

Their "Agentic Configuration" feature claims to reduce product development time by 50%, costs by 75%, and prototype iteration time by 90%. **Now generally available** to all customers and select partners across all insurance lines and geographic markets. 10-minute setup for Claude, Cursor, and VS Code. In March 2026, Socotra became the first insurance core to release generally available AI. For insurance companies already on the Socotra platform, this provides the most comprehensive AI agent integration available.

### Sure MCP (Commercial)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Sure MCP](https://www.sureapp.com/press/sure-launches-insurance-industrys-first-model-context-protocol-mcp-capability-enabling-ai-agents-to-quote-bind-and-service-policies) | — | — | Commercial | Full lifecycle |

Sure launched what it calls **the insurance industry's first MCP capability** enabling AI agents to handle the complete insurance lifecycle:

- **Quote generation** — real-time insurance quotes across Sure's carrier network
- **Policy binding** — AI agents execute binding decisions autonomously
- **Policy administration** — manage changes, endorsements, and renewals
- **Claims initiation** — start and track claims through AI agents
- **Customer service** — handle policyholder inquiries and requests

Beta partners report **95% reduction in quote-to-bind time** and **80% decrease in customer service response times**. Available for enterprise clients and developer partners across all supported insurance lines (auto, homeowners, renters, travel, rental car, product warranty, home warranty, AD&D) and geographic markets. Single interface access to Sure's entire carrier network.

### wadhawan2411radhika/insurance-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [insurance-mcp-server](https://github.com/wadhawan2411radhika/insurance-mcp-server) | — | Python | — | 5 |

A straightforward MCP server for **insurance policy and premium management**:

- `get_due_premiums` — find premiums due for payment
- `get_overdue_premiums` — identify overdue premium payments
- `search_customer` — look up customer information
- `get_policy_summary` — retrieve policy details
- `get_customer_payment_history` — view payment records

Uses SQLite for storage. A good reference implementation for understanding how insurance data flows through MCP, though more of a demo than a production system.

## Claims Processing

### chbhargavareddy/ClaimsProcessingAssistant-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ClaimsProcessingAssistant-MCP](https://github.com/chbhargavareddy/ClaimsProcessingAssistant-MCP) | — | TypeScript | — | Multiple |

An **AI-native claims processing backend** built on MCP:

- **Claims CRUD** — create, read, update, and manage insurance claims
- **AI-powered document analysis** — intelligent validation of claim documents using Claude
- **Advanced validation** — comprehensive error handling and input checking
- **Supabase integration** — cloud database for claims storage
- **Redis caching** — performance optimization for frequently accessed claims

The integration with Claude for document analysis is noteworthy — the AI doesn't just route claims, it examines supporting documents for validity. Built for Claude Desktop integration.

### chandan-akshronix/insurance-ai-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [insurance-ai-mcp-server](https://github.com/chandan-akshronix/insurance-ai-mcp-server) | — | Java/Python | — | Multiple |

An **enterprise-grade claims orchestration system** using Kafka-based microservices:

- Claim orchestration across multiple services
- Kafka-based messaging for reliable claim routing
- AI agent integration for intelligent claim processing
- Database and observability tool connections
- Enterprise architecture patterns (microservices, event-driven)

Takes a very different approach from the TypeScript-based claims servers — this is designed for high-volume enterprise environments where claims processing needs message queuing and distributed service coordination.

## Underwriting Intelligence

### Apify Insurance Underwriting Intelligence MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Insurance Underwriting Intelligence MCP](https://apify.com/ryanclinton/insurance-underwriting-intelligence-mcp/api/mcp) | — | Apify platform | Commercial | 8 actors |

A **property & casualty underwriting MCP** wrapping 8 specialized risk assessment actors:

- **Multi-peril scoring** — comprehensive property risk evaluation across hazard types
- **Disaster history** — historical natural disaster data for any location
- **Seismic exposure** — earthquake risk assessment
- **Flood exposure** — flood zone and risk analysis
- **Environmental liability** — pollution and environmental hazard assessment
- **Crime proximity** — local crime data for risk scoring
- **Climate trajectory** — projected climate risk across 5, 10, and 25-year horizons

Pay-per-event pricing on the Apify platform. For P&C underwriters, this provides data that would otherwise require subscriptions to multiple risk data providers. The climate trajectory modeling across multiple time horizons is particularly valuable as insurers grapple with climate-related loss trends.

### dbbaskette/imc-policy-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [imc-policy-mcp-server](https://github.com/dbbaskette/imc-policy-mcp-server) | — | Java | — | RAG tools |

A **production-ready MCP server for intelligent policy document retrieval** using RAG:

- Advanced RAG techniques for policy document search
- Customer-scoped document access (security boundary per customer)
- Built with Spring AI 1.1.0 on Spring Boot
- Supports STDIO and SSE transports
- Requires Java 21+

Particularly useful for underwriters and claims adjusters who need to quickly find relevant policy language, exclusions, and coverage details across large document collections.

## Insurance Data Intelligence

### Fenris MCP Server (Commercial)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Fenris MCP](https://fenrisd.com/mcp/) | — | — | Commercial | Multiple |

Launched March 2026, Fenris positions its MCP server as **the data layer for insurance AI** — giving AI agents direct access to real insurance intelligence:

- **Consumer data** — household composition, demographics, and predictive scoring
- **Property attributes** — real-time property data for underwriting
- **Vehicle and driver data** — vehicle details and driver information
- **Business information** — commercial insurance data
- **Predictive intelligence** — scoring models for risk assessment

Supports insurance workflows including intake, quoting, underwriting triage, lead routing, and renewal outreach. Compatible with Claude, ChatGPT, Gemini, and custom AI agents supporting MCP. Fenris processes tens of millions of insurance transactions annually — this is production-grade data infrastructure, not a demo. Eliminates the need for custom data pipelines between AI agents and insurance data sources.

## Insurance Connectors

### markswendsen-code/mcp-lemonade

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-lemonade](https://glama.ai/mcp/servers/markswendsen-code/mcp-lemonade) | — | TypeScript | — | Multiple |

An MCP connector for **Lemonade**, the AI-native insurance company:

- File insurance claims through AI agents
- Check claim status and track progress
- Update existing policies
- Download insurance ID cards
- Get quotes for renters, homeowners, pet, and car insurance

Uses Playwright browser automation to interact with Lemonade's platform — this is a scraper-style integration rather than an official API integration. Useful for Lemonade customers who want AI agent access to their insurance, but inherently fragile if Lemonade changes their UI.

### bruteforce17/mcp-server-salesforce-insurance

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-salesforce-insurance](https://github.com/bruteforce17/mcp-server-salesforce-insurance) | — | TypeScript | MIT | 9+ |

Built for **insurance companies on Salesforce**:

- Insurance policy design via Salesforce Product Catalog Management (PCM)
- Object and field management
- Smart object search and schema discovery
- Data queries and cross-object search (SOSL)
- Data manipulation (insert, update, delete, upsert)
- Apex code management

Integrates with Claude Desktop and Cursor for natural language insurance policy design. Many mid-size insurers run on Salesforce — this bridges the gap between their CRM/policy system and AI agents.

### remoprinz/swiss-health-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [swiss-health-mcp](https://github.com/remoprinz/swiss-health-mcp) | — | TypeScript | — | Multiple |

A niche but data-rich MCP server for **Swiss health insurance premiums**:

- 1.6 million premium records from BAG Priminfo (Swiss federal data)
- Coverage across 55 Swiss health insurers
- 11 years of data (2016-2026)
- Premium comparison and trend analysis

Switzerland's mandatory health insurance system makes premium comparison a real consumer need. This server turns that public dataset into a queryable resource for AI assistants helping Swiss residents choose health insurance plans.

### SecureLend/mcp-financial-services

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-financial-services](https://github.com/SecureLend/mcp-financial-services) | — | TypeScript | MIT | Multiple |

An open-source **financial services comparison MCP** that includes insurance:

- Loan comparison (personal and business)
- Insurance product comparison
- Standardized schemas across financial products
- SOC 2 Type 2 certified

Broader than insurance alone, but the standardized approach to comparing financial products — including insurance — through a single MCP interface is valuable for AI-powered financial advisors.

## Compliance & Regulatory

### Ansvar-Systems/eiopa-insurance-mcp (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [eiopa-insurance-mcp](https://github.com/Ansvar-Systems/eiopa-insurance-mcp) | 0 | TypeScript | BSL-1.1 | 7 |

A new MCP server (April 2026) providing **structured access to European insurance regulation**:

- **185 EIOPA publications** — 105 guideline rows and 80 technical standard rows
- **Solvency II** — capital requirements and risk management for European insurers
- **DORA for insurance** — Digital Operational Resilience Act compliance
- **IORP II** — pension fund supervision and governance
- **7 tools** — search, retrieval by reference, category listing, data freshness checking

From the same team behind US_Compliance_MCP. Supports hosted and self-hosted deployments. License converts to Apache-2.0 on 2030-04-13. For insurers operating in the EU, this fills a gap — EIOPA guidelines are notoriously difficult to navigate, and having them queryable through AI agents is immediately valuable.

### Ansvar-Systems/US_Compliance_MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [US_Compliance_MCP](https://github.com/Ansvar-Systems/US_Compliance_MCP) | 1 | TypeScript | — | Multiple |

Now at **v2.0.0** with significantly expanded scope — **50 US regulations, 2,079 sections, 135 definitions**:

- **HIPAA** — health insurance portability and privacy requirements
- **GLBA** — Gramm-Leach-Bliley Act for financial/insurance data protection
- **NYDFS 500** — New York Department of Financial Services cybersecurity requirements for insurance companies
- **SOX** — Sarbanes-Oxley for publicly-traded insurers
- **CCPA/CPRA** — California consumer privacy for policyholder data
- **FISMA, FedRAMP, CMMC 2.0** — federal security frameworks
- **18 state privacy laws** — comprehensive US privacy coverage
- Plus FERPA, COPPA, FDA 21 CFR Part 11, CIRCIA, EPA RMP, FFIEC
- **Automated regulation monitoring** — auto-generates PRs when regulations change
- Published as npm package `@ansvar/us-regulations-mcp`

For insurance compliance teams, having HIPAA, GLBA, and NYDFS 500 queryable through AI agents is immediately practical — these are the three regulatory frameworks that most directly govern insurance operations. The automated monitoring for regulation changes is a significant improvement over the initial release.

### ComplianceCow/cow-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cow-mcp](https://github.com/ComplianceCow/cow-mcp) | 11 | Python | — | 33+ |

A **GRC (Governance, Risk, Compliance) automation** MCP with 33+ tools across 4 servers (271 commits, actively maintained):

- Rules server — regulatory rule queries
- Insights server — control status and coverage reports
- Workflow server — compliance process automation
- Assistant server — AI-guided compliance guidance
- OAuth 2.0 authentication
- Compliance Graph for data ingestion across cloud, SaaS, and Kubernetes

Not insurance-specific, but GRC automation is a core need for insurers managing regulatory requirements across multiple jurisdictions and lines of business.

## Document Processing

### Unstract MCP (Commercial)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Unstract MCP](https://unstract.com/blog/unstract-mcp-server/) | — | Python | Commercial | Multiple |

A commercial document processing MCP that **specifically supports insurance documents**:

- **ACORD forms** — the standard forms used across the insurance industry
- **Certificates of liability insurance** — COI extraction and validation
- **Life insurance applications** — application data extraction
- **Healthcare benefits claims** — health claim form processing
- **Equipment damage reports** — property/casualty documentation
- **Expense claims** — expense report extraction

Claims to reduce manual document processing effort by up to 91.67%. 14-day free trial. For insurance operations teams that process thousands of forms daily, this addresses a real bottleneck — ACORD form extraction alone is a significant pain point in the industry.

## What's Missing

The insurance MCP ecosystem has notable gaps:

- **Actuarial modeling** — no actuarial pricing engines, loss reserving tools, or statistical modeling servers
- **Reinsurance** — no Swiss Re, Munich Re, or treaty/facultative reinsurance management
- **ACORD data standards** — only document extraction (Unstract), no server implementing ACORD messaging standards for system-to-system insurance data exchange
- **Catastrophe modeling** — no RMS, AIR Worldwide, or CoreLogic cat model integration
- **Agency management** — no Applied Epic, Vertafore, or HawkSoft MCP servers (these are what most insurance agencies actually run on)
- **Life/annuity administration** — no policy administration systems for life insurance products
- **Claims adjudication engines** — no Guidewire ClaimCenter, Duck Creek, or Majesco integration (Guidewire has no MCP presence despite being the dominant P&C platform)
- **Parametric insurance** — no index-based or parametric insurance product management
- **Insurance marketplaces** — no Lloyd's, Quotech, or insurance aggregator integration
- **Rating engines** — no comparative rating or insurance quoting engines beyond Root and Sure

## The Bottom Line

**Rating: 3.5/5** — Insurance and InsurTech MCP servers continue to grow with strong commercial backing from four major platforms: Sure (full lifecycle quoting/binding/servicing), Root Platform (actively maintained at v1.3.22), Socotra (now GA for all customers), and Fenris (insurance data intelligence layer). The compliance angle has expanded significantly — US coverage doubled to 50 regulations with automated monitoring, and European insurance regulation (EIOPA/Solvency II/DORA) now has MCP coverage for the first time. Underwriting intelligence from Apify and claims processing options remain solid.

The rating holds at 3.5/5 because despite impressive commercial investment, the fundamental gaps persist. The actuarial, reinsurance, and catastrophe modeling segments — the computational and financial backbone of insurance — are completely absent. Agency management systems that most insurance agencies operate on daily have zero MCP representation. Guidewire, the dominant P&C platform, has no MCP presence. And while Unstract handles ACORD form extraction, no server implements ACORD messaging standards for programmatic insurance data exchange.

For insurers on Sure, Root, or Socotra, the MCP story is genuinely compelling — full lifecycle management through AI agents with proper security and audit trails. Fenris adds a critical data layer that was previously missing. The compliance story now spans both US and EU regulations. For everyone else, this is a category to watch as more insurance platforms provide official MCP integrations.

*This review was last refreshed on 2026-04-28 using Claude Opus 4.6 (Anthropic).*
