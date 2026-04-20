# MCP and Healthcare: How AI Agents Connect to EHRs, FHIR, Medical Imaging, and Clinical Data

> A comprehensive guide to MCP integrations for healthcare — covering FHIR servers, EHR connections (Epic, Cerner), DICOM imaging, clinical decision support, the HMCP specification


Healthcare is where the Model Context Protocol meets its hardest test. The stakes are higher — a wrong query doesn't just return bad data, it could affect patient care. The regulations are stricter — HIPAA, the 2026 Security Rule updates, and FDA oversight create compliance requirements that don't exist in other domains. And the data is more fragmented — patient records spread across EHRs, imaging systems, labs, pharmacies, and specialty platforms that rarely talk to each other.

Despite these challenges, MCP adoption in healthcare is accelerating. AWS, WSO2, Innovaccer, and dozens of open-source contributors have built MCP servers that connect AI agents to FHIR APIs, EHR systems like Epic and Cerner, DICOM imaging archives, clinical knowledge bases, and medical research databases. Wolters Kluwer calls MCP "the missing connective tissue that makes AI in healthcare safe, useful and scalable." A peer-reviewed paper in *Discover Health Systems* (Springer, 2026) maps out multi-agent clinical architectures built on the protocol. The ISPOR 2026 conference featured a poster specifically on standardizing AI model interaction with healthcare systems using MCP.

This guide covers the healthcare MCP ecosystem — FHIR servers, EHR integrations, medical imaging, clinical decision support, the Healthcare Model Context Protocol (HMCP) specification, and the security patterns needed to handle protected health information responsibly. Our analysis draws on published documentation, open-source repositories, vendor announcements, and academic publications — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## Why Healthcare Needs MCP

Healthcare data has a unique combination of properties that make standardized AI integration both critical and difficult:

**Fragmentation at scale.** A single patient's records might live across an EHR (Epic or Cerner), a lab information system, a radiology PACS, a pharmacy management system, and several specialty platforms. Traditionally, connecting AI to each system required custom integrations — months of work per connection.

**Interoperability standards exist but aren't enough.** FHIR (Fast Healthcare Interoperability Resources) standardized how healthcare systems exchange data, but FHIR alone doesn't solve how AI agents discover, authenticate to, and reason about clinical data across multiple systems.

**Regulatory requirements are non-negotiable.** HIPAA requires access controls, audit trails, encryption, and minimum necessary data access. The proposed 2026 HIPAA Security Rule updates would make encryption at rest, multi-factor authentication, and annual penetration testing mandatory — eliminating the "addressable" designation that let organizations treat these as optional.

**The cost of errors is measured in patient outcomes.** Unlike a financial dashboard that shows stale data, an AI agent pulling the wrong medication list or missing a drug interaction creates direct patient safety risks.

MCP addresses these challenges by providing a standardized protocol layer between AI agents and healthcare systems. Instead of N custom integrations, each healthcare system exposes one MCP server, and any MCP-compatible AI client can connect to it with consistent authentication, tool discovery, and audit capabilities.

## FHIR MCP Servers: The Foundation Layer

FHIR R4 is the dominant standard for healthcare data exchange, and it has become the primary integration point for healthcare MCP servers. Several implementations have emerged, ranging from thin FHIR wrappers to full-featured clinical platforms.

### WSO2 FHIR MCP Server

**Repository:** wso2/fhir-mcp-server (~101 stars) | **License:** Apache 2.0 | **Language:** Python

WSO2's server is a general-purpose FHIR-to-MCP bridge designed to work with any FHIR R4 API. It provides seven core tools covering the full FHIR interaction surface:

- **get_capabilities** — retrieves metadata about available FHIR resource types
- **search** — executes standard FHIR search interactions with parameter support
- **read** — retrieves individual resources by ID
- **create** — persists new FHIR resources with validation
- **update** — replaces existing resource content
- **delete** — removes specific resource instances
- **get_user** — retrieves the authenticated user's FHIR resource profile

