---
title: "E-Signature & Digital Signing MCP Servers — DocuSign, SignNow, BoldSign, and More"
date: 2026-03-19T21:00:00+09:00
description: "E-signature MCP servers let AI agents send contracts, track signing status, and manage templates through natural language. We reviewed 8+ servers across official vendor connectors and community implementations. DocuSign leads with an official MCP connector (beta) offering full IAM + eSignature access. SignNow provides the most complete open-source server (15 tools, embedded signing). eSignatures.com has the highest community stars (35) with contract lifecycle management. The ecosystem is maturing fast — multiple vendors now treat MCP as a first-class integration path."
og_description: "E-signature MCP servers: DocuSign official connector (beta, IAM + eSignature, Claude Connectors Directory), SignNow sn-mcp-server (5 stars, 15 tools, embedded signing/editor, STDIO + HTTP), eSignatures.com (35 stars, contract + template management, MIT), BoldSign (4 stars, official, TypeScript, npm package), DocuSign Navigator MCP (This Dot Labs, agreement search), CData DocuSign (read-only, JDBC), SignWell (Pipedream-hosted, 12+ tools). 8+ servers. Rating: 3.5/5."
content_type: "Review"
card_description: "E-signature MCP servers for AI-powered contract workflows. DocuSign offers an official MCP connector (beta) with full IAM and eSignature access through the Claude Connectors Directory. SignNow has the most complete open-source server with 15 tools including embedded signing. eSignatures.com leads community stars at 35 with contract lifecycle management. BoldSign provides an official npm package. The ecosystem is notable for vendor participation — three e-signature companies ship their own MCP servers."
---

E-signatures are one of the few business workflows where AI automation has an obvious, immediate payoff. Draft a contract, fill in signer details, send for signature, track status, download the signed document — every step is API-shaped and benefits from natural language orchestration.

This review covers MCP servers specifically built for **electronic signature workflows** — sending documents for signature, managing templates, tracking signing status, and downloading completed agreements. We're not covering general document management or PDF tools (see our [OCR & Document Intelligence review](/reviews/ocr-document-intelligence-mcp-servers/) for those).

The headline: **vendor participation is unusually strong** in this category. DocuSign, SignNow, BoldSign, and eSignatures.com all ship their own MCP servers — a level of official support rare in the MCP ecosystem. **DocuSign's official connector** (beta) is the most enterprise-ready, available through Claude's Connectors Directory. **SignNow has the most complete open-source implementation** with 15 tools including embedded signing experiences. **eSignatures.com leads community adoption** with the most GitHub stars (35).

## Official Vendor Servers

These servers are built and maintained by the e-signature companies themselves. Official support means better API coverage, faster updates when APIs change, and fewer authentication headaches.

### DocuSign MCP Server (Official, Beta)

