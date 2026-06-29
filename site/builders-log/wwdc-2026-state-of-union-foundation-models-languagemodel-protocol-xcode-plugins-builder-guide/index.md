# WWDC 2026 State of the Union: The Foundation Models Announcements That Weren't in the Keynote

> Apple's June 9 State of the Union added three major Foundation Models announcements that the June 8 keynote skipped: a unified LanguageModel protocol where Claude and Gemini implement the same Swift API as on-device models, free Private Cloud Compute for apps under 2M downloads, and a confirmed open source release this summer.


Apple's WWDC 2026 keynote ran June 8. The Platforms State of the Union ran June 9. These are different sessions for different audiences: the keynote is for press and consumers; the State of the Union is for developers. Every year, the engineering substance lives in the second session.

This year that was especially true for AI builders. The keynote confirmed Siri Extensions, Core AI, and Foundation Models image input — all of which we covered in the [post-keynote guide](/builders-log/wwdc-2026-post-keynote-confirmed-builder-decisions/). The June 9 State of the Union added five things that didn't make the keynote at all.

---

## The Five Announcements

**1. The LanguageModel protocol.** A public Swift interface that third-party AI providers implement to expose cloud models through the same API as Apple's on-device Foundation Models. Anthropic and Google shipped implementations the same day.

**2. Free Private Cloud Compute for small developers.** Apps with fewer than two million first-time App Store downloads get Apple Foundation Models on PCC at no cost. No inference fees.

**3. Dynamic Profiles.** A new primitive for swapping models, tools, and instructions mid-session. This is the Foundation Models answer to multi-agent orchestration.

**4. Open source this summer.** The core Foundation Models framework is confirmed open source, targeting this summer. The utilities package is already open.

**5. Xcode 27 agent plugins via ACP.** Figma and GitHub shipped Xcode Agent Client Protocol plugins at launch. Any agent compatible with ACP can now be plugged into Xcode.

---

## The LanguageModel Protocol: What It Actually Means

This is the announcement with the most surface area for builders.

The Foundation Models framework has always had an on-device model — Apple's language model running on-device via the Neural Engine, CPU, and GPU. Before this week, that model was the only thing the framework could talk to. If you needed Claude or Gemini for more complex queries, you called their APIs separately, with different session management, different error handling, different auth flows.

The LanguageModel protocol changes that. It is a public Swift interface. Any provider that implements it exposes their cloud model with the same API surface as Apple's on-device model. Your app code doesn't change — you update a Swift Package Manager dependency, and the rest of your session logic, tools, and structured output handling continue to work unchanged.

### What's shipping today

**Anthropic:** Published a Swift package implementing the LanguageModel protocol for Claude. Specifically Fable 5 and Opus 4.8 — the two generally available production models. Auth uses OAuth and Keychain. Per-token usage tracking is included, with separate counts for cache tokens and reasoning tokens.

**Google:** Cloud-hosted Gemini models (3.1 Ultra and 3.5 Flash) plug in via the Firebase Apple SDK. Firebase handles auth and billing; the model surface looks identical to Apple's on-device model from your app's perspective.

### The practical architecture

With the LanguageModel protocol, a well-structured Foundation Models app can now do something like this:

```swift
// Development / prototyping: Apple on-device model
let session = LanguageModelSession()

// Swap to Claude for complex queries:
// import AnthropicFoundationModels
// let session = LanguageModelSession(model: ClaudeModel.fable5)

// Swap to Gemini:
// import FirebaseAI
// let session = LanguageModelSession(model: GeminiModel.flash35)
```

The session interface — `respond(to:)`, structured output generation, tool calls, transcript management — is identical across all three. This is significant for two reasons:

**Eval-driven development becomes easier.** You can prototype your feature on Apple's on-device model (no API costs, fully private), then route to Claude or Gemini for eval comparisons, then route production to whichever model performs best — with no architecture changes between prototypes and production.

**Cost-based routing.** Simple queries can stay on-device (zero cost, zero latency, zero privacy exposure). Complex queries can be escalated to a cloud model. The decision point is one line of code.

The practical limitation: the protocol covers structured generation, tool use, and streaming responses. It does not cover model-specific features that have no on-device equivalent — Fable 5's 1M context window, for example, or extended thinking mode in Opus 4.8. Using those features requires calling the Anthropic API directly. The LanguageModel protocol is the shared floor, not the ceiling.

---

## Free Private Cloud Compute: Who Qualifies

Apple announced free access to Foundation Models running on Private Cloud Compute for developers with fewer than two million first-time App Store downloads.

This is the number that matters for qualifying: **first-time App Store downloads**, not total downloads, not monthly active users. An app downloaded two million times once (and then by the same people again for updates) does not necessarily exceed the threshold. Apple's App Store analytics reports this metric directly.

What "free" means: inference costs for calling Apple Foundation Models running on PCC — the server-side, private inference infrastructure Apple operates, which has the same privacy properties as on-device inference (no data stored after processing, hardware-isolated, end-to-end encrypted). This is not the same as on-device inference, which is always free. On-device runs on the user's device with no Apple cloud involvement.

PCC matters for two cases: (a) queries that exceed what on-device can handle well, where you want Apple's larger server-side model rather than a third-party API, and (b) users on older devices without sufficient on-device hardware, where PCC provides a fallback with the same privacy properties.

The 2M download threshold will exclude most enterprise apps and most top-100 consumer apps. For independent developers and early-stage teams, this is meaningful — it removes one of the cost arguments against building on Foundation Models rather than paying per-token API calls to third parties.

---

## Dynamic Profiles: Multi-Agent Without an Orchestration Framework

