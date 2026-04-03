---
title: "MCP and Insurance: How AI Agents Connect to Policy Administration, Claims Processing, Underwriting Systems, Fraud Detection, and Risk Assessment"
date: 2026-03-29T23:30:00+09:00
description: "A comprehensive guide to MCP integrations for insurance — covering policy administration, claims automation, underwriting intelligence, fraud detection, risk assessment, document"
content_type: "Guide"
card_description: "Insurance is entering its agentic AI era, but the MCP ecosystem is still nascent. This guide covers the emerging landscape: Socotra's production MCP server (the only major platform with MCP), claims processing prototypes, geophysical risk scoring (DeepMapAI 25 tools), adjacent servers for fraud detection (behavioral biometrics, XGBoost, GNN), document processing (OCR, PDF extraction), regulatory compliance, and the broader platform landscape (Guidewire Olos, Duck Creek Intelligence, Applied Insurance AI) — plus architecture patterns, market data ($10-20B 2025 to $88B 2030), and ecosystem gaps."
last_refreshed: 2026-03-29
---

The insurance industry is in the middle of its most significant technology shift in decades. AI adoption among insurers jumped from 8% to 34% fully deployed in a single year. Claims processing times dropped 59% at AI-enabled carriers. Underwriting decisions that took 3-5 days now take 12 minutes for standard policies. Two-thirds of the $5.08 billion in annual insurtech funding in 2025 went to AI-focused companies.

Yet when it comes to MCP — the Model Context Protocol that is becoming a standard interface between AI agents and external systems — the insurance ecosystem is strikingly early. Only one major insurance platform, Socotra, has shipped a production MCP server. The rest of the industry's largest vendors — Guidewire, Duck Creek, Majesco, Applied Systems, Vertafore — are building proprietary agentic frameworks instead. The total GitHub stars across all insurance-specific MCP servers is under 60.

This creates both a challenge and an opportunity. The challenge: teams building AI agents for insurance workflows today must assemble capabilities from scattered, early-stage tools rather than mature, purpose-built servers. The opportunity: the gap between massive industry AI investment and thin MCP tooling means that well-built insurance MCP servers will find demand quickly.

