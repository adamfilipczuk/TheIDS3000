# AI Agents Enhancing Cybersecurity in Cyber Physical Systems - IDS3000
<img width="1024" height="700" alt="IDS3000 Logo" src="https://github.com/user-attachments/assets/abe8771b-0558-4e86-a0b1-591d30552429" />

Welcome to the IDS3000 detection and response system. The project leverages agentic AI to provide enhanced responses to network threats. The system is currently trained to work with 4 network captures from the IoT-23 Internet of Things dataset:  
**Malicious**
- `CTU-IoT-Malware-Capture-34-1` (Mirai)
- `CTU-IoT-Malware-Capture-3-1` (Muhstik)  

**Benign**
- `CTU-Honeypot-Capture-4-1` (Phillips Hue)
- `CTU-Honeypot-Capture-5-1` (Amazon Alexa)

- [IoT-23 Dataset Homepage](https://www.stratosphereips.org/datasets-iot23)
- [IoT-23 Dataset Files](https://mcfp.felk.cvut.cz/publicDatasets/IoT-23-Dataset/)

## Contents
- [**Installation and Setup**](#installation-and-setup)
    - [**Dependencies**](#dependencies)
    - [**CrewAI Setup**](#crewai-setup)
    - [**Environment Variables**](#environment-variables)
    - [**Additional Configuration**](#additional-configuration)
         - [**Tensorflow Model**](#tensorflow-model-configuration)
         - [**Docker Container Instructions**](#docker-container-instructions)
### More information
- [**suricata-tcpreplay container advanced configuration**](./suricata-tcpreplay/Readme.md)
- [**Tensorflow model training instructions**](./src/ids3000/tools/classifier/Readme.md)
- [**File Index**](<./File Index.md>)

## Installation and Setup
### Dependencies
Ensure you have **Python >=3.10 <3.13**, **Docker** and **Docker Compose** installed on your system. Linux and WSL users may also need `python-venv` and `pip` if they are not installed with python. To check Python3 is installed and the version number, run the command `python3 --version` or `python --version`. Docker and Compose installation instructions are available at [the Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/) installation reference pages.

### CrewAI Setup
To create a virtual environment for running Crewai, and to install further dependencies; simply run the setup script for your operating system:

#### Linux/WSL  
```bash
chmod +x ./setup-linux.sh
./setup-linux.sh
```

#### MacOS  
```zsh
chmod +x ./setup-mac.sh
./setup-mac.sh
```

#### Windows  
```PowerShell
setup.bat
```

#### Environment Variables
LLM configuration and the Gmail API are managed using environment variables. Add these variables to the `.env` file at the project root:

##### LLM Setup
LLM Configuration differs depending on your LLM provider. OpenAI and Ollama instructions are provided below. For more information, see the [CrewAI LLMs](https://docs.crewai.com/en/concepts/llms) documentation.

###### OpenAI API
Add your `OPENAI_API_KEY` or other LLM key into the `.env` file located at the root of the project. You may also add a [model supported by CrewAI](https://docs.crewai.com/en/concepts/llms#openai).

If using OpenAI, the `.env` file will look similar to below:
```bash
#MODEL=openai/gpt-4o-mini
OPENAI_API_KEY=INSERT_KEY_HERE
```

###### Ollama
Add your Ollama address and port, as well as the model. Model names must be defined when using Ollama.

If using Ollama, the `.env` file will look similar to below:
```bash
MODEL=ollama/llama3
API_BASE=http://localhost:11434
```

See CrewAI's [LLM reference page](https://docs.crewai.com/en/concepts/llms) for more info and examples for other LLM configurations.

##### Tools Email .env
The IDS3000 uses gmail to communicate actions so they can be managed asyncronously. Add the following environment variables to your `.env` file and replace the definitions.
```bash
gmail_email_from_address = "email@example.com"
gmail_email_to_address = "email@gmail.com"
gmail_app_password = "apdj pass word"
```

See [Gmail - Sign in with app passwords](https://support.google.com/mail/answer/185833?hl=en) for more info on gmail app passwords, these are different to a normal gmail password. 

#### Additional Configuration

##### Tensorflow model configuration
Due to size, the Tensorflow classifier model is not distributed in the git repository. You will need to add the tensorflow `.keras` files to the `src/ids3000/tools/classifier/saved_model` folder before running the project. You may also train the model by following the [Tensorflow model training instructions](./src/ids3000/tools/classifier/Readme.md).

### Docker container instructions
To give your agents something to work with, in a separate terminal, navigate to the `suricata-tcpreplay` folder, create a folder labelled `captures` and provide a packet capture [from the IoT-23 dataset](https://mcfp.felk.cvut.cz/publicDatasets/IoT-23-Dataset/IndividualScenarios/) labelled `capture.pcap` for the system to analyse. To build and start the container simply run `docker compose up`. This may take some time on first run, while waiting for the image to build. Detailed instructions are available at the [suricata-tcpreplay container advanced configuration](./suricata-tcpreplay/Readme.md) page.

### Project Run
After [starting the Docker container](#docker-container-instructions), activate the virtual environment and run the project:

### Linux/WSL/MacOS  
```bash
source .venv/bin/activate
crewai run
```

### Windows  
```PowerShell
call .\.venv\Scripts\activate
crewai run
```

This initializes the IDS3000 Crew, assembling the agents and assigning them tasks as defined in the configuration.
