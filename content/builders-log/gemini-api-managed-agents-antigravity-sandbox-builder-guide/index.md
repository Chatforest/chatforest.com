---
title: "Gemini API Managed Agents: Hosted Sandbox Execution in One Call"
date: 2026-06-01
description: "Google launched Managed Agents in the Gemini API at Google I/O 2026. One call spins up an isolated Linux sandbox running the Antigravity agent on Gemini 3.5 Flash. The sandbox persists state between calls. Compute is free during preview. Here's how to use it."
og_description: "One API call. Isolated Linux sandbox. Stateful sessions. Google Search built-in. Custom agents via AGENTS.md. Here's what Gemini API Managed Agents actually does and when to use it over AWS AgentCore."
content_type: "Builder's Log"
categories: ["Google", "Agent Infrastructure", "Developer Tools"]
tags: ["google", "gemini", "managed-agents", "antigravity", "sandbox", "agent-infrastructure", "gemini-api", "stateful-agents", "production-ai", "builders-log"]
---

Google launched Managed Agents in the Gemini API at Google I/O 2026 on May 20. The service gives developers a hosted execution environment for AI agents — one API call spins up an isolated Linux sandbox, the Antigravity agent runs inside it, files and state persist between calls, and the sandbox tears down when you're done.

The problem it solves is the same one AWS AgentCore targets: running agents in production without building the execution infrastructure yourself. Google's version is simpler to start with, ships with one API key instead of an AWS account, and is free to compute during preview.

---

## What It Is

Managed Agents is a hosted agent execution service available through the Gemini API. You do not manage servers, containers, or execution loops. You send a request describing what you want done, and Google runs the agent in a secure Linux environment on their infrastructure.

The service has two layers:

**The Antigravity harness** (`antigravity-preview-05-2026`) is the only supported base agent during preview. It is a general-purpose autonomous agent built on Gemini 3.5 Flash that can plan work, write and execute code, manage files, search the web, and call URLs — all inside its sandbox. You define what you want done; the harness decides how to do it.

**The managed execution environment** is an isolated Linux sandbox spun up per session. The sandbox has a persistent filesystem. Files written in one call are still there in the next. Bash, Python, and Node.js all execute natively. Google Search and URL fetch are available. Network access beyond that is disabled by default and requires an explicit domain allowlist.

---

## Core API

The `google-genai` SDK is the single package for all Gemini API access, including Managed Agents. No Vertex AI or Google Cloud SDK required.

```bash
pip install google-genai
```

The interaction call:

```python
from google import genai

client = genai.Client()  # uses GEMINI_API_KEY from environment

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Fetch the JSON from https://api.example.com/data and write a summary report as report.md",
    system_instruction="You are a data analyst. Be concise and include all numeric values."
)

print(interaction.output_text)
print(f"Environment ID: {interaction.environment_id}")
print(f"Interaction ID: {interaction.id}")
```

The `interaction.environment_id` is your handle to the sandbox. Save it if you need to continue the task in a follow-up call.

---

## Stateful Sessions

Each sandbox has a persistent filesystem. Files written in one interaction are present in the next if you pass the same `environment_id`.

```python
# First call: agent writes a draft
interaction_1 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script to process CSV files and save it as processor.py",
)
env_id = interaction_1.environment_id

# Second call: agent continues in the same sandbox
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    environment=env_id,
    previous_interaction_id=interaction_1.id,
    input="Add error handling to processor.py and write a test file for it",
)

# Third call: agent uses both files
interaction_3 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    environment=env_id,
    previous_interaction_id=interaction_2.id,
    input="Run the tests and fix any failures",
)
```

The `previous_interaction_id` tells the harness where the conversation left off. The agent sees the filesystem state from prior calls without you having to re-explain what was done.

Sandbox environments persist until you explicitly delete them or they expire. The preview documentation does not specify a hard session duration limit — this is a material difference from AgentCore's 8-hour cap, and likely to be addressed when billing and limits are finalized post-preview.

---

## What the Sandbox Can Do

Inside the sandbox, the Antigravity agent has access to:

**Code execution:** Bash commands, Python scripts, and Node.js programs run natively. The agent can install packages (`pip install`, `npm install`) if network access is enabled for the relevant registry domains.

**File system:** Reads and writes files. Files persist across interactions within the same environment. The agent can produce output artifacts — reports, scripts, datasets, HTML files — that you retrieve via the API or have the agent process further.

**Google Search:** Built-in, no configuration needed. The agent uses Search to retrieve current information when needed.

**URL fetch:** The agent can make HTTP requests to retrieve data from specific URLs. This is distinct from general network access.

**Network access:** Disabled by default. Enable specific domains via an allowlist in your configuration. Useful for calling your own APIs or allowing package installation from known registries.

What the sandbox cannot do by default: arbitrary outbound network connections, access to your local filesystem, or access to other Google services without explicit configuration.

---

## Inline Customization

You can override the agent's behavior at call time with `system_instruction`. This is the fastest way to adapt the agent for a specific task:

```python
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the repository structure and find all TODO comments",
    system_instruction="""You are a senior code reviewer.
Focus on security issues and technical debt.
Write all findings to findings.md with severity ratings (Critical/High/Medium/Low).
Do not make any code changes."""
)
```

The `system_instruction` takes precedence over the agent's default behavior. You can use it to constrain scope, enforce output format, set a persona, or control what the agent is allowed to do.

