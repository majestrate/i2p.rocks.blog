Date: 2019-03-06
Tags: lokinet
Category: development
Title: Lokinet Update March 2019
Authors: jeff

We are most likely on schedule for an end of Q1 2019 `"public release"` of lokinet if all goes well in the internal testing phase. `( don't know why we are considering it a public release since the code is public already but eh... ‾\(._.)/‾ )`
We have an internal code freeze in mid march and I hope to have a stable build ready. 

## Unit tests are HARD `D:`

It's been about 10 months since I started working on lokinet full time. The master branch on github has been relatively stable for 2 months and 
work on the staging branch is very heavy. We have currently 855 test cases across 95 test suites and we're not even close to full test coverage.
You can generate a progress report on unit test converage as of now (March 2019) [here](/files/lokinet-coverage-march-2019/). My personal goal is to get
at least 85% coverage on the code base by 2020. Unit tests are great, when you have them. The biggest roadblock to having full unit test coverage is
isn't just making the actual test cases, it's making code testable to begin with. Initially I had a nice high level module design back way in the beginning
when the project was in pure C. As the project (d)evolved into C++ the initial module structure assimilated into 1 big monolithic library. This was a big
mistake as it permitted lazy design choices with highly coupled components. Over the next while in contendum with unit tests I will be modularizing the 
codebase a lot more. This will allow for proper mocks and unit tests. We brought on another very talented developer, Micheal. He has been the biggest
inspiration for me as he started the initiative to have full unit test coverage to begin with. I was too focused on the deliverable and lost sight of the 
overall goals and ethos I started with and I am thankful for this realization.


## Onion routing is HARD `D:`

The biggest troubles I have had so far is with integration testing and network stability over all.
Turns out implementing a distributed onion routing network properly is hard (wow! WHO KNEW!?). The current bugs I am chasing are the following.

* Clients don't try to connect to service nodes after network outage

* Unpexectedly low path build success ratio because of buld timeouts

* Randomly get downstream messages that are garbled after decryption

I'll go into depth on them here one by one.

### Clients don't try to connect to service nodes after network outage

My initial thoughts are that this is caused by either:

* a timer with expontential/linear backoff that doesn't get reset properly and as a result grows freaking huge.

* some other bullshit

For the first possible cause it's pretty easy to mitigate, just add a hard maximum for timer timeouts and warn if we try to set above it.
For the other possible case It'd be best to write unit tests to pinpoint what is failing.

### Unexpectedly low path build success ratio because of build timeouts

The current protocol uses oneshot path build messages and has no way to prematurely cancel a build as a participant.
This was on purpose to try to prevent network malluablity attacks where service nodes passively move builds over service nodes they are colluding
with. It's probably worth it to add a new message for premature path build cancelling so that when a service node goes down it can notify all peers of such.
This is the one thing from i2p that I kept that I despised about i2p's protoocl, mainly because I couldn't come up with any alterntaives right away and was
under serious time constraints. Looking back it's probably no longer optional.

### Randomly get downstream messages that are garbled after decryption

Currently the path hop encryption is not authenticated, not sure how easily I could make it such but that is something to explore for sure.
Because of how onion routing operates it could only really be done in the upstream direction because it's doing decryption when in the upstream
direction. In the downstream direction the recipiant doesn't really know what it's going to get, it arrives with the closest hop's encryption
on the outer most layer. If each hop layer has its own message authentication tags then we'd need 8 slots for each message because the build records
have 8 slots. We don't want to leak the path length so this would increase the overhead by 256 bytes (8 * 32) per upstream and downstream message.

## Conclusion

We will be doing a network upgrade on toynet to 0.4 which has many backwards incompat changes and security improvements, soon.

