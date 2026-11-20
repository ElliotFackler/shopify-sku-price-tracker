import requests


def fetch_all_products(store_url: str, limit: int = 250):
    complete_url = f"{store_url}/products.json"
    all_products: list[dict] = []
    page = 1

    while True:
        response = requests.get(
            complete_url, 
            params={"page": page, "limit": limit}, 
            timeout=30,
            )
        response.raise_for_status()

        data = response.json()
        products = data.get("products",[])
        if not products:
            break

        print(products[1]['id'])
        print(f"Page: {page}")

        all_products.extend(products)
        page += 1

    return all_products


if __name__ == "__main__":
    items = fetch_all_products("https://paddywax.com", limit=10)
    print(f"Fetched {len(items)} products")