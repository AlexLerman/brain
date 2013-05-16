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

Running the App
===============

TODO