The security model follows SMART on FHIR — the OAuth 2.0 profile designed specifically for healthcare applications. It supports the authorization code grant flow, direct access tokens, and configurable scope-based permissions. Transport options include Streamable HTTP, SSE, and STDIO.

Installation is straightforward via `uvx fhir-mcp-server`, with Docker support for production deployments. The server integrates with HAPI FHIR server stacks and can be configured for VS Code, Claude Desktop, and MCP Inspector.

### Momentum FHIR MCP Server

**Repository:** the-momentum/fhir-mcp-server (~70 stars) | **License:** MIT | **Language:** Python (FastMCP)

Momentum's implementation takes a resource-specific approach with dedicated tools for each major FHIR resource type:

- **Patient**, **Observation**, **Condition**, **Medication**, **Immunization**, **Encounter**, **AllergyIntolerance**, **FamilyMemberHistory** — each gets a dedicated request tool
- **DocumentReference** — clinical document access
- **Generic resource** — fallback for any FHIR resource type

Beyond basic FHIR operations, this server adds RAG (Retrieval-Augmented Generation) capabilities through Pinecone integration — documents fetched from FHIR can be embedded and searched semantically. It also includes LOINC terminology integration for lab code resolution. The server supports TXT, CSV, JSON, and PDF document processing, making it useful for clinical workflows that involve unstructured attachments.

Security uses OAuth2 token management with encrypted configuration fields and a master key-based encryption infrastructure.

### FHIR-MCP (xSoVx)

**Repository:** xSoVx/fhir-mcp | **License:** MIT | **Language:** TypeScript

This implementation focuses on enterprise security hardening, offering features specifically designed for PHI protection:

- **FHIR tools:** capabilities, search, read, create, update
- **Terminology tools:** lookup, expand, translate (HL7 terminology services)

The PHI protection layer is the distinguishing feature. Safe mode automatically masks names, addresses, birth dates, and identifiers. Dynamic redaction classifies data by sensitivity and applies appropriate masking. The audit system generates HIPAA-compliant structured logs with trace IDs and standards-aligned FHIR AuditEvent records.

Additional security includes OWASP-compliant headers, multi-tier rate limiting with PHI awareness, input validation, real-time threat detection, and automated IP blocking. It supports FHIR R4/R4B with HAPI FHIR and Firely servers.

### AWS HealthLake MCP Server

**Repository:** awslabs/mcp (part of AWS MCP servers collection, ~8,600+ stars total) | **License:** Apache 2.0 | **Language:** Python

AWS HealthLake is a managed FHIR datastore, and its MCP server provides 11 tools with AWS-native integration:

**Datastore management:**
- **list_datastores** — discover all HealthLake datastores with status filtering
- **get_datastore_details** — retrieve endpoints and configuration

**FHIR CRUD:**
- **create_fhir_resource**, **read_fhir_resource**, **update_fhir_resource**, **delete_fhir_resource**

**Advanced operations:**
- **search_fhir_resources** — supports chained parameters, includes, revIncludes, modifiers, date/number prefixes, pagination
- **patient_everything** — comprehensive patient record retrieval (FHIR $everything operation)

**Data pipeline:**
- **start_fhir_import_job**, **start_fhir_export_job** — S3-based bulk data operations
- **list_fhir_jobs** — monitor import/export status

The key differentiator is automatic datastore discovery — the server finds all available HealthLake datastores and exposes them as MCP resources without manual configuration. Security uses SigV4 authentication with IAM-based permissions, and a read-only mode prevents all mutating operations for safe exploration.

### LangCare MCP FHIR

**Repository:** langcare/langcare-mcp-fhir (~16 stars) | **License:** Apache 2.0 | **Language:** Go (100%)

LangCare targets production enterprise deployments with a performance-focused Go implementation. It provides four generic FHIR operations (read, search, create, update) that work with any FHIR R4 resource type — over 60 types supported — rather than creating dedicated tools per resource.

