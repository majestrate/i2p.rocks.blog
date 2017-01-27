Date: 2016-12-23
Tags: i2p, i2pd, release
Category: blog
Title: i2pd 2.11 released
Authors: PurpleI2P Team

[i2pd](http://i2pd.website/) (I2P Daemon) is a full-featured C++ implementation of I2P client.

I2P (Invisible Internet Protocol) is a universal anonymous network layer. All communications over I2P are anonymous and end-to-end encrypted, participants don't reveal their real IP addresses.

I2P client is a software used for building and using anonymous I2P networks. Such networks are commonly used for anonymous peer-to-peer applications (filesharing, cryptocurrencies) and anonymous client-server applications (websites, instant messengers, chat-servers).

I2P allows people from all around the world to communicate and share information without restrictions.

i2pd is licensed under the 3-clause BSD license, [binary packages are available](https://github.com/PurpleI2P/i2pd/releases/latest) for Debian, Ubuntu, OS X, FreeBSD, Android and Windows.

[View release on GitHub](https://github.com/PurpleI2P/i2pd/releases/tag/2.11.0)

**Changelog for i2pd version 2.11:**

* Full support of zero-hops tunnels
* Tunnel configuration for HTTP and SOCKS proxy
* Websockets support
* Multiple acceptors for SAM destination
* Routing path for UDP tunnels
* Reseed through a floodfill
* Use AVX instructions for DHT and HMAC if applicable
* Fixed HTTP Proxy connection reset for Windows
* Fixed UPnP discovery bug, producing excessive CPU usage
* Fixed sudden SSU thread stop for Windows
* Fixed crash upon SAM session termination
* Handle multiple lookups of the same LeaseSet correctly

