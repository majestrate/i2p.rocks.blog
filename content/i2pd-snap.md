Date: 2017-08-22
Tags: i2p, i2pd, snap, snapcraft, snappy
Category: blog
Title: Exploring snappy package manager. Why it is awesome and how to get started.
Authors: Invisible Villain

For those who don't already know, Snappy is a distribution agnostic package manager for Linux developed by Canonical.

Snap packages are self-contained archives with all required dependencies included. 
Applications run in a secure sandbox environment isolated from the main system, using such technology as 
[Linux namespaces](https://en.wikipedia.org/wiki/Linux_namespaces), [seccomp](https://en.wikipedia.org/wiki/seccomp) and [AppArmor](https://en.wikipedia.org/wiki/AppArmor).

I've recently created [snap package](https://github.com/PurpleI2P/i2pd-snap) for [i2pd](https://github.com/PurpleI2P/i2pd), and very excited to share my experience.

# Awesome features

## Security

Snaps are sandboxed and isolated from your main system. Applications can only have access to system resources allowed by package developer. 

For example, those are system resources allowed to i2pd package:

    plugs: [network,network-bind]

i2pd can only access network, bind ports and use it's own virtual filesystem, everything else will be denied by kernel.

In theory, one could even run untrusted proprietary code safely.

## Snap store

Snaps are simple archives, which can be downloaded and installed by hand as regular deb/rpm ones.
To automate distribution and updates there are snap stores. You may use Ubuntu store or create your own.

Since i2pd is not in the main Ubuntu repository yet, this is a huge advantage for us.
Installing i2pd on any snap-enabled Linux system is as easy as:

    sudo snap install i2pd

And you have i2pd running.

All Ubuntu images since 16.04 come with snapd installed by default. 

## Packaging

To create packages there is a tool called `snapcraft`. You define how package is being built in one `snapcraft.yaml` file and run `snapcraft snap`.

The concept behind snapcraft: there are "apps", "parts" and package metadata.
Parts are building blocks for apps, you define how those parts are being obtained and built. 
Apps are final utilities and daemons, which are available in this package.

If your software is a daemon, snap will create systemd unit for it automatically, just define `daemon: simple`:
    
    apps:
      daemon:
        command: i2pd-wrapper
        daemon: simple

Also, you can easily cross-compile snaps for other architecture with just one parameter `--target-arch`.

I wouldn't say packaging is dead simple, but for what it accomplishes, it is very good.


# Criticism

This post is not an advertisement for snap, so here is full truth about it.

## Snap is not a replacement of your system package manager

Obvious downside of having self-contained package is it takes a lot of disk space.
i2pd deb package size is only ~700KB, snap package size is 14MB. Plus, snaps require to have common Ubuntu Core, which size is 84MB.

So, snaps may be fine for some setups, but not everywhere. 

## Still developing

Snappy was introduced in 2014 and it is still pretty fresh.  
I've tried to install i2pd snap at Debian 9 and it seems to have issues with Ubuntu Core image.
Yet Ubuntu and Fedora setups were successful and easy.

Docs are not the best, but community seems to be very active and helpful. I think it will grow a lot more in the future.

## Systemd

For those who don't like systemd, it is a downside. I don't know if snap can work without it, probably no.


# How to get started

Ubuntu community has created [tutorials](https://tutorials.ubuntu.com) for various things, including snap. 

I would also recommend to have a look at examples by [snapcrafters community](https://github.com/snapcrafters).
Just fork their boilerplate repo and change for your needs, copying features form other examples.


# Final thoughts

I personally like this approach to package distribution. Key features I like are security isolation and ease of use.
There also are alternatives, like [Flatpak](https://github.com/flatpak/flatpak) by Gnome folks, which may be of interest.


