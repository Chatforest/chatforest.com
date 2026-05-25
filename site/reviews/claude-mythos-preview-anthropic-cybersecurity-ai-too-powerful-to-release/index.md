# Claude Mythos Preview — The AI Anthropic Built But Won't Release

> Claude Mythos Preview (April 7, 2026) scores 93.9% on SWE-bench and found thousands of zero-day vulnerabilities across every major OS and browser. Anthropic decided not to release it publicly. Here's what it does, who can access it via Project Glasswing, and what it means for AI safety.


**Editorial note:** Claude Mythos Preview is not publicly available and ChatForest does not have access to it. This article is based on Anthropic's published system card, AISI evaluation reports, reporting from TechCrunch, The Next Web, Dark Reading, Scientific American, and NBC News, and publicly available benchmark data. We do not claim hands-on testing of this model.

---

**At a glance:** Claude Mythos Preview. Launched April 7, 2026. Not publicly available. Access via Project Glasswing (invitation-only, ~50 organizations). Part of our **[AI Tools & Companies reviews](/categories/ai-tools/)**.

---

On April 7, 2026, Anthropic launched a new AI model. Then they declined to release it.

This is the first time a major AI lab has publicly stated that a model was too capable for general availability. The model is Claude Mythos Preview. The decision not to release it is, in its own way, more significant than the model itself.

---

## What Mythos Can Do

Claude Mythos Preview is a new model class built for three areas: cybersecurity, autonomous software engineering, and long-running agentic tasks.

The benchmark numbers establish the baseline:

| Benchmark | Score |
|-----------|-------|
| SWE-bench Verified | 93.9% |
| SWE-bench Pro | 77.8% |
| Terminal-Bench 2.0 | 82.0% |
| USAMO 2026 | 97.6% |

SWE-bench Verified measures autonomous performance on real-world software engineering tasks — fixing bugs, implementing features, navigating unfamiliar codebases. A score of 93.9% represents near-complete autonomous capability on well-specified tasks. That is not the alarming part.

The alarming part is the cybersecurity capability.

---

## The Vulnerability Discovery Numbers

Anthropic used Mythos Preview to conduct what amounts to the most aggressive automated vulnerability discovery program ever run on production software:

- **271 vulnerabilities discovered in Mozilla's Firefox**, with exploits developed for 181 of them
- **Thousands of zero-day vulnerabilities** across every major operating system and every major web browser
- **A 17-year-old remote code execution vulnerability in FreeBSD** — fully autonomously identified and exploited, allowing anyone to gain root access on a machine running NFS

Zero-day vulnerabilities are security flaws unknown to the software's developers. Finding one is significant. Finding thousands, autonomously, across the entire software ecosystem, in weeks, is unprecedented.

As of publication, over 99% of those findings remain unpatched.

---

## The AISI Evaluation

The UK's AI Security Institute (AISI) conducted an independent evaluation of Mythos Preview's cybersecurity capabilities. Key findings:

**On expert-level attack tasks** — tasks that no AI model could complete before April 2025 — Mythos Preview succeeded **73% of the time**. Twelve months ago, the success rate was zero.

**On AISI's 32-step corporate network attack simulation** — a multi-stage test of autonomous cyberattack capability — Mythos Preview completed the full simulation in **3 of 10 attempts**. GPT-5.5, OpenAI's comparable frontier model, completed it in **2 of 10 attempts**.

The AISI framing: Mythos represents a step-change in cyber capability, in a landscape where cyber performance was already improving rapidly. The 73% expert-task rate is not just an improvement over prior models. It's a different category of capability.

---

## Why Anthropic Won't Release It

Anthropic's system card states: "Claude Mythos Preview's large increase in capabilities has led us to decide not to make it generally available."

The core problem is dual use. The same capability that allows Mythos to autonomously discover and exploit vulnerabilities for defensive purposes — auditing software before attackers find it — can be used offensively. An attacker with access to Mythos and a target has a fundamentally different toolkit than any attacker in history.

The theory behind restricted access is sequencing: give defenders a preparation window. If Mythos finds thousands of zero-days and security teams can patch them before the same capability is widely distributed, net security improves. If Mythos is released publicly before those patches land, the opposite happens.

Whether that sequencing logic actually holds — whether patches will land at scale before similar models are developed by others or leaked — is the central open question in the AI security community's response to Mythos.

---

## Project Glasswing

Access to Mythos Preview runs through Project Glasswing, Anthropic's controlled release program. Approximately 50 organizations have access:

**12 founding partners** — AWS, Apple, Cisco, CrowdStrike, Google, JPMorgan Chase, the Linux Foundation, Microsoft, NVIDIA, Palo Alto Networks (and two others not publicly named).

**40+ additional organizations** that build or maintain critical software infrastructure.

The partner list is notable. AWS, Google, and Microsoft are Anthropic's primary cloud distribution partners. Apple and NVIDIA are platform infrastructure. Cisco, CrowdStrike, and Palo Alto Networks are the major enterprise security vendors. The Linux Foundation maintains the open-source infrastructure most of the internet runs on. JPMorgan Chase represents the financial sector.

This is not a beta release program. It is a coordinated defensive deployment across the organizations with the most to lose if Mythos-class capabilities fall into adversarial hands — and the most capability to act on what Mythos finds.

---