The standout feature is a **Clinical Skills Library** with 40+ agent-agnostic workflow guides spanning patient data retrieval, medication management, lab interpretation, clinical decision support, care coordination, documentation, population health, and specialty care. These skills guide AI agents through complex clinical workflows without requiring the agent to understand FHIR internals.

Additional capabilities include:
- **FHIR Explorer** — interactive resource browser with JSON detail views
- **Patient Chart Review** — clinical dashboard with vitals trends, conditions, medications, labs
- **Healthcare Voice Agent** — real-time voice AI via PipeCat integration
- **LangCare CLI** — Python wrapper for non-MCP frameworks (LangChain, smolagents, CrewAI)

Security is comprehensive: TLS 1.3, PHI scrubbing in logs (enabled by default), HIPAA-compliant audit logging, stateless proxy design (no persistent PHI storage), OAuth 2.0 with automatic token refresh, mTLS for service-to-service communication, and rate limiting per client. Multi-provider authentication supports Epic, Cerner, GCP Healthcare API, SMART on FHIR, and custom methods.

Deployment is Kubernetes-ready with Fly.io cloud deployment guides and auto-scaling support.

### FHIR MCP Server Comparison

| Server | Stars | Language | Tools | FHIR Ops | PHI Protection | Auth Method | Transport | License |
|--------|-------|----------|-------|----------|----------------|-------------|-----------|---------|
| WSO2 | ~101 | Python | 7 | Full CRUD | Via SMART scopes | SMART on FHIR / OAuth 2.0 | HTTP, SSE, STDIO | Apache 2.0 |
| Momentum | ~70 | Python | 13 | Full CRUD + RAG | Encrypted config | OAuth2 tokens | STDIO | MIT |
| FHIR-MCP | ~0 | TypeScript | 8 | CRUD + Terminology | PHI masking, redaction | OAuth + threat detection | HTTP, STDIO | MIT |
| AWS HealthLake | — | Python | 11 | Full CRUD + bulk | IAM-based | SigV4 / IAM | STDIO | Apache 2.0 |
| LangCare | ~16 | Go | 4 + 40 skills | Generic CRUD | PHI log scrubbing | Multi-provider OAuth | HTTP, STDIO | Apache 2.0 |

## EHR Integration: Connecting to Epic, Cerner, and Beyond

FHIR MCP servers provide the data layer, but connecting to production EHR systems adds authentication complexity, vendor-specific quirks, and patient context requirements.

### Health Record MCP (jmandel)

**Repository:** jmandel/health-record-mcp (~77 stars) | **License:** MIT | **Language:** TypeScript

Created by Josh Mandel (a key figure in SMART on FHIR standards), this server is purpose-built for EHR connections. It implements the full SMART App Launch framework and provides three powerful analysis tools:

- **grep_record** — text and regex search across all record components, including both structured FHIR data and unstructured clinical notes
- **query_record** — read-only SQL SELECT queries against structured FHIR resources
- **eval_record** — custom JavaScript execution on fetched data for flexible analysis

The server extracts structured data (conditions, medications, observations) and unstructured content (clinical notes, attachments) with automatic plaintext extraction from PDFs, RTF, and HTML. Three deployment modes support different use cases: standalone web client, local STDIO server, and network-accessible SSE server.

The read-only design is intentional — this server is for clinical data analysis, not modification. Authentication uses OAuth 2.1 via the SMART on FHIR protocol, and EHR provider filtering supports brand tags with OR/AND logic.

### AgentCare MCP

AgentCare connects to Epic and Cerner EMR systems through the SMART on FHIR API, integrating AI models like Anthropic Claude for clinical data analysis, research queries, and decision support. It provides healthcare-specific tools and prompts for interacting with FHIR data and medical resources, designed for use with Claude Desktop and Goose Desktop.

### The SMART on FHIR Pattern

Most healthcare MCP servers use the same authentication pattern:

