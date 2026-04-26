# E-Signature & Digital Signing MCP Servers — DocuSign, PandaDoc, SignNow, BoldSign, and More

> E-signature MCP servers reviewed: DocuSign official hosted MCP (beta, IAM + eSignature + Navigator + Maestro, Anthropic partnership), PandaDoc official hosted remote (12+ tools, documents/templates/contacts/webhooks), SignNow sn-mcp-server (5 stars, 18 tools, embedded signing/editor, STDIO + Streamable HTTP), eSignatures.com (36 stars, contract lifecycle, MIT), BoldSign (4 stars, official, 14 tools, TypeScript npm), DocuSign Navigator MCP (This Dot Labs, agreement search), luthersystems DocuSign (JWT FastMCP 8 tools), CData DocuSign (read-only JDBC), SignWell (official npx install + Pipedream hosted), Adobe Sign via Cequence AI Gateway (enterprise MCP proxy). 10+ servers. Rating: 3.5/5.


E-signatures are one of the few business workflows where AI automation has an obvious, immediate payoff. Draft a contract, fill in signer details, send for signature, track status, download the signed document — every step is API-shaped and benefits from natural language orchestration.

This review covers MCP servers specifically built for **electronic signature workflows** — sending documents for signature, managing templates, tracking signing status, and downloading completed agreements. We're not covering general document management or PDF tools (see our [OCR & Document Intelligence review](/reviews/ocr-document-intelligence-mcp-servers/) for those).

The headline: **vendor participation is the strongest of any MCP category**. DocuSign, PandaDoc, SignNow, BoldSign, eSignatures.com, and SignWell all ship their own MCP servers — a level of official support rare in the MCP ecosystem. **DocuSign's official hosted MCP** (beta) is the most enterprise-ready, with an Anthropic partnership bringing DocuSign into Cowork. **PandaDoc now has an official hosted MCP server** — a major addition since our initial review. **SignNow has the most complete open-source implementation** with 18 tools including embedded signing experiences.

## Official Vendor Servers

These servers are built and maintained by the e-signature companies themselves. Official support means better API coverage, faster updates when APIs change, and fewer authentication headaches.

### DocuSign MCP Server (Official, Beta)

