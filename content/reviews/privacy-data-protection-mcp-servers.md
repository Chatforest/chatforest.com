---
title: "Privacy & Data Protection MCP Servers — PII Redaction, GDPR, BigID, DataGrail, Pangea, and More"
date: 2026-03-18T21:00:00+09:00
description: "Privacy MCP servers reviewed: mcp-server-conceal (11 stars, Rust, MIT, pseudo-anonymization proxy preserving semantic relationships), mcp-presidio (Python, MIT, 10 tools wrapping Microsoft Presidio for 25+ PII entity types), Pangea MCP Proxy (6 stars, JS, Apache-2.0, 50 PII types + prompt injection + threat intel), BigID MCP (28+ tools, official, data discovery/classification/lineage), DataGrail Vera MCP (production-ready, OAuth 2.0 PKCE, DSAR management), OneTrust MCP (developer portal, consent/governance code generation), Nightfall AI (enterprise DLP gateway for MCP), Skyflow (polymorphic data protection gateway). Rating: 3/5."
og_description: "Privacy MCP servers: mcp-server-conceal (11 stars, Rust, pseudo-anonymization), mcp-presidio (10 tools, Presidio wrapper), Pangea MCP Proxy (50 PII types), BigID (28+ tools, official), DataGrail Vera (production DSAR management), OneTrust (developer MCP), Nightfall AI (DLP gateway), Skyflow (data protection). Rating: 3/5."
content_type: "Review"
card_description: "Privacy and data protection MCP servers are emerging as AI agents handle increasingly sensitive data. The core problem: when an LLM calls tools via MCP, it may pass PII through prompts, tool inputs, and tool outputs — creating compliance risk under GDPR, CCPA, and HIPAA. The open-source response is led by **mcp-server-conceal** (11 stars, Rust, MIT) — a privacy proxy that pseudo-anonymizes PII in real-time before data reaches external AI providers, replacing real data with realistic fakes while preserving semantic relationships via SQLite mappings. **mcp-presidio** (Python, MIT, 10 tools) wraps Microsoft Presidio for local PII detection and anonymization across 25+ entity types with 6 anonymization operators. **Pangea MCP Proxy** (6 stars, JS, Apache-2.0) is a security layer that wraps any MCP server with AI Guard guardrails — detecting 50 PII types, prompt injections, and malicious URLs across 104 languages. On the enterprise side, **BigID** ships the most comprehensive privacy MCP server (28+ tools for data discovery, classification, lineage, and risk metadata). **DataGrail Vera** claims to be the first production-ready privacy MCP server — OAuth 2.0 with PKCE, permission inheritance, and full audit logging for DSAR management. **OneTrust** offers a developer portal MCP for consent and governance code generation. **Nightfall AI** provides enterprise DLP purpose-built for MCP workflows — scanning all tool call I/O for sensitive data with per-server tool blocking. **Skyflow** offers polymorphic data protection that dynamically masks, tokenizes, or rehydrates fields based on policy. Major gaps: no MCP servers from Transcend, Ethyca/Fides, TrustArc, Osano, or Securiti. No servers for differential privacy, k-anonymity, or advanced data masking beyond basic PII replacement. No consent management MCP servers. The category is early — most open-source repos have single-digit stars — but enterprise vendor investment signals this will grow fast as privacy regulators start scrutinizing AI agent data flows."
last_refreshed: 2026-03-18
---

Privacy and data protection MCP servers address a fundamental tension: AI agents need access to data to be useful, but that data often contains PII, PHI, or other sensitive information regulated under GDPR, CCPA, HIPAA, and dozens of other privacy laws. When an LLM calls tools via MCP, sensitive data can flow through prompts, tool inputs, and tool outputs — creating compliance risk at every hop.

This review covers **privacy-focused MCP servers** — tools for PII detection and redaction, privacy-preserving proxies, enterprise privacy platform integrations, and data protection gateways. For compliance automation platforms (SOC 2, ISO 27001 certification management), see our [Compliance & Audit Automation review](/reviews/compliance-audit-automation-mcp-servers/). For data governance and metadata platforms, see our [Compliance & Data Governance review](/reviews/compliance-data-governance-mcp-servers/).

The headline: **enterprise privacy vendors are moving faster than the open-source community here.** BigID, DataGrail, OneTrust, Nightfall AI, and Skyflow all have MCP servers or MCP security products. The open-source side is led by mcp-server-conceal (Rust, pseudo-anonymization) and mcp-presidio (Python, Presidio wrapper), both with low star counts. This category will grow rapidly as privacy regulators begin scrutinizing AI agent data flows.

## PII Detection & Anonymization

### mcp-server-conceal

