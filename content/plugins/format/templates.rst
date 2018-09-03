Templates
=========

.. sectnum::

Creating new objects_ from scratch is complicated, but using an existing
template is simple. The `factory scenario`_ includes many templates to
make it easier to create new objects.

.. contents::
   :local:
   :backlinks: none

Ships
-----

Ships fall into three broad categories:

.. table::
   :widths: auto

   ================  ========  =================
   Name              Shape     Examples
   ================  ========  =================
   `tpl/warship`_    Triangle  `tpl/fighter`_,
                               `tpl/cruiser`_,
                               `tpl/schooner`_,
                               `tpl/hvc`_,
                               `tpl/gunship`_,
                               `tpl/hvd`_,
                               `tpl/defdrone`_
   `tpl/capship`_    Diamond   `tpl/carrier`_
   `tpl/utilship`_   Plus      `tpl/transport`_,
                               `tpl/engineer`_,
                               `tpl/aslttran`_
   ================  ========  =================

.. _tpl/warship: https://github.com/arescentral/antares-data/blob/master/objects/tpl/fighter.pn
.. _tpl/capship: https://github.com/arescentral/antares-data/blob/master/objects/tpl/capship.pn
.. _tpl/utilship: https://github.com/arescentral/antares-data/blob/master/objects/tpl/utilship.pn

And most ships come from a standard ship class:

.. table::
   :widths: auto

   ===  ================  ====  ====  ====  ====  =====  ==========  ======  ======  ================
   Cls  Name              turn  vel   warp  mass  price  build time  energy  health  Example
   ===  ================  ====  ====  ====  ====  =====  ==========  ======  ======  ================
   1    `tpl/fighter`_    3.0   6.0   no    0.8   ¤3.0   3s          100     600     `ish/fighter`_
   3    `tpl/cruiser`_    2.0   5.0   yes   1.0   ¤5.0   5s          1000    1000    `ish/cruiser`_
   3    `tpl/schooner`_   3.0   7.0   yes   1.0   ¤5.0   5s          750     1000    `ish/schooner`_
   3    `tpl/hvc`_        2.0   5.0   yes   1.0   ¤7.5   7.5s        1000    1000    `ish/hvc`_
   5    `tpl/gunship`_    1.2   4.0   yes   1.2   ¤11.0  10s         3000    2000    `ish/gunship`_
   7    `tpl/hvd`_        2.0   4.5   yes   1.45  ¤32.5  32.5s       2000    2000    `ish/hvd`_
   9    `tpl/defdrone`_   5.0   0.35  no    1.0   ¤5.0   5s          1500    1000    `ish/defdrone`_
   7    `tpl/carrier`_    1.0   3.0   yes   2.0   ¤22.5  30s         5000    5000    `ish/carrier`_
   9    `tpl/transport`_  2.0   3.0   no    1.1   ¤4.0   11s         250     1000    `ish/transport`_
   9    `tpl/engineer`_   2.0   3.0   no    1.1   ¤4.0   11s         800     200     `ish/engineer`_
   9    `tpl/aslttran`_   2.0   3.0   no    1.1   ¤10.0  11s         1200    800     `ish/aslttran`_
   ===  ================  ====  ====  ====  ====  =====  ==========  ======  ======  ================

.. _tpl/fighter: https://github.com/arescentral/antares-data/blob/master/objects/tpl/fighter.pn
.. _tpl/cruiser: https://github.com/arescentral/antares-data/blob/master/objects/tpl/cruiser.pn
.. _tpl/schooner: https://github.com/arescentral/antares-data/blob/master/objects/tpl/schooner.pn
.. _tpl/hvc: https://github.com/arescentral/antares-data/blob/master/objects/tpl/hvc.pn
.. _tpl/gunship: https://github.com/arescentral/antares-data/blob/master/objects/tpl/gunship.pn
.. _tpl/hvd: https://github.com/arescentral/antares-data/blob/master/objects/tpl/hvd.pn
.. _tpl/defdrone: https://github.com/arescentral/antares-data/blob/master/objects/tpl/defdrone.pn
.. _tpl/carrier: https://github.com/arescentral/antares-data/blob/master/objects/tpl/carrier.pn
.. _tpl/transport: https://github.com/arescentral/antares-data/blob/master/objects/tpl/transport.pn
.. _tpl/engineer: https://github.com/arescentral/antares-data/blob/master/objects/tpl/engineer.pn
.. _tpl/aslttran: https://github.com/arescentral/antares-data/blob/master/objects/tpl/aslttran.pn

