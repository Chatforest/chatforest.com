# Customer Success MCP Servers — Gainsight, Planhat, Vitally, Pendo, ChurnZero, and More

> Customer success MCP servers reviewed: Gainsight Agentic Stack (4 official MCP servers: CS+Staircase AI at mcp.staircase.ai + Skilljar + Customer Communities + PX — all GA/beta), Planhat official (api.planhat.com, OAuth 2.0, dynamic CRUD), Pendo official GA (OAuth, 15+ tools + 4 new AI Agent Analytics tools), Custify official (18 tools, health scores + playbooks + tasks, MIT), Vitally community (3 servers: fiscaltec 11 tools, johnjjung 9 tools, mattfdigio C#/.NET Auth0), ChurnZero community (15 tools, health + events + segments), Intercom official remote (12 tools, Streamable HTTP, Help Center article tools added), ChurnKey (2 tools, cancel flow analytics). Rating: 4.0/5.


Customer success has become one of the more vendor-committed MCP categories in under six months. **Gainsight**, **Planhat**, and **Pendo** all launched official MCP servers in early 2026 — and on May 28, Gainsight raised the stakes dramatically with its **"Agentic Stack for Customer Retention"**: four official MCP servers (CS+Staircase AI, Skilljar, Customer Communities, Product Experience), a native Agent Studio for building AI workflows, and a CLI coming this summer. **Pendo's MCP server reached general availability** with four new AI Agent Analytics tools. **Custify** ships an open-source 18-tool server. Community implementations exist for **Vitally** (now three independent servers) and **ChurnZero**. **Intercom** expanded from 6 to 12 tools. Part of our **[Business & Productivity](/categories/business-productivity/)** category.

This review covers **dedicated customer success platforms** (Gainsight, Totango, ChurnZero, Vitally, Custify, Planhat, ClientSuccess), **product experience platforms** relevant to CS workflows (Pendo, Gainsight PX), **churn analytics** (ChurnKey), and **customer support platforms** that bridge into CS (Intercom). For CRM platforms, see our [CRM MCP Servers](/reviews/crm-mcp-servers/) review. For helpdesk/ticketing, see [Customer Support & Helpdesk MCP Servers](/reviews/customer-support-helpdesk-mcp-servers/).

The headline finding: **Gainsight now has four official MCP servers** spanning the full customer lifecycle — CS+Staircase AI (the original), Skilljar (learning content), Customer Communities, and Product Experience (PX). The CS+Staircase AI server is GA; the other three are in open beta. **Gainsight's Agentic Stack** adds Agent Studio (plain-language workflow design) and a CLI coming summer 2026. **Planhat differentiates with dynamic CRUD** — its MCP server auto-discovers data models rather than hardcoding tools. **Custify has the best open-source server** with 18 tools covering the full CS workflow from health scores to playbook automation. **Pendo is now GA** with new AI Agent Analytics tools for querying agent entities and product ideas. **The mid-market is still wide open** — Totango/Catalyst, ClientSuccess, SmartKarrot, and CustomerSuccessBox have no MCP servers at all.

## Dedicated Customer Success Platforms

### Gainsight (Official)

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| Gainsight CS + Staircase AI MCP | Hosted HTTP (`mcp.staircase.ai/mcp`) | OAuth (Google/Microsoft SSO) | Multiple | Yes (GA) |
| Gainsight Skilljar MCP | Hosted HTTP | OAuth | Multiple | Yes (beta) |
| Gainsight Customer Communities MCP | Hosted HTTP | OAuth | Multiple | Yes (beta) |
| Gainsight Product Experience (PX) MCP | Hosted HTTP | OAuth | Multiple | Yes (beta) |

**Gainsight** has executed the most aggressive MCP expansion of any CS vendor. Their journey:

- **April 2, 2026**: MCP announced for Gainsight CS + Staircase AI. GA availability April 25, 2026.
- **May 21, 2026**: Developer Studio for Customer Communities launched (vibe coding for community customization).
- **May 28, 2026**: **Agentic Stack for Customer Retention** — MCP expanded to Skilljar, Customer Communities, and Product Experience (all in open beta); Gainsight Agent Studio launched; pre-built agents shipped; CLI announced.

**Gainsight CS + Staircase AI MCP** (GA) at `mcp.staircase.ai/mcp` provides unified access to both platforms in a single connection — Staircase AI for customer intelligence (sentiment, relationship maps, communication analysis) and Gainsight CS for the system of record (health scores, product usage, renewal/contract data) and system of action (CTAs, success plans, journey programs).

Key capabilities:
- **Query customer data in natural language** — health scores, renewal timelines, sentiment trends, relationship maps
- **Take action directly in Gainsight CS** — update records, manage CTAs, log activities, build success plans
- **Build custom workflows without engineering** — renewal playbooks, risk escalation sequences, QBR preparation
- **Meeting prep in 60 seconds** — health snapshot with recommended talking points
- **Portfolio triage** — "what needs attention?" returns prioritized risk and opportunity signals
- **Account handoff briefs** — comprehensive handoff documentation in minutes

Authentication uses **federated SSO** (Google or Microsoft email with Staircase AI access). Role-based access controls carry over. Works with Claude (via Connectors Directory), ChatGPT, and Gemini.

**Gainsight Skilljar MCP** (open beta) connects the Skilljar customer education platform to MCP-compatible tools including Claude Code, Cursor, and ChatGPT. Build courses conversationally with full lessons in a single prompt, enroll learners at scale, move users between groups, and set auto-enrollment rules — all through natural language.

**Gainsight Customer Communities MCP** (open beta) connects Community activity to AI tools. Query community discussions, surface engagement trends, and turn community sentiment into actionable insights. Useful for CS workflows that rely on peer-to-peer support signals alongside product usage data.

**Gainsight Product Experience (PX) MCP** (open beta) provides instant answers about product adoption, feature engagement, and usage patterns — native Gainsight integration replacing the earlier Pipedream-hosted PX server.

**Gainsight Agent Studio** (launched May 28, 2026) lets teams design and automate AI workflows in plain language, pre-wired with 15 years of CS expertise. No engineering required. Pre-built agents include: Staircase Handoff Analyst, Staircase Risk Analyst, Staircase Expansion Analyst, Community Moderation Agent, and Skilljar AI Tutor.

**Gainsight CLI** (coming summer 2026) will let technical admins use Claude Code, Codex, or Gemini to build Gainsight CS workflows without logging into the UI — the first CS platform to offer CLI-level AI agent access.

### Planhat (Official)

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| Planhat MCP Server | Hosted HTTP (`api.planhat.com/v1/mcp`) | Bearer token / OAuth 2.0 | 3 (dynamic) | Yes |

**Planhat** takes a fundamentally different approach from other CS MCP servers. Instead of exposing dozens of hardcoded tools, it provides **three meta-tools** that dynamically discover and interact with any Planhat data model:

1. **Discover models and operations** — explores available Planhat data models and their supported CRUD operations
2. **Get model parameter schema** — retrieves detailed parameter schemas for validation and form generation
3. **Perform operations** — executes CRUD operations on any discovered model

This means the MCP server **automatically adapts to your Planhat configuration** — custom objects, fields, and relationships are all accessible without server updates. An AI agent can discover what data models exist, understand their schemas, and perform operations, all through the same three tools.

Authentication via **Bearer token** (generated in Planhat App Center with scoped permissions) or **OAuth 2.0** (for third-party integrations like ChatGPT and Claude). Enterprise-grade permissioning controls exactly what data the AI model can access. Demo environment available at `api.planhatdemo.com/v1/mcp`.

The trade-off: the dynamic approach is more flexible but requires more LLM reasoning to navigate than a server with explicit tool names like `get_health_score`. Works with Claude Desktop, ChatGPT, and any MCP-compatible client.

### Custify (Official)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [custifyofficial/custify-mcp](https://github.com/custifyofficial/custify-mcp) | 3 | TypeScript | MIT | 18 | Yes |

**Custify** ships the most comprehensive open-source customer success MCP server. Released March 30, 2026, it covers the full CS workflow across **six categories**:

- **Account tools** — `list_accounts`, `get_account`, `search_accounts`, `list_attributes`
- **Contact tools** — `get_contacts`, `get_contact`
- **Health & usage** — `get_health_scores`, `get_usage_data`, `get_usage_trends`
- **Alerts & segments** — `get_alerts`, `get_segment_membership`
- **Task tools** — `list_tasks`, `get_task`, `list_task_filter_values`, `list_tags`
- **Action tools** — `create_note`, `create_task`, `run_playbook`, `update_custom_fields`

The `run_playbook` tool is notable — it lets AI agents trigger automated CS playbooks directly, bridging the gap between AI analysis and automated action. Authentication via API key (`CUSTIFY_API_KEY` environment variable). MIT license. 13 commits, 3 stars. Early but functional.

### Vitally (Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [fiscaltec/vitally-mcp](https://github.com/fiscaltec/vitally-mcp) | 1 | JavaScript | MIT | 11 | No |
| [johnjjung/vitally-mcp](https://github.com/johnjjung/vitally-mcp) | 1 | JavaScript | MIT | 9 | No |
| [mattfdigio/vitally](https://github.com/mattfdigio/vitally) | — | C# (.NET 10) | — | Multiple | No |

**Vitally** has no official MCP server but now **three community implementations**. The **fiscaltec** version is most complete with **11 tools**: `search_users`, `search_accounts`, `find_account_by_name`, `refresh_accounts`, `get_account_health`, `get_account_conversations`, `get_account_tasks`, `get_account_notes`, `get_note_by_id`, `create_account_note`, and `search_tools`. It requires `VITALLY_API_KEY`, `VITALLY_API_SUBDOMAIN`, and `VITALLY_DATA_CENTER` environment variables.

The **johnjjung** version provides **9 tools** with a similar feature set but includes a **demo mode fallback** — it returns mock data when no API key is configured, useful for testing and evaluation.

The **mattfdigio** version (released March 17, 2026) takes a different technical approach — built in **C# on .NET 10** and secured with **Auth0 (OAuth 2.0)** rather than API key. Searches and retrieves Vitally data including account health scores, users, and conversations. A pre-built Claude Desktop installer with platform-specific binaries (macOS/Linux) and a Docker image are available, making setup accessible to non-developers.

None of the servers cover Vitally's newer AI Copilot features (automated account recaps, intelligent follow-ups), which remain platform-locked. Vitally's official platform has strong AI capabilities but continues to hold them back from MCP.

### ChurnZero (Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [victorsaad-trm/churnzero-mcp](https://github.com/victorsaad-trm/churnzero-mcp) | 0 | TypeScript | — | 15 | No |

**ChurnZero** has a community MCP server with **15 tools** covering:

- **Accounts** — `get_account`, `list_accounts`, `search_accounts`, `get_account_health_score`, `set_account_attribute`
- **Contacts** — `get_contact`, `list_contacts`, `upsert_contact`
- **Events** — `list_events`, `track_event`, `track_module_usage`
- **Tasks** — `list_tasks`, `create_task`
- **Segments & alerts** — `list_segments`, `list_alerts`

Authentication uses **Basic Auth** (base64-encoded email and password) plus API key. Released March 27, 2026, with 0 stars. The server enables reading and writing — `set_account_attribute`, `upsert_contact`, `track_event`, and `create_task` provide write capabilities for AI agents to update ChurnZero data.

ChurnZero itself is investing heavily in **agentic AI** — they offer 12+ AI agents for data enrichment, signal detection, and workflow assistance, plus AI Knowledge Sources that connect to Confluence and Zendesk Guide. But these are ChurnZero-native agents, not MCP-exposed capabilities. No official MCP server from ChurnZero.

### Totango / Catalyst

**No native or community MCP server found.** Totango (which merged with Catalyst in 2024) is available through **Zapier MCP**, **viaSocket MCP**, and **Pipedream MCP** — third-party aggregators that wrap Totango's API into MCP-compatible endpoints. These provide basic actions but lack the depth of dedicated MCP servers. Given Totango's position as a top-tier CS platform, this is the category's most notable gap.

### ClientSuccess, SmartKarrot, CustomerSuccessBox

**No MCP servers found** for any of these platforms. ClientSuccess (acquired by Gainsight in 2024 but still operating separately), SmartKarrot, and CustomerSuccessBox all lack MCP presence — both official and community. These platforms continue to focus on native integrations and traditional API access.

## Product Experience & Analytics

### Pendo (Official)

| Server | Stars | Language | Auth | Tools | Official |
|--------|-------|----------|------|-------|----------|
| Pendo MCP Server | — | Hosted | OAuth | 15+ | Yes (GA) |
| [AsherJN/pendo-mcp](https://github.com/AsherJN/pendo-mcp) | 0 | Python | API key | 15 | No |

**Pendo** has reached **general availability** for its official MCP server. Any paid Pendo customer can connect — an admin enables MCP for the organization. Compatible with Claude (web and desktop), Claude Code, Cursor, VS Code with GitHub Copilot, ChatGPT, Gemini CLI, and **Windsurf** (newly added).

The official server provides access to visitor and account metadata, application analytics, page/feature/track event data, event-level aggregation queries, and visitor activity patterns. **Four new tools** were added for AI Agent Analytics and the Listen ideas module:
- `list_ai_agents` — query AI agents configured in the Pendo platform
- `list_use_cases` — retrieve defined use cases for AI agents
- `list_ai_agent_issues` — surface issue signals from AI agent activity
- `get_ideas` — query Listen ideas directly for feedback and feature prioritization

The server also now supports **developer logs retrieval** — console output and network request/response details from a specific session replay, giving AI tools full browser-level debug context without leaving the AI environment.

Pendo hosted an **MCP Hackathon** and published extensive guides on MCP prompts across product, CS, and support teams — signaling strong ecosystem commitment.

The **community server** by AsherJN provides **15 tools** organized by function:
- **Product discovery** — `search_pages`, `search_features`, `search_track_events`
- **People insights** — `get_visitor_details`, `search_visitors`, `get_account_details`, `search_accounts`, `analyze_segments`
- **Behavioral analytics** — `analyze_usage`, `analyze_feature_adoption`, `analyze_retention`, `analyze_funnels`, `analyze_user_paths`, `calculate_product_engagement`
- **Feedback** — `analyze_nps_feedback`

Zero required parameters with sensible defaults. LLM-optimized output formatting. Python, 4 commits, v1.1.

## Churn Analytics

### ChurnKey

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| ChurnKey MCP (via MCPBundles) | Hosted HTTP | API key | 2 | Partial |

**ChurnKey** provides churn analytics, cancel flow data, and customer health scores through an MCP server hosted on MCPBundles at `mcp.mcpbundles.com/bundle/churnkey`. Two tools are available, focused on session aggregation and churn analytics. Includes a SKILL.md that gives AI agents domain knowledge about when and how to use the tools. API key authentication.

ChurnKey is not a full CS platform — it's specialized for churn reduction through cancel flow optimization, payment recovery, and reactivation campaigns. Pairs well with Stripe MCP for subscription-level customer success triage.

## Customer Support Bridging into CS

### Intercom (Official)

| Server | Stars | Language | Transport | Tools | Official |
|--------|-------|----------|-----------|-------|----------|
| [intercom/intercom-mcp-server](https://github.com/intercom/intercom-mcp-server) | 5 | — | Streamable HTTP (`mcp.intercom.com/mcp`) | ~12 | Yes |

**Intercom** has expanded its official MCP server from 6 to approximately **12 tools**, adding company and Help Center article capabilities beyond the original conversation and contact tools:

- **Universal** — `search` (query DSL across resource types), `fetch` (retrieve any resource by type+ID)
- **Conversations** — `search_conversations`, `get_conversation`
- **Contacts** — `search_contacts`, `get_contact`
- **Companies** — `list_companies`, `get_company`
- **Help Center articles** — `search_articles`, `get_article`, `create_article`

The Help Center article tools are notable for CS workflows — AI agents can now query and create knowledge base content directly. `create_article` lets agents draft Help Center articles from scratch, enabling workflows where support conversations automatically generate documentation.

Intercom also added **MCP connector templates** within its own Fin AI product — prebuilt configurations for Stripe, Shopify, and Linear, letting Fin take actions in external tools via MCP. Intercom is both an MCP server *and* an MCP client.

Authentication via **OAuth** (recommended) or Bearer token. Streamable HTTP transport (recommended) with legacy SSE at `mcp.intercom.com/sse` (deprecated). Currently US-hosted Intercom workspaces only.

Intercom isn't a dedicated CS platform, but its conversation data, contact intelligence, and help center content are critical inputs for customer success workflows. The expanded tool set makes it more useful in multi-platform CS stacks.

## What's Missing

- **Totango / Catalyst** — no native MCP server despite being a market leader (only third-party Zapier/viaSocket/Pipedream wrappers)
- **ClientSuccess** — no MCP server (now Gainsight-owned but operating independently)
- **SmartKarrot** — no MCP server
- **CustomerSuccessBox** — no MCP server
- **Freshsuccess** (Freshdesk Customer Success) — no MCP server (Freshdesk helpdesk has community servers, but the CS module does not)
- **Akita** — no MCP server
- **WalkMe** — no MCP server (digital adoption platform relevant to CS onboarding workflows)
- **UserGuiding** — no MCP server
- **Cross-platform CS workflows** — no unified MCP server spans multiple CS platforms (unlike ITSM's MCP-ITSM multi-platform tool)
- **Health score standardization** — every server exposes health scores differently; no common schema
- **Renewal management** — no server focuses specifically on renewal pipeline, forecasting, or CPQ integration
- **Customer onboarding** — no MCP server covers structured onboarding workflows, milestone tracking, or time-to-value metrics
- **QBR automation** — mentioned in Gainsight marketing but not broken out as discrete MCP tools

## Industry Trends

The customer success MCP landscape reveals three tiers:

1. **Official hosted MCP** (Gainsight, Planhat, Pendo) — vendor-managed endpoints with OAuth, zero local install, enterprise permissioning. This is where the market is heading.
2. **Official open-source** (Custify) — traditional GitHub-hosted servers with API key auth. Lower barrier for developers but more setup required.
3. **Community-only** (Vitally, ChurnZero) — third-party implementations with low adoption (0-1 stars). Functional but unsupported and potentially fragile.

**Gainsight is making the biggest MCP bet in enterprise software.** Their April announcement framed MCP as enabling "agentic customer success." Their May 28 Agentic Stack announcement went further — not just tools but an **Agent Studio** for building retention workflows in plain language, pre-built agents baked with CS domain expertise, and a **CLI** for technical admins. Four official MCP servers covering the entire CS lifecycle (customer data, learning, community, product experience) makes Gainsight the first CS platform with platform-wide agentic coverage.

**Pendo reaching GA validates the market.** Moving from preview to GA signals enterprise readiness. The new AI Agent Analytics tools (`list_ai_agents`, `list_use_cases`) suggest Pendo is positioning its MCP server not just as a data query layer but as a way to observe and manage AI agents running on top of their platform — a meta-level use case.

**Intercom is both server and client.** Intercom doubled its tool count and simultaneously integrated MCP *into* its own Fin AI product (connecting to Stripe, Shopify, Linear). This dual role — exposing customer data via MCP while letting its own AI use MCP to reach external tools — is a preview of how MCP will change enterprise software architecture.

**Product analytics + CS is converging.** Pendo's MCP server isn't just for product teams — their published use cases target CS workflows like health score enrichment, churn signal detection, and onboarding progress tracking. Gainsight PX joining the MCP ecosystem deepens this convergence.

**The Totango gap is conspicuous.** As one of the largest CS platforms (especially after merging with Catalyst), Totango's absence from MCP is the category's biggest miss. Only third-party aggregators (Zapier, viaSocket, Pipedream) provide any MCP access.

## Rating: 4.0 / 5

Customer success MCP servers have matured substantially since the category's early 2026 launch. **Gainsight now ships four official MCP servers** across the customer lifecycle (CS, Skilljar, Communities, PX) plus an Agent Studio and CLI. **Pendo is generally available** with new AI Agent Analytics tools. **Intercom doubled its tool count** to ~12. Custify provides the best open-source option with 18 tools. Vitally now has three community implementations. The persistent gaps — Totango/Catalyst still absent, no cross-platform unified server, renewal management and onboarding still underserved — are real but outweighed by how rapidly the tier-1 vendors are investing. Gainsight's Agentic Stack, in particular, has set a new standard for what "MCP support" looks like in enterprise software.

