Date: 2017-01-16
Tags: i2p, i2pd
Category: blog
Title: i2pd keyinfo tool and more
Authors: Jeff

If you ever ran i2p you've noticed that both java i2p and i2pd use a web ui for most interactions. For some (most, if you count "power users") this is not desirable. Until recently there existed no documented command line tools for simple tasks (i.e. getting the b32 address of a destination given a private key file).

Java i2p has some utilities deep within their codebase for this but no documentation on how to use them. Hence the [i2pd-tools](https://github.com/purplei2p/i2pd) repo was born.

Building:

    git clone --recursive https://github.com/purplei2p/i2pd-tools
    cd i2pd-tools
    make 

The most useful tool in my opinion is `keyinfo`, a tool that extracts useful information about a private key file, i.e. the full destination, the key type and the `.b32.i2p` address.

    ./keyinfo privatekey.dat

The `routerinfo` tool can be used to generate linux iptables rules to permit traffic to a router given its router.info file.

    # generate firewall rules to allow every node currently in the netdb through the firewall
    ./routerinfo -f ~/.i2pd/netDb/*/*.dat > i2p.iptables2.txt

The `keygen` tool generates a destination private key:

    # generate an eddsa destination private key
    ./keygen mysite.dat 7
    
    
More tools will be made when new ideas for tools come about. 

Maybe I'll write an i2p Vanity Address generator like scallion next.