.. _ish/fighter: https://github.com/arescentral/antares-data/blob/master/objects/ish/fighter.pn
.. _ish/cruiser: https://github.com/arescentral/antares-data/blob/master/objects/ish/cruiser.pn
.. _ish/schooner: https://github.com/arescentral/antares-data/blob/master/objects/ish/schooner.pn
.. _ish/hvc: https://github.com/arescentral/antares-data/blob/master/objects/ish/hvc.pn
.. _ish/gunship: https://github.com/arescentral/antares-data/blob/master/objects/ish/gunship.pn
.. _ish/hvd: https://github.com/arescentral/antares-data/blob/master/objects/ish/hvd.pn
.. _ish/defdrone: https://github.com/arescentral/antares-data/blob/master/objects/ish/defdrone.pn
.. _ish/carrier: https://github.com/arescentral/antares-data/blob/master/objects/ish/carrier.pn
.. _ish/transport: https://github.com/arescentral/antares-data/blob/master/objects/ish/transport.pn
.. _ish/engineer: https://github.com/arescentral/antares-data/blob/master/objects/ish/engineer.pn
.. _ish/aslttran: https://github.com/arescentral/antares-data/blob/master/objects/ish/aslttran.pn

To declare a new ship, start with the ``template`` line. At a minimum,
new ships should set rotation.sprite_, rotation.frames_, weapons_,
and shield_color_. They should also have a portrait_, if possible:

.. _rotation.sprite: {filename}/plugins/format/object.rst#rotation
.. _rotation.frames: {filename}/plugins/format/object.rst#rotation
.. _weapons: {filename}/plugins/format/object.rst#weapons
.. _shield_color: {filename}/plugins/format/object.rst#shield-color
.. _portrait: {filename}/plugins/format/object.rst#portrait

.. include:: pn/template-ship.pn
   :code: procyon

Depending on how powerful a race is, it might also make sense to
override health_, energy_, turn_rate_, max_velocity_, warp_speed_, or
other default values.

.. _health: {filename}/plugins/format/object.rst#health
.. _energy: {filename}/plugins/format/object.rst#energy
.. _turn_rate: {filename}/plugins/format/object.rst#turn-rate
.. _max_velocity: {filename}/plugins/format/object.rst#max-velocity
.. _warp_speed: {filename}/plugins/format/object.rst#warp-speed

Projectiles
-----------

.. table::
   :widths: auto

   ===============  ==========  ==========================================
   Name             Appearance  Examples
   ===============  ==========  ==========================================
   `tpl/anipulse`_  animation_  `dev/fullerene/pulse`_, `sfx/energy`_
   `tpl/rotpulse`_  rotation_   `dev/fusion/pulse`_
   `tpl/missile`_   rotation_   `dev/cm/missile`_, `dev/amissile/missile`_
   `tpl/ray`_       ray_        `dev/tspace/beam`_, `dev/trazer/beam`_
   `tpl/bolt`_      bolt_       `dev/pk/ish/beam`_, `dev/conc/pellet`_
   ===============  ==========  ==========================================

.. _animation: {filename}/plugins/format/object.rst#animation
.. _rotation: {filename}/plugins/format/object.rst#rotation
.. _ray: {filename}/plugins/format/object.rst#ray
.. _bolt: {filename}/plugins/format/object.rst#bolt

