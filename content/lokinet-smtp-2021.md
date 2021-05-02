Date: 2021-05-02
Tags: smtp, mx, lokinet, email, anonymous email
Category: blog
Title: Opportunistic SMTP over Lokinet: it could work...
Authors: jeff

STMP, isn't. 
It has a lot of auxillery stuff and it's a nightmare to run a mail exchange.
That being said, 
the excessive flexibility of the protocol stack can be a good thing if you know how to use it.

Given you use a postfix + opendkim setup I have devised a super neato near turnkey way to exchange email between 
mail exchanegs over lokinet while still coexisting with non lokinet mail exchanges. 

To do all this install lokinet, 
persist the snapp keys in `/var/lib/lokinet/lokinet.ini` in the `[network]` section `keyfile=/var/lib/lokinet/hs.private`,
then restart lokinet to apply settings. To get your `.loki` address do a `dig @127.3.2.1 -t cname localhost.loki` (after restart of course)

The changes needed for the mail exchange side is actually really simple.
My dns configs (bind9 style) for my mail exchange are now effectively this:

    IN  MX  10 gha9cxqjzrbcu5dxnx7riomnitm94gkzxcghdmb1nogd5f9oj7oy.loki.
	IN	MX	20 mail.i2p.rocks.
    mail	IN	TXT	( "v=spf1 mx a:mail.i2p.rocks a:gha9cxqjzrbcu5dxnx7riomnitm94gkzxcghdmb1nogd5f9oj7oy.loki -all" )
    mail	IN	A	51.81.46.170

What this means is that all mail exchanges will try resolving the `.loki` address first (and obviously fail) then fall back to the
internet based one. In addition I updated my SPF record to include my `.loki` address.

In addition i added the `.loki` tld to `/etc/opendkim/TrustedHosts` as the network layer is not spoofable (and we do not have txt records in lokinet yet `;_;`).

This setup is entirely untested. 

If someone wants to set up such a setup on their mail exchange, 
please do so and send me an email to `[jeff at i2p <[dot]> rocks]`.

If this experiment works it'll be pretty cool and as you can see it's far far more turnkey than [onionmx](https://github.com/ehloonion/onionmx) which is a very cool project 
but a massive pain the balls to deploy. My hope is that this will provide some more visibility to the network utility that lokinet provides.
