# AWS Bedrock MCP Servers — The Cloud Giant's MCP Arsenal (Refreshed May 2026)

> AWS operates the largest official MCP server collection: 54 open-source servers plus managed remote servers, covering databases, compute, security, cost management, and more.


**At a glance:** AWS publishes **54 open-source MCP servers** in [awslabs/mcp](https://github.com/awslabs/mcp) (8,900 stars, Apache 2.0) plus **managed remote MCP servers** (AWS MCP Server, EKS, ECS, SageMaker) — the largest MCP server collection from any single organization. Servers cover databases (DynamoDB, Neptune, Redshift), compute (ECS, EKS, Lambda), security (IAM, Well-Architected), cost management, and more. MCP client support exists in **Kiro IDE** (replacing Amazon Q Developer), the Q Developer CLI, and Bedrock AgentCore. Part of our **[AI Providers MCP category](/categories/ai-providers/)**.

**May 2026 update:** Since our initial review, AWS has **cleaned house** — removing 12 deprecated server directories (April 21), deprecating Core MCP Server, and launching the **AWS MCP Server (Preview)**, a managed remote server combining API access to 15,000+ AWS services with documentation and Agent SOPs. **OpenAI models arrived on Bedrock** (April 28) including GPT-5.5 and Codex. **Amazon Q Developer IDE plugins are sunsetting** in favor of **Kiro**, AWS's new agentic IDE with native MCP support. Bedrock spending grew **170% quarter-over-quarter** in Q1 2026.

AWS has taken a **go-wide infrastructure approach** to MCP, treating it as a protocol for connecting AI agents to cloud services. Rather than wrapping a single API, AWS built dozens of purpose-specific servers — each one a gateway to a different AWS service. This reflects AWS's core business: they don't sell models (though Bedrock now hosts models from 15+ providers including OpenAI), they sell the infrastructure those models connect to.

[Amazon Web Services](https://aws.amazon.com/) is the world's largest cloud provider. **AWS Q1 2026 revenue: $37.6 billion** (+28% YoY, fastest growth in 15 quarters), with a **$150 billion annualized run rate**. Almost **80% of Fortune 100 companies** use Bedrock. Bedrock processed **more tokens in Q1 2026 than all prior years combined**. AWS is an **AAIF Platinum member** — joining at the foundation's December 2025 launch alongside Anthropic, Google, Microsoft, OpenAI, Block, Bloomberg, and Cloudflare.

**Architecture note:** AWS's MCP strategy is the most **infrastructure-centric** of any AI provider. Where Anthropic created the protocol, Google published 24+ servers for its cloud, and OpenAI focused on client integration, AWS published the largest server collection covering virtually every major AWS service — and is now adding **managed remote MCP servers** that require zero local setup, turning MCP into the universal agent-to-cloud interface.

## What It Does

### The awslabs/mcp Monorepo (54 Open-Source Servers)

The primary repository at [awslabs/mcp](https://github.com/awslabs/mcp) contains 54 individual MCP servers organized by AWS service. The April 21, 2026 release removed 12 deprecated server directories and consolidated functionality, reducing the count from the original 68.

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

| Aspect | Detail |
|--------|--------|
| GitHub | [awslabs/mcp](https://github.com/awslabs/mcp) — 8,900 stars (+4.2%), 1,500 forks (+8.8%) |
| Language | Python |
| License | Apache 2.0 |
| Commits | ~1,505 (+7.5%) |
| Releases | 200+ (latest: April 30, 2026) |
| Transport | stdio only (SSE removed May 2025; Streamable HTTP planned) |
| Installation | `uvx` with one-click install for Kiro, Cursor, VS Code |

### AWS MCP Server (Preview) — Managed Remote

**NEW since our initial review.** The [AWS MCP Server (Preview)](https://docs.aws.amazon.com/aws-mcp/latest/userguide/what-is-mcp-server.html) is a **managed remote MCP server hosted by AWS** that consolidates capabilities from the AWS API MCP and AWS Knowledge servers into a unified interface:

- **15,000+ AWS APIs** — generate and execute calls including for newly released services
- **Real-time AWS documentation** — docs, API references, What's New posts, Getting Started guides, Builder Center, blogs, architectural references, Well-Architected guidance
- **Agent SOPs** — pre-built workflows that guide AI agents through common AWS tasks following best practices, now with **semantic similarity search** for SOP discovery
- **IAM-based auth** — uses existing AWS IAM roles and policies; full CloudTrail audit logging
- **CloudWatch metrics** — operational metrics published for monitoring (March 2026 enhancement)
- **Zero local setup** — connects over HTTPS from any MCP-compatible client

This is AWS's answer to the "stdio only" limitation of the open-source servers — a remote, managed alternative that requires no local Python environment or uvx installation.

### Additional Official Repositories

| Repository | Stars | Description |
|-----------|-------|-------------|
| [aws/mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws) | 249 | AWS MCP Proxy Server with SigV4 authentication |
| [awslabs/run-model-context-protocol-servers-with-aws-lambda](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda) | 353 | Run stdio MCP servers as Lambda functions |
| [aws-samples/sample-serverless-mcp-servers](https://github.com/aws-samples/sample-serverless-mcp-servers) | 230 | Sample MCP servers on AWS Serverless compute |
| [aws-samples/aws-mcp-servers-samples](https://github.com/aws-samples/aws-mcp-servers-samples) | 191 | Additional AWS MCP server samples |
| [awslabs/Log-Analyzer-with-MCP](https://github.com/awslabs/Log-Analyzer-with-MCP) | 154 | Log analysis via MCP |
| [aws-solutions-library-samples/guidance-for-deploying-model-context-protocol-servers-on-aws](https://github.com/aws-solutions-library-samples/guidance-for-deploying-model-context-protocol-servers-on-aws) | 147 | Deployment guidance for MCP on AWS infrastructure |

### MCP Client Support

AWS offers MCP client support across multiple products:

| Product | MCP Support | Detail |
|---------|------------|--------|
| **Kiro IDE** (NEW) | Yes | AWS's new agentic IDE replacing Q Developer IDE plugins. Native MCP support including remote servers. Specs, hooks, steering files, custom subagents |
| Amazon Q Developer CLI | Yes (since April 2025) | stdio and HTTP MCP server support. Progressive server loading — tools become available as servers initialize |
| Amazon Q Developer IDE | **Sunsetting** | End of support April 30, 2027. New signups end May 15, 2026. Users should migrate to Kiro |
| Bedrock Agents | Yes | Native MCP server invocation via AgentCore |
| AgentCore Gateway | Yes | Server-side tool execution — Bedrock auto-discovers tools, presents to model, executes server-side in a single API call (February 2026) |
| AgentCore Runtime | Yes (March 2026) | Stateful MCP sessions in dedicated microVMs, elicitation, sampling, progress notifications |

**Major shift: Amazon Q Developer → Kiro.** AWS announced that Q Developer IDE plugins and paid subscriptions reach [end of support on April 30, 2027](https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/), with new signups ending May 15, 2026. The replacement is **[Kiro](https://kiro.dev/)** — an agentic IDE built for spec-driven development with native MCP support, hooks (automated triggers on file save/commit), steering files (persistent project context), and custom subagents. Q Developer in the AWS Management Console and first-party AWS experiences are not affected.

### Bedrock AgentCore

AgentCore is AWS's platform for deploying and managing AI agents with native MCP support. Several components reached GA in spring 2026:

- **AgentCore Gateway** — centralized MCP tool server; agents discover and invoke MCP tools through a unified interface. **Server-side tool execution** (February 2026) eliminates client-side tool orchestration loops
- **AgentCore Runtime** — deploys MCP servers in managed infrastructure with stateful session support (dedicated microVMs, announced March 10, 2026). Available across 14 AWS regions
- **AgentCore Policy** — GA March 3, 2026. Quality controls and governance for agent deployments
- **AgentCore Evaluations** — GA March 31, 2026. Automated quality evaluations for deployed agents
- **AgentCore CLI** — launched April 2026. Infrastructure-as-code deployment via AWS CDK (Terraform coming). Available in 14 regions at no additional charge
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

### OpenAI (on Bedrock — NEW, Limited Preview)

| Model | Input | Output |
|-------|-------|--------|
| GPT-5.5 | TBD (preview) | TBD (preview) |
| GPT-5.4 | TBD (preview) | TBD (preview) |

**Also available:** Codex (coding agent) and Bedrock Managed Agents powered by OpenAI. OpenAI models on Bedrock inherit IAM, PrivateLink, guardrails, encryption, and CloudTrail logging. Launched **one day after Microsoft's exclusivity deal ended** (April 28, 2026).

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
| Official MCP servers | Yes (54 open-source + managed remote, 8.9K stars) | No (reference servers) | Yes (24+ servers, 3.4K stars) | No | No | Yes (210 stars) | No |
| Server approach | Infrastructure-wide monorepo + managed remote servers | Reference implementations | Managed remote + open-source | Client only | Client only (Llama Stack) | Hub access + Gradio Spaces | Client only |
| MCP client | Yes (Kiro IDE, Q Developer CLI, AgentCore) | Yes (all Claude products) | Yes (Gemini CLI, SDKs) | Yes (ChatGPT, Agents SDK) | Yes (Llama Stack) | No | Yes (Le Chat, Agents API) |
| AAIF member | Yes (Platinum) | Yes (Platinum, co-founder) | Yes (Platinum) | Yes (Platinum, co-founder) | No | No | Yes (Silver) |
| Unique strength | Most servers (54+), managed remote, cloud integration | Created the protocol | Second most servers (24+) | 900M+ weekly users, now on Bedrock too | Fully free models | 1M+ models, Gradio-as-MCP | Open-weight + EU sovereignty |
| Own models | Yes (Nova family) | Yes (Claude family) | Yes (Gemini family) | Yes (GPT/o-series) | Yes (Llama family) | Platform (hosts all) | Yes (Mistral family) |
| Free tier | Yes (AWS Free Tier) | Yes (limited Claude) | Yes (Flash models) | Yes (limited ChatGPT) | Yes (all models free) | Yes (full Hub access) | Yes (Le Chat Free) |

## Known Issues

1. **Open-source server count reduced 68→54** — The April 21 release removed 12 deprecated server directories. While this is good housekeeping, it means some servers that existed at initial review no longer have standalone directories. The AWS MCP Server (Preview) consolidates some of this functionality.

2. **stdio only (open-source servers)** — SSE transport was removed in May 2025, and Streamable HTTP is not yet available for open-source servers. The managed AWS MCP Server (Preview) communicates over HTTPS, partially addressing this limitation.

3. **OpenAPI MCP Server fixed** — Issue [#2533](https://github.com/awslabs/mcp/issues/2533) from our initial review has been resolved: the April 21 release migrated the OpenAPI MCP server to FastMCP 3.x.

4. **URL allowlist bypass vulnerability** — Patched in the April 30 release. Security-relevant fix indicating active security maintenance.

5. **Q Developer IDE sunsetting** — Amazon Q Developer IDE plugins reach end of support April 30, 2027. Users must migrate to Kiro. This transition may cause friction for teams already integrated with Q Developer MCP workflows.

6. **Cloud billing required** — Most servers interact with AWS services that require an active AWS account with billing. Unlike Google's free API tier or Meta's free models, there's no zero-cost path for most MCP server usage.

7. **No Bedrock API wrapper** — While AWS publishes servers for AWS *services*, there's no official MCP server that wraps the Bedrock API itself for model inference. Developers wanting to call Bedrock models via MCP need community solutions.

8. **AWS MCP Server is Preview** — The managed remote server is not yet GA. Expect rapid changes, limited documentation, and potential breaking changes.

9. **AgentCore maturing rapidly** — AgentCore Policy (GA March 3) and Evaluations (GA March 31) reached general availability, but the overall platform is still evolving. AgentCore CLI launched in April 2026 with CDK support only (Terraform coming).

10. **Monorepo complexity** — 54 servers in one repository means navigating a large codebase. Individual servers vary in maturity, documentation quality, and maintenance frequency.

## Bottom Line

**Rating: 4.5 out of 5** (holds from initial review)

AWS continues to operate the **most extensive MCP server infrastructure** of any company. The shift from 68 to 54 open-source servers is actually a positive — removing deprecated directories and consolidating into managed remote servers shows maturation, not retreat. The **AWS MCP Server (Preview)** with 15,000+ API access and Agent SOPs represents the industry's most comprehensive managed MCP offering.

**What changed since March 2026:**

- **Cleaned house**: 12 deprecated servers removed, Core MCP Server deprecated, OpenAPI server fixed
- **Managed remote MCP**: AWS MCP Server (Preview) with 15,000+ APIs, Agent SOPs, IAM auth, CloudWatch metrics
- **OpenAI on Bedrock**: GPT-5.5, GPT-5.4, Codex, and Managed Agents (limited preview, April 28)
- **Q Developer → Kiro**: IDE plugins sunsetting by April 2027; Kiro is the replacement with native MCP, specs, hooks
- **AgentCore maturing**: Policy GA (March 3), Evaluations GA (March 31), CLI launched (April), server-side tool execution (February)
- **Business momentum**: AWS revenue +28% YoY (15-quarter high), Bedrock spending +170% QoQ, 80% Fortune 100 on Bedrock
- **Security**: URL allowlist bypass patched, injection filter hardening, DSQL safe_query

**Why rating holds 4.5/5:** The positives (managed remote servers, OpenAI models, AgentCore maturation, 170% Bedrock growth) are offset by the Q Developer sunset transition risk, AWS MCP Server still in preview, continued lack of Bedrock inference wrapper, and cloud billing requirement. The overall trajectory is clearly positive — AWS is investing more heavily in MCP infrastructure than any other company — but the platform is in transition (Q Developer → Kiro, open-source → managed remote) and transitions carry risk.

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

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official AWS announcements. Information is current as of May 2026. See our [About page](/about/) for details on our review process.*

