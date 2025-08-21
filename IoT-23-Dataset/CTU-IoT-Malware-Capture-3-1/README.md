# Description
- Probable Name: Muhstik
- MD5: b8849fe97e39ae3afd6def618568bb09
- SHA1: b7e73f425b410112acc1c110af0a5d7ba1d3b49e
- SHA256: 5ce13670bc875e913e6f087a4ac0a9e343347d5babb3b5c63e1d1b199371f69a
- Password of zip file: infected
- Duration: 
- Proxy Usage: This capture did not use an intermediate proxy.

- [VirusTotal](https://www.virustotal.com/en/file/5ce13670bc875e913e6f087a4ac0a9e343347d5babb3b5c63e1d1b199371f69a/analysis/)
- [HybridAnalysis](https://www.hybrid-analysis.com/sample/5ce13670bc875e913e6f087a4ac0a9e343347d5babb3b5c63e1d1b199371f69a?environmentId=2)
- RobotHash

[![](https://robohash.org/b8849fe97e39ae3afd6def618568bb09)](https://robohash.org)

# Description of Files

- .capinfos
    - Capinfos file
- .dnstop
    - DNS top file
- .passivedns
    - Passive DNS file
- .pcap
    - Original pcap file
- .weblogng
    - WEB log of http traffic only. Generated with justsniffer
- bro
    - Folder with all the bro output files
- .biargus
    - Argus binary file. Bidirectional flows, 3600s of report time.
- .binetflow
    - Argus text file with bidirectional flows. Report time 3600 secs.
- .uniargus
    - Argus binary file. Unidirectional flows, 5s of report time.
- .uninetflow
    - Argus text file with unidirectional flows. Report time 5 secs. TAB as column separator.

# IP Addresses
    - Infected host: 192.168.2.5
    - Default GW: 192.168.2.1

# Timeline

## Sat May 19 20:56:36 CEST 2018
Started rpi

## Sat May 19 20:57:40 CEST 2018
Infected

# Analysis
Muhstik is a variant of the Tsunami botnet

The IRC channel was connected.

Which seems to be related with Muhstik botnet
http://blog.netlab.360.com/botnet-muhstik-is-actively-exploiting-drupal-cve-2018-7600-in-a-worm-style-en/
https://exchange.xforce.ibmcloud.com/collection/Muhstik-Botnet-Actively-Exploiting-CVE-2018-7600-0547cbc8eb2dc52c344b5da2b7c4063f

The malware infected the Rpi permanently.
- modified the cron
    $ crontab -l
    */5 * * * * /tmp/fce7b8bbd1c1fba1d75b9dc1a60b25f49f68c9ec16b3656b52ed28290fc93c72 > /dev/null 2>&1 &
    */5 * * * * /dev/shm/fce7b8bbd1c1fba1d75b9dc1a60b25f49f68c9ec16b3656b52ed28290fc93c72 > /dev/null 2>&1 &
    */5 * * * * /var/tmp/fce7b8bbd1c1fba1d75b9dc1a60b25f49f68c9ec16b3656b52ed28290fc93c72 > /dev/null 2>&1 &
    */5 * * * * /var/lock/fce7b8bbd1c1fba1d75b9dc1a60b25f49f68c9ec16b3656b52ed28290fc93c72 > /dev/null 2>&1 &

- Installed files on
    - /tmp/fce7b8bbd1c1fba1d75b9dc1a60b25f49f68c9ec16b3656b52ed28290fc93c72
        - does not exist
    - /dev/shm/fce7b8bbd1c1fba1d75b9dc1a60b25f49f68c9ec16b3656b52ed28290fc93c72 
        - md5 39051f30c7fe57342ad15921a611b665
    - /var/tmp/fce7b8bbd1c1fba1d75b9dc1a60b25f49f68c9ec16b3656b52ed28290fc93c72 
        - md5 39051f30c7fe57342ad15921a611b665
    - /var/lock/fce7b8bbd1c1fba1d75b9dc1a60b25f49f68c9ec16b3656b52ed28290fc93c72
        - md5 39051f30c7fe57342ad15921a611b665

Listens in port
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 127.0.0.1:61000         0.0.0.0:*               LISTEN      584/eth0



## Mon May 21 09:05:05 CEST 2018
poweroff

# Disclaimer 
These files were generated in the Stratosphere Lab as part of the Malware Capture Facility Project in the CVUT University, Prague, Czech Republic.
The goal is to store long-lived real botnet traffic and to generate labeled netflows files.
Any question feel free to contact us:
Sebastian Garcia: sebastian.garcia@agents.fel.cvut.cz

You are free to use these files as long as you reference this project and the authors as follows:
Garcia, Sebastian. Malware Capture Facility Project. Retrieved from https://stratosphereips.org
