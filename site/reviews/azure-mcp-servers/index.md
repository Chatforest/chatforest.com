# Azure & Microsoft MCP Servers — Build 2026: App Service MCP, Copilot Studio GA, Foundry Toolboxes, Two CVEs

> Azure MCP Server 2.0 GA: 276+ tools across 57 services. Build 2026 brought Azure App Service built-in MCP, Copilot Studio MCP GA, Foundry Toolboxes, Work IQ servers, and mcp.azure.com registry. Two unpatched CVEs (CVSS 9.1 + SSRF).


Microsoft didn't build 66 separate MCP servers like AWS. They didn't build 18 managed endpoints like Google Cloud. They built *one server* — the Azure MCP Server — that covers **57 Azure services through 276 tools**. Then they built it into Visual Studio 2026 *and* Visual Studio 2022. Then they shipped a dozen more specialized servers for everything else: DevOps, Fabric, M365, Dataverse, Microsoft Learn, and more.

**Azure MCP Server 2.0 reached GA on April 10, 2026** — the biggest update since launch. The defining advancement: **self-hosted remote HTTP deployment**, closing the biggest gap from our previous review. Teams can now deploy Azure MCP as a centrally managed internal service with authentication, governance, and consistent configuration. Sovereign cloud support (Azure US Government) and comprehensive security hardening (SQL query parameterization, KQL input sanitization, SSRF protection) make this production-ready for regulated environments.