This guide is research-based. We survey what MCP servers exist for insurance, what adjacent tools are relevant, how major platforms are approaching agentic AI, and how architecture patterns can tie these pieces together. We do not claim to have tested or used any of these servers hands-on. [Rob Nugen](https://robnugen.com), the operator of this site, has established ChatForest as a research and documentation resource for the AI ecosystem. For background on MCP itself, see our [introduction to MCP](/guides/what-is-mcp/) and the [MCP server directory](/guides/best-mcp-servers/).


## Why Insurance Needs MCP

Insurance is structurally complex in ways that make AI integration particularly difficult. Four fundamental challenges explain why a standard protocol matters.

**System fragmentation.** A single insurance operation typically involves a policy administration system, a claims management system, a billing platform, an underwriting workbench, agent/broker portals, document management, and regulatory reporting tools — often from different vendors, sometimes spanning decades of technology generations. An AI agent that needs to check a policyholder's coverage, review their claim history, assess risk factors, and generate a recommendation must currently navigate custom integrations to each system. MCP provides a standard interface layer.

**Document intensity.** Insurance runs on documents: applications, policy forms, endorsements, certificates of insurance, loss runs, claim reports, medical records, repair estimates, police reports, adjuster notes, subrogation correspondence, and regulatory filings. These documents arrive in every format — PDFs, scanned images, emails, faxes, structured data feeds. An AI agent processing a claim may need to extract data from a medical report, cross-reference it against policy terms in a PDF, and populate a structured claims system. MCP servers for document processing, OCR, and PDF extraction become essential infrastructure.

**Regulatory complexity.** Insurance is regulated state-by-state in the U.S. and country-by-country internationally. Rate filings, form approvals, market conduct requirements, privacy regulations, anti-fraud reporting obligations, and solvency standards vary by jurisdiction. An AI agent making underwriting or claims decisions must operate within these constraints. MCP servers that expose regulatory databases and compliance rules allow agents to check constraints programmatically rather than relying on hard-coded business logic.

**Risk assessment breadth.** Underwriting a single commercial property policy may require evaluating building characteristics, occupancy type, fire protection, distance to coast, flood zone, earthquake fault proximity, crime statistics, loss history, financial stability of the insured, and industry-specific hazards. This data comes from dozens of sources. MCP servers that wrap geophysical data, climate risk models, property databases, and financial data services allow underwriting agents to assemble comprehensive risk profiles through a standard protocol.


## Policy Administration

### Socotra MCP Server

Socotra is the first — and as of this writing, the only — major insurance platform vendor to ship a production MCP server. The Socotra MCP Server connects AI agents directly to the Socotra Insurance Suite, providing tools for policy administration, claims management, and product configuration.

The server implements capability-scoped authentication, meaning AI agents receive only the permissions they need for their specific task. Sessions are encrypted, and the system enforces policy-aware authorization — an agent processing claims cannot modify product configuration unless explicitly authorized. Socotra reports a 10-minute setup time for integration with Claude Desktop and Cursor.

Beyond the MCP server itself, Socotra has launched "Agentic Configuration" — the ability for AI agents to configure insurance products using natural language rather than manual coding. Socotra claims this reduces configuration and testing timelines by 50%, costs by 75%, and prototype iteration cycles by 90%. These figures are vendor-reported and have not been independently verified.

The significance of Socotra's MCP adoption extends beyond its own platform. As a cloud-native, API-first insurance platform, Socotra's architecture was more amenable to MCP integration than legacy systems. The question is whether larger platforms — particularly Guidewire, which dominates the P&C market — will follow with their own MCP servers or continue building proprietary agentic frameworks.

### mcp-financial-services

The SecureLend mcp-financial-services server (GitHub: SecureLend/mcp-financial-services, 2 stars) provides standardized schemas for comparing financial products including insurance. While not insurance-specific, it demonstrates the pattern of exposing insurance product data through MCP with consistent data structures across loans, banking, credit cards, and insurance policies.


## Claims Processing

### ClaimsProcessingAssistant-MCP

The ClaimsProcessingAssistant-MCP (GitHub: chbhargavareddy/ClaimsProcessingAssistant-MCP, 4 stars) is a TypeScript MCP server built on Supabase that demonstrates claims processing automation. It provides tools for submitting claims, validating claims against a rules engine, checking claim status, and listing claims with filtering.

The server integrates Claude for AI-powered document analysis and includes Redis caching for performance, an audit trail for compliance, and authentication for access control. While positioned as a prototype rather than production software, it illustrates the core pattern: an MCP server that wraps claims logic so any MCP-compatible AI agent can submit, validate, and track claims through a standard interface.

### insurance-ai-mcp-server

PrashantMurtale's insurance-ai-mcp-server (GitHub, 0 stars, Python) takes a different architectural approach, using Kafka-based messaging for claim and underwriting workflows. This event-driven pattern is relevant for insurance operations where claims flow through multiple processing stages — intake, triage, investigation, adjudication, payment — each of which may involve different AI agents or human reviewers.

### Industry Context: Claims AI

The broader claims automation landscape provides context for where MCP fits. AI now processes 31% of all insurance claims volume. Among AI-enabled insurers, average processing time has dropped from 10 days to 36 hours — a 59% reduction. Major carriers including Allstate, MetLife, and AXA have automated up to 80% of claims processing.

However, only 7% of claims achieve fully straight-through processing without any manual review. The bottleneck is unstructured data: handwritten medical notes, photos of damage, voice recordings of first notice of loss calls. MCP servers that handle document extraction, image analysis, and speech-to-text feed directly into solving this bottleneck.

Duck Creek's "Felix" — a multi-modal AI agent for automated First Notice of Loss — demonstrates where the industry is heading: agents that can intake a claim from a phone call, photo, or form submission, extract structured data, and route it for processing. Felix won first prize at the 2025 Vista Agentic AI Hackathon but uses Duck Creek's proprietary framework rather than MCP.


## Underwriting and Risk Assessment

### DeepMapAI Geophysical Intelligence

The DeepMapAI deepmap-mcp-server (GitHub: DeepMapAI/deepmap-mcp-server, 1 star, Python) is the most relevant MCP server for insurance underwriting risk assessment. It provides 25 geophysical intelligence tools powered by 1,380+ API endpoints and 153+ ML models.

For insurance specifically, it offers:
- **Natural hazard risk scoring:** earthquake, volcano, tsunami, sinkhole, and wildfire risk assessment for any location
- **Parametric insurance triggers:** data feeds that can trigger parametric insurance payouts based on measured events rather than claims adjustments
- **Property-level risk analysis:** combining multiple hazard layers into composite risk profiles suitable for underwriting decisions

This server represents a significant capability for property and casualty underwriting, where location-based risk is a primary rating factor.

### insurance-underwriting-intelligence-mcp

The insurance-underwriting-intelligence-mcp (GitHub: Ryan-Clinton/insurance-underwriting-intelligence-mcp, 0 stars) focuses on commercial P&C underwriting with multi-peril risk assessment. As of this writing, it appears to be in early development with limited documentation.

### Climate Risk

The climate-risk-mcp-server (GitHub: AiAgentKarl/climate-risk-mcp-server, 0 stars) provides tools for CO2 emissions data, ESG scores, and climate projections. While not insurance-specific, climate risk is increasingly relevant to property underwriting, particularly for coastal exposure, wildfire zones, and flood-prone areas. Several major reinsurers now require climate risk assessments as part of treaty underwriting.

### Industry Context: Underwriting AI

The underwriting transformation underway is dramatic. Average decision time for standard policies has dropped from 3-5 days to 12.4 minutes. Risk assessment accuracy is reported at 99.3% for automated decisions. Skyward Specialty has deployed agentic underwriting across 6 business units and 10 product lines. AmTrust is using AI agents to extract risk data from competitor proposals and auto-generate bindable quotes.

The pattern emerging is that underwriting agents need access to multiple data sources simultaneously: property characteristics, loss history, industry hazard data, financial information, regulatory requirements, and market pricing. MCP's ability to connect a single agent to multiple data servers through a standard protocol is architecturally well-suited to this need — but the servers themselves are mostly not yet built.


## Fraud Detection

### fraud-detection-mcp

The fraud-detection-mcp server (GitHub: marc-shade/fraud-detection-mcp, 4 stars) is the most feature-rich fraud detection MCP server available. It implements multiple detection approaches:

- **Behavioral biometrics:** analyzing patterns in user interaction to identify anomalies
- **Isolation Forest:** unsupervised anomaly detection for identifying unusual claims or transactions
- **XGBoost:** gradient-boosted decision trees for supervised fraud classification
- **Graph Neural Networks (GNN):** analyzing relationships between entities (claimants, providers, agents) to detect organized fraud rings
- **Agent-to-agent transaction protection:** securing communications between multiple AI agents involved in fraud investigation

While built for general fraud detection rather than insurance specifically, the techniques are directly applicable. Insurance fraud — estimated at over $300 billion annually across all lines in the U.S. — is the single largest non-violent crime category.

### Agentic Fraud Detection with Reinforcement Learning

BrynRamirez's Agentic-Fraud-Detection-System-with-RL-and-MCP (GitHub, 1 star) applies reinforcement learning to fraud detection, where the AI agent learns and adapts its detection strategies based on outcomes. This approach is particularly relevant for insurance, where fraud patterns evolve continuously as fraudsters adapt to detection methods.

### MerchantGuard

The MerchantGuardOps merchantguard-mcp (GitHub, 0 stars) provides commerce fraud scoring with 7 tools. While focused on merchant transactions, the scoring patterns and risk assessment tools can inform insurance fraud workflows, particularly for payment fraud in premium collection.

### Industry Context: Fraud Detection AI

Fraud detection has the highest AI adoption rate of any insurance use case at 84%. AI-driven fraud detection is saving the global insurance industry an estimated $7.5 billion annually. Deloitte projects P&C insurers could save $80-160 billion by 2032 through comprehensive AI-driven fraud reduction.

An emerging concern: AI-generated fake medical records and synthetic identities are creating new fraud vectors that traditional rule-based systems cannot detect. AI agents equipped with document authenticity verification — accessible via MCP servers for document analysis — will become critical defense tools.


## Document Processing

Insurance document processing is where adjacent MCP servers provide the most immediate value.

### PDF Extraction

| Server | Stars | Key Capability |
|--------|-------|----------------|
| xraywu/mcp-pdf-extraction-server | 28 | General PDF content extraction |
| vlln/pdffigures-mcp-server | 6 | Figures and tables from PDFs — useful for loss runs and financial statements |
| rsp2k/mcp-pdf | 4 | Comprehensive: OCR, tables, forms, annotations — closest to insurance document needs |
| foxitsoftware/PDFActionInspector | 3 | PDF security analysis with AI risk assessment |

The rsp2k/mcp-pdf server is the most relevant for insurance workflows. It handles OCR for scanned documents (common in legacy claims files), table extraction (essential for loss runs and medical bills), form field extraction (applicable to ACORD forms), and annotation processing. Combined with a claims or underwriting MCP server, it enables an AI agent to ingest a PDF claim submission, extract structured data, and feed it into processing workflows.

### OCR

| Server | Stars | Key Capability |
|--------|-------|----------------|
| sandraschi/ocr-mcp | 9 | FastMCP with DeepSeek-OCR, Florence-2, DOTS models |
| ArneJanning/nanonets-mcp | 1 | Nanonets OCR for PDF, Word, Excel |
| Baronco/Local-Docs-MCP-Tool | 2 | Local document interaction |

Insurance-specific OCR needs include reading handwritten adjuster notes, extracting data from medical records, processing scanned policy applications, and interpreting vehicle damage photos. The general-purpose OCR servers listed above provide a foundation, but insurance-grade accuracy typically requires fine-tuning on industry-specific document types.


## Regulatory and Compliance

### labor-law-mcp

The labor-law-mcp server (GitHub: kentaroajisaka/labor-law-mcp, 50 stars, TypeScript) is the highest-starred insurance-adjacent legal MCP server. It provides 6 tools covering 45 Japanese labor and social insurance laws, including health insurance and pension regulations.

While jurisdiction-specific, it demonstrates the pattern insurance needs globally: an MCP server that exposes regulatory requirements so AI agents can check compliance programmatically. An equivalent server for U.S. state insurance regulations — covering rate filing requirements, form approval rules, market conduct standards, and privacy obligations — would be immediately valuable.

### Broader Compliance Servers

| Server | Stars | Scope |
|--------|-------|-------|
| gibbrdev/gibs-mcp | 3 | EU regulatory: AI Act, GDPR, DORA |
| kevin-bot-openclaw-ops/mcp-banking-compliance | 0 | Banking KYC/AML, sanctions screening |
| ramarimei/healthcare-compliance-mcp | 0 | Healthcare regulatory document search |

The banking compliance server is relevant for insurers that also offer financial products. The healthcare compliance server matters for health insurance and workers' compensation lines where medical data handling is regulated by HIPAA and state equivalents.


## Member Benefits and Eligibility

### member-liability-agent

The member-liability-agent (GitHub: Optimus15/member-liability-agent, 2 stars, Python) focuses on health insurance member benefits and eligibility verification. Built on AWS Bedrock with Claude, it uses MCP tools to check member eligibility, look up benefit details, and calculate liability.

This is a common insurance workflow: a provider calls to verify a patient's coverage, and the agent needs to check eligibility, confirm the specific benefit (deductible, copay, coinsurance, out-of-pocket maximum), and explain coverage limitations. An MCP server that wraps this logic allows any AI agent — whether a customer-facing chatbot, a provider portal assistant, or an internal claims processor — to access the same eligibility data through a standard interface.


## Major Platform Landscape

Understanding how the major insurance platforms approach agentic AI — and where MCP fits or doesn't — is essential context for teams building in this space.

### Guidewire: Olos and Agentic Framework

Guidewire — the dominant technology vendor for P&C insurance — released its "Olos" cloud platform in December 2025. It includes a GenAI Service for building AI capabilities across the platform and an Agentic Framework (in Early Access) for developing and deploying AI agents. Guidewire's Agent Studio provides a development environment for custom AI agents, and PricingCenter offers unified price modeling.

Guidewire has not adopted MCP. Its agentic framework is proprietary, meaning AI agents built for Guidewire cannot easily interact with non-Guidewire systems through a standard protocol. For the large share of the P&C market that runs on Guidewire, this creates a walled garden effect — powerful within the Guidewire ecosystem but isolated from the broader AI agent landscape.

### Duck Creek: Intelligence and Agentic Agents

Duck Creek Intelligence became generally available in December 2025 for North American customers, powered by Microsoft Azure AI. Duck Creek has built notable agentic capabilities:
- **Mora:** an autonomous catastrophe event monitoring system using multiple coordinating AI agents
- **Felix:** a multi-modal AI agent for automated First Notice of Loss intake from various input channels

Duck Creek's approach is built on Microsoft's AI stack rather than MCP. This makes sense given Duck Creek's Azure partnership but means their agentic capabilities are not interoperable with MCP-based tools.

### Applied Systems: Applied Insurance AI

Applied Systems has built an AI suite including Applied Recon (automated reconciliation), Applied Book Builder (risk intelligence), and acquired Planck and Cytora for AI-powered data extraction and risk enrichment. These are proprietary integrations rather than MCP-based.

### Other Platforms

| Platform | AI Status | MCP Adoption |
|----------|-----------|--------------|
| Majesco | Quadrupling AI investment for 2026; building Copilot and Agentic AI | None |
| Vertafore | AI for agency back-office; NL query planned | None |
| Sapiens | AI capabilities in development | None |
| EIS Group | No specific announcements | None |

The pattern is clear: every major insurance platform is investing heavily in AI and agentic capabilities, but only Socotra has adopted MCP. The others are building proprietary frameworks, typically aligned with their cloud partnerships (Microsoft for Duck Creek, various for Guidewire).


## Comparison Table

| Server | Stars | Category | Tools | Maturity | Key Feature |
|--------|-------|----------|-------|----------|-------------|
| labor-law-mcp | 50 | Regulatory/Compliance | 6 | Functional | 45 Japanese insurance/labor laws |
| mcp-pdf-extraction-server | 28 | Document Processing | — | Functional | PDF content extraction |
| sandraschi/ocr-mcp | 9 | Document Processing | — | Functional | Multi-model OCR |
| ClaimsProcessingAssistant-MCP | 4 | Claims | 4 | Prototype | Claims validation rules engine |
| fraud-detection-mcp | 4 | Fraud Detection | — | Functional | XGBoost, GNN, behavioral biometrics |
| rsp2k/mcp-pdf | 4 | Document Processing | — | Functional | OCR, tables, forms, annotations |
| gibbrdev/gibs-mcp | 3 | Compliance | — | Functional | EU AI Act, GDPR, DORA |
| member-liability-agent | 2 | Eligibility | — | Prototype | Benefits verification |
| mcp-financial-services | 2 | Policy/Product | — | Early | Insurance product comparison |
| deepmap-mcp-server | 1 | Risk Assessment | 25 | Functional | Geophysical hazard, parametric triggers |
| Socotra MCP Server | — | Policy Admin/Claims | — | Production | Only major platform with MCP |

Note: Socotra's MCP server is commercial and not on GitHub, so no star count is available.


## Architecture Patterns

### Claims Automation Pipeline

```
┌─────────────┐    ┌──────────────┐    ┌──────────────────┐
│  Claim       │───▶│  Document    │───▶│  Claims          │
│  Submission  │    │  Processing  │    │  Validation      │
│  (email/     │    │  MCP Server  │    │  MCP Server      │
│   portal/    │    │  (OCR, PDF   │    │  (rules engine,  │
│   phone)     │    │   extraction)│    │   coverage check)│
└─────────────┘    └──────────────┘    └──────────────────┘
                                              │
                   ┌──────────────┐           │
                   │  Fraud       │◀──────────┤
                   │  Detection   │           │
                   │  MCP Server  │           ▼
                   │  (XGBoost,   │    ┌──────────────────┐
                   │   GNN)       │───▶│  Adjudication     │
                   └──────────────┘    │  Agent            │
                                       │  (approve/route   │
                                       │   to examiner)    │
                                       └──────────────────┘
```

In this pattern, a coordinating agent receives a claim submission, routes the documents through an OCR/PDF extraction MCP server to produce structured data, validates the claim against policy terms through a claims MCP server, runs fraud detection checks in parallel, and either auto-adjudicates (for simple, low-risk claims) or routes to a human examiner with a pre-assembled case file. The 70-90% of simple claims that industry data suggests can be straight-through processed are the primary target.

### Underwriting Intelligence Workflow

```
┌─────────────┐    ┌──────────────┐    ┌──────────────────┐
│  Submission  │───▶│  Document    │───▶│  Property/Asset   │
│  (app, loss  │    │  Extraction  │    │  Data MCP Server  │
│   runs, SOV) │    │  MCP Server  │    │  (characteristics,│
│              │    │              │    │   loss history)    │
└─────────────┘    └──────────────┘    └──────────────────┘
                                              │
       ┌──────────────┐                       │
       │  Geophysical  │◀─────────────────────┤
       │  Risk MCP     │                       │
       │  (DeepMapAI)  │                       ▼
       │  earthquake,  │              ┌──────────────────┐
       │  wildfire,    │─────────────▶│  Underwriting    │
       │  flood risk   │              │  Agent           │
       └──────────────┘              │  (risk score,    │
                                      │   pricing,       │
       ┌──────────────┐              │   terms)         │
       │  Climate Risk │─────────────▶│                  │
       │  MCP Server   │              └──────────────────┘
       │  (ESG, long-  │
       │   term trends)│
       └──────────────┘
```

The underwriting agent assembles a risk profile by pulling data from multiple MCP servers: document extraction for the submission, property data for asset characteristics, DeepMapAI for location-based hazard scoring, and climate risk for long-term exposure trends. The agent synthesizes these inputs into a risk score, suggested pricing, and recommended policy terms. For standard risks, this can be fully automated; for complex or high-value accounts, the agent prepares a structured brief for human underwriters.

### Fraud Investigation Network

```
┌─────────────┐    ┌──────────────┐    ┌──────────────────┐
│  Flagged     │───▶│  Document    │───▶│  Fraud Detection  │
│  Claim       │    │  Authenticity│    │  MCP Server       │
│              │    │  MCP Server  │    │  (pattern          │
│              │    │  (deepfake,  │    │   analysis,        │
│              │    │   synthetic) │    │   anomaly detect.) │
└─────────────┘    └──────────────┘    └──────────────────┘
                                              │
                                              ▼
                                       ┌──────────────────┐
                   ┌──────────────┐    │  Graph Analysis   │
                   │  External    │───▶│  Agent            │
                   │  Data MCP    │    │  (entity links,   │
                   │  (public     │    │   ring detection,  │
                   │   records,   │    │   SIU referral)    │
                   │   watchlists)│    └──────────────────┘
                   └──────────────┘
```

Fraud investigation increasingly requires analyzing relationships between entities — claimants, providers, repair shops, agents — to detect organized fraud rings. The GNN-based approach in the fraud-detection-mcp server is designed for this. An investigation agent can verify document authenticity (detecting AI-generated fake medical records), run pattern analysis against historical claims, perform graph analysis to map entity relationships, and check external data sources, then either clear the claim or generate a Special Investigations Unit referral with evidence.

### Regulatory Compliance Check

```
┌─────────────┐    ┌──────────────┐    ┌──────────────────┐
│  Product     │───▶│  Regulatory  │───▶│  Rate/Form       │
│  Change      │    │  Database    │    │  Filing           │
│  Request     │    │  MCP Server  │    │  Validation       │
│              │    │  (state reqs,│    │  Agent            │
│              │    │   filings)   │    │                   │
└─────────────┘    └──────────────┘    └──────────────────┘
                                              │
                                              ▼
                   ┌──────────────┐    ┌──────────────────┐
                   │  Compliance  │◀───│  Filing           │
                   │  MCP Server  │    │  Preparation      │
                   │  (GDPR, AI   │    │  Agent            │
                   │   Act, state │    │  (SERFF format,   │
                   │   privacy)   │    │   documentation)  │
                   └──────────────┘    └──────────────────┘
```

When an insurer modifies a product — changing rates, updating policy forms, or adding a new coverage option — regulatory filings may be required in every state where the product is sold. A compliance agent checks the regulatory database MCP server to identify which jurisdictions require filings, validates the proposed changes against state-specific rules, and prepares filing documentation. The labor-law-mcp server demonstrates this pattern for Japanese regulations; an equivalent for U.S. state insurance regulation would be immediately valuable.


## Security and Compliance Considerations

Insurance handles some of the most sensitive data in any industry. AI agents operating in insurance workflows must respect specific constraints.

**Protected Health Information (PHI).** Health insurance and workers' compensation claims involve medical records protected by HIPAA. MCP servers handling this data must implement access controls, audit logging, encryption in transit and at rest, and minimum necessary data principles. An AI agent should not receive a full medical record when it only needs a diagnosis code and treatment dates.

**Personally Identifiable Information (PII).** Policy applications contain Social Security numbers, driver's license numbers, financial information, and detailed personal history. MCP servers must scope data access to what each agent actually needs. Socotra's capability-scoped authentication model — where each agent receives only the permissions required for its specific task — is a reference implementation for this pattern.

**Regulatory audit trails.** Insurance regulators can examine any decision that affects a policyholder — underwriting decisions, claims adjudications, rate classifications. AI agents making or recommending these decisions must generate auditable records. MCP servers should log every tool call, the data returned, and how it was used in the decision chain.

**Anti-fraud reporting.** Insurers have legal obligations to report suspected fraud to state fraud bureaus. AI agents involved in fraud detection must be designed to flag cases for human review and regulatory reporting, not to make final fraud determinations autonomously.

**Rate and form compliance.** In most U.S. states, insurance rates and policy forms must be filed with and approved by the state insurance department before use. AI agents involved in pricing or product configuration must operate within approved parameters. The Socotra MCP server's policy-aware authorization ensures agents cannot modify product configuration beyond approved boundaries.

**Data residency.** Some jurisdictions require insurance data to remain within specific geographic boundaries. MCP servers and the AI agents connecting to them must respect these requirements, which may limit which cloud regions or processing locations can be used.


## Ecosystem Gaps

The insurance MCP ecosystem has significant gaps that represent opportunities for builders.

**No ACORD MCP server.** ACORD (Association for Cooperative Operations Research and Development) is the universal data standard for insurance. ACORD forms and data standards are used across property/casualty, life, health, and reinsurance globally. An MCP server that exposes ACORD form schemas, validates data against ACORD standards, and facilitates ACORD-formatted data exchange would be foundational infrastructure. This is arguably the single highest-value insurance MCP server that could be built.

**No major PAS vendors besides Socotra.** Guidewire, Duck Creek, Majesco, and Applied Systems collectively serve the majority of the P&C insurance market. None have MCP servers. Until they do — or until community-built adapters emerge — AI agents cannot interact with most production insurance systems through MCP.

**No rating engine MCP servers.** Insurance rating engines (from vendors like Earnix, Guidewire's PricingCenter, and Willis Towers Watson's Radar) calculate premiums based on complex actuarial models. No MCP server exposes rating functionality, meaning AI agents cannot currently request premium quotes through the protocol.

**No agency management system integration.** Applied Epic, Vertafore AMS360, HawkSoft, and EZLynx manage the operations of insurance agencies and brokerages. No MCP servers connect to these systems, blocking AI agents from the workflows where most insurance is actually sold and serviced.

**No reinsurance treaty management.** Reinsurance — where insurers transfer risk to reinsurers — involves complex treaty structures, cession calculations, and bordereaux reporting. No MCP tooling exists for this segment, despite reinsurance's heavy reliance on data exchange between parties.

**No actuarial modeling integration.** Actuarial models built in tools like R, Python, SAS, or specialized platforms like AXIS (for life insurance) and ResQ (for P&C reserving) have no MCP adapters. Given that actuaries report spending 60-80% of their time on data gathering and cleaning, MCP servers that feed data directly into actuarial workflows would be immediately valuable.

**No catastrophe modeling.** AIR Worldwide (Verisk), RMS (Moody's), and CoreLogic's cat models are critical infrastructure for property insurance and reinsurance. No MCP servers expose catastrophe model results. DeepMapAI's geophysical tools are the closest available alternative but are not equivalent to full probabilistic cat modeling.

**No state regulatory database.** The NAIC (National Association of Insurance Commissioners) maintains SERFF (System for Electronic Rate and Form Filing) and other regulatory databases. No MCP server exposes state-by-state regulatory requirements, filing statuses, or compliance rules.

**No insurance-specific CRM.** Salesforce and HubSpot MCP servers exist for general CRM, but insurance-specific CRMs like AgencyBloc, Radiusbob, and Insureio have no MCP integration.


## Getting Started

The appropriate entry point depends on your role and the insurance line you work in.

**Claims professionals** should start with document processing: the rsp2k/mcp-pdf server for extracting data from claim submissions and supporting documents, combined with the ocr-mcp server for scanned documents. The ClaimsProcessingAssistant-MCP provides a reference implementation for claims workflow automation, though it is a prototype. For fraud screening, the fraud-detection-mcp server offers the most complete detection toolkit available via MCP.

**Underwriters** will find the DeepMapAI server most immediately useful for location-based risk assessment across multiple natural hazard categories. For document-heavy submissions (loss runs, schedules of values, financial statements), combine PDF extraction MCP servers with property data servers from our [real estate guide](/guides/mcp-real-estate/). The underwriting-specific MCP servers remain too early for production use.

**Compliance and regulatory teams** can evaluate the labor-law-mcp server as a reference for how regulatory databases can be exposed through MCP, even though it covers Japanese rather than U.S. law. The gibbrdev/gibs-mcp server covers EU regulations (AI Act, GDPR, DORA) relevant to insurers operating in Europe.

**Platform teams at carriers** considering MCP adoption should examine Socotra's implementation as the reference model for production-grade insurance MCP servers. Key design decisions — capability-scoped authentication, policy-aware authorization, encrypted sessions — are applicable regardless of the underlying policy administration system.

**InsurTech builders** have a significant opportunity in the gaps identified above. An ACORD-compliant MCP server, a state regulatory database server, or adapters for major PAS vendors would each address a large unmet need. The market context supports investment: AI in insurance is projected to grow from roughly $10-20 billion in 2025 to $88 billion by 2030, and 22% of insurers plan to deploy agentic AI solutions by end of 2026.

**Actuaries** should watch for MCP servers that can feed data directly into modeling workflows. While none exist today, the pattern is straightforward: an MCP server wrapping data sources (loss triangles, exposure data, economic indicators) that an AI agent can query and format for actuarial tools. Our guides on [MCP and data science workflows](/guides/mcp-data-science-workflows/) and [MCP database patterns](/guides/mcp-database-patterns/) cover relevant infrastructure patterns.

The insurance MCP ecosystem is where the broader MCP ecosystem was roughly 18-24 months ago — a handful of servers, one production platform, and enormous unmet demand. The insurance industry's massive AI investment ($5+ billion in annual insurtech funding, 84% of carriers deploying or actively exploring AI) is creating pull. The question is not whether insurance-specific MCP servers will be built, but how quickly the ecosystem matures and whether MCP or proprietary agentic frameworks win the integration layer.

For broader context on MCP in related industries, see our guides on [MCP in financial services](/guides/mcp-finance-fintech/), [MCP in healthcare](/guides/mcp-healthcare-fhir/), and [MCP in legal and contract management](/guides/mcp-legal-contract-management/).
