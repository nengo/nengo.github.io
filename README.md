# Nengo website

This repository contains code and sources files
to generate the [Nengo website](https://www.nengo.ai/).
It's generated with the [Jekyll](http://jekyllrb.com/)
static website generator.

Questions and comments about the content on this website
can be posted on the [Nengo forum](https://forum.nengo.ai/).

Github will build this website on each push.
If you want to build the site locally,
you will need a Ruby environment.

## Build the site locally

### Installation

If you want to build the site just as Github builds it,
you can install the Github pages RubyGem.
From your cloned repository directory, do

```bash
gem install bundler
bundle install
```

Alternatively, to install these requirements
outside of system directories, do

```bash
gem install --user-install bundler
bundle install --path ~/.bundles
```

This will install `bundler` and the Github pages bundle
to your user directory.
If you haven't already, you may have to add
the user Gems folder to your `$PATH`.
To do this for the current session, do

```bash
export PATH=$HOME/.gem/ruby/<version>/bin:$PATH
```

where `<version>` is the version of Ruby you're using.
To have this take effect permanently,
add this line to your `.profile`, `.bashrc`,
or whatever your particular shell uses for configuration.

If you want to serve the page dynamically,
then you also have to install NodeJS.
On Debian and Debian-derivatives,
this can be done with `sudo apt-get install nodejs`.
For more details and install instructions on other platforms,
see the [NodeJS install guilde](
https://nodejs.org/en/download/package-manager/).

When Github pages updates, run

```bash
bundle update
```

To build the site, run

```bash
bundle exec jekyll build
```

The site will be generated in `_site`.

If you would like to serve the site locally, run

```bash
bundle exec jekyll serve
```

The site will now be served at <http://localhost:4000>.

## Props

The site was redesigned in 2019 by a team at
[Fusionbox](https://www.fusionbox.com/)
who were lovely to work with.
