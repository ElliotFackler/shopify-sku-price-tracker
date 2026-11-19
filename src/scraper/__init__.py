import requests

test_store_url = 'https://paddywax.com' + '/products.json?page=1&limit=10'

response = requests.get(test_store_url, timeout=30)
response.raise_for_status()

print(response.text)