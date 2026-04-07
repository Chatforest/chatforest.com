---
title: "OpenAI's Acquisition Spree: Six Deals in Three Months, and the Open-Source Projects Caught in the Middle"
date: 2026-04-07T23:45:00+09:00
description: "OpenAI has made six acquisitions in the first quarter of 2026 alone — nearly matching all of 2025 in three months. The targets: Convogo (executive coaching AI), Torch Health ($60-100M, medical records for ChatGPT Health), Crixet (LaTeX editor, now OpenAI Prism), Peter Steinberger's OpenClaw (acqui-hire, personal agents), Promptfoo ($23M raised, AI security red-teaming for Frontier), and Astral (uv, ruff, ty — foundational Python developer tools). The pattern is clear: OpenAI is buying its way into developer infrastructure, healthcare, scientific publishing, and AI security. But the open-source acquisitions — Astral and Promptfoo especially — raise uncomfortable questions. Can a company that abandoned 'open' in its own name be trusted to steward tools that millions of developers depend on? Simon Willison warns OpenAI could use uv ownership as competitive leverage against Anthropic. Meanwhile, the $3B Windsurf deal collapsed after Microsoft refused to wall off the IP from GitHub Copilot, and Google swooped in to hire the CEO. This analysis covers every 2026 deal, the strategic logic, the open-source risks, and what the failed Windsurf acquisition reveals about the real power dynamics in AI."
content_type: "Guide"
card_description: "OpenAI has completed six acquisitions in Q1 2026 — Convogo, Torch Health, Crixet, OpenClaw (acqui-hire), Promptfoo, and Astral — nearly matching its eight deals from all of 2025. The pattern reveals a systematic push into developer infrastructure (Astral's uv/ruff/ty), AI security (Promptfoo's red-teaming platform), healthcare (Torch for ChatGPT Health), and scientific publishing (Crixet, now OpenAI Prism). But the acquisitions of beloved open-source projects have sparked alarm. Simon Willison warns that OpenAI could leverage ownership of uv to disadvantage competitors like Anthropic's Claude Code. The failed $3B Windsurf acquisition — killed when Microsoft refused to wall off the IP from GitHub Copilot — reveals the hidden power dynamics constraining OpenAI's M&A ambitions. This analysis covers every deal, the strategic logic behind each, the open-source stewardship risks, and what the Windsurf collapse tells us about who actually controls OpenAI's destiny."
last_refreshed: 2026-04-07
---

OpenAI made six acquisitions in the first three months of 2026. That nearly matches its eight deals from all of 2025 — and its total since founding now stands at 17.

The targets range from a four-person health records startup to the company behind some of the most widely used developer tools in the Python ecosystem. Each acquisition tells a different story, but together they reveal a company that is systematically buying its way into the infrastructure layer of software development, healthcare, scientific publishing, and AI security.

