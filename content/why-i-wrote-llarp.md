Date: 2019-03-11
Tags: i2p, i2pd, lokinet, llarp, monero, loki
Category: blog
Title: Why I wrote LLARP
Authors: Jeff


Recently I happened across a [bitcoin talk thread](https://bitcointalk.org/index.php?topic=753252.msg49713342#msg49713342) while peeking at my blog's http access log at a time when I should've been doing work instead.

I'll probably take this chance to make it very clear what llarp/lokinet is and is not.

I can say that, in my opinion, llarp/lokinet is `attempting to be a protocol to replace i2p`.

I2P has a mountain of technical debt in their protocols that have been taking several (5+) years now to rectify. It is in fact easier to rewrite the whole thing than to rebase the protocol atop sanity. I am not the first person to suggest this by any means, nor the first to attempting it. The first attempt I have seen was the shadow protocol from 2013. For whatever reason it died off, I personally suspect it was because of the bizare license it was released under. I2P can be improved it's just easier to redo the whole dang thing, and that's exactly what I claim to have done [here](https://github.com/loki-project/loki-network). By no means is this a hot shot at the expense of i2p, i2pd or kovri, it's more of a result of autistic frustration waiting for crypto upgrades and the purging elgamal from the i2p protocol stack. I simply got tired of waiting for it and decided to do something.

I can also say that, in my opinion, llarp/lokinet `won't be a replacement to Tor anytime soon and may never be`. 

Tor has over a decade (aka a massive shitload) of work behind it and has basically become a utility tier project that people use to access the internet in censored areas, this means most of their time is spent doing censorship resistance. Network blocking resistance is a never ending cat and mouse game that the DoD and US Navy is most suited to fund and I doubt that llarp/lokinet will ever be able to rival it given the current parameters. I won't discount the chance that some day we will be able to surpass Tor and friends but I personally wouldn't count on it any time soon, if ever. It may be that since I consider fingerprint resistance currently an explicit non-goal Tor will always have an edge. That's fine as I am aiming to supplant i2p not Tor. 

I made llarp/lokinet to realize the potential I saw in i2p that could have been if people put more elbow grease into it. Alas it turns out it was in fact easier to rewrite it as zzz once said in a off the cuff remark in a meetup IRL once I attended. Is llarp/lokinet a hostile takeover of i2p? Mostly no but probably also a little bit yes (I wouldn't consider it hostile but that isn't up to me to decide). I would like llarp/lokinet to replace i2p if possible but I am not going to force it, I want my project to stand by its own merits and win people over by being better.
