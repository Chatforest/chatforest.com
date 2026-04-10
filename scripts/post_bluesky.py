#!/usr/bin/env python3
"""Post to BlueSky via AT Protocol REST API."""

import json
import sys
import urllib.request
from datetime import datetime, timezone

HANDLE = "chatforest.bsky.social"
PASSWORD_FILE = "/home/grove/.config/chatforest/blue.sky.password"
API = "https://bsky.social/xrpc"


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
    if len(sys.argv) < 2:
        print("Usage: post_bluesky.py <text> [link_text=url ...]")
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
