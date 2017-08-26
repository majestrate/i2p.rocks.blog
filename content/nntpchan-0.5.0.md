Date: 2017-08-26
Tags: nntpchan, development
Category: blog
Title: nntpchan 0.5.0 released
Authors: jeff

After over a year I am proud to release nntpchan version `0.5.0`.

The daemon has gone through a lot as well as the build system, we have many many new things added.

* smart varnish caching
* ed25519-blake2b signatures
* no longer use cgo, libsodium not used at all, we are 100% pure go now.
* no more noticable gc leaks
* use 1 repo for everything, don't split backend and frontend repo for ease of building

Many features were also gutted:

* filesystem markup cache
* redis support (all of it)

I think this covers everything, so much changed I probably forgot something or a few other things ...

Download on github [here](https://github.com/majestrate/nntpchan/releases/tag/0.5.0) and join us on IRC to peer into the main network.

We're on the following networks:

rizon: irc.rizon.net #nntpchan

freenode: irc.freenode.org #nntpchan

irc2p: irc.dg.i2p #overchan

cjdns/hype: reseed.i2p.rocks #overchan
