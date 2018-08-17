Date: 2018-08-17
Tags: lokinet
Category: development
Title: LokiNET progress report August 2018
Authors: jeff
 

The trip to Melbuorne was great and it was really helpful to meet the loki team.
Everything was inverted, people walked on the opposite side of the sidewalk so I have
to turn off my autopilot in the morning when walking to get coffee. Overall it was a good
trip.

During the trip progress did grind to a halt but lots of new ideas came about as a result
of being in an office with other smart and hard working individuals. One of the ideas was
hidden service topic tags, effectively you can now discover hidden services on the network
by tag, as 16 byte string they set with a topic (opt in), you query the DHT for a topic tag
and get back a list of IntroSets (hidden service descriptors) that claim that tag.
This functionality is used in the loopback test network to automate testing. 
The test network spins up 100 nodes, half of them service nodes, the other half are clients.
The clients each host 1 SNAP (hidden service) with the tag "test" and do a tag prefetch for
hidden services with the tag "test". This made implementing the hidden service traffic much
more straight forward as I could test it all on loopback without having to spin up servers 
on the internet and guess why things dont work. I can have a bird's eye view of my test network
and truly be able to debug it as a whole.

Topic tags will not be exposed to the end user to reduce the complexity and are currently only
used in the loopback testnet. They will remain in the code and be usable on the main network but
I don't know of any real use for them in practice, outside of maybe bittorrent DHT bootstrap or
other SNAP bootstrapping.

I have an IRC channel on freenode, join it if you want to join it say hi it's `#llarp`
I will also soon be making an irc channel for loki (eventually) so people who do not wish to use discord can
chime in with insights.
