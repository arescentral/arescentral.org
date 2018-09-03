Object
======

.. sectnum::

Objects define everything with gameplay behavior attached. They are used
for ships, projectiles, bases, weapons, special effects, spawners and
everything else.

The objects defined in a plugin are often called “base objects”. They
define the initial properties of an object, like its health_ and
energy_, but once a real object is created from it, the attributes of
the real object can differ from the values it was based on.

There are five fundamental object types:

*  Rotations_, which are drawn as sprites that change when turning.
*  Animations_, which are drawn as sprites that change over time.
*  Rays_, which are drawn as lines between points in space.
*  Bolts_, which are drawn as moving lines.
*  Devices_, which are not drawn, and define weapons on other objects.

There is also a system of `templates <#template>`_ that helps manage
these distinctions.

`Example <https://github.com/arescentral/antares-data/blob/master/objects/ish/cruiser.pn>`_

.. contents::
   :local:
   :backlinks: none

Do I need it?
-------------

Probably.

Any new ships, weapons, or locations need to be defined by an object.
Also, if an existing object needs new behavior, then that new behavior
is usually defined by a new object.

On the other hand, it is possible to make a level pack entirely using
existing objects, in which case no new objects are needed.

Naming
------

Objects are in the ``objects`` directory and have a ``.pn`` extension.

By convention, all objects are within a directory named with a
three-letter code. The `factory scenario`_ uses a handful of
conventions:

*  Objects intended only as `templates <#template>`_ for other objects
   (and not to be used directly) are named ``tpl/(name)``.
   
   For example, these are the templates used to define the Ishiman
   heavy cruiser:

   *  ``tpl/any``
   *  ``tpl/oriented``
   *  ``tpl/ship``
   *  ``tpl/warship``
   *  ``tpl/hvc``

*  Ships associated with a race are within a directory with the same
   name as that race. If the ship is of a standard, buildable ship
   class, then the ship is named ``(race)/(class)``. If not, it is
   named ``(race)/etc/(type)`` or possibly
   ``(race)/etc/(type)/(description)``.
   
   For example, the following are all names of Ishiman ships:

   *  ``ish/fighter`` (standard Ishiman fighter)
   *  ``ish/hvc`` (standard Ishiman heavy cruiser)
   *  ``ish/etc/hvc/mod`` (modified HVC from |ch20|_)
   *  ``ish/etc/research`` (research vessel from |ch16|_)

*  Objects which represent fixed locations like planets and space
   stations are in the ``loc`` directory.
   
   Some examples:

   *  ``loc/planet``
   *  ``loc/outpost``
   *  ``loc/sun``

*  Devices and objects associated with them are in the ``dev``
   directory, grouped by weapon. The device is commonly named
   ``dev/(weapon)/gun`` or ``dev/(weapon)/turret``, and the projectile
   is commonly named ``dev/(weapon)/pulse`` or ``dev/(weapon)/beam``.
   
   For example, these are the objects associated with the Humans’
   Magneto Pulse Gun:

   *  ``dev/magneto/gun`` (standard launcher on Cruiser)
   *  ``dev/magneto/rgun`` (rapid launcher on Gunship and Carrier)
   *  ``dev/magneto/pulse`` (projectile)

*  Asteroids are in ``ast``.
  
   For example, these are the three asteroid sizes used in |ch08|_:

   *  ``ast/regular/big``
   *  ``ast/regular/medium``
   *  ``ast/regular/small``

*  Explosions and other special effects are in ``sfx``. These are
   generally visual and non-interactive.
   
   Some examples:

   *  ``sfx/gunsmoke``
   *  ``sfx/explosion/small``
   *  ``sfx/explosion/large``

   Among these are four very special objects, sometimes known as the
   “four blessed objects”. Antares uses these objects directly, but
   unless you’re doing something very special, it’s fine to use the
   versions from the factory scenario:

   *  ``sfx/warp/in``: the “_`warp in flare`”. Created when a ship
      enters warp speed.
   *  ``sfx/warp/out``: the “_`warp out flare`”. Created when a ship
      exits warp speed.
   *  ``sfx/crew``: the “_`castaway crew member`”. Created when a
      player’s flagship is destroyed, and becomes the player’s new
      flagship.
   *  ``sfx/energy``: the “_`energy blob`”. Created when an object with
      `destroy.release_energy <#destroy>`_ is destroyed, one blob for
      each 500 energy_ remaining.

