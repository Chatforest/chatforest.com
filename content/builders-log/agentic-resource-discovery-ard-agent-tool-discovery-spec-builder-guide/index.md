---
title: "ARD: The Open Standard That Lets AI Agents Discover Tools at Runtime (And Why It Changes How You Ship)"
date: 2026-06-29
description: "Agentic Resource Discovery, released June 17 by Google, Microsoft, GitHub, Hugging Face, and 7 other companies, is the missing discovery layer for multi-agent systems. Here's how it works, what the ai-catalog.json manifest contains, and what builders need to do now."
og_description: "ARD solves the static-tool problem: instead of pre-installing every capability an agent might need, publish an ai-catalog.json and let agents find your tool at runtime. 11 companies, Apache 2.0, already live on GitHub Copilot. Here's the builder guide."
content_type: "Builder's Log"
categories: ["AI Agents", "Open Standards", "Developer Tools"]
tags: ["ard", "agentic-resource-discovery", "agent-discovery", "ai-catalog", "mcp", "github-copilot", "agent-finder", "open-spec", "multi-agent", "builders-log", "june-2026"]
sources_audited: 2026-07-31
---

On June 17, 2026, Google and Microsoft published a draft open specification called Agentic Resource Discovery (ARD) ([Google Developers Blog](https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/); [Microsoft Command Line](https://commandline.microsoft.com/agentic-resource-discovery-specification-ard/)). Eleven organizations backed the launch: Cisco, Databricks, GitHub, GoDaddy, Hugging Face, Microsoft, Nvidia, Salesforce, ServiceNow, Snowflake, and Google — confirmed by both companies' own announcement posts. The spec is [Apache 2.0](https://agenticresourcediscovery.org/spec/) and builds on the AI Catalog data model from the Linux Foundation's AI Catalog Working Group, which Google's launch post credits by name.

The first production implementation shipped the same day: [GitHub Copilot's Agent Finder](https://github.blog/changelog/2026-06-17-agent-finder-for-github-copilot-now-available/).

If you are building tools that agents can call — MCP servers, Skills, APIs, workflows — ARD is now the standard way to make them discoverable. Here is what it does and what to do about it.

---

## The Problem ARD Solves

Static agent configuration does not scale.

Today, if you want your MCP server to be available to a user's Claude Code session, they have to know it exists, add it to their config manually, and keep that config current. Same for Skills, API plugins, and every other agent capability. The agent universe is fracturing into hundreds of disconnected tool registries, each requiring a different installation step.

The deeper problem: agents themselves cannot discover capabilities they were not pre-wired with. A production agent handling a user's request cannot ask "what tool handles this?" at runtime — it can only use what was installed at configuration time. That constraint breaks the vision of general-purpose agentic systems.

ARD's [stated goal](https://huggingface.co/blog/agentic-resource-discovery-launch) is to shift "from manually installed, static catalogs to intent-based search that lets an agent find the right capability dynamically, and reach a growing ecosystem of MCP tools, A2A agents, and other services without pre-configuring each one."

---

## What ARD Is (and Is Not)

ARD is a **discovery protocol**. It [answers three questions](https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/) before invocation:

1. Where does the right capability live?
2. Which one should I use for this task?
3. Is it safe to connect to?

It is **not** an execution runtime. Per the [spec](https://agenticresourcediscovery.org/spec/), "Agent authentication is handled by the specific artifact protocol, not the discovery layer" — ARD does not replace MCP, Skills, A2A, or any API platform. Once an agent discovers a resource, it invokes it through that resource's own protocol — an MCP call, a REST API request, whatever that capability uses. ARD only covers the handshake before invocation.

It is also **not** a centralized catalog. The [spec explicitly supports federated, distributed registries](https://agenticresourcediscovery.org/faq/) — "clients decide which registries to query, and registries compose, so an organization can merge its own curated answer set with an upstream one." Enterprises can run internal registries alongside public ones, each with its own trust policies.

---

## Two Primitives

### 1. The `ai-catalog.json` Manifest

Any organization wanting to publish discoverable capabilities hosts a file at a well-known path on their domain:

```
https://yourdomain.com/.well-known/ai-catalog.json
```

The manifest describes available resources — each entry includes a natural-language description, supported media types, and [domain-anchored identity](https://agenticresourcediscovery.org/ai_catalog_spec/): entries reference URNs tied to a verified domain (e.g. `urn:ai:acme.com:tool:ocr`), and an optional `trustManifest` object layers on "verifiable detached JWS signatures" plus workload identity via "SPIFFE IDs, decentralized identifiers (DIDs), or standard HTTPS domains." Domain ownership provides the baseline identity foundation: a catalog at `api.yourcompany.com` is by definition controlled by whoever controls that domain.

Supported media types as of the current draft ([publishing guide](https://agenticresourcediscovery.org/how_to_publish/); [Hugging Face](https://huggingface.co/blog/agentic-resource-discovery-launch)):

- `application/ai-skill` — the default; a Skill-format resource
- `application/mcp-server+json` — an MCP server endpoint
- `application/vnd.huggingface.space+json` — Hugging Face Space

The format is protocol-agnostic: the same manifest envelope works for any capability type.

### 2. The Registry API

Registries are the discovery engines. A [registry crawls published `ai-catalog.json` files](https://agenticresourcediscovery.org/faq/) across domains and builds an index: "Registries act as search engines for the agentic web. They crawl published catalogs, index their contents, and make them searchable." When an agent submits a discovery query, the registry returns ranked, verifiable matches.

The core endpoint is a single `POST /search`, per [Hugging Face's own example](https://huggingface.co/blog/agentic-resource-discovery-launch):

```bash
curl https://huggingface-hf-discover.hf.space/search \
  -H "Content-Type: application/json" \
  -d '{"query": {"text": "fine tune a sentence transformer"}, "pageSize": 5}'
```

The query is natural language. The registry handles semantic matching. The response includes ranked results with trust metadata so the calling agent can evaluate safety before connecting.

[Hugging Face shipped the reference registry implementation](https://huggingface.co/blog/agentic-resource-discovery-launch) — their **Discover Tool** — at launch. It is live at `https://huggingface-hf-discover.hf.space/search` and also accessible as an MCP server at `https://huggingface-hf-discover.hf.space/mcp`.

---

## GitHub Agent Finder: The First Major Production Use

GitHub Copilot shipped [**Agent Finder**](https://github.blog/changelog/2026-06-17-agent-finder-for-github-copilot-now-available/) alongside the ARD announcement on June 17. It is the clearest signal that ARD is not vaporware.

Agent Finder [indexes ARD-compliant resources](https://github.blog/changelog/2026-06-17-agent-finder-for-github-copilot-now-available/) from GitHub's public catalog and any private registries the developer configures — "point agent finder at GitHub's curated public catalog, or at your own private registry of internal resources, and the answers an agent gets are scoped to that source." When a Copilot user issues a prompt, Agent Finder identifies which registered capabilities are relevant, ranks them, and injects them into the context window for the current task ("agents load what the work calls for instead of carrying every tool just in case") — without requiring the user to have pre-installed anything.

The key behavior: **presentation for approval, not silent installation**. Per [GitHub's own changelog](https://github.blog/changelog/2026-06-17-agent-finder-for-github-copilot-now-available/): "No auto installation: Agent finder finds the right tool at the right time. It doesn't silently connect anything. You stay in control of what actually gets wired in." That single design choice separates discovery (ARD's job) from authorization (the user's job) and keeps the trust model clean.

---

## How ARD Fits Into the Existing Stack

The spec positions ARD as sitting **above** existing protocols:

```
User intent
    ↓
ARD discovery (find the right capability)
    ↓
Invocation protocol: MCP / Skill / REST API / A2A
    ↓
Execution
```

If you have an MCP server today, you can make it ARD-discoverable by publishing a manifest that references it. Nothing about the MCP server changes. ARD does not wrap or replace the invocation layer.

Similarly for Skills: the spec defines `application/ai-skill` as a native media type, so existing Skill-format capabilities plug in without modification.

---

## What the Spec Does Not Cover

ARD [explicitly excludes authentication, authorization, and organizational trust decisions](https://agenticresourcediscovery.org/spec/): "Agent authentication is handled by the specific artifact protocol, not the discovery layer." The manifest and registry answer "what exists and where is it?" — they do not answer "is this organization allowed to use it?" That is left to existing governance layers (OAuth, API keys, enterprise policy).

The spec also does not define ranking algorithms; each registry implements its own matching and scoring logic. The [Hugging Face reference implementation](https://huggingface.co/blog/agentic-resource-discovery-launch) uses "the Hub's existing semantic search over Spaces." GitHub has not published Agent Finder's ranking methodology beyond describing the results as "ranked matches" — so the two registries' scoring logic cannot yet be compared in detail, but the spec leaving ranking unstandardized means each registry can (and does) differentiate on it.

---

## Builder Checklist

**If you publish an MCP server or Skill:**

- [ ] Create `https://yourdomain.com/.well-known/ai-catalog.json` describing your resource
- [ ] Set the correct media type (`application/mcp-server+json` for MCP servers)
- [ ] Write a clear natural-language description — registries rank on it, agents query against it
- [ ] Add a [trust manifest](https://agenticresourcediscovery.org/ai_catalog_spec/) (detached JWS signature, plus a SPIFFE ID, DID, or verified HTTPS domain) so registries can verify the catalog came from your domain
- [ ] Submit to the Hugging Face reference registry and watch for GitHub Agent Finder indexing

**If you build agent systems that consume capabilities:**

- [ ] Evaluate whether adding a registry query before capability lookup makes sense for your use case
- [ ] The Hugging Face registry is public and queryable now — try the `POST /search` endpoint
- [ ] MCP clients can connect directly to `https://huggingface-hf-discover.hf.space/mcp`
- [ ] Track which registries your enterprise needs: public (HF), GitHub-curated, and eventually your own internal registry

**If you run an enterprise agent platform:**

- [ ] Review whether you need a private internal registry (ARD is designed for federated deployment)
- [ ] The spec is still a draft — contribute feedback via the GitHub repo before it stabilizes

---

## Why This Matters Now

ARD is not theoretically interesting — it is already deployed in [GitHub Copilot](https://github.blog/changelog/2026-06-17-agent-finder-for-github-copilot-now-available/), shipped to production the same day the spec was announced rather than waiting for the standard to mature first. The spec may evolve; the pattern it establishes will not.

The broader shift is from agent systems where you know every capability at build time to agent systems where discovery happens at runtime based on intent. ARD is the first well-backed attempt to standardize that shift across the industry rather than let every vendor build a proprietary catalog.

If your tool or service can be called by an agent, and it is not ARD-discoverable, it will be harder to reach as more agent clients adopt runtime discovery. Publishing a manifest is low-cost. Not publishing one is a visibility bet you probably should not make.

The full specification is at [agenticresourcediscovery.org](https://agenticresourcediscovery.org/). The quickstart for publishing is at [agenticresourcediscovery.org/how_to_publish/](https://agenticresourcediscovery.org/how_to_publish/). Hugging Face's implementation details and CLI are at [huggingface.co/blog/agentic-resource-discovery-launch](https://huggingface.co/blog/agentic-resource-discovery-launch).
