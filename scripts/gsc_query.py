#!/usr/bin/env python3
"""Query Google Search Console API for chatforest.com search analytics."""

import json
import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY_PATH = "/home/grove/.config/chatforest/google-search-console-key.json"
SITE_URL = "sc-domain:chatforest.com"  # domain property
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]


def get_service():
    creds = service_account.Credentials.from_service_account_file(
        KEY_PATH, scopes=SCOPES
    )
    return build("searchconsole", "v1", credentials=creds)


def query_search_analytics(service, start_date, end_date, dimensions=None, row_limit=25):
    dims = dimensions or ["query"]
    body = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": dims,
        "rowLimit": row_limit,
    }
    return service.searchanalytics().query(siteUrl=SITE_URL, body=body).execute()


def main():
    service = get_service()

    # Top queries last 28 days
    print("=== Top Queries (last 28 days) ===")
    try:
        result = query_search_analytics(
            service, "2026-03-18", "2026-04-14",
            dimensions=["query"], row_limit=50
        )
        rows = result.get("rows", [])
        if not rows:
            print("No data returned. (Site may be too new or no impressions yet.)")
        for row in rows:
            q = row["keys"][0]
            clicks = row.get("clicks", 0)
            impressions = row.get("impressions", 0)
            ctr = row.get("ctr", 0) * 100
            position = row.get("position", 0)
            print(f"  {q:60s} clicks={clicks:4.0f}  impr={impressions:6.0f}  ctr={ctr:5.1f}%  pos={position:5.1f}")
    except Exception as e:
        print(f"Error querying search analytics: {e}")
        return

    # Top pages
    print("\n=== Top Pages (last 28 days) ===")
    try:
        result = query_search_analytics(
            service, "2026-03-18", "2026-04-14",
            dimensions=["page"], row_limit=100
        )
        for row in result.get("rows", []):
            page = row["keys"][0].replace("https://chatforest.com", "")
            clicks = row.get("clicks", 0)
            impressions = row.get("impressions", 0)
            ctr = row.get("ctr", 0) * 100
            position = row.get("position", 0)
            print(f"  {page:70s} clicks={clicks:4.0f}  impr={impressions:6.0f}  ctr={ctr:5.1f}%  pos={position:5.1f}")
    except Exception as e:
        print(f"Error: {e}")

    # Top queries by page for top pages
    print("\n=== Query + Page breakdown (last 28 days) ===")
    try:
        result = query_search_analytics(
            service, "2026-03-18", "2026-04-14",
            dimensions=["query", "page"], row_limit=50
        )
        for row in result.get("rows", []):
            q = row["keys"][0]
            page = row["keys"][1].replace("https://chatforest.com", "")
            clicks = row.get("clicks", 0)
            impressions = row.get("impressions", 0)
            position = row.get("position", 0)
            print(f"  {q:40s} {page:50s} clicks={clicks:3.0f}  impr={impressions:5.0f}  pos={position:5.1f}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
