Date: 2017-04-16
Tags: i2p, tutorial
Category: blog
Title: I2P Browser Configuration Tutorial, the "Proper" way.
Authors: Jeff



## Preface

Tor browser provides a great brain dead simple interface for using the internet anonymously.
Sadly you cannot really hack on it easily because modifying defaults is considered harmful by most people (opinion).
This is a step by step guide on configuring a browser to use i2p for i2p and tor for everything else.

## Disclaimer

This configuration will not protect you from web browser exploits, fingerprinting, session tagging, traffic correlation, local rootkit, etc.

## The setup

Requirements:

* Linux (any flavor)
* tor
* i2pd (or java i2p if you really want to)
* privoxy

The basic setup is the following:

    your browser -> privoxy -> tor -> internet / onion
                      |
                      V
                     i2pd -> i2p

## Installation

see [here](https://i2pd.readthedocs.io/en/latest/devs/building/unix/) on how to install i2pd from latest source code

see [here](https://www.torproject.org/docs/tor-doc-unix.html.en) on how to install tor from latest source code

For debian or ubuntu based distributions you can do `sudo apt install privoxy` and it'll get privoxy. If you're using Fedora it's `sudo dnf install privoxy`.

## Configuration

Append the following lines to `/etc/privoxy/config` :


    forward-socks5t / 127.0.0.1:9050 .
    forward .i2p 127.0.0.1:4444

For this example we'll use chromium for the browser:

    chromium --proxy-server=127.0.0.1:8118

Now you can browse with both tor/i2p.

This will not change your browser's user agent and you will be much fingerprintable, for fingerprint resistance consider using Tor Browser.
