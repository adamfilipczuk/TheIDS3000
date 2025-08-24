# About Observer
This observer is designed to watch the eve.json file for events using pygtail. 
This file will allow us to action events logged by suricata 

## Install
Install pygtail by running `pip install pygtail`


## Run
1. Ensure the docker container "suricata-tcpreplay" is running and is reading replaying a capture.pcap file 

2. Navigate to this directory and run `python observer.py`in powershell or bash. 