.. _tpl/anipulse: https://github.com/arescentral/antares-data/blob/master/objects/tpl/anipulse.pn
.. _dev/fullerene/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/fullerene/pulse.pn
.. _sfx/energy: https://github.com/arescentral/antares-data/blob/master/objects/sfx/energy.pn
.. _tpl/rotpulse: https://github.com/arescentral/antares-data/blob/master/objects/tpl/rotpulse.pn
.. _dev/fusion/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/fusion/pulse.pn
.. _tpl/missile: https://github.com/arescentral/antares-data/blob/master/objects/tpl/missile.pn
.. _dev/cm/missile: https://github.com/arescentral/antares-data/blob/master/objects/dev/cm/missile.pn
.. _dev/amissile/missile: https://github.com/arescentral/antares-data/blob/master/objects/dev/amissile/missile.pn
.. _tpl/ray: https://github.com/arescentral/antares-data/blob/master/objects/tpl/ray.pn
.. _dev/tspace/beam: https://github.com/arescentral/antares-data/blob/master/objects/dev/tspace/beam.pn
.. _dev/trazer/beam: https://github.com/arescentral/antares-data/blob/master/objects/dev/trazer/beam.pn
.. _tpl/bolt: https://github.com/arescentral/antares-data/blob/master/objects/tpl/bolt.pn
.. _dev/pk/ish/beam: https://github.com/arescentral/antares-data/blob/master/objects/dev/pk/ish/beam.pn
.. _dev/conc/pellet: https://github.com/arescentral/antares-data/blob/master/objects/dev/conc/pellet.pn

To declare a new projectile, start with the ``template`` line. The most
important fields for a projectile are its max_velocity_,
expire.after.age_, and collide.damage_. It’s also usually a good idea if
its collide.action_ removes_ itself after impact.

.. _expire.after.age: {filename}/plugins/format/object.rst#expire
.. _collide.damage: {filename}/plugins/format/object.rst#collide
.. _collide.action: {filename}/plugins/format/object.rst#collide
.. _removes: {filename}/plugins/format/action.rst#remove

Beyond those fields, a new projectile needs to have an appearance:

*  For ``tpl/anipulse``, new projectiles need animation.sprite_,
   animation.frames_, and animation.speed_ at a minimum.
*  For ``tpl/rotpulse`` and ``tpl/missile``, new projectiles need
   rotation.sprite_ and rotation.frames_.
*  For ``tpl/ray``, they need ray.to_, ray.hue_, and ray.range_.
*  For ``tpl/bolt``, they need bolt.color_.

.. _animation.sprite: {filename}/plugins/format/object.rst#animation
.. _animation.frames: {filename}/plugins/format/object.rst#animation
.. _animation.speed: {filename}/plugins/format/object.rst#animation
.. _ray.to: {filename}/plugins/format/object.rst#ray
.. _ray.hue: {filename}/plugins/format/object.rst#ray
.. _ray.range: {filename}/plugins/format/object.rst#ray
.. _bolt.color: {filename}/plugins/format/object.rst#bolt

.. _example projectile:

Here’s a basic definition for an animated pulse (``tpl/anipulse``):

.. include:: pn/template-pulse.pn
   :code: procyon

It’s usually good to play the fire sound as part of its create.action_,
so that the same sound will play for that projectile, no matter what
weapon is firing.

.. _create.action: {filename}/plugins/format/object.rst#create

Weapons
-------

Weapons are equipped by ships. There are four sub-categories of weapons.
Most of the differences between weapons are determined by their
`projectiles <#projectile>`_, so the sub-categories are mostly about how
CPU pilots handle the weapons.

*  Guns are used to attack enemies in front of a ship.
*  Turrets are used to attack enemies all around a ship.
*  Devices are used for defense or transportation, rather than attack.
*  Specials are never fired automatically by CPU pilots.

.. table::
   :widths: auto

   ==============  ===========================================
   Name            Examples
   ==============  ===========================================
   `tpl/gun`_      `dev/pk/ish/gun`_, `dev/fusion/rgun`_
   `tpl/turret`_   `dev/laser/turret`_, `dev/pp/twin`_
   `tpl/device`_   `dev/stealth/item`_, `dev/repulser/turret`_
   `tpl/special`_  `dev/assault/ish`_, `dev/assault/can`_
   ==============  ===========================================

