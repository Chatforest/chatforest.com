---
title: "The Federal-State AI Showdown: What Trump's Executive Order Actually Does to State AI Laws"
date: 2026-06-01
description: "EO 14365 (December 2025) directed three federal agencies to challenge state AI laws. Six months later: one stay, one Commerce report nobody has seen, and a compliance limbo every builder needs to understand. State laws still apply. Here is the full map."
og_description: "Trump's EO 14365 targets state AI laws via Commerce, FTC, and a DOJ Litigation Task Force. Six months later, only Colorado enforcement was stayed. State AI laws remain active. Builder compliance guide to the federal-state AI showdown."
content_type: "Builder's Log"
categories: ["AI Policy", "Compliance", "Regulation"]
tags: ["ai-regulation", "federal-preemption", "executive-order", "doj", "ftc", "commerce-department", "state-ai-laws", "compliance", "builder-guide", "colorado", "new-york", "illinois", "connecticut"]
---

There is a real legal tension between the Trump administration's push to override state AI laws and the growing stack of state legislation that passed or is about to pass. Builders are caught in the middle: the federal government says it wants to clear the field, but the field is still full.

This is the practical guide to what EO 14365 actually does, what has happened in the six months since it was signed, and what you need to do with state AI compliance right now.

The short answer: **state AI laws still apply.** Do not slow your compliance work waiting for federal preemption to materialize.

---

## What the Executive Order Actually Says

**EO 14365**, titled "Ensuring a National Policy Framework for Artificial Intelligence," was signed by President Trump on **December 11, 2025**.

The core theory is that fragmented state AI regulation threatens U.S. innovation and competitiveness. But the EO does not itself preempt state laws — it is not a self-executing preemption instrument. Instead, it directed three federal agencies to take specific actions by **March 11, 2026**:

| Agency | Directed Action | Deadline |
|--------|----------------|----------|
| Commerce | Evaluate "onerous" state AI laws; identify them | March 11, 2026 |
| FTC | Issue policy statement classifying state-mandated bias mitigation as a deceptive practice | March 11, 2026 |
| DOJ | Establish an AI Litigation Task Force to challenge state laws in federal court | January 10, 2026 |

Separately, on March 20, 2026, the White House released a **National Policy Framework for Artificial Intelligence** — a set of legislative recommendations to Congress calling for broad preemption of state AI laws. This is a Congressional ask, not a directive with legal force.

### What the EO Explicitly Does NOT Preempt

This is important: EO 14365 expressly **carves out** several categories from preemption pressure:

- State laws protecting **children's safety**
- State laws governing **AI compute and data center infrastructure**
- State **government AI procurement** rules
- Other areas to be determined

If your products are in these spaces, the EO's preemption pressure does not apply to those specific compliance areas.

---

## Six Months Later: What Has Actually Happened

### Commerce Department Evaluation

The Commerce Department submitted its evaluation of "onerous" state laws by the March 11 deadline — but **has not made it public** as of June 1, 2026. The report went to the White House, not to the public record. Analysts at Ropes & Gray and S&P Global describe the current state as "compliance limbo" precisely because this evaluation could trigger BEAD funding consequences for named states, but builders have no visibility into which states were flagged.

What we know: states analysts expect to be named include California, Colorado (pre-SB-189), and potentially Texas. We do not know if Illinois SB 315 or Connecticut's AIRT Act appear in the report.

### FTC Policy Statement

The FTC published its AI policy statement around March 11, 2026. It explains how Section 5 authority applies to AI and articulates the theory that state laws compelling model output alteration for bias mitigation could constitute a "deceptive trade practice" — because the altered outputs are less "truthful."

**What this does NOT do**: The FTC Act does not include an express preemption clause for state laws. The policy statement is interpretive. Courts have not accepted this framing. Law firm analysts including Tech Policy Press and Baker Botts have noted that the underlying theory is untested and would require litigation to establish as binding.

In practice: the FTC statement signals federal posture. It does not invalidate any state law.

### DOJ AI Litigation Task Force

The DOJ's AI Litigation Task Force launched **January 9, 2026**, within the EO's 30-day window. It operates on three legal theories:

- **Dormant Commerce Clause** — state law imposes undue burden on interstate commerce
- **Express or implied federal preemption**
- **Equal Protection** challenges

**Colorado is the only state where the Task Force has acted.** On April 24, 2026, the DOJ intervened in xAI's federal lawsuit challenging Colorado's original AI Act (SB24-205). Three days later, Magistrate Judge Cyrus Y. Chung granted a **stay** of enforcement pending xAI's preliminary injunction motion — which must be filed by **June 11, 2026**.

No other state has seen DOJ intervention as of June 1, 2026.

---

## The Current State Law Map

Here is where each major state AI law stands as of June 1, 2026:

### New York RAISE Act
**Status: Signed and in force, operative date January 1, 2027.**

Governor Hochul signed the RAISE Act on December 19, 2025. The law is in effect but operative requirements (for frontier model developers: safety frameworks, incident reporting, model evaluations) do not apply until January 1, 2027. Chapter amendments to align the timeline more closely with California's approach are pending in committee. No federal challenge has been filed against the RAISE Act. Full builder coverage: [New York RAISE Act Frontier AI Compliance Builder Guide](/builders-log/new-york-raise-act-frontier-ai-compliance-builder-guide/).

