Brandon Randle
2016 November 08
Network Management Notes

# DNS
* You can use `host <domain>` to get IP addresses for a domain name,
ie, `host www.google.com`. You can also use `host <ipaddress>` to get the
actual domain pointed to by the nameserver.
* The file /etc/resolve.conf lists the nameserver used by the system.
* DNS is essentially a distributed database.
  * Is cursed by its success.
  * It is common that when a technology is really good at what it was designed
for, it will be used for things for which it was not intended or designed.
  * Has extra stuff stored inside.

Records
Record Type | Description
 --- | ---
A | hostname->IP, contains an IP address, the hostname returns the IP
AAAA | Contains IPv6 address
 
