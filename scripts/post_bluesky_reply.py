#!/usr/bin/env python3
"""Post a reply to a Bluesky thread (reply-engagement pilot, CEO directive
#2407, 2026-08-26, pilot through 2026-09-09).

Mechanical gates enforced here, not left to agent discretion:
- 1 reply/day hard cap (check_bluesky_reply_today.py), separate from and in
  addition to the existing 1-original-post/day cap.
- Max 1 chatforest.com link per rolling 7 days across all replies
  (check_bluesky_reply_link_this_week.py) — only checked if a link arg is
  passed; replying with a fact + primary source and no chatforest.com link
  is the default and unlimited.

Substance standard (thread is on-topic + reply adds a concrete verifiable
fact) and tone/disclosure rules are judgment calls made by the agent before
invoking this script — see CLAUDE.md "Bluesky reply-engagement pilot".

Usage:
    python3 post_bluesky_reply.py <parent_uri> <parent_cid> <root_uri> <root_cid> <text> [link_text=url ...]

    For a reply to a top-level post, root == parent (same uri/cid).
"""

import json
import sys
import subprocess
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HANDLE = "chatforest.bsky.social"
PASSWORD_FILE = "/home/grove/.config/chatforest/blue.sky.password"
API = "https://bsky.social/xrpc"
REPLY_CAP_SCRIPT = Path(__file__).with_name("check_bluesky_reply_today.py")
LINK_WEEKLY_SCRIPT = Path(__file__).with_name("check_bluesky_reply_link_this_week.py")


def already_replied_today():
    result = subprocess.run([sys.executable, str(REPLY_CAP_SCRIPT)], capture_output=True, text=True)
    print(result.stdout.strip())
    return result.returncode != 0


def link_used_this_week():
    result = subprocess.run([sys.executable, str(LINK_WEEKLY_SCRIPT)], capture_output=True, text=True)
    print(result.stdout.strip())
    return result.returncode != 0


def api_call(endpoint, data, token=None):
    req = urllib.request.Request(
        f"{API}/{endpoint}",
        data=json.dumps(data).encode(),
        headers={"Content-Type": "application/json"},
    )
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def create_session():
    with open(PASSWORD_FILE) as f:
        password = f.read().strip()
    return api_call("com.atproto.server.createSession", {
        "identifier": HANDLE,
        "password": password,
    })


def make_link_facet(text, url, start_text):
    start = text.encode("utf-8").index(start_text.encode("utf-8"))
    end = start + len(start_text.encode("utf-8"))
    return {
        "index": {"byteStart": start, "byteEnd": end},
        "features": [{"$type": "app.bsky.richtext.facet#link", "uri": url}],
    }


def reply(parent_uri, parent_cid, root_uri, root_cid, text, facets=None):
    session = create_session()
    record = {
        "$type": "app.bsky.feed.post",
        "text": text,
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "langs": ["en"],
        "reply": {
            "root": {"uri": root_uri, "cid": root_cid},
            "parent": {"uri": parent_uri, "cid": parent_cid},
        },
    }
    if facets:
        record["facets"] = facets
    result = api_call("com.atproto.repo.createRecord", {
        "repo": session["did"],
        "collection": "app.bsky.feed.post",
        "record": record,
    }, token=session["accessJwt"])
    print(f"Replied: {result['uri']}")
    return result


if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: post_bluesky_reply.py <parent_uri> <parent_cid> <root_uri> <root_cid> <text> [link_text=url ...]")
        sys.exit(1)

    if already_replied_today():
        sys.exit(1)

    parent_uri, parent_cid, root_uri, root_cid, text = sys.argv[1:6]
    remaining = sys.argv[6:]

    has_link_arg = any("=" in a for a in remaining)
    if has_link_arg and link_used_this_week():
        print("BLOCKED: link-discipline cap (max 1 chatforest.com link/week) already used. Not posting with link.")
        sys.exit(1)

    facets = []
    for arg in remaining:
        if "=" in arg:
            link_text, url = arg.split("=", 1)
            try:
                facets.append(make_link_facet(text, url, link_text))
            except ValueError:
                print(f"Warning: '{link_text}' not found in text, skipping facet")

    reply(parent_uri, parent_cid, root_uri, root_cid, text, facets if facets else None)
