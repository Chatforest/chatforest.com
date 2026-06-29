# ARD: The Open Standard That Lets AI Agents Discover Tools at Runtime (And Why It Changes How You Ship)

> Agentic Resource Discovery, released June 17 by Google, Microsoft, GitHub, Hugging Face, and 8 other companies, is the missing discovery layer for multi-agent systems. Here's how it works, what the ai-catalog.json manifest contains, and what builders need to do now.


On June 17, 2026, Google and Microsoft published a draft open specification called Agentic Resource Discovery (ARD). Twelve organizations co-signed the launch: Cisco, Databricks, GitHub, GoDaddy, Hugging Face, Microsoft, Nvidia, Salesforce, ServiceNow, Snowflake, and Google. The spec is Apache 2.0, housed under the Linux Foundation's AI Catalog Working Group.

The first production implementation shipped the same day: GitHub Copilot's Agent Finder.

If you are building tools that agents can call — MCP servers, Skills, APIs, workflows — ARD is now the standard way to make them discoverable. Here is what it does and what to do about it.

---

## The Problem ARD Solves

Static agent configuration does not scale.

Today, if you want your MCP server to be available to a user's Claude Code session, they have to know it exists, add it to their config manually, and keep that config current. Same for Skills, API plugins, and every other agent capability. The agent universe is fracturing into hundreds of disconnected tool registries, each requiring a different installation step.

The deeper problem: agents themselves cannot discover capabilities they were not pre-wired with. A production agent handling a user's request cannot ask "what tool handles this?" at runtime — it can only use what was installed at configuration time. That constraint breaks the vision of general-purpose agentic systems.

ARD's stated goal is to shift from "manually installed, static catalogs to intent-based search that lets an agent find the right capability dynamically."

---

## What ARD Is (and Is Not)

ARD is a **discovery protocol**. It answers three questions before invocation:

1. Where does the right capability live?
2. Which one should I use for this task?
3. Is it safe to connect to?

It is **not** an execution runtime. ARD does not replace MCP, Skills, A2A, or any API platform. Once an agent discovers a resource, it invokes it through that resource's own protocol — an MCP call, a REST API request, whatever that capability uses. ARD only covers the handshake before invocation.

It is also **not** a centralized catalog. The spec explicitly supports federated, distributed registries — enterprises can run internal registries alongside public ones, each with its own trust policies.

---

## Two Primitives

### 1. The `ai-catalog.json` Manifest

Any organization wanting to publish discoverable capabilities hosts a file at a well-known path on their domain:

```
https://yourdomain.com/.well-known/ai-catalog.json
```

The manifest describes available resources — each entry includes a natural-language description, supported media types, and domain-anchored cryptographic identity (Ed25519). Domain ownership provides the baseline identity foundation: a catalog at `api.yourcompany.com` is by definition controlled by whoever controls that domain.

Supported media types as of the current draft:

- `application/ai-skill` — the default; a Skill-format resource
- `application/mcp-server+json` — an MCP server endpoint
- `application/vnd.huggingface.space+json` — Hugging Face Space

The format is protocol-agnostic: the same manifest envelope works for any capability type.

### 2. The Registry API

Registries are the discovery engines. A registry crawls published `ai-catalog.json` files across domains and builds an index. When an agent submits a discovery query, the registry returns ranked, verifiable matches.

The core endpoint is a single `POST /search`:

```bash
curl https://huggingface-hf-discover.hf.space/search \
  -H "Content-Type: application/json" \
  -d '{"query": {"text": "fine tune a sentence transformer"}, "pageSize": 5}'
```

The query is natural language. The registry handles semantic matching. The response includes ranked results with trust metadata so the calling agent can evaluate safety before connecting.

Hugging Face shipped the reference registry implementation — their **Discover Tool** — at launch. It is live at `https://huggingface-hf-discover.hf.space/search` and also accessible as an MCP server at `https://huggingface-hf-discover.hf.space/mcp`.

---

## GitHub Agent Finder: The First Major Production Use

GitHub Copilot shipped **Agent Finder** alongside the ARD announcement on June 17. It is the clearest signal that ARD is not vaporware.

Agent Finder indexes ARD-compliant resources from GitHub's public catalog and any private registries the developer configures. When a Copilot user issues a prompt, Agent Finder identifies which registered capabilities are relevant, ranks them, and injects them into the context window for the current task — without requiring the user to have pre-installed anything.

The key behavior: **presentation for approval, not silent installation**. Agent Finder surfaces matched resources and asks the developer to confirm before connecting. That single design choice separates discovery (ARD's job) from authorization (the user's job) and keeps the trust model clean.

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

ARD explicitly excludes authentication, authorization, and organizational trust decisions. The manifest and registry answer "what exists and where is it?" — they do not answer "is this organization allowed to use it?" That is left to existing governance layers (OAuth, API keys, enterprise policy).

The spec also does not define ranking algorithms. Each registry implements its own matching and scoring logic. The Hugging Face reference implementation uses semantic search over Space metadata; GitHub's Agent Finder uses a different ranking model. Competing registries means competing ranking quality — expect ecosystem differentiation on that axis.

---

## Builder Checklist

**If you publish an MCP server or Skill:**

- [ ] Create `https://yourdomain.com/.well-known/ai-catalog.json` describing your resource
- [ ] Set the correct media type (`application/mcp-server+json` for MCP servers)
- [ ] Write a clear natural-language description — registries rank on it, agents query against it
- [ ] Add Ed25519 domain identity so registries can verify the manifest came from your domain
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

ARD is not theoretically interesting — it is already deployed in the tool that millions of developers use daily (GitHub Copilot). The spec may evolve; the pattern it establishes will not.

The broader shift is from agent systems where you know every capability at build time to agent systems where discovery happens at runtime based on intent. ARD is the first well-backed attempt to standardize that shift across the industry rather than let every vendor build a proprietary catalog.

If your tool or service can be called by an agent, and it is not ARD-discoverable, it will be harder to reach as more agent clients adopt runtime discovery. Publishing a manifest is low-cost. Not publishing one is a visibility bet you probably should not make.

The full specification is at [agenticresourcediscovery.org](https://agenticresourcediscovery.org/). The quickstart for publishing is at [agenticresourcediscovery.org/how_to_publish/](https://agenticresourcediscovery.org/how_to_publish/). Hugging Face's implementation details and CLI are at [huggingface.co/blog/agentic-resource-discovery-launch](https://huggingface.co/blog/agentic-resource-discovery-launch).

