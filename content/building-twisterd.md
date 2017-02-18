Date: 2017-02-18
Tags: twister
Category: blog
Title: Twister the little known p2p twitter
Authors: Jeff

Twister is a little known p2p twitter alternative that uses blockchain and bittorrent technology. Not very many people use twister which is discouraging but the technology powering it is nevertheless genius. Please note that twister is not anonymous by default, I'll cover how to set up twister to run over tor in a future blog maybe.

This blog will be a quick tutorial on building and setting up twister on debian stable.

## Building from source and configuring

Right now the most straight forward way of getting the most up to date version of twister is to build from source, there are some Ubuntu PPAs but those leave a bad taste in my mouth and tend to break installs on occasion.

Building from source can be daunting especially for newbies, this will simplify the process as much as possible.

For those unfamiliar with terminal conventions, any line prefixed with `#` means that the user should run the following command as root, not including the `#`. Conversely, lines prefixed with `$` instructs to run the following command as regular user, again not including the `$`.

Let's begin.

First, install the build dependencies: (if you skip ahead you can see that this is the only command that requires root)

    # apt install libboost-all-dev libdb++-dev build-essential libssl-dev autoconf automake

Clone the core repo:

    $ git clone https://github.com/miguelfreitas/twister-core
    $ cd twister-core

Build the core daemon:

    $ ./bootstrap.sh
    $ make

Install the core daemon:

    # make install

Set up configs for core:

    $ mkdir ~/.twister/ -p
    $ echo 'rpcuser=user' >> ~/.twister/twister.conf
    $ echo 'rpcpassword=pass' >> ~/.twister/twister.conf
    $ echo 'rcpallowip=127.0.0.1' >> ~/.twister/twister.conf

This sets the username and password for the web ui to `user:pass`, you should replace these for security reasons.

Twister separates core daemon and web ui into 2 repositories so now we clone the web ui repo into the config folder:

    $ git clone https://github.com/miguelfreitas/twister-html/ ~/.twister/html

## Bootstrapping

Right now twister's blockchain is about 51MB large which is microscopic compared to every other blockchain out there that I know of. This is because only user registration is done via blockchain, all posts and metadata are exchanged via a variant of Bittorrent's DHT. The DHT does not use mainline bittorrent as twister has custom DHT extensions that would most likely screw with non-twister nodes but I digress.

## Running

Now let's start twister and have it fork into the background:

    $ twisterd -daemon

The web ui will be located at `http://127.0.0.1:28332/` . You'll need to register a new username, right now many names are squatted so be creative. After registering a user you'll have to wait a few minutes to get onto the blockchain, mining blocks may help speed up the process. The edit profile page at `http://127.0.0.1:28332/profile-edit.html` will be enabled once your user is accepted into the blockchain you can start posting, enjoy.
