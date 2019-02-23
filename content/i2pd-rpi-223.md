Date: 2019-02-24
Tags: i2pd, raspberry pi, arm
Category: blog
Title: i2pd 2.23.0 static arm build
Authors: jeff

my unofficial static arm build for i2pd 2.23.0 is up [here](/files/i2pd-rpi/2.23.0/).

**make sure to check the signature and verify the hash**

b2sum:

    e4cf21c06ae441030253dcb636eb05f0b5dc6405879b86b3b8f734a3195856ab20163c780c1c144e47f50dd9f8dc748bd243739262e2bd98fe05dac473c5c4b8  i2pd
    
the build was compiled with `-Os` and stripped for smaller size, so you may have better speed on systems without speculative execution like the raspberry pi 1.

uses: 

* openssl 1.1.1a
* boost 1.62.0