| Detail | Info |
|--------|------|
| [DocuSign MCP Server](https://developers.docusign.com/platform/mcp-server/) | Official (beta) |
| Endpoint | `mcp-d.docusign.com/mcp` |
| License | Proprietary |
| Integration | Claude Connectors Directory, GitHub Copilot, ChatGPT |
| Auth | DocuSign OAuth |
| Capabilities | IAM + eSignature + Navigator + Maestro |

The biggest name in e-signatures now has an official hosted MCP server at `mcp-d.docusign.com/mcp`, exposing DocuSign's Intelligent Agreement Management (IAM) platform to any MCP-compatible client.

### What Works Well

**Full eSignature lifecycle.** Create envelopes, send documents for signature, add attachments to drafts, configure workflow steps (delayed routing, conditional recipients), manage contacts in bulk — the complete contract workflow through natural language.

**Navigator agreement intelligence.** Query agreement metadata, search by key dates, find expiring contracts, and extract clause-level insights. This is the analytical side of DocuSign — "show me all NDAs expiring this quarter" becomes a natural language query.

**Maestro workflow orchestration.** Trigger multi-step approval processes, conditional routing, and complex document workflows. Moves beyond single-envelope signing into full business process automation.

**Anthropic partnership (February 2026).** DocuSign and Anthropic announced a partnership bringing DocuSign capabilities directly into Cowork. This is the deepest AI vendor integration any e-signature company has achieved.

**Enterprise governance preserved.** The MCP server enforces the same permissions, access controls, and audit policies as the DocuSign web UI. Actions are logged in DocuSign's audit trail.

**Multi-client support.** Available as a managed connector in Claude's Connectors Directory, plus documented integrations with GitHub Copilot and ChatGPT.

### What Doesn't Work Well

**Beta status.** Still in beta with potential breaking changes. Production deployment requires DocuSign approval via the developer portal beta program.

**No public GitHub repository.** Unlike the other servers in this review, the official DocuSign MCP server isn't open source. You can't inspect the code, contribute fixes, or self-host it.

**Beta enrollment required.** Developer accounts can access, but production use requires explicit approval — a friction point compared to the self-serve model of open-source alternatives.

### PandaDoc MCP Server (Official, Hosted)

| Detail | Info |
|--------|------|
| [PandaDoc MCP Server](https://developers.pandadoc.com/docs/use-pandadoc-mcp-server) | Official (hosted) |
| Endpoint | `developers.pandadoc.com/mcp` |
| License | Proprietary (hosted) |
| Auth | API Key |
| Tools | 12+ |
| Clients | Claude Desktop, Cursor, Windsurf |

**New since our initial review.** PandaDoc now ships an official hosted MCP server — filling one of the biggest gaps we identified in March 2026.

### What Works Well

**Comprehensive document management.** Create documents from file uploads, create from templates, manage attachments, organize into folders, and move documents between folders. Covers the full document preparation workflow before signatures.

**Template operations.** List templates, get template details, create templates from PDFs or from scratch, and delete templates. Template-driven contract generation is the most common AI automation use case.

**Contact and webhook management.** Create and list contacts, create webhooks for document event notifications. Webhook support enables event-driven automation — get notified when a document is signed, viewed, or completed.

**Hosted remote MCP.** Zero local installation. Connect via `mcp-remote` with your API key. Setup is straightforward with sandbox credentials available for testing.

**Official developer documentation.** Full setup guides on developers.pandadoc.com with supported client documentation for Claude Desktop, Cursor, and Windsurf.

### What Doesn't Work Well

**API key auth only.** Uses API-Key header authentication rather than OAuth. Simpler to set up but less secure for multi-user environments.

**No embedded signing.** Like most servers in this category, PandaDoc's MCP focuses on document preparation and sending rather than embedded in-app signing experiences.

**Sandbox limitations.** Sandbox API keys are available for testing, but behavior may differ from production. No free production tier.

### SignNow sn-mcp-server (Official)

| Detail | Info |
|--------|------|
| [signnow/sn-mcp-server](https://github.com/signnow/sn-mcp-server) | ~5 stars |
| License | Open source |
| Language | Python 3.11+ |
| Tools | 18 |
| Transport | STDIO + Streamable HTTP |

SignNow's official MCP server is the most feature-complete open-source option. 18 tools covering the full signing workflow, including embedded signing experiences that other servers don't offer.

### What Works Well

**Embedded signing/editor.** Beyond basic send-and-track, SignNow's server generates embedded signing links (`create_embedded_invite`), embedded sending experiences (`create_embedded_sending`), and embedded editor sessions (`create_embedded_editor`). These create in-app signing workflows without redirecting users to SignNow's site — critical for product integrations.

**One-shot template workflows.** `send_invite_from_template` combines template selection and invitation into a single tool call. Draft NDA from template, fill in details, send — one step.

**Document upload and field management.** `upload_document` accepts files from local paths, URLs, or MCP resources. `update_document_fields` lets AI agents pre-fill text fields before sending for signature. Combined with templates, this enables fully automated contract generation.

**Dual transport.** Supports both STDIO (for local MCP clients like Claude Desktop) and Streamable HTTP (for Docker/remote deployment). Most e-signature MCP servers only support STDIO.

**Bundled skills library.** The `signnow_skills` tool queries a bundled knowledge base of SignNow-specific workflows and best practices — an unusual but helpful addition for AI agents unfamiliar with e-signature concepts.

**Signing reminders.** `send_invite_reminder` nudges pending signers — a workflow step that other servers leave to manual follow-up.

### What Doesn't Work Well

**Low star count (5).** Despite being an official vendor server with the most tools, it hasn't gained much community traction.

**Python-only.** No TypeScript/Node.js option, which limits integration with JavaScript-heavy MCP toolchains.

**Dual auth complexity.** Supports both username/password (recommended for desktop dev) and OAuth 2.0 (for hosted scenarios). The dual approach can confuse initial setup.

SignNow also provides a companion **sn-api-helper-mcp** ([GitHub](https://github.com/signnow/sn-api-helper-mcp)) specifically designed to assist with SignNow API integration — a documentation/helper server rather than a workflow server.

### BoldSign MCP (Official)

| Detail | Info |
|--------|------|
| [boldsign/boldsign-mcp](https://github.com/boldsign/boldsign-mcp) | ~4 stars |
| License | MIT |
| Language | TypeScript |
| npm | @boldsign/mcp |
| Tools | 14 |
| Regions | US, EU, CA |

BoldSign (by Syncfusion) provides an official TypeScript MCP server published on npm with 14 explicitly documented tools.

### What Works Well

**npm package.** `@boldsign/mcp` installs with one command. Most MCP servers require cloning a repo and building from source — BoldSign's npm distribution is notably more developer-friendly.

**Multi-region support.** Configurable API region (US, EU, CA) for data residency compliance. Important for European organizations under GDPR.

**Well-organized tool categories.** Documents (5 tools: list, details, revoke, send reminders, list team documents), templates (3 tools: list, details, send from template), contacts (2 tools: list, details), users (2 tools: list, details), teams (2 tools: list, details). Clean structure for agent workflows.

**No data storage.** BoldSign emphasizes that the MCP server passes requests directly to the BoldSign API without storing any data locally — an important security property for document signing.

### What Doesn't Work Well

**No embedded signing.** Unlike SignNow, there's no support for generating embedded signing URLs or in-app signing experiences.

**Low star count (4).** Very early in community adoption.

**Requires paid BoldSign account.** Free trial and sandbox available, but the underlying service is paid. No free tier for production use.

### SignWell MCP Server (Official)

| Detail | Info |
|--------|------|
| [SignWell MCP](https://www.signwell.com/resources/signwell-mcp-ai-esignature/) | Official |
| Install | `npx signwell-mcp setup` |
| License | Proprietary |
| Auth | API Key (paid plans) |
| Clients | Claude Desktop, Claude Code, Cursor |

**Updated since our initial review.** SignWell now offers an official npx-based installation alongside the Pipedream-hosted option. Run `npx signwell-mcp setup` and the server configures itself for your MCP client.

### What Works Well

**One-command setup.** `npx signwell-mcp setup` handles installation and client configuration automatically. The simplest setup of any e-signature MCP server.

**Document format support.** Accepts PDF, DOC, DOCX, Pages, PPT, PPTX, Key, XLS, XLSX, Numbers, JPG, PNG, TIFF, and WEBP — the broadest format support in this category.

**Legally compliant signatures.** Full audit trails with timestamps, IP addresses, and signer identity. Compliant with US ESIGN Act, UETA, and EU eIDAS regulation.

**Signing reminders.** Like SignNow, supports sending reminders to pending signers.

### What Doesn't Work Well

**Requires paid SignWell plan.** API access is limited to paid plans. No free tier for production e-signatures.

**No public GitHub repository.** The npx package is distributed through npm but the source code isn't publicly available for inspection.

**Limited tool documentation.** Compared to SignNow's explicit 18-tool listing, SignWell's tool inventory is less clearly documented.

## Community Servers

### eSignatures.com MCP Server

| Detail | Info |
|--------|------|
| [esignaturescom/mcp-server-esignatures](https://github.com/esignaturescom/mcp-server-esignatures) | ~36 stars |
| License | MIT |
| Language | Python |
| Tools | 12 |
| Focus | Contract lifecycle management |

The most-starred e-signature MCP server. Built for eSignatures.com's API, covering the full contract lifecycle from template creation to signed document management.

### What Works Well

**Complete contract lifecycle.** 12 tools across contracts (`create_contract`, `query_contract`, `withdraw_contract`, `delete_contract`, `list_recent_contracts`) and templates (`create_template`, `update_template`, `query_template`, `delete_template`, `list_templates`). Full CRUD operations on both.

**Template collaboration.** `add_template_collaborator`, `remove_template_collaborator`, and `list_template_collaborators` — a workflow feature missing from most other servers. Useful for teams that iterate on contract templates.

**Highest community adoption.** 36 stars makes it the most popular e-signature MCP server on GitHub, suggesting it's the one people actually find and try first.

### What Doesn't Work Well

**eSignatures.com is a smaller platform.** Not DocuSign or SignNow. If you're already using a major e-signature vendor, this server won't help — it only works with eSignatures.com's API.

**Limited recent activity.** 14 commits total on master, with creation in January 2025 and minimal activity since.

### DocuSign Navigator MCP (This Dot Labs)

| Detail | Info |
|--------|------|
| [thisdot/docusign-navigator-mcp](https://github.com/thisdot/docusign-navigator-mcp) | ~0 stars |
| License | MIT |
| Language | TypeScript |
| Focus | Agreement search and analysis |
| Deployed | `docusign-navigator.thisdot.co/mcp` |

A community server focused on DocuSign Navigator — the agreement intelligence side of DocuSign, not the signing workflow.

### What Works Well

**Hosted deployment.** Publicly accessible at `docusign-navigator.thisdot.co/mcp` — no local installation needed.

**Agreement search.** "Show me pending contracts" or "Find agreements expiring this quarter" — natural language access to DocuSign agreement data.

**OAuth 2.0 authentication.** Proper OAuth flow, not just API keys. Works with DocuSign's security model.

**Read-only by design.** Can't accidentally send contracts or modify agreements. Safe for exploration and reporting.

### What Doesn't Work Well

**Navigator only.** For querying agreement data, not for sending documents or managing signing workflows. Complementary to the official DocuSign MCP server, not a replacement.

**Zero stars.** Minimal community adoption despite being well-built and hosted.

**Last updated October 2025.** v1.3.0 release with no recent activity.

### luthersystems DocuSign MCP (Community)

| Detail | Info |
|--------|------|
| [luthersystems/mcp-server-docusign](https://github.com/luthersystems/mcp-server-docusign) | ~1 star |
| License | — |
| Language | Python |
| Tools | 8 |
| Auth | JWT (server-to-server) |

**New since our initial review.** A community DocuSign MCP server built with FastMCP, focused on headless server-to-server automation via JWT authentication.

### What Works Well

**JWT authentication.** True server-to-server auth with no refresh tokens — ideal for headless automation, background processes, and CI/CD pipelines. No interactive OAuth flow needed.

**Organized tool set.** 8 tools across three categories: envelopes (`create_envelope_from_template`, `create_envelope_from_documents`, `get_envelope_status`, `list_envelopes`), templates (`list_templates`, `get_template_definition`), and documents (`list_envelope_documents`, `download_envelope_document`).

**Comprehensive testing.** Includes pytest coverage, unusual for community MCP servers.

### What Doesn't Work Well

**Experimental status.** Explicitly marked as not production-ready with no SLA. APIs and behavior may change.

**1 star.** Minimal adoption.

**No affiliation with DocuSign.** Community integration that may break when DocuSign APIs change.

### CData DocuSign MCP Server

| Detail | Info |
|--------|------|
| [CDataSoftware/docusign-mcp-server-by-cdata](https://github.com/CDataSoftware/docusign-mcp-server-by-cdata) | ~3 stars |
| License | MIT |
| Language | Java |
| Focus | Read-only data queries |

A read-only MCP server that lets you query DocuSign data using natural language, translated to SQL under the hood via CData's JDBC driver.

### What Works Well

**SQL-powered queries.** The JDBC approach means you can query any DocuSign data that CData's driver exposes — envelopes, recipients, templates, audit events — using natural language that gets converted to SQL SELECT statements.

**Table discovery.** Tools for listing available tables and their columns, so you can explore what data is accessible before querying.

### What Doesn't Work Well

**Read-only.** Can't create envelopes, send for signature, or modify anything. For querying/reporting only.

**Requires CData JDBC Driver.** The JDBC driver is a separately licensed commercial product. The MCP server is MIT-licensed but its core dependency isn't free.

**Java dependency.** Requires JVM and Maven build. Heavier infrastructure than Python or TypeScript servers.

## Enterprise Gateway Access

### Adobe Acrobat Sign via Cequence AI Gateway

| Detail | Info |
|--------|------|
| [Cequence AI Gateway](https://docs.aigateway.cequence.ai/) | Enterprise |
| Adobe Sign Endpoints | Agreements, Workflows, Webhooks, Users |
| Auth | OAuth |
| Type | API-to-MCP proxy |

Adobe hasn't built a native MCP server for Acrobat Sign, but **Cequence AI Gateway** transforms Adobe Sign's APIs into MCP-compatible endpoints with enterprise-grade security.

### What Works Well

**Full Adobe Sign API coverage.** Four MCP endpoint groups: Agreements (create, send, track, manage lifecycle), Workflows (conditional routing, parallel approvals, automated actions), Webhooks (real-time event notifications), and Users (user management, permissions, group administration).

**Enterprise security.** Built-in guardrails including automated tool risk scoring and rate limiting. OAuth authentication. Designed for organizations that need governance around AI-to-API access.

**No code changes needed.** Transforms existing Adobe Sign API endpoints into MCP tools automatically — no custom server code required.

### What Doesn't Work Well

**Not free.** Cequence AI Gateway is an enterprise product with custom pricing. Not accessible to individual developers or small teams.

**Indirect access.** This is an API gateway that wraps Adobe Sign, not a native MCP server. Adds a dependency and potential latency.

**Adobe's own absence.** Adobe has MCP servers for Experience Manager, Express, Analytics, and Marketo — but no dedicated Acrobat Sign MCP server. Given Adobe Sign's market share (second only to DocuSign), this remains the most notable gap in the e-signature MCP ecosystem.

## What's Missing

**No native Adobe Acrobat Sign MCP server.** Available through Cequence's enterprise gateway and platform wrappers (Zapier, viaSocket), but no official or community-maintained open-source server. Adobe has prioritized MCP for its creative and marketing tools over its signature product.

**No Dropbox Sign (HelloSign) MCP server.** Available through Pipedream's hosted MCP and Composio integrations, but no dedicated open-source, self-hosted server. Dropbox Sign has official SDKs in multiple languages but hasn't built an MCP server.

**No Zoho Sign, GetAccept, Oneflow, Proposify, or Yousign MCP servers.** These mid-market e-signature platforms have no MCP presence — official or community.

**No Ironclad, Juro, or Icertis CLM integration.** Contract lifecycle management (CLM) platforms that handle the negotiate-redline-sign-store workflow don't have MCP servers. The e-signature MCP ecosystem handles sending and tracking but not the broader contract intelligence workflow.

**No contract analysis/redlining tools.** These servers handle sending and tracking. None offer AI-powered contract review, clause extraction, or redline comparison — a workflow that would pair naturally with MCP.

## The Verdict

**Rating: 3.5 / 5** — Strongest vendor participation of any MCP category, but community adoption remains low.

The e-signature MCP ecosystem stands out for one reason: **vendors actually build and maintain their own servers**. DocuSign, PandaDoc, SignNow, BoldSign, eSignatures.com, and SignWell all ship official MCP implementations. In most MCP categories, you're relying on community wrappers that may break when APIs change. Here, you have official support from six vendors — unmatched anywhere in the MCP ecosystem.

**DocuSign's official hosted MCP** is the enterprise choice — hosted at `mcp-d.docusign.com/mcp`, backed by an Anthropic partnership, with Navigator agreement intelligence and Maestro workflow orchestration. If you're a DocuSign customer, it's the obvious starting point.

**PandaDoc's official hosted MCP** (new since our last review) fills a major gap. 12+ tools for documents, templates, contacts, and webhooks. The hosted deployment means zero infrastructure management.

**SignNow's sn-mcp-server** is the best open-source option. 18 tools, embedded signing support, dual transport, and the only server with a bundled skills library for AI agent guidance.

**For headless automation**, luthersystems' JWT-based DocuSign server enables server-to-server contract workflows without interactive OAuth — useful for background processes and CI/CD pipelines.

The 3.5 rating reflects two realities: vendor support is better than any other MCP category, but star counts are low across the board (the highest is 36), no single server handles the full "draft, negotiate, sign, store" workflow, and Adobe Sign — the second-largest e-signature platform — still lacks a native MCP server. This is a category where MCP adoption is ahead of community adoption — the servers exist, but most developers haven't found them yet.

*Last updated: April 26, 2026. Star counts and features reflect what we found during research. We do not install or test these servers hands-on — our reviews are based on documentation, source code analysis, GitHub activity, and community feedback. See our [methodology note](/reviews/#methodology) for details.*

