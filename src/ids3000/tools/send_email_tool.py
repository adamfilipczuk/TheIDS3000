#create a .env file in this directory containing gmail_app_password = "INSERT PASSWORD"
import json
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

import smtplib
import os
from dotenv import load_dotenv

class send_emailInput(BaseModel):
    """Input schema for send_emailTool."""
    message: str = Field(..., description="A message to be sent by email to the manager")

class send_emailTool(BaseTool):
    name: str = "send_email"
    description: str = (
        "This tool sends an email to a pre-set email using preset credentials. All that is required is a message"
    )
    args_schema: Type[BaseModel] = send_emailInput

    def _run(self, message: str) -> str:
        # Implementation goes here
        try:
            send_email(message)
            return "Email Sent Successfully"
        except:
            return "Error Sending Email"

load_dotenv()

HOST = "smtp.gmail.com"
PORT = 465

FROM_EMAIL = "notification.ids3000@gmail.com"
TO_EMAIL = "email@email.com"
PASSWORD = os.getenv("gmail_app_password")

MESSAGEBASE =f"""Subject: Notification from IDS3000
From: {FROM_EMAIL}
To: {TO_EMAIL}

"""
def send_email(Message):
    smtp = smtplib.SMTP_SSL(HOST, PORT)

    response = smtp.ehlo()
    print(f"[*] Echoing the server: {response}")

    response = smtp.login(FROM_EMAIL, PASSWORD)
    print(f"Logging In: {response}")


    smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGEBASE+Message )
    smtp.quit()

