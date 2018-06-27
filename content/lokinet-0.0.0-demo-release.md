Date: 06-27-2018
Tags: lokinet
Category: development
Title: LokiNET 0.0.0 demo build released
Authors: jeff

In May of 2018, I got an email from loki project with a job offer for a full time position developing my 
toy onion routing protocol called llarp. Since this is an offer to get paid to do my dream job I accepted.
I will continue to work on i2pd but my main focus is now on [LokiNET](https://github.com/loki-project/loki-network).

So, Today I am releasing [LokiNET 0.0.0](/files/lokinet/0.0.0/) a minimal demo build of the mixnet I am building. It doesn't really do anything
interesting right now because there is literally just 1 or 2 nodes that exist. I am releasing this build mainly to get feedback
from potential relay operators BEFORE the loki integration happens. I want to iron out any prelimiary issues with the daemon
before going to loki stagenet. 

Current Features:

* primative preliminary onion routing, no hidden services, no exit functionality (yet)
* encrypted wire protocol for inter node comms
* multithreaded crypto workers
* simple ini style config


If you set up a public relay node please make a PR with the `self.signed` file renamed to `yourname.signed` in `contrib/testnet` directpory inside the [testnet repository](https://github.com/majestrate/llarpd-builder). 

In the future bootstrap will be more automated but for now it's totally manual, this is subject to change.
