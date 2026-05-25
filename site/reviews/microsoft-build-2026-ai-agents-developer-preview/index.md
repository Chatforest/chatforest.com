# Microsoft Build 2026 Preview: AI as Infrastructure, Agent Framework 1.0, and the Developer Stack That Changed

> Microsoft Build 2026 runs June 2–3 in San Francisco. Here's what's confirmed, what's expected, and what AI developers should actually watch in Satya Nadella's keynote and the 200+ sessions.


**Editorial note:** This is a preview article. Microsoft Build 2026 runs June 2–3, 2026. Keynote announcements are unconfirmed as of publication (May 23, 2026). Where noted, information comes from the published session catalog, Microsoft blog posts, and pre-event previews. A post-event review will be published after the keynote.

---

**At a glance:** Microsoft Build 2026. June 2–3, 2026. Fort Mason Center for Arts & Culture, San Francisco. In-person: ~2,500 developers. Online: free. Satya Nadella keynote June 2. Theme: AI agents, trust, developer platform shift. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

Microsoft Build moves to San Francisco for the first time since 2016. The venue shift signals something deliberate. Fort Mason — a waterfront arts campus, not a convention center — caps in-person attendance at around 2,500. The format is explicit: smaller audience, direct access to Microsoft engineers, live systems over slide decks.

That format choice is consistent with the substance of the agenda. Microsoft Build 2026 is not a product announcement event. It is a developer education event for a platform that already shipped.

---

## The Thesis: AI as Infrastructure

The clearest pre-event signal from Microsoft is this framing from their own event preview materials: **AI is no longer an assistant. It is infrastructure.**

Copilot is not a feature inside apps. It is the layer connecting documents, emails, code, and data systems. Agent Framework 1.0 is not a prototype. It is in production, GA'd in April 2026, with .NET and Python libraries shipping side by side.

This framing matters for how to watch Build 2026. The announcements you should pay attention to are not "new AI feature X" — they are integration points: what in Windows, GitHub, Azure, and M365 now treats AI as a first-class runtime dependency.

---

## What's Already Shipped (Build Will Go Deeper)

Build 2026 sessions will dig into things Microsoft has already released. Understanding what's live helps set expectations for what keynote surprises are actually possible.

**Microsoft Agent Framework 1.0** (GA: April 2026) is a production agent orchestration library for .NET and Python. It supports the A2A (Agent-to-Agent) protocol — a structured messaging standard that lets agents built in different runtimes communicate. A Python agent can coordinate with a .NET agent. The Agent Store currently lists 70+ pre-built agents with multi-agent orchestration via A2A.

**Azure AI Foundry** now carries 100+ models in a curated catalog: Anthropic Claude Opus 4.7, OpenAI GPT-5.5, Phi models, and open-weight models from the broader ecosystem. Foundry Local supports running models on-device. The agent builder is no-code; the Foundry Agent Service is production-grade. The Agent Monitoring Dashboard provides observability: operational metrics, evaluation results, hosted-agent tracing.

**GitHub Copilot SDK** has expanded beyond autocomplete. Agentic code fixing is live: Copilot can identify a failing test, trace the bug, propose a fix, and deploy to Azure Container Apps in a single agentic loop. The `azd ai agent run` and `azd ai agent invoke` commands let developers test agents locally before deploying to Foundry.

**Copilot Studio** (April 2026 update) added governance tooling: admins can discover and manage agents across a subscription via Foundry Control Plane. Intelligent workflows handle multi-step orchestration with decision logic.

**Phi-4 Reasoning Vision 15B** is now part of the Phi family — a 15B-parameter model with visual understanding and chain-of-thought reasoning, designed for edge and CPU deployment. The broader Phi family now has over 60 million downloads across Foundry and Hugging Face.

---

## Keynote: What to Watch

Satya Nadella keynotes June 2. Based on session catalog themes and recent Microsoft engineering blog posts, these are the areas worth watching closely:

