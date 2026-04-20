# OpenAI's Acquisition Spree: Six Deals in Three Months, and the Open-Source Projects Caught in the Middle

> OpenAI has made six acquisitions in the first quarter of 2026 alone — nearly matching all of 2025 in three months. The targets: Convogo (executive coaching AI), Torch Health ($60-100M, medical records for ChatGPT Health), Crixet (LaTeX editor, now OpenAI Prism), Peter Steinberger's OpenClaw (acqui-hire, personal agents), Promptfoo ($23M raised, AI security red-teaming for Frontier), and Astral (uv, ruff, ty — foundational Python developer tools). The pattern is clear: OpenAI is buying its way into developer infrastructure, healthcare, scientific publishing, and AI security. But the open-source acquisitions — Astral and Promptfoo especially — raise uncomfortable questions. Can a company that abandoned 'open' in its own name be trusted to steward tools that millions of developers depend on? Simon Willison warns OpenAI could use uv ownership as competitive leverage against Anthropic. Meanwhile, the $3B Windsurf deal collapsed after Microsoft refused to wall off the IP from GitHub Copilot, and Google swooped in to hire the CEO. This analysis covers every 2026 deal, the strategic logic, the open-source risks, and what the failed Windsurf acquisition reveals about the real power dynamics in AI.


