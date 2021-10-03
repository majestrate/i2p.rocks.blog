Date: 2021-10-02
Tags: lokinet, exit, vpn, docker
Category: blog
Title: Hosting a Lokinet Exit - A Guide for the Lazy
Authors: jeff


This is a super abridged guide on setting up a lokinet exit node inside docker.

## prepare the host

docker using apt:

```
apt install docker docker-compose wget
```

get the files needed and set up the exit:

```
mkdir -p /usr/local/exit
cd /usr/local/exit
wget https://gist.github.com/majestrate/7f6933a0c72559537b1614a5e4db8c54/raw/207ca9d76e5af4a1f986e6f4690b5c546c18f493/docker-compose.yml
```

## turn it on

put the exit node up:

```
docker-compose up -d
```

now get the exit node's `.loki` address:

```
docker-compose exec lokinet print-lokinet-address.sh
```

## client usage

your exit node is now usable, you can turn it on on a lokient client using the `lokinet-vpn` command:

```
lokinet-vpn --up --exit putyourexitaddresshere
```
## updating
   
Ocassionally you'll want to update the docker images, you can do that using this command:

```
cd /usr/local/exit && docker-compose pull && docker-compose restart
```

## OH GOD OH FUCK OH GOD

your exit is ready, enjoy the packets.
