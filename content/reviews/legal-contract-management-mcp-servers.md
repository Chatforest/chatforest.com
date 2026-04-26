---
title: "Legal & Contract Management MCP Servers — E-Signatures, Legal Research, Case Law, IP/Trademarks, and More"
date: 2026-03-15T11:30:00+09:00
description: "Legal and contract management MCP servers are bringing AI agents into law offices, contract workflows, and regulatory research. We reviewed 70+ servers across 7 subcategories."
og_description: "Legal & Contract Management MCP servers: 70+ servers across e-signatures (DocuSign official, PandaDoc official, SendForSign, SignNow, DocuSeal, Dropbox Sign, eID Easy 80+ qualified signature providers), legal research (U.S. legislation, CourtListener 3,352 courts, UK case law 22 stars, Lex API 219K acts, French/German/Dutch/Greek/Korean/Turkish/Japanese/Australian/Swiss/Danish/Polish/Argentine law databases, 61 EU regulations), legal reasoning (Cerebra Legal, LegalForge, Blawx, Open Agreements 40+ templates), IP/trademarks (USPTO 54 stars 52 tools, PatSnap, Google Patents, Marka Patent), compliance (HIPAA, FedRAMP, Ansvar EU 61 regulations, Ansvar US 130 statutes), contract management (Concord official CLM, Clio 3+ community servers), and legal operations (Corpo AI entity formation, legal spend analytics, semantic memory). Rating: 4.0/5."
content_type: "Review"
categories: ["/categories/government-legal/"]
card_description: "Legal and contract management MCP servers across e-signatures, legal research, case law, legal reasoning, IP/trademarks, compliance, contract management, and legal operations. This category stands out for its remarkable geographic diversity — we found jurisdiction-specific legal research servers for the United States, United Kingdom, France, Germany, Netherlands, Greece, Denmark, South Korea, Turkey, Japan, Australia, Switzerland, Poland, Argentina, Brazil, Indonesia, and the European Union. The biggest development since our initial review: DocuSign launched an official remote MCP server at mcp-d.docusign.com exposing its Intelligent Agreement Management platform, and PandaDoc released an official MCP server bundle — closing the two largest gaps in the e-signature subcategory. Concord became the first contract lifecycle management vendor with an official MCP server, and Clio now has 3+ community MCP servers for legal practice management. E-signature servers now cover ten platforms including eID Easy with 80+ qualified signature providers for eIDAS compliance. The Ansvar-Systems project systematically built compliance MCP servers for Dutch law (3,251 statutes), US federal law (130 statutes), EU regulations (61 acts), and Greek law (21,119 statutes) — all with remote endpoints and daily freshness checks. The UK gets strong coverage with a case law server (22 stars) and the Lex API MCP (219K acts, 70K judgments, 19 tools). Patent coverage expanded dramatically with riemannzeta/patent_mcp_server (54 stars, 52 tools across USPTO APIs) plus PatSnap and Google Patents servers. Open Agreements (30 stars) provides 40+ legal document templates (NDAs, SAFEs, NVCA docs) as signable DOCX. Corpo enables AI agents to form and govern Wyoming DAO LLCs — the first legal entity formation MCP server. The category earns 4.0/5, up from 3.5 — the vendor gap is closing fast (DocuSign, PandaDoc, Concord now have official servers), geographic coverage expanded to 17+ countries, and the patent and CLM subcategories have real depth. The remaining gaps: no LexisNexis, Westlaw, or Ironclad MCP servers, and no official Adobe Sign server."
last_refreshed: 2026-04-27
---

Legal and contract management MCP servers are bringing AI agents into law offices, contract workflows, and regulatory research. Instead of manually searching case law databases, preparing signature requests, or cross-referencing regulations across jurisdictions, these servers let AI assistants conduct legal research, manage contracts, process e-signatures, and analyze compliance requirements — all through the Model Context Protocol.

The landscape spans seven areas: **e-signature and document signing** (ten platforms including DocuSign and PandaDoc official servers), **legal research and case law** (the largest subcategory, with jurisdiction-specific servers covering 17+ countries), **legal reasoning and document generation** (enterprise analysis to automated legal documents to 40+ signable templates), **IP and trademarks** (USPTO with 54 stars and 52 tools, PatSnap, Google Patents, Turkish trademark office), **compliance and regulatory** (HIPAA, FedRAMP, 61 EU regulations, 130 US federal statutes), **contract management** (Concord CLM, Clio practice management), and **legal operations** (AI entity formation, spend analytics, semantic memory, court system integrations).

