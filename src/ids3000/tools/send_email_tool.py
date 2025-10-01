#create a .env file in this directory containing gmail_app_password = "INSERT PASSWORD"
import json
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import smtplib
import os
from dotenv import load_dotenv
#import traceback 
# useful for debugging, below code commented with '#debug' will provide traceback
# in stdout()

HOST = "smtp.gmail.com"
PORT = 465
FROM_EMAIL = os.getenv("gmail_email_from_address")
TO_EMAIL = os.getenv("gmail_email_to_address")
PASSWORD = os.getenv("gmail_app_password")
MESSAGEBASE =f"""Subject: Notification from IDS3000
From: {FROM_EMAIL}
To: {TO_EMAIL}

"""

class send_emailInput(BaseModel):
    """Input schema for send_emailTool."""
    message: str = Field(..., description="A message to be sent by email to the manager")

class send_emailTool(BaseTool):
    name: str = "send_email"
    description: str = (
                """Sends a **plain-text** email to a preconfigured address. 
                The argument `message` **must be a single string** that will become the body of the email. 
                Do **not** wrap the text in a JSON object or include a `description` field  just give the raw text."""
    )
    args_schema: Type[BaseModel] = send_emailInput

    def _run(self, message: str) -> str:

        load_dotenv()

        # checks environment variables for validity:
        environment_variables = {
            "FROM_EMAIL": FROM_EMAIL,
            "TO_EMAIL": TO_EMAIL,
            "PASSWORD": PASSWORD
        }
        for name, value in environment_variables.items():
            if value is None:
                raise KeyError(f"Environment variable '{name}' is undefined. Please ensure you have set email environment variables.")

        try:
            send_email(message)
            return "Email Sent Successfully"
        except:
#debug            print("Exception occured in send_email_tool:\n")
#debug            print(traceback.format_exc())
            return "Error Sending Email"

def send_email(message_body):
    smtp = smtplib.SMTP_SSL(HOST, PORT)

    response = smtp.ehlo()
    print(f"[*] Connecting to email server: {response}")

    response = smtp.login(FROM_EMAIL, PASSWORD)
    print(f"Logging In: {response}")


    smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGEBASE+message_body )
    smtp.quit()

