Date: 2014-11-07
Tags: irc, i2p, otr, weechat, tutorial
Category: blog
Title: i2p irc and otr with weechat


**BIG FAT DISCLAIMER**

This tutorial is not gaurenteed to provide absolute security as some of the components have not been properly audited.

If you know you are under targeted survailence please by god consult the [EFF](https://eff.org/) .

----

For a while I have been meaning to start a blog about i2p so here it is. First thing's first, a helpful tutorial for newbies.

IRC, internet relay chat ["what hackers use when they don't want to be overheard"](http://youtu.be/O2rGTXHvPCQ) while hacky and primative is a useful chat protocol. In general IRC is not private, server opers may log private messages and public channels are often logged for historical purposes. Considering that IRC is a very public procotocl one can still use it for secure and (more or less) authenticated communications. Off-The-Record, aka OTR is a common plaintext chat encryption protocol that works over IRC and XMPP. It allows you to have a private convorsation with another user given they use OTR as well.

----

Ubuntu setup for i2p + irc + otr:

First set up i2p if you have not already:

    sudo apt-add-repository ppa:i2p-maintainers/i2p
    sudo apt-get update
	sudo apt-get install i2p

Start I2P:

	sudo service i2p start

----

**IMPORTANT NOTE:**

i2p is beta software, please do **NOT** rely on it for strong anonymity.

----

Now we install weechat and pip (python's package manager):

    sudo apt-get install weechat python-pip

We install a dependancyfor weechat-otr, python-potr a pure python implementation of otr:

    sudo pip install python-potr

We get the actual [weechat-otr plugin](https://github.com/mmb/weechat-otr):

    mkdir -p $HOME/.weechat/python/autoload
    cd $HOME/.weechat/
	git clone https://github.com/mmb/weechat-otr

...and we have it autoload:

    ln -s $HOME/.weechat/weechat-otr/weechat-otr.py $HOME/.weechat/python/autoload/

Finally we set up our weechat for i2p

Open weechat in the terminal and set up irc2p:

    /server add irc2p localhost/6668
    /set irc.server.irc2p.nicks yournymhere
	/set irc.server.irc2p.realname yournymhere
	/set irc.server.irc2p.username yournymhere

To have you auto connect when you open weechat:

    /set irc.server.irc2p.autoconnect yes

Now connect to irc2p:

	/connect irc2p

Once connected, try joining a channel:

    /join #i2p-chat

To look at the channels avaiable:

    /list

To begin an otr converstation with someone on irc, please ensure that you have each verified eachother's fingerprints.

----

**IMPORTANT NOTE:**

Please ensure that you actually *do* verify fingerprints via another channel of communication like twitter or telephone, **DO NOT BLOW IT OFF** otherwise someone *may* (in rare cases) be able to impersonate you or your friends if you don't verify and store the fingerprint.

To list your fingerprint:

    /otr fingerprint

----

To start a converstation with someone that has otr:
 
    /query nickname
    /otr start

After you have checked that the fingerprint is identical to the one you have obtained, you can mark it as trusted:

    /otr trust

Once you are done with your private conversation:

    /otr finish


----

**IMPORTANT NOTE:**

By default weechat turns off logging while encrypted with otr, please understand that you are logging a private converstation when you turn logging on. Very rude, possibly dangerous if someone steals your logfiles. Best policy, *don't log private converstations*. If the logs don't exist they can't be stolen.

----
