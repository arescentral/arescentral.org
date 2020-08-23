Building Antares
================

To build Antares from source, follow these instructions in a terminal
window:

1. `Install git`_ and use it to create a clone of the `official Antares
   repository`_:

   .. code-block:: sh

      $ git clone https://github.com/arescentral/antares.git
      $ cd antares

   If you have a GitHub account, you may prefer to `fork the project`_
   from its `project on GitHub`_ and then clone your fork.

.. _official antares repository: https://github.com/arescentral/antares
.. _install git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
.. _fork the project: https://help.github.com/articles/fork-a-repo/
.. _project on GitHub: https://github.com/arescentral/antares

2. Configure the project:

   .. code-block:: sh

      $ ./configure

   You may be missing some dependencies.  If the configure script
   fails, then install them as instructed, and run ``./configure``
   again.

   Optional: `read more about ./configure`_.

3. Build:

   .. code-block:: sh

      $ make

   Optional: `read more about make`_.

4. Play:

   .. code-block:: sh

      $ make run

5. Run the tests:

   .. code-block:: sh

      $ make test

   Optional: `read more about make test`_.

6. (Mac only) For a release build, sign the binary:

   .. code-block:: sh

      $ make sign

7. (Linux only) Install the game:

   .. code-block:: sh

      $ sudo make install

   This will install the game to ``/usr/local/games/antares``, by
   default. You can choose a different location with ``./configure``.


Further reading
---------------

.. _read more about ./configure:

``./configure``
~~~~~~~~~~~~~~~

Normally, it’s sufficient to run ``./configure`` without any arguments.
However, there are some options you can pass to build Antares in
different ways:

*  By default, Antares will be configured in ``opt`` mode, meaning that
   it will try to make the resulting binary as fast as possible. If you
   expect to use a debugger with the resulting binary, you may want to
   use ``dbg`` mode instead, which removes optimizations and compiles
   the binary with debugging information:

   .. code-block:: sh

      $ ./configure --mode=dbg

*  On Linux, the game is installed to ``/usr/local/games/antares`` by
   default. The ``--prefix`` argument to ``./configure`` changes this.

   .. code-block:: sh

      $ ./configure --prefix=/opt/antares


.. _read more about make:

``make``
~~~~~~~~

The ``make`` command (with no arguments) is a wrapper around ``ninja``.
You can also use ``ninja`` directly, which exposes additional options.

*  Keep building even after a failure:

   .. code-block:: sh

      $ ninja -C out/cur -k 0


.. _read more about make test:

``make test``
~~~~~~~~~~~~~

Antares has an extensive suite of regression tests. These play through
several different levels of the game to verify that the same behavior is
observed for the same input.

*  If you're running the tests frequently, running in smoke-test mode
   will speed up the tests:

   .. code-block:: sh

      $ make smoke-test

*  There are more options if you use the wrapped script directly:

   .. code-block:: sh

      $ make
      $ scripts/test.py --type=replay


.. -*- tab-width: 3; fill-column: 72 -*-
