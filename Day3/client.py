# import requests

# response = requests.get('http://server:8000/ping')
# print(response.json())

import time
import requests

for _ in range(5):  # Try 5 times
    try:
        response = requests.get('http://server:8000/ping')
        print(response.json())
        break
    except requests.exceptions.ConnectionError:
        print("Server not ready, retrying...")
        time.sleep(5)  # Wait for 5 seconds before retrying