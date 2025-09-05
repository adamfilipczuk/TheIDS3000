**<h1>AI Agents Enhancing Cybersecurity in Cyber Physical Systems (CPS)</h1>**

<img width="1024" height="700" alt="ChatGPT Image Aug 29, 2025, 05_42_09 PM1" src="https://github.com/user-attachments/assets/abe8771b-0558-4e86-a0b1-591d30552429" />




<h4>Welcome to the IDS3000 detection and response system. This project leverages agentic AI to provide enhanced responses to network threats.</h4>

<img width="375" height="114" alt="crewai-brand-color-2058650934" src="https://github.com/user-attachments/assets/8989944a-3f6b-4469-aad4-364438a4fc69" />

<h4>A brief description of Crewai, Crewai Crews and Crewai Workflows:</h4>

Developed entirely on its own foundation, CrewAI is a rapid and efficient Python framework that operates without LangChain or comparable frameworks.


CrewAI provides developers with an accessible framework that balances ease of use with detailed, low-level customization, making it well-suited for building autonomous AI agents across diverse applications.

• CrewAI Crews: Designed to maximize autonomy and teamwork, allowing developers to build AI groups where each agent is assigned defined roles, tools, and objectives.

• CrewAI Flows: Offer fine-grained, event-based task management, support single LLM calls for precise orchestration, and integrate seamlessly with Crews.

If you would like to know more about Crewai and how to use it, visit the Crewai website [here](https://docs.crewai.com/en/introduction).

## Installation and Setup

<img width="375" height="200" alt="Docker-Logo-2015-2017-1067899226" src="https://github.com/user-attachments/assets/43d7da2a-69e5-4698-83fa-07506761119f" />       <img width="375" height="200" alt="python-logo-800x500-2157912460" src="https://github.com/user-attachments/assets/52282daf-342a-4095-bb23-fa5c864bb87a" />




Ensure you have **Python >=3.10 <3.13**, **Docker** and **Docker Compose** installed on your system. Linux and WSL users may also need `python-venv` and `pip` if they are not installed with python. To check Python3 is installed and the version number, run the command `python3 --version` or `python --version`. Docker and Compose installation instructions are available at [the Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/) installation reference pages.

To create a virtual environment for running Crewai, and to install further dependencies; simply run the setup script for your operating system:

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

### Environment Variables

Add your `OPENAI_API_KEY` or other LLM key into the `.env` file. Most ollama users will need to add the following to their `.env`:
```
MODEL=ollama/llama3
API_BASE=http://localhost:11434
```
See CrewAI's [LLM reference page](https://docs.crewai.com/en/concepts/llms) for more info and examples for other LLM configurations.

Add an app password for the gmail mail sending tool with the format `gmail_app_password = "your app password"` to the `.env` file. See [Gmail - Sign in with app passwords](https://support.google.com/mail/answer/185833?hl=en) for more info on app passwords.


Next, activate the virtual environment for crewai:

### Linux/WSL/MacOS  
```bash
source .venv/bin/activate
```

### Windows  
```PowerShell
call .\.venv\Scripts\activate
```


## Running the Project

To kickstart your crew of AI agents, run this from the root folder of your project:

### Linux/WSL/MacOS  
```bash
crewai run
```

### Windows  
```PowerShell
crewai run
```

This command initializes the IDS3000 Crew, assembling the agents and assigning them tasks as defined in the configuration.

### Alert tracking

To start tracking Suricata alerts, first activate the virtual environment as described in the project setup section, then navigate to `./src/ids3000/alert_tracker/` and run the alert tracking tool:

### Linux/WSL
```bash
python3 alert_tracker.py
```

### MacOS 
```bash
python alert_tracker.py
```

### Windows 
```powershell
python alert_tracker.py
```

### Docker container instructions

To give your agents something to work with, in a separate terminal, navigate to the `suricata-tcpreplay` folder, create a folder labelled `captures` and provide a packet capture labelled `capture.pcap` for the system to analyse. To build and start the container simply run `docker compose up`. 

Detailed instructions are found below.

<img width="375" height="200" alt="0Z2J8xXd3X0SJuphA-3239266095" src="https://github.com/user-attachments/assets/ff7dc5e7-a454-4014-a7b2-2045cd0c15e1" />

The suricata-tcpreplay container integrates **Suricata** and **tcpreplay** to enable live packet replay and analysis. Managed by `docker-compose`, the container is designed for ease of use and system compatibility. It provides basic variables for configuring `tcpreplay` and `suricata`, and exposes Suricata's logs for investigation.

Read the [suricata-tcpreplay container instructions](./suricata-tcpreplay/Readme.md) to set up the container for live packet replay and to give your agents something to work with!