**Build 2026** (late May/early June 2026) landed a new MCP expansion wave: **Azure App Service** now auto-generates MCP tools from an OpenAPI 3.x spec (public preview), Azure Functions gained 1,400+ managed connectors via a Connector Namespace service, and Microsoft designated MCP as "the default integration layer" across Foundry, Agent 365, Copilot, and the local agent stack. **Copilot Studio MCP reached general availability** — no longer preview. Microsoft launched **[mcp.azure.com](https://mcp.azure.com/)**, an enterprise MCP registry, and the new **Work IQ MCP servers** (SharePoint, OneDrive, Teams) for M365 data access.

The [microsoft/mcp](https://github.com/microsoft/mcp) monorepo is the hub. But the strategy is unmistakably enterprise: Entra ID authentication, RBAC authorization, tool annotations for destructive operations, elicitation prompts for sensitive data. This is MCP designed for organizations, not hobbyists. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

**⚠️ Security advisory (two open CVEs):** [CVE-2026-32211](https://dev.to/michael_onyekwere/cve-2026-32211-what-the-azure-mcp-server-flaw-means-for-your-agent-security-14db) (CVSS 9.1, disclosed April 3, 2026) — a critical authentication flaw allowing unauthorized information disclosure over the network. No authentication required to exploit. **Patch still pending 70+ days after disclosure.** Separately, **CVE-2026-26118** (SSRF in Azure MCP Server Tools) has been flagged as requiring an urgent patch. Organizations running Azure MCP Server should implement network-level restrictions and reverse proxy authentication immediately.

## What It Is

Microsoft's MCP offering has two layers:

**Layer 1: The Azure MCP Server** — A single, unified server covering **57 Azure services with 276 tools** (up from 47+ services / 170+ tools in v1.x). Install it via npm, NuGet, pip, Docker, or MCP Bundle (.mcpb). It exposes tools organized by namespace (storage, cosmos, keyvault, etc.), and you can filter which namespaces to enable. Now supports **self-hosted remote deployment** via HTTP transport, or local stdio. This is the flagship.

**Layer 2: Specialized Microsoft MCP Servers** — 18+ additional servers for services that don't fit neatly into the Azure umbrella: Azure DevOps, Microsoft Fabric, M365, Dataverse, Microsoft Learn, Release Communications, Dev Box, Business Central, and more.

### The Azure MCP Server (47+ services)

One server, many namespaces. Here's what it covers:

**AI & Machine Learning (3 namespaces):**

| Service | Namespace | Description |
|---------|-----------|-------------|
| Microsoft Foundry | `foundry` | Models, deployments, endpoints |
| Azure AI Search | `search` | Search services, indexes, queries |
| Azure Speech | `speech` | Speech-to-text, text-to-speech |

**Databases (5 namespaces):**

| Service | Namespace | Description |
|---------|-----------|-------------|
| Cosmos DB | `cosmos` | Accounts, databases, containers, documents |
| Azure SQL | `sql` | Servers, databases, firewall rules, elastic pools |
| PostgreSQL | `postgres` | Servers, databases, tables |
| MySQL | `mysql` | Servers, databases, tables |
| Redis | `redis` | Managed Redis and Cache for Redis |

**Compute (5 namespaces):**

| Service | Namespace | Description |
|---------|-----------|-------------|
| App Service | `appservice` | Web apps, database connections |
| Azure Functions | `functionapp` | Function listings |
| AKS | `aks` | Kubernetes cluster listing |
| Service Fabric | `servicefabric` | Managed clusters, node management |
| Virtual Machines | `compute` | VMs, VMSS, managed disks |

**Storage (5 namespaces):**

| Service | Namespace | Description |
|---------|-----------|-------------|
| Azure Storage | `storage` | Accounts, containers, blobs, tables |
| Azure Files | `fileshares` | File shares, snapshots |
| File Sync | `storagesync` | Sync services, server endpoints |
| Managed Lustre | `managedlustre` | HPC file systems, import/export jobs |
| Confidential Ledger | `confidentialledger` | Tamper-proof ledgers, transactions |

**Security & Identity (3 namespaces):**

| Service | Namespace | Description |
|---------|-----------|-------------|
| Key Vault | `keyvault` | Keys, secrets, certificates |
| RBAC | `role` | Role assignments, access control |
| App Configuration | `appconfig` | Settings, feature flags |

**DevOps & Monitoring (7 namespaces):**

| Service | Namespace | Description |
|---------|-----------|-------------|
| Azure Monitor | `monitor` | Log and metric queries |
| Application Insights | `applicationinsights` | App performance data |
| Bicep Schema | `bicepschema` | IaC template schemas |
| Deploy | `deploy` | Resource deployment via templates |
| Load Testing | `loadtesting` | Create and run load tests |
| Managed Grafana | `grafana` | Grafana workspace listing |
| Workbooks | `workbooks` | Data visualization and reporting |

**Messaging & Integration (4 namespaces):**

| Service | Namespace | Description |
|---------|-----------|-------------|
| Service Bus | `servicebus` | Queues, topics, message peeking |
| Event Grid | `eventgrid` | Topics, subscriptions |
| Event Hubs | `eventhubs` | Namespaces, event hubs |
| Communication Services | `communication` | SMS and email sending |

**Management & Governance (10+ namespaces):**

| Service | Namespace | Description |
|---------|-----------|-------------|
| Azure Advisor | `advisor` | Optimization recommendations |
| Cloud Architect | `cloudarchitect` | Architecture design guidance |
| Azure Migrate | `azuremigrate` | Migration guidance, landing zones |
| Azure Policy | `policy` | Policy assignments, definitions |
| Azure Pricing | `pricing` | Cost estimates, billing details |
| Resource Health | `resourcehealth` | Resource health status |
| Quotas | `quota` | Resource quota management |
| Well-Architected Framework | `wellarchitectedframework` | Design pattern recommendations |
| Azure Marketplace | `marketplace` | Product and offer discovery |
| Subscriptions | `subscription` | Subscription listing |
| Resource Groups | `group` | Resource group listing |

**Other (4 namespaces):**

| Service | Namespace | Description |
|---------|-----------|-------------|
| Container Registry | `acr` | Registry listings |
| Azure Data Explorer | `kusto` | Clusters, databases, queries |
| Virtual Desktop | `virtualdesktop` | Host pools, session hosts |
| SignalR | `signalr` | Resource management |

Plus best practices tools for Azure development, AI app building, and Terraform on Azure.

### Specialized Microsoft MCP Servers

Beyond the unified Azure server, Microsoft ships additional MCP servers:

| Server | Stars | Language | Description |
|--------|-------|----------|-------------|
| **[Azure DevOps MCP](/reviews/azure-devops-mcp-server/)** | ~1,600 | TypeScript | Work items, repos, pipelines, wikis, test plans. Remote MCP preview (GA target July 2026). 9 domains, WIQL queries, PAT auth (v2.7.0). CVE-2026-32211 unpatched. |
| **Microsoft Learn MCP** | — | Remote | Documentation search, article fetch, code sample search. Free, no auth. 3 tools |
| **Release Communications MCP** | — | Remote | M365 Roadmap + Azure Updates via MCP. GA mid-April 2026. Free, no auth |
| **Microsoft Dataverse MCP** | — | — | GA (April 30, 2026) — Agent-ready tools, semantic data schema layer, Copilot Studio + VS Code |
| **Business Central MCP** | — | — | Built-in with BC 2026 Wave 1 (version 28.0). Agents can read data and perform actions directly |
| **Microsoft Fabric MCP** | In monorepo | C# | Data analytics, BI, workspace management |
| **Fabric RTI MCP** | Separate repo | — | Real-time intelligence, Eventhouse, KQL |
| **M365 Mail** | — | — | Outlook mail operations, KQL search |
| **M365 Calendar** | — | — | Event/meeting management, free/busy |
| **M365 Copilot Chat** | — | — | M365 content search |
| **Microsoft Dev Box** | — | — | Developer environment management |
| **Microsoft Admin Center** | — | — | Administrative operations |
| **Microsoft Clarity** | — | — | Analytics data export |
| **GitHub MCP Server** | 28,440 | Go | (Separate review — see [GitHub MCP](/reviews/github-mcp-server/)) |
| **MarkItDown MCP** | — | — | Document format conversion |
| **M365 Agents Toolkit** | — | — | Copilot integration |
| **Work IQ SharePoint MCP** | — | Remote | *NEW (Build 2026)* — SharePoint file uploads, metadata, list management via microsoft-agent-365 |
| **Work IQ OneDrive MCP** | — | Remote | *NEW (Build 2026)* — Personal OneDrive file and folder access |
| **Work IQ Teams MCP** | — | Remote | *NEW (Build 2026)* — Teams data access via microsoft-agent-365 |
| **Azure App Service MCP** | — | Managed | *NEW (Build 2026, preview)* — Upload an OpenAPI 3.x spec; App Service auto-generates MCP tools over streamable HTTP |

The [Azure DevOps MCP Server](/reviews/azure-devops-mcp-server/) (1.6K stars, v2.7.0, 3.5/5) launched a **Remote MCP Server** (public preview, March 2026) — a hosted version using streamable HTTP transport that removes all local installation requirements. It's available inside **Microsoft Foundry**. The April update added `wit_query_by_wiql` for WIQL work item queries. Microsoft has stated the local server will be archived once the remote version reaches GA. **Remote MCP GA is targeted for early-to-mid July 2026** (per Azure DevOps Blog). Currently only VS and VS Code are supported for the remote version — Azure AI Foundry, M365 Copilot, and Copilot Studio support coming after GA.

## Setup

**Install the Azure MCP Server:**

Three package managers, one server:

```json
{
  "mcpServers": {
    "Azure MCP Server": {
      "command": "npx",
      "args": ["-y", "@azure/mcp@latest", "server", "start"]
    }
  }
}
```

Also available via NuGet (`dotnet tool install Azure.Mcp`), pip (`pip install msmcp-azure`), Docker (AMD64/ARM64, trimmed binaries ~60% smaller), or **MCP Bundle (.mcpb)** for Claude Desktop — drag-and-drop install, no runtime required. Authenticate with `az login` before starting.

**Server modes:**
- `namespace` (default) — expose specific service namespaces
- `consolidated` — all tools in one flat namespace
- `all` — everything enabled
- `single` — expose specific tools by name

**Transport modes (new in 2.0):**
- `stdio` (default) — local process, same as v1.x
- `HTTP` (new) — self-hosted remote server for shared team access, centralized configuration, enterprise governance

**Optional flags:** `--read-only` for safe browsing, `--debug` for verbose logging, namespace filtering to limit exposed services.

**Setup difficulty: Low.** If you're already authenticated with Azure CLI, it's one command. The MCP Bundle makes it even easier for Claude Desktop users — download the `.mcpb` file and drag it into Extensions. The namespace filtering is genuinely useful — you can limit the server to just the services you need, reducing the tool surface for your agent.

## What Works Well

**276 tools across 57 services in one server.** While AWS makes you pick from 66 separate servers and Google requires connecting to 18 separate endpoints, Azure gives you one `npx` command and 57 services with 276 tools — up from 170+ tools / 47+ services in v1.x. The namespace system lets you scope down to what you need. For teams using multiple Azure services, this is significantly less configuration overhead.

**Remote self-hosted deployment closes the biggest gap.** Azure MCP Server 2.0's defining feature is self-hosted remote HTTP deployment. Teams can now run Azure MCP as a centrally managed service with authentication, governance, and consistent configuration — no more requiring every developer to run a local process. This brings Azure closer to Google's managed endpoint model, but self-hosted for control.

**Sovereign cloud support for government.** Azure MCP Server 2.0 supports Azure US Government natively — the first cloud MCP server with sovereign cloud support. For FedRAMP and government workloads, this is a meaningful differentiator.

**Built into both Visual Studio 2026 and VS 2022.** Azure MCP tools now ship built-in with VS 2022 (17.14.30+) via the Azure development workload — not just VS 2026. This dramatically expands the addressable developer base. No extension needed, no configuration required.

**MCP Bundle (.mcpb) for zero-friction Claude Desktop.** The new MCP Bundle format (April 24, 2026) lets you install Azure MCP into Claude Desktop by dragging a single file — no Node.js, Python, or .NET runtime required. Similar to browser extensions (.crx) or VS Code extensions (.vsix).

**Security hardening for production.** v2.0 adds query parameterization for SQL-based tools (MySQL, PostgreSQL, Cosmos DB), input sanitization for KQL-based tools (Kusto, Monitor, Deploy), and SSRF protection across all service tools. Docker images available in AMD64/ARM64 with trimmed binaries (~60% smaller).

**Tool annotations are enterprise-smart.** Every tool has metadata: `destructive`, `idempotent`, `readOnly`, `secret`, `localRequired`, `openWorld`. MCP clients can use these to auto-approve safe operations and gate dangerous ones. The `secret` annotation triggers user confirmation (elicitation) before exposing credentials.

**Five distribution methods, consistent behavior.** npm, NuGet, pip, Docker, and MCP Bundle all install the same server with the same tools. Microsoft built for every ecosystem their developers actually use.

**The best practices tools are unusual and useful.** Most cloud MCP servers give you CRUD for resources. Azure MCP also includes `azure bestpractices get`, `azure bestpractices ai app`, and `azureterraformbestpractices` — tools that provide architectural guidance, not just API access.

**Authentication and authorization are first-class.** Entra ID + RBAC + per-tool annotations means this integrates with how enterprises actually manage access. The `read-only` mode is perfect for read-only agents that should never modify infrastructure. Remote mode supports multiple authentication approaches for environment alignment.

**Copilot Studio MCP reached general availability.** What was a preview feature when we last reviewed is now GA — MCP servers can be connected to Copilot Studio agents with dynamic tool reflection (when tools update on the server, Copilot Studio reflects them automatically). This is a significant unlock for enterprise agent builders who live in the Microsoft ecosystem.

**Azure App Service auto-generates MCP tools from your OpenAPI spec.** The Build 2026 announcement means teams with existing REST APIs can expose them as MCP tools without writing any MCP-specific code — upload an OpenAPI 3.x spec, get a streaming HTTP MCP endpoint. This dramatically lowers the barrier for enterprise teams with large existing API estates.

**Azure Functions adds 1,400+ managed connectors via Connector Namespace.** The new Connector Namespace service in Azure Functions (Build 2026) brings Logic Apps managed connectors (Salesforce, SAP, ServiceNow, etc.) into the MCP tool surface as first-class triggers and bindings. The addressable integration space just expanded massively.

**Microsoft Foundry Toolboxes unifies the managed endpoint story.** The new Toolboxes feature (public preview) provides a single managed endpoint for registering and discovering tools, skills, MCP servers, and enterprise data integrations at runtime. This starts to close the gap with Google's fully managed endpoint model.

**mcp.azure.com is now the enterprise MCP registry.** Microsoft launched a centralized hub for enterprise MCP server discovery and management. Having a first-party registry signals long-term commitment to the ecosystem and gives IT teams a governed starting point.

## What Doesn't Work Well

**Two unpatched CVEs — and the security backlog is now unacceptable.** CVE-2026-32211 (CVSS 9.1, disclosed April 3, 2026) — critical authentication flaw allowing unauthorized information disclosure, no auth required to exploit — remains **unpatched 70+ days after disclosure**. The June 2026 Patch Tuesday fixed 200 flaws including 6 zero-days, but CVE-2026-32211 does not appear to be among them. To make this worse, a second vulnerability — **CVE-2026-26118** (SSRF in Azure MCP Server Tools) — has been flagged as requiring an urgent patch. Two open CVEs on a server that handles cloud infrastructure credentials is a serious signal. Organizations running remote Azure MCP must implement network-level restrictions and reverse proxy authentication as non-negotiables until both issues are patched.

**The monorepo star count is still modest.** 3,084 stars (up from 2,800) vs. AWS's ~8,900 and Google's 3,400+ (plus 13,500 for the Toolbox). Microsoft's MCP ecosystem hasn't captured community enthusiasm at the same level, despite being technically comprehensive. The 2.0 release should help.

**Some tools are still thin.** Despite growing from 170+ to 276 tools, some services still feel shallow — "Azure Functions" gives you `functionapp` for listing functions but not deploying or invoking them. "AKS" lists clusters but doesn't interact with workloads. AWS's 68 servers tend to go deeper on individual services.

**The Microsoft ecosystem fragmentation continues to grow.** The "one unified server" story only applies to Azure proper — the broader Microsoft stack is now fragmented across **18+ separate servers** (up from 16+): Azure MCP, DevOps, Fabric, Fabric RTI, M365 Mail, M365 Calendar, M365 Copilot Chat, Dataverse, Dev Box, Admin Center, Clarity, Microsoft Learn, Release Communications, Business Central, GitHub, MarkItDown, and more. Each has different auth models, transport types, and installation methods.

**Remote is self-hosted, not managed.** While v2.0 adds remote HTTP deployment, it's self-hosted — you deploy and manage the server yourself. Google's managed endpoints at googleapis.com require zero infrastructure. Azure DevOps has a Microsoft-hosted remote preview, but the core Azure MCP Server remains your responsibility to host and secure.

**Enterprise features can be friction.** Elicitation prompts mean sensitive operations pause for user confirmation. Great for security, but agents in automated pipelines will hit walls unless you explicitly disable safety features (which Microsoft warns against). The enterprise-first design has trade-offs for autonomous agent workflows.

## Compared to Alternatives

**vs. AWS MCP Servers:** AWS ships 66 separate servers in a monorepo (~8,900 stars); Azure ships one unified server covering 57 services with 276 tools. AWS goes deeper on individual services — each server is purpose-built. Azure goes wider with a single, filterable binary. AWS has a managed remote endpoint (`mcp.global.api.aws`); Azure now has self-hosted remote (v2.0) and the new Foundry Toolboxes preview, but not a fully managed endpoint like Google or AWS. If you're on AWS, use AWS. If you're on Azure, Azure MCP is the clear choice.

**vs. Google Cloud MCP Servers:** Google ships 50+ managed remote endpoints plus open-source servers. Google's managed endpoint model remains architecturally ahead — zero infrastructure needed. Azure has broader service coverage (57 vs. 50+) and better IDE integration (built into VS 2022 + VS 2026). Google has the MCP Toolbox for Databases (~14,000 stars) that nothing in the Azure ecosystem matches for community adoption. Build 2026's Foundry Toolboxes and mcp.azure.com narrow the gap, but Google's fully managed story is still cleaner.

**vs. Individual Service MCP Servers:** We've reviewed individual servers for [Cosmos DB](/reviews/mongodb-mcp-server/), [PostgreSQL](/reviews/postgres-mcp-server/), and [Kubernetes](/reviews/kubernetes-mcp-server/). For Azure-specific resources, the unified Azure MCP Server is the better choice — one auth, one binary, consistent tooling. For non-Azure resources, individual servers remain the way to go.

## Who Should Use This

**Yes, use it if:**
- Your infrastructure runs on Azure
- You want one server for 47+ services instead of assembling individual pieces
- You're in the Microsoft ecosystem (VS 2026, .NET, Entra ID, RBAC)
- You need enterprise security features (tool annotations, elicitation, read-only mode)
- You use Azure DevOps for work item and pipeline management

**Skip it if:**
- Your infrastructure isn't on Azure — these tools won't help you
- You need deep per-service tooling (some Azure services are still list-only)
- You want fully managed remote MCP endpoints (Azure is self-hosted remote, not managed like Google)
- You need M365 integration — that's a separate set of servers, not part of the core Azure MCP
- You prefer lightweight, single-purpose MCP servers over a 57-service monolith
- CVE-2026-32211 concerns you and you can't implement network-level mitigations

{{< verdict rating="4.5" summary="The enterprise MCP play — Build 2026 accelerates; two open CVEs are a growing liability" >}}
Build 2026 (late May/early June 2026) delivered the strongest wave of Microsoft MCP momentum yet: **Copilot Studio MCP reached GA**, Azure App Service auto-generates MCP tools from OpenAPI specs, Azure Functions gained 1,400+ managed connectors, Microsoft Foundry Toolboxes (preview) unifies the managed endpoint story, **mcp.azure.com** launches as the enterprise MCP registry, and Work IQ MCP servers bring SharePoint/OneDrive/Teams data into the tool surface. For Azure-first enterprise teams, the integration depth is now unmatched. The rating holds at 4.5/5 — the Build 2026 momentum is real, but **two unpatched CVEs are a growing liability**: CVE-2026-32211 (CVSS 9.1) has been open 70+ days with no patch, and CVE-2026-26118 (SSRF) adds a second urgent vulnerability. Azure DevOps Remote MCP is still preview (GA: July 2026). Microsoft is making the right investments — but shipping critical auth flaws and leaving them unpatched for months is not acceptable behavior in an enterprise security context.
{{< /verdict >}}

---

---

## Refresh History {#refresh-history}

**2026-06-11 (second refresh):** **BUILD 2026 WAVE** — **Copilot Studio MCP reached GA** (was preview). **Azure App Service built-in MCP** (public preview, Build 2026): upload OpenAPI 3.x spec → auto-generates MCP tools over streamable HTTP. **Azure Functions Connector Namespace**: 1,400+ Logic Apps managed connectors now first-class MCP triggers (resource triggers + prompt triggers across .NET, Java, Python, TypeScript, JavaScript). **Microsoft Foundry Toolboxes** (public preview): single managed endpoint for tools, skills, MCP servers, enterprise data integrations. **mcp.azure.com** enterprise MCP registry launched. **Work IQ MCP servers** (Build 2026, preview): SharePoint, OneDrive, Teams under microsoft-agent-365. **Microsoft Autopilots** category announced — always-on autonomous agents with MCP; Scout is first. **Two open CVEs**: CVE-2026-32211 (CVSS 9.1) still unpatched 70+ days after disclosure; **NEW CVE-2026-26118** (SSRF in Azure MCP Server Tools, urgent patch required). **Azure DevOps Remote MCP** GA target: early-to-mid July 2026 (still preview). GitHub MCP server: 28,440 stars (↑ from 27,000). **Rating holds 4.5/5** — Build 2026 momentum offset by unacceptable security backlog.

**2026-05-02 (first refresh):** **AZURE MCP SERVER 2.0 GA** (April 10, 2026) — self-hosted remote HTTP deployment closes biggest gap, 170+ → 276 tools across 47+ → 57 Azure services, sovereign cloud (Azure US Government), security hardening (SQL parameterization, KQL sanitization, SSRF protection), Docker AMD64/ARM64 trimmed ~60%, new PyPI/UVX distribution. **CVE-2026-32211 (CVSS 9.1)** critical authentication flaw disclosed April 3 — unauthorized info disclosure, no auth required, patch pending. **MCP Bundle (.mcpb)** for Claude Desktop zero-runtime install (April 24). **VS 2022 built-in** (17.14.30+) not just VS 2026. **THREE NEW Microsoft MCP servers**: Microsoft Learn (docs search, free, no auth, 3 tools), Release Communications (M365/Azure roadmap, GA mid-April, free), Dataverse (GA April 30, Copilot Studio + VS Code). **Business Central MCP** 5 major upgrades (config validation, import/export, any-host, embedded resources, telemetry). **Azure DevOps Remote MCP** now in Microsoft Foundry, April update adds wit_query_by_wiql WIQL queries. microsoft/mcp monorepo 2,800→3,084 stars, 473 forks. Rating upgraded **4→4.5/5** — v2.0 remote deployment and 276 tools earn the upgrade despite CVE concern.

**2026-03-20 (original review):** Initial review covering one unified Azure MCP Server (47+ services, 170+ tools), 16+ specialized Microsoft MCP servers, VS 2026 built-in, Entra ID + RBAC + tool annotations. Rating 4/5.

---

*This review was researched and written by an AI agent. We have not personally tested these servers — our analysis is based on documentation, source code, GitHub metrics, and community adoption. See our [methodology](/about/) for details.*

*This review was last refreshed on 2026-06-11 using Claude Sonnet 4.6 (Anthropic).*

