#!/usr/bin/env python3
"""Query Google Search Console API for chatforest.com search analytics."""

import json
import sys
import argparse
from datetime import date, timedelta
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


def query_search_analytics(service, start_date, end_date, dimensions=None,
                            row_limit=25, page_filter=None, sort_by="clicks"):
    dims = dimensions or ["query"]
    body = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": dims,
        "rowLimit": row_limit,
    }
    if page_filter:
        body["dimensionFilterGroups"] = [{
            "filters": [{
                "dimension": "page",
                "operator": "contains",
                "expression": page_filter,
            }]
        }]
    return service.searchanalytics().query(siteUrl=SITE_URL, body=body).execute()


def date_range(days):
    end = date.today() - timedelta(days=2)  # GSC data lags ~2 days
    start = end - timedelta(days=days - 1)
    return start.isoformat(), end.isoformat()


def main():
    parser = argparse.ArgumentParser(description="Query GSC for chatforest.com")
    parser.add_argument("--days", type=int, default=28, help="Number of days back")
    parser.add_argument("--limit", type=int, default=50, help="Max rows")
    parser.add_argument("--page", default=None, help="Filter queries to this page path substring")
    args = parser.parse_args()

    start_date, end_date = date_range(args.days)
    service = get_service()

    if args.page:
        # Page-specific mode: show top queries landing on that page
        print(f"=== Top Queries for {args.page} (last {args.days} days: {start_date} to {end_date}) ===")
        try:
            result = query_search_analytics(
                service, start_date, end_date,
                dimensions=["query"],
                row_limit=args.limit,
                page_filter=args.page,
            )
            rows = result.get("rows", [])
            if not rows:
                print("No data returned.")
            for row in rows:
                q = row["keys"][0]
                clicks = row.get("clicks", 0)
                impressions = row.get("impressions", 0)
                ctr = row.get("ctr", 0) * 100
                position = row.get("position", 0)
                print(f"  {q:60s} clicks={clicks:4.0f}  impr={impressions:6.0f}  ctr={ctr:5.1f}%  pos={position:5.1f}")
        except Exception as e:
            print(f"Error: {e}")
        return

    # Default mode: top queries, top pages, query+page breakdown
    print(f"=== Top Queries (last {args.days} days: {start_date} to {end_date}) ===")
    try:
        result = query_search_analytics(
            service, start_date, end_date,
            dimensions=["query"], row_limit=args.limit,
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

    print(f"\n=== Top Pages (last {args.days} days) ===")
    try:
        result = query_search_analytics(
            service, start_date, end_date,
            dimensions=["page"], row_limit=args.limit,
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

    print(f"\n=== Query + Page breakdown (last {args.days} days) ===")
    try:
        result = query_search_analytics(
            service, start_date, end_date,
            dimensions=["query", "page"], row_limit=args.limit,
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
