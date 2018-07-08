Date: 2018-07-08
Tags: lokinet
Category: development
Title: LokiNET progress report July 2018
Authors: jeff


Progress on LokiNET has been good, so far I have met my goals for this current stretch.

Onion routing and the Router Contact (called a RouterInfo in i2p) DHT works (mostly). 
The exit vpn was initially the next part I was going to work on but after talking 
with the rest of the team it will probably be the last thing I work on as you have 
to be a crazy person to run an exit node for any network out there. 

The next stretch will be getting the hidden services to work, this has a few compontents. 

Before anything you need to implement the basic datatypes that are used, specifically Introduction sets,
(called a leaseset in i2p), which means you need to implement Introductions (lease in i2p), 
Service Info ( destination blob in i2p), service address ( .b32.i2p address in i2p ), 
Identity ( destination private keys in i2p ), signing, verifiying and serialization for all of the
previous entities. That's mostly done as of writing, some parts of the serialization is unfinished but
the unit tests for signing and verifying introduction sets pass.


You need to handle publishing introduction sets to the DHT, server side handling, then client side handling. 
Next you need to implement fetching introduction sets from the DHT, again server side then client side. 
So we got 1 task, implementing hidden services, that turns out to be 4 features to implement and we're not 
even half way in @_@. So, once publishing and fetching introduction sets is done, we need to build messages
to send, this is before implementing the Hidden Service data messages (called i2cp message from i2p).

![HELP! I NEED AN ADULT!]({filename}/images/lokinet-july-2018/mfw.png "HELP! I NEED AN ADULT!")

A simple sounding goal like "implementing hidden services" can often expand really fast into many tasks
each with their own subtasks.

I'll be leaving for Melborune Australia next week and I'll be there until the end of July, loki project is
flying me out to synchronize with the rest of the team. We'll see what happens.

I have an IRC channel for dev, #llarp on freenode, join it if you want.
