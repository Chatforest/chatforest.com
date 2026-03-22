---
title: "Healthcare & Medical MCP Servers — FHIR, PubMed, Clinical Trials, DICOM, Drug Databases, and More"
date: 2026-03-15T10:16:00+09:00
description: "Healthcare and medical MCP servers are connecting AI agents to clinical data, medical research, drug databases, and imaging systems via the Model Context Protocol. We reviewed 30+ servers across 6 subcategories. FHIR/EHR Integration: wso2/fhir-mcp-server (98 stars, Python, Apache-2.0 — expose any FHIR server as MCP with full CRUD, SMART-on-FHIR auth, stdio/SSE/HTTP transport), jmandel/health-record-mcp (75 stars, TypeScript, MIT — SMART on FHIR EHR access with grep/SQL/JavaScript query tools), the-momentum/fhir-mcp-server (68 stars, Python, MIT — 11 tools for FHIR resources with Pinecone vector search and LOINC integration), rkirkendall/medplum-mcp (14 stars, TypeScript, MIT — 33 tools for Medplum FHIR CRUD), langcare/langcare-mcp-fhir (15 stars, Go — enterprise-grade EHR proxy for Epic/Cerner/GCP with 40+ clinical skills library, TLS 1.3, PHI scrubbing), AWS HealthLake MCP (part of awslabs/mcp 8.5K stars — 11 FHIR tools with automatic datastore discovery, read-only mode, 96% test coverage). Medical Research: JackKuo666/PubMed-MCP-Server (104 stars, Python, MIT — 5 tools for PubMed search/metadata/PDF download/deep analysis, most starred research MCP server), cyanheads/clinicaltrialsgov-mcp-server (58 stars, TypeScript, Apache-2.0 — 7 tools for ClinicalTrials.gov with trend analysis/patient matching/study comparison, 92% test coverage), JackKuo666/ClinicalTrials-MCP-Server (15 stars, Python, MIT — 7 tools with CSV export), pascalwhoop/medical-mcps (14 stars, Python, MIT — 100+ tools across 14 biomedical APIs including PubMed/OpenFDA/KEGG/UniProt/GWAS/ChEMBL). Multi-Source Healthcare Hubs: Cicatriiz/healthcare-mcp-public (101 stars, JavaScript, MIT — 9 tools for FDA drugs/PubMed/clinical trials/ICD-10/DICOM/medical calculator, most starred healthcare MCP server), JamesANZ/medical-mcp (75 stars, TypeScript, MIT — 15 tools for FDA/WHO/PubMed/Google Scholar/RxNorm/AAP, no API keys needed, fully local). Drug & Pharmacology: openpharma-org/drugbank-mcp-server (2 stars, JavaScript, MIT — 17,000+ drug records with interactions/pathways/structure search via SQLite), openpharma-org/nlm-codes-mcp (0 stars, TypeScript, MIT — ICD-10/ICD-11/HCPCS/NPI/HPO/LOINC/RxTerms via NLM Clinical Tables API). Medical Imaging: ChristianHinge/dicom-mcp (86 stars, Python, MIT — 11 tools for DICOM/PACS query/move/PDF extraction, most starred imaging MCP server), fluxinc/dicom-mcp-server (3 stars, Python, LGPL-2.1 — DICOM connectivity testing). Healthcare Standards & Compliance: innovaccer/Healthcare-MCP (28 stars, Python, MIT — HMCP specification extending MCP for HIPAA compliance with OAuth 2.0/SMART-on-FHIR/audit logging), Cicatriiz/pophive-mcp-server (17 stars, JavaScript — Yale PopHIVE public health surveillance data with 11 datasets). Rating: 4.0/5."
og_description: "Healthcare & Medical MCP servers: Cicatriiz/healthcare-mcp-public (101 stars, JavaScript — 9 tools for FDA/PubMed/clinical trials/ICD-10/DICOM), wso2/fhir-mcp-server (98 stars, Python, Apache-2.0 — FHIR CRUD with SMART-on-FHIR auth), JackKuo666/PubMed-MCP-Server (104 stars, Python, MIT — PubMed search/analysis/PDF download), ChristianHinge/dicom-mcp (86 stars, Python, MIT — 11 tools for DICOM/PACS query/move), JamesANZ/medical-mcp (75 stars, TypeScript, MIT — 15 tools for FDA/WHO/PubMed/RxNorm), jmandel/health-record-mcp (75 stars, TypeScript, MIT — SMART on FHIR EHR access), cyanheads/clinicaltrialsgov-mcp-server (58 stars, TypeScript — 7 tools for trial search/analysis/patient matching). 30+ servers reviewed. Rating: 4.0/5."
content_type: "Review"
card_description: "Healthcare and medical MCP servers across FHIR/EHR integration, medical research, multi-source healthcare hubs, drug databases, medical imaging, and healthcare standards. The healthcare MCP landscape is surprisingly mature for a regulated industry. FHIR integration leads the category with multiple competing implementations — WSO2's server (98 stars) exposes any FHIR server as MCP with full CRUD operations and SMART-on-FHIR authentication, while health-record-mcp (75 stars) takes an innovative approach with grep, SQL, and JavaScript query tools over EHR data. The Momentum's FHIR server (68 stars) adds Pinecone vector search for semantic retrieval across clinical documents. AWS HealthLake MCP (part of the 8.5K-star awslabs/mcp repo) brings enterprise backing with 11 tools, automatic datastore discovery, and read-only mode for production safety. LangCare (15 stars, Go) targets enterprise deployments with TLS 1.3, PHI scrubbing, and a 40+ clinical skills library. Medical research servers are the most polished subcategory. PubMed-MCP-Server (104 stars) provides deep paper analysis with PDF downloads. The ClinicalTrials.gov server by cyanheads (58 stars) offers patient-to-trial matching, trend analysis, and study comparison with 92% test coverage. Medical-mcps (14 stars) is the most ambitious — unifying 14 biomedical APIs (PubMed, OpenFDA, KEGG, UniProt, GWAS Catalog, ChEMBL, and more) into 100+ tools through a single endpoint. Multi-source healthcare hubs aggregate multiple medical APIs into single servers — healthcare-mcp-public (101 stars, most starred in the category) bundles FDA drugs, PubMed, clinical trials, ICD-10 codes, DICOM metadata, and a medical calculator. Medical-mcp (75 stars) provides 15 tools across FDA, WHO, PubMed, Google Scholar, and RxNorm with zero API keys required. Drug and pharmacology servers include DrugBank MCP (17,000+ drugs with interaction/pathway/structure search) and NLM Codes MCP (ICD-10/ICD-11/HCPCS/LOINC/RxTerms via the NLM Clinical Tables API). Medical imaging is represented by ChristianHinge/dicom-mcp (86 stars) with 11 tools for querying patients/studies/series on PACS systems, moving DICOM data between nodes, and extracting PDF reports from DICOM files. Healthcare standards are evolving — Innovaccer's HMCP specification (28 stars) extends MCP with HIPAA compliance, OAuth 2.0, and audit logging as a dedicated healthcare protocol layer. PopHIVE (17 stars) provides public health surveillance data from Yale. The category earns 4.0/5 — the breadth is impressive with every major healthcare data domain covered, FHIR integration has strong competition driving quality, research servers are production-ready, and vendor participation (AWS, WSO2, Innovaccer, LangCare) signals institutional confidence. The gaps: no Epic or Cerner official MCP servers yet, medical imaging is limited to DICOM metadata (no actual image analysis), mental health and genomics are nearly absent, and most servers lack HIPAA compliance documentation despite handling PHI."
last_refreshed: 2026-03-15
---

