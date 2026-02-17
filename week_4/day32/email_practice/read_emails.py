import os
import imaplib
import email
from email.header import decode_header
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("EMAIL")
my_password = os.getenv("APP_PASSWORD")

imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(my_email, my_password)
imap.select("INBOX")

status, messages = imap.search(None, "ALL")
mail_ids = messages[0].split()

latest_5 = mail_ids[-5:]
for mail_id in reversed(latest_5):
    status, msg_data = imap.fetch(mail_id, "(RFC822)")

    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])

            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8")

            from_ = msg.get("From")

            print("From:", from_)
            print("Subject:", subject)
            print("-" * 50)

imap.logout()
