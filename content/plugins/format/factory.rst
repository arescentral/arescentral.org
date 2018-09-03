The Factory Scenario
====================

.. sectnum::

The original data for Ares, by Nathan Lamont, is referred to as the
“Ares factory scenario”. It serves as a base for all other scenarios.
Often, it is convenient to refer to resources from the factory scenario
instead of creating everything from scratch.

.. contents::
   :local:
   :backlinks: none

Antares
-------

For licensing reasons, the `Antares factory scenario`_ differs slightly
from the Ares factory scenario. It contains replacements for some
sounds, when the originals could not be included. If possible, Antares
downloads and patches in the original sounds to restore the Ares factory
scenario.

Generally, you can ignore the difference between the Ares and Antares
factory scenarios.

.. _Antares factory scenario: https://github.com/arescentral/antares-data

Licensing
---------

The Antares factory scenario is licensed_ under the |cc-by-nc-sa|. In
practical terms, what this means is:

*  If you don’t copy or modify any of the factory scenario’s files,
   then you don’t have any obligations.

   You can still reference its files. For example, it’s OK to:

   *  List objects_ from the factory scenario in a level_ that you
      wrote yourself.
   *  Write a new object_ with a template_ from the factory scenario.
   *  Set a player’s race_ to one of the races from the factory
      scenario.
   *  Play music_ or sounds_ from the factory scenario.
   *  Show pictures_ or sprites_ from the factory scenario.

*  If you copy or modify any of the factory scenario’s files, you need
   to follow the terms of its license_. You need to release your
   changes under the terms of the same license, and mark them as such.

.. _licensed: https://github.com/arescentral/antares-data/blob/master/COPYING
.. _license: https://github.com/arescentral/antares-data/blob/master/COPYING
.. _template: {filename}/plugins/format/object.rst#template

Levels
------

*  `Solo levels`_:

   *  Tutorials:

      #. |tut1|_
      #. |tut2|_
      #. |tut3|_

   *  Campaign:

      #. |ch01|_
      #. |ch02|_
      #. |ch03|_
      #. |ch04|_
      #. |ch05|_
      #. |ch06|_
      #. |ch07|_
      #. |ch08|_
      #. |ch09|_
      #. |ch10|_
      #. |ch11|_
      #. |ch12|_
      #. |ch13|_
      #. |ch14|_
      #. |ch15|_
      #. |ch16|_
      #. |ch17|_
      #. |ch18|_
      #. |ch19|_
      #. |ch20|_

   *  Other levels:

      *  |srtm|_
      *  |dev1|_

*  `Net levels`_:

   #. |net1|_
   #. |net2|_
   #. |net3|_
   #. |net4|_
   #. |net5|_

.. _Solo levels: {filename}/plugins/format/level.rst#solo
.. _Net levels: {filename}/plugins/format/level.rst#net

Races
-----

*  |uns-pl|_
*  |ish-pl|_
*  |can-pl|_
*  |gai-pl|_
*  |sal-pl|_
*  |aud-pl|_
*  |obi-pl|_
*  |ele-pl|_
*  |baz-pl|_
*  |gro-pl|_

Objects
-------

Templates
~~~~~~~~~

.. table::
   :widths: 5 5 5 5 20 60

   +---+---+---+---+------------------+------------------------------------------------------------+
   | Template                         | Description                                                |
   +===+===+===+===+==================+============================================================+
   | `tpl/any`_                       | root; never used directly                                  |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   | `tpl/rotation`_              | objects with a sprite given by facing                      |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   |   | `tpl/ship`_              | persistent and controllable flying objects                 |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   |   |   | `tpl/warship`_       | ships shown as a triangle when zoomed out                  |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   |   |   |   | `tpl/fighter`_   | small ships without hyperdrive and light weaponry          |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   |   |   |   | `tpl/cruiser`_   | small ships with hyperdrive and light weaponry             |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   |   |   |   | `tpl/schooner`_  | small ships with hyperdrive and basic weaponry             |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   |   |   |   | `tpl/hvc`_       | small ships with hyperdrive and heavy weaponry             |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   |   |   |   | `tpl/gunship`_   | medium ships with heavy weaponry                           |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   |   |   |   | `tpl/hvd`_       | large ships with devastating weaponry                      |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   |   |   |   | `tpl/defdrone`_  | small ships with slow speed and high shields               |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   |   |   | `tpl/capship`_       | ships shown as a diamond when zoomed out                   |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   |   |   |   | `tpl/carrier`_   | large ships that carry and launch fighters                 |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   |   |   | `tpl/utilship`_      | ships shown as a plus when zoomed out                      |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   |   |   |   | `tpl/transport`_ | small ships that land on and capture planets               |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   |   |   |   | `tpl/engineer`_  | small ships used to capture flak drones                    |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   |   |   |   | `tpl/aslttran`_  | medium ships that carry EVATs to capture stations          |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   | `tpl/evat`_                  | soldiers launched from assault transports                  |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   | `tpl/rotpulse`_              | rotated projectiles                                        |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   |   | `tpl/missile`_           | projectiles that turn and seek their target                |
   +---+---+---+---+------------------+------------------------------------------------------------+
   | `tpl/animation`_                 | objects with a fixed or cycling sprite                     |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   | `tpl/waypoint`_              | points that can be selected and navigated to               |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   |   | `tpl/planet`_            | fixed objects captured by transports                       |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   |   | `tpl/structure`_         | fixed objects that can be shot at                          |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   |   |   | `tpl/station`_       | structures that fight back                                 |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   | `tpl/effect`_                | non-interactive animations drawn above ships               |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   | `tpl/scenery`_               | non-interactive animations drawn below ships               |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   | `tpl/hazard`_                | rocks, debris, and other collidable hazards                |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   | `tpl/drone`_                 | animated, ship-like objects                                |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   | `tpl/anipulse`_              | animated projectiles                                       |
   +---+---+---+---+------------------+------------------------------------------------------------+
   | `tpl/ray`_                       | point-to-point vector effects                              |
   +---+---+---+---+------------------+------------------------------------------------------------+
   | `tpl/bolt`_                      | vector projectiles that move along a trajectory            |
   +---+---+---+---+------------------+------------------------------------------------------------+
   | `tpl/device`_                    | non-physical objects activated by other objects            |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   | `tpl/gun`_                   | devices used for attacking forwards                        |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   | `tpl/turret`_                | devices used for attacking in all directions               |
   +---+---+---+---+------------------+------------------------------------------------------------+
   |   | `tpl/special`_               | devices used only when explicitly ordered                  |
   +---+---+---+---+------------------+------------------------------------------------------------+

