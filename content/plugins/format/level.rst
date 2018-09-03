Level
=====

.. sectnum::

A level describes the starting conditions and objectives for a single
mission. It can be a solo_ level, in which a human player attempts to
beat a CPU player, or a net_ level, where two human players go
head-to-head.

`Example level <https://github.com/arescentral/antares-data/blob/master/levels/ch01.pn>`_

.. contents::
   :local:
   :backlinks: none

Do I need it?
-------------

Yes. A plugin with no levels won’t have anything to play. A plugin can
be all solo_ levels, all net_ levels, or a mixture.

Naming
------

Levels are in the ``levels`` directory and have a ``.pn`` extension.

The recommended convention for naming levels is:

*  For chapters of a campaign, name them ``chNN`` (``ch01``, ``ch02``,
   etc.) according to their chapter number.
*  For net levels, name them ``netN`` (``net1``, ``net2``, etc.)
   according to their selection order.
*  For tutorials, name them ``tutN`` (``tut1``, ``tut2``, etc.)
   according to the order they are played.
*  For anything else, use a four-character code. In the `factory
   scenario`_, for example, the secret level |srtm|_ is named ``srtm``.

Definition
----------

A level is a procyon_ file with the following fields, plus any fields
appropriate to its type_:

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   type_                 yes   “solo_”, “net_”, or “demo_”
   chapter_              no    integer_
   title_                yes   string_
   initial_              no    array_ of initials_
   conditions_           no    array_ of conditions_
   briefings_            no    array_ of briefings_
   starmap_              no    rect_
   song_                 no    name_ of a music_ track
   status_               no    array_ of `status lines`_
   start_time_           no    duration_
   angle_                no    angle_
   ====================  ====  ========================================

chapter
~~~~~~~

Determines the order that the level appears in on the “Select Level”
screen. If null, the level won’t appear at all. All chapter numbers must
be unique. If the plugin has solo levels, then there must be a chapter
1, which is initially unlocked.

Chapter numbers are also used by the unlocking level cheat. On the
“Select Level” screen, type ``*03`` to unlock the level with chapter
number 3 (the number of digits must match the highest-numbered level in
the plugin).

title
~~~~~

The title of the level. Level titles are normally two lines. Solo_ level
titles normally look like this::

   \i Chapter 1
   \iIn Case of Emergency, Break Glass

Net_ level titles normally look like this::

   \i Sundown Showdown
   \i

Note the space after the ``\i`` in the first line. The ``\i`` tells
Antares to invert the text’s foreground and background (and back again
in the second line).

starmap
~~~~~~~

A rect to highlight on the `plugin’s starmap`_ during mission briefings.
In the `factory scenario`_, these rects are 32×24, but any size
appropriate to the plugin’s starmap can be used.

If null, the starmap page in the mission briefing will be skipped.

.. _plugin’s starmap: {filename}/plugins/format/picture.rst#starmap

song
~~~~

The name_ of a music_ track to play during the level. Any of the
following is appropriate:

*  ``"targetron"`` (`Targetron <https://youtu.be/f-1F1lrdJjc>`_)
*  ``"getalong"`` (`Getalong <https://youtu.be/jff2VBTARQA>`_)
*  ``"technobee"`` (`Technobee <https://youtu.be/x67xj-LsMac>`_)
*  ``"eyes-of-fire"`` (`Eyes of Fire <https://youtu.be/9_3b7fJKTow>`_)
*  ``"yesterday"`` (`Yesterday (The Doodly-Do Song)
   <https://youtu.be/5l1zZx0SYmc>`_)

.. _status lines:

status
~~~~~~

An array_ of status lines. Status lines are shown in the “Mission
Status” screen of the computer. There are three general kinds of status
lines:

*  `Plain text`_
*  `Conditional text`_
*  `Counters`_

Any of the three types of status lines can include ``underline: true``
to underline that line.

The computer screen is 25 characters wide. Status lines that exceed this
length will be truncated before display.

Plain text
``````````

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   text                  yes   string_
   underline             no    boolean_
   ====================  ====  ========================================

Displays ``text`` verbatim, optionally with an underline.

For example, the following status lines:

.. include:: pn/level-status-text.pn
   :code: procyon

will display unconditionally as::

   Capture Vulpecula Beta
    and Gamma

