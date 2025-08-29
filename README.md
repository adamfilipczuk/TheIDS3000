**<h1>AI Agents Enhancing Cybersecurity in Cyber Physical Systems (CPS)</h1>**

<img width="1536" height="1024" alt="ChatGPT Image Aug 29, 2025, 05_42_09 PM1" src="https://github.com/user-attachments/assets/abe8771b-0558-4e86-a0b1-591d30552429" />




<h4>Welcome to the IDS3000 detection and response system. This project leverages agentic AI to provide enhanced responses to network threats.</h4>

## Installation and Setup

Ensure you have **Python >=3.10 <3.13** installed on your system, as well as **Docker** and **Docker Compose**. 

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

