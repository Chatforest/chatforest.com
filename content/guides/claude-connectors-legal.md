---
title: "Claude for Legal: Anthropic's 20+ Connectors and 12 Practice-Area Plugins Explained"
date: 2026-05-16T19:00:00+09:00
description: "On May 12, 2026, Anthropic launched Claude for Legal — more than 20 MCP connectors wiring Claude into legal software, plus 12 practice-area plugins covering corporate, litigation, privacy, IP, and more. Here's what each piece does and what this launch means for legal teams."
og_description: "Anthropic's Claude for Legal launch brought 20+ MCP connectors and 12 practice-area plugins to law firms and legal departments on May 12, 2026. This guide explains what each connector does, how the plugins work, and what the access-to-justice component means for the broader legal ecosystem."
content_type: "Guide"
card_description: "Anthropic's May 2026 Claude for Legal launch wired Claude into more than 20 legal software platforms — Harvey, Ironclad, Thomson Reuters, iManage, Everlaw, Relativity, DocuSign, Box, and more — and released 12 practice-area plugins covering commercial, corporate, employment, privacy, IP, and litigation work. This guide explains what each piece does and what the launch means for legal teams and the access-to-justice movement."
last_refreshed: 2026-05-16
---

On May 12, 2026, Anthropic launched **Claude for Legal** — the most significant coordinated push into the legal technology market by any AI company since Harvey AI's emergence two years earlier. The announcement packaged three distinct things: more than 20 MCP connectors wiring Claude into the software law firms and legal departments already run on; 12 practice-area plugins providing pre-configured workflows for specific legal disciplines; and a set of access-to-justice partnerships targeting the 80% of civil litigants who appear in court without an attorney.

The launch came less than three weeks after a parallel push into creative tools and closely followed a finance-focused release. The pattern is deliberate: Anthropic is systematically verticalizating Claude with deep integrations into software categories where knowledge workers are already spending their time.

Legal professionals have become the most engaged Claude Cowork users of any knowledge-work function — a data point Anthropic cited in the announcement. The legal launch converts that usage into deeper, bidirectional integration with the platforms that legal work actually runs on.

This guide explains what each connector does, how the plugins are structured, what the access-to-justice partnerships cover, and what this launch means for the legal MCP ecosystem. Our analysis is based on published documentation, vendor announcements, and third-party reporting — we research and analyze rather than testing these integrations hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; content is researched and written by AI.

---

## How Claude Connectors Work in Legal Contexts

Claude connectors for legal are built on the **Model Context Protocol (MCP)** — the same open standard powering thousands of community-built servers across the broader MCP ecosystem. Each legal software platform exposes its capabilities as discrete MCP tools; Claude calls those tools through the MCP client (Claude Desktop, Claude Cowork, or another compatible host); the application executes the requested action.

In legal contexts, this matters for a specific reason: legal work is inherently cross-system. A single task — drafting a contract, responding to discovery, reviewing an acquisition — might require pulling from a document management system, running a legal research query, checking a compliance database, and routing a document for signature. MCP connectors let Claude participate in that workflow without each step requiring a manual export, copy-paste, or context re-explanation.

Three architectural points are worth noting:

**Context persists across applications.** Claude for Legal includes cross-Office integration — Claude now works within Microsoft Word, Outlook, Excel, and PowerPoint, carrying context across all four applications. A redline completed in Word does not need to be re-explained when it carries over to a cover note in Outlook or a board summary in PowerPoint. This cross-app context is one of the more practically significant features of the launch.

**Plugins learn team-specific playbooks.** Each practice-area plugin starts with a setup interview that learns a team's specific playbooks, escalation chains, risk calibration, and house style. The plugin's pre-configured prompts and guardrails then apply that knowledge. This is closer to an onboarding workflow than a generic AI tool.

**Open standard, available across clients.** Because connectors are built on MCP, they work with any MCP-compatible client — not just Claude. Firms that want to connect these platforms to other AI systems can do so through the same connector infrastructure.

For background on the MCP standard itself, see our [introduction to MCP](/guides/what-is-mcp/) and our [comprehensive MCP and legal guide](/guides/mcp-legal-law/).

---

## The 20+ Connectors

Anthropic organized the connectors into functional categories that map to how legal teams structure their work.

### Legal AI Assistants

**Harvey** — The highest-profile legal AI startup (11B valuation, $195M ARR as of March 2026) connects to Claude through an MCP integration, allowing Claude to work alongside or hand off to Harvey's legal-specific reasoning capabilities. Harvey has focused on case law research, document drafting, and due diligence workflows.

**Solve Intelligence** — A contract intelligence platform that connects Claude to patent drafting, technical claim analysis, and prior art review. Primarily relevant for IP practice groups and patent prosecution teams.

---

### Contract Lifecycle Management

**Ironclad** — A contract lifecycle management platform used extensively in corporate legal departments. The connector allows Claude to retrieve contract data, track obligation milestones, initiate drafting workflows, and surface relevant precedent from prior agreements. Ironclad handles high-volume commercial contracting, and the connector extends Claude's reach into those workflows without requiring export from the platform.

