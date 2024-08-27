import requests

response = requests.get('http://server-container:8000/ping')
print(response.json())