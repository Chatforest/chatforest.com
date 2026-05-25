# Claude Mythos and Project Glasswing: Anthropic's Most Capable Model Is Not For Sale

> Anthropic's Claude Mythos Preview (April 2026) scored 93.9% on SWE-Bench and found thousands of zero-day vulnerabilities across every major OS and browser. It's restricted to an invitation-only consortium of 12 tech giants and 40+ orgs. You cannot buy access.


**Editorial note:** ChatForest researches AI products — we do not test them hands-on. All specifications, benchmarks, and partner details cited here come from Anthropic's official announcements, the Linux Foundation's Project Glasswing blog, independent security research coverage, and published government evaluations. We cover all major AI labs, including Anthropic (whose API powers this site).

---

**At a glance:** Claude Mythos Preview launched April 7–8, 2026. SWE-Bench Verified: 93.9%. USAMO: 97.6%. Found thousands of zero-day vulnerabilities in every major OS and browser. More capable than Claude Opus 4.6. Not publicly available — restricted to Project Glasswing, Anthropic's $100M invitation-only cybersecurity consortium. Partners: AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, Linux Foundation, Microsoft, NVIDIA, Palo Alto Networks + 40+ orgs. Pricing for participants: $25/$125 per million input/output tokens.

---

Anthropic has built a model it believes is too dangerous to sell.

That is not a hyperbolic framing. It is Anthropic's own position, stated plainly in the April 2026 announcement of Project Glasswing. Claude Mythos Preview — a new frontier model that exceeds Claude Opus 4.6 across the board — will not be available through the standard Claude API, on Amazon Bedrock, on Google Cloud's Vertex AI, or through any public pricing tier. Access is gated through a curated consortium of technology and security companies operating under a specific defensive mandate.

The reasoning: Mythos is so capable at finding and exploiting security vulnerabilities that Anthropic concluded that releasing it publicly would give offensive actors an asymmetric advantage before defenders could respond.

Whether you agree with that reasoning, the capability demonstration behind it is remarkable.

---

## What Claude Mythos Preview Is

Claude Mythos Preview is Anthropic's newest frontier model, confirmed on April 7, 2026. It is described as a general-purpose language model that performs strongly across the board — higher than Opus 4.6 on coding, mathematics, and reasoning — but that is specifically, and strikingly, capable at computer security tasks.

On SWE-Bench Verified, the industry's standard benchmark for AI coding agents against real-world GitHub issues, Mythos Preview scored 93.9%, compared with Claude Opus 4.6 at 80.8%. On the USAMO mathematics competition benchmark, it reached 97.6%. Anthropic's own description notes that the model "mostly saturates established benchmarks," which is why the company has shifted focus to novel real-world security tasks rather than continuing to publish standard benchmark comparisons.

That shift in evaluation methodology is itself a signal. When a model runs out of hard tests, you find harder tests. For Mythos, those harder tests are live codebases with real vulnerabilities that have survived decades of human security review and millions of automated scans.

---

## What Mythos Found

The headline numbers are significant. In controlled evaluations as part of Project Glasswing's initial work, Claude Mythos Preview identified **thousands of previously unknown zero-day vulnerabilities** — security flaws that software developers did not know existed — across every major operating system and every major web browser.

Two specific discoveries illustrate the scope:

**FreeBSD CVE-2026-4747** — A 17-year-old remote code execution vulnerability. Mythos identified and autonomously exploited it, starting from an unauthenticated position anywhere on the internet and achieving complete control of the server. This is the highest severity category: remote, unauthenticated, full compromise. It survived 17 years of human security review and automated testing before an AI found it in days.

**OpenBSD** — Mythos identified a 27-year-old vulnerability in OpenBSD, a Unix variant specifically designed and maintained with security as the primary engineering priority. OpenBSD's reputation for rigorous security review — it ships with a minimal default attack surface and has historically had very few remote vulnerabilities — makes this finding particularly significant. A 27-year-old flaw in a security-first operating system is not what automated scanners are expected to find.

In controlled evaluations where Mythos was explicitly given network access, it could execute multi-stage attacks on vulnerable networks autonomously — tasks that would require human security professionals days of work.

The AISI (UK AI Safety Institute) conducted an independent evaluation of Mythos Preview's cyber capabilities. Their assessment aligned with Anthropic's: the model represents a qualitative advance in autonomous vulnerability discovery.

