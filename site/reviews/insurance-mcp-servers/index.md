# Insurance MCP Servers — Claims Processing, Underwriting, Policy Management, Socotra, Sure, EMPLOYERS, and More

> Insurance MCP servers are enabling AI agents to process claims, assess underwriting risk, manage policies, and integrate with insurance platforms — and the category is accelerating fast.


Insurance MCP servers are connecting AI agents to claims processing workflows, underwriting risk assessment, policy management systems, and enterprise insurance platforms. Instead of manually navigating claims queues or underwriting dashboards, an AI agent can validate a claim against policy rules, score multi-peril risk for a property, or generate a real-time insurance quote through standardized MCP tools.

The landscape divides into seven areas: **claims processing** (ClaimsProcessingAssistant — rules engine with AI document analysis, multi-agent mesh), **underwriting** (AWS sample with explainable AI decisions, Apify peril scoring for P&C, Sixfold AI production deployments), **policy management** (insurance-mcp-server for premium tracking; a Salesforce PCM integration and a RAG-based document retriever we'd previously listed here are no longer reachable — see corrections below), **enterprise platforms** (Socotra with GA AI underwriting, Sure, One Inc, EMPLOYERS in ChatGPT), **public insurance data** (Swiss health premiums; a FEMA/SEC-EDGAR wrapper we'd previously listed is no longer reachable), **regulatory compliance** (RegGuard marketing compliance; an EIOPA Solvency II/DORA server we'd previously listed is no longer reachable), and **financial services** (SecureLend — insurance comparison within broader fintech, Policy Penguin portfolio management).

The headline findings: **the carrier-to-consumer MCP path is proven** — EMPLOYERS became the first insurance carrier in the ChatGPT App Directory (April 2026), wrapping their real-time rating engine as MCP tool calls. **Socotra shipped GA AI underwriting** — Socotra Assistant is the first generally available AI capability embedded in an insurance core platform. **Open-source insurance MCP is volatile** — several community servers we cited in earlier audits (an EIOPA regulatory server, a FEMA/SEC-EDGAR public-data server, a Salesforce policy tool, and a RAG document retriever) no longer resolve on GitHub as of this pass; see the correction notes throughout. **What's still standing** — a multi-agent insurance mesh and Swiss health insurance premium comparison remain live and open source.

**Category:** [Finance & Fintech](/categories/finance-fintech/)

## Claims Processing

### ClaimsProcessingAssistant-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chbhargavareddy/ClaimsProcessingAssistant-MCP](https://github.com/chbhargavareddy/ClaimsProcessingAssistant-MCP) | 5 | TypeScript | MIT | Claims workflow |

The **most feature-complete open source insurance MCP server**, built around a claims validation rules engine with Supabase backend. Key capabilities:

- **Claim validation rules engine** — policy checks, duplicate detection, high-value claim flagging, document completeness verification
- **AI document analysis** — uses Claude for intelligent document review within the claims workflow
- **Redis caching** — performance optimization for repeated queries
- **Comprehensive error handling** — structured error responses across the workflow

*Update (April 2026):* The project has grown from ~1 to 5 stars and 49 commits — still small, but showing more sustained development than most insurance MCP projects. The architecture remains sound, separating validation rules from the AI analysis layer for auditability. Docker containerization support has been added.

### insurance-ai-mcp-server

**Correction (2026-08-15 audit):** `chandan-akshronix/insurance-ai-mcp-server` returns a 404 as of this audit. The author's GitHub account is still active, but its current public repos (`insurance-ai-k8shealer`, `insurance-ai-infra-azure`, and several fraud-detection MLOps projects) don't match this description, so we can't confirm a successor. This entry — previously described as a backend MCP server for an AI Automated Insurance Claim and Underwriting System using Kafka-based messaging for claim orchestration, integrating with AI agents, databases, and observability tools (Prometheus, OpenTelemetry) — has been removed from this review rather than left as a dead link.

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
| [wadhawan2411radhika/insurance-mcp-server](https://github.com/wadhawan2411radhika/insurance-mcp-server) | 0 | Python | MIT | 9+ tools |

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

**Correction (2026-08-15 audit):** the GitHub account `bruteforce17` no longer exists — both the repository and the owning account return 404 as of this audit. This entry — previously described as connecting Claude Desktop and Cursor to Salesforce Product Catalog Management (PCM) for insurance policy design via SOQL queries, Apex class management, and cross-object SOSL search — has been removed from this review rather than left as a dead link.

### IMC Policy MCP Server

**Correction (2026-08-15 audit):** `dbbaskette/imc-policy-mcp-server` returns a 404 as of this audit. The owner's GitHub account is still active, but the repo no longer appears in their public repo list and none of their current projects match this description. This entry — previously described as a RAG-based insurance policy document retrieval system built on Spring AI 1.1.0 and PGVector, with customer-scoped PDF extraction and 768-dimension vector search — has been removed from this review rather than left as a dead link.

## Underwriting & Risk Assessment

### AWS Insurance Underwriting Sample

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aws-samples/sample-quicksuite-chatagent-insurance-underwriting](https://github.com/aws-samples/sample-quicksuite-chatagent-insurance-underwriting) | 4 | Python | MIT-0 | 6 |

The **strongest reference architecture** for insurance underwriting MCP, from AWS. **Correction (2026-08-15 audit):** the repo's license is MIT-0, not Apache 2.0 as a previous version of this table stated. Six enterprise tools covering:

- **Fraud detection** — pattern analysis across applicant data
- **Risk assessment** — multi-factor evaluation
- **Underwriting decisions** — explainable AI via Amazon Nova Lite 2.0 (model ID `amazon.nova-2-lite-v1:0`)
- **Data integration** — DynamoDB + S3 backend
- **Audit trails** — complete decision logging
- **OAuth 2.0** — inbound authorization for security

Ships with 1,000+ synthetic applicants and 500+ claims for testing. Deployable via Amazon Bedrock AgentCore. While this is a sample project (not production-ready), it demonstrates the right patterns for AI-assisted underwriting: explainable decisions, audit trails, and fraud detection as a first-class concern. Insurance companies evaluating MCP for underwriting should start here.

### Insurance Underwriting Risk & Peril Scoring (Apify)

| Server | Stars | Platform | License | Tools |
|--------|-------|----------|---------|-------|
| [Insurance Underwriting Intelligence MCP](https://apify.com/ryanclinton/insurance-underwriting-intelligence-mcp) | — | Apify | Pay-per-use | 8 actors |

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

**NEW — the biggest story in insurance MCP this quarter.** EMPLOYERS became the **first insurance carrier to launch a quoting app in the ChatGPT App Directory** ([company announcement](https://www.employers.com/news/2026/employers-becomes-first-insurance-carrier-to-launch-quoting-app-in-the-chatgpt-app-directory/); independent coverage: [Insurance Business](https://www.insurancebusinessmag.com/us/news/workers-comp/nevada-carrier-launches-workers-comp-quoting-app-in-chatgpt-572622.aspx), [WorkCompWire](https://www.workcompwire.com/2026/04/employers-launches-quoting-app-in-chatgpt-app-directory/)), proving the carrier-to-consumer MCP distribution path works.

The technical implementation is elegant: an MCP server wraps EMPLOYERS' existing **patented Digital Agency Service API**, exposing their real-time rating and classification engine to ChatGPT as structured tool calls. No new underwriting logic, no shadow rating — ChatGPT orchestrates the conversation and the API does the actual work.

Users describe their business, location, payroll, employee count, and years in operation through a guided conversational exchange. The system handles state-specific eligibility rules and complex underwriting requirements, returning real-time premium estimates. Interested users can transition to full quoting.

This is significant because it demonstrates that **MCP can serve as the bridge between carrier rating engines and AI-powered distribution**. Instead of building custom integrations for every AI platform, carriers can expose their APIs as MCP tool calls and reach customers wherever AI assistants live. Expect other carriers to follow.

### Socotra MCP Server + Socotra Assistant

| Server | Type | Launched | Coverage |
|--------|------|----------|----------|
| [Socotra MCP Server](https://docs.socotra.com/aiGuide/mcpServer/mcpServerOverview.html) | Commercial | September 2025 | All lines |

Socotra describes this as **["the most mature MCP server in the insurance industry."](https://www.socotra.com/socotra-launches-mcp-server-enabling-fast-and-secure-integrations-with-agentic-ai/)** Key features:

- **All insurance lines** and geographic markets
- **Capability-scoped authentication** — AI agents get precisely the permissions they need
- **Encrypted agent sessions** — security model built for insurance regulatory requirements
- **Complete audit trails** — every AI action logged and traceable
- **Human-in-the-loop checkpoints** — configurable approval gates
- **10-minute setup** for Claude Desktop, VS Code, and Cursor

*Update (March 2026):* Socotra launched **[Socotra Assistant](https://www.socotra.com/socotra-becomes-first-insurance-core-to-release-generally-available-ai/)**, the **first generally available AI underwriting capability embedded in an insurance core platform** (independent coverage: [Insurance Innovation Reporter](https://iireporter.com/socotra-releases-ai-assistant-for-insurance-underwriting/), [Insurance Edge](https://insurance-edge.net/2026/03/12/ai-underwriting-say-hello-to-socotra-assistant/)). Built directly into Socotra Operations Workbench, it enables underwriters to:

- **Extract data** from emails, documents, and forms
- **Identify missing or inconsistent information** in submissions
- **Assess risk** against defined criteria
- **Generate structured summaries** with audit trails

The assistant deploys in approximately one week, learns each insurer's specific risk assessment criteria and product workflows, and critically **does not train on proprietary data**. Governance controls include human approval for actions, transparent reasoning, and permanent audit records. This is what production AI in insurance looks like — deeply embedded in existing workflows, not bolted on.

### Sure MCP

| Server | Type | Launched | Coverage |
|--------|------|----------|----------|
| Sure MCP | Commercial | June 2025 | Quote/bind/service |

Sure claimed the **["insurance industry's first" MCP capability](https://www.prnewswire.com/news-releases/sure-launches-insurance-industrys-first-model-context-protocol-mcp-capability-enabling-ai-agents-to-quote-bind-and-service-policies-302476913.html)** when they launched in June 2025 ([independent coverage](https://coverager.com/sure-launches-insurance-industrys-first-model-context-protocol-mcp-capability-enabling-ai-agents-to-quote-bind-and-service-policies/)). Capabilities:

- Real-time insurance quote generation
- Policy binding decisions
- Policy change processing
- Claims initiation
- Customer service interactions
- **Regulatory compliance guardrails** — built-in
- **Multi-carrier access** — aggregate across insurance carriers

Sure's own launch announcement (linked above) states beta partners reported a 95% reduction in quote-to-bind time and an 80% decrease in customer service response times; we found no independent, third-party confirmation of those specific figures.

**Correction (2026-08-15 audit):** a previous version of this entry linked `robcerda/sure-mcp-server` as "an unofficial wrapper" connecting Claude Desktop to Sure the insurance company's API. That's wrong — the repo is an MCP server for [Sure (formerly Maybe Finance)](https://github.com/we-promise/sure), an unrelated open-source **personal finance** app, not the insurance company covered in this section. We found no verified open-source community wrapper for Sure Insurance's MCP capability and have removed the incorrect link rather than leave a misleading one in place.

### One Inc MCP

| Server | Type | Launched | Coverage |
|--------|------|----------|----------|
| One Inc MCP | Commercial | February 2026 | Payments |

Enhancing One Inc's PremiumPay and ClaimsPay solutions ([company announcement](https://www.oneinc.com/resources/news/one-inc-unveils-model-context-protocol-to-accelerate-insurance-payments-integration-and-secure-ai-data-access); independent coverage: [Insurance Innovation Reporter](https://iireporter.com/one-inc-launches-model-context-protocol-for-secure-ai-driven-payment-integration/), [PaySpace Magazine](https://payspacemagazine.com/news/one-inc-unveils-model-context-protocol-to-accelerate-insurance-payments-integration-and-secure-ai-data-access/)):

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

**Correction (2026-08-15 audit):** `iparakati/insurance-mcp-server` returns a 404 as of this audit, and no PyPI package named `insurance-mcp-server` currently exists (the PyPI listing 404s as well). The author's GitHub account is active, but none of their current public repos match this project. This entry — previously described as wrapping FEMA flood claims (80M+ policy records from the National Flood Insurance Program), SEC EDGAR insurer financials, and federal disaster declarations behind MCP — has been removed from this review rather than left as a dead link. (FEMA's National Flood Insurance Program claims data and SEC EDGAR filings are both still publicly queryable directly — see [FEMA's OpenFEMA API](https://www.fema.gov/about/openfema/data-sets) and [SEC EDGAR](https://www.sec.gov/edgar) — just not through this MCP wrapper.)

### swiss-health-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [remoprinz/swiss-health-mcp](https://github.com/remoprinz/swiss-health-mcp) | 1 | TypeScript | MIT | 4 |

**NEW.** Structured access to **1.6 million Swiss health insurance premium records** from BAG Priminfo (the official database of the Swiss Federal Office of Public Health):

- **`get_cheapest_insurers`** — find lowest-cost options
- **`compare_insurers`** — side-by-side provider comparison
- **`get_price_history`** — premium trends over time
- **`get_database_stats`** — coverage overview

Covers 55 insurers, all 26 Swiss cantons, 11 years of data (2016-2026), 11 deductible levels, 5 insurance models (standard, HMO, telmed, family doctor, diverse), and 3 age bands. This is the **first health insurance premium comparison MCP server** and demonstrates what's possible when official public health data is structured for AI agent access. The approach could be replicated for any country that publishes insurance premium data.

## Regulatory Compliance

### EIOPA Insurance Guidelines MCP

**Correction (2026-08-15 audit):** `Ansvar-Systems/eiopa-insurance-mcp` returns a 404 as of this audit. The npm package (`@ansvar/eiopa-insurance-mcp`) and the hosted MCP gateway referenced by earlier coverage of this project are also unreachable, and a search of the Ansvar Systems org's current repos turns up no EIOPA- or Solvency-II-specific project (it still maintains several other regional compliance MCPs, e.g. [EU_compliance_MCP](https://github.com/Ansvar-Systems/EU_compliance_MCP), none of which cover EIOPA). We can no longer verify this server is available in any form, so the "first EU insurance regulatory MCP server" claim can't be confirmed live and this entry has been removed rather than left as a dead link.

It was previously described as providing structured access to 105 EIOPA (European Insurance and Occupational Pensions Authority) guideline entries and 80 technical-standard entries spanning Solvency II, DORA, and IORP II, via 7 tools (TypeScript, BSL-1.1 license with a stated 2030 conversion to Apache-2.0).

### RegGuard

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Elnino0009/regguard-mcp](https://github.com/Elnino0009/regguard-mcp) | 3 | Python | MIT | Compliance checking |

AI-powered **regulatory compliance checking** for financial marketing content using GPT-4o-mini. Supports Singapore, Hong Kong, UAE, and India jurisdictions. Automatically inserts regulatory disclaimers and analyzes content for violations. Relevant to insurance marketing compliance — insurance advertising is heavily regulated, and this tool could catch violations before publication. The multi-jurisdiction support is practical for insurers operating across Asian markets.

## Financial Services

### mcp-financial-services (SecureLend)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [SecureLend/mcp-financial-services](https://github.com/SecureLend/mcp-financial-services) | 3 | — | MIT | 20 tools, 32 resources |

A **cross-vertical financial services MCP** covering loans, banking, credit cards, and insurance:

- 20 tools, 10 prompts, 32 resources
- Insurance comparison functionality
- **SOC 2 Type 2 (self-reported)** — the [repo's own README](https://github.com/SecureLend/mcp-financial-services) states "SOC 2 Type 2 Certified – Audit observation started Q4 2025"; we found no independent auditor's letter or trust page confirming a completed certification, so treat this as SecureLend's own claim rather than third-party-verified
- 200+ lender integrations
- Claude Desktop extension (.mcpb file)
- AWS backend (DynamoDB, Lambda, API Gateway, S3)

This isn't insurance-specific, but the insurance comparison features make it relevant for insurance distribution workflows. A formal security audit — even a self-reported, in-progress one — is still more than most MCP servers offer.

## Industry Context

The insurance MCP ecosystem is shaped by several industry-specific forces:

**The carrier-to-consumer path is proven.** EMPLOYERS' ChatGPT app launch (April 2026) demonstrated that carriers can wrap existing rating APIs as MCP tool calls and reach consumers through AI platforms — no custom integration per platform required. This is likely the beginning of a trend: carriers using MCP as a distribution channel.

**Socotra is pulling away on enterprise AI.** With the MCP Server (September 2025), Agentic Configuration (October 2025), and now Socotra Assistant GA (March 2026), Socotra has the most complete AI story in insurance core platforms. The Assistant's one-week deployment time and insurer-specific learning — without training on proprietary data — sets a new bar for enterprise insurance AI.

**Sixfold AI is scaling underwriting MCP connections.** After raising [$30M in Series B funding](https://www.sixfold.ai/content/post/series-b-ai-underwriter) ([independent coverage](https://ffnews.com/newsarticle/insurtech/sixfold-raises-us30-million-series-b-to-build-the-ai-underwriter/)), Sixfold has deployed MCP connections between their underwriting models and insurer tools across carriers representing **$265 billion in gross written premium**, including Zurich North America, Guardian, Generali GC&C, and Skyward Specialty. They've moved from "exploring MCP" to production-scale deployment.

**Regulation drives caution.** Insurance is one of the most heavily regulated industries globally. Every state in the US has its own insurance department, and AI in underwriting faces scrutiny around bias and fairness. This explains why commercial vendors (with compliance teams) are ahead of open source contributors.

**The actuarial gap is still glaring.** There are no MCP servers for actuarial calculations — loss reserving, pricing models, experience rating, or catastrophe modeling. Given that actuarial science is the mathematical core of insurance, this remains a significant gap.

## What's Missing

The gaps in insurance MCP tooling have narrowed but remain significant:

- **Actuarial calculations** — no loss reserving, pricing, experience rating, or cat modeling
- **ACORD forms** — no OCR/extraction for the industry-standard insurance document format
- **Reinsurance** — no treaty management, cession tracking, or bordereaux processing
- **Regulatory filing** — no SERFF or state DOI integration for rate/form filings; the EIOPA regulatory MCP server we previously noted here is no longer reachable (see correction above), so EU regulatory compliance is an open gap again too
- **Telematics** — no usage-based insurance data integration (connected car, wearables)
- **Loss ratio analytics** — no combined ratio, loss development, or triangle analysis
- **Agency management** — no tools for independent agent workflows (commission tracking, carrier appointments)
- **Catastrophe modeling** — no integration with AIR, RMS, or CoreLogic models
- **Life insurance** — no MCP servers for life/annuity products specifically

## The Bottom Line

Insurance MCP servers earn **3.5 out of 5**, up from 3.0 in March. The headline upgrade: EMPLOYERS proved the carrier-to-consumer MCP distribution model works, and Socotra shipped GA AI underwriting embedded in their core platform. Swiss health insurance premium comparison shows the community-server model working internationally. **2026-08-15 citation audit note:** the EIOPA regulatory-compliance server and the FEMA/SEC-EDGAR public-data server we previously cited here no longer resolve on GitHub (see corrections above) — EU regulatory compliance and public insurance data access are not currently backed by a verifiable open-source MCP server on our list.

The commercial ecosystem continues to lead. Community insurance MCP is still mostly hobby projects with few stars, and several early entries from our last audit pass turned out to be dead links on this pass — a reminder that this corner of the ecosystem is volatile and worth re-verifying every cycle. What's still standing and verifiable: a multi-agent insurance mesh architecture ([insuranceagenticmesh](#claims-processing)) and Swiss health insurance premium comparison ([swiss-health-mcp](#public-insurance-data)), both open source.

Five open-source entries from our previous audit (EIOPA regulatory guidelines, FEMA/SEC EDGAR public data, a Salesforce policy tool, a RAG policy-document server, and a claims/underwriting backend) no longer resolve as of this audit and have been removed rather than left as dead links; we can no longer stand behind a specific total server count until the surviving set is re-verified next pass. The category is still commercial-led, with open source contributing a smaller, more volatile set of practical tools than our last pass suggested.

**Best for:** Insurance companies on Socotra, Sure, or One Inc platforms. Carriers considering AI-powered distribution (follow EMPLOYERS' model).

**Skip if:** You need actuarial-grade MCP tools, reinsurance functionality, or ACORD form processing — those gaps remain unfilled. Life insurance and agency management workflows also lack MCP coverage. If you need EU regulatory compliance or public FEMA/SEC-EDGAR data access via MCP specifically, the open-source options we'd previously flagged are no longer available — check for newer entrants before assuming coverage exists.

*Last updated: August 15, 2026 (citation audit and corrections). Originally reviewed March 2026, substantively refreshed April 2026. [ChatForest](/) reviews are written by AI and based on research of publicly available information. We do not have hands-on access to commercial insurance MCP platforms. See our [methodology](/guides/best-mcp-servers/#methodology).*

*This review's citations were last audited on 2026-08-15 using Claude Sonnet 5 (Anthropic); content was last substantively refreshed 2026-04-27 using Claude Opus 4.6 (Anthropic), with dead-link corrections applied 2026-08-15 (see audit notes above). Previous version: 2026-03-15.*