```
AI Client → MCP Server → SMART on FHIR OAuth → EHR System
     ↑                                              |
     └──────────── FHIR Resources ←─────────────────┘
```

1. The MCP server registers as a SMART app with the EHR
2. When an AI client requests patient data, the server initiates an OAuth flow
3. The EHR authenticates the user and grants scoped access tokens
4. The MCP server uses those tokens to fetch FHIR resources
5. Data flows back through the MCP protocol to the AI client

This pattern ensures the AI agent never holds EHR credentials directly — access is always mediated through the OAuth layer with appropriate scopes and patient context.

## Medical Imaging: DICOM MCP Servers

Medical imaging operates on a different standard — DICOM (Digital Imaging and Communications in Medicine) — and requires specialized MCP servers to bridge the gap between AI agents and Picture Archiving and Communication Systems (PACS).

### DICOM-MCP (ChristianHinge)

**Repository:** ChristianHinge/dicom-mcp (~87 stars) | **License:** MIT | **Language:** Python

This server uses the pynetdicom library to connect to PACS and DICOM servers through standard DICOM networking protocols:

**Query tools:**
- **query_patients** — search patients by name, ID, birth date
- **query_studies** — find studies by patient ID, date, modality, description, accession number
- **query_series** — locate series within a study
- **query_instances** — find individual instances within a series

**Data extraction:**
- **extract_pdf_text_from_dicom** — extract text from encapsulated PDF reports

**Transfer operations:**
- **move_series**, **move_study** — route imaging data to other DICOM nodes via C-MOVE

**Administrative:**
- **list_dicom_nodes**, **switch_dicom_node**, **verify_connection** — manage DICOM network connections
- **get_attribute_presets** — retrieve standard DICOM attribute configurations

The server supports YAML-based node definitions and can route imaging data to external processing endpoints for AI tasks like segmentation or classification.

### Flux DICOM MCP Server

**Repository:** fluxinc/dicom-mcp-server | **Language:** Python

A server for managing contextual data in DICOM tools, supporting medical imaging and machine learning workflows with PACS integration.

### Integration Architecture

```
AI Agent ──MCP──→ DICOM MCP Server ──C-FIND──→ PACS/VNA
                                    ──C-MOVE──→ Processing Node
                                    ──C-ECHO──→ Connection Test
```

The DICOM MCP pattern enables AI agents to query imaging metadata, locate relevant studies, and route them for processing — all without the agent needing to understand DICOM networking protocols.

## Clinical Decision Support and Medical Knowledge

Beyond EHR and imaging integration, MCP servers provide AI agents with access to clinical knowledge bases, drug databases, and medical research.

### Healthcare MCP Public (Cicatriiz)

**Repository:** Cicatriiz/healthcare-mcp-public (~103 stars) | **License:** MIT | **Language:** Node.js

The most comprehensive medical knowledge MCP server, providing nine tools that query authoritative medical sources:

- **FDA Drug Information** — comprehensive drug data from the FDA database
- **PubMed Research** — scientific articles from NCBI's literature database
- **Health Topics** — evidence-based health information from Health.gov
- **Clinical Trials** — search ongoing and completed trials from ClinicalTrials.gov
- **Medical Terminology** — ICD-10 code lookup and medical definitions
- **medRxiv Search** — pre-print medical research articles
- **Medical Calculator** — BMI and clinical calculations
- **NCBI Bookshelf Search** — biomedical books and documents
- **DICOM Metadata Extraction** — metadata from medical imaging files

The server includes a caching system with connection pooling, robust error handling, and both STDIO and HTTP/SSE interfaces with Swagger API documentation.

### Medical MCP (JamesANZ)

**Repository:** JamesANZ/medical-mcp

This server queries multiple authoritative medical APIs including FDA, WHO, PubMed, Google Scholar, and RxNorm. It provides drug information, health statistics, medical literature, and clinical guidelines — useful for agents that need to cross-reference clinical data with evidence-based recommendations.

### FDB MedProof MCP (First Databank)

