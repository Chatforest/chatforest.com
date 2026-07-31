# Thinking Token Billing Visibility, MCP Tunnels Endpoint Migration, and Opus 4.6 Fast Mode Removal: Three June 2026 Anthropic API Updates

> Three operational API changes from late May and June 2026: usage.output_tokens_details.thinking_tokens now breaks out thinking spend per call; the MCP tunnels management API migrated from the Admin API to the Claude API under a new beta header; and fast mode for Opus 4.6 was silently removed without an error, downgrading requests to standard speed and standard pricing.


Three changes from May 27 to June 29, 2026 that don't individually warrant a blog post but together describe how Anthropic is tightening observability and transitioning the managed-agents API surface. None require a beta header to act on. All affect production systems quietly.

---

## 1. Thinking token billing is now visible per call (May 27)

Before this change, the `usage` object in a Messages API response told you total output tokens billed but did not break out how many of those tokens were extended thinking. Thinking tokens and response text bill at the same rate per output token, so the total was correct, but the split was invisible.

Starting May 27, per [Anthropic's Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview), the response includes:

```json
{
  "usage": {
    "input_tokens": 1240,
    "output_tokens": 3800,
    "output_tokens_details": {
      "thinking_tokens": 2100
    }
  }
}
```

In this example, 2,100 of the 3,800 billed output tokens went to thinking; 1,700 went to the actual response text. No beta header required. It's documented as part of the [budget rules and tuning guidance for thinking tokens](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#budget-rules-and-tuning), so it applies to any model that supports adaptive or extended thinking.

**In streaming**: the breakdown appears only on the final `message_delta` event, [confirmed in Anthropic's extended thinking documentation](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#budget-rules-and-tuning). Intermediate events carry the running `output_tokens` total but not the `thinking_tokens` split. If you are aggregating usage from streaming calls, you must wait for the final delta to get the breakdown.

### Why this matters in practice

With [adaptive thinking on by default for Claude Fable 5](https://platform.claude.com/docs/en/release-notes/overview) (launched June 9, always-on adaptive thinking) and [Claude Sonnet 5](https://platform.claude.com/docs/en/release-notes/overview) (launched June 30, adaptive thinking on by default), and with `effort: "high"` [the default on Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8) across all surfaces including the Messages API, thinking activity is no longer something you explicitly opt into — it happens based on what the model judges the request needs. This makes per-call thinking visibility more important, not less. A prompt that previously triggered no thinking may now trigger several thousand thinking tokens depending on model and effort setting.

Concrete uses for this field:

- **Cost auditing**: For agentic loops with many tool calls and sub-calls, log `thinking_tokens` per turn to identify which steps consume disproportionate thinking budget.
- **Prompt development**: When tuning prompts, compare `thinking_tokens` across variants. A prompt that triggers significantly more thinking is either genuinely harder for the model or ambiguous enough to force extended reasoning you did not intend to pay for.
- **Effort parameter calibration**: If you lower `effort` from `high` to `medium` and want to confirm thinking activity actually reduced, `thinking_tokens` gives you the ground truth. The total `output_tokens` change tells you cost; the `thinking_tokens` breakdown tells you why.

For streaming applications that display a running cost estimate to users or operators, update your usage parser to extract `thinking_tokens` from the final `message_delta` before computing estimated cost per call.

---

## 2. MCP tunnels management API migrated from Admin API to Claude API (June 22)

MCP tunnels ([research preview, launched May 19](https://platform.claude.com/docs/en/release-notes/overview)) let Managed Agents sessions and the Messages API reach MCP servers inside your private network. Per [Anthropic's MCP tunnels overview](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview), "traffic flows over an outbound-only connection, so you don't need to open inbound firewall ports, expose services to the public internet, or allowlist Anthropic's IP ranges on your origin." The feature was useful from day one, but its management API landed on an odd surface: the Admin API at `/v1/organizations/tunnels`.

On June 22, that surface moved.

| | Before June 22 | After June 22 |
|---|---|---|
| Endpoint base | `/v1/organizations/tunnels` (Admin API) | `/v1/tunnels` (Claude API) |
| Beta header | (Admin API credentials, no beta header) | `anthropic-beta: mcp-tunnels-2026-06-22` |
| Auth scope (WIF) | Admin API access | `workspace:manage_tunnels` |

The previous surface remains available during a migration window; per the [Tunnels API reference](https://platform.claude.com/docs/en/api/beta/tunnels), the new surface "supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window." Anthropic has not published an end date for that window. The recommendation is to migrate proactively rather than wait. (Full change details, including the exact endpoint, header, and scope, are documented in the [June 22, 2026 release note](https://platform.claude.com/docs/en/release-notes/overview).)

### What the migration means architecturally

The move from Admin API to Claude API is not just a URL change. The [Admin API](https://platform.claude.com/docs/en/build-with-claude/administration-api) is an organization-level surface that requires an Admin API key, provisioned only by organization members with the admin role, and is used to manage organization members, workspaces, and API keys. Placing tunnel management there was expedient for a research preview but created an access-control problem: any system that needed to create or update MCP tunnels needed admin-level API keys. That is a larger blast radius than the operation warrants.

The Claude API surface is workspace-scoped. The new WIF scope, `workspace:manage_tunnels`, grants access only to the [MCP tunnels API](https://platform.claude.com/docs/en/manage-claude/wif-reference#oauth-scopes) — creating, listing, and archiving tunnels and their certificates — rather than the broader `workspace:developer` scope an API key would carry. You grant exactly the scope the workload needs, nothing more. A CI/CD pipeline that provisions MCP tunnels for agent deployments can use a short-lived WIF token with this scope rather than a long-lived Admin API key.

### Migration steps

If you have code that manages MCP tunnels:

1. Update the base URL from the Admin API to the Claude API (`/v1/tunnels`).
2. Add `anthropic-beta: mcp-tunnels-2026-06-22` to your request headers. The previous surface required no beta header because it was on the Admin API; the new surface is on the Claude API which uses beta headers for research preview features.
3. If you are using Workload Identity Federation, add the `workspace:manage_tunnels` scope to your federation rule and remove any Admin API permissions you were granting solely for tunnel management.
4. Update any documentation or runbooks that reference the old endpoint path.

The [Tunnels API reference](https://platform.claude.com/docs/en/api/beta/tunnels) reflects the new surface.

---

## 3. Opus 4.6 fast mode silently removed (June 29)

On [May 28, when Opus 4.8 launched](https://www.anthropic.com/news/claude-opus-4-8), Anthropic [deprecated fast mode for Opus 4.6 with approximately 30-day removal notice](https://platform.claude.com/docs/en/release-notes/overview). That removal [happened on June 29](https://platform.claude.com/docs/en/release-notes/overview).

What makes this notable is not that it happened — the deprecation was well-flagged — but **how** it happened.

Separately, Anthropic [deprecated fast mode for Opus 4.7 on June 25](https://platform.claude.com/docs/en/release-notes/overview), with removal scheduled for July 24: requests to `claude-opus-4-7` with `speed: "fast"` will fail after that date. That is the standard removal pattern: deprecation notice → hard error at removal.

Opus 4.6 did not get a hard error. Instead, per [Anthropic's June 29, 2026 release note](https://platform.claude.com/docs/en/release-notes/overview):

> Requests to `claude-opus-4-6` with `speed: "fast"` no longer run at fast speed or premium pricing: **they run at standard speed, are billed at standard rates, and do not return an error.** The response's `usage.speed` field reports the speed used.

The request succeeds. No exception to catch. No `400` to handle. The only indication that fast mode is no longer active is `usage.speed` in the response. Anthropic's [fast mode documentation](https://platform.claude.com/docs/en/build-with-claude/fast-mode#checking-which-speed-was-used) confirms this is unique to Opus 4.6: "Instead of returning an error like other models that don't support fast mode, it silently switches to standard speed."

### Why silent removal matters

Teams with `speed: "fast"` hardcoded for Opus 4.6 in production have two effects now: they are paying standard rates (not fast mode's premium, so cost goes down) and getting standard speed (not fast mode's [up to 2.5× throughput boost](https://platform.claude.com/docs/en/build-with-claude/fast-mode), so latency goes up). Neither change generates a monitoring alert unless you are explicitly tracking response speed or cross-referencing `usage.speed`.

For latency-sensitive workflows — agent loops with hard time budgets, streaming interfaces with expected response times, parallel pipelines sized for fast mode throughput — a silent downgrade to standard speed is an operational incident that looks like a slowdown rather than a configuration change. It may take time to diagnose because nothing errored.

**Check `usage.speed` on any Opus 4.6 calls that previously used fast mode.** If it returns `"standard"`, fast mode is gone. Your options are:

- Migrate to Opus 4.8 fast mode (research preview, waitlist at [claude.com/fast-mode](https://claude.com/fast-mode))
- Migrate to Opus 4.7 fast mode before July 24 (same research preview)
- Accept standard speed on Opus 4.6 or migrate to a newer model without fast mode

### The two removal patterns, side by side

| Model | Fast mode removal behavior |
|---|---|
| Claude Opus 4.6 | Silent. Standard speed + standard billing. No error. Check `usage.speed`. |
| Claude Opus 4.7 | Hard error on July 24, 2026. `speed: "fast"` requests fail after removal. |

If you have fast mode configured for both models in different parts of your codebase, the monitoring and mitigation strategies differ. Opus 4.6 needs passive monitoring of `usage.speed`; Opus 4.7 needs proactive migration before July 24.

---

## Summary

| Change | Date | Action |
|---|---|---|
| `usage.output_tokens_details.thinking_tokens` available | May 27 | Add to usage parser; extract from final `message_delta` in streaming |
| MCP tunnels endpoint migrated to `/v1/tunnels` | June 22 | Update endpoint, add `mcp-tunnels-2026-06-22` header, update WIF scope |
| Opus 4.6 fast mode silently removed | June 29 | Check `usage.speed` on Opus 4.6 calls; migrate to 4.7 or 4.8 fast mode if needed |

None of these changes are breaking in the error-returning sense. That is the risk: they affect billing accuracy, access control posture, and latency behavior without surfacing as failures. The operational lesson is the same for all three: API surface changes that don't error still require active response.

