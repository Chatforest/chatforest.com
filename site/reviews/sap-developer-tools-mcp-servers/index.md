# SAP Developer Tools MCP Servers — UI5, CAP, Fiori, MDK, and ABAP for Agentic Coding

> SAP's official MCP servers for developer tooling reviewed: UI5 MCP (81 stars, 8+ tools, v0.2.9), CAP MCP (70 stars, v0.0.4, 2 tools), Fiori MCP (experimental), MDK MCP (v0.3, 4 tools), and the new ABAP MCP Server (GA Sapphire 2026, bundled in ADT, code navigation + migration + clean-core). Rating: 4/5.


SAP serves over 400,000 customers worldwide and has built one of the largest developer communities in enterprise software. For years, SAP development meant navigating dense toolchains: the Cloud Application Programming Model (CAP) for backend services, SAPUI5 (OpenAjax-based framework) and SAP Fiori elements for UX, the Mobile Development Kit (MDK) for mobile apps, and ABAP — the original SAP language running on hundreds of thousands of ERP and S/4HANA systems. In 2025, SAP made a coordinated move to bring MCP to this ecosystem, and at Sapphire 2026 (May 2026) they closed the final major gap by shipping an official ABAP MCP Server. Part of our **[Developer Tools MCP category](/categories/developer-tools/)**.

The headline finding: **SAP is one of the most coordinated enterprise MCP adopters**, with five official servers now covering the full SAP development stack. The **UI5 MCP Server** is the most mature of the open-source servers — actively maintained at v0.2.9, designed to solve a concrete problem (UI5 API hallucination). The **CAP server** is architecturally sound for CDS-model-grounded development. The **Fiori** and **MDK servers** cover their respective niches. And the newly GA **ABAP MCP Server**, bundled in ABAP Development Tools and powered by SAP's own SAP-ABAP-1 foundation model, brings agentic capability to the language that runs most of the world's SAP systems. SAP officially recommends running all five together.

---

## Overview

| Server | Distribution | Stars | Version | Status | License |
|--------|-------------|-------|---------|--------|---------|
| UI5 MCP Server | npm `@ui5/mcp-server` | ~81 | v0.2.9 | Stable | Apache-2.0 |
| CAP MCP Server | npm `@cap-js/mcp-server` | ~70 | v0.0.4 | Early | Apache-2.0 |
| Fiori MCP Server | npm `@sap-ux/fiori-mcp-server` | — | v0.x | Experimental | Apache-2.0 |
| MDK MCP Server | npm `@sap/mdk-mcp-server` | — | v0.3 | Beta | Apache-2.0 |
| UI5 Web Components | npm `@ui5/webcomponents-mcp-server` | — | v0.x | Beta | Apache-2.0 |
| **ABAP MCP Server** | **Bundled in ADT (Eclipse + VS Code)** | — | GA May 2026 | **GA** | Proprietary |

The four open-source servers are available on npm and compatible with Claude Desktop, Claude Code, Cursor, Windsurf, VS Code (Copilot), GitHub Copilot, and Cline. All use stdio transport. The ABAP MCP Server ships inside SAP's ABAP Development Tools and integrates with Joule for Developers on SAP BTP.

---

## UI5 MCP Server — The Flagship

