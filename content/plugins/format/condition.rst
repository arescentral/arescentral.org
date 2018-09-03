Condition
=========

.. sectnum::

A condition triggers events in a level_. Each condition has a when_
property, which specifies what to watch for, and an action_ sequence
that specifies what to do when the condition is triggered. There are
many types of conditions, such as destroyed_, owner_ and time_.

Every level_ has an array_ of conditions. Because conditions are tied to
a level, they can only refer to that level’s initials_, not to objects
created during game play.

Conditions are checked once per second, or whenever a `check action`_
runs.

.. _check action: {filename}/plugins/format/action.rst#check

`Example condition <https://github.com/arescentral/antares-data/blob/master/levels/ch01.pn#L113-L125>`_

.. contents::
   :local:
   :backlinks: none

Definition
----------

A condition is a procyon_ value with the following fields:

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   disabled_             no    boolean_
   persistent_           no    boolean_
   when_                 yes   when_
   subject_              no    `object reference`_
   direct_               no    `object reference`_
   action                yes   array_ of actions_
   ====================  ====  ========================================

disabled
~~~~~~~~

If true, the condition is not initially enabled and will not trigger.
Conditions can be enabled or disabled with the `condition action`_.
Conditions are also disabled after they trigger, unless they are
persistent_.

.. _condition action: {filename}/plugins/format/action.rst#condition

persistent
~~~~~~~~~~

If true, the condition does not become disabled_ after it triggers.

.. _subject:
.. _direct:

subject, direct
~~~~~~~~~~~~~~~

The `subject object`_ and `direct object`_ that will be used if the
condition’s action_ executes.


.. _subject object: {filename}/plugins/format/action.rst#subject-object
.. _direct object: {filename}/plugins/format/action.rst#direct-object

when
~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   type                  yes   “autopilot_”, “building_”, “cash_”,
                               “computer_”, “count_”, “score_”,
                               “destroyed_”, “distance_”, “health_”,
                               “identity_”, “message_”, “owner_”,
                               “ships_”, “speed_”, “target_”, “time_”,
                               or “zoom_”
   ====================  ====  ========================================

op
~~

All conditions have a field called ``op``. This determines the
comparison to make. All conditions support:

*  ``"eq"`` (equal)
*  ``"ne"`` (not equal)

Some conditions additionally support:

*  ``"lt"`` (less than)
*  ``"gt"`` (greater than)
*  ``"le"`` (less than or equal)
*  ``"ge"`` (greater than or equal)

Types
-----

autopilot
~~~~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   op                    yes   “eq” or “ne”
   player                yes   index_ of a player
   value                 yes   boolean_
   ====================  ====  ========================================

Compares the given ``player``’s autopilot status (``true`` = on
autopilot, ``false`` = not on autopilot) to ``value``.

Preconditions: ``player`` is an active, human player.

building
~~~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   op                    yes   “eq” or “ne”
   player                yes   index_ of a player
   value                 yes   boolean_
   ====================  ====  ========================================

Compares the given ``player``’s build status (``true`` = building
something, ``false`` = not building anything) to ``value``.

Preconditions: ``player`` is an active player with a build object.

cash
~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   op                    yes   “eq”, “ne”, “lt”, “gt”, “le”, or “ge”
   player                yes   index_ of a player
   value                 yes   money_
   ====================  ====  ========================================

Compares the given ``player``’s cash reserves to ``value``.

Preconditions: ``player`` is an active player.

computer
~~~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   op                    yes   “eq” or “ne”
   screen                yes   “main”, “build”, “special”, “message”,
                               or “status”
   line                  no    integer_
   ====================  ====  ========================================

Compares the local player’s computer screen to ``screen``. If ``line``
is not null, compares the local players screen and line to ``(screen,
line)``.

.. warning:: not net-safe. Use only in `solo levels`_.

.. _solo levels: {filename}/plugins/format/level.rst#solo

count
~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   op                    yes   “eq”, “ne”, “lt”, “gt”, “le”, or “ge”
   value                 yes   integer_
   of                    yes   array_ of conditions
   ====================  ====  ========================================

Evaluates the sub-conditions in ``of`` and compares the count of
sub-conditions that are true to ``value``. This can simulate different
logical operators, like “all”, “any”, or “not”.

Some example count conditions:

*  First player owns all three planets:

   .. include:: pn/condition-count-all.pn
      :code: procyon

*  Either or both of the first player’s carriers has been destroyed:

   .. include:: pn/condition-count-either.pn
      :code: procyon

destroyed
~~~~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   op                    yes   “eq” or “ne”
   object                yes   `object reference`_
   value                 yes   boolean_
   ====================  ====  ========================================