*  Objects which are no longer used are moved to ``zzz``, or deleted.

Definition
----------

An object is a procyon_ file with the following fields:

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   template_             no    name_ of an object
   long_name_            yes   string_
   short_name_           yes   string_
   tags_                 no    tags_
   notes_                no    ignored
   `class, race`_        no    ignored
   portrait_             no    name_ of a picture_
   price_                yes   money_
   build_time_           yes   duration_
   health_               yes   integer_
   energy_               yes   integer_
   shield_color_         no    color_
   occupy_count_         yes   integer_
   mass_                 yes   number_
   max_velocity_         yes   speed_
   thrust_               yes   acceleration_
   warp_speed_           yes   speed_
   warp_out_distance_    yes   distance_
   turn_rate_            yes   `angular speed`_
   initial_velocity_     no    range_ of speeds_
   initial_direction_    yes   range_ of angles_
   autotarget_           yes   boolean_
   icon_                 no    icon_
   weapons_              no    weapons_
   destroy_              yes   destroy_
   expire_               yes   expire_
   create_               no    create_
   collide_              yes   collide_
   activate_             no    activate_
   arrive_               yes   arrive_
   target_               yes   target_
   rotation_             no    rotation_
   animation_            no    animation_
   ray_                  no    ray_
   bolt_                 no    bolt_
   device_               no    device_
   ai_                   yes   ai_
   ====================  ====  ========================================

template
~~~~~~~~

The name_ of another object. Antares merges together an object and its
template to get the final attributes for that object. For example, each
of the following objects uses the previous object as a template:

*  `tpl/any`_ (base template for any object)
*  `tpl/oriented`_ (object with a rotating sprite)
*  `tpl/ship`_ (oriented object that thinks and can be controlled)
*  `tpl/warship`_ (ship shown as triangles when zoomed out)
*  `tpl/hvc`_ (warship with medium shielding and attack power)
*  `ish/hvc`_ (HVC for Ishimans, with appropriate sprite and weapons)
*  `ish/etc/hvc/mod`_ (Ishiman HVC with Elejeetian weapons)

.. _tpl/any: https://github.com/arescentral/antares-data/blob/master/objects/tpl/any.pn
.. _tpl/oriented: https://github.com/arescentral/antares-data/blob/master/objects/tpl/oriented.pn
.. _tpl/ship: https://github.com/arescentral/antares-data/blob/master/objects/tpl/ship.pn
.. _tpl/warship: https://github.com/arescentral/antares-data/blob/master/objects/tpl/warship.pn
.. _tpl/hvc: https://github.com/arescentral/antares-data/blob/master/objects/tpl/hvc.pn
.. _ish/hvc: https://github.com/arescentral/antares-data/blob/master/objects/ish/hvc.pn
.. _ish/etc/hvc/mod: https://github.com/arescentral/antares-data/blob/master/objects/ish/etc/hvc/mod.pn

Antares merges together two maps_ key by key. If an object and its
template both have a value for some key, then it recursively merges the
values for that key. If only one has a value for some key, it takes that
value. When merging any other values, it takes the object’s value and
discards the template’s.

There are several `templates in the factory scenario`_ that make it
easier to create new objects.

.. _templates in the factory scenario: {filename}/plugins/format/templates.rst

long_name
~~~~~~~~~

A long-form string_ naming the object. It should be at most 25
characters, with words capitalized. It is displayed:

*  when a ship is newly selected
*  when a ship is destroyed
*  when a base is captured or lost
*  in the “Build” screen of the computer
*  in the object info displayed during mission briefings

Typical values are “Cruiser” or “Heavy Destroyer” for ships, and “PK
Beam” or “Fusion Pulse” for weapons.

short_name
~~~~~~~~~~

A short-form string_ naming the object. It should be at most 8
characters, with all letters capitalized. It is displayed as part of the
object info for a player’s control and target objects in the in-game
instruments.

Typical values are “CRUISER” or “HVDSTRYR” for ships, and “PKBEAM” or
“F PULSE” for weapons.

tags
~~~~

A tags_ map. An object’s tags can be referenced from:

*  An action’s if.tags_.
*  An object’s `ai.target.prefer.tags <#ai-target>`_.
*  An object’s `ai.target.force.tags <#ai-target>`_.
*  An object’s `ai.combat.engages.if.tags <#ai-combat>`_.
*  An object’s `ai.combat.engaged.if.tags <#ai-combat>`_.

