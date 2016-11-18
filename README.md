# i2p.rocks blog repo #

## building ##

### dependancies ###

* git
* pelican
* python 3.x (required by pelican)

### setting up ###

    git clone https://github.com/majestrate/i2p.rocks.blog
    cd i2p.rocks.blog
    make clean

#### tools for ipfs publishing ####

	https://github.com/ipfs/go-ips
	https://github.com/whyrusleeping/ipfs-key
	https://github.com/whyrusleeping/ipns-pub
	

### deploying ###

    make publish ssh_upload ipfs

