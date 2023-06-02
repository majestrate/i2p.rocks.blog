Date: 06-02-2023
Tags: blog, opentracker, bittorrent, outage
Category: blog
Title: opentracker.i2p.rocks june 2023 temporary outage
Authors: jeff

On June 1 2023 while applying some slight tuning of tcp sysfs parameters opentracker.i2p.rocks experienced a cascading failure caused by nginx dog piling and spiking the load average of the box well over 100 from excessive cpu usage from tls overhead.

ernesto from torrentfreak seemed to have noticed this and I replied to an email from someone inquring about this outage.

The opentracker is still active on udp 6969. I ended up remapping the A record for opentracker.i2p.rocks to go to a small terrahost VPS I have. I run opentracker.i2p.rocks as a kind of bonzai tree zen garden project but I like to keep it reliable. At the current moment I am busy job hunting in the Boston area ([hire me?](/cv.html)) and will reprovision the server as a proper TLS terminator running FreeBSD on bare metal once that search has completed. Please excuse the sudden unexpected outage of the tls announce url, I expect it to return by end of Q3 at the latest and mid june at the earliest.

I should have another blog update sometime by Monday or so (probably) on other things unrelated to this outage.
