Date: 2019-01-05
Tags: i2p, i2pd, kovri
Category: blog
Title: Kovri and the curious case of code rot (part 3)
Authors: Jeff

Before the final post I'll give on this topic, a bit of backstory as I understand it.

During winter of 2015 (or was it 2016? I forget.) orignal the original author of i2pd took a 2 week winter vacation while the codebase 
was in shambles. During this break some of the contributors of i2pd decicded to hard fork the codebase starting with turning all the tabs 
to spaces. It is unclear if anonimal was a part of the group or not.

When original came back he flipped his living shit and put his new changes that used openssl onto bitbucket and then later merged it
on github in another branch. This is the historical reason why i2pd uses the `openssl` branch and not `master` as the primary branch.

kovri is based off the code base before the openssl branch which is truly godawful, however almost none of it remains in i2pd today.

This morning anonimal put a message on a pastebin directed to `#monero-dev` and I think he does make some good points but fundamentally misses 
the underlying problem.

He has said a few things specifically his reasoning why the codebase `"is a steaming pile of dog-shit"`


> * I was the only dissenting voice before the fork that said DO NOT FORK THIS CODEBASE. I should've ignored fluffypony.

This part is unclear if it is true as I have no information on this.

> * I've only been able to dedicate ~30% of my time so far to code development because, up until now, no one else was running the project (see my FFS)

The monero fork was made because the code was really bad, it was the fork maintainer's responsiblity to remidy this. Rather, that is what was promised.

> * There was no design planning, no concept of architecture, nothing but stream-of-conscience writing in the code that was forked. A very large, convoluted technology with no planning or even conventional coding standards = recipe for disaster.

Such is the state of i2p and many other free software projects, monero included. That is what happens, it's just a reality. When someone goes off to make a thing it usually devolves into a stream of concience with little planning. Almost nothing is planned out and executed the same, I learned this myself with llarp but maybe that's another blog post.

> * Every code change makes every other change a complete waste of time to deal with because there's no real design in place to support either. Experienced developers see the overarching problems and walk away. To simply "swap-out" old code with new code has proven to be a waste of time because all the old interfaces need to go.

I won't use the no true scottsman fallacy here. The primary I2PD fork managed to sort out the code a bit better after a bit of elbow grease was applied over a few years. Alas, this is the state of software engineering, newbies take on a huge challange and churn out a shit. Experience comes from iteration on piles of shit because eventually everything is in the end a shined turd anyways. Nothing is pure as such is a myth. No one starts out with a great plan and doesn't get dirty along the way, that's just not realistic. From what I understand, experienced developers would buckle down and do their job and get it done, but I wouldn't know as I am not THAT experienced, yet.

> * fluffypony flaked, on multiple levels, hardcore, having left me to do everything after promising before the fork that Monero contributors would be involved (why the fuck would I create Kovri if Monero wasn't going to contribute? Answer: incentive, and because I believed in Monero technology and still do, but I could've simply contributed to Monero code instead of doing this project).

I have also experienced this but I don't think it's reasonable to blame other people for the lack of results that was promised.

> If I had my way, I'd spend the next ~4 months designing a new router implementation from the ground-up and write it from scratch. At this point though, I'm tired, and I've created a better solution with Sekreta.

I have already done this myself with llarp and I'll warn that such plans never pan out into the ideal you've imagined. There are always unexpected gotchas and unforseen roadblocks. Over time, my experiences has shown me that these are just a part of the job description and I feel like I am not alone in this regard.

... the post gets progressively more angry into a trainwreck, so I'll start wrapping up.


> Now, if you want me to hook this pile of crap into Monero, ask yourself why haven't YOU (metaphorical you) done it? Why do you expect ME to be the fall guy, yet again? Why ignore 99% of the critical-problems in favor of solving 1% of non-critical problems?

Why? It's in the job description, you were supposed to fix up kovri and maintain it such that it would be acceptable by monero standards, at least that was the vibe everyone seemed to get. You took on the job, you couldn't do it and now you're blaming other people. Just own up on your mistakes and be honest with everyone and more importantly be honest with yourself, specifically with regards to your ability to maintain a code base. Don't bite off more than you can chew.

Anonimal, it would be nice to have a chat about how monero can better help anonymize transactions using another layer, but don't you think you've dug yourself a big enough hole? Promising a new and improved layer ontop of existing ones when you couldn't even manage? All by yourself? The realm of higher latency networking which is most definately the future but they lack an end user demographic, adding monero would help that indeed but come back down to earth. One thing I have learned is that you can't do everything yourself. It's not bad to ask for help from others, just get off your high horse and stop blaming others for your own mistakes and miscalculations. I don't hold anything against you as I have been in similar sitatuons, the way out is to be honset about the sitatuon and humble about your capabilities and hope people understand.


