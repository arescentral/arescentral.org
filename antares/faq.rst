FAQ-Answered Questions
======================

..  contents::
    :local:
    :backlinks: none

1. General
----------

1.1. Where can I get Antares?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
..  include:: /release.rsti

1.2. Who wrote Antares?
~~~~~~~~~~~~~~~~~~~~~~~
See Antares's `AUTHORS`_ file. Most of the work was done by
`Nathan Lamont`_, who wrote the original game for Mac OS Classic, Ares,
and `Chris Pickel`_, who ported it to Mac OS X as Antares.

..  _AUTHORS: https://github.com/arescentral/antares/blob/develop/AUTHORS
..  _Nathan Lamont: http://biggerplanet.com/
..  _Chris Pickel: http://sfiera.net/

1.3. When will Antares 1.0 be released?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
As soon as the `release issues`_ have been resolved. Some of the
highlights of these issues are:

*   Completing the move from Ares's software renderer to the OpenGL
    hardware renderer.
*   Making other performance improvements.
*   Adding support for creating and playing back replays.
*   Improving the test suite.

..  _release issues: https://github.com/arescentral/antares/issues?q=is%3Aissue+is%3Aopen+-milestone%3ALater+

1.4. How similar is Antares to Ares?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Very near to pixel-perfect. In general, there are three reasons Antares
may not be a pixel-perfect match to Ares in a given situation:

*   Ares used a custom software renderer when zooming in and out,
    whereas Antares uses an OpenGL hardware renderer.
*   Antares incorporates fixes for minor bugs that were present in Ares.
*   Antares is not yet a complete replacement for Ares.

1.5. What platforms does Antares run on?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Antares currently builds and runs on:

*   Mac OS X (|antares-latest-osx-version|)

In the future, it may also run on:

*   Linux, probably by Antares 1.0 (Issue 78)
*   Windows, with no expected timeline (Issue 79)

There are no plans to port it to Mac OS Classic, or to any mobile
platform.

1.6. What is the status of multiplayer in Antares?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None to speak of at present. When it eventually exists, Antares
multiplayer will likely look very different from Ares multiplayer. Some
things that will probably change are:

*   Multiplayer will support more than 2 players.
*   In order to support 3+ players, the lobby will look completely
    different, with a chat interface more similar to :abbr:`IRC
    (Internet Relay Chat)`.
*   Players playing the same race as an opponent will choose their own
    tint, instead of a tint for each such opponent (Issue 6).
*   If custom avatars are supported, the mechanism will be different.
*   The networking protocol will use `state synchronization`_ over
    :abbr:`UDP (User Datagram Protocol)` instead of input sychronization
    over NetSprockets.
*   `GameRanger`_ will not be supported. Another metaserver may replace
    it.

..  _state synchronization: http://nclabs.org/articles/5
..  _GameRanger: http://www.gameranger.com/

1.7. Where does the name "Antares" come from?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Antares is the common name for `α Scorpii`_. Its name means "anti-Ares",
because although it is a bright red star similar in appearance to Mars
(Ares), it is something very different.

..  _α Scorpii: http://en.wikipedia.org/wiki/Antares

2. Plugins
----------

2.1. What format does Antares use for plugins?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Antares plugin format is essentially the same as the traditional
Ares plugin format, except that instead of storing resources in the
resource fork, it stores files in a zip archive.  This means that the
same plugin bundles can be used on all platforms.

2.2. How do I use plugins written for Ares with Antares?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
There is no tool for converting a plugin from one format to another. If
a plugin you want to play is not available for Antares, you can `post a
request`_ for it to be converted manually.

..  _post a request: http://www.ambrosiasw.com/forums/index.php?showtopic=130975

2.3. What tools exist for plugin development?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The best tool at present is `Athena`_, by `Scott McClaugherty`_. Because
the Antares plugin format is so similar to that used by Ares, it would
also be possible to do much of the work in Hera (if you'd want to) and
then have the plugin manually converted.

..  _Athena: https://github.com/gamefreak/Athena
..  _Scott McClaugherty: https://github.com/gamefreak

..  -*- tab-width: 4; fill-column: 72 -*-
