Date: 2016-11-25
Tags: i2p, i2pd, GFW, freedom
Category: blog
Title: Connecting to I2P network through restrictive firewalls
Authors: Darknet Villain

If you'll ever experience problems with connecting to [I2P network](https://i2pd.website), your Internet Service Provider may be blocking access to I2P bootstrap servers.
It is not a big deal if you have access to GitHub.

Edit reseed section in your [i2pd](https://i2pd.website) config file `i2pd.conf` file like that:

    [reseed]
    verify = true
    file = https://github.com/r4sas/i2pd-reseed/releases/download/1.0/i2pseeds.su3

or run binary with option:

    ./i2pd --verify true --reseed.file https://github.com/r4sas/i2pd-reseed/releases/download/1.0/i2pseeds.su3

and you will bootstrap to I2P network from GitHub.

Alternatively, simply download [this file](https://github.com/r4sas/i2pd-reseed/releases/download/1.0/i2pseeds.su3) with web browser and reseed from local file:

    ./i2pd --verify true --reseed.file i2pseeds.su3
