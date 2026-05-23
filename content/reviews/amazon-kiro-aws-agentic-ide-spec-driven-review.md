---
title: "Amazon Kiro Review — The Agentic IDE That Writes the Spec Before the Code"
date: 2026-05-23
description: "Amazon Kiro is AWS's agentic IDE powered by Claude and Amazon Nova via Bedrock. Its core differentiator: spec-driven development — Kiro generates requirements documents and acceptance criteria before it writes a line of code. We cover how it works, who it's for, and whether the spec-first philosophy holds up in production."
og_description: "Amazon Kiro is an AWS-built agentic IDE that turns natural language into formal specs (EARS notation), then generates and maintains code from those specs. Powered by Claude Sonnet + Amazon Nova via Bedrock. Free tier: 50 interactions/month. Pro: $19/month. Rated 3.5/5."
content_type: "Review"
card_description: "Amazon Kiro is an agentic IDE from AWS that inverts the Cursor/Copilot model: the spec is source-of-truth; code is a build artifact. You describe a feature in natural language, Kiro produces structured requirements in EARS notation, and only after you approve does it write code. Event-driven Hooks automate tests, docs, and downstream changes on file save or PR open. Steering Rules configure agent behavior per project or globally. Powered by Claude Sonnet (reasoning) + Amazon Nova (code gen) via Amazon Bedrock. Deep integration with CodeCatalyst, Q Developer, and IAM. Free: 50 interactions/month; Pro: $19/month. Launched mid-2025. The spec-driven model genuinely reduces rework for complex features — but the gate between spec and code adds friction that solo developers building quick prototypes will find frustrating."
tags: ["amazon", "aws", "kiro", "agentic-coding", "ide", "claude", "bedrock", "developer-tools", "spec-driven", "mcp"]
categories: ["reviews"]
rating: 4
author: "ChatForest"
---

Most AI coding tools start with code. Amazon Kiro starts with a plan.

**Kiro** is an agentic IDE from AWS that inverts the standard AI coding workflow. Where Cursor and GitHub Copilot take a prompt and immediately generate code, Kiro takes a prompt, generates a formal requirements document with structured acceptance criteria, waits for your review and approval, and *then* writes code. The spec is the unit of work. Code is what happens after you sign off on the spec.

This is a deliberate response to what AWS calls "vibe coding" — the pattern of prompting an AI, accepting whatever it generates, and iterating through bugs until something resembling the intended behavior emerges. Kiro's thesis is that the vibe coding loop is a symptom of skipping the requirements phase, not a feature.

Whether that thesis is right for your workflow is the central question in this review.

---

## What Kiro Is

Kiro is a VS Code fork with a deep agent layer built in. It launched publicly in mid-2025 and entered 2026 as one of the more technically distinctive entries in the AI IDE market — not because it generates better code than Cursor, but because it approaches software development differently.

The three capabilities that define Kiro are:

1. **Spec-Driven Development** — natural language to structured requirements before code generation
2. **Hooks** — event-driven automations that fire on IDE events
3. **Steering Rules** — project and global configuration files that shape agent behavior

Each of these maps to a real problem in production software development that most AI tools don't address.

---

## How Spec-Driven Development Works

The workflow begins with a feature description in natural language — the same kind of prompt you'd give Cursor or Copilot. Kiro's first move is not to write code.

Kiro generates a **specification document** containing:

- **Functional requirements** written in EARS (Easy Approach to Requirements Syntax) notation — a structured format that captures conditions, system behavior, and expected outcomes in a consistent, auditable form
- **Acceptance criteria** — concrete, testable conditions that define when the feature is done
- **Design artifacts** — when relevant, component diagrams or interface definitions

You review the spec. You can edit it. You can reject it and rewrite it. The spec becomes the explicit contract between what you want and what the agent will build.

When you approve, Kiro generates code against the spec. If the generated code passes acceptance criteria, it's done. If it doesn't, Kiro revises — not by improvising, but by checking its output against the criteria you approved.

The practical result is that the conversation between developer and agent is captured in a version-controlled document, not just in a chat log. When you revisit the feature six months later, you have the spec — not just the code.

---

## Hooks: Event-Driven Automation

**Hooks** are Kiro's automation layer. They fire on IDE events and trigger predefined agent actions:

| Trigger | Example Actions |
|---|---|
| File save | Run tests, update docs, regenerate fixtures |
| PR open | Generate PR summary, check spec compliance |
| Dependency change | Cascade spec updates, flag breaking changes |
| Manual trigger | Custom workflows on demand |

Hooks are defined in configuration files at the project level. A team can define a standard set of Hooks that apply to every contributor — consistent test runs, documentation updates, and compliance checks — without relying on individual developer discipline to run them.

This is not the same as a CI/CD pipeline. Hooks run inside the IDE during development, before code reaches a pipeline. The goal is to catch spec drift, test failures, and documentation debt in the edit loop, not after a commit.

---

## Steering Rules

**Steering Rules** are configuration files (`.kiro/steering/`) that specify how Kiro agents behave within a project or globally:

- Coding standards and style preferences
- Preferred libraries, frameworks, and version constraints
- Deployment environment details
- Security constraints and forbidden patterns
- Workflow preferences (e.g., always generate tests alongside code)

Steering Rules are the mechanism by which a team encodes its engineering norms into the agent layer. A rule like "all database queries must use parameterized statements" or "always use the internal logging library, not console.log" persists across sessions, contributors, and features without needing to be restated in every prompt.

The `.kiro/` directory is committed to the repository. Steering Rules are part of the codebase, reviewable and version-controlled like any other configuration.

---

## Under the Hood: Claude + Nova via Bedrock

Kiro routes between two models depending on the task:

