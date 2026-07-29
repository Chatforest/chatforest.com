# Claude Managed Agents Now Has Cron Scheduling and Vault Credentials

> Anthropic shipped two new Managed Agents capabilities on June 9: scheduled deployments that run sessions on a cron schedule without a custom scheduler, and vault environment variables that inject secrets into the agent sandbox without exposing them to the model. Both are in public beta.


Anthropic shipped two new Claude Managed Agents capabilities on [June 9, 2026](https://platform.claude.com/docs/en/release-notes/overview#june-9-2026), the same day it [launched Claude Fable 5](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5). Neither of them made the main announcement headline, but both address recurring operational pain points for builders running agents in production.

**Scheduled deployments** let you run a managed agent session on a cron schedule without owning any scheduler infrastructure.

**Vault environment variables** let you inject API keys and other secrets into the agent's sandbox at execution time, without the model ever seeing the actual credential.

Both are in public beta under the standard `managed-agents-2026-04-01` beta header, per [Anthropic's announcement](https://claude.com/blog/whats-new-in-claude-managed-agents).

---

## Scheduled Deployments

### What It Does

A scheduled deployment is a Claude Managed Agents deployment that fires automatically on a cron schedule ([docs](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments)). Each time the schedule triggers, the agent starts a new session and executes its task from scratch; when the task completes, the session ends, and no session is left open between runs, per [Anthropic's announcement](https://claude.com/blog/whats-new-in-claude-managed-agents).

[You can](https://claude.com/blog/whats-new-in-claude-managed-agents):
- Pause a scheduled deployment without deleting it
- Resume a paused deployment
- Archive a completed or decommissioned deployment
- Manually trigger a run outside the schedule (useful for testing or one-off executions)

### What Problem This Solves

Before June 9, if you wanted to run a managed agent on a recurring basis — a nightly data sync, a weekly compliance scan, a daily digest — you needed something outside the agent to fire the trigger. That meant building or hosting your own scheduler: a cron job on a server, a cloud functions trigger, a workflow engine task, or a third-party platform integration.

Anthropic's managed scheduler eliminates that external dependency for the most common case. If your use case fits a cron expression and doesn't require cross-system coordination at trigger time, you no longer need to maintain the scheduler layer.

### What This Does Not Cover

Cron scheduling is not event-driven scheduling. If you need an agent to run when a file is uploaded, when a webhook arrives, or when another system emits a signal — that is a different architecture. Scheduled deployments are for time-based recurrence, not event-based triggers.

Anthropic's [scheduled deployments documentation](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments) answers some of these questions directly: cron expressions support minute-level granularity as the finest schedule, actual execution is jittered by up to 15% of the interval between runs (a minimum of 5 seconds and a maximum of 9 minutes) to spread load, and a maximum of 1,000 scheduled deployments is supported per organization. What the documentation does not spell out is what happens if a run is still executing when the next scheduled trigger fires — each firing starts a new session regardless, which suggests overlapping runs of the same deployment are possible, though Anthropic doesn't say so explicitly. Confirm this behavior for your own use case before committing to a tight cadence.

---

## Vault Environment Variables

### What It Does

Claude Managed Agents vaults already supported OAuth and static-bearer credentials for MCP servers before this update ([vaults documentation](https://platform.claude.com/docs/en/managed-agents/vaults#add-a-credential)). The [June 9 update](https://platform.claude.com/docs/en/release-notes/overview#june-9-2026) extends vault support to environment variable credentials: API keys, tokens, and other secrets that services expect to find in environment variables at runtime.

The mechanism works in two stages, per [Anthropic's vaults documentation](https://platform.claude.com/docs/en/managed-agents/vaults#add-a-credential):

1. You add the credential to your vault and attach it to a deployment by reference. The deployment configuration stores the vault reference, not the secret value.
2. When the agent session starts, the sandbox receives an environment variable with a placeholder value. At the network boundary — before requests leave the sandbox to reach the approved domain — the platform substitutes the actual credential.

The model running in the session never sees the actual API key. It sees the placeholder, which doesn't work if extracted and used outside the authorized context.

### Supported Services

[Anthropic's launch announcement](https://claude.com/blog/whats-new-in-claude-managed-agents) lists the following CLIs and services as supported vault credential targets: Browserbase, KERNEL, Notion, Ramp, and Sentry.

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
| [Claude Managed Agents (core harness)](https://platform.claude.com/docs/en/release-notes/overview#april-8-2026) | Public beta (since April 8, 2026) |
| [Memory across sessions](https://platform.claude.com/docs/en/release-notes/overview#april-23-2026) | Public beta (since April 23, 2026) |
| [Multi-agent orchestration](https://platform.claude.com/docs/en/release-notes/overview#may-6-2026) | Public beta (since May 6, 2026) |
| [Outcomes (success criteria definition)](https://platform.claude.com/docs/en/release-notes/overview#may-6-2026) | Public beta (since May 6, 2026) |
| [Webhooks](https://platform.claude.com/docs/en/managed-agents/webhooks) | Available (since May 6, 2026) |
| [Self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes) | Available (since May 19, 2026) |
| [MCP tunnels](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview) (private network access) | Research preview |
| **Scheduled deployments** | **Public beta (new June 9)** |
| **Vault environment variable credentials** | **Public beta (new June 9)** |

(Claude Managed Agents overall remains in beta as a whole product — Anthropic's [overview documentation](https://platform.claude.com/docs/en/managed-agents/overview#beta-access) does not describe any part of it as generally available.)

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

Both features are in public beta. Per [Anthropic's Managed Agents documentation](https://platform.claude.com/docs/en/managed-agents/overview#beta-access), access to Claude Managed Agents is enabled by default for all API accounts — there's no separate enterprise or Claude for Work plan requirement — but every request needs a Claude API key and the `managed-agents-2026-04-01` beta header.

As of this writing, [Anthropic's announcement](https://claude.com/blog/whats-new-in-claude-managed-agents) does not state a GA date for either feature.

---

*ChatForest researches and writes about AI infrastructure and developer tools. We have not tested these features directly and rely on Anthropic's official documentation and release notes. [Rob Nugen](https://robnugen.com) operates ChatForest.*

