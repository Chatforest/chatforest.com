---
title: "MCP and Cloud Providers: How AWS, Azure, Google Cloud, and Cloudflare Deploy and Host the Model Context Protocol"
date: 2026-03-29T18:00:00+09:00
description: "A comprehensive guide to MCP integration across major cloud providers — covering Amazon Bedrock AgentCore, AWS Lambda MCP hosting, 66+ AWS MCP servers, Amazon Q Developer, Google"
content_type: "Guide"
card_description: "Every major cloud provider now offers native MCP support — from managed server hosting to enterprise gateways. This guide covers AWS (Bedrock AgentCore, Lambda, Q Developer, 66+ servers), Google Cloud (managed MCP servers, Vertex AI, ADK), Azure (Foundry, Functions, Copilot, Semantic Kernel), and Cloudflare (Workers, MCP Portals), plus cross-cutting patterns for authentication, deployment, and multi-cloud architectures."
last_refreshed: 2026-04-04
---

When Anthropic open-sourced the Model Context Protocol in November 2024, cloud providers faced a choice: build proprietary alternatives or embrace the open standard. By early 2026, every major cloud provider chose the latter. AWS maintains 66+ official MCP servers. Google Cloud offers fully managed remote MCP servers for BigQuery, Spanner, and a dozen other services. Azure built MCP into Functions, Foundry, and Copilot. Cloudflare turned Workers into the fastest way to deploy MCP servers at the edge.

The result is a cloud MCP ecosystem where the protocol itself is standardized but the hosting, authentication, and governance patterns vary significantly across providers. Choosing the right cloud integration depends on your existing infrastructure, security requirements, and whether you need serverless simplicity or enterprise-grade gateway patterns.

This guide covers every major cloud provider's MCP integration with architectural details, authentication patterns, and deployment guidance. Our analysis draws on official cloud documentation, engineering blog posts, and published benchmarks — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## Cloud Provider MCP Support at a Glance

| Provider | MCP Hosting | Managed MCP Servers | IDE/Dev Tools | Authentication | AAIF Role |
|---|---|---|---|---|---|
| **AWS** | Lambda, Bedrock AgentCore | 66+ (awslabs/mcp) | Q Developer, Kiro | IAM, CloudTrail | Platinum |
| **Google Cloud** | Cloud Run, managed | 10+ managed (BigQuery, Maps, GKE, etc.) | Gemini CLI, ADK | IAM, org-level controls | Platinum |
| **Microsoft Azure** | Azure Functions (GA) | Foundry MCP Server | Copilot, VS 2026 | Entra ID, RBAC | Platinum |
| **Cloudflare** | Workers (edge) | 13 official | N/A | Zero Trust, OAuth | Platinum |
| **Vercel** | Functions (Fluid Compute) | 1 (Vercel platform) | AI SDK 6 | OAuth | N/A |
| **DigitalOcean** | App Platform, Droplets | 9 services (remote MCP) | N/A | Bearer token, OAuth | N/A |

All four major providers are platinum members of the [Agentic AI Foundation](/guides/mcp-ecosystem-2026-state-of-the-standard/) (AAIF), formed December 2025 under the Linux Foundation to govern MCP's future.

## AWS: The Broadest MCP Ecosystem

Amazon Web Services has built the most expansive MCP offering of any cloud provider, with managed runtime environments, serverless hosting, 66+ official MCP servers covering nearly every AWS service, and deep integration into their developer tools.

### Amazon Bedrock AgentCore

[Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) provides a managed runtime for MCP servers, running each user session in a dedicated, isolated microVM. This is the most enterprise-ready MCP hosting option in any cloud:

