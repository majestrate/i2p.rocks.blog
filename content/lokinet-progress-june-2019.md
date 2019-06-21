Date: 2019-06-21
Tags: lokinet
Category: development
Title: Quick Lokinet Update, June 2019 (1 year in).
Authors: jeff

One year has passed since working on lokinet full time and we've managed to make something
that works and does stuff. The upcoming release is being held off until "stability fixes"
are applied. When lokinet works it works very well, the problem we face right now is 
(I suspect) some lingering path handover logic errors which can be tuned out with time.
I'd really like to do a release but have been to hold off until the "stability fixes" are
applied. I don't know how long that will take and would rather do a release now so we can
start iterating on scaling the network and handling any possible issues in that. Over all
I suspect are ready for launch.

## Lokinet on mobile

The next step in development is the mobile port, which I am dreading. The lokinet code was
not made with mobile in mind, it was made to run on a soho router originally. To me, it 
seems it will be a pain in the balls to make it work seamlessly on mobile and not worth the
trouble at the current place in development we are at. Let it be known, I personally think
the mobile port is a mistake and a waste of dev time. 

My first justification for that thought is that the mobile app stores are the central point 
of control and because of their monopoly on that point tech giants will be able to effectively 
cut us out of their ecosystem at any time they wish, including the initial phase. I do not 
think we'll be accepted into the IOS app store.

A second justification is that the VPN APIs on these platforms are an even more fragmented
mess than on desktop. With mobile comes multiple new sets of boilerplate that I don't have 
time to maintain. 

A third justification is that phones have the worst connectivity of any other
platform in the history of man kind, I don't think we CAN provide a stable experience on
mobile just because of the spotty networking situation, all of this is omitting all the 
possible network filtering bullshit we may encounter on mobile data networks. 

A fourth justifcation, battery life and power management add a new dimension for the problems on
mobile to fractal into. Not only do you have to worry about network being flaky but the OS
freezing the application at arbtirary times for "power saving" reasons.

I could go on, but over all, mobile phones are bad and you should feel bad for propagating 
them as a platform for end user applications. 

## Consensus 2019

I met a lot of cool people while at consensus 2019 including David Chaum and his team working 
on some [really neat mixed latency mixnet technology that has post quantum properties](https://www.elixxir.io/)
that you should check out. Lots of other cool people were there and lots of interesting topics
were brought up. The common theme I got out of all the feedback was that lokinet `needs` delays.
I have added slots for these in the protocol spec but they have yet to be implemented.

The future looks very futuristic and I have no idea what will happen going forward.