### Illinois SB 315 (Artificial Intelligence Safety Measures Act)
**Status: Passed legislature 110-0, pending Governor Pritzker's signature. Not yet signed.**

SB 315 passed the Illinois House unanimously on May 27, 2026. Pritzker has publicly committed to signing it. If signed, it takes effect **January 1, 2027**. SB 315 is the first U.S. law mandating third-party safety audits of frontier AI models — requiring large AI developers to create safety frameworks, conduct catastrophic-risk assessments, and submit to third-party evaluations. Builders have roughly 19 months to prepare if Pritzker signs. Full compliance guide: [Illinois SB 315 AI Safety Audit Compliance](/builders-log/illinois-sb-315-ai-safety-audit-frontier-developer-compliance-2026/).

### Connecticut AIRT Act
**Status: Signed May 27, 2026. Initial provisions effective October 1, 2026.**

Governor Lamont signed SB 5 on May 27, 2026. It creates five separate regulatory regimes — employment AI, AI companions, synthetic content watermarking, frontier model whistleblower requirements, and social media recommenders — with staggered deadlines from October 2026 through January 2028. The October 1, 2026 deadline for employment AI tools is four months away. Full breakdown: [Connecticut AIRT Act: Five Separate AI Regulations in One Law](/builders-log/connecticut-airt-act-sb5-five-regime-ai-law-builder-compliance-guide/).

### Colorado AI Act (SB24-205 → SB 189)
**Status: Original law stayed by federal court; replaced by SB 189 signed May 14, 2026. SB 189 effective January 1, 2027. Both laws face ongoing legal challenge.**

The original Colorado AI Act (SB24-205) was slated to take effect June 30, 2026, but:
1. A federal court stayed enforcement on April 27 pending xAI's injunction motion
2. Governor Polis signed **SB 189** on May 14, which repeals and replaces SB24-205 with a narrower, notice-based transparency law — effective January 1, 2027

xAI and potentially the DOJ are expected to challenge SB 189 as well. As of June 1, SB24-205's original June 30 effective date is moot — it has been replaced. SB 189 goes into effect January 1, 2027, unless a court enjoins it before then.

### New York A3411B (GenAI Warning Labels)
**Status: Passed legislature, delivered to Governor Hochul. Not yet signed.**

A3411B passed the NY Senate 58-2 on March 9, 2026 and was delivered to Hochul. It requires generative AI operators to display a "clear and conspicuous" notice that AI outputs may be inaccurate. Penalty: up to $1,000 per user who did not receive the notice (each user = a separate violation). Takes effect 90 days after signing. Hochul has not signed or vetoed as of June 1. There is no public indication of her timeline or intent.

---

## What Builders Should Do Now

Six months into the EO, legal consensus is clear: **federal preemption actions to date do not nullify state AI laws.** Every major law firm analysis on this question reaches the same conclusion.

**1. Continue state law compliance work. Do not pause for preemption.**

The EO directs agencies to take actions that may eventually produce judicial invalidation of specific laws. That process involves litigation, preliminary injunctions, appeals, and potentially years of proceedings. Colorado's enforcement stay affects only that specific law in that specific case. You cannot rely on the Colorado stay to excuse non-compliance with Connecticut or New York requirements.

**2. Track the Commerce Department report.**

When the Commerce evaluation eventually becomes public, it will reveal which state laws the administration considers "onerous" — and therefore which states face BEAD broadband funding threats. That political lever could cause some states to amend laws preemptively. If the states relevant to your product are named, compliance timelines may shift. If they are not named, expect no federal relief.

**3. Understand the EO's carve-outs for your vertical.**

If your products are focused on children's safety, AI compute infrastructure, or government AI procurement, the EO expressly preserves state law authority in those areas. Your compliance obligation is unchanged and has no federal preemption cover.

**4. Build for multiple regulatory scenarios.**

Good compliance architecture accommodates: (a) state laws remaining fully enforceable, (b) specific laws being enjoined pending litigation, and (c) eventual federal legislation creating a uniform standard. The builders who are struggling are those who built for one scenario only. Design your compliance program to be adjustable.

**5. The DOJ task force moves slowly.**

The Task Force launched in January 2026. As of June 1, it has acted against one state. Even from referral to preliminary injunction can take many months; a final court ruling takes years. State laws are enforceable until a court says otherwise. Do not conflate federal policy posture with legal reality.

---

## What to Watch

- **June 11, 2026** — xAI must file its Colorado preliminary injunction motion (SB 189). This is the next concrete legal event in the preemption timeline.
- **Commerce Department report** — May be released publicly or leaked. States named face BEAD funding threats and political pressure to amend laws.
- **NY A3411B** — Every week Hochul has not signed or vetoed is not a signal. She has ten months to act after the legislature adjourns. Watch for press statements or a chapter amendment process.
- **Illinois SB 315 signature** — Pritzker's public commitment makes this close to certain, but the clock for the January 1, 2027 effective date does not start until signing.
- **Federal legislation** — The March 20 National Policy Framework is a Congressional ask. If Congress moves on it (unlikely in 2026 given the Senate calendar), that would be the most consequential preemption development.

---

The federal-state AI regulatory collision is real, but the collision is slow. The practical reality for builders in 2026 is that state law compliance is required, federal preemption is a process not a fact, and the uncertainty favors building compliance programs that are flexible rather than programs that bet on one outcome.