Healthcare and medical MCP servers are connecting AI agents to the full spectrum of clinical and biomedical data. Instead of navigating complex FHIR APIs, searching PubMed manually, or learning DICOM protocols, these servers let agents query patient records, search medical literature, look up drug interactions, browse clinical trials, and interact with imaging systems — all through the Model Context Protocol.

The landscape spans six areas: **FHIR/EHR integration** (multiple competing implementations for accessing electronic health records), **medical research** (PubMed and ClinicalTrials.gov access), **multi-source healthcare hubs** (servers bundling FDA, PubMed, ICD-10, and more), **drug and pharmacology databases** (DrugBank, RxNorm, NLM codes), **medical imaging** (DICOM/PACS interaction), and **healthcare standards** (HIPAA-compliant protocol extensions and public health data).

The headline findings: **PubMed-MCP-Server is the most starred research server** at 104 stars with deep paper analysis and PDF downloads. **Healthcare-mcp-public is the most starred healthcare hub** at 101 stars, bundling 9 tools across FDA, PubMed, clinical trials, ICD-10, and DICOM. **WSO2's FHIR server leads EHR integration** at 98 stars with SMART-on-FHIR auth. **DICOM-mcp is the sole serious imaging server** at 86 stars with 11 tools for PACS interaction. **Medical-mcps unifies 14 biomedical APIs** into 100+ tools through a single endpoint. **No major EHR vendor (Epic, Cerner) has released an official MCP server** despite strong community demand. **Innovaccer's HMCP proposes a healthcare-specific MCP extension** for HIPAA compliance and multi-agent clinical workflows.

