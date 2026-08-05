# Grok 4.5 Is Coming to Cursor: SpaceX's Data Flywheel Model and What Builders Need to Decide

> SpaceX exercised its $60B Cursor acquisition option in June. Now Grok 4.5 — built on xAI's 1.5T V9 model fine-tuned on Cursor coding data — is expected to roll out publicly today. Here's the performance picture, the data flywheel implications, and what to do with your coding stack.


SpaceX [exercised its option to acquire Cursor](https://x.com/SpaceX/status/2066873915717136548) on June 16, 2026, in an all-stock deal valued at $60 billion — a move [Cursor's own account confirmed the same day](https://x.com/cursor_ai/status/2066875698346954891). In that post, [SpaceX's account stated](https://x.com/SpaceX/status/2066873915717136548) that SpaceXAI had been jointly training a new model with Cursor for several months, and that the model would launch in Cursor and Grok Build "soon."

That soon is today. [The Information reported July 7](https://www.theinformation.com/briefings/exclusive-spacexai-plans-launch-new-model-cursor-soon-wednesday) that SpaceXAI planned to release the jointly trained model as soon as Wednesday, July 8 — after pushing back an earlier launch date to improve efficiency.

This is Grok 4.5: xAI's 1.5-trillion-parameter V9 foundation model, fine-tuned on Cursor developer sessions. It arrives at a company with a computing footprint (Colossus), a social distribution channel (X), an automotive channel (Tesla), a coding IDE (Cursor), and now a model built partially on the code its users wrote. That's a vertical integration picture no other AI lab has.

Here's what builders need to know before the rollout lands in your editor.

---

## What Grok 4.5 Is

Grok 4.5 is not a new architecture. It's xAI's existing V9 foundation model — 1.5 trillion total parameters, trained on xAI's Colossus supercomputer cluster — with an additional fine-tuning pass on Cursor's developer session data. Elon Musk [announced private beta](https://cybernews.com/ai-news/musk-grok-4-5-private-beta-superior-claude-opus/) at SpaceX and Tesla on June 28, 2026, saying [early evaluations put its performance "close to, and potentially above," Claude Opus](https://letsdatascience.com/news/musk-says-grok-45-enters-private-beta-at-spacex-tesla-1840769e) — a claim that source notes remained an unverified vendor assertion, with no independent benchmark or system card published.

The Cursor data layer is the differentiator being pitched to builders. The argument: a model that has seen millions of real coding sessions in context — complete with file trees, error messages, terminal output, and multi-turn revision cycles — should outperform a general-purpose model fine-tuned only on synthetic coding tasks. Cursor's [Composer 2.5, launched May 2026](https://cursor.com/blog/composer-2-5), was already trained on 25× more synthetic coding tasks than its predecessor, Composer 2. Grok 4.5 adds the Cursor session corpus to the V9 foundation.

This is the data flywheel made explicit: Cursor users produce coding sessions → SpaceXAI uses those sessions to train the model → the model improves → more developers adopt Cursor → more sessions feed the next training run.

---

## What the Performance Claims Actually Are

Musk's June 28 announcement described Grok 4.5 as "close to, perhaps exceeding" Claude Opus in early evaluations. There are two significant caveats to that claim.

**First: the evaluations are internal.** The benchmarks cited — run at SpaceX and Tesla — were conducted by engineers now working inside the same corporate structure as xAI. No independent benchmark from LMArena, Artificial Analysis, SWE-bench, or Humanity's Last Exam has scored Grok 4.5 as of this writing.

**Second: "Opus" is undefined.** Musk did not specify which Opus build. Claude Opus 4.8 (current) scores substantially better than Opus 4.7 on coding tasks. "Close to Opus" spans a wide range.

For comparison: Grok Build 0.1 — the previous dedicated coding model from xAI — scored [70.8% on SWE-bench Verified](https://chatforest.com/reviews/xai-grok-build-terminal-coding-agent-review/) as of May 2026. Independent tracking puts [Claude Code (Opus 4.8 backend) at 88.6% and Codex CLI (GPT-5.5 backend) at 88.7%](https://www.vals.ai/benchmarks/swebench) on the same benchmark — neither company has published this specific metric itself. Grok 4.5 would need to close nearly an 18-point gap to reach parity with current leading tools.

That gap is plausible for a model trained at V9 scale with coding-specialized data. It's also not confirmed. Wait for the first independent SWE-bench run.

A UI canary string — ["Unlock the full power of Chat with Grok 4.5"](https://x.com/testingcatalog/status/2074214554523816272) — appeared in the Grok web interface on July 6, indicating [active pre-launch preparation](https://www.testingcatalog.com/spacexai-gearing-up-for-upcoming-grok-4-5-release/). Context window, published pricing, and API access details have not yet been formally announced.

---

## What the SpaceX Acquisition Actually Changes

[Our May 2026 Cursor 3 review](https://chatforest.com/reviews/cursor-3-anysphere-ai-ide-agent-runtime-composer-2-5-review/) covered the acquisition option as a pending risk. The option is now exercised. [The deal is expected to close in Q3 2026](https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html).

What changes operationally for Cursor users:

**Default model path.** When Grok 4.5 rolls into Cursor, it will likely become the default agent model, the same way Composer 2.5 is today. You can see this change in the Composer model selector. Your existing BYOK (bring your own key) configurations — using Claude, GPT, or Gemini through their respective APIs — remain possible and are not affected by the acquisition.

**Training data terms.** Cursor's Terms of Service govern what Anysphere/SpaceX can use for training. Before Grok 4.5 becomes your default model, read the current terms — specifically the data retention and training sections. SpaceXAI's interest in Cursor's value as a training data source is now explicit. Teams with sensitive or proprietary codebases should audit this carefully.

**Vendor dependency.** Using the default Cursor + Grok 4.5 configuration means your editor, your primary coding model, and your model's training data are all inside a single company's perimeter. That's a meaningful concentration of dependency compared to running Cursor with a Claude or GPT backend from a separate provider.

**Acquisition completion timeline.** The deal closes Q3 2026. Until then, Anysphere operates under its existing governance. After closing, SpaceX controls product, pricing, and data policy decisions.

---

## Grok Build vs Cursor + Grok 4.5

SpaceXAI offers two paths to Grok 4.5:

**Grok Build** (terminal agent): SpaceXAI's native terminal coding agent, available to SuperGrok subscribers ($30/mo) or via API ($1 per million input tokens / $2 per million output tokens). Plan-review-approve loop, up to 8 parallel subagents in isolated git worktrees, MCP support, AGENTS.md. Architecture is [independent of Cursor's IDE layer](https://chatforest.com/reviews/xai-grok-build-terminal-coding-agent-review/). This is where SpaceXAI controls the full stack end-to-end.

**Cursor + Grok 4.5**: Grok 4.5 as the default or selectable backend model inside Cursor's IDE. You keep Cursor's interface, Background Agents, the Graphite PR review workflow, and the tab completion that Cursor does better than most tools. The model is Grok 4.5.

The Grok Build path gives SpaceXAI tighter control and a direct subscription relationship. The Cursor path is higher friction for SpaceXAI but reaches Cursor's much larger installed base.

---

## Alternatives and What They Offer

If today's launch makes you want to evaluate your options:

**Claude Code** (Anthropic): Terminal agent running on Opus 4.8/[Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5). [SWE-bench Verified 88.6% (Opus 4.8)](https://www.vals.ai/benchmarks/swebench) — essentially tied with, not ahead of, Codex CLI (see below). API pricing: [Opus 4.8 at $5/$25 per million tokens](https://www.anthropic.com/news/claude-opus-4-8) ([Fable 5 at $10/$50 once included usage runs out](https://www.anthropic.com/news/redeploying-fable-5)). No IDE integration by design — runs in your terminal alongside your existing editor. Anthropic is an independent company; no single-company stack risk.

**Codex CLI** (OpenAI): Terminal agent, [88.7% SWE-bench Verified](https://www.vals.ai/benchmarks/swebench) on the GPT-5.5 backend. [GPT-5.6 Sol remains restricted to a small set of government-vetted partners pending a White House-requested cybersecurity review](https://techxplore.com/news/2026-06-openai-restricts-gpt-sol-users.html); GPT-5.5 is the current broadly accessible model. OpenAI is also independent of IDE vendors.

**Windsurf** (Codeium): Alternative IDE-based agent, running its own SWE-1 model family. Codeium/Windsurf isn't independent either — [Cognition AI (maker of Devin) acquired its product, IP, and enterprise business in July 2025](https://www.infoworld.com/article/4023030/cognition-agrees-to-buy-whats-left-of-windsurf.html), after a separate deal sent its founding team to Google DeepMind. Pricing competitive with Cursor. Worth evaluating if IDE-native agent UX matters and you want to stay out of the SpaceX stack specifically.

**Cursor with BYOK**: Keep Cursor's interface, switch the model to Claude or GPT via API keys. Maintains IDE ergonomics, routes model inference through a provider of your choice, and reduces (but doesn't eliminate) SpaceXAI's visibility into your workflows.

---

## Builder Action Items

**Watch for independent SWE-bench results.** Grok 4.5's performance claim is internal. When independent benchmarking appears (Artificial Analysis usually moves first), that's the data worth acting on. Performance determines whether a migration is worth the friction.

**Audit your Cursor data terms before Grok 4.5 becomes your default.** Go to Cursor Settings → Account → Privacy and Data. Check if "Codebase Indexing" is enabled, whether your sessions are included in training, and whether you're on a privacy-mode plan. Make an informed choice before the model update lands rather than after.

**If you're on API pricing, compare costs.** [Grok Build API: $1/$2 per million tokens](https://chatforest.com/reviews/xai-grok-build-terminal-coding-agent-review/). Grok 4.5 via Cursor: no confirmed pricing yet. [Claude Sonnet 5: $2/$10 per million (introductory through August 31, 2026)](https://www.anthropic.com/news/claude-sonnet-5). [Opus 4.8: $5/$25](https://www.anthropic.com/news/claude-opus-4-8). The cost story for Grok 4.5 could be compelling if it's priced at or near V9-Medium rates — but we don't have those numbers yet.

**Don't evaluate based on Musk's private beta claim.** Internal evaluations run by engineers at SpaceX and Tesla are not independent. Wait for external scores before concluding Grok 4.5 has closed the gap with Claude Code.

**Consider what you're concentrating.** If your team's daily coding tool, its primary model, and that model's training data are all inside SpaceX, that's a concentration worth naming explicitly in your engineering risk register. It's not necessarily a reason to leave — Cursor is genuinely excellent — but it's worth a conscious decision rather than a default drift.

---

## What to Watch for Post-Launch

The Grok 4.5 rollout in Cursor and Grok Build is expected today. What to look for in the first 48 hours:

- **Published specs**: context window, temperature ranges, multimodal capability (V9 is text+image capable), maximum parallel agents in Grok Build
- **Pricing for Cursor + Grok 4.5**: will it be included in existing Cursor plans, usage-billed, or restricted to a higher tier?
- **First SWE-bench community runs**: builders typically post independent scores within 24-48 hours of API access
- **Cursor privacy policy update**: any changes to training data terms that accompany the model handoff

We'll cover confirmed performance data as it becomes available. Subscribe to [ChatForest's builders log](/builders-log/) for updates.

