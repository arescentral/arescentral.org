Action
======

.. sectnum::

An `action sequence`_ is triggered by an object_ or condition_ to make
things happen. There are many types_ of actions, such as capture_,
create_, destroy_, and win_.

For example, if a transport lands on a planet, it triggers a capture_
action that changes the planet’s owner. Then, if a condition_ sees the
ownership change, it could trigger a win_ action, ending the level_ in
victory for the new owner.

.. contents::
   :local:
   :backlinks: none

What, Where, When, How
----------------------

What
~~~~

In any given action, there are two objects with different roles:

*  A _`subject object`. The subject object is normally the one acting
   in an action. When a missile collides with a ship, the missile is
   the subject object. When a transport lands on a planet, the
   transport is the subject object.
*  A _`direct object`. The direct object is usually the one acted upon
   by the action. When a missile collides with a ship, the ship is the
   direct object. When a transport lands on a planet, the planet is the
   direct object.

Most actions are defined in terms of what they do to these objects. In a
capture_ action, the subject object captures the direct object.

Actions can also be reflexive_. This swaps the roles of the subject
object and direct object. In a reflexive capture_ action, the subject
object is captured by the direct object.

Where
~~~~~

Actions take place at a location. Normally, this is the center of the
`direct object`_ (or `subject object`_ if reflexive_). When a missile
collides with a ship, the location is at the center of the ship.

One exception: when a weapon fires, that action takes place at the
`weapon’s positions`_ on the firing ship, rather than the center of the
ship.

.. _weapon’s positions: {filename}/plugins/format/object.rst#weapons

When
~~~~

Every condition_ has an associated action. If the condition becomes
true, it executes its action with its subject object and direct object.

An object_ can have up to six different actions. It is always the
`subject object`_ for its own actions, but the `direct object`_ depends
on the action:

.. table::
   :widths: auto

   =========================  =================  =================
   Action                     subject object     direct object
   =========================  =================  =================
   create.action_             self               self
   destroy.action_            self               self
   expire.action_             self               self
   expire.action_ (land_)     self               object’s target
   collide.action_            self               collided object
   activate.action_           self               self
   activate.action_ (weapon)  self               nearest foe
   arrive.action_             self               object’s target
   =========================  =================  =================

.. _activate.action: {filename}/plugins/format/object.rst#activate
.. _arrive.action: {filename}/plugins/format/object.rst#arrive
.. _collide.action: {filename}/plugins/format/object.rst#collide
.. _destroy.action: {filename}/plugins/format/object.rst#destroy
.. _create.action: {filename}/plugins/format/object.rst#create
.. _expire.action: {filename}/plugins/format/object.rst#expire

How
~~~

All actions come in arrays_, which together make up an _`action
sequence`. Actions in a sequence execute one after another until the
whole sequence has executed.

If there is a delay_ action, that postpones the remainder of the
sequence until the delay duration finishes.

It’s possible for an action from one sequence to trigger another action
sequence. In this case, the second action sequence will run to
completion, and then the first action sequence will resume. For example,
if a gun’s activate.action_ creates a bullet and gunsmoke, then the
bullet’s create.action_ will run before the gun creates the gunsmoke.

Definition
----------

An action is a procyon_ value with the following fields, plus any fields
appropriate to its type_:

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   type_                 yes   “age_”, “assume_”, “cap_speed_”,
                               “capture_”, “check_”, “cloak_”,
                               “condition_”, “create_”, “delay_”,
                               “destroy_”, “disable_”, “energize_”,
                               “equip_”, “fire_”, “flash_”, “group_”,
                               “heal_”, “hold_”, “key_”, “land_”,
                               “message_”, “morph_”, “move_”,
                               “occupy_”, “pay_”, “play_”, “push_”,
                               “remove_”, “reveal_”, “score_”,
                               “select_”, “spark_”, “spin_”, “target_”,
                               “thrust_”, “warp_”, “win_”, or “zoom_”
   reflexive_            no    boolean_
   if_                   no    filter_
   override_             no    override_
   ====================  ====  ========================================

reflexive
~~~~~~~~~

If ``reflexive`` is true, then the roles of the `subject object`_ and
`direct object`_ are swapped.

