---
title: "NY GBL §396-b Is Live: The Synthetic Performer Ad Disclosure Law Builders Need to Know"
date: 2026-06-10
description: "New York's synthetic performer law went into effect June 9, 2026. If your AI-generated digital humans appear in ads reaching New York audiences, you must conspicuously disclose it — or face penalties up to $5,000 per violation. Here's what the law actually says and what builders must do."
og_description: "NY GBL §396-b is now in effect. Any advertisement featuring an AI-generated digital human must disclose it. Effective June 9, 2026. First violation: $1,000. Subsequent: $5,000. Platform publishers have a 5-day takedown obligation. Here's the compliance breakdown."
content_type: "Builder's Log"
categories: ["Regulation", "Compliance", "New York"]
tags: ["new-york", "synthetic-performer", "ai-advertising", "disclosure", "gbl-396b", "compliance", "builder-guide", "ai-generated-content", "digital-human", "june-2026"]
---

New York's synthetic performer disclosure law, codified as General Business Law §396-b, went into effect on June 9, 2026 — 180 days after Governor Hochul signed S.8420-A/A.8887-B on December 11, 2025. If you build, deploy, or publish AI-generated advertising that reaches New York audiences and includes a digital human standing in for a real actor, you now have legal obligations.

This is not a frontier AI developer law. It covers any entity that produces or publishes advertisements with AI-generated human-looking performers.

---

## The Core Obligation

When an advertisement includes a "synthetic performer," the advertiser must make a **conspicuous disclosure** of that fact.

That is the whole law, in one sentence. The rest is definitions, exemptions, penalties, and platform obligations.

---

## What Is a "Synthetic Performer"

The statutory definition is precise and it is worth reading carefully.

A synthetic performer is a digitally created asset that:

1. Is created, reproduced, or modified using **generative AI or a software algorithm**, AND
2. Is **intended to give the impression** that it is engaging in an audiovisual or visual performance of a human performer who is **not recognizable as any identifiable natural person**

Two elements must both be true. The asset must be algorithm-generated, and it must be intended to look like a generic human rather than a specific identifiable real person.

**Point 1 matters for tooling scope.** The law covers any software algorithm — not only AI. A procedurally generated avatar created with older 3D tools would count if it meets element 2. The "AI" framing in press coverage is accurate for most current use cases, but the legal scope is broader.

**Point 2 distinguishes this law from New York's other AI image law.** A deepfake or digital replica of a recognizable real person — a celebrity, a deceased actor, a famous athlete — is governed by S.8882, a separate law covering right of publicity for deceased personalities and digital replicas of identifiable individuals. GBL §396-b specifically targets the opposite case: AI-generated humans intended to look like plausible but non-identifiable people.

---

## What Is Not Covered

The law has explicit exemptions that builders should understand.

**Audio-only advertisements.** The law covers audiovisual and visual performances. An AI-generated voiceover with no visual component is not in scope. (That said, voice clones of identifiable people may be covered by other laws.)

**AI used solely for language translation.** If an advertisement features a real human performer and AI is used only to translate their speech into another language, no disclosure is required.

**Advertisements for expressive works.** Ads for films, television shows, streaming content, documentaries, video games, and similar works are exempt if the synthetic performer's use is "consistent with the underlying work." A movie trailer that features the same AI-generated characters from the film is not subject to disclosure requirements. A standalone product ad that happens to feature an AI-generated actor is not exempt on these grounds.

**Abstract and non-human representations.** Cartoons, mannequins, and abstract avatars are not synthetic performers if they are not intended to mimic human performers. An illustrated mascot is not in scope. A photorealistic AI-generated person intended to look human is.

**Media publisher liability.** Newspapers, magazines, television networks, streaming services, cable systems, and billboard companies are not liable for running non-compliant third-party ads. Section 230 protections are expressly preserved for content providers. The obligation sits with the advertiser, not the publisher — except for the takedown obligation described below.

---

## The Actual Knowledge Standard

The law applies to advertisers who include a synthetic performer **with actual knowledge** of its presence. This standard matters for how you structure your production workflow.

If you commission an ad from a production vendor who uses AI-generated characters without disclosing that to you, and you had no way to know, you have an argument that actual knowledge was absent.

In practice, this means:

- **Vendor contracts should explicitly require disclosure** of any synthetic performers in deliverables
- **Production review workflows should include a synthetic performer check** before publication
- **If you receive a notification that an ad you published contains an undisclosed synthetic performer**, you now have actual knowledge — and the 5-day clock starts

---

## Platform and Publisher Obligations: The 5-Day Takedown Rule

Even though media publishers are not primarily liable, they have a secondary obligation. If a publisher receives **notice** that an advertisement on its platform contains an undisclosed synthetic performer, it must either:

- Remove the non-compliant ad, OR
- Bring it into compliance with the disclosure requirement

within **5 days** of receiving that notice.

Failure to act within that window exposes the publisher to enforcement.

**What this means for ad platforms and SaaS tools that place or serve ads:** If your platform accepts third-party advertisements and you receive a complaint or notice about a non-compliant synthetic performer, you have a 5-day window to act. Build a notice intake process and make sure it routes to someone who can pull the ad.