.. _if.tags: {filename}/plugins/format/action.rst#if

notes
~~~~~

Notes about the object. Ignored by Antares, but kept around for
informational purposes. It might contain an annotated version of
long_name_, such as “Cruiser (no warp drive)” or “Transport (fleeing,
for chapter 9)”

class, race
~~~~~~~~~~~

Ignored by Antares, but kept around for informational purposes. These
used to be the way that ships were mapped to different races.

portrait
~~~~~~~~

The name_ of a picture_ representing this object. If a briefing_
references this object, this is the picture that the game displays.

price
~~~~~

The amount of money_ it takes to build this object.

build_time
~~~~~~~~~~

The duration_ of time it takes to build this object.

health
~~~~~~

The amount of shielding this object has. An object’s health is modified
when an object with `collide.damage <#collide>`_ hits it or through the
`heal action`_. Objects can also recharge their shields, converting
energy_ into health over time.

When an object’s health is reduced to zero, the object is `destroyed
<#destroy>`_.

.. _heal action: {filename}/plugins/format/action.rst#heal

energy
~~~~~~

The amount of energy this object has. An object also has a battery, with
5 times this amount of energy. Energy is used to:

*  fire weapons with an `energy cost <#device>`_.
*  enter and maintain `warp speed`_.
*  `recharge shields <#health>`_, up to half the maximum.
*  `restock ammo <#device>`_, up to half the maximum.

The battery is used to recharge the available energy.

shield_color
~~~~~~~~~~~~

A color_ shown when the object collides with another object. The
stronger the object’s remaining `shields <#health>`_, the more
completely the color covers the object’s sprite.

Good shield colors are ``"white"``, ``{indigo: 240}``, ``{gold: 240}``,
or a shade of 240 with any hue_ that contrasts with the ship’s sprite.

Only meaningful for objects with sprites (rotations_ and animations_).

occupy_count
~~~~~~~~~~~~

An integer_ used in conjunction with the `occupy action`_ to capture
objects. If the occupy action increases a player’s occupation counter
for this object past ``occupy_count``, that player captures the object.

Only meaningful if `destroy.neutralize <#destroy>`_ and `target.base
<#target>`_ are both true.

.. _occupy action: {filename}/plugins/format/action.rst#occupy

mass
~~~~

A number_ which determines how the object reacts to a collision.
Collisions are not realistic, as both objects in the collision will
bounce backward. The higher an object’s mass, the slower its new
velocity will be after the collision.

Values are typically very small: cruisers have a mass of 1.0, the
smallest ships, such as fighters, have 0.8, and the largest, such as
carriers and gateships, have 2.0.

max_velocity
~~~~~~~~~~~~

The maximum speed_ of the object. Thrust_ cannot accelerate an object
past its max_velocity, but other sources of velocity can, such as
initial_velocity_ or the `push action`_. If zero, the object is
completely stationary, and nothing can move it.

Most ships have a ``max_velocity`` between 3.0 and 7.0.

.. _push action: {filename}/plugins/format/action.rst#push

thrust
~~~~~~

The amount of acceleration_ an object can apply. Thinking objects decide
whether or not they want to accelerate. Non-thinking objects always
apply full thrust.

Most ships have a ``thrust`` between 0.008 and 0.156.

.. _warp speed:

warp_speed
~~~~~~~~~~

The speed_ of the object when traveling at warp speed. If zero, the
object cannot enter warp.

Only meaningful for thinking objects.

warp_out_distance
~~~~~~~~~~~~~~~~~

The distance_ at which an object will start to exit warp in order to
arrive at its target. Objects with a high max_velocity_, high
warp_speed_, or low thrust_ should have a large ``warp_out_distance``.

Most ships have a ``warp_out_distance`` between 1000 and 7200.

Only meaningful for objects with a warp_speed_.

turn_rate
~~~~~~~~~

The rate at which an object can turn. If zero, the object cannot turn.
If null, the object has no facing at all, and always applies thrust in
the direction of its nearest enemy.

Most ships have a ``turn_rate`` between 1.0 and 3.0.

initial_velocity
~~~~~~~~~~~~~~~~

A range_ of possible speeds_ for the object at its time of creation. If
zero, the object is initially stationary. If null, its max_velocity_ is
used. If a range, a velocity is chosen at random.

