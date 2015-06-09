Building Antares
================

To build Antares from source, follow these instructions in a terminal
window:

..  highlight:: sh

1.  Download, unzip, and enter the |antares-latest-src|:

    ..  rst-class:: highlight-sh
    ..  container::

        ..  rst-class:: highlight
        ..  container::

            ..  parsed-literal::

                $ curl -O |antares-latest-src-url|
                $ unzip Antares-Source-|antares-latest|.zip
                $ cd Antares-|antares-latest|

    Or use ``git`` to create a clone of the `official Antares
    repository`_::

        $ git clone https://github.com/arescentral/antares.git
        $ cd antares

    If you have a GitHub account, you may prefer to `fork the project`_
    from its `project on GitHub`_ and then clone your fork.

2.  Configure the project::

        $ ./configure

    You may be missing some dependencies.  If the configure script
    fails, then install them as instructed, and run ``./configure``
    again.

3.  Build the project::

        $ make

4.  Install the factory scenario (necessary only on Linux)::

        $ out/cur/antares-install-data

    The Mac version will do this automatically the first time you play
    the game.

5.  Play::

        $ make run

6.  Run the tests::

        $ make test

    Antares has an extensive suite of regression tests, which play
    through several different levels of the game to verify that the same
    behavior is observed for the same input.  If you're running the
    tests frequently, running in smoke-test mode will speed up the
    tests::

        $ make smoke-test

    There are more options if you use the wrapped script directly::

        $ scripts/test.py --type=replay

7.  For a release build, sign the binary::

        $ make sign

8.  Antares does not currently use the ``install`` target.


Further reading
---------------

*   By default, Antares will be configured in ``opt`` mode, meaning that
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

*   The Makefile bundled with Antares is a wrapper around ``ninja``.
    You can also use ``ninja`` directly, which exposes additional
    options::

        $ ninja -C out/cur -h



..  _xcode: https://itunes.apple.com/en/app/xcode/id497799835
..  _gyp: https://code.google.com/p/gyp/
..  _ninja: https://martine.github.io/ninja/manual.html
..  _homebrew: http://brew.sh/
..  _official antares repository: https://github.com/arescentral/antares
..  _fork the project: http://help.github.com/fork-a-repo/
..  _project on GitHub: https://github.com/arescentral/antares

..  -*- tab-width: 4; fill-column: 72 -*-
