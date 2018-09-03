Race
====

.. sectnum::

A race defines the attributes of a player faction, most importantly the
available set of ships. In `solo levels`_, players are assigned a race
directly. In `net levels`_, players can choose a race.

Ships are made available according to the race’s name, as described in
the documentation for initials_’ base_ and build_ fields.

`Example <https://github.com/arescentral/antares-data/blob/master/races/ish.pn>`_

.. _solo levels: {filename}/plugins/format/level.rst#solo
.. _net levels: {filename}/plugins/format/level.rst#net
.. _base: {filename}/plugins/format/initial.rst#base
.. _build: {filename}/plugins/format/initial.rst#build

.. contents::
   :local:
   :backlinks: none

Do I need it?
-------------

Maybe.

If your plugin adds a new race, you’ll obviously need to define it. If
not, and your plugin just uses existing races, you don’t need to define
any.

Naming
------

Races are in the ``races`` directory and have a ``.pn`` extension.

The recommended convention for races is to name them with a three-letter
code related to their name. In the `factory scenario`_, the ten defined
races are:

*  ``ish`` (|ish-pl|_)
*  ``can`` (|can-pl|_)
*  ``gai`` (|gai-pl|_)
*  ``obi`` (|obi-pl|_)
*  ``baz`` (|baz-pl|_)
*  ``sal`` (|sal-pl|_)
*  ``aud`` (|aud-pl|_)
*  ``ele`` (|ele-pl|_)
*  ``uns`` (|uns-pl|_/United Nations of Sol)
*  ``gro`` (|gro-pl|_)

Definition
----------

A race is a procyon_ file with the following fields:

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   numeric_              yes   ignored
   adjective_            yes   string_
   plural_               yes   string_
   military_             yes   string_
   homeworld_            yes   string_
   hue_                  yes   hue_
   not_hue_              no    array_ of hues_
   advantage_            yes   string_
   ====================  ====  ========================================

numeric
~~~~~~~

A historical value, not used by Antares. Ares identified races by number
(e.g. ``100`` for |ish-pl|_ and ``200`` for |can-pl|_), but Antares
references races by name (e.g. ``ish`` for |ish-pl| and ``can`` for
|can-pl|).

.. _adjective:
.. _plural:
.. _military:
.. _homeworld:

adjective, plural, military, homeworld
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Descriptive strings_ for a race. ``adjective`` is used when selecting a
race in a net game. The other three strings are only informational, and
not used anywhere in Antares.

.. _hue_field:
.. _not_hue:

hue, not_hue
~~~~~~~~~~~~

Hues_ describing the color of a race’s ships.

``hue`` is the main color of the ships. When selecting an alternate
color in a net game, ``hue`` is the default choice, and ships won’t be
recolored if they match the player.

When selecting an alternate color in a net game, ``not_hue`` lists other
colors which shouldn’t be allowed because they are too similar to
``hue``.

advantage
~~~~~~~~~

A number_ describing the relative strength of this race’s ships. In the
`factory scenario`_, the |gai-pl| are 1.0, the |can-pl| are 2.0, and the
|ele-pl| are 3.0.

.. include:: epilog.rsti
.. -*- tab-width: 3; indent-tabs-mode: nil; fill-column: 72 -*-
