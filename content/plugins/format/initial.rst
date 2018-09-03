Initial
=======

.. sectnum::

An initial is an object created by the level_. Initials form the
starting setup of the level, and are used by conditions_ to script
additional events after gameplay starts.

`Example initial <https://github.com/arescentral/antares-data/blob/master/levels/ch01.pn#L52-L56>`_

.. contents::
   :local:
   :backlinks: none

Definition
----------

An initial is a procyon_ value with the following fields:

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   base_                 yes   remapped name_ of an object_
   owner_                no    index_ of a player
   at_                   yes   point_
   hide_                 no    boolean_
   flagship_             no    boolean_
   target.initial_       no    index_ of an initial
   target.lock_          no    boolean_
   override.name_        no    string_
   override.sprite_      no    name_ of a sprite_
   earning_              no    money_
   build_                no    array_ of remapped names_ of objects_
   ====================  ====  ========================================

base
~~~~

What kind of object_ this is. Before creating the object, Antares first
attempts to map the name through its owner_’s race.

*  If ``race/base`` exists, that name is used.
*  If not, ``base`` is used as-is.

This feature is used in `net levels`_. If an initial specifies ``base:
"hvd"``, and the player chooses to play |ish-pl|_ (``ish``), then it
will be an Ishiman heavy destroyer (``ish/hvd``). If the player chooses
|can-pl|_ (``can``), then it will be a Cantharan heavy destroyer
(``can/hvd``). The net level must not allow the player to choose
|ele-pl|_, as no object named ``ele/hvd`` or ``hvd`` exists.

In `solo levels`_, player races are fixed, so it’s recommended (but not
required) to use ``base: "ish/hvd"`` or ``base: "can/hvd"`` for clarity.

.. _net levels: {filename}/plugins/format/level.rst#net
.. _solo levels: {filename}/plugins/format/level.rst#solo

owner
~~~~~

The index_ of the player that initially owns the object. If null, the
object is neutral.

at
~~

The point_ at which to create the object. Most levels are randomly
rotated, and the level’s rotation is applied to this location.

hide
~~~~

If ``true``, then the object won’t be created at the beginning of the
level. It can be explicitly created later by the `reveal action`_.

.. _reveal action: {filename}/plugins/format/action.rst#reveal

flagship
~~~~~~~~

If ``true``, then this object is its owner_’s flagship. Every human
player must have exactly one flagship. Non-human players should not have
a flagship.

target.initial
~~~~~~~~~~~~~~

The index_ of another initial for this object to target. A player can
later reassign this object’s target, unless target.lock_ is ``true``.

target.lock
~~~~~~~~~~~

If ``true``, then it is not possible for a player to order this object
to a new target. This should typically be used with target.initial_.
Together, they lock the object into guard or escort duty.

The object’s target can still be changed by the `target action`_ or
`hold action`_.

.. _hold action: {filename}/plugins/format/action.rst#hold
.. _target action: {filename}/plugins/format/action.rst#target

override.name
~~~~~~~~~~~~~

A replacement name for the object. Most planets and stations have their
names overridden, so that the player can easily tell them apart. Typical
names from the `factory scenario`_ would be:

.. table::
   :widths: auto

   =========  ==========================================
   Object     Name
   =========  ==========================================
   |sun|      Regulus
   |planet|   Regulus Alpha, Regulus Beta, Regulus Gamma
   |moon|     Regulus Alpha 1, Regulus Alpha 2
   |bunker|   Bunker Station 1, Bunker Station 2
   |power|    Power Station R-1, Power Station R-2
   |outpost|  Outpost 1, Outpost 2, Outpost 3
   =========  ==========================================

Names should be at most 25 characters. Longer names won’t fit in the
computer.

override.sprite
~~~~~~~~~~~~~~~

A replacement sprite_ for the object. Most planets and moons have their
sprites overridden.

.. warning:: The override sprite must have the same number of frames as
   the original sprite.

There are a large number of override sprites available for planets and
moons:

