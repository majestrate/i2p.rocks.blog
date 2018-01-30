Date: 2018-01-30
Tags: i2p, i2pd, release
Category: blog
Title: i2pd 2.18 released
Authors: PurpleI2P Team

[i2pd](http://i2pd.website/) (I2P Daemon) is a full-featured C++ implementation of I2P client.

I2P (Invisible Internet Protocol) is a universal anonymous network layer. All communications over I2P are anonymous and end-to-end encrypted, participants don't reveal their real IP addresses.

I2P client is a software used for building and using anonymous I2P networks. Such networks are commonly used for anonymous peer-to-peer applications (filesharing, cryptocurrencies) and anonymous client-server applications (websites, instant messengers, chat-servers).

I2P allows people from all around the world to communicate and share information without restrictions.

i2pd is licensed under the 3-clause BSD license, [binary packages are available](https://github.com/PurpleI2P/i2pd/releases/latest) for Debian, Ubuntu, OS X, FreeBSD, Android and Windows.

[View release on GitHub](https://github.com/PurpleI2P/i2pd/releases/tag/2.18.0)

**Changelog for i2pd version 2.18:**

### Added
- Show tunnel nicknames for I2CP destination in WebUI
- Re-create HTTP and SOCKS proxy by tunnel reload
- Graceful shutdown as soon as no more transit tunnels
### Changed
- Regenerate shared local destination by tunnel reload
- Use transient local destination by default if not specified
- Return correct code if pid file can't be created
- Timing and number of attempts for adressbook requests
- Certificates list
### Fixed
- Malformed addressbook subsctiption request
- Build with boost 1.66
- Few race conditions for SAM
- Check LeaseSet's signature before update
