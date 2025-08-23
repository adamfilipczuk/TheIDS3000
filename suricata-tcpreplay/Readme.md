# suricata-tcpreplay

This is a Docker container that integrates suricata and tcpreplay for live packet replay and investigation by suricata. The container is managed by docker-compose for system compatibility and ease of use.The container provides basic variables for configuring the use of tcpreplay, and exposes suricata's logs for investigation purposes.

##Installation and setup - WSL/Ubuntu

The system was created using Windows Subsystem For Linux using Ubuntu. These instructions should work for WSL and Ubuntu systems. To install WSL use the command `wsl --install` or consult the [WSL Installation Instructions.](https://learn.microsoft.com/en-us/windows/wsl/install)

### Docker/Compose installation
`sudo snap install docker`  
`sudo apt install docker-compose`

Clone this repository, and from the suricata-tcpreplay folder:
* **Provide a packet capture**  
Place a .pcap file in ./captures. By default the capture should be labelled 'capture.pcap'.

* **Start container using docker-compose**
`docker compose up`
 
This will run Suricata and tcpreplay with preprogrammed settings. You may access the suricata logs, importantly the eve.json file, from ./suricata.

###Environment variables and advanced configuration

You may use environment variables to configure Suricata and tcpreplay by editing `compose.yaml` or by running with environment variables set at runtime.

###Suricata variables

The SURICATA\_RULES variable specifies a path to a custom .rules file. The custom file must be placed in the suricata folder with a rule format of `./suricata/xyz.rules.`

The SURICATA\_CONF variable specifies a path to a custom .yaml configuration file. The custom file must be placed in the suricata folder with a rule format of `./suricata/xyz.yaml`
                                                                             
    - SURICATA\_RULES=./suricata/xyz.rules                                         
    - SURICATA\_CONF=./suricata./xyz.yaml                                          

###TCPReplay variables

The LOOPS variable specifies the max packet replay loops provided by tcpreplay before it shuts down. This is a standard int with a default of `10`.

The SPEED variable specifies the replay speed multiplier. This is formatted as a decimal with a default value of `15.0` (Fifteen times realtime speed). 

The FILENAME variable specifies a path to a custom .pcap file. The custom file must be placed in the captures folder with a with a format of `./captures/xyz.pcap` 

    - LOOPS=10
    - SPEED=15.0
    - FILENAME=capture.pcap     

#Runtime configuration example

    docker compose run \
    -e LOOPS=50 \
    -e SPEED=10.0 \
    -e FILENAME=2018-20-08-19-53-26.pcap \
    -e SURICATA_RULES=/etc/suricata/rules/local.rules \
    suricata-tcpreplay
