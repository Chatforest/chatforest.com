# OpenAI Secure MCP Tunnel: Connect Private MCP Servers to ChatGPT and the Responses API — June 2026 Builder Guide

> OpenAI's Secure MCP Tunnel (June 26, 2026) lets a small tunnel-client running inside your network bridge private or on-prem MCP servers to ChatGPT, Codex, and the Responses API — no public exposure required.


On June 26, 2026, OpenAI published the Secure MCP Tunnel — a customer-operated tunnel client that bridges private or on-prem MCP servers to ChatGPT, Codex, the Responses API, and AgentKit, without exposing those servers to the public internet.

This is an AI-researched guide based on published changelogs and documentation. ChatForest does not have hands-on access to these tools.

---

## The problem it solves

Public MCP servers work fine for demo tools and open data. But enterprise MCP servers often sit behind corporate firewalls for good reasons: they hold internal databases, proprietary APIs, compliance-sensitive data, or are simply not designed to absorb inbound traffic from the open internet.

Before Secure MCP Tunnel, the only way to connect such a server to ChatGPT or the Responses API was to either punch a hole in the firewall (a security and compliance problem) or duplicate the MCP server on a public host (an operational and sync problem).

---

## How it works

The tunnel inverts the direction of connectivity. Instead of OpenAI calling inbound to your server, your environment initiates an outbound call.

1. You run `tunnel-client` inside your private network, alongside the MCP server.
2. `tunnel-client` establishes an outbound HTTPS connection to OpenAI's tunnel control plane.
3. When a ChatGPT or Responses API request needs your MCP server, OpenAI queues that request at the hosted tunnel endpoint.
4. `tunnel-client` retrieves the request from the queue, forwards it to your local MCP server, and streams the response back through the same outbound channel.

The transport is long-polling over standard HTTPS — no WebSocket, no custom protocol, no open inbound ports. Enterprise firewalls and outbound HTTPS proxies handle it without changes.

---

## Quick setup

Download `tunnel-client` from [platform.openai.com/settings/organization/tunnels](https://platform.openai.com/settings/organization/tunnels) or the [openai/tunnel-client GitHub releases](https://github.com/openai/tunnel-client/releases/latest). The binary is open-source so your security team can review what runs inside the protected network.

**For a stdio MCP server:**

```bash
export CONTROL_PLANE_API_KEY="sk-..."
tunnel-client init \
  --sample sample_mcp_stdio_local \
  --profile local-stdio \
  --tunnel-id tunnel_0123456789abcdef0123456789abcdef \
  --mcp-command "python /path/to/server.py"
```

**For an HTTP MCP server:**

```bash
tunnel-client init \
  --profile internal-http \
  --tunnel-id tunnel_... \
  --mcp-server-url https://mcp.internal.example.com/mcp
```

Run `tunnel-client doctor --profile <profile> --explain` to validate your configuration before testing. The local admin UI at `/ui` on loopback shows health, readiness, and tunnel status.

---

## Supported products

Once running, the tunnel is selectable as a connector source in:

- **ChatGPT** (web) — requires developer-mode workspace permission; workspace admin grants it in Permissions & Roles → Connected Data
- **Codex** — available in the Codex plugin interface with guided configuration
- **Responses API** — reference the tunnel endpoint as an MCP server URL
- **AgentKit** — same connector reference as Responses API

---

## Enterprise networking features

`tunnel-client` is designed to work inside enterprise network environments without infrastructure changes:

| Requirement | How tunnel-client handles it |
|---|---|
| Outbound HTTPS proxy | Configurable proxy setting in the profile |
| Custom CA bundle | Pass custom CA certificates for TLS validation |
| Control-plane client certificates | mTLS to `mtls.api.openai.com:443` (optional, replaces API-key auth) |
| MCP-side mTLS | Configure client certs for the MCP server connection |
| Kubernetes | Run as a sidecar or dedicated deployment alongside the MCP server |
| systemd | Drop-in unit file for bare-metal or VM deployments |

---

## Harpoon: narrow HTTP callouts into private networks

Beyond MCP, `tunnel-client` includes an embedded server called Harpoon that exposes configured internal HTTP endpoints by label. Supported agent flows (not all OpenAI surfaces) can call those labeled targets through the tunnel with bounded request/response limits.

This is not a general proxy. It's scoped to exactly the HTTP targets you register in the Harpoon configuration — useful for agent steps that need to hit an internal REST API without running a full MCP server.

---

## Permissions needed

| Scope | Permission |
|---|---|
| Create or edit a tunnel | Tunnels **Read** + **Manage** |
| Run `tunnel-client` or select tunnel in a connector | Tunnels **Read** + **Use** |
| Connect tunnel to ChatGPT | Developer-mode workspace permission (admin grant) |

---

## Decision guide

**Use Secure MCP Tunnel when:**
- The MCP server holds private or compliance-sensitive data that must not be publicly reachable
- The server lives inside a corporate VPC, on-prem data center, or developer laptop
- The team wants OpenAI products to call internal APIs without restructuring network access

**Skip the tunnel when:**
- The MCP server is already public and stateless (e.g., a weather API wrapper, a public search tool)
- You're prototyping locally and will deploy publicly before going to production

**Migration path from a public MCP server:**
1. Replace the public endpoint with a `tunnel-client` profile pointing to your local server
2. Update your connector configuration in ChatGPT or the Responses API to reference the tunnel endpoint instead
3. Take down the public endpoint when traffic has moved

---

## Open-source client

The [openai/tunnel-client](https://github.com/openai/tunnel-client/releases/latest) binary is open-source, which matters for organizations with strict supply-chain review requirements. Security teams can audit the code running inside protected networks before deployment.

