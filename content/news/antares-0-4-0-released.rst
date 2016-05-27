Antares 0.4.0 Released
======================

:date:      2011-10-03
:author:    sfiera
:tags:      antares, mac, release

`Antares 0.4.0`_ has been released. This release fixes several issues:

* Issue 21 (Briefing points clipped at edge of map)
* Issue 23 (Smearing in third tutorial)
* Issue 42 (Pausing via CAPS causes smearing)
* Issue 44 (Mouse areas wrong for help and play-again screens)
* Issue 58 (Design new replay file format)
* Issue 60 (Mac menu bar intercepts events in full-screen)
* Issue 63 (Minicomputer double-click threshold is proportional to time
  game has been open.)
* Issue 45 (Music preferences not really respected)
* Issue 52 (Scaled-up static is squashed horizontally.)
* Issue 54 (Sprites unnecessarily hidden at right edge of screen.)
* Issue 55 (At 1:16, squares clipped but other shapes disappear)
* Issue 64 (Kinetic beams have a black contrail)
* Issue 67 (Stars sometimes flash when leaving warp)

The sprite-drawing engine has been moved out of software and into
OpenGL, hopefully providing performance improvements and certainly
making Antares more maintainable in the long run.  Other parts of the
game are still drawn in software, however.

In addition, Antares 0.4.0 is the first release of Antares to open up
its `source code repository`_.  If you're interested in helping with the
game, it has a `contributing page
<{filename}/antares/contributing.rst>`_ detailing ways to help.

..  _Antares 0.4.0: http://downloads.arescentral.org/Antares/Antares-0.4.0.zip
..  _source code repository: https://github.com/arescentral/antares

..  -*- tab-width: 4; fill-column: 72 -*-