## FHIR / EHR Integration

### wso2/fhir-mcp-server (Most Popular FHIR Server)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [wso2/fhir-mcp-server](https://github.com/wso2/fhir-mcp-server) | 98 | Python | Apache-2.0 | 7 |

WSO2's open-source FHIR MCP server is the most starred FHIR-specific implementation. Its key value proposition: **expose any FHIR server or API as an MCP server** without custom coding. Provides full CRUD operations on FHIR resources:

- **get_capabilities** — retrieve metadata about available FHIR resource types
- **search** — execute FHIR search interactions with full parameter support
- **read** — retrieve individual resources by type and ID
- **create / update / delete** — full write operations on FHIR resources
- **get_user** — retrieve the authenticated user's FHIR profile

Supports three transport modes (stdio, SSE, streamable HTTP) with SMART-on-FHIR authentication. Compatible with Claude Desktop, VS Code, and MCP Inspector. The Python package installs via pip, making setup straightforward.

### jmandel/health-record-mcp (Innovative Query Interface)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jmandel/health-record-mcp](https://github.com/jmandel/health-record-mcp) | 75 | TypeScript | MIT | 3 |

Takes a fundamentally different approach to EHR access. Instead of exposing FHIR operations directly, it provides **three powerful query tools** that let agents explore clinical data flexibly:

- **grep_record** — text/regex search across all record data
- **query_record** — read-only SQL SELECT queries on FHIR data
- **eval_record** — custom JavaScript execution on fetched data

Uses SMART on FHIR standards for secure EHR connection via the SMART App Launch flow. Supports standalone web client, local stdio MCP server, and experimental SSE server modes. This design means agents can answer complex clinical questions without needing to know FHIR query syntax — they can write SQL or grep for patterns across the entire patient record.

### the-momentum/fhir-mcp-server (Vector Search + FHIR)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [the-momentum/fhir-mcp-server](https://github.com/the-momentum/fhir-mcp-server) | 68 | Python | MIT | 11 |

The Momentum's FHIR server combines traditional FHIR resource access with **AI-powered document search**. Beyond the 8 FHIR resource tools (patient, observation, condition, medication, immunization, encounter, allergy, generic), it adds:

- **add_document_to_pinecone** — ingest clinical documents into vector database
- **search_pinecone** — semantic search across stored documents using embeddings
- **get_loinc_codes** — medical observation standardization

This RAG-ready architecture means agents can semantically search clinical notes, discharge summaries, and other unstructured documents alongside structured FHIR data. Supports OAuth2 authentication, multi-format document ingestion (TXT, CSV, JSON, PDF), and Docker deployment.