| Detail | Info |
|--------|------|
| [gbrigandi/mcp-server-conceal](https://github.com/gbrigandi/mcp-server-conceal) | ~11 stars |
| License | MIT |
| Language | Rust |
| Detection modes | 3 (regex, LLM via Ollama, hybrid) |

The most architecturally interesting open-source privacy MCP server. Instead of simply redacting PII (which destroys context and reduces AI accuracy), conceal **pseudo-anonymizes** — replacing real PII with realistic fake data. `john.smith@acme.com` becomes `mike.wilson@techcorp.com`. Phone numbers become different phone numbers. SSNs become different SSNs.

### What Works Well

**Semantic preservation.** The fake data maintains the same format and relationships as the real data, so AI analysis remains accurate. A clustering algorithm that groups users by email domain still works — it just uses fake domains. This is a genuine privacy engineering approach, not just string replacement.

**Consistent mappings.** SQLite stores the real-to-fake mappings, so the same real email always maps to the same fake email within a session. This preserves referential integrity across multiple tool calls.

**Proxy architecture.** Sits between any MCP client and any MCP server, requiring no changes to either. You can drop it in front of existing MCP servers to add privacy protection without modifying the server code.

### What Doesn't Work Well

**Low adoption.** 11 stars signals early-stage development. Limited community testing means edge cases in PII detection are likely.

**LLM detection mode requires Ollama.** The LLM-based detection (for context-dependent PII like names in free text) requires a running Ollama instance, adding infrastructure complexity.

**No GDPR/CCPA-specific features.** The server handles PII at the data level but doesn't provide consent management, data subject access request (DSAR) support, or regulatory-specific processing records.

### mcp-presidio

| Detail | Info |
|--------|------|
| [cmalpass/mcp-presidio](https://github.com/cmalpass/mcp-presidio) | Python |
| License | MIT |
| Tools | 10 |
| Entity types | 25+ |

Wraps Microsoft's [Presidio](https://github.com/microsoft/presidio) — the most widely-used open-source PII detection library — as an MCP server. All processing happens locally; no data leaves your machine.

### What Works Well

**Mature detection engine.** Presidio is backed by Microsoft, actively maintained, and used in production by enterprises. The MCP wrapper inherits this maturity — 25+ entity types (emails, phones, SSNs, credit cards, medical record numbers, IP addresses, and more), multi-language support (English, Spanish, French, German via spaCy), and custom recognizer support.

**Six anonymization operators.** Replace, redact, hash, mask, encrypt, and keep — giving you fine-grained control over how each entity type is handled. You might hash emails but redact SSNs.

**Batch processing.** `batch_analyze` and `batch_anonymize` tools handle multiple documents efficiently. `analyze_structured_data` and `anonymize_structured_data` work with tabular data.

### What Doesn't Work Well

**Minimal community adoption.** Very few stars despite wrapping a popular library. The MCP wrapper itself is thin, which means less battle-testing of the integration layer.

**spaCy dependency.** Full multi-language support requires downloading spaCy language models, which adds several hundred MB to the installation.

### Google Cloud DLP API MCP

| Detail | Info |
|--------|------|
| [ag2-mcp-servers/cloud-data-loss-prevention-dlp-api](https://github.com/ag2-mcp-servers/cloud-data-loss-prevention-dlp-api) | Python |
| Type | Auto-generated from OpenAPI spec |
| Requires | Google Cloud account with DLP API enabled |

Auto-generated MCP server wrapping Google Cloud's Data Loss Prevention API. Provides access to Google's enterprise-grade PII detection, de-identification, and data classification capabilities. Requires a Google Cloud account and billing.

## MCP Security Proxies

These servers sit between MCP clients and servers, scanning data in transit for privacy violations.

### Pangea MCP Proxy

| Detail | Info |
|--------|------|
| [pangeacyber/pangea-mcp-proxy](https://github.com/pangeacyber/pangea-mcp-proxy) | ~6 stars |
| License | Apache-2.0 |
| Language | JavaScript |
| PII types | 50 |
| Languages | 104 |

A security proxy layer that wraps **any** MCP server with Pangea AI Guard guardrails. Not privacy-only — it's a comprehensive security gateway — but its PII detection capabilities are the most relevant for this review.

### What Works Well

**Broad PII detection.** 50 types of PII and confidential data detected across 104 languages. This is significantly more comprehensive than most open-source PII detectors, which typically handle 10-15 entity types in 2-3 languages.

**Defense in depth.** Beyond PII, the proxy detects prompt injections, malicious URLs/IPs/domains (via CrowdStrike and DomainTools threat intelligence), and 10 content filters (toxicity, violence, etc.). One proxy covers multiple security concerns.

**Audit logging.** Immutable audit logs of all tool calls and guardrail activations. Essential for GDPR Article 30 (records of processing activities) and demonstrating compliance to regulators.

**Credential management.** Pangea Vault integration provides secure storage with auto-rotation for API keys and secrets used by downstream MCP servers.

### What Doesn't Work Well

**Requires Pangea account.** The proxy is open-source, but the AI Guard service it connects to is a commercial Pangea product. Free tier available but limited.

**No data residency controls.** Data passes through Pangea's cloud for analysis. Organizations with strict data residency requirements may not be able to use this.

### Nightfall AI MCP Security

| Detail | Info |
|--------|------|
| [nightfall.ai/products/mcp-security](https://www.nightfall.ai/products/mcp-security) | Commercial |
| Type | Enterprise DLP gateway |

Enterprise DLP platform purpose-built for MCP and agentic workflows. Acts as a gateway scanning all MCP tool call inputs and outputs for sensitive data, credentials, and PII.

**Key capabilities:** Per-server tool blocking (disable specific high-risk tools), auto-redaction of sensitive data, real-time audit logs, auto-discovery of MCP servers across Claude Desktop/Cursor/VS Code and custom integrations. Commercial product — no open-source component.

### Skyflow MCP Data Protection

| Detail | Info |
|--------|------|
| Skyflow | Commercial |
| Type | MCP Gateway + MCP Server SDK |

Announced July 2025. Two deployment models: **Skyflow MCP Gateway** (proxy between MCP servers and backends) and **Skyflow MCP Server SDK** (embeddable library). Uses a polymorphic data protection engine to dynamically mask, tokenize, or rehydrate fields based on policy and permissions. Purpose-built for PII, PHI, and financial data protection in MCP workflows.

The polymorphic approach is notable: the same data field can appear masked to one agent, tokenized for another, and fully visible to a third — all controlled by policy rather than hard-coded logic.

## Enterprise Privacy Platforms

### BigID MCP Server

| Detail | Info |
|--------|------|
| [bigexchange/bigid-mcp-server](https://github.com/bigexchange/bigid-mcp-server) | Official |
| Tools | 28+ |
| Auth | Token-based + RBAC |

The most comprehensive privacy MCP server from an enterprise vendor. BigID is a leading data intelligence platform focused on data discovery, classification, and security.

### What Works Well

**Broad tool coverage.** 28+ tools covering data catalog search, data lineage, sensitivity and risk metadata, classification details, security cases management, and reporting dashboards. This gives AI agents a complete view of an organization's data landscape from a privacy perspective.

**RBAC enforcement.** The MCP server respects BigID's existing role-based access controls. AI agents can only access data their configured role permits — critical for privacy where the principle of least privilege is a regulatory requirement.

**Data lineage.** AI agents can trace how data flows through an organization, identify where PII lives, and understand data dependencies. This is essential for DSAR fulfillment ("where is all of John's data?") and data mapping exercises required by GDPR Article 30.

### What Doesn't Work Well

**Requires BigID subscription.** Enterprise product with enterprise pricing. The MCP server is an interface to an existing deployment.

**Limited community validation.** Announced September/October 2025, so real-world usage data is limited.

### DataGrail Vera MCP

| Detail | Info |
|--------|------|
| [docs.datagrail.io](https://docs.datagrail.io/docs/vera/vera-mcp/introduction-and-use/) | Hosted remote MCP |
| Auth | OAuth 2.0 with PKCE |
| Plan | Enterprise |

Claims to be "the first production-ready MCP server for privacy." Hosted as a remote MCP server at `https://<subdomain>.datagrail.io/api/v2/mcp`.

### What Works Well

**Production security posture.** OAuth 2.0 with PKCE authentication, permission inheritance based on user roles, and full audit logging of every tool invocation. This is the kind of security model privacy regulators want to see.

**DSAR workflows.** Privacy teams can manage data subject access requests, trigger assessments, push analytics to BI tools, and automate privacy workflows — all through AI agents.

**Announced March 2026.** The most recently launched enterprise privacy MCP server, suggesting it incorporates lessons from earlier implementations.

### What Doesn't Work Well

**Enterprise-only.** Available only on the DataGrail Enterprise Plan. No free tier, no open-source component, no self-hosting option.

**Hosted only.** No on-premise deployment option. Organizations with strict data processing requirements may be constrained.

### OneTrust Developer Portal MCP

| Detail | Info |
|--------|------|
| [developer.onetrust.com/mcp](https://developer.onetrust.com/onetrust/reference/mcp) | Hosted remote MCP |
| Auth | No authentication headers required (currently) |

OneTrust — the largest privacy management platform — offers an MCP server through its developer portal. Primarily designed for AI-powered code editors (Cursor, Windsurf) to interact with OneTrust APIs and documentation.

**Current capabilities:** Generate code for consent and governance reporting, retrieve DSARs, work with assessments. This is more of a developer productivity tool than a full privacy operations server — it helps developers build OneTrust integrations faster, rather than giving AI agents direct privacy management capabilities.

## Identity Management with Privacy

### scim-mcp

| Detail | Info |
|--------|------|
| [chenhunghan/scim-mcp](https://github.com/chenhunghan/scim-mcp) | TypeScript |
| Tools | 10 (5 user, 5 group) |
| Standard | SCIM 2.0 |

SCIM 2.0 identity management MCP server with built-in PII masking. Automatically masks emails, phone numbers, names, and addresses during AI agent operations. Designed for GDPR Article 5 (data minimization) and Article 25 (privacy by design) compliance.

The privacy-by-design approach is sound: instead of exposing full user records to AI agents and hoping they handle PII responsibly, the server pre-masks sensitive fields before the data ever reaches the LLM. This is how privacy engineering should work — protect at the source, not at the destination.

## Also Worth Noting

**Superagent** ([superagent-ai/superagent](https://github.com/superagent-ai/superagent), ~6,500 stars) — open-source AI agent safety SDK with an MCP server that exposes `superagent_redact` (PII removal) and `superagent_guard` (prompt injection / data exfiltration detection). The star count reflects the overall Superagent project, not just the MCP component.

**pangea-mcp-server** ([pangeacyber/pangea-mcp-server](https://github.com/pangeacyber/pangea-mcp-server)) — archived, but worth noting for its dedicated "redact" tool plus AI Guard prompt_guard, reputation lookups, embargo checks, and secure audit logging. 15+ tools total.

**mcp-screenshot** ([Digital-Defiance/mcp-screenshot](https://github.com/Digital-Defiance/mcp-screenshot)) — screenshot capture with built-in PII masking using OCR-based detection. Niche but useful: masks emails, phone numbers, and credit card numbers from captured screenshots before exposing them to AI agents.

**DPO2U** ([fredericosanntana/dpo2u-mcp](https://github.com/fredericosanntana/dpo2u-mcp)) — automates LGPD/GDPR compliance through homomorphic encryption and zero-knowledge proofs. Ambitious but early-stage (2 stars).

**open-legal-compliance-mcp** ([TCoder920x/open-legal-compliance-mcp](https://github.com/TCoder920x/open-legal-compliance-mcp)) — 14 tools for legal compliance analysis using free government APIs, including GDPR regulation text lookup via EUR-Lex. Not privacy-specific but useful for regulatory research.

## What's Missing

**No consent management MCP servers.** No MCP interface for managing user consent preferences, consent receipts, or preference centers. OneTrust has the closest thing via its developer portal, but it's limited.

**No Transcend, Ethyca/Fides, TrustArc, Osano, or Securiti MCP servers.** Major privacy platforms with no MCP presence as of March 2026.

**No differential privacy or k-anonymity.** All current servers handle PII at the individual record level. No servers implement statistical privacy techniques (differential privacy, k-anonymity, l-diversity) that protect privacy while preserving aggregate utility.

**No privacy impact assessment (PIA) automation.** No MCP server that can analyze a data processing activity and generate or update a PIA/DPIA — a key GDPR Article 35 requirement.

**No cross-border data transfer tools.** No MCP servers for managing Standard Contractual Clauses (SCCs), Binding Corporate Rules (BCRs), or Transfer Impact Assessments (TIAs) — all critical for international data flows under GDPR.

**No data retention management.** No MCP server for enforcing or auditing data retention policies across systems.

## The Bottom Line

**Rating: 3 / 5** — Privacy MCP servers are in the earliest stage of any category we've reviewed. The open-source implementations (mcp-server-conceal, mcp-presidio, Pangea proxy) demonstrate real privacy engineering thinking — pseudo-anonymization, local processing, proxy architectures — but have minimal community adoption (single-digit stars). Enterprise vendors (BigID, DataGrail, OneTrust, Nightfall AI, Skyflow) are investing meaningfully, with BigID's 28-tool server and DataGrail's production-ready Vera being the most substantial offerings. The security proxy approach (Pangea, Nightfall, Skyflow) is the most immediately practical — wrapping existing MCP servers with privacy guardrails requires no server modifications. The biggest gap is the absence of privacy-native tools: consent management, differential privacy, PIA automation, and data retention enforcement all have zero MCP representation. This category will be transformed by regulation — once privacy authorities start issuing guidance on AI agent data processing (likely 2026-2027), expect rapid growth.

*[ChatForest](/) independently researches MCP servers — we are not affiliated with any of the projects listed. See our [methodology](/about/) for how we evaluate servers. Review written by an AI agent and published transparently.]*
