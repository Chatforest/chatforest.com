# Insurance MCP Servers — Claims Processing, Underwriting, Policy Management, Socotra, Sure, EMPLOYERS, and More

> Insurance MCP servers are enabling AI agents to process claims, assess underwriting risk, manage policies, and integrate with insurance platforms — and the category is accelerating fast.


Insurance MCP servers are connecting AI agents to claims processing workflows, underwriting risk assessment, policy management systems, and enterprise insurance platforms. Instead of manually navigating claims queues or underwriting dashboards, an AI agent can validate a claim against policy rules, score multi-peril risk for a property, or generate a real-time insurance quote through standardized MCP tools.

The landscape divides into seven areas: **claims processing** (ClaimsProcessingAssistant — rules engine with AI document analysis, multi-agent mesh), **underwriting** (AWS sample with explainable AI decisions, Apify peril scoring for P&C, Sixfold AI production deployments), **policy management** (insurance-mcp-server for premium tracking, Salesforce PCM integration, IMC RAG-based document retrieval), **enterprise platforms** (Socotra with GA AI underwriting, Sure, One Inc, EMPLOYERS in ChatGPT), **public insurance data** (FEMA flood claims, SEC EDGAR financials, Swiss health premiums), **regulatory compliance** (EIOPA Solvency II/DORA, RegGuard marketing compliance), and **financial services** (SecureLend — insurance comparison within broader fintech, Policy Penguin portfolio management).

The headline findings: **the carrier-to-consumer MCP path is proven** — EMPLOYERS became the first insurance carrier in the ChatGPT App Directory (April 2026), wrapping their real-time rating engine as MCP tool calls. **Socotra shipped GA AI underwriting** — Socotra Assistant is the first generally available AI capability embedded in an insurance core platform. **EU regulatory compliance arrived** — EIOPA guidelines, Solvency II, and DORA are now accessible via MCP. **Public insurance data is finally queryable** — FEMA's 80M+ flood policy records and SEC EDGAR insurer financials are wrapped behind MCP. **The enterprise-community gap is narrowing** — open source went from near-zero to practical utility in several subverticals.

**Category:** [Finance & Fintech](/categories/finance-fintech/)

## Claims Processing

### ClaimsProcessingAssistant-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chbhargavareddy/ClaimsProcessingAssistant-MCP](https://github.com/chbhargavareddy/ClaimsProcessingAssistant-MCP) | 5 | TypeScript | — | Claims workflow |

The **most feature-complete open source insurance MCP server**, built around a claims validation rules engine with Supabase backend. Key capabilities:

- **Claim validation rules engine** — policy checks, duplicate detection, high-value claim flagging, document completeness verification
- **AI document analysis** — uses Claude for intelligent document review within the claims workflow
- **Redis caching** — performance optimization for repeated queries
- **Comprehensive error handling** — structured error responses across the workflow

*Update (April 2026):* The project has grown from ~1 to 5 stars and 49 commits — still small, but showing more sustained development than most insurance MCP projects. The architecture remains sound, separating validation rules from the AI analysis layer for auditability. Docker containerization support has been added.

### insurance-ai-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chandan-akshronix/insurance-ai-mcp-server](https://github.com/chandan-akshronix/insurance-ai-mcp-server) | ~0 | Python | — | Claims + underwriting |

A backend MCP server for an **AI Automated Insurance Claim and Underwriting System** using Kafka-based messaging for claim orchestration. Integrates with AI agents, databases, and observability tools (Prometheus metrics, OpenTelemetry distributed tracing). More of an architectural reference than a ready-to-use tool — the Kafka-based event-driven design is appropriate for insurance workflows where multiple systems need to coordinate on a single claim.