---

## Disclosure Requirements: The Undefined Gap

The law requires a "conspicuous disclosure" but does not define what conspicuous means, does not specify placement, does not specify language, and does not specify size or duration requirements.

As of now, there is no regulatory guidance. The New York Attorney General's office has enforcement authority, but no formal rules have been issued.

Market practices are still forming. For reference, what other disclosure frameworks have treated as conspicuous in comparable contexts:

- **FTC endorsement guidance**: Disclosures must be "clear and conspicuous" — placed so consumers will actually notice and understand them, not buried in fine print or scrolled-past footnotes
- **Ad superimpositions**: Text overlaid on screen long enough to read (usually 3+ seconds minimum in broadcast contexts)
- **Digital ad labeling conventions**: Formats like "AD" or "Sponsored" in corners of display ads have established visual conventions; a synthetic performer disclosure may follow similar patterns

A conservative approach: include a clear text label (e.g., "This advertisement features an AI-generated performer") that is visible for the duration of any visual content, or adjacent to the ad in digital placement contexts. Until regulatory guidance or enforcement actions set clearer standards, "when in doubt, make it visible" is the defensible position.

---

## Penalties

- **First violation**: Civil penalty of $1,000
- **Subsequent violations**: Civil penalty of $5,000 per violation
- **No private right of action**: The law is enforced by the state, not by individual consumers or competitors

The per-violation framing matters. If you run the same non-compliant ad across 50 placements after a first violation, that is potentially 49 subsequent-violation penalties. For a large ad campaign, the math accumulates quickly.

---

## The Companion Law: S.8882 (Digital Replicas of Real People)

GBL §396-b covers synthetic performers — AI-generated people not recognizable as any specific real person. New York's companion law S.8882 covers the opposite case: AI-generated or digitally altered representations of **identifiable real people** used commercially without authorization.

S.8882 covers both living and deceased individuals. For deceased persons, liability extends for 40 years post-death. Unauthorized commercial use triggers damages of at least $2,000, actual compensatory damages, profits, and potential punitive damages. S.8882 took effect immediately upon signing in December 2025, so it has been in force since then.

Together, these two laws cover the spectrum:
- Generic AI-generated human in an ad → GBL §396-b (disclosure obligation)
- AI-generated version of a recognizable real person in a commercial context → S.8882 (right of publicity liability)

---

## Builder Checklist

**If you build AI avatar or digital human generation tools:**
- If you know or reasonably expect your outputs will appear in advertisements, document that in your terms of service and surface disclosure requirements to your users
- You are a producer of synthetic performers; whether you are the "advertiser" depends on how your tool is deployed

**If you build ad creation platforms or campaign management tools:**
- Add a synthetic performer flag to your creative asset metadata schema
- Surface a disclosure-required prompt when synthetic performers are tagged
- Build your notice intake process for the 5-day takedown obligation

**If you are a marketer or agency using AI-generated talent:**
- Audit current campaigns for synthetic performers
- Confirm disclosure placement meets a reasonable "conspicuous" standard
- Update vendor contracts to require synthetic performer identification in deliverables
- Document your review process to establish actual knowledge chain of custody

**If you serve ads at the platform layer:**
- Build a notice intake queue and a 5-day SLA for takedowns
- Review your terms of service with advertisers to allocate disclosure responsibility

---

## Scope Note: Reach

The law applies to advertisements that may reach New York audiences. New York has roughly 19.5 million residents and is one of the top five U.S. digital advertising markets. A national ad campaign almost certainly reaches New York. A geo-targeted campaign that explicitly excludes New York might create a carve-out, but relying on geotargeting exclusions as a compliance strategy carries its own risks if targeting is imprecise.

The safe default: treat GBL §396-b as applicable to any advertisement with a U.S. national reach.

---

## Federal Preemption Context

When Hochul signed S.8420-A in December 2025, the Trump administration's AI executive order was framing state AI regulations as potential impediments to national AI competitiveness. The EO expressed a federal preference against state-level AI regulation fragmentation.

However, the EO does not itself preempt state law. Federal preemption requires either a specific federal statute or a constitutional conflict. Neither currently exists for state AI disclosure requirements in advertising. GBL §396-b is in force, and the legal pathway to challenge it on federal preemption grounds is not straightforward.

Until a federal court issues a preemption ruling or Congress passes legislation that explicitly displaces state AI advertising rules, this law applies.

---

## Status Summary

| Item | Detail |
|---|---|
| Law | NY GBL §396-b (S.8420-A / A.8887-B) |
| Signed | December 11, 2025 |
| Effective | June 9, 2026 |
| Scope | Advertisements with AI-generated digital humans, reaching New York audiences |
| Disclosure required | Yes — conspicuous, undefined format |
| First violation penalty | $1,000 |
| Subsequent violation penalty | $5,000 |
| Platform takedown window | 5 days after notice |
| Private right of action | No |
| Companion law | S.8882 (digital replicas of real/deceased people, effective immediately Dec 2025) |

The law is live. If your advertising pipeline touches synthetic performers, the compliance clock is running.
