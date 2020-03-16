Date: 2019-09-22
Tags: llarp, lokinet, tutorial, debian, ubuntu
Category: blog
Title: Installing Lokinet on Ubuntu
Authors: Jeff

## Intro

This blog post will guide you through the process of installing lokinet using our apt repo and is 
aimed at people whom are just getting into linux and may not know how to do such.

## Setup

If you want to learn don't copy paste, if you want it to just do stuff and don't care yeah just copy paste.

Open up a terminal, in stock ubuntu it's `control alt T`.

Now we want to grab the apt repo's public keys, this is used to verify packages.

```bash
curl -s https://deb.imaginary.stream/public.gpg | sudo apt-key add -
```

(This requires you to enter your admin password because it is using sudo)

Next we want to add the apt repo to the system's apt repo list:

```bash
echo "deb https://deb.imaginary.stream $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/imaginary.stream.list
```

(This will auto detect what version you are using and add it to a file)

Now update apt and install lokinet

```bash
sudo apt update
sudo apt install lokinet
```

## Usage

Once lokinet is installed it should be running in the background. The lokinet apt packages on ubuntu and debian automatically
set up the required DNS settings for accessing SNApps.

### SNApps

* [wiki](http://dw68y1xhptqbhcm5s8aaaip6dbopykagig5q5u1za4c7pzxto77y.loki/wiki/)

For help or idle chatter you can open an IRC client up and join our internal IRC network [here](irc://dw68y1xhptqbhcm5s8aaaip6dbopykagig5q5u1za4c7pzxto77y.loki/lokinet), play nice, have fun and don't forget that everyone is in a very diverse set of timezones so people may be quiet.
