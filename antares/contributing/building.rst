Building Antares
================

To build Antares from source, follow these instructions:

..  highlight:: sh

1.  Use ``git`` to create a clone of the `official Antares
    repository`_::

        $ git clone https://github.com/arescentral/antares.git
        $ cd antares

    If you have a GitHub account, you may prefer to `fork the project`_
    from its `project on GitHub`_ and then clone your fork.

2.  Install gyp_::

        $ brew install --HEAD scripts/gyp.rb  # Mac, via homebrew
        $ sudo aptitude install gyp  # Ubuntu

3.  Install ninja_::

        $ brew install ninja  # Mac, via homebrew
        $ sudo aptitude install ninja-build  # Ubuntu

4.  Check out the submodules::

        $ git submodule init
        $ git submodule update

5.  Configure the project::

        $ ./configure

    By default, Antares will be configured in ``opt`` mode, meaning that
    it will try to make the resulting binary as fast as possible.  For
    development, you may want to use ``dev`` mode, which will try to
    speed up the compilation process instead::

        $ ./configure --mode=dev

    If you expect to use ``gdb`` with the resulting binary, you may want
    to use ``dbg`` mode, which compiles the binary with debugging
    information::

        $ ./configure --mode=dbg

    If in doubt, use ``--mode=dev`` if you're planning to do development
    work, and use the default if you just want a more recent version of
    the game.

6.  Build the project::

        $ make

    The Makefile bundled with Antares is a wrapper around ``ninja``.
    You can also use ``ninja`` directly, which exposes additional
    options::

        $ ninja -C out/cur -h

7.  Install the factory scenario::

        $ out/cur/antares-install-data

    The Mac version of Antares already does this, so if you've played
    the game already on Mac, there should be no need (the installer will
    detect this and do nothing in that case).

    This is necessary on the Linux version, or if you want to run the
    tests without first playing the game on Mac.

8.  Run the tests::

        $ make test

    Antares has an extensive suite of regression tests, which play
    through several different levels of the game to verify that the same
    behavior is observed for the same input.  If you're running the
    tests frequently, running in smoke-test mode will speed up the
    tests::

        $ make smoke-test

    Again, there are more options if you use the wrapped script
    directly::

        $ scripts/test.py --type=replay

9.  Play the results::

        $ make run

    Antares does not currently use the ``install`` target.

10. For a release build, sign the binary::

        $ make sign

..  _gyp: https://code.google.com/p/gyp/
..  _ninja: http://martine.github.io/ninja/manual.html
..  _homebrew: http://brew.sh/
..  _official antares repository: https://github.com/arescentral/antares
..  _fork the project: http://help.github.com/fork-a-repo/
..  _project on GitHub: https://github.com/arescentral/antares

..  -*- tab-width: 4; fill-column: 72 -*-
