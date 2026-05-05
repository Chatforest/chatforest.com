---
title: "SAP Developer Tools MCP Servers — UI5, CAP, Fiori, and MDK for Agentic Coding"
date: 2026-05-05T16:00:00+09:00
description: "SAP's official MCP servers for developer tooling reviewed: UI5 MCP (81 stars, 8+ tools, v0.2.9), CAP MCP (70 stars, v0.0.4, 2 tools), Fiori MCP (experimental, Fiori elements generation), MDK MCP (v0.3, 4 tools, mobile). All Apache-2.0. Rating: 3.5/5."
og_description: "SAP's 4 official developer MCP servers: UI5 (81 stars, 8+ tools, scaffolding + API search + linting), CAP (70 stars, v0.0.4, CDS model + doc search), Fiori (experimental, Fiori elements generation), MDK (v0.3, 4 tools, mobile apps). All Apache-2.0. Rating: 3.5/5."
content_type: "Review"
card_description: "SAP is the only major enterprise software vendor to ship four official, coordinated MCP servers targeting developer productivity — all Apache-2.0, all launched in 2025. The UI5 MCP Server (81 stars, v0.2.9) is the most mature: 8+ tools covering API reference search, app scaffolding, linting, TypeScript conversion, and UI Integration Cards. The CAP MCP Server (70 stars, v0.0.4) provides two tools for semantic search over the CDS model and CAP documentation. The SAP Fiori MCP Server (experimental) generates and edits Fiori elements applications from CAP projects. The MDK MCP Server (v0.3) supports mobile app generation, validation, migration, and deployment for SAP Mobile Services. SAP recommends running all four together for the full agentic development stack. The category earns 3.5/5 — serious enterprise commitment, with the UI5 server already delivering genuine value and CAP/Fiori/MDK in active development."
last_refreshed: 2026-05-05
---

SAP serves over 400,000 customers worldwide and has built one of the largest developer communities in enterprise software. For years, SAP development meant navigating dense toolchains: the Cloud Application Programming Model (CAP) for backend services, SAPUI5 (OpenAjax-based framework) and SAP Fiori elements for UX, the Mobile Development Kit (MDK) for mobile apps, and ABAP for legacy systems. In 2025, SAP made a coordinated move to bring MCP to this ecosystem — not via one generalist server, but four targeted servers, each covering a specific layer of the SAP development stack. Part of our **[Developer Tools MCP category](/categories/developer-tools/)**.

The headline finding: **SAP is one of the most coordinated enterprise MCP adopters**, with four official servers all released within weeks of each other in September 2025, all Apache-2.0 licensed, all maintained by SAP engineering teams. The **UI5 MCP Server is the standout** — the most mature of the four, actively maintained at v0.2.9, and designed to solve a concrete problem (UI5 API hallucination). The **CAP server** is early but architecturally sound. The **Fiori server** is experimental and narrower in scope. The **MDK server** is the most complete for its niche. SAP officially recommends using all four together.

---

## Overview

| Server | npm Package | Stars | Version | Status | License |
|--------|------------|-------|---------|--------|---------|
| UI5 MCP Server | `@ui5/mcp-server` | ~81 | v0.2.9 | Stable | Apache-2.0 |
| CAP MCP Server | `@cap-js/mcp-server` | ~70 | v0.0.4 | Early | Apache-2.0 |
| Fiori MCP Server | `@sap-ux/fiori-mcp-server` | — | v0.x | Experimental | Apache-2.0 |
| MDK MCP Server | `@sap/mdk-mcp-server` | — | v0.3 | Beta | Apache-2.0 |
| UI5 Web Components | `@ui5/webcomponents-mcp-server` | — | v0.x | Beta | Apache-2.0 |

All five servers are available on npm and compatible with Claude Desktop, Claude Code, Cursor, Windsurf, VS Code (Copilot), GitHub Copilot, and Cline. All use stdio transport.

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

SAP's recommended configuration for full-stack SAP development uses all four official servers simultaneously:

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

The intended workflow: CAP defines your data service (CDS model, OData endpoint), the Fiori server generates the UI from the service, the UI5 server handles component-level development and linting, and the MDK server handles the mobile channel. Together they cover the full SAP BTP development stack for a modern project.

**IDE Support:** Cursor, Windsurf, GitHub Copilot (VS Code), Cline, Claude Code, Claude Desktop.

---

## What's Not Covered

**ABAP.** The official servers do not cover ABAP on-premise development. ABAP is the original SAP programming language running on hundreds of thousands of SAP ERP, S/4HANA, and ECC systems. Community servers fill some of this gap.

**SAP Integration Suite / BTP Integration.** No official MCP server for iFlow development, API management, or the BTP Integration Suite.

**SAP Analytics Cloud / Datasphere.** No official server for analytics development. Community Datasphere servers exist.

**HANA.** No official SAP HANA MCP server from SAP directly (community options exist).

**S/4HANA / Business Application Studio.** SAP Business Application Studio has no MCP server. S/4HANA extensions via RAP (RESTful ABAP Programming Model) are not covered.

---

## Assessment

**Rating: 3.5/5**

SAP has made a more coordinated MCP push than most enterprise software vendors of its scale. All four official servers launched in the same release window, all Apache-2.0, all targeting a coherent developer workflow. The UI5 MCP Server is the strongest of the group — actively maintained, meaningful tool count, solving a concrete pain point (API hallucination). The CAP server is architecturally sound despite being early-stage. Fiori and MDK are more specialized but complete for their audiences.

The gaps that prevent a higher rating: ABAP is unaddressed, S/4HANA extensions are unaddressed, and the Fiori server's experimental status and CAP-only constraint limit real-world applicability today. The star counts (81 for UI5, 70 for CAP) are modest — this ecosystem is in early adoption within the SAP developer community.

For SAP developers, the UI5 MCP server in particular is worth adding immediately. The hallucination-prevention value alone justifies the setup.

| Aspect | Score | Notes |
|--------|-------|-------|
| Coverage | 3/5 | CAP + UI5 + Fiori + MDK covered; ABAP, Analytics, HANA absent |
| Maturity | 3/5 | UI5 stable; CAP/Fiori/MDK early stage |
| Tool depth | 4/5 | UI5 has 10 well-designed tools; CAP semantic search is clever |
| Adoption | 3/5 | 81 stars (UI5), 70 stars (CAP) — early but genuine traction |
| Licensing | 5/5 | All Apache-2.0 — no BSL, no proprietary constraints |
| **Overall** | **3.5/5** | Strongest enterprise framework MCP commitment in the ecosystem |
