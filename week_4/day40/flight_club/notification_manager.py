import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:

    def __init__(self):
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("APP_PASSWORD")
        self.to_number = os.getenv("MY_NUMBER")
        self.smtp_address = os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]

    def send_sms(self, message_body):
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(self.email, self.password)
            msg = EmailMessage()
            msg.set_content(message_body)
            msg["Subject"] = "Flight Deal Alert"
            msg["From"] = self.email
            msg["To"] = self.to_number
            smtp.send_message(msg)
        print("Message sent successfully.")

    def send_emails(self, email_list, email_body):
        with smtplib.SMTP(self.smtp_address) as connection:
            connection.starttls()
            connection.login(self.email, self.password)
            for email in email_list:
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )