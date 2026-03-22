---
title: "Insurance & InsurTech MCP Servers — Policy Management, Claims Processing, Underwriting Intelligence, and Compliance"
date: 2026-03-15T23:55:00+09:00
description: "Insurance and InsurTech MCP servers are a surprisingly active category with 15+ servers across 6 subcategories. Policy Platforms: Root Platform MCP (official, TypeScript, MIT — quote creation, policy management, full insurance workflows, sandbox/production), Socotra MCP (commercial, most mature insurance MCP — full lifecycle with capability-scoped auth, encrypted agent sessions, policy-aware authorization, every AI action logged), insurance-mcp-server (Python, 5 tools — premium tracking, overdue payments, customer search, SQLite). Claims Processing: ClaimsProcessingAssistant-MCP (TypeScript — AI-powered document analysis, Supabase, Redis caching, comprehensive validation), insurance-ai-mcp-server (Java/Python, Kafka microservices — claim orchestration, enterprise architecture). Underwriting: Apify Insurance Underwriting Intelligence MCP (8 actors — multi-peril scoring, disaster history, seismic/flood exposure, climate trajectory 5/10/25yr), imc-policy-mcp-server (Java, Spring AI 1.1.0 — RAG-based policy document retrieval, customer-scoped search). Insurance Connectors: mcp-lemonade (TypeScript, Playwright — file claims, check status, update policies, get quotes for renters/homeowners/pet/car), mcp-server-salesforce-insurance (TypeScript, MIT — 9+ tools, Salesforce PCM for policy design), swiss-health-mcp (TypeScript — 1.6M Swiss health insurance premium records, 55 insurers, 2016-2026). Compliance: US_Compliance_MCP (Python — HIPAA, GLBA, NYDFS 500, SOX, CCPA with NIST mappings), cow-mcp (Python — 33+ GRC tools, OAuth 2.0). Document Processing: Unstract MCP (commercial — ACORD forms, certificates of liability, healthcare claims, expense reports). Gaps: no actuarial modeling, no reinsurance, no ACORD data standards server, no catastrophe modeling, no agency management systems, no life/annuity administration, no claims adjudication engines, no parametric insurance. Rating: 3.5/5."
og_description: "Insurance & InsurTech MCP servers: Root Platform MCP (official, full insurance workflows), Socotra MCP (most mature, enterprise-grade), Apify Underwriting Intelligence (8 actors, multi-peril scoring), ClaimsProcessingAssistant-MCP (AI document analysis), swiss-health-mcp (1.6M premium records). 15+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "Insurance and InsurTech MCP servers for AI-powered policy management, claims processing, underwriting intelligence, and regulatory compliance. This is a surprisingly active category with strong commercial backing. **Root Platform launches official insurance MCP** — Root Insurance's @rootplatform/mcp-server (TypeScript, MIT) is the standout, providing AI agents with comprehensive tools for creating quotes, managing policies, and handling complete insurance workflows. Supports sandbox and production environments with a Root API key. Root is a leading InsurTech platform — this is commercially-backed infrastructure, not a hobby project. **Socotra claims 'most mature insurance MCP'** — Socotra's commercial MCP server enables AI agents to execute full insurance lifecycle workflows with enterprise security: capability-scoped authentication, encrypted agent sessions, and policy-aware authorization. Every AI action is logged and traceable — critical for regulated industries. Their 'Agentic Configuration' feature claims to reduce product development time by 50% and costs by 75%. 10-minute setup for Claude and Cursor. **Underwriting intelligence gets multi-peril scoring** — the Apify Insurance Underwriting Intelligence MCP wraps 8 specialized actors for property & casualty risk assessment: multi-peril scoring, disaster history, seismic and flood exposure, environmental liability, crime proximity, and climate trajectory modeling across 5, 10, and 25-year horizons. Pay-per-event pricing on the Apify platform. **Claims processing reaches AI-native quality** — ClaimsProcessingAssistant-MCP (TypeScript) provides claims CRUD with AI-powered document analysis, Supabase integration, Redis caching, and comprehensive validation. Meanwhile, insurance-ai-mcp-server takes an enterprise microservices approach with Kafka-based claim orchestration. **Salesforce insurance gets MCP integration** — mcp-server-salesforce-insurance (TypeScript, MIT) provides 9+ tools for insurance companies using Salesforce PCM, enabling natural language policy design and management. **Swiss health insurance premiums go queryable** — swiss-health-mcp (TypeScript) exposes 1.6 million Swiss health insurance premium records across 55 insurers from 2016-2026, enabling AI agents to compare premiums and analyze trends. **RAG-based policy document retrieval** — imc-policy-mcp-server (Java, Spring Boot, Spring AI 1.1.0) provides production-ready intelligent insurance policy document search using advanced RAG techniques with customer-scoped security. **Lemonade gets AI agent access** — mcp-lemonade uses Playwright browser automation to interact with Lemonade's insurance platform: file claims, check status, update policies, download ID cards, and get quotes across renters, homeowners, pet, and car insurance. **Compliance tooling covers insurance regulations** — US_Compliance_MCP (Python) provides query tools for HIPAA (health insurance), GLBA (financial/insurance), NYDFS 500 (NY insurance companies), plus SOX, CCPA, and NIST control mappings. ComplianceCow's cow-mcp adds 33+ GRC automation tools. **ACORD form processing via Unstract** — Unstract's commercial MCP server handles insurance document extraction including ACORD forms, certificates of liability insurance, life insurance applications, healthcare benefits claims, and equipment damage reports. Claims to reduce manual effort by up to 91.67%. **Major gaps remain** — no actuarial modeling or pricing engines, no reinsurance platforms (Swiss Re, Munich Re), no ACORD data standards server (only document extraction), no catastrophe modeling (RMS, AIR, CoreLogic), no agency management systems (Applied Epic, Vertafore), no life/annuity administration, no claims adjudication engines, no parametric/index insurance, no insurance marketplaces or aggregators, no policy administration systems beyond Root and Socotra. The category earns 3.5/5 — impressive commercial backing from Root Platform and Socotra, strong underwriting intelligence from Apify, and solid claims processing options. The compliance angle is well-covered for US regulations. But the actuarial, reinsurance, and catastrophe modeling segments — the computational backbone of insurance — are completely absent, and agency management systems that most insurance agencies run on have no MCP representation."
last_refreshed: 2026-03-15
---