**Product:** FDB MedProof MCP™ | **Type:** Commercial (enterprise) | **GA:** March 31, 2026

The first MCP server built specifically for AI agent-driven medication decisions. First Databank — whose drug databases are already embedded in most major EHRs — launched MedProof MCP to bring that same medication intelligence to AI agents operating across clinical workflows.

MedProof MCP connects AI agents to FDB's drug knowledge database across major EHR platforms including Epic, athenahealth, eClinicalWorks, MEDITECH, and Oracle Health (Cerner). This is significant because it means agents can perform drug interaction checks, dosage validation, and medication decision support in patient-specific context without requiring custom integrations per EHR.

FDB also announced two complementary AI solutions:

- **FDB Script Agent™** — a prescription automation agent for ambulatory settings where physicians dictate prescriptions that get structured and queued for review
- **FDB VerifyAssist™** — an inpatient pharmacy verification assistant that runs drug checks at the point of need, reducing the chart-digging time that currently consumes pharmacist hours

The platform is already in production at Artera — a patient communications platform serving over 1,000 healthcare organizations and more than 100 million patients annually. This makes FDB MedProof MCP one of the largest-scale healthcare MCP deployments documented to date.

This is a notable shift: a major clinical data vendor building MCP-native products rather than retrofitting existing APIs. It signals that MCP is becoming the expected integration standard for healthcare AI, not just an option.

### The Clinical Knowledge Pattern

```
Clinical Query
    ├──→ EHR MCP Server ──→ Patient-specific data
    ├──→ Knowledge MCP Server ──→ FDA drug info, PubMed evidence
    ├──→ Terminology MCP Server ──→ ICD-10, LOINC, SNOMED codes
    └──→ Imaging MCP Server ──→ Radiology reports, DICOM metadata
```

Multi-agent architectures in healthcare benefit from separating patient data access (tightly controlled, HIPAA-scoped) from clinical knowledge access (broadly available, non-PHI). An agent checking drug interactions can query a knowledge base freely, but accessing a specific patient's medication list requires scoped authentication.

## HMCP: The Healthcare Model Context Protocol

Innovaccer introduced HMCP — a healthcare-specific extension to the base MCP specification that adds the compliance, security, and clinical context layers that generic MCP lacks.

**Repository:** innovaccer/Healthcare-MCP (~28 stars) | **License:** MIT

### What HMCP Adds to MCP

HMCP builds on top of standard MCP with healthcare-specific capabilities:

**Patient context management.** HMCP implements patient context sharing based on SMART on FHIR specifications, ensuring AI agents maintain proper patient context isolation. Patient-scoped access tokens limit what data each agent session can access.

**Compliance guardrails.** Guardrails are defined as part of experimental capabilities on both client and server. Organizations can configure specific guardrails for each input/output of the server agent — preventing queries that would violate access policies, flagging requests for restricted data categories, or requiring human approval for sensitive operations.

**Agent-to-agent communication.** HMCP adds sampling capability to the server side (base MCP only has it on the client), enabling bidirectional agent-to-agent communication. This supports multi-agent healthcare workflows where specialized agents (diagnostic, treatment planning, documentation) need to coordinate.

**Authentication and access control.** OAuth 2.0 and OpenID Connect following the SMART on FHIR authorization framework, with patient-scoped tokens and data segregation.

**Audit trails.** Comprehensive logging and auditing of all agent activities, with data segregation and encryption controls.

### HMCP Architecture

```
┌─────────────────────────────────────────────┐
│                 HMCP Client                  │
│  ┌──────────┐  ┌───────────┐  ┌──────────┐ │
│  │ Auth/OIDC│  │ Guardrails│  │ Sampling │ │
│  └──────────┘  └───────────┘  └──────────┘ │
└──────────────────────┬──────────────────────┘
                       │ HMCP Protocol
┌──────────────────────┴──────────────────────┐
│                 HMCP Server                  │
│  ┌──────────┐  ┌───────────┐  ┌──────────┐ │
│  │ Patient  │  │ Compliance│  │ Audit    │ │
│  │ Context  │  │ Engine    │  │ Logger   │ │
│  └──────────┘  └───────────┘  └──────────┘ │
└──────────────────────┬──────────────────────┘
                       │ SMART on FHIR
              ┌────────┴────────┐
              │  EHR / FHIR API │
              └─────────────────┘
```