| Detail | Info |
|--------|------|
| [DocuSign MCP Server](https://developers.docusign.com/platform/mcp-server/) | Official (beta) |
| License | Proprietary |
| Integration | Claude Connectors Directory |
| Auth | DocuSign OAuth |
| Capabilities | IAM + eSignature |

The biggest name in e-signatures now has an official MCP server, available through the Claude Connectors Directory. This isn't a community wrapper — it's built by DocuSign and surfaces both their Identity and Access Management (IAM) platform and core eSignature capabilities.

### What Works Well

**Full eSignature lifecycle.** Create envelopes, send documents for signature, add attachments to drafts, configure workflow steps (delayed routing, conditional recipients), manage contacts in bulk — the complete contract workflow through natural language.

**Enterprise governance preserved.** The MCP server enforces the same permissions, access controls, and audit policies as the DocuSign web UI. Your AI assistant can't do anything your account can't already do. Actions are logged in DocuSign's audit trail.

**Claude Connectors Directory integration.** Available as a managed connector in Claude, meaning setup is simpler than self-hosted MCP servers. OAuth handles authentication automatically.

**Practical use cases.** DocuSign highlights creating contracts from Master Service Agreement templates, sending customer intake packets with identity verification, reviewing AI-suggested redlines, and searching for contracts by expiration date or specific clauses.

### What Doesn't Work Well

**Beta status.** Still in beta with potential breaking changes. Documentation is developer-focused but the feature set may shift.

**Claude-centric.** While MCP is an open standard, the managed connector experience is currently optimized for Claude. Other MCP clients can connect but may require more manual setup.

**No public GitHub repository.** Unlike the other servers in this review, the official DocuSign MCP server isn't open source. You can't inspect the code, contribute fixes, or self-host it.

### SignNow sn-mcp-server (Official)

| Detail | Info |
|--------|------|
| [signnow/sn-mcp-server](https://github.com/signnow/sn-mcp-server) | ~5 stars |
| License | MIT |
| Language | Python |
| Tools | 15 |
| Transport | STDIO + Streamable HTTP |

SignNow's official MCP server is the most feature-complete open-source option. 15 tools covering the full signing workflow, including embedded signing experiences that other servers don't offer.

### What Works Well

**Embedded signing/editor.** Beyond basic send-and-track, SignNow's server generates embedded signing links, embedded sending experiences, and embedded editor sessions. These create in-app signing workflows without redirecting users to SignNow's site — critical for product integrations.

**One-shot template workflows.** `send_invite_from_template` and `create_embedded_*_from_template` combine template selection and action into a single tool call. Draft NDA from template, fill in details, send — one step.

**Dual transport.** Supports both STDIO (for local MCP clients like Claude Desktop) and Streamable HTTP (for web-based and remote integrations). Most e-signature MCP servers only support STDIO.

**Document field pre-filling.** `update_document_fields` lets AI agents pre-fill text fields before sending for signature. Combine with template creation for fully automated contract generation.

### What Doesn't Work Well

**Low star count (5).** Despite being an official vendor server, it hasn't gained much community traction yet. Launched January 2025.

**Python-only.** No TypeScript/Node.js option, which limits integration with JavaScript-heavy MCP toolchains.

### BoldSign MCP (Official)

| Detail | Info |
|--------|------|
| [boldsign/boldsign-mcp](https://github.com/boldsign/boldsign-mcp) | ~4 stars |
| License | MIT |
| Language | TypeScript |
| npm | @boldsign/mcp |
| Regions | US, EU, CA |

BoldSign (by Syncfusion) provides an official TypeScript MCP server published on npm. Clean integration path for Node.js environments.

### What Works Well

**npm package.** `@boldsign/mcp` installs with one command. Most MCP servers require cloning a repo and building from source — BoldSign's npm distribution is notably more developer-friendly.

**Multi-region support.** Configurable API region (US, EU, CA) for data residency compliance. Important for European organizations under GDPR.

**Organized tool categories.** Documents (list, details, revoke, send reminders), templates (list, details, create from template), contacts, users, and teams. Well-structured for agent workflows.

### What Doesn't Work Well

**No embedded signing.** Unlike SignNow, there's no support for generating embedded signing URLs or in-app signing experiences.

**Low star count (4).** Very early in community adoption.

**Requires paid BoldSign account.** Free trial and sandbox available, but the underlying service is paid. No free tier for production use.

## Community Servers

### eSignatures.com MCP Server

| Detail | Info |
|--------|------|
| [esignaturescom/mcp-server-esignatures](https://github.com/esignaturescom/mcp-server-esignatures) | ~35 stars |
| License | MIT |
| Language | Python |
| Focus | Contract lifecycle management |

The most-starred e-signature MCP server. Built for eSignatures.com's API, covering the full contract lifecycle from template creation to signed document management.

### What Works Well

**Complete contract lifecycle.** Create contracts (draft or send immediately), withdraw unsigned contracts, delete drafts, list recent contracts. Template management includes creation, updates, deletion, and collaborator access control.

**Template collaboration.** Invite others to edit templates and revoke editing rights — a workflow feature missing from most other servers. Useful for teams that iterate on contract templates.

**Highest community adoption.** 35 stars makes it the most popular e-signature MCP server on GitHub, suggesting it's the one people actually find and try first.

### What Doesn't Work Well

**eSignatures.com is a smaller platform.** Not DocuSign or SignNow. If you're already using a major e-signature vendor, this server won't help — it only works with eSignatures.com's API.

**Last updated January 2025.** No recent commits, which could indicate stability or abandonment.

### DocuSign Navigator MCP (This Dot Labs)

| Detail | Info |
|--------|------|
| [thisdot/docusign-navigator-mcp](https://github.com/thisdot/docusign-navigator-mcp) | ~0 stars |
| License | MIT |
| Language | TypeScript |
| Focus | Agreement search and analysis |

A community server focused on DocuSign Navigator — the agreement intelligence side of DocuSign, not the signing workflow. Query and analyze existing agreements with natural language.

### What Works Well

**Agreement search.** "Show me pending contracts" or "Find agreements expiring this quarter" — natural language access to DocuSign agreement data without navigating the web dashboard.

**OAuth 2.0 authentication.** Proper OAuth flow, not just API keys. Works with DocuSign's security model.

**Read-only by design.** Can't accidentally send contracts or modify agreements. Safe for exploration and reporting.

### What Doesn't Work Well

**Navigator only.** This is for querying agreement data, not for sending documents or managing signing workflows. Complementary to the official DocuSign MCP server, not a replacement.

**Zero stars.** Minimal community adoption.

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

### SignWell MCP Server (Pipedream)

| Detail | Info |
|--------|------|
| [SignWell MCP](https://mcp.pipedream.com/app/signwell) | Hosted on Pipedream |
| License | Proprietary (hosted) |
| Tools | 12+ |
| Focus | E-signature document workflows |

SignWell's MCP server is hosted on Pipedream's MCP infrastructure rather than distributed as a self-hosted repo. 12+ tools for sending documents, tracking status, and managing signature workflows.

### What Works Well

**Zero infrastructure.** Hosted by Pipedream — no local installation, no dependencies to manage. Configure your MCP client to point at the Pipedream endpoint and go.

**Legally binding signatures.** SignWell specializes in legally binding e-signatures with audit trails and compliance features.

### What Doesn't Work Well

**Not self-hostable.** Pipedream-hosted only. Your API credentials and document metadata flow through Pipedream's infrastructure.

**Limited visibility.** No public GitHub repo to inspect. You're trusting the hosted implementation.

## What's Missing

**No Adobe Acrobat Sign MCP server.** Adobe has MCP servers for Experience Manager and Express, but no dedicated Acrobat Sign MCP server. Given Adobe Sign's market share (second to DocuSign), this is a notable gap. Third-party platforms like Zapier and viaSocket offer wrappers, but no native implementation.

**No Dropbox Sign (HelloSign) MCP server.** Available through Pipedream's hosted MCP, but no open-source, self-hosted server. Dropbox Sign has official SDKs in multiple languages but hasn't built an MCP server.

**No PandaDoc MCP server on GitHub.** PandaDoc is listed in some MCP directories (Composio) but there's no dedicated open-source repository for a PandaDoc MCP server.

**No contract analysis/redlining tools.** These servers handle sending and tracking. None offer AI-powered contract review, clause extraction, or redline comparison — a workflow that would pair naturally with MCP.

## The Verdict

**Rating: 3.5 / 5** — Notable for vendor participation, but the ecosystem is still early.

The e-signature MCP ecosystem stands out for one reason: **vendors actually build and maintain their own servers**. DocuSign, SignNow, BoldSign, and eSignatures.com all ship official MCP implementations. In most MCP categories, you're relying on community wrappers that may break when APIs change. Here, you have official support.

**DocuSign's official connector** is the enterprise choice — managed, governed, and integrated into Claude's Connectors Directory. If you're a DocuSign customer, it's the obvious starting point.

**SignNow's sn-mcp-server** is the best open-source option. 15 tools, embedded signing support, dual transport, MIT license. It's what you want if you need a self-hosted, inspectable implementation.

**eSignatures.com** has the most community traction (35 stars) and the most complete contract lifecycle management, but ties you to a smaller platform.

The 3.5 rating reflects two realities: vendor support is better than almost any other MCP category, but star counts are low across the board (the highest is 35), no server above handles the full "draft, negotiate, sign, store" workflow, and Adobe Sign and Dropbox Sign are conspicuously absent. This is a category where MCP adoption is ahead of community adoption — the servers exist, but most developers haven't found them yet.

*Last updated: March 19, 2026. Star counts and features reflect what we found during research. We do not install or test these servers hands-on — our reviews are based on documentation, source code analysis, GitHub activity, and community feedback. See our [methodology note](/reviews/#methodology) for details.*
