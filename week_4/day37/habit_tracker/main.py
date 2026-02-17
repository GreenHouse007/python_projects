import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = os.getenv("PIXELA_GRAPH_ID")

if not USERNAME or not TOKEN or not GRAPH_ID:
    raise ValueError("Missing PIXELA_USERNAME / PIXELA_TOKEN / PIXELA_GRAPH_ID in .env")

pixela_endpoint = "https://pixe.la/v1/users"

headers = {"X-USER-TOKEN": TOKEN}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

## POST
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Water Drinking",
    "unit": "cups",
    "type": "float",
    "color": "ajisai"
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": input("How much water did you drink today? "),
}

res = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print("Create pixel:", res.status_code, res.text)



update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

new_pixel_data = {
    "quantity": "4.5"
}

## PUT
# res = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(res.text)



delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"


## DELETE
# res = requests.delete(url=delete_endpoint, headers=headers)
# print(res.text)

