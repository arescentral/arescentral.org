Types
=====

.. sectnum::

.. contents::
   :local:
   :backlinks: none

Procyon
-------

Aside from sound and graphics, most Antares data files use `Procyon
notation`_. Procyon is a text-based format with indented blocks. It
looks like this:

.. _Procyon notation: https://github.com/arescentral/procyon

.. include:: pn/types-procyon.pn
   :code: procyon

.. _basic types:

Basic
-----

Null
~~~~

Generally, anything not specified is assumed to be null (no value), but
it can also be explicitly specified.

Boolean
~~~~~~~

Either ``true`` or ``false``. Generally, if a boolean is not required,
the assumed value is ``false``.

Integer
~~~~~~~

A whole number, such as ``0`` or ``42`` or ``-9000``.

Number
~~~~~~

A number, optionally with a fractional component, such as ``0.0`` or
``4.2`` or ``-9000``.

Usually, numbers in Antares have a resolution of (1/256). Fractional
differences smaller than this may be ignored.

String
~~~~~~

A piece of text. There are two ways to write a string: first, a short
way, by putting the text in quotes ``"like this"``; and second, by using
``>`` and ``|`` in an indented block:

.. include:: pn/types-string.pn
   :code: procyon

As of Antares 0.9.0, the game fonts_ are limited to MacRoman_, so only
the following characters should be used:

.. table::
   :widths: auto

   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | MacRoman: printable character set                                                                                             |
   +=======+=======+=======+=======+=======+=======+=======+=======+=======+=======+=======+=======+=======+=======+=======+=======+
   |       | ``!`` | ``"`` | ``#`` | ``$`` | ``%`` | ``&`` | ``'`` | ``(`` | ``)`` | ``*`` | ``|`` | ``,`` | ``-`` | ``.`` | ``/`` |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | ``0`` | ``1`` | ``2`` | ``3`` | ``4`` | ``5`` | ``6`` | ``7`` | ``8`` | ``9`` | ``:`` | ``;`` | ``<`` | ``=`` | ``>`` | ``?`` |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | ``@`` | ``A`` | ``B`` | ``C`` | ``D`` | ``E`` | ``F`` | ``G`` | ``H`` | ``I`` | ``J`` | ``K`` | ``L`` | ``M`` | ``N`` | ``O`` |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | ``P`` | ``Q`` | ``R`` | ``S`` | ``T`` | ``U`` | ``V`` | ``W`` | ``X`` | ``Y`` | ``Z`` | ``[`` | ``\`` | ``]`` | ``^`` | ``_`` |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | |btk| | ``a`` | ``b`` | ``c`` | ``d`` | ``e`` | ``f`` | ``g`` | ``h`` | ``i`` | ``j`` | ``k`` | ``l`` | ``m`` | ``n`` | ``o`` |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | ``p`` | ``q`` | ``r`` | ``s`` | ``t`` | ``u`` | ``v`` | ``w`` | ``x`` | ``y`` | ``z`` | ``{`` | ``|`` | ``}`` | ``~`` |       |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | ``Ä`` | ``Å`` | ``Ç`` | ``É`` | ``Ñ`` | ``Ö`` | ``Ü`` | ``á`` | ``à`` | ``â`` | ``ä`` | ``ã`` | ``å`` | ``ç`` | ``é`` | ``è`` |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | ``ê`` | ``ë`` | ``í`` | ``ì`` | ``î`` | ``ï`` | ``ñ`` | ``ó`` | ``ò`` | ``ô`` | ``ö`` | ``õ`` | ``ú`` | ``ù`` | ``û`` | ``ü`` |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | ``†`` | ``°`` | ``¢`` | ``£`` | ``§`` | ``•`` | ``¶`` | ``ß`` | ``®`` | ``©`` | ``™`` | ``´`` | ``¨`` | ``≠`` | ``Æ`` | ``Ø`` |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | ``∞`` | ``±`` | ``≤`` | ``≥`` | ``¥`` | ``µ`` | ``∂`` | ``∑`` | ``∏`` | ``π`` | ``∫`` | ``ª`` | ``º`` | ``Ω`` | ``æ`` | ``ø`` |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | ``¿`` | ``¡`` | ``¬`` | ``√`` | ``ƒ`` | ``≈`` | ``∆`` | ``«`` | ``»`` | ``…`` |       | ``À`` | ``Ã`` | ``Õ`` | ``Œ`` | ``œ`` |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | ``–`` | ``—`` | ``“`` | ``”`` | ``‘`` | ``’`` | ``÷`` | ``◊`` | ``ÿ`` | ``Ÿ`` | ``⁄`` | ``€`` | ``‹`` | ``›`` | ``ﬁ`` | ``ﬂ`` |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | ``‡`` | ``·`` | ``‚`` | ``„`` | ``‰`` | ``Â`` | ``Ê`` | ``Á`` | ``Ë`` | ``È`` | ``Í`` | ``Î`` | ``Ï`` | ``Ì`` | ``Ó`` | ``Ô`` |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
   | ```` | ``Ò`` | ``Ú`` | ``Û`` | ``Ù`` | ``ı`` | ``ˆ`` | ``˜`` | ``¯`` | ``˘`` | ``˙`` | ``˚`` | ``¸`` | ``˝`` | ``˛`` | ``ˇ`` |
   +-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+

