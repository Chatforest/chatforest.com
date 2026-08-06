---
title: "Anthropic agent-memory-2026-07-22: Three Breaking Changes to Fix Before July 22 — Builder's Migration Guide"
date: 2026-07-13
description: "On July 22, 2026, Anthropic's managed-agents-2026-04-01 beta header automatically adopts new memory-list behavior. If you call GET /v1/memory_stores/{id}/memories, three parameters silently change. Migrate before the deadline."
tags: ["anthropic", "claude", "managed-agents", "memory", "api", "breaking-change", "migration", "python"]
sources_audited: 2026-08-06
---

Anthropic has introduced a new beta header — `agent-memory-2026-07-22` — that changes how memory listing works for Managed Agents memory stores. The new behavior is available now as an opt-in. On **July 22, 2026**, the older `managed-agents-2026-04-01` header automatically adopts the same behavior for memory store list calls. This is documented in [Anthropic's July 2, 2026 API release note](https://platform.claude.com/docs/en/release-notes/api) announcing the `agent-memory-2026-07-22` header.

If you call `GET /v1/memory_stores/{memory_store_id}/memories` in your agent and do not update your code before July 22, three things will silently change — and one of them will throw a `400` if your parameters are wrong.

This is a research-based guide. We reviewed [Anthropic's Managed Agents memory documentation](https://platform.claude.com/docs/en/managed-agents/memory), the [API release notes](https://platform.claude.com/docs/en/release-notes/api), and the [beta headers reference](https://platform.claude.com/docs/en/api/beta-headers). We did not test the API endpoints ourselves.

---

## Context: What Is the Managed Agents Memory Store?

Anthropic launched persistent memory for Managed Agents in public beta on [April 23, 2026](https://platform.claude.com/docs/en/release-notes/api). Agents can write facts, preferences, or session state to a memory store, then retrieve them in future sessions. Each memory has a path (like a filesystem) — for example, `/user/profile.md`, `/project/123/context.md` — [addressed and mounted the same way documents are described in Anthropic's memory guide](https://platform.claude.com/docs/en/managed-agents/memory).

The listing API — `GET /v1/memory_stores/{id}/memories` — lets you retrieve stored memories by [path prefix, depth, and ordering](https://platform.claude.com/docs/en/managed-agents/memory#list-memories). This is the endpoint that changes on July 22.

---

## What Changes on July 22

All three changes below are documented together in [Anthropic's July 2, 2026 release note for the `agent-memory-2026-07-22` header](https://platform.claude.com/docs/en/release-notes/api) and reflected in the current [memory store listing reference](https://platform.claude.com/docs/en/managed-agents/memory#list-memories).

### Change 1: `order_by` and `order` Are Ignored

**Before (current behavior with `managed-agents-2026-04-01`):**
You can sort results by passing `order_by` (e.g., `created_at`, `updated_at`) and `order` (`asc` or `desc`). Results come back in the requested order.

**After July 22:**
`order_by` and `order` are silently ignored. Results return in a stable, **server-defined order**. Your code still runs — no error — but any sorting logic you wrote around these parameters is wrong.

**Impact:** If your agent processes memories in a specific sequence (e.g., most recently updated first), you can no longer rely on the API for that ordering. Sort client-side instead.

### Change 2: `depth` Restricted to 0, 1, or Omitted

**Before:**
`depth` can be any non-negative integer, letting you retrieve memories at arbitrary nesting levels below the `path_prefix`.

**After July 22:**
`depth` accepts only `0`, `1`, or being omitted entirely. Sending any other value (e.g., `depth=2` or `depth=5`) returns a **`400` error**.

**Impact:** This is the silent bomb. If you're passing `depth=2` or higher to retrieve deeply nested memories, your code will throw after July 22. Review every `memories.list()` call.

### Change 3: `path_prefix` Must End With `/` and Matches Whole Segments

**Before:**
`path_prefix="user"` matches any path that starts with the substring `user` — including `user`, `username`, `users`, `user_data`.

**After July 22:**
`path_prefix` must end with a slash (`/`). It matches whole path segments, not substrings. `path_prefix="user/"` matches paths starting with `user/` as a directory-style prefix, but not `username/` or `user_data/`.

Additionally, if you pass a `path_prefix` without a trailing slash, you now get a **`400` error**.

**Impact:** Two problems. First, any call using a prefix without a trailing slash will fail with 400. Second, even calls you fix (by adding `/`) may silently return fewer results than before if you were relying on substring matching.

---

## The Header Change

The new behavior is gated behind the `agent-memory-2026-07-22` beta header. Sending this header opts you in **now** — you don't need to wait until July 22.

**Critical rule:** Do **not** combine `agent-memory-2026-07-22` with `managed-agents-2026-04-01` on a single memory store request. Sending both returns a `400` error. This is stated explicitly in [Anthropic's beta headers reference](https://platform.claude.com/docs/en/api/beta-headers#endpoint-specific-headers), which also confirms memory store endpoints (`/v1/memory_stores` and sub-resources) require `agent-memory-2026-07-22` while agent, session, and environment endpoints keep using `managed-agents-2026-04-01`.

```python
# Wrong — 400 error
headers = {
    "anthropic-beta": "managed-agents-2026-04-01, agent-memory-2026-07-22"
}

# Correct — use the new header alone on memory store calls
headers = {
    "anthropic-beta": "agent-memory-2026-07-22"
}
```

If your agent already sends `managed-agents-2026-04-01` globally (e.g., in a shared HTTP client config), you need to strip it and replace it with `agent-memory-2026-07-22` **specifically on memory store endpoint calls**. Other Managed Agents endpoints continue to use `managed-agents-2026-04-01`.

---

## Page Cursor Invalidation

Page cursors issued **without** the `agent-memory-2026-07-22` header are not valid **with** it. If you use pagination over memory results, you must restart from the first page when you adopt the new header. Do not resume from an old cursor — it will not work across the header boundary. Anthropic states this directly in the [memory store documentation](https://platform.claude.com/docs/en/managed-agents/memory) and the [July 2, 2026 release note](https://platform.claude.com/docs/en/release-notes/api): "Page cursors issued without the header aren't valid with it, so restart from the first page when you adopt it."

---

## Migration Checklist

**Find every call to the memory list endpoint:**

```bash
# Search your codebase for memory list calls
grep -r "memory_stores" . --include="*.py"
grep -r "memories.list" . --include="*.py"
grep -r "v1/memory_stores" . --include="*.ts"
```

**For each call, fix these issues before July 22:**

1. **Remove `order_by` and `order` parameters.** Move any sort logic to client-side code.

2. **Audit `depth`.** If you pass `depth=2` or higher, restructure your path hierarchy so a single depth-1 query covers what you need — or make multiple depth-1 calls across sub-prefixes.

3. **Fix `path_prefix`.** Add trailing slash to all prefixes. Verify that the narrower whole-segment matching still returns the memories you expect. Test with your actual stored paths.

4. **Switch the header.** Replace `managed-agents-2026-04-01` with `agent-memory-2026-07-22` on memory store list calls.

5. **Reset pagination.** If you cache page cursors, invalidate them and restart from the first page.

**Before-and-after example:**

```python
# BEFORE — breaks or returns wrong results after July 22
memories = client.beta.memory_stores.memories.list(
    store.id,
    path_prefix="user",        # no trailing slash → 400 error after July 22
    depth=3,                   # invalid → 400 error after July 22
    order_by="updated_at",     # ignored after July 22
    order="desc",              # ignored after July 22
)

# AFTER — correct now, remains correct after July 22
memories = client.beta.memory_stores.memories.list(
    store.id,
    path_prefix="user/",       # trailing slash required
    depth=1,                   # only 0 or 1 valid
    # no order_by/order — sort client-side if needed
)
# Sort client-side if order matters
memories_sorted = sorted(memories, key=lambda m: m.updated_at, reverse=True)
```

---

## Why These Changes (Our Read, Not Anthropic's Stated Rationale)

Anthropic's [release note](https://platform.claude.com/docs/en/release-notes/api) and [memory documentation](https://platform.claude.com/docs/en/managed-agents/memory) describe *what* changes but do not publish an explicit rationale for *why*. The following is our own inference, not a quoted or sourced claim from Anthropic:

- **Stable server ordering** plausibly removes dependence on sort-at-read semantics that could be expensive at scale. Clients that need ordering can sort cheaply in memory.
- **Depth restriction to 0 or 1** plausibly avoids expensive recursive tree traversals. Agent developers who find they need deeper nesting should flatten their path hierarchy or make targeted per-prefix queries.
- **Whole-segment path matching** makes prefix semantics unambiguous — `user/` cannot accidentally match `username/`. This reduces a class of subtle bugs where agents read more (or less) than intended.

---

## Timeline

| Date | Event |
|------|--------|
| Now (July 13, 2026) | `agent-memory-2026-07-22` header available; new behavior opt-in |
| **July 22, 2026** | `managed-agents-2026-04-01` automatically adopts new list behavior on memory endpoints |
| After July 22 | Code sending `depth>=2` or `path_prefix` without trailing slash gets `400`; ordering no longer controllable via API |

**You have 9 days.** The safe path is to adopt `agent-memory-2026-07-22` now, verify your agent in staging, and deploy before July 22.

---

## Bottom Line

Three changes, one deadline. The `order_by`/`order` change is silent — code keeps running but ordering breaks. The `depth` and `path_prefix` changes will throw `400` errors if you have invalid values. Check your codebase now, fix before July 22, and opt into the new header in staging to verify the behavior change doesn't break any memory retrieval logic your agent relies on.
