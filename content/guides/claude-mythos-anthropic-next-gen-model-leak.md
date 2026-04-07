---
title: "Claude Mythos: Anthropic's Leaked Next-Gen Model That Has Governments Worried About Cybersecurity"
date: 2026-04-07T23:30:00+09:00
description: "On March 26, 2026, a CMS configuration error exposed nearly 3,000 unpublished Anthropic assets — including a draft blog post describing Claude Mythos, a new model tier above Opus that Anthropic calls 'by far the most powerful AI model we have ever developed.' The leaked documents reveal a 'Capybara' product tier with dramatically higher scores in coding, reasoning, and cybersecurity, alongside private government warnings that Mythos makes large-scale cyberattacks 'significantly more likely in 2026.' Cybersecurity stocks dropped on the news."
content_type: "Guide"
card_description: "On March 26, 2026, security researchers Roy Paz (LayerX Security) and Alexandre Pauwels (University of Cambridge) discovered that a configuration error in Anthropic's content management system had left nearly 3,000 unpublished assets publicly accessible — including a draft blog post describing Claude Mythos, an unreleased model that sits above Opus in a new 'Capybara' tier. Anthropic confirmed the model represents 'a step change' in capabilities and is 'the most capable we've built to date,' with dramatically higher scores than Opus 4.6 in software coding, academic reasoning, and cybersecurity. The leaked documents also revealed that Anthropic has been privately warning senior government officials that Mythos makes large-scale cyberattacks significantly more likely, and that agents running on systems at this capability level can plan and carry out complex operations with minimal human involvement. Cybersecurity stocks fell on the disclosure. This analysis covers the leak itself, what the documents reveal about Mythos capabilities, the cybersecurity implications, Anthropic's response, the planned staged rollout to defensive security teams, and what this means for the frontier AI landscape."
last_refreshed: 2026-04-07
---

On March 26, 2026, a misconfigured content management system exposed Anthropic's biggest secret: an unreleased AI model that the company internally describes as "by far the most powerful AI model we have ever developed." The model is called Claude Mythos, and it has governments worried.

