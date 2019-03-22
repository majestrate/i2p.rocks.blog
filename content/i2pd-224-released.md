Date: 2019-03-21
Tags: i2p, i2pd, release
Category: blog
Title: i2pd 2.24 released
Authors: PurpleI2P Team

[i2pd](http://i2pd.website/) (I2P Daemon) is a full-featured C++ implementation of I2P client.

I2P (Invisible Internet Protocol) is a universal anonymous network layer. All communications over I2P are anonymous and end-to-end encrypted, participants don't reveal their real IP addresses.

I2P client is a software used for building and using anonymous I2P networks. Such networks are commonly used for anonymous peer-to-peer applications (filesharing, cryptocurrencies) and anonymous client-server applications (websites, instant messengers, chat-servers).

I2P allows people from all around the world to communicate and share information without restrictions.

i2pd is licensed under the 3-clause BSD license, [binary packages are available](https://github.com/PurpleI2P/i2pd/releases/latest) for Debian, Ubuntu, OS X, FreeBSD, Android and Windows.

[View release on GitHub](https://github.com/PurpleI2P/i2pd/releases/tag/2.24.0)

**Changelog for i2pd version 2.24:**

### Added
- Support of transient keys for LeaseSet2
- Support of encrypted LeaseSet2
- Recognize signature type 11 (RedDSA)
- Support websocket connections over HTTP proxy
- Ability to disable full addressbook persist
### Changed
- Don't load peer profiles if non-persistant
- REUSE_ADDR for ipv6 acceptors
- Reset eTags if addressbook can't be loaded
### Fixed
- Build with boost 1.70
- Filter out unspecified addresses from RouterInfo
- Check floodfill status change
- Correct SAM response for invalid key
- SAM crash on termination for Windows
- Race condition for publishing