Copy of the orignal message from https://paste.debian.net/plain/1058561

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

#monero-dev

2019-01-03 23:24:37     anonimal        If anyone is confused or angry, I implore you to ask questions.
2019-01-03 23:25:30     thrmo   I'm just sad that you wasted so much your time and the community ditched so much money and hopes (and the opportunity to research other venues) on kovri
2019-01-03 23:25:39     thrmo   other than that I wish sekreta the best
2019-01-03 23:26:09     krakn   Can anyone fill me in on this issue?
2019-01-03 23:27:27     anonimal        krakn: which one? Sekreta questions are in #sekreta / #sekreta-dev
2019-01-03 23:28:00     krakn   What thrmo said
2019-01-03 23:28:54     anonimal        Ah, there's a very clear timeline and I can certainly harp on the various issues. Not #monero-dev worthy though for the most part.
2019-01-03 23:29:08     thrmo   this is probably not the best venue for that krakn
2019-01-03 23:29:14     krakn   Gotcha
2019-01-03 23:31:14     anonimal        So, let's clarify some of the confusion, as it's #monero-dev related.
2019-01-03 23:33:49     thrmo   please go ahead then anonimal

First, to your clarify the "so much money" claim (it's not the first time this has come up), $50k is not a lot of money for a year's wage. Market manipulation made it go in every direction. I was screwed in 2018 just like a lot of other people. I would've made more money working at ABC corp instead of Monero; less stress too, and less taxes on fake money instead of real electronic money. Oh, and did I mention how much of my time I've donated over the years?

Secondly, I do feel like I wasted *some* of my time but I'm ultimately responsible for my actions. My FFS clearly documents what has happened over the course of development. I've built this project from the ground up after everyone else abandoned it. I've also taught every developer that has come through the project - and that's not a waste of time.

Thirdly, this codebase is a steaming pile of dog-shit. Still. Because of the following reasons:

* I was the only dissenting voice before the fork that said DO NOT FORK THIS CODEBASE. I should've ignored fluffypony.
* I've only been able to dedicate ~30% of my time so far to code development because, up until now, no one else was running the project (see my FFS)
* There was no design planning, no concept of architecture, nothing but stream-of-conscience writing in the code that was forked. A very large, convoluted technology with no planning or even conventional coding standards = recipe for disaster.
* Every code change makes every other change a complete waste of time to deal with because there's no real design in place to support either. Experienced developers see the overarching problems and walk away. To simply "swap-out" old code with new code has proven to be a waste of time because all the old interfaces need to go.
* fluffypony flaked, on multiple levels, hardcore, having left me to do everything after promising before the fork that Monero contributors would be involved (why the fuck would I create Kovri if Monero wasn't going to contribute? Answer: incentive, and because I believed in Monero technology and still do, but I could've simply contributed to Monero code instead of doing this project).

In hindsight, I should've ignored everyone and done this correctly from the beginning. Kovri is an *extremely* sound idea, and is absolutely necessary as a concept; but Kovri 2.0 needs to happen before Kovri 1.0; and almost no one in this community seems to fully understand this nor care for that matter (but maybe that will change now?).

If I had my way, I'd spend the next ~4 months designing a new router implementation from the ground-up and write it from scratch. At this point though, I'm tired, and I've created a better solution with Sekreta.

Now, if you want me to hook this pile of crap into Monero, ask yourself why haven't YOU (metaphorical you) done it? Why do you expect ME to be the fall guy, yet again? Why ignore 99% of the critical-problems in favor of solving 1% of non-critical problems?

Integration and dependencies are a COMMITMENT. A REAL COMMITMENT. Do you even KNOW what you'll be committing to? Why would ANYONE here want to commit to something that they've put almost no time and effort into and know almost nothing about?

Keep in mind, if I was a malicious person, I would've hooked Kovri in 2017 and reaped the bounty of 0days; thus doubling my profits at the community's expense. But I'm not that person.

So, if the Monero community, of which less than 10 people have actually contributed to Kovri Project, really wants to be a leader in privacy; then I'd advise for everyone to please look at the situation more objectively.

Single-system overlay network anonymity solutions are NOT THE FUTURE. I truly believe this because evidence is starting to grow supporting this idea.

I believe that Sekreta *is* the future. If not Sekreta, then an offshoot of (or something very similar) until societal collapse engineers new hardware from the ground-up. At that point though, the cheapest solution will win; not the most private. So, until then, the massive gaping holes for network privacy adoption are filled up more by Sekreta than anything else at the moment. This has been empirically proven.

Sekreta is also the chance for this community to redeem itself while proving to be a privacy leader. I'll tell you right now, the SOCKS proxy cop-out, a proxy of which I offered to implement years ago but was shot down, the proxy I wanted to implement because MONERO COULD'VE BEEN USING KOVRI THIS WHOLE TIME AS A RESULT, the proxy of which its non-usage was (affectionately called) Ponzirelli's foundation for the Kovri movement, should be a greater danger signal than anything else.

Now, where do we stand? If you're still concerned about having a baked-in I2P router, then you're completely missing the big picture. Here's your best options at this point:

1. Allow me to bill my 2nd to last milestone to Sekreta. By "allow", I mean that only the very few people who donated $50k should really have their voices considered
2. Allow me to use my *last* milestone to integrate Sekreta into Monero. Monero gets the credit as privacy leader as well as opens up the possibility to adopt Sekreta as a Monero Community project
3. Integration will consist first of the convenience API. Monero will be the testbed for developing this extremely important component. Rudimentary hooks into Tor and/or Kovri will soon follow. Components like SEK and 4SE can still be in the design process at this time because Monero would be only using a primitive SSD via the Convenience API. I want this done now. NOW. I can complete the integration by Q1 2019 and preliminary hooks by Q2 at the latest (this would interfere with the planning phase so expect related inconveniences as a result). If I have experienced engineers helping me though, we could get this done sooner.
4. My future FFS requests would be primarily for Sekreta as it is a new, innovative, solution - but I have no plans on "abandoning" Kovri.

*or*

1. Don't allow me to bill for Sekreta, piss me off, lose the opportunity to innovate, and get a shit-router integrated instead. Other privacy projects will realize that Sekreta is *NOT* a Monero thing and will adopt as a result
2. You're stuck with a dependency that no one will have the confidence to use and will instead want to default ALL OF THEIR TRANSACTIONS over Tor via Monero's proxy-of-shame https://forum.getmonero.org/9/work-in-progress/90923/lee-clagett-vtnerd-broadcast-transactions-over-tor-hidden-service. This is a great threat to privacy: not philosophically, but absolutely fucking empirically as proven by Sekreta - and puts Monero into shit-coin tier innovation. Boring.
3. Pigeon-hole Monero while projects like Nym take the lead in privacy https://www.coindesk.com/this-binance-backed-crypto-startup-wants-to-anonymize-everything (Sekreta eliminates a big chunk of Nym's edge)
4. My back taxes (apparently no one mentioned that monero = income tax), and being burned in 2018, will make me do what I need to do to survive.

I recommend that Kovri continue development in tandem with Sekreta. I've handed over almost all the reigns to Sean so I can devote time to Kovri code development over anything else kovri related, but I have no interest in Kovri 1.0. Also, Monero should have no interest in Kovri 1.0 because other implementations are being developed in tandem (as noted in the Sekreta draft). Sekreta CAPITALIZES on this new privacy ecosystem VERY WELL at YOUR benefit, so I would advise to think about the future and diverge your time and funding as appropriate.

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEEhhics1I4lOeLdKbZqduz5FECfEFAlwuu1cACgkQZqduz5FE
CfHo5Q/+OyVDf+Zm8GhoVWE03ISMn85gArQVwnUIpGmBndfJAoSIe6ZP2eeDITFe
Z/dTzALDFsxm+TAdnd030VegEQRcNGUR/k26XOdzVcNKvzgf5jl3H9EooK9U/fpq
pOURUfYszmRitjSbbmfXegkMntKTSeuinih/m29+bD4/z8hhv2CghdOD/esMXeEN
hUGUPrTTaB1FerEH7mhrWV5dgYB6gkA9fQx0MQHW5bjYN8HdhGPHtOW+DcSwVOri
EPUTAb9kT+VlhDO8xx1N6MtkKkvRmpW3gvRXM1poEynjktiu1t/1YYu/ZSa+Ygxy
cHA2zxqzTpFg33Ax/lqIV7bs3U4aQ6FZBruMlBK5nrYv1BQQktz/ZTjaYa+KLQLI
43uRHxoHqBMHM29cYCHhXmeZoY24X9I/JTQRUfaM1uATJN90s1Eyk6PNadHZ45aK
23XBs3FWmC9P2jF+gmxQSwInnbGlh9rddI0NQl9R8+d8Vyp95SxyEF8/fzm8zivs
ClVYezFsrXuyB3jyXJSzhKA2D2yQSHDZr8ZIDkZqlkk+k6Kz0Q+W6u8UgmpfIzE2
qyPhsI4+ZDLu0CYLE+dgdItRhGNEVUyy6vj3q3ZLu8YodHxJYR3hlb/HUiIoKm6d
DV6sYk5XHfjpsc9Ig/7c9bq3UqzEiBKLVyOgyCcfJadFGkP9I/w=
=RpFS
-----END PGP SIGNATURE-----
```
