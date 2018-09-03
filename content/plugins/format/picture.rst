Picture
=======

.. sectnum::

A picture is a simple PNG_ images. Pictures are used as backgrounds in
the game’s interface, in mission briefings, and in prologues and
epilogues. They are not used in-game and are never animated; sprites_
are used for that.

`Example <https://github.com/arescentral/antares-data/blob/master/pictures/splash.png>`_

.. contents::
   :local:
   :backlinks: none

Do I need it?
-------------

Maybe.

If you’re adding new ships, you’ll probably want to add pictures for
them so that you can show them in mission briefings. Also, if you’re
adding levels, you may want to add pictures to show in prologues and
epilogues.

If none of that applies, you don’t need to add any pictures.

Naming
------

Pictures are in the ``pictures`` directory and have a ``.png`` file
extension.

There are two special pictures used directly by Antares, the splash_ and
starmap_ pictures:

*  ``splash`` (shown during game startup)
*  ``starmap`` (shown during mission briefings)

Additionally, any picture which which is used as the portrait_ for an
object_ has the same name as that object. Finally, the `factory
scenario`_ uses three directories for other pictures:

*  ``brf/...``, for pictures shown during mission briefings, but not
   corresponding to any object.
*  ``log/...``, for pictures shown during prologues and epilogues.
*  ``gui/...``, for pictures used in the game interface.

.. _portrait: {filename}/plugins/format/object.rst#portrait

Definition
----------

Antares supports PNG_ image files.

Special pictures
----------------

splash
~~~~~~

A picture to show while the game is launching. It will be shown centered
in the screen, possibly cropped, without being scaled up or down. The
image should be at least 640×480.

If the plugin does not have a picture named ``splash``, the `factory
scenario’s splash screen`_ is used instead.

.. _factory scenario’s splash screen: https://github.com/arescentral/antares-data/blob/master/pictures/splash.png

starmap
~~~~~~~

The image that is shown at the beginning of mission briefings. It should
be sized to match the mission briefing box (533×361) and will be cropped
if it’s too large.

In the `factory scenario`_, the indicator drawn around the current star
system is a 32×24 box. If you provide your own star map, you may prefer
to use similarly-sized stars.

If the plugin does not have a picture named ``starmap``, the `factory
scenario’s starmap`_ is used instead.

.. _factory scenario’s starmap: https://github.com/arescentral/antares-data/blob/master/pictures/starmap.png

.. include:: epilog.rsti
.. -*- tab-width: 3; indent-tabs-mode: nil; fill-column: 72 -*-
