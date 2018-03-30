Date: 2018-03-30
Tags: xmpp, i2p, i2pd, decentralization, p2p, privacy
Category: blog
Title: New life for XMPP. Build your own decentralized messenger!
Authors: Darknet Villain

![img]({filename}/images/decentralized-messenger-xmpp/xmpp-1.jpeg)

The idea of building decentralized messenger run by users, not corporations, is not new. But the process of building it costs a lot of money and takes a lot of time. But what if we take the old good [XMPP protocol](https://en.wikipedia.org/wiki/XMPP), which has everything already implemented for us?

That's not "real P2P", you may argue, for using XMPP one needs to have a server running with a registered domain name. Yes, but we can run our server software on a local host and use [virtual I2P network](https://en.wikipedia.org/wiki/I2P) for connecting with other servers. I2P (Invisible Internet Protocol) allows us to use virtual .i2p address instead of a real domain name, plus it gives us advanced protection against [illegal dragnet surveillance](https://en.wikipedia.org/wiki/PRISM_%28surveillance_program%29). 

That way we have:

- Hybrid P2P messenger, which can be run both on end-user devices and on high-performance server infrastructure.
- Features which many of "real P2P" messengers miss: offline message delivery, "cloud storage" for history and contacts, using one account on multiple devices.
- All kinds of end-user applications are available (desktop, mobile, web).
- Censorship resistance and advanced privacy protection as a bonus from using I2P.

Let's get it!

# Installing I2P client and creating a server I2P tunnel

In this guide we are going to use lightweight I2P client called [i2pd](https://github.com/PurpleI2P/i2pd). Look at [official documentation](https://i2pd.readthedocs.io/en/latest/user-guide/install/) for detailed instructions on how to install it.

After installation is completed, create a server I2P tunnel. It will provide us a virtual .i2p address with which our XMPP server will be available to the world. Write the following lines in [tunnels.conf](https://i2pd.readthedocs.io/en/latest/user-guide/tunnels/) file:

    [prosody-s2s]
    type=server
    host=127.0.0.1
    port=5269
    inport=5269
    keys=prosody.dat

    [prosody-c2s]
    type=server
    host=127.0.0.1
    port=5222
    inport=5222
    keys=prosody.dat

If you plan to use messenger only on a local host, prosody-c2s section may be omitted. Restart i2pd to apply new settings and look at webconsole http://127.0.0.1:7070/ page `I2P tunnels` for a new I2P address:

![img]({filename}/images/decentralized-messenger-xmpp/xmpp-2.png)

Save this xxx.b32.i2p address, it will be a domain name of your XMPP server.

# Installing and configuring XMPP server

We will use [prosody](https://prosody.im/) XMPP server, it is the most lightweight and has ready to use module for I2P. Installation instructions are available at [official documentation](https://prosody.im/download/start), in Debian/Ubutntu just run `apt install prosody`.

bit32 library for lua is required for `mod_darknet` module. If your lua version is less than 5.2 (most likely), run `apt install lua-bit32`.

Install [mod_darknet](https://github.com/majestrate/mod_darknet) module. It is required so that prosody could make outgoing connections with I2P Socks5 proxy. Download [this file](https://raw.githubusercontent.com/majestrate/mod_darknet/master/mod_darknet.lua) to prosody modules directory, usually it is `/usr/lib/prosody/modules`.

Edit config file `/etc/prosody/prosody.cfg.lua`. Replace xxx.b32.i2p with your address:

    interfaces = { "127.0.0.1" };
    admins = { "admin@xxx.b32.i2p" };
    modules_enabled = {
        "roster"; "saslauth"; "tls"; "dialback"; "disco"; "posix"; "private"; "vcard"; "register"; "admin_adhoc"; "darknet"; 
    };
    modules_disabled = {};
    allow_registration = false;
    darknet_only = true;
    c2s_require_encryption = true;
    s2s_secure_auth = false;
    authentication = "internal_plain";

    -- On Debian/Ubuntu
    daemonize = true;
    pidfile = "/var/run/prosody/prosody.pid";
    log = {
        error = "/var/log/prosody/prosody.err";
        "*syslog";
    }
    certificates = "certs";

    VirtualHost "xxx.b32.i2p";
    ssl = {
        key = "/etc/prosody/certs/xxx.b32.i2p.key";
        certificate = "/etc/prosody/certs/xxx.b32.i2p.crt";
    }
 
The last step is certificates generation. Run the following:

    openssl genrsa -out /etc/prosody/certs/xxx.b32.i2p.key 2048
    openssl req -new -x509 -key /etc/prosody/certs/xxx.b32.i2p.key -out /etc/prosody/certs/xxx.b32.i2p.crt -days 3650
    chown root:prosody /etc/prosody/certs/*.b32.i2p.{key,crt}
    chmod 640 /etc/prosody/certs/*.b32.i2p.{key,crt}

Restart prosody to apply new settings.

# Creating accounts and connecting clients

Adding admin account:

    prosodyctl adduser admin@xxx.b32.i2p

Now configure your XMPP client (for example, [Pidgin](https://pidgin.im)). 

![img]({filename}/images/decentralized-messenger-xmpp/xmpp-3.png)

If you are connecting to a localhost, specify custom server address 127.0.0.1 port 5222.

![img]({filename}/images/decentralized-messenger-xmpp/xmpp-4.png)

If you are connecting to a server remotely via I2P, specify a Socks5 proxy server 127.0.0.1:4447. 

![img]({filename}/images/decentralized-messenger-xmpp/xmpp-5.png)

If everything is configured correctly, you will be able add other users of I2P federation to your contacts and chat with them. 

To test your setup, add `hello@xmppoeiqpbeelicgkoim3ibegjonbqwh7vv7d6nsju73tjjmujpq.b32.i2p` to your contacts and send it "hello".

# (Advanced) Clearnet-to-I2P federation

It is also possible to configure your existing "clearnet" XMPP server to join I2P federation and chat with darknet users. For that, create a tunnel as described above. Each user that wishes to communicate with your server will have to add custom mapping to their prosody config file. That is how my server is configured to communicate with `i2p.rocks` server:

    darknet_map = {
        ["i2p.rocks"] = "ynkz7ebfkllljitiodcq52pa7fgqziomz4wa7tv4qiqldghpx4uq.b32.i2p";
        ["muc.i2p.rocks"] = "ynkz7ebfkllljitiodcq52pa7fgqziomz4wa7tv4qiqldghpx4uq.b32.i2p";
    }
 
If you have any questions, you may ask them at our XMPP conference `federation@muc.i2p.rocks`. Happy chatting! 
