---
title: "Figma Make Now Edits Your Production Codebase: The Design-Code Loop Closes"
date: 2026-05-29
description: "Figma Make launched a limited beta on May 28 that connects directly to live Git repos, lets designers edit production UI code visually, and pushes changes back as GitHub PRs. Paired with Claude Code's Figma MCP, the design-to-code pipeline is now genuinely bidirectional."
og_description: "Figma Make can now import your actual Git repo, let a designer change a button color by clicking it, and open a GitHub PR with the code change. It's Mac-only and limited beta — but it marks the end of design handoff as a separate step. Here's what the shift means for how AI-native teams build."
content_type: "Builder's Log"
categories: ["AI Industry", "Developer Tools", "Workflow"]
tags: ["figma", "figma-make", "github", "design-tools", "developer-workflow", "claude-code", "mcp", "design-to-code", "product-launch", "agentic"]
---

On May 28, 2026, Figma shipped a limited beta of something that changes the design-developer handoff model at its foundation: Figma Make can now connect directly to a live Git repository, let a designer visually edit the running application's UI, and push those changes back to engineering as a GitHub pull request — without the designer writing a line of code.

This is not a prototyping tool. It connects to your real codebase.

---

## What the Integration Does

Figma Make's new GitHub integration adds three things to what was previously a sandbox:

**1. Repo import.** Inside the Figma Beta desktop app (Mac only, for now), users connect a GitHub account or organization, select a repository, and Make installs dependencies and spins up a local dev server automatically. The canvas renders the running application.

**2. Direct editing.** Select any visible UI element — a button, a heading, a layout container — and adjust its color, font, spacing, or position on the canvas. Make identifies the relevant code behind that element and modifies it to match. The edit is reflected live. No code editor needed.

**3. PR creation.** Changes accumulate as local commits inside Figma Make's environment. When the designer is ready to ship, they generate a branch and open a pull request directly from Make. The PR lands in the standard GitHub workflow that the engineering team already reviews.

**Access:** Limited beta launched May 28, 2026. Mac only (Figma Beta desktop app required). Windows and Linux support is on the roadmap with no date given. Credits are not consumed during beta.

---

## The Direction of Flow

One important constraint: **sync is one-directional**. Changes flow from Figma Make to GitHub. If an engineer merges a PR and the codebase moves forward, Figma Make does not automatically pull those changes back into the canvas. A designer would need to re-import.

This means the tool is most useful for discrete, bounded visual changes — not ongoing collaboration on a fast-moving branch.

---

## The Other Half: Claude Code → Figma

Figma Make's GitHub integration completes a loop that Anthropic opened in February 2026.

On February 17, Figma and Anthropic announced a Claude Code integration that runs in the reverse direction: from production code into Figma. With the Figma MCP installed, a developer can type "Send this to Figma" inside a Claude Code session, and Claude captures the live running UI from the browser — production, staging, or localhost — and converts it into editable Figma frames. Text becomes editable text. Buttons become separate components. Layouts use auto-layout.

That integration answers the question: *what does the live app actually look like right now, in Figma?*

Figma Make's new integration answers the reverse: *how do I get a design change into production code without a developer?*

Together they form a loop:

```
Claude Code edits code → "Send this to Figma" → designer sees canvas
Designer changes button color in Make → PR opened → engineer reviews and merges
Claude Code picks up merged change → "Send this to Figma" → canvas is current again
```

Neither tool fully automates the loop. Both require deliberate action from a human at each step. But the handoff steps that previously required Slack threads, Figma export files, redline documents, and spec interpretation are gone.

---

## What This Means for Builder Teams

### The scope of "who can ship" expands

Figma Make's GitHub integration means a product manager or designer can now make a visual change to production UI — typographic adjustment, spacing fix, color update, layout shift — and submit it for engineering review without touching a code editor. The PR gates the change, but the human initiating the change does not need to be a developer.

For small teams where "move this 8 pixels" routinely sits in an engineering backlog, this compresses the cycle significantly.

### The governance model holds

The integration does not bypass the review process — it routes through it. Changes land as PRs. Engineers see the diff. They can reject, request changes, or merge exactly as they would with any other contribution. For teams that want AI-assisted design changes without losing audit trails or breaking CI pipelines, this is the right architecture.

### Visual editing has limits

What Figma Make can confidently change is narrow: visual properties. Color values, font sizes, spacing tokens, layout direction. It cannot safely handle changes that depend on business logic, feature flags, conditional rendering, or application state. A button that looks like a static UI element may actually render conditionally based on a user role. A layout that appears simple may depend on a data shape from an API.

Designers using this tool need to understand where visual and logic boundaries are in their codebase — or be prepared to work closely with engineers on changes where it is ambiguous.

### Mac-only adoption is real friction

The requirement for the Figma Beta desktop app on macOS limits who can participate in the beta right now. Teams on Linux (common in engineering) or Windows cannot use it yet. For mixed-OS organizations, this means the tool will primarily be trialed by designers rather than the full cross-functional team during the beta phase.

### AI-native product teams have an advantage here

Teams that have already established AI-assisted coding workflows — particularly those using Claude Code — are positioned to stack this effectively. The Claude Code → Figma direction is already in production for some teams. Adding Figma Make → GitHub creates a feedback loop where design intent and code reality stay in tighter sync than they typically would.

---

## What It Is Not

Figma Make's GitHub integration is **not** a visual regression testing tool. It does not validate that the code change achieves the visual outcome across browsers, screen sizes, or states. That still requires testing infrastructure.

It is **not** a design system enforcement layer. Figma Make does not know whether the color value you changed is a token from your design system or a hardcoded value sitting outside it. Token discipline is the team's responsibility.

It is **not** a replacement for a frontend developer on complex changes. For anything beyond contained visual edits, engineer involvement remains essential.

---

## Bottom Line

Figma Make's GitHub integration is the first tool that makes the design-to-production step feel like a single action rather than a handoff chain. Its scope is deliberately limited: visual properties, Mac-only, beta access, one-directional sync. Those limitations are appropriate for a first release that touches production codebases.

The more significant shift is architectural. Paired with Claude Code's Figma MCP, Figma has now instrumented both directions of the design-code relationship. Code can flow to canvas. Canvas changes can flow back to code. The remaining gap — keeping the two in sync automatically as both evolve — is the obvious next step.

For builders, the practical question is not whether to use it yet. It is whether your team's design-dev workflow will be competitive in two years if you have not built intuition for tools that collapse this boundary now.

The beta is the time to build that intuition.
