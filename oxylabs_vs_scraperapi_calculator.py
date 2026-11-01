#!/usr/bin/env python3
"""Oxylabs vs ScraperAPI E-Commerce Scraping TCO Calculator 2026."""
import argparse

def calculate(requests_count=1000000):
    # Oxylabs E-Commerce Scraper API: Starts at ~$49/mo for 14k reqs (~$3.50/1k). At 1M reqs, enterprise plan is ~$1,000/mo ($1.00/1k).
    oxylabs_monthly = 1000.0

    # ScraperAPI Startup: 1,000,000 credits for $134.10/mo (annual) or $149/mo (monthly).
    scraperapi_monthly = 134.10

    monthly_savings = oxylabs_monthly - scraperapi_monthly
    annual_savings = monthly_savings * 12.0

    print("=" * 65)
    print(f"Oxylabs vs ScraperAPI: {requests_count:,} Requests Comparison")
    print("=" * 65)
    print(f"Oxylabs E-Commerce API:    ${oxylabs_monthly:.2f}/mo ($1.00 per 1k requests)")
    print(f"ScraperAPI Startup Plan:   ${scraperapi_monthly:.2f}/mo ($0.134 per 1k requests)")
    print(f"Monthly Cost Difference:   ${monthly_savings:.2f}/mo (ScraperAPI is 86.6% cheaper)")
    print(f"Annual Capital Saved:      ${annual_savings:.2f}/yr")
    print("=" * 65)
    return scraperapi_monthly, oxylabs_monthly, annual_savings

if __name__ == "__main__":
    calculate()
