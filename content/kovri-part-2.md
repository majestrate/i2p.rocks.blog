Date: 2018-12-12
Tags: i2p, i2pd, kovri, llarp
Category: blog
Title: Kovri and the curious case of code rot (part 2)
Authors: Jeff

Kovri has decided to fork the i2p protocol stack [[1]](https://gitlab.com/kovri-project/kovri/issues/1000). I too have had frustrations
with the direction and pase of java i2p and I can understand why they made this descision. 

In my personal opinion, I don't think kovri will succeed in their fork of the i2p protocol stack with its current talent pool.
After their 2 years of shuffling whitespaces around and not noticing code leaking regions of memory (until stiffing a security researcher that found it while exploit hunting) I don't think they'll produce a minimum viable product for a very very very long time, if ever.
This is not meant to poke fun at the people at monero and kovri as I really wanted to see the fork succeed, very much so and I am dissapointed in the net
result of the effort.

Parallell to all this kovri tom foolery, since Late April 2018 I have made a fully functioning i2p `"redux"` from the ground up.
Very much thankfully I have been hired to work on this full time. The protocol stack is called `LLARP` which is an acronym for `Low Latency Anon Routing Protocol`.

`LLARP` is an open standard that anyone can implement in their favorate language. It's a packet based onion routing network utilizing bidirectional onion routing `"paths"`. It uses bittorrent encoding for message serialization with fast cryptographic primatives `x25519` for key exchanges `blake2` for hash/keyed hash and `xchacha20` for symettric cipher. 
While the `"protocol docs"` are currently a hot mess in the spirit of being just like i2p (i kid), they can be improved if someone complains loud enough.
The reference implementation is in C++ licensed under ZLIB, a very good permissive license with some good verbiage like `"The origin of this software must not be misrepresented; you must not claim that you wrote the original software."` which I find quite valuable.

The current reference implementation is called [lokinet](https://github.com/loki-project/loki-network) which has some additional neato features like cryptoeconomic anti-sybil incentives but I digress. The future kovri is aiming for has already been implemented and I welcome anyone that wants to help build it up.
