---
title: "E-Signature & Digital Signing MCP Servers — DocuSign, PandaDoc, SignNow, BoldSign, and More"
date: 2026-03-19T21:00:00+09:00
description: "E-signature MCP servers reviewed: DocuSign official hosted MCP (Global Open Beta, no intake form, IAM + eSignature + Navigator + Maestro + Iris AI Assistant + Agent Studio, Anthropic partnership), PandaDoc official hosted remote (OAuth, documents/templates), SignNow sn-mcp-server (8 stars, 25 tools, embedded signing/editor, STDIO + Streamable HTTP), eSignatures.com (38 stars, 23 tools, contract lifecycle, MIT), BoldSign (7 stars, official, 14 tools, TypeScript npm), DocuSign Navigator MCP (This Dot Labs, agreement search), luthersystems DocuSign (JWT FastMCP 8 tools), CData DocuSign (read-only JDBC), SignWell (official npx install + Pipedream hosted), Adobe Sign via Cequence AI Gateway (enterprise MCP proxy). 10+ servers. Rating: 3.5/5."
og_description: "E-signature MCP servers: DocuSign official hosted MCP (Global Open Beta, Iris AI Assistant + Agent Studio at Momentum 2026, Anthropic partnership), PandaDoc official (OAuth, hosted), SignNow (25 tools, embedded signing), BoldSign (14 tools, npm), eSignatures.com (38 stars, 23 tools), SignWell (official npx). Rating: 3.5/5."
content_type: "Review"
categories: ["/categories/government-legal/"]
card_description: "E-signature MCP servers for AI-powered contract workflows. DocuSign is now in Global Open Beta at mcp-d.docusign.com/mcp — no intake form required — with IAM, eSignature, Navigator, Maestro, and Momentum 2026 additions: Iris AI Assistant (contract review, redlining, obligation tracking) and Agent Studio (natural language → custom agents; U.S. early access, broader rollout July 2026) plus the Anthropic partnership. PandaDoc ships an official hosted MCP server at developers.pandadoc.com/mcp covering documents and templates via OAuth. SignNow has the most complete open-source server with 25 tools (8 stars) including embedded signing. BoldSign provides an official npm package with 14 tools. eSignatures.com leads community stars at 38 with 23 tools. SignWell offers official npx-based installation. luthersystems adds JWT server-to-server auth with 8 FastMCP tools for headless automation. Adobe Acrobat Sign accessible through Cequence AI Gateway. Dropbox Sign still has no dedicated server. Rating: 3.5/5 — vendor support is the strongest of any MCP category, but the full draft-negotiate-sign-store workflow gap persists."
last_refreshed: 2026-06-11
sources_audited: 2026-08-15
---

E-signatures are one of the few business workflows where AI automation has an obvious, immediate payoff. Draft a contract, fill in signer details, send for signature, track status, download the signed document — every step is API-shaped and benefits from natural language orchestration.

This review covers MCP servers specifically built for **electronic signature workflows** — sending documents for signature, managing templates, tracking signing status, and downloading completed agreements. We're not covering general document management or PDF tools (see our [OCR & Document Intelligence review](/reviews/ocr-document-intelligence-mcp-servers/) for those).

The headline: **vendor participation is the strongest of any MCP category**. DocuSign, PandaDoc, SignNow, BoldSign, eSignatures.com, and SignWell all ship their own MCP servers — a level of official support rare in the MCP ecosystem. **DocuSign's official hosted MCP** (beta) is the most enterprise-ready, with an Anthropic partnership bringing DocuSign into Cowork. **PandaDoc now has an official hosted MCP server** — a major addition since our initial review. **SignNow has the most complete open-source implementation** with 25 tools including embedded signing experiences.

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

