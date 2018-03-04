Date: 2018-03-05
Tags: sbuild schroot build raspberrypi rpi raspbian environment
Category: blog
Title: Building sbuild environment for cross-building raspbian packages on amd64/i386 machines
Authors: R4SAS

Used documents and topics:
* https://wiki.debian.org/mk-sbuild
* https://log.cyconet.org/2013/11/25/crossbuilding-debian-packages-with-sbuild-for-raspbian/
* https://gist.github.com/waja/7639011

#### Install requirements, set distribution to install

    apt-get install gnupg dirmngr curl sbuild ubuntu-dev-tools qemu-user-static binfmt-support
    export RELEASE="stretch"

Recommended to work under user with full `sudo` access without password prompting.

(needed to install packages and mount chroot, requrement by mk-sbuild)

You can ignore second line if want every time write password when it asked.

    useradd -m -s /bin/bash -G sudo,sbuild builder
    echo "builder ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
    su - builder

#### Creating keyring for raspbian archive used by debootstrap

    curl -sL http://archive.raspbian.org/raspbian.public.key | gpg --import -
    gpg --export 9165938D90FDDD2E > $HOME/raspbian-archive-keyring.gpg

#### Write sources file

    cat > $HOME/rpi.sources <<EOF
    deb http://archive.raspbian.org/raspbian/ RELEASE main contrib non-free rpi
    deb-src http://archive.raspbian.org/raspbian/ RELEASE main contrib non-free rpi
    EOF

#### Set-up mk-sbuild

    cat > $HOME/.mk-sbuild.rc <<EOF
    SOURCE_CHROOTS_DIR="$HOME/chroots"
    DEBOOTSTRAP_KEYRING="$HOME/raspbian-archive-keyring.gpg"
    TEMPLATE_SOURCES="$HOME/rpi.sources"
    SKIP_UPDATES="1"
    SKIP_PROPOSED="1"
    SKIP_SECURITY="1"
    EATMYDATA="1"
    EOF

#### Create chroot and configure

    mk-sbuild --name $RELEASE-rpi --arch=armhf --debootstrap-mirror=http://archive.raspbian.org/raspbian/ $RELEASE

#### Build package

    sbuild --arch=armhf -c $RELEASE-rpi-armhf -d $RELEASE <package>_<version>.dsc

or later you can use it without defining $RELEASE

    sbuild --arch=armhf -c stretch-rpi-armhf -d stretch <package>_<version>.dsc
