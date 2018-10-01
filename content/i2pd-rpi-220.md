Date: 2018-10-01
Tags: i2pd, raspberry pi, arm
Category: blog
Title: i2pd 2.20.0 static arm build
Authors: jeff

my unofficial static arm build for i2pd 2.20.0 is up [here](/files/i2pd-rpi/2.20.0/).

**make sure to check the signature or verify the hash**

b2sum:

    68c93b6638f3c71f196bda651a564ea33f5e11196c328d471845f3998419821f0f992f184ad6990f6cda182bfcff6015ce8f93cf5b68a2907db7fe5d6da94e79  i2pd
    
sha256sum:

    3ed75a9d9edef80e14dfdeb89452d1ace2d370e3ee0f4b101105a13706e7c949  i2pd

    
the build was compiled with `-Os` and stripped for smaller size, so you may have better speed on systems without speculative execution like the raspberry pi 1.
