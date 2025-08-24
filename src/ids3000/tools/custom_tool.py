import json
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."

class LogParserInput(BaseModel):
    """Input schema for LogParser"""
    filename: str = Field(..., description="file name or path to file.")

class LogParserTool(BaseTool):
    name: str = "LogParser"
    description: str = "This tool parses a suricata eve.json file and provides the alerts in a human readable format."
    args_schema: Type[BaseModel] = LogParserInput

    def _run(self, filename: str) -> str:
        signatures = {}
        categories = {}

        try:
            with open(filename, 'r') as f:
                for line in f:
                    try:
                        event = json.loads(line)
                        if 'alert' in event:
                            if 'signature' in event['alert']:
                                signature = event['alert']['signature']
                                signatures[signature] = signatures.get(signature, 0) + 1
                            if 'category' in event['alert']:
                                category = event['alert']['category']
                                categories[category] = categories.get(category, 0) + 1
                    except json.JSONDecodeError:
                        continue
        except FileNotFoundError:
            return f"Error: File not found at {filename}"

        sorted_signatures = sorted(signatures.items(), key=lambda item: item[1], reverse=True)
        sorted_categories = sorted(categories.items(), key=lambda item: item[1], reverse=True)

        output = 'Unique signatures and their counts:\n'
        for signature, count in sorted_signatures:
            output += f'  {signature}: {count}\n'

        output += '\nUnique categories and their counts:\n'
        for category, count in sorted_categories:
            output += f'  {category}: {count}\n'
        
        return output

