---
title: "AWS Bedrock MCP Servers — The Cloud Giant's 68-Server MCP Arsenal"
date: 2026-03-23T18:00:00+09:00
description: "AWS has the largest official MCP server collection of any company: 68 servers in a single monorepo covering databases, compute, security, cost management, and more. Plus MCP client support in Amazon Q and Bedrock AgentCore."
og_description: "AWS publishes 68 official MCP servers (8.5K stars), is an AAIF Platinum member, and offers MCP client support in Amazon Q Developer and Bedrock AgentCore. Rating: 4.5/5."
content_type: "Review"
card_description: "AWS operates the largest official MCP server collection: 68 servers in a single Apache 2.0 monorepo covering every major AWS service. Combined with MCP client support in Amazon Q Developer and Bedrock AgentCore, AWS has built the most comprehensive cloud-native MCP ecosystem."
last_refreshed: 2026-03-23
---

**At a glance:** AWS publishes **68 official MCP servers** in [awslabs/mcp](https://github.com/awslabs/mcp) (8,540 stars, Apache 2.0) — the largest MCP server collection from any single organization. Servers cover databases (DynamoDB, Neptune, Redshift), compute (ECS, EKS, Lambda), security (IAM, Well-Architected), cost management, and more. MCP client support exists in Amazon Q Developer (CLI + IDE plugins) and Bedrock AgentCore.

AWS has taken a **go-wide infrastructure approach** to MCP, treating it as a protocol for connecting AI agents to cloud services. Rather than wrapping a single API, AWS built dozens of purpose-specific servers — each one a gateway to a different AWS service. This reflects AWS's core business: they don't sell models (though Bedrock hosts nearly 100), they sell the infrastructure those models connect to.

[Amazon Web Services](https://aws.amazon.com/) is the world's largest cloud provider. **AWS 2025 revenue: $128.7 billion** (+20% YoY), with a **$142 billion annualized run rate**. AWS holds approximately **30-32% cloud market share** (ahead of Azure at ~20% and Google Cloud at ~13%). Amazon overall: approximately **$2.2 trillion market cap**, approximately **1,576,000 employees** (AWS: ~139,000). AWS is an **AAIF Platinum member** — joining at the foundation's December 2025 launch alongside Anthropic, Google, Microsoft, OpenAI, Block, Bloomberg, and Cloudflare.

**Architecture note:** AWS's MCP strategy is the most **infrastructure-centric** of any AI provider. Where Anthropic created the protocol, Google published 24+ servers for its cloud, and OpenAI focused on client integration, AWS published **68 servers** covering virtually every major AWS service — turning MCP into the universal agent-to-cloud interface.

## What It Does

### The awslabs/mcp Monorepo (68 Servers)

The primary repository at [awslabs/mcp](https://github.com/awslabs/mcp) contains 68 individual MCP servers organized by AWS service:

| Category | Servers |
|----------|---------|
| Databases | DynamoDB, Neptune, DocumentDB, ElastiCache, Redshift, Postgres, S3 Tables |
| AI/ML | Bedrock Data Automation, Bedrock Custom Model Import, Bedrock Knowledge Bases, SageMaker AI, Nova Canvas |
| Compute & Containers | ECS, EKS, Lambda, Serverless |
| Infrastructure as Code | CDK, CloudFormation, Terraform |
| Security | IAM, Well-Architected Security |
| Observability | CloudWatch, CloudTrail |
| Cost Management | Cost Explorer, Billing & Cost Management, AWS Pricing |
| Developer Tools | AWS Documentation, CodePipeline, CodeBuild |
| Agent Infrastructure | Bedrock AgentCore |
| Networking & Storage | VPC, S3, Cloud Storage |

| Aspect | Detail |
|--------|--------|
| GitHub | [awslabs/mcp](https://github.com/awslabs/mcp) — 8,540 stars, 1,379 forks |
| Language | Python |
| License | Apache 2.0 |
| Commits | ~1,400 |
| Releases | 185 (latest: March 17, 2026) |
| Transport | stdio only (SSE removed May 2025; Streamable HTTP planned) |
| Installation | `uvx` with one-click install for Kiro, Cursor, VS Code |

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
| Amazon Q Developer CLI | Yes (since April 2025) | stdio and HTTP MCP server support |
| Amazon Q Developer IDE | Yes | VS Code, JetBrains, Visual Studio, Eclipse plugins |
| Bedrock Agents | Yes | Native MCP server invocation via AgentCore |
| AgentCore Gateway | Yes | Centralized MCP tool server — unified discovery and invocation |
| AgentCore Runtime | Yes (March 2026) | Stateful MCP sessions in dedicated microVMs, elicitation, sampling, progress notifications |

AWS is one of the most comprehensive MCP client implementors, spanning developer tools (Q Developer), managed AI services (Bedrock Agents), and infrastructure (Lambda, AgentCore).

### Bedrock AgentCore

AgentCore, announced in early 2026, is AWS's platform for deploying and managing AI agents with native MCP support:

- **AgentCore Gateway** — centralized MCP tool server; agents discover and invoke MCP tools through a unified interface
- **AgentCore Runtime** — deploys MCP servers in managed infrastructure with stateful session support (dedicated microVMs, announced March 10, 2026)
- Supports elicitation, sampling, and progress notifications for MCP sessions

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

AWS Bedrock hosts models from 15+ providers. On-demand pricing per 1 million tokens:

### Amazon Nova (AWS First-Party)

| Model | Input | Output |
|-------|-------|--------|
| Nova Pro | $0.80 | $3.20 |
| Nova Lite | $0.06 | $0.24 |
| Nova Micro | $0.035 | $0.14 |

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
| Official MCP servers | Yes (68 servers, 8.5K stars) | No (reference servers) | Yes (24+ servers, 3.4K stars) | No | No | Yes (210 stars) | No |
| Server approach | Infrastructure-wide monorepo | Reference implementations | Managed remote + open-source | Client only | Client only (Llama Stack) | Hub access + Gradio Spaces | Client only |
| MCP client | Yes (Q Developer, AgentCore) | Yes (all Claude products) | Yes (Gemini CLI, SDKs) | Yes (ChatGPT, Agents SDK) | Yes (Llama Stack) | No | Yes (Le Chat, Agents API) |
| AAIF member | Yes (Platinum) | Yes (Platinum, co-founder) | Yes (Platinum) | Yes (Platinum, co-founder) | No | No | Yes (Silver) |
| Unique strength | Most servers (68), cloud integration | Created the protocol | Second most servers (24+) | 900M+ weekly users | Fully free models | 1M+ models, Gradio-as-MCP | Open-weight + EU sovereignty |
| Own models | Yes (Nova family) | Yes (Claude family) | Yes (Gemini family) | Yes (GPT/o-series) | Yes (Llama family) | Platform (hosts all) | Yes (Mistral family) |
| Free tier | Yes (AWS Free Tier) | Yes (limited Claude) | Yes (Flash models) | Yes (limited ChatGPT) | Yes (all models free) | Yes (full Hub access) | Yes (Le Chat Free) |

## Known Issues

1. **238 open issues** — The monorepo's issue count reflects the breadth of 68 servers. Active maintenance is a double-edged sword: frequent releases (185 total) mean frequent dependency changes and potential breakage.

2. **stdio only** — SSE transport was removed in May 2025, and Streamable HTTP is not yet available. This limits deployment options for remote/hosted MCP server scenarios outside of AgentCore.

3. **OpenAPI MCP Server broken** — Issue [#2533](https://github.com/awslabs/mcp/issues/2533): all published versions fail to start due to fastmcp 3.x incompatibility with no version constraint. Indicates dependency management challenges in a large monorepo.

4. **AWS Documentation server slow** — Issue [#2435](https://github.com/awslabs/mcp/issues/2435): `aws-documentation-mcp-server` takes 3.24 seconds to load vs typical sub-1-second for other servers.

5. **Windows compatibility issues** — Issue [#1307](https://github.com/awslabs/mcp/issues/1307): `aws-msk-mcp-server` fails on Windows/Cursor ("No tools, prompts, or resources"). Cross-platform support varies by server.

6. **Deprecated servers** — Several servers (Cloud Control API, CDK, Terraform) are marked deprecated with recommendations to use alternatives, creating confusion about which server to use for a given service.

7. **Cloud billing required** — Most servers interact with AWS services that require an active AWS account with billing. Unlike Google's free API tier or Meta's free models, there's no zero-cost path for most MCP server usage.

8. **No Bedrock API wrapper** — While AWS publishes 68 servers for AWS *services*, there's no official MCP server that wraps the Bedrock API itself for model inference. Developers wanting to call Bedrock models via MCP need community solutions.

9. **AgentCore is new** — AgentCore Runtime's stateful MCP support was announced March 2026. As a new product, expect rapid changes, limited documentation, and potential breaking changes during preview.

10. **Monorepo complexity** — 68 servers in one repository means navigating a large codebase. Individual servers vary in maturity, documentation quality, and maintenance frequency.

## Bottom Line

**Rating: 4.5 out of 5**

AWS has built the **most extensive MCP server infrastructure** of any company. With 68 official servers covering virtually every major AWS service, AAIF Platinum membership, and MCP client support across Amazon Q Developer and Bedrock AgentCore, AWS treats MCP as the standard interface between AI agents and cloud infrastructure.

The **infrastructure-centric approach** is uniquely AWS. While Anthropic created the protocol and Google published 24+ servers, AWS went further — 68 servers, a Lambda runtime for hosting MCP servers, a proxy for SigV4 authentication, and AgentCore for managed MCP server deployment. This isn't just MCP support; it's MCP as a first-class cloud primitive.

The **4.5/5 rating** — the highest in this AI provider series — reflects the sheer breadth and depth of AWS's MCP investment. No other company comes close to 68 official servers. The community ecosystem (714 repos) is also the largest. Amazon Q Developer's MCP client support across CLI and four IDE platforms is comprehensive. And AgentCore represents the industry's first managed MCP server infrastructure.

What keeps it from 5/5: the monorepo has 238 open issues, stdio-only transport limits remote deployment, there's no Bedrock inference wrapper, several servers are deprecated, and the rapid pace of 185 releases risks stability. Cloud billing requirements also mean there's no free experimentation path for most servers.

**Who benefits most from AWS's MCP ecosystem:**

- **AWS-native teams** — If your infrastructure runs on AWS, these 68 servers give your AI agents direct access to every service: databases, compute, security, cost management, and more
- **Enterprise architects** — AgentCore provides managed MCP server infrastructure with SigV4 auth, IAM integration, and stateful sessions — the kind of enterprise-grade agent tooling that other providers don't yet offer
- **Agent builders** — Amazon Q Developer's MCP client across CLI and IDE, combined with Bedrock's nearly 100 models and Agents framework, creates a complete agent development stack

**Who should be cautious:**

- **Multi-cloud teams** — These servers are AWS-specific; there's no abstraction layer for Azure or GCP equivalents
- **Cost-sensitive experiments** — Unlike Meta's free models or Google's free API tier, most AWS MCP servers require active AWS billing; experimentation costs real money
- **Teams wanting model-level MCP access** — There's no official Bedrock inference MCP server; the 68 servers connect to AWS services, not to Bedrock model endpoints directly

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official AWS announcements. Information is current as of March 2026. See our [About page](/about/) for details on our review process.*
