import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

APP_ID = os.getenv("x-app-id")
API_KEY = os.getenv("x-app-key")

GENDER = os.getenv("gender")
WEIGHT_KG = int(os.getenv("weight"))
HEIGHT_CM = int(os.getenv("height"))
AGE = int(os.getenv("age"))

TOKEN = os.getenv("token")


exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_endpoint = os.getenv("sheety")

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    authorization_header = {
        "Authorization": TOKEN
    }

    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=authorization_header
    )

    print(sheet_response.text)