import json
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from pygtail import Pygtail
import os


class observer_toolInput(BaseModel):
    """Input schema for observer_Tool."""
    message: str = Field(..., description="A message to be sent by email to the manager")

class observer_toolTool(BaseTool):
    name: str = "observer_tool"
    description: str = (
        "This tool returns changes in a log file which stores alerts from suricata"
    )
    args_schema: Type[BaseModel] = observer_toolInput

    def _run(self, message: str) -> str:
        # Implementation goes here
        file_to_watch = "eve.json"
        watch_dir = os.path.abspath(
            os.path.join("..", "..", "..", "suricata-tcpreplay", "suricata")
        )
        full_path = os.path.join(watch_dir, file_to_watch)

        try:
            log = ""
            for line in Pygtail(full_path):
                log+= line
            return log
            
        except:
            return "Error Observing"
