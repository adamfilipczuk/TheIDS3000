**<h1>AI Agents Enhancing Cybersecurity in Cyber Physical Systems (CPS)</h1>**

<img width="1536" height="1024" alt="ChatGPT Image Aug 29, 2025, 05_42_09 PM1" src="https://github.com/user-attachments/assets/abe8771b-0558-4e86-a0b1-591d30552429" />




<h4>Welcome to the IDS3000 detection and response system. This project leverages agentic AI to provide enhanced responses to network threats.</h4>

<img width="375" height="114" alt="crewai-brand-color-2058650934" src="https://github.com/user-attachments/assets/8989944a-3f6b-4469-aad4-364438a4fc69" />

<h4>A brief description of Crewai, Crewai Crews and Crewai Workflows:</h4>

Developed entirely on its own foundation, CrewAI is a rapid and efficient Python framework that operates without LangChain or comparable frameworks.


CrewAI provides developers with an accessible framework that balances ease of use with detailed, low-level customization, making it well-suited for building autonomous AI agents across diverse applications.

• CrewAI Crews: Designed to maximize autonomy and teamwork, allowing developers to build AI groups where each agent is assigned defined roles, tools, and objectives.

• CrewAI Flows: Offer fine-grained, event-based task management, support single LLM calls for precise orchestration, and integrate seamlessly with Crews.

If you would like to know more about Crewai and how to use it, visit the Crewai website [here](https://docs.crewai.com/en/introduction).

## Installation and Setup

Ensure you have **Python >=3.10 <3.13** installed on your system, as well as **Docker** and **Docker Compose**. Ubuntu and Debian systems, including WSL may also require `python3.11-venv`.

To create a virtual environment for running Crewai, and to install basic dependencies; simply run the setup script for your operating system:

### Linux/WSL  
```bash
chmod +x ./setup-linux.sh
./setup-linux.sh
```

### MacOS  
```zsh
chmod +x ./setup-mac.sh
./setup-mac.sh
```

### Windows  
```PowerShell
setup.bat
```
Next, activate the virtual environment to install crewai:

### Linux/WSL/MacOS  
```bash
source .venv/bin/activate
crewai install
```

### Windows  
```PowerShell
.\.venv\Scripts\activate
crewai install
```

### Environment Variables

**Add your `OPENAI_API_KEY` or other LLM key into the `.env` file**

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

### Linux/WSL/MacOS  
```bash
source .venv/bin/activate
crewai run
```

### Windows  
```PowerShell
.\.venv\Scripts\activate
crewai run
```
This command initializes the IDS3000 Crew, assembling the agents and assigning them tasks as defined in the configuration.

### Docker container instructions

The suricata-tcpreplay container integrates **Suricata** and **tcpreplay** to enable live packet replay and analysis. Managed by `docker-compose`, the container is designed for ease of use and system compatibility. It provides basic variables for configuring `tcpreplay` and `suricata`, and exposes Suricata's logs for investigation.

Read the [suricata-tcpreplay container instructions](./suricata-tcpreplay/Readme.md) to set up the container for live packet replay and to give your agents something to work with!