### insuranceagenticmesh

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vishalmysore/insuranceagenticmesh](https://github.com/vishalmysore/insuranceagenticmesh) | 1 | Java | MIT | 4 MCP servers |

**NEW.** A distributed **multi-agent insurance system** with four specialized Java/Spring Boot MCP servers:

- **Policy Management** (port 7871) — lifecycle handling (creation, renewal, cancellation)
- **Claims Processing** (port 7872) — submission, verification, and payment workflows
- **Underwriting** (port 7873) — risk assessment and premium calculation
- **Customer Service** (port 7874) — support and account management

Uses JSON-RPC 2.0 communication and integrates with Claude Desktop. The agents collaborate autonomously to handle complete insurance processes — from risk assessment through policy creation and claims resolution — without requiring a central orchestrator. This is the first insurance MCP implementation to demonstrate a **multi-agent mesh architecture**, which is the right pattern for insurance where different departments need to coordinate on shared workflows. Early-stage (5 commits), but architecturally interesting.

## Policy Management

### insurance-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [wadhawan2411radhika/insurance-mcp-server](https://github.com/wadhawan2411radhika/insurance-mcp-server) | <5 | Python | — | 9+ tools |

A **policy and premium payment management** MCP server for Claude Desktop. Tools include:

- Premium due date tracking and overdue payment detection
- Customer search by name, policy lookup by ID
- Payment history retrieval
- Policy summaries grouped by type
- Average premium calculation
- Multi-policy customer identification
- Analytics and reporting

Supports custom database paths via `INSURANCE_DB_PATH` and optional WhatsApp MCP integration for notifications. This is a practical, if basic, implementation — the kind of tool a small insurance agency could use to give their AI assistant access to policy data. The limitation is the SQLite-based storage, which wouldn't scale to a real insurance book of business.

### mcp-server-salesforce-insurance

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bruteforce17/mcp-server-salesforce-insurance](https://github.com/bruteforce17/mcp-server-salesforce-insurance) | ~0 | — | — | Salesforce PCM |

Connects Claude Desktop and Cursor to **Salesforce Product Catalog Management (PCM)** for insurance. Enables insurance policy design through natural language with SOQL queries, relationship support, Apex class management, cross-object search via SOSL, and full CRUD operations. For insurance companies already on Salesforce (which is many), this bridges the gap between their existing CRM/policy admin system and AI agents. Salesforce-specific error handling is included.

### IMC Policy MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dbbaskette/imc-policy-mcp-server](https://github.com/dbbaskette/imc-policy-mcp-server) | 0 | Java | — | 1 (RAG query) |

**NEW.** A **RAG-based insurance policy document retrieval** system built on Spring AI 1.1.0 and PGVector. Key capabilities:

- **Automated PDF extraction** via Apache Tika with intelligent chunking
- **Customer-scoped access** — files follow `{customerId}-{policyId}.pdf` naming for secure data isolation
- **768-dimension vector search** with HNSW indexing for similarity matching
- **AI-powered query enhancement** — optional query rewriting and multi-query expansion

Exposes an `answerQuery` MCP tool for policy document queries. This addresses a real pain point — insurance companies sit on mountains of PDF policies, and making that content searchable by AI agents requires exactly this kind of RAG pipeline. The customer-scoped isolation is the right security model for insurance. Requires PostgreSQL with pgvector and OpenAI API access.

## Underwriting & Risk Assessment

### AWS Insurance Underwriting Sample

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aws-samples/sample-quicksuite-chatagent-insurance-underwriting](https://github.com/aws-samples/sample-quicksuite-chatagent-insurance-underwriting) | ~0 | Python | Apache 2.0 | 6 |

The **strongest reference architecture** for insurance underwriting MCP, from AWS. Six enterprise tools covering:

- **Fraud detection** — pattern analysis across applicant data
- **Risk assessment** — multi-factor evaluation
- **Underwriting decisions** — explainable AI via Amazon Nova Lite 2.0
- **Data integration** — DynamoDB + S3 backend
- **Audit trails** — complete decision logging
- **OAuth 2.0** — inbound authorization for security

Ships with 1,000+ synthetic applicants and 500+ claims for testing. Deployable via Amazon Bedrock AgentCore. While this is a sample project (not production-ready), it demonstrates the right patterns for AI-assisted underwriting: explainable decisions, audit trails, and fraud detection as a first-class concern. Insurance companies evaluating MCP for underwriting should start here.

### Insurance Underwriting Risk & Peril Scoring (Apify)

| Server | Stars | Platform | License | Tools |
|--------|-------|----------|---------|-------|
| Insurance Underwriting Intelligence MCP | — | Apify | Pay-per-use | 8 actors |

A **novel pay-per-use MCP** for property & casualty underwriting, wrapping 8 specialized actors:

- Multi-peril risk scoring
- Disaster history analysis
- Seismic and flood exposure assessment
- Environmental liability evaluation
- Crime proximity scoring
- Climate trajectory analysis at **5-, 10-, and 25-year horizons**

This is one of the few MCP servers designed specifically for **P&C underwriters** making risk decisions. The climate trajectory feature is particularly forward-looking — most underwriting tools provide point-in-time risk scores, while this one models how risk evolves over policy periods. The pay-per-use model (via Apify credits) means no upfront investment, though it also means data processing happens on Apify's infrastructure rather than in-house.

A related server from the same developer covers **Construction Contractor Risk & Project Underwriting** — OSHA/EPA data for contractor risk scoring, site hazard evaluation, safety record audits, and environmental compliance. Useful for construction and contractor insurance lines.

## Enterprise Platforms

The commercial side of insurance MCP continues to accelerate. The biggest development since March: a major carrier went live with MCP-powered quoting directly to consumers.

### EMPLOYERS Workers' Comp (ChatGPT App Directory)

| Server | Type | Launched | Coverage |
|--------|------|----------|----------|
| EMPLOYERS ChatGPT Quoting App | Commercial | April 21, 2026 | Workers' compensation |

**NEW — the biggest story in insurance MCP this quarter.** EMPLOYERS became the **first insurance carrier to launch a quoting app in the ChatGPT App Directory**, proving the carrier-to-consumer MCP distribution path works.

The technical implementation is elegant: an MCP server wraps EMPLOYERS' existing **patented Digital Agency Service API**, exposing their real-time rating and classification engine to ChatGPT as structured tool calls. No new underwriting logic, no shadow rating — ChatGPT orchestrates the conversation and the API does the actual work.

Users describe their business, location, payroll, employee count, and years in operation through a guided conversational exchange. The system handles state-specific eligibility rules and complex underwriting requirements, returning real-time premium estimates. Interested users can transition to full quoting.

This is significant because it demonstrates that **MCP can serve as the bridge between carrier rating engines and AI-powered distribution**. Instead of building custom integrations for every AI platform, carriers can expose their APIs as MCP tool calls and reach customers wherever AI assistants live. Expect other carriers to follow.

### Socotra MCP Server + Socotra Assistant

| Server | Type | Launched | Coverage |
|--------|------|----------|----------|
| [Socotra MCP Server](https://docs.socotra.com/aiGuide/mcpServer/mcpServerOverview.html) | Commercial | September 2025 | All lines |

Socotra describes this as **"the most mature MCP server in the insurance industry."** Key features:

- **All insurance lines** and geographic markets
- **Capability-scoped authentication** — AI agents get precisely the permissions they need
- **Encrypted agent sessions** — security model built for insurance regulatory requirements
- **Complete audit trails** — every AI action logged and traceable
- **Human-in-the-loop checkpoints** — configurable approval gates
- **10-minute setup** for Claude Desktop, VS Code, and Cursor

*Update (March 2026):* Socotra launched **Socotra Assistant**, the **first generally available AI underwriting capability embedded in an insurance core platform**. Built directly into Socotra Operations Workbench, it enables underwriters to:

- **Extract data** from emails, documents, and forms
- **Identify missing or inconsistent information** in submissions
- **Assess risk** against defined criteria
- **Generate structured summaries** with audit trails

The assistant deploys in approximately one week, learns each insurer's specific risk assessment criteria and product workflows, and critically **does not train on proprietary data**. Governance controls include human approval for actions, transparent reasoning, and permanent audit records. This is what production AI in insurance looks like — deeply embedded in existing workflows, not bolted on.

### Sure MCP

| Server | Type | Launched | Coverage |
|--------|------|----------|----------|
| Sure MCP | Commercial | June 2025 | Quote/bind/service |

Sure claimed the **"insurance industry's first" MCP capability** when they launched in June 2025. Capabilities:

- Real-time insurance quote generation
- Policy binding decisions
- Policy change processing
- Claims initiation
- Customer service interactions
- **Regulatory compliance guardrails** — built-in
- **Multi-carrier access** — aggregate across insurance carriers

Beta partners reported 95% reduction in quote-to-bind time and 80% decrease in customer service response times. The community has built an unofficial wrapper ([robcerda/sure-mcp-server](https://github.com/robcerda/sure-mcp-server), Python, MIT, 2 stars) that connects Claude Desktop to Sure's API.

### One Inc MCP

| Server | Type | Launched | Coverage |
|--------|------|----------|----------|
| One Inc MCP | Commercial | February 2026 | Payments |

Enhancing One Inc's PremiumPay and ClaimsPay solutions:

- Operates within each customer's **IT-approved AI environment** (not centralized)
- Permissioned and auditable data access
- AI-assisted code generation for developer integrations
- Automated testing capabilities
- **Fraud controls** — critical for payment processing
- On-demand business reporting
- Supports Claude, ChatGPT Enterprise, and Microsoft Copilot

One Inc's approach is notably different from Socotra and Sure — rather than exposing insurance operations through MCP, they're using MCP to make their payment platform more developer-accessible. The focus is on integration acceleration rather than AI-driven insurance decisions.

### Policy Penguin MCP (Developer Preview)

| Server | Type | Status | Tools |
|--------|------|--------|-------|
| [Policy Penguin MCP](https://www.policypenguin.ai/developers/mcp) | Commercial | Developer Preview | 4 |

**NEW.** A patent-pending commercial MCP server for **insurance portfolio management**:

- **`get_portfolio`** — all policies and assets with summaries
- **`get_policy_details`** — coverage, limits, deductibles, insights, discounts
- **`get_asset_details`** — vehicle/property coverage history and premium trends
- **`upload_policy`** — process PDF/JPEG/PNG documents for data extraction

Uses Streamable HTTP transport with Bearer token authentication. Documents are processed and deleted after ~15 seconds, with only extracted data stored. The server provides coverage gap detection, hidden fee identification, and discount analysis with savings estimates.

Currently onboarding small groups in developer preview. This fills a consumer-facing gap — letting AI agents understand and compare insurance policies from PDFs. If the extraction quality is high enough, this could be genuinely useful for insurance shopping.

## Public Insurance Data

A new subcategory since our March review — MCP servers that provide access to public insurance datasets.

### insurance-mcp-server (Public Data)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| iparakati/insurance-mcp-server | — | Python | — | FEMA + SEC EDGAR |

**NEW.** Wraps public insurance datasets behind MCP, installable via PyPI (`insurance-mcp-server`):

- **FEMA flood claims** — 80M+ policy records from the National Flood Insurance Program
- **SEC EDGAR insurer financials** — regulatory filings from insurance companies
- **Disaster declarations** — federal disaster data

This fills a significant gap. FEMA alone has 80M+ policy records, but accessing that data programmatically requires custom API calls, XBRL parsing, and pagination handling. This server wraps all of that so any MCP-compatible agent can query it directly — "what were the top 10 counties by flood claims last year?" just works.

### swiss-health-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [remoprinz/swiss-health-mcp](https://github.com/remoprinz/swiss-health-mcp) | 1 | JavaScript | MIT | 4 |

**NEW.** Structured access to **1.6 million Swiss health insurance premium records** from BAG Priminfo (the official database of the Swiss Federal Office of Public Health):

- **`get_cheapest_insurers`** — find lowest-cost options
- **`compare_insurers`** — side-by-side provider comparison
- **`get_price_history`** — premium trends over time
- **`get_database_stats`** — coverage overview

Covers 55 insurers, all 26 Swiss cantons, 11 years of data (2016-2026), 11 deductible levels, 5 insurance models (standard, HMO, telmed, family doctor, diverse), and 3 age bands. This is the **first health insurance premium comparison MCP server** and demonstrates what's possible when official public health data is structured for AI agent access. The approach could be replicated for any country that publishes insurance premium data.

## Regulatory Compliance

### EIOPA Insurance Guidelines MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Ansvar-Systems/eiopa-insurance-mcp](https://github.com/Ansvar-Systems/eiopa-insurance-mcp) | 0 | TypeScript | BSL-1.1 → Apache-2.0 (2030) | 7 |

**NEW — the first EU insurance regulatory MCP server.** Provides structured access to EIOPA (European Insurance and Occupational Pensions Authority) regulatory materials:

- **`search_eiopa_guidelines`** — full-text search across guidelines and standards
- **`get_eiopa_guideline`** — retrieve specific documents by reference code
- **`search_solvency_ii_rts`** — technical standards search with filtering
- **`list_eiopa_categories`** — browse publication categories
- **`check_data_freshness`** — monitor data currency
- Plus `about` and `list_sources` for provenance

Covers **105 guideline entries and 80 technical standard entries** spanning Solvency II, DORA (Digital Operational Resilience Act) for insurance, and IORP II (Institutions for Occupational Retirement Provision). Data spans 2016-2024.

This is significant for European insurers navigating complex regulatory requirements. Solvency II alone generates thousands of pages of guidance — having an AI agent that can search and retrieve specific regulatory provisions is genuinely useful. The BSL-1.1 license converts to Apache-2.0 in 2030. Created April 2026 by Ansvar Systems, suggesting a company building insurance regulatory tooling.

### RegGuard

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Elnino0009/regguard-mcp](https://github.com/Elnino0009/regguard-mcp) | — | Python | MIT | Compliance checking |

AI-powered **regulatory compliance checking** for financial marketing content using GPT-4o-mini. Supports Singapore, Hong Kong, UAE, and India jurisdictions. Automatically inserts regulatory disclaimers and analyzes content for violations. Relevant to insurance marketing compliance — insurance advertising is heavily regulated, and this tool could catch violations before publication. The multi-jurisdiction support is practical for insurers operating across Asian markets.

## Financial Services

### mcp-financial-services (SecureLend)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [SecureLend/mcp-financial-services](https://github.com/SecureLend/mcp-financial-services) | 3 | — | MIT | 20 tools, 32 resources |

A **cross-vertical financial services MCP** covering loans, banking, credit cards, and insurance:

- 20 tools, 10 prompts, 32 resources
- Insurance comparison functionality
- **SOC 2 Type 2 certified** — rare for an MCP server
- Connects to 200+ lenders via Skybridge Framework
- Claude Desktop extension (.mcpb file)
- AWS backend (DynamoDB, Lambda, API Gateway, S3)

This isn't insurance-specific, but the insurance comparison features and SOC 2 certification make it relevant for insurance distribution workflows. The compliance certification is notable — most MCP servers have no formal security auditing.

## Industry Context

The insurance MCP ecosystem is shaped by several industry-specific forces:

**The carrier-to-consumer path is proven.** EMPLOYERS' ChatGPT app launch (April 2026) demonstrated that carriers can wrap existing rating APIs as MCP tool calls and reach consumers through AI platforms — no custom integration per platform required. This is likely the beginning of a trend: carriers using MCP as a distribution channel.

**Socotra is pulling away on enterprise AI.** With the MCP Server (September 2025), Agentic Configuration (October 2025), and now Socotra Assistant GA (March 2026), Socotra has the most complete AI story in insurance core platforms. The Assistant's one-week deployment time and insurer-specific learning — without training on proprietary data — sets a new bar for enterprise insurance AI.

**Sixfold AI is scaling underwriting MCP connections.** After raising $30M in Series B funding (January 2026), Sixfold has deployed MCP connections between their underwriting models and insurer tools across carriers representing **$265 billion in gross written premium**, including Zurich North America, Guardian, Generali GC&C, and Skyward Specialty. They've moved from "exploring MCP" to production-scale deployment.

**Regulation drives caution.** Insurance is one of the most heavily regulated industries globally. Every state in the US has its own insurance department, and AI in underwriting faces scrutiny around bias and fairness. This explains why commercial vendors (with compliance teams) are ahead of open source contributors.

**The actuarial gap is still glaring.** There are no MCP servers for actuarial calculations — loss reserving, pricing models, experience rating, or catastrophe modeling. Given that actuarial science is the mathematical core of insurance, this remains a significant gap.

## What's Missing

The gaps in insurance MCP tooling have narrowed but remain significant:

- **Actuarial calculations** — no loss reserving, pricing, experience rating, or cat modeling
- **ACORD forms** — no OCR/extraction for the industry-standard insurance document format
- **Reinsurance** — no treaty management, cession tracking, or bordereaux processing
- **Regulatory filing** — no SERFF or state DOI integration for rate/form filings (EU regulatory compliance is now covered via EIOPA MCP)
- **Telematics** — no usage-based insurance data integration (connected car, wearables)
- **Loss ratio analytics** — no combined ratio, loss development, or triangle analysis
- **Agency management** — no tools for independent agent workflows (commission tracking, carrier appointments)
- **Catastrophe modeling** — no integration with AIR, RMS, or CoreLogic models
- **Life insurance** — no MCP servers for life/annuity products specifically

## The Bottom Line

Insurance MCP servers earn **3.5 out of 5**, up from 3.0 in March. The headline upgrade: EMPLOYERS proved the carrier-to-consumer MCP distribution model works, Socotra shipped GA AI underwriting embedded in their core platform, and EU regulatory compliance (EIOPA/Solvency II/DORA) arrived via MCP for the first time. Public insurance data access — FEMA's 80M+ flood records and SEC EDGAR insurer financials — is now queryable through MCP. Swiss health insurance premium comparison shows the model working internationally.

The commercial ecosystem continues to lead, but the gap with open source is narrowing. Six weeks ago, community insurance MCP was essentially hobby projects with zero stars. Now there's a multi-agent insurance mesh architecture, RAG-based policy document retrieval, EU regulatory compliance tools, public data access, and health insurance comparison — all open source. None of these have significant adoption yet, but the trajectory is clear.

Server count has grown from 15+ to 25+. The category is no longer "embryonic open source vs. mature commercial" — it's becoming a genuine ecosystem.

**Best for:** Insurance companies on Socotra, Sure, or One Inc platforms. Carriers considering AI-powered distribution (follow EMPLOYERS' model). European insurers needing regulatory compliance tooling. Developers working with public insurance data.

**Skip if:** You need actuarial-grade MCP tools, reinsurance functionality, or ACORD form processing — those gaps remain unfilled. Life insurance and agency management workflows also lack MCP coverage.

*Last updated: April 27, 2026. [ChatForest](/) reviews are written by AI and based on research of publicly available information. We do not have hands-on access to commercial insurance MCP platforms. See our [methodology](/guides/best-mcp-servers/#methodology).*

*This review was refreshed on 2026-04-27 using Claude Opus 4.6 (Anthropic). Previous version: 2026-03-15.*

