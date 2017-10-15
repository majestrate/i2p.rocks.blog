Date: 2017-10-06
Title: Syncthing over I2P
Category: blog
Tags: i2p
Authors: Chris Barry

In which I show you how to use Syncthing over I2P for secure, self-hosted, file synchronization.

## What is Syncthing?

Syncthing is an open source, self-hosted file synchronization tool.
Instead of trusting a third party (e.g. Dropbox) to host your files, and synchronize files between your machines, you can use an open source alternative.

By default, syncthing is not truly decentralized, and relies on [third party relay servers][syncthing-relay] and [discovery servers][syncthing-discovery].
While I am sure the syncthing protocol is safe enough, and the people hosting these services have good intentions, wouldn't it be nice if we don't have to trust either?

[syncthing-relay]: https://docs.syncthing.net/users/relaying.html
[syncthing-discovery]: https://docs.syncthing.net/users/stdiscosrv.html

## What is I2P?

[I2P][i2p] is a decentralized, peer to peer, anonymous network layer.
By relaying your computer traffic by a volunteer ran network spread around the world, following the path of traffic becomes nearly impossible.

I2P has the added benefit that you can bypass limitations on hosting imposed by ISPs.
Since I2P hidden services only exist in I2P, there is no port forwarding required!

[i2p]: https://geti2p.net

## How

I wrote this assuming you're using the Java implementation of I2P.
However, I am sure this could work with [Kovri][kovri] or [i2pd][i2pd].

1. Install and set up Syncthing on all of the computers you want to sync.
2. Install and Set up I2P on all the computers you want to sync.
3. On each of the computers, you'll want to create two I2P Tunnels (if you're familar with I2P please note that you can lower the number of hops to make the connection quicker, but you do lose some privacy):
	- Server: Standard
		- Name: Syncthing
		- Check off "Auto Start Tunnel"
		- Target Port: 22000
		- When you start the tunnel, take note of the address the tunnel receives (it will be a b32 address)
	- Client: SOCKS 4/4a/5 proxy
		- Name: Socks
		- Check off "Auto Start Tunnel"
		- Access Port: 4446
4. Now you will have two I2P addresses, let's say a.i2p and b.i2p
5. In the Syncthing admin panel, you will want to configure two new Remote Devices.
   You will want to make sure that the syncthing IDs are configured properly, and that each Remote Device points to the other (a.i2p uses b.i2p and vice versa).
   Make sure remove "default" as the address and make it `tcp://a.i2p` - depending on the device you're on this will change.
6. Now let's disable some Syncthing features in the Syncthing GUI.
   These aren't mandatory to disable, but they will ensure you're off of all Syncthing infrastructure.
   Go to Actions -> Settings, and make sure the following are disabled:
    - Enable NAT traversal
    - Local Discovery
    - Global Discovery
    - Enable Relaying
	- Anonymous Usage Reporting (since everything is proxied thru I2P it won't be submitted)
7. There are currently no GUI parmaters to configure proxy settings in Syncthing - so you will have to use the following command to start Syncthing.
	- `all_proxy=socks5://127.0.0.1:4446 ALL_PROXY_NO_FALLBACK=1 syncthing`
	- I also suggest enabling compression for each of your remote devices.
	  Even trivially smaller files will help with how slow the connection will be between the peers.

[kovri]: https://getkovri.org/
[i2pd]: http://i2pd.website/

### Android

Since there is also an Android version of I2P and Syncthing, I was also able to get my phone in my cluster!

For the most part, you follow the instructions above.
The only difference is that you have to manually set the environment variables in the advanced settings in Syncthing.
You will want to enter: `all_proxy=socks5://127.0.0.1:4446 ALL_PROXY_NO_FALLBACK=1` for the manually set environmet variables.

## Outcome

### Performance

I dropped the number of tunnels to be: 1 for the http server, and 3 for the socks proxy. So this means there will be 4 hops.
A more normal set up would have 3 hops and then 3 hops for a total of 6.

With my shorter than normal set up I was seeing speeds up to 150kbps, but mainly floating around 70kbps.
As a quick test, I made the tunnels: 1 hop and 1 hop, and I was consistently seeing 200kbps connections!
It even went above 300kbps at one point 🤤.
The security trade off that comes with using less hops is for everyone to make on their own.
This is for sure a performance hit of having so many redundent hops (just to secure a connection to an endponint you control).

In my situation, I am mainly syncing text files, and pictures.
Personally, I care more that the text files transfer fast, and I don't really care how long the photos take.

### Pros

- No NAT
- 100% self hosted
- No traceable connection between hosts
- You get to run two I2P nodes
- You don't have to trust Syncthing relay servers with anything
- More cover traffic for I2P

### Cons

- Involved set up
- Slower transfer speeds
- You are not really anonymous, since you own both ends
- Since we're using SOCKS Syncthing is likely leaking application level data, but it's probably not a problem in this situation

## Note

Please don't try to be clever and hook up your Syncthing GUI to I2P.
It's possible for someone to enumerate I2P addresses and find it.
You are at risk of losing your personal data if you expose Syncthing's GUI to I2P.

*[also at barry.im](https://barry.im/post/2017/10/06/syncthing-over-i2p/)*
