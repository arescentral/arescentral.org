:orphan:
:date:      2014-02-02
:author:    Chris Pickel <sfiera@sfzmail.com>

Antares 0.7.0 Released
======================

`Antares 0.7.0`_ has been released for Mac OS X 10.8+.  This release
fixes a number of bugs and adds supports for gamepads such as the Xbox
360 controller.  It also is the first Antares release to be signed and
sandboxed.

The 10.8+ requirement is unforunate, but unavoidable as Xcode on 10.9
(which I use) doesn't support building against any earlier OS version.

The full list of enhancements fulfilled:

* Issue 56 (Creation of new replays)
* Issue 73 (Make smoke test versions of replays)
* Issue 90 (Extract STR# resources as JSON)
* Issue 91 (Extract TEXT resources as UTF-8)
* Issue 94 (Stop using ADB key codes)
* Issue 107 (Feature Request: Support original MADH music)
* Issue 129 (Sandbox Antares)

The full list of bugs fixed:

* Issue 17 (Mouse isn't hidden)
* Issue 33 (Orientation of level sometimes not random)
* Issue 46 (F1 help doesn't toggle as documented.)
* Issue 50 (Collision flashes can persist after quitting game)
* Issue 59 (Sounds continue to play after level ends)
* Issue 65 (Screen labels persist after level ends)
* Issue 66 (Antares should be 64-bit clean)
* Issue 125 (Demo playback begins immediately at main menu)
* Issue 126 (Brackets persist in mission briefing)
* Issue 127 (Caps Lock pause can cause image persistence)
* Issue 128 (Mission briefing buttons not clickable)
* Issue 130 (Bad interaction with sticky keys)

..  _Antares 0.7.0: http://downloads.arescentral.org/Antares/Antares-0.7.0.zip

..  -*- tab-width: 4; fill-column: 72 -*-