### AWS HealthLake MCP Server (Enterprise Cloud)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [awslabs/mcp (HealthLake)](https://github.com/awslabs/mcp/tree/main/src/healthlake-mcp-server) | 8,500+ (repo) | Python | Apache-2.0 | 11 |

Part of AWS's official MCP server collection, the HealthLake MCP server provides **11 tools for FHIR resource management** with enterprise-grade features:

- **Automatic datastore discovery** — no manual configuration of HealthLake datastores
- **Read-only mode** — blocks all mutations for production/audit environments
- **Advanced search** — chained parameters, includes, revIncludes, modifiers, pagination
- **FHIR job management** — import and export operations
- **Patient-everything** — comprehensive patient data retrieval

Built with AWS SigV4 authentication, 235 tests with 96% coverage. The read-only mode is a thoughtful safety feature missing from most healthcare MCP servers — essential for deployments where AI agents should observe but not modify clinical data.

### langcare/langcare-mcp-fhir (Enterprise EHR Proxy)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [langcare/langcare-mcp-fhir](https://github.com/langcare/langcare-mcp-fhir) | 15 | Go | — | 4 |

An enterprise-grade MCP server designed as a **stateless proxy to any FHIR R4 EMR** — Epic, Cerner, or GCP Healthcare API. Written entirely in Go for performance, with security features unusual in the MCP ecosystem:

- **TLS 1.3 encryption** — all communications encrypted in transit
- **PHI scrubbing in logs** — protected health information automatically removed from log output
- **HIPAA-compliant audit logging** — comprehensive activity tracking
- **OAuth2 support** — works with Epic, Cerner, and GCP authentication flows

Ships with a **40+ Clinical Skills Library** — agent-agnostic workflow guides covering medication management, lab interpretation, clinical decision support, documentation, and population health. Also includes embedded React-based MCP Apps (FHIR Explorer, Patient Chart Review) that render directly in compatible clients.

### rkirkendall/medplum-mcp (Most Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rkirkendall/medplum-mcp](https://github.com/rkirkendall/medplum-mcp) | 14 | TypeScript | MIT | 33 |

The most tool-rich FHIR server with **33 dedicated tools** covering 8 FHIR resource types. Each resource gets full CRUD operations plus search — Patient, Practitioner, Organization, Encounter, Observation, MedicationRequest, Medication, and EpisodeOfCare. Also includes a general `generalFhirSearch` tool for querying any resource type. Designed specifically for the Medplum open-source healthcare platform.

## Medical Research

### JackKuo666/PubMed-MCP-Server (Most Popular Research Server)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [JackKuo666/PubMed-MCP-Server](https://github.com/JackKuo666/PubMed-MCP-Server) | 104 | Python | MIT | 5 |

The most starred medical research MCP server and a critical tool for biomedical literature access. Bridges AI assistants with PubMed's database of 30+ million citations:

- **search_pubmed_key_words** — keyword-based article search
- **search_pubmed_advanced** — advanced parameter-based queries
- **get_pubmed_article_metadata** — rapid metadata retrieval
- **download_pubmed_pdf** — full-text PDF download when available
- **deep_paper_analysis** — comprehensive paper analysis with structured output

The PDF download and deep analysis tools set this apart from basic PubMed search — agents can retrieve full papers and extract structured insights, not just titles and abstracts.

### cyanheads/clinicaltrialsgov-mcp-server (Best Clinical Trials Access)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cyanheads/clinicaltrialsgov-mcp-server](https://github.com/cyanheads/clinicaltrialsgov-mcp-server) | 58 | TypeScript | Apache-2.0 | 7 |

The most sophisticated ClinicalTrials.gov MCP server, going well beyond basic search with analytical capabilities:

- **clinicaltrials_search_studies** — full-text and filtered search with geographic proximity
- **clinicaltrials_get_study** — batch retrieval of up to 5 studies by NCT ID
- **clinicaltrials_get_study_results** — outcomes and adverse events for completed trials
- **clinicaltrials_analyze_trends** — statistical aggregation across up to 5,000 studies
- **clinicaltrials_compare_studies** — side-by-side analysis of 2-5 trials
- **clinicaltrials_find_eligible_studies** — patient-to-trial matching with location-based sorting
- **clinicaltrials_get_field_values** — enum value discovery with study count frequency

