Date: 2018-07-28
Tags: i2pd, raspberry pi, arm
Category: blog
Title: i2pd 2.19.0 static arm build
Authors: jeff

my unofficial static arm build for i2pd 2.19.0 is up [here](/files/i2pd-rpi/2.19.0/).

I use another branch for these builds located [here](https://github.com/majestrate/i2pd/tree/rpi-builds), it contains a few backports so I can compile with the [toolchain](https://github.com/s2ack/arm-bcm2708hardfp-linux-gnueabi) I use. 

**make sure to check the signature or verify the hash**

b2sum:

    84541717ac7c4592c45280ef76283df73604b94eb459d3c7b8f4fdb304c02cbe9caf00f9c38cb7a9829dac0d26958ee728775162eeda2456c9386fad53df6f76  i2pd
    
sha256sum:

    eec2e8bc9926f9fe0943457c7c5b274be6943dbaadc2693bd9341bf7747be499  i2pd

    
