Date: 2017-03-21
Tags: i2p, monotone, tutorial
Category: blog
Title: I2P and Monotone, an intro guide for the lazy
Authors: Jeff

## Preface

[Monotone](https://www.monotone.ca/) is the version control software used by [Java I2P](https://geti2p.net/), [dn42](https://dn42.net/) and (probably) a few other projects.

> monotone is a free distributed version control system. It provides a simple, single-file transactional version store, with fully disconnected operation and an efficient peer-to-peer synchronization protocol.

Java I2P chose this initially because it was 2006 (aka git doesn't exist yet) and they needed to fast import a CVS dump to rescue their project. SVN suffered the same problem as CVS did, centralization. To this day Java I2P uses monotone internally inside I2P as revision control and it's a great match for I2P.

Advantages:

* Resumeable transactions (this is THE big one)
* Every commit is signed
* It's not Git

Monotone's `mtn push` and `mtn pull` are not atomic, they can resume if interrupted. This is a [YUUUGE]({static}/images/mtn/yuuuge.jpg) advantage over git as tcp/i2p connections break quite often, git would have to start from the very beginning if interrupted. While there are github mirrors of the source code, this is most likely the main reason why Java I2P continues to use monotone exclusively.

Monotone sounds great for I2P, right? Perhaps not, as with all things it's not without pitfalls.

Disadvantages:

* Slow merge and review functions
* It's rather Obscure, Higher barrier of entry for new contributors
* It's not Git

Most developers never heard of monotone, let alone know how to use it. This is a [YUUUGE]({static}/images/mtn/yuuuge.jpg) disadvantage for Java I2P. Most new contributors give up before submitting any code or patches because of monotone (myself included).

This is a guide to try and break that cycle.


## Monotone is EASY! :D

... if you have someone to hold your hand, this guide will try to do that a bit. Going forward I am going to assume you are familiar with the command line and a very basic understanding of git.

Let's install monotone, on a debian based system it's simple:

    # apt install monotone

Initialize the monotone database:

    $ mtn -d :default db init

This creates `~/.monotone` and populates `~/.monotone/databases/` with a file called `default.mtn`, a sqlite file.

Since this is an i2p monotone guide let's check some source code out from i2p's repos over i2p. Java I2P has a client tunnel set up for you that autostarts, very useful.

    $ mtn -d :default pull 'mtn://127.0.0.1:8998?i2p.www' -k ''

This pulls the `i2p.www` branch from java i2p's mtn server over i2p. This may take a bit. If you want to pull every branch do `mtn -d :default pull 'mtn://127.0.0.1:8998?*'`, which would take a few hours.

Now Let's check out that branch into a workspace., i first like to create a `~/mtn/` directory for all my monotone workspaces

    $ mkdir ~/mtn/
    $ cd ~/mtn/
    $ mtn -d :default co --branch i2p.www

You'll get a subdirectory at `~/mtn/i2p.www/` that conatins the files for the `i2p.www` branch.

HOLD ON THIS IS CONFUSING `D:`

No problem. Let's define some terms:

* Branch - analogous to a git repository (the `.git` directory) but with only 1 git branch
* Database - analogous to a git hosting solution like github, it contains every `Branch` you know of
* Workspace - where you check out a `Branch` and work on the files
* Revision - analogous to a git commit object
* Certificate - a signature of a `Revision`

What you just did is:

* install monotone
* create a new monotone database
* pull the `i2p.www` branch over i2p
* check out the `i2p.www` branch in to a workspace at `~/mtn/i2p.www/`


To commit things to monotone you'll need to generate a monotone signing key:

    $ mtn keygen your@email.tld

you are required to password protect the key file, you'll get a prompt:

    enter passphrase for key ID [your@email.tld] (...):

... and a confirmation:

    confirm passphrase for key ID [your@email.tld] (...):

... followed by:

    mtn: generating key-pair 'your@email.tld'
    mtn: storing key-pair your@email.tld in '/home/jeff/.monotone/keys/'
    mtn: storing public key your@email.tld in ''
    mtn: key 'your@email.tld' has hash 'ad1b8dfb3643e801e4cb2b16446261527e477e27'


The private keys are stored in `~/.monotone/keys/` make sure to back them up!

To print out your public key you can do `mtn pubkey your@email.tld` to do that.

Okay, let's try commiting a fix to the website, let's say we added a file called `TEST.txt` , we need to add it to the project.

    $ cd ~/mtn/i2p.www/
    $ echo "test" > test.txt
    $ mtn add test.txt

once you are ready commit the changes to the database as a new branch, using your new signing key:

    $ mtn -d :default ci -b i2p.www.yourname -k your@email.tld

obviously replace `yourname` with the name you want to be known as, this is a convention.

now let's remove that file...

    $ mtn rm test.txt

... and commit that change

    $ mtn -d :default ci -b i2p.www.yourname -k your@email.tld

Now let's do something applied, we'll get the java i2p source code from monotone...

    $ cd ~/mtn/
    $ mtn -d :default pull `mtn://127.0.0.1:8998?i2p.i2p` -k ''
    $ mtn -d :default co --branch i2p.i2p

... and build an `update.zip` to upgrade you install to an experimental build, make sure you have `ant` installed, if you don't `apt install ant`.

    $ cd ~/mtn/i2p.i2p/
    $ ant updater

If the build works then you'll have an `update.zip` at `~/mtn/i2p.i2p/update.zip`. You can try out experimental your build, copy it to `~/.i2p/` and gracefully restart the i2p router. This is only recommended for people that want to help find and report bugs.

If all went well, you just compiled the bleeding edge java i2p from source code, anonymously. YAY.


## Monotone is HARD! D:

If you want to start contributing code, this is where the hard part happens. Usually the process for new developers is:

* generate a `commit` key and a `transport` key
* get on irc2p
* sign the new developer contract
* get your `commit` key added to the developer list
* get your `transport` key whitelisted to the i2p mtn server

Most people quit half way through, but there is a faster way: run your own monotone server.

If you feel like having a fun and painful adventure, check out the monotone manual, `man mtn`.

For more info on contributing, check out the [new developers guide](https://geti2p.net/en/get-involved/guides/new-developers) on the Java I2P website.