- **Claude Sonnet** — used for reasoning-heavy work: spec generation, acceptance criteria, architectural decisions, code review, complex debugging
- **Amazon Nova** — used for high-throughput code generation: scaffold generation, boilerplate, repetitive transformations

Both models run via **Amazon Bedrock**, making Kiro a natural fit for teams already operating on AWS infrastructure. IAM roles govern model access, which satisfies a compliance requirement that purely API-key-based tools cannot meet.

The multi-model routing is not exposed to users directly. Kiro decides which model to invoke based on task type. The experience is a single agent; the backend is optimized per workload.

---

## AWS Ecosystem Integration

Kiro integrates natively with the AWS developer stack:

- **Amazon CodeCatalyst** — project management, sprint boards, and issue tracking connect directly to Kiro's agent layer. An issue assigned to you in CodeCatalyst can be ingested as a Kiro spec with one command.
- **Amazon Q Developer** — the AI security scanning layer from Q Developer runs alongside Kiro, flagging security issues at authoring time
- **Amazon Bedrock** — model inference, access control, and audit logging through the standard Bedrock control plane
- **IAM** — Kiro operations inherit your AWS role, not a separate API key

For teams running AWS-native infrastructure, this integration reduces the onboarding surface area. The toolchain is consistent with existing security posture and observability setup.

---

## MCP Support

Kiro includes native **Model Context Protocol (MCP)** support, enabling connection to any MCP-compatible tool server. This means:

- External context sources (databases, documentation, internal APIs) can be made available to Kiro's agent during spec generation and code writing
- MCP servers already built for Claude Code, Cursor, or other clients work with Kiro without modification
- Teams can extend Kiro's capabilities with custom tools without waiting for first-party integrations

The MCP integration is configured in `.kiro/mcp.json`, following the same connection pattern used by other MCP-compatible clients.

---

## Pricing

| Tier | Price | Interactions |
|---|---|---|
| Free | $0 | 50/month |
| Pro | $19/month | Unlimited (fair use) |

The $19/month Pro tier is competitive with Cursor ($20/month) and positions Kiro as a lower-cost alternative for teams primarily working in AWS ecosystems. The free tier at 50 interactions is meaningful for evaluation but not sufficient for daily development.

---

## Who Kiro Is For

**Kiro fits teams that:**
- Build on AWS and want a consistent security and compliance posture
- Are shipping complex features where rework costs are high
- Want agent behavior encoded at the project level, not negotiated per prompt
- Already use CodeCatalyst and want IDE integration

**Kiro may frustrate developers who:**
- Work primarily outside AWS (limited ecosystem benefit)
- Build quick prototypes where the spec-approval gate adds latency without proportional value
- Prefer the fast, iterative, low-ceremony loop of Cursor or Windsurf

The spec-first model is a genuine workflow change, not just a UI difference. Teams that have suffered from vibe-coded technical debt will find the structure useful. Developers who prefer to think through code directly may find the spec approval step a detour.

---

## Comparison: Kiro vs. Cursor vs. GitHub Copilot

|  | Kiro | Cursor | GitHub Copilot |
|---|---|---|---|
| **Core model** | Spec-first → code | Prompt → code | Inline completion + agent |
| **Backend** | Claude + Nova via Bedrock | Frontier models (selectable) | GPT-4o, Claude, Gemini |
| **Primary pricing** | $19/month Pro | $20/month Pro | $10/month Pro |
| **AWS integration** | Native (IAM, Bedrock, CodeCatalyst) | None | Limited |
| **MCP support** | Yes | Yes | Limited |
| **Spec artifact** | Version-controlled requirements | None | None |
| **Hooks** | Yes (event-driven) | Limited | No |
| **Steering rules** | Yes (project + global) | Cursor rules | No |
| **Enterprise market share** | Growing, AWS-native segment | Strong | 42%, Fortune 100 default |

---

## Limitations

**The free tier is limited.** 50 interactions per month is enough to evaluate the spec-driven workflow but not enough for daily use. The $19/month Pro tier is the realistic entry point.

**AWS lock-in is real.** The deep Bedrock/IAM/CodeCatalyst integration that makes Kiro compelling for AWS teams makes it less useful for teams on GCP, Azure, or mixed-cloud infrastructure. The model routing and compliance benefits evaporate without the AWS context.

**Spec overhead for simple tasks.** For a two-line bug fix or a quick refactor, the spec → approval → code flow adds steps that faster tools skip. Kiro's strength is proportional to the complexity and team size of the work. Solo developers building small projects may find Cursor's friction-free loop more productive.

**Relatively new in the market.** Kiro launched in mid-2025. The community, plugin ecosystem, and Stack Overflow answer surface are smaller than Cursor or Copilot. Teams evaluating it in production should expect to resolve more issues without community reference.

---

## Rating: 4/5

Kiro represents a coherent and defensible thesis about what agentic coding tools should do: encode intent explicitly, generate artifacts that outlive the chat session, and automate the downstream maintenance work that AI-generated code creates.

The spec-driven model is not hype. Teams that adopt it report meaningfully less rework on complex features, because the acceptance criteria surface misunderstandings between developer intent and agent interpretation before code is written rather than after.

The 4/5 reflects the coherence of that thesis, strong execution on the core workflow, and competitive pricing. The deductions come from the AWS lock-in (a real constraint outside that ecosystem) and the learning curve relative to more permissive tools like Cursor. Kiro is not for every developer — but for teams shipping production software on AWS who have felt the consequences of vibe coding, it's the most serious engineering-discipline tool in the AI IDE market.

---

*ChatForest researches AI tools and platforms; we do not test them hands-on. Our reviews are based on publicly available documentation, developer community reports, benchmark data, and press coverage.*
