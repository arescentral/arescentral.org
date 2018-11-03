Ten Years
=========

:date:    2018-11-03
:author:  sfiera
:tags:    misc

Ares was open-sourced__ ten years ago yesterday. I figure that’s as good
a time as any to look back and forward.

__	http://biggerplanet.com/ares

*	The first Antares release was a year later. At that time, most of the
	people interested in open-source Ares were focused on recreating it
	instead of porting it. I gave myself one year to demonstrate that
	porting it was possible. It worked! However, the first release had no
	sound, was missing lots of the interface, and drew the game by
	implementing half of QuickDraw and throwing a bitmap on the screen.

*	In 2010, two years in, Ambrosia’s registration of arescentral.com__
	expired, and I snagged it along with arescentral.org. If you have an
	old Mac, you should be able to use the links included with Ares to
	get here.

__	http://arescentral.com/

*	In 2011, Antares added support for plugins. At the time, there was a
	plugin editor too (Athena__), though it hasn’t seen much work since
	then.

__	https://github.com/gamefreak/Athena

*	In 2012, the half-backed QuickDraw implementation was replaced with a
	real, OpenGL-based graphics engine. This needed some expertise that I
	didn’t originally have—how do you draw static in a shader? How do you
	outline a sprite?

*	In 2015, Antares ran on Linux for the first time. Initially, it was a
	compile-it-yourself deal, but now it’s available through `package
	managers`__.

__	/antares/linux

*	In 2018, the old binary plugin format was replaced by a `modern,
	simpler format`__.

__	/plugins/format

Looking forward, there are still two things missing:

*	“Version 1.0”
*	Multiplayer

They’re really the same thing. Lack of multiplayer support is what
prevents me from declaring version 1.0. Now, in the past, I’ve said
Antares would support multiplayer again “by the ten year mark” (as if
that day would ever come!). It will take a bit longer, but it’s going to
happen.

I don’t want to make promises about when there will be a beta ready to
test, beyond the fact that I won’t make any progress in the next three
months due to “real life” stuff. However, I will need testers. So, if
you would be interested, please either:

*	Join `#antares on Discord`__
*	`Email me`__
  
__	https://discord.gg/x6XPsP6
__	mailto:sfiera@twotaled.com

.. -*- tab-width: 3; indent-tabs-mode: nil; fill-column: 72 -*-