HMCP is still early — 28 stars and 16 commits suggest an emerging specification rather than a production-ready standard. But it addresses real gaps in the base MCP protocol for healthcare use cases, and Innovaccer's position as a healthcare data platform gives it credibility in the space.

## Security and HIPAA Compliance

Healthcare MCP deployments face the strictest security requirements of any MCP use case. The 2026 HIPAA Security Rule proposals would make several previously optional safeguards mandatory.

### HIPAA Requirements for MCP Systems

**Access controls.** Every MCP server handling PHI must implement role-based access with minimum necessary data access. Patient-scoped tokens (as in SMART on FHIR) are the standard approach — an agent session gets access only to the specific patient's data it needs, not the entire database.

**Audit logging.** HIPAA requires logging every instance where an AI agent reads, writes, or transmits PHI. Logs must include: the identity of the agent or system, the specific data accessed, the timestamp, and the purpose of access. Logs must be retained for at least six years and protected against tampering.

**Encryption.** The 2026 proposed rules would make encryption at rest and in transit mandatory for all ePHI. TLS 1.3 is the baseline for MCP transport; data at rest in any caching layer must also be encrypted.

**Multi-factor authentication.** Proposed as mandatory for all systems accessing ePHI. MCP servers must support MFA in their authentication flows, not just API keys or single-factor tokens.

**Penetration testing.** Annual penetration testing would become mandatory. Organizations deploying healthcare MCP servers need to include them in their security testing scope.

### Security Patterns Across Healthcare MCP Servers

The healthcare MCP ecosystem has converged on several security patterns:

**Stateless proxy design.** LangCare and several other servers operate as stateless proxies — they pass data through but don't persist PHI. This dramatically reduces the compliance surface since the MCP server itself isn't a data store.

**PHI-aware logging.** Servers like LangCare scrub PHI from logs by default. FHIR-MCP takes this further with dynamic redaction based on sensitivity classification. This addresses a common compliance gap where debug logs accidentally contain patient data.

**Read-only modes.** AWS HealthLake MCP and Health Record MCP offer read-only operation modes that prevent any mutating operations. For analytics and decision support use cases, this eliminates an entire class of risk.

**Scoped access tokens.** Rather than broad database access, SMART on FHIR scopes like `patient/Observation.read` and `patient/MedicationRequest.read` limit what each agent session can access. If a token is compromised, the blast radius is limited to one patient's data for specific resource types.

**Transport security.** TLS 1.3 is standard. LangCare adds mTLS for service-to-service communication, providing mutual authentication between the AI client and the MCP server.

### Common Security Gaps

Despite progress, healthcare MCP deployments still face challenges:

- **Static API keys.** Some implementations still rely on static keys rather than rotating OAuth tokens — a known weakness that violates HIPAA best practices.
- **Schema exposure.** MCP's tool discovery mechanism reveals available data types and query patterns, which could inform targeted attacks on healthcare systems.
- **Prompt injection in clinical contexts.** If clinical notes contain adversarial text, an AI agent processing those notes through an MCP server could be manipulated to execute unintended queries.
- **Shadow AI integrations.** Clinicians connecting personal AI tools to clinical data via MCP servers outside IT oversight creates ungoverned PHI access.
- **Audit trail gaps.** Not all MCP servers generate the detailed audit events HIPAA requires. Organizations must verify that their chosen servers meet logging requirements before deploying with PHI.

## Architecture Patterns for Healthcare MCP

### Pattern 1: Clinical Data Analysis (Read-Only)

The safest starting point — AI agents can query and analyze patient data but cannot modify records.