- **Session isolation** — each MCP session runs in its own microVM, with session context maintained via the `Mcp-Session-Id` header
- **Stateful MCP features** (announced March 2026) — supports elicitation (server-initiated multi-turn conversations), sampling (servers request AI text generation from clients), and progress notifications for long-running operations
- **Protocol versions** — supports MCP spec versions 2025-06-18 and 2025-03-26
- **Gateway integration** — AgentCore acts as an MCP gateway with built-in IAM-based permissions, zero credential exposure, and CloudTrail audit logging
- **Regional availability** — 14 AWS regions across North America, Europe, and Asia-Pacific

The AgentCore gateway pattern is significant: rather than exposing MCP servers directly, AgentCore sits in front of them, handling authentication, authorization, and audit logging centrally. This aligns with the [enterprise gateway patterns](/guides/mcp-gateway-proxy-patterns/) that organizations increasingly adopt as they scale MCP deployments.

### AWS Lambda as MCP Server Host

For teams that want serverless MCP without the full AgentCore runtime, [AWS Lambda](/guides/mcp-serverless-deployment/) provides a lighter-weight option:

- **Container-based deployment** — Express-based MCP servers deploy as containerized Lambda functions behind API Gateway, with the AWS Lambda Web Adapter translating HTTP requests
- **Python support** — a dedicated Python library provides serverless HTTP handlers for MCP using Lambda with DynamoDB for session management
- **Transport** — uses Streamable HTTP (sessionless) — SSE transport was deprecated as of the MCP spec 2025-03-26
- **AWS Serverless MCP Server** — a purpose-built server supporting Lambda event source mapping tools, announced October 2025

Lambda-hosted MCP servers suit teams already invested in the serverless model and needing pay-per-invocation pricing without the overhead of managing infrastructure.

### 66+ Official AWS MCP Servers

