FAQ-Answered Questions
======================

..  sectnum::

..  contents::
    :local:
    :backlinks: none

General
-------

Where can I get Antares?
~~~~~~~~~~~~~~~~~~~~~~~~
..  include:: ../release.rsti

Who wrote Antares?
~~~~~~~~~~~~~~~~~~
See Antares's `AUTHORS`_ file. Most of the work was done by
`Nathan Lamont`_, who wrote the original game for Mac OS Classic, Ares,
and `Chris Pickel`_, who ported it to Mac OS X as Antares.

..  _AUTHORS: https://github.com/arescentral/antares/blob/master/AUTHORSS
..  _Nathan Lamont: http://biggerplanet.com/
..  _Chris Pickel: https://sfiera.net/

When will Antares 1.0 be released?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
As soon as multiplayer_ is (re-)added.

How similar is Antares to Ares?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Very near to pixel-perfect. In general, there are three reasons Antares
may not be a pixel-perfect match to Ares in a given situation:

*   Ares used a custom software renderer when zooming in and out,
    whereas Antares uses an OpenGL hardware renderer.
*   Antares incorporates fixes for minor bugs that were present in Ares.
*   Antares is not yet a complete replacement for Ares.

What platforms does Antares run on?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Antares currently builds and runs on:

*   Mac OS X (|antares-latest-osx-version|)
*   Linux

In the future, it may also run on:

*   Windows_ (`Issue 79`_)

There are no plans to port it to Mac OS Classic, or to any mobile
platform.

.. _Issue 79: https://github.com/arescentral/antares/issues/79

Where does the name "Antares" come from?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Antares is the common name for `α Scorpii`_. Its name means "anti-Ares",
because although it is a bright red star similar in appearance to Mars
(Ares), it is something very different.

.. _α Scorpii: https://en.wikipedia.org/wiki/Antares

Plugins
-------

What is the status of plugins in Antares?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Plugins are fully supported. However, the format is different from the
format used in Ares. Several plugins are available on the `Plugins
page`_.

.. _Plugins page: /plugins

What format does Antares use for plugins?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
An Antares plugin is a Zip archive with the extension “.antaresplugin”.
It contains text configuration files, along with images and sounds.

Full details on the format are in the `plugin documentation`_.

.. _plugin documentation: /plugins/format

How do the Antares and Ares plugin formats differ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
There are three main ways:

*  Ares plugins use the resource fork. Antares plugins are Zip archives.
*  Ares plugin data is mostly binary. Antares plugin data is mostly
   text.
*  Ares plugin data is numbered. Antares plugin data is named.

For example, in Ares, the Ishiman Cruiser is the first 318 bytes of
'bsob' 500. In Antares, it is the file `objects/ish/cruiser.pn`_.

.. _objects/ish/cruiser.pn: https://github.com/arescentral/antares-data/blob/master/objects/ish/cruiser.pn

How do I use plugins written for Ares with Antares?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
There is no tool for converting a plugin from one format to another. If
a plugin you want to play is not available for Antares, you can `send a
request`_ for it to be converted manually.

.. _send a request: mailto:antares-dev@arescentral.org

What tools exist for plugin development?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Currently, there are no tools for developing Antares plugins. Since the
files are readable text, building a tool is not a priority, but if you
are interested in developing one, `talk to the developer`_.

.. _talk to the developer: mailto:antares-dev@arescentral.org

Multiplayer
-----------

What is the status of multiplayer in Antares?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None to speak of at present. When it eventually exists, Antares
multiplayer will likely look very different from Ares multiplayer. Some
things that will probably change are:

*  Multiplayer will support more than 2 players.
*  In order to support 3+ players, the lobby will look completely
   different, with a more traditional chatroom interface.
*  Players playing the same race as an opponent will choose their own
   tint, instead of a tint for each such opponent (`Issue 6`_).
*  If custom avatars are supported, the mechanism will be different.
*  The networking protocol will use `state synchronization`_ over UDP
   instead of input sychronization over NetSprockets.
*  `GameRanger`_ will not be supported. Another metaserver may replace
   it.

.. _Issue 6: https://github.com/arescentral/antares/issues/6
.. _state synchronization: https://github.com/arescentral/antares/blob/master/doc/net.rst
.. _GameRanger: https://www.gameranger.com/

When will multiplayer support be released?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
There is no expected timeline for multiplayer support.

Windows
-------

What is the status of Windows support in Antares?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Antares is not available for Windows.

However, on Linux, some parts of the game can be compiled with mingw and
run under WINE.

When will Windows support be released?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
There is no expected timeline for Windows support.

Why compile with mingw instead of on Windows?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The main Antares developer doesn’t have a Windows machine and doesn’t
really know anything about developing for Windows. Compiling with mingw
was possible without any of that equipment or knowledge.

There’s no real reason it needs to use mingw. As long as Travis_ can
continue to run the tests, it would be fine to compile natively on
Windows. However, it’s probably necessary to continue to compile with
clang_, and to use MSYS2_ for that.

.. _Travis: https://travis-ci.org/
.. _clang: https://packages.msys2.org/base/mingw-w64-clang
.. _MSYS2: https://www.msys2.org/

What steps need to be taken?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A general overview might be:

*  Choose paths for installed application data (`win-dirs.cpp`_), so
   that it’s possible to build ``antares-install-data.exe``.
*  Implement the offscreen OpenGL driver (`Issue 324
   <https://github.com/arescentral/antares/issues/324>`_), so that it’s
   possible to build ``build-pix.exe``, ``offscreen.exe``, and
   ``replay.exe``.
*  Implement the real video driver (`Issue 323
   <https://github.com/arescentral/antares/issues/323>`_) and sound
   driver (`Issue 322
   <https://github.com/arescentral/antares/issues/322>`_).
*  Compile ``antares-glfw.exe``.
*  Package it properly as a Windows application.

More specifically, in `BUILD.gn`_, there are a bunch of places that
something like the following appears::

   if (target_os == "win") {
     group -= [ entry ]
   }

Any place that appears, it indicates a gap in Windows support.

.. _win-dirs.cpp: https://github.com/arescentral/antares/blob/master/src/config/win-dirs.cpp
.. _BUILD.gn: https://github.com/arescentral/antares/blob/master/BUILD.gn

.. include:: ../epilog.rsti

.. -*- tab-width: 3; fill-column: 72 -*-
