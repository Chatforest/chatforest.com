# Bluesky Attie: The Claude-Powered AI App That Lets You Vibe-Code Your Social Feed

> On March 28, 2026, Bluesky unveiled Attie at the ATmosphere conference — a standalone AI assistant powered by Anthropic's Claude that lets users build custom social feeds using plain language. Former CEO Jay Graber stepped down to build it. This guide covers the architecture, AT Protocol integration, vibe-coding vision, competitive positioning, and honest limitations.


On March 28, 2026, Bluesky unveiled Attie at the ATmosphere conference — a standalone AI app that lets users build custom social feeds by describing what they want in plain English. It's powered by Anthropic's Claude and built on the AT Protocol.

The pitch: instead of a platform deciding what you see, you tell an AI what you want and it writes the feed algorithm for you. No coding required. And the long-term vision goes further — Bluesky wants users to eventually vibe-code entire social applications from scratch using nothing but natural language.

This guide covers the architecture, AT Protocol integration, competitive context, and honest limitations. Our analysis draws on reporting from [TechCrunch](https://techcrunch.com/2026/03/28/bluesky-leans-into-ai-with-attie-an-app-for-building-custom-feeds/), [The Next Web](https://thenextweb.com/news/blueskys-new-attie-app-uses-ai-to-give-you-full-control-over-your-social-feed), [PCWorld](https://www.pcworld.com/article/3102155/blueskys-new-ai-app-can-vibe-code-your-social-feed.html), [Gizmodo](https://gizmodo.com/bluesky-has-a-new-app-and-its-all-about-ai-2000739514), and [Winbuzzer](https://winbuzzer.com/2026/03/31/bluesky-attie-ai-custom-feeds-app-xcxwbn/) — we research and analyze rather than testing products hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

---

## Why This Matters: Who Controls Your Feed?

Social media feeds are algorithmic black boxes. X (formerly Twitter), Instagram, TikTok, and Facebook all decide what you see based on engagement optimization — maximizing time-on-platform, not user satisfaction. Users have almost no control beyond muting keywords or unfollowing accounts.

Bluesky took a different approach from the start. Built on the AT Protocol, it supports custom feed generators — algorithmic feeds created by third parties. But building one requires programming knowledge, which limits the feature to developers.

Attie removes that barrier. Instead of writing code, you describe what you want in a chat interface:

- "Show me posts about AI research from people I follow, skip anything about crypto"
- "Build a feed of landscape photography with no reposts"
- "I want to see discussion threads about climate policy, prioritize long-form posts"

Claude interprets the intent, writes the feed logic, and deploys it to your account. The feed updates in real time as new posts come in.

This is a genuine power shift. For the first time on a major social platform, non-technical users can define their own algorithmic experience through conversation.

## How Attie Works

### AT Protocol Foundation

Attie runs on the AT Protocol (ATProto), Bluesky's open protocol for decentralized social networking. This matters because:

- **Shared data layer** — Attie can access your social graph, post history, likes, and interactions across any ATProto-compatible app, not just Bluesky
- **Portable identity** — you sign in with your Atmosphere account (your identity across the ATProto ecosystem), not a new account
- **Open feed generators** — custom feeds are a native ATProto feature, so Attie-created feeds work across any compatible client

Because ATProto is an open protocol with shared data, Attie has rich context about your interests without needing you to manually configure preferences. It can analyze what you post about, who you interact with, and what content you engage with — then use that understanding to build feeds that actually match what you want.

### Claude as the Engine

Under the hood, Attie uses Anthropic's Claude as a coding agent. When you describe a feed in natural language, Claude:

1. **Interprets your intent** — understanding not just keywords but the tone and type of content you want
2. **Writes feed logic** — generates the algorithmic rules that filter, rank, and surface posts
3. **Deploys the feed** — makes it available on your account, accessible from any ATProto client
4. **Iterates on feedback** — you can refine the feed through continued conversation ("fewer reposts," "more from this topic")

This is Claude functioning as an agentic coding assistant — translating natural language into working feed algorithms in real time.

### The "Vibe-Coding" Concept

Bluesky's term for this approach is "vibe-coding." Rather than specifying exact filter rules (show posts with keyword X from accounts Y), you describe the vibe:

- "I want a feed that feels like early Twitter — short, witty observations from real people"
- "Show me the kind of posts that would spark a good dinner conversation"
- "Build me a morning briefing feed — news and analysis, no memes"

The AI interprets these fuzzy, intent-based descriptions and maps them to concrete algorithmic logic. It's a natural evolution of how people already describe their preferences — they rarely say "filter by engagement_score > 0.7 AND follower_count < 10000"; they say "I want interesting posts from regular people."

## Leadership Context

Attie's significance is underscored by who's building it. Jay Graber, Bluesky's co-founder and CEO since its inception, stepped down from the CEO role to lead this project. She now holds the title of Chief Innovation Officer, heading a new Exploration team focused on building new products for the Atmosphere ecosystem.

Toni Schneider stepped in as interim CEO to handle day-to-day operations while Graber focuses on Attie and the broader vision of AI-powered social applications.

This is unusual. CEOs don't typically step down to lead a single product unless they believe it represents the future of the company. It signals that Bluesky sees AI-powered user customization — not just decentralization — as its core competitive advantage.

## The Bigger Vision: Vibe-Coding Social Apps

Custom feeds are the starting point, but Bluesky's roadmap for Attie goes much further. The plan is to let users build entire social applications using only natural language.

Imagine telling Attie:

- "Build me a book club app where members can share quotes, rate books, and see a weekly digest"
- "Create a local community board for my neighborhood — posts with location tags, event listings, and a marketplace"
- "I want a collaborative playlist app where people can suggest songs and vote"

Because ATProto is an open protocol with portable identity and shared data, these apps would interoperate with Bluesky and each other. Your followers, social graph, and content would carry across applications.

This is the most ambitious part of the vision — and the most uncertain. Building custom feeds from natural language is a constrained problem with clear inputs and outputs. Building entire applications is orders of magnitude more complex. But if it works, it transforms Bluesky from a Twitter alternative into a platform where anyone can create social software.

## Competitive Context

### Versus X (Grok)

X offers Grok, an AI assistant integrated into the platform. But Grok operates within X's closed ecosystem — it can summarize trends, answer questions, and generate content, but it cannot modify your algorithmic feed or build custom feed logic. The algorithm remains under X's control.

Attie inverts this: the AI works for *you*, building *your* algorithm, on an open protocol where *you* own your data.

### Versus Meta (Instagram, Threads)

Meta's approach to AI focuses on content generation (Meta AI for chat, AI-generated content in feeds) and engagement optimization. Users cannot customize their algorithmic experience beyond basic controls. Meta has no equivalent to user-defined feed generators.

### Versus Mastodon / Fediverse

Mastodon offers chronological timelines with no algorithmic feeds at all — by design. Some users prefer this purity, but it means discovery is limited to who you follow and what they boost. Attie offers a middle path: algorithmic feeds that exist, but that *you* control rather than a platform.

### The Unique Position

Attie occupies a space no one else is targeting: **user-controlled AI-generated algorithms on an open protocol**. It combines:

- Open protocol (like Mastodon) — but with AI-powered discovery
- AI integration (like X/Grok) — but serving the user, not the platform
- Feed customization (like Bluesky's existing feed generators) — but accessible to non-developers

## Current Availability

Attie launched as an invite-only beta at the ATmosphere conference on March 28, 2026. Conference attendees were the first testers. A public waitlist is open for broader access.

Bluesky recently secured $100 million in funding, giving it over three years of financial runway — important context for a product that generates no direct revenue and depends on Anthropic's Claude API (which costs money per request).

## Honest Limitations

**Beta stage, invite-only.** Most people can't use Attie yet. The experience of early beta testers may not represent the final product.

**Claude API costs.** Every feed generation and refinement request hits Anthropic's API. At scale — millions of users building and refreshing custom feeds — this could be expensive. Bluesky hasn't disclosed how it plans to fund this long-term. The $100 million runway helps, but API costs scale linearly with usage.

**Feed quality depends on AI interpretation.** Natural language is ambiguous. "Interesting posts from regular people" means different things to different users. The gap between what you describe and what the AI builds may require significant iteration to close.

**Privacy implications.** For Attie to build good feeds, it needs to analyze your social graph, interactions, and content preferences. On an open protocol, this data is already public — but concentrating it in an AI system that builds behavioral profiles is a different dynamic than distributed, unanalyzed public data.

**Vibe-coding apps is speculative.** Building custom feeds is a relatively constrained task. Building entire social applications from natural language is vastly more complex. The app-building roadmap is a vision, not a shipped feature, and may take years to materialize — if it does at all.

**AT Protocol adoption is still niche.** Bluesky has grown significantly, but the broader ATProto ecosystem remains small compared to X, Instagram, or TikTok. Attie's value proposition depends partly on the richness of the content available through the protocol.

**No offline or self-hosted option.** Attie requires Bluesky's infrastructure and Anthropic's API. Users who value decentralization may find it ironic that the feed customization layer is centralized.

## What to Watch

- **Public launch timeline** — when Attie moves from invite-only to general availability
- **Monetization model** — how Bluesky plans to sustain Claude API costs at scale (subscription? freemium? usage caps?)
- **Feed quality benchmarks** — whether AI-generated feeds actually surface better content than default algorithms
- **App-building features** — any progress toward the vibe-coding-apps vision beyond feed customization
- **Third-party integrations** — whether other ATProto apps adopt Attie's feed generation capabilities
- **Competitive response** — whether X, Meta, or Mastodon introduce similar user-controlled algorithmic features

## Bottom Line

Attie is the first serious attempt to let non-technical users control their social media algorithm through conversation with an AI. Built on an open protocol and powered by Claude, it represents a fundamentally different vision for social media — one where the algorithm serves the user rather than the platform.

The current reality is modest: an invite-only beta that builds custom feeds. But the trajectory — from custom feeds to custom apps, all through natural language — would reshape how people interact with social software if it succeeds.

The most telling signal is Jay Graber stepping down as CEO to build this. Bluesky isn't treating AI-powered customization as a feature. It's treating it as the future of the company.

