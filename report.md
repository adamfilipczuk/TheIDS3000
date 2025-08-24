**Mirai Botnet Detection & DDOS Classification Report**

**Summary:**
Strong evidence of Mirai botnet activity and DDOS attacks has been detected. Immediate action must be taken to mitigate these threats and prevent further malicious activity.

**Key Findings:**

* **ET CHAT IRC PONG**: Multiple occurrences of ET CHAT IRC PONG, indicating potential Mirai botnet activity.
* **DDOS Attacks:** Evidence of DDOS attacks targeting various IP addresses, including 185.244.25.235 and 192.168.1.195.
* **IRC Traffic:** Heavy IRC traffic detected, including PRIVMSG, NOTICE, PART, KICK, and MODE commands.
* **ELF executable sent**: A potential ELF executable was sent when a remote host claimed to send a Text File.

**Timeline:**

* 2018-12-22T00:55:32.322498+1000: Heavy IRC traffic detected, including PRIVMSG, NOTICE, PART, KICK, and MODE commands.
* 2018-12-22T01:03:42.459479+1000: NTP query sent to IP address 185.244.25.235.
* 2018-12-22T01:10:28.610859+1000: DDOS attack detected, targeting IP address 185.244.25.235.
* 2018-12-22T01:21:04.303864+1000: Heavy IRC traffic detected, including PRIVMSG, NOTICE, PART, KICK, and MODE commands.

**Recommendations:**

1. **Immediate Action:** Take immediate action to block and mitigate the Mirai botnet activity.
2. **Network Monitoring:** Continuously monitor network traffic for signs of malicious activity.
3. **System Updates:** Ensure all systems are up-to-date with the latest security patches.
4. **User Education:** Educate users on best practices for online safety and cybersecurity.

**Conclusion:**
Based on the analysis, it is clear that a Mirai botnet is active in the network, conducting DDOS attacks and sending malicious traffic. Immediate action must be taken to mitigate these threats and prevent further malicious activity.

**Full Report:**

```
{
  "timestamp": "2018-12-22T00:55:32.322498+1000",
  "flow_id": 661983042138264,
  "pcap_cnt": 1241,
  "event_type": "http",
  ...
}

{
  "timestamp": "2018-12-22T01:03:42.459479+1000",
  "flow_id": 1722695934846685,
  "pcap_cnt": 4333,
  "event_type": "alert",
  ...
}

{
  "timestamp": "2018-12-22T01:10:28.610859+1000",
  "flow_id": 383071871034451,
  "pcap_cnt": 2996,
  "event_type": "alert",
  ...
}
```