.. _tpl/device: https://github.com/arescentral/antares-data/blob/master/objects/tpl/device.pn
.. _dev/stealth/item: https://github.com/arescentral/antares-data/blob/master/objects/dev/stealth/item.pn
.. _dev/repulser/turret: https://github.com/arescentral/antares-data/blob/master/objects/dev/repulser/turret.pn
.. _tpl/gun: https://github.com/arescentral/antares-data/blob/master/objects/tpl/gun.pn
.. _dev/pk/ish/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/pk/ish/gun.pn
.. _dev/fusion/rgun: https://github.com/arescentral/antares-data/blob/master/objects/dev/fusion/rgun.pn
.. _tpl/turret: https://github.com/arescentral/antares-data/blob/master/objects/tpl/turret.pn
.. _dev/laser/turret: https://github.com/arescentral/antares-data/blob/master/objects/dev/laser/turret.pn
.. _dev/pp/twin: https://github.com/arescentral/antares-data/blob/master/objects/dev/pp/twin.pn
.. _tpl/special: https://github.com/arescentral/antares-data/blob/master/objects/tpl/special.pn
.. _dev/assault/ish: https://github.com/arescentral/antares-data/blob/master/objects/dev/assault/ish.pn
.. _dev/assault/can: https://github.com/arescentral/antares-data/blob/master/objects/dev/assault/can.pn

When creating a weapon, the important things to declare are the name,
device_ fields, and activate.action_:

.. include:: pn/template-weapon.pn
   :code: procyon

Note how some of the values have been copied from the `example
projectile`_ above:

*  The weapon’s device.speed_ is equal to the projectile’s
   max_velocity_.
*  The weapon’s device.range_ is equal to the projectile’s max_velocity
   times its expire.after.age_ (keeping in mind that max_velocity is a
   speed_ in `px/t` and that expire.after.age is a duration_ of ``1s``,
   or ``60t``).

In the common case, where projectiles have a constant velocity, these
calculations should work as-is. If projectiles speed up or slow down,
then they may need to be adjusted.

.. _device: {filename}/plugins/format/object.rst#device
.. _activate.action: {filename}/plugins/format/object.rst#activate
.. _device.speed: {filename}/plugins/format/object.rst#device
.. _device.range: {filename}/plugins/format/object.rst#device

Waypoints
---------

Fixed locations that the player can select are called waypoints. There
are three sub-categories of waypoints:

*  Planets can build ships and be captured by transports.
*  Structures can be shot at and destroyed.
*  Stations can be neutralized and captured by assault transports.

.. table::
   :widths: auto

   ================  ===============================
   Name              Examples
   ================  ===============================
   `tpl/waypoint`_   `loc/jumpgate`_
   `tpl/planet`_     `loc/planet`_, `loc/moon`_
   `tpl/structure`_  `loc/power`_, `aud/etc/device`_
   `tpl/station`_    `loc/bunker`_, `loc/outpost`_
   ================  ===============================

.. _tpl/waypoint: https://github.com/arescentral/antares-data/blob/master/objects/tpl/waypoint.pn
.. _loc/jumpgate: https://github.com/arescentral/antares-data/blob/master/objects/loc/jumpgate.pn
.. _tpl/planet: https://github.com/arescentral/antares-data/blob/master/objects/tpl/planet.pn
.. _loc/planet: https://github.com/arescentral/antares-data/blob/master/objects/loc/planet.pn
.. _loc/moon: https://github.com/arescentral/antares-data/blob/master/objects/loc/moon.pn
.. _tpl/structure: https://github.com/arescentral/antares-data/blob/master/objects/tpl/structure.pn
.. _loc/power: https://github.com/arescentral/antares-data/blob/master/objects/loc/power.pn
.. _aud/etc/device: https://github.com/arescentral/antares-data/blob/master/objects/aud/etc/device.pn
.. _tpl/station: https://github.com/arescentral/antares-data/blob/master/objects/tpl/station.pn
.. _loc/outpost: https://github.com/arescentral/antares-data/blob/master/objects/loc/outpost.pn
.. _loc/bunker: https://github.com/arescentral/antares-data/blob/master/objects/loc/bunker.pn

Before creating a new waypoint, consider whether the object needs to act
differently, or just look different. For example, the Gaitori Habitat
Station in |ch02|_ and the Salrilian Battlestation in |ch15|_ are
actually just `Bunker Stations`_ with an override.sprite_.

.. _Bunker Stations: https://github.com/arescentral/antares-data/blob/master/objects/loc/bunker.pn
.. _override.sprite: {filename}/plugins/format/initial.rst#override-sprite

Decoration
----------

Decorations make the game look interesting but aren’t interactive. There
are two sub-categories:

*  Effects are drawn over ships’ sprites. They usually disappear when
   their animation completes.
*  Scenery is drawn under ships. Sometimes it disappears; other times it
   sticks around.

