import requests

response = requests.get('https://api.telegram.org/bot6994561004:AAGLrnpXG8UrqFPI6R1ZnN2Uv6I_M0nePCI/getupdates')

print(response.json())