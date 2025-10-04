#create a .env file in this directory containing gmail_app_password = "INSERT PASSWORD"
import json
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import smtplib
import os
from dotenv import load_dotenv
import time
import socket
#import traceback 
# useful for debugging, below code commented with '#debug' will provide traceback
# in stdout()

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

        try:
            send_email(message)
            return "Email Sent Successfully"
        except:
#debug            print("Exception occured in send_email_tool:\n")
#debug            print(traceback.format_exc())
            return "Error Sending Email"

load_dotenv()

HOST = "smtp.gmail.com"
PORTS = [465, 587]
RETRIES = 3 # number of retries for both ports
LOOPS = 3 #number of loops over both ports
DELAY = 5 #seconds between retries
HOST_DELAY = 15 #seconds to wait for host to respond

FROM_EMAIL = os.getenv("gmail_email_from_address")
TO_EMAIL = os.getenv("gmail_email_to_address")
PASSWORD = os.getenv("gmail_app_password")

# checks environment variables for validity:
environment_variables = {
    "FROM_EMAIL": FROM_EMAIL,
    "TO_EMAIL": TO_EMAIL,
    "PASSWORD": PASSWORD
}
for name, value in environment_variables.items():
    if value is None:
        raise KeyError(f"Environment variable '{name}' is undefined. Please ensure you have set email environment variables.")


MESSAGEBASE =f"""Subject: Notification from IDS3000
From: {FROM_EMAIL}
To: {TO_EMAIL}

"""
def send_email(message_body):
    tries = 0
    loop = 0
    port_index = 0
    host_down = 0

    while loop < LOOPS:
        port = PORTS[port_index]
        try:
            if port == 465:
                smtp = smtplib.SMTP_SSL(HOST, port, timeout=10)
            else:
                smtp = smtplib.SMTP(HOST, port, timeout=10)
                smtp.starttls()

            response = smtp.ehlo()
            print(f"[*] Connecting to email server: {response}")

            response = smtp.login(FROM_EMAIL, PASSWORD)
            print(f"Logging In: {response}")


            smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGEBASE+message_body )    
            smtp.quit()
            return True

        except (socket.gaierror, socket.herror, socket.timeout):
            host_down += 1
            if host_down >= RETRIES:
                print("Error sending email: Host down, aborting email send")
                return False
            print(f"Error sending email: Host down, retrying in {HOST_DELAY} seconds...")
            time.sleep(HOST_DELAY)
            continue

        except (socket.timeout, ConnectionRefusedError, OSError) as e:
            print(f"Error sending email on port {port}: retrying in 5 seconds...")
            port_index = (port_index + 1) % len(PORTS)
                
        tries += 1
        if tries >= RETRIES:
            tries = 0
            loop += 1
        time.sleep(DELAY)

    if loop >= LOOPS:
        print("Error sending email: Max retries reached, dropping email")
        return False

