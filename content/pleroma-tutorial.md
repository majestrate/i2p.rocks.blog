Date: 2018-03-11
Tags: pleroma
Category: blog
Title: The magical world of Pleroma, setting up your instance.
Authors: jeff

This little blog post will guide a user through installing pleroma on a "$3 instance" as suggested by lain.

First, what is pleroma?

Pleroma is an OStatus and ActivityPub compatable server, a component of the [fediverse](https://robek.world/featured/what-is-gnu-social-and-is-mastodon-social-a-twitter-clone/) of which GNU Social and Mastodon belong to as well. Think if twitter was structued how email is. With Email you have many different servers, yahoo mail, gmail, aol, (etc) that all can send mail to each other but are owned by different entities, the thing they have in common is they all speak SMTP. OStatus and AcitivityPub are each the "Twitter of SMTP", tweets/toots/shitposts/japanese-moonrunes are exchanged between servers. Many users can be on 1 server, (in fact mastodon.social and pawoo.net have a large chunk of the users) or 1 user can run their own server just for them (which is what I do, sorta).

This guide may be outdated but the [pleroma wiki](https://git.pleroma.social/pleroma/pleroma/wikis/Installing%20on%20Debian%20based%20distributions) should always be up to date.

Things you'll need before getting started:

* ssh client
* a domain name

For this setup we're going to use Debian Stretch (as of writing it's debian stable) on digitial ocean.

I chose DigitalOcean because they have absolutely fantastic documentation.

Required things to do before hand:

* [Spin up a VPS](https://www.digitalocean.com/community/tutorials/how-to-create-your-first-digitalocean-droplet)
* [Generate an ssh key](https://www.digitalocean.com/community/tutorials/how-to-use-ssh-keys-with-putty-on-digitalocean-droplets-windows-users)
* Add a DNS A Record with the IP Address of your droplet.
* Make sure that your domain resolves to the ip address of your droplet, hint: use `ping -c 1 your-domain.tld` to test.


Some VERY IMPORTANT notes:

* Lines that start with `%` mean that they should be executed as root user
* Lines that start with `$` mean that they should NOT be executed as root user
* don't include `%` or `$` in the command itself.

Once that's all set up, log into the droplet as root.

Get the build dependancies:

    :::bash
    % apt-get install build-essential git wget postgresql nginx certbot sudo
    
install elixir, the one in debian stretch is too old:

    :::bash
    % wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb
    % dpkg -i erlang-solutions_1.0_all.deb
    % apt-get update
    % apt-get install --no-install-recommends elixir esl-erlang
   

Add a new user called pleroma:

    :::bash
    % useradd pleroma
    % mkdir /home/pleroma && chown pleroma:pleroma /home/pleroma
    
Switch to that user:

    :::bash
    % su - pleroma
    
Now that you're the pleroma user, clone the pleroma source code:

    :::bash
    $ git clone https://git.pleroma.social/pleroma/pleroma ~/pleroma
    
now move into the code's directory:

    :::bash
    $ cd ~/pleroma
    
The following is from the [pleroma readme](https://git.pleroma.social/pleroma/pleroma/blob/develop/README.md)

Get the dependancies for elixir:

    :::bash
    $ mix deps.get

Generate a config, this will ask a few questions:

    :::bash
    $ mix generate_config

Copy the generated config in place:

    :::bash
    $ cp config/generated_config.exs config/prod.secret.exs
    
Drop back down to root:

    :::bash
    $ exit

Then set up postgres:

    :::bash
    % chmod +x /home/pleroma/pleroma/config/setup_db.psql
    % su - postgres -c "psql -f /home/pleroma/pleroma/config/setup_db.psql"

Log back into the pleroma user...

    :::bash
    % su - pleroma
    
go into the pleroma directory:

    :::bash
    $ cd ~/pleroma
    
and run the database migrations, every time you upgrade the software make sure you run the migrations.

    :::bash
    $ MIX_ENV=prod mix ecto.migrate
    
Check to see if the configs work, run the server in the foreground:

    :::bash
    $ MIX_ENV=prod mix phx.server
    
The server runs on port 4000, you can check to see if it works by going to http://your-doman.tld:4000/api/v1/instance

Once that works, interrupt the server with control-c ( `^c` )

quit back to root...

    :::bash    
    $ quit

... so you can install the init scripts:

    :::bash
    % cp /home/pleroma/pleroma/installation/pleroma.service /etc/systemd/system/ 


make sure pleroma.service has in the service section the following entries,
specifically the two Environmental variables:

    :::bash
    [Service]
    User=pleroma
    WorkingDirectory=/home/pleroma/pleroma
    Environment="HOME=/home/pleroma"
    Environment="MIX_ENV=prod"
    ExecStart=/usr/local/bin/mix phx.server
    ExecReload=/bin/kill $MAINPID
    KillMode=process
    Restart=on-failure


enable and start pleroma:

    :::bash
    % systemctl enable pleroma --now

    :::bash
    % cp /home/pleroma/pleroma/installation/pleroma.nginx /etc/nginx/sites-enabled/

edit the `/etc/nginx/sites-enabled/pleroma.nginx` file, replace `example.tld` with your domain.

The config should look similar to this:

    :::bash
    proxy_cache_path /tmp/pleroma-media-cache levels=1:2 keys_zone=pleroma_media_cache:10m max_size=10g
                 inactive=720m use_temp_path=off;

    server {
       listen         80;
       server_name    yourdomain.tld;
       
       location / {
         return         301 https://$server_name$request_uri;
       }
       
       location ^~ /.well-known/acme-challenge/ {
          allow all;
          root /var/lib/letsencrypt/;
          default_type "text/plain";
          try_files $uri =404;
       }
    }

    server {
        listen 443;
        ssl on;
        ssl_session_timeout 5m;

        ssl_certificate           /etc/letsencrypt/live/yourdomain.tld/fullchain.pem;
        ssl_certificate_key       /etc/letsencrypt/live/yourdomain.tld/privkey.pem;

        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_ciphers "HIGH:!aNULL:!MD5 or HIGH:!aNULL:!MD5:!3DES";
        ssl_prefer_server_ciphers on;
 
        server_name yourdomain.tld;

        location / {
          add_header 'Access-Control-Allow-Origin' '*';
          proxy_http_version 1.1;
          proxy_set_header Upgrade $http_upgrade;
          proxy_set_header Connection "upgrade";
          proxy_set_header Host $http_host;
          proxy_pass http://localhost:4000$request_uri;
        }

        location /proxy {
          proxy_cache pleroma_media_cache;
          proxy_cache_lock on;
          proxy_pass http://localhost:4000$request_uri;
        }

        location /.well-known/ {
            proxy_set_header Host $http_host;
            proxy_pass http://localhost:4000$request_uri;
        }
    
        location ^~ /.well-known/acme-challenge/ {
          allow all;
          root /var/lib/letsencrypt/;
          default_type "text/plain";
          try_files $uri =404;
        }
      }
      
reload nginx and set up ssl with certbot

    :::bash
    % systemctl reload nginx
    % mkdir -p /var/lib/letsencrypt/.well-known
    % certbot certonly --email your@emailaddress --webroot -w /var/lib/letsencrypt/ -d yourdomain

make sure to change "yourdomain" to be the domain you are using and "your@emailaddress" to an email address you check.

reload nginx once more

    :::bash
    % systemctl reload nginx
    
Then go to https://yourdoman.tld/ to verify that it works.

That completes the howto setup guide.

If you have any problems setting up please join the dev chat for assistance and feel free to ask questions.

* [matrix](https://matrix.heldscal.la/#/room/#freenode_#pleroma:matrix.org)

* `#pleroma` on freenode irc network

On freenode I go by the handle `__uguu__` , don't ask to ask, just ask and someone will get to you (eventually) `:^)`

    
   