Insurance and InsurTech MCP servers let AI assistants manage policies, process claims, assess underwriting risk, and navigate regulatory compliance. Instead of logging into separate policy administration systems, claims platforms, and compliance databases, these servers let AI agents handle insurance workflows through the Model Context Protocol.

This review covers the **insurance and InsurTech** vertical — policy platforms, claims processing, underwriting intelligence, insurance connectors, compliance, and document processing. For healthcare-adjacent insurance servers, see our [Healthcare MCP review](/reviews/healthcare-medical-mcp-servers/). For financial services broadly, see our [Finance MCP review](/reviews/finance-mcp-servers/).

The headline findings: **Root Platform and Socotra provide commercially-backed policy lifecycle MCP servers.** **Apify delivers multi-peril underwriting intelligence with climate trajectory modeling.** **Claims processing reaches AI-native quality** with document analysis and Kafka-based orchestration. **Compliance covers HIPAA, GLBA, and NYDFS 500.** **Actuarial modeling, reinsurance, and catastrophe modeling are completely missing.**

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

Install via npm with your Root API key. This is significant because Root is a publicly-traded InsurTech company — this isn't a demo but a commercially-backed interface to real insurance operations. The MIT license means you can inspect and extend the integration.

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

Their "Agentic Configuration" feature claims to reduce product development time by 50%, costs by 75%, and prototype iteration time by 90%. 10-minute setup for Claude and Cursor. For insurance companies already on the Socotra platform, this provides the most comprehensive AI agent integration available.

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

### Ansvar-Systems/US_Compliance_MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [US_Compliance_MCP](https://github.com/Ansvar-Systems/US_Compliance_MCP) | — | Python | — | Multiple |

A compliance MCP server covering **regulations directly relevant to insurance**:

- **HIPAA** — health insurance portability and privacy requirements
- **GLBA** — Gramm-Leach-Bliley Act for financial/insurance data protection
- **NYDFS 500** — New York Department of Financial Services cybersecurity requirements for insurance companies
- **SOX** — Sarbanes-Oxley for publicly-traded insurers
- **CCPA/CPRA** — California consumer privacy for policyholder data
- Plus FERPA, COPPA, FDA 21 CFR Part 11, CIRCIA, EPA RMP, FFIEC, and state privacy laws
- NIST control mappings included

For insurance compliance teams, having HIPAA, GLBA, and NYDFS 500 queryable through AI agents is immediately practical — these are the three regulatory frameworks that most directly govern insurance operations.

### ComplianceCow/cow-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cow-mcp](https://github.com/ComplianceCow/cow-mcp) | — | Python | — | 33+ |

A **GRC (Governance, Risk, Compliance) automation** MCP with 33+ tools across 4 servers:

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
- **Claims adjudication engines** — no Guidewire ClaimCenter, Duck Creek, or Majesco integration
- **Parametric insurance** — no index-based or parametric insurance product management
- **Insurance marketplaces** — no Lloyd's, Quotech, or insurance aggregator integration
- **Rating engines** — no comparative rating or insurance quoting engines beyond Root

## The Bottom Line

**Rating: 3.5/5** — Insurance and InsurTech MCP servers are a surprisingly active category with genuine commercial backing. Root Platform and Socotra provide real policy lifecycle management. Apify's underwriting intelligence offers multi-peril risk scoring with climate projections. Claims processing has both AI-native and enterprise microservices approaches. The compliance angle is well-covered for US insurance regulations.

The rating reflects strong commercial investment balanced against significant gaps. The actuarial, reinsurance, and catastrophe modeling segments — the computational and financial backbone of insurance — are completely absent. Agency management systems that most insurance agencies operate on daily have zero MCP representation. And while Unstract handles ACORD form extraction, no server implements ACORD messaging standards for programmatic insurance data exchange.

For insurers on Root or Socotra, the MCP story is genuinely compelling — full lifecycle management through AI agents with proper security and audit trails. For everyone else, this is a category to watch as more insurance platforms follow Root's lead in providing official MCP integrations.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
