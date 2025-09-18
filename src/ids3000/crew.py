from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from .tools import send_email_tool

#Instantiate Tools
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
            verbose=False
        )
    
    @task
    def suricata_report(self) -> Task:
        return Task(
            config=self.tasks_config['suricata_report'], # type: ignore[index]
        )

    @agent
    def incident_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['incident_manager'], # type: ignore[index]
            verbose=False
        )

    @task
    def incident_planning(self) -> Task:
        return Task(
            config=self.tasks_config['incident_planning'], # type: ignore[index]
        )

    @agent
    def email_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['email_agent'],
            verbose=False,
            tools=[send_email]
        )
    
    @task
    def email_task(self) -> Task:
        return Task(
            config=self.tasks_config['email_task'],
        )

    @agent
    def cisco_admin(self) -> Agent:
        return Agent(
            config=self.agents_config['cisco_admin'], # type: ignore[index]
            verbose=False
        )

    @task
    def cisco_configuration_report(self) -> Task:
        return Task(
            config=self.tasks_config['cisco_configuration_report'], # type: ignore[index]
        )

    @task
    def supply_router_commands(self) -> Task:
        return Task(
            config=self.tasks_config['supply_router_commands'], # type: ignore[index]
        )

    @task
    def supply_switch_commands(self) -> Task:
        return Task(
            config=self.tasks_config['supply_switch_commands'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Ids3000 crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
