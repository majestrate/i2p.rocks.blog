Date: 2016-09-12
Tags: i2p, i2pd, i2lua
Category: blog
Title: Meet i2lua -- I2P router with "smart" configuration
Authors: Invisible Villain

With [i2lua](https://github.com/majestrate/i2lua) you can add custom logic to your [Invisible Internet](http://i2pd.website) router
 by writing scripts in [Lua](https://en.wikipedia.org/wiki/Lua_%28programming_language%29).

Lua is a full-featured programming language, which means you can resolve complex issues with it. 

Some basic tasks you can accomplish with i2lua:

* make all tunnels to have only trusted nodes as first hop (restricted routes, similar to Tor's guard nodes)
* make I2P router to only use high-speed nodes for building tunnels
* create tunnels with first hop in specific countries (e.g. make connections only to Russia and Germany)
* implement custom node profiling mechanism

and so on.

[Example script for i2lua](https://github.com/majestrate/i2lua/blob/master/contrib/examples/example.lua)
