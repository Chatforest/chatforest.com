# MCP Server Packaging & Distribution: npm, PyPI, Docker, DXT, and the Official Registry

> A comprehensive guide to packaging and distributing MCP servers — covering npm/npx publishing, PyPI/uvx distribution, Docker containerization (Docker MCP Toolkit, ToolHive), DXT


Building an MCP server is the easy part. Getting it into users' hands — reliably, across platforms, with the right dependencies — is where most projects stall. As of March 2026, the ecosystem offers at least six distinct distribution paths, each with different trade-offs around ease of use, security, discoverability, and production-readiness.

This guide covers the full MCP server packaging and distribution landscape. Our analysis draws on official documentation, registry specifications, vendor tooling, and community practices — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## The Distribution Landscape at a Glance

| Method | Best for | Runtime needed | Transport | Discovery |
|---|---|---|---|---|
| **npm / npx** | JS/TS servers, developer audience | Node.js | stdio | npmjs.com |
| **PyPI / uvx** | Python servers, data science audience | Python (or uv) | stdio | pypi.org |
| **Docker containers** | Isolation, multi-language, enterprise | Docker/OCI runtime | stdio or HTTP | Docker Hub, MCP Catalog |
| **DXT (Desktop Extensions)** | Non-technical users, Claude Desktop | None (bundled) | stdio | desktopextensions.com, mcp.so |
| **Official MCP Registry** | Universal discovery, verified identity | Varies | Varies | registry.modelcontextprotocol.io |
| **Managed platforms** | Production HTTP, serverless | Platform-managed | Streamable HTTP | Smithery, Cloudflare, TrueFoundry |

Most servers should target at least two: one package registry (npm or PyPI) for developers, plus the official MCP Registry for discoverability. Production servers add Docker. Consumer-facing tools add DXT.

## npm / npx: JavaScript and TypeScript Servers

The most common distribution path for TypeScript MCP servers. Users run your server with a single npx command — no global install needed.

### How It Works

npx downloads your package from the npm registry into a temporary cache, resolves dependencies, and executes the entry point. Claude Desktop, Cursor, and VS Code all support npx-based server configurations natively:

```json
{
  "mcpServers": {
    "my-server": {
      "command": "npx",
      "args": ["-y", "my-mcp-server"],
      "env": {
        "API_KEY": "..."
      }
    }
  }
}
```

The `-y` flag auto-confirms the install prompt. Environment variables pass credentials without embedding them in the package.

### Publishing Workflow

1. **Structure your package** with a `bin` field in `package.json` pointing to your CLI entry point
2. **Set `"type": "module"`** if using ES modules (most modern MCP SDKs expect this)
3. **Include a shebang** (`#!/usr/bin/env node`) in your entry file
4. **Publish:** `npm publish` (or `npm publish --access public` for scoped packages)
5. **Test:** `npx your-package-name` should start the server

### Trade-offs

**Advantages:** Universal among JS developers. Zero-install via npx. Mature versioning, dependency resolution, and security scanning (npm audit). Every MCP client supports npx natively.

**Disadvantages:** Requires Node.js on the user's machine. npx can be slow on first run (downloading dependencies). No sandboxing — the server runs with the user's full permissions. Version pinning is opt-in, so users may get unexpected updates.

## PyPI / uvx: Python Servers

The standard path for Python MCP servers, especially in data science and ML tooling. uvx (from the uv package manager) is the Python equivalent of npx — it creates an isolated environment and runs the package without permanent installation.

### How It Works

```json
{
  "mcpServers": {
    "my-server": {
      "command": "uvx",
      "args": ["my-mcp-server"],
      "env": {
        "API_KEY": "..."
      }
    }
  }
}
```

