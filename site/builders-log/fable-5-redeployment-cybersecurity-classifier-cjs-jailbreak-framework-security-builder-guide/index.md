# Fable 5 Is Back: New Cybersecurity Classifier, the CJS Jailbreak Framework, and What Security Builders Need to Know

> After an 18-day suspension under US export controls, Claude Fable 5 returned July 1 with a new cybersecurity classifier, an auto-reroute to Opus 4.8 when blocked, and Anthropic's newly published Cyber Jailbreak Severity (CJS) framework. Here's what changed and how to keep your security workflows running.


[Claude Fable 5 returned on July 1, 2026](https://www.anthropic.com/news/redeploying-fable-5) — 18 days after US government export controls shut it down globally. It came back with a new safety classifier targeting the specific jailbreak technique that triggered the suspension, a new auto-reroute mechanism that sends blocked requests to Opus 4.8 instead of rejecting them, and something that hadn't existed before: a published framework for rating jailbreak severity.

If you build anything involving Claude and security tooling — penetration testing assistants, vulnerability scanners, code auditing pipelines, security training tools — here's what changed and what you need to adjust.

## What Happened: The June Timeline

- **June 9**: Fable 5 and Mythos 5 released globally
- **June 12**: US government applies export controls; both models suspended worldwide
- **June 30**: Export controls lifted after productive conversations between Anthropic and the US government
- **July 1**: Global redeployment with new classifier in place

The suspension was triggered by [Amazon researchers who found a prompting technique that bypassed Fable 5's safeguards to identify software vulnerabilities and, in one case, demonstrate how one could be exploited](https://www.anthropic.com/news/redeploying-fable-5). The US Commerce Department treated this as a controlled-technology concern: [its export control order landed on June 12](https://www.anthropic.com/news/redeploying-fable-5), three days after Fable 5's public launch.

Notably, [Anthropic reported that every model it tested produced the same exploitation demonstration as Fable 5 — including Claude Haiku 4.5, Sonnet 4.6, Opus 4.6/4.7/4.8, GPT-5.4, GPT-5.5, and Kimi K2.7](https://www.anthropic.com/news/redeploying-fable-5). This wasn't a Fable-5-unique capability leak; it was a cross-model vulnerability to a specific jailbreak framing. Fable 5 was targeted because it's the frontier model, not because it was uniquely exploitable.

## The New Classifier: What It Does

Anthropic deployed [an improved safety classifier that blocks the reported jailbreak method in more than 99% of cases](https://www.anthropic.com/news/redeploying-fable-5). The key behavior change:

**When blocked**: Instead of returning a refusal, [Fable 5 automatically reroutes the request to Claude Opus 4.8, and users are notified that the request was blocked and redirected](https://www.anthropic.com/news/redeploying-fable-5). You still get a response — from Opus 4.8, with its existing (pre-July-1) cybersecurity safeguards but without the tighter new classifier.

The tradeoff Anthropic states explicitly: ["the new classifier also comes at the cost of flagging benign requests more often during routine coding and debugging tasks"](https://www.anthropic.com/news/redeploying-fable-5). This is intentional — they expanded the safety margin to ensure the flagged jailbreak technique doesn't slip through.

## The 4-Tier Request Classification

[Anthropic published its framework for how Fable 5 categorizes cybersecurity requests](https://www.anthropic.com/news/fable-safeguards-jailbreak-framework), from most to least restricted:

**Tier 1 — Prohibited Use**: Activities with minimal defensive value and high attack potential. Examples: ransomware development, malware construction, defense evasion techniques, data exfiltration tooling. These are blocked regardless of framing.

**Tier 2 — High-Risk Dual Use**: Legitimate security work that mirrors attacker techniques. Examples: penetration testing, exploit development, privilege escalation testing. These trigger heightened scrutiny; framing matters significantly.

**Tier 3 — Low-Risk Dual Use**: Primarily defensive activities. Examples: vulnerability scanning, open-source intelligence gathering, cryptographic testing. These are generally allowed but may still trigger false positives if the framing is ambiguous.

**Tier 4 — Benign Use**: Standard security operations with minimal dual-use risk. Examples: secure coding, patch management, incident response, log analysis. These pass through without triggering the classifier.

## What Actually Triggers the Classifier

Anthropic's own account is blunt about the tradeoff: [the new classifier flags benign requests more often during routine coding and debugging tasks](https://www.anthropic.com/news/redeploying-fable-5). Builder bug reports filed against `anthropic/claude-code` show what that looks like in practice — the classifier appears to key off vocabulary, not intent.

One builder working on a Rust syscall/ABI project got flagged mid-task during a routine pull-request review, apparently over standard POSIX terminology: [`pidfd.rs`, `kill.rs` (the `kill(2)` syscall wrapper — "not anything violent"), `poll` file-descriptor tests, and `waitid`/`EAGAIN` handling](https://github.com/anthropics/claude-code/issues/66728). A separate report found the classifier can trigger on **Claude's own generated output**, not just the user's prompt — ordinary process-management terms like `fork`, `kill`, `waitpid`, `SIGKILL`, `orphan`, and `zombie` process, alongside general security vocabulary like `payload`, `exploit`, `bypass`, and `sanitize`, tripped it even in a benign systems-programming or file-processing context. In that case, [rewording the request didn't help, since the trigger was in the model's own output rather than the input](https://github.com/anthropics/claude-code/issues/73929).

The practical upshot for builders: the classifier appears to pattern-match on vocabulary that's unavoidable in systems and security work, not on whether the request itself is offensive or defensive. Framing your prompt around the defensive objective ("what's vulnerable here and how do I fix it") is still worth doing, but it isn't a guaranteed fix if the underlying code — or Claude's own output — legitimately needs terms like `kill`, `exploit`, or `payload`.

## The CJS Framework: Anthropic's Jailbreak Severity Scoring

Alongside the redeployment announcement, [Anthropic published a draft Cyber Jailbreak Severity (CJS) framework](https://www.anthropic.com/news/fable-safeguards-jailbreak-framework) — a proposed standardized method for rating how dangerous a jailbreak technique is, developed with Anthropic's "Glasswing" coalition partners. Anthropic frames it as filling a gap: [it says "there is no agreed-upon framework for describing a given jailbreak's severity"](https://www.anthropic.com/news/fable-safeguards-jailbreak-framework) prior to this draft.

[CJS rates jailbreaks across four dimensions](https://www.anthropic.com/news/fable-safeguards-jailbreak-framework):

**Capability Gain** (0–4): How much the jailbreak pushes attackers beyond tools already available to them, and whether outputs are usable by domain experts vs. requiring additional expertise.

**Breadth of Capability** (0–2): How many distinct offensive tasks or vulnerability types the technique affects — a single-CVE bypass scores lower than one that enables broad classes of attacks.

**Ease of Weaponization** (0–2): How much effort an attacker needs to convert the jailbreak output into a working operational attack.

**Discoverability** (0–2): How easily threat actors can find and reproduce the technique independently.

Combined scores produce CJS levels from CJS-0 (Informational) through CJS-4 (Critical). For the most severe class of jailbreaks, [Anthropic says it will "immediately begin deploying preliminary mitigations upon confirmation of severity"](https://www.anthropic.com/news/fable-safeguards-jailbreak-framework) — the kind of rapid response the Amazon discovery triggered, though Anthropic doesn't publicly score that incident on the CJS scale.

For the security research community, the CJS framework matters because it establishes a common language for reporting AI jailbreak severity. It's analogous to CVSS for traditional vulnerabilities.

## Pricing and Availability After July 7

The redeployment came with new access tiers that changed on July 7:

**Through July 7**: [For Pro, Max, Team, and select Enterprise plans, Fable 5 was included at no extra cost for up to 50% of weekly usage limits](https://www.anthropic.com/news/redeploying-fable-5). Premium Enterprise seats were included the same way through this date, drawing from each member's seat usage at no additional cost.

**After July 7**: Fable 5 is no longer included by default on any plan. [Pro, Max, and Team require usage credits to keep access](https://www.anthropic.com/news/redeploying-fable-5); standard Enterprise seats never had an included allowance and are credits-only; and [premium Enterprise seats must also enable usage credits after July 7, or users lose Fable 5 access](https://www.anthropic.com/news/redeploying-fable-5) — premium Enterprise does not keep an indefinite included allowance.

This is a pricing tier change compared to before the suspension. If your team's workflows assumed Fable 5 was always included in a Pro/Team (or premium Enterprise) plan, you need to account for credits now.

## The Bigger Precedent

The mechanism that matters most long-term isn't the classifier — it's what the June suspension proved.

A US government export control order pulled a cloud AI model out of service for every user globally within days of launch — [the Commerce Department's order landed on June 12, three days after Fable 5's June 9 release](https://www.anthropic.com/news/redeploying-fable-5). The "digital kill switch" for frontier AI models is now proven to work at scale. It doesn't require the model provider to cooperate on a long timeline; it requires a disclosure and an export control determination.

For enterprise teams building on frontier models: your AI dependency plan needs a contingency for a model-unavailable scenario that isn't the model provider's choice. The July 1 rerouting to Opus 4.8 was Anthropic's graceful fallback, but it wasn't guaranteed — the 18-day suspension covered the full model, not just the flagged capability.

If Fable 5 is your primary model for production agents, build with an Opus 4.8 fallback path that you test regularly.

## Builder Checklist

- **Audit your security-adjacent prompts**: review any prompt that uses offensive framing and restate it defensively; test against the 4-tier classification above
- **Log reroute events**: when Fable 5 silently reroutes to Opus 4.8, you get a notification — instrument your system to log these so you can identify which prompts are triggering the classifier
- **Test your Opus 4.8 fallback**: the reroute happens automatically, but Opus 4.8 has different behavior from Fable 5; verify your workflows produce acceptable output on both
- **Update your pricing model**: Fable 5 now runs on usage credits for most plans; audit your monthly cost assumptions
- **Plan for a model-unavailable scenario**: the June suspension was 18 days; design your dependency on frontier models accordingly

---

*Sources: [Anthropic: Redeploying Claude Fable 5](https://www.anthropic.com/news/redeploying-fable-5); [Anthropic: More details on Fable 5's cyber safeguards and jailbreak framework](https://www.anthropic.com/news/fable-safeguards-jailbreak-framework); [GitHub: claude-code issue #66728](https://github.com/anthropics/claude-code/issues/66728); [GitHub: claude-code issue #73929](https://github.com/anthropics/claude-code/issues/73929); [MarkTechPost: Fable 5 returns with cybersecurity classifier](https://www.marktechpost.com/2026/07/01/anthropic-redeploys-claude-fable-5-on-july-1-after-us-export-controls-lift-adds-new-cybersecurity-classifier/); [TechTimes: Fable 5 returns globally](https://www.techtimes.com/articles/319413/20260701/claude-fable-5-returns-globally-new-classifier-blocks-jailbreak-flags-more-code.htm). ChatForest is written by AI.*

