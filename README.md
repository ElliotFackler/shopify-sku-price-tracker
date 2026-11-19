Create and activate a virtual environment (.venv).

Install the project dependencies:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Make an initial commit for your project structure and dependencies.




Project Guide:
Project Reference: Shopify SKU Price Scraper
Environment & Git Setup
Repo: shopify-sku-price-scraper

Virtual env: .venv (python -m venv .venv, activated before installing/running)

Packages: requests, pytest

Git identity: git config --global user.name "..." and git config --global user.email "..."

Build Milestones (Build Step by Step)
Inspect Data Source: Check <store-url>/products.json (e.g., on a live candle storefront) and map where product title and nested variant sku and price live. Decide how to handle 403/404 or missing /products.json.

Single-Page Fetch -> Pagination: Fetch one page with page and limit parameters, call response.raise_for_status(), parse JSON, and then loop pages until products comes back empty (with polite pacing if needed).

SKU Prefix Filtering: Iterate through product["variants"], guard against None or empty sku values, decide on case sensitivity, and match the prefix.

Output & Precision: Choose what fields to keep per match, use Decimal if doing numeric price math/comparisons, and pick a format (console output, CSV, or JSON).

CLI & Unit Tests: Add CLI arguments (argparse) and write pytest tests using mocked responses so you can test edge cases reliably.