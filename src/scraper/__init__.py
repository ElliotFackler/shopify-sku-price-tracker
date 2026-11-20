from client import fetch_all_products


if __name__ == "__main__":
    items = fetch_all_products("https://paddywax.com", limit=10)
    print(f"Fetched {len(items)} products")