The headline findings: **The vendor gap is closing fast** — DocuSign launched an official remote MCP server at mcp-d.docusign.com, PandaDoc released an official MCP bundle, and Concord became the first CLM vendor with MCP support. **Legal research remains the strongest subcategory**, now covering 17+ countries including new Dutch (3,251 statutes), Greek (21,119 statutes), and UK (219K acts, 70K judgments) servers. **E-signature servers now cover ten platforms** including eID Easy with 80+ qualified signature providers for eIDAS compliance. **EU regulations expanded from 37 to 61 acts** through Ansvar-Systems' comprehensive compliance MCP. **Patent coverage exploded** with riemannzeta/patent_mcp_server reaching 54 stars and 52 tools across USPTO APIs. **Clio has 3+ community MCP servers** for legal practice management. **Open Agreements** (30 stars) provides 40+ legal document templates as signable DOCX files. **Geographic diversity expanded** from 14 to 17+ countries. **Corpo enables AI agents to form Wyoming DAO LLCs** — the first legal entity formation MCP server.

## E-Signature & Document Signing

### DocuSign Official MCP Server *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| DocuSign MCP (official) | — | — | — | — |

**The biggest gap in the original review — now filled.** DocuSign launched an official remote MCP server at `mcp-d.docusign.com/mcp`, exposing the Intelligent Agreement Management (IAM) platform to any MCP-compatible client. Agents can create and send envelopes for signature, check envelope status, query agreement metadata and key dates through Navigator, trigger Maestro workflows for multi-step approval processes, and retrieve AI-powered agreement insights. Compatible with Claude Desktop, Claude Code, ChatGPT, GitHub Copilot, and custom agent frameworks. DocuSign also partnered with Anthropic to bring capabilities directly into Claude Cowork. With over 1 million customers, this is by far the most widely-used platform in the legal MCP ecosystem. Currently in beta. Multiple community implementations also exist: luthersystems/mcp-server-docusign (Python, JWT auth, 8 tools), thisdot/docusign-navigator-mcp (TypeScript, MIT, Navigator queries), and CData's read-only connector.

### PandaDoc Official MCP Server *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [PandaDoc/pandadoc-mcpb](https://github.com/PandaDoc/pandadoc-mcpb) | — | JavaScript | MIT | — |

**The second biggest gap — also filled.** PandaDoc released an official MCP server bundle providing direct API access to documents, templates, contacts, and granular document components (fields, attachments, recipients). Agents can create and populate professional contracts, proposals, and reports by describing what they need in natural language. Uses the `.mcpb` bundle format (zip archives containing a local MCP server and manifest, similar to Chrome extensions). Compatible with Cursor, Windsurf, and Claude Desktop. Also includes documentation search and code generation capabilities for PandaDoc API usage.

### eID Easy MCP Server *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| eID Easy MCP | — | Node.js | Open source | — |

Qualified electronic signatures for AI agent workflows. Integrates with **80+ trusted signature providers** across simple, advanced, and qualified electronic signature levels — making it the most legally robust e-signature MCP server. Supports eIDAS compliance and the 2026 eCoC deadline for EU Digital Identity Wallets. Built-in fraud prevention. Where other e-signature MCP servers handle convenience signing, eID Easy enables identity-based signing with full legal recognition. Currently supports Claude Desktop with ChatGPT in beta.

### SendForSign MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| SendForSign MCP | — | — | — | — |

Official MCP server from SendForSign enabling AI agents to interact with document templates and e-signature workflows. Create contracts from templates, send documents for signature, and track signing status — all through natural language. The integration targets the growing demand for AI-assisted contract preparation where agents draft documents and route them for approval without manual dashboard navigation.

### SignNow MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| SignNow MCP | — | — | — | — |

Official MCP server from SignNow (an airSlate product) for comprehensive e-signature management. Covers template management, signature invites, embedded signing experiences, and document downloads. SignNow has over 28 million users, making this one of the larger platforms with MCP support. The embedded signing capability is notable — it allows building signing flows directly into AI-assisted workflows rather than redirecting users to external pages.

### caffeinebounce/docuseal-mcp-server (DocuSeal Integration)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [caffeinebounce/docuseal-mcp-server](https://github.com/caffeinebounce/docuseal-mcp-server) | — | — | — | — |

