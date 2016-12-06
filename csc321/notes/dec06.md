Brandon Randle
2016 December 06
Network Management Notes

## Final Exam Prep
* Chapter 6: Viewing Network Connections
  * Know netstat (lsof)
  * Hostname services
    * /etc/hosts, what is this used for
  * netstat layout of output
    * id columns, know what they are
  * determine listening/established connections
  * Windows/unix
* Chapter 7: Network Testing
  * Why testing
  * Normal vs. abnormal traffic
    * when? what? why?
  * Load testers / port scanners
  * Firewalls/proxys/load balancers
  * Reporting problems
* Chapter 8: DNS
  * What is it?
  * Nameservers
    * what? how?
  * zones / hierarchy
  * authoritative / recursive nameservers
  * process for host/IP lookup, how does it happen
  * forward vs. reverse lookups
  * record types
    * A, AAAA, PTR, etc.
  * caching
  * how to query
    * response codes
    * nslookup/host
    * windows vs. unix
  * BIND / ldns
  * hosts file /etc/hosts
  * name resolution order
  * DNS as single point of failure (when or if to disable)
* Chapter 9: Packet Sniffing
  * Packet sniffer
    * what? why?
  * Application tests vs. packet sniffing vs. network test
  * dangers of packet sniffing
  * tcpdump / wireshark
  * security issues
    * privilege
    * etc.
  * encryption and packets
  * interpret tcpdump output
  * BPI and filtering
    * why not use grep?
  * PCAP files
* Chapter 10: Creating Traffic
  * Why create traffic? Why note use application to create traffic?
  * netcat ("swiss army knife")
  * netcat competitors
  * using netcat
    * connect to existing service (TCP/UDP)
    * creating listeners
    * errors
