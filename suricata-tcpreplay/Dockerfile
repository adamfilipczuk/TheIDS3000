FROM ubuntu:latest
RUN apt update -y && apt upgrade -y
RUN apt install -y tcpreplay software-properties-common net-tools
RUN add-apt-repository -y ppa:oisf/suricata-stable
RUN apt update -y
RUN apt install -y suricata jq
RUN suricata-update
RUN mkdir captures
VOLUME /captures
RUN mkdir suricata
VOLUME /suricata
COPY services.sh /usr/local/bin/services.sh
RUN chmod +x /usr/local/bin/services.sh
CMD ["/usr/local/bin/services.sh"]