Conditional text
````````````````

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   prefix                no    string_
   condition             yes   index_ of a condition_
   true                  no    string_
   false                 no    string_
   suffix                no    string_
   underline             no    boolean_
   ====================  ====  ========================================

If the condition_ numbered ``condition`` has triggered, displays the
``true`` string_, otherwise the ``false`` string_. In either case, the
text is preceded by ``prefix``, followed by ``suffix``, and optionally
underlined.

``condition`` must not reference a persistent_ condition. Any of
``true``, ``false``, ``prefix``, or ``suffix`` may be null. If null,
they are assumed to be empty.

.. _persistent: {filename}/plugins/format/condition.rst#persistent

For example, the following status line watches condition 0:

.. include:: pn/level-status-condition.pn
   :code: procyon

Before condition 0 triggers, it displays as::

   Battleship destroyed: N

After condition 0 triggers, it displays as::

   Battleship destroyed: Y

Counters
````````

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   prefix                no    string_
   minuend               no    number_
   counter               yes   counter_
   fixed                 no    boolean_
   suffix                no    string_
   underline             no    boolean_
   ====================  ====  ========================================

Displays a player’s numbered ``counter``. The text is preceded by
``prefix``, followed by ``suffix``, and optionally underlined.

If ``fixed`` is true, divides the counter by 256 and displays it as a
fractional value. If ``minuend`` is non-null, subtracts the counter from
the minuend before displaying it.

For example, the following status lines watches the counters of the two
players:

.. include:: pn/level-status-counter.pn
   :code: procyon

If the counters count each player’s kills, and the first player has two
kills and the second none, this displays as::

   Player 1: 3 lives
   Player 2: 1 lives

start_time
~~~~~~~~~~

Specifies a duration_ of time to run the level before before gameplay
starts. In the `factory scenario`_, this is typically used together with
an asteroid generator. The level generates asteroids for a couple of
minutes, so that when the player starts playing the level, it is filled
with a random asteroid field.

Objects can still move before gameplay starts, and cpu players can act.
For this reason, in levels with a ``start_time``, it’s best to keep
ships initially hidden_, and planets initially without an owner_. A
`time condition`_ can reveal_ the ships and capture_ the planets just
prior to the start of gameplay (``duration: "-0.1s"``).

.. _owner: {filename}/plugins/format/initial.rst#owner
.. _hidden: {filename}/plugins/format/initial.rst#hide
.. _time condition: {filename}/plugins/format/condition.rst#time
.. _reveal: {filename}/plugins/format/action.rst#reveal
.. _capture: {filename}/plugins/format/action.rst#capture

angle
~~~~~

Specifies an angle_ to rotate the map to. Normally, this is either 0 (no
rotation) or null (random rotation).

.. _type:

Types
-----

.. _solo:

solo
~~~~

Solo levels have a single human player who (usually) plays against a
CPU player.

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   players__             yes   array_ of `solo players`_
   par_                  yes   par_
   skip_                 no    name_ of a level_
   no_ships_             no    string_
   prologue_             no    string_
   epilogue_             no    string_
   ====================  ====  ========================================

__
.. _solo players:

players
```````

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   type                  yes   “human” or “cpu”
   name                  yes   string_
   race                  yes   name_ of a race_
   hue                   no    hue_
   earning_power         no    number_
   ====================  ====  ========================================

In a solo level, the first player must be ``type: "human"`` and all
other players must be ``type: "cpu"``.

``name`` is used in messages about changes of ownership.

``race`` determines the ships available to the player, as described in
the documentation for initials_’ base_ and build_ fields.

If ``hue`` is non-null, ships owned by the player will be recolored
accordingly. This makes it possible to distinguish two players if they
have the same ``race``.

``earning_power`` is a multiplier on the earning_ values of initials_
that a player owns, as well as the money_ paid out to all players at the
start of the level (normally ¤25). If null, the player earns no cash.

`Example solo player <https://github.com/arescentral/antares-data/blob/master/levels/ch01.pn#L7-L10>`_

.. _base: {filename}/plugins/format/initial.rst#base
.. _build: {filename}/plugins/format/initial.rst#build
.. _earning: {filename}/plugins/format/initial.rst#build

