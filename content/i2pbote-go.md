Date: 2017-01-27
Tags: i2p, i2pbote
Category: blog, development
Title: i2pbote in go coming soon and i2p.rocks irc reverse proxy
Authors: Jeff

I have started working on an i2pbote implementation in go on [github](https://github.com/majestrate/i2pboted). Currently it is non functional but in the coming months I'll be blogging about the development process as things get done.

If you know go and want to help expedite the development, get onto irc2p and join `#i2pd-dev` channel.

In additioon, i2p.rocks now has experimental irc reverse proxy at `*.i2p.rocks` port 6697 using TLS, i.e. to access `irc.dg.i2p` you can connect `irc.dg.i2p.rocks` on port 6697 using ssl. Right now I don't have a wildcard certificate so you'll have to manually trust the connection. Source code for the reverse proxy is on [github](https://github.com/majestrate/tls2socks).

A super simple link for the irc channel using the i2p.rocks reverse rpoxy is [ircs://irc.dg.i2p.rocks/i2p-chat](ircs://irc.dg.i2p.rocks/i2p-chat).

Please do not send private info like login credentials over this service as tls is only used to route your request to socks proxy, everything is plain text inside the reverse proxy, think of it like tor2web for irc on i2p.

