Date: 2018-09-29
Tags: lokinet
Category: development
Title: LokiNET 0.2.3 soooooon ™
Authors: jeff
 
LokiNET 0.2.3 release will be happening soon-ish this week probably, at least I think.

This is a manditory update and is the first end user ready release that does
meaningful things for the end user. Specifically, primordial support for hidden services.
The code for path handover is not there yet so long lived connections that have low packet 
transmission rates like IRC may suffer greatly.

added:

* dns automapping (linux only right now)
* tun interface (linux only right now)
* bootstrap script (linux only right now)
* config autogeneration

fixed:

* dht no longer should store old descriptors
* improved debian packaging so that it "just works"