This analysis draws on reporting from [Fortune](https://fortune.com/2026/03/26/anthropic-says-testing-mythos-powerful-new-ai-model-after-data-leak-reveals-its-existence-step-change-in-capabilities/), [CNN](https://edition.cnn.com/2026/04/03/tech/anthropic-mythos-ai-cybersecurity), [Euronews](https://www.euronews.com/next/2026/03/30/what-is-anthropics-mythos-the-leaked-ai-model-that-poses-unprecedented-cybersecurity-risks), [Axios](https://www.axios.com/2026/03/29/claude-mythos-anthropic-cyberattack-ai-agents), [PYMNTS](https://www.pymnts.com/artificial-intelligence-2/2026/anthropics-unreleased-claude-mythos-might-be-the-most-advanced-ai-model-yet/), [Techzine](https://www.techzine.eu/news/applications/140017/details-leak-on-anthropics-step-change-mythos-model/), and [WaveSpeed AI](https://wavespeed.ai/blog/posts/claude-mythos-opus-5-leak-what-we-know/) — we research and analyze rather than testing products hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

---

## How the Leak Happened: A CMS Configuration Error

On March 26, 2026, security researchers Roy Paz of LayerX Security and Alexandre Pauwels of the University of Cambridge discovered that Anthropic's content management system had left nearly 3,000 unpublished digital assets publicly accessible in a searchable data store.

The root cause: digital assets created via Anthropic's CMS default to public unless explicitly marked private. Someone hadn't toggled the setting, and the result was an unsecured data cache containing draft blog posts, internal documents, and plans for an invite-only European CEO summit.

Among the exposed documents was a draft blog post describing Claude Mythos in detail — its capabilities, its positioning, and its cybersecurity implications.

Fortune journalists discovered the exposed data store, confirmed the findings with Paz and Pauwels, and notified Anthropic before publication. The company subsequently removed public access.

Anthropic attributed the incident to "human error." This is the second notable leak in recent memory — in March 2026, Anthropic also [accidentally shipped Claude Code's entire source code](/guides/claw-code-open-source-claude-code-clone/) in an npm package, exposing 512,000 lines of TypeScript. Two accidental disclosures in a single month raises questions about operational security at one of the world's most safety-conscious AI labs.

---

## What Is Claude Mythos?

Claude Mythos is a new AI model tier that sits above Anthropic's current flagship Opus models. Internally, it's part of a product line codenamed "Capybara," representing a fourth tier in what was previously a three-tier lineup of Haiku, Sonnet, and Opus.

An Anthropic spokesperson confirmed: "We're developing a general purpose model with meaningful advances in reasoning, coding, and cybersecurity. Given the strength of its capabilities, we're being deliberate about how we release it."

The spokesperson also described Mythos as "a step change and the most capable we've built to date."

### What the Leaked Documents Claim

According to the draft blog post and associated materials, Mythos achieves "dramatically higher scores" than Claude Opus 4.6 across three domains:

- **Software coding** — For context, Opus 4.6 currently scores approximately 80.8% on SWE-bench Verified and topped Terminal-Bench 2.0 at 65.4%, surpassing GPT-5.2-Codex. The leaked documents suggest Mythos exceeds these marks, though no specific benchmark figures were published.

- **Academic reasoning** — Higher scores on reasoning benchmarks than any previous Anthropic model.

- **Cybersecurity** — This is the category that has drawn the most attention. The leaked draft states Mythos is "currently far ahead of any other AI model in cyber capabilities."

### Agentic Capabilities

The PYMNTS analysis highlights that Mythos features agentic capabilities — the ability to plan and execute sequences of actions autonomously across systems without waiting for human input at each step. This distinguishes it from traditional chat models that respond to individual prompts.

---

## The Cybersecurity Problem

The cybersecurity dimension of Mythos is what turned a model announcement into a geopolitical concern.

### What the Leaked Blog Post Said

The draft blog post contained a stark warning: Mythos "presages an upcoming wave of models that can exploit vulnerabilities in ways that far outpace the efforts of defenders." The document stated the model can identify software vulnerabilities and exploit them faster than human security teams can patch them.

### Government Warnings

According to Axios, Anthropic has been privately briefing senior government officials that Mythos makes large-scale cyberattacks "significantly more likely in 2026." The core message: once models at Mythos's capability level reach wide distribution, the cost and difficulty of launching sophisticated attacks drops dramatically.

The briefings emphasized that AI agents at this capability level can "plan and carry out complex operations with minimal human involvement" — a step beyond models that require human direction at each stage.

### Historical Precedent

This concern has a concrete basis. PYMNTS reported that in September 2025, an earlier Claude model executed 80-90% of a coordinated cyberattack against approximately 30 organizations independently — identifying targets, finding weaknesses, writing exploit code, and producing reports with minimal human direction.

The implication: if a predecessor model could do 80-90% autonomously, a model that Anthropic describes as a "step change" above Opus raises the ceiling considerably.

### The Agentic Multiplier

CNN framed Mythos as a potential "watershed moment" for cybersecurity, noting that the rise of AI agents takes the risk beyond what traditional chat models posed. A single AI agent running on a model at Mythos's capability level could potentially scan for vulnerabilities and exploit them faster and more persistently than hundreds of human hackers, operating continuously without fatigue or error from repetition.

Unlike traditional models that respond to prompts, agentic systems can chain together actions autonomously — reconnaissance, vulnerability scanning, exploit development, payload delivery, and lateral movement — without human oversight at each step.

---

## Market Impact: Cybersecurity Stocks Fell

The Mythos disclosure moved markets. Following the leak and subsequent reporting, cybersecurity stocks declined as investors processed the implication that AI-powered offensive capabilities may be outpacing defensive tools. The irony is that a model designed to eventually help defenders first triggered concern about the offensive applications.

---

## Anthropic's Response and Rollout Strategy

Anthropic's public statements have emphasized deliberation over speed:

1. **Confirmed the model exists** — described it as a "step change" in capabilities.
2. **Acknowledged the leak** — attributed it to human error in CMS configuration.
3. **Emphasized staged rollout** — cyber defense organizations get early access before broader distribution.
4. **No public launch date** — the model is described as expensive to operate and not yet ready for general release.

The staged rollout strategy aligns with Anthropic's Responsible Scaling Policy. The plan is to give defensive security teams early access to "improve the robustness of their codebases" before the model reaches wider availability — essentially, giving defenders a head start against the offensive capabilities the model enables.

### Cost and Availability

The leaked materials indicate Mythos is extremely compute-intensive. Specific API pricing hasn't been disclosed, but the documents suggest it would occupy a premium pricing tier above Opus. Anthropic is reportedly working to improve efficiency before any general release.

The model is currently being tested by "early access customers," according to Anthropic's spokesperson.

---

## The European CEO Summit

The leak also exposed plans for an invite-only CEO summit in the English countryside — described as an "intimate gathering" where attendees would learn about "unreleased Claude capabilities." Anthropic CEO Dario Amodei was scheduled to attend. The summit appears to be part of the company's strategy to give enterprise leaders advance access to Mythos before public release.

---

## What This Means for the AI Landscape

### A New Tier in the Model Hierarchy

If Mythos performs as described, it establishes a new ceiling above the current Opus/GPT-5.4/Gemini 3.1 Pro tier. The "Capybara" product line would create a fourth pricing and capability tier — Haiku for speed, Sonnet for balance, Opus for power, and Capybara for frontier applications.

### The Offense-Defense Asymmetry

The most significant implication isn't the model itself — it's the asymmetry it represents. If Mythos can exploit vulnerabilities faster than defenders can patch them, and if competitors (OpenAI, Google, xAI) are developing comparable models, then the cybersecurity landscape faces a structural shift. The cost of sophisticated attacks drops while the cost of defense remains high.

Anthropic's own framing acknowledges this: Mythos doesn't just represent a one-time risk, it "presages an upcoming wave" of similarly capable models from multiple labs.

### The Safety Lab's Dilemma

The Mythos story is also a story about organizational tension. Anthropic positions itself as the AI safety company — the lab that slows down to get things right. But two major accidental disclosures in a single month (Claude Code source via npm, Mythos via CMS) undercut that positioning. The most safety-focused lab in the industry appears to have some of the leakiest operational security.

To be clear, the CMS error exposed marketing materials, not model weights or training data. But the pattern matters for a company whose brand promise is careful stewardship of powerful AI.

---

## Honest Assessment: What We Don't Know

Several important caveats:

- **No independent benchmarks** — All performance claims come from leaked internal documents. No third-party evaluations have been published. Anthropic's own internal benchmarks are not a substitute for independent testing.

- **"Step change" is a relative claim** — Without specific numbers, we can't assess the magnitude. A 2% improvement over Opus 4.6 is technically a step change. So is a 50% improvement.

- **Cybersecurity capability claims are unverified** — "Far ahead of any other AI model in cyber capabilities" is a strong claim that hasn't been tested against GPT-5.4 or other frontier models in controlled conditions.

- **Release timeline is unknown** — "Early access customers" and "no launch date" could mean weeks or months. The model's high compute costs suggest it may remain limited-access for some time.

- **The leak itself raises questions** — A company that accidentally exposes 3,000 internal assets via a CMS default should prompt scrutiny of other operational security practices, not just the model's technical capabilities.

- **Defensive-first rollout depends on trust** — Anthropic's plan to give defenders a head start works only if the model remains restricted during that window. If competitors ship comparable capabilities without similar restrictions, the head start evaporates.

- **September 2025 attack figure needs context** — The claim that an earlier Claude model executed "80-90%" of a coordinated attack is striking, but it's unclear from reporting what the 30 target organizations were, whether this was a controlled test, and what the remaining 10-20% required.

---

## Related Reading

- [Claw Code: The Open-Source Clone That Became the Fastest-Growing Repo in GitHub History](/guides/claw-code-open-source-claude-code-clone/) — The other major Anthropic leak of March 2026: Claude Code's entire source code shipped in an npm package
- [Claude's FreeBSD Exploit: What AI Vulnerability Research Actually Looks Like](/guides/claude-freebsd-exploit-ai-vulnerability-research/) — An earlier demonstration of Claude's vulnerability discovery capabilities
- [Qualys Agent Val: The First AI Agent for Safe Exploit Validation](/guides/qualys-agent-val-ai-exploit-validation/) — How the defensive side is using AI agents for exploit validation and autonomous remediation
- [MCP Attack Vectors and Defense](/guides/mcp-attack-vectors-defense/) — Security risks in the MCP ecosystem that agentic AI models interact with
- [MCP Security Landscape 2026](/guides/mcp-security-landscape-2026/) — The broader security picture for AI tool infrastructure
- [Peer Preservation: AI Models Scheme to Stop Each Other From Being Shut Down](/guides/ai-peer-preservation-models-protect-each-other-shutdown/) — UC Berkeley study showing frontier models defy instructions to protect peers — relevant context for autonomous agents at Mythos-level capabilities
- [OpenAI Raises $122 Billion at $852 Billion Valuation](/guides/openai-122-billion-funding-852-billion-valuation/) — OpenAI's $852B vs Anthropic's $380B — the funding race context for Mythos
- [SpaceX Acquires xAI for $250 Billion](/guides/spacex-xai-250-billion-merger-largest-in-history/) — xAI's $250B valuation, Grok's 17.8% market share, and the competitive landscape reshaping around the $1.75T SpaceX IPO