Compares ``object``’s state (``true`` = destroyed, ``false`` = not
destroyed) to ``value``.

The comparison really considers whether the object exists or not, so a
`hidden initial`_ that has yet to be `revealed`_ counts as “destroyed”
(``true``) for the purposes of this condition.

.. _hidden initial: {filename}/plugins/format/initial.rst#hide
.. _revealed: {filename}/plugins/format/action.rst#reveal

distance
~~~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   op                    yes   “eq”, “ne”, “lt”, “gt”, “le”, or “ge”
   from                  yes   `object reference`_
   to                    yes   `object reference`_
   value                 yes   number_
   ====================  ====  ========================================

Compares the cartesian distance between the two objects ``from`` and
``to`` to ``value``.

Preconditions: the objects ``from`` and ``to`` both exist.

health
~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   op                    yes   “eq”, “ne”, “lt”, “gt”, “le”, or “ge”
   object                yes   `object reference`_
   value                 yes   number_
   ====================  ====  ========================================

Compares ``object``’s health fraction to ``value``. ``value: 1.0`` means
“full health”, ``value: 0.5`` means “half health”, and ``value: 0`` is
equivalent to the destroyed_ condition.

identity
~~~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   op                    yes   “eq” or “ne”
   a                     yes   `object reference`_
   b                     yes   `object reference`_
   ====================  ====  ========================================

Compares the identity of the objects ``a`` and ``b``. This is usually
not interesting if both ``a`` and ``b`` reference initials_, but can be
useful with other forms of `object references`_:

.. include:: pn/condition-identity.pn
   :code: procyon

Preconditions: the objects ``a`` and ``b`` both exist.

message
~~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   op                    yes   “eq” or “ne”
   id                    yes   integer_
   page                  yes   integer_
   ====================  ====  ========================================

Compares the message ID and page the local player is viewing to ``(id,
page)``.

.. warning:: not net-safe. Use only in `solo levels`_.

Preconditions: the local player is viewing a message.

owner
~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   op                    yes   “eq” or “ne”
   object                yes   `object reference`_
   player                yes   index_ of a player
   ====================  ====  ========================================

Compares the owner of ``object`` to ``player``.

Preconditions: ``object`` exists.

score
~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   op                    yes   “eq”, “ne”, “lt”, “gt”, “le”, or “ge”
   counter               yes   counter_
   value                 yes   integer_
   ====================  ====  ========================================

Compares the value of the counter_ ``counter`` to ``value``.

ships
~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   op                    yes   “eq”, “ne”, “lt”, “gt”, “le”, or “ge”
   player                yes   index_ of a player
   value                 yes   integer_
   ====================  ====  ========================================

Compares the ship count of ``player`` to ``value``.

speed
~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   op                    yes   “eq”, “ne”, “lt”, “gt”, “le”, or “ge”
   object                yes   `object reference`_
   value                 yes   number_
   ====================  ====  ========================================

Compares the speed of ``object`` to ``value``.

Preconditions: ``object`` exists.

target
~~~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   op                    yes   “eq” or “ne”
   object                yes   `object reference`_
   target                yes   `object reference`_
   ====================  ====  ========================================

Compares the target of ``object`` to the object ``target``.

Preconditions: ``object`` and ``target`` both exist.

time
~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   op                    yes   “eq”, “ne”, “lt”, “gt”, “le”, or “ge”
   duration              yes   duration_
   legacy_start_time     no    boolean_
   ====================  ====  ========================================

Compares the elapsed game time to ``duration``. If the level has a
start_time_ setup phase, then positive durations indicate time during
actual gameplay, and negative durations indicate setup time.

.. _start_time: {filename}/plugins/format/level.rst#start-time

(use of the ``legacy_start_time`` [#time-legacy-start-time]_ field is
not recommended. It exists only for compatibility with some Hera-created
scenarios)

zoom
~~~~

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   op                    yes   “eq”, “ne”, “lt”, “gt”, “le”, or “ge”
   value                 yes   “2:1”, “1:1”, “1:2”, “1:4”, “1:16”,
                               “foe”, “object”, or “all”
   ====================  ====  ========================================

Compares the local player’s zoom level to ``zoom``.

.. warning:: not net-safe. Use only in `solo levels`_.

Footnotes
---------

.. [#time-legacy-start-time] In Ares, all ``duration`` values were
   positive, and the setup time in a level with start_time_ counted for
   ⅓ as much as gameplay time. ``legacy_start_time: true`` preserves
   this behavior for compatibility.

.. include:: epilog.rsti
.. -*- tab-width: 3; indent-tabs-mode: nil; fill-column: 72 -*-
