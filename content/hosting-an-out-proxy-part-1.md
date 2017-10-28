Date: 2017-10-28
Tags: i2p
Category: blog
Title: hosting an outproxy for i2p (part 1)
Authors: jeff

This quick blog was requested by someone on IRC and it details how to set up an outproxy on i2p.

If this is too quick a guide or you feel like you don't know what you're doing then I'd suggest against running an outproxy.

Software used:

* debian stable

* i2pd

* tinyproxy


The setup process goes as follows:

* install i2pd and tinyproxy

* edit tinyproxy.conf to have sane defaults

* have tinyproxy deny access to loopback

* create an i2p server tunnel pointing to 127.0.0.1:8888

* publish destination of outproxy


/etc/tinyproxy/tinyproxy.conf

    User tinyproxy
    Group tinyproxy
    Port 8888
    Listen 127.0.0.1
    Timeout 600
    DefaultErrorFile "/usr/share/tinyproxy/default.html"
    Logfile "/dev/null"
    LogLevel Warning
    PidFile "/run/tinyproxy/tinyproxy.pid"
    MinSpareServers 5
    MaxSpareServers 20
    StartServers 10
    MaxRequestsPerChild 0
    Allow 127.0.0.1/8
    ViaProxyName "tinyproxy"
    Filter "/etc/tinyproxy/filter"
    FilterExtended On
    ConnectPort 443
    

/etc/tinyproxy/filters

    ^127\.
    ^10\.

/etc/i2pd/i2pd.conf

    ntcp=false
    ssu=true
    notransit=true

/etc/i2pd/tunnels.conf

    [outproxy]
    type=server
    host=127.0.01
    port=8888
    keys=outproxy.dat
    signaturetype=7
    inbound.length=1
    outbound.length=1
