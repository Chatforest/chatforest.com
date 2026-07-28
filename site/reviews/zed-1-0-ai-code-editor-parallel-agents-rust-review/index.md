# Zed 1.0 Review — The Fastest AI Code Editor, Now With Parallel Agents

> Zed 1.0 shipped April 29, 2026 — five years of development, written in Rust, built for the parallel-agent era. Native GPU rendering, Agent Client Protocol for Claude/Codex/Gemini CLI integration, and simultaneous multi-agent threads. Here is what it is, how it compares to Cursor and VS Code, and who should switch.


Zed ([zed.dev](https://zed.dev/)) shipped version 1.0 on [April 29, 2026](https://zed.dev/blog/zed-1-0) — [five years of development and more than a million lines of Rust](https://zed.dev/blog/zed-1-0) — and is the first stable release of an editor whose founders built [real-time collaborative editing on CRDT-based syncing as a founding technical bet](https://zed.dev/team), later adding [native, GPU-accelerated UI rendering](https://zed.dev/blog/videogame). The timing is deliberate: the 1.0 milestone arrives alongside a significant AI upgrade that makes Zed directly competitive with Cursor and GitHub Copilot in the agentic coding market.

The headline claim is performance. Zed is written natively in Rust rather than on Electron, the Chromium-based framework underlying both VS Code and Cursor (Cursor is [itself a fork of VS Code's codebase](https://visualstudiomagazine.com/articles/2026/01/26/what-a-difference-a-vs-code-fork-makes-antigravity-cursor-and-windsurf-compared.aspx)). Zed renders its own UI through [GPUI, a GPU-accelerated framework the team built from scratch](https://zed.dev/blog/videogame), which [engineering posts describe tuning to hold a 120-frames-per-second budget on Metal (macOS) and Vulkan (Linux)](https://zed.dev/blog/120fps). Independent reviews of the 1.0 release repeatedly describe the editor as faster to cold-start and lighter on idle memory than Electron-based alternatives — but the specific millisecond- and megabyte-level figures circulating across third-party comparison posts vary widely and inconsistently from source to source, and are not corroborated by any figures Zed itself has published, so we don't repeat a specific number here as established fact.

---

## What Zed Actually Is

Zed is a native code editor written in Rust, built by [Zed Industries](https://zed.dev/team). The company was founded by [Nathan Sobo, who led the Atom team at GitHub; Antonio Scandurra, who architected Atom's Teletype collaborative-editing package alongside Sobo; and Max Brunsfeld, creator of the Tree-sitter parsing framework](https://zed.dev/team). The editor began as a multiplayer-first tool — real-time collaborative editing was core, not an add-on — and has [added AI features since August 2024](https://zed.dev/blog/zed-ai).

At 1.0, the product spans three capability areas:

**Editor fundamentals**: Tree-sitter-based syntax highlighting and structural navigation, [language server protocol (LSP) support across roughly 80 documented languages](https://zed.dev/docs/languages), [multi-cursor editing, fuzzy file search, and syntax-tree-based navigation](https://zed.dev/features). The editing experience is deliberately minimal and fast.

**AI integration**: The built-in AI panel (powered by Anthropic, OpenAI, Google, or any OpenAI-compatible API with BYOK) handles inline completions, chat, and agentic edits. [Zeta2 is Zed's own open-weight edit-prediction model](https://zed.dev/blog/zeta2), trained specifically on open-source code for edit-prediction speed rather than general reasoning. [MCP server support](https://zed.dev/docs/ai/mcp) lets agents access filesystem, GitHub, Slack, and custom tools through the standard protocol.

**Agent Client Protocol (ACP)**: The headline 1.0 feature. [ACP is an open standard Zed created](https://zed.dev/acp) so that any AI agent can integrate natively with any compatible editor. At launch, [Claude Agent, Codex, and the open-source OpenCode support ACP and run directly inside Zed](https://zed.dev/blog/zed-1-0), building on [Gemini CLI's earlier reference-implementation integration](https://zed.dev/blog/bring-your-own-agent-to-zed). You can install, switch, and combine agents without leaving the editor.

---

## The Parallel Agents Feature

The architectural bet in Zed 1.0 is that the future of AI coding is concurrent — multiple agents working simultaneously on isolated worktrees, with the developer reviewing and merging their outputs.

The new [**Threads sidebar**](https://zed.dev/blog/parallel-agents) implements this. You open multiple agent threads in a single window, each working on a separate Git worktree branched from your current HEAD. One thread might be writing tests, another refactoring a data model, a third debugging a CI failure. When ready, you review each thread's diff and merge the results.

Cursor also runs multiple agents concurrently — [Cursor 2.0, announced in October 2025, lets up to eight background agents work in parallel across separate git worktrees or remote machines](https://cursor.com/blog/2-0) — so concurrent execution by itself isn't unique to Zed. What Zed's Threads sidebar adds is native, in-editor orchestration of ACP-based agents from multiple vendors (Claude Agent, Codex, Gemini CLI) side by side, rather than being tied to one vendor's own agent.

For throughput-limited workloads (large refactors, multi-file feature implementations, test generation at scale), running agents in parallel can reduce wall-clock time. The tradeoff is increased token spend and the coordination overhead of reviewing multiple concurrent diffs.

[**Terminal Threads**](https://zed.dev/blog/terminal-threads), which shipped in Zed 1.3.5 on May 20, 2026 (a few weeks after the 1.0 release), extend the same model to shell sessions: multiple terminal agents running in parallel, each in its own worktree, each visible in the sidebar.

---

## Agent Client Protocol in Practice

ACP solves a real problem: today's AI coding agents each have their own integration story. Cursor has [proprietary background/cloud agents](https://cursor.com/help/ai-features/background-agents), [Claude Code has its own IDE extension](https://code.claude.com/docs/en/overview), Codex has [a CLI](https://github.com/openai/codex). Every editor must individually implement each agent's API.

ACP inverts this. An agent that implements ACP once works inside any ACP-compatible editor. [Zed created and shipped ACP as the first production editor to support it](https://zed.dev/acp), and the protocol is open — [JetBrains has since partnered with Zed to bring native ACP support to IntelliJ IDEA, PyCharm, and WebStorm](https://blog.jetbrains.com/ai/2025/10/jetbrains-zed-open-interoperability-for-ai-coding-agents-in-your-ide/).

At 1.0, the practical benefit is that users can run Claude Agent or Codex inside Zed without patching together CLI wrappers. The agent sees the full editor context — open files, cursor position, selection, diagnostics — and can make edits using the same mechanisms as Zed's own inline AI.

[**MCP server support**](https://zed.dev/docs/ai/mcp) is separate from ACP but complementary. Agents running inside Zed can connect to any MCP server, giving them access to external context (databases, GitHub issues, documentation) through the same standard that [Claude Code](https://code.claude.com/docs/en/mcp), Cursor, and [Google's Antigravity IDE](https://antigravity.google/docs/mcp) also use.

---

## Performance vs. Alternatives

The core architectural difference is real and easy to verify even without precise benchmark numbers:

| Metric | Zed 1.0 | VS Code | Cursor |
|--------|---------|---------|--------|
| Runtime | [Native (Rust)](https://zed.dev/blog/zed-1-0) | Electron/Chromium | Electron/Chromium (Cursor is [a VS Code fork](https://visualstudiomagazine.com/articles/2026/01/26/what-a-difference-a-vs-code-fork-makes-antigravity-cursor-and-windsurf-compared.aspx)) |
| UI rendering | [GPU-accelerated (GPUI, Metal/Vulkan)](https://zed.dev/blog/120fps) | Chromium DOM | Chromium DOM |

VS Code and Cursor are both built on Electron, which runs a full Chromium runtime inside every editor process; Cursor is itself a fork of VS Code and inherits that architecture. Zed runs natively instead. Multiple independent reviewers report this translates into a faster cold start and lower idle memory use in practice, though the exact figures each reviewer reports differ enough from each other that we aren't treating any single third-party number as an authoritative, reproducible benchmark.

**What Cursor still wins on**: deep codebase context. Cursor's [Composer model](https://cursor.com/blog/2-0), [semantic codebase indexing that builds a searchable embedding index of the whole project](https://cursor.com/blog/secure-codebase-indexing), and [Cloud Agents (formerly called Background Agents) that run autonomously on dedicated remote VMs](https://cursor.com/help/ai-features/background-agents) are still ahead of Zed's Agent Panel on projects with hundreds of thousands of lines. The delta is narrowing as Zed ships ACP agent integrations, but if you're on a 500K-line monorepo and rely heavily on Cursor's retrieval, 1.0 is not yet a clean replacement.

---

## Extension Ecosystem Gap

This is the honest limitation. VS Code's marketplace, per [Microsoft's own documentation](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace), lists "thousands of extensions" spanning "hundreds of programming languages and tasks." Zed's extension marketplace, by contrast, [offers "hundreds of community-created extensions"](https://zed.dev/extensions), and growing.

Zed covers the essentials well: language servers, formatters, linters, debuggers, and themes for all mainstream languages. But niche language support, custom UI panels, framework-specific tooling, and enterprise integrations (Jira, Salesforce, Datadog) are sparse. The Zed extension API is different from VS Code's — existing VS Code extensions do not port without rewriting.

If your workflow depends on specific VS Code extensions, verify Zed equivalents exist before switching. The gap is closing with each weekly release but is real today.

---

## Pricing

Three tiers, [per Zed's pricing page](https://zed.dev/pricing):

- **Free**: 2,000 accepted edit predictions, plus unlimited use of any model via BYOK (your own API keys, any OpenAI-compatible endpoint, or [Ollama for local models](https://zed.dev/docs/ai/use-a-local-model)). Zed [retired its old "50 free hosted prompts per month" allowance when it moved hosted-model billing to a token-based model in September 2025](https://zed.dev/blog/pricing-change-llm-usage-is-now-token-based) — free-tier usage is no longer prompt-metered.
- **Pro**: [$10/month](https://zed.dev/pricing) — unlimited edit predictions, $5 of included monthly token credits (additional usage billed at API list price plus 10%), two-week free trial with $20 in initial credit
- **Business**: [$30 per seat per month](https://zed.dev/pricing) — org-wide AI model policies, data governance controls, unified spend visibility, and role-based access control on top of Pro features

The BYOK path is the practical choice for developers already paying for Claude, OpenAI, or Gemini API access. You bring your own keys, Zed provides the editor and ACP integration, and your usage goes entirely through your existing API contracts.

---

## Who Should Switch

**Switch now if you**: are performance-constrained on RAM-heavy machines, prioritize editor responsiveness above deep AI context features, work across multiple concurrent tasks that could benefit from parallel agent threads, or want native ACP integration with Claude Agent or Codex without CLI wrappers.

**Wait if you**: depend on VS Code extension ecosystem for critical workflows, work on large monorepos where Cursor's semantic codebase retrieval is central to your flow, or use enterprise AI integrations that haven't shipped ACP support yet.

**Run both if you**: want Zed for fast editing and terminal work while keeping Cursor for deep multi-file AI sessions.

---

## Assessment

Zed 1.0 is a strong architectural bet for the parallel-agent era. Native performance, ACP as an open standard, and concurrent agent execution via isolated Git worktrees are sound design decisions. The extension ecosystem gap and Cursor's remaining codebase-retrieval advantage mean it is not a universal replacement today.

**Rating: 4 / 5** — Among the fastest AI code editors in production thanks to its native Rust/GPU architecture, with a clean, native multi-agent (ACP) architecture. Excellent for performance-sensitive or parallel-workflow use cases. The extension ecosystem gap holds it from 5 for users migrating from VS Code with heavy plugin dependencies.

*ChatForest researches and reviews AI tools; we do not test them hands-on.*

