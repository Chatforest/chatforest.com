#!/usr/bin/env python3
"""Mechanical pre-post check for the Bluesky 1-post/day hard cap.

Queries the PUBLIC (no-auth) AT-proto feed endpoint for the account's own
posts and checks whether any post already has createdAt on the current UTC
date. This is the source of truth for "have we posted today" — never
WORKLOG.md, never session/run memory, since each hourly cron run starts with
no memory of what a prior run did.

Usage:
    python3 check_bluesky_posted_today.py
    Exit code 0 + "OK_TO_POST"      -> no post yet today, safe to post
    Exit code 1 + "ALREADY_POSTED"  -> a post already exists today, DO NOT POST
    Exit code 2 + "ERROR: ..."      -> feed fetch failed; treat as unsafe to
                                       post (fail closed) and report the error
"""

import json
import sys
import urllib.request
from datetime import datetime, timezone

ACTOR = "chatforest.bsky.social"
FEED_API = "https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed"


def main():
    url = f"{FEED_API}?actor={ACTOR}&limit=10"
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"ERROR: could not fetch Bluesky feed ({e}). Fail closed: do not post.")
        sys.exit(2)

    today = datetime.now(timezone.utc).date()

    for item in data.get("feed", []):
        record = item.get("post", {}).get("record", {})
        created_at = record.get("createdAt", "")
        try:
            post_date = datetime.fromisoformat(created_at.replace("Z", "+00:00")).date()
        except ValueError:
            continue
        if post_date == today:
            print(f"ALREADY_POSTED: found post at {created_at} (UTC today is {today}). DO NOT POST.")
            sys.exit(1)

    print(f"OK_TO_POST: no post found for UTC today ({today}).")
    sys.exit(0)


if __name__ == "__main__":
    main()
