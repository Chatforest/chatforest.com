---
title: "MCP Registry & Server Discovery Guide (2026)"
date: 2026-03-28T14:00:00+09:00
description: "How the MCP Registry works, how to discover servers, how to publish your own, and how enterprises manage private registries. Covers the official registry API and server cards."
content_type: "Guide"
card_description: "The MCP ecosystem now has an official registry for server discovery. Here's how it works and how to use it."
last_refreshed: 2026-03-28
---

The MCP ecosystem hit a turning point in September 2025 when the [MCP Steering Committee launched the official MCP Registry](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/) — an open catalog and API for discovering publicly available MCP servers. Before the registry, finding MCP servers meant browsing GitHub, reading blog posts, or stumbling across mentions in Discord channels. Now there's a single authoritative source, with a standardized API that clients can query programmatically.

This guide covers how the registry works, how to discover servers, how to publish your own, and how enterprises are building private registries on top of it. Our analysis draws on the [official registry documentation](https://registry.modelcontextprotocol.io/docs), the [registry GitHub repository](https://github.com/modelcontextprotocol/registry), and community implementations — we research and analyze rather than testing implementations hands-on.

## Why a Registry Matters

Before the registry, the MCP server ecosystem had a discovery problem. Thousands of servers existed across GitHub, npm, and PyPI, but finding the right one for a specific task required manual research. Different clients maintained their own curated lists. There was no standard way to verify that a server was what it claimed to be.

The registry solves three problems:

1. **Discovery** — a single place to search for servers by name, description, or capability
2. **Trust** — namespace authentication ties servers to verified GitHub accounts or domains
3. **Standardization** — a common API that any client or marketplace can consume

Think of it like npm for MCP servers, but focused on metadata and discovery rather than package hosting. The registry doesn't host server code — it stores metadata that points to where servers are published (npm, PyPI, Docker Hub, etc.).

## The Registry API

The official registry lives at `registry.modelcontextprotocol.io` and exposes a REST API currently at version v0.1 (in API freeze, meaning no breaking changes while v0.2 is developed).

### Listing Servers

```bash
# List the first 10 servers
curl "https://registry.modelcontextprotocol.io/v0.1/servers?limit=10"

# Search for filesystem-related servers
curl "https://registry.modelcontextprotocol.io/v0.1/servers?search=filesystem"
```

Results come back with server metadata including name, description, repository URL, and available packages.

### Pagination

The API uses cursor-based pagination. Each response includes a `nextCursor` value if more results exist:

```bash
# First page
curl "https://registry.modelcontextprotocol.io/v0.1/servers?limit=20"

# Next page (using cursor from previous response)
curl "https://registry.modelcontextprotocol.io/v0.1/servers?limit=20&cursor=abc123"
```

### Server Versions

Each server can have multiple published versions:

```bash
# List all versions of a server
curl "https://registry.modelcontextprotocol.io/v0.1/servers/io.github.modelcontextprotocol/filesystem/versions"

# Get a specific version
curl "https://registry.modelcontextprotocol.io/v0.1/servers/io.github.modelcontextprotocol/filesystem/versions/1.0.0"
```

### The OpenAPI Spec

The registry publishes a complete [OpenAPI specification](https://registry.modelcontextprotocol.io/docs) that any downstream registry can implement. This is intentional — the goal is for the official registry to be one of many registries sharing a common API surface, not the only registry.

## How Server Names Work

MCP server names follow a reverse-DNS namespace format that ties them to verified identities:

- `io.github.username/server-name` — tied to a GitHub account
- `com.example/server-name` — tied to a domain you control

This prevents impersonation. Only the verified owner of a GitHub account or domain can publish servers under that namespace. If someone publishes `io.github.anthropic/filesystem`, you know it actually comes from Anthropic's GitHub organization.

### Namespace Verification

The registry supports three verification methods:

1. **GitHub OAuth** — authenticate with your GitHub account to claim `io.github.{username}` namespaces
2. **GitHub OIDC** — for CI/CD pipelines that need to publish without interactive login
3. **DNS/HTTP verification** — prove domain ownership to claim `com.yourdomain` namespaces (similar to how SSL certificate authorities verify domains)

## Publishing a Server

Publishing to the registry means creating a `server.json` file that describes your server's metadata.

### The server.json Format

```json
{
  "$schema": "https://static.modelcontextprotocol.io/schemas/2025-10-17/server.schema.json",
  "name": "io.github.yourorg/your-server",
  "description": "What your server does",
  "repository": {
    "url": "https://github.com/yourorg/your-server",
    "source": "github"
  },
  "version": "1.0.0",
  "packages": [
    {
      "registryType": "npm",
      "identifier": "@yourorg/your-mcp-server",
      "version": "1.0.0",
      "transport": {
        "type": "stdio"
      }
    }
  ]
}
```

Key fields:

- **name** — the namespaced identifier (must match your verified namespace)
- **packages** — where the actual server code is published (npm, PyPI, Docker, etc.)
- **transport** — how clients connect (stdio, streamable-http, etc.)

### Using mcp-publisher

The `mcp-publisher` CLI tool helps generate and validate server.json files:

```bash
# Initialize a new server.json
npx mcp-publisher init

# Validate your server.json
npx mcp-publisher validate

# Publish to the registry
npx mcp-publisher publish
```

The tool walks you through the namespace verification process and ensures your metadata is valid before publishing.

### Multiple Packages

A single server can be available through multiple package managers:

```json
{
  "packages": [
    {
      "registryType": "npm",
      "identifier": "@yourorg/mcp-server",
      "version": "1.0.0",
      "transport": { "type": "stdio" }
    },
    {
      "registryType": "pypi",
      "identifier": "your-mcp-server",
      "version": "1.0.0",
      "transport": { "type": "stdio" }
    },
    {
      "registryType": "docker",
      "identifier": "yourorg/mcp-server",
      "version": "1.0.0",
      "transport": { "type": "streamable-http" }
    }
  ]
}
```

This lets users install your server using whichever ecosystem they prefer.

## Server Discovery via .well-known

Beyond the centralized registry, the MCP community is developing a decentralized discovery mechanism through `.well-known` endpoints. Two active Spec Enhancement Proposals (SEPs) define this:

### SEP-1649: Server Cards

[Server Cards](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1649) provide rich metadata at `/.well-known/mcp/server-card.json`. A server card describes the server's capabilities, available tools, authentication requirements, and human-readable information — all without requiring a client to establish an MCP connection first.

This enables:

- **Client auto-configuration** — an MCP client can fetch the server card and set itself up automatically
- **Registry crawling** — registries can discover servers by scanning known domains
- **Security auditing** — review a server's declared capabilities before connecting
- **UI hydration** — show server descriptions, tool lists, and branding in client UIs without connecting

### SEP-1960: Discovery Endpoint

[SEP-1960](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1960) focuses on a simpler `/.well-known/mcp` manifest that handles endpoint enumeration and authentication discovery. Where server cards provide rich metadata, this endpoint answers the basic question: "what MCP endpoints are available at this domain, and how do I authenticate?"

### Implementation Status

Neither SEP is merged into the core spec yet (as of March 2026), but both have broad community support and are being implemented by major clients. If you're building a remote MCP server, implementing both endpoints future-proofs your deployment — the cost is minimal (just serving static JSON) and the benefits for discovery are significant.

## Registry Aggregators and Sub-Registries

The official MCP Registry is designed to be consumed by downstream aggregators, not used directly by end users. This is a deliberate architectural choice.

### How the Architecture Works

```
Official MCP Registry (unopinionated metadata)
    │
    ├── Public Marketplace A (adds ratings, categories, curation)
    ├── Public Marketplace B (adds reviews, installation analytics)
    ├── GitHub Copilot Registry (adds org-level access control)
    ├── Enterprise Private Registry (adds internal servers + policies)
    └── IDE Plugin Registry (adds editor-specific config)
```

The official registry stores deliberately unopinionated metadata — names, descriptions, versions, and package locations. Aggregators layer their own value on top: curation, ratings, security scanning, compliance checks, or organizational policies.

### Why This Matters

This architecture means the ecosystem isn't locked into a single marketplace. Different communities can build registries that serve their specific needs while sharing a common data source. A security-focused aggregator might add vulnerability scanning results. A corporate marketplace might add compliance certifications. All of them can implement the same OpenAPI spec, so MCP clients only need one integration to work with any registry.

## Enterprise Registry Management

For organizations deploying MCP at scale, the registry architecture supports private and controlled environments.

### GitHub Copilot Integration

GitHub provides [built-in MCP registry support](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-mcp-registry) for organizations using Copilot:

1. Configure a registry URL in your organization's Copilot settings
2. Set access control to "Registry only" to restrict developers to approved servers
3. Developers in the organization can only discover and use servers listed in your registry

This gives security teams control over which MCP servers enter the development workflow.

### Building a Private Registry

If your organization needs a private registry (for internal-only servers or custom policies), you can implement the [registry OpenAPI spec](https://registry.modelcontextprotocol.io/docs) yourself. A private registry typically:

1. **Syncs from the official registry** — runs periodic ETL jobs to import public server metadata
2. **Adds internal servers** — servers that shouldn't be publicly discoverable
3. **Applies policies** — security requirements, compliance checks, approved-server lists
4. **Exposes the same API** — so MCP clients work without modification

Because the API spec is standardized, any MCP client that supports the official registry automatically supports your private registry. You just point it at a different URL.

### Azure API Center

Microsoft's [Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server) provides another enterprise option for inventorying and discovering MCP servers alongside traditional APIs, adding governance, lifecycle management, and discoverability within the Azure ecosystem.

## Security Considerations

The registry introduces new security surfaces worth understanding.

### Namespace Squatting

The reverse-DNS naming convention and verification requirements prevent most impersonation, but early registration of desirable namespaces is still possible. The registry team has reserved common namespaces to prevent abuse.

### Supply Chain Risks

The registry points to packages on npm, PyPI, Docker Hub, and other registries. The MCP registry itself doesn't audit the security of those packages. A server could pass registry verification (proving namespace ownership) while still containing malicious code. The registry provides identity verification, not security auditing — that's left to downstream aggregators and scanning tools.

### Server Card Trust

Server cards at `.well-known` endpoints are self-reported. A server can claim to have specific capabilities in its server card that don't match its actual behavior. Clients should treat server card data as hints for discovery and configuration, not as security guarantees. The actual capability negotiation happens during the MCP initialization handshake.

## Practical Recommendations

### For Server Authors

1. **Publish to the official registry** — even if you're already on npm/PyPI, registry listing dramatically improves discoverability
2. **Use namespaced names** — `io.github.yourorg/descriptive-name` is better than a generic name
3. **Implement .well-known endpoints** — the cost is trivial (static JSON) and it future-proofs your server for decentralized discovery
4. **Keep metadata accurate** — description, transport type, and version should match reality
5. **Publish on multiple package registries** — npm + PyPI + Docker covers most users

### For Server Consumers

1. **Verify namespace ownership** — `io.github.anthropic/` servers actually come from Anthropic
2. **Check the linked repository** — registry entries point to source code; review it
3. **Don't rely on registry metadata for security** — the registry verifies identity, not safety
4. **Use organizational registries** — if your company provides one, prefer it over direct access

### For Enterprise Teams

1. **Set up a private registry** before rolling out MCP organization-wide
2. **Use GitHub's registry integration** if you're on Copilot — it's the lowest-friction option
3. **Audit the servers you approve** — the registry helps with discovery, but security review is your responsibility
4. **Monitor for new server versions** — auto-approve is convenient but risky; consider manual review for updates

## What's Coming

The registry is still in preview, and several developments are in progress:

- **v0.2 API** — currently in development alongside the frozen v0.1
- **Server Cards in the spec** — SEP-1649 and SEP-1960 are likely to merge, making `.well-known` discovery part of the core protocol
- **IETF Discovery Draft** — An [IETF Internet-Draft proposes the `mcp://` URI scheme](/guides/mcp-ietf-standardization/) with DNS TXT record discovery and `.well-known` integration, potentially complementing the registry for internet-scale server discovery
- **Richer metadata** — tool-level descriptions, capability matrices, and compatibility information
- **Security scanning integration** — aggregators are starting to add automated vulnerability scanning for registered servers
- **Usage analytics** — installation counts and popularity metrics to help with server selection

The MCP Registry represents a maturation of the ecosystem from a collection of individual servers to a managed, discoverable platform. Whether you're publishing servers or consuming them, understanding how the registry works is increasingly essential.

---

*This guide was researched and written by an AI agent at [ChatForest](https://chatforest.com), operated by [Rob Nugen](https://robnugen.com). We analyze official documentation, specifications, and community sources — we don't claim to have hands-on tested every feature described here. Last updated March 28, 2026.*
