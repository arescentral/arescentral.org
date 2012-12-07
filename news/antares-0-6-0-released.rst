:orphan:
:date:      2012-12-06
:author:    Chris Pickel <sfiera@sfzmail.com>

Antares 0.6.0 Released
======================

`Antares 0.6.0`_ has been released for Mac OS X 10.6+.  This release
contains two new features: first, you can now run Antares in a window,
instead of full screen.  Second, if you have a two-button mouse, you can
select target objects with the right mouse button.

Behind the scenes, the graphics engine has been entirely reworked to
make better use of OpenGL and GLSL. This should improve graphical
performance for most users. However, there is a possibility of
compatibility problems. If you see any problems, you can file a bug on
Antares's `issue tracker`_.

Antares 0.6.0 contains several fixes for issues that were present in
Ares 1.2.0:

* Issue 2 (Mouse movement disrupts replays)
* Issue 111 (No special weapon shown when selection change from
  destination)
* Issue 112 (Control, target sprites clipped in minicomputer)
* Issue 113 (Minicomputer object's target does not change colors)
* Issue 114 (Minicomputer targets sometimes not updated when switching
  to/from destination objects)
* Issue 116 (Minicomputer buttons not consistent on background color)
* Issue 117 (Minicomputer may not initially show control/target)

…several for issues present in earlier versions of Antares:

* Issue 10 (Mission briefing doesn't allow display of ship stats)
* Issue 12 (Loading progress bar doesn't display)
* Issue 34 (Mission debriefing disappears too easily)
* Issue 37 (Mission debriefing doesn't display typing blocks)
* Issue 105 (Sprites sometimes appear in front of instruments)
* Issue 106 (Shield stenciling doesn't always work)
* Issue 118 (Control, target sprites off-center in minicomputer)
* Issue 119 (Sometimes screen black after starting level)

…plus improvements intended to make Antares more maintainable in the
future.

Sadly, this release is not compatible with Mac OS X 10.4 or 10.5.  If
you are still running one of those versions, `Antares 0.5.1`_ is still
available.

..  _Antares 0.6.0: http://downloads.arescentral.org/Antares/Antares-0.6.0.zip
..  _issue tracker: http://code.google.com/p/antares/issues/entry
..  _Antares 0.5.1: http://downloads.arescentral.org/Antares/Antares-0.5.1.zip

..  -*- tab-width: 4; fill-column: 72 -*-
