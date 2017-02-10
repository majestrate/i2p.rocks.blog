Date: 2017-02-10
Tags: i2p, i2pd, Ubuntu, Debian, AppArmor, Security, Hardending
Category: blog
Title: Hardending i2pd setup with AppArmor
Authors: Darknet Villain

Quoting Wikipedia:

> AppArmor ("Application") is a Linux kernel security module that allows the system administrator to restrict programs' capabilities with per-program profiles. Profiles can allow capabilities like network access, raw socket access, and the permission to read, write, or execute files on matching paths. AppArmor supplements the traditional Unix discretionary access control (DAC) model by providing mandatory access control (MAC). It was included in the mainline Linux kernel since version 2.6.36 and its development has been supported by Canonical since 2009.

It is a great tool to hardend security for any of your applications on Linux, 
including [Invisible Internet router](http://i2pd.website).

Now we have added [i2pd profile for AppArmor](https://raw.githubusercontent.com/PurpleI2P/i2pd/openssl/contrib/apparmor/usr.sbin.i2pd) 
which you can just throw into your profiles directory and it will just work.

Instruction
-----------

First, make sure you have AppArmor installed and working. Run the following:

    sudo apparmor_status

If you have AppArmor, it should output ``apparmor module is loaded.`` and list available rules.

If not, follow instructions for how to setup AppArmor: 
[Ubuntu](https://help.ubuntu.com/community/AppArmor) (should be installed by default), 
[Debian](https://wiki.debian.org/AppArmor/HowToUse),
[Arch Linux](https://wiki.archlinux.org/index.php/AppArmor),
[Gentoo](https://wiki.gentoo.org/wiki/AppArmor).

After you have installed and enabled AppArmor, download and copy profile into your profiles directory. In Debian/Ubuntu:

    wget -O usr.sbin.i2pd https://raw.githubusercontent.com/PurpleI2P/i2pd/openssl/contrib/apparmor/usr.sbin.i2pd && sudo cp usr.sbin.i2pd /etc/apparmor.d/

Finally, enable it:

    sudo aa-enforce /usr/sbin/i2pd

Now, every behavior which is not allowed by the profile will be restricted and such event will be logged to syslog.
You may want to periodically inspect logged events with the following command:

    sudo aa-logprof

Generally, it should not show anything (which is good).

Notes
-----

Our profile is designed for Debian/Ubuntu i2pd packages and was tested with basic i2pd behavior.
You may want to customize it according to your specific situation.

Contributions are welcome at [GitHub](https://github.com/PurpleI2P/i2pd).

AppArmor resources: [AppArmor Wiki](http://wiki.apparmor.net/), [Ubuntu Wiki about AppArmor](https://wiki.ubuntu.com/AppArmor). 
