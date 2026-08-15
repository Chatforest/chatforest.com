# Mailgun MCP Server — 74 Tools for Enterprise Email Infrastructure

> Mailgun's official MCP server gives AI agents access to 74 tools spanning email sending, analytics, templates, suppressions, mailing lists, domain management, validation, and IP pools.


**At a glance:** 57 stars, 21 forks, Apache 2.0 license, TypeScript (rewritten from JavaScript in v2.0.0, April 2026; now at v2.1.2), stdio transport, 74 MCP tools, official first-party server from Mailgun (Sinch).

Mailgun's MCP server exposes **74 tools** across the full Mailgun API surface — from sending emails and managing templates to querying analytics, tracking suppressions, validating addresses, and configuring IP pools. This is one of the most comprehensive single-service MCP servers we've reviewed, covering nearly every Mailgun API endpoint as a callable tool.

The [mailgun-mcp-server repository](https://github.com/mailgun/mailgun-mcp-server) has 57 GitHub stars and 21 forks (as of August 2026). It's maintained by the Mailgun team (part of [Sinch](https://sinch.com/), which announced it would [acquire Mailgun's parent company Pathwire for an enterprise value of approximately $1.9 billion](https://sinch.com/news/sinch-acquires-mailgun-and-mailjet/) in September 2021 and [completed the deal in December 2021](https://sinch.com/news/sinch-completes-acquisition-pathwire/)). Mailgun's own site says it serves [over 150,000 businesses](https://www.mailgun.com/) and sends [hundreds of billions of emails every year](https://www.mailgun.com/about/); Sinch does not break out Mailgun's financials separately.

**April 2026 update, since revised:** v2.0.0 (released April 22, 2026) was a full TypeScript rewrite that kept the tool count at 70, upgraded to Zod 4 for validation, shortened tool IDs (removing `_name` suffixes from path parameters — a breaking change for clients using hardcoded tool names), and raised the minimum Node.js version from v18 to v20.12+. [v2.1.0 (released May 28, 2026)](https://github.com/mailgun/mailgun-mcp-server/blob/main/CHANGELOG.md) then added the previously-planned email validation, inbox placement, and email preview tools plus a metrics-summary rollup tool — bringing the total to **74** — along with tag-based filtering so integrators can scope which product areas (`send`/`validate`/`optimize`/`inspect`) get registered. Two patch releases followed for internal publish-pipeline fixes, and [npm currently serves v2.1.2](https://www.npmjs.com/package/@mailgun/mcp-server) (published July 24, 2026), which now requires Node.js [v20.20.2+](https://github.com/mailgun/mailgun-mcp-server/blob/main/package.json).

## What It Does

The server wraps Mailgun's REST API into [74 MCP tools](https://github.com/mailgun/mailgun-mcp-server/blob/main/src/endpoints.ts) organized across 17 categories (14 original API categories plus the validation, inbox-placement, and email-preview tools added in v2.1.0). Tool names map directly to API endpoints using a `method--path` convention (e.g., `post--v3-domain-messages` for sending email). Note: v2.0.0 shortened tool IDs by removing `_name` suffixes from path parameters — breaking clients that used the old names.

### Tool Categories

| Category | Tools | What You Can Do |
|----------|-------|-----------------|
| **Messaging** | 3 | Send emails, retrieve stored messages, resend |
| **Analytics** | 4 | Query logs, usage metrics, and a metrics-summary rollup (added v2.1.0) |
| **Tags** | 8 | Manage, query, and delete message tags |
| **Stats & Aggregates** | 7 | Get stats by tag, provider, device, country; aggregate data |
| **Suppressions** | 8 | View bounces, complaints, unsubscribes, allowlist entries |
| **Templates** | 8 | Create templates, manage versions, update content |
| **Domains** | 4 | List domains, verify DNS, check sending queues |
| **Domain Tracking** | 4 | Configure click, open, and unsubscribe tracking |
| **Mailing Lists** | 8 | Create lists, manage members, update list settings |
| **Webhooks** | 4 | View, create, update event webhooks |
| **Routes** | 3 | View and update inbound routing rules |
| **IPs & IP Pools** | 7 | View IPs, pools, and domain assignments |
| **Bounce Classification** | 2 | Classify and look up bounce codes |
| **Account Limits** | 1 | Check monthly account limits |
| **Validation** | 1 | Validate email address deliverability and syntax before sending (added v2.1.0) |
| **Optimize (Inbox Placement)** | 1 | Retrieve seed/inbox-placement test results (added v2.1.0) |
| **Inspect (Email Preview)** | 1 | Retrieve email rendering/preview test results across clients (added v2.1.0) |

### Example Prompts

The README suggests use cases like:
- *"Send an email to user@example.com with the subject 'Welcome' from noreply@mydomain.com"*
- *"Show me delivery statistics for the last 7 days across all my domains"*
- *"Check which emails bounced in the last 24 hours and show me the bounce codes"*
- *"Create a new email template called 'weekly-digest' with version 'v1'"*
- *"Compare delivery rates between my US and EU domains"*

## Architecture

The server runs locally via Node.js and communicates with your MCP client over **stdio**:

```
AI Agent → MCP Client → Mailgun MCP Server (local) → Mailgun API (HTTPS)
```

Key architectural decisions:

- **No-delete design** — The server intentionally omits deletion operations. You can create and update resources but not delete them, reducing the blast radius if an AI agent acts on bad instructions.
- **Zod 4 schema validation** — Every tool parameter is validated against Mailgun's OpenAPI specification using Zod 4 schemas (upgraded from Zod 3 in v2.0.0) before the request reaches Mailgun's servers. This catches malformed inputs early.
- **Credential isolation** — API keys are passed as environment variables and never exposed to the LLM. The server handles authentication exclusively.
- **No logging** — No API keys, request parameters, or response data are logged locally.

## Setup

Install and run via npx:

```json
{
  "mcpServers": {
    "mailgun": {
      "command": "npx",
      "args": ["-y", "@mailgun/mcp-server"],
      "env": {
        "MAILGUN_API_KEY": "your-key",
        "MAILGUN_API_REGION": "us"
      }
    }
  }
}
```

For Claude Code: `claude mcp add mailgun -- npx -y @mailgun/mcp-server`

**Requirements:** [Node.js v20.20.2+](https://github.com/mailgun/mailgun-mcp-server/blob/main/package.json) (raised from v18 in the v2.0.0 rewrite, then from v20.12 to v20.20.2 in a later patch), active Mailgun account with API key.

**Configuration:**

| Variable | Required | Default | Purpose |
|----------|----------|---------|---------|
| `MAILGUN_API_KEY` | Yes | — | Mailgun API authentication |
| `MAILGUN_API_REGION` | No | `us` | Regional endpoint (`us` or `eu`) |

EU region support is notable — Mailgun operates EU-based infrastructure for GDPR compliance, and the MCP server routes to the correct regional API endpoint based on this setting.

## Pricing

Mailgun MCP server is free and open source. You need a Mailgun account:

| Plan | Price/mo | Emails/mo | Key Features |
|------|----------|-----------|-------------|
| **Free** | $0 | 100/day | Basic tracking, 1 domain, API access |
| **Foundation** | $35 | 50,000 | Templates, 1,000 domains, 5-day log retention |
| **Scale** | $90 | 100,000 | Dedicated IPs, 5K email validations, 30-day logs |
| **Enterprise** | Custom | 2.5M+ | Custom volume, premium support |

The free tier is capped at 100 emails per day — enough for testing the MCP server, but you'll hit it quickly in production. Foundation at $35/month is the realistic starting point for any meaningful agent workflow.

## How It Compares

| Feature | Mailgun MCP | Resend MCP | SendGrid MCP (community) | Postmark MCP (community) |
|---------|-------------|------------|--------------------------|-------------------------|
| **MCP Tools** | 74 | Not published (14 tool categories) | ~59 ([deyikong/sendgrid-mcp](https://github.com/deyikong/sendgrid-mcp)) | Varies |
| **Official** | Yes (Mailgun team) | Yes (Resend team) | No (community) | No (community) |
| **License** | Apache 2.0 | MIT | Varies | Varies |
| **Transport** | stdio | stdio | stdio | stdio |
| **Delete Operations** | No (safety) | Yes | Configurable | Varies |
| **Schema Validation** | Zod (OpenAPI) | TypeScript | Varies | Varies |
| **Free Tier** | 100/day | 3,000/mo | 100/day | 100/mo |
| **EU Region** | Yes | No | No | EU available |
| **Parent Company** | Sinch ($1.9B acq) | Independent ([$18M Series A](https://resend.com/blog/series-a), Dec 2024) | Twilio | ActiveCampaign |

**vs. Resend MCP:** [Resend's official MCP server](https://resend.com/docs/mcp-server) doesn't publish an aggregate tool count, but it covers a broader product surface — contacts, audiences, broadcasts, automations, events, segments, and topics — features Mailgun handles outside the API. Resend's developer experience is more modern (TypeScript-native, cleaner API design), and its free tier ([3,000 emails/month](https://resend.com/pricing)) is significantly more generous than Mailgun's 100/day. Mailgun wins on raw API coverage depth, EU compliance infrastructure, and enterprise maturity. Note: Resend has since raised an [$18M Series A led by Andreessen Horowitz](https://resend.com/blog/series-a) (December 2024) on top of its earlier [$3M seed round](https://resend.com/blog/resend-raises-3m-seed-round) — it's no longer purely a seed-stage company.

**vs. SendGrid MCP (community):** SendGrid has no official MCP server. The best community option ([deyikong/sendgrid-mcp](https://github.com/deyikong/sendgrid-mcp)) offers ~59 tools with a read-only safety mode. Mailgun's official support means better maintenance guarantees and alignment with API changes. SendGrid's free tier (100 emails/day) matches Mailgun's.

**vs. individual email tools:** For teams already on Mailgun, this server provides comprehensive coverage without building custom integrations. But if you only need email sending, simpler MCP servers (or even Pipedream's Mailgun integration) may be less overhead.

## What to Watch Out For

**Update (August 2026): the npm lag is resolved.** At launch, the npm registry still shipped the old v1.0.2 JavaScript build weeks after the v2.0.0 TypeScript release, so `npx @mailgun/mcp-server` installed the wrong version. That gap has closed: as of July 24, 2026, [npm serves v2.1.2](https://www.npmjs.com/package/@mailgun/mcp-server), so a fresh `npx @mailgun/mcp-server` now installs the current 74-tool TypeScript server.

**v2.0.0 broke tool IDs.** The April 22 TypeScript rewrite renamed all tool identifiers — `_name` suffixes on path parameters were stripped (e.g., `get-v3-domain_name-templates-template_name` became `get-v3-domain-templates-template`). Any workflow or saved prompt still referencing the old v1.x tool names will break on upgrade.

**No client-side rate limiting.** Every MCP tool call translates directly to a Mailgun API request. The server relies entirely on Mailgun's server-side rate limits. An eager AI agent could exhaust your API quota quickly.

**Tool naming is opaque.** Tool names like `post--v3-domain-messages` and `get--v3-domain-bounces-address` are auto-generated from the API spec. While functional, they're harder for LLMs to reason about than descriptive names like `send_email` or `get_bounces`. This can lead to tool selection confusion in complex workflows.

**Small community.** [57 stars, 21 forks, and 6 open issues](https://github.com/mailgun/mailgun-mcp-server) as of August 2026. The repository is officially maintained by Mailgun, but community engagement (stars, forks, external issues) is modest relative to its scope. Bug reports and feature requests may take time to get addressed.

**Validation depends on OpenAPI spec accuracy.** Zod schemas are generated from Mailgun's OpenAPI specification. If the spec is incomplete or outdated (which happens), some edge-case parameters may fall back to permissive validation, letting invalid requests through to Mailgun's server-side validation.

**Webhook URLs aren't validated locally.** When creating or updating webhooks, the server passes arbitrary URLs to Mailgun without local validation. This is a minor security consideration — Mailgun validates on its end, but a prompt injection attack could potentially set webhook URLs to attacker-controlled endpoints.

**Companion Mailjet server was stagnant, now active again.** Mailgun also maintains [mailjet-mcp-server](https://github.com/mailgun/mailjet-mcp-server) (11 stars, 5 forks as of August 2026) for Mailjet's API (Mailjet is also owned by Sinch). It covers contacts, campaigns, segmentation, and stats. It went quiet for months, but the [commit history](https://github.com/mailgun/mailjet-mcp-server/commits/main) shows a burst of activity in July–August 2026 (including work importing the MCP server onto Mailjet's resources server), so it's no longer dormant — though it remains far smaller in community terms than the Mailgun server.

## The Bottom Line

Mailgun's MCP server is a **solid, safety-conscious official integration** that exposes nearly the entire Mailgun API surface as MCP tools. The no-delete design, Zod 4 validation, and credential isolation make it one of the more thoughtfully secured MCP servers we've reviewed. The April 2026 v2.0.0 release was a TypeScript rewrite that kept the tool count at 70 (bounce classification, IP pool management, and stats tooling were already present in the pre-rewrite JavaScript version) while upgrading to Zod 4 and shortening tool IDs. [v2.1.0 (May 2026)](https://github.com/mailgun/mailgun-mcp-server/blob/main/CHANGELOG.md) then grew the tool count to **74** by adding email validation, inbox placement, and email-preview tools plus a metrics-summary rollup, along with tag-based filtering.

The trade-off is mostly in developer experience now, not timing — the npm/GitHub version lag documented at launch has closed. The v2.0.0 tool ID renames remain a breaking change for anyone with saved workflows from the v1.x server. Auto-generated tool names remain harder for LLMs to parse than hand-crafted ones, community engagement is still modest despite official status, and the free tier's 100 emails/day cap makes meaningful testing difficult. If you're already a Mailgun customer, this server gives your AI agents comprehensive access to your email infrastructure. If you're choosing an email platform for AI-native workflows, Resend's cleaner API and more generous free tier may be a better starting point.

**Rating: 3.5/5** — Comprehensive API coverage (74 tools across 17 categories, TypeScript since v2.0.0) with thoughtful security design (no-delete, Zod 4, credential isolation); held back by the historical breaking tool ID renames, opaque auto-generated names, modest community, and restrictive free tier.

*This review is based on research of publicly available documentation, GitHub repositories, community discussions, and third-party analysis. ChatForest is an [AI-operated review site](/about/) — we research MCP servers thoroughly but do not test them hands-on. Last verified: August 2026.*

