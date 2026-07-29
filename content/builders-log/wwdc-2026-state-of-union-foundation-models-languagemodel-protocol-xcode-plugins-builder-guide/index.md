---
title: "WWDC 2026 State of the Union: The Foundation Models Announcements That Weren't in the Keynote"
date: 2026-06-10
description: "Apple's June 9 State of the Union added three major Foundation Models announcements that the June 8 keynote skipped: a unified LanguageModel protocol where Claude and Gemini implement the same Swift API as on-device models, free Private Cloud Compute for apps under 2M downloads, and a confirmed open source release this summer."
og_description: "The WWDC 2026 keynote covered Core AI and Foundation Models image input (Siri Extensions was never announced on stage — it only surfaced later as disabled beta code). The June 9 State of the Union added the things builders actually care about: a unified LanguageModel Swift protocol (Claude and Gemini plug in as drop-in replacements for on-device models), free PCC compute under 2M downloads for App Store Small Business Program members, Dynamic Profiles for multi-agent, and Xcode 27 agent plugins from Figma and GitHub."
content_type: "Builder's Log"
sources_audited: 2026-07-30
categories: ["Apple", "Developer Tools", "Platform Strategy"]
tags: ["wwdc-2026", "foundation-models", "languagemodel-protocol", "xcode-27", "apple", "ios-27", "swift", "anthropic", "gemini", "acp", "mcp", "multi-agent", "open-source", "python-sdk", "figma", "github", "june-2026"]
---

Apple's WWDC 2026 keynote ran June 8. The Platforms State of the Union ran June 9. These are different sessions for different audiences: the keynote is for press and consumers; the State of the Union is for developers. Every year, the engineering substance lives in the second session.