Generally, ``initial_velocity`` should be null, to defer to
max_velocity_. Two exceptions are:

*  Projectiles that start slow and accelerate after creation, such as
   the `Onas Pulse`_.
*  Projectiles that are inaccurate and start at random speeds, such as
   `Flak`_.

.. _Onas Pulse: https://github.com/arescentral/antares-data/blob/master/objects/dev/onas/pulse.pn
.. _Flak: https://github.com/arescentral/antares-data/blob/master/objects/dev/flak/pulse.pn

initial_direction
~~~~~~~~~~~~~~~~~

A range_ of angles_ indicating the possible directions for the object at
its time of creation. The initial direction may be relative to some
other direction, depending on how it was created.

Typical values are:

*  ``{begin: 0, end: 360}`` for ships, meaning any random direction
*  ``0``, for accurate projectiles from guns and turrets
*  ``{begin: -3, end: 4}``, for projectiles that are inaccurate up to
   ±3°.

autotarget
~~~~~~~~~~

If true, this object is created facing its nearest enemy. If
initial_direction_ is not 0, it will be added, making the turret
somewhat inaccurate.

icon
~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   shape                 yes   “square”, “triangle”, “diamond”, or
                               “plus”
   size                  yes   integer_
   ====================  ====  ========================================

Determines the icon shown when the zoom level is 1:16 or smaller. The
actual pixel size of the icon will be about twice ``icon.size``.

weapons
~~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   pulse.base            yes   name_ of an object_
   pulse.positions       yes   array_ of points_
   beam.base             yes   name_ of an object_
   beam.positions        yes   array_ of points_
   special.base          yes   name_ of an object_
   special.positions     yes   array_ of points_
   ====================  ====  ========================================

Up to three weapons mounted on the ship. The names ``weapons.pulse``,
``weapons.beam``, and ``weapons.special`` refer to weapon 1, weapon 2,
and the special weapon of a ship, respectively.

A weapon’s ``base`` must be a device_. When a ship activates one of its
weapons, it executes that weapon’s `activate.action <#activate>`_ with
the nearest enemy as the `direct object`_. The weapon itself is never
created, though the weapon’s activate.action usually executes a `create
action`_ to create a projectile.

Each weapon can have up to three positions. These allow the ship to fire
from different parts of its sprite, such as its cannons. These positions
rotate with the ship. A `(+x, +y)` value would be in the rear right of
the ship, and a `(–x, –y)` value would be in the front left. If omitted,
the weapon fires from the center of the ship.

Only thinking objects use weapons, but a `fire action`_ could explicitly
activate a non-thinking object’s weapons.

.. _fire action: {filename}/plugins/format/action.rst#fire
.. _create action: {filename}/plugins/format/action.rst#create

destroy
~~~~~~~

An object’s destroy block specifies how it should act when its health_
is reduced to zero.

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   die                   yes   boolean_
   neutralize            yes   boolean_
   release_energy        yes   boolean_
   action                yes   array_ of actions_
   ====================  ====  ========================================

If ``destroy.neutralize`` is true, then the object’s owner loses control
of it, and the object is restored to full health_. After it becomes
neutral, it executes its ``destroy.action`` with itself as the `direct
object`_. Until it gains a new owner, the object won’t participate in
combat.

If ``destroy.neutralize`` is false, then:

*  If ``destroy.release_energy`` is true, the object releases one
   `energy blob`_ for every 500 energy_ remaining,
*  The object executes its ``destroy.action`` with itself as the
   `direct object`_, and
*  If ``destroy.die`` is true, the object removes itself from play.

expire
~~~~~~

Many (most) objects are not permanent and dissappear after some time.
The expire block determines when and how they should disappear.

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   after.age             no    range_ of durations_
   after.animation       yes   boolean_
   die                   yes   boolean_
   action                yes   array_ of actions_
   ====================  ====  ========================================

If ``expire.after.age`` is not null, the object is given a random age
in that range_ at creation. After this length of time (unless modified
by the `age action`_), the object expires. This is useful for
projectiles that should travel some distance and then disappear.

If ``expire.after.animation`` is true, and the object is an animation_,
then the object expires after its animation completes, instead of
cycling. This is useful for effects like explosions that should
disappear at the end of their animation.

When an object expires, it executes its ``expire.action`` with itself as
the `direct object`_. Then, if ``expire.die`` is true, it removes itself
from play.

