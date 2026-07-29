# No, Apple Didn't Put MCP on Siri: What WWDC 2026 Actually Shipped in Xcode 27

> WWDC 2026 did not ship system-wide MCP support for Siri or Core AI, despite that claim circulating after the keynote. What Apple actually confirmed: Xcode 27 deepens the MCP support it introduced in Xcode 26.3, with MCP-based plugins for tools like Figma and GitHub. Here's what Apple's own WWDC26 sessions say — and don't say.


**Correction (2026-07-29):** This piece originally claimed WWDC 2026 shipped "system-wide MCP" support that let Siri invoke MCP servers registered by any app, with Core AI routing to MCP as a tool target, plus app-bound, MDM, and user-registration paths. A claim-by-claim source check found none of that in Apple's own WWDC26 materials — not the keynote, not the [Apple Intelligence developer guide](https://developer.apple.com/wwdc26/guides/apple-intelligence/), not the [Platforms State of the Union](https://developer.apple.com/videos/play/wwdc2026/102/) session, not the [Meet Core AI](https://developer.apple.com/videos/play/wwdc2026/324/) session. What Apple actually confirmed is narrower and is described below. The fabricated sections have been removed rather than re-sourced, per this site's citation policy.

---

At WWDC 2026, Apple confirmed it is deepening [Model Context Protocol (MCP) support inside Xcode 27](https://developer.apple.com/videos/play/wwdc2026/102/) — the same IDE-level MCP work it started with Xcode 26.3 in February 2026. Apple did **not** announce Siri invoking MCP servers, Core AI routing to MCP servers, or any user- or MDM-facing MCP registration surface. [Apple's own keynote recap](https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more/) and [Apple Intelligence developer guide](https://developer.apple.com/wwdc26/guides/apple-intelligence/) for WWDC26 make no mention of MCP at all — the MCP news is confined to the developer-tools track.

If you operate a public MCP server today, WWDC 2026 did not add a new client class of "any iPhone or Mac." It added incremental capability to one existing client: Xcode.

---

## What Was Actually Announced at WWDC 2026

Confirmed, from Apple's own [Platforms State of the Union](https://developer.apple.com/videos/play/wwdc2026/102/) session:

**Xcode 27 plugins can bundle MCP-based tools.** In Apple's words: "A plugin can contain skills, just markdown files that teach the agent new tasks. It can contain tools using the Model Context Protocol." Plugins can also bring "an agent of your choice" via a separate, Apple-specific Agent Client Protocol.

**Xcode 27 ships first-party MCP connectors for design and source-control tools.** Per Apple: "With MCP, Xcode also connects to the tools you already use, from design apps like Figma to services like GitHub." Figma and GitHub are cited as the first two plugin integrations.

**No system-wide MCP client, no Siri invocation, no Core AI routing.** These claims appear in third-party speculation (see below) but not in any WWDC26 session transcript reviewed for this correction, nor in Apple's press materials.

---

## Context: Where MCP Was Before Today

To understand why this matters, the timeline:

**November 2024:** Anthropic [publishes the MCP specification](https://www.anthropic.com/news/model-context-protocol). MCP defines a standardized client-server protocol for AI systems to call external tools, read resources, and use prompt templates.

**Early 2025:** Major platforms adopt the protocol. Claude, ChatGPT, Gemini, and most agentic frameworks begin shipping MCP clients. The server ecosystem grows rapidly — today, MCP servers exist for GitHub, Stripe, Figma, PostgreSQL, Slack, Kubernetes, and hundreds of other tools.

**February 2026 (Xcode 26.3):** Apple [ships MCP support in Xcode](https://9to5mac.com/2026/02/26/apple-releases-xcode-26-3-with-support-for-agentic-coding/). The IDE exposes 20 built-in tools via an MCP server — file system operations, build and test controls, diagnostics, and Apple documentation search. Claude Code and OpenAI Codex both connect via this MCP surface. This is the first MCP support in any Apple product.

**June 2026 (WWDC 2026):** Apple [expands MCP support inside Xcode 27](https://developer.apple.com/videos/play/wwdc2026/102/) — plugin-bundled MCP tools, plus first-party MCP connectors for Figma and GitHub. This is a deepening of the IDE surface, not a move to the operating system: Apple's WWDC26 materials do not describe MCP as a system-level API available to arbitrary apps, Siri, or Core AI.

---

## What Core AI Is — and Why It's Not an MCP Story

Core AI, previewed at WWDC 2026, is a new on-device inference framework. In Apple's own description from the [Meet Core AI](https://developer.apple.com/videos/play/wwdc2026/324/) session, it "marks the next evolution of on-device AI execution across Apple platforms" and is "the inference framework powering on-device Apple Intelligence" — covering model optimization, conversion, debugging, and deployment on Apple silicon.

That session makes no mention of MCP, external tool servers, or routing requests to third-party endpoints. Core AI is about running models locally; it is a separate, unrelated announcement from Xcode's MCP work, and this piece originally conflated the two.

---

## What This Means for Builders, Realistically

**If you build with Claude Code, Codex, or another MCP-compatible coding agent inside Xcode:** the practical change from WWDC 2026 is that Xcode 27 plugins can now package MCP tools directly, and Apple ships first-party MCP connectors for Figma and GitHub. If your team already has an MCP server for internal tooling, packaging it as an Xcode 27 plugin is the concrete, sourced opportunity here — not a Siri integration.

**If you operate a public MCP server:** nothing about iOS or macOS as a runtime target changed at WWDC 2026. Your server's client base is still IDEs and desktop AI apps that ship MCP clients (Claude, ChatGPT, Gemini, Xcode), per the adoption history above — not iPhones running Siri.

**If you saw the "MCP goes system-wide on iOS" claim elsewhere:** it traces to unconfirmed reports and speculative analysis pieces (for example, a September 2025 [9to5mac report on early macOS Tahoe 26.1 beta code](https://9to5mac.com/2025/09/22/macos-tahoe-26-1-beta-1-mcp-integration/) hinting at possible future OS-level MCP work, well before WWDC 2026 and for an earlier OS cycle). That is a rumor about a different release, not a WWDC 2026 announcement. If and when Apple confirms a system-wide MCP surface for Siri or Core AI, this page will be updated with the primary source.

---

## Related Coverage

- [WWDC 2026 Keynote Confirmed: Siri Is Now Gemini, Core AI Replaces Core ML, MCP Goes Platform-Wide](/builders-log/wwdc-2026-keynote-confirmed-apple-ai-platform-builder-guide/) — post-keynote builder guide; note its "MCP Goes Platform-Wide" framing has not been independently re-verified as part of this correction and should be treated with the same caution applied here until it is audited
- [MCP Specification 2026-07-28 Release Candidate](/builders-log/mcp-spec-2026-07-28-release-candidate-stateless-breaking-changes-builder-guide/) — the upcoming protocol revision with stateless architecture and TTL caching
- [iOS 27 Siri Extensions API Builder Guide](/builders-log/ios-27-siri-extensions-api-builder-guide-wwdc-2026/) — the Extensions framework (different from MCP: this is for AI providers, not tool servers)

---

*Originally written June 8, 2026, claiming Apple had shipped system-wide MCP at WWDC 2026. Corrected 2026-07-29 after a claim-level source audit found that claim unsupported by Apple's WWDC26 materials; see the correction note at the top of this page.*

