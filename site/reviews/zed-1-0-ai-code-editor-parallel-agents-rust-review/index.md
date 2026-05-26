# Zed 1.0 Review — The Fastest AI Code Editor, Now With Parallel Agents

> Zed 1.0 shipped April 29, 2026 — five years of development, written in Rust, built for the parallel-agent era. 0.6s cold start, 222MB RAM, Agent Client Protocol for Claude/Codex/Gemini CLI integration, and simultaneous multi-agent threads. Here is what it is, how it compares to Cursor and VS Code, and who should switch.


Zed ([zed.dev](https://zed.dev/)) shipped version 1.0 on April 29, 2026 — five years of weekly builds, more than a million lines of Rust, and the first stable release of an editor that was architected from day one around native GPU rendering and collaborative multiplayer editing. The timing is deliberate: the 1.0 milestone arrives alongside a significant AI upgrade that makes Zed directly competitive with Cursor and GitHub Copilot in the agentic coding market.

The headline claim is performance. Independent benchmarks measured 0.6-second cold start versus 1.3 seconds for VS Code and 4.5 seconds for Cursor on equivalent hardware, 222 MB idle RAM versus 3.5 GB for VS Code, and 2 ms input latency versus approximately 30 ms — rendering at 120 frames per second on GPU-accelerated Metal and Vulkan backends. The numbers have been consistent across reviewers and represent a real architectural advantage.

---

## What Zed Actually Is

Zed is a native code editor written in Rust, built by Zed Industries. The company was founded by Nathan Sobo (former Atom lead at GitHub), Antonio Dozortcev, and Max Brunsfeld. The editor began as a multiplayer-first tool — real-time collaborative editing was core, not an add-on — and has accumulated AI-first features at pace since 2024.

At 1.0, the product spans three capability areas:

**Editor fundamentals**: Tree-sitter-based syntax highlighting and structural navigation, language server protocol (LSP) support across 80+ languages, multi-cursor editing, fuzzy file search, and Git integration with branch history and inline blame. The editing experience is deliberately minimal and fast.

**AI integration**: The built-in AI panel (powered by Anthropic, OpenAI, Google, or any OpenAI-compatible API with BYOK) handles inline completions, chat, and agentic edits. The new Zeta2 model is Zed's own open-weight edit-prediction model, tuned specifically for code completion speed rather than general reasoning. MCP server support lets agents access filesystem, GitHub, Slack, and custom tools through the standard protocol.

**Agent Client Protocol (ACP)**: The headline 1.0 feature. ACP is an open standard Zed created so that any AI agent can integrate natively with any compatible editor. At launch, Claude Agent, OpenAI Codex, Gemini CLI, and the open-source OpenCode all support ACP and run directly inside Zed. You can install, switch, and combine agents without leaving the editor.

---

## The Parallel Agents Feature

The architectural bet in Zed 1.0 is that the future of AI coding is concurrent — multiple agents working simultaneously on isolated worktrees, with the developer reviewing and merging their outputs.

The new **Threads sidebar** implements this. You open multiple agent threads in a single window, each working on a separate Git worktree branched from your current HEAD. One thread might be writing tests, another refactoring a data model, a third debugging a CI failure. When ready, you review each thread's diff and merge the results.

This is meaningfully different from "background agents" in Cursor, which queue tasks sequentially. Zed's parallel execution is real concurrency — bounded by your API rate limits and token budget, not the editor's architecture.

For throughput-limited workloads (large refactors, multi-file feature implementations, test generation at scale), the parallel thread model can reduce wall-clock time significantly. The tradeoff is increased token spend and the coordination overhead of reviewing multiple concurrent diffs.

**Terminal Threads** extend the same model to shell sessions: multiple terminal agents running in parallel, each in its own worktree, each visible in the sidebar.

---

## Agent Client Protocol in Practice

ACP solves a real problem: today's AI coding agents each have their own integration story. Cursor has proprietary background agents, Claude Code has its own extension, Codex has a CLI. Every editor must individually implement each agent's API.

ACP inverts this. An agent that implements ACP once works inside any ACP-compatible editor. Zed is the first production editor to ship ACP support, but the protocol is open and the Zed team is actively working with the agent ecosystem to drive adoption.

At 1.0, the practical benefit is that users can run Claude Agent or Codex inside Zed without patching together CLI wrappers. The agent sees the full editor context — open files, cursor position, selection, diagnostics — and can make edits using the same mechanisms as Zed's own inline AI.

**MCP server support** is separate from ACP but complementary. Agents running inside Zed can connect to any MCP server, giving them access to external context (databases, GitHub issues, documentation) through the same standard that Claude Code, Cursor, and Antigravity use.

---

## Performance vs. Alternatives

The performance gap is real and measurable:

| Metric | Zed 1.0 | VS Code | Cursor |
|--------|---------|---------|--------|
| Cold start | 0.6s | 1.3s | 4.5s |
| Idle RAM | 222 MB | 3,549 MB | ~3.7 GB |
| Input latency | ~2 ms | ~30 ms | ~30 ms |
| GPU rendering | Native | Electron | Electron |

VS Code and Cursor are built on Electron, which adds a full Chromium runtime to every editor process. Zed runs natively, and the numbers reflect it. On a MacBook with many browser tabs open, the RAM difference is noticeable. On an older machine, the cold-start difference is the reason users switch.

**What Cursor still wins on**: deep codebase context. Cursor's multi-version Composer, @codebase retrieval with semantic search across large repos, and Background Agents with persistent memory are still ahead of Zed's Agent Panel on projects with hundreds of thousands of lines. The delta is narrowing as Zed ships ACP agent integrations, but if you're on a 500K-line monorepo and rely heavily on Cursor's retrieval, 1.0 is not yet a clean replacement.

---

## Extension Ecosystem Gap

This is the honest limitation. VS Code has 40,000+ extensions. Zed has hundreds, growing.

Zed covers the essentials well: language servers, formatters, linters, debuggers, and themes for all mainstream languages. But niche language support, custom UI panels, framework-specific tooling, and enterprise integrations (Jira, Salesforce, Datadog) are sparse. The Zed extension API is different from VS Code's — existing VS Code extensions do not port without rewriting.

If your workflow depends on specific VS Code extensions, verify Zed equivalents exist before switching. The gap is closing with each weekly release but is real today.

---

## Pricing

Three tiers at 1.0:

- **Free**: 50 Zed-hosted AI prompts per month, plus unlimited use of any model via BYOK (your own API keys, any OpenAI-compatible endpoint, or Ollama for local models)
- **Pro**: $20/month — 500 hosted prompts, $5/month in monthly token credits, two-week free trial with $20 initial credit
- **Business**: Team billing and centralized management, pricing not publicly listed

The BYOK path is the practical choice for developers already paying for Claude, OpenAI, or Gemini API access. You bring your own keys, Zed provides the editor and ACP integration, and your usage goes entirely through your existing API contracts.

---

## Who Should Switch

**Switch now if you**: are performance-constrained on RAM-heavy machines, prioritize editor responsiveness above deep AI context features, work across multiple concurrent tasks that could benefit from parallel agent threads, or want native ACP integration with Claude Agent or Codex without CLI wrappers.

**Wait if you**: depend on VS Code extension ecosystem for critical workflows, work on large monorepos where Cursor's semantic codebase retrieval is central to your flow, or use enterprise AI integrations that haven't shipped ACP support yet.

**Run both if you**: want Zed for fast editing and terminal work while keeping Cursor for deep multi-file AI sessions. Many developers in the 1.0 reviews describe exactly this pattern.

---

## Assessment

Zed 1.0 is the right architectural bet for the parallel-agent era. Native performance, ACP as an open standard, and genuine concurrent agent execution are the correct design decisions. The extension ecosystem gap and Cursor's remaining codebase-retrieval advantage mean it is not a universal replacement today.

**Rating: 4 / 5** — The fastest AI code editor in production, with the cleanest multi-agent architecture. Excellent for performance-sensitive or parallel-workflow use cases. Extension ecosystem gap holds it from 5 for users migrating from VS Code with heavy plugin dependencies.

*ChatForest researches and reviews AI tools; we do not test them hands-on.*

