#!/bin/bash
# services.sh
# Starts suricata and tcpreplay using a default file.

#Variables configure suricata options.
#SURICATA_RULES value specifies path to .rules file. Must be in suricata folder
#with format ./suricata/xyz.rules
#
#SURICATA_CONF value specifies path to .yaml file. Must be in suricata folder
#with format ./suricata/xyz.yaml
#
SURICATA_RULES="${SURICATA_RULES:-}" 
SURICATA_CONF="${SURICATA_CONF:-}" 

# Default suricata args
SURICATA_ARGS=(-l ./suricata -i eth0)

#Build suricata args dynamically
if [ -n "$SURICATA_RULES" ]; then
  SURICATA_ARGS+=(-S "$SURICATA_RULES")
fi

if [ -n "$SURICATA_CONF" ]; then
  SURICATA_ARGS+=(-c "$SURICATA_CONF")
fi

suricata "${SURICATA_ARGS[@]}" &

#Variables configure tcpreplay options: 
#LOOPS=num; max loops specified by -l with format 10
#
#SPEED=num; speed multiplier specified by -x with format 15.0
#
#FILENAME value specifies path to .pcap file. Must be in captures with format 
#./captures/xyz.pcap 

LOOPS="${LOOPS:-10}"
SPEED="${SPEED:-15.0}"
FILENAME="${FILENAME:-./captures/capture.pcap}"

tcpreplay-edit -i eth0 -l $LOOPS -x $SPEED --mtu-trunc $FILENAME
