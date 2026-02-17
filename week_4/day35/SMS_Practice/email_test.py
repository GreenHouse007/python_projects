import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("EMAIL")
my_password = os.getenv("APP_PASSWORD")
my_number = os.getenv("MY_NUMBER")

msg = EmailMessage()
msg.set_content("Hello from a script!")
msg["Subject"] = "Testing"
msg["From"] = my_email
msg["To"] = my_number

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(my_email, my_password)
    smtp.send_message(msg)