**1. Phi-5 or first-party frontier model announcement**
Phi-4 Reasoning Vision is the most capable Phi to date, but it sits below the frontier tier ($1.25–$2.50/M range) by a significant margin. Microsoft has been building MAI (Microsoft AI Research) models quietly. If Build 2026 includes a Phi-5 or MAI-series announcement at frontier capability, it would change Microsoft's competitive position significantly. This is the highest-stakes keynote unknown.

**2. GitHub Copilot as a full coding agent**
GitHub Copilot has been moving from "tab completion" to "agent that writes, runs, and debugs code." The session catalog includes deep dives on the Copilot SDK. Watch for whether Nadella positions Copilot as capable of handling a full issue-to-PR workflow autonomously — and what enterprise safety controls come with that.

**3. Windows AI API surface**
Windows 12 is in developer preview. Build 2026 is where Microsoft traditionally ships the developer APIs that will define the next Windows generation. Watch for announcements about AI capabilities exposed at the OS layer: local model inference, agent sandboxing, PC-level memory and context management.

**4. Azure AI Foundry cost control tooling**
One session theme is "model-cost control." Foundry already has 100+ models and pricing varies wildly. Watch for announcements about cost visibility dashboards, per-model spend analytics, and intelligent routing between models based on task complexity and budget. This is less exciting but operationally critical for enterprise teams.

**5. A2A protocol standardization progress**
Microsoft is one of the key proponents of the A2A protocol (alongside Google and Anthropic). Build 2026 may announce expanded A2A compatibility with third-party agent frameworks (LangGraph, CrewAI, AutoGen) and a broader Agent Store catalog. If A2A gets real cross-vendor adoption at Build, it becomes the baseline for multi-agent enterprise systems.

---

## Notable Speakers

Beyond Nadella, the confirmed speaker list includes names with strong technical credibility in the developer AI space:

**Simon Willison** (Datasette founder) — known for his rigorous, skepticism-forward writing on AI tooling and LLMs. His presence signals that Build 2026 is trying to speak to developers who want depth over marketing.

**Shawn Wang (swyx)** — founder of smol.ai, prolific writer on AI engineering. A core voice in the "LLM engineering" community. His sessions tend to be opinionated and practical.

**Chip Huyen** — author of *AI Engineering* and *Designing Machine Learning Systems*, Stanford lecturer, widely read on ML production systems. Her presence alongside the "production systems" track is not accidental.

**Priyanka Sharma** — Interim SVP of Product at Thiink, focused on enterprise AI product deployment.

---

## Format and Access

**In-person:** ~2,500 developers. Fort Mason Center, San Francisco. $1,099 ticket. Sessions are L-200 to L-400 technical depth — no introductory filler, live code expected.

**Online:** Free. Keynote and select sessions livestreamed. Full session catalog available after the event.

**Session catalog** went live in April 2026 and is searchable by track (developer tools, cloud platform, agents and apps, responsible AI, Windows, model training).

---

## What This Run Won't Cover

Three things Build 2026 almost certainly will *not* substantially address:

- **OpenAI's roadmap.** Microsoft's Azure partnership with OpenAI is deep, but Build is Microsoft's platform event. GPT-5.5 and beyond will be available on Azure AI Foundry; the strategy discussion will stay at the SDK and infrastructure layer, not model capability comparisons.

- **Consumer product announcements.** Copilot in M365 consumer apps, Bing AI features, Xbox AI — these have their own event cadence. Build is developer-focused.

- **Pricing changes to Azure AI.** Foundry model pricing follows Azure pricing pages, not keynote announcements.

---

## Post-Event

This article will be updated with key announcements after Satya Nadella's June 2 keynote. The questions above — Phi-5, Copilot as coding agent, Windows AI APIs, A2A standardization — are the specific things ChatForest will be tracking.

If Microsoft answers even two of those four cleanly, Build 2026 will have been worth the $1,099 ticket. If the keynote is mostly "here's more of what you already know about Copilot," it will be a different kind of event entirely.

---

*Microsoft Build 2026 opens June 2, 2026. Free online registration available at Microsoft's official event site. ChatForest will publish a post-event review after the June 2 keynote.*

