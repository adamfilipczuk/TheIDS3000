# Suricata-TCPReplay

This Docker container integrates **Suricata** and **tcpreplay** to enable live packet replay and analysis by Suricata. Managed by `docker-compose`, the container is designed for ease of use and system compatibility. It provides basic variables for configuring `tcpreplay` and `suricata`, and exposes Suricata's logs for investigation.

## Installation and Setup (WSL/Ubuntu)

This system was developed using **Windows Subsystem for Linux (WSL)** with **Ubuntu**. These instructions are tailored for WSL and Ubuntu environments. To install WSL, use the command `wsl --install` or refer to the official [WSL Installation Instructions](https://learn.microsoft.com/en-us/windows/wsl/install).

---

### Docker and Docker-Compose Installation

* Install Docker:
    ```bash
    sudo snap install docker
    ```
* Install Docker-Compose:
    ```bash
    sudo apt install docker-compose
    ```

After installation, clone this repository. From within the `suricata-tcpreplay` folder, follow these steps:

1.  **Provide a Packet Capture:** Place a `.pcap` file in the `./captures` directory. The default file name to be provided is `capture.pcap`.

2.  **Start the Container:** Run the following command to start Suricata and tcpreplay with the default settings:
    ```bash
    docker compose up
    ```
    Suricata's logs, including the important `eve.json` file, will be accessible in the `./suricata` directory.

---

## Advanced Configuration

You can customize Suricata and tcpreplay settings using **environment variables**. This can be done by editing the `compose.yaml` file or by setting the variables at runtime.

### Suricata Variables

* **`SURICATA_RULES`**: Specifies a path to a custom `.rules` file. The file must be placed in the `./suricata` folder.
    
    ```compose.yaml
    - SURICATA_RULES=./suricata/xyz.rules
    ```

* **`SURICATA_CONF`**: Specifies a path to a custom `.yaml` configuration file. The file must be placed in the `./suricata` folder.
    
    ```compose.yaml
    - SURICATA_CONF=./suricata/xyz.yaml
    ```

### TCPReplay Variables

* **`LOOPS`**: Specifies the maximum number of packet replay loops before `tcpreplay` shuts down. This is a standard integer with a default value of `10`.
    
    ```compose.yaml
    - LOOPS=10
    ```

* **`SPEED`**: Specifies the replay speed multiplier. This is a decimal with a default value of `15.0` (fifteen times real-time speed).
    
    ```compose.yaml
    - SPEED=15.0
    ```

* **`FILENAME`**: Specifies the path to a custom `.pcap` file. The file must be placed in the `./captures` folder with the format `./captures/xyz.pcap`.
    
    ```compose.yaml
    - FILENAME=./captures/capture.pcap
    ```

---

### Runtime Configuration Example

```bash
docker compose run \
-e LOOPS=50 \
-e SPEED=10.0 \
-e FILENAME=2018-20-08-19-53-26.pcap \
-e SURICATA_RULES=/etc/suricata/rules/local.rules \
suricata-tcpreplay
