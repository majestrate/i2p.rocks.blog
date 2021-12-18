Date: 2021-10-02
Tags: lokinet, exit, vpn, docker
Category: blog
Title: Hosting a Lokinet Exit - A Guide for the Lazy
Authors: jeff


This is a super abridged guide on setting up a lokinet exit node inside docker.

## prepare the host

docker using apt:

```sg
$ sudo apt install docker docker-compose wget
```

grab the `docker-compose.yml`

```sh
$ mkdir -p /usr/local/exit/
$ wget https://github.com/oxen-io/oxen-docker/raw/main/lokinet/docker-compose.yml -O /usr/local/exit/docker-compose.yml
```

## turn it on

put the exit node up:

```sh
$ cd /usr/local/exit && docker-compose up -d
```

now get the exit node's `.loki` address:

```sh
$ cd /usr/local/exit && docker-compose exec lokinet print-lokinet-address.sh
```

## client usage

your exit node is now usable, you can turn it on on a lokient client using the `lokinet-vpn` command:

```sh
$ lokinet-vpn --up --exit putyourexitaddresshere
```
## updating
   
Ocassionally you'll want to update the docker images, you can do that using this command:

```sh
$ cd /usr/local/exit && docker-compose pull && docker-compose restart
```

## OH GOD OH FUCK OH GOD

your exit is ready, enjoy the packets.