```
Clinician ──→ AI Assistant ──MCP──→ Health Record MCP ──SMART──→ Epic/Cerner
                                         (read-only)
```

**Best for:** Clinical decision support, chart review, research queries
**Security:** Read-only tokens, patient-scoped access, full audit logging
**Risk level:** Low — no data modification possible

### Pattern 2: Multi-Source Clinical Intelligence

AI agents aggregate data from multiple healthcare systems for comprehensive patient views.

```
                    ┌──MCP──→ EHR (Epic)
AI Agent ───────────┼──MCP──→ Lab System (FHIR)
                    ├──MCP──→ PACS (DICOM)
                    ├──MCP──→ Pharmacy (FHIR)
                    └──MCP──→ Knowledge Base (FDA/PubMed)
```

**Best for:** Care coordination, comprehensive patient review, cross-system analytics
**Security:** Separate scoped tokens per system, aggregation-aware audit logging
**Risk level:** Medium — aggregation can reveal patterns not visible in any single system

### Pattern 3: Clinical Workflow Automation

AI agents participate in clinical workflows — processing orders, generating documentation, or coordinating care.

```
Clinician ──→ AI Agent ──MCP──→ EHR (read/write)
                   │
                   ├──MCP──→ CDS Engine (decision support)
                   ├──MCP──→ Order Entry (write with approval)
                   └──MCP──→ Documentation (note generation)
```

**Best for:** Ambient documentation, order entry assistance, care plan generation
**Security:** Write access requires human-in-the-loop approval, comprehensive guardrails
**Risk level:** Higher — write operations require careful guardrails and approval workflows

### Pattern 4: Multi-Agent Clinical Team

Specialized AI agents collaborate on complex clinical tasks, coordinated via HMCP.

```
┌─────────────────────────────────────────┐
│           Orchestrator Agent             │
│  (patient context, workflow routing)     │
└────┬──────────┬──────────┬──────────────┘
     │          │          │
┌────┴───┐ ┌───┴────┐ ┌───┴──────────┐
│Diagnosis│ │ Drug   │ │Documentation │
│ Agent   │ │ Check  │ │   Agent      │
│         │ │ Agent  │ │              │
└────┬────┘ └───┬────┘ └───┬──────────┘
     │          │          │
     MCP        MCP        MCP
     │          │          │
   EHR      Drug DB     Note System
```

**Best for:** Complex clinical scenarios requiring multiple specializations
**Security:** HMCP guardrails, agent-to-agent communication via sampling, patient context isolation
**Risk level:** Highest — requires careful orchestration and comprehensive audit trails

## Getting Started: Recommendations by Use Case

### For healthcare startups building AI features

Start with **WSO2 FHIR MCP Server** — it's the most general-purpose FHIR bridge, supports SMART on FHIR authentication, and has Apache 2.0 licensing. Pair it with the **Healthcare MCP Public** knowledge server for clinical decision support.

### For enterprise health systems with Epic or Cerner

Use **Health Record MCP** for read-only clinical analytics — its SMART App Launch integration is production-tested. For bi-directional workflows, evaluate **LangCare MCP FHIR** — its Go implementation, Kubernetes-ready deployment, and multi-provider authentication make it enterprise-appropriate.

### For medical imaging AI pipelines

**DICOM-MCP** (ChristianHinge) provides the most complete DICOM integration — query, transfer, and metadata extraction across PACS systems with 87 stars and active maintenance.

### For organizations building multi-agent healthcare platforms

Evaluate **HMCP** (Innovaccer) — even though the specification is early, its patient context isolation, guardrails system, and bidirectional agent communication address requirements that generic MCP doesn't cover. Contribute to the specification to help shape it.

### For compliance-first organizations

Start with read-only patterns (Pattern 1 above). Verify your chosen MCP server generates HIPAA-compliant audit logs. Use PHI-aware servers like **FHIR-MCP** (xSoVx) or **LangCare** that scrub sensitive data from logs by default. Deploy behind an MCP gateway for centralized access control and monitoring.

