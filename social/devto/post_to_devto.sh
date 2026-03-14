#!/bin/bash
# Post an article to dev.to using their API
# Usage: ./post_to_devto.sh <markdown_file>
#
# The markdown file should have dev.to frontmatter (title, description, tags, canonical_url)
# Articles are created as drafts (published: false) by default

set -euo pipefail

API_KEY_FILE="/home/grove/.config/chatforest/devto_api_key"

if [ ! -f "$API_KEY_FILE" ]; then
    echo "ERROR: API key file not found at $API_KEY_FILE"
    echo "Rob needs to generate one from dev.to Settings > Extensions > API Keys"
    exit 1
fi

API_KEY=$(cat "$API_KEY_FILE")
ARTICLE_FILE="${1:?Usage: $0 <markdown_file>}"

if [ ! -f "$ARTICLE_FILE" ]; then
    echo "ERROR: Article file not found: $ARTICLE_FILE"
    exit 1
fi

# Read the markdown content
BODY_MARKDOWN=$(cat "$ARTICLE_FILE")

# Post to dev.to API
curl -s -X POST "https://dev.to/api/articles" \
    -H "api-key: $API_KEY" \
    -H "Content-Type: application/json" \
    -d "$(jq -n --arg body "$BODY_MARKDOWN" '{"article": {"body_markdown": $body}}')" \
    | jq '.'

echo ""
echo "Article posted (as draft). Check https://dev.to/dashboard to review and publish."