.. table::
   :widths: auto

   ==============  ===============================================
   Name            Examples
   ==============  ===============================================
   `tpl/effect`_   `sfx/explosion/large`_, `sfx/warp/in`_
   `tpl/scenery`_  `loc/sun`_, `loc/jump/node`_, `sfx/jump/large`_
   ==============  ===============================================

.. _tpl/effect: https://github.com/arescentral/antares-data/blob/master/objects/tpl/effect.pn
.. _sfx/explosion/large: https://github.com/arescentral/antares-data/blob/master/objects/sfx/explosion/large.pn
.. _sfx/warp/in: https://github.com/arescentral/antares-data/blob/master/objects/sfx/warp/in.pn
.. _tpl/scenery: https://github.com/arescentral/antares-data/blob/master/objects/tpl/scenery.pn
.. _loc/sun: https://github.com/arescentral/antares-data/blob/master/objects/loc/sun.pn
.. _loc/jump/node: https://github.com/arescentral/antares-data/blob/master/objects/loc/jump/node.pn
.. _sfx/jump/large: https://github.com/arescentral/antares-data/blob/master/objects/sfx/jump/large.pn

For example, a new explosion needs an animation.sprite_,
animation.frames_, and animation.speed_, and should
expire.after.animation_:

.. include:: pn/template-explosion.pn
   :code: procyon

It’s usually good to play the explosion sound as part of its
create.action_, so that the same sound will play for that explosion,
no matter what object is exploding.

.. _expire.after.animation: {filename}/plugins/format/object.rst#expire

Hazards
-------

Hazards are non-thinking objects that collide with ships and otherwise
cause trouble.

.. table::
   :widths: auto

   ===============  =================================================
   Name             Examples
   ===============  =================================================
   `tpl/hazard`_    `sfx/debris/a`_, `ast/regular/big`_, `ast/nasty`_
   ===============  =================================================

.. _tpl/hazard: https://github.com/arescentral/antares-data/blob/master/objects/tpl/hazard.pn
.. _sfx/debris/a: https://github.com/arescentral/antares-data/blob/master/objects/sfx/debris/a.pn
.. _ast/regular/big: https://github.com/arescentral/antares-data/blob/master/objects/ast/regular/big.pn
.. _ast/nasty: https://github.com/arescentral/antares-data/blob/master/objects/ast/nasty.pn

Miscellaneous
-------------

Some objects don’t fit neatly into the categories above:

*  EVATs are mostly ship-like, but can’t be selected and expire after a
   while. They have special behavior for occupying stations.
*  Rotations have a different appearance depending on their direction,
   but don’t fit neatly into any other categories (like ships,
   projectiles or EVATs).
*  Drones are mostly ship-like, but are animations_ instead of
   rotations_.

.. _animations: {filename}/plugins/format/object.rst#animation
.. _rotations: {filename}/plugins/format/object.rst#rotation

.. table::
   :widths: auto

   ===============  ==============================
   Name             Examples
   ===============  ==============================
   `tpl/rotation`_  `loc/flak`_, `dev/holo/decoy`_
   `tpl/evat`_      `ish/evat`_, `can/evat`_
   `tpl/drone`_     `zrb/spawn`_
   ===============  ==============================

.. _tpl/rotation: https://github.com/arescentral/antares-data/blob/master/objects/tpl/rotation.pn
.. _loc/flak: https://github.com/arescentral/antares-data/blob/master/objects/loc/flak.pn
.. _dev/holo/decoy: https://github.com/arescentral/antares-data/blob/master/objects/dev/holo/decoy.pn
.. _tpl/evat: https://github.com/arescentral/antares-data/blob/master/objects/tpl/evat.pn
.. _ish/evat: https://github.com/arescentral/antares-data/blob/master/objects/ish/evat.pn
.. _can/evat: https://github.com/arescentral/antares-data/blob/master/objects/can/evat.pn
.. _tpl/drone: https://github.com/arescentral/antares-data/blob/master/objects/tpl/drone.pn
.. _zrb/spawn: https://github.com/arescentral/antares-data/blob/master/objects/zrb/spawn.pn

.. include:: epilog.rsti
.. -*- tab-width: 3; indent-tabs-mode: nil; fill-column: 72 -*-
