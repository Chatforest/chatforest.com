# Chaos Engineering MCP Servers — LitmusChaos, Chaos Mesh, Gremlin, Steadybit, Harness, and More

> Chaos engineering MCP servers let AI agents manage fault injection experiments, monitor resilience, and track chaos results through natural language.


Chaos engineering — the practice of deliberately injecting faults to find weaknesses before they become outages — is a natural fit for MCP integration. AI agents that can discover, execute, and analyze chaos experiments through natural language lower the barrier to entry for teams that know they should be testing resilience but find the YAML-heavy workflows intimidating. The category spans three areas: **CNCF platforms** (LitmusChaos, Chaos Mesh), **commercial reliability platforms** (Gremlin, Steadybit, Harness), and **cloud-native fault injection** (AWS FIS).

The headline finding: **LitmusChaos has the strongest official MCP server** with 17 tools covering experiment management, infrastructure monitoring, environment organization, resilience probes, ChaosHub integration, and analytics — the full chaos experiment lifecycle in one server, though development has stalled since November 2025. **Chaos Mesh MCP has the deepest fault injection coverage** with 33 tools across 7 chaos types (network, stress, pod, IO, HTTP, DNS, physical machine), but it's a community project with minimal adoption. **Harness is the breakout performer** — growing from 30 to 50 stars with 461 commits, now using a registry-based architecture that dispatches 10 consolidated tools to 139 resource types across 30 toolsets. **Gremlin has expanded beyond read-only** with reliability test execution capabilities added in early 2026. The main gap is still in **direct fault execution** — most servers either manage experiments or report on results, but few give the AI agent a "break this now" button with proper safety controls.

**Category:** [Cloud & Infrastructure](/categories/cloud-infrastructure/)

## CNCF Platforms

