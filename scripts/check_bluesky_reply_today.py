#!/usr/bin/env python3
"""Mechanical pre-reply check for the Bluesky reply-engagement pilot's
1-reply/day hard cap (CEO directive #2407, 2026-08-26, pilot through
2026-09-09).

Queries the account's own feed (posts_with_replies filter) and checks
whether any REPLY (a post whose record carries a `reply` field, i.e. it has
a parent/root) already has createdAt on the current UTC date. This cap is
separate from, and in addition to, the existing 1-original-post/day cap
(check_bluesky_posted_today.py) — a day can have at most 1 post AND at most
1 reply, checked independently.

Source of truth is always the live feed, never WORKLOG/session memory — same
discipline as the existing posting-cap gate, since each run starts with no
memory of what a prior run did.

Usage:
    python3 check_bluesky_reply_today.py
    Exit 0 + "OK_TO_REPLY"        -> no reply yet today, safe to reply
    Exit 1 + "ALREADY_REPLIED"    -> a reply already exists today, DO NOT REPLY
    Exit 2 + "ERROR: ..."         -> feed fetch failed; fail closed, do not reply
"""

import json
import sys
import urllib.request
from datetime import datetime, timezone

ACTOR = "chatforest.bsky.social"
FEED_API = "https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed"


def main():
    url = f"{FEED_API}?actor={ACTOR}&filter=posts_with_replies&limit=20"
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"ERROR: could not fetch Bluesky feed ({e}). Fail closed: do not reply.")
        sys.exit(2)

    today = datetime.now(timezone.utc).date()

    for item in data.get("feed", []):
        record = item.get("post", {}).get("record", {})
        if not record.get("reply"):
            continue  # not a reply, an original post
        created_at = record.get("createdAt", "")
        try:
            post_date = datetime.fromisoformat(created_at.replace("Z", "+00:00")).date()
        except ValueError:
            continue
        if post_date == today:
            print(f"ALREADY_REPLIED: found reply at {created_at} (UTC today is {today}). DO NOT REPLY.")
            sys.exit(1)

    print(f"OK_TO_REPLY: no reply found for UTC today ({today}).")
    sys.exit(0)


if __name__ == "__main__":
    main()
