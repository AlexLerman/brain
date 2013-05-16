Installation
============

Clone the repo, make sure you have bundler installed:

```bash
gem list --local | grep bundler
```

If the above command doesn't output a line like `bundler (1.3.5)`, run:

```bash
gem install bundler
```

and then:

```bash
bundle install
```

to install the gems in the Gemfile.

Running Specs
=============

```bash
rspec spec
```

Using Guard
===========

Guard is an awesome tool that will watch files and perform actions when they
change. To use it, first open two terminal windows (Guard will hog one).

Run this command:

```
guard
```

That's it. Guard is configured to run specs when any files in `app/` or `lib/`
change, and will also run `bundle install` if you change the Gemfile.

For the actual configuration, check out the Guardfile. For the gory details,
look at [Guard on Github](https://github.com/guard/guard).

To stop Guard, use `quit` or `Ctrl-D`. `Ctrl-C` merely cancels the current Guard
command.

Running the App
===============

TODO