.. _MacRoman: https://en.wikipedia.org/wiki/MacRoman
.. |btk| replace:: :literal:`\``

Array
~~~~~

A list of items. There are two ways to write an array: first, a short
way, by putting the items in brackets ``["like", "this"]``; and second,
by using ``*`` in an indented block:

.. include:: pn/types-array.pn
   :code: procyon

Map
~~~

A sequence of keys and values. There are two ways to write a map: first,
a short way, by putting the keys and values in braces ``{like:
"this"}``; and second, by using ``:`` in an indented block:

.. include:: pn/types-map.pn
   :code: procyon

Many Antares data types are maps, with their fields defined in a table
like this:

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   name                  yes   string_
   at                    yes   point_
   eats.leaves           no    boolean_
   eats.humans           no    boolean_
   ====================  ====  ========================================

For the above definition, this is one possible corresponding value:

.. include:: pn/types-map-thrntz.pn
   :code: procyon

Derived
-------

Duration
~~~~~~~~

A string_ specifying a length of time. The four units of time in Antares
are:

*  hours (h)
*  minutes (m), each ¹⁄₆₀ of an hour
*  seconds (s), each ¹⁄₆₀ of a minute
*  ticks (t), each ¹⁄₆₀ of a second

Most things in Antares run at a granularity of ``3t`` or ``0.05s``, so
differences shorter than that usually aren’t meaningful.

Fractional amounts of time are valid. ``0.5m`` is the same as ``30s``,
and ``0.01h`` is the same as ``36s``. Antares can’t represent durations
shorter than a tick, though, so ``0.01s`` or ``0.6t`` isn’t valid.

Combining multiple units is valid. ``1m30s`` is the same as ``1.5m``.

The following are all valid durations:

.. include:: pn/types-duration.pn
   :code: procyon

Distance
~~~~~~~~

A number_ indicating the distance between two points in space. When the
game is zoomed to 1:1, distances correspond to pixels: a distance of 200
shows as a distance of 200 pixels.

Speed
~~~~~

A number_ indicating a change in distance_ over time, in units of
`px/t`, or pixels-per-`tick <#duration>`_. When the game is zoomed to
1:1, an object moving at a speed of `5.0 px/t` moves 5 pixels per tick,
or 300 pixels per second.

Acceleration
~~~~~~~~~~~~

A number_ indicating a change in speed_ over time, in units of `px/t²`,
or pixels-per-`tick <#duration>`_-squared. An object accelerating at
`0.05 px/t²` will increase its speed by 0.05 per tick, or 3.0 per
second.

Angle
~~~~~

An integer_ in units of degrees, usually from 0 to 360. An angle of 0°
means straight up or north. An angle of 90° means straight right or
east.

Angular Speed
~~~~~~~~~~~~~

A number_ indicating a change in angle_ over time, in units of `°/t`, or
degrees-per-`tick <#duration>`_. An object turning at `2.0°/t` will
change its direction by 2 degrees per tick, or 120 degrees per second,
making a full rotation in 3 seconds.

Point
~~~~~

A map_ specifying a 2-dimensional location. Points have an ``x`` and a
``y`` component, both numbers_ (often distances_ or integers_). The
following are all valid points:

.. include:: pn/types-point.pn
   :code: procyon

Coordinates are mapped to quadrants as follows::

   NW    N    NE
         ╷   
      -x │ +x
      -y │ -y
   W ────┼──── E
      -x │ +x
      +y │ +y
         ╵   
   SW    S    SE

Rect
~~~~

