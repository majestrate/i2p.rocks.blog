Date: 2016-10-14
Tags: i2p, i2pd, xmpp, IM, OTR
Category: blog
Title: Anonymous instant messaging with end-to-end encryption
Authors: Invisible Villain


Centralized commercial IM providers are a real threat to our privacy. They often require users to run proprietary software, confirm their identity with SMS and give away control over their data.

We always have a freedom to take control back over our private communications.

In this tutorial, we will use XMPP as decentralized and open-source instant messaging system, OTR for end-to-end encryption and I2P network to anonymize our network activities.


Install i2pd
------------

I2P (Invisible Internet Protocol) is a universal anonymous network layer. All communications over I2P are anonymous and end-to-end encrypted, participants don't reveal their real IP addresses.

If you don't have I2P client already, go to [i2pd.website](http://i2pd.website), install and run it.



Install XMPP client
-------------------

Make sure your client supports [OTR encryption](http://wiki.xmpp.org/web/OTR). In this tutorial we will use psi+. 

Windows users can find downloads [here](https://sourceforge.net/projects/psiplus/files/). 

In Debian/Ubuntu, run following commands:

    sudo apt-get install psi-plus psi-plus-plugins

Psi+ will ask you to setup an account at the first run, just press cancel.



Configure XMPP client
---------------------

**Add I2P Socks5 proxy**

![Image]({static}/images/xmpp-tut/socks-config.png)

Options -&gt; Application -&gt; Proxy settings -&gt; press Edit -&gt; press New -&gt; create proxy "I2P socks", type Socks version 5, Host: 127.0.0.1, port: 4447 -&gt; press Save



**Improving privacy**

![Image]({static}/images/xmpp-tut/client-switch.png)

Options -&gt; Plugins -&gt; select "Client switcher plugin" in dropdown menu -&gt; check "Load this plugin" -&gt; check "For all accounts" -&gt; choose Response mode: not implemented -&gt; check "Deny iq time request" 



Register an account
-------------------

![Image]({static}/images/xmpp-tut/reg1.png)

Account setup -&gt; Add -&gt; Enter your desired account name, check "Register new account" and press Add

![Image]({static}/images/xmpp-tut/reg2.png)

Fill Server: i2p.rocks -&gt; check "Manually specify Server Host/Port", then fill Host: ynkz7ebfkllljitiodcq52pa7fgqziomz4wa7tv4qiqldghpx4uq.b32.i2p, Port: 5222, select Proxy "I2P Socks". Press Next

![Image]({static}/images/xmpp-tut/reg3.png)

Enter your username and long random password. Press Next.

![Image]({static}/images/xmpp-tut/config-account.png)

Open Account Properties, Misc and set your resourse name "Manual" and enter some random string, like "null". Set STUN/TURN to "don't use".

You have successfully registered and set up your account.



Create OTR private key
----------------------

![Image]({static}/images/xmpp-tut/otr-generate.png)

Options -&gt; Plugins -&gt; select "Off-the-Record Messaging Plugin" -&gt; check "Load this plugin" -&gt; "My private keys" tab -&gt; select your account and press "Generate new key".



Using OTR encryption
--------------------

![Image]({static}/images/xmpp-tut/verify-fingerprints.png)

![Image]({static}/images/xmpp-tut/finally-secure.png)

Later on, you will add new contacts and authenticate them with fingerprint verification. OTR button is a little lock in chat window, just above text input field.



About i2p.rocks
---------------

i2p.rocks server is connected with all other XMPP servers in the Internet. It supports both I2P and Tor darknets for anonymous access.

Invite your friends and chat with REAL privacy!