*  `loc/planets/aqua-minerale <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/aqua-minerale/image.png>`_
*  `loc/planets/bahamas <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/bahamas/image.png>`_
*  `loc/planets/bluegas <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/bluegas/image.png>`_
*  `loc/planets/blueyellow-marble <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/blueyellow-marble/image.png>`_
*  `loc/planets/brightgas <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/brightgas/image.png>`_
*  `loc/planets/bruised <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/bruised/image.png>`_
*  `loc/planets/calmpurple <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/calmpurple/image.png>`_
*  `loc/planets/clay <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/clay/image.png>`_
*  `loc/planets/cloudtones <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/cloudtones/image.png>`_
*  `loc/planets/dirtcloud <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/dirtcloud/image.png>`_
*  `loc/planets/earth <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/earth/image.png>`_
*  `loc/planets/fall <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/fall/image.png>`_
*  `loc/planets/goldtone <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/goldtone/image.png>`_
*  `loc/planets/graysplotch <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/graysplotch/image.png>`_
*  `loc/planets/jungle <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/jungle/image.png>`_
*  `loc/planets/lava <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/lava/image.png>`_
*  `loc/planets/marble-streakedpurple <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/marble-streakedpurple/image.png>`_
*  `loc/planets/marshmellow <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/marshmellow/image.png>`_
*  `loc/planets/marslike <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/marslike/image.png>`_
*  `loc/planets/moldymud <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/moldymud/image.png>`_
*  `loc/planets/nastyswirl <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/nastyswirl/image.png>`_
*  `loc/planets/purple-stripes-ugly <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/purple-stripes-ugly/image.png>`_
*  `loc/planets/purpleblue <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/purpleblue/image.png>`_
*  `loc/planets/purplegas <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/purplegas/image.png>`_
*  `loc/planets/purpleyellow-trouble <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/purpleyellow-trouble/image.png>`_
*  `loc/planets/purtygas <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/purtygas/image.png>`_
*  `loc/planets/redwhite-excitement <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/redwhite-excitement/image.png>`_
*  `loc/planets/sandyred <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/sandyred/image.png>`_
*  `loc/planets/saturny <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/saturny/image.png>`_
*  `loc/planets/splatterpaint-pink <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/splatterpaint-pink/image.png>`_
*  `loc/planets/sta-puft <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/sta-puft/image.png>`_
*  `loc/planets/tiedye-lava <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/tiedye-lava/image.png>`_
*  `loc/planets/uglypaint <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/uglypaint/image.png>`_
*  `loc/planets/yellow-cookie <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/yellow-cookie/image.png>`_
*  `loc/planets/yellow <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/yellow/image.png>`_
*  `loc/planets/yerrear <https://github.com/arescentral/antares-data/tree/master/sprites/loc/planets/yerrear/image.png>`_ 

earning
~~~~~~~

How much money_ a player earns for owning this object. This value is
multiplied by a player’s earning_power_. The initial pays out the
resulting amount of money over the course of every ten seconds.

Typical values from the `factory scenario`_ are:

.. table::
   :widths: auto

   ==============  =======
   Object          earning
   ==============  =======
   Planet          ¤1.0
   Moon            ¤1.0
   Bunker Station  ¤1.0
   Minor Bunker    ¤0.75
   Power Station   ¤1.0
   Outpost         ¤0.5
   Minor Outpost   ¤0.25
   ==============  =======

.. _earning_power: {filename}/plugins/format/level.rst#solo-players

build
~~~~~

An array_ of objects_ that can be built at this object. Up to six
entries can be listed.

When determining what objects an initial can build, Antares first maps
each entry ``base`` according to the initial’s owner’s race_:

*  If ``race/base`` exists, that name is used.
*  If not, and ``base`` exists, that name is used.
*  Otherwise, the entry is ignored.

For example, imagine a level has |ish-adj|_, (``ish``), |can-adj|_
(``can``), and |uns-adj|_ (``uns``) players, and Earth’s build array is:

.. include:: pn/initial-build.pn
   :code: procyon

In this case:

*  All players can build their respective cruisers on Earth, because
   ``ish/cruiser``, ``can/cruiser``, and ``uns/cruiser`` all exist.
*  The |ish-pl| and |can-pl| can build their respective heavy cruisers, but
   not the |uns-pl|. There is no object named ``uns/hvc`` or ``hvc``.
*  All players can build |can-adj| defense drones, even the |ish-pl|.
   Antares checks for ``ish/can/defdrone`` and ``can/defdrone``, but not
   ``ish/defdrone``. 
*  No players can build |gro-adj| gateships. ``gro/gateship`` doesn’t
   exist, nor anything like it.

.. _ships: {filename}/plugins/format/race.rst#ships

.. include:: epilog.rsti
.. -*- tab-width: 3; indent-tabs-mode: nil; fill-column: 72 -*-