For example, if an missile hits a ship and explodes, its collide action
needs a create_ action to create the explosion and a remove_ action to
remove the missile. The create_ action should be reflexive_, so that the
explosion is centered on the missile, not the ship. The remove_ action
should also be reflexive, so that it removes the missile, not the ship.

.. _filter:

if
~~

Each action can have filters set on it. If the `direct object`_ does not
match an action’s filters, the action sequence skips that action. The
following fields are supported:

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   tags                  no    tags_
   owner                 no    “any”, “same”, or “different”
   attributes            no    attributes
   ====================  ====  ========================================

If override.direct_ is used, the filters apply to the new direct object.
However, reflexive_ doesn’t make the filters apply to the `subject
object`_; they still apply to the direct object.

For example, a transport’s “arrive” action specifies:

.. include:: pn/action-if.pn
   :code: procyon

This ensures that the transport only attempts to land on a hostile
planet. It will never:

*  land on a station, flak drone, ship, or other non-planet, because of
   the tag filter, or
*  land on a friendly planet, because of the owner filter.

(use of the ``attributes`` [#attributes]_ field is not recommended. It
exists only for compatibility with some Hera-created scenarios)

.. _override.direct:

override
~~~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   subject               no    `object reference`_
   direct                no    `object reference`_
   ====================  ====  ========================================

Executes the action on a different `subject object`_ or `direct object`_
from the default. This can be used in level-specific actions to operate
on a level’s initial_ objects.

For example, in |ch16|_, overrides are used to order both escort ships
to attack. One action’s ``override.subject`` is the first escort, and
the following action’s ``override.subject`` is the second escort.

Overrides only affect their own action. Subsequent actions in the action
sequence use the original objects.

.. _type:

Types
-----

There are many different types of actions. Most actions have additional
fields according to their type. The action types are:

.. table::
   :widths: auto

   ==========  =======================================================
   Type        Description
   ==========  =======================================================
   age_        modifies the time before an object expires_
   assume_     turns an object into an initial_ object
   cap_speed_  modifies an object’s max_velocity_
   capture_    modifies an object’s owner
   check_      causes conditions_ to be re-checked
   cloak_      makes an object invisible
   condition_  enables or disable conditions_
   create_     creates objects
   delay_      delays execution of an `action sequence`_
   destroy_    destroys an object
   disable_    impairs an object’s controls
   energize_   modifies an object’s energy_
   equip_      modifies an object’s weapon_
   fire_       triggers an object’s weapon_
   flash_      causes the player’s screen to flash
   group_      executes multiple actions
   heal_       modifies an object’s health_
   hold_       orders an object to hold position
   key_        enables or disable a player’s controls
   land_       causes an object to land on its target
   message_    displays a message to the player
   morph_      changes an object from one type to another
   move_       modifies an object’s location
   occupy_     modifies the occupation count of an object
   pay_        modifies a player’s money_
   play_       plays a sound_
   push_       modifies an object’s velocity
   remove_     removes an object from existence
   reveal_     shows a hidden initial_ object
   score_      modifies a player’s score counters
   select_     selects the screen and line of a player’s computer
   slow_       decreases an object’s velocity
   spark_      creates a sparkly visual effect
   |speed|__   modifies an object’s velocity
   spin_       imparts spin to an object
   stop_       zeroes an object’s velocity
   target_     orders an object to target another object
   thrust_     imparts thrust to an object
   warp_       causes an object to enter warp speed
   win_        ends the level in victory or loss
   zoom_       sets the player’s zoom level
   ==========  =======================================================

.. _max_velocity: {filename}/plugins/format/object.rst#max-velocity
.. _energy: {filename}/plugins/format/object.rst#energy
.. _health: {filename}/plugins/format/object.rst#health
.. _weapon: {filename}/plugins/format/object.rst#weapons
.. _expires: {filename}/plugins/format/object.rst#expire

age
~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   relative              no    boolean_
   value                 yes   range_ of durations_
   ====================  ====  ========================================

Modifies the `direct object`_’s expire.after.age_. Picks a random
duration from ``value``. If ``relative`` is ``true``, adds that duration
to the object’s age. Otherwise, sets the object’s age to that duration.

.. _expire.after.age: {filename}/plugins/format/object.rst#expire

assume
~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   which                 yes   integer_
   ====================  ====  ========================================

Causes the `direct object`_ to become an initial_ object. Adds the first
counter_ of the first player to ``which``, and gives the object the
resulting initial object number.

.. warning:: Assume actions were created for the tutorial and are not
   well-suited to other uses. Talk to antares-dev_ before using.

cap_speed
~~~~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   value                 no    speed_
   ====================  ====  ========================================

Sets the `direct object`_’s max_velocity_. If ``value`` is null, then
sets the direct object’s max_velocity to its default value.

capture
~~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   player                no    index_ of a player
   ====================  ====  ========================================

Changes the owner of the `direct object`_:

*  If ``player`` is null, sets the owner of the `direct object`_ to the
   owner of the `subject object`_.
*  If not, sets the owner of the `direct object`_ to ``player``.

check
~~~~~

Causes all conditions_ to be re-checked, possibly triggering their own
action sequences.

Checking conditions isn’t free, so this action should only be used when
it’s likely that a condition became true, such as after modifying a
player’s score_. [#check]_

Check actions have no additional fields.

cloak
~~~~~

Causes the `direct object`_ to become invisible. The cloak action can
affect any object, even one that doesn’t have a cloaking device. The
object will decloak if it uses its pulse or beam weapon, but not if it
uses its special weapon.

Cloak actions have no additional fields.

condition
~~~~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   enable                no    array_ of indexes_ of conditions_
   disable               no    array_ of indexes_ of conditions_
   ====================  ====  ========================================

Enables all of the conditions_ listed in ``enable`` and disables the
ones in ``disable``. This can be used to script a situation in which
events need to happen in sequence.

For example, if the player needs to visit two planets in a specific
order, there could be two conditions, with the latter disabled. Upon
visiting Example Alpha, the first condition would enable the second.
Upon visiting Example Beta, the second condition would declare victory.
(if the order doesn’t matter, using the score_ action might be easier)

Condition indexes_ are tied to a particular level_, so the condition
action should generally be used by other conditions, not by objects_.

create
~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   base                  yes   name_ of an object_
   count                 no    range_ of integers_
   relative_velocity     no    boolean_
   relative_direction    no    boolean_
   inherit               no    boolean_
   distance              no    distance_
   within                no    “circle” or “square”
   legacy_random         no    boolean_
   ====================  ====  ========================================

Creates ``count`` new objects_ of type ``base``, centered on the `direct
object`_.

If ``count`` is null, creates 1 new object. If ``count`` is a range,
picks a count randomly within the range, and creates nothing if the
result is ≤0. For example, ``count: {begin: 1, end: 6}`` means to
randomly create at least 1 and at most 5 new objects. ``count: {begin:
-4, end: 2}`` means to create a new object with a 1 in 6 chance.

If ``relative_velocity`` is true, adds the current velocity of the
direct object to that of the new objects. If ``relative_direction``
is true, adds the current direction of the direct object. Guns should
set ``relative_direction`` when creating their projectiles. Turrets
should set ``autotarget`` on their projectiles and not set
``relative_direction``.

If ``inherit`` is set, the new object’s is ordered to target the direct
object’s target. Otherwise, the new object is ordered to target the
direct object. If the object is neutral or its target.order_ is false,
then its target is cleared.

If ``distance`` is set, the new objects will be created at random
distances up to the given amount.

(use of the ``within`` [#create-within]_ and ``legacy_random``
[#create-legacy-random]_ fields is not recommended. They exist only for
compatibility with some Hera-created scenarios)

.. _target.order: {filename}/plugins/format/object.rst#target

delay
~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   duration              yes   duration_
   ====================  ====  ========================================

Postpones further processing of the current `action sequence`_ until
``duration`` has passed. [#delay]_

.. warning:: Use sparingly. The delay action is potentially expensive.
   It can slow the game down or eat up memory due to the extra cost of
   maintaining the action queue.

destroy
~~~~~~~

Destroys the `direct object`_. If the direct object has a
destroy.action_, executes its destroy.action. Then, unless the direct
object’s destroy.die_ is true, removes it from existence.

Destroy actions have no additional fields.

.. _destroy.die: {filename}/plugins/format/object.rst#destroy

disable
~~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   duration              yes   range_ of durations_
   ====================  ====  ========================================

Impairs control of the `direct object`_ for some length of time. Only
meaningful for objects that think and attempt to control their movement
(including players’ flagships). While control is impaired, there’s a
chance that a pressed or released key might not register.

Takes a random duration_ in ``duration`` and divides it by the direct
object’s mass. The direct object’s controls are impaired for this long.
If the direct object’s controls were already impaired, the old remaining
duration is replaced by the new duration.

If the remaining time an object is disabled is `d`, the likelihood that
a key will fail to register is `(d – ¼) ÷ d`. Turning is disabled for
the full duration.

For example, a Zerbilite’s collide.action_ has a disable action with
``duration: {begin: "0s", end: "3s"}``. If a Zerbilite collides with an
Ishiman carrier (``mass: 2.0``), it will disable the carrier for up to
1.5 seconds. If it disables the carrier for the full 1.5 seconds, the
carrier will initially ignore ⅚ of keypresses, and regain control over
time.

energize
~~~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   value                 yes   integer_
   ====================  ====  ========================================

Increases the current energy_ of the `direct object`_ by ``value``. If
that would increase the object’s energy past full, the balance is added
to the object’s battery.

equip
~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   which                 yes   “pulse”, “beam”, or “special”
   base                  yes   name_ of an object_
   ====================  ====  ========================================

Replaces one of the `direct object`_’s weapons. Sets the weapon ``which``
to ``base``, restoring it to full ammunition.

.. warning:: Untested and unsupported, for now. Talk to antares-dev_
   before using.

fire
~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   which                 yes   “pulse”, “beam”, or “special”
   ====================  ====  ========================================

Fires one of the `direct object`_’s weapons. Fails if the direct object
is not able to fire the weapon (insufficient ammo or energy, weapon
fired too recently, or no weapon equipped in that slot).

flash
~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   duration              yes   duration_
   color                 yes   color_
   ====================  ====  ========================================

Causes the player’s entire screen to flash. Overlays the screen with a
solid ``color`` for the ``duration``.

group
~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   of                    yes   array_ of actions
   ====================  ====  ========================================

Groups together multiple actions. Actions in the group are all affected
by the if_, and override_ of the group.

Group actions should never be reflexive_ (it would work, but be
confusing).

heal
~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   value                 yes   integer_
   ====================  ====  ========================================

Adds ``value`` to the `direct object`_’s health.

Positive values heal the direct object. Health is capped at the direct
object’s maximum.

Negative values cause the direct object to take damage. If the direct
object’s health would be decreased below 0, it is destroyed_.

.. note:: For damage-dealing projectiles, it is usually better to set
   collide.damage_ on the projectile, instead of dealing damage from
   its collide.action_.

.. _destroyed: {filename}/plugins/format/object.rst#destroy
.. _collide.damage: {filename}/plugins/format/object.rst#collide
.. _collide.action: {filename}/plugins/format/object.rst#collide

hold
~~~~

Removes the `direct object`_’s target and causes it to maintain its
current position.

Hold actions have no additional fields.

key
~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   enable                no    array_ of keys
   disable               no    array_ of keys
   ====================  ====  ========================================

Enables or disables the use of certain keys by the player. ``enable``
or ``disable`` is a list of strings that name keys. Some of the keys,
like ``"mouse"`` are not really keys, but other kinds of player input
that can be disabled.

By default, all keys are enabled.

.. note:: Key actions were created for the tutorial. While there may be
   other uses, please talk to antares-dev_ before using, as there may
   be better options.

.. table::
   :widths: auto

   ====================  ===============================================
   Key                   Action
   ====================  ===============================================
   *Ship keys*
   ---------------------------------------------------------------------
   ``"up"``              Accelerate
   ``"down"``            Decelerate
   ``"left"``            Turn Counter-clockwise
   ``"right"``           Turn Clockwise
   ``"pulse"``           Fire Weapon 1
   ``"beam"``            Fire Weapon 2
   ``"special"``         Fire/Activate Special
   ``"warp"``            Warp
   *Command keys*
   ---------------------------------------------------------------------
   ``"select_friend"``   Select Friendly
   ``"select_foe"``      Select Hostile
   ``"select_base"``     Select Base
   ``"target"``          Target
   ``"order"``           Order to Go
   ``"zoom_in"``         Scale In
   ``"zoom_out"``        Scale Out
   ``"comp_up"``         Computer Previous
   ``"comp_down"``       Computer Next
   ``"comp_accept"``     Computer Accept/Select/Do
   ``"comp_back"``       Computer Cancel/Back Up
   *Shortcut keys*
   ---------------------------------------------------------------------
   ``"zoom_shortcut"``   Zoom to 1:1/1:2/1:4/1:16/Closest
                         Hostile/Closest Object/All
   *Virtual keys*
   ---------------------------------------------------------------------
   ``"comp_message"``    Use computer’s “Messages” screen
   ``"comp_special"``    Use computer’s “Special Orders” screen
                         (including “Transfer Control” shortcut)
   ``"comp_build"``      Use computer’s “Build” screen
   ``"send_message"``    Send messages with “return” key [#key-message]_
   ``"mouse"``           Select objects with mouse
   ====================  ===============================================

land
~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   speed                 yes   integer_
   ====================  ====  ========================================

Causes the `direct object`_ to land at its target. The object will
shrink to nothingness, after which it will execute its expire.action_
with its target as the `direct object`_.

Used (with reflexive_) in the arrive.action_ for transports landing on
planets or ships going through jump gates.

message
~~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   id                    no    integer_
   pages                 yes   array_ of strings_
   ====================  ====  ========================================

Displays message text at the bottom of the player’s screen. Each string
in ``pages`` is a page of text that the player will see.

Strings can contain formatting characters like ``\\i``.

``id`` is optional. It is used only by the `message condition`_.

.. _message condition: {filename}/plugins/format/action.rst#message

morph
~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   base                  yes   name_ of an object_
   keep_ammo             no    boolean_
   ====================  ====  ========================================

Changes the base type of the `direct object`_. The object is reset and
recreated with the defaults from ``base``, preserving only:

*  Owner
*  Velocity and orientation
*  Health, energy, and battery
*  Cloaking (if active)
*  Weapon ammunition (if ``keep_ammo`` is true)

.. warning:: Don’t change an object’s fundamental type (ray to
   rotation, animation to device, etc.)

The morph action can be used in many ways to create complicated
behaviors. It can:

*  Create an extended destruction sequence. In |ch20|_, the Cantharan
   gateship’s destroy.action_ morphs the gateship into a form that
   creates lots of smaller explosions before finally expiring.
*  Activate a disabled object. In |ch14|_, the Bazidanese battleship
   starts in a “disabled” form and morphs into an active form when
   freed.
*  Disable an active object. In |net3|_, a Grolk cruiser’s
   destroy.action_ morphs it into an inactive form and teleports it to
   a tractor moor.
*  Enable or disable interactions. In |ch04|_, the Obish transport
   morphs between a form that can pick up prisoners and a form that
   can’t, depending on whether the transport is full.

move
~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   origin                no    “level”, “subject”, “direct”
   to                    no    point_
   distance              no    distance_
   within                no    “circle” or “square”
   ====================  ====  ========================================

Modifies the location of the `direct object`_. The new location is
relative to an ``origin``, one of:

*  ``"level"`` (the default), the center (0, 0) of the level,
*  ``"subject"``, the location of the `subject object`_, or
*  ``"direct"``, the location of the `direct object`_.

(in a reflexive_ action, modifies the location of the `subject object`_,
but ``"subject"`` and ``"direct"`` still have their original meanings)

Offsets the new location by ``to``. This offset takes the scenario’s
rotation into account. This is typically used with ``origin: "subject"``
to place an object at an absolute location.

If ``distance`` is set, the new location will additionally be offset by
a random distance up to the given amount.

(use of the ``within`` [#create-within]_ field is not recommended. It
exists only for compatibility with some Hera-created scenarios)

occupy
~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   value                 yes   integer_
   ====================  ====  ========================================

Adds ``value`` to the occupation count of the `direct object`_ for the
owner of the `subject object`_. Requires that the direct object sets:

*  occupy_count_
*  destroy.neutralize_
*  target.base_

When a player’s occupation count on an object reaches occupy_count_,
that player takes control over the object. This is used in the `factory
scenario`_ when EVATs take over stations.

.. _occupy_count: {filename}/plugins/format/object.rst#occupy-count
.. _destroy.neutralize: {filename}/plugins/format/object.rst#destroy
.. _target.base: {filename}/plugins/format/object.rst#target

pay
~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   value                 yes   money_
   player                no    index_ of a player
   ====================  ====  ========================================

Adds ``value`` to a player’s cash reserves. If ``value`` is negative,
reduces the player’s cash (but not below zero). If ``player`` is null,
pays the `direct object`_’s owner. If ``player`` is non-null, pays
``player``.

play
~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   priority              yes   integer_ from 0 to 5 inclusive
   persistence           yes   duration_
   absolute              no    boolean_
   volume                yes   integer_ from 0 to 255 inclusive
   sound                 no    name_ of a sound_
   any                   no    array_ of ``{sound: "name of sound}``
   ====================  ====  ========================================

Plays a sound_. If ``sound`` is non-null, plays that sound. Otherwise,
picks a sound at random from ``any``.

Plays the sound at the given ``volume``. Unless ``absolute`` is true,
the sound’s origin is centered on the `direct object`_. The sound’s
volume is reduced proportionately to the player flagship’s distance from
the sound’s origin. ``absolute`` sounds play at full volume no matter
how far away the player’s flagship is.

Antares has a limited number of sound channels to play sounds with.
``priority`` and ``persistence`` affect how it decides when to stop a
sound and allow a more important or recent sound to take over the
channel. Higher ``priority`` makes it more likely that a sound will
play, and longer ``persistence`` means it will be longer before another
sound can take over its channel. The exact rules are:

*  if the same sound is already playing at the same or lower
   ``volume``, stop it and take over its channel. Otherwise,
*  if any sound is playing at a lower ``volume``, stop it and take over
   its channel. Otherwise,
*  if any sound is playing at a lower ``priority``, stop it and take
   its channel. Otherwise,
*  if any sounds have been playing for longer than their
   ``persistence``, stop and take the channel of the sound that is
   furthest past its persistence.

If Antares can’t find a suitable channel per the above rules, the sound
doesn’t play.

push
~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   value                 no    speed_
   ====================  ====  ========================================

Modifies the velocity of the `direct object`_, applying the change in
the direction that the `subject object`_ is facing.

If ``value`` is non-null, sets the direct object’s direction to match
the direct object, and its speed to ``value`` (like the Cantharan
gateship’s Shrikeolator).

If ``value`` is null, treats the push like a collision (like the
Elejeetian Cruiser’s Onas Pulse):

#. Takes the difference between the two objects’ velocity.
#. Divides that change by the mass of the direct object.
#. Adds the modified difference to the direct object’s velocity.
#. Caps the direct object’s speed to its max_velocity_.

See also: slow_, |speed|__, and stop_.

remove
~~~~~~

Removes the `direct object`_ from existence. Does not execute its
destroy_ action.

Remove actions have no additional fields.

reveal
~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   initial               yes   array_ of indexes_ of initials_
   ====================  ====  ========================================

Reveals the hidden_ initial_ objects specified by ``initial``.

“Revealing” actually means creating the object, so revealing an object
executes its create_ action.

.. _hidden: {filename}/plugins/format/initial.rst#hide

score
~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   counter               yes   counter_
   value                 yes   integer_
   ====================  ====  ========================================

Adds ``value`` to the score ``counter``. If ``counter.player`` is null,
modifies the score of `direct object`_’s owner.

select
~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   screen                yes   “main”, “build”, “special”, “message”,
                               or “status”
   line                  yes   integer_
   ====================  ====  ========================================

Selects the given ``screen`` and ``line`` number in the player’s
computer.

slow
~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   value                 yes   number_
   ====================  ====  ========================================

Decreases the velocity of the `direct object`_, without changing its
direction. Multiplies the current velocity by ``value``. For example,
``value: 0.75`` means to decrease its current velocity by one quarter.

See also: push_, |speed|__, and stop_.

spark
~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   count                 yes   integer_
   hue                   yes   hue_
   velocity              yes   number_
   age                   yes   duration_
   ====================  ====  ========================================

Creates ``count`` single-pixel visual effects, centered on the `direct
object`_ and shooting away at speed up to ``velocity``. If there is no
direct object, they are created at the center of the screen. Up to 125
sparks may exist on-screen at any given time.

The sparks are ``hue``-colored. They are initially bright and fade over
time. After they have been around for the duration_ ``age``, they
disappear.

.. |speed| replace:: speed
__ #speed
__ #speed
__ #speed
__ #speed
__ #speed

speed
~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   value                 yes   speed_
   relative              no    boolean_
   ====================  ====  ========================================

Modifies the velocity of the `direct object`_, without changing its
direction. If ``relative`` is true, adds ``value`` to the object’s
current velocity. Otherwise, sets its velocity to ``value``.

See also: push_, slow_, and stop_.

spin
~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   value                 yes   range_ of numbers_
   ====================  ====  ========================================

Spins the `direct object`_. Requires that:

*  The direct object can turn (``turn_rate`` is not null), *and*
*  either:
   *  the direct object is non-thinking, *or*
   *  the direct object is disabled_.

Picks a random turn velocity from ``value`` and sets it on the direct
object. If a disabled_ direct object regains control, it will stop
spinning.

Almost always used together with the disable_ action.

.. _disabled: #disable

stop
~~~~

Sets the velocity of the `direct object`_ to zero. This is equivalent to
a slow_ or |speed|__ action with a ``value`` of 0.

Stop actions have no additional fields.

See also: push_, slow_, and |speed|__.

target
~~~~~~

Sets the `subject object`_’s target to the `direct object`_.

Target actions have no additional fields.

thrust
~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   value                 yes   range_ of accelerations_
   ====================  ====  ========================================

Sets the current thrust_ of the `direct object`_. Only meaningful for
non-thinking objects; thinking objects control their own thrust.

warp
~~~~

Causes the `direct object`_ to enter warp. There is no delay or energy
cost.

Warp actions have no additional fields.

win
~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   player                no    index_ of a player
   next                  no    name_ of a level_
   text                  yes   string_
   ====================  ====  ========================================

Ends the level_, displaying ``text`` in the mission debriefing.

In a solo_ level, if ``player`` is the human player, declares victory
for the player. If ``next`` is non-null, unlocks that level_ and
continues the game. If ``next`` is null, ends the game in victory.

In a solo_ level, if ``player`` is a non-human player, ends the level in
defeat. The player will be given the option to retry or exit. ``next``
is ignored.

In a net_ level, declares victory for ``player``. ``next`` is ignored.

.. _solo: {filename}/plugins/format/level.rst#solo
.. _net: {filename}/plugins/format/level.rst#solo

zoom
~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   value                 yes   “2:1”, “1:1”, “1:2”, “1:4”, “1:16”,
                               “foe”, “object”, or “all”
   ====================  ====  ========================================

Sets the player’s zoom level to ``value``.

Footnotes
---------

.. [#attributes] TODO(sfiera): document.
.. [#check] The check_ action is new to Antares. In Ares, conditions
   were checked at the end of any action sequence with a message_ or
   score_ action, but there wasn’t otherwise a way of re-checking
   conditions.
.. [#create-within] In Ares, random distances were within a square: the
   random point within distance `d` would be placed within `(x±d,
   y±d)`. In such a square, the points in the corners have a cartesian
   distance much greater than `d`. Antares defaults to a circle
   instead, so that the resulting distance is actually within `d`, but
   preserves compatibility in the `factory scenario`_ by using the
   square logic.
.. [#create-legacy-random] Normally, if ``count`` is a range, then
   Antares rolls a die to determine how many objects to count.
   ``legacy_random`` tells Antares to roll a die even if ``count`` is a
   fixed number. Preserving compatibility with Ares requires ensuring
   that the same dice are rolled in the same order.
.. [#delay] The delay_ action is new to Antares. In Ares, every action
   could have a delay (though almost none did).
.. [#key-message] As of Antares 0.9.0, sending messages with the
   “return” key doesn’t work at all, though.

.. include:: epilog.rsti
.. -*- tab-width: 3; indent-tabs-mode: nil; fill-column: 72 -*-