This year that was especially true for AI builders. The keynote confirmed Core AI as a new on-device model framework and Foundation Models image input ([session 241, "What's new in the Foundation Models framework"](https://developer.apple.com/videos/play/wwdc2026/241/)) — both covered in the [post-keynote guide](/builders-log/wwdc-2026-post-keynote-confirmed-builder-decisions/). **Correction:** an earlier draft of this piece also listed "Siri Extensions" as keynote-confirmed. It was not. Apple never announced a third-party Siri Extensions system on stage — it surfaced only afterward as disabled code that Bloomberg's Mark Gurman found in the iOS 27 developer beta, with no confirmed shipping date ([The Next Web](https://thenextweb.com/news/apple-siri-extensions-third-party-ai-missing-wwdc); [Daring Fireball, linking Gurman's reporting](https://daringfireball.net/linked/2026/06/08/gurman-siri-ai-extensions)). See our [post-keynote guide](/builders-log/wwdc-2026-post-keynote-confirmed-builder-decisions/) for the full correction. The June 9 State of the Union added five things that didn't make the keynote at all.

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

**Anthropic:** Published [`ClaudeForFoundationModels`](https://github.com/anthropics/ClaudeForFoundationModels), a Swift package conforming Claude to the LanguageModel protocol. The compiled-in model constants at launch are `.sonnet5` (Claude Sonnet 5) and `.opus5` (Claude Opus 5) — not every Claude model, and custom model IDs require you to declare capabilities by hand ([Anthropic's Apple Foundation Models docs](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models)). Auth is API-key (development only — a bundled key is extractable from a shipping binary) or a proxied backend relay for production; Anthropic's docs do not describe an OAuth/Keychain path for this package. The docs also explicitly list **token counting as unsupported** through this integration ("Features with no representation in Apple's protocol are not available through it, including: ... Token counting"), so per-token usage tracking is not something this package exposes (same source).

**Google:** Cloud-hosted Gemini models plug in via the Firebase Apple SDK (specifically the Firebase AI Logic library), authenticated with Firebase App Check ([Firebase blog](https://firebase.blog/posts/2026/06/apple-foundation-models-gemini/); [Google's own announcement](https://blog.google/innovation-and-ai/technology/developers-tools/bringing-gemini-models-to-apple-developers/)). Firebase's own example code names `gemini-3.5-flash` as a supported model; Google's Gemini 3.1 Ultra is the current top-tier model in the same family, though neither Google nor Firebase's post enumerates a single definitive list of every Gemini model available through the integration. Developers choose between the free-tier Gemini Developer API or the enterprise Gemini Enterprise Agent Platform API (formerly Vertex AI) for billing; the model surface looks identical to Apple's on-device model from your app's perspective.

### The practical architecture

With the LanguageModel protocol, a well-structured Foundation Models app can now do something like this:

```swift
// Development / prototyping: Apple on-device model
let session = LanguageModelSession()

// Swap to Claude for complex queries:
// import ClaudeForFoundationModels
// let model = ClaudeLanguageModel(name: .opus5, auth: .apiKey(apiKey))
// let session = LanguageModelSession(model: model)

// Swap to Gemini (exact Firebase Apple SDK call not independently verified for this snippet —
// see the Firebase and Google sources linked above for the current API):
// import FirebaseAI
// let session = LanguageModelSession(model: <Firebase-provided Gemini model, e.g. "gemini-3.5-flash">)
```

The session interface — `respond(to:)`, structured output generation, tool calls, transcript management — is identical across all three. This is significant for two reasons:

**Eval-driven development becomes easier.** You can prototype your feature on Apple's on-device model (no API costs, fully private), then route to Claude or Gemini for eval comparisons, then route production to whichever model performs best — with no architecture changes between prototypes and production.

**Cost-based routing.** Simple queries can stay on-device (zero cost, zero latency, zero privacy exposure). Complex queries can be escalated to a cloud model. The decision point is one line of code.

The practical limitation: the protocol covers structured generation, tool use, and streaming responses. It does not cover model-specific features that have no on-device equivalent. Anthropic's own docs for the package list what's left out: prompt-caching controls (caching itself is applied automatically, but cache TTL and breakpoint placement aren't configurable), stop sequences, batch processing, the Files API, token counting, and beta headers ([Anthropic's Apple Foundation Models docs](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models)). Using any of those requires calling the Claude API directly rather than going through the LanguageModel protocol. The LanguageModel protocol is the shared floor, not the ceiling.

---

## Free Private Cloud Compute: Who Qualifies

Apple announced free access to Foundation Models running on Private Cloud Compute for developers **enrolled in the App Store Small Business Program** with fewer than two million total first-time App Store downloads — both conditions apply, not just the download count ([Apple Newsroom](https://www.apple.com/newsroom/2026/06/apple-aids-app-development-with-new-intelligence-frameworks-and-advanced-tools/)).

This is the number that matters for qualifying, on top of Small Business Program enrollment: **first-time App Store downloads**, not total downloads, not monthly active users. An app downloaded two million times once (and then by the same people again for updates) does not necessarily exceed the threshold. Apple's App Store analytics reports this metric directly. If you're not already enrolled in the Small Business Program — it requires no more than $1M in proceeds in the prior calendar year, and new developers with no revenue history qualify from day one ([Apple Developer — App Store Small Business Program](https://developer.apple.com/app-store/small-business-program/)) — check your eligibility before assuming the free tier applies to you.

What "free" means: inference costs for calling Apple Foundation Models running on PCC — the server-side, private inference infrastructure Apple operates, which processes data statelessly with no persistent storage and encrypts it end-to-end from the device ([Apple Security Research — Private Cloud Compute](https://security.apple.com/blog/private-cloud-compute/)). Session 241 describes the PCC-hosted model as a larger, reasoning-capable model separate from the on-device one ([session 241, "What's new in the Foundation Models framework"](https://developer.apple.com/videos/play/wwdc2026/241/)). This is not the same as on-device inference, which is always free. On-device runs on the user's device with no Apple cloud involvement.

PCC matters for two cases: (a) queries that exceed what on-device can handle well, where you want Apple's larger server-side model rather than a third-party API, and (b) users on older devices without sufficient on-device hardware, where PCC provides a fallback with the same privacy properties.

The combination of the Small Business Program's $1M proceeds cap and the 2M download threshold will exclude most enterprise apps and most top-100 consumer apps. For independent developers and early-stage teams that qualify for both, this is meaningful — it removes one of the cost arguments against building on Foundation Models rather than paying per-token API calls to third parties.

---

## Dynamic Profiles: Multi-Agent Without an Orchestration Framework

The Foundation Models framework has a new primitive: Dynamic Profiles. These let your app swap the underlying model, tool set, and system instructions on the fly, within a continuous session. The session context (the transcript) persists through the swap.

The practical use case: a single conversation that routes different query types to different model configurations. A coding assistant might use one profile for code generation (a higher-reasoning-level configuration) and a different profile for documentation queries (faster, cheaper model) — Apple's own sample code sets this per-profile with a `.reasoningLevel(.deep)` modifier ([session 242](https://developer.apple.com/videos/play/wwdc2026/242/)). The user does not see a session break.

Before Dynamic Profiles, building this in Foundation Models required managing multiple sessions and stitching transcripts manually. The new primitive handles the context continuity.

Apple's WWDC session on agentic workflows ([session 242, "Build agentic app experiences with the Foundation Models framework"](https://developer.apple.com/videos/play/wwdc2026/242/)) covers the engineering details: shared context management (via `historyTransform` and session properties), privacy boundaries between profiles (redacting transcript entries when switching to less-private models), and key-value cache coordination across profile switches (appending to the transcript preserves the cache; rewriting history invalidates it).

This is not a full multi-agent orchestration framework. There is no built-in agent graph, no persistent memory layer, no automatic handoff between agents. Dynamic Profiles is a lower-level primitive. The comparison to existing frameworks like LangGraph or Anthropic's agent SDK is not apt — this is closer to what Apple thinks multi-agent should look like inside a single iOS app, not a server-side orchestration system.

---

## Open Source This Summer

Apple confirmed the Foundation Models framework will go open source later this summer ([MacRumors](https://www.macrumors.com/2026/06/09/apple-outlines-major-ai-and-developer-tool-updates/); [session 241](https://developer.apple.com/videos/play/wwdc2026/241/)).

What's already open: the **utilities package** — transcript management, the skill API, chat-completions interface, and reusable profile modifiers for agentic patterns ([session 242](https://developer.apple.com/videos/play/wwdc2026/242/)). Developers can inspect, fork, or contribute to this package now.

What's coming: the **core framework itself**, including the inference infrastructure. Apple also confirmed that the core framework runs on Linux servers via Swift's open-source runtime ([session 241](https://developer.apple.com/videos/play/wwdc2026/241/)).

The Linux support is notable. It means the Foundation Models API — including the LanguageModel protocol — can run on non-Apple server hardware. An app that uses the Foundation Models framework for on-device iOS inference could theoretically share model-calling logic with a server-side Swift component running on Linux, using the same API surface for both cloud and on-device inference.

This is still a confirmed-future announcement, not a shipped feature. "Later this summer" means no earlier than August; Apple's open-source release cadence typically follows developer betas. Watch the Swift open-source repositories for the actual drop.

---

## Xcode 27: Agent Plugins via ACP

The June 8 keynote covered Xcode 27's AI features, including Swift Assist and Foundation Models Playground. The June 9 State of the Union added Xcode 27's agent plugin system.

**Correction:** an earlier draft of this piece (matching an error repeated elsewhere in our WWDC 2026 coverage) called this release "Xcode 17" and invented a story about Apple renaming Xcode to match the OS version number. There is no such renaming, and no "Xcode 17" — Apple's own developer site, session pages, and newsroom post all name this release **Xcode 27**, aligned with iOS 27 / macOS 27 ([Apple Newsroom](https://www.apple.com/newsroom/2026/06/apple-aids-app-development-with-new-intelligence-frameworks-and-advanced-tools/); [WWDC26 session videos](https://developer.apple.com/videos/play/wwdc2026/102/)). Xcode's version numbers have tracked the OS major version since Xcode 26, the prior release — this is not new with Xcode 27.

The plugin system is built on the Agent Client Protocol (ACP). Any agent that implements ACP can be plugged into Xcode's agent conversation panel. The conversation behaves like a file — it can be opened, split, stacked in the Navigator alongside your code files. Agents can run tests, drive the simulator, switch between light/dark preview configurations, and control a running app end-to-end.

**Day-one plugins:**

**Figma** — Figma's Xcode integration runs as an MCP server that gives an agent "design context such as components, variables, layout data, FigJam content, and Make resources," can "generate code from selected frames," and uses Code Connect to keep generated code aligned with real components ([Figma Help Center](https://help.figma.com/hc/en-us/articles/41061095668759-Xcode-and-Figma-Set-up-the-MCP-server)). Apple's newsroom post names Figma and GitHub as "the first to offer seamless installation between their tools and Xcode" ([Apple Newsroom](https://www.apple.com/newsroom/2026/06/apple-aids-app-development-with-new-intelligence-frameworks-and-advanced-tools/)).

**GitHub** — GitHub and Figma are Apple's named first-party ACP/MCP launch partners for Xcode 27 (same Apple Newsroom source). GitHub's own Copilot coding agent — separately documented — can already turn an assigned issue into a pull request by working autonomously in the background, running tests and opening the PR for review; how much of that surfaces specifically through the new Xcode ACP integration versus GitHub's existing Xcode extension isn't detailed in Apple's or GitHub's launch materials, so treat the exact division of capabilities as unconfirmed until GitHub publishes integration-specific documentation.

**Claude, ChatGPT, Gemini** — Xcode 27 brings "agents from Anthropic, Google, and OpenAI directly into a developer's workflow," per Apple's own newsroom language, with any ACP-compatible agent able to join a session ([Apple Newsroom](https://www.apple.com/newsroom/2026/06/apple-aids-app-development-with-new-intelligence-frameworks-and-advanced-tools/)). We have not found a primary source ranking the completeness of one provider's integration over another in early betas, so that comparison has been cut rather than asserted without a source.

**MCP tools** — Apple's own framing distinguishes the two protocols: ACP governs which agents can connect to Xcode, while MCP governs the tool calls an agent makes once connected (file reads, builds, test runs, diagnostics). Plugins can expose MCP servers to the Xcode agent panel — the Figma integration above is itself one example. If your project has an MCP server for database inspection, API exploration, or documentation lookup, that server's tools are available to any ACP-compatible agent in Xcode.

The ACP plugin SDK is part of the public Xcode 27 developer beta ([Apple Newsroom](https://www.apple.com/newsroom/2026/06/apple-aids-app-development-with-new-intelligence-frameworks-and-advanced-tools/)).

---

## What to Do with This

If you are building iOS or macOS apps that use AI:

**Read the LanguageModel protocol documentation today.** If you have an existing Foundation Models app that calls Apple's on-device model, evaluate whether the Anthropic or Google Swift packages give you a drop-in path to cloud-model escalation. The session management work is already done. The incremental cost to add cloud model routing is now very low.

**Check your Small Business Program status and first-time download count.** If you're enrolled in the App Store Small Business Program and your app is under 2M first-time downloads, the free PCC access is available now in iOS 27 beta. This doesn't affect your development timeline but does affect your cost model in production.

**Pull the iOS 27 developer beta and look at Dynamic Profiles.** If your app has any multi-turn AI conversation flow, the WWDC session 242 is worth watching. The Dynamic Profiles primitive may simplify code you currently maintain manually.

**Evaluate Xcode 27 agent plugins for your development workflow.** If your team uses Figma and GitHub, both plugins are shipping at launch. For teams that have invested in MCP servers for internal tooling, the MCP-to-Xcode bridge may be immediately useful.

The open source announcement is a longer-horizon item. The core framework going open source this summer will matter more for teams building server-side Swift infrastructure or who want to inspect the inference implementation. Watch the Swift open-source repos for the actual release.

---

*Coverage based on the WWDC 2026 Platforms State of the Union (June 9, 2026). Apple Developer session videos for Foundation Models: [What's new in Foundation Models](https://developer.apple.com/videos/play/wwdc2026/241/) (session 241) and [Build agentic app experiences](https://developer.apple.com/videos/play/wwdc2026/242/) (session 242).*
