# Amazon Kiro Review — The Agentic IDE That Writes the Spec Before the Code

> Amazon Kiro is AWS's agentic IDE, running Claude, OpenAI, and open-weight models via Bedrock and an Auto model router. Its core differentiator: spec-driven development — Kiro generates requirements documents and acceptance criteria before it writes a line of code. We cover how it works, who it's for, and whether the spec-first philosophy holds up in production.


Most AI coding tools start with code. Amazon Kiro starts with a plan.

**[Kiro](https://aws.amazon.com/documentation-overview/kiro/)** is an agentic IDE from AWS that inverts the standard AI coding workflow. Where Cursor and GitHub Copilot take a prompt and immediately generate code, Kiro takes a prompt, generates a formal requirements document with structured acceptance criteria, waits for your review and approval, and *then* writes code. The spec is the unit of work. Code is what happens after you sign off on the spec.

This is a deliberate response to what AWS calls "vibe coding" — the pattern of prompting an AI, accepting whatever it generates, and iterating through bugs until something resembling the intended behavior emerges. Kiro's thesis is that the vibe coding loop is a symptom of skipping the requirements phase, not a feature.

Whether that thesis is right for your workflow is the central question in this review.

---

## What Kiro Is

Kiro is a VS Code fork ([built on Code OSS](https://kiro.dev/)) with a deep agent layer built in. AWS launched it in public preview on [July 14, 2025](https://kiro.dev/blog/introducing-kiro/), then took it to [general availability on November 17, 2025](https://kiro.dev/blog/general-availability/), adding a CLI, property-based testing, checkpoint/rewind, and team plans at that point. It entered 2026 as one of the more technically distinctive entries in the AI IDE market — not because it generates better code than Cursor, but because it approaches software development differently.

The three capabilities that define Kiro are:

1. **Spec-Driven Development** — natural language to structured requirements before code generation
2. **Hooks** — event-driven automations that fire on IDE events
3. **Steering Rules** — project and global configuration files that shape agent behavior

Each of these maps to a real problem in production software development that most AI tools don't address.

---

## How Spec-Driven Development Works

The workflow begins with a feature description in natural language — the same kind of prompt you'd give Cursor or Copilot. Kiro's first move is not to write code.

Kiro generates a **specification document** containing:

- **Functional requirements** written in [EARS (Easy Approach to Requirements Syntax) notation](https://kiro.dev/docs/specs/feature-specs/requirements-first/) — a structured `WHEN [condition] THE SYSTEM SHALL [behavior]` format that captures conditions, system behavior, and expected outcomes in a consistent, auditable form. This is still Kiro's documented approach as of Kiro's own docs (last updated August 2026).
- **Acceptance criteria** — concrete, testable conditions that define when the feature is done
- **Design artifacts** — when relevant, component diagrams or interface definitions

You review the spec. You can edit it. You can reject it and rewrite it. The spec becomes the explicit contract between what you want and what the agent will build.

When you approve, Kiro generates code against the spec. If the generated code passes acceptance criteria, it's done. If it doesn't, Kiro revises — not by improvising, but by checking its output against the criteria you approved.

The practical result is that the conversation between developer and agent is captured in a version-controlled document, not just in a chat log. When you revisit the feature six months later, you have the spec — not just the code.

*Correction (2026-08-23): Kiro now also offers a [Quick Spec](https://kiro.dev/docs/specs/quick-spec/) mode that generates requirements, design, and tasks in one pass without approval gates, for well-understood features. The full three-phase, approval-gated flow described above remains the default and is still what AWS documents as the standard workflow.*

---

## Hooks: Event-Driven Automation

**[Hooks](https://kiro.dev/docs/hooks/)** are Kiro's automation layer: "shell commands or agent prompts" that run automatically when specific events happen in a session. They fire on IDE/agent events and trigger predefined agent actions:

| Trigger | Example Actions |
|---|---|
| File save (`PostFileSave`) | Run tests, update docs, regenerate fixtures |
| Task/tool execution (`PreToolUse`/`PostToolUse`) | Gate dangerous operations, validate changes before commits |
| Session start/stop | Generate PR summary, check spec compliance |
| Manual trigger | Custom workflows on demand |

Hooks are defined as JSON files in `.kiro/hooks/` at the project level. A team can define a standard set of Hooks that apply to every contributor — consistent test runs, documentation updates, and compliance checks — without relying on individual developer discipline to run them.

This is not the same as a CI/CD pipeline. Hooks run inside the IDE during development, before code reaches a pipeline. The goal is to catch spec drift, test failures, and documentation debt in the edit loop, not after a commit.

---

## Steering Rules

**[Steering Rules](https://kiro.dev/docs/steering/)** are markdown configuration files (`.kiro/steering/` at the workspace level, or `~/.kiro/steering/` for global rules that apply across projects) that specify how Kiro agents behave within a project or globally:

- Coding standards and style preferences
- Preferred libraries, frameworks, and version constraints
- Deployment environment details
- Security constraints and forbidden patterns
- Workflow preferences (e.g., always generate tests alongside code)

Steering Rules are the mechanism by which a team encodes its engineering norms into the agent layer. A rule like "all database queries must use parameterized statements" or "always use the internal logging library, not console.log" persists across sessions, contributors, and features without needing to be restated in every prompt.

The `.kiro/` directory is committed to the repository. Steering Rules are part of the codebase, reviewable and version-controlled like any other configuration.

---

## Under the Hood: Multi-Model, With Claude at the Center

*Correction (2026-08-23): This section originally described Kiro as routing between "Claude Sonnet" and "Amazon Nova." That could not be re-verified. Kiro's own [launch coverage](https://kiro.dev/blog/introducing-kiro/) describes it shipping with Claude Sonnet 4 and 3.7 as its models, and the current [available-models documentation](https://kiro.dev/docs/models/available-models/) and [models overview](https://kiro.dev/docs/models/) list Anthropic Claude (Opus and Sonnet families, plus Haiku), OpenAI's GPT-5.6, and several open-weight models (DeepSeek, Qwen3 Coder, GLM, MiniMax) — Amazon Nova is not among them. The Nova claim has been removed rather than left uncorrected.*

Kiro is no longer a two-model tool. Per [Kiro's model documentation](https://kiro.dev/docs/models/available-models/), users can manually pick a specific model for a chat session, or leave it on **Auto** — "Kiro's model router," which automatically selects a model per task and is described as targeting "Claude Sonnet 4.5-class quality or better" on the free tier and "Claude Opus-class quality or better" on paid tiers. The available models include:

- **Anthropic Claude** — Opus and Sonnet families (including Sonnet 5), plus Haiku, for reasoning-heavy work: spec generation, acceptance criteria, architectural decisions, code review
- **OpenAI GPT-5.6** — offered as an alternative frontier option
- **Open-weight models** — DeepSeek, Qwen3 Coder, GLM, and MiniMax, generally lower-cost/credit options for higher-throughput code generation

Models run via **Amazon Bedrock** for the Bedrock-hosted options, which keeps IAM-based access control and audit logging in play for teams that need it — a compliance path that purely API-key-based tools can't match. Whether every listed model (e.g., the OpenAI and open-weight options) is served through Bedrock specifically versus a direct provider integration is not detailed in Kiro's public docs; treat "via Bedrock" as accurate for the Claude models and Bedrock-native deployments, not as a blanket statement about every model on the list.

Auto routing is not exposed as a visible decision to the user by default, but manual model selection is available — a material change from Kiro's original invisible-routing design.

---

## AWS Ecosystem Integration

Kiro integrates natively with the AWS developer stack:

- **Amazon CodeCatalyst** — *Correction (2026-08-23): AWS [closed CodeCatalyst to new customers on November 7, 2025](https://docs.aws.amazon.com/codecatalyst/latest/userguide/migration.html); existing spaces keep working but no new spaces can be created and AWS "does not plan to introduce new features." AWS is directing customers toward [GitLab Duo with Amazon Q](https://aws.amazon.com/blogs/devops/announcing-general-availability-of-gitlab-duo-with-amazon-q/) instead. Treat any CodeCatalyst-to-Kiro integration as legacy, relevant only to teams with pre-existing CodeCatalyst spaces, not a current onboarding path.*
- **Amazon Q Developer** — Kiro and Amazon Q Developer are positioned as complementary security tooling: an [AWS Security Blog post](https://aws.amazon.com/blogs/security/five-ways-to-use-kiro-and-amazon-q-to-strengthen-your-security-posture/) describes using both together for tasks like scanning resources, drafting policies, and CVE research, and Kiro's own agent includes a security-review task that performs an OWASP-aligned review of a file or directory. This is a looser coupling than "Q Developer's scanner runs inside Kiro" — they're separate tools AWS documents using in tandem, not one embedded in the other.
- **Amazon Bedrock** — model inference, access control, and audit logging through the standard Bedrock control plane, for the Bedrock-hosted models (see model section above)
- **IAM** — Kiro operations inherit your AWS role, not a separate API key

For teams running AWS-native infrastructure, this integration reduces the onboarding surface area. The toolchain is consistent with existing security posture and observability setup — though the CodeCatalyst piece of that story is now legacy rather than current.

---

## MCP Support

Kiro includes native **[Model Context Protocol (MCP)](https://kiro.dev/docs/mcp/)** support, enabling connection to any MCP-compatible tool server. This means:

- External context sources (databases, documentation, internal APIs) can be made available to Kiro's agent during spec generation and code writing
- MCP servers already built for Claude Code, Cursor, or other clients work with Kiro without modification
- Teams can extend Kiro's capabilities with custom tools without waiting for first-party integrations

*Correction (2026-08-23): the MCP config path was previously given as `.kiro/mcp.json`. Per Kiro's own docs, the correct workspace-level path is `.kiro/settings/mcp.json` (accessible via the "Kiro: Open workspace MCP config" command), with a separate user-level config and support for per-agent `mcpServers` fields in agent config files.* MCP is supported in the IDE, CLI, and Web interfaces, with some limitations on remote servers in Web; mobile is not yet supported.

---

## Pricing

*Correction (2026-08-23): pricing changed since this review was first published. Per [Kiro's official pricing page](https://kiro.dev/pricing/) and [FAQ](https://kiro.dev/faq/), the Free tier now grants 50 credits/month (roughly, but not exactly, "interactions" — different models and actions consume credits at different rates) rather than a flat interaction count, Pro is now $20/month rather than $19, and three higher paid tiers were added at [Kiro's November 2025 GA launch](https://kiro.dev/blog/general-availability/):*

| Tier | Price | Credits/month |
|---|---|---|
| Free | $0 | 50 |
| Pro | $20/user/month | 1,000 |
| Pro+ | $40/user/month | 2,000 |
| Pro Max | $100/user/month | 5,000 |
| Power | $200/user/month | 10,000 |
| Enterprise | Custom | Custom — centralized billing, SSO, usage analytics |

Add-on credits cost $0.04 each. The $20/month Pro tier now matches Cursor's $20/month Pro plan exactly, rather than undercutting it as this review originally reported — Kiro is no longer the cheaper option, just a comparably priced one with a deeper AWS integration story. The free tier's 50 credits/month is meaningful for evaluation but not sufficient for daily development.

---

## Who Kiro Is For

**Kiro fits teams that:**
- Build on AWS and want a consistent security and compliance posture
- Are shipping complex features where rework costs are high
- Want agent behavior encoded at the project level, not negotiated per prompt
- Have an existing Amazon CodeCatalyst space and want IDE integration (note: CodeCatalyst has been [closed to new customers since November 2025](https://docs.aws.amazon.com/codecatalyst/latest/userguide/migration.html), so this applies only to pre-existing users)

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
| **Backend** | [Claude, OpenAI GPT-5.6, open-weight models via Auto router, Bedrock](https://kiro.dev/docs/models/available-models/) | Frontier models (selectable) | GPT-4o, Claude, Gemini |
| **Primary pricing** | [$20/month Pro](https://kiro.dev/pricing/) | [$20/month Pro](https://cursor.com/pricing) | [$10/month Pro](https://github.com/features/copilot/plans) |
| **AWS integration** | Native (IAM, Bedrock); CodeCatalyst legacy-only since Nov 2025 | None | Limited |
| **MCP support** | Yes | Yes | Limited |
| **Spec artifact** | Version-controlled requirements | None | None |
| **Hooks** | Yes (event-driven) | Limited | No |
| **Steering rules** | Yes (project + global) | Cursor rules | No |
| **Enterprise market share** | Growing, AWS-native segment | Strong | ~42% of paid AI coding tools per market-research aggregation ([getpanto.ai](https://www.getpanto.ai/blog/github-copilot-statistics)); 90% of Fortune 100 use Copilot per Microsoft's own FY2025 Q4 earnings disclosure, [reported by TechCrunch](https://techcrunch.com/2025/07/30/github-copilot-crosses-20-million-all-time-users/) |

---

## Limitations

**The free tier is limited.** 50 credits per month is enough to evaluate the spec-driven workflow but not enough for daily use. The [$20/month Pro tier](https://kiro.dev/pricing/) is the realistic entry point — and for teams that outgrow Pro's 1,000 credits, Pro+ ($40/month), Pro Max ($100/month), and Power ($200/month) exist above it.

**AWS lock-in is real, though the shape of it has shifted.** The deep Bedrock/IAM integration that makes Kiro compelling for AWS teams makes it less useful for teams on GCP, Azure, or mixed-cloud infrastructure. The compliance benefits of IAM-governed access evaporate without the AWS context. The CodeCatalyst piece of that story is now moot for new users, since [CodeCatalyst stopped accepting new customers in November 2025](https://docs.aws.amazon.com/codecatalyst/latest/userguide/migration.html).

**Spec overhead for simple tasks.** For a two-line bug fix or a quick refactor, the spec → approval → code flow adds steps that faster tools skip. Kiro's strength is proportional to the complexity and team size of the work. Solo developers building small projects may find Cursor's friction-free loop more productive.

**Relatively new in the market.** Kiro launched in mid-2025. The community, plugin ecosystem, and Stack Overflow answer surface are smaller than Cursor or Copilot. Teams evaluating it in production should expect to resolve more issues without community reference.

---

## Rating: 4/5

Kiro represents a coherent and defensible thesis about what agentic coding tools should do: encode intent explicitly, generate artifacts that outlive the chat session, and automate the downstream maintenance work that AI-generated code creates.

The spec-driven model is not hype. Teams that adopt it report meaningfully less rework on complex features, because the acceptance criteria surface misunderstandings between developer intent and agent interpretation before code is written rather than after.

The 4/5 reflects the coherence of that thesis, strong execution on the core workflow, and competitive pricing. The deductions come from the AWS lock-in (a real constraint outside that ecosystem) and the learning curve relative to more permissive tools like Cursor. Kiro is not for every developer — but for teams shipping production software on AWS who have felt the consequences of vibe coding, it's the most serious engineering-discipline tool in the AI IDE market.

---

## Sources

- [Kiro documentation — AWS](https://aws.amazon.com/documentation-overview/kiro/) — official feature documentation, links to full docs
- [Kiro pricing — kiro.dev](https://kiro.dev/pricing/) — current tiers: Free, Pro, Pro+, Pro Max, Power, Enterprise
- [Kiro FAQ — kiro.dev](https://kiro.dev/faq/) — pricing, free tier, model selection details
- [Available models — kiro.dev docs](https://kiro.dev/docs/models/available-models/) — current model lineup and Auto router behavior
- [Introducing Kiro — kiro.dev blog](https://kiro.dev/blog/introducing-kiro/) — July 14, 2025 preview launch, original model set
- [Kiro is generally available — kiro.dev blog](https://kiro.dev/blog/general-availability/) — November 17, 2025 GA launch, CLI, property-based testing, team plans
- [Specs / Requirements-First Workflow — kiro.dev docs](https://kiro.dev/docs/specs/feature-specs/requirements-first/) — EARS notation, requirements/design/tasks workflow
- [Quick Spec — kiro.dev docs](https://kiro.dev/docs/specs/quick-spec/) — expedited spec mode without approval gates
- [Hooks — kiro.dev docs](https://kiro.dev/docs/hooks/) — hook trigger events and configuration
- [Steering — kiro.dev docs](https://kiro.dev/docs/steering/) — steering rules directory structure and scope
- [MCP — kiro.dev docs](https://kiro.dev/docs/mcp/) — MCP configuration paths and platform support
- [How to migrate from CodeCatalyst — AWS docs](https://docs.aws.amazon.com/codecatalyst/latest/userguide/migration.html) — CodeCatalyst closed to new customers November 7, 2025
- [Five ways to use Kiro and Amazon Q to strengthen your security posture — AWS Security Blog](https://aws.amazon.com/blogs/security/five-ways-to-use-kiro-and-amazon-q-to-strengthen-your-security-posture/) — Kiro/Q Developer security tooling relationship
- [Cursor pricing — cursor.com](https://cursor.com/pricing) — $20/month Pro plan, for comparison table
- [GitHub Copilot plans — github.com](https://github.com/features/copilot/plans) — $10/month Pro plan, for comparison table
- [GitHub Copilot crosses 20M all-time users — TechCrunch](https://techcrunch.com/2025/07/30/github-copilot-crosses-20-million-all-time-users/) — reports Microsoft's own 90%-of-Fortune-100 disclosure
- [GitHub Copilot Statistics — getpanto.ai](https://www.getpanto.ai/blog/github-copilot-statistics) — market-share aggregation (~42% of paid AI coding tools); secondary/aggregator source, used alongside the TechCrunch citation above, not in place of it
- [AWS Kiro: Why Amazon's Agentic IDE Goes Beyond Vibe Coding — Devoteam](https://www.devoteam.com/expert-view/aws-kiro-beyond-vibe-coding/) — spec-driven development analysis

---

*ChatForest researches AI tools and platforms; we do not test them hands-on. Our reviews are based on publicly available documentation, developer community reports, benchmark data, and press coverage.*

