# OpenAI Safety Usage Dashboard: Monitor Blocked Responses API Requests by User — June 2026 Builder Guide

> OpenAI's new Safety Usage Dashboard shows blocked Responses API requests organized by safety_identifier, giving multi-tenant builders a proactive monitoring view instead of waiting for violation emails.


On June 23, 2026, OpenAI added a Safety Usage Dashboard to the API platform at `platform.openai.com/usage/safety`. The dashboard shows blocked Responses API requests, organized by the `safety_identifier` values you send on each request.

This is an AI-researched guide based on published changelogs and documentation. ChatForest does not have hands-on access to these tools.

---

## What the Safety Usage Dashboard does

When a Responses API request is blocked by OpenAI's safety classifiers, the event now appears in the Safety dashboard tagged with whatever `safety_identifier` you passed on the request. That gives you a per-user view of safety blocks across your entire organization — without waiting for a violation email from OpenAI.

The dashboard is read-only and covers Responses API requests. It lives at `platform.openai.com/usage/safety`.

---

## The prerequisite: passing safety_identifier on every request

The dashboard is only useful if you tag your requests. Without `safety_identifier`, blocked requests have no user attribution and the dashboard can't tell you anything actionable.

**Responses API (Python SDK):**

```python
response = client.responses.create(
    model="gpt-5.5",
    input="...",
    safety_identifier="user_abc123"
)
```

**Chat Completions API (Python SDK):**

```python
response = client.chat.completions.create(
    model="gpt-5.5",
    messages=[{"role": "user", "content": "..."}],
    safety_identifier="user_abc123"
)
```

**Realtime API (WebSocket session credential):**

```
OpenAI-Safety-Identifier: user_abc123
```
Pass this as an HTTP header when obtaining session credentials.

**Best practice:** Don't send email addresses or usernames directly. Hash the identifier first — the value just needs to be stable across sessions for the same user, not human-readable. Use a keyed HMAC of your internal user ID.

Note: safety identifiers don't carry over between APIs or sessions. A user blocked via Responses API is not automatically blocked in Chat Completions, and vice versa.

---

## Enforcement escalation: what happens before you see the dashboard

The Safety Usage Dashboard gives you visibility into a system that was already running before the dashboard existed. Here's how enforcement works:

| Stage | What happens |
|---|---|
| Request classification | Every GPT-5 request is classified into risk thresholds. Low-risk requests pass through normally. |
| Repeated high-risk hits | OpenAI sends a warning email to your organization. Requests still complete, but you're on notice. |
| Sustained violations (~7 days) | Your organization loses GPT-5 access entirely until resolved. |
| High-confidence policy violation | The specific `safety_identifier` is permanently blocked. All future requests from that identifier receive an `identifier_blocked` error. |

The permanent block is the critical one: OpenAI currently cannot unblock individual safety identifiers. Once an identifier is blocked, that user cannot use your application's OpenAI-backed features. You'd need to contact OpenAI support to discuss org-level access, and the underlying user account in your system is effectively banned from the AI features.

---

## What to do when you see blocked requests in the dashboard

**Step 1 — Map the identifier back to the user.** Your `safety_identifier` values should be internally traceable. Look up who that hashed ID belongs to in your system.

**Step 2 — Pull the request context.** Review what prompts the user was sending around the time of the block. Your own request logs (not OpenAI's) are the place to do this — OpenAI's dashboard shows that a block happened, not the content that triggered it.

**Step 3 — Decide your response.** Options:
- Suspend the user from AI features in your system while you investigate
- Implement additional input filtering for that user before re-enabling
- Permanently revoke access if the violation was intentional abuse

**Step 4 — Do not try to rotate identifiers.** Giving a blocked user a new `safety_identifier` to circumvent the block violates OpenAI's terms of service and could escalate enforcement to the entire organization.

---

## Decision guide: should you implement safety_identifier?

| Situation | Recommendation |
|---|---|
| Single-user app (personal tool, internal script) | Skip it — one user means no attribution value; the dashboard won't add anything. |
| Multi-tenant SaaS with untrusted input | Implement immediately. This is the key scenario the feature is designed for. |
| B2B app with vetted enterprise customers | Implement, but lower priority — vetted users generate fewer violations. |
| High-volume app where one bad actor could pull org access | High priority. The identifier lets OpenAI block the actor, not the org. |

The `safety_identifier` parameter costs nothing and adds no latency. The only reason to skip it is if your application is genuinely single-user.

---

## Pairing with inline moderation (June 4)

Two safety features shipped within weeks of each other in June 2026:

- **Inline moderation scores (June 4):** Add `moderation={"model": "omni-moderation-latest"}` to a Responses API call, and the response includes flagged/score data for both input and output. Useful for soft-blocking, logging, or showing users a content warning before or after generation.

- **Safety Usage Dashboard (June 23):** Shows requests that OpenAI's own classifiers actually blocked, tagged by safety_identifier. This is enforcement-layer data, not soft-flag data.

These operate at different levels. Inline moderation is a tool you run and act on yourself. The Safety Usage Dashboard shows what OpenAI's enforcement system did regardless of your own moderation layer.

A full safety observability stack uses both: your own moderation layer (inline scores) to catch borderline content early, and the Safety Dashboard to see what made it past your layer and got blocked by OpenAI's classifiers.

---

## Limitations

- **Responses API only:** The dashboard covers Responses API blocked requests. Chat Completions blocks may not appear.
- **Read-only, no export API:** The dashboard is a UI-only view. There's no documented API endpoint to programmatically retrieve blocked request data.
- **No content included:** The dashboard shows that a request was blocked, not what the request contained. You need your own request logging to see the content.
- **No unblock via dashboard:** Individual safety_identifier blocks are permanent and can only be addressed by contacting OpenAI support.
- **Identifiers don't cross APIs:** A blocked Responses API identifier is not automatically blocked in Chat Completions or Realtime.

---

## The bottom line

If you're running a multi-tenant application on OpenAI's Responses API, add `safety_identifier` to every request today — not because of the dashboard, but because it limits blast radius if one of your users triggers an enforcement action. The dashboard is the reward: instead of finding out about blocks via an email from OpenAI's trust and safety team, you can see them as they happen and respond on your own timeline.

