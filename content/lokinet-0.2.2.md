Date: 2018-09-10
Tags: lokinet
Category: development
Title: LokiNET 0.2.2 released
Authors: jeff
 
The first mostly working version of LokiNET has been released, 0.2.2.

This means that it's now time to start getting people to run LokiNET routing infrastructure, yes 
that includes you. If you have a spare server and don't mind a little bit of bandwidth being
put to use for "science and such" please consider helping out by setting up lokinet in particiation mode.

The rest of this blog will document the process of compiling from source and setting


Install the build dependencies (assuming ubuntu or debian here):

    $ sudo apt install libcap-dev build-essential cmake ninja-build git
        
    
Next, check out the lokinet source code, this repo is recursive.

    $ git clone --recursive https://github.com/loki-project/lokinet-builder ~/lokinet-builder
         
Now we build lokinet

    $ cd ~/lokinet-builder
    $ make

The result is a `lokinet` binary as well as a few other tools that you can ignore for now.

Install the `lokinet` binary to somewhere in your `$PATH`

    $ sudo cp lokinet /usr/local/bin/

To run on the network you'll need a bootstrap node.

The `contrib/testnet/i2procks.signed` file is my nodeinfo for the lokinet running on i2p.rocks, you can substitute that with
your own if you already have a `self.signed` file from a working lokinet.

At the moment lokinet auto generates a config if non is present, we'll do this so we get a base config we can modify.
Also set aside a new directory for lokinet for now.

    $ mkdir -p ~/lokinet/
    $ cd ~/lokinet/
    
Now we start as a client node, it won't go anywhere because we don't have any peers.

    $ lokinet

A `daemon.ini` file should have been generated.

Ensure that in `daemon.ini` there is a `[bind]` section with a value something like `eth0=1090`

If there isn't one the machine you are on a machine that doesn't have a network interface with a public address.

To remidy this, see the `[router]` section in `daemon.ini`

uncomment and set `public-address` to your public ip and `public-port` to `1090`.


Lastly add the following to the end of `daemon.ini` to tell lokinet to connect to the bootstrap node.

    [connect]
    i2procks=i2procks.signed
  
Copy `~/lokinet-builder/contrib/testnest/i2procks.signed` file to `~/lokinet/i2procks.signed` and restart lokinet.

If all goes well then you should see some logging output and maybe a few erorrs and warnings (but that is fine).
Your node will slowly start exploring the network and as clients build paths you'll be used in them. Please try 
to have decent uptime as this release does not have peer profiling yet.
