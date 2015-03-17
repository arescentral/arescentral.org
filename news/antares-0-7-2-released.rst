:orphan:
:date:      2014-04-03
:author:    Chris Pickel <sfiera@sfzmail.com>

Antares 0.7.2 Released
======================

`Antares 0.7.2`_ has been released for Mac OS X 10.8+.  This is a hotfix
release primarily targeting retina support:

* Issue 135 (Doesn't work on retina displays)
* Issue 140 (Crash on startup - non-window mode only)

On retina displays, the game should now make use of retina resolution in
windowed mode (i.e. at 1:2 zoom, you will see ships in full detail).
However, I don't have a retina display, so I can't confirm this myself
(or even that I've fixed the reported crashes).  I'd appreciate it if
anyone with a retina display could `report how it works`_.

Additionally, there's one bugfix and a feature for developers:

* Issue 139 (Game crashes on pressing F1)
* Issue 73 (Parallelize Antares tests)

..  _report how it works: mailto:sfiera@sfzmail.com
..  _Antares 0.7.2: http://downloads.arescentral.org/Antares/Antares-0.7.2.zip

..  -*- tab-width: 4; fill-column: 72 -*-