.. _tpl/any: https://github.com/arescentral/antares-data/blob/master/objects/tpl/any.pn
.. _tpl/rotation: https://github.com/arescentral/antares-data/blob/master/objects/tpl/rotation.pn
.. _tpl/ship: https://github.com/arescentral/antares-data/blob/master/objects/tpl/ship.pn
.. _tpl/warship: https://github.com/arescentral/antares-data/blob/master/objects/tpl/warship.pn
.. _tpl/fighter: https://github.com/arescentral/antares-data/blob/master/objects/tpl/fighter.pn
.. _tpl/cruiser: https://github.com/arescentral/antares-data/blob/master/objects/tpl/cruiser.pn
.. _tpl/schooner: https://github.com/arescentral/antares-data/blob/master/objects/tpl/schooner.pn
.. _tpl/hvc: https://github.com/arescentral/antares-data/blob/master/objects/tpl/hvc.pn
.. _tpl/gunship: https://github.com/arescentral/antares-data/blob/master/objects/tpl/gunship.pn
.. _tpl/hvd: https://github.com/arescentral/antares-data/blob/master/objects/tpl/hvd.pn
.. _tpl/defdrone: https://github.com/arescentral/antares-data/blob/master/objects/tpl/defdrone.pn
.. _tpl/capship: https://github.com/arescentral/antares-data/blob/master/objects/tpl/capship.pn
.. _tpl/carrier: https://github.com/arescentral/antares-data/blob/master/objects/tpl/carrier.pn
.. _tpl/utilship: https://github.com/arescentral/antares-data/blob/master/objects/tpl/utilship.pn
.. _tpl/transport: https://github.com/arescentral/antares-data/blob/master/objects/tpl/transport.pn
.. _tpl/engineer: https://github.com/arescentral/antares-data/blob/master/objects/tpl/engineer.pn
.. _tpl/aslttran: https://github.com/arescentral/antares-data/blob/master/objects/tpl/aslttran.pn
.. _tpl/evat: https://github.com/arescentral/antares-data/blob/master/objects/tpl/evat.pn
.. _tpl/rotpulse: https://github.com/arescentral/antares-data/blob/master/objects/tpl/rotpulse.pn
.. _tpl/missile: https://github.com/arescentral/antares-data/blob/master/objects/tpl/missile.pn
.. _tpl/animation: https://github.com/arescentral/antares-data/blob/master/objects/tpl/animation.pn
.. _tpl/waypoint: https://github.com/arescentral/antares-data/blob/master/objects/tpl/waypoint.pn
.. _tpl/planet: https://github.com/arescentral/antares-data/blob/master/objects/tpl/planet.pn
.. _tpl/structure: https://github.com/arescentral/antares-data/blob/master/objects/tpl/structure.pn
.. _tpl/station: https://github.com/arescentral/antares-data/blob/master/objects/tpl/station.pn
.. _tpl/effect: https://github.com/arescentral/antares-data/blob/master/objects/tpl/effect.pn
.. _tpl/scenery: https://github.com/arescentral/antares-data/blob/master/objects/tpl/scenery.pn
.. _tpl/hazard: https://github.com/arescentral/antares-data/blob/master/objects/tpl/hazard.pn
.. _tpl/drone: https://github.com/arescentral/antares-data/blob/master/objects/tpl/drone.pn
.. _tpl/anipulse: https://github.com/arescentral/antares-data/blob/master/objects/tpl/anipulse.pn
.. _tpl/ray: https://github.com/arescentral/antares-data/blob/master/objects/tpl/ray.pn
.. _tpl/bolt: https://github.com/arescentral/antares-data/blob/master/objects/tpl/bolt.pn
.. _tpl/device: https://github.com/arescentral/antares-data/blob/master/objects/tpl/device.pn
.. _tpl/gun: https://github.com/arescentral/antares-data/blob/master/objects/tpl/gun.pn
.. _tpl/turret: https://github.com/arescentral/antares-data/blob/master/objects/tpl/turret.pn
.. _tpl/special: https://github.com/arescentral/antares-data/blob/master/objects/tpl/special.pn

Ships and EVATs
~~~~~~~~~~~~~~~

Standard
````````

=================  =================  =================  =================  =================  =================  =================
Which              Fighter            Cruiser            Schooner           Heavy Cruiser      Gunship            Heavy Destroyer
=================  =================  =================  =================  =================  =================  =================
Template           `tpl/fighter`_     `tpl/cruiser`_     `tpl/schooner`_    `tpl/hvc`_         `tpl/gunship`_     `tpl/hvd`_       
|uns-adj|          `uns/fighter`_     `uns/cruiser`_                                           `uns/gunship`_     `uns/hvd`_    
|ish-adj|          `ish/fighter`_     `ish/cruiser`_     `ish/schooner`_    `ish/hvc`_         `ish/gunship`_     `ish/hvd`_     
|can-adj|          `can/fighter`_     `can/cruiser`_     `can/schooner`_    `can/hvc`_         `can/gunship`_     `can/hvd`_     
|gai-adj|          `gai/fighter`_     `gai/cruiser`_                                           `gai/gunship`_     `gai/hvd`_    
|sal-adj|          `sal/fighter`_     `sal/cruiser`_                                           `sal/gunship`_     `sal/hvd`_    
|aud-adj|          `aud/fighter`_     `aud/cruiser`_                                           `aud/gunship`_     `aud/hvd`_
|ele-adj|                             `ele/cruiser`_
=================  =================  =================  =================  =================  =================  =================

