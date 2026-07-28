# Windsurf 2.0 Review — Devin in the IDE, Agent Command Center, and SWE-1.5 at 950 Tokens/Second

> Windsurf 2.0 (April 15, 2026) ships the first deep IDE + cloud agent integration: Devin now runs directly inside the editor, an Agent Command Center manages all sessions in one Kanban view, and Cognition's SWE-1.5 model hits 950 tokens/second. Here's what works and what doesn't.


**At a glance:** [Windsurf 2.0](https://devin.ai/blog/windsurf-2-0/). Released April 15, 2026. Developer: Cognition AI ([acquired Windsurf / Codeium in July 2025](https://cognition.com/blog/windsurf)). Key features: Agent Command Center, Devin integration, Spaces, SWE-1.5 model at 950 tok/s, Codemaps. Pricing: Free / Pro ($20/mo) / Max ($200/mo) / Teams ($40/user/mo) / Enterprise. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

Windsurf did not start as an ambitious product. It started as Codeium — a free AI autocomplete extension that did one thing well and charged nothing for it. For most of 2022–2024, that was the pitch: solid code completion, generous free tier, no credit system to worry about.

The [rebrand to Windsurf in April 2025](https://devin.ai/blog/windsurf-rebrand-announcement/) was the first signal that the product was changing directions. The [acquisition by Cognition AI in July 2025](https://cognition.com/blog/windsurf) — [an estimated $250M](https://techcrunch.com/2025/08/01/more-details-emerge-on-how-windsurfs-vcs-and-founders-got-paid-from-the-google-deal/) for a company with [$82M ARR and 350+ enterprise customers](https://cognition.com/blog/windsurf), and roughly [210 of its ~250 employees](https://techcrunch.com/2025/08/01/more-details-emerge-on-how-windsurfs-vcs-and-founders-got-paid-from-the-google-deal/) staying on after Google hired away its CEO and a handful of researchers — confirmed it. Cognition makes Devin, the cloud autonomous coding agent. The acquisition made the thesis obvious: put the cloud agent inside the IDE.

Windsurf 2.0 is that thesis, shipped.

---

## The Acquisition Context

Understanding what Windsurf 2.0 is requires understanding why Cognition bought Codeium.

Devin — Cognition's original product — is a cloud agent that handles complex software engineering tasks autonomously: debugging, deployment, testing, code review. [It runs on its own VM with a browser, terminal, and computer-use capabilities](https://docs.devin.ai/desktop/devin). It keeps working after you close your laptop. The limitation is distribution: Devin lives at a URL, not inside the tools developers already use.

Windsurf — formerly Codeium — had the opposite profile. It was a local IDE with strong developer adoption ([1M+ developers within four months of its November 2024 launch](https://www.lennysnewsletter.com/p/the-untold-story-of-windsurf-varun-mohan), per co-founder and CEO Varun Mohan), a capable agentic layer called Cascade, and a customer base that already trusted it for daily coding. Its weakness was cloud reach: everything stayed local.

The acquisition fused both: Devin gets the IDE distribution channel; Windsurf gets the cloud agent tier. That's Windsurf 2.0.

---

## Agent Command Center

The highest-concept feature in Windsurf 2.0 is the **[Agent Command Center](https://devin.ai/blog/windsurf-2-0/)** — a Kanban-style panel inside the editor that shows every agent session, local and cloud, organized by status.

This is a new UX paradigm for coding tools. The traditional model is: one IDE session, one developer, sequential work. Windsurf 2.0 proposes: one interface, multiple agent sessions running in parallel, with the developer acting more as a director than a coder.

Each card in the Agent Command Center represents an agent session — a local Cascade session working in the current workspace, or a Devin cloud session running on a remote VM. You can see what each agent is doing, review its progress, redirect it, or promote its output back into your editor. You do not need to switch windows or tab between browser and terminal to track cloud work.

The practical implication: you can start a Cascade session to refactor a local module, hand off a deployment task to Devin, and monitor both in the same vertical pane while you write new code. Neither task blocks the other. Neither requires your attention until something needs review.

Whether developers actually work this way depends on the individual, but the interface is well-designed for those who do.

---

## Spaces: Context That Persists Across Sessions

Windsurf 2.0 adds **[Spaces](https://www.testingcatalog.com/windsurf-2-0-adds-devin-and-agent-command-center/)** as the organizational layer above individual sessions.

A Space groups everything related to a task or project: agent sessions (local and cloud), pull requests, files, and shared context. When you open a new agent session inside a Space, it inherits the accumulated context from previous sessions — the project conventions, relevant files, decisions that were made. The agent does not start cold.

This is a meaningful quality-of-life improvement. One of the persistent frustrations with agentic coding tools is that each new session requires re-establishing context. Paste the same background, re-explain the constraints, re-specify the style guide. Spaces reduces that by carrying project knowledge forward.

In practice, Spaces work well for medium-term projects — a sprint, a feature branch, a debugging investigation. They're less useful for one-off tasks, and the context accumulation can occasionally work against you if earlier sessions made decisions you've since revised. There's no explicit mechanism for pruning outdated context from a Space.

---

## Devin Integration

**Devin cloud agent** is now available directly inside Windsurf, [included in Pro, Max, and Teams plans](https://www.testingcatalog.com/windsurf-2-0-adds-devin-and-agent-command-center/). [New GitHub connections receive up to $50 in initial usage credits](https://www.testingcatalog.com/windsurf-2-0-adds-devin-and-agent-command-center/).

The flow: plan locally with Cascade, identify a task that needs autonomous multi-step execution — a complex deployment, a testing pass, a documentation update — and delegate to Devin with one click. Devin picks up the task in the Agent Command Center, runs on its cloud VM, and continues working independently. You can close the laptop. The PR it produces appears in your editor when it's done.

The integration is smoother than the previous workflow of switching to a separate Devin session and re-establishing context. The handoff from Cascade to Devin is one action. The review happens inside the same interface.

Two caveats worth noting:

First, **Devin is still rolling out gradually**. As of mid-April 2026, [some Pro subscribers did not see Devin Cloud in their Windsurf interface; Cognition's own guidance was to log out and log back in](https://docs.devin.ai/desktop/changelog). The rollout is gradual by design — cloud agent compute is expensive to provision — but it means the headline feature of 2.0 is not uniformly available at launch.

Second, **cloud agents involve trust questions** that local agents don't. Devin is operating on your codebase, making commits, potentially touching deployment pipelines, from a cloud VM you don't control directly. Cognition's security posture for Devin is documented, but this is meaningfully different from a local Cascade session. Enterprise customers will need to evaluate this carefully.

---

## SWE-1.5: Speed as a Feature

Cognition shipped a proprietary coding model alongside the Devin integration: **SWE-1.5**.

The headline claim: [950 tokens/second — 13× faster than Claude Sonnet 4.5 and 6× faster than Claude Haiku 4.5](https://devin.ai/blog/swe-1-5/), achieved by partnering with Cerebras for inference. In practical terms, a Kubernetes manifest edit that took a typical agent 20 seconds now completes in under 5 seconds.

Speed matters more than it sounds for agentic coding. The bottleneck in an agentic loop is often not the quality of any individual output — it is the latency between steps. A slow model creates a rhythm where developers fall out of flow: you issue an instruction, the agent runs, you wait, you review, you issue the next instruction. At 950 tokens/second, those waits shrink to the point where the loop feels more like conversation than batch processing.

[SWE-1.5 is available alongside Claude Sonnet 4.6 and GPT-5.4](https://docs.devin.ai/desktop/models) on paid plans. Users choose which model to use per session; SWE-1.5 is not the only option.

What Cognition does not claim for SWE-1.5 is quality leadership. The model is positioned on speed, not on benchmark supremacy. For complex reasoning tasks — novel architectural decisions, sophisticated debugging, code design tradeoffs — users will likely route to Claude Sonnet 4.6 or GPT-5.4. SWE-1.5 is the right choice for high-frequency tasks where latency matters more than depth.

---

## Codemaps: The Differentiator Nobody Else Has

**Codemaps** is a feature in Windsurf's stack that, [by Cognition's own description, has no direct equivalent in Copilot, Claude Code, or Codex](https://cognition.com/blog/codemaps) as of May 2026.

[Codemaps generates AI-annotated visual navigation of a codebase](https://cognition.com/blog/codemaps). Instead of static file trees or text-search, Codemaps builds a live, semantically-aware diagram of the codebase: modules, their relationships, the data flowing between them, and AI annotations explaining non-obvious patterns.

The use case this solves is well-known to anyone who has inherited a large monorepo or legacy codebase: how do you understand a system you didn't build? Traditional tools give you a directory tree and a grep. Codemaps gives you a diagram that understands what the code does, not just what it's named.

The limitation is that it requires time to build the map — for large codebases, the initial generation takes meaningful compute. But once built, navigating and understanding unfamiliar code becomes qualitatively different.

As of this writing, Cursor 3, GitHub Copilot, Grok Build, and Amazon Kiro have not announced a directly comparable feature.

---

## Competitive Position vs. Cursor 3

Windsurf's most direct competitor is **Cursor 3**, which shipped [Build in Parallel](https://cursor.com/changelog/05-07-26) (May 7, 2026) and [Composer 2.5](https://cursor.com/blog/composer-2-5) (May 18, 2026).

The comparison:

| Feature | Windsurf 2.0 | Cursor 3 |
|---|---|---|
| Parallel agent sessions | Yes (Agent Command Center) | Yes (Build in Parallel) |
| Cloud agent integration | Yes (Devin, included) | No (local only) |
| Proprietary model | SWE-1.5 (950 tok/s, speed-focused) | Not confirmed |
| Visual code navigation | Codemaps (unique) | No |
| Free tier | Yes (limited quota) | Yes (limited quota) |
| Pro pricing | $20/mo | $20/mo |

Both tools are at parity on parallel local agents and base pricing. Windsurf pulls ahead on the cloud agent story — Devin integration has no direct Cursor equivalent. Cursor has a larger developer community and an established ecosystem of integrations, which is a real advantage for non-technical vibe-coding adoption.

The honest answer is that the right choice between them depends on your workflow. If you are writing solo or in small teams with tight local iteration loops, Cursor 3 is an excellent tool and the ecosystem advantage is real. If you are managing multiple concurrent coding workstreams — including tasks you want to hand off to cloud execution — Windsurf 2.0's architecture is more purpose-built for that.

---

## Pricing

| Plan | Price | Key inclusions |
|---|---|---|
| Free | $0 | Limited daily/weekly quota, unlimited Tab autocomplete |
| Pro | $20/mo | Full quota, all models (Claude Sonnet 4.6, GPT-5.4, SWE-1.5), Devin access |
| Max | $200/mo | Higher quota for heavy users |
| Teams | $40/user/mo | Everything in Pro + admin controls, centralized billing, priority support |
| Enterprise | Custom | SSO, RBAC, hybrid deployment, volume discounts |

Pricing per [Devin's official pricing page](https://devin.ai/pricing) (Windsurf plans are now sold under the Devin/Cognition pricing structure).

One note on the free tier: Tab autocomplete does not consume quota. For developers who want Windsurf primarily as an autocomplete tool with occasional deeper agent sessions, the free tier is genuinely useful rather than a trial gimmick.

---

## What to Watch

Three things that will determine whether Windsurf 2.0 holds its position:

**Devin rollout completion.** The gradual availability at launch is pragmatic but creates an uneven user experience. Once Devin is uniformly accessible for Pro subscribers, the value proposition of the $20 tier — a cloud autonomous agent bundled in — becomes a strong differentiator.

**SWE-1.5 quality trajectory.** Right now SWE-1.5 is positioned on speed. If Cognition can improve quality benchmarks while maintaining throughput, it becomes a genuine two-axis advantage. If quality stays at the current level, SWE-1.5 remains useful but not decisive.

**Codemaps expansion.** Codemaps is unique today. The question is whether Cursor, GitHub Copilot, or Amazon Kiro ships a comparable feature in 2026. If they do, the differentiator window closes. Cognition's advantage here is time-to-market, not a moat.

---

## Bottom Line

Windsurf 2.0 is the most structurally novel IDE update of 2026. Not because it is better than the alternatives at any single task, but because it proposes a different model of how developers work: directing a portfolio of agents — local and cloud — rather than pairing with a single assistant.

The Agent Command Center and Spaces make that model navigable. Devin gives it a cloud execution tier. SWE-1.5 removes the speed tax from high-frequency loops. Codemaps adds a capability no competitor currently offers.

The caveats are real: Devin's gradual rollout, the trust questions around cloud agents in codebases, and Cursor's stronger developer community. But those are launch frictions, not architectural flaws.

For developers who manage multiple concurrent coding projects and want a tool built around that workflow, Windsurf 2.0 is the best-positioned option as of May 2026.

**Rating: 4/5** — Genuine architectural advance with unique features; limited by Devin's incomplete rollout and a still-developing quality story for SWE-1.5.

---

**What to read next:** For competitive context, see our **[Cursor Composer 2.5 review](/reviews/cursor-composer-2-5-coding-model-review/)**, **[Amazon Kiro review](/reviews/amazon-kiro-aws-agentic-ide-spec-driven-review/)**, and **[Grok Build review](/reviews/xai-grok-build-terminal-coding-agent-review/)**. For the cloud agent comparison, see our **[Microsoft Agent 365 review](/reviews/microsoft-agent-365-m365-e7-frontier-suite-enterprise-ai-governance-review/)**.

---

## Sources

- [Devin.ai Blog: Windsurf 2.0 — Introducing the Agent Command Center and Devin in Windsurf](https://devin.ai/blog/windsurf-2-0/)
- [Testing Catalog: Windsurf 2.0 adds Devin and Agent Command Center](https://www.testingcatalog.com/windsurf-2-0-adds-devin-and-agent-command-center/)
- [CodePick: Windsurf 2.0 deep dive — full evolution after the Cognition acquisition](https://codepick.dev/en/guides/windsurf-2-new-features/)
- [Cognition: Cognition's acquisition of Windsurf](https://cognition.com/blog/windsurf)
- [TechCrunch: More details emerge on how Windsurf's VCs and founders got paid from the Google deal](https://techcrunch.com/2025/08/01/more-details-emerge-on-how-windsurfs-vcs-and-founders-got-paid-from-the-google-deal/)
- [Devin.ai Blog: The Next Chapter — Renaming to Windsurf](https://devin.ai/blog/windsurf-rebrand-announcement/)
- [Lenny's Newsletter: The untold story of Windsurf (Varun Mohan)](https://www.lennysnewsletter.com/p/the-untold-story-of-windsurf-varun-mohan)
- [Devin Docs: Devin in Devin Desktop](https://docs.devin.ai/desktop/devin)
- [Devin Docs: Changelog](https://docs.devin.ai/desktop/changelog)
- [Devin Docs: AI Models](https://docs.devin.ai/desktop/models)
- [Devin.ai Blog: Introducing SWE-1.5 — Our Fast Agent Model](https://devin.ai/blog/swe-1-5/)
- [Cognition: Windsurf Codemaps — Understand Code, Before You Vibe It](https://cognition.com/blog/codemaps)
- [Cursor Changelog: PR Review, Build Plan in Parallel, and Split PRs (05-07-26)](https://cursor.com/changelog/05-07-26)
- [Cursor Blog: Introducing Composer 2.5](https://cursor.com/blog/composer-2-5)
- [Devin.ai: Pricing](https://devin.ai/pricing)

