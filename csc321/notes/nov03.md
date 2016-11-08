Brandon Randle
2016 November 03
Network Management Notes

# Network Architecture Complications
* Firewall!! BAD!
* Packet Filtering
* Proxy Servers
  * The goal of a proxy is to intercept web traffic in and out; they tend to
man-in-the-middle SSL traffic.
  * Proxies tend to decrypt the SSL traffic, read it, and re-encrypt it before
sending it along. This allows the folks running the proxy to monitor info that
enters and leaves the network. This can be used in a situation where the
organization is paranoid about loss of information (like intellectual property)
* Load Balancer

* Open a Ticket
  * Provide a description of behavior
  * "connection refused"
  * "connection timed out"

* Problem Prevention
  * _stopping issues before they happen_
  * Provide the netadmin with goals
    * goals imply tools
    * listen to netadmin about possible tools
  * provide accurate information
  * don't take it personally 

* Firewall
  * A policy enforcement device
  * uses TCP/UDP/etc. ports, protocols, and IP addresses
  * begins as "default deny", namely, by default you deny everything first,
and you explicitly allow certain things through them.
  * Old-school firewalls were routers with non-trivial ACLs
  * Firewalls do deep-packet inspection

* Router
  * Connect together subnets at the networking layer
  * Have ways of dealing with traffic
  * Access Control List (ACL, pronounced "ackle") 
    * These provide packet filtering
  * Routers and firewalls have in common that they both filter traffic.
    * The difference is that firewalls these days tend to look INSIDE the
packets to assess their contents and look for anomalies
  * Routers and their ACLs are very simple. 
  * Routers don't modifiy the packets. It either goes through or drops on the
floor.

* Proxy
  * If data is changed en-route, it's usually the proxy.
  * Proxies can and do a certain amount of mangling of packets
  * Proxies perform their own requests. They act as complete intercepts of
data. 

* Load Balancer
  * Requests from outside come to the edge router.
    * The web server sits behind the edge router.
    * The edge router would love to send all requests directly to the web
server.
    * However, if you're receiving tons of connections (like Google), such
a load can not be handled.
    * Instead, the edge router forwards the traffic to the load balancer, 
which then divies up the traffic to several web servers. 

# Domain Name System (DNS)
* Basics
  * Maps hostnames to an IP address. 
  * DNS is the purview of the network team
  * Uses the nameserver to resolve the addresses.

* Nameserver
  * Searches for and collects host<->ip
  * has local cache
  * reaches out to nameserver if not local
  * If you want to connect using hostnames, you have to have information about
your nameserver.
  * Nameserver is either hardcoded, DHCP automatic, or specified by an ip
address.

* DNS Hierarchy
  * "zones"
  * Zones are a level of the hiearchy
  * There is a root zone, beneath with you have other subzones.
  * The root zone is the parent zone of x child zone(s). This is the phrasing
used to describe zones. Parents can also be children. (Very similar/almost
identical to class relationships.)
  * The root's child zones are the TLD (Top-Level Domains), including things
such as .com, .net, .org, and every other TLD.
  * The TLD child zones are Domains, such as google.com, wwf.org, wikipedia.org
, and so forth.
  * Every TLD has a "zone file" which is a complete collection of data about
that zone. These "zone files" live on authoritative nameservers.  
  * Recursive servers, as opposed to authoritative servers, look for data. They
handle client requests and find authoritative servers.
  * You don't run an authoritative and recursive nameserver on the same system.
This is what Google would call "crossing the streams". They need to be on a
different host. Back in the day, this was done with different hardware. Today
you can use virtualization to achieve the same effect.

  * Distributed Database

  * Forward DNS - hostname->IP, resolves to multiple IP addresses
  * Reverse DNS - IP->host, always resolves to one host.
