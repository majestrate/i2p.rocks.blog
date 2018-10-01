Date: 2018-10-01
Tags: i2pd, raspberry pi, arm
Category: blog
Title: i2pd 2.20.0 static arm build
Authors: jeff

my unofficial static arm build for i2pd 2.20.0 is up [here](/files/i2pd-rpi/2.20.0/).

**make sure to check the signature or verify the hash**

b2sum:

    f10bf0c2e913e420125ac392fa9c27f8ccdd16268acec5a1ef7e5b96621e813b05c5361c862e2bfa48e3d3590c7dff127c9676ddc78f7497945f120161ac43be  i2pd

sha256sum:

    bc5ab06804f076c0b8118e1bf29aef1ba5432bf39440c0b5d696187b87312f84  i2pd

    
the build was compiled with `-Os` and stripped for smaller size, so you may have better speed on systems without speculative execution like the raspberry pi 1.

uses: 

* openssl 1.1.1 
* boost 1.62.0
