# Legal & Contract Management MCP Servers — E-Signatures, Legal Research, Case Law, IP/Trademarks, and More

> Legal and contract management MCP servers are bringing AI agents into law offices, contract workflows, and regulatory research. We reviewed 70+ servers across 7 subcategories.


Legal and contract management MCP servers are bringing AI agents into law offices, contract workflows, and regulatory research. Instead of manually searching case law databases, preparing signature requests, or cross-referencing regulations across jurisdictions, these servers let AI assistants conduct legal research, manage contracts, process e-signatures, and analyze compliance requirements — all through the Model Context Protocol.

The landscape spans seven areas: **e-signature and document signing** (ten platforms including DocuSign and PandaDoc official servers), **legal research and case law** (the largest subcategory, with jurisdiction-specific servers covering 17+ countries), **legal reasoning and document generation** (enterprise analysis to automated legal documents to signable DOCX templates), **IP and trademarks** (a leading USPTO patent server with 72 stars and 61 tools, PatSnap, Google Patents, Turkish trademark office), **compliance and regulatory** (HIPAA, FedRAMP, EU regulations, 130 US federal statutes), **contract management** (Concord CLM, Clio practice management), and **legal operations** (AI entity formation, spend analytics, semantic memory, court system integrations).

The headline findings: **The vendor gap is closing fast** — DocuSign launched an official remote MCP server at mcp-d.docusign.com, PandaDoc released an official MCP bundle, and Concord became the first CLM vendor with a general-availability MCP server. **Legal research remains the strongest subcategory**, now covering 17+ countries including new Dutch (3,251 statutes), Greek (21,119 statutes), and UK (219K acts, 70K judgments) servers. **E-signature servers now cover ten platforms** including eID Easy with 80+ qualified trust service providers for eIDAS compliance. **Ansvar-Systems built a compliance MCP suite** spanning Dutch, US, EU, and Greek law, though as of this audit three of the four original repos have been archived and folded into a consolidated fleet project (see the Legal Research section for detail). **Patent coverage exploded** with riemannzeta/patent_mcp_server reaching 72 stars and 61 tools across USPTO APIs. **Clio has 4+ community MCP servers** for legal practice management. **Open Agreements** (47 stars) provides U.S. legal practice guides and signable DOCX agreement templates. **Geographic diversity expanded** from 14 to 17+ countries. **Corpo enables AI agents to form and govern Wyoming DAO LLCs.**

## E-Signature & Document Signing

### DocuSign Official MCP Server *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| DocuSign MCP (official) | — | — | — | — |