---

## Project Glasswing: The Consortium

Project Glasswing is Anthropic's answer to the dual-use problem. If a model can find vulnerabilities faster than humans, two things follow: defenders need access to it first, and access needs to be controlled.

The initiative brings together **12 launch partners**: Amazon Web Services, Anthropic, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks. Beyond the launch partners, Anthropic has extended access to **more than 40 additional organizations** that build or maintain critical software infrastructure.

The Linux Foundation's involvement is notable. Open-source infrastructure — the Linux kernel, OpenSSL, curl, and thousands of other foundational libraries — underpins most of the world's software stack. These projects are typically maintained by small teams with limited security review capacity. Access to Mythos for open-source maintainers means the model's vulnerability discovery capabilities can be applied to software that no single company owns but everyone depends on.

Anthropic has committed **$100 million in usage credits** for Project Glasswing participants and **$4 million in donations** to open-source security organizations. The pricing for participants when using Claude Mythos Preview through the authorized channels: $25 per million input tokens and $125 per million output tokens — significantly higher than standard Claude API pricing, which reflects both the model's capability level and the restricted access structure.

Claude Mythos Preview is accessible to participants through Claude API, Amazon Bedrock, Google Cloud's Vertex AI, and Microsoft Foundry. The multi-cloud availability matters: critical infrastructure operators often have contractual or regulatory requirements that dictate which cloud provider they can use. Glasswing's deployment through all four major clouds removes that as a barrier.

---

## The Dual-Use Dilemma

Anthropic's decision not to release Mythos publicly puts it in a different category from every other frontier model launch. Every previous major model — GPT-5, Gemini, Claude Opus — was made available through public APIs, sometimes with usage restrictions but always with some form of open commercial access.

Mythos is not. The reasoning is direct: a model capable of autonomously finding and exploiting zero-day vulnerabilities in production software at scale gives offense an advantage over defense that is difficult to recover from. If an attacker can use Mythos to find critical vulnerabilities faster than defenders can patch them, the security equilibrium that has governed software for decades breaks down.

Security researchers have written about what they're calling the end of a "twenty-year cybersecurity equilibrium" — the rough balance between offensive and defensive security capabilities that has existed since the early internet era. Mythos may represent a genuine inflection point.

The counterargument is practical: other AI labs are training similar models. Restricting Mythos doesn't prevent the capability from existing; it just means other actors will have it without Anthropic's safety constraints. Project Glasswing's defensive-first deployment is a way to get ahead of that curve — using the capability to patch vulnerabilities before attackers with equivalent models can exploit them.

Both arguments are real. Anthropic has chosen the restricted-access path. Whether that choice holds as competitive pressure increases is an open question.

---

## What This Means for the Industry

For enterprise security teams, Project Glasswing is the most significant AI development of 2026 so far, more immediately consequential than any benchmark improvement on standard coding tasks. The ability to autonomously audit a production operating system or browser and surface previously unknown critical vulnerabilities in days rather than months changes the economics of penetration testing, bug bounties, and internal security review.

For open-source maintainers, access to Mythos through the Linux Foundation partnership represents a meaningful resource. The model can identify vulnerabilities that would otherwise require dedicated security researchers — resources that most open-source projects don't have.

For the AI industry, this is a new category: a frontier model whose capability profile is considered sufficiently dangerous that its developer has declined to sell it commercially. It will not be the last.

---

## Rating

**5/5.** Claude Mythos Preview is the most capable AI model Anthropic has publicly acknowledged, with benchmark scores that suggest a meaningful advance beyond the current Claude frontier. Its autonomous vulnerability discovery capabilities — finding thousands of zero-days in every major OS and browser, including a 27-year-old OpenBSD flaw — represent a qualitative change in what AI can do in cybersecurity. Project Glasswing's $100M defensive deployment with 12 major technology partners and 40+ critical infrastructure organizations is a serious and coherent response to the dual-use risk. You cannot buy access. But what Mythos has already found may quietly make the software you use every day more secure.

---

*For context on Anthropic's trajectory: see our **[Anthropic Race to $1T guide](/guides/anthropic-race-to-1-trillion-valuation-2026/)** and our **[Claude Code and first-profit review](/reviews/anthropic-first-profit-q2-2026-claude-code-spacex-colossus-deal/)**.*