AWS maintains the largest collection of official MCP servers of any cloud provider at [github.com/awslabs/mcp](https://github.com/awslabs/mcp), organized by category:

**Essential/Managed (remote servers):**
- AWS Knowledge, AWS API, AWS Documentation — fully managed, no local setup

**Infrastructure:**
- CloudFormation, CDK, Terraform, EKS, ECS, Serverless, Lambda, Step Functions, IoT SiteWise

**Databases:**
- DynamoDB, Aurora PostgreSQL/MySQL, DSQL, DocumentDB, Neptune, Keyspaces, Timestream, ElastiCache, MemoryDB, Redshift

**AI/ML:**
- Bedrock Knowledge Bases, Bedrock Data Automation, Bedrock Custom Model Import, SageMaker AI, Nova Canvas, Q Business, Q Index

**Operations:**
- CloudWatch, CloudTrail, IAM, Support, Cost Explorer, Billing, Pricing, Well-Architected Security

**Data & Analytics:**
- S3 Tables, Data Processing (Glue/EMR), MSK

**Developer:**
- Git Repo Research, Code Documentation, Frontend, Synthetic Data, OpenAPI, AppSync

**Specialized:**
- HealthOmics, HealthImaging, HealthLake (healthcare); Cloud WAN, Transit Gateway, VPC, Network Firewall, VPN (networking)

This breadth means that an AWS-native team can connect AI agents to virtually any AWS service via MCP without building custom integrations.

### Amazon Q Developer

Amazon's AI coding assistant supports MCP as both a consumer and an integration point:

- **CLI MCP support** (April 2025) — supports both local MCP servers (stdio) and remote MCP servers (HTTP with OAuth)
- **IDE MCP support** (June 2025) — available in VS Code and JetBrains plugins
- **Remote MCP servers** (September 2025) — HTTP and OAuth-based authentication for services like Atlassian and GitHub

### AWS Kiro IDE

AWS's newer development environment includes native MCP integration for connecting to documentation, databases, and APIs. It works with the awslabs MCP server collection and includes features like IAM Policy Autopilot (February 2026) available as a one-click MCP-powered tool.

## Google Cloud: Managed MCP Servers

Google Cloud's MCP strategy centers on fully managed, remote MCP servers — pre-built, cloud-hosted servers that require no local infrastructure and integrate directly with Google Cloud services.

### Managed MCP Servers

Launched December 2025, Google's managed MCP servers provide enterprise-ready access to core cloud services:

**Currently available:**

| Server | Capabilities |
|---|---|
| **BigQuery** | Query records, generate forecasts — data accessed without loading into context windows |
| **Google Maps Platform** | Navigation, geocoding, route data via Maps Grounding Lite |
| **Compute Engine (GCE)** | Provision and manage VM instances |
| **Google Kubernetes Engine (GKE)** | Kubernetes + GKE API access via structured, discoverable interface |
| **AlloyDB, Cloud SQL, Spanner** | PostgreSQL-compatible database operations |
| **Firestore, Bigtable** | NoSQL workloads |
| **Developer Knowledge** | Google Cloud documentation and best practices |

**Coming soon:**
- Cloud Run, Cloud Storage, Cloud Resource Manager
- Looker, Pub/Sub, Dataplex Universal Catalog
- Database Migration Service, BigQuery Migration Service, Memorystore, Database Center, Kafka

### Cloud API Registry

Available in preview in the Google Cloud console, the Cloud API Registry provides centralized management of MCP servers and tools that agents can access. It integrates with Apigee to transform existing managed APIs into custom MCP servers — a significant feature for enterprises with large existing API portfolios.

### Vertex AI Agent Builder

Google's agent development platform supports MCP tools natively:

- MCP tool consumption in agent builder workflows
- Enhanced Tool Governance for MCP servers
- Deployment to Vertex AI Agent Engine with direct ADK integration
- Organization-level, folder-level, and project-level admin controls

### Agent Development Kit (ADK)

Google's [Agent Development Kit](https://google.github.io/adk-docs/) provides first-class MCP support across three languages:

- **Python ADK v1.0.0** — production-ready stable release
- **TypeScript ADK** — launched December 2025
- **Java ADK v0.1.0** — initial release extending MCP support to the Java ecosystem

ADK agents can both consume MCP tools and expose their own capabilities as MCP servers, enabling bidirectional integration. Agents built with ADK deploy to Vertex AI Agent Engine. For more on how ADK and other frameworks integrate MCP, see our [AI frameworks guide](/guides/mcp-ai-frameworks-langchain-langgraph-crewai/).

### Gemini API MCP Support

The Gemini API includes built-in MCP server support in Python and JavaScript SDKs (experimental):

- Automatically calls MCP tools when needed
- Connects to both local and remote MCP servers
- Currently only accesses the tools endpoint (`list_tools`) — resources and prompts not yet supported
- **Gemini CLI** also includes native MCP server support

### Cloud Run as MCP Host

For custom MCP servers, [Cloud Run](https://cloud.google.com/run/docs/host-mcp-servers) provides container-based hosting with:

- Streamable HTTP transport support (not stdio)
- Auto-scaling based on demand
- IAM-based access control for team sharing
- Documentation last updated March 2026

### Agent2Agent (A2A) and MCP

Google created the [Agent2Agent (A2A) protocol](/guides/mcp-vs-a2a-protocol-comparison/) as a complement to MCP: while MCP connects agents to tools and data, A2A connects agents to other agents. IBM's Agent Communication Protocol (ACP) merged with A2A in September 2025, creating a unified agent-to-agent standard governed by a Technical Steering Committee including Google, Microsoft, AWS, Cisco, Salesforce, ServiceNow, and SAP.

## Microsoft Azure: Enterprise MCP Integration

Microsoft's MCP strategy spans Azure infrastructure, developer tools, and the Microsoft 365 ecosystem — the broadest horizontal reach of any cloud provider's MCP offering.

### Azure AI Foundry (Microsoft Foundry)

The [Foundry MCP Server](https://mcp.ai.azure.com) launched December 2025 at Ignite as a cloud-hosted MCP endpoint:

- **Hosted at `mcp.ai.azure.com`** — zero local process management required
- **Entra ID authentication** with Azure RBAC permissions enforcement
- **Activity logging** for auditability; Conditional Access via Azure Policy
- **Tools tab** — single entry point for MCP servers, A2A endpoints, Azure AI Search, SharePoint, Fabric, and 1,400+ business systems
- **Azure DevOps Remote MCP Server** (public preview March 2026) — provides AI agent access to work items, pull requests, pipelines, repos, and wikis

The Foundry approach treats MCP as one tool integration mechanism among several (alongside A2A and traditional connectors), providing a unified governance layer regardless of the underlying protocol.

### Azure Functions MCP Extension

The Azure Functions MCP extension reached general availability (GA) after entering public preview in April 2025:

- **Language support** — C#/.NET, Java, JavaScript/Node.js, Python, TypeScript
- **Two deployment models:**
  - **Native MCP tool triggers** — write Functions that respond to MCP tool calls using the built-in MCP bindings
  - **Self-hosted MCP servers** (public preview) — deploy existing MCP SDK-based servers without code changes via custom handlers ("lift and shift" with `host.json` configuration)
- **Flex Consumption plan** — serverless scale with pay-for-what-you-use billing
- **Built-in security** — On-Behalf-Of (OBO) authentication, Streamable HTTP transport

The self-hosted option is particularly useful for teams with existing MCP servers who want Azure's scaling and security without rewriting their server code. See our [serverless deployment guide](/guides/mcp-serverless-deployment/) for detailed patterns.

### GitHub Copilot MCP Integration

MCP support went GA in VS Code 1.102 (July 2025) and has since expanded across the GitHub ecosystem:

- **Built-in sandboxing** — MCP servers run in isolated environments
- **OAuth authentication** — secure connection to remote MCP servers
- **Settings Sync** — MCP server configurations sync across devices
- **GitHub MCP Server** — built into Copilot CLI, available to all GitHub users regardless of plan, no configuration needed
- **GitHub MCP Registry** — curated list of easily addable MCP servers
- **Cross-IDE support** — works across VS Code, JetBrains, Xcode, Visual Studio 2026
- **Enterprise controls** — "MCP servers in Copilot" policy for Business/Enterprise plans

For more on MCP integration across coding tools, see our [AI coding tools guide](/guides/mcp-setup-ai-coding-tools/).

### Semantic Kernel

Microsoft's [Semantic Kernel](/guides/mcp-ai-frameworks-langchain-langgraph-crewai/) provides first-class MCP support as both host (client) and server:

- Requires Semantic Kernel Python v1.28.1+
- Supports stdio, SSE, and containerized MCP servers
- Multi-language: C#, Python, Java
- Part of the Microsoft Agent Framework (combining Semantic Kernel + AutoGen)

### Visual Studio 2026

The latest Visual Studio ships with Azure MCP Server built-in out-of-the-box (GA):

- **Azure Skills Plugin** — bundles Azure skills, Azure MCP Server, and Foundry MCP Server in a single install
- **Transport options** — stdio, SSE, Streamable HTTP

### Microsoft 365 Copilot and Copilot Studio

MCP support in declarative agents reached public preview at Ignite 2025:

- Integrates with 1,400+ systems via MCP, Power Platform connectors, and Microsoft Graph
- Custom MCP servers planned for 2026 Wave 1 — reusable, governed MCP servers combining connector actions, tools from other MCP servers, and custom APIs
- Model choice across GPT-5 and third-party models

## Cloudflare: MCP at the Edge

Cloudflare has positioned Workers as the fastest and most cost-effective way to deploy MCP servers, combining edge computing with Zero Trust security.

### Workers as MCP Server Host

[Cloudflare Workers](https://developers.cloudflare.com/agents/guides/remote-mcp-server/) run MCP servers across 300+ edge locations worldwide:

- **Free tier** — 100K requests/day, making it the most accessible MCP hosting option
- **Edge deployment** — sub-100ms latency for users near any Cloudflare PoP
- **OAuth support** — built-in authentication for MCP servers
- **Auto-scaling** — no infrastructure management

### 13 Official MCP Servers

Cloudflare launched 13 official MCP servers in May 2025:

- **Documentation** — Cloudflare docs and best practices
- **Workers Bindings** — KV, R2, D1, Durable Objects management
- **AI Gateway** — AI request routing and caching
- **AutoRAG** — retrieval-augmented generation
- **Audit Logs** — security and compliance logging
- **Workers Observability** — monitoring and debugging
- **Radar** — internet traffic data and trends
- **Turnstile** — CAPTCHA and bot management
- **CASB** — Cloud Access Security Broker
- **Cloudflare API** — 2,500+ endpoints across DNS, Workers, R2, Zero Trust

### MCP Server Portals

The most distinctive feature of Cloudflare's MCP offering is MCP Server Portals (open beta for all Cloudflare One customers):

- **Centralized gateway** — a single HTTP endpoint aggregating multiple MCP servers
- **OAuth + Cloudflare Access authentication** — identity and device posture verification for every request
- **Per-request logging** — full audit trail of all MCP interactions
- **Admin-curated tools** — administrators select which tools and prompt templates are available per portal
- **Zero Trust integration** — Cloudflare Access verifies both identity and device posture

This portal model effectively implements the [enterprise MCP gateway pattern](/guides/mcp-gateway-proxy-patterns/) as a managed service, avoiding the need for teams to build and maintain their own gateway infrastructure.

**Upcoming features** include blocking non-portal MCP servers, prompt-injection screening, one-click deployment templates, and ML-based anomaly detection.

## Vercel: Developer-Focused MCP Hosting

Vercel offers MCP server hosting optimized for the JavaScript/TypeScript ecosystem:

- **Fluid Compute** — reduces serverless cold starts by reusing function instances, important for MCP's connection-oriented model
- **Vercel MCP Server** — a public endpoint at `https://mcp.vercel.com` for connecting your Vercel account to AI clients (read-only data access)
- **AI SDK 6** — full MCP support with agents, tool execution approval, DevTools, and reranking
- **OAuth authentication** — HTTP + OAuth transport (upgraded from SSE)

## DigitalOcean: Developer-Friendly Cloud MCP

DigitalOcean launched its [MCP Server](https://github.com/digitalocean/digitalocean-mcp) publicly in April 2026, covering 9 services with both local and remote MCP endpoints — making it the most comprehensive MCP integration from a mid-tier cloud provider.

### Supported Services

The DigitalOcean MCP Server covers: **Accounts**, **App Platform**, **Databases**, **DOKS** (managed Kubernetes), **Droplets**, **Insights**, **Marketplace**, **Networking**, and **Spaces Storage**. Each service is available as its own remote MCP endpoint at a dedicated HTTPS URL, so you can connect only the services you need.

### Remote MCP (No Local Install)

DigitalOcean offers remote MCP endpoints for all 9 services — connect your AI tools to DigitalOcean without installing any binaries locally. Each service runs as its own MCP server at a dedicated HTTPS endpoint, using OAuth for authentication.

### Local MCP Server

The local option runs as a Go binary connecting to 9 services via bearer token authentication. Typical operations include deploying apps from GitHub repos, provisioning databases, managing Droplets, and querying Kubernetes clusters — all through natural language.

### Where DigitalOcean fits

DigitalOcean's MCP server targets developers and small-to-mid-sized teams who use DigitalOcean as their primary cloud. It lacks the enterprise governance features of AWS (IAM session isolation, CloudTrail), Azure (Entra ID, Conditional Access), or Cloudflare (Zero Trust), but offers a simpler setup path with less configuration overhead. The remote MCP option is particularly useful for quick integration without managing local infrastructure.

## Cloud-Native Authentication for MCP

The [MCP authorization specification](/guides/mcp-authorization-oauth/) finalized June 2025 is based on OAuth 2.1, with MCP servers classified as OAuth Resource Servers. Each cloud provider implements this differently:

| Provider | Auth Mechanism | Key Features |
|---|---|---|
| **AWS** | IAM roles + CloudTrail | Zero credential exposure, session-level isolation |
| **Google Cloud** | Cloud IAM | Organization/folder/project-level controls, MCP auth compliance |
| **Azure** | Entra ID + RBAC | Scoped tokens, Conditional Access, On-Behalf-Of (OBO) |
| **Cloudflare** | Zero Trust + OAuth | Device posture verification, per-request logging |

### The Credential Gap

Despite the OAuth 2.1 specification, research shows that 88% of MCP servers require credentials but 53% still rely on insecure long-lived static secrets — only 8.5% implement OAuth. Cloud-native authentication helps close this gap:

- **Workload Identity Federation** — AWS IAM roles, GCP Workload Identity Federation, and Azure Managed Identities avoid static secrets entirely
- **Just-in-time credentials** — enterprise MCP gateways issue short-lived tokens scoped to specific operations
- **Audit trails** — CloudTrail (AWS), Cloud Audit Logs (GCP), and Azure Activity Log provide compliance-ready logging

For a deeper dive into MCP credential management, see our [credential and secret management guide](/guides/mcp-credential-secret-management/).

## Enterprise MCP Gateways

As MCP deployments scale, organizations are adopting gateway patterns — session-aware reverse proxies fronting multiple MCP servers behind a single endpoint:

**Cloud-native gateways:**
- **Amazon Bedrock AgentCore** — built-in gateway with IAM permissions and CloudTrail logging
- **Cloudflare MCP Server Portals** — managed gateway with Zero Trust integration
- **Google Cloud API Registry** — centralized management with Apigee integration

**Third-party gateways:**
- **Lasso MCP Gateway** (open-source, April 2025) — standalone gateway with policy enforcement
- **Traefik Hub** — Triple Gate Pattern for routing and security

Gateway features typically include OAuth 2.1/SAML SSO/OIDC authentication, per-client consent enforcement, centralized policy management, and comprehensive audit logging. For architectural patterns, see our [gateway and proxy patterns guide](/guides/mcp-gateway-proxy-patterns/).

## Multi-Cloud MCP Architectures

Organizations running MCP across multiple clouds typically adopt one of three patterns:

### 1. Distributed Regional Pattern
Deploy MCP servers in each cloud region closest to your data, respecting data residency requirements. Use cloud-native MCP servers (AWS's awslabs servers, Google's managed servers) for cloud-specific operations, with a central registry tracking available servers across environments.

### 2. Gateway Proxy Pattern
A central MCP gateway (Bedrock AgentCore, Cloudflare Portals, or a self-hosted solution) fronts MCP servers across multiple clouds, providing unified authentication, routing, and observability. Agents connect to one endpoint and the gateway handles cross-cloud routing.

### 3. Layered Protocol Pattern
Use MCP for agent-to-tool connections and [A2A](/guides/mcp-vs-a2a-protocol-comparison/) for agent-to-agent communication, with enterprise gateways bridging cloud boundaries at both protocol layers.

## Choosing a Cloud Provider for MCP

The right choice depends on your existing infrastructure and specific requirements:

**Choose AWS if:**
- You're already invested in the AWS ecosystem — the 66+ official MCP servers cover nearly every service
- You need managed MCP hosting with session isolation (Bedrock AgentCore)
- You want the broadest selection of pre-built MCP servers
- Enterprise security (IAM, CloudTrail) is a priority

**Choose Google Cloud if:**
- You want fully managed, zero-setup MCP servers for core services
- You're using Vertex AI Agent Builder or the Agent Development Kit
- You need both MCP (agent-to-tool) and A2A (agent-to-agent) support
- You're building with the Gemini API

**Choose Azure if:**
- You're in a Microsoft-centric enterprise (Entra ID, M365, GitHub)
- You need MCP integrated with existing GitHub Copilot workflows
- You want MCP alongside 1,400+ Power Platform connectors in Foundry
- You're using Semantic Kernel or the Microsoft Agent Framework

**Choose Cloudflare if:**
- You want the lowest-cost MCP hosting (100K requests/day free)
- Edge latency matters — 300+ PoPs worldwide
- You need Zero Trust security with device posture verification
- You want managed MCP gateway (Portals) without building infrastructure

**Choose Vercel if:**
- You're in the JavaScript/TypeScript ecosystem
- You're already using Vercel for deployments
- You want the simplest developer experience for deploying MCP servers

## Security Considerations

Cloud-hosted MCP introduces specific [security considerations](/guides/mcp-server-security/) beyond those of self-hosted deployments:

1. **Shared responsibility** — cloud providers manage infrastructure security, but you're responsible for MCP server logic, tool permissions, and data access controls
2. **Credential management** — prefer cloud-native identity (IAM roles, managed identities, workload identity federation) over static API keys
3. **Network boundaries** — use VPC endpoints (AWS), Private Service Connect (GCP), or Private Link (Azure) for MCP servers that shouldn't be publicly accessible
4. **Audit logging** — enable cloud-native audit trails (CloudTrail, Cloud Audit Logs, Azure Activity Log) for all MCP interactions
5. **Tool poisoning** — research shows [security vulnerabilities](/guides/mcp-attack-vectors-defense/) in 5% of open-source MCP servers; cloud-managed servers undergo provider security review but custom servers need independent validation

## What's Coming

The cloud MCP landscape is evolving rapidly:

- **Stateless MCP** — the specification committee targets June 2026 for making MCP fully stateless, which would simplify serverless hosting significantly
- **Server Cards** — a metadata standard for MCP servers that would enable cloud marketplaces and automated discovery
- **Google Cloud** is expanding managed MCP servers to Cloud Run, Cloud Storage, Looker, Pub/Sub, and more
- **Azure** plans custom MCP servers in Copilot Studio for 2026 Wave 1
- **Cloudflare** is adding prompt-injection screening and ML anomaly detection to MCP Portals
- **[MCP Dev Summit](/guides/mcp-dev-summit-2026-guide/)** — April 2–3, 2026 in New York City brought together cloud providers and the MCP community with 95+ sessions on security, enterprise patterns, and protocol evolution

## Related Guides

- [MCP Server Deployment and Hosting](/guides/mcp-server-deployment-hosting/) — hosting patterns beyond cloud providers
- [MCP Serverless Deployment](/guides/mcp-serverless-deployment/) — deep dive into serverless MCP patterns
- [MCP Gateway and Proxy Patterns](/guides/mcp-gateway-proxy-patterns/) — enterprise gateway architectures
- [MCP Authorization and OAuth](/guides/mcp-authorization-oauth/) — authentication specification details
- [MCP Credential and Secret Management](/guides/mcp-credential-secret-management/) — secure credential handling
- [MCP Enterprise Infrastructure](/guides/mcp-enterprise-infrastructure/) — enterprise deployment patterns
- [MCP and OpenAI Integration](/guides/mcp-openai-integration/) — OpenAI's MCP surfaces
- [MCP and Anthropic Claude Integration](/guides/mcp-anthropic-claude-integration/) — Claude's MCP integration
- [MCP and AI Frameworks](/guides/mcp-ai-frameworks-langchain-langgraph-crewai/) — framework-level MCP support
- [MCP Ecosystem in 2026](/guides/mcp-ecosystem-2026-state-of-the-standard/) — state of the standard
- [MCP vs A2A Protocol Comparison](/guides/mcp-vs-a2a-protocol-comparison/) — MCP and Agent2Agent
