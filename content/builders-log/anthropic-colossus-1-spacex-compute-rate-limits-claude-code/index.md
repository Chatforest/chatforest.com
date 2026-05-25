---
title: "Anthropic Rents xAI's Old GPU Farm: What the $1.25B/Month Colossus 1 Deal Means for Your Rate Limits"
date: 2026-05-26
description: "Anthropic signed a $1.25 billion-per-month contract for SpaceX's Colossus 1 — the Memphis facility xAI used to train Grok, now running 220,000 NVIDIA GPUs for Claude. Three rate limit increases in five weeks followed. Here's what changed, what expires on July 13, and how to think about it."
content_type: "Builder's Log"
categories: ["Anthropic", "Claude Code", "Infrastructure"]
tags: ["anthropic", "claude", "claude-code", "rate-limits", "spacex", "colossus", "compute", "xai", "developer-platform", "capacity"]
---

Anthropic had a problem that builders kept noticing: Claude Code would grind into its limits at the worst possible time — mid-refactor, mid-pipeline run, mid-agentic loop. The frustration was real enough that "Claude rate limit" was becoming a deciding factor in evaluations against OpenAI Codex.

On May 6, 2026, Anthropic announced a compute deal with SpaceX that changed the underlying math. Seven days later came a second capacity expansion. Between the two announcements, Anthropic pushed through three distinct rate limit improvements in five weeks. Here is what happened, what it costs Anthropic, and what builders need to know before July 13.

## The Compute: Colossus 1 in Memphis

Colossus 1 is a 300-megawatt data center in Memphis, Tennessee, built by SpaceX and initially operated as xAI's training facility for the Grok model family. It houses more than 220,000 NVIDIA GPUs — H100s, H200s, and GB200s — across a single site.

By early 2026, xAI had shifted most of its active training to Colossus 2, leaving Colossus 1 running at roughly 11% of capacity. SpaceX, which operated the physical facility, had a very large, very expensive building sitting mostly idle.

Anthropic signed an agreement for exclusive access to the entire facility: all 220,000-plus GPUs, all 300 megawatts, at a reported cost of $1.25 billion per month through May 2029. Over the contract term, that totals more than $40 billion — one of the largest compute commitments in AI history.

Anthropic also disclosed it has "expressed interest in partnering with SpaceX to develop multiple gigawatts of orbital AI compute capacity." That is a longer-horizon bet that is not yet real infrastructure, but it signals the scale Anthropic believes it needs.

## The Rate Limit Timeline

The Colossus 1 capacity was not immediately online — Anthropic said it would come available within a month of the May 6 announcement. But the company moved quickly on rate limits regardless, apparently confident enough in the incoming capacity to expand limits ahead of the hardware going live.

Three changes happened in quick succession:

**Peak-hour limits removed.** Before May 6, Pro and Max subscribers faced reduced throughput during peak usage windows. That cap was eliminated entirely.

**Hourly limits doubled (May 6).** Claude Code's five-hour usage blocks doubled for Pro, Max, Team, and seat-based Enterprise plans. For API developers, the jump was more dramatic: Tier 1 input tokens per minute went from 30,000 to 500,000 — a 16x increase — and output tokens per minute from 8,000 to 80,000 (10x).

**Weekly limits up 50% (May 13).** A week after the hourly doubling, Anthropic raised the weekly ceiling by another 50% across Pro, Max, Team, and Enterprise. This closed the gap between Claude Code's weekly budget and OpenAI Codex's, which had been a complaint point in direct comparisons.

The net effect: if you were hitting walls in March, your per-session and per-week capacity in late May is roughly three to four times what it was. No configuration change required — the increases apply automatically to existing plans.

## The July 13 Cliff

There is a date builders should have on their radar: **July 13, 2026 at 6PM PDT**.

The 50% weekly limit increase from May 13 is explicitly temporary through that date. Anthropic has not announced whether the new ceiling will become permanent, revert to the pre-May baseline, or land somewhere in between.

The hourly doubling and peak-hour removal are not publicly flagged as temporary, but they were also announced in the same competitive context. It would be unusual for Anthropic to hold the hourly floor while rolling back the weekly ceiling, but unusual things do happen in competitive product cycles.

The practical builder read: the window between now and July 13 is a good one to run your heaviest Claude Code workloads. If you have been deferring intensive refactors, batch processing pipelines, or extended agentic sessions because of limit anxiety, the next six weeks are the time to execute them.

After July 13, watch for an Anthropic announcement. If the weekly limits are made permanent, that signals Anthropic believes the Colossus 1 capacity has stabilized delivery. If they roll back, expect the product team to take another pass at limits within the following quarter — the competitive pressure from Codex is not going away.

## The Competitive Subtext

Anthropic did not acquire Colossus 1 in a vacuum. OpenAI's Codex agent has been gaining attention for long-horizon coding tasks, and Claude Code's rate limits had become a recurring friction point in the comparison. Several developers posted publicly that they had cancelled Max plans because of rate-limit walls.

Renting xAI's old training facility is a blunt way to close that gap. Anthropic got 220,000 GPUs on a facility that was effectively stranded — xAI had moved on, SpaceX needed a tenant, and Anthropic needed capacity. The economics work because xAI had already absorbed the construction cost.

For builders, the competitive dynamic translates simply: both Claude Code and Codex are now operating at higher capacity ceilings than they were in Q1 2026. The deciding variable is shifting back toward capability and workflow fit rather than raw availability.

## What Builders Should Do

**Before July 13:**
- If you have been rationing heavy Claude Code sessions, stop rationing. The capacity is there.
- Run the agentic workloads you have been holding back. Measure actual output quality, not just limit headroom.
- If you are evaluating Claude Code vs Codex, this is a more level comparison than it was in March.

**Around July 13:**
- Watch for Anthropic's announcement on whether the 50% weekly increase becomes permanent.
- If it reverts, your decision calculus on plan tier may change. Build your budget models around the base limits, not the temporary expansion.

**Longer term:**
- The $40 billion compute commitment is a statement about Anthropic's ambitions. A company that spends $1.25B/month on inference capacity is not planning to be capacity-constrained at current growth rates.
- The orbital compute interest is speculative but directionally meaningful: Anthropic is thinking about the infrastructure problem at scales well beyond what any existing data center can provide.

## Bottom Line

Anthropic's rate limit problem was a capacity problem. The Colossus 1 deal is a direct, expensive, and high-speed response to that problem. Three rate limit improvements in five weeks is an unusually fast operational cadence — Anthropic clearly decided this was worth moving on before the hardware was even online.

The July 13 expiration on the weekly boost is the near-term unknown. Mark the date, run your heavier workloads now, and decide on plan configuration after Anthropic clarifies what sticks.
