Date: 2016-07-29
Tags: i2p, git, tutorial
Category: blog
Title: self hosted git inside i2p


This is a quick howto guide on setting up a very minimal git repo for sharing code inside i2p using any modern linux distro. ([What is git?](https://git-scm.com/))

Please note this is not a general git tutorial, you will need to know a little git.

## Simple setup

Git proxy settings are easy, it's deep in the man pages but usually there's no need to set them it seems daunting.

For all this you'll need `ssh`, `git`, `connect-proxy` and `i2pd` (see [here](https://github.com/PurpleI2P/i2pd/releases) for i2pd)

For ubuntu xenial (root needed)
 
    #!bash
    wget https://github.com/PurpleI2P/i2pd/releases/download/2.8.0/i2pd_2.8.0-1xenial1_amd64.deb -O i2pd.deb
    dpkg -i i2pd.deb
    apt install ssh git connect-proxy

### Client side 

(The following should be run as your regular user)

Create a shell script for proxying over i2p, `127.0.0.1:4447` is i2pd's socks proxy, it's enabled by default.

    #!bash
    echo 'connect-proxy -S 127.0.0.1:4447 -R remote $*' > ~/i2p-socks-proxy
    chmod +x ~/i2p-socks-proxy

Set your proxy settings to use that script for i2p

    #!bash
    git config --global core.gitproxy ~/i2p-socks-proxy for i2p

### Cloning a repo

Try cloning a repo from `git.repo.i2p` (this uses `pull.git.repo.i2p`)

    #!bash
    git clone git://3so7htzxzz6h46qvjm3fbd735zl3lrblerlj2xxybhobublcv67q.b32.i2p/sha3.git

If all is well then you'll have a directory `sha3` with that git repo in it.

If you just want to clone repos you're done (yey) however, if you want to set up a full git setup complete with daemon continue reading.

## The Full Setup

Git is fully decentralized, anyone can host their own git repos and share them with others. Setting up a git daemon for the first time can feel daunting but don't worry, I'll go through every step.

### SSH Keys

Generate an ssh keypair on your development machine, this will be used for pushing to your repository securely...

    #!bash
    ssh-keygen -t ed25519

This creates 2 files, the private key (`~/.ssh/id_ed25519`) and the public key (`~/.ssh/id_ed25519.pub`).

*NEVER SHARE YOUR PRIVATE KEY.*

### Setting up the git daemon

(The following will require root)

We'll a user just for serving the git repo...

    #!bash
    adduser --system --disabled-password --home /srv/githome gitserv

Set up `.ssh` directory with correct permissions:

    mkdir -p /srv/githome/.ssh
    chown gitserv:gitserv /srv/githome/.ssh
    chmod 700 /srv/githome/.ssh/
    
Now append your ssh public key (`id_ed25519.pub`) to `/srv/githome/.ssh/authorized_keys`, This will allow you to login with your ssh keys you just generated.

Set up the git directory ...

    #!bash
    mkdir -p /srv/githome/git

Make sure permissions are okay ...

    #!bash
    chown gitserv:gitserv -R /srv/githome/git/
    chmod 700 /srv/githome/git/
    
Start the git daemon ...

    #!bash
    git daemon --base-path=/srv/githome/git --detach --export-all --user=gitserv --reuseaddr /srv/githome/git

So what does that `git daemon` command do? Let's break it down...

* `--base-path=/srv/githome/git` If you run git daemon with `--base-path=/srv/githome/git` on `example.com`, then if you later try to pull `git://example.com/hello.git`, git daemon will interpret the path as `/srv/githome/git/hello.git`.

* `--detach` Detach from the shell and log to syslog.

* `--export-all` Allow pulling from all directories that look like Git repositories even if they are not explicitly exported using the `git-daemon-export-ok` file

* `--user=gitserv` run as `gitserv` user.

* `--reuseaddr` Allows the server to restart without waiting for old connections to time out.

* `/srv/githome/git` The directory to serve in.


For autostarting `git-daemon` on boot, you can add that command to `/etc/rc.local` 

### Setting up i2pd

Add 2 entries to `/etc/i2pd/tunnels.conf` ...

    [git-daemon]
    type=server
    host=127.0.0.1
    port=9418
    keys=server-privkey.dat

    [ssh-daemon]
    type=server
    host=127.0.0.1
    port=22
    keys=server-privkey.dat

... and restart/reload i2pd

At the moment the easiest way i2p tunnel addresses can be found in the i2pd [webui](http://127.0.0.1:7070/?page=i2p_tunnels), the above config entries will share the same destination. In this example we'll just say that the address is `address.b32.i2p`, in reality it will be a lot longer.


### Repositories

(the following should be run as your regular user)

To push an initial git repo you'll need to ammend `~/.ssh/config` to use `~/i2p-socks-proxy` to connect.

Put the following in `~/.ssh/config` ...

    Host address.b32.i2p
    User gitserv
    IdentityFile ~/.ssh/id_ed25519
    ProxyCommand ~/i2p-socks-proxy address.b32.i2p 22

Make a test git repo, add a file to it and commit the initial git revision:

    #!bash
    mkdir test
    cd test
    git init .
    echo "test" > test.txt
    git commit -a -m'initial commit'

Add a git remote repo and push to it

    #!bash
    git remote add origin ssh://address.b32.i2p/git/test.git
    git push -u origin master

It will (probably) take a few moments for it to connect so be patient.

Others can reach that repo by cloning it ...

    #!bash
    git clone git://address.b32.i2p/test.git

... or by adding you as a remote repo.

    #!bash
    git remote add yourname-i2p git://address.b32.i2p/test.git
    git fetch yourname-i2p
    

## Follow Ups

If you spot an error in these instructions let me know on [twitter](https://twitter.com/ampernand) or via [email](mailto:ampernand+blog@gmail.com)



