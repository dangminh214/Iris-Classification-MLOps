import requests # type: ignore

import json

data = {"features": [5, 6, 7, 8]}

url = "http://127.0.0.1:8888/predict/"

data = json.dumps(data) 

response = requests.post(url, data=data, headers={"Content-Type": "application/json"})  # Ensure correct content type

print(response.json())
