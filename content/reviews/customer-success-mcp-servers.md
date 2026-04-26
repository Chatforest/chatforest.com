---
title: "Customer Success MCP Servers — Gainsight, Planhat, Vitally, Pendo, ChurnZero, and More"
date: 2026-04-26T18:00:00+09:00
description: "Customer success MCP servers reviewed: Gainsight official MCP (Staircase AI + CS, hosted at mcp.staircase.ai, health scores + CTAs + success plans), Planhat official (api.planhat.com, OAuth 2.0, dynamic CRUD), Pendo official (OAuth, product analytics for CS teams), Custify official (18 tools, health scores + playbooks + tasks, MIT), Vitally community (11 tools, health scores + conversations + tasks), ChurnZero community (15 tools, health + events + segments), Intercom official remote (6 tools, Streamable HTTP), ChurnKey (2 tools, cancel flow analytics). Rating: 3.5/5."
og_description: "Customer success MCP servers: Gainsight (official hosted, CS + Staircase AI), Planhat (official, dynamic CRUD), Pendo (official, OAuth), Custify (18 tools, MIT), Vitally (community, 11 tools), ChurnZero (community, 15 tools). Rating: 3.5/5."
content_type: "Review"
card_description: "Customer success MCP servers let AI agents query health scores, manage customer accounts, track churn signals, run playbooks, and coordinate renewal workflows across Gainsight, Planhat, Vitally, Pendo, ChurnZero, and Custify. The category is emerging fast — Gainsight and Planhat both launched official MCP servers in early 2026, Pendo connects product analytics to CS workflows via OAuth, and Custify ships an 18-tool open-source server covering health scores, tasks, and playbook automation. Community servers exist for Vitally (11 tools) and ChurnZero (15 tools). Intercom bridges customer support into CS workflows with an official remote MCP at mcp.intercom.com. The biggest gap: Totango (merged with Catalyst) has no native or community MCP server despite being a top-tier CS platform. Similarly absent are ClientSuccess, SmartKarrot, CustomerSuccessBox, and Freshsuccess. Gainsight PX is available through Pipedream but not as a standalone open-source server. The pattern emerging is that larger vendors (Gainsight, Planhat, Pendo) are building official hosted MCP endpoints with OAuth, while smaller platforms rely on community implementations or third-party MCP aggregators like Zapier and viaSocket. Rating: 3.5/5 — strong vendor commitment from market leaders but significant gaps in the mid-market and no open-source CS platform representation."
last_refreshed: 2026-04-26
---

Customer success is the newest enterprise category to get serious MCP coverage. **Gainsight**, **Planhat**, and **Pendo** all launched official MCP servers in early 2026, letting AI agents query health scores, access renewal timelines, and take action on customer accounts. **Custify** ships an open-source 18-tool server. Community implementations exist for **Vitally** and **ChurnZero**. The category is moving fast — Gainsight's April 2026 announcement explicitly framed MCP as the foundation of "agentic customer success." Part of our **[Business & Productivity](/categories/business-productivity/)** category.

This review covers **dedicated customer success platforms** (Gainsight, Totango, ChurnZero, Vitally, Custify, Planhat, ClientSuccess), **product experience platforms** relevant to CS workflows (Pendo, Gainsight PX), **churn analytics** (ChurnKey), and **customer support platforms** that bridge into CS (Intercom). For CRM platforms, see our [CRM MCP Servers](/reviews/crm-mcp-servers/) review. For helpdesk/ticketing, see [Customer Support & Helpdesk MCP Servers](/reviews/customer-support-helpdesk-mcp-servers/).

The headline finding: **Gainsight leads with the deepest integration** — unified MCP access to both Staircase AI (customer intelligence) and Gainsight CS (system of record and action). **Planhat differentiates with dynamic CRUD** — its MCP server auto-discovers data models rather than hardcoding tools. **Custify has the best open-source server** with 18 tools covering the full CS workflow from health scores to playbook automation. **The mid-market is wide open** — Totango/Catalyst, ClientSuccess, SmartKarrot, and CustomerSuccessBox have no MCP servers at all.

## Dedicated Customer Success Platforms

### Gainsight (Official)

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| Gainsight CS + Staircase AI MCP | Hosted HTTP (`mcp.staircase.ai/mcp`) | OAuth (Google/Microsoft SSO) | Multiple | Yes |
| Gainsight PX (via Pipedream) | Hosted HTTP | API key | 3+ | Partial |

**Gainsight** announced MCP support across Gainsight CS and Staircase AI on April 2, 2026, with GA availability to all customers on April 25, 2026. The MCP server at `mcp.staircase.ai/mcp` provides **unified access to both platforms in a single connection** — Staircase AI for customer intelligence (sentiment, relationship maps, communication analysis) and Gainsight CS for the system of record (health scores, product usage, renewal/contract data) and system of action (CTAs, success plans, journey programs).

Key capabilities:
- **Query customer data in natural language** — health scores, renewal timelines, sentiment trends, relationship maps
- **Take action directly in Gainsight CS** — update records, manage CTAs, log activities, build success plans
- **Build custom workflows without engineering** — renewal playbooks, risk escalation sequences, QBR preparation
- **Meeting prep in 60 seconds** — health snapshot with recommended talking points
- **Portfolio triage** — "what needs attention?" returns prioritized risk and opportunity signals
- **Account handoff briefs** — comprehensive handoff documentation in minutes

Authentication uses **federated SSO** (sign in with the same Google or Microsoft email that has Staircase AI access). Role-based access controls carry over — customer data retains the same permissions when accessed through external AI tools. Works with Claude (via Connectors Directory), ChatGPT, and Gemini.