A map_ specifying a 2-dimensional rectangle. Rects have ``left``,
``top``, ``right``, and ``bottom`` components, all numbers_ (often
distances_ or integers_). In a non-empty rect, ``left < right`` and
``top < bottom``. The following are all valid, non-empty rects:

.. include:: pn/types-rect.pn
   :code: procyon

Range
~~~~~

A number_ or map_ specifying a range of values. If specified as a
number, then the range contains only that specific value. If specified
as a map_, then it is a `half-open interval`_ with a ``begin`` and
``end`` component, containing all values `x` such that `begin ≤ x <
end`. The following are all valid ranges:

.. _half-open interval: https://en.wiktionary.org/wiki/half-open_interval

.. include:: pn/types-range.pn
   :code: procyon

If the range is integer_-valued, then the last two ranges are
equivalent, containing only 5 (and ``5`` is the preferred form).
However, if they are number_-valued, then ``{begin: 5, end: 6}`` also
includes values like 5.5 and 5.923.

Counter
~~~~~~~

A map_ specifying one of a player’s three counters. Counters have two
keys: ``player``, the index_ of a player in the level, and ``which``,
the number of a counter, numbered from 0 to 2. The following are all
valid counters:

.. include:: pn/types-counter.pn
   :code: procyon

In some cases, such as a `score action`_, it may also be valid to omit
``player``:

.. include:: pn/types-counter-omit.pn
   :code: procyon

.. _score action: {filename}/plugins/format/action.rst#score

Money
~~~~~

A number_ specifying an amount of cash. Players `earn money`_ from
planets and stations that they own, and `spend money`_ to build ships. A
player’s cash is shown on the right-hand side of the screen. Each of the
100 small green bars is worth ¤1, and each of the 7 large yellow bars is
worth ¤100.

A player’s income is the sum of the earning_ of initials_ that they own,
multiplied by their earning_power_. A player earns their income every
ten seconds of game time.

.. _earn money: {filename}/plugins/format/initial.rst#earning
.. _spend money: {filename}/plugins/format/object.rst#price
.. _earning: {filename}/plugins/format/initial.rst#earning
.. _earning_power: {filename}/plugins/format/level.rst#solo-players

Hue
~~~

A string_ specifying a hue, such as “purple”. A hue may be combined with
a shade (like “dark” or “very light”) to get a specific color_ (“dark
purple” or “very light purple”). There are sixteen hues in Antares:

.. role:: gray(literal)
   :class: gray
.. |gray| replace:: :gray:`"gray"`
.. role:: orange(literal)
   :class: orange
.. |orange| replace:: :orange:`"orange"`
.. role:: yellow(literal)
   :class: yellow
.. |yellow| replace:: :yellow:`"yellow"`
.. role:: blue(literal)
   :class: blue
.. |blue| replace:: :blue:`"blue"`
.. role:: green(literal)
   :class: green
.. |green| replace:: :green:`"green"`
.. role:: purple(literal)
   :class: purple
.. |purple| replace:: :purple:`"purple"`
.. role:: indigo(literal)
   :class: indigo
.. |indigo| replace:: :indigo:`"indigo"`
.. role:: salmon(literal)
   :class: salmon
.. |salmon| replace:: :salmon:`"salmon"`
.. role:: gold(literal)
   :class: gold
.. |gold| replace:: :gold:`"gold"`
.. role:: aqua(literal)
   :class: aqua
.. |aqua| replace:: :aqua:`"aqua"`
.. role:: pink(literal)
   :class: pink
.. |pink| replace:: :pink:`"pink"`
.. role:: pale-green(literal)
   :class: pale-green
.. |pale-green| replace:: :pale-green:`"pale-green"`
.. role:: pale-purple(literal)
   :class: pale-purple
.. |pale-purple| replace:: :pale-purple:`"pale-purple"`
.. role:: sky-blue(literal)
   :class: sky-blue
.. |sky-blue| replace:: :sky-blue:`"sky-blue"`
.. role:: tan(literal)
   :class: tan
.. |tan| replace:: :tan:`"tan"`
.. role:: red(literal)
   :class: red
.. |red| replace:: :red:`"red"`

+---------------+---------------+---------------+---------------+
| Antares hues                                                  |
+===============+===============+===============+===============+
| |gray|        | |orange|      | |yellow|      | |blue|        |
+---------------+---------------+---------------+---------------+
| |green|       | |purple|      | |indigo|      | |salmon|      |
+---------------+---------------+---------------+---------------+
| |gold|        | |aqua|        | |pink|        | |pale-green|  |
+---------------+---------------+---------------+---------------+
| |pale-purple| | |sky-blue|    | |tan|         | |red|         |
+---------------+---------------+---------------+---------------+

