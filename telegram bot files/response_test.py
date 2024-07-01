import requests

response = requests.get('https://api.telegram.org/bot<api_key>/getupdates')

print(response.json())