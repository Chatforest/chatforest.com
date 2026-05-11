# The Palantir MCP Server — Foundry Developer Tools for AI Agents

> Palantir's official MCP server gives AI agents 80+ tools for building and modifying Foundry applications — datasets, ontology, code repositories, Python transforms, and more. Requires a Foundry subscription.


Part of our **[Data Warehouse & Lakehouse MCP Servers roundup](/reviews/data-warehouse-lakehouse-mcp-servers/)**.

**At a glance:** [palantir/palantir-mcp](https://github.com/palantir/palantir-mcp) — 8 GitHub stars, TypeScript, MIT license. v0.13.0 (April 28, 2026). GA since July 14, 2025. 80+ tools across 14 categories. Supports Claude Code, Cursor, Cline, Continue, GitHub Copilot in VS Code, and Windsurf.

Palantir Foundry is an enterprise AI and data operating system used by large organizations — governments, defense contractors, financial institutions, healthcare systems — to build data pipelines, ontologies, and AI-powered applications on top of their most sensitive data. If you are a Foundry developer, this MCP server puts your entire development environment inside your AI IDE.

The `@palantir/mcp` package — installed automatically by the thin open-source wrapper at palantir/palantir-mcp — gives AI agents two things: **context** (curated knowledge about Palantir libraries and Foundry architecture, so agents write idiomatic code) and **tools** (actions to explore your environment and take real steps in Foundry). This became generally available across all Palantir enrollments on July 14, 2025.

A second, separate MCP server — **Ontology MCP (OMCP)** — serves a different role: it exposes your application's ontology resources to external AI agents as MCP tools, enabling them to read objects, run actions, and query data from outside Foundry. OMCP is still in beta. This review covers both.

## What It Does

### Palantir MCP — For Foundry Developers

The official Palantir MCP organizes its 80+ tools into 14 categories:

#### Compass Tools (4 tools)

Tools for resource management and project discovery within Foundry: list resources, search projects, and create new projects. These tools let agents navigate your Foundry environment before modifying anything.

#### Dataset Tools (9 tools)

The core data interaction layer. Includes schema retrieval, SQL query execution, dataset creation, build status checks, and dataset statistics. Agents can query your Foundry datasets directly via SQL, inspect schemas, and create new derived datasets — without leaving the IDE.

#### Data Lineage Tools (1 tool)

Returns the resource graph for data lineage visualization: which datasets feed which transforms, which transforms feed which applications. Useful for understanding impact before making changes.

#### Ontology Tools (12 tools)

The deepest integration point. These 12 tools cover the full ontology configuration surface: object types, link types, and action types. Agents can search, inspect, and modify your ontology schema — creating new object types, defining relationships between them, and configuring actions that write back to underlying datasets. All ontology modifications go through Foundry's proposal review workflow, requiring human approval before changes take effect.

#### Object Set Tools (2 tools)

Query and aggregation functions for ontology objects — retrieve objects matching a filter, aggregate across object sets. These bridge the schema-level ontology tools with actual data retrieval.

#### OSDK Tools (2 tools)

Documentation and code examples for the Ontology SDK (OSDK). Agents use these to understand the TypeScript/Python APIs for building OSDK applications before generating code.

#### Platform SDK Tools (2 tools)

API reference and documentation for Platform SDK endpoints. Similar to OSDK tools but targeting the lower-level Platform SDK for more advanced Foundry integrations.

#### Code Repository Tools (6 tools)

Git operations within Foundry's code repository system: clone repositories, create pull requests, browse code, manage commits. Agents can navigate your Foundry code repos and propose changes, mirroring a normal developer Git workflow.

#### Global Branching Tools (4 tools)

Branch lifecycle management in Foundry's global branching system: create branches, merge proposals, manage branch state. Foundry's branching model spans multiple resources simultaneously (unlike standard Git), and these tools give agents full access to the workflow.

#### Developer Console Tools (4 tools)

SDK generation and application configuration within the Developer Console. Agents can generate OSDK client code for your ontology and configure application settings — reducing the mechanical work of setting up new OSDK applications.

#### Compute Module Tools (4 tools)

Module lifecycle and function execution management. Agents can invoke Compute Module functions, check their execution status, and manage module state — enabling iterative, agent-driven serverless function development.

#### Data Connection Tools (4 tools)

REST API data source and webhook configuration. Agents can define new external data connections into Foundry, pointing at REST APIs and mapping their responses to Foundry datasets.

#### Documentation Search Tools (9 tools)

Curated documentation search across multiple Palantir and related technologies. The most prominent tool here — semantic search across Palantir's documentation — requires Anthropic's AIP (Palantir's AI Platform). Organizations without AIP enabled will see reduced documentation search capability.

---

### Ontology MCP (OMCP) — For External AI Agents

Where Palantir MCP is for developers building inside Foundry, Ontology MCP serves external AI agents consuming Foundry data. Configure it inside Developer Console, point an external MCP client at it, and the AI agent gets tools matching your application's scope: read objects, execute actions, query data.

The critical governance distinction: access is bounded by **application scopes**. The OMCP server exposes only the resources your Developer Console application has permission to access. This makes it viable for production data interaction — external agents cannot reach beyond the application's defined boundaries.

**Tradeoff**: any data returned to the AI agent leaves Foundry and is processed by the external LLM provider. The documentation is explicit about this: "By enabling Ontology MCP on your local device with LLMs hosted outside of Palantir AIP, you are making data in your Palantir environment available to an external MCP client." Organizations with strict data residency requirements must weigh this against the use case.

OMCP is currently in **beta**, with its API subject to change.

## Installation

An administrator must first enable Palantir MCP in the Foundry Control Panel under **Code Repositories**. Once enabled, individual developers:

1. Generate a user token from their Foundry account settings
2. Configure their IDE with the MCP server, pointing at their Foundry hostname (e.g., `mycompany.palantirfoundry.com`)
3. Provide the token as the `FOUNDRY_TOKEN` environment variable

Supported IDEs: **Claude Code**, **Cursor**, **Cline**, **Continue**, **GitHub Copilot in VS Code**, **Windsurf**. The Claude Code integration is a first-class supported path — Palantir's docs show `claude mcp add palantir-mcp` as the quickest setup.

The public GitHub repository (palantir/palantir-mcp) is a lightweight TypeScript wrapper that handles preflight checks (Node.js version, network connectivity, token validation), configures NPM to use Foundry's internal package registry, and downloads and runs the private `@palantir/mcp` package. The actual tool implementations live inside that private package, which is updated independently — users get the latest tools without changing their local configuration.

## What Works Well

**Breadth without sprawl.** 80+ tools is a large number, but the 14-category organization reflects the actual Foundry development surface: datasets, ontology, repos, transforms, modules, applications, connections, and documentation. Every major daily-driver task for a Foundry developer is covered.

**Proposal-first writes.** Ontology modifications don't apply immediately — they create proposals that require human review and approval before taking effect. This is the right default for a system that manages enterprise production data. Agents can draft ontology changes freely; human architects approve them.

**Write protections on datasets.** Agents can create new datasets but cannot update or delete existing ones. For a platform that holds organizations' most sensitive operational data, non-destructive defaults are essential.

**Always-current tooling.** Because the actual `@palantir/mcp` package is downloaded fresh from Foundry's registry each time the server starts, developers don't need to update their MCP configuration to get new tools. Palantir can ship tool updates without requiring user action.

**Claude Code as a first-class integration.** Palantir's documentation features Claude Code alongside Cursor as a primary supported IDE. The server is listed as a supported MCP configuration in Claude Code's project scope (`.mcp.json`), making it straightforward to enable for an entire Foundry development team.

**Security-conscious data flow documentation.** Palantir clearly documents what data leaves Foundry and where it goes by IDE (Anthropic for Claude Code, Microsoft for Copilot, etc.). This transparency is uncommon among enterprise MCP servers and helps platform security teams make informed decisions.

## What's Not

**Foundry subscription required — hard stop for most developers.** Palantir Foundry is an enterprise platform with enterprise pricing. If you don't already have a Foundry subscription, there is no evaluation path, no free tier, and no sandbox. The GitHub repository has 8 stars partly because the potential user base is limited to existing Foundry customers — a small fraction of the broader developer community.

**Ontology MCP is still Beta.** The more interesting server for external AI integration — OMCP — is not yet stable. APIs will change. Organizations planning production integrations around OMCP are building on a moving target.

**Data governance complexity at the boundary.** The moment external AI agents connect to Ontology MCP with an external LLM, sensitive Foundry data crosses the boundary to that LLM provider. For organizations whose entire rationale for using Foundry is strict data control, this is a significant tradeoff that requires careful governance. In-platform AIP usage keeps data inside Foundry, but that limits AI IDE choice to Palantir's own tooling.

**Low GitHub visibility signal.** 8 stars on palantir/palantir-mcp reflects its role as a thin installer wrapper, not community adoption of the actual MCP server. The `@palantir/mcp` package itself — where the 80+ tools live — is private and distributed through Foundry's internal registry. External adoption metrics are essentially invisible.

**Node.js dependency.** The wrapper requires Node.js, adding a runtime dependency that some development environments may not have. The preflight check catches this early, but it's an additional setup step compared to servers distributed as compiled binaries.

## How It Compares

Palantir MCP occupies a unique position: it is not competing with general-purpose database MCP servers or data warehouse connectors. Its 80+ tools are almost entirely about the Foundry *development workflow* — building the ontology, writing transforms, creating OSDK applications, managing code. By contrast, most enterprise data platform MCP servers focus on *querying data*.

The closest structural parallel is the [Databricks managed MCP servers](https://www.databricks.com/) — both provide a suite of tools across a proprietary enterprise data platform, both are officially maintained, and both require a subscription. Databricks offers four managed servers (Unity Catalog, Vector Search, Agent Evaluation, and SQL Execution). Palantir's approach is more unified — a single server covering developer tooling — plus the separate OMCP for data consumers.

The community Palantir Foundry MCP server by Dana K. Williams (available on PulseMCP) provides a narrower alternative — ontology data interaction and SQL queries — without the full developer workflow coverage of the official server. For organizations that only need to query Foundry data from an external AI agent, it may be worth evaluating alongside OMCP.

| Option | Type | Audience | Scope | Status |
|--------|------|----------|-------|--------|
| [palantir/palantir-mcp](https://github.com/palantir/palantir-mcp) | Official | Foundry developers | 80+ tools: ontology, datasets, repos, transforms | GA (v0.13.0) |
| Ontology MCP (OMCP) | Official | External AI agents | Application-scoped ontology read/write | Beta |
| Community Foundry MCP | Community | External AI agents | Ontology data, SQL queries | Available |

## Rating: 4/5 — Essential for Foundry Developers; Invisible to Everyone Else

For Palantir Foundry developers, this MCP server is a genuine productivity multiplier. The tool coverage matches the actual daily development workflow, the security design is thoughtful (proposal-first writes, write protections, clear data flow documentation), and the always-current packaging means teams aren't managing version drift. Palantir treating Claude Code as a first-class integration path accelerates adoption.

The 4/5 rather than 5/5 reflects two real gaps: Ontology MCP — the compelling half of the story for external AI integration — is still Beta, and the data governance tradeoff at the LLM boundary is genuinely significant for an enterprise platform whose core selling point is data control.

For the 99% of developers who don't use Palantir Foundry: this review doesn't apply to your stack. Palantir MCP has no standalone value — it is entirely a Foundry extension. That's not a criticism; it's the architecture. For Foundry shops, it's worth deploying immediately.