MCP server for DocuSeal, the open-source document signing platform. Manages document templates, creates and tracks signature requests, and monitors submission status. DocuSeal itself has 8,000+ GitHub stars as an open-source alternative to DocuSign, making this integration particularly relevant for self-hosted legal workflows. Agents can create signing flows from templates and track completion without switching between interfaces.

### bmbouter/mcp-dropbox-sign

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bmbouter/mcp-dropbox-sign](https://github.com/bmbouter/mcp-dropbox-sign) | — | — | — | — |

MCP server for the Dropbox Sign API (formerly HelloSign) supporting signature requests, template management, and signing workflows. Dropbox Sign is widely used in tech companies and integrates with the broader Dropbox ecosystem. This community-built server exposes the core signing API for AI agent access.

### esignaturescom/mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [esignaturescom/mcp-server](https://github.com/esignaturescom/mcp-server) | — | — | — | — |

Official MCP server from eSignatures.io facilitating contract and template management with customizable signing options. The platform focuses on simplicity — straightforward contract creation and signing without the complexity of enterprise CLM platforms.

### signbee/signbee-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [signbee/signbee-mcp](https://github.com/signbee/signbee-mcp) | — | — | — | — |

Document signing server for AI agents with markdown and PDF support plus certified delivery. The markdown support is distinctive — most e-signature platforms require pre-formatted documents, but signbee lets agents draft in markdown and convert to signable documents in one flow. Certified delivery provides legal proof that documents were received.

### e签宝 MCP Server (Chinese Market)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| esign-cn-open-source e签宝 MCP | — | — | — | — |

Chinese electronic signature platform MCP server supporting file uploads, PDF conversion, and complete signing workflows. e签宝 (eSign China) is one of the largest e-signature platforms in the Chinese market. This server bridges the gap for AI agents operating in Chinese legal and business contexts where domestic e-signature platforms are required for regulatory compliance.

## Legal Research & Case Law

This is the standout subcategory — and the most geographically diverse category in the entire MCP ecosystem. Community developers across 17+ countries have built MCP servers wrapping their national legal databases, giving AI agents access to legislation, case law, and judicial decisions across jurisdictions. Since March, major additions include the Netherlands (3,251 statutes), Greece (21,119 statutes), and the United Kingdom (219K acts, 70K judgments).

### JamesANZ/us-legal-mcp (U.S. Legislation)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [JamesANZ/us-legal-mcp](https://github.com/JamesANZ/us-legal-mcp) | — | — | — | — |

Comprehensive access to U.S. legislation through government APIs. Search federal statutes, browse the U.S. Code, and retrieve full text of legislative documents. Built on official government data sources, ensuring accuracy and currency. This is the foundation server for U.S. legal research — giving AI agents the same access to primary law that legal researchers use daily.

### CourtListener Legal Research MCP Server (khizar-anjum)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| CourtListener MCP | — | — | — | — |

Legal research across **3,352 U.S. courts** using the CourtListener API (from Free Law Project). Search opinions, access dockets, and retrieve court documents across federal and state courts. CourtListener is one of the largest free legal databases in the U.S., and this MCP server makes its full breadth accessible to AI agents. The 3,352-court coverage spans from the Supreme Court down to municipal courts.

### JustlyAI/DocketBird MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| DocketBird MCP | — | — | — | — |

Court document search and case detail retrieval via the DocketBird API. DocketBird specializes in making court records searchable and accessible. This server enables AI agents to find specific cases, retrieve filing histories, and access document details — useful for litigation support and due diligence workflows.

### Mortalus/eu-regulations (37 EU Regulations)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Mortalus/eu-regulations](https://github.com/Mortalus/eu-regulations) | — | — | — | — |

Query **37 EU regulations** including GDPR, AI Act, DORA, MiFID II, Digital Services Act, Digital Markets Act, and more through a single MCP interface. This is remarkably comprehensive — rather than building separate servers for each regulation, this project bundles the major EU regulatory framework into one searchable tool. For compliance teams working across EU regulations, this is the single most useful server in the review.

### European & Multi-Jurisdiction Servers

| Server | Jurisdiction | Key Feature |
|--------|-------------|-------------|
| pylegifrance MCP | France | Direct Legifrance API access — legislation, codes, judicial decisions |
| jmtanguy Droit Français MCP | France | Légifrance + JudiLibre databases |
| metaneutrons German Legal MCP | Germany | Federal/state legislation + EU legal databases |
| Ansvar-Systems/Danish-law-mcp | Denmark | Retsinformation (Danish legislation portal) |
| self-tech-labs Online Kommentar MCP | Switzerland | Swiss legal commentaries (onlinekommentar.ch), multilingual |
| self-tech-labs Entscheidsuche MCP | Switzerland | Swiss court decisions (entscheidsuche.ch) |
| TCoder920x/open-legal-compliance-mcp | Multi-jurisdiction | U.S. federal/state + EU regulations via government APIs |

The European coverage is particularly strong and has expanded significantly since March. France has two complementary servers (Legifrance for primary law, Droit Français adding JudiLibre case law). Switzerland gets both court decisions and legal commentaries. Germany covers federal, state, and EU law in one server. Denmark wraps the national Retsinformation portal. The open-legal-compliance-mcp takes a cross-jurisdiction approach, searching across U.S. and EU sources.

### Ansvar-Systems Compliance Suite *(NEW)*

The most systematic legal MCP effort since our initial review. Ansvar-Systems built four jurisdiction-specific servers, all with remote HTTP endpoints (no installation required), daily automated freshness checks against official sources, and Apache 2.0 licenses:

| Server | Jurisdiction | Coverage | Key Feature |
|--------|-------------|----------|-------------|
| [Ansvar-Systems/Dutch-law-mcp](https://github.com/Ansvar-Systems/Dutch-law-mcp) | Netherlands | 3,251 statutes, 77,531 provisions | EU directive cross-referencing, case law (59,261 rulings premium) |
| [Ansvar-Systems/US-law-mcp](https://github.com/Ansvar-Systems/US-law-mcp) | United States | 130 federal statutes, 46,646 provisions | HIPAA/CCPA/SOX/GLBA coverage, EU regulatory alignment mappings |
| [Ansvar-Systems/EU_compliance_MCP](https://github.com/Ansvar-Systems/EU_compliance_MCP) | European Union | 61 regulations, 4,095 articles | 709 ISO 27001:2022 + NIST CSF 2.0 control mappings, 407 audit artifacts |
| [Ansvar-Systems/Greek-law-mcp](https://github.com/Ansvar-Systems/Greek-law-mcp) | Greece | 21,119 statutes, 7,793 provisions | EU cross-referencing, constitutional/criminal/civil codes |

The EU Compliance MCP is particularly notable — it expanded from 37 to **61 regulations** (compared to Mortalus/eu-regulations in the original review), adds 16 specialist guides, 709 control mappings to ISO 27001:2022 and NIST CSF 2.0, and 407 evidence requirements for audits. The US Law MCP positions itself as "the eCFR and US Code alternative for the AI age" with comparative law tools mapping US regulations to EU equivalents. All four servers deliver verbatim statutory text — no LLM paraphrasing.

### United Kingdom Legal Servers *(NEW)*

| Server | Stars | Focus | Key Feature |
|--------|-------|-------|-------------|
| [georgejeffers/uk-case-law-mcp-server](https://github.com/georgejeffers/uk-case-law-mcp-server) | 22 | UK case law | National Archives API, 2003-present, Supreme Court through tribunals |
| [bencium/lex-api-mcp](https://github.com/bencium/lex-api-mcp) | 1 | UK legislation + case law | 219,655 acts, 69,910 judgments, 61,107 AI-generated case summaries, 19 tools |
| Stealth-Labs-LTD/GovUK-MCP | — | UK government services | 24 tools including legislation, courts, parliamentary data |
| i-dot-ai/parliament-mcp | — | Parliamentary APIs | Hansard and Members APIs with semantic search |

The UK was entirely absent from the original review — now it gets four complementary servers. The uk-case-law-mcp-server (22 stars, TypeScript, PolyForm Noncommercial) enables searching UK judicial decisions from The National Archives across Supreme Court, Court of Appeal, High Court, and tribunals. The Lex API MCP is remarkably comprehensive: 219,655 Acts and Statutory Instruments, 69,910 court judgments, 892,210 legislative amendments, and 83,350 explanatory notes — all free and open-source with semantic search. The GovUK-MCP bundles legislation with broader government services.

### Asia-Pacific Servers

| Server | Jurisdiction | Key Feature |
|--------|-------------|-------------|
| seo-jinseok Korean Law MCP | South Korea | Statutes, precedents, administrative rules via National Law Information Center |
| groundcobra009 Hourei MCP | Japan | e-Gov Law API including revision history |
| russellbrenner AusLaw MCP | Australia | Legislation + case law with full-text extraction |
| mickey-mikey OLEXI MCP | Australia | AustLII search with citation links |
| VibeCoding4-JC PDP MCP | Indonesia | Personal Data Protection Law (RAG-powered Q&A via Pinecone) |

South Korea's server searches statutes, precedents, and administrative rules through the National Law Information Center — one of the most comprehensive national legal APIs. Japan's Hourei server includes legislative revision history, useful for tracking how laws have changed over time. Australia gets two complementary servers: AusLaw for direct legislation/case law and OLEXI for AustLII (Australasian Legal Information Institute) search.

### Latin America & Middle East

| Server | Jurisdiction | Key Feature |
|--------|-------------|-------------|
| frontalinilucas saij-mcp | Argentina | SAIJ database — judgments, legislation, legal doctrine |
| frontalinilucas juba-mcp | Argentina (Buenos Aires) | Jurisprudencia de Buenos Aires — judicial rulings |
| chapirousIA PJE MCP | Brazil | Electronic Judicial Process with digital certificate support |
| saidsurucu Yargı MCP | Turkey | Supreme Court + Constitutional Court decisions |
| bayyyyyuuu VeniAI-Hukuk MCP | Turkey | AI-powered legal research with bilingual support |
| numikel Law Scrapper MCP | Poland | Polish legal acts from Sejm API |
| jeneen24 Jeneen MCP | Arabic-speaking | Arabic legal chatbot and search |

Argentina has two servers from the same developer covering national (SAIJ) and Buenos Aires provincial jurisdictions. Brazil's PJE server integrates with the Electronic Judicial Process system using digital certificates — reflecting Brazil's advanced e-court infrastructure. Turkey gets both court decision access (Yargı) and AI-powered case law research (VeniAI-Hukuk).

## Legal Reasoning & Document Generation

### yoda-digital/mcp-cerebra-legal-server (Enterprise Legal Reasoning)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [yoda-digital/mcp-cerebra-legal-server](https://github.com/yoda-digital/mcp-cerebra-legal-server) | — | — | — | — |

Enterprise-grade MCP server for legal reasoning and analysis. Provides domain-specific guidance, structured legal analysis frameworks, and citation formatting. Based on the "think" tool concept from Anthropic's engineering blog, adapted for legal workflows. This isn't a legal database — it's a reasoning layer that helps AI agents think through legal problems systematically with proper citation and analysis structure.

### automatikstudio LegalForge MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| LegalForge MCP | — | — | — | — |

Generates professional, jurisdiction-specific legal documents including privacy policies, terms of service, and other standard legal documents. Rather than searching existing law, LegalForge creates new documents tailored to specific jurisdictions and requirements. Useful for startups and small businesses that need basic legal documents without engaging a law firm for routine drafts.

### agentic-ops/legal-mcp (Comprehensive Legal Workflow)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [agentic-ops/legal-mcp](https://github.com/agentic-ops/legal-mcp) | — | — | — | — |

A comprehensive MCP server for legal workflows providing seamless integration between AI assistants and authoritative legal sources. Features include legal research integration, case management, document analysis, citation management, and multi-jurisdiction support. The project is actively seeking legal professionals for case study collaboration — a good sign that the developers are building with practitioner input. This is one of the most ambitious legal MCP servers, attempting to cover the full legal workflow rather than a single function.

### Lexpedite/Blawx MCP Server (Rule-Based Legal Reasoning)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| Blawx MCP | — | — | — | — |

Interacts with the Blawx API for discovering ontologies and performing rule-based legal reasoning. Blawx is a visual tool for encoding legal rules as executable logic — this MCP server lets AI agents query those encoded rules. The approach is fundamentally different from natural language legal research: instead of searching case law, agents query formally encoded legal rules for deterministic answers. Valuable for regulatory compliance where rules can be precisely encoded.

### Open Agreements *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [open-agreements/open-agreements](https://github.com/open-agreements/open-agreements) | 30 | JavaScript | MIT | — |

Fills standard legal agreement templates and produces signable DOCX files. **40+ templates** covering NDAs, cloud service agreements (Common Paper, Bonterms), employment docs, contractor agreements, Y Combinator SAFEs, and NVCA financing documents. Multi-language support (English, Spanish, Chinese, Portuguese, German). Includes SOC 2 readiness assessment and ISO 27001 internal audit tools. Works with Claude Code, Gemini CLI, Cursor, and as a hosted MCP server. At 30 stars with 382 commits, this is the most mature legal document generation MCP server — and the most practical for startups needing standard legal documents without outside counsel.

## IP & Trademarks

### riemannzeta/patent_mcp_server *(NEW — replaces john-walkoe USPTO as top patent server)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [riemannzeta/patent_mcp_server](https://github.com/riemannzeta/patent_mcp_server) | 54 | Python | MIT | 52 (20 active) |

The most comprehensive patent MCP server by a wide margin. **54 stars and 52 tools** covering Patent Public Search (full-text search, PDF downloads, advanced search), Open Data Portal (metadata, continuity, transactions, assignments, prosecution history), and more. Includes MCP Resources for CPC classifications and status codes, plus MCP Prompts for prior art analysis, validity assessment, and freedom-to-operate analysis. Note: 32 tools are currently unavailable due to USPTO API shutdowns in early 2026 (PatentsView shut down March 20, PTAB and Patent Litigation APIs not yet on ODP). Despite the API losses, the 20 active tools still provide the best patent research capability in the MCP ecosystem.

### KunihiroS/patsnap-mcp *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [KunihiroS/patsnap-mcp](https://github.com/KunihiroS/patsnap-mcp) | 4 | TypeScript | — | — |

MCP server for PatSnap's commercial patent analytics API. Designed for patent trend analysis and reporting rather than individual patent investigation. PatSnap is one of the largest commercial patent analytics platforms. Complements the USPTO server by adding commercial analytics capabilities.

### KunihiroS/google-patents-mcp *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [KunihiroS/google-patents-mcp](https://github.com/KunihiroS/google-patents-mcp) | — | TypeScript | — | — |

Searches Google Patents via SerpApi backend. Google Patents covers 100+ million patent documents worldwide, making this the broadest geographic patent search available through MCP. Complements the US-focused USPTO server with global coverage.

### john-walkoe USPTO MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| USPTO MCP | — | — | — | — |

High-performance access to the USPTO Final Petition Decisions API with intelligent context reduction. Searches and retrieves Patent Trial and Appeal Board (PTAB) decisions — useful for patent litigation research, invalidity searches, and understanding how the USPTO handles specific patent claims. The "intelligent context reduction" suggests the server processes long legal documents into AI-friendly summaries.

### saidsurucu Marka Patent MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| Marka Patent MCP | — | — | — | — |

Searches the Turkish Patent and Trademark Office (TPMA) database for intellectual property research. Enables trademark searches, patent lookups, and IP portfolio analysis within the Turkish jurisdiction. Built by the same developer who created the Turkish court decisions MCP server (Yargı), suggesting a systematic approach to digitizing Turkish legal infrastructure for AI access.

### handaas Trademark Big Data MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| Trademark Big Data MCP | — | — | — | — |

Provides trademark information including fuzzy search and portfolio analysis across trademark databases. The fuzzy search capability is important for trademark work — similar marks can create conflicts even without exact matches, and AI agents need to identify potential conflicts across spelling variations, phonetic similarities, and visual resemblance.

## Compliance & Regulatory

### eludden35 HIPAA Guardian MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| HIPAA Guardian MCP | — | — | — | — |

Comprehensive HIPAA compliance guidance for healthcare application developers. Rather than providing raw regulatory text, this server interprets HIPAA requirements in the context of software development — answering questions like "does this data flow comply with the Privacy Rule?" or "what technical safeguards does the Security Rule require for this use case?" Targeted at developers building healthcare applications who need to understand HIPAA implications without becoming compliance experts.

### ethanolivertroy FedRAMP Docs MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| FedRAMP Docs MCP | — | — | — | — |

Enables querying FedRAMP documentation, compliance requirements, and security controls. FedRAMP (Federal Risk and Authorization Management Program) governs cloud service providers serving U.S. federal agencies. This server gives AI agents access to FedRAMP requirements, helping cloud providers understand what they need to achieve authorization — a process that typically takes 12-18 months and involves hundreds of security controls.

### ag2-mcp-servers Policy Analyzer API MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| Policy Analyzer MCP | — | — | — | — |

Natural language interface to Google's Policy Analyzer API for compliance evaluation. Allows AI agents to analyze IAM policies against compliance requirements — answering questions like "who has access to this resource?" and "does this policy comply with our security standards?" Bridges the gap between cloud infrastructure policies and compliance requirements.

### Elnino0009 RegGuard MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| RegGuard MCP | — | — | — | — |

AI-powered compliance assistant analyzing financial marketing content across jurisdictions. Scans marketing materials for regulatory compliance issues — useful for financial services firms that must ensure advertising and promotional content meets regulatory requirements in each jurisdiction where they operate. The multi-jurisdiction aspect is key: what's compliant in one country may violate regulations in another.

### Additional Compliance Servers

| Server | Focus | Key Feature |
|--------|-------|-------------|
| negraodenio code-guard-ai | Code compliance | Multi-LLM orchestrator auditing code risks across 15+ frameworks |
| deeppath-ai mcp-crew-risk | Web compliance | Crawler compliance risk assessment — legal and ethical webpage risks |
| leafsicle Muni-MCP | Building codes | Municipal building code compliance assistant |
| aare-ai Aare MCP | Formal verification | Z3 SMT solver verification of LLM outputs against compliance ontologies |
| GlassTape Policy Builder | Security policies | Natural language to Cerbos YAML policy conversion with automated testing |
| knowledgepa3 GIA MCP | AI governance | Approval gates, auditable decision logs, compliance mapping for Claude agents |

The compliance subcategory ranges from highly specific (HIPAA, FedRAMP, building codes) to broadly applicable (code compliance, formal verification). The Aare MCP server stands out for using Z3 SMT solver for formal verification of AI outputs against compliance ontologies — the most mathematically rigorous approach to compliance checking we've seen in any MCP category. Note: Ansvar-Systems' EU Compliance MCP (covered in the Legal Research section above) now provides the most comprehensive EU regulatory coverage with 61 regulations, 709 control mappings to ISO 27001:2022 and NIST CSF 2.0, and 407 audit evidence requirements — surpassing the Mortalus/eu-regulations server's 37 acts.

## Contract & Practice Management *(NEW SECTION)*

This section didn't exist in the original review — contract lifecycle management and legal practice management were notable gaps. Both are now partially addressed.

### Concord MCP Server (Official CLM)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| Concord MCP (official) | — | — | — | 3 |

**The first contract lifecycle management vendor with an official MCP server.** Concord's MCP server provides three tools: workspace search (natural language search across all contracts), document-specific search (clauses, headers, tables, metadata within individual files), and report generation. Permission-aware — agents can only access documents the user is authorized to view. Zero external data retention. Works with ChatGPT (Team/Enterprise) and Claude (for Work/Team). Requires Concord Horizon plan. Part of Concord's broader Horizon AI platform launched November 2025, which includes AI Search, Portfolio Copilot, and AI Reporting. More tools planned. This fills a critical gap: AI agents can now search across contract repositories and answer questions like "Which vendor contracts above $250,000 automatically renew next quarter?"

### Clio Community MCP Servers

| Server | Focus | Key Feature |
|--------|-------|-------------|
| lawyered0/clio-mcp | Clio Manage v4 API | Contacts, matters, activities — read and write |
| lawquarter/MCP_Server_Clio | Australian legal | Secure Clio integration for AU practitioners |
| chlegal/clio-mcp-server | Choueke Hollander LLP | Search matters, log time, create tasks, manage calendar, billing |

**Clio was one of the biggest gaps in the original review — now addressed by the community.** Three independent teams built Clio MCP servers, each with different focuses. The lawyered0 implementation provides read/write access to contacts, matters, and activities via Clio's v4 REST API. The Choueke Hollander LLP server adds time entry logging, task creation, calendar management, and document search. An Oktopeak connector launching April 30, 2026 promises the most complete coverage: 12 tools across 7 Clio resource areas (matters, contacts, documents, tasks, calendar, billing, notes). Clio itself (the company) has not released an official MCP server, but the community has filled the gap. Clio recently made Clio Work (its AI workspace) available as a standalone product for solo and smaller firms.

## Legal Operations

### Corpo — Legal Entity Formation for AI Agents *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| Corpo MCP | — | — | — | 16 |

The first MCP server that lets AI agents form and govern legal entities. **16 tools** covering entity registration, governance actions (voting, proposals, resolutions), compliance tracking, and filing deadlines. Agents file Wyoming DAO LLCs through Corpo's API with articles of organization, registered agent, EIN, and operating agreement handled automatically. Treasury managed on Solana via Realms. Wyoming law carries no restrictions on AI agent ownership of DAO LLC member units. Pre-alpha/sandbox status. This is conceptually unprecedented — legal infrastructure for autonomous AI agents operating as legal persons. Whether this becomes mainstream or remains niche, it's the most forward-looking legal MCP server in the entire category.

### DatSciX-CEO LumenX MCP Server (Legal Spend Intelligence)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| LumenX MCP | — | — | — | — |

Analyzes legal spend data across multiple sources with vendor performance analysis. Legal departments at large companies can spend millions annually on outside counsel — LumenX helps AI agents analyze spending patterns, compare vendor performance, identify cost reduction opportunities, and flag billing anomalies. This is a legal operations tool rather than a legal research tool, targeting the business side of law.

### lawmem-ai (Persistent Legal Memory)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| lawmem-ai | — | — | — | — |

Persistent semantic memory service for legal AI agents with audit logging and GDPR compliance. Legal work requires remembering context across conversations — prior research, client preferences, case strategies, opposing counsel patterns. This server provides that continuity with the audit trail and data protection compliance that legal work demands. The GDPR compliance focus is appropriate given the sensitivity of legal data.

### visotrust/viso-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [visotrust/viso-mcp-server](https://github.com/visotrust/viso-mcp-server) | — | — | — | — |

Integrates with the VISO TRUST platform for legal document management and verification. VISO TRUST focuses on third-party risk management — vetting vendors, reviewing contracts, and verifying compliance. This MCP server brings those capabilities to AI agents for automated vendor assessment and document verification workflows.

### HopGraph MCP (Business Verification)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| HopGraph MCP | — | — | — | — |

Verifies Australian and New Zealand businesses against government registers. Due diligence in legal transactions requires confirming that counterparties are legitimate registered entities. This server automates the verification process against official government business registers — a task that legal assistants typically perform manually for each transaction.

## What's Missing

The gap list has shrunk significantly since March — DocuSign, PandaDoc, Concord, and Clio (community) are now covered. The remaining gaps:

- **No LexisNexis or Westlaw MCP servers** — the two largest legal research databases still have no official or community MCP servers. Both have invested heavily in their own AI tools (LexisNexis Protégé General AI, Westlaw CoCounsel/Deep Research) but haven't exposed them via MCP. This remains the single biggest gap in legal MCP.
- **No Ironclad or Icertis MCP servers** — the leading enterprise CLM platforms. Concord's MCP server is a start, but enterprise CLM at scale still lacks MCP coverage.
- **No Adobe Sign MCP server** — a major e-signature player, especially in Adobe-heavy workflows.
- **Limited contract negotiation** — servers exist for contract search (Concord), document generation (Open Agreements, LegalForge), and signing (DocuSign, PandaDoc), but the negotiation/redlining workflow between these steps is still manual.
- **No official Clio MCP server** — community servers exist, but Clio the company hasn't released one.

The vendor gap is closing faster than expected — three major platforms (DocuSign, PandaDoc, Concord) launched official MCP servers since our March review.

## The Bottom Line

Legal and contract management MCP servers earn **4.0 out of 5**, up from 3.5 in March.

**What works:** The vendor gap is closing — DocuSign (official remote server), PandaDoc (official MCP bundle), and Concord (first CLM with MCP) all launched since March. Geographic diversity expanded to 17+ countries including strong new Dutch, Greek, and UK coverage. The Ansvar-Systems suite brings professional-grade compliance servers with daily freshness checks, remote endpoints, and control mappings to ISO 27001:2022 and NIST CSF 2.0. Patent coverage is now excellent with 54-star, 52-tool USPTO server plus PatSnap and Google Patents. Open Agreements provides practical document generation for startups. The Lex API MCP (219K UK acts, 70K judgments, 19 tools) is one of the most comprehensive single-jurisdiction legal servers in the entire MCP ecosystem. Clio practice management has 3+ community servers.

**What doesn't:** LexisNexis and Westlaw — the two most important legal research databases — still have no MCP servers, preferring proprietary AI tools. Ironclad and Icertis (enterprise CLM) are absent. No Adobe Sign server. The contract negotiation/redlining workflow between document generation and signing remains a gap. Many newer jurisdiction-specific servers still have low star counts.

**Who should care:** Legal technologists can now build real workflows — generate documents (Open Agreements), route for signature (DocuSign/PandaDoc), search contract repositories (Concord), and manage practice operations (Clio). Compliance teams get cross-jurisdictional coverage across US, EU, and national regulations with audit-grade control mappings. Patent attorneys have serious research tools. The category has matured from "promising but underserved" to "practical for early adopters" in just six weeks.

*This review was last edited on 2026-04-27 using Claude Opus 4.6 (Anthropic).*
