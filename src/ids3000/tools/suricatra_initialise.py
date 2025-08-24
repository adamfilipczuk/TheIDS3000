import subprocess


#needs to be changed to work with a config file later

subprocess.run(["D:\Suricata\suricata.exe",
                "-c", "D:\Suricata\suricata.yaml",
                "-r", "D:\datasets\Mirai_dataset.pcap",
                "-l", "D:\Suricata\log"])



#suricata.exe
# "-c", "D:\Suricata\suricata.yaml"
# "-r", "D:\datasets\Mirai_dataset.pcap"
# "-l", "D:\Suricata\log"
