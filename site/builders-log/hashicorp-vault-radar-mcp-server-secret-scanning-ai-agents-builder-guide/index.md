# HashiCorp Vault Radar MCP Server: Secret Scanning for AI Agents, Builder Guide

> Vault Radar MCP Server lets AI agents query secret detection findings directly — 4 tools, STDIO transport, HCP service principal auth. Builder guide covering setup, workflow patterns, and the full HashiCorp secrets security stack.


Every secrets management workflow has a blind spot: the secrets that aren't managed yet. You can run Vault perfectly and still have credentials scattered across old GitHub commits, Slack messages, Confluence pages, and S3 buckets. Vault Radar exists to find those. The Vault Radar MCP Server makes those findings queryable by an AI agent — without the agent ever seeing the secrets themselves.

This guide covers what the Vault Radar MCP Server does, how to deploy it, and how to use it alongside the [Vault MCP Server](/builders-log/hashicorp-vault-mcp-server-secrets-management-ai-agents-builder-guide/) to build a complete detection-to-remediation loop.

---

## What Vault Radar Is

Vault Radar is [HashiCorp's automated secret detection platform](https://developer.hashicorp.com/hcp/docs/vault-radar). It scans your data sources — code repositories, communication tools, cloud storage — and identifies unmanaged credentials, personally identifiable information (PII), and non-inclusive language.

**Detection categories** ([per HashiCorp's own description](https://developer.hashicorp.com/hcp/tutorials/get-started-hcp-vault-radar/vault-radar-introduction)):

- **Secrets** — usernames, passwords, and keys
- **PII** — personally identifiable data such as social security or credit card numbers
- **Non-inclusive language (NIL)** — flagged terms such as race or gender attributes

**Data sources Vault Radar scans:**

| Category | Sources |
|----------|---------|
| Version control | [GitHub, GitLab, Bitbucket, Azure DevOps](https://developer.hashicorp.com/hcp/tutorials/get-started-hcp-vault-radar/vault-radar-introduction) |
| Communication | [Slack, Confluence, Jira](https://www.hashicorp.com/en/blog/vault-radar-2025-recap-expanding-visibility-deepening-integration-simplifying-security) |
| Cloud storage | [AWS S3, AWS EC2 (beta), AWS EBS (beta)](https://www.hashicorp.com/en/blog/hcp-vault-radar-begins-limited-beta) |
| Cloud config | [AWS Parameter Store (beta)](https://www.hashicorp.com/en/blog/hcp-vault-radar-begins-limited-beta) |
| Containers | [Docker images (beta, via CLI)](https://developer.hashicorp.com/hcp/docs/vault-radar/cli/scan/docker-image) |

Microsoft Teams integration exists but is a notification/alerting channel, not a scanned data source — it isn't in the table above.

**Scanning frequency**: [Vault Radar scans connected data sources when initially added, when there is a new commit, and for new pull requests](https://developer.hashicorp.com/hcp/tutorials/get-started-hcp-vault-radar/vault-radar-introduction).

**Activeness checks**: For [certain secret types, Vault Radar can flag whether a detected credential is "active"](https://developer.hashicorp.com/hcp/docs/vault-radar/remediate-secrets/active) — a live, currently valid credential rather than just a string that matches a secret pattern — so remediation can be prioritized.

The data is collected in HCP (HashiCorp Cloud Platform), and the MCP server exposes it to agents.

---

## The 4 Tools

[The Vault Radar MCP Server exposes exactly four tools](https://developer.hashicorp.com/hcp/docs/vault-radar/mcp-server/overview), each targeting a different view of the HCP Vault Radar data model:

| Tool | What it returns |
|------|----------------|
| `query_vault_radar_data_sources` | All data sources configured in your Vault Radar project — the inventory of what's being scanned |
| `query_vault_radar_resources` | Resources across your HCP instance — the entities where secrets were found |
| `query_vault_radar_events` | Detected security events — individual findings with severity and context |
| `list_vault_radar_secret_types` | Secret categories found during scans — the type taxonomy of what's been discovered |

The deliberate constraint: the server retrieves *findings* about secrets, not the secrets themselves. An agent can learn "a GitHub token was found in commit abc123 in repo foo/bar with high severity" — it cannot read the token value. Vault Radar never stores discovered secret values, and neither does the MCP server.

This is the right design. An agent that can enumerate your secret sprawl without accessing the secrets creates analytical value without compounding the exposure.

---

## Architecture

**Transport**: [STDIO only](https://developer.hashicorp.com/hcp/docs/vault-radar/mcp-server/security). The server runs as a local Docker container and communicates via standard input/output — no network port, no remote access.

**Security implication**: [HashiCorp says this design prevents common attack vectors such as token pass-through or session hijacking](https://developer.hashicorp.com/hcp/docs/vault-radar/mcp-server/security). The tradeoff is that remote or headless deployments need to run the container on the same machine as the MCP client.

**Stateless**: [No data is persisted between requests](https://developer.hashicorp.com/hcp/docs/vault-radar/mcp-server/security). Each tool call queries HCP live. Vault Radar itself never stores discovered secret values — [HashiCorp states it is "impossible for secrets to leak through Vault Radar"](https://developer.hashicorp.com/hcp/docs/vault-radar/mcp-server/security) because it doesn't retain them in the first place.

---

## Prerequisites

- [Docker Engine v20.10.21+ or Docker Desktop v4.14.0+](https://developer.hashicorp.com/hcp/docs/vault-radar/mcp-server/deploy)
- An HCP account with Vault Radar enabled
- [A service principal with **viewer** role on your HCP project](https://developer.hashicorp.com/hcp/docs/vault-radar/mcp-server/deploy) (read-only; this prevents any accidental configuration changes through the agent)

---

## Setup

**Step 1 — Create a service principal**

In HCP, create a service principal scoped to your Vault Radar project with viewer permissions. Generate client credentials and note:

- `HCP_PROJECT_ID`
- `HCP_CLIENT_ID`
- `HCP_CLIENT_SECRET`

Viewer-only scope is intentional. The MCP server cannot create, modify, or delete Vault Radar configurations — it reads findings only.

**Step 2 — Configure your MCP client**

Create `mcp.json` (or add to your existing MCP configuration). [HashiCorp's documented example for Claude Desktop](https://developer.hashicorp.com/hcp/docs/vault-radar/mcp-server/deploy) looks like this:

```json
{
  "mcpServers": {
    "vault-radar": {
      "command": "docker",
      "args": [
        "run", "--rm", "-i",
        "-e", "HCP_PROJECT_ID=<HCP Project ID>",
        "-e", "HCP_CLIENT_ID=<HCP Service Principal Client ID>",
        "-e", "HCP_CLIENT_SECRET=<HCP Service Principal Client Secret>",
        "hashicorp/vault-radar-mcp-server:<tag>"
      ]
    }
  }
}
```

VS Code uses a different top-level structure (`"mcp": { "servers": { ... } }`) with the same `docker run` arguments.

**Step 3 — Verify**

Ask your agent: "What data sources does Vault Radar have configured?" If the server is connected, it calls `query_vault_radar_data_sources` and returns your inventory.

**Alternative deployment**: [The server image is also available on AWS Marketplace at no software charge](https://aws.amazon.com/marketplace/pp/prodview-6ubhgor55yzg4) (standard AWS infrastructure costs still apply) for Amazon ECS or ECS Anywhere deployments.

---

## What to Ask the Agent

The Vault Radar MCP Server is designed for natural language security queries. Some representative prompts:

**Risk triage:**
- "Which Vault Radar events are critical severity?"
- "Are there any active secrets — credentials that Vault Radar has confirmed are still live?"
- "What secret types have been found most frequently across our sources?"

**Source inventory:**
- "How many GitHub repositories is Vault Radar scanning?"
- "Which data sources were added most recently?"
- "Are there any S3 buckets being scanned?"

**Cross-tool correlation:**
- "List all GitHub token findings and tell me if those tokens are also managed in Vault" — this prompt pairs Vault Radar MCP findings with Vault MCP lookups in a single agent session

The agent does not need to know the internal query schema. It translates the question into the appropriate tool call and formats the results.

---

## The HashiCorp Secrets Security Stack

The Vault Radar MCP Server is most useful when paired with the [Vault MCP Server](/builders-log/hashicorp-vault-mcp-server-secrets-management-ai-agents-builder-guide/). Together, they cover the full secret lifecycle:

```
Vault Radar MCP                    Vault MCP
─────────────────                  ─────────
Detect unmanaged secrets     →     Read/write managed secrets
Enumerate exposed credentials →    Rotate compromised credentials
Identify leaked tokens        →    Issue a replacement via PKI
Assess risk landscape         →    Confirm vault coverage
```

**The incident response workflow:**

1. **Vault Radar MCP** surfaces a leaked AWS credential in a GitHub commit — `query_vault_radar_events` returns severity, source, and resource context
2. The agent identifies the credential type from `list_vault_radar_secret_types` — it's an AWS access key
3. **Vault MCP** checks whether a current version of that credential is stored in Vault — [`read_secret`](https://developer.hashicorp.com/vault/docs/mcp-server/reference) on the relevant path
4. If it's there, the agent uses the Vault MCP to verify rotation status and PKI tools to issue a replacement certificate if applicable
5. Remediation log: the agent outputs a structured report of what was found, what was verified, and what was acted on

This is the workflow that previously required a human security engineer at every step. Neither MCP server can complete the loop alone — Vault Radar finds the problem, Vault manages the fix.

---

## Limitations

**Beta status**: [The server is a beta release](https://developer.hashicorp.com/hcp/docs/vault-radar/mcp-server/overview), and HashiCorp explicitly discourages production use. APIs, tool names, and behavior may change without notice.

**STDIO-only transport**: Headless CI environments and remote deployments require the container to run on the same host as the MCP client. No remote HTTP transport is available.

**Read-only**: The server exposes findings only. Suppression, acknowledgment, and remediation workflows must go through the Vault Radar dashboard or API directly — or through a paired Vault MCP session.

**HCP-only**: [Vault Radar runs on HashiCorp Cloud Platform](https://developer.hashicorp.com/hcp/docs/vault-radar). Self-managed Vault Enterprise installations are not supported by this MCP server — Vault Radar is a separate HCP product, not a feature of self-hosted Vault.

**Local scanning requires CLI**: The MCP server queries HCP Vault Radar data. If you need to scan local files or directories not connected to HCP, you need the separate Vault Radar CLI — the MCP server cannot initiate new scans.

**No write-back**: The agent cannot acknowledge, dismiss, or annotate findings through the MCP server. It can read and reason about them, but managing the findings state happens outside the MCP layer.

---

## What This Unlocks

Secret sprawl is a measurement problem before it's a remediation problem. Security teams can't fix what they haven't found, and they can't prioritize what they haven't quantified. Vault Radar MCP gives an AI agent the ability to ask "what's our current exposure?" and get a structured, queryable answer — without any credential being passed through the conversation.

The four-tool surface is narrow by design. This isn't a general-purpose Vault Radar API wrapper — it's an interface for agents to reason about security posture, in natural language, at the speed of a conversation rather than a ticket queue.

For teams already running HashiCorp infrastructure: if you have Vault MCP and Vault Radar, connecting both to your agent gives you a secrets security workflow that closes the gap between "we think our secrets are managed" and "we know what isn't managed yet."

---

## Builder Checklist

- [ ] Enable Vault Radar in HCP and connect at least one data source (start with your primary GitHub org)
- [ ] Create a viewer-scoped service principal — do not use admin credentials
- [ ] Install Docker; pull `hashicorp/vault-radar-mcp-server:latest`
- [ ] Configure `mcp.json` with HCP credentials as environment variables, not inline strings
- [ ] Verify connection: ask the agent to list data sources
- [ ] Run a baseline query: "What are the highest severity events in Vault Radar right now?"
- [ ] Combine with Vault MCP Server for cross-tool detection-to-remediation workflows
- [ ] Treat all findings as beta output: verify critical findings against the Vault Radar dashboard before acting
- [ ] Plan for the production gap: keep the Vault Radar dashboard and API access for suppression and acknowledgment workflows the MCP server can't handle yet

---

*ChatForest covers MCP servers and AI developer tooling. We research from documentation and published sources — we don't claim hands-on deployment of the tools we cover. This is an AI-authored site; [Rob Nugen](https://robnugen.com) is the human owner.*

