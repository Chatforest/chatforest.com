#!/bin/bash
# Post to Blue Sky (AT Protocol)
# Usage: ./post_to_bluesky.sh "Post text" [link_url] [link_title] [link_description]
#
# Blue Sky posts: max 300 graphemes
# Supports an optional external link card (embed)

set -euo pipefail

HANDLE="chatforest.bsky.social"
PASSWORD_FILE="/home/grove/.config/chatforest/blue.sky.password"

# Mechanical 1-post/day gate: the live public feed is the source of truth,
# never WORKLOG/session memory (each cron run has no memory of prior runs —
# that's exactly what caused the 2026-07-27 cap-violation incident, inbox
# #2271). Fails closed: if the check script errors, it exits nonzero and we
# refuse to post.
if ! python3 "$(dirname "$0")/../../scripts/check_bluesky_posted_today.py"; then
  echo "ERROR: pre-post check blocked this post (already posted today, or feed check failed). Not posting." >&2
  exit 1
fi

PASSWORD=$(cat "$PASSWORD_FILE")

export POST_TEXT="$1"
export LINK_URL="${2:-}"
export LINK_TITLE="${3:-}"
export LINK_DESC="${4:-}"

# Step 1: Create session (login)
SESSION=$(curl -s -X POST "https://bsky.social/xrpc/com.atproto.server.createSession" \
  -H "Content-Type: application/json" \
  -d "{\"identifier\": \"$HANDLE\", \"password\": \"$PASSWORD\"}")

export POST_DID=$(echo "$SESSION" | python3 -c "import sys,json; print(json.load(sys.stdin)['did'])" 2>/dev/null)
ACCESS_TOKEN=$(echo "$SESSION" | python3 -c "import sys,json; print(json.load(sys.stdin)['accessJwt'])" 2>/dev/null)

if [ -z "$POST_DID" ] || [ -z "$ACCESS_TOKEN" ]; then
  echo "ERROR: Failed to authenticate with Blue Sky"
  echo "$SESSION"
  exit 1
fi

echo "Authenticated as $POST_DID"

# Step 2: Build the post JSON
export CREATED_AT=$(date -u +"%Y-%m-%dT%H:%M:%S.000Z")

POST_JSON=$(python3 << 'PYEOF'
import json, re, os

text = os.environ["POST_TEXT"]
link_url = os.environ.get("LINK_URL", "")
link_title = os.environ.get("LINK_TITLE", "")
link_desc = os.environ.get("LINK_DESC", "")
created_at = os.environ["CREATED_AT"]
did = os.environ["POST_DID"]

record = {
    "$type": "app.bsky.feed.post",
    "text": text,
    "createdAt": created_at,
    "langs": ["en"],
}

# Detect URLs in text and create link facets
facets = []
for m in re.finditer(r'https?://[^\s\)]+', text):
    url = m.group(0)
    byte_start = len(text[:m.start()].encode('utf-8'))
    byte_end = len(text[:m.end()].encode('utf-8'))
    facets.append({
        "index": {"byteStart": byte_start, "byteEnd": byte_end},
        "features": [{"$type": "app.bsky.richtext.facet#link", "uri": url}]
    })

if facets:
    record["facets"] = facets

# Add external link embed if provided
if link_url:
    record["embed"] = {
        "$type": "app.bsky.embed.external",
        "external": {
            "uri": link_url,
            "title": link_title or "",
            "description": link_desc or "",
        }
    }

payload = {
    "repo": did,
    "collection": "app.bsky.feed.post",
    "record": record,
}

print(json.dumps(payload))
PYEOF
)

# Step 3: Create the post
RESULT=$(curl -s -X POST "https://bsky.social/xrpc/com.atproto.repo.createRecord" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -d "$POST_JSON")

# Check for success
URI=$(echo "$RESULT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('uri',''))" 2>/dev/null)
if [ -n "$URI" ]; then
  echo "Posted successfully: $URI"
else
  echo "ERROR: Failed to post"
  echo "$RESULT"
  exit 1
fi
