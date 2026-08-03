---
title: "Vercel's Production Agent Stack: AI SDK 7, eve, Connect, and Agent Run Observability — Builder Guide"
date: 2026-07-04
description: "Vercel's full production agent toolkit landed in June–July 2026: AI SDK 7 adds WorkflowAgent and tool approvals, eve turns agents into directories, Connect ends long-lived secrets, and the new Agent Runs MCP tools expose full trace data. Here is how the pieces fit together."
tags: ["vercel", "ai-sdk", "agents", "mcp", "typescript", "javascript", "observability", "eve"]
sources_audited: 2026-08-03
---

Vercel's agent story has shifted from infrastructure to a complete production toolkit. At [Ship London](https://vercel.com/ship/london) (June 17, 2026) the company launched [AI SDK 7](https://vercel.com/changelog/ai-sdk-7), the [eve agent framework](https://vercel.com/blog/introducing-eve), and [Vercel Connect](https://vercel.com/blog/introducing-vercel-connect) in a single event. [Vercel Services](https://vercel.com/blog/vercel-ship-2026-recap) went live July 1. [Agent Run observability via MCP](https://vercel.com/changelog/agent-runs-vercel-mcp-cli) arrived July 3. This guide maps each piece and shows how they connect.

---

## The four pieces

| Layer | What it is | Status |
|---|---|---|
| **AI SDK 7** | Provider-agnostic agent runtime — WorkflowAgent, tool approvals, HarnessAgent | GA |
| **eve** | Open-source directory-based agent framework that deploys on Vercel | [Beta](https://github.com/vercel/eve) ([Apache 2.0](https://github.com/vercel/eve/blob/main/LICENSE)) |
| **Vercel Connect** | Task-scoped short-lived credentials for third-party APIs | Public Beta |
| **Agent Run Observability** | MCP tools to query eve agent traces and token usage | [Shipped July 3](https://vercel.com/changelog/agent-runs-vercel-mcp-cli) |

---

## AI SDK 7

### What changed from v6

AI SDK 7 is a major version. The three changes most likely to affect you:

**Node.js 22 and ESM are now required.** Earlier LTS versions are unsupported. All imports must use ESM syntax (`import`) or `.mjs` files.

**Three APIs renamed:**
- `system` → `instructions`
- `onFinish` → `onEnd`
- `StreamTextResult.fullStream` → `stream`

**Run the codemod first:**
```bash
npx @ai-sdk/codemod v7
```

The codemod handles the straightforward renames automatically. After running it, do a manual pass for the semantic changes (tool approval policy, telemetry setup).

### WorkflowAgent: durable execution

The biggest addition. A `ToolLoopAgent` runs entirely in memory — if the process dies, the run is gone. [`WorkflowAgent` runs inside a Vercel Workflow](https://ai-sdk.dev/v7/docs/agents/workflow-agent), so each tool execution is a durable step with automatic retries (3 attempts by default) and state persistence.

Use `WorkflowAgent` when your agent tasks take more than a few seconds, involve external APIs that can fail, or need human-in-the-loop approval at checkpoints.

### Tool approvals

v7 replaces the per-tool `needsApproval` flag with a policy parameter at the agent level:

```typescript
const agent = new ToolLoopAgent({
  model,
  tools,
  toolApproval: {
    policy: 'user-approval',        // or 'auto-approve', 'auto-deny', custom function
    onApproval: async (toolCall) => {
      // notify user, wait for response
    },
  },
});
```

Four policies: `user-approval`, `auto-approve`, `auto-deny`, or a custom function that receives the tool call and returns `approved | denied | pending`.

### HarnessAgent: wrap external agents

New in v7 — `HarnessAgent` wraps external agent runtimes (Claude Code, Codex, Deep Agents, OpenCode, Pi) behind the AI SDK interface. Your orchestration layer stays provider-agnostic even when delegating to specialized coding agents.

### MCP Apps

[AI SDK 7 adds MCP Apps](https://vercel.com/changelog/ai-sdk-7): MCP support that distinguishes model-visible from app-only tools and uses tool metadata to render app-specific UI inside sandboxed iframes, communicating over JSON-RPC for tools, resources, logs, and display updates — so a builder can ship an interactive tool UI without the user leaving an MCP-compatible client.

### Observability

The [`@ai-sdk/otel` package](https://vercel.com/changelog/ai-sdk-7) is now the standard path for OpenTelemetry. Every operation — model call, tool execution, step start/end — emits a span.

```typescript
import { generateText, registerTelemetry } from 'ai';
import { OpenTelemetry } from '@ai-sdk/otel';
registerTelemetry(new OpenTelemetry());
```

Separately, step results now expose their own timing and throughput fields directly — response time, total step time, tool execution time, time to first output, and output tokens per second — available via lifecycle callbacks whether or not you've wired up OpenTelemetry.

[AI SDK 7 also emits structured telemetry through the Node.js tracing channel](https://vercel.com/changelog/ai-sdk-7), so observability providers can subscribe once and keep async context across streaming and tool execution without an OTel collector if you just need local structured logs.

### Terminal UI for local development

[`@ai-sdk/tui`](https://vercel.com/changelog/ai-sdk-7) gives you a TUI for testing agents locally — inspect every LLM call, tool input/output, and token count in the terminal without setting up a dashboard.

```typescript
import { ToolLoopAgent } from 'ai';
import { runAgentTUI } from '@ai-sdk/tui';

const agent = new ToolLoopAgent({ model: 'openai/gpt-5.5' });
await runAgentTUI({ agent });
```

---

## eve: directory-based agents

### The core idea

An eve agent is a directory:

```
agent/
  agent.ts           # model config
  instructions.md    # system prompt
  tools/             # one .ts file per tool
  skills/            # one .md file per playbook
  connections/       # API and MCP server configs
  channels/          # integration adapters (Slack, Discord, etc.)
  schedules/         # cron automation
  subagents/         # nested agent directories
```

Everything is file-system-first. [Eve](https://vercel.com/blog/introducing-eve) discovers and validates the directory on build, compiles a manifest, and serves it as a durable runtime on Vercel.

### Minimal start

```typescript
// agent/agent.ts
import { defineAgent } from 'eve';
export default defineAgent({
  model: 'anthropic/claude-opus-4.8',
});
```

Add `agent/instructions.md` as the system prompt. Tools are individual TypeScript files in `agent/tools/` — each file exports one function and its schema. Skills are Markdown files in `agent/skills/` that the agent retrieves on demand.

### Deploy

```bash
vercel deploy
```

No additional configuration: an eve agent is [an ordinary Vercel project](https://vercel.com/blog/introducing-eve), so it deploys the way any other frontend or backend does. Durable execution runs on the open-source Workflow SDK, and the sandbox adapter swaps to Vercel Sandbox without a code change. Local and production environments use identical code.

### Channels and integrations

Built-in channels: Slack, Discord, Microsoft Teams, Telegram, Twilio, GitHub, Linear, HTTP API, and custom implementations.

Built-in connections: Slack, GitHub, Snowflake, Salesforce, Notion, Linear, plus generic OAuth and MCP server support.

Activating a channel is one file in `agent/channels/`:

```typescript
// agent/channels/slack.ts
import { defineChannel } from 'eve/channels/slack';
export default defineChannel({ token: process.env.SLACK_TOKEN });
```

---

## Vercel Connect: no long-lived secrets

### The problem it solves

The conventional pattern — store an API token in an environment variable, use it every time the agent needs the third-party service — leaves a standing secret that lives forever and has broad scope. A breach anywhere in the supply chain can expose it.

Connect replaces the stored token with runtime credential exchange. When the agent needs to act, it requests a short-lived credential scoped to that specific task. The token expires when the task completes.

### How it works

1. Register a [connector](https://vercel.com/docs/connect) once in the Vercel dashboard. Slack, GitHub, Snowflake, and Salesforce are natively-managed connector types; anything else (Notion, Linear, etc.) connects via generic Custom OAuth or a static API key.
2. Set permissions at registration time — e.g., a GitHub connector scoped to one repo and read-only.
3. In your agent, the SDK fetches and refreshes tokens automatically at runtime.

No secret to store, rotate, or audit.

### [Pricing](https://vercel.com/docs/connect/pricing)

| Plan | Included | Overage |
|---|---|---|
| Hobby | 5,000 token requests/month | — |
| Pro / Enterprise | — | $3 per 10,000 token requests |

---

## Agent Run Observability via MCP

[Added July 3](https://vercel.com/changelog/agent-runs-vercel-mcp-cli), the Vercel MCP server now includes four Agent Runs tools. Any MCP-compatible client (Claude Code, Cursor, etc.) can query your eve agent's production behavior directly in the same context as your code.

### [Setup](https://vercel.com/docs/agent-resources/vercel-mcp)

```bash
npx add-mcp https://mcp.vercel.com
```

This detects your installed AI clients and configures the Vercel MCP server for each one (Claude Code, Cursor, and others each have their own one-line variant in Vercel's docs). The four new tools:

**`list_agent_run_projects`** — find all projects in your team with eve agent activity. Returns run counts and average durations per project.

**`list_agent_runs`** — paginated list of runs for a project, with status, model, trigger, token usage, and time series.

**`get_agent_run`** — metadata for a single run: events, workflow metadata, usage, and subagent breakout.

**`get_agent_run_trace`** — full trace: every turn, message, reasoning step, tool call, and token count. Use this to debug unexpected behavior in production.

### Practical debugging workflow

When an eve agent does something unexpected in production:

1. `list_agent_runs` — find the run by time range or search
2. `get_agent_run_trace` — inspect the full message sequence and tool calls
3. Compare against your `agent/tools/` source to find the divergence

This replaces the previous pattern of adding `console.log` to tools and redeploying to reproduce.

---

## How the pieces fit

A typical production eve agent uses all four layers:

- **AI SDK 7 WorkflowAgent** handles durable execution so multi-step tasks survive crashes and support human approval gates.
- **eve** provides the directory structure, channel adapters, and `vercel deploy` path.
- **Vercel Connect** gives the agent's tools task-scoped credentials for GitHub, Slack, Notion, etc., without storing long-lived secrets.
- **Agent Run MCP tools** let you inspect production traces without leaving your coding environment.

For prototyping or simple automations, eve alone with standard API keys is sufficient. Connect becomes worth adding when you have multiple tools accessing the same third-party services or when audit trails matter.

---

## Migration notes for existing AI SDK 6 users

1. Update Node.js to 22+
2. Switch to ESM (`"type": "module"` in `package.json`, or rename files to `.mjs`)
3. Upgrade packages: `npm install ai@7 @ai-sdk/anthropic@latest @ai-sdk/openai@latest`
4. Run `npx @ai-sdk/codemod v7` for mechanical renames
5. Replace `needsApproval` per-tool with a `toolApproval` policy on the agent
6. Migrate telemetry from `experimental_telemetry` to `@ai-sdk/otel`

The codemod handles most steps 4 and 5 automatically, but review its output before committing.

---

## What to watch

- **eve is still in beta**: [Vercel's own repo says as much](https://github.com/vercel/eve) — "the framework, APIs, documentation, and behavior may change before general availability." There's no 1.0 release yet; treat directory structure and connection configs as subject to change.
- **Vercel Connect GA**: currently Public Beta; pricing may adjust at GA.
- **HarnessAgent**: [AI SDK 7's release notes](https://vercel.com/changelog/ai-sdk-7) list Claude Code, Codex, Deep Agents, OpenCode, and Pi adapters together with no stated distinction in maturity between them — worth verifying directly against your target runtime before depending on one in production.

---

*Research note: this guide is based on Vercel's published documentation, changelog, and Ship 2026 recap. ChatForest has not deployed or tested this stack independently.*