Color
~~~~~

A specific color. There are three ways to specify a color:

*  As a string_ (black, white, or clear).

*  As a map_ with ``r`` (red), ``g`` (green), and ``b`` (blue)
   components, plus optionally an ``a`` (alpha) component, all ranging
   from 0 to 255.

*  As a map_ with a hue_ key and a shade ranging from 0 to 255.

The following are all valid colors:

.. include:: pn/types-color.pn
   :code: procyon

Tags
~~~~

A map_ of booleans_. This is used to mark different kinds of objects. An
object has any tags mapped to ``true``, and does not have any tags
mapped to ``false`` or ``null``. The following are all valid tag maps:

.. include:: pn/types-tags.pn
   :code: procyon

Any string can be used, but these are the tags used in the `factory
scenario`_:

*  ``asteroid``: for regular asteroids (not the big green ones)
*  ``boarder``: for EVATs
*  ``disabled``: for CTF moors, after a jailbreak
*  ``energizable``: for anything an energy blob can provide energy to
*  ``engineer``: for engineering pods
*  ``flak``: for flak drones
*  ``jumpgate``: for the Jumpgate in `Yo Ho Ho`
*  ``miner``: for astrominers
*  ``normal``: for most objects
*  ``normal-attacker``: for most objects
*  ``planet``: for planets and moons
*  ``prisoner``: for Obiards in `Shoplifter 1`
*  ``reactivator``: for CTF moors, after a jailbreak
*  ``rendezvous``: for target locations, like shipyards or the UNS Ares
*  ``rescue``: for rescue ships in `Shoplifter 1` and `Shoplifter 2`
*  ``station``: for space stations, like Bunker Stations and Outposts

Matching
````````

An `object’s tags`_ list the tags that it has. An object has all tags
mapped to true, and lacks tags mapped to false (or mapped to null, or
not listed).

In other contexts, a tags map is a filter on an object’s tags. An object
matches if it has all tags that the filter maps to true, and lacks all
tags that the filter maps to false.

.. _object’s tags: {filename}/plugins/format/object.rst#tags

Tag matching is used so that some things happen only under certain
conditions. For example:

*  Asteroids are only engaged by astrominers, because astrominers
   specify ``tags: {miner: true}`` and asteroids specify ``engaged:
   {if: {tags: {miner: true}}}``.
*  Transports only land on planets, because planets specify ``tags:
   {planet: true}`` and transports’ arrive actions specify ``if:
   {planet: true}``.
*  Obish prisoners only attempt to board the Obish transport, because
   the Obish transport specifies ``tags: {rescue: true}`` and the
   prisoners specify ``engages: {if: {tags: {rescue: true}}}``.

Name
~~~~

A string_ naming a resource (level_, object_, race_, picture_, sprite_,
sound_, or music_ track). Names don’t include the top-level directory or
extension, so if ``sfx/explosion/large`` is the name of an object, then
Antares will look for an object at ``objects/sfx/explosion/large.pn``.
If it is the name of a sound, then Antares will look for a sound at
``pictures/sfx/explosion/large.aiff``.

Antares first searches the current plugin for the named resource. If the
plugin does not contain it, then it looks in the `factory scenario`_.

Index
~~~~~

An integer_ naming a condition_, initial_, or player_ in the current
level_. The first entry is numbered 0, so if ``3`` is the index of an
initial, then it refers to the fourth initial in the current level.

.. _player: {filename}/plugins/format/level.rst#solo-players

Object Reference
~~~~~~~~~~~~~~~~

A map_ referencing an in-game object. It contains any *one* of the
following fields:

.. table::
   :widths: auto

   ====================  ========================================
   Field                 Type
   ====================  ========================================
   initial               index_ of an initial_
   flagship              index_ of a player
   control               index_ of a player
   target                index_ of a player
   ====================  ========================================

The following are all valid object references:

.. include:: pn/types-object-reference.pn
   :code: procyon

URL
~~~

A string_ containing a fully-specified URL. Generally, the URL scheme
should be ``https`` (preferred) or ``http``. URLs with other schemes may
be ignored. The following are all valid URLs:

.. include:: pn/types-url.pn
   :code: procyon

.. include:: epilog.rsti
.. -*- tab-width: 3; indent-tabs-mode: nil; fill-column: 72 -*-
