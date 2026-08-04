#!/usr/bin/env python3
"""Post to BlueSky via AT Protocol REST API."""

import json
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HANDLE = "chatforest.bsky.social"
PASSWORD_FILE = "/home/grove/.config/chatforest/blue.sky.password"
API = "https://bsky.social/xrpc"
PUBLIC_FEED_API = "https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed"
TUESDAY_RESERVATION_SCRIPT = Path(__file__).with_name("check_tuesday_dispatch_reservation.py")


def tuesday_slot_reserved():
    """Mechanical Tuesday gate (CEO directive, inbox #2301, 2026-08-04): on UTC
    Tuesdays the day's single post is reserved for the Dispatch newsletter plug
    until that week's Dispatch has actually sent. See
    check_tuesday_dispatch_reservation.py and CLAUDE.md 'Bluesky cross-posting
    rules'. Fails closed: any error blocks the post."""
    result = subprocess.run(
        [sys.executable, str(TUESDAY_RESERVATION_SCRIPT)],
        capture_output=True, text=True,
    )
    print(result.stdout.strip())
    if result.returncode not in (0,):
        return True
    return False


def already_posted_today():
    """Mechanical 1-post/day gate: query the account's own public feed (source
    of truth, never WORKLOG/session memory) and check for a post already
    dated today (UTC). Fails closed: any fetch error blocks the post.
    See CLAUDE.md 'Bluesky cross-posting rules' (inbox #2271 incident)."""
    url = f"{PUBLIC_FEED_API}?actor={HANDLE}&limit=10"
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"ERROR: could not verify feed before posting ({e}). Refusing to post (fail closed).")
        return True

    today = datetime.now(timezone.utc).date()
    for item in data.get("feed", []):
        created_at = item.get("post", {}).get("record", {}).get("createdAt", "")
        try:
            post_date = datetime.fromisoformat(created_at.replace("Z", "+00:00")).date()
        except ValueError:
            continue
        if post_date == today:
            print(f"BLOCKED: a Bluesky post already exists today ({created_at}). 1/day hard cap. Not posting.")
            return True
    return False


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
    """Create a facet for a link. start_text is the display text to find in text."""
    start = text.encode("utf-8").index(start_text.encode("utf-8"))
    end = start + len(start_text.encode("utf-8"))
    return {
        "index": {"byteStart": start, "byteEnd": end},
        "features": [{"$type": "app.bsky.richtext.facet#link", "uri": url}],
    }


def post(text, facets=None):
    session = create_session()
    record = {
        "$type": "app.bsky.feed.post",
        "text": text,
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "langs": ["en"],
    }
    if facets:
        record["facets"] = facets
    result = api_call("com.atproto.repo.createRecord", {
        "repo": session["did"],
        "collection": "app.bsky.feed.post",
        "record": record,
    }, token=session["accessJwt"])
    print(f"Posted: {result['uri']}")
    return result


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("Usage: post_bluesky.py <text> [link_text=url ...]")
        print("There is no --help lookup: argv[1] is posted verbatim as the live post text.")
        sys.exit(0 if len(sys.argv) >= 2 else 1)

    if already_posted_today():
        sys.exit(1)

    if tuesday_slot_reserved():
        sys.exit(1)

    text = sys.argv[1]
    facets = []
    for arg in sys.argv[2:]:
        if "=" in arg:
            link_text, url = arg.split("=", 1)
            try:
                facets.append(make_link_facet(text, url, link_text))
            except ValueError:
                print(f"Warning: '{link_text}' not found in text, skipping facet")

    post(text, facets if facets else None)