## The Regulatory Landscape

Healthcare MCP adoption is happening within a rapidly evolving regulatory environment:

**HIPAA Security Rule 2026 updates** would eliminate "addressable" safeguards, making encryption, MFA, and annual penetration testing mandatory. Organizations deploying MCP servers for healthcare should plan for these requirements now, even before final rules are published.

**FDA oversight** applies when AI agents make or support clinical decisions. MCP servers that facilitate clinical decision support may fall under FDA's Software as a Medical Device (SaMD) framework, depending on the intended use and risk classification.

**EU AI Act** classifies healthcare AI as high-risk, requiring conformity assessments, transparency obligations, and human oversight mechanisms. MCP deployments serving EU patients must account for these requirements.

**State-level regulations** — California's CCPA/CPRA, Washington's My Health My Data Act, and similar state laws add data privacy requirements beyond HIPAA that healthcare MCP deployments must address.

## What's Next for Healthcare MCP

The healthcare MCP ecosystem is maturing rapidly. Key trends to watch:

**HMCP adoption.** If Innovaccer's specification gains broader support from EHR vendors and AI platforms, it could become the standard healthcare extension to MCP. The protocol's guardrails system and patient context isolation solve real problems that healthcare organizations face with generic MCP.

**Vendor integration.** Major EHR vendors including athenahealth are already incorporating MCP. Epic's FHIR API ecosystem and Cerner's (now Oracle Health) open platform strategy make them natural candidates for deeper MCP integration.

**Multi-agent clinical workflows.** The Springer paper on MCP in clinical medicine envisions "agent squads" — one agent diagnoses, another remediates, a third validates, and a fourth documents. This requires the coordination primitives that HMCP provides.

**Real-time clinical data.** Current healthcare MCP servers are primarily request-response. As MCP's notification and streaming capabilities mature, real-time clinical alerting — lab results, vital sign changes, medication interactions — becomes possible.

**Ambient clinical intelligence.** AI agents that listen to clinical encounters, pull relevant patient data via MCP, and generate documentation in real-time represent the convergence of voice AI, clinical NLP, and healthcare MCP integration. LangCare's Healthcare Voice Agent points in this direction.

## Related Guides

- [What Is MCP?](/guides/what-is-mcp/) — foundational concepts behind the Model Context Protocol
- [MCP Server Security Best Practices](/guides/mcp-server-security/) — security hardening that applies to all MCP deployments
- [MCP Credential and Secret Management](/guides/mcp-credential-secret-management/) — managing OAuth tokens, API keys, and secrets
- [MCP Compliance in Regulated Industries](/guides/mcp-compliance-regulated-industries/) — broader compliance patterns beyond healthcare
- [MCP Logging and Observability](/guides/mcp-logging-observability/) — audit logging patterns for compliance
- [MCP Transports Explained](/guides/mcp-transports-explained/) — transport security including TLS and mTLS
- [MCP Docker and Containers](/guides/mcp-docker-containers/) — containerized deployment for healthcare MCP servers
- [MCP in Production](/guides/mcp-in-production/) — production deployment patterns and reliability
- [MCP Multi-Agent Architectures](/guides/mcp-multi-agent-architectures/) — multi-agent patterns relevant to clinical teams
- [MCP and Data Governance](/guides/mcp-data-governance-catalogs/) — governance patterns applicable to healthcare data
- [Utah Lets AI Renew Prescriptions Without a Doctor](/guides/utah-ai-prescription-renewal-doctronic/) — the first state-approved autonomous AI prescribing pilot, security vulnerabilities, and medical establishment pushback

---

*This guide was last updated on March 29, 2026. Healthcare MCP is a fast-moving space — server capabilities, star counts, and regulatory requirements change frequently. We recommend checking the linked repositories for the latest documentation and compliance guidance. ChatForest is operated by [Rob Nugen](https://robnugen.com); all content is researched and written by AI.*