.. note:: there is a separate meaning of ``expire.action`` used by the
   `land action`_.

.. _age action: {filename}/plugins/format/action.rst#age
.. _land action: {filename}/plugins/format/action.rst#land

create
~~~~~~

The create block specifies actions that takes place when an object is
created.

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   action                yes   array_ of actions_
   ====================  ====  ========================================

When an object is created, it executes its ``create.action`` with itself
as the `direct object`_.

collide
~~~~~~~

The collide block specifies when and how an object should hit other
objects and be hit by them.

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   as.subject            yes   boolean_
   as.direct             yes   boolean_
   solid                 yes   boolean_
   edge                  yes   boolean_
   damage                yes   integer_
   action                yes   array_ of actions_
   ====================  ====  ========================================

When two objects overlap, they collide if one object’s
``collide.as.subject`` is true and the other’s ``collide.as.direct`` is
true. The `subject object`_ will:

*  Deduct its ``collide.damage`` from the `direct object`_’s health_.
*  Interrupt the direct object’s cloaking.
*  Execute its ``collide.action`` with the other object as its direct
   object (or itself if the ``collide.damage`` was enough to destroy
   the other object).
*  Flash the screen, if the collision did damage to the local
   player’s flagship.

If both objects’s ``collide.as.subject`` and ``collide.as.direct`` are
true, then the collision then happens in the other direction. After
that, if both objects’ ``collide.solid`` is true, then the objects
bounce away from each other according to their mass.

If ``collide.edge`` is true, then the object will bounce off the edge of
the universe instead of passing through it. Thinking, permanent objects
such as ships should set ``collide.edge`` to true, and temporary objects
like projectiles should set it to false.

activate
~~~~~~~~

Some objects execute actions periodically. The activate block determines
when and how they do so. The activate action is also used by devices_.

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   period                no    range_ of durations_
   action                yes   array_ of actions_
   ====================  ====  ========================================

If ``activate.period`` is not null, then the object will periodically
activate. Each time, a random duration from ``activate.period`` is
chosen. After that duration, the object executes its ``activate.action``
with itself as the `direct object`_.

Weapons_ can also be activated. When a ship activates one of its
equipped weapons, it executes that weapon’s ``activate.action`` with
itself as the `subject object`_ and its nearest foe as the `direct
object`_.

arrive
~~~~~~

Some actions execute actions when they reach certain targets. The arrive
block determines when and how they take action.

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   distance              yes   distance_
   action                yes   array_ of actions_
   ====================  ====  ========================================

When an object is within ``arrive.distance`` of its target, it executes
its ``arrive.action`` with its target as the `direct object`_. The
object won’t execute it again until after receiving a new target.

It’s not usually useful for an object to react identically when it
reaches every target, so an ``arrive.action`` usually specifies
if.tags_.

.. _if.tags: {filename}/plugins/format/action.rst#if

target
~~~~~~

An object’s target block determines how it interacts with selection and
orders.

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   base                  yes   boolean_
   hide                  yes   boolean_
   radar                 yes   boolean_
   order                 yes   boolean_
   select                yes   boolean_
   lock                  yes   boolean_
   ====================  ====  ========================================

If ``target.base`` is true, then this object is a planet, station, or
other strategic location. Bases are selected with the “select base” key
instead of “select friendly” or “select foe”.

If ``target.hide`` is true, then this object hides nearby objects when
zoomed out to 1:16 or further. It does not objects friendly to it or
bases. Unless a player also has a nearby object, that player cannot
select objects in this object’s vicinity.

If ``target.radar`` is true, then this object appears on the player’s
radar when nearby.

If ``target.order`` is true, then this object can have a target. Without
this, ``target.lock`` is probably not meaningful.

If ``target.select`` is true, then this object can be selected. Without
this, ``target.base`` and ``target.order`` are probably not meaningful.

If ``target.lock`` is true, then this object can accept a new target
when selected by a player and given an order.

.. _rotations:

rotation
~~~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   sprite                yes   name_ of a sprite_
   layer                 yes   1, 2, or 3
   scale                 yes   number_
   frames                yes   range_ of integers_
   ====================  ====  ========================================

A rotation has a ``rotation.sprite`` and picks a frame to display based
on the orientation of the object. The angles_ [0, 360) are mapped to
``rotation.frames``. In order to ensure that the object’s rotation is
smooth, the sprite should have at least 24 frames.

