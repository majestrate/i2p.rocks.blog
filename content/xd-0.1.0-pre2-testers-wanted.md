Date: 2018-01-22
Tags: i2p development XD
Category: blog
Title: XD 0.1.0-pre2 released, testers wanted.
Authors: jeff


I have been writing an i2pd compatable bittorrent client called [XD](https://github.com/majestrate/XD) in golang. It has reached an almost end user ready state. 0.1.0 will be the first "official" release of it. Before that happens I need some beta testers.

If you want to help test it you can do the following

## install i2pd from git 

There are some bugfixes that are applicable to XD that are not in 2.17 yet.

If you don't know how to build from source the documentation is [here](https://i2pd.readthedocs.io/en/latest/devs/building/requirements/)

## download and run XD

latest release [here](https://github.com/majestrate/XD/releases)

right now XD uses the current working directory as the data directory so make a new directory and put the executable there.

On Unix systems you can do something like this:

    $ mkdir ~/XD/
    $ cd ~/XD/
    $ cp /path/to/downloaded/XD .

then make a symlink for `XD-cli`

    $ ln -s XD XD-cli 

on windows you can copy `XD.exe` to `XD-cli.exe`

## add some torrents

there is a webui located on loopback [here](http://127.0.0.1:1488/) by default.

I have a test torrent on my eepsite [here](http://psi.i2p/mu/ebin.torrent), copy that url and put it in the `"torrent location"` text field of the UI, press `"add"` and it'll fetch, add and preallocate the torrent and start downloading once the network session with i2p is fully made. That torrent contains my latest albumn so no one will be mad if you download it (but I may be mad if you DON'T download it D:<).

There is also a small torrent index called [anodex.i2p](http://anodex.i2p/?i2paddresshelper=Je-EL3yA0a1MAtMjup-U13rw0FJ7lxh6iMqNag-W~lHxZX4JOo21XqFZlViXBFoBdjNpDPSE44G3HpCSLnKg5D~Jw-6RiADrlAKId0ZYo2Ilpk5rGjBAzpAjebvGD0PM0eUsm5Y3S4byKTLnT0QFjc~cy7mP~jP~8YbtygqsgBxTl17icSGPQWlPS-mE1XJD1nw8-6pepOxQd-mX0MUrmI8oldeUzHPDxerRm9MM2OADg7lV9GBUjbMnbQm-xu4xiMSZRZbRxTWHql9VDYYvc0l5mbeAzZrMT99vFr~GtEw7yNwIFneweZRb9OaVsOpfBmgHzS~Y0hfqwQPHu8FbLEaAByHcmAFo4FWGMa0oc6m2S8shCzV9l1WDgREwcclPI1H4ScgjyKBeIV4lJlY8RlrvsTspN1p5mtKJMeOijb80v-6SLISSAGCz6FEiSu7o3m3~mi2mmlsltruDmRLZoLXhOEJXxCWYt8KgTMlWgIN~CeV5y8ckvl~rPcjwjQJhBQAEAAcAAA==) that takes uploads without needing an account, source code for the index is located on i2p [here](http://git.psi.i2p/psi/torrent.ano/). Please note that the index does not track swarm stats yet so some (or most) of the torrents may be without seeds.

## bugs

Please report all bugs or problems you encounter to the issue tracker on either [github](https://github.com/majestrate/XD/issues) or [my git](http://git.psi.i2p/psi/XD/issues) .
