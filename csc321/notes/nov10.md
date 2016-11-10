Brandon Randle
2016 November 10
Network Management Notes

# DNS Final Notes
* `/etc/hosts` is your "local zone file"
  * Stay on top of this
  * config management, eg Ansible, Puppet, Chef
* Name Resolution Order
  * DNS
  * Hosts File
  * LDAP
  * local database
  * WINDOWS
    * hosts file -first-
  * UNIX
    * `/etc/nsswitch.conf`
    * `/etc/host.conf`
* Disabling DNS
  * netstat
  * traceroute
  * ping
  * SSH

# Packet Sniffing
* packet: Layer 3, Layer 4
* 5-tuple
  * (srcIP, srcPort, destIP, destPort, Protocol)

# Troubleshooting
* Client reach server?
  * traceroute
* server reach client?

# Sniffing
* watches traffic at the interface
* filtering
* caveat emptor: vendor will always say "check your firewall"
  * they will always assume first that the problem is on your end
  * therefore, check the firewall first and have data ready to give to vendor

* PII (Personally Identifiable Information)
  * This is radioactive. These are things like SSNs, addresses, etc. that allows
one to identify a person.
  * Viewing this information == lawsuit 
  * Avoid this information like the plague. Filter it out if at all possible,
and absolutely NEVER save it.
  * Certification standards require encryption over SSL or using port 443
  * Only ever touch layer 5 encrypted
