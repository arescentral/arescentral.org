Antares 0.7.0 Released
======================

:date:      2014-02-02
:author:    sfiera
:tags:      antares, mac, release

`Antares 0.7.0`_ has been released for Mac OS X 10.8+.  This release
fixes a number of bugs and adds supports for gamepads such as the Xbox
360 controller.  It also is the first Antares release to be signed and
sandboxed.

The 10.8+ requirement is unforunate, but unavoidable as Xcode on 10.9
(which I use) doesn't support building against any earlier OS version.

The full list of enhancements fulfilled:

* Issue 59 (Creation of new replays)
* Issue 76 (Make smoke test versions of replays)
* Issue 93 (Extract STR# resources as JSON)
* Issue 94 (Extract TEXT resources as UTF-8)
* Issue 97 (Stop using ADB key codes)
* Issue 110 (Feature Request: Support original MADH music)
* Issue 132 (Sandbox Antares)

The full list of bugs fixed:

* Issue 20 (Mouse isn't hidden)
* Issue 36 (Orientation of level sometimes not random)
* Issue 49 (F1 help doesn't toggle as documented.)
* Issue 53 (Collision flashes can persist after quitting game)
* Issue 62 (Sounds continue to play after level ends)
* Issue 68 (Screen labels persist after level ends)
* Issue 69 (Antares should be 64-bit clean)
* Issue 128 (Demo playback begins immediately at main menu)
* Issue 129 (Brackets persist in mission briefing)
* Issue 130 (Caps Lock pause can cause image persistence)
* Issue 131 (Mission briefing buttons not clickable)
* Issue 133 (Bad interaction with sticky keys)

..  _Antares 0.7.0: https://downloads.arescentral.org/Antares/Antares-0.7.0.zip

..  -*- tab-width: 4; fill-column: 72 -*-
