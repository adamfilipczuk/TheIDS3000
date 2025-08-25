from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import (FileReadTool, DirectoryReadTool) # type: ignore
from .tools import custom_tool,send_email_tool

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

#instantiate tools
log_parser=custom_tool.LogParserTool()
file_read = FileReadTool(file_path='./knowledge/eve.json')
directory_read = DirectoryReadTool()
send_email = send_email_tool.send_emailTool()

@CrewBase
class Ids3000():
    """Ids3000 crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def suricata_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['suricata_analyst'], # type: ignore[index]
            verbose=True,
            tools=[log_parser, file_read, directory_read]
        )
    
    @agent
    def email_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['email_agent'],
            verbose=True,
            tools=[send_email]
        )

    # @agent
    # def incident-responder(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['incident-responder'], # type: ignore[index]
    #         verbose=True,
    #         tools=[]
    #     )

    @task
    def alerts_overview(self) -> Task:
        return Task(
            config=self.tasks_config['alerts_overview'], #type: ignore[index]
        )

    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task'], #type: ignore[index]
            output_file='analysis.md'
        )
    
    @task
    def email_task(self) -> Task:
        return Task(
            config=self.tasks_config['email_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, #Automatically created by the @agent decorator
            tasks=self.tasks, #Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
