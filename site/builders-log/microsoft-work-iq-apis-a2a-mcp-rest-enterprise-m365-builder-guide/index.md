# Microsoft Work IQ APIs: 10 Tools Replace 1,000 Pipelines — GA June 16, 2026

> Work IQ gives agents semantic access to Microsoft 365 data via A2A, MCP, and REST. GA June 16. Here is the complete builder reference: 10 generic tools, 12 MCP servers, auth model, pricing, and known limits.


Microsoft [announced Work IQ APIs on June 2, 2026](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/) at Build 2026. They go generally available on **June 16, 2026** — eleven days from now, per [Microsoft's GA licensing notice](https://www.microsoft.com/en-us/licensing/news/work-iq-general-availability).

The pitch: agents that need enterprise data (email, calendar, Teams threads, files, SharePoint, meetings, people context) have historically required custom ETL pipelines, index sync jobs, custom compliance layers, and per-resource tool sets. Work IQ replaces all of that with ten generic tools and a permission-trimmed secure layer backed by Microsoft Graph v1.0, per [Microsoft's Work IQ API overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/api-overview).

This guide covers what Work IQ is, the 10 tools in detail, the three integration protocols, auth, pricing, and what to watch out for.

---

## The Core Problem Work IQ Solves

When you build an agent that needs to reason about enterprise context, you typically build:

- A data pipeline to extract email/calendar/Teams content
- An embedding + vector store to make it searchable
- A compliance layer to trim results to the requesting user's permissions
- A set of per-resource tools (one for mail, one for calendar, one for Teams...)
- A sync job to keep the index fresh

Work IQ eliminates all of that. It routes every request through Microsoft's Graph API layer, applies the user's actual M365 permissions on every call, and exposes the results through a unified 10-tool interface. Agents never read data the user can't access. No custom vector stores, no sync jobs. ([Work IQ API overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/api-overview))

The architectural principle: **fewer tools, more paths**. The 10 tools work on resource paths (like `/me/messages` or `/me/events/{id}`). Adding support for a new data type means adding a new path — the tool surface stays fixed. ([Work IQ MCP overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/mcp/overview))

---

## Three Integration Protocols

Work IQ supports three ways to connect as of GA ([Work IQ API overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/api-overview); [A2A quickstart](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/a2a/quickstart)):

| Protocol | Base URL | Best For |
|---|---|---|
| A2A (Agent-to-Agent) | `https://workiq.svc.cloud.microsoft/a2a/` | Multi-agent orchestration; structured task delegation |
| Remote MCP | `https://agent365.svc.cloud.microsoft/agents/tenants/{tenantId}/servers/mcp_MailTools` | IDEs, CLIs, coding assistants (Claude Code, GitHub Copilot) |
| REST | Unified endpoint (GA June 16) | Web apps, service-hosted agents, orchestrators |

A local MCP mode is also available via `workiq mcp` (stdio) for local dev environments. ([Work IQ MCP overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/mcp/overview))

### A2A Protocol Details

Uses JSON-RPC 2.0. Supports A2A v1.0 and v0.3. Version is selected via the `A2A-Version` request header; v0.3 is default if the header is omitted. ([A2A quickstart](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/a2a/quickstart))

- v1.0 method name: `SendMessage`
- Multi-turn conversations tracked via `contextId`
- A [.NET A2A SDK](https://github.com/a2aproject/a2a-dotnet) is available; a raw-HTTP sample is also provided for porting to other languages

Auth scope: `api://workiq.svc.cloud.microsoft/WorkIQAgent.Ask` ([A2A quickstart](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/a2a/quickstart))

Quick C# example:
```csharp
var credential = new InteractiveBrowserCredential(clientId);
var token = await credential.GetTokenAsync(
    new (["api://workiq.svc.cloud.microsoft/WorkIQAgent.Ask"]));
var client = new A2AClient(
    new Uri("https://workiq.svc.cloud.microsoft/a2a/"), httpClient);
```

### Remote MCP Details

Each server has its own URL path segment. The mail server, for example:
```
https://agent365.svc.cloud.microsoft/agents/tenants/{tenantId}/servers/mcp_MailTools
```

MCP clients auto-discover authentication config via `/.well-known/oauth-protected-resource`. ([Work IQ MCP overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/mcp/overview))

To connect Claude Code or another MCP client, add to `.mcp.json` (per [Microsoft's Agent 365 tooling guide](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview), which documents this exact configuration for Claude Code, GitHub Copilot CLI, and VS Code):
```json
{
  "mcpServers": {
    "WorkIQ-MailServer": {
      "type": "http",
      "url": "https://agent365.svc.cloud.microsoft/agents/tenants/{tenantId}/servers/mcp_MailTools",
      "oauth": {
        "clientId": "{clientId}",
        "callbackPort": 8080
      }
    }
  }
}
```

---

## The 10 Generic Tools — Complete Reference

Tool names, parameters, defaults, and caps below are drawn from Microsoft's [Work IQ MCP tool reference](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/mcp/tool-reference) and [Work IQ MCP overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/mcp/overview).

### Entity Tools (6)

**`fetch`**
Reads one or more entities by resource path. Supports fetching multiple paths in parallel.
- Parameter: `entityUrls` (string array) — relative resource paths, e.g., `/me/messages`, `/me/events/{event-id}`
- Default `$top` of 25; max 100. Teams chat messages hard-capped at 10 per request.
- `$skip` and `$skiptoken` are blocked (no cursor pagination).

**`create_entity`**
Creates a new entity in a collection.
- Parameters: `parentUrl` (string) — e.g., `/me/events`, `/me/messages`; `jsonBody` (string) — JSON matching the resource schema.

**`update_entity`**
Updates an existing entity via PATCH.
- Parameters: `entityUrl` (string) — e.g., `/me/messages/{message-id}`; `jsonBody` (string).

**`delete_entity`**
Deletes an entity.
- Parameter: `entityUrl` (string) — e.g., `/me/messages/{id}`
- Returns: `statusCode: 204` on success.

**`do_action`**
Executes a side-effect action: send mail, copy, move, reply.
- Parameter: `actionUrl` (string) — e.g., `/me/messages/{message-id}/send`; optional `jsonBody`.

**`call_function`**
Calls a Microsoft Graph function to compute derived data: schedules, deltas, search results.
- Parameter: `functionUrl` (string) — e.g., `/me/calendarview?startdatetime=...&enddatetime=...`

### Copilot Tools (2)

**`ask`**
Asks Microsoft 365 Copilot (or a specific agent) a natural-language question about the user's data.
- Parameters: `question` (string); optional `agentId`, `fileUrls` (OneDrive/SharePoint URLs for context), `conversationId` (multi-turn), `timeZone` (IANA identifier).
- Response includes `response` (text) and `conversationId` for continuing the thread.

**`list_agents`**
Lists available agents that can be used with `ask`.
- No parameters.
- Returns: array of `{agentId, name, provider}`.

### Schema Tools (2)

**`get_schema`**
Retrieves the OpenAPI schema for a specific operation at runtime. Agents discover data structure dynamically without predefined models loaded into context.
- Parameters: `operationIds` OR `path` (not both); `operationType` (required: `fetch`, `create`, or `update`); optional `format` (`jsonschema` or `typescript`).
- Currently covers Microsoft Graph v1.0 only (not beta).

**`search_paths`**
Searches available API paths by prefix or regex. Use this to discover which resource paths are available before calling other tools.
- Parameter: `filter` (string) — prefix or regex, e.g., `messages` or `.*calendar.*`
- Response: array of `{path, operations[]}` objects.
- Currently covers Microsoft Graph v1.0 only.

### Common Path Patterns

```
fetch /me/messages                      → read emails
do_action /me/sendMail                  → send email
create_entity /me/events               → create calendar event
fetch /me/chats/{id}/messages           → read Teams chat messages
call_function /search/query             → semantic search across M365
ask "What deals closed this quarter?"  → invoke Copilot with natural language
```

Allowed resource path prefixes by default: `/me/`, `/users/`, `/sites/`
Blocked path segments: `/authentication/`, `/servicePrincipals/`

---

## Data Sources Exposed

Via the tool + path model (backed by Microsoft Graph v1.0), per the [Work IQ API overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/api-overview) and the [Work IQ permissions list](https://github.com/microsoft/work-iq/blob/main/ADMIN-INSTRUCTIONS.md):
- Email (Outlook/Exchange)
- Calendar events and meetings
- Files (OneDrive and SharePoint)
- Microsoft Teams chats and channel messages
- People and organizational context (manager, direct reports, profiles, user search)
- Microsoft Search (semantic search across all of the above)
- Meeting transcripts (`OnlineMeetingTranscript.Read.All`)
- External items via Copilot connectors (`ExternalItem.Read.All`)
- Dynamics 365 / Dataverse business data (via [separate MCP servers](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview))

---

## The MCP Server Catalog (Agent 365)

Work IQ ships as a set of managed MCP servers. Admins enable or block servers from the M365 admin center under "Agents and Tools." (Catalog and admin controls per [Microsoft's Agent 365 tooling servers overview](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview).)

| Server | Capabilities |
|---|---|
| Work IQ Copilot | Chat with M365 Copilot; multi-turn threads; grounding with files |
| Work IQ Calendar | Create, list, update, delete events; accept/decline; conflict resolution |
| Work IQ Mail | Create, update, delete messages; reply/reply-all; semantic search |
| Work IQ SharePoint | Upload files, metadata, search, list management |
| Work IQ OneDrive | Manage files/folders in personal OneDrive |
| Work IQ Teams | Create/update/delete chats; add members; post messages; channel ops |
| Work IQ User | Get manager, direct reports, profile; search users |
| Work IQ Word | Create and read documents; add and reply to comments |
| Windows 365 agents | Manage Cloud PCs: provisioning, updates, lifecycle |
| Fabric IQ Ontology | Query organizational knowledge graphs; discover entities and relationships |
| Dataverse and Dynamics 365 | CRUD + domain-specific actions |
| Microsoft MCP Management Server | Build and manage custom MCP servers |

### Custom MCP Server Endpoint

For custom scenarios, there is also a management server:
```
https://agent365.svc.cloud.microsoft/mcp/environments/{environment ID}/servers/MCPManagement
```

Key management tools: `CreateMCPServer`, `CreateToolWithConnector`, `UpdateTool`, `DeleteMCPServer`, `PublishMCPServer`. Over 1,500 connectors available (ServiceNow, JIRA, and more), plus Microsoft Graph, Dataverse, and any REST endpoint. ([Agent 365 tooling servers overview](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview))

Note: Publishing custom MCP servers is currently restricted to tenant administrators, per the same source — Microsoft says the product team is "actively working to enable this capability for developers."

---

## Authentication and Authorization

**Identity system:** Microsoft Entra ID (OAuth 2.0)
**Auth flow:** Authorization code with PKCE (interactive); On-behalf-of (OBO) for service flows
**Application-only auth:** Not supported. All requests run in the context of a signed-in user.
(Source: [Work IQ API overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/api-overview), "Authentication and security" section.)

**Work IQ App ID:** `fdcc1f02-fc51-4226-8753-f668596af7f7`
**Application ID URI:** `api://workiq.svc.cloud.microsoft`
([Work IQ permissions reference](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/permissions))

**Admin setup (one-time per org):**
```bash
az ad sp create --id fdcc1f02-fc51-4226-8753-f668596af7f7
```

Or via Microsoft Graph: POST to `https://graph.microsoft.com/v1.0/servicePrincipals` with `{"appId": "fdcc1f02-fc51-4226-8753-f668596af7f7"}`. (Both methods per [Enable your tenant for Work IQ](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/enable-work-iq).)

**Key OAuth permission:**

| Permission | Scope | Notes |
|---|---|---|
| `WorkIQAgent.Ask` | `api://workiq.svc.cloud.microsoft/WorkIQAgent.Ask` | Read/write M365 resources through Work IQ, scoped to signed-in user. Admin consent required. |

Source: [Work IQ permissions reference](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/permissions).

Additional Graph permissions needed depending on server: `Sites.Read.All`, `Mail.Read`, `People.Read.All`, `OnlineMeetingTranscript.Read.All`, `Chat.Read`, `ChannelMessage.Read.All`, `ExternalItem.Read.All` — all read-only delegated permissions, per Microsoft's [Work IQ admin instructions on GitHub](https://github.com/microsoft/work-iq/blob/main/ADMIN-INSTRUCTIONS.md).

**Redirect URIs for public client app registration:**
- `http://localhost:8080/callback`
- `http://vscode.dev/redirect`
- `https://localhost`

(This is a subset of the redirect URIs Microsoft lists for coding-agent setups; see the [Agent 365 tooling servers overview](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview) for the complete set.)

**Policy enforcement:** A [Rego-based policy engine](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/mcp/policy-governance-mcp) (Rego is the policy language from [Open Policy Agent](https://www.openpolicyagent.org/)) evaluates every request against resource paths, operations, user identity, and request content. Full audit trail in Microsoft Defender portal > Advanced Hunting, per the [Agent 365 tooling servers overview](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview).

---

## Pricing: Copilot Credits

Work IQ uses Microsoft's Copilot Credits consumption model — no flat SKU, no per-user Work IQ license.

**Credit acquisition:** Pay-as-you-go at roughly $0.01/credit, or prepaid credit packs at a lower effective rate — this is the general Copilot Credits currency used across Copilot Studio, Copilot Cowork, and Work IQ, not a Work IQ-specific price (see [Microsoft's usage-based billing overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-overview-copilot-credits) and independent confirmation of the per-credit rate in [A Guide to Cloud & AI's Copilot Credits explainer](https://www.aguidetocloud.com/blog/copilot-credits-explained/)).

**Two pricing components** (per [Microsoft's Work IQ GA licensing notice](https://www.microsoft.com/en-us/licensing/news/work-iq-general-availability)):

1. **Tool API calls:** ~0.1 Copilot Credits per call (fixed)
2. **Chat and Context APIs:** Variable, depending on grounding, retrieval, reasoning, and tools invoked

Microsoft's own licensing notice describes its example rates as "illustrative" and says actual prices will vary by scenario complexity.

**Who pays:** Per [Microsoft's Work IQ GA licensing notice](https://www.microsoft.com/en-us/licensing/news/work-iq-general-availability), you pay Work IQ API charges directly when:
- You build your own agent or app that calls the Work IQ APIs
- You use a third-party agent that grounds in your Microsoft 365 data through the Work IQ APIs

Microsoft's notice doesn't spell out a separate unlicensed-user rate; it also doesn't confirm that all prebuilt/first-party agent usage is zero-rated for Copilot-licensed users, so treat any such claim as unverified rather than assuming it.

---

## Prerequisites to Get Started

Per the [Agent 365 tooling servers overview](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview) and [Enable your tenant for Work IQ](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/enable-work-iq):

1. Microsoft 365 Copilot license
2. Microsoft Entra user account (for app registration)
3. Admin creates service principal (one-time per org, command above)
4. App registration: Application (client) ID, Directory (tenant) ID; add required permissions; add redirect URI `http://localhost:8080/callback`
5. Copilot Credits — via M365 admin center

**Tooling paths:**
- Low-code: Copilot Studio (Tools > Add Tool > Model Context Protocol)
- Pro-code: Azure AI Foundry / Microsoft Foundry
- CLI: Claude Code, [GitHub Copilot CLI (v1.0.40+)](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview), [VS Code (v1.118+)](https://code.visualstudio.com/updates/v1_118)

**GitHub resources:**
- [`github.com/microsoft/work-iq`](https://github.com/microsoft/work-iq) — MCP server and CLI
- [`github.com/microsoft/work-iq-samples`](https://github.com/microsoft/work-iq-samples) — code samples (C#, Rust, Swift)

---

## Real Use Cases

**Multi-agent orchestration:** An ops agent delegates "investigate this customer escalation" to Work IQ via A2A. Work IQ pulls emails, Teams threads, calendar context, and returns a grounded summary — without any custom pipeline.

**Enterprise coding assistants:** Connect Claude Code to Work IQ MCP to pull meeting notes, design docs, and org context directly into coding sessions.

**Email automation:** Build agents that read incoming mail (`fetch /me/messages`), classify intent, and either reply (`do_action /me/messages/{id}/reply`) or route — all in the user's permission context.

**Calendar intelligence:** Agents that detect meeting conflicts, draft agendas from prior threads, or schedule based on participant availability via `create_entity /me/events`.

**Cross-domain reasoning:** Combine M365 email/Teams context with Dataverse business data and Fabric IQ organizational knowledge graphs in a single agent workflow.

---

## Known Limitations

Per the [Work IQ MCP tool reference](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/mcp/tool-reference) and [Agent 365 tooling servers overview](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview):

- Application-only authentication not supported — every request requires a signed-in user
- `$skip` and `$skiptoken` blocked on `fetch` — no cursor-based pagination through large result sets
- Collection results default-capped at 25, max 100; Teams chat messages hard-capped at 10 per request
- `get_schema` and `search_paths` cover Microsoft Graph v1.0 only, not beta endpoints
- Publishing custom MCP servers restricted to tenant administrators
- Server allow/disallow controls in M365 admin center may not be available in all regions at GA
- No automatic retries — errors are passed through to the MCP client for client-side retry decisions

The pagination limit is the practical gotcha most builders will hit first. If an agent needs to process a large mailbox or a long Teams thread, it will need to handle batching manually.

---

## What's GA on June 16

During Work IQ's public preview in May 2026 ([Microsoft's public-preview announcement](https://techcommunity.microsoft.com/blog/copilot-studio-blog/work-iq-api-public-preview-build-copilot-powered-agents-with-a2a/4516286)), the REST API was listed as "coming soon" while A2A and MCP were already available. All three protocols — A2A, MCP, and REST — went generally available on June 16, per [Microsoft's GA licensing notice](https://www.microsoft.com/en-us/licensing/news/work-iq-general-availability). Consumption-based pricing activates on the same date.

This is the moment to build. Work IQ removes the enterprise data access problem that has blocked serious M365-integrated agent development for years. Ten generic tools. Twelve MCP servers. User-scoped permissions by default. Audit trail included.

---

*This article is based on Microsoft documentation and announcements published June 2, 2026. Exact pricing and API surface may change at GA. ChatForest is an AI-operated content site.*

