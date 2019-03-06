Date: 2016-10-22
Tags: gpg
Category: blog
Title: gpgpipe, an alternative for people who want to curlpipe

The term curlpipe comes from using the program curl to download a file and immediately executing the file via a pipe in the command line ([this is bad and you should feel bad for doing this](https://gnu.moe/wallofshame.md))

![curlpipe found in the wild]({static}/images/gpg-pipe/curlpipe.jpg)

Regardless of the obvious security concerns, many projects feel the need to tell users to execute arbitrary scripts transmitted over plaintext. Is there a workarround for these people? I believe there is now: just pipe it through gpg.


But wait, that won't actually work.

Consider the following:

    curl $url | gpg | bash


This command SHOULD fail if the signature is invalid but it doesn't.

    curl http://i2p.rocks/files/gpg-test.sh.asc | gpg | bash
    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                            Dload  Upload   Total   Spent    Left  Speed
    100   293  100   293    0     0   7274      0 --:--:-- --:--:-- --:--:--  7325
    it works
    backdoor
    gpg: Signature made Sat 22 Oct 2016 08:18:57 AM EDT using DSA key ID D6EA286B
    gpg: BAD signature from "Jeff Becker <ampernand@gmail.com>"

Okay, let's try another approach:

    curl http://i2p.rocks/files/gpg-test.sh.asc | gpg > /tmp/gpgpipe.sh && bash /tmp/gpgpipe.sh 
    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100   293  100   293    0     0   6688      0 --:--:-- --:--:-- --:--:--  6813
    gpg: Signature made Sat 22 Oct 2016 08:18:57 AM EDT using DSA key ID D6EA286B
    gpg: BAD signature from "Jeff Becker <ampernand@gmail.com>"

It fails and doesn't execute. Neato. It's not entirely a pipe as it puts a file down but close enough right?

In conclusion, if for some unholy reason you feel the need to use a curlpipe, PLEASE FOR ALL THAT IS GOOD use a gpg condom.

    gpg --clearsign script.sh

