Date: 2017-12-04
Tags: i2p, i2pd, release
Category: blog
Title: i2pd 2.17 released
Authors: PurpleI2P Team

[i2pd](http://i2pd.website/) (I2P Daemon) is a full-featured C++ implementation of I2P client.

I2P (Invisible Internet Protocol) is a universal anonymous network layer. All communications over I2P are anonymous and end-to-end encrypted, participants don't reveal their real IP addresses.

I2P client is a software used for building and using anonymous I2P networks. Such networks are commonly used for anonymous peer-to-peer applications (filesharing, cryptocurrencies) and anonymous client-server applications (websites, instant messengers, chat-servers).

I2P allows people from all around the world to communicate and share information without restrictions.

i2pd is licensed under the 3-clause BSD license, [binary packages are available](https://github.com/PurpleI2P/i2pd/releases/latest) for Debian, Ubuntu, OS X, FreeBSD, Android and Windows.

[View release on GitHub](https://github.com/PurpleI2P/i2pd/releases/tag/2.17.0)

**Changelog for i2pd version 2.17:**

### Added
- Reseed through HTTP and SOCKS proxy
- Show status of client services through web console
- Change log level through web connsole
- transient keys for tunnels
- i2p.streaming.initialAckDelay parameter
- CRYPTO\_TYPE for SAM destination
- signature and crypto type for newkeys BOB command
### Changed
- Correct publication of ECIES destinations
- Disable RSA signatures completely
### Fixed
- CVE-2017-17066
- Possible buffer overflow for RSA-4096
- Shutdown from web console for Windows
- Web console page layout
