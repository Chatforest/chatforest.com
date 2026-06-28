---
title: "AI Coding Hits 97% Enterprise Adoption — but 70% of Teams Have No Governance: The Builder's Audit"
date: 2026-06-28
description: "Black Duck's March 2026 survey of 831 enterprise engineers found near-universal AI coding tool adoption but a governance gap that wipes out the efficiency gains. Teams with governance are 55% more likely to hit major productivity improvements. Here is what to audit."
og_description: "97% of enterprise developers use AI coding tools. Only 30% have governance in place. Teams that do are 55% more likely to see major efficiency gains. Black Duck's 831-person study unpacked for builders."
content_type: "Builder's Log"
categories: ["Developer Tools", "AI Governance", "Security"]
tags: ["ai-coding", "governance", "black-duck", "enterprise", "devsecops", "security", "productivity", "june-2026", "builder-guide"]
---

Nearly every enterprise software team is using AI coding tools. Most of them are flying without instruments.

**Black Duck** published *The State of AI-Powered Software Development* on June 9, 2026, surveying **831 enterprise software engineers and DevOps professionals** at organizations with 500+ employees. The March 2026 survey was conducted with independent research firm UserEvidence across a range of industries.

The headline finding gets attention: **97% enterprise adoption** of AI coding assistants. The finding that should drive your next sprint doesn't: **only 30% of those teams have full governance in place.** And teams that do have governance are **55% more likely to report major efficiency improvements** than those that don't.

Speed without governance is not an advantage — it's a liability accumulation.

---

## What Teams Are Getting Right

The productivity numbers are real. Not AI-vendor-sponsored survey real — 831-engineer real.

- **92%** of teams report improved productivity and release velocity
- **58%** say the improvement is *major*, not marginal
- Developers reclaim an **average of 8 hours per week**
- **53%** have grown total code volume by more than 25%

Eight hours a week is a full day. For a 10-person team that fully adopts AI coding tools, that is 80 person-hours weekly — roughly two full-time engineers worth of recovered capacity. This is not hypothetical upside. It is the median result already showing up across the organizations surveyed.

The adoption number confirms what most builders already know from experience: AI coding is not a new experiment to evaluate. It is the current baseline. Arguing about whether to adopt puts you in the minority.

---

## The Governance Gap

Here is where the data diverges from the headline narrative.

**68%** of respondents say automated tracking of AI-generated code is *extremely important*. Only **30%** have it.

That is a 38-point conviction-to-action gap. The teams who know governance matters are largely the same teams that haven't implemented it.

Why does this gap persist? The bottleneck data suggests where the drag is:

- **52%** face bottlenecks in manual code review
- **51%** encounter security testing delays
- **48%** deal with code rework requirements

AI tools accelerate the writing of code faster than review pipelines can absorb it. The result is either a queue that grows until something breaks, or teams skip review to keep velocity up. Neither outcome is sustainable.

---

## The Security Exposure

The security picture is the most actionable finding for teams with production systems.

- **64%** of respondents express moderate or extreme concern about security defects from AI-generated code
- **Nearly 90%** encounter issues with AI-generated code at some point
- **51%** of the teams with the highest security concern are also the *heaviest* AI users

That correlation is not surprising — more AI-generated code means more surface area — but it is worth stating clearly: the teams most exposed to AI-generated security defects are the ones who have adopted AI tools most aggressively. Adoption intensity and security risk track together in the current tooling environment.

The finding is not an argument against adoption. It is an argument for pairing adoption with instrumentation.

---

## What Governance Actually Means

The survey probed what developers want from governance, not just whether they have it.

- **86%** believe AI should evaluate AI-generated code (automated review in the pipeline)
- **84%** prefer keeping humans in the loop via pull requests or IDE suggestions

These two numbers together sketch the model: automated AI-to-AI review as a first pass, with human sign-off at merge gates. The preference for human-in-the-loop is not resistance to automation — it is a quality signal, a preference for maintaining accountability at the point where code becomes production reality.

Black Duck CEO Jason Schmitt framed it plainly: **"speed without governance is a liability, not an advantage."**

---

## The 55% Efficiency Multiplier

The ROI case for governance is in the survey itself. Teams with full governance in place are **55% more likely to report a major improvement in efficiency** compared to teams with partial or no governance.

That number inverts the common framing that governance is overhead. Governance does not slow teams down on net — it converts raw code velocity into reliable delivery. The teams capturing the full productivity gains from AI coding tools are the ones who have closed the instrumentation gap.

---

## Builder Audit: Four Areas to Check

Based on the survey findings, the governance gap shows up in four specific operational areas. Each is auditable in an afternoon.

**1. AI code tracking**
Can you identify what percentage of your current codebase was authored or significantly modified by AI tools? If not, you are in the 70% without automated tracking. Start with IDE telemetry or commit metadata tagging.

**2. Review pipeline capacity**
Is your PR review queue growing? Measure time-to-merge over the past 90 days against your AI adoption curve. If merge latency is increasing while AI tool usage increases, you have a review bottleneck. Options: automated pre-review (AI-checks-AI), stricter scope limits on AI-generated PRs, or dedicated review capacity.

**3. Security gate integration**
Are your existing SAST and dependency scanning tools configured to flag patterns common in AI-generated code? AI assistants sometimes produce code that passes style checks but includes subtle security issues — particularly around input validation, secret handling, and dependency choices. Check whether your security tooling has been tuned since AI adoption accelerated.

**4. Rework tracking**
Are you measuring code churn? High churn on AI-generated code is a signal that review gates are thin. Track the ratio of AI-generated code that gets substantially modified within 30 days of merge.

---

## What This Means for Your Stack

The Black Duck study is an enterprise survey — 500+ employee organizations. But the governance gap it documents shows up at much smaller team sizes. Any team shipping AI-generated code into production without instrumentation is accumulating the same technical and security debt, just faster.

The path from 97% adoption to full productivity capture runs through the 30% that have closed the governance gap. The 55% efficiency differential between governed and ungoverned teams is not a projection — it is the current measured outcome across 831 organizations.

The adoption decision is already made. The governance decision is still pending for most teams.

---

*Source: Black Duck, [The State of AI-Powered Software Development](https://www.blackduck.com/resources/analyst-reports/state-of-ai-powered-software-development.html), published June 9, 2026. Survey of 831 enterprise software engineers conducted March 2026 with UserEvidence.*
