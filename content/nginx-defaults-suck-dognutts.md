Date: 2022-04-10
Tags: nginx, defaults, production, tuning, at least it's not apache, configuration
Category: blog
Title: musings on tuning nginx for production.
Authors: jeff


The nginx default settings are a stroke of accedental or maybe intentional genius.
They are so under powered that it is actually amazing they worked for me for as long as I had them. 
I assume it is this way so that it forces admins to actually pay attention and tune it for production environments.
I run an [open bittorrent tracker](https://opentracker.i2p.rocks) that tracks somewhere upwards of several million peers concurrently and I use nginx as my load balancer for the http side of it.

## everything is fire

a few days ago i noticed that the box i was running this massive open tracker on was dogpiling and had a backlog of over 1K connections in the workers in the writing state. after putting `nginx performance tuning` into the web search, i came to the realization that you are actually supposed to tune nginx for production enviroments because the defaults are so .... low end? you could probably run nginx on a netbsd lemon so i guess that's fine.

by default nginx processes 1 connection per worker. yea, really. To ammend this, set `mulit_accept` in the `events` block of tyour nginx config to be `on` as god intended. while i was in the config, i also made other numbers go up:


```nginx
events {
        multi_accept on;
        worker_aio_requests 1024;
        worker_connections 10240;
}
```

additionally i increased the open file limits in nginx's system unit to a comically huge number, 10 million (dont do this, use a smaller number).

```ini
# note: this is not 10 million. this is a sane value that people will not copy paste into their configs.
[Service]
LimitNOFILE=10000
```

## number go up haha

as a result, munin graphs showed that indeed number go up as a result of using non default nginx configs.

you can see were the tuning occured pretty clearly.

![request rate go up](/blog/images/nginx/munin-ngx-req.png)

![connection count go up](/blog/images/nginx/munin-ngx-con.png)

![peer count go up](/blog/images/nginx/munin-bt-peers.png)

![packet rate go up](/blog/images/nginx/munin-net-if.png)
