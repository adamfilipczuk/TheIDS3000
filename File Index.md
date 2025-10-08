# File Index
This index file explains all major files and folders in the IDS3000 project. The most important files for setup and project configuration and use are **bolded**.

## Table of Contents
- [**Project Root**](#project-root)
- [**src/ids3000**](#srcids3000)
	- [Tools Folder](#tools-folder) 
- [**suricata-tcpreplay**](#suricata-tcpreplay)
## Project Root

```
TheIDS3000
├── .env
├── .git/
├── .gitignore
├── knowledge/
├── README.md
├── setup.bat
├── setup-linux.sh
├── setup-mac.sh
├── requirements.txt
├── pyproject.toml
├── uv.lock
├── output/
│   ├── cisco_configuration_report.md
│   ├── cisco_router_commands.txt
│   ├── cisco_switch_commands.txt
│   ├── data_queue.json
│   ├── email.txt
│   ├── incident_plan.md
│   └── suricata_report.md
└── src/
│   └── ids3000/
└── suricata-tcpreplay/
```

| File(s)                               | Description                                                                                                                                                                                          |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| .**env**                              | Environment variable file. Add your LLM information and email tool info here according to the project setup instructions.                                                                            |
| .git/                                 | Git files containing commit history etc.                                                                                                                                                             |
| .gitignore                            | Git configuration file.                                                                                                                                                                              |
| knowledge/                            | Folder used by CrewAI for providing static data sources to LLMs. Not used in project. Read the [CrewAI Knowledge documentation](https://docs.crewai.com/en/concepts/knowledge) for more information. |
| README.md                             | Project Readme file.                                                                                                                                                                                 |
| **setup***.**bat**,.**sh**            | Setup scripts for Windows, MacOS and Linux. Creates a Python virtual environment with project dependencies installed.                                                                                |
| requirements.txt                      | Base dependencies for CrewAI. Further dependencies are managed by uv.                                                                                                                                |
| **pyproject**.**toml**                | Project configuration and package manifest used by uv for dependency management. Add further dependencies here.                                                                                      |
| uv.lock                               | Lockfile for uv containing dependency versions used in the current install.                                                                                                                          |
| **output**/                           | Contains project outputs created by agents. Files are updated each time the project is ran.                                                                                                          |
| **output**/**cisco**\*                | `cisco_admin` agent reports.                                                                                                                                                                         |
| **output**/**data_queue**.**json**    | The processed eve.json data passed to the agent at run time. Not proper json format, pipe "\|" delimiters are used by the classifier during the run.                                                 |
| **output**/**email**.**txt**          | Text of the email send by `email_agent`.                                                                                                                                                             |
| **output**/**incident_plan**.**md**   | Network incident report and action plan created by `incident_manager`.                                                                                                                               |
| **output**/**suricata_report**.**md** | Traffic analysis report created by `suricata_analyst`.                                                                                                                                               |
| **src**/**ids3000/**                  | Agent configuration and main logic here.                                                                                                                                                             |
| **suricata-tcpreplay**                | The setup files for the suricata-tcpreplay container.                                                                                                                                                |
## src/ids3000

```
TheIDS3000/src/ids3000/
├── alert_tracker.py
├── socket_listener.py
├── crew.py
├── main.py
├── config
│   ├── agents.yaml
│   └── tasks.yaml
└── tools
    ├── classifier
    │   ├── classifier.py
    │   ├── data
    │   │   ├── conn.log.labeled
    │   │   └── eve.json
    │   ├── saved_model
    │   │   ├── classifier_tf_min.keras
    │   │   └── preprocessor_tf_min.keras
    │   └── training.py
    ├── custom_tool.py
    ├── classifier_tool.py
    └── send_email_tool.py
```

| File                   | Description                                                                                                                                                                                                                                                                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **alert_tracker.py**   | Bridging utility. Polls /TheIDS3000/suricata-tcpreplay/suricata/eve.json for changes and sends them in chunks to a socket object.                                                                                                                                                                                                         |
| **socket_listener.py** | Bridging utility. Listens to the socket object created by alert_tracker and adds objects to a queue.                                                                                                                                                                                                                                      |
| **crew.py**            | Crew (agents) instantiation. Agents and tasks are instantiated and defined according to agents/tasks.yaml instructions. See [CrewAI Crews documentation](https://docs.crewai.com/en/concepts/crews) for more information.                                                                                                                 |
| **main.py**            | Entrypoint to the project. This file handles passing inputs to the crew, running the crew and other methods such as crew tests. `crewai run` is equivalent to `main.run()`. An example main is shown in the [CrewAI 'build your first crew'](https://docs.crewai.com/en/guides/crews/first-crew#step-6%3A-set-up-your-main-script) guide. |
| **config/agents.yaml** | Agent definitions. See [CrewAI Agents documentation](https://docs.crewai.com/en/concepts/agents) for more information.                                                                                                                                                                                                                    |
| **config/tasks.yaml**  | Tasks definitions. See [CrewAI Tasks documentation](https://docs.crewai.com/en/concepts/tasks) for more information.                                                                                                                                                                                                                      |
| **tools/**             | Agent tools, so that agents can interact with their world. See [CrewAI Tools documentation](https://docs.crewai.com/en/concepts/tools) for more information.                                                                                                                                                                              |
### Tools Folder
| File                     | Description                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **classifier_tool.py**   | Tool definition for ML classifier. This is used by an agent to run the classifier.                                                                                                                                                                                                                                                                                                                  |
| **send_email_tool.py**   | Tool definition for Gmail API. This is used by an agent to access the Gmail API.                                                                                                                                                                                                                                                                                                                    |
| classifier/              | Classifier files.                                                                                                                                                                                                                                                                                                                                                                                   |
| classifier/classifier.py | The actual python classification logic.                                                                                                                                                                                                                                                                                                                                                             |
| classifier/data          | Data used for training the classifier. <br><br>`conn.log.labeled` is a concatenated csv file of labelled dataset objects from the IoT-23 dataset. You can find the individual labelled files in the IoT-23 objects, under the `bro/` folder. E.g, `CTU-Honeypot-5-1/bro/conn.log.labeled`.<br><br>`eve.json` is sample suricata eve data used with the classifier in standalone mode for debugging. |
| classifier/saved_model/  | This folder stores ML model files. You must place your \*.keras files here, or train a model using training.py, which will save the model files here.                                                                                                                                                                                                                                               |
| classifier/training.py   | Training script for the classifier. You must place a `conn.log.labeled` file in `classifier/data` to train the classifier. You may need to check the labeled file to ensure all headers are tab delineated. Some files have a mix of tab delineated and space delineated headers straight out of the dataset.                                                                                       |
## suricata-tcpreplay

```
TheIDS3000/suricata-tcpreplay
├── Dockerfile
├── compose.yaml
├── Readme.md
├── services.sh
├── captures
│   └── capture.pcap
└── suricata
    ├── eve.json
    ├── eve.json.offset
    ├── fast.log
    ├── stats.log
    └── suricata.log
```

| File                  | Description                                                                                                                                                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dockerfile            | Creates the suricata-tcpreplay image using Docker build.                                                                                                                                                                          |
| **compose.yaml**      | Used to build and manage the container using docker compose. Contains environment variables to change suricata and tcpreplay configurations. **Edit these variables** if you require custom suricata or tcpreplay configurations. |
| **Readme.md**         | suricata-tcpreplay container readme file.                                                                                                                                                                                         |
| services.sh           | Shell script used to configure the docker container and to start suricata and tcpreplay. Manages environment variables within the container.                                                                                      |
| captures/             | Place `capture.pcap` here.                                                                                                                                                                                                        |
| suricata/             | Suricata logs. Bridging utilities access this location.                                                                                                                                                                           |
| **suricata/eve.json** | The Suricata Extended Event log file. See [Suricata Eve JSON Format](https://docs.suricata.io/en/latest/output/eve/eve-json-format.html) documentation for more information.                                                      |
| eve.json.offset       | Offset file used by pygtail to track file changes. Part of bridging utilities.                                                                                                                                                    |
| fast.log              | Suricata logfile. Human readable alert format.                                                                                                                                                                                    |
| stats.log             | Suricata logfile. Performance statistics.                                                                                                                                                                                         |
| suricata.log          | Suricata logfile. Engine logs, warnings and errors.                                                                                                                                                                               |