---

## Custom Agents: AGENTS.md + SKILL.md

For repeatable workflows, define your agent as configuration files and register it as a named managed agent — then invoke it by ID rather than passing instructions every call.

The agent configuration lives in your sandbox environment:

```
.agents/
  AGENTS.md          # agent instructions (loaded automatically on startup)
skills/
  web-scraper/
    SKILL.md         # skill definition
  report-writer/
    SKILL.md
```

**AGENTS.md** is the agent's system prompt, written in Markdown. It defines persona, guidelines, constraints, and default behaviors. The agent loads `.agents/AGENTS.md` automatically when the sandbox starts.

```markdown
# Data Analyst Agent

You are a meticulous data analyst. When given a data task:

1. Always validate input data before processing
2. Document assumptions in a NOTES.md file
3. Write all output to the /output directory
4. Include row counts and null value counts in any CSV summary

Never modify source files. Work only with copies.
```

**SKILL.md** defines a reusable capability that can be discovered via the Skill Registry:

```markdown
# Skill: CSV Summarizer
Description: Reads a CSV file and produces a structured summary with row counts, 
column types, null percentages, and min/max/mean for numeric columns.

Input: path to CSV file
Output: summary.md written to the working directory
```

Register the configuration to the Skill Registry and invoke your custom agent by its registered ID:

```python
interaction = client.interactions.create(
    agent="my-data-analyst-v1",   # your registered agent ID
    input="Process the uploaded Q1_revenue.csv"
)
```

---

## Pricing

**During preview:** Compute is free. Sandbox CPU, memory, and execution time are not billed. You pay only for token usage at standard Gemini 3.5 Flash rates:

| Resource | Price |
|---|---|
| Input tokens | $1.50 / 1M tokens |
| Output tokens | $9.00 / 1M tokens |

**After preview:** Billing will extend to Sessions, Code Execution, and Memory Bank at rates to be announced. Google has not published post-preview compute pricing as of this writing. Budget accordingly — the current free-compute period is a preview incentive, not the production pricing model.

Google Search calls within the sandbox are billed per-query at standard Gemini API Search grounding rates.

---

## Managed Agents vs. AgentCore: A Decision Framework

Both services exist to remove agent infrastructure work from builders. They differ significantly in execution model, ecosystem, and where in the stack they operate.

| | Google Managed Agents | AWS AgentCore |
|---|---|---|
| **Isolation model** | Shared Linux sandbox per session | Per-session microVM (Firecracker) |
| **Session duration** | TBD (preview) | 8 hours max |
| **Base model** | Gemini 3.5 Flash only (preview) | Any Bedrock model; OpenAI preview |
| **Framework support** | Antigravity harness (built-in) | LangGraph, CrewAI, LlamaIndex, Strands, custom |
| **Entry requirement** | Gemini API key | AWS account + IAM |
| **Compute billing** | Free during preview | $0.0895/vCPU-hr + $0.00945/GB-hr |
| **Governance** | Google API security model | IAM, PrivateLink, CloudTrail, Guardrails |
| **Network** | Disabled by default; domain allowlist | Configurable per agent |
| **Best fit** | Prototyping, Google-native stacks, quick deployment | Enterprise, model-agnostic, regulated workloads |

**Use Managed Agents when:**
- You are already using Gemini 3.5 Flash and want the shortest path to production
- Your task fits a general-purpose autonomous agent without needing a specific framework
- You are in early development and want free sandbox compute during preview
- You want configuration-as-code via AGENTS.md without orchestration code

**Use AgentCore when:**
- You are AWS-native and need IAM, PrivateLink, CloudTrail audit trails
- You need model flexibility — GPT-5.5, Nova, or other Bedrock models
- You have existing LangGraph, CrewAI, or LlamaIndex code you want to host
- You need per-user microVM isolation with guaranteed session duration guarantees
- Your workload requires more than 8 hours of continuous execution

---

## Preview Constraints

Before building on Managed Agents for production workloads, note the current limitations:

- **Single base agent:** Only `antigravity-preview-05-2026` is available. You can customize via AGENTS.md and system instructions, but cannot bring your own model or framework.
- **Preview stability:** The API surface, environment behavior, and pricing can all change. Google has not announced a GA timeline.
- **Network defaults:** Outbound network access is off by default. Any external API calls require domain allowlist configuration.
- **Gemini 3.5 Flash only:** No access to Gemini 3.5 Pro or other models during preview. Tasks requiring deeper reasoning than Flash provides cannot currently be routed to a more capable model within the Managed Agents API.
- **No usage dashboard yet:** Token and session usage reporting in AI Studio does not yet break out Managed Agents separately from standard Gemini API usage.

---

## Getting Started

Managed Agents require a standard Gemini API key — the same key used for any Gemini API call. No Vertex AI project, no Google Cloud billing account, no additional setup.

```bash
export GEMINI_API_KEY=your_key_here
pip install google-genai
python your_agent_script.py
```

The API is available through Google AI Studio for prototyping and through the `google-genai` SDK for code. You can also test the Antigravity agent directly in the AI Studio Playground before writing any code.

For enterprise workloads requiring the full compliance and governance stack (VPC, audit logging, custom networking), the equivalent service is Managed Agents on Gemini Enterprise Agent Platform, accessed through the Google Cloud Console — not the Gemini API. The same conceptual model applies, but the access path, billing, and isolation guarantees differ.