uvx is part of [uv](https://github.com/astral-sh/uv), a Rust-powered Python package manager that's dramatically faster than pip. It resolves dependencies, creates a temporary virtual environment, installs the package, and runs the entry point — all in seconds. Users can alternatively use `pip install` for permanent installations.

### Publishing Workflow

1. **Define entry points** in `pyproject.toml` under `[project.scripts]`
2. **Use a build backend** — setuptools, hatchling, or flit
3. **Build:** `python -m build` or `uv build`
4. **Publish:** `twine upload dist/*` or `uv publish`
5. **Test:** `uvx your-package-name` should start the server

### Trade-offs

**Advantages:** Natural for Python-heavy ecosystems (data science, ML, API integrations). uvx provides dependency isolation automatically. uv's Rust implementation makes installs fast. Strong integration with scientific computing libraries.

**Disadvantages:** Requires Python or uv installed. Python dependency resolution can be complex (C extensions, platform-specific wheels). Slower startup than Node.js for simple servers. Fewer MCP clients have first-class uvx support compared to npx.

## Docker: Containerized Distribution

Docker is becoming the standard for production MCP server distribution. Containers solve the "works on my machine" problem entirely — dependencies, runtimes, and configuration are all bundled in the image.

### The Docker MCP Ecosystem

Docker has built a comprehensive MCP infrastructure with three components:

**Docker MCP Catalog** — A curated collection of 300+ verified MCP server images on Docker Hub (`hub.docker.com/mcp`). Each image has versioning, provenance tracking, and automated security updates. Think of it as Docker Hub specifically for MCP.

**Docker MCP Toolkit** — A management interface integrated into Docker Desktop. Browse the catalog, launch servers with one click, organize them into profiles for different projects, and connect them to AI clients through the MCP Gateway. No manual configuration files needed.

**Docker MCP Gateway** — Routes requests from AI clients (Claude Code, Cursor, Zed) to the right containerized server. Handles authentication, lifecycle management, and transport bridging.

### Publishing a Docker MCP Server

```dockerfile
FROM node:22-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --production
COPY . .
ENTRYPOINT ["node", "src/index.js"]
```

For Python:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml .
RUN pip install --no-cache-dir .
COPY . .
ENTRYPOINT ["python", "-m", "my_mcp_server"]
```

Publish to Docker Hub or any OCI registry. Submit to the Docker MCP Catalog for broader discovery.

### ToolHive: Enterprise Container Management

[ToolHive](https://github.com/stacklok/toolhive) by Stacklok is an open-source (Apache 2.0) platform specifically designed for running MCP servers in containers with enterprise-grade security:

- **Isolation by default** — Every server runs in a locked-down container with only the permissions it needs
- **No exposed ports** — ToolHive proxies all communication through stdio; the container has no direct network access
- **Secret management** — Credentials are injected securely, never in plaintext
- **Fine-grained permissions** — Network access controls, filesystem restrictions, resource limits
- **Kubernetes-native** — Deploy MCP servers as Kubernetes workloads with the same security model
- **Built-in registry** — ToolHive maintains a registry of pre-vetted server images that can be launched with `thv run <server-name>`

ToolHive addresses a real gap: most MCP servers run with the same permissions as the user, accessing the full filesystem and network. ToolHive's container sandboxing ensures a compromised server can't exfiltrate data or pivot to other systems.

### Trade-offs

**Advantages:** Complete environment isolation. Language-agnostic — any runtime works. Production-proven technology. Security sandboxing. Docker MCP Catalog provides curated discovery. ToolHive adds enterprise controls.

**Disadvantages:** Docker must be installed (significant overhead for casual users). Larger distribution size than npm/pip packages. Container startup adds latency. Filesystem access requires explicit volume mounts. More complex configuration than npx/uvx for development use.

## DXT: Desktop Extensions for One-Click Install

Desktop Extensions (DXT) are Anthropic's answer to MCP's installation problem. Launched in June 2025, DXT packages an entire MCP server — code, dependencies, configuration — into a single `.dxt` file that non-technical users can install with one click in Claude Desktop.

### What's Inside a DXT File

A `.dxt` file is a zip archive containing:

- **`manifest.json`** — Metadata, configuration schema, permissions, platform requirements
- **Server implementation** — The actual MCP server code
- **Bundled dependencies** — Everything the server needs, pre-installed
- **Platform-specific overrides** — Different binaries or paths for Windows vs. macOS

The `manifest.json` is the heart of the extension:

```json
{
  "name": "my-extension",
  "version": "1.0.0",
  "description": "A useful MCP tool",
  "mcp": {
    "command": "node",
    "args": ["server.js"]
  },
  "configuration": {
    "api_key": {
      "type": "string",
      "description": "Your API key",
      "required": true,
      "storage": "keychain"
    }
  }
}
```

Note the `"storage": "keychain"` — DXT can store sensitive configuration in the OS keychain rather than plaintext JSON files. This is a significant security improvement over manual `claude_desktop_config.json` editing.

### Building DXT Packages

Anthropic provides an official toolchain:

```bash
npm install -g @anthropic-ai/dxt
dxt init          # Scaffold the extension structure
# ... implement your server ...
dxt pack          # Generate the .dxt file
```

`dxt pack` bundles everything into the archive, validates the manifest, and produces a distributable file.

### Distribution Channels

- **[desktopextensions.com](https://www.desktopextensions.com/)** — Anthropic's official directory
- **[mcp.so/dxt](https://mcp.so/dxt)** — Community directory with DXT listings
- **Direct download** — Host on your own site or GitHub releases
- **Awesome lists** — [awesome-claude-dxt](https://github.com/milisp/awesome-claude-dxt) curates DXT extensions

### Trade-offs

**Advantages:** Zero technical knowledge required from users. One-click install. Bundled dependencies eliminate version conflicts. Keychain integration for secrets. Automatic updates. The best UX for non-developer audiences.

**Disadvantages:** Currently Claude Desktop only — other MCP clients don't support DXT yet. Larger file sizes due to bundled dependencies. Requires Node.js to build (though Node.js runtime is bundled in Claude Desktop). Limited to stdio transport. Building DXT packages adds a packaging step to your workflow.

## The Official MCP Registry

The [MCP Registry](https://registry.modelcontextprotocol.io) launched in preview in September 2025 with an API freeze at v0.1 in October 2025. It's the canonical place for MCP server discovery — a community-driven, permissively licensed registry maintained by the official MCP registry working group.

### Namespace System

Server names follow reverse-DNS format that ties them to verified identities:

| Namespace pattern | Verification method | Example |
|---|---|---|
| `io.github.username/*` | GitHub OAuth/OIDC | `io.github.jane/weather-server` |
| `io.github.orgname/*` | GitHub org membership | `io.github.acme/internal-tools` |
| `com.example/*` | DNS TXT record or HTTP challenge | `com.example/api-server` |

This namespace system is crucial: it prevents impersonation and establishes supply-chain trust. Only the verified owner of a GitHub account or domain can publish under their namespace.

### The server.json Format

Each registry entry uses a standardized `server.json`:

```json
{
  "name": "io.github.jane/weather-server",
  "version": "1.2.0",
  "description": "Real-time weather data via MCP",
  "repository": "https://github.com/jane/weather-mcp",
  "packages": {
    "npm": { "name": "@jane/weather-mcp", "version": "1.2.0" },
    "pypi": { "name": "weather-mcp", "version": "1.2.0" },
    "docker": { "image": "jane/weather-mcp", "tag": "1.2.0" }
  },
  "remotes": [
    { "url": "https://weather-mcp.jane.dev/mcp" }
  ],
  "tools": [
    { "name": "get_weather", "description": "Get current weather for a location" }
  ]
}
```

The `packages` field points to where the server can actually be downloaded — npm, PyPI, Docker, or GitHub/GitLab releases. The `remotes` field lists cloud-hosted instances.

### Publishing to the Registry

1. **Create `server.json`** in your repository root following the schema
2. **Authenticate** via the registry CLI: `mcpctl auth login` (GitHub OAuth or domain verification)
3. **Validate:** `mcpctl validate server.json`
4. **Publish:** `mcpctl publish`

The registry validates namespace ownership, checks that referenced packages exist on their respective registries, and enforces that packages come from trusted public registries.

### Registry Validation Rules

The official registry enforces stricter rules than community directories:

- **Namespace authentication** — You must prove ownership of the namespace
- **Package ownership verification** — Referenced npm/PyPI packages must be controlled by you
- **Trusted registries only** — Packages must come from npmjs.com, pypi.org, or Docker Hub
- **Moderation** — Community members can flag servers violating moderation guidelines; maintainers can denylist entries

### Trade-offs

**Advantages:** Canonical discovery location. Verified publisher identity prevents impersonation. Multi-format — points to npm, PyPI, Docker, or hosted URLs. Growing client integration. Free to use.

**Disadvantages:** Still in preview — API and policies may change. Currently only supports GitHub/GitLab releases for artifact hosting. Limited search and filtering compared to community directories like mcp.so or Glama. Requires verification setup.

## Managed Platforms and Automated Generation

Several platforms handle packaging, hosting, and distribution as a service.

### Speakeasy: OpenAPI-to-MCP Generation

[Speakeasy](https://www.speakeasy.com/product/mcp-server) generates production-ready MCP servers from OpenAPI specifications. Each API endpoint becomes an MCP tool that AI agents can discover and use. Beyond generation, Speakeasy handles distribution through three channels:

- **DXT packaging** — Generates `.dxt` files for Claude Desktop with guided setup for API keys and credentials
- **npm publishing** — Standard npm packages with versioning and dependency management
- **Cloudflare Workers** — Edge-deployed MCP servers with low latency

This is particularly valuable for API companies that want to offer MCP access without building servers from scratch.

### Smithery: Registry and Deployment Platform

[Smithery](https://smithery.ai) provides both a discovery directory (7,300+ servers) and a deployment platform. The Smithery CLI (`npx skills add smithery/cli`) lets developers install and configure MCP servers interactively. For server authors, Smithery offers hosted deployment where you push your code and Smithery handles containerization, scaling, and endpoint management.

### TrueFoundry: stdio-to-HTTP Deployment

[TrueFoundry](https://www.truefoundry.com/docs/mcp-server-deployment/deploy-mcp-server-from-npx-uvx) specializes in deploying npx/uvx-based stdio servers as production HTTP services. It wraps your server with mcp-proxy to convert stdio to Streamable HTTP, deploys it as a managed service, and provides monitoring, scaling, and authentication.

## Transport Bridging: stdio to HTTP

Most MCP servers are built for stdio (standard input/output) — they run as local subprocesses. But production deployments often need HTTP. Several tools bridge this gap:

### mcp-proxy

[mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) is the most widely used bridge. It launches your stdio server as a subprocess and exposes it over Streamable HTTP or SSE:

```bash
mcp-proxy --port 8080 -- node my-server.js
```

Key features:
- **Multiplexing** — Run multiple named stdio servers behind one proxy instance
- **Bidirectional** — Can also convert HTTP servers to stdio for local use
- **Production-ready** — Prebuilt binaries, Homebrew formula, container images
- **Actively maintained** — Last updated March 2026

### mcp-bridge

[mcp-bridge](https://github.com/brrock/mcp-bridge) is a lightweight alternative focused on converting stdio servers to SSE or Streamable HTTP. It's designed for serverless environments where stdio is incompatible (e.g., Vercel, AWS Lambda).

### When to Bridge

- **Development:** Keep stdio. It's simpler, faster, and every client supports it
- **Team sharing:** Bridge to HTTP so multiple developers can share one server instance
- **Production:** Bridge to HTTP behind a reverse proxy (nginx, Caddy) with TLS
- **Serverless:** Bridge to Streamable HTTP for platform compatibility

## Choosing Your Distribution Strategy

### Decision Matrix

| Your situation | Recommended approach |
|---|---|
| **Open-source tool, developer audience** | npm or PyPI + Official MCP Registry |
| **Enterprise internal tool** | Docker + ToolHive + private registry |
| **Consumer product for Claude users** | DXT + desktopextensions.com |
| **API company adding MCP support** | Speakeasy generation → npm + DXT + Cloudflare |
| **Production service, multiple clients** | Docker + HTTP transport + MCP Registry |
| **Quick prototype or personal tool** | npm/PyPI only, configure via npx/uvx |

### Multi-Channel Publishing

The strongest distribution strategy covers multiple channels:

1. **Package registry** (npm or PyPI) — For developers who want to customize or self-host
2. **Docker image** — For production deployments with isolation requirements
3. **Official MCP Registry** — For discoverability across the ecosystem
4. **DXT** — For non-technical Claude Desktop users (if applicable)
5. **Community directories** — Submit to mcp.so, Glama, Smithery for additional visibility

### Versioning Best Practices

- Use semantic versioning across all channels (npm, PyPI, Docker tags, registry)
- Keep versions synchronized — users expect `1.2.0` on npm and `1.2.0` on Docker Hub to behave identically
- Pin dependencies in Docker images and DXT bundles to avoid surprise breaks
- Use the MCP Registry's version field to point to the latest stable release

## Security Considerations

Distribution is a supply-chain concern. A compromised MCP server package can access everything the user's AI assistant can — files, APIs, credentials.

**For publishers:**
- Enable 2FA on npm, PyPI, and Docker Hub accounts
- Use namespace verification on the official MCP Registry
- Sign Docker images with Cosign or Docker Content Trust
- Pin dependencies to specific versions in lock files
- Run security scanning in CI (npm audit, pip-audit, Trivy for containers)

**For consumers:**
- Prefer servers from the official MCP Registry (verified publishers)
- Use Docker or ToolHive for isolation in production
- Audit environment variables — don't pass more credentials than the server needs
- Pin versions in your client configuration rather than using `latest`
- Review the server's tool list and permissions before granting access

## What's Coming

The MCP distribution ecosystem is evolving rapidly:

- **Registry maturity** — The official MCP Registry is moving toward GA, with richer search, categories, and client-side integration (auto-discovery of servers matching your tools)
- **DXT expansion** — Other MCP clients beyond Claude Desktop are expected to adopt the DXT format or similar one-click packaging
- **Docker MCP Catalog growth** — Docker is actively expanding its curated catalog and tightening security scanning
- **Automated generation** — Tools like Speakeasy and Stainless are making it possible to generate and distribute MCP servers entirely from API specs
- **Enterprise registries** — Organizations are building private MCP registries for internal server distribution, similar to private npm registries
- **Supply-chain attestation** — SLSA and Sigstore integration for MCP packages, ensuring build provenance and tamper evidence

## Further Reading on ChatForest

- [What Is MCP?](/guides/what-is-mcp/) — Foundational overview of the Model Context Protocol
- [Build Your First MCP Server](/guides/build-your-first-mcp-server/) — Step-by-step server creation tutorial
- [MCP Server Frameworks & SDKs](/guides/mcp-server-frameworks-sdks/) — TypeScript SDK, Python SDK, and framework comparison
- [FastMCP Production Guide](/guides/fastmcp-production-guide/) — Deep dive into the FastMCP Python framework
- [MCP Docker & Containers](/guides/mcp-docker-containers/) — Container patterns for MCP servers
- [MCP Server Deployment & Hosting](/guides/mcp-server-deployment-hosting/) — Production hosting strategies
- [MCP Registry & Server Discovery](/guides/mcp-registry-server-discovery/) — How discovery works across the ecosystem
- [MCP Transports Explained](/guides/mcp-transports-explained/) — stdio vs. SSE vs. Streamable HTTP deep dive

