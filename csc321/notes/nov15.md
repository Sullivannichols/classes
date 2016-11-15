Brandon Randle
2016 November 15
Network Management Notes

## The Role of Packet Sniffing
* Use your various tools first.
* Once you've exhausted your tools, then go to packet sniffing.
* Layers:
    * Layer 5: Top
    * Layer 4: Transport
    * Layer 3: Network / Internet World
    * Layer 2: Datalink
    * Layer 1: Physical

## Packet Sniffers
* tcpdump
  * cmdline
  * general purpose packet filter and analysis tool
  * exists to dump tcp information to the os
  * it's everywhere (some tweaks)
  * Berkeley Packet Filtering (BPF) (it's a way of expressing a filter)
  * small in size
  * Windows: WinDump.exe /WinPcap lib
    * not going to spend time on this
* Wireshark
  * GUI tool
  * Huge, lots of dependencies
    * lots of little tools
    * hacky scripts
    * spit & bailing wire
    * clever optimizations...ie, security holes
    * This software is swiss cheese. It was essentially made to be exploited.
  * Packet Analysis
  * Offline
  * Reads PCAP file (could get this file from tcpdump
  * Reconstructs sessions (this is its primary 'claim to fame')
    * A session is a reconstruction of those five-tuples (sip, sport, dip,
 dport, proto) that share the relationships between the items within the tuple
  * Never never NEVER EVER put on production environments
    * This is only to be used on some sort of disposable VM
    * You must treat all unvetted network traffic as radioactive and hostile

## Sniffing & Security
* Packet sniffers always require elevated privileges
* sidebar: never run something as root; only the operating system should be
 running as root
  * Anything running as root could leave the door open for exploitation
* supply chain attack: attacking a library associated with a service
* Most modern OSs will run things like tcpdump in a sandbox to keep it contained
  * This is still not sufficient for security.
* Wireshark ist Verboten

## Interfaces
* Layer 1 & 2
* Packet sniffers have to "attach" to a layer 2 interface
  * ie, eth0 on a linux box
  * en0 (1st ethernet)
  * lo (loopback)(an entirely logical interface)
  * Most OSs will have at least one physical interface and will have one to two
 logical interfaces
  * On Windows you have 6.5 gojillion interfaces
    * Windows has tons of logical interfaces used for various things
  * USB interfaces

## File Transfer Protocol
* Unencrypted, unsecure
* Telnet is also unsecure
* SSH, SFTP are encrypted and secure
