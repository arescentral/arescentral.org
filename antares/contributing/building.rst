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

2.  Install dependencies.  On Mac, Xcode_ includes everything needed.
    You may need to agree to the license agreement.  On Linux, install
    the tools needed to build binaries with clang, plus some libraries::

        $ sudo apt-get install \
            build-essential clang libc++-dev \
            libneon27-dev libopenal-dev \
            libgl1-mesa-dev libglu1-mesa-dev \
            libxrandr-dev libxcursor-dev libxinerama-dev  # Ubuntu

    Several libraries are bundled with the Antares source (GLFW, libpng,
    libmodplug, libsndfile, libzip, librezin) because they are needed by
    the Mac version.  These are statically-linked into the resulting
    binary, but the Linux version might link them dynamically in the
    future.

3.  Install gyp_::

        $ brew install --HEAD scripts/gyp.rb  # Mac, via homebrew
        $ sudo apt-get install gyp  # Ubuntu

4.  Install ninja_::

        $ brew install ninja  # Mac, via homebrew
        $ sudo apt-get install ninja-build  # Ubuntu

5.  Check out the submodules::

        $ git submodule init
        $ git submodule update

6.  Configure the project::

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

7.  Build the project::

        $ make

    The Makefile bundled with Antares is a wrapper around ``ninja``.
    You can also use ``ninja`` directly, which exposes additional
    options::

        $ ninja -C out/cur -h

8.  Install the factory scenario::

        $ out/cur/antares-install-data

    The Mac version of Antares already does this, so if you've played
    the game already on Mac, there should be no need (the installer will
    detect this and do nothing in that case).

    This is necessary on the Linux version, or if you want to run the
    tests without first playing the game on Mac.

9.  Run the tests::

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

10.  Play the results::

        $ make run

    Antares does not currently use the ``install`` target.

11. For a release build, sign the binary::

        $ make sign

..  _xcode: https://itunes.apple.com/en/app/xcode/id497799835
..  _gyp: https://code.google.com/p/gyp/
..  _ninja: http://martine.github.io/ninja/manual.html
..  _homebrew: http://brew.sh/
..  _official antares repository: https://github.com/arescentral/antares
..  _fork the project: http://help.github.com/fork-a-repo/
..  _project on GitHub: https://github.com/arescentral/antares

..  -*- tab-width: 4; fill-column: 72 -*-
