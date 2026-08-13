---
title: "The Docker MCP Server — Your AI Agent's Container Workshop"
date: 2026-03-14T12:14:00+09:00
description: "ckreiling's Docker MCP server gives AI agents full container lifecycle management — create, run, stop, build, plus networks and volumes. 736 stars, 99 forks, 19 tools, community-built. The maintainer resumed activity in August 2026, but the security vulnerabilities disclosed in April remain unaddressed past the June 24, 2026 disclosure deadline."
og_description: "Docker MCP server: 19 tools for containers, images, networks, volumes. 736 stars, 99 forks, PyPI v0.3.0, SSH remote support. Rating: 3/5."
content_type: "Review"
card_description: "Community Docker MCP server — 19 tools for container lifecycle, image management, networks, and volumes. Remote Docker via SSH, docker_compose prompt, security-conscious defaults. Maintainer resumed commits in August 2026 after a 14-month gap, but the disclosed security vulnerabilities are still open past the June 24, 2026 disclosure deadline."
last_refreshed: 2026-08-13
sources_audited: 2026-08-13
---

Nineteen tools. One Docker socket. And suddenly your AI agent can spin up containers, build images, manage networks, and handle volumes — all through natural language.

**At a glance:** ~[736 stars](https://github.com/ckreiling/mcp-server-docker/stargazers), [99 forks](https://github.com/ckreiling/mcp-server-docker/network/members), 54 commits, [14 open issues](https://github.com/ckreiling/mcp-server-docker/issues), [13 open PRs](https://github.com/ckreiling/mcp-server-docker/pulls), [PyPI v0.3.0](https://pypi.org/project/mcp-server-docker/) (August 2026), GPL-3.0. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

The [Docker MCP server](https://github.com/ckreiling/mcp-server-docker) by [Christian Kreiling](https://github.com/ckreiling) is the most comprehensive community-built MCP server for Docker operations. With 736 stars and 99 forks, it's been a popular choice for developers who want their AI agents to manage Docker environments directly. It's not official from Docker, Inc. — but it's what many people have used for container management. After 14 months of silence, the maintainer resumed activity in August 2026 — [merging a migration to the MCP Python SDK v2](https://github.com/ckreiling/mcp-server-docker/pull/56) and [cutting release v0.3.0 on August 7](https://github.com/ckreiling/mcp-server-docker/releases) — but the critical security vulnerabilities [disclosed in April](https://github.com/ckreiling/mcp-server-docker/issues/50) remain unaddressed, and the 90-day coordinated-disclosure deadline (June 24, 2026) has now passed with no maintainer response on record.

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

## What's New (August 2026 Update)

After **14 months of silence**, the maintainer resumed activity: [PR #56](https://github.com/ckreiling/mcp-server-docker/pull/56), migrating the server to the MCP Python SDK v2, was merged on **August 7, 2026** (opened by an automated integration bot and approved by Christian Kreiling), and [release v0.3.0](https://pypi.org/project/mcp-server-docker/) shipped the same day — the first release since v0.2.1 in June 2025. Several new community PRs followed within days, including two draft PRs adding a `SECURITY.md` policy file ([#57](https://github.com/ckreiling/mcp-server-docker/pull/57), [#58](https://github.com/ckreiling/mcp-server-docker/pull/58)). That said, the return to activity is partial: the specific critical vulnerability report below has received no maintainer response at all, even after the release.

**Security disclosure deadline has passed — no confirmed public fix.** [Issue #50](https://github.com/ckreiling/mcp-server-docker/issues/50) (opened April 7, 2026), filed by security researcher Håkon Åmdal, reports **host filesystem access and container escape vulnerabilities**. The researcher first emailed the maintainer on March 24, 2026 — after 14 days with no response, they escalated to a public GitHub issue and set a 90-day coordinated-disclosure deadline of **June 24, 2026**. As of this update (August 13, 2026), the issue is still open with **zero recorded maintainer response** — no GitHub comment, no linked PR or commit fixing it — even though the maintainer has since merged other work. We could not find evidence that Håkon Åmdal has published the promised full technical exploit details; the issue thread itself shows no such disclosure. Readers should treat the underlying vulnerability as unconfirmed-but-credible and unpatched, not resolved.

**MCPSafe automated security scan (May 12, 2026).** [Issue #51](https://github.com/ckreiling/mcp-server-docker/issues/51), filed by the automated `mcpsafe-gh` bot, reports an AIVSS score of **91/100 (Grade B)** — 2 medium-severity findings from automated analysis. Still open, no maintainer response. A second, independent (if automated) security signal on top of issue #50.

**Security hardening PR still unmerged.** [PR #49](https://github.com/ckreiling/mcp-server-docker/pull/49) (opened March 20, 2026) proposes blocking dangerous host paths in volume mounts and build contexts — directly relevant to the disclosed vulnerabilities. Still open roughly five months later, even after the maintainer's August activity.

**Schema validation fix still unmerged.** [PR #48](https://github.com/ckreiling/mcp-server-docker/pull/48) (opened March 19, 2026) would fix the VS Code Copilot validation errors reported in issues [#46](https://github.com/ckreiling/mcp-server-docker/issues/46) and [#25](https://github.com/ckreiling/mcp-server-docker/issues/25). Still unreviewed.

**13 open PRs, 1 merged since June 2025.** [PR #56](https://github.com/ckreiling/mcp-server-docker/pull/56) is the only merge in over a year. The rest span security-policy drafts, a `ServerSettings` fix (#52), exec support (#31), and several new fixes filed in the days right after the August release (#59, #60, #61).

**PulseMCP stats.** [~167K all-time visitors, ~7,300 weekly, ranked #275 globally (#168 in the past week)](https://www.pulsemcp.com/servers/ckreiling-mcp-server-docker) — a sharp jump in weekly traffic compared to earlier in 2026, plausibly tied to the resumed release activity and the ongoing security-issue discussion.

**Docker's official ecosystem continues to advance — and had its own scare.** The [Docker MCP Gateway](https://github.com/docker/mcp-gateway) (~1,500 stars) is now at v0.43.3 (July 16, 2026) and actively maintained. Two CVEs landed this year: [CVE-2026-33252](https://osv.dev/vulnerability/CVE-2026-33252) (CSRF in the Go MCP SDK's HTTP transport, CVSS 7.1, patched in go-sdk v1.4.1) and the more severe [CVE-2026-55887](https://github.com/docker/mcp-gateway/security/advisories/GHSA-r2xf-7jw5-pjg6) (CVSS 8.7 argument-injection flaw in the Gateway's own OCI-label parser, letting a malicious image label mount host paths or run as root — patched in Gateway v0.42.2). So Docker's official Gateway isn't immune to container-escape-class bugs either; the meaningful difference is that Docker shipped a fix within its own disclosure window, while ckreiling's issue #50 has sat unaddressed since April. The [MCP Catalog has 300+ servers](https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/), and [Dynamic MCP](https://docs.docker.com/ai/mcp-catalog-and-toolkit/dynamic-mcp/) lets agents add servers on-demand at runtime. The [Docker Hub MCP Server](https://github.com/docker/hub-mcp) (159 stars) handles image discovery. The gap between Docker's official MCP infrastructure and this community server remains large, even with the maintainer's August activity.

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

**Unpatched critical security vulnerabilities.** [Issue #50](https://github.com/ckreiling/mcp-server-docker/issues/50) discloses host filesystem access and container escape vulnerabilities. The maintainer has not responded to the security researcher's email (March 24) or the public issue (April 7) — and still hasn't even after resuming other repository activity in August. A security hardening PR (#49) addressing related attack vectors has also gone unreviewed. For a server with direct Docker socket access, this is a serious concern.

**14 months dark, then a partial return.** The repository went from v0.2.1/June 2025 to zero commits for over a year, then resumed in August 2026 with [PR #56 merged and v0.3.0 released](https://github.com/ckreiling/mcp-server-docker/releases) on August 7. Of 13 open PRs (including security fixes, exec support, and a stalled secrets PR), only that one has been merged since June 2025 — the disclosed security issue specifically has still received no maintainer response. [PulseMCP](https://www.pulsemcp.com/servers/ckreiling-mcp-server-docker) notes they are "temporarily maintaining the server.json file" themselves. GPL-3.0 licensing may further deter forks.

## How It Compares

The Docker MCP server space has shifted significantly. Docker, Inc.'s official ecosystem now dominates, and the community alternatives are mostly stalled — though ckreiling's own project shows that "stalled" isn't necessarily permanent.

**vs. [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp) (~497 stars, 66 forks):** Simpler — only 4 tools (create container, deploy compose, get logs, list containers). But it directly supports `docker-compose.yml` deployment, which ckreiling's doesn't. 12 open issues, 4 open PRs as of this update — modest but ongoing community activity. MIT licensed.

**vs. [ofershap/mcp-server-docker](https://github.com/ofershap/mcp-server-docker):** TypeScript alternative with a smaller tool set including `exec_command` (which ckreiling's lacks). Only 2 stars, but it has a commit as recent as August 10, 2026, so the "dormant" read from earlier in 2026 no longer holds — it's a low-adoption but currently-maintained project. MIT licensed.

**vs. [Docker Hub MCP Server](https://github.com/docker/hub-mcp) (159 stars):** Official Docker, Inc. project — manages Docker Hub (image discovery, repository management), not local containers. Complementary, not competitive. Apache-2.0 licensed.

**vs. Docker MCP Toolkit + Gateway (~1,500 stars, [v0.43.3](https://github.com/docker/mcp-gateway/releases)):** This is now the clear center of gravity. The Gateway is open source, ships with Docker Desktop, and the [MCP Catalog offers 300+ servers](https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/). It isn't invulnerable — a CVSS 8.7 argument-injection flaw ([CVE-2026-55887](https://github.com/docker/mcp-gateway/security/advisories/GHSA-r2xf-7jw5-pjg6)) was disclosed and patched (v0.42.2) in May-June 2026 — but the turnaround was weeks, not the months-and-counting silence on ckreiling's issue #50. [Dynamic MCP](https://docs.docker.com/ai/mcp-catalog-and-toolkit/dynamic-mcp/) lets agents discover and add servers on-demand, and [Docker Offload](https://docs.docker.com/offload/) scales agent workloads to the cloud. ckreiling's server could theoretically run *inside* the Toolkit, but Docker's own catalog increasingly offers equivalent container management capabilities — with active security maintenance that ckreiling's server still lacks for its highest-severity open issue.

**vs. [Kubernetes MCP servers](https://github.com/topics/mcp-kubernetes):** If you're at the Kubernetes scale, you need Kubernetes-specific tools. Docker MCP servers target the docker/docker-compose layer — local development, simple deployments, CI/CD pipelines. Different audience.

## The Bottom Line

The Docker MCP server was the most practical way to give AI agents Docker management capabilities. Nineteen tools covering containers, images, networks, and volumes is still a solid foundation, and the SSH remote support, plan-and-apply prompt, and security defaults showed thoughtful design.

By August 2026, the picture is mixed rather than uniformly worse. On one hand, the maintainer resumed activity: [PR #56 merged and v0.3.0 shipped on August 7](https://github.com/ckreiling/mcp-server-docker/releases), the first release in 14 months. On the other, **the critical security vulnerabilities disclosed in April remain unpatched and unacknowledged** (host filesystem access, container escape) — [issue #50](https://github.com/ckreiling/mcp-server-docker/issues/50) has zero maintainer response even after the August activity. A second, automated security signal arrived May 12 when [MCPSafe flagged AIVSS 91/100](https://github.com/ckreiling/mcp-server-docker/issues/51). Twelve of thirteen open community PRs remain unmerged, including a security hardening fix ([#49](https://github.com/ckreiling/mcp-server-docker/pull/49)) directly relevant to the disclosed vulnerabilities. **The 90-day coordinated-disclosure deadline of June 24, 2026 has now passed.** We found no evidence the researcher has published the promised exploit details, but the underlying report — and the maintainer's silence on it specifically — stands unresolved.

Meanwhile, Docker's official MCP ecosystem has matured further. The [MCP Gateway](https://github.com/docker/mcp-gateway) (~1,500 stars, v0.43.3) with its catalog of 300+ servers, Dynamic MCP, and Docker Offload provides a comprehensive, actively maintained alternative — one that also shipped a same-year container-escape-class CVE fix ([CVE-2026-55887](https://github.com/docker/mcp-gateway/security/advisories/GHSA-r2xf-7jw5-pjg6)) within weeks, not months.

For basic local use cases — "what containers are running?" or "spin up a Redis instance" — the server still functions, and the maintainer's return suggests the project is no longer flatly abandoned. But users should be aware that the specific disclosed security issue remains unpatched, especially in any environment where the Docker socket has access to sensitive workloads. For anything beyond experimentation, Docker's MCP Toolkit and Gateway remain the safer choice.

**Rating: 3 out of 5** *(unchanged since April 2026)* — the tool design remains solid, and the August 2026 release shows the project isn't dead, but a publicly disclosed critical security vulnerability that has now gone unaddressed past its own 90-day disclosure deadline — even through a maintainer's return to other activity — keeps this a risk to run in any serious environment. Docker's official ecosystem remains the better-governed alternative.

| | |
|---|---|
| **MCP Server** | Docker MCP Server |
| **Publisher** | ckreiling (community) |
| **Repository** | [ckreiling/mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) |
| **Stars** | ~736 |
| **Forks** | ~99 |
| **Tools** | 19 (+ resources and prompts) |
| **Transport** | stdio |
| **Language** | Python |
| **License** | GPL-3.0 |
| **Pricing** | Free |
| **Our rating** | 3/5 |

*Disclosure: This review is based on publicly available documentation, GitHub repository data, community discussions, and web research. We do not test MCP servers hands-on. All claims reflect what we found in public sources as of the date below. This review was written by an AI (Claude) and may contain errors — we encourage readers to verify details independently.*

*This review was last edited on 2026-08-13 using Claude Sonnet 5 (Anthropic).*
