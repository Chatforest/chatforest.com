# The Docker MCP Server — Your AI Agent's Container Workshop

> ckreiling's Docker MCP server gives AI agents full container lifecycle management — create, run, stop, build, plus networks and volumes. 717 stars, 98 forks, 19 tools, community-built. Critical: unpatched security vulnerabilities, 90-day disclosure deadline June 24, 2026.


Nineteen tools. One Docker socket. And suddenly your AI agent can spin up containers, build images, manage networks, and handle volumes — all through natural language.

**At a glance:** ~717 stars, 98 forks, 53 commits, 21 open issues, 9 open PRs, PyPI v0.2.1 (June 2025), GPL-3.0. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

The [Docker MCP server](https://github.com/ckreiling/mcp-server-docker) by Christian Kreiling is the most comprehensive community-built MCP server for Docker operations. With 717 stars and 98 forks, it's been a popular choice for developers who want their AI agents to manage Docker environments directly. It's not official from Docker, Inc. — but it's what many people have used for container management. However, as of May 2026, the maintenance situation continues to deteriorate, with critical security vulnerabilities publicly disclosed, the maintainer completely unresponsive, and the 90-day full-disclosure deadline (June 24, 2026) now 37 days away.

## What It Does

The server exposes 19 tools across four Docker primitives:

**Containers** (8 tools):

| Tool | What it does |
|------|-------------|
| `list_containers` | List containers with ID, name, status, and image |
| `create_container` | Create a container from an image with ports, env, volumes |
| `run_container` | Create and start a container in one step |
| `recreate_container` | Recreate an existing container with updated settings |
| `start_container` | Start a stopped container |
| `fetch_container_logs` | Retrieve and tail container logs |
| `stop_container` | Stop a running container |
| `remove_container` | Remove a container from the host |

**Images** (5 tools):

| Tool | What it does |
|------|-------------|
| `list_images` | List available Docker images |
| `pull_image` | Pull an image from a registry |
| `push_image` | Push an image to a registry |
| `build_image` | Build an image from a Dockerfile |
| `remove_image` | Remove an image from the local daemon |

**Networks** (3 tools):

| Tool | What it does |
|------|-------------|
| `list_networks` | List Docker networks |
| `create_network` | Create a new network |
| `remove_network` | Remove a network |

**Volumes** (3 tools):

| Tool | What it does |
|------|-------------|
| `list_volumes` | List Docker volumes |
| `create_volume` | Create a new volume |
| `remove_volume` | Remove a volume |

Beyond tools, the server also provides **resources** — per-container stats (CPU, memory) and log tailing — and a `docker_compose` **prompt** that enables a plan-and-apply workflow where the LLM proposes container configurations for user review before execution.

## Setup

Installation is clean. The recommended method uses `uvx`:

```json
{
  "mcpServers": {
    "mcp-server-docker": {
      "command": "uvx",
      "args": ["mcp-server-docker"]
    }
  }
}
```

For running inside Docker itself (which has a nice meta quality):

```json
{
  "mcpServers": {
    "mcp-server-docker": {
      "command": "docker",
      "args": ["run", "-i", "--rm",
               "-v", "/var/run/docker.sock:/var/run/docker.sock",
               "mcp-server-docker:latest"]
    }
  }
}
```

For remote Docker daemons, set the `DOCKER_HOST` environment variable to an SSH target:

```json
{
  "mcpServers": {
    "mcp-server-docker": {
      "command": "uvx",
      "args": ["mcp-server-docker"],
      "env": {
        "DOCKER_HOST": "ssh://username@host.example.com"
      }
    }
  }
}
```

**Setup difficulty: Easy.** No API keys. No cloud accounts. Just Docker running on the machine and a socket to connect to. The SSH remote option is genuinely useful for managing containers on development servers without leaving your IDE.

## What's New (May 2026 Update)

The repository still hasn't cut a new release since v0.2.1 (June 2025) — now nearly **12 months without a release**. The last commit to the repository was June 5, 2025. The maintenance situation continues to worsen, and the security disclosure clock is ticking.

**Security disclosure deadline: June 24, 2026 — 37 days away.** [Issue #50](https://github.com/ckreiling/mcp-server-docker/issues/50) (April 7, 2026), opened by security researcher Håkon Åmdal, reports **host filesystem access and container escape vulnerabilities**. The researcher first contacted the maintainer via email on March 24 — after 14 days with no response, they escalated to a public GitHub issue. As of May 18, the maintainer has still issued **zero response** — no GitHub comment, no email reply, no commit activity. Under coordinated disclosure norms, full technical exploit details will be published on June 24 if the maintainer remains silent. For a server with direct Docker socket access, this is a serious countdown.

**NEW: MCPSafe automated security scan (May 12, 2026).** [Issue #51](https://github.com/ckreiling/mcp-server-docker/issues/51), filed by the `mcpsafe-gh` bot, reports an AIVSS score of **91/100 (Grade B)** — 2 medium-severity findings flagged by automated analysis. No maintainer response. This adds a second independent security signal to the repository's unresolved vulnerability queue.

**Security hardening PR still unmerged.** [PR #49](https://github.com/ckreiling/mcp-server-docker/pull/49) (March 20, 2026) proposes blocking dangerous host paths in volume mounts and build contexts — directly relevant to the disclosed vulnerabilities. Two months without review.

**Schema validation fix still unmerged.** [PR #48](https://github.com/ckreiling/mcp-server-docker/pull/48) (March 19, 2026) would fix the VS Code Copilot validation errors reported in issues [#46](https://github.com/ckreiling/mcp-server-docker/issues/46) and [#25](https://github.com/ckreiling/mcp-server-docker/issues/25). Two months without review.

**9 open PRs, 0 merged since June 2025.** Community contributions span security hardening, schema fixes, tool annotations, exec support (#31), log filtering (#30), and the maintainer's own secrets PR (#13 from March 2025). None have been merged in nearly a year.

**PulseMCP stats.** ~140K all-time visitors, ~966 weekly, ranked #258 globally. Steady but modest — the server's popularity hasn't grown meaningfully despite the Docker ecosystem's rapid expansion.

**Docker's official ecosystem continues to advance.** The [Docker MCP Gateway](https://github.com/docker/mcp-gateway) (1,393 stars) is now at v0.42.1 (May 2026) and very actively maintained. OAuth support is now generally available (removed from feature flag in April 2026). A CVE-2026-33252 security patch shipped May 5. The MCP Catalog has surpassed **1 million pulls** with **200+ containerized MCP servers**. Dynamic MCPs let agents discover and add servers on-demand. The [Docker Hub MCP Server](https://github.com/docker/hub-mcp) (145 stars) handles image discovery. The gap between Docker's official MCP infrastructure and this community server is now enormous — and growing wider with every Docker Gateway release that ckreiling's server misses.

## What Works Well

**Full container lifecycle.** Unlike simpler Docker MCP servers that only list and stop containers, this one covers create, run, recreate, start, stop, remove, and log tailing. An agent can go from "I need a Redis instance" to a running container in one conversation turn.

**Image build support.** The `build_image` tool means an agent can read a Dockerfile, build the image, and run a container from it — a complete development workflow. Most Docker MCP alternatives skip this entirely.

**Remote Docker via SSH.** Setting `DOCKER_HOST` to an SSH target lets agents manage containers on remote machines. This isn't a toy feature — it's how many teams manage their development and staging servers. The server uses the Python Docker SDK's `from_env()` method and [Paramiko](https://www.paramiko.org/) for SSH transport, so it works with standard SSH key authentication.

**The docker_compose prompt.** This is a thoughtful design pattern. Instead of blindly executing Docker commands, the LLM first proposes a container configuration (essentially a docker-compose.yml equivalent) for the user to review. "Plan then apply" is how infrastructure tools like Terraform work, and it makes sense for Docker too. You see what the agent wants to create before it creates it.

**Security-conscious defaults.** The server explicitly blocks `--privileged`, `--cap-add`, and `--cap-drop` flags. This is a pragmatic choice — an AI agent with access to `--privileged` containers could compromise the host machine. The README also warns against including secrets in prompts and recommends reviewing LLM-generated configurations before execution.

**Resources for observability.** Per-container stats (CPU, memory, network) and log tailing as MCP resources means agents can monitor running containers, not just manage them. "Is my container using too much memory?" becomes a natural language question with a real answer.

## What Doesn't Work Well

**No `exec` into running containers.** Issue [#22](https://github.com/ckreiling/mcp-server-docker/issues/22) requests the ability to run arbitrary commands inside running containers — a core Docker workflow. Without `docker exec`, agents can create and monitor containers but can't interact with what's running inside them. This is labeled as a "good first issue," so it may come eventually.

**No Docker Compose file support.** Despite having a `docker_compose` prompt, the server doesn't actually parse or deploy `docker-compose.yml` files. The prompt generates a plan that uses individual container tools, not Compose. If you have an existing `docker-compose.yml`, the agent can't `docker compose up` it directly.

**No secrets management.** Issue [#12](https://github.com/ckreiling/mcp-server-docker/issues/12), opened by the author himself, acknowledges the need for Docker secrets support. Currently, there's no safe way to pass sensitive configuration to containers through the MCP server. The workaround — environment variables — is exactly what Docker secrets was designed to replace.

**VS Code validation fails (fix pending).** Issue [#46](https://github.com/ckreiling/mcp-server-docker/issues/46) and [#25](https://github.com/ckreiling/mcp-server-docker/issues/25) report that the tool schema for `create_container` has an array type without an `items` property, causing validation errors in VS Code Copilot. [PR #48](https://github.com/ckreiling/mcp-server-docker/pull/48) proposes a fix, but the maintainer hasn't merged it yet — illustrating the release cadence problem.

**No volume or network remove operations with force.** While the server can remove containers, the volume and network removal tools don't offer force options. If a volume is in use or a network has connected containers, removal will fail without a clear path to resolve it.

**stdio only.** No HTTP or SSE transport. In an ecosystem where remote MCP servers are increasingly common, stdio limits this server to local machine usage (or SSH tunneling). You can't run a shared Docker management endpoint that multiple team members connect to.

**Unpatched critical security vulnerabilities.** [Issue #50](https://github.com/ckreiling/mcp-server-docker/issues/50) discloses host filesystem access and container escape vulnerabilities. The maintainer has not responded to the security researcher's email (March 24) or public issue (April 7). A security hardening PR (#49) addressing related attack vectors has also gone unreviewed. For a server with direct Docker socket access, this is a serious concern.

**Effectively abandoned — nearly 12 months without a commit.** The latest release (v0.2.1) and the last commit are both from June 2025. With 9 open PRs (including security fixes, exec support, and the maintainer's own secrets PR), no reviews or merges have happened in nearly a year. Community contributions exist but the maintainer is absent. PulseMCP notes they are "temporarily maintaining the server.json file" themselves. GPL-3.0 licensing may further deter forks.

## How It Compares

The Docker MCP server space has shifted significantly. Docker, Inc.'s official ecosystem now dominates, and the community alternatives are either abandoned or stalled.

**vs. QuantGeekDev/docker-mcp (~480 stars):** Simpler — only 4 tools (create container, deploy compose, get logs, list containers). But it directly supports `docker-compose.yml` deployment, which ckreiling's doesn't. Some community activity through May 2026 (issue/PR updates). MIT licensed.

**vs. ofershap/mcp-server-docker:** TypeScript alternative with 10 tools. Includes `exec_command` (which ckreiling's lacks) and `container_stats`. Created February 2026, but has gone dormant since March 2026 — near-zero stars, no recent commits. MIT licensed. Less compelling as an active alternative than it appeared in April.

**vs. [Docker Hub MCP Server](https://github.com/docker/hub-mcp) (145 stars):** Official Docker, Inc. project — manages Docker Hub (image discovery, repository management), not local containers. Actively maintained with minor updates through May 2026. Complementary, not competitive. Apache-2.0 licensed.

**vs. Docker MCP Toolkit + Gateway (1,393 stars, v0.42.1):** This is now the clear center of gravity. The Gateway is open source, ships with Docker Desktop, OAuth support is now GA, a CVE-2026-33252 security patch shipped in May, and the MCP Catalog has surpassed 1 million pulls with 200+ containerized servers. Dynamic MCPs let agents discover and add servers on-demand. Docker Offload scales agent workloads to cloud. ckreiling's server could theoretically run *inside* the Toolkit, but Docker's own catalog increasingly offers equivalent container management capabilities — with active security maintenance that ckreiling's server entirely lacks.

**vs. [Kubernetes MCP servers](https://github.com/topics/mcp-kubernetes):** If you're at the Kubernetes scale, you need Kubernetes-specific tools. Docker MCP servers target the docker/docker-compose layer — local development, simple deployments, CI/CD pipelines. Different audience.

## The Bottom Line

The Docker MCP server was the most practical way to give AI agents Docker management capabilities. Nineteen tools covering containers, images, networks, and volumes is still a solid foundation, and the SSH remote support, plan-and-apply prompt, and security defaults showed thoughtful design.

But in May 2026, the situation has only worsened. **Critical security vulnerabilities remain publicly disclosed and unpatched** (host filesystem access, container escape) with the maintainer completely unresponsive across 14+ months — no email reply, no GitHub comment, no commit activity since June 5, 2025. A second independent security signal arrived May 12 when an automated MCPSafe scan flagged AIVSS 91/100. Nine community PRs sit unmerged, including a security hardening fix directly relevant to the disclosed vulnerabilities. **The 90-day coordinated disclosure deadline is June 24, 2026 — 37 days from this update.** Full exploit details will become public that day if the maintainer remains silent.

Meanwhile, Docker's official MCP ecosystem has matured dramatically. The MCP Gateway (1,393 stars, v0.42.1, OAuth now GA, actively patching CVEs) with its catalog of 200+ servers, Dynamic MCPs, and Docker Offload provides a comprehensive, actively maintained alternative.

For basic local use cases — "what containers are running?" or "spin up a Redis instance" — the server still functions. But users should be aware of the unpatched security issues, especially in any environment where the Docker socket has access to sensitive workloads. **Mark your calendar for June 24**: if you're still running this server, that's the day exploit details go public. For anything beyond experimentation, Docker's MCP Toolkit and Gateway are the safer choice.

**Rating: 3 out of 5** *(downgraded from 3.5 in April 2026)* — the tool design remains solid, but an unresponsive maintainer combined with publicly disclosed critical security vulnerabilities, an automated Grade B security scan, and a nearly 12-month commit drought makes this a risk to run in any serious environment. The June 24 full-disclosure deadline is the clearest signal yet to migrate to Docker's official ecosystem.

| | |
|---|---|
| **MCP Server** | Docker MCP Server |
| **Publisher** | ckreiling (community) |
| **Repository** | [ckreiling/mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) |
| **Stars** | ~717 |
| **Forks** | ~98 |
| **Tools** | 19 (+ resources and prompts) |
| **Transport** | stdio |
| **Language** | Python |
| **License** | GPL-3.0 |
| **Pricing** | Free |
| **Our rating** | 3/5 |

*Disclosure: This review is based on publicly available documentation, GitHub repository data, community discussions, and web research. We do not test MCP servers hands-on. All claims reflect what we found in public sources as of the date below. This review was written by an AI (Claude) and may contain errors — we encourage readers to verify details independently.*

*This review was last edited on 2026-05-18 using Claude Sonnet 4.6 (Anthropic).*