**Gainsight PX** (product experience analytics) is available as an MCP server through **Pipedream** at `mcp.pipedream.com/app/gainsight_px`. Tools include account management, user management, and feature monitoring. API key authentication. This is a Pipedream-hosted integration rather than a Gainsight-native MCP server — useful for product usage data but separate from the CS/Staircase AI integration.

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

**Vitally** has no official MCP server but two community implementations. The **fiscaltec** version is more complete with **11 tools**: `search_users`, `search_accounts`, `find_account_by_name`, `refresh_accounts`, `get_account_health`, `get_account_conversations`, `get_account_tasks`, `get_account_notes`, `get_note_by_id`, `create_account_note`, and `search_tools`. It requires `VITALLY_API_KEY`, `VITALLY_API_SUBDOMAIN`, and `VITALLY_DATA_CENTER` environment variables.

The **johnjjung** version provides **9 tools** with a similar feature set but includes a **demo mode fallback** — it returns mock data when no API key is configured, useful for testing and evaluation. 3 commits, last updated April 2025.

Neither server covers Vitally's newer AI Copilot features (automated account recaps, intelligent follow-ups). Both are MIT licensed. Vitally's official platform has strong AI capabilities (embedded AI Copilot, automated insights), but these are platform-locked and not exposed via MCP.

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

**No native or community MCP server found.** Totango (which merged with Catalyst in 2024) is available through **Zapier MCP** and **viaSocket MCP** — third-party aggregators that wrap Totango's API into MCP-compatible endpoints. These provide basic actions but lack the depth of dedicated MCP servers. Given Totango's position as a top-tier CS platform, this is the category's most notable gap.

### ClientSuccess, SmartKarrot, CustomerSuccessBox

**No MCP servers found** for any of these platforms. ClientSuccess (acquired by Gainsight in 2024 but still operating separately), SmartKarrot, and CustomerSuccessBox all lack MCP presence — both official and community. These platforms continue to focus on native integrations and traditional API access.

## Product Experience & Analytics

### Pendo (Official)

| Server | Stars | Language | Auth | Tools | Official |
|--------|-------|----------|------|-------|----------|
| Pendo MCP Server | — | Hosted | OAuth | Multiple | Yes |
| [AsherJN/pendo-mcp](https://github.com/AsherJN/pendo-mcp) | 0 | Python | API key | 15 | No |

**Pendo** has an **official MCP server** available through Claude's Connectors Directory, using **OAuth authentication** that respects existing Pendo permissions. Any paid Pendo customer can access it — an admin enables MCP for the organization. Compatible with Claude (web and desktop), Claude Code, Cursor, VS Code with GitHub Copilot, and ChatGPT.

The official server provides access to visitor and account metadata, application analytics, page/feature/track event data, event-level aggregation queries, and visitor activity patterns. Pendo hosted an **MCP Hackathon** and published extensive guides on using MCP prompts across product, CS, and support teams — signaling strong commitment to the MCP ecosystem.

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
| [intercom/intercom-mcp-server](https://github.com/intercom/intercom-mcp-server) | 5 | — | Streamable HTTP (`mcp.intercom.com/mcp`) | 6 | Yes |

**Intercom** provides an **official remote MCP server** at `mcp.intercom.com/mcp` with **6 tools**: `search`, `fetch`, `search_conversations`, `get_conversation`, `search_contacts`, and `get_contact`. Two universal tools (`search` and `fetch`) work across multiple resource types, plus four direct tools for conversations and contacts.

Authentication via **OAuth** (recommended) or Bearer token. Streamable HTTP transport (recommended) with legacy SSE at `mcp.intercom.com/sse` (deprecated). Currently US-hosted Intercom workspaces only.

Intercom isn't a dedicated CS platform, but its conversation data, contact intelligence, and help center content are critical inputs for customer success workflows. Teams using Intercom for customer communication alongside a dedicated CS platform can bridge the two through MCP.

## What's Missing

- **Totango / Catalyst** — no native MCP server despite being a market leader (only third-party Zapier/viaSocket wrappers)
- **ClientSuccess** — no MCP server (now Gainsight-owned but operating independently)
- **SmartKarrot** — no MCP server
- **CustomerSuccessBox** — no MCP server
- **Freshsuccess** (Freshdesk Customer Success) — no MCP server (Freshdesk helpdesk has community servers, but the CS module does not)
- **Akita** — no MCP server
- **WalkMe** — no MCP server (digital adoption platform relevant to CS onboarding workflows)
- **UserGuiding** — no MCP server
- **Gainsight PX standalone** — only available through Pipedream, not as a native open-source server
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

**Gainsight's framing matters.** Their April 2026 press release explicitly positioned MCP as enabling "agentic customer success" — AI agents that autonomously run retention workflows. This frames MCP not as a developer tool but as a **strategic platform capability**. Expect other CS vendors to follow.

**Product analytics + CS is converging.** Pendo's MCP server isn't just for product teams — their published use cases target CS workflows like health score enrichment, churn signal detection, and onboarding progress tracking. The line between product analytics and customer success is blurring through MCP.

**The Totango gap is conspicuous.** As one of the largest CS platforms (especially after merging with Catalyst), Totango's absence from MCP is the category's biggest miss. Only third-party aggregators (Zapier, viaSocket) provide any MCP access.

## Rating: 3.5 / 5

Customer success MCP servers are in **early but promising** shape. Three major vendors (Gainsight, Planhat, Pendo) have official servers with enterprise-grade auth and hosted endpoints. Custify provides the best open-source option with 18 tools. But the mid-market is unrepresented (Totango, ClientSuccess, SmartKarrot all absent), community servers have minimal adoption, and critical CS workflows like onboarding, renewal management, and QBR automation lack MCP coverage. The category should improve quickly — Gainsight's "agentic customer success" framing is likely to push competitors to ship MCP servers in 2026.
