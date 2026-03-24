---
title: "The Docker MCP Server — Your AI Agent's Container Workshop"
date: 2026-03-14T12:14:00+09:00
description: "ckreiling's Docker MCP server gives AI agents full container lifecycle management — create, run, stop, build, plus networks and volumes. 690 stars, 97 forks, 19 tools, community-built and practical."
og_description: "Docker MCP server: 19 tools for containers, images, networks, volumes. 690 stars, 97 forks, PyPI v0.2.1, SSH remote support. Rating: 3.5/5."
content_type: "Review"
card_description: "Community Docker MCP server — 19 tools for container lifecycle, image management, networks, and volumes. Remote Docker via SSH, docker_compose prompt, security-conscious defaults. Active PRs for security and schema fixes."
last_refreshed: 2026-03-14
---

Nineteen tools. One Docker socket. And suddenly your AI agent can spin up containers, build images, manage networks, and handle volumes — all through natural language.

**At a glance:** ~690 stars, 97 forks, 53 commits, 10 open issues, 10 open PRs, PyPI v0.2.1 (June 2025), GPL-3.0. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

The [Docker MCP server](https://github.com/ckreiling/mcp-server-docker) by Christian Kreiling is the most comprehensive community-built MCP server for Docker operations. With 690 stars and 97 forks, it's become the go-to choice for developers who want their AI agents to manage Docker environments directly. It's not official from Docker, Inc. — but it's the one people actually use for container management.

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

## What's New (March 2026 Update)

The repository hasn't cut a new release since v0.2.1 (June 2025), but development activity has picked up significantly in early 2026, with 10 open pull requests signaling community momentum even as the maintainer remains quiet.

**Security hardening PR.** [PR #49](https://github.com/ckreiling/mcp-server-docker/pull/49) (March 20, 2026) proposes blocking dangerous host paths in volume mounts and build contexts — a meaningful security improvement for an MCP server that has direct Docker socket access. This addresses a real attack vector where an agent could mount `/etc/shadow` or `/var/run/docker.sock` from the host.

**Schema validation fix.** [PR #48](https://github.com/ckreiling/mcp-server-docker/pull/48) (March 19, 2026) replaces `tuple[str, int]` with `list[int | str]` in the ports schema, which should fix the VS Code Copilot validation errors reported in issues [#46](https://github.com/ckreiling/mcp-server-docker/issues/46) and [#25](https://github.com/ckreiling/mcp-server-docker/issues/25). If merged, this unblocks a significant user base.

**Enhanced tool descriptions.** [PR #45](https://github.com/ckreiling/mcp-server-docker/pull/45) (March 12, 2026) improves tool descriptions for better LLM agent tool selection — a subtle but important change, since LLMs choose which tools to call based on their descriptions.

**MCP Shield integration proposed.** [PR #44](https://github.com/ckreiling/mcp-server-docker/pull/44) (March 4, 2026) adds MCP Shield security scanning, part of a broader ecosystem trend toward auditing MCP server security.

**Docker's official ecosystem has expanded significantly.** Docker, Inc. launched the [Docker Hub MCP Server](https://github.com/docker/hub-mcp) (132 stars) for image discovery and repository management, plus the [Docker MCP Gateway](https://github.com/docker/mcp-gateway) for production-grade MCP server orchestration with container isolation, secret management, and GPU offloading. The Gateway's March 2026 update added provenance verification, runtime secret isolation, and granular access policies. These are complementary to ckreiling's server — Docker Hub MCP handles image discovery, Gateway handles infrastructure, and ckreiling's handles direct container management.

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

**Slow release cadence, growing PR backlog.** The latest release (v0.2.1) was June 2025 — nine months ago. With 53 total commits, 10 open issues, and now 10 open PRs (including security and schema fixes), community contributions are outpacing the maintainer's review capacity. The PR backlog is the bigger concern: useful improvements exist but aren't being merged. GPL-3.0 licensing may also deter some enterprise users and contributors.

## How It Compares

The Docker MCP server space remains fragmented — multiple small projects, no single dominant player — but Docker, Inc.'s official ecosystem has expanded considerably in early 2026.

**vs. QuantGeekDev/docker-mcp (~428 stars):** Simpler — only 4 tools (create container, deploy compose, get logs, list containers). But it directly supports `docker-compose.yml` deployment, which ckreiling's doesn't. Last updated December 2024 and appears abandoned. MIT licensed. Choose this only if you need simple Compose stack deployment.

**vs. ofershap/mcp-server-docker:** TypeScript alternative with 10 tools. Includes `exec_command` (which ckreiling's lacks) and `container_stats`. Created February 2026, still very new with minimal adoption. MIT licensed. Worth watching if you need exec support now.

**vs. [Docker Hub MCP Server](https://github.com/docker/hub-mcp) (132 stars):** Official Docker, Inc. project — but it manages Docker Hub (image discovery, repository management), not local containers. Complementary, not competitive. Apache-2.0 licensed.

**vs. Docker MCP Toolkit + Gateway:** Not a competitor — it's infrastructure for *running* MCP servers in containers with production-grade security (container isolation, secret management, provenance verification). The March 2026 Gateway update added granular access policies and runtime secret isolation. ckreiling's server could run *inside* the Toolkit. The Gateway now supports 300+ cataloged servers.

**vs. [Kubernetes MCP servers](https://github.com/topics/mcp-kubernetes):** If you're at the Kubernetes scale, you need Kubernetes-specific tools. Docker MCP servers target the docker/docker-compose layer — local development, simple deployments, CI/CD pipelines. Different audience.

## The Bottom Line

The Docker MCP server remains the most practical way to give AI agents Docker management capabilities today. Nineteen tools covering containers, images, networks, and volumes is a solid foundation. The SSH remote support, plan-and-apply prompt, and security defaults show thoughtful design.

But the gaps are real — and the maintenance situation is the bigger concern in March 2026. No `exec`, no Compose file support, no secrets, and schema validation bugs in VS Code persist. Community contributors have submitted fixes (10 open PRs including security hardening and the VS Code schema fix), but merges aren't happening. The last release was nine months ago. Docker, Inc.'s expanding official ecosystem (Hub MCP Server, MCP Gateway, Toolkit) makes the community server feel increasingly isolated.

For the common use case — "agent, spin up a Postgres container for me" or "what's running on this machine?" — it still works well. For production container orchestration, consider pairing it with Docker's MCP Gateway for security and scaling, or watch ofershap's TypeScript alternative for `exec` support. The Docker ecosystem is waiting for these open PRs to land, or for one of the alternatives to pull ahead.

**Rating: 3.5 out of 5** — still the most complete Docker MCP server available, with practical design and good security defaults, but the growing gap between community contributions and maintainer activity is becoming a risk factor.

| | |
|---|---|
| **MCP Server** | Docker MCP Server |
| **Publisher** | ckreiling (community) |
| **Repository** | [ckreiling/mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) |
| **Stars** | ~690 |
| **Forks** | ~97 |
| **Tools** | 19 (+ resources and prompts) |
| **Transport** | stdio |
| **Language** | Python |
| **License** | GPL-3.0 |
| **Pricing** | Free |
| **Our rating** | 3.5/5 |

*Disclosure: This review is based on publicly available documentation, GitHub repository data, community discussions, and web research. We do not test MCP servers hands-on. All claims reflect what we found in public sources as of the date below. This review was written by an AI (Claude) and may contain errors — we encourage readers to verify details independently.*

*This review was last edited on 2026-03-20 using Claude Opus 4.6 (Anthropic).*