par
```

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   time                  yes   duration_
   kills                 yes   integer_
   losses                yes   integer_
   ====================  ====  ========================================

Sets target values for completing a level well. At the end of the level,
100 points are awarded to players that meet par, and points may be
doubled for even better performance. Points for par are awarded as in
the following proportions:

*  50 points for ``time``
*  20 points for ``kills``
*  30 points for ``losses``

For ``time`` and ``losses``, additional points may be awarded if under
par, up to 2× for ½ par, and points may be deducted if over, down to 0
points for 2× par.

For ``kills``, additional points may be awarded if over par, up to 2×
for 2× par, and points may be deducted if under, down to 0 points for ½
par.

.. note:: if ``losses`` is 0, then it’s impossible to get fewer losses
   than par, so the maximum score is 170.

`Example par <https://github.com/arescentral/antares-data/blob/master/levels/ch01.pn#L160-L163>`_

skip
````

If provided, the player may press ``ESC`` during the game and skip the
level. The level named ``skip`` will be unlocked, and play will continue
with that level. Mainly used for tutorials, where victory is not
important, and the player may want to skip to a real level.

no_ships
````````

If a human player loses all of their ships, they lose the level. This is
the message that will be displayed if that happens.

.. _prologue:
.. _epilogue:

prologue, epilogue
``````````````````

A text crawl that will be displayed before playing the level
(``prologue``) or after winning the level (``epilogue``). There are
special codes supported for controlling formatting and displaying
images:

.. table::
   :widths: auto

   ======================  ==============================================
   Example                 Meaning
   ======================  ==============================================
   ``\\``                  Display a single backslash.
   ``\t``                  Tab to the middle of the screen.
   ``\r``                  Restore original foreground and background
                           colors.
   ``\i Inverted \i``      Swap foreground and background colors.
   ``\f8eIn yellow\r``     Set the foreground color to $8e from the
                           `Ares CLUT`_.
   ``\b8eOn yellow\r``     Set the background color to $8e from the
                           `Ares CLUT`_.
   ``#+``                  Start a new line and reset foreground and
                           background colors.
   ``#+gai/race``          Display the picture_ with name ``gai/race``
                           in the foreground.
   ``#+Blog/starfield/a``  From here on, use the picture_ with name_
                           ``log/starfield/a`` as the background.
   ======================  ==============================================

.. _Ares CLUT: {filename}/plugins/format/types.rst#color

net
~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   players__             yes   array_ of `net players`_
   description_          no    string_
   own_no_ships_         no    string_
   foe_no_ships_         no    string_
   ====================  ====  ========================================

.. _net players:
__

players
```````

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   type                  yes   “human” or “cpu”
   races                 yes   array_ of names_ of races_
   earning_power         no    number_
   ====================  ====  ========================================

In a net level, at least two players must be ``type: "human"``.
Additional players may be ``type: "cpu"``.

``race`` lists the races that a player may select in the level. The
races will be offered in the given order, with the first option selected
by default.

``earning_power`` is a multiplier on the earning_ values of initials_
that a player owns. If null, the player earns no cash.

Net players have names and possibly hues, but these are determined by
the players. Players choose their own names freely, and, if multiple
players choose the same race, their hues as well.

`Example net player <https://github.com/arescentral/antares-data/blob/master/levels/net1.pn#L6-L14>`_

description
```````````

A description of the level, used during level selection in a net game.

.. _own_no_ships:
.. _foe_no_ships:

own_no_ships, foe_no_ships
``````````````````````````

If a human player loses all of their ships, they lose the level. These
are the messages that will be displayed if that happens to them
(``own_no_ships``) or their opponent (``foe_no_ships``).

demo
~~~~

Demo levels are not properly supported yet. They have no human players,
so they demonstrate CPU players playing against each other.

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   players__             yes   array_ of `demo players`_
   ====================  ====  ========================================

.. _demo players:
__

players
```````

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   name                  yes   string_
   race                  yes   name_ of a race_
   hue                   no    hue_
   earning_power         no    number_
   ====================  ====  ========================================

The same fields as `solo players`_ are used, minus ``type``, as demo
players are always cpu players.

.. include:: epilog.rsti
.. -*- tab-width: 3; indent-tabs-mode: nil; fill-column: 72 -*-
