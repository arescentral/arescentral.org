Building Antares
================

To build Antares from source, follow these instructions:

..  highlight:: sh

1.  Use ``git`` to create a clone of the `official Antares repository`_,
    and check out the ``develop`` branch::

        $ git clone https://code.google.com/p/antares/
        $ cd antares
        $ git checkout develop

    If you have a GitHub account, you may prefer to `fork the project`_
    from its `mirror on GitHub`_ and then clone your fork.

2.  Check out the submodules::

        $ git submodule init
        $ git submodule update

3.  Configure the project::

        $ ./configure

    By default, Antares will be configured in ``opt`` mode, meaning that
    it will try to make the resulting binary as fast as possible.  For
    development, you may want to use ``dev`` mode, which will try to
    speed up the compilation process instead::

        $ ./configure -mdev

    If you expect to use ``gdb`` with the resulting binary, you may want
    to use ``dbg`` mode, which compiles the binary with debugging
    information::

        $ ./configure -mdbg

    If in doubt, use ``-mdev`` if you're planning to do development
    work, and use the default if you just want a more recent version of
    the game.

4.  Build the project::

        $ make

    The Makefile bundled with Antares is a wrapper around ``waf``.  You
    can also use the ``waf`` script directly, which exposes additional
    options::

        $ ./waf -p

5.  Run the tests::

        $ make test

    Antares has an extensive suite of regression tests, which play
    through several different levels of the game to verify that the same
    behavior is observed for the same input.  Again, using the ``waf``
    script directly exposes additional options::

        $ ./waf test --test-filter=antares/replay/space-race

6.  Play the results::

        $ ./build/antares/Antares.app/Contents/MacOS/Antares

    Antares does not currently use the ``install`` target.

..  _official antares repository: https://code.google.com/p/antares/source/
..  _fork the project: http://help.github.com/fork-a-repo/
..  _mirror on GitHub: https://github.com/arescentral/antares

..  -*- tab-width: 4; fill-column: 72 -*-