=================  =================  =================  =================  =================  =================  =================
Which              Defense Drone      Carrier            Transport          Engineer Pod       Assault Transport  EVAT
=================  =================  =================  =================  =================  =================  =================
Template           `tpl/defdrone`_    `tpl/carrier`_     `tpl/transport`_   `tpl/engineer`_    `tpl/aslttran`_    `tpl/evat`_
|uns-adj|                             `uns/carrier`_     `uns/transport`_                      `uns/aslttran`_    [#uns-evat]_
|ish-adj|          `ish/defdrone`_    `ish/carrier`_     `ish/transport`_   `ish/engineer`_    `ish/aslttran`_    `ish/evat`_
|can-adj|          `can/defdrone`_    `can/carrier`_     `can/transport`_   `can/engineer`_    `can/aslttran`_    `can/evat`_
|gai-adj|                             `gai/carrier`_     `gai/transport`_   `gai/engineer`_    `gai/aslttran`_    `gai/evat`_
|sal-adj|                             `sal/carrier`_     `sal/transport`_                      `sal/aslttran`_    `sal/evat`_
|aud-adj|                             `aud/carrier`_     `aud/transport`_                      `aud/aslttran`_    `aud/evat`_
|obi-adj|                                                `obi/transport`_
=================  =================  =================  =================  =================  =================  =================

.. _tpl/evat: https://github.com/arescentral/antares-data/blob/master/objects/tpl/evat.pn
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

.. _uns/fighter: https://github.com/arescentral/antares-data/blob/master/objects/uns/fighter.pn
.. _uns/cruiser: https://github.com/arescentral/antares-data/blob/master/objects/uns/cruiser.pn
.. _uns/gunship: https://github.com/arescentral/antares-data/blob/master/objects/uns/gunship.pn
.. _uns/hvd: https://github.com/arescentral/antares-data/blob/master/objects/uns/hvd.pn
.. _uns/defdrone: https://github.com/arescentral/antares-data/blob/master/objects/uns/defdrone.pn
.. _uns/carrier: https://github.com/arescentral/antares-data/blob/master/objects/uns/carrier.pn
.. _uns/transport: https://github.com/arescentral/antares-data/blob/master/objects/uns/transport.pn
.. _uns/aslttran: https://github.com/arescentral/antares-data/blob/master/objects/uns/aslttran.pn

.. _ish/evat: https://github.com/arescentral/antares-data/blob/master/objects/ish/evat.pn
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

.. _can/evat: https://github.com/arescentral/antares-data/blob/master/objects/can/evat.pn
.. _can/fighter: https://github.com/arescentral/antares-data/blob/master/objects/can/fighter.pn
.. _can/cruiser: https://github.com/arescentral/antares-data/blob/master/objects/can/cruiser.pn
.. _can/schooner: https://github.com/arescentral/antares-data/blob/master/objects/can/schooner.pn
.. _can/hvc: https://github.com/arescentral/antares-data/blob/master/objects/can/hvc.pn
.. _can/gunship: https://github.com/arescentral/antares-data/blob/master/objects/can/gunship.pn
.. _can/hvd: https://github.com/arescentral/antares-data/blob/master/objects/can/hvd.pn
.. _can/defdrone: https://github.com/arescentral/antares-data/blob/master/objects/can/defdrone.pn
.. _can/carrier: https://github.com/arescentral/antares-data/blob/master/objects/can/carrier.pn
.. _can/transport: https://github.com/arescentral/antares-data/blob/master/objects/can/transport.pn
.. _can/engineer: https://github.com/arescentral/antares-data/blob/master/objects/can/engineer.pn
.. _can/aslttran: https://github.com/arescentral/antares-data/blob/master/objects/can/aslttran.pn

.. _gai/evat: https://github.com/arescentral/antares-data/blob/master/objects/gai/evat.pn
.. _gai/fighter: https://github.com/arescentral/antares-data/blob/master/objects/gai/fighter.pn
.. _gai/cruiser: https://github.com/arescentral/antares-data/blob/master/objects/gai/cruiser.pn
.. _gai/gunship: https://github.com/arescentral/antares-data/blob/master/objects/gai/gunship.pn
.. _gai/hvd: https://github.com/arescentral/antares-data/blob/master/objects/gai/hvd.pn
.. _gai/defdrone: https://github.com/arescentral/antares-data/blob/master/objects/gai/defdrone.pn
.. _gai/carrier: https://github.com/arescentral/antares-data/blob/master/objects/gai/carrier.pn
.. _gai/transport: https://github.com/arescentral/antares-data/blob/master/objects/gai/transport.pn
.. _gai/engineer: https://github.com/arescentral/antares-data/blob/master/objects/gai/engineer.pn
.. _gai/aslttran: https://github.com/arescentral/antares-data/blob/master/objects/gai/aslttran.pn

.. _sal/evat: https://github.com/arescentral/antares-data/blob/master/objects/sal/evat.pn
.. _sal/fighter: https://github.com/arescentral/antares-data/blob/master/objects/sal/fighter.pn
.. _sal/cruiser: https://github.com/arescentral/antares-data/blob/master/objects/sal/cruiser.pn
.. _sal/gunship: https://github.com/arescentral/antares-data/blob/master/objects/sal/gunship.pn
.. _sal/hvd: https://github.com/arescentral/antares-data/blob/master/objects/sal/hvd.pn
.. _sal/defdrone: https://github.com/arescentral/antares-data/blob/master/objects/sal/defdrone.pn
.. _sal/carrier: https://github.com/arescentral/antares-data/blob/master/objects/sal/carrier.pn
.. _sal/transport: https://github.com/arescentral/antares-data/blob/master/objects/sal/transport.pn
.. _sal/aslttran: https://github.com/arescentral/antares-data/blob/master/objects/sal/aslttran.pn

.. _aud/evat: https://github.com/arescentral/antares-data/blob/master/objects/aud/evat.pn
.. _aud/fighter: https://github.com/arescentral/antares-data/blob/master/objects/aud/fighter.pn
.. _aud/cruiser: https://github.com/arescentral/antares-data/blob/master/objects/aud/cruiser.pn
.. _aud/gunship: https://github.com/arescentral/antares-data/blob/master/objects/aud/gunship.pn
.. _aud/hvd: https://github.com/arescentral/antares-data/blob/master/objects/aud/hvd.pn
.. _aud/defdrone: https://github.com/arescentral/antares-data/blob/master/objects/aud/defdrone.pn
.. _aud/carrier: https://github.com/arescentral/antares-data/blob/master/objects/aud/carrier.pn
.. _aud/transport: https://github.com/arescentral/antares-data/blob/master/objects/aud/transport.pn
.. _aud/aslttran: https://github.com/arescentral/antares-data/blob/master/objects/aud/aslttran.pn

.. _ele/cruiser: https://github.com/arescentral/antares-data/blob/master/objects/ele/cruiser.pn

.. _obi/transport: https://github.com/arescentral/antares-data/blob/master/objects/obi/transport.pn

Tutorial Ships
~~~~~~~~~~~~~~

*  `can/etc/transport/tut1 <https://github.com/arescentral/antares-data/blob/master/objects/can/etc/transport/tut1.pn>`_,
   the cloaked transport in |tut1|_.
*  `ish/etc/cruiser/tut3 <https://github.com/arescentral/antares-data/blob/master/objects/ish/etc/cruiser/tut3.pn>`_,
   built in |tut3|_.

Campaign Ships
~~~~~~~~~~~~~~

*  Ships seen in multiple chapters:

   *  `obi/escort <https://github.com/arescentral/antares-data/blob/master/objects/obi/escort.pn>`_,
      the Obish escort seen in several levels.
   *  `ish/etc/astrominer <https://github.com/arescentral/antares-data/blob/master/objects/ish/etc/astrominer.pn>`_,
      the astrominer in |ch07|_ and |ch08|_.

*  |ch01|:

   *  `gai/etc/transport/ch1 <https://github.com/arescentral/antares-data/blob/master/objects/gai/etc/transport/ch1.pn>`_

*  |ch02|:

   *  `loc/relay <https://github.com/arescentral/antares-data/blob/master/objects/loc/relay.pn>`_,
      the relay stations.

*  |ch04|:

   *  `obi/etc/liner <https://github.com/arescentral/antares-data/blob/master/objects/obi/etc/liner.pn>`_,
      the rescue vessel.
   *  `obi/etc/transport/rescue <https://github.com/arescentral/antares-data/blob/master/objects/obi/etc/transport/rescue.pn>`_,
      the Obish transport when ready to pick up Obiards.
   *  The prison labs:

      *  `gai/etc/lab/base <https://github.com/arescentral/antares-data/blob/master/objects/gai/etc/lab/base.pn>`_
      *  `gai/etc/lab/burning <https://github.com/arescentral/antares-data/blob/master/objects/gai/etc/lab/burning.pn>`_

   *  The Obiard prisoners:

      *  `obi/etc/obiard/returning <https://github.com/arescentral/antares-data/blob/master/objects/obi/etc/obiard/returning.pn>`_
      *  `obi/etc/obiard/turning <https://github.com/arescentral/antares-data/blob/master/objects/obi/etc/obiard/turning.pn>`_
      *  `obi/etc/obiard/waving <https://github.com/arescentral/antares-data/blob/master/objects/obi/etc/obiard/waving.pn>`_

   *  `gai/etc/spawner/obj <https://github.com/arescentral/antares-data/blob/master/objects/gai/etc/spawner/obj.pn>`_,
      used to periodically spawn Gaitori ships.
   *  `gai/etc/spawner/item <https://github.com/arescentral/antares-data/blob/master/objects/gai/etc/spawner/item.pn>`_,
      the weapon used by ``gai/etc/spawner/obj``

*  |ch07|:

   *  The asteroid (slow, random direction):

      *  `ast/otr/big <https://github.com/arescentral/antares-data/blob/master/objects/ast/otr/big.pn>`_
      *  `ast/otr/medium <https://github.com/arescentral/antares-data/blob/master/objects/ast/otr/medium.pn>`_
      *  `ast/otr/small <https://github.com/arescentral/antares-data/blob/master/objects/ast/otr/small.pn>`_

*  |ch08|:

   *  `can/etc/spawner/obj <https://github.com/arescentral/antares-data/blob/master/objects/can/etc/spawner/obj.pn>`_,
      used to periodically spawns Cantharan ships.
   *  `can/etc/spawner/item <https://github.com/arescentral/antares-data/blob/master/objects/can/etc/spawner/item.pn>`_,
      the weapon used by ``can/etc/spawner/obj``.

*  |ch11|:

   *  `uns/ares <https://github.com/arescentral/antares-data/blob/master/objects/uns/ares.pn>`_,
      the titular UNS Ares.
   *  `ish/etc/hvd/rescue <https://github.com/arescentral/antares-data/blob/master/objects/ish/etc/hvd/rescue.pn>`_,
      the Ishiman HVD when ready to pick up humans.
   *  The prison labs:

      *  `sal/etc/lab/base <https://github.com/arescentral/antares-data/blob/master/objects/sal/etc/lab/base.pn>`_
      *  `sal/etc/lab/burning <https://github.com/arescentral/antares-data/blob/master/objects/sal/etc/lab/burning.pn>`_

   *  Human prisoners:

      *  `uns/etc/human/returning <https://github.com/arescentral/antares-data/blob/master/objects/uns/etc/human/returning.pn>`_
      *  `uns/etc/human/turning <https://github.com/arescentral/antares-data/blob/master/objects/uns/etc/human/turning.pn>`_
      *  `uns/etc/human/waving <https://github.com/arescentral/antares-data/blob/master/objects/uns/etc/human/waving.pn>`_

*  |ch12|:

   *  `uns/etc/bttlship <https://github.com/arescentral/antares-data/blob/master/objects/uns/etc/bttlship.pn>`_,
      the hybrid Ishiman-Obish battleship.
   *  `loc/shipyard <https://github.com/arescentral/antares-data/blob/master/objects/loc/shipyard.pn>`_,
      the shipyard that builds the battleship.
   *  `ish/etc/cargo <https://github.com/arescentral/antares-data/blob/master/objects/ish/etc/cargo.pn>`_,
      the vessels delivering cargo to the shipyard.

*  |ch13|:

   *  `ele/etc/escape-pod <https://github.com/arescentral/antares-data/blob/master/objects/ele/etc/escape-pod.pn>`_
   *  `ish/etc/tug <https://github.com/arescentral/antares-data/blob/master/objects/ish/etc/tug.pn>`_,
      the tractor tug.
   *  The Elejeetian liner:

      *  `ele/etc/liner/disabled <https://github.com/arescentral/antares-data/blob/master/objects/ele/etc/liner/disabled.pn>`_,
         its initial, disabled form.
      *  `ele/etc/liner <https://github.com/arescentral/antares-data/blob/master/objects/ele/etc/liner.pn>`_,
         used after the tractor tug starts “pulling” it.

*  |ch14|:

   *  `can/etc/border-drone <https://github.com/arescentral/antares-data/blob/master/objects/can/etc/border-drone.pn>`_
   *  The Bazidanese battleship:

      *  `baz/bttlship <https://github.com/arescentral/antares-data/blob/master/objects/baz/bttlship.pn>`_,
         its active form.
      *  `baz/etc/bttlship/moored <https://github.com/arescentral/antares-data/blob/master/objects/baz/etc/bttlship/moored.pn>`_,
         its initial, disabled form.

   *  `loc/moor <https://github.com/arescentral/antares-data/blob/master/objects/loc/moor.pn>`_,
      the tractor moor.

*  |ch16|:

   *  `ish/etc/research <https://github.com/arescentral/antares-data/blob/master/objects/ish/etc/research.pn>`_,
      the Ishiman research vessel.
   *  `aud/etc/device <https://github.com/arescentral/antares-data/blob/master/objects/aud/etc/device.pn>`_,
      the Audemedon massive device.

*  |ch18|:

   *  `uns/etc/transport/ch18 <https://github.com/arescentral/antares-data/blob/master/objects/uns/etc/transport/ch18.pn>`_

*  |ch19|:

   *  `can/gateship/base <https://github.com/arescentral/antares-data/blob/master/objects/can/gateship/base.pn>`_,
      the initial form of the Cantharan gateship.
   *  `can/gateship/jump <https://github.com/arescentral/antares-data/blob/master/objects/can/gateship/jump.pn>`_,
      used when it flees through a jump gate.

*  |ch20|:

   *  `ast/shoot/nasty <https://github.com/arescentral/antares-data/blob/master/objects/ast/shoot/nasty.pn>`_,
      the nastiroid shooter.
   *  `ish/etc/hvc/mod <https://github.com/arescentral/antares-data/blob/master/objects/ish/etc/hvc/mod.pn>`_,
      the modified Ishiman heavy cruiser.
   *  `can/gateship/damaged <https://github.com/arescentral/antares-data/blob/master/objects/can/gateship/damaged.pn>`_,
      the initial, damaged form of the Cantharan gateship.
   *  `can/gateship/dying <https://github.com/arescentral/antares-data/blob/master/objects/can/gateship/dying.pn>`_,
      the gateship’s extended destruction sequence.

Net Level Ships
~~~~~~~~~~~~~~~

*  |net3|

   *  Cruisers for players 1 and 2, both active and inactive after being
      sent to jail:

      *  `gro/ctf/cruiser/p1-active <https://github.com/arescentral/antares-data/blob/master/objects/gro/ctf/cruiser/p1-active.pn>`_
      *  `gro/ctf/cruiser/p1-inactive <https://github.com/arescentral/antares-data/blob/master/objects/gro/ctf/cruiser/p1-inactive.pn>`_
      *  `gro/ctf/cruiser/p2-active <https://github.com/arescentral/antares-data/blob/master/objects/gro/ctf/cruiser/p2-active.pn>`_
      *  `gro/ctf/cruiser/p2-inactive <https://github.com/arescentral/antares-data/blob/master/objects/gro/ctf/cruiser/p2-inactive.pn>`_

   *  Flagpods for players 1 and 2:

      *  `gro/ctf/flag/p1 <https://github.com/arescentral/antares-data/blob/master/objects/gro/ctf/flag/p1.pn>`_
      *  `gro/ctf/flag/p2 <https://github.com/arescentral/antares-data/blob/master/objects/gro/ctf/flag/p2.pn>`_

   *  Prison moors for players 1 and 2, both active and inactive after a
      jailbreak:

      *  `gro/ctf/moor/p1-active <https://github.com/arescentral/antares-data/blob/master/objects/gro/ctf/moor/p1-active.pn>`_
      *  `gro/ctf/moor/p1-inactive <https://github.com/arescentral/antares-data/blob/master/objects/gro/ctf/moor/p1-inactive.pn>`_
      *  `gro/ctf/moor/p2-active <https://github.com/arescentral/antares-data/blob/master/objects/gro/ctf/moor/p2-active.pn>`_
      *  `gro/ctf/moor/p2-inactive <https://github.com/arescentral/antares-data/blob/master/objects/gro/ctf/moor/p2-inactive.pn>`_

*  |net4|

   *  `gro/cruiser <https://github.com/arescentral/antares-data/blob/master/objects/gro/cruiser.pn>`_,
      the Grolk cruiser used in |net4|_.

Weapons and Projectiles
~~~~~~~~~~~~~~~~~~~~~~~

=======================================  ==========================  ==========================  ==========================
Name                                     Device(s)                   Projectile                  Effects
=======================================  ==========================  ==========================  ==========================
ASB Beam Cannon                          `dev/asb/gun`_              `dev/asb/bolt`_
Antimatter Reactor                       `dev/anti1/gun`_,           `dev/anti1/pulse`_
                                         `dev/anti1/rapid`_
Antimatter Type II                       `dev/anti2/gun`_            `dev/anti2/pulse`_          `dev/anti2/pulse2`_
Atomic Pulse                             `dev/atomic/turret`_        `dev/atomic/pulse`_         `sfx/sparkle`_
Audemedon Missile                        `dev/amissile/launcher`_    `dev/amissile/missile`_
CTF Reactivator (P1)                     `dev/reactivator/p1`_
CTF Reactivator (P2)                     `dev/reactivator/p2`_
Charged Form Cannon                      `dev/cform/gun`_            `dev/cform/pulse`_
Chronon Particle Gun                     `dev/chronon/gun`_          `dev/chronon/pulse`_
ClusterCell Array                        `dev/cluster/turret`_       `dev/cluster/pulse`_
Concussive Pellet                        `dev/conc/gun`_             `dev/conc/pellet`_          `sfx/gunsmoke`_
Cruise Missile                           `dev/cm/launcher`_,         `dev/cm/missile`_
                                         `dev/cm/five`_
Electronic Jam                           `dev/jammer/turret`_
Flak Artillery                           `dev/flak/turret`_          `dev/flak/pulse`_           `dev/flak/flak`_
Fullerene Gun                            `dev/fullerene/gun`_        `dev/fullerene/pulse`_
Fusion Pulse Reactor                     `dev/fusion/gun`_,          `dev/fusion/pulse`_
                                         `dev/fusion/rapid`_
Holographic Decoy                        `dev/holo/item`_            `dev/holo/decoy`_
Inasa Pulse Gun                          `dev/inasa/gun`_,           `dev/inasa/pulse`_
                                         `dev/inasa/rapid`_
Kinetic Laser                            `dev/kl/gun`_               `dev/kl/bolt`_
LRPK Beam (Salrilian)                    `dev/pk/sal/gun`_           `dev/pk/sal/bolt`_
Laser Cannon                             `dev/laser/gun`_            `dev/laser/gun-bolt`_
Laser Turret                             `dev/laser/turret`_         `dev/laser/turret-bolt`_
Lepton Beam Cannon                       `dev/lepton/gun`_           `dev/lepton/bolt`_
Lightwave Pulse                          `dev/mine/gun`_             `dev/mine/pulse`_
Magneto Pulse Gun                        `dev/magneto/gun`_,         `dev/magneto/pulse`_
                                         `dev/magneto/rapid`_
Magno Launcher                           `dev/magno/turret`_         `dev/magno/pulse`_
Neutron Pulse Gun                        `dev/neutron/gun`_          `dev/neutron/pulse`_
Newo Beam Cannon                         `dev/newo/gun`_             `dev/newo/bolt`_
Onas Pulse Gun                           `dev/onas/gun`_             `dev/onas/pulse`_
P-K Beam (Cantharan)                     `dev/pk/can/gun`_           `dev/pk/can/bolt`_
P-K Beam (Ishiman)                       `dev/pk/ish/gun`_,          `dev/pk/ish/bolt`_
                                         `dev/pk/ish/rapid`_,
                                         `dev/pk/ish/hand`_
Photoreactor Pulse                       `dev/photo/gun`_,           `dev/photo/pulse`_
                                         `dev/photo/light`_
Plasma Ball Gun                          `dev/fireball/gun`_         `dev/fireball/pulse`_       `dev/fireball/trail`_
ProtoPulse Cannon                        `dev/pp/turret`_,           `dev/pp/pulse`_
                                         `dev/pp/twin`_
Protopulse 2 Gun                         `dev/pp2/pulse`_            `dev/pp2/gun`_
Quasimatter Gun                          `dev/quasi/gun`_            `dev/quasi/pulse`_
R-Plasma Launcher                        `dev/rplasma/gun`_          `dev/rplasma/pulse`_
Repulser Beam                            `dev/repulser/turret`_      `dev/repulser/bolt`_
Shrikeolator                             `dev/shrikeolator/turret`_  `dev/shrikeolator/pulse`_
Stealth Field                            `dev/stealth/item`_
Trans-Space Bolt                         `dev/tspace/gun`_           `dev/tspace/ray`_
Trazer Cannon                            `dev/trazer/gun`_           `dev/trazer/ray`_
Z Beam Cannon                            `dev/zbeam/turret`_         `dev/zbeam/bolt`_
=======================================  ==========================  ==========================  ==========================

.. _dev/amissile/launcher: https://github.com/arescentral/antares-data/blob/master/objects/dev/amissile/launcher.pn
.. _dev/amissile/missile: https://github.com/arescentral/antares-data/blob/master/objects/dev/amissile/missile.pn
.. _dev/anti1/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/anti1/gun.pn
.. _dev/anti1/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/anti1/pulse.pn
.. _dev/anti1/rapid: https://github.com/arescentral/antares-data/blob/master/objects/dev/anti1/rapid.pn
.. _dev/anti2/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/anti2/gun.pn
.. _dev/anti2/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/anti2/pulse.pn
.. _dev/anti2/pulse2: https://github.com/arescentral/antares-data/blob/master/objects/dev/anti2/pulse2.pn
.. _dev/asb/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/asb/gun.pn
.. _dev/asb/bolt: https://github.com/arescentral/antares-data/blob/master/objects/dev/asb/bolt.pn
.. _dev/atomic/turret: https://github.com/arescentral/antares-data/blob/master/objects/dev/atomic/turret.pn
.. _dev/atomic/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/atomic/pulse.pn
.. _sfx/sparkle: https://github.com/arescentral/antares-data/blob/master/objects/sfx/sparkle.pn
.. _dev/cform/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/cform/gun.pn
.. _dev/cform/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/cform/pulse.pn
.. _dev/chronon/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/chronon/gun.pn
.. _dev/chronon/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/chronon/pulse.pn
.. _dev/cluster/turret: https://github.com/arescentral/antares-data/blob/master/objects/dev/cluster/turret.pn
.. _dev/cluster/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/cluster/pulse.pn
.. _dev/cm/launcher: https://github.com/arescentral/antares-data/blob/master/objects/dev/cm/launcher.pn
.. _dev/cm/missile: https://github.com/arescentral/antares-data/blob/master/objects/dev/cm/missile.pn
.. _dev/cm/five: https://github.com/arescentral/antares-data/blob/master/objects/dev/cm/five.pn
.. _dev/conc/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/conc/gun.pn
.. _dev/conc/pellet: https://github.com/arescentral/antares-data/blob/master/objects/dev/conc/pellet.pn
.. _sfx/gunsmoke: https://github.com/arescentral/antares-data/blob/master/objects/sfx/gunsmoke.pn
.. _dev/fireball/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/fireball/gun.pn
.. _dev/fireball/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/fireball/pulse.pn
.. _dev/fireball/trail: https://github.com/arescentral/antares-data/blob/master/objects/dev/fireball/trail.pn
.. _dev/flak/turret: https://github.com/arescentral/antares-data/blob/master/objects/dev/flak/turret.pn
.. _dev/flak/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/flak/pulse.pn
.. _dev/flak/flak: https://github.com/arescentral/antares-data/blob/master/objects/dev/flak/flak.pn
.. _dev/fullerene/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/fullerene/gun.pn
.. _dev/fullerene/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/fullerene/pulse.pn
.. _dev/fusion/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/fusion/gun.pn
.. _dev/fusion/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/fusion/pulse.pn
.. _dev/fusion/rapid: https://github.com/arescentral/antares-data/blob/master/objects/dev/fusion/rapid.pn
.. _dev/holo/item: https://github.com/arescentral/antares-data/blob/master/objects/dev/holo/item.pn
.. _dev/holo/decoy: https://github.com/arescentral/antares-data/blob/master/objects/dev/holo/decoy.pn
.. _dev/inasa/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/inasa/gun.pn
.. _dev/inasa/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/inasa/pulse.pn
.. _dev/inasa/rapid: https://github.com/arescentral/antares-data/blob/master/objects/dev/inasa/rapid.pn
.. _dev/jammer/turret: https://github.com/arescentral/antares-data/blob/master/objects/dev/jammer/turret.pn
.. _dev/kl/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/kl/gun.pn
.. _dev/kl/bolt: https://github.com/arescentral/antares-data/blob/master/objects/dev/kl/bolt.pn
.. _dev/laser/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/laser/gun.pn
.. _dev/laser/gun-bolt: https://github.com/arescentral/antares-data/blob/master/objects/dev/laser/gun-bolt.pn
.. _dev/laser/turret: https://github.com/arescentral/antares-data/blob/master/objects/dev/laser/turret.pn
.. _dev/laser/turret-bolt: https://github.com/arescentral/antares-data/blob/master/objects/dev/laser/turret-bolt.pn
.. _dev/lepton/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/lepton/gun.pn
.. _dev/lepton/bolt: https://github.com/arescentral/antares-data/blob/master/objects/dev/lepton/bolt.pn
.. _dev/magneto/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/magneto/gun.pn
.. _dev/magneto/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/magneto/pulse.pn
.. _dev/magneto/rapid: https://github.com/arescentral/antares-data/blob/master/objects/dev/magneto/rapid.pn
.. _dev/magno/turret: https://github.com/arescentral/antares-data/blob/master/objects/dev/magno/turret.pn
.. _dev/magno/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/magno/pulse.pn
.. _dev/mine/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/mine/gun.pn
.. _dev/mine/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/mine/pulse.pn
.. _dev/neutron/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/neutron/gun.pn
.. _dev/neutron/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/neutron/pulse.pn
.. _dev/newo/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/newo/gun.pn
.. _dev/newo/bolt: https://github.com/arescentral/antares-data/blob/master/objects/dev/newo/bolt.pn
.. _dev/onas/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/onas/gun.pn
.. _dev/onas/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/onas/pulse.pn
.. _dev/photo/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/photo/gun.pn
.. _dev/photo/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/photo/pulse.pn
.. _dev/photo/light: https://github.com/arescentral/antares-data/blob/master/objects/dev/photo/light.pn
.. _dev/pk/can/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/pk/can/gun.pn
.. _dev/pk/can/bolt: https://github.com/arescentral/antares-data/blob/master/objects/dev/pk/can/bolt.pn
.. _dev/pk/ish/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/pk/ish/gun.pn
.. _dev/pk/ish/bolt: https://github.com/arescentral/antares-data/blob/master/objects/dev/pk/ish/bolt.pn
.. _dev/pk/ish/rapid: https://github.com/arescentral/antares-data/blob/master/objects/dev/pk/ish/rapid.pn
.. _dev/pk/ish/hand: https://github.com/arescentral/antares-data/blob/master/objects/dev/pk/ish/hand.pn
.. _dev/pk/sal/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/pk/sal/gun.pn
.. _dev/pk/sal/bolt: https://github.com/arescentral/antares-data/blob/master/objects/dev/pk/sal/bolt.pn
.. _dev/pp/turret: https://github.com/arescentral/antares-data/blob/master/objects/dev/pp/turret.pn
.. _dev/pp/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/pp/pulse.pn
.. _dev/pp/twin: https://github.com/arescentral/antares-data/blob/master/objects/dev/pp/twin.pn
.. _dev/pp2/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/pp2/pulse.pn
.. _dev/pp2/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/pp2/gun.pn
.. _dev/quasi/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/quasi/gun.pn
.. _dev/quasi/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/quasi/pulse.pn
.. _dev/reactivator/p1: https://github.com/arescentral/antares-data/blob/master/objects/dev/reactivator/p1.pn
.. _dev/reactivator/p2: https://github.com/arescentral/antares-data/blob/master/objects/dev/reactivator/p2.pn
.. _dev/repulser/turret: https://github.com/arescentral/antares-data/blob/master/objects/dev/repulser/turret.pn
.. _dev/repulser/bolt: https://github.com/arescentral/antares-data/blob/master/objects/dev/repulser/bolt.pn
.. _dev/rplasma/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/rplasma/gun.pn
.. _dev/rplasma/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/rplasma/pulse.pn
.. _dev/shrikeolator/turret: https://github.com/arescentral/antares-data/blob/master/objects/dev/shrikeolator/turret.pn
.. _dev/shrikeolator/pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/shrikeolator/pulse.pn
.. _dev/stealth/item: https://github.com/arescentral/antares-data/blob/master/objects/dev/stealth/item.pn
.. _dev/trazer/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/trazer/gun.pn
.. _dev/trazer/ray: https://github.com/arescentral/antares-data/blob/master/objects/dev/trazer/ray.pn
.. _dev/tspace/gun: https://github.com/arescentral/antares-data/blob/master/objects/dev/tspace/gun.pn
.. _dev/tspace/ray: https://github.com/arescentral/antares-data/blob/master/objects/dev/tspace/ray.pn
.. _dev/zbeam/turret: https://github.com/arescentral/antares-data/blob/master/objects/dev/zbeam/turret.pn
.. _dev/zbeam/bolt: https://github.com/arescentral/antares-data/blob/master/objects/dev/zbeam/bolt.pn

EVAT Assault Teams and Fighter Launch Bays
``````````````````````````````````````````

==================  ==================  ==================
Race                Assault Team        Launch Bay
==================  ==================  ==================
Human               [#uns-evat]_        `dev/bay/uns`_
Ishiman             `dev/assault/ish`_  `dev/bay/ish`_
Cantharan           `dev/assault/can`_  `dev/bay/can`_
Gaitori             `dev/assault/gai`_  `dev/bay/gai`_
Salrilian           `dev/assault/sal`_  `dev/bay/sal`_
Audemedon           `dev/assault/aud`_  `dev/bay/aud`_
==================  ==================  ==================

.. _dev/assault/ish: https://github.com/arescentral/antares-data/blob/master/objects/dev/assault/ish.pn
.. _dev/assault/can: https://github.com/arescentral/antares-data/blob/master/objects/dev/assault/can.pn
.. _dev/assault/gai: https://github.com/arescentral/antares-data/blob/master/objects/dev/assault/gai.pn
.. _dev/assault/sal: https://github.com/arescentral/antares-data/blob/master/objects/dev/assault/sal.pn
.. _dev/assault/aud: https://github.com/arescentral/antares-data/blob/master/objects/dev/assault/aud.pn
.. _dev/bay/uns: https://github.com/arescentral/antares-data/blob/master/objects/dev/bay/uns.pn
.. _dev/bay/ish: https://github.com/arescentral/antares-data/blob/master/objects/dev/bay/ish.pn
.. _dev/bay/can: https://github.com/arescentral/antares-data/blob/master/objects/dev/bay/can.pn
.. _dev/bay/gai: https://github.com/arescentral/antares-data/blob/master/objects/dev/bay/gai.pn
.. _dev/bay/sal: https://github.com/arescentral/antares-data/blob/master/objects/dev/bay/sal.pn
.. _dev/bay/aud: https://github.com/arescentral/antares-data/blob/master/objects/dev/bay/aud.pn

Hazards
~~~~~~~

Asteroids
`````````

*  Regular asteroids

   *  `ast/regular/big <https://github.com/arescentral/antares-data/blob/master/objects/ast/regular/big.pn>`_
   *  `ast/regular/medium <https://github.com/arescentral/antares-data/blob/master/objects/ast/regular/medium.pn>`_
   *  `ast/regular/small <https://github.com/arescentral/antares-data/blob/master/objects/ast/regular/small.pn>`_

*  Other asteroids

   *  `ast/nasty <https://github.com/arescentral/antares-data/blob/master/objects/ast/nasty.pn>`_,
      big green nastiroids you don’t want to touch.
   *  `ast/rand-dir <https://github.com/arescentral/antares-data/blob/master/objects/ast/rand-dir.pn>`_,
      created at a ±45° angle

*  Shooters

   *  `ast/shoot/lite/down <https://github.com/arescentral/antares-data/blob/master/objects/ast/shoot/lite/down.pn>`_
   *  `ast/shoot/lite/up <https://github.com/arescentral/antares-data/blob/master/objects/ast/shoot/lite/up.pn>`_
   *  `ast/shoot/narrow/down <https://github.com/arescentral/antares-data/blob/master/objects/ast/shoot/narrow/down.pn>`_
   *  `ast/shoot/narrow/up <https://github.com/arescentral/antares-data/blob/master/objects/ast/shoot/narrow/up.pn>`_
   *  `ast/shoot/wide/down <https://github.com/arescentral/antares-data/blob/master/objects/ast/shoot/wide/down.pn>`_
   *  `ast/shoot/wide/up <https://github.com/arescentral/antares-data/blob/master/objects/ast/shoot/wide/up.pn>`_

Zerbilites
``````````

* `zrb/base <https://github.com/arescentral/antares-data/blob/master/objects/zrb/base.pn>`_
* `zrb/spawn <https://github.com/arescentral/antares-data/blob/master/objects/zrb/spawn.pn>`_

Debris
``````

*  `sfx/debris/a <https://github.com/arescentral/antares-data/blob/master/objects/sfx/debris/a.pn>`_
*  `sfx/debris/b <https://github.com/arescentral/antares-data/blob/master/objects/sfx/debris/b.pn>`_
*  `sfx/debris/c <https://github.com/arescentral/antares-data/blob/master/objects/sfx/debris/c.pn>`_

Locations
~~~~~~~~~

*  `loc/bunker <https://github.com/arescentral/antares-data/blob/master/objects/loc/bunker.pn>`_
*  `loc/flak <https://github.com/arescentral/antares-data/blob/master/objects/loc/flak.pn>`_
*  `loc/jump/gate <https://github.com/arescentral/antares-data/blob/master/objects/loc/jump/gate.pn>`_
*  `loc/jump/node <https://github.com/arescentral/antares-data/blob/master/objects/loc/jump/node.pn>`_
*  `loc/moon <https://github.com/arescentral/antares-data/blob/master/objects/loc/moon.pn>`_
*  `loc/outpost <https://github.com/arescentral/antares-data/blob/master/objects/loc/outpost.pn>`_
*  `loc/planet <https://github.com/arescentral/antares-data/blob/master/objects/loc/planet.pn>`_
*  `loc/power <https://github.com/arescentral/antares-data/blob/master/objects/loc/power.pn>`_
*  `loc/sun <https://github.com/arescentral/antares-data/blob/master/objects/loc/sun.pn>`_

Special effects
~~~~~~~~~~~~~~~

*  Blessed Objects

   *  `sfx/crew <https://github.com/arescentral/antares-data/blob/master/objects/sfx/crew.pn>`_
   *  `sfx/energy <https://github.com/arescentral/antares-data/blob/master/objects/sfx/energy.pn>`_
   *  `sfx/warp/in <https://github.com/arescentral/antares-data/blob/master/objects/sfx/warp/in.pn>`_
   *  `sfx/warp/out <https://github.com/arescentral/antares-data/blob/master/objects/sfx/warp/out.pn>`_

*  Explosions

   *  `sfx/explosion/asteroid <https://github.com/arescentral/antares-data/blob/master/objects/sfx/explosion/asteroid.pn>`_
   *  `sfx/explosion/energy <https://github.com/arescentral/antares-data/blob/master/objects/sfx/explosion/energy.pn>`_
   *  `sfx/explosion/flak <https://github.com/arescentral/antares-data/blob/master/objects/sfx/explosion/flak.pn>`_
   *  `sfx/explosion/gas <https://github.com/arescentral/antares-data/blob/master/objects/sfx/explosion/gas.pn>`_
   *  `sfx/explosion/giant <https://github.com/arescentral/antares-data/blob/master/objects/sfx/explosion/giant.pn>`_
   *  `sfx/explosion/lab <https://github.com/arescentral/antares-data/blob/master/objects/sfx/explosion/lab.pn>`_
   *  `sfx/explosion/large-hit <https://github.com/arescentral/antares-data/blob/master/objects/sfx/explosion/large-hit.pn>`_
   *  `sfx/explosion/large <https://github.com/arescentral/antares-data/blob/master/objects/sfx/explosion/large.pn>`_
   *  `sfx/explosion/missile-hit <https://github.com/arescentral/antares-data/blob/master/objects/sfx/explosion/missile-hit.pn>`_
   *  `sfx/explosion/quasi <https://github.com/arescentral/antares-data/blob/master/objects/sfx/explosion/quasi.pn>`_
   *  `sfx/explosion/shrikeolator <https://github.com/arescentral/antares-data/blob/master/objects/sfx/explosion/shrikeolator.pn>`_
   *  `sfx/explosion/small <https://github.com/arescentral/antares-data/blob/master/objects/sfx/explosion/small.pn>`_
   *  `sfx/explosion/supernova <https://github.com/arescentral/antares-data/blob/master/objects/sfx/explosion/supernova.pn>`_

*  Jump gate effects

   *  `sfx/jump/large <https://github.com/arescentral/antares-data/blob/master/objects/sfx/jump/large.pn>`_
   *  `sfx/jump/small <https://github.com/arescentral/antares-data/blob/master/objects/sfx/jump/small.pn>`_

Footnotes
---------

.. [#uns-evat] The Human Assault Transport launches Ishiman EVATs.

.. include:: epilog.rsti
.. -*- tab-width: 3; indent-tabs-mode: nil; fill-column: 72 -*-
