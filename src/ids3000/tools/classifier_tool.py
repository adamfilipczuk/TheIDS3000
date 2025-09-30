from .classifier.classifier import classify_eve
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
#import traceback 
# useful for debugging, below code commented with '#debug' will provide traceback
# in stdout()

class classifierInput(BaseModel):
    """Input schema for Classifier Tool."""
    message: str = Field(..., description="A string of event data can be passed to this tool, it will classify probability of maliciousness, then return the data. ")

class classifier_Tool(BaseTool):
    name: str = "classifier_tool"
    description: str = (
                """This runs eve.json alert data through an AI classifier to advise on porbability of maliciousness"""
    )
    args_schema: Type[BaseModel] = classifierInput

    def _run(self, message: str) -> str:

        try:
            
            return classify_eve(message)
        except:
#debug            print("Exception occured in classifier_tool:\n") 
#debug            print(traceback.format_exc())
            return "Error with Classification"