### LitmusChaos

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [litmuschaos/litmus-mcp-server](https://github.com/litmuschaos/litmus-mcp-server) | 15 | Go | 17 | stdio |

**litmuschaos/litmus-mcp-server** (15 stars, Go, 30 commits) is the official MCP server for LitmusChaos 3.x, the CNCF-incubating chaos engineering platform. Seventeen tools organized into seven categories:

**Experiment management** (4 tools) — `list_chaos_experiments`, `get_chaos_experiment`, `run_chaos_experiment`, `stop_chaos_experiment`. Full lifecycle control: discover available experiments, inspect details, execute on-demand or via cron-like schedules, and stop running experiments with granular control.

**Execution monitoring** (2 tools) — `list_experiment_runs`, `get_experiment_run_details`. Track fault-level success/failure signals, monitor active executions in near real-time, view resiliency score calculations, and retrieve detailed run history with status and duration.

**Infrastructure management** (3 tools) — `list_chaos_infrastructures`, `get_infrastructure_details`, `register_chaos_infrastructure`. Monitor infrastructure heartbeat, last-seen time, and readiness. Generate installation manifests tailored to namespace-scoped or cluster-scoped deployments.

**Environment organization** (2 tools) — `list_environments`, `create_environment`. Create and manage PROD/NON_PROD environments, associate infrastructures with environments, filter experiments by environment context.

**Resilience probes** (2 tools) — `list_resilience_probes`, `create_resilience_probe`. Four built-in probe types: HTTP, Command, Kubernetes, and Prometheus. Plug-and-play architecture for steady-state and post-injection validations.

**ChaosHub integration** (2 tools) — `list_chaos_hubs`, `get_chaos_faults`. Browse chaos faults and documentation, support multiple hubs (Git-backed and remote), categorization and search.

**Analytics** (2 tools) — `get_experiment_statistics`, plus project-wide experiment and infrastructure statistics, resiliency score distributions, and run status breakdowns.

Installation via `go install`, `make build`, or Docker container. Requires Go 1.21+, access to a LitmusChaos 3.x Chaos Center, and valid project credentials with access token. The official documentation at docs.litmuschaos.io includes a dedicated MCP server section. This remains the most complete dedicated chaos engineering MCP server — it covers the full experiment lifecycle from fault discovery through execution tracking and resilience scoring. However, the repository has been dormant since November 2025 with no new commits, which is a concern for long-term maintenance.

### Chaos Mesh

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [ernestolee13/chaos-mesh-mcp](https://github.com/ernestolee13/chaos-mesh-mcp) | 2 | Python | 33 | stdio |

**ernestolee13/chaos-mesh-mcp** (2 stars, Python, MIT, 10 commits, December 2025) is a community MCP server for Chaos Mesh, the CNCF-incubating chaos engineering platform. Thirty-three tools organized across 7 chaos types plus management:

**NetworkChaos** (4 tools) — delay, packet loss, network partition, corruption. Simulate degraded network conditions between services or pods.

**StressChaos** (3 tools) — CPU stress, memory stress, combined stress. Apply resource pressure to containers to test behavior under load.

**PodChaos** (3 tools) — pod kill, pod failure, container kill. The classic chaos engineering primitives — destroy pods and watch recovery.

**IOChaos** (4 tools) — latency injection, fault injection, attribute override, data corruption. Test how applications handle slow, broken, or corrupted file system operations.

**HTTPChaos** (4 tools) — abort, delay, replace, patch. Manipulate HTTP traffic at the connection and content level — simulate API failures, slow responses, or modified payloads.

**DNSChaos** (2 tools) — error injection, random IP responses. Requires chaos-dns-server pod in the cluster.

**PhysicalMachineChaos** (5 tools) — CPU stress, memory stress, disk fill, process kill, clock skew. Extends beyond Kubernetes to bare-metal or VM targets via the Chaosd agent.

**Management & validation** (8 tools) — environment validation (3 tools), plus experiment status, listing, deletion, pause, resume, and event tracking (5 tools).

Requirements: Kubernetes v1.15+ (tested with v1.27.6), Chaos Mesh v2.6+ (tested with v2.8.0), Python 3.10-3.12, kubectl configured. Install via pip from GitHub. Despite the 2-star count, this is the most comprehensive fault injection MCP server available — 33 tools covering every Chaos Mesh chaos type including the less common PhysicalMachineChaos and DNSChaos. The lack of adoption and zero commits since December 2025 are the main concerns. No official Chaos Mesh MCP server exists yet.

## Commercial Platforms

### Gremlin

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [gremlin/mcp](https://github.com/gremlin/mcp) | 6 | TypeScript | 11+ | stdio |

**gremlin/mcp** (6 stars, TypeScript, Apache 2.0, 7 commits) is the official MCP server for Gremlin's Reliability Intelligence platform. The core tool set includes `list_services`, `get_service_dependencies`, `get_reliability_report`, `get_pricing_report`, `get_client_summary`, `get_attack_summary`, `get_recent_reliability_tests`, and `get_current_test_suite`.

**New in early 2026:** Gremlin has expanded beyond purely read-only operations. A February 2026 update added `run_reliability_test` and `get_pending_test_runs` — the first write capabilities, allowing AI agents to trigger reliability test execution. A March 31, 2026 update introduced dynamic API tools with Search and Execute capabilities, using OpenAPI spec tokenization to route queries across endpoints. The same update improved client compatibility with an elicitation handler for clients that don't support the elicitation protocol.

Key use cases: identify services that need testing, discover uncovered critical dependencies, detect gaps in test coverage, generate reliability reports, and now trigger reliability tests. RBAC scoping via API keys adds access control. Containerized isolation for security.

Requires Node.js 22+, npm, and a Gremlin account with REST API key. Part of Gremlin's broader Reliability Intelligence launch. The evolution from read-only to including test execution marks a significant shift — Gremlin is cautiously enabling AI-driven chaos while maintaining safety through its platform's existing guardrails.

### Steadybit

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [steadybit/mcp](https://github.com/steadybit/mcp) | 0 | Java | 11 | stdio |

**steadybit/mcp** (0 stars, Java, MIT, 71 commits, 22 releases) is the official MCP server for Steadybit's chaos engineering platform. Eleven tools:

- `list-experiment-designs` / `get_experiment_design` — browse and inspect experiment definitions
- `list_experiment_executions` / `get_experiment_execution` — review execution history and results
- `list_actions` — discover available chaos actions in the platform
- `list_environments` / `list_teams` — organizational context
- `list_experiment_schedules` — view automated experiment schedules
- `list_experiment_templates` / `get_experiment_template` — browse reusable templates
- `create_experiment_from_template` — the only write operation, creating experiments from existing templates

Docker deployment: `docker run -i --rm -e API_TOKEN ghcr.io/steadybit/mcp:latest`. Also supports native image compilation via GraalVM for lower resource usage. Requires API_TOKEN environment variable and optional API_URL configuration. Steadybit positioned this as "the first MCP server for chaos engineering" when they launched it, though LitmusChaos and others were close behind. The template-based experiment creation is a smart safety pattern — the AI agent can create experiments but only from pre-approved templates, not arbitrary fault configurations. With 71 commits and 22 releases, Steadybit has the most consistent release cadence in this category — despite 0 stars, suggesting enterprise-focused adoption that doesn't register on GitHub's social metrics.

### Harness

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [harness/mcp-server](https://github.com/harness/mcp-server) | 50 | Go | 10 (consolidated) | stdio, HTTP |

**harness/mcp-server** (50 stars, Go, 461 commits) is Harness's unified MCP server, now significantly expanded with a **registry-based architecture** that dispatches 10 consolidated tools to 139 resource types across 30 toolsets — chaos engineering is one module alongside pipelines, secrets, security, cost management, and more.

The server has evolved from individual per-resource tools to a dispatch model where tools like `harness_list`, `harness_get`, and `harness_create` route to any resource type. For chaos engineering, this means experiment discovery, execution, result retrieval, and probe management are all available through the consolidated tool interface. The server also includes 27 prompt templates for common workflows and supports multi-project discovery without hardcoded configuration.

Requires Harness Platform access with Chaos Engineering enabled, API key, Organization ID, and Project ID. Go 1.23+ for building from source. Now supports both stdio and HTTP transport, with Docker and Kubernetes deployment options. The 461 commits and +67% star growth (30→50) since March 2026 make Harness the most actively developed chaos-capable MCP server. The value proposition is strongest for teams already using Harness — you get chaos engineering alongside 29 other platform toolsets in one server. For chaos-only use cases, LitmusChaos's dedicated server offers more focused tooling.

## Cloud-Native Fault Injection

### AWS Fault Injection Service

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [RadiumGu/aws-fis-mcp-server](https://github.com/RadiumGu/aws-fis-mcp-server) | 3 | Python | 10 | stdio |

**RadiumGu/aws-fis-mcp-server** (3 stars, Python, MIT, 13 commits, January 2025) enables interaction with AWS Fault Injection Service for managing chaos experiments on AWS workloads. Ten tools split between read-only and write operations:

**Read-only** (6 tools, always available) — `list_experiment_templates`, `get_experiment_template`, `list_experiments`, `get_experiment`, `list_action_types`, `generate_template_example`.

**Write operations** (4 tools, require `--allow-writes` flag) — `start_experiment`, `stop_experiment`, `create_experiment_template`, `delete_experiment_template`.

Read-only mode by default is the right safety choice for a fault injection service. Region support with configurable defaults. Structured error messaging for blocked operations. Requires Python 3.10+, boto3, and AWS credentials with FIS permissions. Community project — no official AWS MCP server for FIS exists, though the awslabs/mcp monorepo (4,700+ stars) covers many AWS services. This fills the FIS gap for teams running chaos experiments on AWS.

## MCP Client & Agent Resilience Testing

Three related projects focus on testing the resilience of AI agents and MCP clients themselves:

**Typewise/mcp-chaos-rig** (10 stars, TypeScript, MIT, 21 commits, v1.5.0 April 2026) is a local MCP server that breaks on demand for testing MCP client implementations. It provides a web UI (localhost:4100/ui) where developers can simulate: **authentication failures** (OAuth 2.1 flow breakdowns, bearer token rejection, token expiry, refresh token issues), **tool instability** (enable/disable tools, schema version switching, `tools/changed` notifications), and **reliability degradation** (random latency injection, configurable failure rates 0–100%). Live request logging with JSON-RPC inspection and SSE response monitoring. This is not traditional chaos engineering — it's fault injection for MCP protocol compliance testing. Created February 2026, actively maintained.

**deepankarm/agent-chaos** (21 stars, Python, Apache 2.0, 57 commits, v0.1.3 January 2026) is a chaos engineering framework for testing AI agent resilience. Instead of breaking infrastructure, it breaks the AI stack itself — injecting LLM failures (rate limits, server errors, timeouts, stream interruptions), tool failures (errors, timeouts, data corruption), and prompt injection attacks. Integrates with DeepEval and Pydantic Evals for semantic evaluation. Randomized chaos combinations via fuzzing. No new commits since January 2026, but still the most complete agent-level chaos framework available.

**Alexey Tyurin's MCP Reliability Playbook** (Google Cloud Community, March 2026) documents chaos testing patterns for MCP-based systems — a reference project demonstrating 9 reliability patterns with automated chaos tests that inject faults and verify graceful degradation. The chaos testing framework is generic enough to work with any MCP-based system, with efforts to extract it into a standalone open-source project.

## What's Missing

The chaos engineering MCP landscape has significant gaps:

- **No ChaosBlade MCP server** — Alibaba's CNCF Sandbox project (6,000+ stars) has no MCP integration
- **No Toxiproxy MCP server** — Shopify's TCP proxy for chaos testing (the most widely adopted tool by repository count) has no MCP server
- **No PowerfulSeal MCP server** — though the project appears dormant since 2021
- **No Netflix Chaos Monkey MCP server** — the tool that started it all has no MCP integration
- **No Chaos Toolkit MCP server** — the open API standard for chaos engineering lacks MCP connectivity
- **No Azure Chaos Studio MCP server** — Microsoft's `azure-mcp` repo was archived August 2025, redirecting to `microsoft/mcp` which covers 40+ Azure services but no Chaos Studio. No GCP equivalent either
- **Limited safety controls** — most servers that allow fault injection don't implement approval workflows, blast radius limits, or automatic rollback through MCP
- **No cross-platform abstraction** — each server is tightly coupled to its platform; no unified chaos engineering MCP interface exists
- **No GameDay orchestration** — no MCP server coordinates multi-team chaos experiments or manages the full GameDay workflow

## The Bottom Line

Chaos engineering MCP servers are maturing unevenly. **LitmusChaos** remains the recommendation for teams wanting the most focused chaos MCP integration — 17 tools covering the full experiment lifecycle — but its dormancy since November 2025 is a concern. **Harness** is the breakout story, growing 67% in stars with 199 new commits and a sophisticated registry-based architecture that makes chaos engineering one of 30 integrated toolsets. **Gremlin** has made the most interesting philosophical shift, expanding beyond read-only with reliability test execution — cautiously enabling AI-driven chaos through its platform's existing safety controls. **Steadybit** keeps shipping (71 commits, 22 releases) despite zero community visibility on GitHub. **Chaos Mesh MCP** still offers the deepest fault injection coverage (33 tools across 7 chaos types) but needs community adoption. **AWS FIS MCP** fills the AWS gap but appears stalled. A new sub-category is emerging around **MCP protocol resilience testing** — mcp-chaos-rig and agent-chaos focus on breaking the AI tooling stack itself rather than infrastructure.

Rating: **3.5 out of 5** — Good platform coverage from CNCF projects and commercial tools, meaningful tool depth in LitmusChaos and Chaos Mesh, and Harness's rapid growth shows commercial momentum. But adoption remains early across the board, dedicated CNCF servers are stalling, and significant gaps persist (ChaosBlade, Toxiproxy, Chaos Monkey, cloud providers). Gremlin's move toward AI-triggered test execution is the most promising directional signal.

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic). We do not have hands-on access to these tools — our analysis is based on public repositories, documentation, and changelogs. Last refreshed 2026-04-25.*