The Foundation Models framework has a new primitive: Dynamic Profiles. These let your app swap the underlying model, tool set, and system instructions on the fly, within a continuous session. The session context (the transcript) persists through the swap.

The practical use case: a single conversation that routes different query types to different model configurations. A coding assistant might use one profile for code generation (high-capability, extended thinking enabled) and a different profile for documentation queries (faster, cheaper model). The user does not see a session break.

Before Dynamic Profiles, building this in Foundation Models required managing multiple sessions and stitching transcripts manually. The new primitive handles the context continuity.

Apple's WWDC session on agentic workflows (session 242, "Build agentic app experiences with the Foundation Models framework") covers the engineering details: shared context management, privacy boundaries between profiles, and key-value cache coordination across profile switches.

This is not a full multi-agent orchestration framework. There is no built-in agent graph, no persistent memory layer, no automatic handoff between agents. Dynamic Profiles is a lower-level primitive. The comparison to existing frameworks like LangGraph or Anthropic's agent SDK is not apt — this is closer to what Apple thinks multi-agent should look like inside a single iOS app, not a server-side orchestration system.

---

## Open Source This Summer

Apple confirmed the Foundation Models framework will go open source later this summer.

What's already open: the **utilities package** — transcript management, the skill API, chat-completions interface. Developers can inspect, fork, or contribute to this package now.

What's coming: the **core framework itself**, including the inference infrastructure. Apple also confirmed that the core framework runs on Linux servers via Swift's open-source runtime.

The Linux support is notable. It means the Foundation Models API — including the LanguageModel protocol — can run on non-Apple server hardware. An app that uses the Foundation Models framework for on-device iOS inference could theoretically share model-calling logic with a server-side Swift component running on Linux, using the same API surface for both cloud and on-device inference.

This is still a confirmed-future announcement, not a shipped feature. "Later this summer" means no earlier than August; Apple's open-source release cadence typically follows developer betas. Watch the Swift open-source repositories for the actual drop.

---

## Xcode 27: Agent Plugins via ACP

The June 8 keynote covered Xcode 17's three AI features: Swift Assist, on-device predictive completion, and Foundation Models Playground. The June 9 State of the Union added Xcode 27's agent plugin system.

Wait — Xcode 17? Xcode 27? Both are correct, confusingly. Apple renamed Xcode to match the OS version number starting with this release. Xcode 17 (the traditional numbering) is now also called Xcode 27 in Apple's developer documentation (matching iOS 27 / macOS 27). The two names refer to the same release.

The plugin system is built on the Agent Client Protocol (ACP). Any agent that implements ACP can be plugged into Xcode's agent conversation panel. The conversation behaves like a file — it can be opened, split, stacked in the Navigator alongside your code files. Agents can run tests, drive the simulator, switch between light/dark preview configurations, and control a running app end-to-end.

**Day-one plugins:**

**Figma** — The Figma Xcode plugin connects your design tokens, components, and screen layouts directly to Xcode's agent panel. An agent can reference a specific Figma frame, read its properties, and generate SwiftUI code that matches the design. This closes the design-to-code loop that previously required manual inspection or third-party integrations.

**GitHub** — The GitHub Xcode plugin brings repository context, pull request workflows, and GitHub Copilot into the Xcode agent panel. This overlaps with GitHub's existing Xcode extension, but the ACP integration gives agents deeper access to Xcode internals — running tests, reading build errors, navigating the project structure — rather than just generating code inline.

**Claude, ChatGPT, Gemini** — Anthropic, OpenAI, and Google are confirmed as bringing their agents into Xcode, though the exact shipping timelines for each differ. Apple's demos at WWDC used all three. Anthropic's Claude integration is the most complete in early betas, consistent with Claude Code's existing strong support for agentic coding workflows.

**MCP tools** — Plugins can also expose MCP servers to the Xcode agent panel. If your project has an MCP server for database inspection, API exploration, or documentation lookup, that server's tools are available to any ACP-compatible agent in Xcode.

The ACP plugin SDK is part of the public Xcode 27 developer beta, available today for anyone in the Apple Developer Program.

---

## What to Do with This

If you are building iOS or macOS apps that use AI:

**Read the LanguageModel protocol documentation today.** If you have an existing Foundation Models app that calls Apple's on-device model, evaluate whether the Anthropic or Google Swift packages give you a drop-in path to cloud-model escalation. The session management work is already done. The incremental cost to add cloud model routing is now very low.

**Check your first-time download count.** If your app is under 2M first-time downloads, the free PCC access is available now in iOS 27 beta. This doesn't affect your development timeline but does affect your cost model in production.

**Pull the iOS 27 developer beta and look at Dynamic Profiles.** If your app has any multi-turn AI conversation flow, the WWDC session 242 is worth watching. The Dynamic Profiles primitive may simplify code you currently maintain manually.

**Evaluate Xcode 27 agent plugins for your development workflow.** If your team uses Figma and GitHub, both plugins are shipping at launch. For teams that have invested in MCP servers for internal tooling, the MCP-to-Xcode bridge may be immediately useful.

The open source announcement is a longer-horizon item. The core framework going open source this summer will matter more for teams building server-side Swift infrastructure or who want to inspect the inference implementation. Watch the Swift open-source repos for the actual release.

---

*Coverage based on the WWDC 2026 Platforms State of the Union (June 9, 2026). Apple Developer session videos for Foundation Models: [What's new in Foundation Models](https://developer.apple.com/videos/play/wwdc2026/241/) (session 241) and [Build agentic app experiences](https://developer.apple.com/videos/play/wwdc2026/242/) (session 242).*

