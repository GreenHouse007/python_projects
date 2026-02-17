import os
import smtplib
import ssl
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("EMAIL")
my_password = os.getenv("APP_PASSWORD")

context = ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as connection:
    connection.ehlo()
    connection.starttls(context=context)
    connection.ehlo()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg="Subject: New Email\n\nThis is the body of my email."
    )
