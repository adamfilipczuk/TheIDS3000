# Suricata-TCPReplay

This Docker container integrates **Suricata** and **tcpreplay** to enable live packet replay and analysis by Suricata. Managed by `docker-compose`, the container is designed for ease of use and system compatibility. It provides basic variables for configuring `tcpreplay` and exposes Suricata's logs for investigation.

## Installation and Setup (WSL/Ubuntu)

This system was developed and tested using **Windows Subsystem for Linux (WSL)** with **Ubuntu**. These instructions are tailored for WSL and Ubuntu environments. To install WSL, use the command `wsl --install` or refer to the official [WSL Installation Instructions](https://learn.microsoft.com/en-us/windows/wsl/install).

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

1.  **Provide a Packet Capture:** Place a `.pcap` file in the `./captures` directory. The default file name is `capture.pcap`.

2.  **Start the Container:** Run the following command to start Suricata and tcpreplay with the default settings:
    ```bash
    docker compose up
    ```
    Suricata's logs, including the important `eve.json` file, will be accessible in the `./suricata` directory.

---

## Advanced Configuration

You can customize Suricata and tcpreplay settings using **environment variables**. This can be done by editing the `compose.yaml` file or by setting the variables at runtime.

### Suricata Variables

* **`SURICATA_RULES`**: Specifies a custom `.rules` file path. Place your custom rule file (e.g., `xyz.rules`) in the `./suricata` folder.
* **`SURICATA_CONF`**: Specifies a custom `.yaml` configuration file path. Place your custom configuration file (e.g., `xyz.yaml`) in the `./suricata` folder.

**Example:**
```bash
- SURICATA_RULES=./suricata/xyz.rules
- SURICATA_CONF=./suricata/xyz.yaml
