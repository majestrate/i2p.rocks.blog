# i2p.rocks blog repo #

## Repositories

* [github](https://github.com/majestrate/i2p.rocks.blog/)
* [tor](http://git.psii2pdloxelodts.onion/psi/i2p.rocks.blog/)
* [i2p](http://git.psi.i2p/psi/i2p.rocks.blog/)

## building ##

### dependancies ###

* git
* pelican
* python 3.x (required by pelican)

### setting up ###

    git clone https://github.com/majestrate/i2p.rocks.blog
    cd i2p.rocks.blog
    make html

### deploying via ssh ###

    make ssh_upload

## New Blog Posts ##

Copy `templates/blog.md` to `content/name-of-blog-post.md`

edit `content/name-of-blog-post.md`

commit with `git add content/name-of-blog-post.md && git commit -a`

add pull request.
