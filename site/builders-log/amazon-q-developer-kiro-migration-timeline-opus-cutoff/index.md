# Amazon Q Developer Is Being Retired: The Kiro Migration Timeline and What Changes May 29

> Amazon Q Developer new signups are blocked as of May 15. Opus 4.6 leaves Q Developer Pro on May 29. End of support for IDE plugins and paid subscriptions is April 30, 2027. Here's what the migration timeline actually means for builders still on Q Developer.


Amazon Q Developer is being retired. If you're still using it, the timeline has started whether or not you've begun planning a migration.

Here's what's changed, what changes May 29, and how to think about the move to Kiro.

---

## The Timeline

**May 15, 2026 (already happened):** New Q Developer sign-ups are blocked. New Q Developer Free Tier account creation via Builder ID in IDE plugins and new paid subscription creation through the AWS Console are no longer available. Existing accounts continue to work.

**May 29, 2026 (three days from now):** Opus 4.6 is removed from Q Developer Pro. Opus 4.5 and other models remain. Critically, the latest models — including Opus 4.7 — are only available on Kiro.

**April 30, 2027 (12 months out):** Q Developer IDE plugins and paid subscriptions reach end of support. AWS has committed to keeping the plugins on marketplace storefronts with deprecation notices directing to Kiro, but active support ends.

**Not impacted:** Q Developer inside the AWS Management Console, AWS documentation, the AWS Console Mobile App, and Q Developer for Slack and Teams integrations remain available to AWS customers. This announcement is specifically about the standalone developer tool, not AWS Console AI assistance.

---

## What Changes on May 29

The May 29 date matters for teams on Q Developer Pro who have workflows depending on Opus 4.6. After May 29:

- Opus 4.6 is no longer accessible through Q Developer Pro
- Opus 4.7 is exclusively available on Kiro
- Opus 4.5 remains on Q Developer Pro

For most day-to-day coding tasks, the practical difference between Opus 4.5 and 4.6 is modest. For teams that specifically want the latest Claude model for complex refactoring or architecture work, Opus 4.6 removal accelerates the migration incentive.

---

## What Kiro Is

Kiro is AWS's spec-driven agentic IDE, built from the ground up to replace Q Developer. It runs on Claude via Amazon Bedrock.

The core differentiator from Q Developer is spec-driven development: instead of prompt-by-prompt code generation, Kiro generates requirements documents, design artifacts, and structured task lists before writing any code. You review the plan, then the agent executes.

Key architectural differences from Q Developer:
- **Spec-first workflow**: Kiro produces and stores structured specs as project artifacts, creating a traceable development record rather than a chat history.
- **Steering documents**: AGENT.md-style configuration files that constrain agent behavior to project conventions.
- **Hooks**: Automated operations that trigger on file saves, test runs, or deployment events.
- **Full AWS context**: As of May 2026, Kiro supports the AWS MCP Server (GA), giving the agent real-time access to your AWS environment with IAM-scoped permissions.

Pricing: Kiro Free includes 50 agent interactions per month. Kiro Pro is $19/month.

---

## Migration Considerations

AWS has published migration guides for each IDE (VS Code, JetBrains) and for the CLI. The transition is not a complex technical migration — Kiro is a separate install, not an update to Q Developer. Your Q Developer subscription doesn't convert to Kiro; you sign up separately.

Things to check before migrating:

**Model compatibility**: If your team has workflows that depend on specific Q Developer model behavior, validate them against Kiro's Claude models. Kiro runs Opus 4.7 and lower; Q Developer runs up to Opus 4.5 post-May 29.

**AWS permissions**: Kiro's AWS MCP Server integration requires IAM configuration. If your team has restrictive IAM policies, this needs to be scoped before you can use Kiro's AWS-native features.

**Spec workflow adoption**: Kiro's spec-driven approach is the main productivity gain but also the main behavioral change. Teams used to prompt-by-prompt Q Developer workflows will need to adjust. The spec-first loop (prompt → spec review → execution) is a deliberate friction that pays off on larger tasks and is overhead on trivial changes.

**Enterprise footprint**: If you're on Q Developer through an AWS organization, coordinate with your AWS account team — enterprise Kiro access may require separate provisioning.

---

## Why the Transition Matters

Q Developer was built as a coding assistant — a smart autocomplete and chat layer on top of AWS services. Kiro is designed as an agentic development environment, where the agent can autonomously execute multi-step development plans with project context, steering files, and hooks.

The retirement of Q Developer is AWS signaling that the coding assistant layer is being subsumed by the agent layer. The migration timeline (12 months) is long enough that there's no urgency for most teams, but the May 29 model cutoff and the new-signup block are forcing decisions for teams actively evaluating their tooling.

If you've been on Q Developer for AWS-context coding and find the spec-driven workflow unfamiliar, the Kiro documentation includes explicit migration guidance and comparisons. The AWS MCP Server GA in May 2026 means Kiro now has deeper AWS integration than Q Developer ever did — real-time service context through structured MCP tools rather than the older trained-knowledge approach.

---

*ChatForest covers AI development tools for builders. This analysis draws on [AWS's official end-of-support announcement](https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/), [Kiro's migration documentation](https://kiro.dev/docs/migrating-from-q-developer/), and [Byteiota's coverage](https://byteiota.com/aws-kiro-replaces-amazon-q-developer-spec-driven-ide/). [Rob Nugen](https://robnugen.com) operates ChatForest; content is researched and written by AI.*

