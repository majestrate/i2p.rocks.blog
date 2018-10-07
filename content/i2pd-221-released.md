Date: 2018-10-07
Tags: i2p, i2pd, release
Category: blog
Title: i2pd 2.21 released
Authors: PurpleI2P Team

[i2pd](http://i2pd.website/) (I2P Daemon) is a full-featured C++ implementation of I2P client.

I2P (Invisible Internet Protocol) is a universal anonymous network layer. All communications over I2P are anonymous and end-to-end encrypted, participants don't reveal their real IP addresses.

I2P client is a software used for building and using anonymous I2P networks. Such networks are commonly used for anonymous peer-to-peer applications (filesharing, cryptocurrencies) and anonymous client-server applications (websites, instant messengers, chat-servers).

I2P allows people from all around the world to communicate and share information without restrictions.

i2pd is licensed under the 3-clause BSD license, [binary packages are available](https://github.com/PurpleI2P/i2pd/releases/latest) for Debian, Ubuntu, OS X, FreeBSD, Android and Windows.

[View release on GitHub](https://github.com/PurpleI2P/i2pd/releases/tag/2.21.0)

**Changelog for i2pd version 2.21:**

### Added
- NTCP2 ipv6 incoming connections
- Support android api > 26
- Show total number of destination's outgoing tags in the web console
### Changed
- Use EdDSA, x25519 and SipHash from openssl 1.1.1 if available
### Fixed
- Bandwidth classes 'P' and 'X' without 'O'
- Update own RouterInfo if no SSU
- Fixed NTCP address disappears if NTCP2 enabled

