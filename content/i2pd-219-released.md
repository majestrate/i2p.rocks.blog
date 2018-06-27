Date: 2018-06-27
Tags: i2p, i2pd, release
Category: blog
Title: i2pd 2.19 released
Authors: PurpleI2P Team

[i2pd](http://i2pd.website/) (I2P Daemon) is a full-featured C++ implementation of I2P client.

I2P (Invisible Internet Protocol) is a universal anonymous network layer. All communications over I2P are anonymous and end-to-end encrypted, participants don't reveal their real IP addresses.

I2P client is a software used for building and using anonymous I2P networks. Such networks are commonly used for anonymous peer-to-peer applications (filesharing, cryptocurrencies) and anonymous client-server applications (websites, instant messengers, chat-servers).

I2P allows people from all around the world to communicate and share information without restrictions.

i2pd is licensed under the 3-clause BSD license, [binary packages are available](https://github.com/PurpleI2P/i2pd/releases/latest) for Debian, Ubuntu, OS X, FreeBSD, Android and Windows.

[View release on GitHub](https://github.com/PurpleI2P/i2pd/releases/tag/2.19.0)

**Changelog for i2pd version 2.19:**

### Added
- ECIES support for RouterInfo
- HTTP outproxy authentication
- AVX/AESNI runtime detection
- Implementation of I2CP reconfigure
- Datagrams to websocks
- Initial implementation of NTCP2
- Added I2PControl method "ClientServicesInfo"
### Changed
- Android build using gradle
- EdDSA for RouterInfo by default
- Multiple changes for QT GUI
### Fixed
- Fixed tunnels reload
- Fixed headers in webconsole
- Correct SAM session name
- Updated docker
