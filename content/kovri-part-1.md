Date: 2017-09-27
Tags: i2p, i2pd, kovri, e-drama
Category: blog
Title: Kovri and the curious case of code rot (part 1)
Authors: Jeff

I'd like to preface this going in as being clear that I like monero project and think they make a damn fine coin.
Yes, they have a rather elitist community but such comes with the territory. I have interfaced with the kovri codebase in the past
and I can say that the project left me rather disapointed. To really get a good grasp of the sitatuon I need to go back to 2014 (?).

## i2pcpp and i2pd 0.x.x

In the begininning there was i2pcpp, a decent partially working i2p router written in C++ 11 for FreeBSD by a guy with the nym orion.
Orion was originally funded by the monero community but discontinued i2pcpp after i2p's protocols left a sour taste in his mouth.
My only role in i2pcpp was trying to compile it on Linux as at the time my C++ was pretty much non existent. Orion is a very capable person,
he made some of the best C++ code I have seen to date, not too complex yet not overly simplistic. 

Around the time i2pcpp was discontinued someone approached the author of i2pd, orignal and offered him some promise of funding to make
a C++ implementation of i2p. The details are unclear to me but orignal asserts that fluffypony directly sought him out on the pretense that
he may be able to get a monetary compensation. The quality of i2pd 0.x.x in 2015 was abhorant, lots of memory leaks, a Buffer overflow here
and there and MIXING SPACES AND TABS with all files in one directory. It used cryptopp and boost.

## "Forking" i2pd

Around 2016 orignal left for a period of time for holiday, some people thought he left for good so a bunch of contributors (myself included)
"forked the repository". When i say "fork" I mean push changes to the repo like refactoring the directory structure and changing all files to use 
spaces not tabs, all without orignal's knowlege. When orignal came back he was fuming, he pushed some code to bitbucket and rebased stuff there, 
the new codebase for i2pd used openssl and zlib instead of cryptopp because of a bug in cryptopp. I moved over to try and work on kovri because it 
uses...

SPACES

NOT

BOTH TABS AND SPACES.

## Contributing to Kovri

I started trying to fix bugs in kovri but the maintainer of the project anonimal was insufferable and I could not continue so I went back to i2pd.
I am not alone in experiencing this as I have talked to 2 other previous contributors and we came to the same conlcusions about why anonimal acted 
the way he did. He was probably a kid that bit off more than he could chew, in deep shit with lots of XMR being allocated for him to do dev work.
We knew he had minimal C++ experience from his relatively small amount of C++ changes.

## Kovri is code rot

Kovri's code is based off a i2pd-0.x.x git revision, possibly one of the worst revisions in the code. Some parts of the code have been fixed 
but most of the underlying problems have been hidden behind pedantic C++14 boilerplate code, directories refactored and files reformattted with
uncrustify. None of the underlying bugs they started with have been fixed to my knowledge (as of writing this blog post) and the repository is
full of changes of everything you can think of besides C++. Lots of github flare, bash scripts, unit testing, git submodules, but very few changes
in the parts that actually provide functionality. Despite massive lots of publicity kovri has yet to provide a stable router and progress seems to have
stalled while monero project hunts for new contributors. 

This blog got pretty long so I'll put more information in Part 2, comming soon ™
