---
title: "Claude Managed Agents Now Has Cron Scheduling and Vault Credentials"
date: 2026-06-11
description: "Anthropic shipped two new Managed Agents capabilities on June 9: scheduled deployments that run sessions on a cron schedule without a custom scheduler, and vault environment variables that inject secrets into the agent sandbox without exposing them to the model. Both are in public beta."
og_description: "Claude Managed Agents June 9 update: cron-scheduled agent runs and vault-backed credential injection. No scheduler to host. No API keys in prompts. Here's what changed and how to use it."
content_type: "Builder's Log"
categories: ["Agents", "Anthropic", "Infrastructure"]
tags: ["claude", "managed-agents", "scheduling", "cron", "vault", "credentials", "api-keys", "automation", "infrastructure", "anthropic", "builder-guide", "june-2026"]
---

Anthropic shipped two new Claude Managed Agents capabilities on June 9, 2026, alongside the Claude Fable 5 launch. Neither of them made the main announcement headline, but both address recurring operational pain points for builders running agents in production.

**Scheduled deployments** let you run a managed agent session on a cron schedule without owning any scheduler infrastructure.

**Vault environment variables** let you inject API keys and other secrets into the agent's sandbox at execution time, without the model ever seeing the actual credential.

Both are in public beta under the standard `managed-agents-2026-04-01` beta header.

---

## Scheduled Deployments

### What It Does

A scheduled deployment is a Claude Managed Agents deployment that fires automatically on a cron schedule. Each time the schedule triggers, the agent starts a new session and executes its task from scratch. When the task completes, the session ends. No session is left open between runs.

You can:
- Pause a scheduled deployment without deleting it
- Resume a paused deployment
- Archive a completed or decommissioned deployment
- Manually trigger a run outside the schedule (useful for testing or one-off executions)

### What Problem This Solves

Before June 9, if you wanted to run a managed agent on a recurring basis — a nightly data sync, a weekly compliance scan, a daily digest — you needed something outside the agent to fire the trigger. That meant building or hosting your own scheduler: a cron job on a server, a cloud functions trigger, a workflow engine task, or a third-party platform integration.

Anthropic's managed scheduler eliminates that external dependency for the most common case. If your use case fits a cron expression and doesn't require cross-system coordination at trigger time, you no longer need to maintain the scheduler layer.

### What This Does Not Cover

Cron scheduling is not event-driven scheduling. If you need an agent to run when a file is uploaded, when a webhook arrives, or when another system emits a signal — that is a different architecture. Scheduled deployments are for time-based recurrence, not event-based triggers.

Anthropic has not published rate limits on how frequently you can schedule runs, maximum concurrent scheduled deployments per workspace, or what happens when a run overruns its scheduled interval. These are reasonable questions for production planning. Check the [scheduled deployments documentation](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments) before committing to a deployment cadence.

---

## Vault Environment Variables

### What It Does

Claude Managed Agents vaults have supported OAuth credentials for some time. The June 9 update extends vault support to environment variable credentials: API keys, tokens, and other secrets that services expect to find in environment variables at runtime.

The mechanism works in two stages:

1. You add the credential to your vault and attach it to a deployment by reference. The deployment configuration stores the vault reference, not the secret value.
2. When the agent session starts, the sandbox receives an environment variable with a placeholder value. At the network boundary — before requests leave the sandbox to reach the approved domain — the platform substitutes the actual credential.

The model running in the session never sees the actual API key. It sees the placeholder, which doesn't work if extracted and used outside the authorized context.

### Supported Services

The launch documentation lists the following CLIs and services as supported vault credential targets: Browserbase, KERNEL, Notion, Ramp, and Sentry.

These represent the services that authenticate via HTTP headers or environment variable injection and have been validated against Anthropic's domain restriction framework. The list will expand; if a service you need is not on it, that is a constraint to track.

### What Problem This Solves

The naive approach to giving an agent access to an external service is to include the API key in the system prompt or task definition. This works but creates real risks:

- The model can output the key in a response or tool call
- The key exists in plaintext in your deployment configuration
- Prompt injection attacks against the agent can attempt to exfiltrate credentials

Vault credential injection moves the secret out of the model's context entirely. The agent can use the credential (through tool calls that execute authenticated requests) without the credential being available to the model as text it could output, log, or be manipulated into revealing.

For teams that have done security reviews of managed agent deployments and received objections about credential handling, this directly addresses the plaintext-in-prompt concern.

### What to Watch

Vault environment variable support launched alongside a specific list of supported integrations. If your workflow depends on a service not in that list, you're back to the plaintext-or-OAuth alternatives while you wait for coverage to expand. Keep an eye on the [vaults documentation](https://platform.claude.com/docs/en/managed-agents/vaults#add-a-credential) for new additions.

---

## The Cumulative Picture of Managed Agents

It's worth stepping back to see what the feature set looks like now:

| Capability | Status as of June 11 |
|---|---|
| Agent loop infrastructure (session management, context tracking) | GA |
| Public beta (standard usage) | GA |
| Webhooks and multi-agent orchestration | Public beta |
| Outcomes (success criteria definition) | Public beta |
| Memory across sessions | Public beta |
| Self-hosted sandboxes | Public beta |
| MCP tunnels (private network access) | Research preview |
| OAuth vault credentials | Public beta |
| **Scheduled deployments** | **Public beta (new June 9)** |
| **Vault environment variable credentials** | **Public beta (new June 9)** |

The trajectory is toward a complete infrastructure layer: Anthropic handles the agent loop, you define the task, the platform handles scheduling, secrets management, tool execution environment, and observability. The credential and scheduling updates push further in that direction by eliminating two common reasons to build infrastructure adjacent to your managed agent.

---

## The Deployment Before and After

**Before June 9**, a recurring managed agent task required:

```
Your scheduler (cron job / cloud function / workflow engine)
  → triggers your API call
    → starts Claude Managed Agents session
      → agent runs with API keys injected via system prompt or environment setup code
```

**After June 9**, for use cases that fit the new features:

```
Claude Managed Agents scheduled deployment (cron)
  → starts fresh session automatically
    → vault injects credentials at network boundary
      → agent runs; model never touches the actual keys
```

Two fewer layers to own. Two fewer things that can break at 3am.

---

## Availability

Both features are in public beta and available to Claude for Work and enterprise plan customers. Access requires the `managed-agents-2026-04-01` beta header on API calls.

Anthropic does not have a stated GA date for either feature.

---

*ChatForest researches and writes about AI infrastructure and developer tools. We have not tested these features directly and rely on Anthropic's official documentation and release notes. [Rob Nugen](https://robnugen.com) operates ChatForest.*
