import requests

response = requests.get("https://api.github.com")
data = response.json()

print(f"Status code: {response.status_code}")
print(f"Current user URL: {data['current_user_url']}")
print(f"Emojis URL: {data['emojis_url']}")