## The Unauthorized Access Incident

On April 7, 2026 — the same day Anthropic announced Mythos — a group of unauthorized users gained access to it.

The method: a private Discord channel of researchers who hunt for access to unreleased AI models guessed the model's API URL based on Anthropic's established URL naming conventions for other models. A third-party contractor credential provided an additional access path.

Anthropic stated it was investigating and found no evidence of system impact. The incident lasted hours before access was revoked.

The episode reveals a gap between intended access controls and actual controls. Project Glasswing is structured around invitation and vetting. The actual barrier was a guessable URL and a contractor credential. For a model whose central justification for restricted access is preventing dangerous capability from spreading, the unauthorized access on day one was an uncomfortable proof of concept about containment limits.

---

## The Legacy Banking Vulnerability Story

Among Mythos's findings, the most structurally significant may be in banking infrastructure.

COBOL-based core banking systems — many built in the 1970s and 1980s — power transaction processing at the world's largest financial institutions. Mythos used contextual reasoning to map the business logic of these systems and identify vulnerabilities that pattern-matching security tools had missed for decades:

- **Temporal race conditions**: 50-millisecond windows in batch processing that allow double-spending
- **Precision decay**: cumulative floating-point errors in long-dated derivatives
- **Shadow logic**: undocumented branching paths in credit scoring algorithms
- **API mismatch**: sanitization failures between modern JSON payloads and legacy fixed-width COBOL fields

The model also built a systemic risk map of inter-bank lending networks, identifying how a failure in one legacy module could cascade through SWIFT and ACH.

Bank of England Governor Andrew Bailey requested a meeting with Anthropic to discuss the findings. The Financial Stability Board followed up. These are the bodies responsible for global financial systemic risk. The fact that AI-discovered vulnerabilities in legacy banking code triggered meetings at that level signals how seriously the findings were taken.

---

## GPT-5.5 and the Dual-Frontier Problem

Mythos is not alone. OpenAI's GPT-5.5 also passed AISI's 32-step corporate network attack simulation (2 of 10 attempts vs. Mythos's 3 of 10). Both models represent capabilities that, in the AISI framing, cross a meaningful threshold in autonomous offensive cyber.

Anthropic has chosen not to release Mythos publicly. OpenAI has released GPT-5.5 with API access. The models are roughly comparable on the AISI simulation. The capability is now distributed — at least to anyone with an OpenAI API key.

This creates the "dual-frontier" problem that security researchers have been warning about: if one lab withholds a dangerous capability and another releases a comparable one, the net effect of the withholding may be minimal. The capability still enters the ecosystem. What changes is which lab's name appears on it.

Anthropic's answer, implicit in the Project Glasswing structure, is that the sequencing still matters — that getting defenders a preparation window of months, even if the capability becomes available through other means, is better than releasing everything simultaneously. Whether that calculation is correct is genuinely uncertain.

---

## What Mythos Means for AI Safety

There is a larger significance to the Mythos moment that goes beyond the specific capability numbers.

Anthropic has publicly stated that a model exceeded what it considers safe for general release. This is the first time any major AI lab has made this statement about a shipped model. It establishes a precedent and a vocabulary for the next threshold.

The implicit argument is that capability is not monotonically deployable — that there are levels of capability where the risks of open access outweigh the benefits, and where responsible development means building the capability, using it carefully for defensive purposes, and sequencing its release rather than shipping it.

That argument is contestable. The Project Glasswing partner list includes the world's largest technology companies and defense-adjacent security vendors — organizations with their own competitive interests in AI capability. "Responsible restricted access" and "competitive moat" can look similar from the outside.

But the alternative framing — that every capability should be released because someone else will develop it anyway — has its own problems. Mythos is a test of whether the AI industry can develop genuinely shared safety norms around frontier capability, or whether each lab will default to maximizing distribution and call it openness.

The AISI evaluation exists because the UK government negotiated model access before deployment. The Project Glasswing structure exists because Anthropic chose to build it. The banking vulnerability meetings exist because Mythos surfaced findings that the financial system's existing security infrastructure had not. None of these happened automatically. They required decisions.

---

## What to Watch

**Patch rates.** The 99% of Mythos's findings that remain unpatched is the most important number in this story. Whether the sequencing argument holds depends on whether defenders actually patch at scale during the preparation window.

**GPT-5.5 vs. Mythos capability trajectory.** Both models passed the AISI simulation. Which lab's next generation will be more capable, and by how much, will determine whether dual-frontier withholding remains viable as a strategy.

**Project Glasswing disclosures.** What the 50 Glasswing partner organizations have found with Mythos, and what they've patched, has not been systematically disclosed. Aggregate transparency here — how many vulnerabilities have been remediated, across which systems — would be significant.

**The unauthorized access follow-up.** Anthropic said it found no evidence of system impact. An external post-incident report on what access controls failed, and what was changed, would be worth reading.

**The next model.** Anthropic has not said when Mythos will become generally available, or whether it will be succeeded by a more capable model before that happens. The next decision point on the release question will reveal whether April 7 was a one-time exception or a policy.

---

*ChatForest covers AI tools, platforms, and infrastructure. This article is based on public reporting and official evaluation documents. ChatForest does not have access to Claude Mythos Preview and does not claim any hands-on assessment of the model's capabilities.*

