# Legal & Contract Management MCP Servers — E-Signatures, Legal Research, Case Law, IP/Trademarks, and More

> Legal and contract management MCP servers are bringing AI agents into law offices, contract workflows, and regulatory research. We reviewed 50+ servers across 6 subcategories.


Legal and contract management MCP servers are bringing AI agents into law offices, contract workflows, and regulatory research. Instead of manually searching case law databases, preparing signature requests, or cross-referencing regulations across jurisdictions, these servers let AI assistants conduct legal research, manage contracts, process e-signatures, and analyze compliance requirements — all through the Model Context Protocol.

The landscape spans six areas: **e-signature and document signing** (seven platforms from SendForSign to Dropbox Sign), **legal research and case law** (the largest subcategory, with jurisdiction-specific servers covering 14+ countries), **legal reasoning and document generation** (enterprise analysis to automated legal documents), **IP and trademarks** (USPTO, Turkish trademark office, portfolio analysis), **compliance and regulatory** (HIPAA, FedRAMP, EU regulations, financial marketing), and **legal operations** (spend analytics, semantic memory, court system integrations).

The headline findings: **Legal research is the strongest subcategory**, with community developers systematically wrapping government legal APIs for AI access — covering the U.S., France, Germany, Denmark, South Korea, Turkey, Japan, Australia, Switzerland, Poland, Argentina, Brazil, Indonesia, and the EU. **E-signature servers cover seven platforms** but lack the two largest (DocuSign and PandaDoc have no official MCP servers). **EU regulations get dedicated coverage** with 37 acts including GDPR, AI Act, DORA, and MiFID II accessible through a single server. **No major legal tech vendor has released an official MCP server** — no Clio, LexisNexis, Westlaw, or Ironclad. **Geographic diversity is unmatched** — no other MCP category covers this many jurisdictions. **Most servers are early-stage** with minimal GitHub traction, reflecting the legal industry's cautious approach to AI adoption.

## E-Signature & Document Signing

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

This is the standout subcategory — and the most geographically diverse category in the entire MCP ecosystem. Community developers across 14+ countries have built MCP servers wrapping their national legal databases, giving AI agents access to legislation, case law, and judicial decisions across jurisdictions.

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

The European coverage is particularly strong. France has two complementary servers (Legifrance for primary law, Droit Français adding JudiLibre case law). Switzerland gets both court decisions and legal commentaries. Germany covers federal, state, and EU law in one server. Denmark wraps the national Retsinformation portal. The open-legal-compliance-mcp takes a cross-jurisdiction approach, searching across U.S. and EU sources.

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

## IP & Trademarks

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

The compliance subcategory ranges from highly specific (HIPAA, FedRAMP, building codes) to broadly applicable (code compliance, formal verification). The Aare MCP server stands out for using Z3 SMT solver for formal verification of AI outputs against compliance ontologies — the most mathematically rigorous approach to compliance checking we've seen in any MCP category.

## Legal Operations

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

The biggest gaps in this category:

- **No DocuSign MCP server** — the largest e-signature platform (over 1 million customers) has no official or significant community MCP server
- **No PandaDoc MCP server** — the second-largest e-signature platform
- **No Clio MCP server** — the dominant legal practice management platform
- **No LexisNexis or Westlaw MCP servers** — the two largest legal research databases
- **No Ironclad or Icertis MCP servers** — the leading contract lifecycle management platforms
- **No Adobe Sign MCP server** — a major e-signature player
- **Limited contract lifecycle management** — no CLM-specific servers for contract creation, negotiation, execution, and renewal workflows
- **No legal billing/time tracking** — despite being a core legal operations function

The absence of major legal tech vendors is notable but not surprising — the legal industry moves slowly on technology adoption, and many legal platforms serve regulated clients who require extensive security reviews before enabling AI integrations.

## The Bottom Line

Legal and contract management MCP servers earn **3.5 out of 5**.

**What works:** The geographic diversity of legal research servers is unmatched in the MCP ecosystem — 14+ countries with dedicated servers wrapping national legal databases. The e-signature subcategory covers seven platforms. EU regulation access through a single server covering 37 acts is genuinely useful. The legal reasoning tools (Cerebra Legal, Blawx) take thoughtful approaches to a hard problem.

**What doesn't:** Most servers have minimal GitHub traction (0-20 stars) and are early-stage projects. The absence of major legal tech vendors (DocuSign, Clio, LexisNexis, Westlaw, Ironclad) leaves significant gaps in the most commonly used legal tools. Contract lifecycle management — arguably the highest-value legal AI use case — has almost no MCP coverage. Many jurisdiction-specific servers provide limited documentation, making it hard to evaluate quality without deep legal domain expertise.

**Who should care:** Legal technologists exploring AI integration, compliance teams needing cross-jurisdictional regulatory access, developers building legal workflow tools, and law firms evaluating MCP as a path to AI-assisted research. The legal research servers are immediately practical for anyone working with the covered jurisdictions. The e-signature servers are useful for contract automation workflows. The compliance servers address real enterprise needs — but the overall category needs vendor buy-in to reach its potential.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

