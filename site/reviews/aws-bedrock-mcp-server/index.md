# AWS Bedrock MCP Servers — The Cloud Giant's MCP Arsenal (Refreshed June 2026)

> AWS operates the largest official MCP server collection: 54 open-source servers plus a managed GA remote server, covering databases, compute, security, cost management, and more.


**At a glance:** AWS publishes **54+ open-source MCP servers** (grown to [62 as of this audit](https://awslabs.github.io/mcp/servers)) in [awslabs/mcp](https://github.com/awslabs/mcp) (9,600 stars, Apache 2.0) plus a **GA managed remote MCP server** (AWS MCP Server) — the largest MCP server collection from any single organization. Servers cover databases (DynamoDB, Neptune, Redshift), compute (ECS, EKS, Lambda), security (IAM, Well-Architected), cost management, and more. MCP client support exists in **Kiro IDE** (replacing Amazon Q Developer), the Q Developer CLI, and Bedrock AgentCore. Part of our **[AI Providers MCP category](/categories/ai-providers/)**.

**June 2026 update:** The [**AWS MCP Server reached general availability**](https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/) (May 6, 2026) with major new capabilities: **Agent Skills** replacing Agent SOPs, **sandboxed Python execution** against AWS APIs, IAM context keys for human/agent permission separation, and no additional charge. It is now part of the **Agent Toolkit for AWS** umbrella. [**OpenAI GPT-5.5, GPT-5.4, and Codex moved from limited preview to GA on Bedrock**](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-openai-models-codex-generally-available/) (June 1, 2026) with pricing now matching OpenAI first-party rates. **AgentCore gained Terraform support** via [provider v6.49.0](https://github.com/hashicorp/terraform-provider-aws/releases/tag/v6.49.0) (June 4, 2026), and the Runtime added AG-UI protocol support and bring-your-own filesystem via S3/EFS. **Kiro IDE** added [parallel task execution, Quick Plan mode, and Requirements Analysis](https://kiro.dev/changelog/ide/0-12/) in May (not June as an earlier version of this review stated). Three new CVEs to note.

AWS has taken a **go-wide infrastructure approach** to MCP, treating it as a protocol for connecting AI agents to cloud services. Rather than wrapping a single API, AWS built dozens of purpose-specific servers — each one a gateway to a different AWS service. This reflects AWS's core business: they don't sell models (though Bedrock now hosts models from 15+ providers including OpenAI), they sell the infrastructure those models connect to.

[Amazon Web Services](https://aws.amazon.com/) is the world's largest cloud provider. [**AWS Q1 2026 revenue: $37.6 billion**](https://www.cnbc.com/2026/04/29/aws-earnings-q1-2026.html) (+28% YoY, fastest growth in 15 quarters), with a [**$150 billion annualized run rate**](https://www.digitalcommerce360.com/2026/04/30/amazon-aws-revenue-growth-milestone-q1-fy26/). [Almost **80% of Fortune 100 companies** use Bedrock](https://finance.yahoo.com/technology/ai/articles/amazon-strengthens-bedrock-ecosystem-whats-145700198.html). [Bedrock processed **more tokens in Q1 2026 than all prior years combined**](https://futurumgroup.com/insights/amazon-q1-fy-2026-aws-momentum-builds-as-ai-infrastructure-spend-surges/). AWS is an [**AAIF Platinum member**](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) — joining at the foundation's December 2025 launch alongside Anthropic, Google, Microsoft, OpenAI, Block, Bloomberg, and Cloudflare.

**Architecture note:** AWS's MCP strategy is the most **infrastructure-centric** of any AI provider. Where Anthropic created the protocol, Google published 24+ servers for its cloud, and OpenAI focused on client integration, AWS published the largest server collection covering virtually every major AWS service — and is now adding **managed remote MCP servers** that require zero local setup, turning MCP into the universal agent-to-cloud interface.

## What It Does

### The awslabs/mcp Monorepo (54 Open-Source Servers)

The primary repository at [awslabs/mcp](https://github.com/awslabs/mcp) contained 54 individual MCP servers organized by AWS service as of the last refresh. The April 21, 2026 release removed 12 deprecated server directories and consolidated functionality, reducing the count from the original 68. Since then, several new servers have been added — as of this audit (2026-08-15), [awslabs.github.io/mcp/servers](https://awslabs.github.io/mcp/servers) lists **62 servers** ("Showing 62 of 62 servers"); check that page for the current authoritative list, as the count changes frequently. **Note:** the AWS Cloud Control API (CCAPI) MCP server referenced below has since been [deprecated](https://awslabs.github.io/mcp/servers/ccapi-mcp-server) in favor of the AWS IAC MCP Server.

| Category | Servers |
|----------|---------|
| Databases | DynamoDB, Neptune, DocumentDB, ElastiCache, Redshift, Postgres, S3 Tables, DSQL |
| AI/ML | Bedrock Data Automation, Bedrock Custom Model Import, Bedrock Knowledge Bases, SageMaker AI, Nova Canvas, SageMaker Unified Studio (Spark) |
| Compute & Containers | ECS, EKS, Lambda, Serverless |
| Infrastructure as Code | CDK, CloudFormation, Terraform |
| Security | IAM, Well-Architected Security |
| Observability | CloudWatch, CloudTrail, CloudWatch Synthetics |
| Cost Management | Cost Explorer, Billing & Cost Management, AWS Pricing (now with cost allocation tags, billing view analytics) |
| Developer Tools | AWS Documentation, CodePipeline, CodeBuild |
| Agent Infrastructure | Bedrock AgentCore |
| Networking & Storage | VPC, S3, Cloud Storage, Network |
| Enterprise | AWS Systems Manager for SAP, AWS For SAP Management (NEW April 29, 2026) |
| Infrastructure | AWS Cloud Control API (CCAPI) — natural language CRUDL for 1,200+ resource types via Cloud Control API. **Since [deprecated](https://awslabs.github.io/mcp/servers/ccapi-mcp-server)** in favor of the AWS IAC MCP Server (as of this audit) |
| Agent Infrastructure | Amazon Bedrock AgentCore MCP Server (NEW 2026) |

| Aspect | Detail |
|--------|--------|
| GitHub | [awslabs/mcp](https://github.com/awslabs/mcp) — 9,600 stars, 1,700 forks (as of 2026-08-15) |
| Language | Python |
| License | Apache 2.0 |
| Commits | 1,500+ |
| Releases | 210+ (latest: June 2026) |
| Transport | stdio only (SSE removed May 2025; Streamable HTTP planned) |
| Installation | `uvx` with one-click install for Kiro, Cursor, VS Code |

### AWS MCP Server (GA) — Managed Remote

The [AWS MCP Server](https://docs.aws.amazon.com/aws-mcp/latest/userguide/what-is-mcp-server.html) **reached general availability on May 6, 2026** — graduating from preview with major new capabilities. It is now part of the **Agent Toolkit for AWS**, a suite that includes the MCP Server, skills, and plugins to help coding agents work more effectively on AWS:

- **15,000+ AWS APIs** — any API through a single tool, including operations requiring file uploads and long-running execution
- **Real-time AWS documentation** — docs, API references, What's New posts, Getting Started guides, Builder Center, blogs, architectural references, Well-Architected guidance; **documentation retrieval no longer requires authentication**
- **Agent Skills** (replaced Agent SOPs) — curated guidance loaded on demand, keeping context window usage low; contributed and maintained by AWS service teams; **reduces hallucination and keeps agents focused**
- **Sandboxed script execution** — agents run Python code against AWS services for multi-step operations, without access to your local filesystem or shell tools
- **IAM context keys** — fine-grained permission separation between human and agent calls; restrict agent to read-only while human retains mutating operations
- **CloudWatch metrics** under the AWS-MCP namespace — observe MCP server calls separately from direct human calls for compliance audit trails
- **Zero local setup** — connects over HTTPS from any MCP-compatible client
- **No additional charge** — pay only for the AWS resources your agents use
- **Available in** Northern Virginia and Frankfurt at GA launch

This is AWS's answer to the "stdio only" limitation of the open-source servers — a remote, managed alternative that requires no local Python environment or uvx installation.

### Additional Official Repositories

| Repository | Stars | Description |
|-----------|-------|-------------|
| [aws/mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws) | 339 | AWS MCP Proxy Server with SigV4 authentication |
| [awslabs/run-model-context-protocol-servers-with-aws-lambda](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda) | 378 | Run stdio MCP servers as Lambda functions |
| [aws-samples/sample-serverless-mcp-servers](https://github.com/aws-samples/sample-serverless-mcp-servers) | 243 | Sample MCP servers on AWS Serverless compute |
| [aws-samples/aws-mcp-servers-samples](https://github.com/aws-samples/aws-mcp-servers-samples) | 189 | Additional AWS MCP server samples — **now archived** (read-only) |
| [awslabs/Log-Analyzer-with-MCP](https://github.com/awslabs/Log-Analyzer-with-MCP) | 167 | Log analysis via MCP |
| [aws-solutions-library-samples/guidance-for-deploying-model-context-protocol-servers-on-aws](https://github.com/aws-solutions-library-samples/guidance-for-deploying-model-context-protocol-servers-on-aws) | 153 | Deployment guidance for MCP on AWS infrastructure |

### MCP Client Support

AWS offers MCP client support across multiple products:

| Product | MCP Support | Detail |
|---------|------------|--------|
| **Kiro IDE** | Yes | AWS's agentic IDE replacing Q Developer IDE plugins. Native MCP support including remote servers. Specs, hooks, steering files, custom subagents. [**GA November 2025.**](https://siliconangle.com/2025/11/17/aws-launches-kiro-general-availability-team-features-cli-support/) [May 2026](https://kiro.dev/changelog/ide/0-12/): parallel task execution (up to 4x faster), Quick Plan mode (single-pass spec generation), Requirements Analysis (automated reasoning to catch logical gaps). [Claude Opus 4.8 added experimentally](https://kiro.dev/changelog/models/claude-opus-4-8-now-available/) (1M context), May 29, 2026. |
| Amazon Q Developer CLI | Yes (since April 2025) | stdio and HTTP MCP server support. Progressive server loading — tools become available as servers initialize |
| Amazon Q Developer IDE | **Sunsetting** | End of support April 30, 2027. New signups end May 15, 2026. Users should migrate to Kiro |
| Bedrock Agents | Yes | Native MCP server invocation via AgentCore |
| AgentCore Gateway | Yes | Server-side tool execution — Bedrock auto-discovers tools, presents to model, executes server-side in a single API call (February 2026) |
| AgentCore Runtime | Yes (March 2026) | Stateful MCP sessions in dedicated microVMs, elicitation, sampling, progress notifications |

**Amazon Q Developer → Kiro (ongoing migration).** AWS announced that Q Developer IDE plugins and paid subscriptions reach [end of support on April 30, 2027](https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/), with new signups ending May 15, 2026. The replacement is **[Kiro](https://kiro.dev/)** — an agentic IDE built for spec-driven development with native MCP support, hooks (automated triggers on file save/commit), steering files (persistent project context), and custom subagents. Kiro reached GA in November 2025 and added a Kiro CLI at GA. Q Developer in the AWS Management Console and first-party AWS experiences are not affected.

### Bedrock AgentCore

AgentCore is AWS's platform for deploying and managing AI agents with native MCP support. Several components reached GA in spring 2026:

- **AgentCore Gateway** — centralized MCP tool server; agents discover and invoke MCP tools through a unified interface. **Server-side tool execution** (February 2026) eliminates client-side tool orchestration loops
- **AgentCore Runtime** — GA October 2025. Deploys MCP servers in managed infrastructure with stateful session support (dedicated microVMs). Available across [15 AWS regions](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-four-additional-regions/). **March 2026**: added AG-UI protocol support. **May 2026**: bring-your-own file system via Amazon S3 Files and Amazon EFS
- **AgentCore Policy** — GA March 3, 2026. Security controls defining agent action boundaries; verification happens outside the agent's reasoning loop before reaching tools or data
- **AgentCore Evaluations** — GA March 31, 2026. Automated quality evaluations for deployed agents based on real-world behavior
- **AgentCore CLI** — launched April 2026. Terraform resources for AgentCore (`aws_bedrockagentcore_gateway` and related) have existed in the AWS provider since mid-2025; [**provider v6.49.0**](https://github.com/hashicorp/terraform-provider-aws/releases/tag/v6.49.0) (June 4, 2026) extended the `aws_bedrockagentcore_gateway` resource with new MCP session/streaming configuration blocks, alongside existing CDK support. Available in 15 regions at no additional charge
- Supports elicitation, sampling, and progress notifications for stateful MCP sessions

## Community Servers

| Repository | Stars | Language | License | Description |
|-----------|-------|----------|---------|-------------|
| [RafalWilinski/aws-mcp](https://github.com/RafalWilinski/aws-mcp) | 297 | TypeScript | — | "Talk with your AWS using Claude" — general AWS MCP server |
| [alexei-led/aws-mcp-server](https://github.com/alexei-led/aws-mcp-server) | 182 | Python | MIT | AWS CLI commands in a safe containerized environment via MCP |
| [ravikiranvm/aws-finops-mcp-server](https://github.com/ravikiranvm/aws-finops-mcp-server) | 176 | Python | MIT | AWS FinOps cost analysis via MCP |
| [rishikavikondala/mcp-server-aws](https://github.com/rishikavikondala/mcp-server-aws) | 128 | Python | MIT | General-purpose AWS MCP server |
| [aarora79/aws-cost-explorer-mcp-server](https://github.com/aarora79/aws-cost-explorer-mcp-server) | 127 | Python | MIT | AWS Cost Explorer data via MCP |
| [groovyBugify/aws-security-mcp](https://github.com/groovyBugify/aws-security-mcp) | 81 | Python | Apache 2.0 | AWS security analysis via MCP |
| [zxkane/mcp-server-amazon-bedrock](https://github.com/zxkane/mcp-server-amazon-bedrock) | 23 | JavaScript | MIT | Amazon Bedrock Nova Canvas image generation |

Total GitHub search results for "aws mcp server": **714 repositories** — the largest community ecosystem of any cloud provider.

## Bedrock Model Pricing

AWS Bedrock hosts models from 15+ providers — and now **OpenAI** (limited preview, April 28, 2026). On-demand pricing per 1 million tokens:

### Amazon Nova (AWS First-Party)

| Model | Input | Output |
|-------|-------|--------|
| Nova Pro | $0.80 | $3.20 |
| Nova Lite | $0.06 | $0.24 |
| Nova Micro | $0.035 | $0.14 |

### OpenAI (on Bedrock — GA June 1, 2026)

| Model | Input | Output |
|-------|-------|--------|
| GPT-5.5 | Matches OpenAI pricing | Matches OpenAI pricing |
| GPT-5.4 | Matches OpenAI pricing | Matches OpenAI pricing |

**Also available:** Codex (via Codex App, Codex CLI, and IDE integrations with VS Code, JetBrains, Xcode). OpenAI models on Bedrock inherit IAM, PrivateLink, guardrails, encryption, and CloudTrail logging. Launched in limited preview April 28, 2026 ([one day after Microsoft's exclusivity ended](https://www.forbes.com/sites/aliciapark/2026/04/27/openai-and-microsoft-end-exclusive-partnership-and-revenue-sharing/)); **moved to GA June 1, 2026**. Pricing matches OpenAI first-party rates and usage counts toward existing AWS commitments. GPT-5.5 and GPT-5.4 support the Responses API on Bedrock; console support coming. GPT-5.4 now available in AWS GovCloud (US-West).

### Anthropic Claude (on Bedrock)

| Model | Input | Output |
|-------|-------|--------|
| Claude Opus 4.6 | $5.00 | $25.00 |
| Claude Sonnet 4.6 | $3.00 | $15.00 |
| Claude Haiku 4.5 | $1.00 | $5.00 |

### Meta Llama (on Bedrock)

| Model | Input | Output |
|-------|-------|--------|
| Llama 3.1 405B | $5.32 | $16.00 |
| Llama 3.1 70B | $2.65 | $3.50 |
| Llama 3.1 8B | $0.30 | $0.60 |

### Other Providers (on Bedrock)

| Model | Input | Output |
|-------|-------|--------|
| Mistral Large 3 | TBD | TBD |
| Mistral Large | $4.00 | $12.00 |
| Cohere Command R+ | $2.50 | $10.00 |
| DeepSeek v3.2 | $0.62 | $1.85 |
| Gemma 3 27B | $0.23 | $0.38 |
| MiniMax M2 | $0.30 | $1.20 |

**Batch inference** offers 50% discount vs on-demand. Nearly **100 serverless models** available plus **100+ via Bedrock Marketplace**.

### Bedrock Key Features

| Feature | Description |
|---------|-------------|
| Bedrock Agents | Autonomous agents that perceive, reason, and act |
| Knowledge Bases | Fully managed RAG with source attribution |
| Guardrails | Block up to 88% harmful content, 99% accuracy on hallucination detection via Automated Reasoning |
| Model Evaluation | Compare and evaluate models |
| Fine-tuning | Customize models with your data |
| AgentCore | Deploy and manage agents with native MCP support |

## AI Provider MCP Comparison

| Feature | AWS | Anthropic | Google | OpenAI | Meta/Llama | Hugging Face | Mistral |
|---------|-----|-----------|--------|--------|------------|-------------|---------|
| Official MCP servers | Yes (54+ open-source + managed remote, 9.6K stars) | No (reference servers) | Yes (24+ servers, 3.4K stars) | No | No | Yes (210 stars) | No |
| Server approach | Infrastructure-wide monorepo + managed remote servers | Reference implementations | Managed remote + open-source | Client only | Client only (Llama Stack) | Hub access + Gradio Spaces | Client only |
| MCP client | Yes (Kiro IDE, Q Developer CLI, AgentCore) | Yes (all Claude products) | Yes (Gemini CLI, SDKs) | Yes (ChatGPT, Agents SDK) | Yes (Llama Stack) | No | Yes (Le Chat, Agents API) |
| AAIF member | Yes (Platinum) | Yes (Platinum, co-founder) | Yes (Platinum) | Yes (Platinum, co-founder) | No | No | Yes (Silver) |
| Unique strength | Most servers (54+), managed remote, cloud integration | Created the protocol | Second most servers (24+) | 900M+ weekly users, now on Bedrock too | Fully free models | 1M+ models, Gradio-as-MCP | Open-weight + EU sovereignty |
| Own models | Yes (Nova family) | Yes (Claude family) | Yes (Gemini family) | Yes (GPT/o-series) | Yes (Llama family) | Platform (hosts all) | Yes (Mistral family) |
| Free tier | Yes (AWS Free Tier) | Yes (limited Claude) | Yes (Flash models) | Yes (limited ChatGPT) | Yes (all models free) | Yes (full Hub access) | Yes (Le Chat Free) |

## Known Issues

1. **Open-source server count reduced 68→54, since grown to 62** — The April 21 release removed 12 deprecated server directories. While this is good housekeeping, it means some servers that existed at initial review no longer have standalone directories. The AWS MCP Server (now GA) consolidates some of this functionality.

2. **stdio only (open-source servers)** — SSE transport was removed in May 2025, and Streamable HTTP is not yet available for open-source servers. The managed AWS MCP Server (GA) communicates over HTTPS, partially addressing this limitation.

3. **OpenAPI MCP Server fixed** — Issue [#2533](https://github.com/awslabs/mcp/issues/2533) from our initial review has been resolved: the April 21 release migrated the OpenAPI MCP server to FastMCP 3.x.

4. **URL allowlist bypass vulnerability** — Patched in the April 30 release. Security-relevant fix indicating active security maintenance.

5. **Q Developer IDE sunsetting** — Amazon Q Developer IDE plugins reach end of support April 30, 2027. Users must migrate to Kiro. This transition may cause friction for teams already integrated with Q Developer MCP workflows.

6. **Cloud billing required** — Most servers interact with AWS services that require an active AWS account with billing. Unlike Google's free API tier or Meta's free models, there's no zero-cost path for most MCP server usage.

7. **No Bedrock API wrapper** — While AWS publishes servers for AWS *services*, there's no official MCP server that wraps the Bedrock API itself for model inference. Developers wanting to call Bedrock models via MCP need community solutions.

8. [**CVE-2026-4270: File access restriction bypass**](https://aws.amazon.com/security/security-bulletins/2026-007-AWS/) — Improper protection in the no-access and workdir feature of AWS API MCP Server (versions >= 0.2.14, < 1.3.9) allowed bypass of intended file access restrictions and exposure of arbitrary local file contents. Patched in v1.3.9.

9. [**CVE-2026-5058**](https://www.sentinelone.com/vulnerability-database/cve-2026-5058/) ([NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-5058)) and [**CVE-2026-5059: Critical RCE in community aws-mcp-server**](https://www.sentinelone.com/vulnerability-database/cve-2026-5059/) ([NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-5059)) — Two critical command injection vulnerabilities (CVSS 9.8) disclosed April 11, 2026 in community aws-mcp-server packages allow remote code execution without authentication. These affect community-maintained packages, not the official awslabs/mcp monorepo. If you use third-party AWS MCP server packages, verify they are not affected.

10. **AgentCore maturing rapidly** — The platform continues to evolve. AgentCore CLI now supports both CDK and Terraform (June 4, 2026). Runtime added AG-UI protocol and bring-your-own filesystem. The overall pattern is rapid iteration, so check release notes before upgrading.

10. **Monorepo complexity** — 54 servers in one repository means navigating a large codebase. Individual servers vary in maturity, documentation quality, and maintenance frequency.

## Bottom Line

**Rating: 4.5 out of 5** (holds from initial review)

AWS continues to operate the **most extensive MCP server infrastructure** of any company. The shift from 68 to 54 (now 62) open-source servers is actually a positive — removing deprecated directories and consolidating into managed remote servers shows maturation, not retreat. The **AWS MCP Server (GA)** with 15,000+ API access and Agent Skills represents the industry's most comprehensive managed MCP offering.

**What changed since May 2026:**

- **AWS MCP Server → GA** (May 6, 2026): Agent Skills replace Agent SOPs, sandboxed Python execution, IAM context keys, now part of Agent Toolkit for AWS; available in N. Virginia + Frankfurt; no additional charge
- **OpenAI on Bedrock → GA** (June 1, 2026): GPT-5.5, GPT-5.4, Codex move from limited preview to production; pricing matches OpenAI first-party rates; GovCloud availability added
- **AgentCore Terraform**: [Provider v6.49.0](https://github.com/hashicorp/terraform-provider-aws/releases/tag/v6.49.0) (June 4, 2026) extends the existing `aws_bedrockagentcore_gateway` resource with MCP session/streaming config blocks
- **AgentCore Runtime updates**: AG-UI protocol support (March 2026); bring-your-own filesystem via S3 Files and EFS (May 2026)
- **Kiro IDE updates** ([May 2026](https://kiro.dev/changelog/ide/0-12/), not June as an earlier version of this review stated): Parallel task execution (up to 4x faster), Quick Plan mode, Requirements Analysis, [Claude Opus 4.8 experimental](https://kiro.dev/changelog/models/claude-opus-4-8-now-available/) (May 29)
- **Security**: CVE-2026-4270 patched (file access bypass in AWS API MCP Server); CVE-2026-5058/5059 critical RCE in community aws-mcp-server packages (CVSS 9.8)
- **Cloud Control API MCP Server**: Server managing 1,200+ AWS resources through natural language via Cloud Control API — **since deprecated** in favor of the AWS IAC MCP Server (noted as of this audit)

**Prior changes (March → May 2026):**
- Cleaned house: 12 deprecated servers removed (68→54), Core MCP deprecated, OpenAPI server fixed
- OpenAI arrived on Bedrock (limited preview, April 28)
- Q Developer → Kiro announced; IDE plugins sunset by April 2027
- AgentCore: Policy GA (March 3), Evaluations GA (March 31), CLI launched (April), server-side tool execution (February)
- URL allowlist bypass patched; [170% Bedrock spending growth QoQ](https://finance.yahoo.com/technology/ai/articles/amazon-strengthens-bedrock-ecosystem-whats-145700198.html)

**Why rating holds 4.5/5:** The managed server reaching GA and OpenAI models moving to production are meaningful positive milestones. The new CVEs in community packages are a warning, and the open-source/managed transition is still ongoing. The Q Developer sunset transition continues to carry friction risk. The overall trajectory is the strongest of any cloud provider — AWS is investing more in MCP infrastructure than anyone else — but the platform is in continuous transition and that carries inherent risk.

**Who benefits most from AWS's MCP ecosystem:**

- **AWS-native teams** — 54 open-source servers plus managed remote servers give AI agents direct access to virtually every AWS service
- **Enterprise architects** — AgentCore with Policy GA, Evaluations GA, and server-side tool execution provides the most mature managed MCP infrastructure available
- **Agent builders** — Kiro IDE with native MCP, combined with Bedrock's growing model catalog (now including OpenAI), creates a complete agent development stack

**Who should be cautious:**

- **Q Developer IDE users** — Start planning migration to Kiro now; IDE plugins sunset April 2027, new signups end May 15, 2026
- **Multi-cloud teams** — These servers are AWS-specific; there's no abstraction layer for Azure or GCP equivalents
- **Cost-sensitive experiments** — Unlike Meta's free models or Google's free API tier, most AWS MCP servers require active AWS billing
- **Teams wanting model-level MCP access** — Still no official Bedrock inference MCP server

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official AWS announcements. Information is current as of June 2026. See our [About page](/about/) for details on our review process.*

**Refresh history:** Initial review March 2026 · Refreshed May 2026 · Refreshed June 2026