The object’s sprite is scaled up or down according to
``rotation.scale``. At 1:1 zoom, a sprite with a scale of 1.0 displays
at its original size. A scale of 2.0 makes it twice as large, and a
scale of 0.5 halves the size.

Sprites are drawn in layers. Layer 1 is for background objects like
planets and stations. Layer 2 is for ships. Layer 3 is for foreground
objects like projectiles and explosions.

.. _animations:

animation
~~~~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   sprite                yes   name_ of a sprite_
   layer                 yes   1, 2, or 3
   scale                 yes   number_
   frames                yes   range_ of numbers_
   direction             yes   “+”, “-”, or “?”
   speed                 yes   number_
   first                 yes   range_ of numbers_
   ====================  ====  ========================================

An animation has an ``animation.sprite`` and changes its frame over
time. the frame cycles within ``animation.frames`` [#animation-frames]_
(or expires at the end if `expires.after.animation <#expire>`_ is true)

The animation cycles at ``animation.speed`` frames per tick_. If
``animation.direction`` is ``"+"``, the frame index increases over time.
If ``"-"``, the frame index decreases over time. If ``"?"``, each object
chooses between ``"+"`` and ``"-"`` randomly.

The animation starts with a random frame from within
``animation.first``. This is usually set to  either 0 (start at the
first frame) or the same as ``animation.frames`` (start at any random
frame in the animation).

An animation’s sprite has a ``animation.layer`` and ``animation.scale``.
These function the same as in rotation_.

.. _tick: {filename}/plugins/format/types.rst#duration

ray
~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   hue                   no    hue_
   to                    yes   “object” or “coord”
   lightning             yes   boolean_
   accuracy              yes   distance_
   range                 yes   distance_
   ====================  ====  ========================================

Rays are drawn as lines between two points in space. The origin point is
locked to the object that created the ray (typically a ship firing a
weapon). The end point (``ray.to``) is either locked to a nearby foe
(``"object"``, like the Salrilian Carrier’s T-Space Bolt) or to the
relative point a foe occupied at the time the ray was created
(``"coord"``, like the Audemedon Carrier’s Trazer Beam).

The ray shimmers, taking on different shades of ``ray.hue``.

The distance from origin to end point may be at most ``ray.range``. If
``ray.accuracy`` is non-zero and ``ray.to`` is ``"coord"``, a random
distance up to ``ray.accuracy`` is added to the ray’s end point.

If ``ray.lightning`` is true, extra zigzags are added to give the ray
the appearance of a lightning bolt.

Rays are drawn on top of all sprites.

.. _bolts:

bolt
~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   color                 yes   color_
   ====================  ====  ========================================

A ray is drawn as a moving line of a given ``bolt.color``. The faster
the bolt moves, the longer the line.

Bolts are drawn on top of all sprites.

.. _devices:

device
~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   usage.attacking       yes   boolean_
   usage.defense         yes   boolean_
   usage.transportation  yes   boolean_
   fire_time             yes   duration_
   energy_cost           yes   integer_
   ammo                  yes   integer_
   restock_cost          yes   integer_
   range                 yes   distance_
   speed                 yes   speed_
   direction             yes   “fore” or “omni”
   ====================  ====  ========================================

Devices are not drawn at all. They define weapons_ wielded by other
objects. Generally, the only attributes meaningful for a device are its
names, ``activate.action``, and ``device`` block.

``device.usage`` determines when an CPU pilot will activate the device:

*  ``device.usage.attacking``: if true, activates this device when the
   wielder has a hostile ship in its sights.
*  ``device.usage.defense``: if true, activates when the wielder is in
   the sights of a hostile ship.
*  ``device.usage.transportation``: if true, and the device is equipped
   as ``weapons.special``, activates when the wielder wants to go a long
   distance, similarly to its warp drive.

``device.fire_time`` determines how long must pass after each
activation before the device can be activated again.

If ``device.energy_cost`` is non-zero, the device consumes that much
energy_ with each activation, and the wielder must have at least that
much energy to activate it.

If ``device.ammo`` is non-zero, the device has a limited number of
charges, and the wielder must have at least one charge remaining to
activate it. If ``device.restock_cost`` is non-zero, then the wielder
can restock the charges, up to half ``device.ammo``, by consuming
``device.restock_cost`` energy_ for each charge.

The values of ``device.range``, ``device.speed``, and
``device.direction`` depend on the objects created by the device’s
``activate.action``. They are used as hints to CPU pilots about how to
use the weapon, and don’t control the weapon’s actual parameters.

Projectile weapons
``````````````````

A device is a projectile weapon if it creates rotations_, animations_,
or bolts_ as projectiles. These weapons take time to hit their target,
so CPU pilots need to know how to adjust their aiming.

``device.speed`` is the projectile’s velocity. If the device doesn’t
have a fixed velocity, it should be an average velocity.

``device.range`` is the furthest distance_ that the weapon can hit. It
is typically the projectile’s `velocity <#max-velocity>`_ × `age
<#expire>`_. If the device doesn’t have a fixed velocity, or expires in
some other manner than ``expire.after.age``, calculating it may be more
involved.

If the projectile’s autotarget_ is true, then the weapon’s
``device.direction`` is “omni”. Otherwise, it is “fore”.

Ray weapons
```````````

A device is a ray weapon if it creates `rays <#ray>`_ as projectiles.
These weapons hit targets in any direction instantaneously.

``device.range`` should match the projectile’s ``ray.range``.

``device.speed`` should be ``inf`` (infinite speed), as no aiming
correction is required.

``device.direction`` should be “omni”.

Direct weapons
``````````````

A device is a direct weapon if it doesn’t create a projectile at all,
like the Cantharan gateship’s `Electronic Jammer`_. These weapons act
directly on the nearest foe.

``device.range`` should be the furthest effective range of the weapon.
``device.speed`` should be ``inf``. ``device.direction`` should be
“omni”.

.. _Electronic Jammer: https://github.com/arescentral/antares-data/blob/master/objects/dev/jammer/device.pn

Non-weapons
```````````

Not every device is intended for shooting enemies. Some examples of
non-weapons are:

*  `Stealth fields <https://github.com/arescentral/antares-data/blob/master/objects/dev/stealth/item.pn>`_
*  `Launching bays <https://github.com/arescentral/antares-data/blob/master/objects/dev/bay/ish.pn>`_
*  `Assault teams <https://github.com/arescentral/antares-data/blob/master/objects/dev/assault/uns.pn>`_

For stealth fields and launching bays, ``device.range`` is still
relevant. It determines how near an enemy ship need be before the
wielder feels threatened and activates the device. ``device.speed`` and
``device.direction`` are not relevant, as the wielder doesn’t need to
aim.

For assault teams, none of the three fields are relevant, as the weapon
is fired only as part of ``arrive.action``, never by a CPU pilot.

ai
~~

An object’s AI block determines how CPU players and pilots handle the
object. It is generally meaningful only for thinking objects.

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   combat                yes   ai.combat_
   target                yes   ai.target_
   escort                yes   ai.escort_
   build                 yes   ai.build_
   ====================  ====  ========================================

ai.combat
`````````

The AI combat block determines how a CPU pilot handles the object in
battle.

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   hated                 yes   boolean_
   guided                yes   boolean_
   engages               yes   boolean_ or map_
   engages.if.tags       yes   tags_
   engaged               yes   boolean_ or map_
   engaged.if.tags       yes   tags_
   evades                yes   boolean_
   evaded                yes   boolean_
   skill.num             yes   integer_
   skill.den             yes   integer_
   ====================  ====  ========================================

The main purpose of the AI combat block is to determine whether an
object:

*  `hates` another object (enters combat with it)
*  `engages` another object (attempts to shoot it)
*  `evades` another object (runs away when threatened by it)

A defending object `hates` any nearby hostile object which has its
``ai.combat.hated`` flag set to true. This object will not shoot at a
hated object unless it also engages it (and has weapons to engage it
with). Instead, it will attempt to get close to that object and touch
it. This is used for the `energy blob`_.

An attacking object `engages` an object that it hates, attempting to
shoot it, if the attacking object’s ``ai.combat.engages`` and the
defending object’s ``ai.combat.engaged`` fields allow. This requires:

*  Either:

   *  The attacking object’s ``ai.combat.engages`` is true, or
   *  The attacking object’s ``ai.combat.engages.if.tags`` match_ the
      defending object; and

*  Either:

   *  The defending object’s ``ai.combat.engaged`` is true, or
   *  The defending object’s ``ai.combat.engaged.if.tags`` match_ the
      attacking object.

.. _match: {filename}/plugins/format/types.rst#tags

A defending object `evades` any nearby hostile object if the attacking
object is facing it, the attacking object’s ``ai.combat.evaded`` is
true, and the defending object’s ``ai.combat.evades`` is true.

If ``ai.combat.guided`` is true, the object steers towards hostiles, but
may lose track of a hostile object if it is no longer in front of the
guided object.

``skill.num`` and ``skill.den`` introduce some randomness into an CPU
pilot’s actions. Whenever a CPU pilot wants to press a virtual key, the
likelihood that the keypress succeeds is ``skill.num / skill.den``. The
default of 3/21 should be kept for most thinking objects.

ai.target
`````````

The AI target block determines how a CPU player assigns targets to the
object.

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   prefer.base           no    boolean_
   prefer.local          no    boolean_
   prefer.owner          yes   “any”, “same”, or “different”
   prefer.tags           yes   tags_
   force.base            no    boolean_
   force.local           no    boolean_
   force.owner           yes   “any”, “same”, or “different”
   force.tags            yes   tags_
   ====================  ====  ========================================

If ``prefer.base`` is true, a CPU player prefers to assign targets with
``target.base: true``. If ``force.base`` is true, a CPU player *only*
assigns targets with ``target.base: true``.

If ``prefer.local`` is true, a CPU player prefers to assign targets in
the vicinity of this object. If ``force.local`` is true, a CPU player
*only* assigns targets in the vicinity of this object.

If ``prefer.owner`` is ``"same"``, a CPU player prefers to assign
friendly targets. If ``"different"``, a CPU player prefers to assign
hostile targets. If ``force.owner`` is either value, a CPU player *only*
assigns such targets.

If ``prefer.tags`` is non-empty, a CPU player prefers to assign targets
with `matching tags`_. If ``force.tags`` is non-empty, a CPU player
*only* assigns targets with matching tags.

.. _matching tags: {filename}/plugins/format/types.rst#tags

ai.escort
`````````

The AI escort block determines how a CPU player assigns escorts to
friendly objects.

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   class                 yes   integer_
   power                 yes   number_
   need                  yes   number_
   ====================  ====  ========================================

An object is only ever assigned escorts with a lower ``ai.escort.class``
than its own. This prevents the possibility of a carrier escorting a
fighter, for example. Sample values are 1 (fighters), 3 (cruisers), 5
(gunships), 7 (carriers), 9 (transports), and 10 (planets).

When determining whether an object needs escorts, a CPU player compares
that object’s ``ai.escort.need`` to the sum of the ``ai.escort.power``
of friendly objects in its vicinity. If the friendly escort power does
not meet the need, the CPU player attempts to add more escorts.

ai.build
````````

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   ratio                 yes   number_
   needs_escort          yes   boolean_
   legacy_non_builder    yes   boolean_
   ====================  ====  ========================================

When deciding what to build, a CPU player considers all options, and
picks one randomly with a likelihood proportional to each object’s
``ai.build.ratio``. It won’t build anything it can’t assign a target to
(per ``ai.target.force``), but otherwise isn’t any smarter about what it
builds.

If ``ai.build.needs_escort`` is true, then a CPU player won’t build a
second object of this type until the first one’s ``ai.escort.need`` is
satisfied.

(use of ``legacy_non_builder`` [#ai-build-legacy-non-builder]_ fields is
not recommended. It exists only for compatibility with some Hera-created
scenarios)

Footnotes
---------

.. [#animation-frames] In the `factory scenario`_, most animations’
   ``frames`` are something like ``{begin: 0.0, end: 5.004}`` for a
   six-frame animation. This is not recommended. It actually preserves
   a bug in Ares, where the last frame would be shown too briefly. In
   this example, it should be ``{begin: 0, end: 6}`` for a six-frame
   animation, but fixing it would break compatibility.
.. [#ai-build-legacy-non-builder] In Antares, all ``target.base``
   objects can build ships. In Ares, this was usually the case, and
   ``legacy_non_builder`` preserves the exceptions. This matters because
   CPU players roll a die for each build object to determine what to
   build, and compatibility requires rolling the same dice in the same
   order. ``legacy_non_builder`` tells Antares not to roll a die even if
   ``target.base`` is true.

.. _subject object: {filename}/plugins/format/action.rst#direct-object
.. _direct object: {filename}/plugins/format/action.rst#direct-object
.. include:: epilog.rsti
.. -*- tab-width: 3; indent-tabs-mode: nil; fill-column: 72 -*-
