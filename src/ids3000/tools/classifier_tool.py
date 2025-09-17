from tools.classifier import classify_eve
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
                """This runs eve.json alert data through an AI classifier to advise on porbability of maliciousness"""
    )
    args_schema: Type[BaseModel] = send_emailInput

    def _run(self, eveData: str) -> str:

        try:
            
            return classify_eve(eveData)
        except:
            return "Error with Classification"