**GitHub:** [UI5/mcp-server](https://github.com/UI5/mcp-server) · ~81 stars · Apache-2.0 · v0.2.9

The UI5 MCP Server is the most mature of SAP's MCP offering and addresses a well-defined problem: AI coding assistants hallucinate SAPUI5 APIs. UI5 has thousands of components, properties, and methods, and LLMs routinely invent APIs that don't exist or suggest deprecated patterns. The UI5 MCP server solves this by giving the AI agent direct access to the live UI5 API reference, UI5 CLI tools, linting, and project scaffolding.

### Tools

| Tool | Purpose |
|------|---------|
| `get_api_reference` | Searches and returns UI5 API docs for a given component or namespace |
| `create_ui5_app` | Scaffolds a new UI5 app from one of the official project templates |
| `get_guidelines` | Returns UI5 development best practices for the current project context |
| `get_project_info` | Extracts metadata and configuration from the current UI5 project |
| `get_version_info` | Returns current UI5 framework version information |
| `run_ui5_linter` | Runs `@ui5/linter` and returns analysis results and issue reports |
| `get_typescript_conversion_guidelines` | Returns guidelines for converting SAPUI5 apps from JavaScript to TypeScript |
| `get_integration_cards_guidelines` | Returns guidelines for building UI Integration Cards |
| `create_integration_card` | Scaffolds a new UI Integration Card project |
| `run_manifest_validation` | Validates the app's manifest against the UI5 Manifest schema |

Ten tools in total, covering the full SAPUI5 development lifecycle: scaffolding, documentation lookup, code quality, TypeScript migration, and Integration Cards. The server connects to SAP's live API reference, meaning the AI agent is always working from current documentation rather than stale training data.

### What Works Well

**Hallucination prevention.** The API reference tool gives agents accurate, current documentation for UI5's extensive component library. This solves a real problem that affects any developer using AI coding assistants with SAPUI5.

**Full development lifecycle.** Most MCP developer tools cover only one thing (documentation or scaffolding or linting). The UI5 server covers all three — plus TypeScript conversion and manifest validation. This is rare breadth.

**Active maintenance.** v0.2.9 indicates real iteration — this isn't a launch-and-forget project. The addition of Integration Cards support in a later release shows the SAP team is tracking developer needs.

**Context awareness.** `get_project_info` and `get_guidelines` are project-aware — they examine the current workspace rather than returning generic documentation. This allows more relevant recommendations.

### What's Missing

**No runtime tools.** The server cannot start a development server, run unit tests, or preview an application. You can scaffold and lint, but not run. Developers still need to invoke `ui5 serve` manually.

**SAPUI5 focus only.** The UI5 framework (XML views, MVC pattern) is the original SAP UI technology. The UI5 Web Components framework (see below) and SAP Fiori elements have their own separate MCP servers, creating a fragmented experience for developers who span multiple UI technologies.

---

## CAP MCP Server — CDS Model + Documentation Intelligence

**GitHub:** [cap-js/mcp-server](https://github.com/cap-js/mcp-server) · ~70 stars · Apache-2.0 · v0.0.4

The Cloud Application Programming Model (CAP) is SAP's primary framework for building cloud-native services on SAP BTP. CAP uses the Core Data Services (CDS) language to define data models, services, and annotations — and the compiled CDS model contains the canonical representation of your application's domain. The CAP MCP server makes this model available to AI agents.

### Tools

| Tool | Purpose |
|------|---------|
| `search_model` | Fuzzy search over compiled CDS definition names (entities, services, annotations, endpoints) |
| `search_docs` | Semantic vector search over preprocessed CAP documentation |

Only two tools, but they address the two most common AI assistant failures in CAP development: not knowing the project's data model and not knowing the framework's APIs.

**`search_model`** performs fuzzy matching against CDS definition names — searching for "book" finds the "Books" entity. This grounds the AI agent in the actual project structure rather than having it infer the model from raw `.cds` files. It exposes entities, services, annotations, and HTTP endpoints from the compiled model.

**`search_docs`** uses local vector embeddings to search preprocessed CAP documentation. The embeddings are pre-built by SAP and shipped with the package — no external API call required. This provides semantic search (not just keyword match) over the full CAP framework documentation.

### What Works Well

**Model grounding.** Giving agents access to the compiled CDS model (not the raw `.cds` source) is architecturally correct — it exposes the same view that the CAP runtime uses. This means the agent understands actual service endpoints, resolved annotations, and computed relationships.

**Local documentation search.** Pre-embedded CAP docs ship with the npm package — no API key required, no latency from external lookups, works offline. Semantic search finds relevant documentation even when the query terms don't exactly match documentation headings.

**Composable.** SAP explicitly designed this server to be used alongside the Fiori MCP server — CAP provides the data service layer, Fiori handles the UI generation layer.

### What's Missing

**Very early stage.** v0.0.4 with two tools is a starting point. There's no CDS project generation, no migration assistance, no service testing, no BTP deployment support. The tool count is expected to grow significantly.

**CAP Node.js only.** The server currently targets CAP Node.js projects. CAP Java is not supported in this version.

---

## SAP Fiori MCP Server — Fiori Elements Application Generation

**GitHub:** [SAP/open-ux-tools](https://github.com/SAP/open-ux-tools/tree/main/packages/fiori-mcp-server) · npm: `@sap-ux/fiori-mcp-server` · Apache-2.0 · Experimental

SAP Fiori elements generates UI5-based applications from OData annotations — developers declare the shape of the UI in annotations, and Fiori elements renders standard floorplans (List Report, Object Page, Analytical List, etc.). The Fiori MCP server makes this generation pipeline accessible to AI coding assistants.

### Tools

| Tool | Purpose |
|------|---------|
| `find_fiori_apps` | Scans workspace directory to find existing SAP Fiori applications |
| `get_functionalities` | Returns supported operations for creating or modifying a Fiori app |
| `execute_functionality` | Executes a specific operation to create or modify a Fiori application |
| `search_documentation` | Semantic search over Fiori elements, Annotations, UI5, and SAP Fiori tools docs |

The flow: the agent finds existing apps in the workspace, queries what operations are available, executes generation or modification operations with parameters, and can search documentation mid-session when it needs framework guidance.

### What Works Well

**Fiori elements generation.** Creating Fiori elements applications from scratch requires knowledge of OData service metadata, annotation files, and Fiori tools CLI. The MCP server abstracts this into operations that an AI agent can invoke based on natural language intent.

**Documentation integration.** The `search_documentation` tool covers Fiori elements, OData Annotations, SAPUI5, and Fiori Tools — giving the agent framework knowledge without requiring pretrained expertise.

**CAP integration.** In v1, generation targets CAP Node.js projects. The combination of CAP MCP + Fiori MCP allows end-to-end development: define the data model in CAP, then generate the UI from it in Fiori elements.

### What's Missing

**Experimental status.** SAP flags this server as experimental and subject to rapid change. The v1 generator only targets CAP Node.js; OData V4 services from non-CAP sources are not yet supported.

**Limited floorplan control.** The generator follows Fiori elements conventions — it doesn't expose fine-grained UI customization. Teams with significant Fiori extensions or custom sections may find the server's scope insufficient.

---

## MDK MCP Server — Mobile Development Kit

**GitHub:** [SAP/mdk-mcp-server](https://github.com/SAP/mdk-mcp-server) · npm: `@sap/mdk-mcp-server` · Apache-2.0 · v0.3 (January 20, 2026)

The Mobile Development Kit (MDK) is SAP's platform for building offline-capable mobile applications that run on SAP Mobile Services. MDK uses a declarative JSON-based schema to define pages, actions, and rules — and the MDK CLI handles build and deployment to iOS and Android. The MDK MCP server exposes this entire workflow to AI coding assistants.

### Tools

| Tool | Purpose |
|------|---------|
| `mdk_generate` | Generate a new MDK project or add pages/actions to an existing one |
| `mdk_validate` | Validate the project schema against the MDK schema definitions |
| `mdk_build` | Build the MDK application bundle |
| `mdk_deploy` | Deploy the app and generate a QR code for onboarding via SAP Mobile Services |

v0.3 consolidated to 4 tools (optimized from more in earlier versions) plus added support for generating MDK Rule definitions.

### What Works Well

**Full lifecycle coverage.** Generate → validate → build → deploy is a complete pipeline. The QR code generation for Mobile Services onboarding is a practical last-mile feature — developers can go from "create a new app" to "scan this QR code to test on your device" in one AI-assisted session.

**Project templates.** The generator supports Base, Empty, List-Detail, and CRUD templates. Combined with the OData service metadata from the `.service.metadata` file, the agent can scaffold a mobile app connected to a real backend service.

**Schema validation.** MDK's JSON schema is complex and version-specific. The validate tool catches schema errors before a build attempt — a concrete quality-of-life improvement over manual MDK development.

**Community adoption evidence.** An SAP community post documented building a real AI-Powered Business Card Scanner using MDK + MCP — demonstrating that the server is production-viable for real workflows, not just demos.

### What's Missing

**Specialized audience.** MDK is for enterprise mobile development on SAP Mobile Services. Developers outside the SAP mobile ecosystem have no use for this server. The addressable audience is a subset of SAP's already-specialized developer base.

**Cloud Foundry CLI dependency.** Creating new applications requires the CF CLI and a configured `.service.metadata` file with SAP Mobile Services connection details. The setup prerequisite is non-trivial for developers new to SAP BTP.

---

## ABAP MCP Server — Official SAP ABAP Development Tools Integration

**Distribution:** Bundled in ABAP Development Tools for Eclipse and VS Code · Official SAP product · GA May 2026 (Sapphire 2026) · Proprietary

The ABAP MCP Server closes the most significant gap in SAP's MCP portfolio. ABAP — the language powering hundreds of thousands of SAP ERP, ECC, and S/4HANA systems — was conspicuously absent from SAP's 2025 MCP launch. At Sapphire 2026, SAP shipped the ABAP MCP Server as part of a broader "agentic AI for ABAP" initiative. It is not a standalone npm package; it ships bundled inside SAP's official ABAP Development Tools (ADT) for both Eclipse and the new ABAP Cloud Extension for VS Code.

Unlike the four open-source servers above, the ABAP MCP Server is proprietary and tightly integrated with **SAP-ABAP-1** — SAP's own ABAP foundation model, trained on 250 million lines of ABAP code — accessed via SAP AI Core on BTP as part of the Joule for Developers subscription.

### Capabilities

The ABAP MCP Server exposes classic ADT operations as MCP tools, making them available to any MCP-compatible AI coding assistant:

| Capability | Description |
|-----------|-------------|
| Code navigation | Browse and locate ABAP objects across the system |
| Object creation | Create ABAP development objects (programs, classes, function groups) |
| Syntax checking | Run syntax validation on ABAP code |
| Unit test execution | Execute ABAP Unit tests and return results |
| Source retrieval | Retrieve source for ABAP programs, classes, Function Groups, Function Modules, and structures |
| Clean-core compliance | Validate code against S/4HANA clean-core requirements |

These capabilities are exposed to external AI clients — GitHub Copilot, Amazon Q Developer, Claude, and MCP-compatible IDEs like Cursor — without requiring those clients to implement ADT-specific protocols.

### The ABAP Migration Agent

The flagship use case shipping with the ABAP MCP Server is an autonomous **custom-code migration agent** for ECC → S/4HANA migration. The agent-driven workflow:

1. Retrieve existing ECC source code via the ABAP MCP Server
2. Check clean-core compatibility (identify deprecated APIs, direct table access, etc.)
3. Generate a migrated S/4HANA version using SAP-ABAP-1
4. Run ABAP Unit tests to validate correctness
5. Return the migrated, tested code

This is one of the first SAP-native multi-step agentic workflows using MCP as the execution layer — ABAP MCP is the tool surface that lets the agent interact with a live SAP system, not just generate code in a sandbox.

### What Works Well

**Fills the largest gap.** ABAP runs more enterprise business logic than any other SAP language. The community servers by Marian Zeis have been bridging this gap; the official ADT-bundled server brings first-party support, SAP-ABAP-1 model integration, and Joule for Developers licensing.

**IDE agnosticism.** ABAP development was historically locked to Eclipse ADT. The MCP server decouples ABAP system access from the IDE — VS Code, Cursor, or any MCP-compatible assistant can now perform ABAP development tasks without Eclipse.

**Multi-agent compatibility.** GitHub Copilot, Amazon Q Developer, and Claude are all explicitly supported via the SAP-Anthropic partnership (announced concurrently at Sapphire 2026). This is among the first cases where major AI coding assistants from competing vendors can all connect to the same ABAP system through a shared MCP protocol.

**SAP-ABAP-1 grounding.** The underlying model is trained on 250 million lines of ABAP — more ABAP-specific training than any general-purpose LLM. Code generation and migration recommendations reflect actual ABAP patterns rather than extrapolated general programming knowledge.

### What's Missing

**Proprietary and bundled.** Unlike the four open-source servers, there is no public GitHub repository, no npm package, and no community-visible version history. Self-hosting, customization, or inspection of the server internals is not possible.

**Requires Joule for Developers subscription.** Access to SAP-ABAP-1 and the agentic features runs through SAP AI Core on BTP under Joule for Developers licensing. As of Sapphire 2026, the promotion is free through September 2026; after that, consumption-based pricing via AI Units applies. Teams on-premise without BTP footprint face a higher barrier.

**No RAP/Steampunk support at launch.** RESTful ABAP Programming Model (RAP) — the modern clean-core ABAP extension model — is not fully covered at GA. The migration agent focuses on classical ABAP to clean-core conversion, not new RAP development workflows.

---

## UI5 Web Components MCP Server — Framework-Agnostic SAP UI Components

**GitHub:** [UI5/webcomponents-mcp-server](https://github.com/UI5/webcomponents-mcp-server) · npm: `@ui5/webcomponents-mcp-server` · Apache-2.0

A fifth server, separate from the main UI5 MCP Server, targeting developers who use UI5 Web Components in non-SAPUI5 contexts — React, Angular, Vue, Svelte, or plain JavaScript. UI5 Web Components are standards-based web components (not SAPUI5) that implement the SAP Fiori design system without requiring the SAPUI5 framework.

### What It Does

- Fetch API docs for any UI5 Web Component (properties, slots, events, methods) across `@ui5/webcomponents`, `@ui5/webcomponents-fiori`, and `@ui5/webcomponents-ai` packages
- Get integration guides for React, Angular, or JavaScript — including installation, imports, and usage examples
- List all available UI5 Web Components with summaries
- Fetch documentation file content directly

This server is narrower than the main UI5 MCP Server — no scaffolding, no linting — but it serves a different audience: developers building SAP Fiori-styled UIs using modern frameworks without the SAPUI5 stack.

---

## Community SAP MCP Servers

The SAP community has built additional servers not covered by the four official offerings:

**[marianfoo/mcp-sap-docs](https://github.com/marianfoo/mcp-sap-docs)** (169 stars, v0.3.21) — aggregates SAP Help Portal documentation, UI5 API reference, CAP docs, ABAP keyword reference, and SAP Community content into a single searchable MCP tool. Hybrid BM25 + semantic search, offline-capable, zero-config npx install. The most widely-adopted community SAP MCP server.

**ABAP / ADT servers** — independent consultant Marian Zeis has built **[arc-1](https://github.com/marianfoo/arc-1)** (v0.7.2, 1,367+ unit tests) for enterprise ABAP ADT integration, and **[abap-mcp-server](https://github.com/marianfoo/abap-mcp-server)** for unified ABAP/RAP documentation search with a public hosted endpoint. These cover classical and modern ABAP development that the official CAP/Fiori servers don't touch.

**SAP Notes access** — **[mcp-sap-notes](https://github.com/marianfoo/mcp-sap-notes)** uses Playwright browser automation to search SAP's proprietary Notes/KBA database — content not available via any official API.

For a full review of Zeis's four servers and how they complement the official SAP offering, see our **[Marian Zeis SAP Community MCP Servers review](/reviews/marianfoo-sap-community-mcp-servers/)**.

A [community-maintained list](https://github.com/marianfoo/sap-ai-mcp-servers) (marianfoo/sap-ai-mcp-servers) tracks 20+ SAP MCP servers (official and community) as of 2026.

---

## Using the Stack Together

SAP's recommended configuration for modern BTP development uses all four open-source servers simultaneously:

```json
{
  "mcpServers": {
    "ui5": { "command": "npx", "args": ["-y", "@ui5/mcp-server"] },
    "cap": { "command": "npx", "args": ["-y", "@cap-js/mcp-server"] },
    "fiori": { "command": "npx", "args": ["-y", "@sap-ux/fiori-mcp-server"] },
    "mdk": { "command": "npx", "args": ["-y", "@sap/mdk-mcp-server"] }
  }
}
```

The intended workflow: CAP defines your data service (CDS model, OData endpoint), the Fiori server generates the UI from the service, the UI5 server handles component-level development and linting, and the MDK server handles the mobile channel. Together they cover the full SAP BTP development stack for a modern cloud-native project.

**ABAP stack:** The ABAP MCP Server is configured separately, through ABAP Development Tools for VS Code — it connects directly to the SAP ABAP system via ADT and Joule for Developers on BTP, rather than an npx command.

**IDE Support:** Cursor, Windsurf, GitHub Copilot (VS Code), Cline, Claude Code, Claude Desktop. ABAP MCP additionally supports Amazon Q Developer (officially tested by SAP) via the SAP-Anthropic partnership announced at Sapphire 2026.

---

## What's Not Covered

**ABAP (now officially addressed).** As of Sapphire 2026, SAP ships an official ABAP MCP Server bundled in ABAP Development Tools. Classical ABAP development, syntax checking, unit tests, and S/4HANA migration workflows are now covered. RAP (RESTful ABAP Programming Model) support is partial at GA. Community servers by Marian Zeis remain valuable for teams without BTP/Joule for Developers access.

**SAP Integration Suite / BTP Integration.** No official MCP server for iFlow development, API management, or the BTP Integration Suite.

**SAP Analytics Cloud / Datasphere.** No official server for analytics development. Community Datasphere servers exist.

**HANA.** No official SAP HANA MCP server from SAP directly (community options exist).

**Business Application Studio.** SAP Business Application Studio has no MCP server of its own, though it hosts MCP-compatible AI assistants that connect to the ABAP MCP Server.

---

## Assessment

**Rating: 4/5** *(refreshed May 2026 — up from 3.5/5)*

SAP has made a more coordinated MCP push than any enterprise software vendor of comparable scale. The four open-source servers (UI5, CAP, Fiori, MDK) launched in a tight window in 2025, all Apache-2.0, targeting a coherent developer workflow. The UI5 MCP Server is the strongest of the open-source group — actively maintained, meaningful tool count, solving a concrete pain point (SAPUI5 API hallucination). The CAP server is architecturally sound. Fiori and MDK are more specialized but complete for their audiences.

The Sapphire 2026 addition of the **ABAP MCP Server** resolves the largest gap from the original review. ABAP is the language running most of the world's SAP systems, and its absence from the MCP portfolio was the most significant limitation. The official ADT-integrated server — powered by SAP-ABAP-1, supporting GitHub Copilot, Amazon Q, Claude, and Cursor, with an autonomous ECC→S/4HANA migration agent — is a substantial addition.

The rating stops at 4/5 because: the ABAP server is proprietary and requires a Joule for Developers subscription (breaking the otherwise clean Apache-2.0 story), SAP Integration Suite and Analytics Cloud remain unaddressed, and the Fiori server's experimental status persists.

For SAP developers: the UI5 MCP Server is worth adding immediately; the ABAP MCP Server is worth evaluating seriously if your team is on BTP and facing S/4HANA migration work.

| Aspect | Score | Notes |
|--------|-------|-------|
| Coverage | 4/5 | ABAP now officially addressed; Integration Suite, Analytics, HANA still absent |
| Maturity | 3.5/5 | UI5 + ABAP stable; CAP/Fiori/MDK still early |
| Tool depth | 4/5 | UI5 (10 tools) + ABAP migration agent are the standouts |
| Adoption | 3/5 | 81 stars (UI5), 70 stars (CAP) — early but genuine traction |
| Licensing | 4/5 | Open-source servers all Apache-2.0; ABAP server proprietary (requires BTP/Joule) |
| **Overall** | **4/5** | Most complete enterprise framework MCP commitment in the ecosystem |