The patient-to-trial matching tool is particularly valuable for clinical research coordinators — it can find eligible trials for a patient based on their conditions and location. 92% test coverage and Cloudflare Workers deployment show production-quality engineering.

### pascalwhoop/medical-mcps (Most Comprehensive Biomedical)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pascalwhoop/medical-mcps](https://github.com/pascalwhoop/medical-mcps) | 14 | Python | MIT | 100+ |

The most ambitious medical MCP server, unifying **14 biomedical APIs into 100+ tools** through a single endpoint:

- **Literature:** PubMed/PubTator3 for article search and annotation
- **Drugs:** OpenFDA for adverse events and drug labels, ChEMBL for compound data
- **Genetics:** MyVariant.info for variant annotation, GWAS Catalog for genome-wide associations
- **Proteins:** UniProt for protein data, MyGene.info for gene information
- **Pathways:** Reactome, KEGG, and Pathway Commons for biological pathway analysis
- **Disease:** OMIM and MyDisease.info for disease-gene relationships
- **Clinical trials:** ClinicalTrials.gov and NCI Clinical Trials APIs
- **Knowledge graphs:** Every Cure Matrix, OpenTargets Platform

Available as a unified cloud endpoint. This is a research powerhouse — a single MCP connection gives agents access to the major biomedical databases that researchers typically access through dozens of different interfaces.

### JackKuo666/ClinicalTrials-MCP-Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [JackKuo666/ClinicalTrials-MCP-Server](https://github.com/JackKuo666/ClinicalTrials-MCP-Server) | 15 | Python | MIT | 7 |

A Python-focused ClinicalTrials.gov server with **CSV export capabilities** — search trials, get full study details, generate statistics, and save results to CSV files for offline analysis. Also provides MCP resources for direct data access. A lighter alternative to the cyanheads server when you need data export more than analytical tools.

## Multi-Source Healthcare Hubs

### Cicatriiz/healthcare-mcp-public (Most Starred Healthcare Server)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Cicatriiz/healthcare-mcp-public](https://github.com/Cicatriiz/healthcare-mcp-public) | 101 | JavaScript | MIT | 9 |

The most starred healthcare-specific MCP server, providing a **single entry point to multiple medical data sources**:

- **FDA Drug Information** — search and retrieve drug data with multiple search types (general, label, adverse events)
- **PubMed Research** — medical literature search with date range filtering
- **Health Topics** — evidence-based health information from Health.gov (English/Spanish)
- **Clinical Trials** — search with status filtering and eligibility details
- **Medical Terminology (ICD-10)** — diagnosis code lookup by code or description
- **medRxiv Search** — pre-print biomedical articles
- **NCBI Bookshelf Search** — biomedical books and reference materials
- **DICOM Metadata Extraction** — parse metadata from medical imaging files
- **Medical Calculator** — BMI calculation

The breadth makes this ideal as a general-purpose medical assistant backend. Features caching, connection pooling, both HTTP/SSE and stdio interfaces, and Swagger UI documentation. 72 commits show steady development.

### JamesANZ/medical-mcp (No API Keys Needed)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [JamesANZ/medical-mcp](https://github.com/JamesANZ/medical-mcp) | 75 | TypeScript | MIT | 15 |

Differentiates with **zero API key requirements** — every data source is freely accessible, making setup trivial. Provides 15 tools across multiple medical domains:

- **Drug tools** — search drugs, get details, search nomenclature via FDA and RxNorm
- **Literature** — PubMed (30M+ articles), Google Scholar, multi-database search
- **Statistics** — WHO health statistics by country
- **Pediatrics** — AAP guidelines, pediatric drug search, child health statistics
- **Clinical guidelines** — evidence-based clinical guideline search