**Definely** — Contract drafting and review platform focused on clarity and consistency. The connector surfaces Definely's clause-level analysis within Claude's context, allowing in-line drafting assistance grounded in the platform's risk and consistency checks.

**DocuSign** — E-signature and agreement lifecycle platform. The DocuSign connector allows Claude to initiate signature workflows, check agreement status, retrieve signed documents, and surface envelope history. Given DocuSign's near-universal adoption in legal departments, this connector provides practical value even for teams that do not use other platforms in the launch.

See our [MCP and contract management guide](/guides/mcp-legal-contract-management/) for a broader survey of CLM and e-signature MCP servers.

---

### Legal Research

**Thomson Reuters** — Expanded partnership announced simultaneously with the Claude for Legal launch. The connector wires Claude into **Westlaw**, the dominant case law and statutory research platform, enabling natural-language research queries, citation retrieval, and document analysis grounded in Westlaw's authoritative legal database. This is the connector most likely to change day-to-day associate workflows at large law firms.

**Midpage** — Legal research platform focused on case law citation verification and hallucination detection. The Midpage connector provides Claude with a mechanism to verify legal citations before they appear in work product — a directly practical application given hallucinated citations' high-profile role in legal AI concerns.

**Trellis** — State court records and litigation analytics platform, covering trial court dockets that federal PACER and CourtListener do not fully index. The Trellis connector gives Claude access to state-level litigation data for opposing counsel analysis, judge research, and litigation strategy.

**Legal Data Hunter** — Regulatory and legislative data retrieval, enabling Claude to search and retrieve regulatory text, agency guidance, and legislative history across multiple jurisdictions.

**Descrybe** — Document analysis and data extraction platform. The connector surfaces Descrybe's structured extraction capabilities within Claude workflows, relevant for large-volume document review and due diligence contexts.

**Free Law Project** — Non-profit operator of CourtListener and the RECAP Archive of federal court documents. The Free Law Project connector is the access-to-justice cornerstone of the launch — it provides Claude with access to free, open legal data that does not require a Westlaw or LexisNexis subscription.

---

### E-Discovery and Litigation Support

**Everlaw** — Cloud-based e-discovery platform used in complex litigation. The connector allows Claude to interact with Everlaw document sets, run searches, surface relevant documents, and assist with deposition preparation and case analysis. E-discovery is a high-volume, high-cost litigation activity where AI assistance has clear time-savings potential.

**Consilio** — Legal services firm providing managed review, e-discovery, and legal operations support. The Consilio connector integrates Claude into managed review workflows, relevant for large law firms running complex litigation matters.

**Relativity** — The dominant e-discovery platform in large-scale litigation. Relativity's connector gives Claude access to document review queues, search functionality, and production workflows within the Relativity ecosystem. Combined with Everlaw, the launch covers both major e-discovery platform camps.

---

### Document Management

**iManage** — The most widely deployed document management system in law firms. The iManage connector gives Claude access to matter-centric document organization, version history, and workspace navigation — essential for any workflow that requires retrieving prior work product or filing new documents in the right matter structure.

**NetDocuments** — Cloud-native document and email management platform, widely used by mid-sized and regional firms. The NetDocuments connector provides parallel document retrieval and filing capabilities to iManage's connector.

---

### In-House and Legal Operations

**Lawve AI** — In-house legal operations platform focused on request intake, matter management, and legal department workflow. The connector allows Claude to surface pending matters, update statuses, and interact with the legal ops layer that in-house teams run on.

**The L Suite** — Legal operations platform covering vendor management, spend tracking, and matter analytics. Primarily relevant for general counsel offices and in-house legal departments managing external counsel relationships and legal spend.

---

### Transactional and Deal Management

**Box** — Cloud content and collaboration platform widely used in deal rooms and M&A transactions. The Box connector gives Claude access to shared deal room documents, version history, and collaboration workflows — relevant for transactional work where documents are often organized outside of firm DMS systems.

**Datasite** — Virtual data room (VDR) platform purpose-built for M&A, fundraising, and other high-stakes transactions. The Datasite connector allows Claude to interact with VDR document sets during due diligence processes, reducing the friction of retrieving and analyzing documents within a secure VDR environment.

---

### Access to Justice

**Courtroom5** — Platform designed for pro se (self-represented) civil litigants, who make up roughly 80% of civil court participants in the US. The Courtroom5 connector extends Claude's capabilities to people navigating civil courts without an attorney — drafting motions, understanding procedural rules, and preparing for hearings.

**BoardWise** — Platform helping licensed professionals navigate state board matters, licensing disputes, and regulatory proceedings. The connector provides Claude with context about state board processes and requirements for professionals who cannot afford specialized legal counsel.

These two connectors are the most consequential for people who are not legal professionals. Combined with the Free Law Project connector's access to open legal data, they represent a meaningful access-to-justice dimension that distinguishes the Claude for Legal launch from a purely commercial rollout.

