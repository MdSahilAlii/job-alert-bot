import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

def send_email(job_listings):
    if not job_listings:
        return

    body = "Hi Sahil,\n\nHere are today's fresher job listings:\n\n" + "\n\n".join(job_listings)
    body += "\n\n– Your Job Bot 🤖"

    msg = MIMEText(body)
    msg['Subject'] = "🧑‍💻 Daily Job Alerts - Fresher Dev Roles"
    msg['From'] = EMAIL
    msg['To'] = TO_EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, APP_PASSWORD)
        server.send_message(msg)
