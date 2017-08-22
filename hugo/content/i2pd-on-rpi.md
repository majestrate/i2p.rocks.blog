Date: 2016-06-26
Tags: i2p, i2pd, tutorial
Category: blog
Title: Cross-Compile static I2PD for Raspberry Pi

(this guide is probably out of date)

I have recently successfully built [i2pd](http://i2pd.website) for the raspberry pi using a cross compiler on Ubuntu 16.04 LTS for amd64. So far i2pd has an uptime of over a week with no crashes or memory leaks running a small [irc server](irc://6mk5za2izxm5ubu7bhzw3io7x5h6yjnlc7iccmn2ilbwptceaiwq.b32.i2p/). There are still a few things i2pd could do better, specifically more documentation but I digress.

## Building

First off if you don't have `git` install it along with the basic compiler stuffs.

    #!bash
    $ sudo apt install git build-essential

To build a static i2pd for raspberry pi you'll need to build an environment with all the i2pd dependencies. We'll use ubuntu's gcc arm cross compiler for this.

    #!bash
    $ sudo apt install g++-arm-linux-gnueabihf gcc-arm-linux-gnueabihf

We don't want to mix the libraries we are going to build with our system libraries as they are for ARM not x86 so we'll make a separate directory to hold them.

    #!bash
    $ export RPI="~/rpi"
    $ mkdir -p "$RPI/src"


Optionally you can have `$RPI` defined in `.bashrc` so you don't have to export it every time you want to build:

`$ echo 'export RPI="~/rpi"' >> ~/.bashrc`

Now on to building all the dependencies for i2pd (from source of course)

### Building Zlib

We'll start with the simplest dependency, `zlib`

Obtain and unpack zlib...

    #!bash
    $ cd $RPI/src
    $ wget http://zlib.net/zlib-1.2.8.tar.gz
    $ tar -xzf zlib-1.2.8.tar.gz

... then build and install.

    #!bash
    $ cd zlib-1.2.8
    $ CHOST=arm-linux-gnueabihf ./configure --prefix=$RPI --static
    $ make && make install

If all is well continue to the next step.

### Building libressl

For this static build I'll be using `libressl` instead of `openssl` for "security" reasons.

Grab the source...

    #!bash
    $ cd $RPI/src
    $ git clone https://github.com/libressl-portable/portable libressl
    $ cd libressl

... then build and install.

    #!bash
    $ ./autogen.sh
    $ ./configure --host=arm-linux-gnueabihf --prefix=$RPI
    $ make && make install

### Building Boost

Here's the dependency that has a little gotcha, `boost`.

Grab the source...

    #!bash
    $ cd $RPI/src
    $ wget https://sourceforge.net/projects/boost/files/boost/1.61.0/boost_1_61_0.tar.gz
    $ tar -xzf boost_1_61_0.tar.gz
    $ cd boost_1_61_0

Set up the build with just libraries we need...

    #!bash
    $ ./bootstrap.sh --prefix=$RPI --without-icu --without-libraries='python,mpi,log,wave,graph,math,context,coroutine,coroutine2,iostreams'

Now for the gotcha, you want to cross compile to arm so you're going to have to patch `project-config.jam`.

    #!bash
    $ sed 's/using\ gcc/using\ gcc\ \:\ arm\ \:\ arm-linux-gnueabihf-g\+\+/' < project-config.jam > project-config.jam.new
    $ mv project-config.jam.new project-config.jam

... now build and install, there may be errors but that's (probably) okay.

    #!bash
    $ ./b2 -toolset=arm install

### Building i2pd

Finally we have all the dependencies for i2pd built, now build the daemon itself.

Grab the source...

    #!bash
    $ cd $RPI/src
    $ git clone https://github.com/purplei2p/i2pd
    $ cd i2pd

... and compile

    #!bash
    $ make CXX=arm-linux-gnueabihf-g++ LIBDIR="$RPI/lib" USE_AESNI=no USE_STATIC=yes INCFLAGS="-I$RPI/include"

If all goes right you'll get a statically compiled i2pd that runs on the raspberry pi.

Optionally you can strip the debugging symbols from the static binary with `arm-linux-gnueabihf-strip i2pd`

Copy to your rpi, run it as a non root user and enjoy.

If any steps don't work please feel free to contact me on [twitter](https://twitter.com/ampernand) or via [email](mailto:ampernand@gmail.com)

----

Update:

My static builds for rpi can be found [here](/files/i2pd-rpi/)
