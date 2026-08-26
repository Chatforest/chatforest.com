#!/usr/bin/env python3
"""Mechanical check for the reply-pilot's link-discipline rule (CEO directive
#2407, 2026-08-26): max 1 chatforest.com link across all replies per UTC
week (rolling 7 days, not calendar week).

Scans the account's own feed (posts_with_replies) for replies in the last 7
days whose facets link to chatforest.com. Source of truth is the live feed,
never WORKLOG/session memory.

Usage:
    python3 check_bluesky_reply_link_this_week.py
    Exit 0 + "OK_TO_LINK"        -> no chatforest.com link in a reply in the last 7 days
    Exit 1 + "LINK_USED: ..."    -> a reply already linked chatforest.com this week
    Exit 2 + "ERROR: ..."        -> feed fetch failed; fail closed, treat as used
"""

import json
import sys
import urllib.request
from datetime import datetime, timedelta, timezone

ACTOR = "chatforest.bsky.social"
FEED_API = "https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed"


def main():
    url = f"{FEED_API}?actor={ACTOR}&filter=posts_with_replies&limit=50"
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"ERROR: could not fetch Bluesky feed ({e}). Fail closed: treat link as used.")
        sys.exit(2)

    cutoff = datetime.now(timezone.utc) - timedelta(days=7)

    for item in data.get("feed", []):
        record = item.get("post", {}).get("record", {})
        if not record.get("reply"):
            continue  # not a reply
        created_at = record.get("createdAt", "")
        try:
            post_dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        except ValueError:
            continue
        if post_dt < cutoff:
            continue
        for facet in record.get("facets", []) or []:
            for feature in facet.get("features", []) or []:
                uri = feature.get("uri", "")
                if "chatforest.com" in uri:
                    print(f"LINK_USED: reply at {created_at} already linked {uri} (within last 7 days).")
                    sys.exit(1)

    print("OK_TO_LINK: no chatforest.com link found in a reply in the last 7 days.")
    sys.exit(0)


if __name__ == "__main__":
    main()