Runs 100% locally with no tracking, no logs, no cloud dependency. The pediatric focus is unique in the category — no other server provides dedicated AAP guideline and pediatric literature search tools.

## Drug & Pharmacology

### openpharma-org/drugbank-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [openpharma-org/drugbank-mcp-server](https://github.com/openpharma-org/drugbank-mcp-server) | 2 | JavaScript | MIT | 16 methods |

Access to **17,430+ pharmaceutical records** via a high-performance SQLite backend. A single `drugbank_info` tool exposes 16 search methods:

- Search by name, indication, target, ATC code, structure, category, carrier, transporter, half-life
- Get drug details, interactions (drug-drug and food), pathways, products, external identifiers, salts, similar drugs

Covers 13,166 small molecule drugs plus 4,264 biotech compounds. The SQLite backend means fast queries with minimal memory overhead — no external API calls needed. Drug interaction lookup is particularly valuable for clinical decision support.

### openpharma-org/nlm-codes-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [openpharma-org/nlm-codes-mcp](https://github.com/openpharma-org/nlm-codes-mcp) | 0 | TypeScript | MIT | 11 methods |

Provides access to **clinical coding systems** via the NLM Clinical Tables API. A single `nlm_ct_codes` tool supports 11 medical coding systems: ICD-10-CM, ICD-11, HCPCS Level II, NPI (organizations and individuals), HPO vocabulary, conditions, RxTerms, LOINC questions, NCBI genes, and major surgeries/implants. Essential for billing, clinical documentation, and regulatory compliance workflows.

### johnyquest7/Medical_calculator_MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [johnyquest7/Medical_calculator_MCP](https://github.com/johnyquest7/Medical_calculator_MCP) | 2 | Python | MIT | — |

A focused MCP server for medical calculations — BMI, GFR, dosage calculations, and other clinical formulas. Integrates with Claude Desktop for clinical decision support.

## Medical Imaging

### ChristianHinge/dicom-mcp (Most Popular Imaging Server)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ChristianHinge/dicom-mcp](https://github.com/ChristianHinge/dicom-mcp) | 86 | Python | MIT | 11 |

The leading medical imaging MCP server, enabling AI agents to interact with **DICOM servers (PACS, VNA, etc.)**. Provides 11 tools across four categories:

**Querying:**
- **query_patients** — search by name, ID, birth date
- **query_studies** — find studies by patient ID, date, modality
- **query_series** — locate series within studies
- **query_instances** — find individual DICOM instances

**Data Movement:**
- **move_series / move_study** — send DICOM data to other configured nodes

**Document Extraction:**
- **extract_pdf_text_from_dicom** — extract text from PDF reports stored as DICOM objects

**Utilities:**
- **list_dicom_nodes / switch_dicom_node** — manage DICOM node connections
- **verify_connection** — test connectivity
- **get_attribute_presets** — retrieve query attribute configurations

The server requires a YAML configuration defining DICOM nodes and calling AE titles. This enables complex workflows like "find all MRI studies for patient X from the last 6 months, then move them to the research PACS" — tasks that normally require specialized DICOM tooling.

### fluxinc/dicom-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [fluxinc/dicom-mcp-server](https://github.com/fluxinc/dicom-mcp-server) | 3 | Python | LGPL-2.1 | 3 |

A lighter DICOM server focused on **connectivity testing** — list nodes, C-ECHO by node name, and direct C-ECHO. Useful for verifying DICOM network configurations but lacks the query and data movement capabilities of ChristianHinge's server.

## Healthcare Standards & Public Health

### innovaccer/Healthcare-MCP (HMCP Specification)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [innovaccer/Healthcare-MCP](https://github.com/innovaccer/Healthcare-MCP) | 28 | Python | MIT | — |

Not a tool server but a **protocol specification** — the Healthcare Model Context Protocol (HMCP) extends MCP with healthcare-specific capabilities:

- **HIPAA-compliant security** — access management with comprehensive audit trails
- **OAuth 2.0 / SMART on FHIR** — client credentials and authorization code with PKCE flows
- **Multi-agent workflows** — bidirectional agent-to-agent communication via sampling endpoints
- **Patient context isolation** — based on SMART on FHIR specifications

HMCP addresses the biggest gap in healthcare MCP adoption: there's no standard way to ensure MCP servers handling PHI meet regulatory requirements. Innovaccer provides both the specification and an SDK (HMCPServer, HMCPClientConnector) for building compliant implementations. Still early (28 stars) but could become foundational as healthcare MCP adoption grows.

### Keragon Healthcare MCP (HIPAA-Compliant Platform)

Keragon offers a **commercial healthcare MCP platform** purpose-built for regulated environments:

- **300+ healthcare integrations** — EHRs, billing platforms, CRMs, scheduling systems
- **Least-privilege access control** — define exactly what data each AI agent can access, down to specific fields
- **End-to-end audit logging** — every tool call and payload logged for compliance
- **HIPAA-compliant by design** — built for regulated healthcare from the ground up

Currently in beta with 100 free tool calls per day. Unlike open-source alternatives, Keragon handles the compliance infrastructure so developers can focus on clinical workflows rather than security architecture.

### Cicatriiz/pophive-mcp-server (Public Health Surveillance)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Cicatriiz/pophive-mcp-server](https://github.com/Cicatriiz/pophive-mcp-server) | 17 | JavaScript | — | 5 |

Provides access to **Yale School of Public Health's PopHIVE** surveillance data — 11 datasets covering immunizations, respiratory diseases, chronic diseases, hospital capacity, injury/overdose tracking, and youth mental health. Featured on Claude. Tools include filter by state/demographics, compare states with statistical analysis, time series trend analysis, dataset catalog, and cross-dataset search. Production-ready for population health research.

## What's Missing

The healthcare MCP ecosystem has impressive breadth but notable gaps:

- **No official EHR vendor servers** — neither Epic nor Cerner has released an MCP server, despite both having extensive FHIR APIs. Community servers bridge the gap but lack vendor support.
- **Medical imaging limited to metadata** — DICOM servers query and move imaging data but can't analyze images. No integration with medical imaging AI models (MedGemma, RadImageNet, etc.).
- **Genomics nearly absent** — MyVariant.info is available through medical-mcps but there's no dedicated genomics MCP server for 23andMe, gnomAD, or clinical sequencing data.
- **Mental health gap** — the only mental health MCP server (mcp-ai-therapy) is an AI therapy chatbot, not a clinical tool. No servers for PHQ-9 screening, therapy note management, or psychiatric assessment tools.
- **HIPAA compliance unclear** — most servers handle PHI but don't document their compliance posture. Only LangCare, Keragon, and HMCP explicitly address HIPAA.
- **No pharmacy workflow servers** — drug databases exist but there's nothing for e-prescribing, medication reconciliation, or pharmacy management systems.

## The Bottom Line

**Rating: 4.0 / 5**

Healthcare MCP servers earn a strong rating thanks to impressive breadth — every major healthcare data domain has at least one MCP server, from EHR access to drug databases to medical imaging to public health surveillance. The FHIR subcategory has genuine competition (6+ implementations) driving quality and innovation. Medical research servers are polished and practical — PubMed-MCP-Server and the ClinicalTrials.gov server are production-ready tools that genuinely accelerate biomedical research workflows.

What elevates this category: vendor participation is strong (AWS, WSO2, Innovaccer, LangCare, Keragon) and the HMCP specification signals that healthcare-specific standards are being developed rather than ignored. Multi-source hubs like healthcare-mcp-public (101 stars) and medical-mcp (75 stars) lower the barrier to entry by bundling multiple APIs into single servers.

What holds it back from 4.5: the absence of official EHR vendor servers creates reliance on community bridges, medical imaging stops at DICOM metadata without actual image analysis, compliance documentation is spotty across most projects, and specialized clinical domains (mental health, genomics, pharmacy workflows) are underserved. The technology is there — the regulatory and vendor ecosystem is still catching up.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
