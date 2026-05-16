# AWS MCP Server (GA) — Managed Remote Access to 15,000+ AWS APIs, No Local Install Required

> AWS's managed remote MCP server reached general availability May 6, 2026. Eleven tools give AI agents authenticated access to 15,000+ AWS API operations via IAM, sandboxed Python execution, and documentation search — all cloud-hosted with no local STDIO setup. Free to use; pay only for AWS resources consumed. US East and EU Frankfurt only at launch. Rating 4/5.


**At a glance:** The AWS MCP Server reached general availability on May 6, 2026 — a managed, cloud-hosted MCP server that gives AI agents authenticated access to virtually all of AWS's API surface through eleven tools. Unlike the [awslabs/mcp monorepo's](/reviews/aws-mcp-servers/) 54 separate STDIO-based servers, this is a single remote endpoint: no `uv pip install`, no local daemon, no STDIO subprocess. Authentication is IAM-based (SigV4), every action is logged to CloudTrail, and the server is offered at no additional charge — you pay for the AWS resources your agent creates and nothing more. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

[AWS MCP Server](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) is the managed, cloud-hosted component of the broader **Agent Toolkit for AWS** — AWS's production-ready suite for connecting AI agents to cloud infrastructure. The toolkit also includes agent plugins (aws-core, aws-agents, aws-data-analytics) and 43 skill modules across 13 categories covering Lambda, EventBridge, Kinesis, Step Functions, CDK, and more.

## Background: Two Different AWS MCP Products

If you've read our [existing review of aws-mcp-servers](/reviews/aws-mcp-servers/), you know the awslabs monorepo: 54 active open-source STDIO servers covering S3, DynamoDB, CloudFormation, ECS, and dozens more. Each runs as a local subprocess on your machine.

The new AWS MCP Server (GA) is something architecturally distinct. It was briefly called "AWS MCP (Preview)" in some documentation and was mentioned as a single entry in the awslabs review table. It is now GA and deserves its own treatment:

| | awslabs/mcp monorepo | AWS MCP Server (GA) |
|---|---|---|
| Servers | 54 active (separate) | 1 unified endpoint |
| Deployment | Local STDIO subprocess | Remote cloud-hosted |
| Auth | AWS credentials locally | IAM SigV4 (remote) |
| Audit | Your responsibility | CloudWatch + CloudTrail built in |
| Install | Per-server pip/uvx | Lightweight proxy config |
| API coverage | Service-specific tools | 15,000+ APIs via `call_aws` |
| Claude.ai browser | Not compatible | Compatible |
| Stars | 8,900 | N/A (managed service) |

## The Eleven Tools

AWS MCP Server exposes two categories of tools.

### AWS Knowledge Tools

| Tool | Description |
|------|-------------|
| `aws___retrieve_skill` | Retrieves a full skill module — workflows, best practices, decision frameworks, step-by-step procedures for a specific AWS domain |
| `aws___search_documentation` | Searches all AWS documentation: API references, best practices, service guides, and skills. Can filter to skills-only or mixed results |
| `aws___read_documentation` | Fetches any AWS documentation page and converts it to markdown for consumption by an AI assistant |
| `aws___recommend` | Returns content recommendations for documentation pages based on related topics and commonly viewed content |
| `aws___list_regions` | Returns all AWS region identifiers and names |
| `aws___get_regional_availability` | Checks regional availability for specific services, features, SDK APIs, and CloudFormation resources |

### AWS API Tools

| Tool | Description |
|------|-------------|
| `aws___call_aws` | Executes authenticated AWS API calls. Supports 15,000+ AWS APIs with automatic credential management, proper syntax validation, and error handling |
| `aws___suggest_aws_commands` | Returns descriptions and syntax for relevant AWS APIs — including newly released APIs that may not yet be in the model's training data |
| `aws___run_script` | Executes Python code in a sandboxed environment with AWS API access. Handles listing resources, parallel API calls, multi-step workflows, cross-service checks, and retry logic — without access to your local filesystem or shell |
| `aws___get_presigned_url` | Generates pre-signed Amazon S3 URLs for uploading or downloading files; handles cases where a CLI command would require a local file path |
| `aws___get_tasks` | Polls the status of long-running tasks started by `aws___call_aws` or `aws___run_script` when those return a task ID with working status |

The design philosophy here is clear: **small number of powerful tools, not hundreds of narrow ones**. `aws___call_aws` alone can reach any of AWS's 15,000+ API operations. New APIs launched by AWS are supported within days. `aws___run_script` handles multi-step workflows that would otherwise require the agent to chain dozens of sequential tool calls.

## Authentication and Governance

Authentication is IAM-based using SigV4 signing. A lightweight proxy on the developer's side handles credential passing; documentation retrieval specifically does not require authentication.

Two global IAM condition context keys are automatically attached to all requests that flow through the managed server:

- `aws:ViaAWSMCPService` — set to `true` for any request made through an AWS managed MCP server
- `aws:CalledViaAWSMCP` — contains the service principal of the specific managed MCP server

These context keys can be used in standard IAM policies to grant or deny actions specifically for agent-initiated requests — without writing separate permission sets. Organizations can write policies like "allow EC2 reads via the MCP server but deny EC2 writes" using the same policy language they already use.

All actions are logged to **AWS CloudTrail** automatically and emit metrics via **Amazon CloudWatch**. This is a significant enterprise differentiator versus the STDIO-based monorepo servers, where audit logging is either absent or must be wired up manually.

## Agent Toolkit for AWS

The AWS MCP Server is part of a broader Agent Toolkit launched simultaneously at GA. Key components:

**Plugins** (installable into Claude Code via `/plugin install` or the Claude Marketplace):
- `aws-core` — foundational AWS interaction patterns
- `aws-agents` — agent orchestration and Bedrock AgentCore patterns
- `aws-data-analytics` — analytics workflows: Kinesis, Glue, Athena, Redshift

**Skills** — 43 atomic skill modules across 13 categories using the Open Agent Skills standard for cross-tool compatibility. Categories cover serverless (Lambda, SAM, CDK), containers (ECS, EKS), storage (S3, EFS), databases (RDS, DynamoDB), AI/ML (Bedrock, SageMaker), security (IAM, GuardDuty), and more.

Skills work with `aws___retrieve_skill` and `aws___search_documentation` — the agent searches available skills, retrieves the relevant one, and uses its embedded workflow as a step-by-step guide for complex multi-resource operations.

## Setup and Integration

The AWS MCP Server is a remote endpoint, not a local server. Setup involves:

1. Configuring AWS credentials (existing IAM credentials work)
2. Creating an environment-specific agent IAM role with appropriate permission boundaries
3. Installing the lightweight proxy and pointing your MCP client at the remote endpoint
4. Adding the AWS MCP Server connection to your Claude Code or other MCP client configuration

Claude Code, Cursor, and Kiro CLI are explicitly supported. Because it's remote HTTP rather than STDIO, it also works with **claude.ai browser** — something the awslabs monorepo servers do not support.

## Regional Availability

At GA launch: **US East (N. Virginia)** and **Europe (Frankfurt)** only.

The managed endpoint in your region can make API calls to any AWS region — you're not limited to operating within those two regions, but your MCP traffic itself routes through them. This is relevant for:

- **Data residency compliance** — MCP traffic passes through N. Virginia or Frankfurt depending on your endpoint configuration
- **Latency** — for teams in Asia-Pacific, Latin America, or other regions, the MCP endpoint adds round-trip latency vs a local server
- **Enterprise procurement** — some organizations have hard requirements against traffic traversing specific regions

AWS will presumably expand regional coverage over time, but it's a real limitation at launch.

## Pricing

No additional charge for the AWS MCP Server itself. You pay for:

- AWS resources created or modified by your agent's API calls
- Any applicable data transfer costs from those resources
- CloudWatch metrics storage if you configure extended retention

There is no per-call pricing for the MCP layer. For teams that use AWS heavily, this pricing model is effectively zero marginal cost for the integration layer.

## What's Different vs the Monorepo

Having covered the [awslabs/mcp monorepo](/reviews/aws-mcp-servers/) at length, the clearest comparison points:

**Managed > STDIO for enterprises.** The monorepo servers are excellent but require per-developer installation, local credential management, and produce no centralized audit trail. For regulated industries (finance, healthcare, government), the GA server's CloudTrail integration and IAM context keys are table stakes.

**Single endpoint < 54 specialized servers.** The monorepo's dedicated servers for S3, DynamoDB, CloudFormation, etc. often have deeper service-specific context than `aws___call_aws`. A developer working primarily with Bedrock or CDK may get more targeted help from the corresponding monorepo server. The GA server's breadth is its strength, not its depth.

**`aws___run_script` is genuinely new.** The sandboxed Python execution tool — blocked from local filesystem and shell access — enables multi-step workflows that would otherwise require many sequential tool calls. This capability doesn't exist in the standard monorepo architecture.

**Knowledge + API in one server.** The monorepo's Documentation MCP and Knowledge MCP are separate servers that require separate configuration. The GA server integrates knowledge, skills, and API execution under one connection.

## Limitations

**Two regions only at launch.** US East and EU Frankfurt. Teams in APAC or other regions face added latency and potential data residency concerns.

**IAM risk remains yours.** CloudTrail provides forensics but not prevention. An overly permissive agent role is still an overly permissive agent role. AWS recommends explicit denies, permission boundaries, and SCPs — none of which the MCP server enforces for you.

**Skills may conflict with org policy.** The skill modules suggest architectural patterns (Lambda, CDK, SAM) that may not align with your organization's platform standards. Policy-as-code and human review gates remain the organization's responsibility.

**No monorepo parity.** Some services in the 54-server monorepo (Bedrock Data Automation, CDK, specific analytics tooling) have richer context than the general-purpose `call_aws` tool provides. The GA server doesn't replace the monorepo for teams with specialized workflows.

**Setup complexity for enterprises.** Creating environment-specific agent IAM roles with appropriate naming conventions for CloudTrail readability — before broad adoption — is a non-trivial initial investment.

## Verdict

The AWS MCP Server GA is a mature, production-ready offering. Eleven carefully designed tools cover the full range of AWS interaction: knowledge retrieval, documentation, API execution, sandboxed scripting, and presigned URLs. The IAM integration is deep and standard — not a bolt-on. CloudTrail logging out of the box removes a major objection for enterprise adoption. The no-additional-charge pricing removes another.

The two-region constraint is real. So is the AWS monorepo, which remains the better choice for specialized service workloads. But for teams that want a single MCP connection with enterprise governance, broad API coverage, and zero infrastructure to maintain, this is what AWS managed infrastructure looks like applied to the agent layer.

**Rating: 4/5** — Excellent governance architecture and the most complete single-endpoint AWS MCP offering available. Held back by limited regional availability at GA and service depth that lags the specialized monorepo servers for specific workloads.

---

*The AWS MCP Server is managed and hosted by Amazon Web Services. ChatForest researched this review using public documentation, official AWS blog posts, and third-party coverage. We did not test the service directly.*