**Full eSignature lifecycle.** [Create and send envelopes for signature, from scratch or from templates, and check envelope status](https://www.docusign.com/blog/developers/docusign-mcp-server-legal-ai-integration) — core contract-sending workflow through natural language.

**Navigator agreement intelligence.** [Query agreement lists and pull structured metadata](https://www.docusign.com/blog/developers/docusign-mcp-server-legal-ai-integration) through Agreement Manager (`getAllAgreements`, `getAgreementDetails`). This is the analytical side of DocuSign — asking for agreements by status or date becomes a natural language query.

**Maestro workflow orchestration.** [Trigger preconfigured multi-step workflows](https://www.docusign.com/blog/developers/docusign-mcp-server-legal-ai-integration) via Workflow Builder (`getWorkflowTriggerRequirements`, `triggerWorkflow`). Moves beyond single-envelope signing into full business process automation.

**Anthropic partnership (February 2026).** [DocuSign and Anthropic announced a partnership](https://www.docusign.com/company/news-center/docusign-partners-with-anthropic-to-bring-its-intelligent-contract-workflows-to-cowork) bringing DocuSign capabilities directly into Cowork. This is the deepest AI vendor integration any e-signature company has achieved.

**Enterprise governance preserved.** The MCP server enforces the same permissions, access controls, and audit policies as the DocuSign web UI. Actions are logged in DocuSign's audit trail.

**Multi-client support.** Available as a [managed connector in Claude's Connectors Directory](https://developers.docusign.com/platform/mcp-server/), with documented integrations for GitHub Copilot and ChatGPT as well.

**Iris AI Assistant (Momentum 2026, U.S. early access).** [DocuSign's Iris-powered AI assistant](https://www.docusign.com/company/news-center/docusign-unveils-ai-assistant-and-agents-to-power-the-next-era-of-agreement-work) transforms contracts into active workflow components: review, redlining, approval routing, obligation tracking, and automated follow-up. Announced at Docusign's Momentum conference on May 21, 2026; broader U.S. rollout begins July 2026.

**Agent Studio (Momentum 2026, U.S. early access).** Describe agreement workflows in natural language; Agent Studio converts them into custom agents tied to internal playbooks, policies, and connected systems like Salesforce. [Three pre-built agent patterns](https://www.docusign.com/products/agents): intake and triage, smart redlining, and relationship intelligence.

**IAM for Sales GA.** [Globally available as of the May 2026 Momentum announcement](https://www.docusign.com/company/news-center/docusign-unveils-ai-assistant-and-agents-to-power-the-next-era-of-agreement-work). **IAM for HR** entering U.S. early access in June 2026. **AI-assisted Web Forms** going global in June 2026.

### What Doesn't Work Well

**Beta status.** [Now in Global Open Beta](https://www.docusign.com/blog/developers/momentum-26-agentic-agreement-workflows) (as of Momentum 2026) — no intake form or additional approval required for production use. Developer and production accounts can connect directly. Potential breaking changes still possible before GA.

**No public GitHub repository.** Unlike the other servers in this review, the official DocuSign MCP server isn't open source. You can't inspect the code, contribute fixes, or self-host it.

**Iris and Agent Studio are U.S.-only early access.** The MCP integration itself is globally available, but the highest-value features (Iris AI Assistant, Agent Studio) are in U.S. early access with broader rollout beginning July 2026.

### PandaDoc MCP Server (Official, Hosted)

| Detail | Info |
|--------|------|
| [PandaDoc MCP Server](https://developers.pandadoc.com/docs/use-pandadoc-mcp-server) | Official (hosted) |
| Endpoint | `developers.pandadoc.com/mcp` |
| License | Proprietary (hosted) |
| Auth | [OAuth](https://developers.pandadoc.com/docs/getting-started-with-mcp) |
| Tools | [Documents, templates](https://developers.pandadoc.com/docs/what-you-can-do-with-pandadoc-mcp) |
| Clients | [Claude Desktop, Claude Code, Cursor, VS Code, Windsurf](https://developers.pandadoc.com/docs/supported-mcp-clients), and more |

**New since our initial review.** PandaDoc now ships an official hosted MCP server — filling one of the biggest gaps we identified in March 2026.

### What Works Well

**Document management from natural language.** [Create documents from file uploads and from templates](https://developers.pandadoc.com/docs/what-you-can-do-with-pandadoc-mcp), then search, send, and track them — all through prompts like "Create a new NDA for John Smith at Acme Corp using our standard NDA template."

**Template operations.** [List templates, get template details (roles, fields, tokens), and create templates from an uploaded PDF](https://developers.pandadoc.com/docs/what-you-can-do-with-pandadoc-mcp). Template-driven contract generation is the most common AI automation use case.

**Hosted remote MCP.** Zero local installation. Connect through your AI client's [OAuth consent flow](https://developers.pandadoc.com/docs/getting-started-with-mcp) — click Allow/Authorize and grant access to your PandaDoc account.

**Official developer documentation.** Full setup guides on developers.pandadoc.com with supported client documentation for Claude Desktop, Cursor, and Windsurf.

### What Doesn't Work Well

**OAuth-only, no API key option.** Every client must complete an interactive OAuth consent flow (click Allow, then Authorize) to connect — there's no documented API-key path, which complicates unattended/headless automation.

**No embedded signing.** Like most servers in this category, PandaDoc's MCP focuses on document preparation and sending rather than embedded in-app signing experiences.

**EU accounts need a separate setup step.** [The PandaDoc connector in Claude's connector directory only authenticates global accounts](https://developers.pandadoc.com/docs/getting-started-with-mcp) — EU account holders must manually add a custom connector pointed at `mcp.pandadoc.eu/v1/mcp` rather than using the directory listing.

### SignNow sn-mcp-server (Official)

| Detail | Info |
|--------|------|
| [signnow/sn-mcp-server](https://github.com/signnow/sn-mcp-server) | ~8 stars |
| License | Open source |
| Language | Python 3.11+ |
| Tools | 25 |
| Transport | STDIO + Streamable HTTP |

SignNow's official MCP server is the most feature-complete open-source option. 25 tools covering the full signing workflow, including embedded signing experiences that other servers don't offer.

### What Works Well

**Embedded signing/editor.** Beyond basic send-and-track, SignNow's server generates embedded signing links (`create_embedded_invite`), embedded sending experiences (`create_embedded_sending`), and embedded editor sessions (`create_embedded_editor`). These create in-app signing workflows without redirecting users to SignNow's site — critical for product integrations.

**One-shot template workflows.** `send_invite_from_template` combines template selection and invitation into a single tool call. Draft NDA from template, fill in details, send — one step.

**Document upload and field management.** `upload_document` accepts files from local paths, URLs, or MCP resources. `update_document_fields` lets AI agents pre-fill text fields before sending for signature. Combined with templates, this enables fully automated contract generation.

**Dual transport.** Supports both STDIO (for local MCP clients like Claude Desktop) and Streamable HTTP (for Docker/remote deployment). Most e-signature MCP servers only support STDIO.

**Bundled skills library.** The `signnow_skills` tool queries a bundled knowledge base of SignNow-specific workflows and best practices — an unusual but helpful addition for AI agents unfamiliar with e-signature concepts.

**Signing reminders.** `send_invite_reminder` nudges pending signers — a workflow step that other servers leave to manual follow-up.

### What Doesn't Work Well

**Low star count (~8).** Despite being an official vendor server with the most tools, it hasn't gained much community traction.

**Python-only.** No TypeScript/Node.js option, which limits integration with JavaScript-heavy MCP toolchains.

**Dual auth complexity.** Supports both username/password (recommended for desktop dev) and OAuth 2.0 (for hosted scenarios). The dual approach can confuse initial setup.

SignNow also provides a companion **sn-api-helper-mcp** ([GitHub](https://github.com/signnow/sn-api-helper-mcp)) specifically designed to assist with SignNow API integration — a documentation/helper server rather than a workflow server.

### BoldSign MCP (Official)

| Detail | Info |
|--------|------|
| [boldsign/boldsign-mcp](https://github.com/boldsign/boldsign-mcp) | ~7 stars |
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

**No data storage.** [BoldSign emphasizes that the MCP server passes requests directly to the BoldSign API without storing any data locally](https://boldsign.com/blogs/mcp-server-ai-esignature-automation/) — an important security property for document signing.

### What Doesn't Work Well

**No embedded signing.** Unlike SignNow, there's no support for generating embedded signing URLs or in-app signing experiences.

**Low star count (~7).** Very early in community adoption.

**Requires paid BoldSign account.** [A free API sandbox and 30-day trial are available for testing](https://developers.boldsign.com/how-to-guides/what-are-the-options-you-have-with-a-boldsign-trial-account-and-developer-sandbox-account/), but production use requires a paid plan starting around $5/user/month.

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

**Limited tool documentation.** Compared to SignNow's explicit 25-tool listing, SignWell's tool inventory is less clearly documented.

## Community Servers

### eSignatures.com MCP Server

| Detail | Info |
|--------|------|
| [esignaturescom/mcp-server-esignatures](https://github.com/esignaturescom/mcp-server-esignatures) | ~38 stars |
| License | MIT |
| Language | Python |
| Tools | 23 |
| Focus | Contract lifecycle management |

The most-starred e-signature MCP server. Built for eSignatures.com's API, covering the full contract lifecycle from template creation to signed document management.

### What Works Well

**Complete contract lifecycle.** 23 tools across contracts, signers, placeholder fields, content, templates, and collaborators — including full CRUD on contracts (`create_contract`, `query_contract`, `withdraw_contract`, `delete_contract`, `list_recent_contracts`) and templates (`create_template`, `update_template`, `query_template`, `delete_template`, `list_templates`).

**Template collaboration.** `add_template_collaborator`, `remove_template_collaborator`, and `list_template_collaborators` — a workflow feature missing from most other servers. Useful for teams that iterate on contract templates.

**Highest community adoption.** 38 stars makes it the most popular e-signature MCP server on GitHub, suggesting it's the one people actually find and try first.

### What Doesn't Work Well

**eSignatures.com is a smaller platform.** Not DocuSign or SignNow. If you're already using a major e-signature vendor, this server won't help — it only works with eSignatures.com's API.

### DocuSign Navigator MCP (This Dot Labs)

| Detail | Info |
|--------|------|
| [thisdot/docusign-navigator-mcp](https://github.com/thisdot/docusign-navigator-mcp) | ~1 star |
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

**~1 star.** Minimal community adoption despite being well-built and hosted.

**Last updated October 2025.** [v1.3.0 release](https://github.com/thisdot/docusign-navigator-mcp/releases) with no recent activity since.

### luthersystems DocuSign MCP (Community)

| Detail | Info |
|--------|------|
| [luthersystems/mcp-server-docusign](https://github.com/luthersystems/mcp-server-docusign) | ~2 stars |
| License | MIT |
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

**~2 stars.** Minimal adoption.

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

**Full Adobe Sign API coverage.** Four MCP endpoint groups: [Agreements](https://docs.aigateway.cequence.ai/docs/applications/productivity-document-management/adobe-sign-agreements/) (create, send, track, manage lifecycle), [Workflows](https://docs.aigateway.cequence.ai/docs/applications/productivity-document-management/adobe-sign-workflows/) (conditional routing, parallel approvals, automated actions), [Webhooks](https://docs.aigateway.cequence.ai/docs/applications/productivity-document-management/adobe-sign-webhooks/) (real-time event notifications), and [Users](https://docs.aigateway.cequence.ai/docs/applications/productivity-document-management/adobe-sign-users/) (user management, permissions, group administration).

**Enterprise security.** [Built-in guardrails including automated tool risk scoring and rate limiting](https://docs.aigateway.cequence.ai/docs/guides/security-policies/). OAuth authentication. Designed for organizations that need governance around AI-to-API access.

**No code changes needed.** Transforms existing Adobe Sign API endpoints into MCP tools automatically — no custom server code required.

### What Doesn't Work Well

**Not free.** [Cequence AI Gateway is an enterprise product with custom/tiered pricing](https://www.cequence.ai/products/ai-gateway/). Not accessible to individual developers or small teams.

**Indirect access.** This is an API gateway that wraps Adobe Sign, not a native MCP server. Adds a dependency and potential latency.

**Adobe's own absence.** Adobe has official MCP servers for [Experience Manager](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/ai/mcp-servers/overview), [Express and other Creative Cloud tools](https://developer.adobe.com/adobe-for-creativity/), [Analytics](https://developer.adobe.com/analytics-mcp/docs/), and [Marketo](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/mcp-server) — but no dedicated Acrobat Sign MCP server.

## What's Missing

**No native Adobe Acrobat Sign MCP server.** Available through Cequence's enterprise gateway and platform wrappers ([Zapier](https://zapier.com/mcp/adobe-acrobat-sign), [viaSocket](https://viasocket.com/mcp/adobe-acrobat-sign)), but no official or community-maintained open-source server. Adobe's own MCP servers cover [Experience Manager](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/ai/mcp-servers/overview), [Creative Cloud tools](https://developer.adobe.com/adobe-for-creativity/), [Analytics](https://developer.adobe.com/analytics-mcp/docs/), and [Marketo](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/mcp-server) — not its signature product.

**No Dropbox Sign (HelloSign) MCP server.** Available through [Pipedream's](https://pipedream.com/apps/hellosign) hosted integrations and [Composio's](https://composio.dev/toolkits/dropbox_sign) MCP toolkit, but no dedicated open-source, self-hosted server.

**Zoho Sign and Yousign have third-party MCP access; GetAccept, Oneflow, and Proposify appear to have none.** Zoho Sign is listed as a [supported service on Zoho's own platform-wide MCP](https://www.zoho.com/mcp/services/zoho-services.html), and Yousign is reachable through third-party wrappers like [viaSocket](https://viasocket.com/mcp/yousign). GetAccept, Oneflow, and Proposify have no dedicated MCP server we could find, official or community.

**CLM coverage is thin.** [Ironclad now has an official MCP server](https://support.ironcladapp.com/hc/en-us/articles/39887091143319-Ironclad-MCP-Server) (read-only, permission-aware contract queries, officially supported only through Slackbot, ChatGPT, and Claude), but Juro and Icertis appear to have none yet. Contract lifecycle management (CLM) platforms that handle the negotiate-redline-sign-store workflow remain mostly outside the e-signature MCP ecosystem, which still centers on sending and tracking rather than the broader contract intelligence workflow.

**No contract analysis/redlining tools.** These servers handle sending and tracking. None offer AI-powered contract review, clause extraction, or redline comparison — a workflow that would pair naturally with MCP.

## The Verdict

**Rating: 3.5 / 5** — Strongest vendor participation of any MCP category, but community adoption remains low.

The e-signature MCP ecosystem stands out for one reason: **vendors actually build and maintain their own servers**. DocuSign, PandaDoc, SignNow, BoldSign, eSignatures.com, and SignWell all ship official MCP implementations. In most MCP categories, you're relying on community wrappers that may break when APIs change. Here, you have official support from six vendors — unmatched anywhere in the MCP ecosystem.

**DocuSign's official hosted MCP** is the enterprise choice — hosted at `mcp-d.docusign.com/mcp`, backed by an Anthropic partnership, with Navigator agreement intelligence and Maestro workflow orchestration. If you're a DocuSign customer, it's the obvious starting point.

**PandaDoc's official hosted MCP** (new since our last review) fills a major gap. Tools cover documents and templates, authenticated via OAuth. The hosted deployment means zero infrastructure management.

**SignNow's sn-mcp-server** is the best open-source option. 25 tools, embedded signing support, dual transport, and the only server with a bundled skills library for AI agent guidance.

**For headless automation**, luthersystems' JWT-based DocuSign server enables server-to-server contract workflows without interactive OAuth — useful for background processes and CI/CD pipelines.

The 3.5 rating reflects two realities: vendor support is better than any other MCP category, but star counts are low across the board (the highest is 38), no single server handles the full "draft, negotiate, sign, store" workflow, and Adobe Sign still lacks a native MCP server. This is a category where MCP adoption is ahead of community adoption — the servers exist, but most developers haven't found them yet.

*Last updated: June 11, 2026. Star counts and features reflect what we found during research. We do not install or test these servers hands-on — our reviews are based on documentation, source code analysis, GitHub activity, and community feedback. See our [methodology note](/reviews/#methodology) for details.*
