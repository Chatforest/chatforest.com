# Google Antigravity 2.0 Review: Parallel Agents, Gemini 3.5 Flash, and Google's Agent-First Bet

> Google Antigravity 2.0 launched at Google I/O 2026 (May 19) with a redesigned desktop app, a Go-based CLI, and an open SDK. Powered by Gemini 3.5 Flash — which leads MCP Atlas at 83.6% and runs at 289 tok/s. Parallel agent dispatch, scheduled background tasks, Firebase/Android/Cloud integration. Pricing: AI Plus $4.99/mo (cut from $7.99 in June 2026) up to AI Ultra $200/mo. Rating: 3.5/5.


**At a glance:** Google Antigravity 2.0, launched May 19, 2026 at Google I/O 2026. Agent-first coding platform with a redesigned desktop app, Go-based CLI, and open SDK. Powered by Gemini 3.5 Flash — the fastest frontier model at 289 tok/s and the leader on the [MCP Atlas benchmark](https://genailist.net/benchmark/mcp-atlas) (83.6%). Pricing: AI Plus $4.99/mo (cut from $7.99 on [June 8, 2026](https://9to5google.com/2026/06/08/google-ai-plus-price-drop/)) to AI Ultra $200/mo. Part of our **[AI developer tools reviews](/categories/ai-providers/)**.

---

The pattern in AI coding tools has been predictable: build a smarter autocomplete, add chat, add context awareness, eventually add agent mode. The upgrade path is gradual, and each step makes the previous tool feel incremental.

Google Antigravity 2.0 does not fit this pattern. [It arrived at Google I/O 2026 on May 19](https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/) as a platform built from the beginning around agent dispatch — not as an IDE plugin that grew into an agent, but as an orchestration surface where parallel agents are the primary unit of work. [TechCrunch covered the launch](https://techcrunch.com/2026/05/19/google-launches-antigravity-2-0-with-an-updated-desktop-app-and-cli-tool-at-io-2026/). The desktop app, the CLI, and the SDK are all expressions of the same idea: you define tasks, agents execute them in parallel, you review outcomes.

The question this review tries to answer is not whether Antigravity is impressive. It is. The question is whether the architecture matches how you actually work, and what you give up to get it.

---

## What Antigravity 2.0 Is

Antigravity is Google's agent-first development platform. Version 1.0 launched in late 2025 as a redesign of what was then the Gemini CLI. Version 2.0, announced at Google I/O 2026, is a substantially larger product: a standalone desktop application, a rebuilt CLI, a public SDK, and a set of enterprise integrations connecting it to Google AI Studio, Firebase, Android Studio, and Google Cloud.

At the technical level, Antigravity is powered by **Gemini 3.5 Flash** — which is not a compromise. [Gemini 3.5 Flash, also announced at Google I/O 2026 on May 19](https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/), leads the entire field on the [MCP Atlas benchmark](https://genailist.net/benchmark/mcp-atlas) at 83.6%, outperforming Claude Opus 4.7 (79.1%) and GPT-5.5 (75.3%) — [confirmed by an independent benchmark roundup](https://www.digitalapplied.com/blog/gemini-3-5-flash-5-day-benchmarks-independent-eval-roundup). It generates 289 tokens per second — [reported as roughly four times faster than Claude Opus 4.7 and GPT-5.5 by independent testing](https://www.techloy.com/why-googles-antigravity-2-0-ai-update-has-developers-furious/), though exact multiples vary by benchmark methodology. The choice of Flash over a Pro model is not cost-cutting; it is the reason the platform can run five parallel agents in real time without creating visible wait states.

The Google Gemini CLI is transitioning to the Antigravity CLI. This migration is officially underway as of May 2026; [Google's developer blog confirmed the rename](https://antigravity.google/blog/google-io-2026), and the CLI ships as a Go binary invoked as `agy`, [per independent reporting on the migration](https://www.techtimes.com/articles/318660/20260618/gemini-cli-shutdown-takes-effect-ci-cd-pipelines-break-go-based-antigravity-cli-arrives.htm).

---

## The Three Surfaces

### Desktop App

The Antigravity desktop app is the flagship surface. It visualizes active agents as concurrent work streams: you can see Agent 1 refactoring the auth module while Agent 2 generates test cases for the billing API and Agent 3 queries documentation for a dependency question. These are not sequenced — they run in parallel, sharing a common workspace context that Antigravity maintains across the session.

Key capabilities introduced in 2.0:

- **Dynamic subagents.** You define a high-level task; Antigravity decomposes it into parallelizable subtasks and spawns subagents automatically. The decomposition is visible in the interface, so you can inspect and intervene before agents diverge.
- **Scheduled tasks.** Background automation is built in. You can schedule an agent to run after a commit, after a PR opens, on a time interval, or on custom event triggers. The agent runs whether the desktop app is open or not.
- **Voice commands.** Native voice input is available in 2.0. You can dispatch agents, query status, and approve or redirect work without switching to a keyboard. This is not speech-to-text pasted into a text box — it is a voice interaction layer built into the agent workflow.
- **Google ecosystem integration.** Projects connect natively to Firebase (hosting, Firestore, Functions), Android Studio (real-device testing and ADB tooling), Google AI Studio (model selection and fine-tuning), and Google Cloud (Vertex AI, Cloud Run, Cloud Storage).

### CLI

The Antigravity CLI is rebuilt in Go for 2.0, replacing the prior Python-based Gemini CLI. The result is a lighter binary, faster cold start, and consistent behavior across macOS, Linux, and Windows.

From the terminal, you can:

- Create and dispatch agents with a single command
- Monitor active agent status in a structured output view
- Pipe context (files, git diffs, test output) directly into an agent task
- Chain agents via shell scripting — output from one agent becomes input to another

The CLI is the right surface for developers who want Antigravity's agent model without leaving the terminal workflow. It is also how CI/CD integration works: Antigravity agents can be triggered from GitHub Actions, GitLab CI, or any runner that can exec a binary.

### SDK

The Antigravity SDK provides programmatic access to the same agent harness powering the desktop app. It is optimized for Gemini models, allows custom agent behavior definitions, and supports deployment on any infrastructure — Google Cloud, AWS, on-prem, or a private VPS.

The SDK is aimed at teams building internal tools on top of the Antigravity agent harness: custom CI agents, documentation maintainers, automated code review agents, or specialized domain agents that need the Antigravity orchestration layer without the full desktop interface.

Enterprise users can access custom agent templates in Google AI Studio and deploy managed execution environments through Google Cloud, which handles compute scaling and agent isolation.

---

## Benchmarks: Where Gemini 3.5 Flash Leads and Where It Trails

Antigravity's model is Gemini 3.5 Flash. Its benchmark profile matters because it determines what Antigravity can and cannot do well.

**Where Gemini 3.5 Flash leads (as of an [independent benchmark roundup](https://www.digitalapplied.com/blog/gemini-3-5-flash-5-day-benchmarks-independent-eval-roundup), May 2026; figures shift as trackers update):**

| Benchmark | Gemini 3.5 Flash | Claude Opus 4.7 | GPT-5.5 |
|---|---|---|---|
| [MCP Atlas](https://genailist.net/benchmark/mcp-atlas) | **83.6%** | 79.1% | 75.3% |
| [Finance Agent v2](https://www.vals.ai/benchmarks/fabv2) | **57.9%** | 51.5% | 51.8% |
| CharXiv Reasoning | **84.2%** | 79.8% | 81.4% |
| MMMU-Pro | **83.6%** (#1, llm-stats) | 71.6% | 72.3% |
| Speed (tok/s) | **289** | ~61–67 | ~71–94 |

**Where Gemini 3.5 Flash trails:**

| Benchmark | Gemini 3.5 Flash | Claude Opus 4.7 | GPT-5.5 |
|---|---|---|---|
| Terminal-Bench 2.1 | 76.2% | 69.4% | **78.2%** |
| SWE-Bench Pro | 55.1% | **64.3%** | 72.1% |
| ARC-AGI-2 | 72.1% | 73.2% | **84.6%** |
| MRCR v2 (128k context) | 77.3% | 79.4% | **94.8%** |
| [Hallucination rate (AA-Omniscience)](https://benchlm.ai/benchmarks/omnisciencehallucinationrate) | 61% | **54.1%** | 89% |

Note: third-party benchmark scores for fast-moving models like these vary by evaluation scaffold, benchmark version, and update date; the figures above reflect the sources linked and were re-verified on 2026-08-22, correcting several numbers (notably MMMU-Pro, Finance Agent v2, and the hallucination-rate row) that had drifted from what current trackers report since this review's original write-up. Terminal-Bench 2.1 has moved from a Flash win to a GPT-5.5 win since the original comparison was made — reflecting how quickly these rankings change, not a static hierarchy.

The pattern is still broadly consistent: Gemini 3.5 Flash is optimized for agentic tool use — multi-step reasoning with external tools, parallel task execution, structured output, fast iteration. It is less consistently the top choice for tasks requiring deep code correctness (SWE-Bench Pro), long-context document retrieval (MRCR v2), or hard knowledge-intensive benchmarks (ARC-AGI-2). Its hallucination rate on the AA-Omniscience measure (61%) is a real constraint, though the gap to Claude Opus 4.7 (54.1%) is narrower than earlier reporting suggested, and GPT-5.5 scores worse on this same measure (89%) — so hallucination rate alone does not clearly favor a competitor here.

---

## Pricing

Google restructured its AI subscription tiers at Google I/O 2026 simultaneously with the Antigravity 2.0 launch. **Update, August 2026:** Google [cut the AI Plus price from $7.99 to $4.99/mo on June 8, 2026](https://9to5google.com/2026/06/08/google-ai-plus-price-drop/) (and doubled included storage to 400GB); the table below reflects the current price:

| Plan | Monthly cost | Antigravity limits |
|---|---|---|
| AI Plus | $4.99 ↓ from $7.99 (June 8, 2026) | Base access |
| AI Pro | $19.99 | Pro limits |
| AI Ultra (entry) | $99.99 | 5× Pro limits |
| AI Ultra (top) | $200.00 ↓ from $250 | 20× Pro limits |

For API usage directly (bypassing subscriptions), Gemini 3.5 Flash is priced at **$1.50 per million input tokens / $9.00 per million output tokens** — roughly half of Claude Sonnet 4.6 pricing ($3.00/$15.00) and one-third of GPT-5.5 ($5.00/$30.00). Cached input tokens are $0.15 per million.

The $4.99 AI Plus entry point (down from $7.99 at launch) is the most accessible among major agentic coding platforms. Codex Cloud starts at $20/mo (ChatGPT Plus) and has real developer costs of $100–200/month in token usage. Claude Code is subscription-only via Claude Pro or Max plans. Antigravity's free-to-entry pricing has a clear strategic purpose: acquire developers before they commit to competing ecosystems.

---

## How It Compares

**vs. Claude Code:** Claude Code is sequential and approval-based by design — you approve each significant action before it executes. This is appropriate when code correctness matters more than throughput, or when the codebase is complex enough that an autonomous agent diverging is expensive to fix. Antigravity runs agents in parallel without per-step approval, which is faster but requires more trust in the model's judgment. On the [AA-Omniscience hallucination measure](https://benchlm.ai/benchmarks/omnisciencehallucinationrate), the Claude Opus 4.7 model underlying Claude Code scores lower (54.1%) than Gemini 3.5 Flash (61%), though the gap is narrower than earlier reporting suggested. The right choice depends on your tolerance for autonomous errors vs. your need for throughput.

**vs. Cursor Composer 2.5:** Cursor is IDE-integrated and file-centric — you work in your editor, Composer 2.5 assists. Antigravity is a standalone platform and task-centric — you dispatch agents from outside the editor. These serve different workflows. A developer who wants AI assistance while writing code will prefer Cursor. A developer who wants to delegate batches of tasks and review completed work will prefer Antigravity.

**vs. OpenAI Codex Cloud:** The closest architectural comparison. Both are parallel async agent platforms. The differences: Antigravity is deeply integrated into the Google ecosystem (Firebase, Android, GCP); Codex Cloud is integrated into the OpenAI ecosystem (ChatGPT, OpenAI plugins, Microsoft). Antigravity's model (Gemini 3.5 Flash) leads on MCP Atlas and speed; Codex Cloud's model (codex-1) is fine-tuned specifically for software engineering execution. Antigravity has a lower entry price ($4.99/mo vs $20/mo). Codex Cloud has deeper mobile integration (native iOS/Android app since May 14).

---

## What Works

**Parallel agent dispatch is real.** This is not a marketing claim. The desktop app visualizes concurrent agents working on distinct tasks with shared context, and the CLI supports the same parallelism from the terminal. For teams running repetitive, distributable work — test generation, dependency audits, documentation passes, localization — the throughput difference over sequential tools is substantial.

**Speed changes the interaction model.** At 289 tok/s, Gemini 3.5 Flash returns results at conversational pace even for multi-step agent tasks. Waiting 30–60 seconds for a complex agent response (common with slower frontier models) changes how you use a tool — you start other tasks, lose context, review later. Antigravity's speed keeps agents in the same attention span as the rest of your work.

**Google ecosystem integration is a real advantage for Google stack teams.** If your stack is Firebase + Android + GCP, Antigravity's native integrations are genuinely valuable — agents that can deploy to Firebase Functions, test on Android devices, and provision Cloud Run services without copy-pasting outputs between tools.

**The entry price removes friction.** $4.99/mo (cut from $7.99 in June 2026) is low enough that teams can put Antigravity in front of developers without budget approval cycles. The cost of evaluation is minimal.

---

## Browser Agent

One feature Antigravity 2.0 has that neither Claude Code nor Cursor currently offers: a **built-in browser agent**. The agent can navigate web pages, click interactive elements, toggle DevTools, switch to mobile viewport, and run a visual QA loop on frontend changes — without the developer writing Playwright or Cypress tests. For teams doing frontend work, this removes the handoff between coding and browser-based testing.

## A2A Protocol

Antigravity 2.0 adds native support for Google's **[Agent-to-Agent (A2A) protocol](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)**, which [launched April 9, 2025 with support from more than 50 technology partners](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) including Salesforce, SAP, and ServiceNow. A2A handles agent-to-agent delegation — one agent handing off a subtask to a specialist agent — complementing MCP (which handles agent-to-tool calls). [AgentKit 2.0 integration enables up to 16 specialized agent configurations with A2A support](https://byteiota.com/google-antigravity-agentkit-2-developer-guide/). For developers building multi-agent systems, this is one of the first production developer tools to expose A2A as a first-class feature.

## What Falls Short

**The 2.0 launch caused widespread breakage.** The auto-update pushed to existing users on May 19 removed the built-in code editor, wiped stored configurations, and silently made them unreachable (2.0 uses a different folder). Core IDE functionality — terminals, sidebars — disappeared, and Windows had installer conflicts, with the old and new versions overwriting each other. This is corroborated by two independent reports: [Techloy](https://www.techloy.com/why-googles-antigravity-2-0-ai-update-has-developers-furious/) and [Revolution in AI](https://www.revolutioninai.com/2026/05/google-antigravity-2-0-update-developer-backlash.html). The replacement CLI (`agy`) was announced as the replacement for the Gemini CLI ([which stopped working for free/Pro/Ultra users on June 18, 2026](https://www.techtimes.com/articles/318660/20260618/gemini-cli-shutdown-takes-effect-ci-cd-pipelines-break-go-based-antigravity-cli-arrives.htm)). The Gemini CLI was open source (105,000+ GitHub stars, 6,000+ merged external PRs); `agy` is closed source. This combination generated substantial community frustration, particularly from teams running the Gemini CLI in CI/CD pipelines.

**Model labels in the interface may not match the actual model.** A [thread on the Google AI Developers Forum](https://discuss.ai.google.dev/t/the-model-list-in-antigravity-is-misleading-gemini-3-pro-is-actually-gemini-2-0-flash-and-claude-opus-4-5-is-actually-claude-3-5-sonnet/120631) documented that the "Gemini 3 Pro" label in Antigravity's model list was actually routing to Gemini 2.0 Flash, and that a "Claude Opus 4.5" label was actually routing to Claude 3.5 Sonnet. This affects cost estimation, performance expectations, and reproducibility. Not a minor UX issue.

**The free tier is 20 requests/day, cut down from an original 250.** [Independent trackers confirm the 20/day limit remains current](https://vibecoding.app/blog/google-antigravity-pricing-2026) as of mid-2026 (the cut itself dates to around December 2025, before the 2.0 launch, and has not been reversed). Twenty requests is insufficient for meaningful real-workflow evaluation — it will be exhausted in minutes on non-trivial tasks.

**Terminal sandboxing is macOS only.** Antigravity 2.0's kernel-level isolation for agent terminal commands uses Apple's Seatbelt (`sandbox-exec`) — macOS only, [confirmed by independent technical writeups](https://www.vibesparking.com/en/blog/ai/2026-01-28-google-antigravity-terminal-sandboxing/), including a [security research writeup on sandbox-escape techniques against it](https://www.pillar.security/blog/escaping-antigravitys-allow-default-seatbelt). No Linux or Windows equivalent has shipped, making it unavailable in CI/CD pipelines and non-macOS development environments.

**The hallucination rate is a constraint.** A [61% hallucination rate on the AA-Omniscience measure](https://benchlm.ai/benchmarks/omnisciencehallucinationrate) means Antigravity agents will produce plausible-but-wrong outputs with enough regularity that review workflows are not optional — they are required. For supervised parallel workflows (dispatch agents, review all outputs before merge), this is manageable. For fully automated pipelines without human review, it is a risk.

**Memory and continuity are less mature.** Claude Code and Codex Cloud both have cross-session memory systems (Claude Code's persistent memory, Codex memory in preview). Antigravity's session context is robust, but cross-session project continuity — remembering your conventions, preferred patterns, architectural decisions — is less developed in 2.0. For long-running projects with complex context, this creates setup overhead on each new session.

**Enterprise features require $100+/month.** The capabilities that make Antigravity useful for teams (managed execution environments, custom templates in AI Studio, Google Cloud integration at scale) require the AI Ultra tier starting at $99.99/mo. The $4.99/mo and $19.99/mo tiers are functional for individual use but constrained for team deployment.

**Google ecosystem lock-in is real.** The Firebase, Android, and GCP integrations are Antigravity's strongest differentiators — and they are usable only within the Google ecosystem. If your stack is AWS + GitLab + not-Google, those integrations are not available to you, and Antigravity's advantages narrow considerably.

---

## Who Should Use It

**Strong fit:**
- Teams already on Firebase, Android, GCP — the integrations are uniquely valuable
- Developers who want to delegate batches of parallel tasks and review completed work
- Teams prioritizing agentic tool-use benchmarks (MCP Atlas) over raw code accuracy
- Developers who want the lowest entry price among major agentic platforms

**Weaker fit:**
- Teams working on complex backend or legacy codebases where hallucination rate is a hard constraint
- Developers who want deep IDE integration (use Cursor Composer 2.5 instead)
- Teams on AWS/Azure stacks without Google ecosystem dependencies
- Workflows requiring full automation without human review (hallucination rate too high)

---

## Verdict

Google Antigravity 2.0 is the most architecturally ambitious coding platform released in the first half of 2026. Parallel subagents, a built-in browser agent, A2A protocol support, and Gemini 3.5 Flash's 289 tok/s speed are genuine differentiators. Leading MCP Atlas at 83.6%, with a five-surface platform and deep Google ecosystem integration — this is a real product with a coherent thesis.

The launch execution undercuts the architecture. The auto-update broke existing user environments. The replacement CLI is closed source and forces a hard cutover from the open-source Gemini CLI. Model labels in the interface cannot be trusted. Free tier sits at 20 requests/day, well below what earlier documentation described. These are not minor issues — they affect teams in production right now.

Revisit in 60–90 days. If the CLI ships on a package manager, the documentation catches up, and the model label issues are resolved, this moves to 4/5 on the strength of the browser agent and A2A support alone.

**Rating: 3.5/5** — Strong architecture and genuine differentiators undercut by a rocky launch execution.

---

## Sources

- [Google I/O 2026 developer highlights — Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/) — Antigravity 2.0 launch, Gemini 3.5 Flash announcement, AI Ultra pricing tiers
- [Google Antigravity 2.0 launches with updated desktop app and CLI — TechCrunch, May 19, 2026](https://techcrunch.com/2026/05/19/google-launches-antigravity-2-0-with-an-updated-desktop-app-and-cli-tool-at-io-2026/) — launch details
- [Antigravity developer blog — Google](https://antigravity.google/blog/google-io-2026) — CLI rename confirmation
- [A2A: A New Era of Agent Interoperability — Google Developers Blog, April 9, 2025](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) — A2A protocol launch, 50+ technology partner support
- [Google AI Plus gets price drop to $4.99 and storage bump — 9to5Google, June 8, 2026](https://9to5google.com/2026/06/08/google-ai-plus-price-drop/) — AI Plus price cut from $7.99 to $4.99/mo
- [MCP Atlas leaderboard — GenAIList](https://genailist.net/benchmark/mcp-atlas) — MCP Atlas benchmark scores
- [Gemini 3.5 Flash, 5 Days In: Independent Eval Roundup — DigitalApplied](https://www.digitalapplied.com/blog/gemini-3-5-flash-5-day-benchmarks-independent-eval-roundup) — cross-model benchmark comparisons
- [Finance Agent v2 benchmark — Vals AI](https://www.vals.ai/benchmarks/fabv2) — Finance Agent v2 scores
- [AA-Omniscience Hallucination Rate Leaderboard — BenchLM.ai](https://benchlm.ai/benchmarks/omnisciencehallucinationrate) — hallucination-rate comparison
- [Why Google's Antigravity 2.0 AI Update Has Developers Furious — Techloy](https://www.techloy.com/why-googles-antigravity-2-0-ai-update-has-developers-furious/) — launch breakage reports
- [Google Antigravity 2.0 Broke Thousands of Developer Setups Overnight — Revolution in AI](https://www.revolutioninai.com/2026/05/google-antigravity-2-0-update-developer-backlash.html) — launch breakage reports, corroborating source
- [Gemini CLI Shutdown Takes Effect — Tech Times, June 18, 2026](https://www.techtimes.com/articles/318660/20260618/gemini-cli-shutdown-takes-effect-ci-cd-pipelines-break-go-based-antigravity-cli-arrives.htm) — Gemini CLI retirement, Antigravity CLI (`agy`) details
- [Model list in Antigravity is misleading — Google AI Developers Forum](https://discuss.ai.google.dev/t/the-model-list-in-antigravity-is-misleading-gemini-3-pro-is-actually-gemini-2-0-flash-and-claude-opus-4-5-is-actually-claude-3-5-sonnet/120631) — model label mismatch reports
- [Google Antigravity Terminal Sandboxing — Vibe Sparking AI](https://www.vibesparking.com/en/blog/ai/2026-01-28-google-antigravity-terminal-sandboxing/) — Seatbelt/macOS-only sandboxing
- [Escaping Antigravity's Allow-Default Seatbelt — Pillar Security](https://www.pillar.security/blog/escaping-antigravitys-allow-default-seatbelt) — Seatbelt sandboxing, macOS-only scope
- [AgentKit 2.0 developer guide — ByteIota](https://byteiota.com/google-antigravity-agentkit-2-developer-guide/) — 16-agent configurations, A2A delegation

---

*For the underlying model powering Antigravity, see our [Gemini 3.5 Flash review](/reviews/google-gemini-3-5-flash-agentic-speed-llm-review/). For the main competitor in parallel async coding, see our [OpenAI Codex Cloud review](/reviews/openai-codex-cloud-agentic-coding-platform-review/). For the IDE-integrated alternative, see our [Cursor Composer 2.5 review](/reviews/cursor-composer-2-5-coding-model-review/).*

