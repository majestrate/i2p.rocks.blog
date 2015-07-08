Date: 2015-07-08
Tags: blog, nntpchan, livechan
Category: blog, nntpchan, livechan
Title: NNTPChan Part 1 -- Torchan and Overchan

After some downtime, I finally got around to restoring my blog since there's something to talk about.

I have been working on rebasing some software for a decentralized imageboard so that it can work with clearnet.

Wait wat? Here's The backstory.

In the beginning, there was Torchan. Rather, there was a version of Torchan that didn't permit *that* content. ( \*cough\*seepea\*cough\* ). It was according to the original host, most likely the largest tor only imageboard at the time.
After a series of DoS attacks, internet drama, vps bills piling up, the original host decided to hand off the site and the private keys to someone else.
What happened after that caused the desire to create an imageboard that is invulnerable to any kind of global power grab. The new host, initially using the nym "dgft", didn't want to play nice. The new moderation team effectively made the site
absolutely inaccesable, disabling images, nuking threads that disagreed with moderation or any other policies or anything that wasn't "WE LOVE YOU ADMIN". A global power grab. This caused the eventual death of Torchan and the community fragmented.
Some intermediary imageboards popped up, trichan, oniichan and alliumIB. Trichan was a yotsubaX imageboard ran by triphorce, hosted on the original freedom hosting which got nuked by FBI (thanks obama). alliumIB, was hosted on a VPS provider that did an exit scam.
Oniichan was a tinyboard based imageboard that "consumed by the overchan".

While the refugees on Torchan sat on irc, Anonet was building overchan. [Anonet](http://anonet.org/faq.htm), a BGP routing community, provides an alternative BGP routed internet that sits atop VPN Tunnels on top of VPN Tunnels. Their motto, tunneling tunnels of tunnels, is quite fitting. A few obscure software have come out of the Anonet community
but the most important one is SRNd and the overchan protocol spec. Overchan is a protocol guideline for a decentralized nntp based forum, including a pastebin and imageboard with decentralized, optional moderation via cryptograpgically signed articles.
With overchan, you can use any existing nntp daemon (i.e. inn2) to manage and forward nntp articles on top of which you build your own HTTP based UI, called frontend. SRNd ( Some Random NNTP Daemon ) was a quarky nntp daemon + assorted plugins that was the overchan's
reference implementation. There were many different implementations of overchan, including one written in haskell but all except SRNd were lost to time.

Next blog will be about the differences between nntpchan and overchan. Don't worry there aren't any that break backwards compatibility.
