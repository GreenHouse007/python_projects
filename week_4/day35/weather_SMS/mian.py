import requests

import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("EMAIL")
my_password = os.getenv("APP_PASSWORD")
my_number = os.getenv("MY_NUMBER")

msg = EmailMessage()
msg.set_content("Bring an umbrella. ☂️")
msg["Subject"] = "Rain is Coming"
msg["From"] = my_email
msg["To"] = my_number

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OWM_API_KEY")


weather_params = {
    "lat": 40.534271,
    "lon": -112.298447,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
#print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if 200 <= condition_code < 700:
        will_rain = True
if will_rain:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(my_email, my_password)
        smtp.send_message(msg)