OpenAI made [six acquisitions in the first three months of 2026](https://news.crunchbase.com/ma/data-openai-2023-2026-acquisitions-open-source-astral-promptfoo/). That nearly matches its [eight deals from all of 2025](https://news.crunchbase.com/ma/data-openai-2023-2026-acquisitions-open-source-astral-promptfoo/) — and its total since founding [now stands at 17](https://news.crunchbase.com/ma/data-openai-2023-2026-acquisitions-open-source-astral-promptfoo/).

The targets range from a [four-person health records startup](https://techcrunch.com/2026/01/12/openai-buys-tiny-health-records-startup-torch-for-reportedly-100m/) to the company behind [some of the most widely used developer tools in the Python ecosystem](https://www.cnbc.com/2026/03/19/openai-to-acquire-developer-tooling-startup-astral.html). Each acquisition tells a different story, but together they reveal a company that is systematically buying its way into the infrastructure layer of software development, healthcare, scientific publishing, and AI security.

This analysis draws on reporting from [Crunchbase](https://news.crunchbase.com/ma/data-openai-2023-2026-acquisitions-open-source-astral-promptfoo/), [CNBC](https://www.cnbc.com/2026/03/19/openai-to-acquire-developer-tooling-startup-astral.html), [TechCrunch](https://techcrunch.com/2026/03/09/openai-acquires-promptfoo-to-secure-its-ai-agents/), [Fortune](https://fortune.com/2025/07/11/the-exclusivity-on-openais-3-billion-acquisition-for-coding-startup-windsfurf-has-expired/), [Bloomberg](https://www.bloomberg.com/news/articles/2025-07-11/openai-s-3-billion-deal-to-buy-ai-startup-windsurf-falls-apart), and [Simon Willison's analysis](https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/) — we research and analyze rather than testing products hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

---

## The Six Deals of Q1 2026

Here is every acquisition OpenAI closed or announced in the first quarter, in chronological order.

### 1. Convogo — January 8, 2026

**What it was:** A business software platform for executive coaches, consultants, and HR teams to [automate leadership assessments and feedback reporting](https://techcrunch.com/2026/01/08/openai-to-acquire-the-team-behind-executive-coaching-ai-tool-convogo/). The startup [began as a "weekend hackathon"](https://techcrunch.com/2026/01/08/openai-to-acquire-the-team-behind-executive-coaching-ai-tool-convogo/) sparked by co-founder Matt Cooper's mother, an executive coach who wanted AI to automate report writing.

**Deal structure:** [All-stock acqui-hire](https://dataconomy.com/2026/01/09/openai-acquires-convogo-team-to-boost-ai-cloud-efforts/). OpenAI is [not acquiring Convogo's IP or technology](https://techcrunch.com/2026/01/08/openai-to-acquire-the-team-behind-executive-coaching-ai-tool-convogo/) — only the three co-founders ([Matt Cooper, Evan Cater, Mike Gillett](https://www.pymnts.com/artificial-intelligence-2/2026/openai-hires-co-founders-of-ai-powered-tool-convogo/)). Convogo's product will be wound down.

**Why it matters:** The team is joining OpenAI's ["AI cloud efforts"](https://techcrunch.com/2026/01/08/openai-to-acquire-the-team-behind-executive-coaching-ai-tool-convogo/). This is a pure talent play — OpenAI wanted the people, not the product. The deal marks [OpenAI's ninth acquisition in a year](https://techcrunch.com/2026/01/08/openai-to-acquire-the-team-behind-executive-coaching-ai-tool-convogo/), per PitchBook data.

### 2. Torch Health — January 12, 2026

**What it was:** A one-year-old app that [aggregates medical records from hospitals, labs, wearables, and consumer testing companies](https://techcrunch.com/2026/01/12/openai-buys-tiny-health-records-startup-torch-for-reportedly-100m/) into one place. The Torch team described their technology as ["a medical memory for AI, unifying scattered records into a context engine"](https://siliconangle.com/2026/01/12/openai-buys-torch-bring-unified-medical-data-chatgpt-health/).

**Deal structure:** All-equity, valued between [$60 million](https://www.cnbc.com/2026/01/12/open-ai-torch-health-care-technology.html) and [$100 million](https://techcrunch.com/2026/01/12/openai-buys-tiny-health-records-startup-torch-for-reportedly-100m/) (reports vary). Torch's [four-person team](https://techcrunch.com/2026/01/12/openai-buys-tiny-health-records-startup-torch-for-reportedly-100m/) joins OpenAI.

**Why it matters:** Torch was acquired [days after OpenAI unveiled ChatGPT Health](https://techcrunch.com/2026/01/12/openai-buys-tiny-health-records-startup-torch-for-reportedly-100m/), a new experience that lets users connect medical records and wellness apps to the chatbot. Co-founder [Ilya Abyzov confirmed](https://siliconangle.com/2026/01/12/openai-buys-torch-bring-unified-medical-data-chatgpt-health/) the team and its tech will be part of ChatGPT Health. Torch gives OpenAI domain-specific healthcare data expertise, regulatory workflow knowledge, and a consumer-facing product that accelerates ChatGPT's vertical push into healthcare.

A four-person startup acquired for up to $100 million — roughly $25 million per employee — signals how aggressively OpenAI values domain expertise in regulated industries.

### 3. Crixet — January 2026

**What it was:** A [browser-based LaTeX editor](https://www.useoctree.com/blog/crixet-to-prism) with error detection and team collaboration features.

**What it became:** [OpenAI Prism](https://openai.com/index/introducing-prism/) — a ChatGPT-based collaborative editor for scientific documents, [launched January 27, 2026](https://leaveit2ai.com/ai-tools/academic-research/chatgpt-prism). Users can add formulas or visualizations by describing them in natural language, [chat with GPT-5.2 Thinking to explore ideas and test hypotheses](https://openai.com/index/introducing-prism/), transform hand-drawn sketches into diagrams, generate summaries, and [search sources from arXiv](https://openai.com/index/introducing-prism/). Prism is [free to use — no subscriptions or seat limits](https://openai.com/prism/).

**Why it matters:** This is OpenAI's bet on scientific publishing. Prism targets the same audience as [Overleaf](https://www.useoctree.com/blog/crixet-to-prism) (the dominant LaTeX collaboration platform), but with AI-native features. If ChatGPT becomes the way scientists write papers, OpenAI owns the workflow.

### 4. Peter Steinberger / OpenClaw — February 15, 2026

**What it was:** OpenClaw is an [open-source personal agent](https://steipete.me/posts/2026/openclaw) that [went viral on GitHub, hitting 198,000 stars](https://businessengineer.ai/p/openai-openclaw-deal-and-the-war). Peter Steinberger, an Austrian developer, built it. The agent [operates via messaging apps — WhatsApp, Telegram, Signal, and iMessage](https://businessengineer.ai/p/openai-openclaw-deal-and-the-war) — letting users delegate real-world tasks through chat.

**Deal structure:** [Acqui-hire](https://techcrunch.com/2026/02/15/openclaw-creator-peter-steinberger-joins-openai/). Sam Altman [personally announced](https://www.cnbc.com/2026/02/15/openclaw-creator-peter-steinberger-joining-openai-altman-says.html): "Peter Steinberger is joining OpenAI to drive the next generation of personal agents. He is a genius with a lot of amazing ideas about the future of very smart agents interacting with each other to do very useful things for people." Both [Mark Zuckerberg and Sam Altman made competing offers](https://steipete.me/posts/2026/openclaw) — Zuckerberg reached out via WhatsApp.

**What happened to OpenClaw:** It will [move to a non-profit foundation](https://steipete.me/posts/2026/openclaw) and remain open-source under the MIT licence, with [OpenAI sponsoring but not controlling](https://aitoolsreview.co.uk/insights/openai-acquihires-openclaw) the foundation.

**Why it matters:** [Steinberger said](https://steipete.me/posts/2026/openclaw) he could have turned OpenClaw into a company, but "it's not really exciting for me. What I want is to change the world, not build a large company, and teaming up with OpenAI is the fastest way to bring this to everyone." OpenAI is buying vision and agent-architecture expertise, not code.

### 5. Promptfoo — March 9, 2026

**What it was:** An [AI security platform for identifying and remediating vulnerabilities](https://techcrunch.com/2026/03/09/openai-acquires-promptfoo-to-secure-its-ai-agents/) in AI systems during development. [Open-source CLI and library](https://www.promptfoo.dev/blog/promptfoo-joining-openai/) for evaluating and red-teaming LLM applications. [Trusted by over 25% of Fortune 500 companies](https://futurumgroup.com/insights/openai-acquires-promptfoo-gaining-25-foothold-in-fortune-500-enterprises/), with [more than 350,000 developers](https://www.promptfoo.dev/blog/promptfoo-joining-openai/) having used it and [130,000 active each month](https://www.promptfoo.dev/blog/promptfoo-joining-openai/). Founded by [Ian Webster](https://www.promptfoo.dev/blog/promptfoo-joining-openai/) (former Discord LLM engineering lead) and [Michael D'Angelo](https://www.promptfoo.dev/blog/promptfoo-joining-openai/) (former VP of engineering at Smile Identity).

**Deal structure:** [Financial terms undisclosed](https://www.cnbc.com/2026/03/09/open-ai-cybersecurity-promptfoo-ai-agents.html). Promptfoo had [raised $23 million at an $86 million valuation](https://techcrunch.com/2026/03/09/openai-acquires-promptfoo-to-secure-its-ai-agents/).

**Integration:** Promptfoo's [automated red-teaming, prompt-injection detection, data-leak prevention, jailbreak identification, and compliance monitoring](https://openai.com/index/openai-to-acquire-promptfoo/) will be integrated into [OpenAI Frontier](https://techcrunch.com/2026/03/09/openai-acquires-promptfoo-to-secure-its-ai-agents/) — the company's platform for building and operating AI coworkers.

**Open-source commitment:** [OpenAI says it expects to continue building out Promptfoo's open-source offering](https://openai.com/index/openai-to-acquire-promptfoo/).

**Why it matters:** As AI agents gain autonomy, the attack surface grows exponentially. Promptfoo gives OpenAI native security testing capabilities for the agentic era. This is defensive infrastructure — if enterprises are going to deploy AI agents through Frontier, they need to know those agents can't be jailbroken, injected, or tricked into leaking data.

### 6. Astral — March 19, 2026

**What it was:** The company behind [uv (a Python package installer and resolver), Ruff (a Python linter and formatter), and ty (a Python type checker)](https://openai.com/index/openai-to-acquire-astral/). These are [some of the most widely used developer tools in the Python ecosystem](https://www.cnbc.com/2026/03/19/openai-to-acquire-developer-tooling-startup-astral.html) — uv alone has reshaped how millions of developers manage Python dependencies.

**Deal structure:** [Not disclosed](https://www.cnbc.com/2026/03/19/openai-to-acquire-developer-tooling-startup-astral.html). Astral's team joins OpenAI to [work on Codex](https://openai.com/index/openai-to-acquire-astral/), OpenAI's AI coding assistant — which has seen [3x user growth and 5x usage increase since the start of the year, with over 2 million weekly active users](https://openai.com/index/openai-to-acquire-astral/) at the time of the announcement, [reaching 3 million weekly users by April 8](https://www.businesstoday.in/technology/story/openai-codex-celebrates-3-million-weekly-users-ceo-sam-altman-resets-usage-limits-524717-2026-04-08).

**Open-source commitment:** [OpenAI says it plans to support Astral's open-source products after closing](https://astral.sh/blog/openai).

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

Two of these acquisitions — Astral and Promptfoo — involve beloved open-source projects. In both cases, OpenAI has [promised to continue supporting](https://openai.com/index/openai-to-acquire-astral/) the [open-source versions](https://openai.com/index/openai-to-acquire-promptfoo/). In both cases, skeptics have reason to worry.

### Simon Willison's Warning About Astral

Simon Willison, one of the most respected voices in the Python ecosystem, [published a detailed analysis](https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/) of the Astral acquisition that captures the community's ambivalence:

**Concern 1: No track record.** ["OpenAI don't yet have much of a track record with respect to acquiring and maintaining open source projects."](https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/) This is the first time OpenAI has owned truly critical open-source infrastructure. There's no precedent to judge by.

**Concern 2: Product vs. talent.** Product-plus-talent acquisitions can turn into talent-only acquisitions later. If OpenAI decides the engineering team is more valuable working on Codex than maintaining uv, the open-source projects could [wither through neglect](https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/) rather than explicit abandonment.

**Concern 3: Competitive leverage.** ["One bad version of this deal would be if OpenAI start using their ownership of uv as leverage in their competition with Anthropic."](https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/) OpenAI could theoretically steer uv's development to work better inside OpenAI's stack than anywhere else. The MIT license means anyone can fork, but ["maintenance priorities" and "feature direction"](https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/) are harder to replicate than code.

**The safety net:** [Willison acknowledges](https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/) that permissive licensing (MIT) means the worst case is "fork and move on," not "software disappears forever." But forking load-bearing infrastructure is costly and disruptive, even when it's legally straightforward.

### The Broader Pattern

A [joint statement signed by eight open-source foundations](https://openssf.org/blog/2025/09/23/open-infrastructure-is-not-free-a-joint-statement-on-sustainable-stewardship/) — including the [Python Software Foundation, Rust Foundation, Eclipse Foundation, and OpenJS Foundation](https://www.itbrew.com/stories/2025/09/25/stewards-of-public-open-source-infrastructure-say-it-s-time-to-change-how-it-is-funded) — in September 2025 warned that open source ["operates under a dangerously fragile premise"](https://openssf.org/blog/2025/09/23/open-infrastructure-is-not-free-a-joint-statement-on-sustainable-stewardship/) reliant on goodwill. OpenAI's acquisitions of Astral and Promptfoo are a live test of that premise.

The dynamic is not unique to OpenAI. When any well-funded company acquires open-source projects, the community faces the same question: will corporate ownership accelerate development, or will it eventually subordinate community interests to corporate strategy?

OpenAI's particular history — a company that [started as a nonprofit in 2015](https://en.wikipedia.org/wiki/OpenAI), then [transitioned to a "capped" for-profit in 2019](https://time.com/7328674/openai-chatgpt-sam-altman-elon-musk-timeline/), then [closed its models](https://futurism.com/artificial-intelligence/openai-sheds-roots-ethical-non-profit) while keeping "Open" in the name, and most recently [restructured into a public benefit corporation](https://openai.com/index/evolving-our-structure/) — makes the question especially pointed.

---

## The Deal That Died: Windsurf and the Microsoft Veto

To understand the real constraints on OpenAI's acquisition strategy, look at the deal that didn't happen.

In May 2025, OpenAI agreed to buy [Windsurf (formerly Codeium)](https://fortune.com/2025/07/11/the-exclusivity-on-openais-3-billion-acquisition-for-coding-startup-windsfurf-has-expired/), an AI-native coding IDE, [for $3 billion](https://www.itpro.com/software/development/openais-plan-to-acquire-ai-coding-startup-windsurf-ended-in-disaster-heres-how-the-deal-fell-apart) — at the time, its largest acquisition ever. The deal made strategic sense: Windsurf was a direct competitor to Cursor and a strong complement to Codex.

But the deal [collapsed in July 2025](https://fortune.com/2025/07/11/the-exclusivity-on-openais-3-billion-acquisition-for-coding-startup-windsfurf-has-expired/), and the reason reveals something important about OpenAI's corporate structure.

### What Actually Killed It

The failure wasn't primarily antitrust. Microsoft, as OpenAI's strategic partner, [holds rights to much of OpenAI's IP under a sweeping agreement](https://winbuzzer.com/2025/07/15/anatomy-of-a-collapse-the-wild-takeover-saga-of-windsurf-featuring-openai-anthropic-microsoft-google-and-cognition-xcxwbn/) — including [access to model weights, code, and any IP OpenAI gains through acquisitions](https://winbuzzer.com/2025/07/15/anatomy-of-a-collapse-the-wild-takeover-saga-of-windsurf-featuring-openai-anthropic-microsoft-google-and-cognition-xcxwbn/). OpenAI sought a special exception to wall off Windsurf's IP from Microsoft. [Windsurf CEO Varun Mohan reportedly made clear he didn't want Microsoft anywhere near the startup's tech](https://winbuzzer.com/2025/07/15/anatomy-of-a-collapse-the-wild-takeover-saga-of-windsurf-featuring-openai-anthropic-microsoft-google-and-cognition-xcxwbn/), given GitHub Copilot's position as a direct competitor.

The logic from Microsoft's perspective was straightforward: Windsurf was a direct competitor to [GitHub Copilot](https://techstartups.com/2025/07/11/openai-windsurf-end-acquisition-talks-over-microsoft-ip-concerns-google-swoops-in/), Microsoft's own highly profitable AI coding assistant. Allowing OpenAI to acquire Windsurf while walling off its technology from Microsoft would mean Microsoft was effectively financing its own competition.

### Google Swoops In

After the [exclusivity period expired](https://fortune.com/2025/07/11/the-exclusivity-on-openais-3-billion-acquisition-for-coding-startup-windsfurf-has-expired/), Google struck a deal to [pay about $2.4 billion for top talent and licensing rights](https://www.cnbc.com/2025/07/11/google-windsurf-ceo-varun-mohan-latest-ai-talent-deal-.html) from Windsurf. Google [hired Windsurf CEO Varun Mohan and co-founder Douglas Chen](https://www.cnbc.com/2025/07/11/google-windsurf-ceo-varun-mohan-latest-ai-talent-deal-.html), along with [approximately 40 senior R&D staff](https://techcrunch.com/2025/08/01/more-details-emerge-on-how-windsurfs-vcs-and-founders-got-paid-from-the-google-deal/), to work at DeepMind. Meanwhile, [Cognition (maker of the AI coding agent Devin) acquired Windsurf](https://techcrunch.com/2025/07/14/cognition-maker-of-the-ai-coding-agent-devin-acquires-windsurf/) itself as a company.

### What This Reveals

The Windsurf episode shows that OpenAI's M&A freedom is constrained by [Microsoft's contractual IP rights](https://winbuzzer.com/2025/07/12/googles-2-4b-windsurf-deal-followed-openai-collapse-over-microsoft-ip-veto-xcxwbn/). Under the [restructured partnership announced October 2025](https://blogs.microsoft.com/blog/2025/10/28/the-next-chapter-of-the-microsoft-openai-partnership/), Microsoft's [IP rights for models and products extend through 2032](https://blogs.microsoft.com/blog/2025/10/28/the-next-chapter-of-the-microsoft-openai-partnership/), and Microsoft holds an investment [valued at approximately $135 billion, representing roughly 27% on a diluted basis](https://blogs.microsoft.com/blog/2025/10/28/the-next-chapter-of-the-microsoft-openai-partnership/). OpenAI cannot acquire companies whose IP would threaten Microsoft's products without Microsoft's consent. This limits the scope of OpenAI's acquisition strategy to areas that don't directly compete with Microsoft's existing businesses.

It also explains why the Astral and Promptfoo acquisitions went through smoothly — Python developer tools and AI security testing don't threaten any major Microsoft product line.

---

## The Numbers in Context

OpenAI's Q1 2026 spending spree is happening against a backdrop of [record AI funding](https://news.crunchbase.com/venture/record-breaking-funding-ai-global-q1-2026/):

- [**$297 billion**](https://news.crunchbase.com/venture/record-breaking-funding-ai-global-q1-2026/) raised by startups globally in Q1 2026 — [AI captured 81% of all funding](https://news.crunchbase.com/venture/record-breaking-funding-ai-global-q1-2026/)
- [**$252.6 billion**](https://news.crunchbase.com/venture/funding-surges-all-stages-ai-north-america-q1-2026/) raised in the US and Canada alone — [more than 3x the prior quarter, smashing the previous record of $95.7 billion](https://news.crunchbase.com/venture/funding-surges-all-stages-ai-north-america-q1-2026/) set in Q3 2021
- [**$122 billion**](https://openai.com/index/accelerating-the-next-phase-ai/) — OpenAI's own fundraising round, at an [**$852 billion valuation**](https://www.cnbc.com/2026/03/31/openai-funding-round-ipo.html), co-led by [SoftBank, Andreessen Horowitz, D.E. Shaw Ventures, MGX, and TPG](https://techcrunch.com/2026/03/31/openai-not-yet-public-raises-3b-from-retail-investors-in-monster-122b-fund-raise/), with participation from [Amazon ($50B), Nvidia ($30B), and Microsoft](https://techcrunch.com/2026/03/31/openai-not-yet-public-raises-3b-from-retail-investors-in-monster-122b-fund-raise/)
- [**$2.66 billion**](https://tracxn.com/d/sectors/agentic-ai/__oyRAfdUfHPjf2oap110Wis0Qg12Gd8DzULlDXPJzrzs) raised by agentic AI companies specifically in 2026 through April — a [142.6% increase over 2025](https://tracxn.com/d/sectors/agentic-ai/__oyRAfdUfHPjf2oap110Wis0Qg12Gd8DzULlDXPJzrzs)

OpenAI is not just acquiring companies. It is acquiring at a pace that reflects the broader acceleration of the AI industry. With [$122 billion in fresh capital](https://openai.com/index/accelerating-the-next-phase-ai/) and [revenue crossing $2 billion per month](https://www.coindesk.com/tech/2026/04/01/openai-raises-a-record-usd122-billion-at-as-revenue-crosses-usd2-billion-per-month), it has the war chest to continue.

---

## What We Don't Know

Several important questions remain unanswered:

1. **Actual deal values.** Most of the 2026 acquisitions have undisclosed terms. We know Torch was [$60M](https://www.cnbc.com/2026/01/12/open-ai-torch-health-care-technology.html)–[$100M](https://techcrunch.com/2026/01/12/openai-buys-tiny-health-records-startup-torch-for-reportedly-100m/), and OpenAI's most expensive 2025 deal was the [$6.5 billion acquisition of io](https://techcrunch.com/2025/05/21/jony-ive-to-lead-openais-design-work-following-6-5b-acquisition-of-his-company/) (Jony Ive's AI hardware startup), but the Astral and Promptfoo prices are unknown.

2. **Long-term open-source commitment.** OpenAI has promised to maintain [uv, ruff](https://astral.sh/blog/openai), and [Promptfoo](https://www.promptfoo.dev/blog/promptfoo-joining-openai/) as open-source projects. There is no enforcement mechanism beyond reputation and [MIT licensing](https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/).

3. **Integration timelines.** How quickly will Promptfoo become part of [Frontier](https://openai.com/index/openai-to-acquire-promptfoo/)? Will Astral's tools be integrated into [Codex](https://openai.com/index/openai-to-acquire-astral/) in ways that advantage OpenAI's platform?

4. **Microsoft's future veto power.** Will Microsoft block other acquisitions? The [restructured partnership through 2032](https://blogs.microsoft.com/blog/2025/10/28/the-next-chapter-of-the-microsoft-openai-partnership/) preserves Microsoft's IP rights. How does this constraint shape what OpenAI can and cannot buy?

5. **Antitrust scrutiny.** The FTC has taken a tougher stance on tech mergers. At what point does OpenAI's accumulation of developer infrastructure attract regulatory attention?

6. **Competitive response.** How will Anthropic, Google, and others respond to OpenAI owning critical open-source developer tools?

---

## The Bottom Line

OpenAI's 2026 acquisition strategy is aggressive, systematic, and revealing. The company is building a full-stack platform — from healthcare data ([Torch](https://techcrunch.com/2026/01/12/openai-buys-tiny-health-records-startup-torch-for-reportedly-100m/)) to scientific publishing ([Prism](https://openai.com/index/introducing-prism/)) to developer tools ([Astral](https://openai.com/index/openai-to-acquire-astral/)) to security testing ([Promptfoo](https://openai.com/index/openai-to-acquire-promptfoo/)) to agent architecture ([OpenClaw](https://techcrunch.com/2026/02/15/openclaw-creator-peter-steinberger-joins-openai/)) — through strategic M&A rather than purely internal development.

The open-source acquisitions are the ones to watch. If OpenAI maintains uv, ruff, and Promptfoo as genuine community projects, it earns credibility as a steward of developer infrastructure. If it slowly starves them, steers them toward OpenAI-only optimizations, or [uses them as competitive leverage](https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/), it confirms the worst fears about what happens when open-source projects get swallowed by well-funded platforms.

The Windsurf failure reminds us that OpenAI is not a fully autonomous actor. [Microsoft's contractual rights](https://blogs.microsoft.com/blog/2025/10/28/the-next-chapter-of-the-microsoft-openai-partnership/) constrain what OpenAI can acquire and how it can use what it buys. The real power dynamic in AI isn't just about which company builds the best model — it's about who controls the infrastructure around those models, and who gets to veto whom.

[Six deals in three months](https://news.crunchbase.com/ma/data-openai-2023-2026-acquisitions-open-source-astral-promptfoo/). Seventeen total since founding. And the [$122 billion war chest](https://openai.com/index/accelerating-the-next-phase-ai/) is far from empty.

---

## Related Guides

- [OpenAI's Economic Blueprint: Robot Taxes, Wealth Funds, and Four-Day Workweeks](/guides/openai-economic-blueprint-robot-taxes-wealth-fund/) — OpenAI's policy vision for the economic disruption its technology creates
- [The Enterprise AI Power Shift: Anthropic Takes 40% of LLM Spend](/guides/anthropic-overtakes-openai-enterprise-market-share/) — the broader market context for OpenAI's acquisitions: Anthropic has overtaken OpenAI in enterprise LLM market share and revenue
- [The New Yorker's OpenAI Investigation: Secret Memos, Safety Failures, and a Pattern of 'Lying'](/guides/new-yorker-openai-investigation-altman-safety-crisis/) — The Ronan Farrow investigation adds internal governance context to OpenAI's aggressive expansion strategy