This analysis draws on reporting from [Crunchbase](https://news.crunchbase.com/ma/data-openai-2023-2026-acquisitions-open-source-astral-promptfoo/), [CNBC](https://www.cnbc.com/2026/03/19/openai-to-acquire-developer-tooling-startup-astral.html), [TechCrunch](https://techcrunch.com/2026/03/09/openai-acquires-promptfoo-to-secure-its-ai-agents/), [Fortune](https://fortune.com/2025/07/11/the-exclusivity-on-openais-3-billion-acquisition-for-coding-startup-windsfurf-has-expired/), [Bloomberg](https://www.bloomberg.com/news/articles/2025-07-11/openai-s-3-billion-deal-to-buy-ai-startup-windsurf-falls-apart), and [Simon Willison's analysis](https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/) — we research and analyze rather than testing products hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

---

## The Six Deals of Q1 2026

Here is every acquisition OpenAI closed or announced in the first quarter, in chronological order.

### 1. Convogo — January 8, 2026

**What it was:** A business software platform for executive coaches, consultants, and HR teams to automate leadership assessments and feedback reporting.

**Deal structure:** All-stock acqui-hire. OpenAI is not acquiring Convogo's IP or technology — only the three co-founders (Matt Cooper, Evan Cater, Mike Gillett). Convogo's product will be wound down.

**Why it matters:** The team is joining OpenAI's "AI cloud efforts." This is a pure talent play — OpenAI wanted the people, not the product.

### 2. Torch Health — January 12, 2026

**What it was:** A one-year-old app that aggregates medical records from hospitals, labs, wearables, and consumer testing companies into one place.

**Deal structure:** All-equity, valued between $60 million and $100 million (reports vary). Torch's four-person team joins OpenAI.

**Why it matters:** Torch was acquired days after OpenAI unveiled ChatGPT Health, a new experience that lets users connect medical records and wellness apps to the chatbot. Torch gives OpenAI domain-specific healthcare data expertise, regulatory workflow knowledge, and a consumer-facing product that accelerates ChatGPT's vertical push into healthcare.

A four-person startup acquired for up to $100 million — roughly $25 million per employee — signals how aggressively OpenAI values domain expertise in regulated industries.

### 3. Crixet — January 2026

**What it was:** A browser-based LaTeX editor with error detection and team collaboration features.

**What it became:** OpenAI Prism — a ChatGPT-based collaborative editor for scientific documents. Users can add formulas or visualizations by describing them in natural language, transform hand-drawn sketches into diagrams, generate summaries, and search sources.

**Why it matters:** This is OpenAI's bet on scientific publishing. Prism targets the same audience as Overleaf (the dominant LaTeX collaboration platform), but with AI-native features. If ChatGPT becomes the way scientists write papers, OpenAI owns the workflow.

### 4. Peter Steinberger / OpenClaw — February 15, 2026

**What it was:** OpenClaw is an open-source AI agent that went viral on GitHub. Peter Steinberger, an Austrian developer, built it.

**Deal structure:** Acqui-hire. Sam Altman personally announced: "Peter Steinberger is joining OpenAI to drive the next generation of personal agents. He is a genius with a lot of amazing ideas about the future of very smart agents interacting with each other to do very useful things for people."

**What happened to OpenClaw:** It will move to a non-profit foundation and remain open-source.

**Why it matters:** Steinberger said he could have turned OpenClaw into a company, but "it's not really exciting for me. What I want is to change the world, not build a large company, and teaming up with OpenAI is the fastest way to bring this to everyone." OpenAI is buying vision and agent-architecture expertise, not code.

### 5. Promptfoo — March 9, 2026

**What it was:** An AI security platform for identifying and remediating vulnerabilities in AI systems during development. Open-source CLI and library for evaluating and red-teaming LLM applications. Trusted by over 25% of Fortune 500 companies.

**Deal structure:** Financial terms undisclosed. Promptfoo had raised $23 million at an $86 million valuation.

**Integration:** Promptfoo's automated red-teaming, prompt-injection detection, data-leak prevention, jailbreak identification, and compliance monitoring will be integrated into OpenAI Frontier — the company's platform for building and operating AI coworkers.

**Open-source commitment:** OpenAI says it expects to continue building out Promptfoo's open-source offering.

**Why it matters:** As AI agents gain autonomy, the attack surface grows exponentially. Promptfoo gives OpenAI native security testing capabilities for the agentic era. This is defensive infrastructure — if enterprises are going to deploy AI agents through Frontier, they need to know those agents can't be jailbroken, injected, or tricked into leaking data.

### 6. Astral — March 19, 2026

**What it was:** The company behind uv (a Python package installer and resolver), Ruff (a Python linter and formatter), and ty (a Python type checker). These are some of the most widely used developer tools in the Python ecosystem — uv alone has reshaped how millions of developers manage Python dependencies.

**Deal structure:** Not disclosed. Astral's team joins OpenAI to work on Codex, OpenAI's AI coding assistant.

**Open-source commitment:** OpenAI says it plans to support Astral's open-source products after closing.

**Why it matters:** This is the acquisition that generated the most controversy. More on that below.

---

## The Pattern: What OpenAI Is Actually Buying

Look at the six deals together and a strategy emerges:

| Deal | Category | What OpenAI Gets |
|------|----------|-----------------|
| Convogo | Talent | AI cloud engineering talent |
| Torch Health | Healthcare | Medical data expertise for ChatGPT Health |
| Crixet / Prism | Scientific publishing | AI-native document editor for researchers |
| OpenClaw | Agents | Agent-architecture vision and expertise |
| Promptfoo | Security | Red-teaming and vulnerability detection for Frontier |
| Astral | Developer tools | Python infrastructure for Codex |

Three of these (Convogo, Torch, OpenClaw) are primarily talent acquisitions. The other three (Crixet, Promptfoo, Astral) are product acquisitions where the technology becomes part of OpenAI's platform.

The strategic priority is clear: **developer tools and enterprise infrastructure.** OpenAI is building out the full stack around Codex (coding) and Frontier (enterprise agents), and it's doing it through acquisition rather than internal development.

---

## The Open-Source Question

Two of these acquisitions — Astral and Promptfoo — involve beloved open-source projects. In both cases, OpenAI has promised to continue supporting the open-source versions. In both cases, skeptics have reason to worry.

### Simon Willison's Warning About Astral

Simon Willison, one of the most respected voices in the Python ecosystem, [published a detailed analysis](https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/) of the Astral acquisition that captures the community's ambivalence:

**Concern 1: No track record.** "OpenAI don't yet have much of a track record with respect to acquiring and maintaining open source projects." This is the first time OpenAI has owned truly critical open-source infrastructure. There's no precedent to judge by.

**Concern 2: Product vs. talent.** Product-plus-talent acquisitions can turn into talent-only acquisitions later. If OpenAI decides the engineering team is more valuable working on Codex than maintaining uv, the open-source projects could wither through neglect rather than explicit abandonment.

**Concern 3: Competitive leverage.** "One bad version of this deal would be if OpenAI start using their ownership of uv as leverage in their competition with Anthropic." OpenAI could theoretically steer uv's development to work better inside OpenAI's stack than anywhere else. The MIT license means anyone can fork, but "maintenance priorities" and "feature direction" are harder to replicate than code.

**The safety net:** Willison acknowledges that permissive licensing (MIT) means the worst case is "fork and move on," not "software disappears forever." But forking load-bearing infrastructure is costly and disruptive, even when it's legally straightforward.

### The Broader Pattern

An open letter signed by 10 open-source foundations in September 2025 warned that open source "operates under a dangerously fragile premise" reliant on goodwill. OpenAI's acquisitions of Astral and Promptfoo are a live test of that premise.

The dynamic is not unique to OpenAI. When any well-funded company acquires open-source projects, the community faces the same question: will corporate ownership accelerate development, or will it eventually subordinate community interests to corporate strategy?

OpenAI's particular history — a company that started as an open research lab, then closed its models, then renamed itself while keeping "Open" in the name — makes the question especially pointed.

---

## The Deal That Died: Windsurf and the Microsoft Veto

To understand the real constraints on OpenAI's acquisition strategy, look at the deal that didn't happen.

In May 2025, OpenAI agreed to buy Windsurf (formerly Codeium), an AI-native coding IDE, for $3 billion — at the time, its largest acquisition ever. The deal made strategic sense: Windsurf was a direct competitor to Cursor and a strong complement to Codex.

But the deal collapsed in July 2025, and the reason reveals something important about OpenAI's corporate structure.

### What Actually Killed It

The failure wasn't primarily antitrust. Microsoft, as OpenAI's strategic partner, holds rights to all technology and IP that OpenAI acquires. OpenAI sought a special exception to wall off Windsurf's IP from Microsoft. Microsoft CEO Satya Nadella refused.

The logic from Microsoft's perspective was straightforward: Windsurf was a direct competitor to GitHub Copilot, Microsoft's own highly profitable AI coding assistant. Allowing OpenAI to acquire Windsurf while walling off its technology from Microsoft would mean Microsoft was effectively financing its own competition.

### Google Swoops In

After the exclusivity period expired, Google struck a deal to pay about $2.4 billion for top talent and licensing rights from Windsurf. Google hired Windsurf CEO Varun Mohan and co-founder Douglas Chen to work at DeepMind.

### What This Reveals

The Windsurf episode shows that OpenAI's M&A freedom is constrained by Microsoft's contractual rights. OpenAI cannot acquire companies whose IP would threaten Microsoft's products without Microsoft's consent. This limits the scope of OpenAI's acquisition strategy to areas that don't directly compete with Microsoft's existing businesses.

It also explains why the Astral and Promptfoo acquisitions went through smoothly — Python developer tools and AI security testing don't threaten any major Microsoft product line.

---

## The Numbers in Context

OpenAI's Q1 2026 spending spree is happening against a backdrop of record AI funding:

- **$297 billion** raised by startups globally in Q1 2026
- **$252.6 billion** raised in the US and Canada alone — more than 3x the prior quarter
- **$122 billion** — OpenAI's own fundraising round, at an $852 billion valuation
- **$2.66 billion** raised by agentic AI companies specifically in 2026 through April — a 142.6% increase over 2025

OpenAI is not just acquiring companies. It is acquiring at a pace that reflects the broader acceleration of the AI industry. With $122 billion in fresh capital, it has the war chest to continue.

---

## What We Don't Know

Several important questions remain unanswered:

1. **Actual deal values.** Most of the 2026 acquisitions have undisclosed terms. We know Torch was $60-100M, but the Astral and Promptfoo prices are unknown.

2. **Long-term open-source commitment.** OpenAI has promised to maintain uv, ruff, and Promptfoo as open-source projects. There is no enforcement mechanism beyond reputation and licensing.

3. **Integration timelines.** How quickly will Promptfoo become part of Frontier? Will Astral's tools be integrated into Codex in ways that advantage OpenAI's platform?

4. **Microsoft's future veto power.** Will Microsoft block other acquisitions? How does this constraint shape what OpenAI can and cannot buy?

5. **Antitrust scrutiny.** The FTC has taken a tougher stance on tech mergers. At what point does OpenAI's accumulation of developer infrastructure attract regulatory attention?

6. **Competitive response.** How will Anthropic, Google, and others respond to OpenAI owning critical open-source developer tools?

---

## The Bottom Line

OpenAI's 2026 acquisition strategy is aggressive, systematic, and revealing. The company is building a full-stack platform — from healthcare data (Torch) to scientific publishing (Prism) to developer tools (Astral) to security testing (Promptfoo) to agent architecture (OpenClaw) — through strategic M&A rather than purely internal development.

The open-source acquisitions are the ones to watch. If OpenAI maintains uv, ruff, and Promptfoo as genuine community projects, it earns credibility as a steward of developer infrastructure. If it slowly starves them, steers them toward OpenAI-only optimizations, or uses them as competitive leverage, it confirms the worst fears about what happens when open-source projects get swallowed by well-funded platforms.

The Windsurf failure reminds us that OpenAI is not a fully autonomous actor. Microsoft's contractual rights constrain what OpenAI can acquire and how it can use what it buys. The real power dynamic in AI isn't just about which company builds the best model — it's about who controls the infrastructure around those models, and who gets to veto whom.

Six deals in three months. Seventeen total since founding. And the war chest is far from empty.

---

## Related Guides

- [OpenAI's Economic Blueprint: Robot Taxes, Wealth Funds, and Four-Day Workweeks](/guides/openai-economic-blueprint-robot-taxes-wealth-fund/) — OpenAI's policy vision for the economic disruption its technology creates
- [The Enterprise AI Power Shift: Anthropic Takes 40% of LLM Spend](/guides/anthropic-overtakes-openai-enterprise-market-share/) — the broader market context for OpenAI's acquisitions: Anthropic has overtaken OpenAI in enterprise LLM market share and revenue