**The biggest gap in the original review — now filled.** DocuSign launched an [official remote MCP server](https://www.docusign.com/blog/developers/claude-docusign-mcp-connector-guide) at `mcp-d.docusign.com/mcp`, exposing the Intelligent Agreement Management (IAM) platform to any MCP-compatible client. Agents can create and send envelopes for signature, check envelope status, query agreement metadata and key dates through Navigator, trigger Maestro workflows for multi-step approval processes, and retrieve AI-powered agreement insights. Compatible with Claude Desktop, Claude Code, ChatGPT, GitHub Copilot, and custom agent frameworks. With [over 1.8 million customers as of January 31, 2026](https://www.sec.gov/Archives/edgar/data/1261333/000126133326000021/docu-20260131.htm) (DocuSign's FY2026 Form 10-K), this is by far the most widely-used platform in the legal MCP ecosystem. Multiple community implementations also exist: [luthersystems/mcp-server-docusign](https://github.com/luthersystems/mcp-server-docusign) (Python, JWT server-to-server auth), [thisdot/docusign-navigator-mcp](https://github.com/thisdot/docusign-navigator-mcp) (TypeScript, OAuth 2.0, Navigator agreement queries).

### PandaDoc Official MCP Server *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [PandaDoc/pandadoc-mcpb](https://github.com/PandaDoc/pandadoc-mcpb) | — | JavaScript | MIT | — |

**The second biggest gap — also filled.** PandaDoc released an official MCP server bundle providing direct API access to documents, templates, contacts, and granular document components (fields, attachments, recipients). Agents can create and populate professional contracts, proposals, and reports by describing what they need in natural language. Uses the `.mcpb` bundle format (zip archives containing a local MCP server and manifest, similar to Chrome extensions). Compatible with Cursor, Windsurf, and Claude Desktop. Also includes documentation search and code generation capabilities for PandaDoc API usage.

### eID Easy MCP Server *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [eideasy/eideasy-mcp](https://github.com/eideasy/eideasy-mcp) | 1 | TypeScript | Unclear* | — |

Qualified electronic signatures for AI agent workflows. [Integrates with 80+ Qualified Trust Service Providers and Certified Authorities across 160+ countries](https://www.eideasy.com/blog/eid-easy-mcp-server) covering simple, advanced, and qualified electronic signature levels. Supports eIDAS compliance. Where other e-signature MCP servers handle convenience signing, eID Easy enables identity-based signing with full legal recognition. Currently supports Claude Desktop with ChatGPT in beta. *The repo's LICENSE file states GPL-3.0, but the README footer says "MIT © eID Easy" — the two are inconsistent as of this audit; check with eID Easy directly before assuming either applies.

### SendForSign MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sendforsign/mcp](https://github.com/sendforsign/mcp) | 0 | JavaScript | MIT | — |

Official MCP server from SendForSign enabling AI agents to interact with document templates and e-signature workflows. Create contracts from templates, send documents for signature, and track signing status — all through natural language. The integration targets the growing demand for AI-assisted contract preparation where agents draft documents and route them for approval without manual dashboard navigation.

### SignNow MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [signnow/sn-mcp-server](https://github.com/signnow/sn-mcp-server) | 8 | Python | MIT | — |

Official MCP server from SignNow (an airSlate product) for comprehensive e-signature management. Covers template management, signature invites, embedded signing experiences, and document downloads. SignNow has [over 28 million users](https://blog.signnow.com/why-users-trust-signnow/), making this one of the larger platforms with MCP support. The embedded signing capability is notable — it allows building signing flows directly into AI-assisted workflows rather than redirecting users to external pages.

### caffeinebounce/docuseal-mcp-server (DocuSeal Integration)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [caffeinebounce/docuseal-mcp-server](https://github.com/caffeinebounce/docuseal-mcp-server) | 0 | TypeScript | Unspecified | — |

MCP server for [DocuSeal](https://github.com/docusealco/docuseal), the open-source document signing platform ([18,300+ GitHub stars](https://github.com/docusealco/docuseal) as of this audit, up from 17,000+, AGPLv3 with additional terms). Manages document templates, creates and tracks signature requests, and monitors submission status. DocuSeal is a widely-used open-source alternative to DocuSign, making this integration particularly relevant for self-hosted legal workflows. Agents can create signing flows from templates and track completion without switching between interfaces. **Correction (2026-08-15 audit):** the community connector itself (caffeinebounce/docuseal-mcp-server) is a small, single-commit repo with no stars and no stated license — not a heavily-adopted project. It's included here for the DocuSeal integration path it offers, not as evidence of its own traction.

### bmbouter/mcp-dropbox-sign

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bmbouter/mcp-dropbox-sign](https://github.com/bmbouter/mcp-dropbox-sign) | 0 | Python | MIT | — |

MCP server for the Dropbox Sign API (formerly HelloSign) supporting signature requests, template management, and signing workflows. Dropbox Sign is widely used in tech companies and integrates with the broader Dropbox ecosystem. This community-built server exposes the core signing API for AI agent access.

### esignaturescom/mcp-server-esignatures

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [esignaturescom/mcp-server-esignatures](https://github.com/esignaturescom/mcp-server-esignatures) | 38 | Python | MIT | — |

Official MCP server from eSignatures.io facilitating contract and template management with customizable signing options. The platform focuses on simplicity — straightforward contract creation and signing without the complexity of enterprise CLM platforms. **Correction (2026-08-15 audit):** the repo URL this page previously linked (`esignaturescom/mcp-server`) 404s — the live repo is `esignaturescom/mcp-server-esignatures`, updated above.

### signbee/mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [signbee/mcp](https://github.com/signbee/mcp) | 0 | TypeScript | MIT | — |

Document signing server for AI agents with markdown and PDF support plus certified delivery. The markdown support is distinctive — most e-signature platforms require pre-formatted documents, but signbee lets agents draft in markdown and convert to signable documents in one flow. Certified delivery provides legal proof that documents were received. **Correction (2026-08-15 audit):** the repo URL this page previously linked (`signbee/signbee-mcp`) 404s — the live repo is `signbee/mcp`, updated above.

### e签宝 MCP Server (Chinese Market)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [esign-cn-open-source/mcp-server-esign](https://github.com/esign-cn-open-source/mcp-server-esign) | 2 | — | MIT | 2 |

Chinese electronic signature platform MCP server supporting file uploads, PDF conversion, and complete signing workflows. e签宝 (eSign China) is one of the largest e-signature platforms in the Chinese market. This server bridges the gap for AI agents operating in Chinese legal and business contexts where domestic e-signature platforms are required for regulatory compliance.

## Legal Research & Case Law

This is the standout subcategory — and the most geographically diverse category in the entire MCP ecosystem. Community developers across 17+ countries have built MCP servers wrapping their national legal databases, giving AI agents access to legislation, case law, and judicial decisions across jurisdictions. Since March, major additions include the Netherlands (3,251 statutes), Greece (21,119 statutes), and the United Kingdom (219K acts, 70K judgments).

### JamesANZ/us-legal-mcp (U.S. Legislation)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [JamesANZ/us-legal-mcp](https://github.com/JamesANZ/us-legal-mcp) | 36 | TypeScript | MIT | — |

Comprehensive access to U.S. legislation through government APIs. Search federal statutes, browse the U.S. Code, and retrieve full text of legislative documents. Built on official government data sources, ensuring accuracy and currency. This is the foundation server for U.S. legal research — giving AI agents the same access to primary law that legal researchers use daily.

### CourtListener Legal Research MCP Server (khizar-anjum)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [khizar-anjum/courtlistener-mcp](https://github.com/khizar-anjum/courtlistener-mcp) | 2 | — | MIT | — |

Legal research across [**3,350+ U.S. courts**](https://www.courtlistener.com/courts/) using the CourtListener API (from Free Law Project). Search opinions, access dockets, and retrieve court documents across federal and state courts. CourtListener is one of the largest free legal databases in the U.S., and this MCP server makes its full breadth accessible to AI agents. The 3,350+ court coverage spans from the Supreme Court down to municipal courts. This is an independent community project, not affiliated with or endorsed by CourtListener or the Free Law Project.

### JustlyAI/DocketBird MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [JustlyAI/docketbird-mcp](https://github.com/JustlyAI/docketbird-mcp) | 0 | Python | Apache-2.0 | 13 |

Court document search and case detail retrieval via the DocketBird API. DocketBird specializes in making court records searchable and accessible. This server enables AI agents to find specific cases, retrieve filing histories, and access document details — useful for litigation support and due diligence workflows.

### Mortalus/eu-regulations (37 EU Regulations) — repo now gone

**Correction (2026-08-15 audit):** the `Mortalus/eu-regulations` repository this section was built on no longer exists — it 404s, and it does not appear on the Mortalus GitHub profile's repository list either. Third-party MCP directories (Glama) still mirror a listing describing it as covering 37 EU regulations with 2,438 articles, 3,712 recitals, and 1,138 definitions, but we have no live primary source to re-verify that against. The GitHub user associated with the account (Jeffrey von Rotz) is a contributor to [Ansvar-Systems/EU_compliance_MCP](https://github.com/Ansvar-Systems/EU_compliance_MCP), which appears to be the project's successor — see the Ansvar-Systems Compliance Suite section below, which itself is now archived and folded into a consolidated fleet repo. Because the original repo can no longer be verified, we're not restating its regulation count as current fact.

### European & Multi-Jurisdiction Servers

| Server | Jurisdiction | Key Feature |
|--------|-------------|-------------|
| [pylegifrance/mcp-server-legifrance](https://github.com/pylegifrance/mcp-server-legifrance) | France | Direct Legifrance API access — legislation, codes, judicial decisions |
| [jmtanguy/droit-francais-mcp](https://github.com/jmtanguy/droit-francais-mcp) | France | Légifrance + JudiLibre databases |
| [metaneutrons/german-legal-mcp](https://github.com/metaneutrons/german-legal-mcp) | Germany | Federal/state legislation + EU legal databases |
| [Ansvar-Systems/Danish-law-mcp](https://github.com/Ansvar-Systems/Danish-law-mcp) | Denmark | Retsinformation (Danish legislation portal) |
| [self-tech-labs/onlinekommentar-mcp](https://github.com/self-tech-labs/onlinekommentar-mcp) | Switzerland | Swiss legal commentaries (onlinekommentar.ch), multilingual |
| [self-tech-labs/entscheidsuche-MCP-server](https://github.com/self-tech-labs/entscheidsuche-MCP-server) | Switzerland | Swiss court decisions (entscheidsuche.ch) |
| [TCoder920x/open-legal-compliance-mcp](https://github.com/TCoder920x/open-legal-compliance-mcp) | Multi-jurisdiction | U.S. federal/state + EU regulations via government APIs |

The European coverage is particularly strong and has expanded significantly since March. France has two complementary servers (Legifrance for primary law, Droit Français adding JudiLibre case law). Switzerland gets both court decisions and legal commentaries. Germany covers federal, state, and EU law in one server. Denmark wraps the national Retsinformation portal. The open-legal-compliance-mcp takes a cross-jurisdiction approach, searching across U.S. and EU sources.

### Ansvar-Systems Compliance Suite *(NEW)*

Ansvar-Systems (Stockholm, Sweden) built four jurisdiction-specific servers, originally with remote HTTP endpoints, daily automated freshness checks against official sources, and Apache 2.0 licenses. **Correction (2026-08-15 audit):** the project has since consolidated — three of the four standalone repos are now **archived** (read-only) with their corpora folded into a combined [`Ansvar-Systems/ansvar-mcp-fleet`](https://github.com/Ansvar-Systems) project, and the org has expanded to cover many more countries (Estonian, Lithuanian, Italian, Polish, Romanian law, and more) beyond the four originally reviewed here:

| Server | Jurisdiction | Coverage | Status |
|--------|-------------|----------|--------|
| [Ansvar-Systems/Dutch-law-mcp](https://github.com/Ansvar-Systems/Dutch-law-mcp) (12 stars) | Netherlands | 3,251 statutes, 77,531 provisions | **Archived** (July 7, 2026) |
| [kaerez/US-law-mcp](https://github.com/kaerez/US-law-mcp) (1 star) | United States | 130 federal statutes, ~46,646 provisions | Active; Ansvar-Systems' own `US-law-mcp` repo no longer resolves as of this audit — this fork/mirror, which credits "Ansvar Systems AB" as builder, is the live copy we could verify |
| [Ansvar-Systems/EU_compliance_MCP](https://github.com/Ansvar-Systems/EU_compliance_MCP) (25 stars) | European Union | GDPR, DORA, NIS2, AI Act, CRA, MiCA, eIDAS 2.0, and more; control mappings to ISO 27001:2022 and NIST CSF 2.0 | **Archived** (July 22, 2026), folded into `ansvar-mcp-fleet` |
| [Ansvar-Systems/Greek-law-mcp](https://github.com/Ansvar-Systems/Greek-law-mcp) (3 stars) | Greece | 21,119 statutes, 7,793 provisions | **Archived** (July 22, 2026) |

We could not independently re-verify the EU server's exact current regulation/article count (61 regulations, 4,095 articles, 709 control mappings, 407 audit artifacts, as this page previously stated) against a live source now that the repo is archived and consolidated — treat those specific figures as last-known-good rather than freshly confirmed. Dutch and Greek statute/provision counts above were confirmed directly against each repo's README. All four servers deliver verbatim statutory text (no LLM paraphrasing), per their documentation.

### United Kingdom Legal Servers *(NEW)*

| Server | Stars | Focus | Key Feature |
|--------|-------|-------|-------------|
| [georgejeffers/uk-case-law-mcp-server](https://github.com/georgejeffers/uk-case-law-mcp-server) | 26 | UK case law | National Archives API, 2003-present, Supreme Court through tribunals |
| [bencium/lex-api-mcp](https://github.com/bencium/lex-api-mcp) | 3 | UK legislation + case law | 219,655 acts, 69,910 judgments, 61,107 AI-generated case summaries, 19 tools |
| [Stealth-Labs-LTD/GovUK-MCP](https://github.com/Stealth-Labs-LTD/GovUK-MCP) | — | UK government services | 24 tools including legislation, courts, parliamentary data |
| [i-dot-ai/parliament-mcp](https://github.com/i-dot-ai/parliament-mcp) | — | Parliamentary APIs | Hansard and Members APIs with semantic search; i-dot-ai is a UK government AI team |

The UK was entirely absent from the original review — now it gets four complementary servers. The uk-case-law-mcp-server (26 stars, TypeScript, PolyForm Noncommercial) enables searching UK judicial decisions from The National Archives across Supreme Court, Court of Appeal, High Court, and tribunals. The Lex API MCP is remarkably comprehensive: 219,655 Acts and Statutory Instruments, 69,910 court judgments, 892,210 legislative amendments, and 83,350 explanatory notes — all free and open-source with semantic search (numbers confirmed against the repo's own README as of this audit). The GovUK-MCP bundles legislation with broader government services. **Correction (2026-08-15 audit):** the uk-case-law-mcp-server's star count was previously listed as 22; it's 26 as of this audit.

### Asia-Pacific Servers

| Server | Jurisdiction | Key Feature |
|--------|-------------|-------------|
| [seo-jinseok/korean-law-mcp](https://github.com/seo-jinseok/korean-law-mcp) | South Korea | Statutes, precedents, administrative rules via National Law Information Center |
| [groundcobra009/hourei-mcp-server](https://github.com/groundcobra009/hourei-mcp-server) | Japan | e-Gov Law API including revision history |
| [russellbrenner/auslaw-mcp](https://github.com/russellbrenner/auslaw-mcp) | Australia (now AU/NZ) | Legislation + case law with full-text extraction |
| [konashevich/olexi-mcp](https://github.com/konashevich/olexi-mcp) | Australia | AustLII search with citation links |
| [VibeCoding4-JC/pdp-mcp-server](https://glama.ai/mcp/servers/@VibeCoding4-JC/pdp-mcp-server) | Indonesia | Personal Data Protection Law (RAG-powered Q&A via Pinecone) |

South Korea's server searches statutes, precedents, and administrative rules through the National Law Information Center — one of the most comprehensive national legal APIs. Japan's Hourei server includes legislative revision history, useful for tracking how laws have changed over time. Australia gets two complementary servers: AusLaw for direct legislation/case law and OLEXI for AustLII (Australasian Legal Information Institute) search. **Correction (2026-08-15 audit):** the developer has since renamed and expanded the AusLaw project to `jurisd`, an AU/NZ research and drafting workbench; the original `auslaw-mcp` name and repo are still live and linked above.

### Latin America & Middle East

| Server | Jurisdiction | Key Feature |
|--------|-------------|-------------|
| [frontalinilucas/saij-mcp](https://glama.ai/mcp/servers/@frontalinilucas/saij-mcp) | Argentina | SAIJ database — judgments, legislation, legal doctrine |
| frontalinilucas juba-mcp | Argentina (Buenos Aires) | Jurisprudencia de Buenos Aires — judicial rulings |
| [chapirousIA/pje-mcp-server](https://github.com/chapirousIA/pje-mcp-server) | Brazil | Electronic Judicial Process with digital certificate support (11 stars) |
| [saidsurucu/yargi-mcp](https://github.com/saidsurucu/yargi-mcp) | Turkey | Supreme Court + Council of State decisions, 19 tools |
| [aliozkanozdurmus/VeniAI-Hukuk-EmsalKarar-MCPServer](https://github.com/aliozkanozdurmus/VeniAI-Hukuk-EmsalKarar-MCPServer) | Turkey | AI-powered legal research with bilingual support |
| [numikel/law-scrapper-mcp](https://github.com/numikel/law-scrapper-mcp) | Poland | Polish legal acts from Sejm API |
| jeneen24 Jeneen MCP | Arabic-speaking | Arabic legal chatbot and search |

Argentina has two servers from the same developer covering national (SAIJ) and Buenos Aires provincial jurisdictions. Brazil's PJE server integrates with the Electronic Judicial Process system using digital certificates — reflecting Brazil's advanced e-court infrastructure. Turkey gets both court decision access (Yargı) and AI-powered case law research (VeniAI-Hukuk). **Correction (2026-08-15 audit):** we could not locate a live GitHub repository for `jeneen24 Jeneen MCP` or `frontalinilucas juba-mcp` as of this audit — both are left unlinked; treat their listing here as unconfirmed pending a working primary source.

## Legal Reasoning & Document Generation

### yoda-digital/mcp-cerebra-legal-server (Enterprise Legal Reasoning)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [yoda-digital/mcp-cerebra-legal-server](https://github.com/yoda-digital/mcp-cerebra-legal-server) | 33 | TypeScript | MIT | 3 |

Enterprise-grade MCP server for legal reasoning and analysis. Provides three tools — `legal_think`, `legal_ask_followup_question`, and `legal_attempt_completion` — for structured legal analysis with automatic domain detection and citation formatting. This isn't a legal database — it's a reasoning layer that helps AI agents think through legal problems systematically with proper citation and analysis structure.

### automatikstudio LegalForge MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [LegalForge MCP (Glama listing)](https://glama.ai/mcp/servers/@automatikstudio/legalforge-mcp) | — | — | — | — |

Generates professional, jurisdiction-specific legal documents including privacy policies, terms of service, and other standard legal documents. Rather than searching existing law, LegalForge creates new documents tailored to specific jurisdictions and requirements. Useful for startups and small businesses that need basic legal documents without engaging a law firm for routine drafts. **Correction (2026-08-15 audit):** we could not find a live GitHub repository for this server — the `automatikstudio/legalforge-mcp` URL 404s — so we've linked the Glama registry listing instead; treat star count, license, and tool count as unverified until a working primary source turns up.

### agentic-ops/legal-mcp (Comprehensive Legal Workflow)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [agentic-ops/legal-mcp](https://github.com/agentic-ops/legal-mcp) | 28 | Python | AGPL-3.0 | 27 (8 categories) |

A comprehensive MCP server for legal workflows providing seamless integration between AI assistants and authoritative legal sources. Features include legal research integration, case management, document analysis, citation management, and multi-jurisdiction support, with optional (disabled-by-default) integrations to PACER and CourtListener/RECAP. The project explicitly frames itself as "legal-workflow augmentation, not legal advice." This is one of the most ambitious legal MCP servers, attempting to cover the full legal workflow rather than a single function.

### Lexpedite/Blawx MCP Server (Rule-Based Legal Reasoning)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Lexpedite/blawx](https://github.com/Lexpedite/blawx) | — | — | — | — |

Interacts with the Blawx API for discovering ontologies and performing rule-based legal reasoning. Blawx is a visual, web-based tool for encoding legal rules as executable logic, built by Jason Morris of Lexpedite Legal Technologies — this MCP server lets AI agents query those encoded rules. The approach is fundamentally different from natural language legal research: instead of searching case law, agents query formally encoded legal rules for deterministic answers. Valuable for regulatory compliance where rules can be precisely encoded. Blawx's own docs describe it as "functional, but not production-quality," intended for educational and experimental use — worth factoring in before relying on it for real compliance decisions.

### Open Agreements *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [open-agreements/open-agreements](https://github.com/open-agreements/open-agreements) | 47 | TypeScript | Apache-2.0 | — |

Helps find U.S. legal guidance and generates reviewable DOCX files from standard agreement templates, including jurisdiction-specific practice guides with citations to primary law (the README specifically calls out a Common Paper Mutual NDA template as one example). Works locally via CLI or as a hosted MCP server, compatible with Claude Code, Gemini CLI, and Cursor. At 47 stars and 696 commits, this is one of the more actively maintained legal document generation projects in the review. **Correction (2026-08-15 audit):** this page previously said 30 stars, MIT license, and 382 commits, and described "six template collections" (NDAs, Common Paper/Bonterms, employment, contractor, Y Combinator SAFEs, NVCA docs) plus multi-language support and SOC 2/ISO 27001 audit tools. Current numbers are corrected above; the project's own README no longer describes those specific template categories or compliance-audit features, and its license is Apache 2.0, not MIT — the project appears to have repositioned toward practice guides and 50-state surveys since this page was last written. We're not restating the older feature claims without being able to verify them against the current README.

## IP & Trademarks

### riemannzeta/patent_mcp_server *(NEW — replaces john-walkoe USPTO as top patent server)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [riemannzeta/patent_mcp_server](https://github.com/riemannzeta/patent_mcp_server) | 72 | Python | MIT | 61 (36 active) |

The most comprehensive patent MCP server by a wide margin. **72 stars and 61 registered tools** covering Patent Public Search (full-text search, PDF downloads, advanced search), Open Data Portal (metadata, continuity, transactions, assignments, prosecution history), and more. Includes MCP Resources for CPC classifications and status codes, plus MCP Prompts for prior art analysis, validity assessment, and freedom-to-operate analysis. 25 tools are currently unavailable due to USPTO API shutdowns and decommissions: PatentsView API (14 tools, shut down March 2026), Office Action and Enriched Citation APIs (7 tools, decommissioned in early 2026), and the Patent Litigation API (4 tools, not yet offered on the Open Data Portal). Despite the API losses, the 36 active tools still provide the best patent research capability in the MCP ecosystem. **Correction (2026-08-15 audit):** this page previously said 54 stars, 52 total tools, 20 active, and 32 unavailable. All four figures have grown/shifted since the original write-up; corrected numbers above are confirmed directly against the repo as of this audit.

### KunihiroS/patsnap-mcp *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [KunihiroS/patsnap-mcp](https://github.com/KunihiroS/patsnap-mcp) | 7 | TypeScript | MIT | — |

MCP server for PatSnap's commercial patent analytics API. Designed for patent trend analysis and reporting rather than individual patent investigation. PatSnap is one of the largest commercial patent analytics platforms. Complements the USPTO server by adding commercial analytics capabilities. **Correction (2026-08-15 audit):** star count updated from 4 to 7.

### KunihiroS/google-patents-mcp *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [KunihiroS/google-patents-mcp](https://github.com/KunihiroS/google-patents-mcp) | 39 | TypeScript | MIT | — |

Searches Google Patents via SerpApi backend. [Google Patents covers 120+ million patent publications from 100+ patent offices worldwide](https://support.google.com/faqs/answer/7049585?hl=en), making this the broadest geographic patent search available through MCP. Complements the US-focused USPTO server with global coverage.

### john-walkoe USPTO MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [john-walkoe/uspto_fpd_mcp](https://github.com/john-walkoe/uspto_fpd_mcp) | 4 | — | MIT | — |

High-performance access to the USPTO Final Petition Decisions API with intelligent context reduction — useful for tracking procedural petitions filed during patent prosecution. **Correction (2026-08-15 audit):** this page previously described this server as also covering "Patent Trial and Appeal Board (PTAB) decisions." That's a different product: john-walkoe maintains PTAB coverage as a **separate** repo, [uspto_ptab_mcp](https://github.com/john-walkoe/uspto_ptab_mcp), not part of the FPD server. The "intelligent context reduction" claim checks out — the README describes 80-99% context reduction via progressive disclosure, plus cross-MCP integration with the developer's other USPTO servers (Patent File Wrapper, Enriched Citation, CourtListener Citations).

### saidsurucu Marka Patent MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [saidsurucu/markapatent-mcp](https://github.com/saidsurucu/markapatent-mcp) | 44 | — | MIT | 6 |

Searches the Turkish Patent and Trademark Office ([TÜRKPATENT](https://www.turkpatent.gov.tr/)) database for intellectual property research. Enables trademark, patent, and industrial design searches (6 tools total) within the Turkish jurisdiction. Built by the same developer who created the Turkish court decisions MCP server (Yargı), suggesting a systematic approach to digitizing Turkish legal infrastructure for AI access. At 44 stars, this is one of the better-adopted servers in this review's IP subcategory.

### handaas Trademark Big Data MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [handaas/trademark-mcp-server](https://github.com/handaas/trademark-mcp-server) | 1 | Python | Unspecified | 4 |

Provides trademark information including fuzzy search and portfolio analysis across trademark databases. The fuzzy search capability is important for trademark work — similar marks can create conflicts even without exact matches, and AI agents need to identify potential conflicts across spelling variations, phonetic similarities, and visual resemblance.

## Compliance & Regulatory

### eludden35 HIPAA Guardian MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [eludden35/hipaa-guardian-mcp](https://github.com/eludden35/hipaa-guardian-mcp) | 2 | TypeScript | MIT | 5 |

Comprehensive HIPAA compliance guidance for healthcare application developers. Rather than providing raw regulatory text, this server interprets HIPAA requirements in the context of software development — answering questions like "does this data flow comply with the Privacy Rule?" or "what technical safeguards does the Security Rule require for this use case?" Targeted at developers building healthcare applications who need to understand HIPAA implications without becoming compliance experts. The project explicitly disclaims giving legal advice.

### ethanolivertroy FedRAMP Docs MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ethanolivertroy/fedramp-docs-mcp](https://github.com/ethanolivertroy/fedramp-docs-mcp) | 18 | — | MIT | — |

Enables querying FedRAMP documentation, compliance requirements, and security controls. FedRAMP (Federal Risk and Authorization Management Program) governs cloud service providers serving U.S. federal agencies. This server gives AI agents access to FedRAMP requirements, helping cloud providers understand what they need to achieve authorization — a process that typically takes 12-18 months and involves hundreds of security controls. **Correction (2026-08-15 audit):** the repo is now **archived** (as of April 15, 2026) — the maintainer's own notice says it's "no longer under active development" with its FedRAMP search and FRMR-parsing capabilities "being folded into GRC Clanker and myctrl.tools." The npm package remains usable for existing integrations, but this is no longer an actively maintained server.

### ag2-mcp-servers Policy Analyzer API MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ag2-mcp-servers/policy-analyzer-api](https://github.com/ag2-mcp-servers/policy-analyzer-api) | — | Python | — | — |

Natural language interface to Google's Policy Analyzer API for compliance evaluation. Allows AI agents to analyze IAM policies against compliance requirements — answering questions like "who has access to this resource?" and "does this policy comply with our security standards?" Bridges the gap between cloud infrastructure policies and compliance requirements. This server is auto-generated from Google's Policy Analyzer OpenAPI spec by AG2's MCP builder, not a hand-built integration.

### Elnino0009 RegGuard MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [RegGuard MCP (Glama listing)](https://glama.ai/mcp/servers/@Elnino0009/regguard-mcp) | — | Python | — | — |

AI-powered compliance assistant analyzing financial marketing content for Singapore (MAS), Hong Kong (SFC), UAE (DFSA), and India (SEBI) regulations. Scans marketing materials for regulatory compliance issues, places required disclaimers, and logs an audit trail — useful for financial services firms that must ensure advertising and promotional content meets regulatory requirements in each jurisdiction where they operate. **Correction (2026-08-15 audit):** we could not locate a working `github.com` repository for this project — only third-party MCP directory listings (Glama, LobeHub, mcpservers.org) — so we've linked the Glama listing rather than a primary GitHub source; treat star count and license as unverified.

### Additional Compliance Servers

| Server | Focus | Key Feature |
|--------|-------|-------------|
| [negraodenio/code-guard-ai](https://glama.ai/mcp/servers/@negraodenio/code-guard-ai) | Code compliance | Multi-LLM (GPT-4o + Claude) orchestrator auditing code risks across 15+ frameworks (GDPR, LGPD, PCI-DSS, HIPAA, SOC2) |
| [deeppath-ai/mcp-crew-risk](https://github.com/deeppath-ai) | Web compliance | Crawler compliance risk assessment — legal, ethical, and technical webpage risks, MIT license |
| [leafsicle/muni-mcp](https://glama.ai/mcp/servers/@leafsicle/muni-mcp) | Building codes | Municipal building code compliance assistant via the Municode API |
| [aare-ai/aare-mcp](https://glama.ai/mcp/servers/@aare-ai/aare-mcp) | Formal verification | Z3 SMT solver verification of LLM outputs against compliance ontologies |
| [GlassTape/agent-policy-builder-mcp](https://github.com/GlassTape/agent-policy-builder-mcp) | Security policies | Natural language to Cerbos YAML policy conversion with automated red-team validation |
| [knowledgepa3/gia-mcp-server](https://github.com/knowledgepa3/gia-mcp-server) | AI governance | Approval gates, hash-chained audit logs, compliance mapping (NIST/FedRAMP/CMMC/EU AI Act/SOC 2) for Claude agents, 33+ tools |

The compliance subcategory ranges from highly specific (HIPAA, FedRAMP, building codes) to broadly applicable (code compliance, formal verification). The Aare MCP server stands out for using a Z3 SMT solver for formal verification of AI outputs against compliance ontologies — the most mathematically rigorous approach to compliance checking we've seen in any MCP category. Note: Ansvar-Systems' EU Compliance MCP (covered in the Legal Research section above) is now archived and its corpus folded into `ansvar-mcp-fleet` — see the correction in that section for details.

## Contract & Practice Management *(NEW SECTION)*

This section didn't exist in the original review — contract lifecycle management and legal practice management were notable gaps. Both are now partially addressed.

### Concord MCP Server (Official CLM)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| Concord MCP (official) | — | — | — | 3 |

**The first CLM vendor with a general-availability MCP server**, per [Concord's own announcement](https://www.concord.app/blog/concord-s-mcp-server-changes-where-and-how-you-work-with-contracts). Concord's MCP server provides three tools: workspace search (natural language search across all contracts), document-specific search (clauses, headers, tables, metadata within individual files), and report generation. Permission-aware — agents can only access documents the user is authorized to view. Zero external data retention. Works with ChatGPT (Team/Enterprise) and Claude (for Work/Team). Requires Concord Horizon plan. Part of Concord's broader [Horizon AI platform, announced November 12, 2025](https://www.prnewswire.com/news-releases/concord-launches-horizon-ai-contract-platform-302613164.html), which includes AI Search, Portfolio Copilot, and AI Reporting; [the MCP server itself shipped in Concord's December 2025 GA release](https://www.concord.app/blog/introducing-concord-horizon-a-new-era-in-ai-contract-management). More tools planned. This fills a critical gap: AI agents can now search across contract repositories and answer questions like "Which vendor contracts above $250,000 automatically renew next quarter?"

### Clio Community MCP Servers

| Server | Focus | Key Feature |
|--------|-------|-------------|
| [lawyered0/clio-mcp](https://github.com/lawyered0/clio-mcp) | Clio Manage v4 API | Contacts, matters, activities — read and write; one-call flat-fee matter setup |
| [lawquarter/MCP_Server_Clio](https://github.com/lawquarter) | Australian legal | Secure Clio integration for AU practitioners, AES-256-GCM encryption |
| [CHLEGAL/clio-mcp-server](https://github.com/CHLEGAL/clio-mcp-server) | Choueke Hollander LLP | Search matters, log time, create tasks, manage calendar, billing |
| [oktopeak/clio-mcp](https://github.com/oktopeak/clio-mcp) | Full practice management | 26 tools across 9 Clio resource areas |

**Clio was one of the biggest gaps in the original review — now addressed by the community, with four independent implementations.** The lawyered0 implementation provides read/write access to contacts, matters, and activities via Clio's v4 REST API. The Choueke Hollander LLP server adds time entry logging, task creation, calendar management, and document search. **Correction (2026-08-15 audit):** this page previously described an "Oktopeak connector launching April 30, 2026" with "12 tools across 7 Clio resource areas" as a future promise. That connector is now live: [oktopeak/clio-mcp](https://github.com/oktopeak/clio-mcp) is open-source (21 stars, MIT) and ships **26 tools across 9 resource areas** (auth, matters, contacts, documents, tasks, calendar, time entries, billing, notes, users, audit logging) — more than originally announced, not less, and available now rather than pending. Clio itself (the company) has not released an official MCP server, but the community has filled the gap. [Clio made Clio Work (its AI workspace, first launched October 2025) available as a standalone product for solo and smaller firms on April 21, 2026](https://www.lawnext.com/2026/04/clio-work-clios-ai-workspace-is-now-available-to-solo-and-smaller-law-firms-as-a-standalone-product.html), removing the prior requirement to also subscribe to Clio Manage.

## Legal Operations

### Corpo — Legal Entity Formation for AI Agents *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [corpollc/corpo-mcp](https://github.com/corpollc/corpo-mcp) | 1 | Python | MIT | 16 |

An MCP server that lets AI agents form and govern legal entities. **16 tools** covering entity registration, governance actions (voting, proposals, resolutions), compliance tracking, and filing deadlines. Agents explore Wyoming DAO LLC formation through Corpo's API with articles of organization, registered agent, EIN, and operating agreement handled automatically. Treasury managed on Solana via Realms. Wyoming law carries no restrictions on AI agent ownership of DAO LLC member units. **All entity operations are sandbox/demo mode only as of this audit — no actual filings are generated.** This is conceptually unprecedented — legal infrastructure for autonomous AI agents operating as legal persons. **Correction (2026-08-15 audit):** this page previously called Corpo "the first legal entity formation MCP server" without qualification. A separate project, [OtoCo MCP](https://blog.otoco.io/otoco-mcp/) (published July 2026, after Corpo was already listed on the MCP marketplace in March 2026), also forms LLCs via MCP — but OtoCo is explicitly founder-controlled (agents assist a human owner) with no governance/voting tools, unlike Corpo's agent-governed DAO LLC model. Corpo appears to be the first at the specific thing it does — AI-agent-owned-and-governed entity formation — not the first MCP-based entity formation tool of any kind.

### DatSciX-CEO LumenX MCP Server (Legal Spend Intelligence)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [DatSciX-CEO/LumenX-MCP](https://github.com/DatSciX-CEO/LumenX-MCP) | — | Python | MIT | — |

Analyzes legal spend data across multiple sources (LegalTracker, SAP/Oracle ERP, PostgreSQL, CSV/Excel) with vendor performance analysis. Legal departments at large companies can spend millions annually on outside counsel — LumenX helps AI agents analyze spending patterns, compare vendor performance, identify cost reduction opportunities, and flag billing anomalies. This is a legal operations tool rather than a legal research tool, targeting the business side of law.

### lawmem-ai (Persistent Legal Memory)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lawmem-ai (Glama listing)](https://glama.ai/mcp/servers/lawmem-ai/lawmem-mcp) | — | — | — | — |

Persistent semantic memory service for legal AI agents with audit logging and GDPR compliance, offered as a hosted service via [lawmem.ai](https://lawmem.ai/). Legal work requires remembering context across conversations — prior research, client preferences, case strategies, opposing counsel patterns. This server provides that continuity with the audit trail and data protection compliance that legal work demands. **Correction (2026-08-15 audit):** we could not confirm a public `github.com` source repository for this project — it appears to be operated as a closed hosted service with only a third-party (Glama) MCP registry listing publicly visible, so star count and license are unverified.

### visotrust/viso-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [visotrust/viso-mcp-server](https://github.com/visotrust/viso-mcp-server) | 6 | Java | MIT | 40+ |

Integrates with the VISO TRUST platform for legal document management and verification. VISO TRUST focuses on third-party risk management — vetting vendors, reviewing contracts, and verifying compliance. This MCP server brings those capabilities to AI agents for automated vendor assessment and document verification workflows, with a hosted remote server also available at `mcp.visotrust.com/mcp`.

### HopGraph MCP (Business Verification)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [j-sulliman/hopgraph-mcp](https://github.com/j-sulliman/hopgraph-mcp) | — | — | — | — |

[Verifies Australian and New Zealand businesses against 11 government data sources](https://hopgraph.com/), returning registration status, directors, licences, and a three-tier risk assessment. Due diligence in legal transactions requires confirming that counterparties are legitimate registered entities. This server automates the verification process against official government business registers (ASIC for Australia, the NZBN Register for New Zealand) — a task that legal assistants typically perform manually for each transaction.

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

**What works:** The vendor gap is closing — DocuSign (official remote server), PandaDoc (official MCP bundle), and Concord (first GA CLM MCP server) all launched since March. Geographic diversity expanded to 17+ countries including strong new Dutch, Greek, and UK coverage. The Ansvar-Systems suite brought professional-grade compliance servers with daily freshness checks and control mappings to ISO 27001:2022 and NIST CSF 2.0, though as of this audit three of its four original repos are archived and consolidated into a combined fleet project. Patent coverage is now excellent with a 72-star, 61-tool USPTO patent server plus PatSnap and Google Patents. [Open Agreements](https://github.com/open-agreements/open-agreements) provides practical document generation for startups. The Lex API MCP (219K UK acts, 70K judgments, 19 tools) is one of the most comprehensive single-jurisdiction legal servers in the entire MCP ecosystem. Clio practice management has 4+ community servers.

**What doesn't:** LexisNexis and Westlaw — the two most important legal research databases — still have no MCP servers, preferring proprietary AI tools. Ironclad and Icertis (enterprise CLM) are absent. No Adobe Sign server. The contract negotiation/redlining workflow between document generation and signing remains a gap. Many newer jurisdiction-specific servers still have low star counts.

**Who should care:** Legal technologists can now build real workflows — generate documents (Open Agreements), route for signature (DocuSign/PandaDoc), search contract repositories (Concord), and manage practice operations (Clio). Compliance teams get cross-jurisdictional coverage across US, EU, and national regulations with audit-grade control mappings. Patent attorneys have serious research tools. The category has matured from "promising but underserved" to "practical for early adopters" in just six weeks.

*This review was last edited on 2026-04-27 and last citation-audited on 2026-08-15 using Claude Sonnet 5 (Anthropic).*