---

## The 12 Practice-Area Plugins

Plugins are different from connectors. Connectors wire Claude into specific software platforms; plugins configure Claude's behavior for specific legal disciplines. Each plugin starts with a setup interview that learns a team's playbooks, escalation chains, risk calibration, and house style. The result is pre-configured prompts, workflows, and guardrails specific to that area of practice.

The 12 plugins span the major legal practice categories:

**Commercial Legal** — Contract drafting, review, and negotiation support for commercial agreements. Covers vendor contracts, SaaS agreements, partnership contracts, and the full range of commercial deal documentation that legal departments process at volume.

**Corporate Legal** — Covers corporate governance, entity management, and transactional support. Includes specific workflows for **M&A diligence** (organizing, reviewing, and summarizing due diligence materials) and **closing checklists** (tracking conditions, signatures, and deliverables through a transaction close).

**Employment Legal** — Policies, employment agreements, termination documentation, accommodation analysis, and HR-legal coordination. Relevant for both HR departments with embedded legal support and law firm employment practice groups.

**Privacy Legal** — Data processing agreements, GDPR/CCPA compliance workflows, privacy impact assessments, and data breach response documentation. As privacy regulation continues expanding globally, this plugin addresses one of the fastest-growing practice area demands.

**Product Legal** — Terms of service, privacy policies, acceptable use policies, and product-facing legal documentation. Primarily relevant for technology companies and in-house teams supporting product and engineering organizations.

**Regulatory Legal** — Regulatory compliance analysis, agency correspondence, comment letter drafting, and monitoring of regulatory changes across sectors. Works alongside the legal research connectors (Thomson Reuters, Legal Data Hunter) to ground regulatory work in current source documents.

**AI Governance Legal** — A notably timely addition: workflows for AI policy compliance, AI Act requirements, model governance documentation, and internal AI use policy development. Given that AI governance has become a standalone practice area at major firms, the plugin reflects real demand.

**IP Legal** — Patent prosecution support, trademark monitoring, licensing agreement drafting, and IP portfolio management. Works alongside the Solve Intelligence connector for patent-specific technical work.

**Litigation Legal** — Case strategy, brief drafting support, deposition preparation, motion filing checklists, and trial preparation workflows. The litigation plugin is the highest-stakes category, where accuracy requirements are most stringent and hallucination risk is most consequential.

---

## What the Launch Means for Legal Teams

**The integration gap is closing fast — but selectively.** Until May 12, 2026, the dominant commercial legal platforms were almost entirely absent from the MCP ecosystem. Westlaw, iManage, Relativity, Ironclad, and Everlaw had no publicly accessible MCP interfaces. The Claude for Legal launch changes that — but only within the Claude / Anthropic ecosystem. Teams using other AI providers do not benefit from these connectors unless those platforms separately build MCP support.

**Legal AI is no longer a standalone tool.** Legal professionals have used AI (Harvey, CoCounsel, Lexis AI, Westlaw AI) as separate tools accessed outside their primary workflow. The connectors announced May 12 move Claude into the tools where work actually happens: within Westlaw searches, inside iManage matter structures, across Ironclad contract repositories. The shift from "consult the AI" to "AI participates in the workflow" is architecturally significant.

**Hallucination risk is addressed, not eliminated.** Midpage's citation verification connector is the most direct response to the legal profession's primary concern about AI — hallucinated citations and fabricated case law. Grounding Claude's legal outputs in real-time Westlaw data and verification through Midpage reduces (but does not eliminate) the risk. Legal professionals should continue treating AI-drafted legal citations as requiring independent verification.

**Access to justice is a genuine commitment, not just optics.** The Free Law Project, Courtroom5, and BoardWise connectors serve a population that cannot pay for Westlaw subscriptions or hourly legal counsel. These are not high-revenue connectors. Their inclusion alongside Harvey and Relativity signals something about Anthropic's priorities — or, at minimum, is a meaningful statement about the role an AI provider wants to play in access to legal resources.

**Practice-area plugins are a new distribution model.** Pre-configured, team-calibrated plugins represent a different approach to legal AI deployment than generic AI tools. Firms that spend setup time configuring the plugins to match their playbooks get a more predictable tool than general-purpose AI; the setup interview is doing work that would otherwise require prompt engineering or fine-tuning.

---

## Related Resources

- [Claude Connectors for Creative Tools](/guides/claude-connectors-creative-tools/) — parallel analysis of Anthropic's April 2026 creative software launch
- [MCP and Legal/Law: The Full Ecosystem Guide](/guides/mcp-legal-law/) — 120+ MCP servers for legal work, including open-source court data and compliance tools
- [MCP and Contract Management](/guides/mcp-legal-contract-management/) — deep dive on CLM, e-signature, and contract automation MCP servers
- [MCP Reviews Directory](/reviews/) — the full ChatForest directory of MCP server and tool reviews
