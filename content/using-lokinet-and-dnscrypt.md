Date: 2020-03-16
Tags: lokinet, dns, dnscrypt, dnscrypt-proxy, configuration
Category: blog
Title: Lokinet with DNSCrypt-Proxy
Authors: Jeff

## Intro

This is a quick intro with how to use lokinet with dnscrypt-proxy on ubuntu/debian based distros
to secure your dns queries from spying eyes, as requested by someone on an XMPP muc.

## Setup

You want to first install `dnscrypt-proxy`

    # apt update
    # apt install dnscrypt-proxy 

Next install `lokinet` see [this blog post](/blog/installing-lokinet-on-ubuntu.html) on how to do that.

## Configuration

By default your system will want to use `dnscrypt-proxy` as system resolver, this is fine as you can 
always forward dns for `.loki` and `.snode` to lokinet.

In `/etc/dnscrypt-proxy/dnscrypt-proxy.toml` you want to add an option to provide a fowarding file:

    forwarding_rules = '/etc/dnscrypt-proxy/forwarding-rules.txt'

In a new file at `/etc/dnscrypt-proxy/forwarding-rules.txt'`put the following forwarding rules:

    loki 127.3.2.1
    snode 127.3.2.1
    0.10.in-addr.arpa 127.3.2.1
    
    
The first rule says to forward the `.loki` gtld to lokinet dns (127.3.2.1)

The second rule says to forward the `.snode` gtld to lokinet dns

The third rule is for reverse dns for `10.0.0.0/16` ip range so you can resolve the .loki address from the range owned by lokinet.

If you do not use `10.0.0.0/16` for lokinet's ephemeral IP range change the third rule to match the range you use.

Finally you want to set your primary dns resolver to use `127.0.2.1` (not `127.3.2.1` that is lokinet dns)
