Date: 2018-12-04
Tags: lokinet
Category: development
Title: Quick Lokinet Update December 2018
Authors: jeff

A very large amount of work happened with lokinet development since the last blog update in august.
As of writing, exit traffic works, hidden services work and service node traffic is wired up but untested.
I also took the liberty of refactoring the dns code used in lokinet. 

Most people know DNS as the protocol that is used to map human readable names to ip addresses on the internet 
using recursive lookups and such, but I see it as something else. 
If lokinet is to thrive you want to make the transition to it as painless as possible, 
hence why I chose DNS as the primary mechanism of controlling when to look up things on the network.
DNS is already used to do almost everything I was trying to do, so why reinvent the wheel?
That protocol is the one most if not all network aware programs use first when trying to figure out how to connect to something.

By having lokinet expose IP an DNS only, everything written should trivially work with little or no application porting needed. 

Lokinet's use of DNS can be explained as a forwarding, non caching DNS MiTM proxy that intercepts 2 TLDs, (.loki and .snode)
It intercepts dns queries and if the TLDs (top layer domain) is NOT loki or snode it will blindly forward any queries it gets 
to an upstream provider randomly chosen from list configured at runtime 
(I currently use [dnscrypt proxy](https://dnscrypt.info) as my upstream resolver on my workstation). 
Any replies from the upstream DNS provider are forwarded to the requester.

Right now the assumption is that Lokinet's DNS is on a LAN or loopback address and is properly firewalled from any kind of bogon traffic. 
This is probably not a safe thing to expect as a default as people can do really weird and dumb things if you let them.
I am toying with the idea of mapping the i2p and onion using via transparent proxy but that is a low priority right now and would explode the complexity of what I am doing at this moment.
I may toy with per IP endpoint request isolation, where address A and B both get their own set of network paths for lookups and ip traffic. This may entail poking firewall rules into the system to prevent A and B from using each other's paths. Further research is required, they are just ideas I had.
