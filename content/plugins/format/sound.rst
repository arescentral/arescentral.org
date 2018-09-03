Sound
=====

.. sectnum::

A sound is a short piece of AIFF_ audio. Sounds could play when firing a
weapon, when a ship explodes, when a button is clicked, or any number of
other situations.

.. contents::
   :local:
   :backlinks: none

Do I need it?
-------------

Maybe.

If you’re adding new weapons, you’ll probably want to add new sounds for
them. Also, other actions may benefit from sounds: an object’s arrival
or destruction, for example.

If none of that applies, you don’t need to add any sounds.

Naming
------

Sounds are in the ``sounds`` directory and have a ``.aiff`` file
extension.

By convention, the name for a sound starts with a three-letter
directory. Sounds that correspond to an object_ in some straightforward
way share their name. In the `factory scenario`_, for example, most of
the sounds associated with weapons are named ``dev/(weapon)``, and the
sounds associated with explosions are in ``sfx/explosion/(kind)``. Beeps
and other sounds used by the game’s user interface are in ``gui``.

Definition
----------

Antares supports AIFF_ sounds.

.. include:: epilog.rsti
.. -*- tab-width: 3; indent-tabs-mode: nil; fill-column: 72 -*-
