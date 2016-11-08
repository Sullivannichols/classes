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

# DNS Records
| Record Type | Description |
| ----------- | ----------- |
| A           | IP address  | 
| AAAA | IPv6 address |
| PTR (pointer) | hostname (ie, reverse DNS) |
| SOA (start of authority) | Cache timing, contact info (timing & responsibility) |
| CNAME (canonical name) | DNS alias (host1->host0, host2->host0) |
| MX (mail exchange) | mail server info for the zone |

# DNS Caching
* Recursive servers receive from authoritative server:
  * Answers
  * Timing
* Cache responses
* on expiry, recursive server deletes entry
* TAKES TIME (24 hours)
