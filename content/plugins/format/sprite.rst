Sprite
======

.. sectnum::

A sprite is a collection of images used in-game. Depending on how a
sprite is used, the individual images may be frames of an `object’s
animation`_ or angles in an `object’s rotation`_. It is defined by three
files: a procyon_ definition, a PNG_ image, and a PNG_ overlay.

.. _object’s animation: {filename}/plugins/format/object.rst#animation
.. _object’s rotation: {filename}/plugins/format/object.rst#rotation

*  `Example definition <https://github.com/arescentral/antares-data/blob/master/sprites/ish/cruiser.pn>`_
*  `Example image <https://github.com/arescentral/antares-data/blob/master/sprites/ish/cruiser/image.png>`_
*  `Example overlay <https://github.com/arescentral/antares-data/blob/master/sprites/ish/cruiser/overlay.png>`_

.. contents::
   :local:
   :backlinks: none

Do I need it?
-------------

Maybe.

If you’re adding new ships or other objects, you’ll probably need
sprites for them. If you have no new objects, or are just modifying
existing objects, then you don’t need to add any sprites.

Naming
------

A sprite has three associated files in the ``sprites`` directory. The
sprite definition has the ``.pn`` extension. The sprite image ends in
``/image.png``. The overlay image ends in ``/overlay.png``.

By convention, sprites have the same name as the object that uses them.

Definition
----------

A sprite’s definition is a procyon_ file with the following fields:

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   frames                yes   array_ of frames_
   ====================  ====  ========================================

frames
~~~~~~

An array_ of frames specifying the individual frames, each with the
following fields:

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   left                  yes   integer_
   top                   yes   integer_
   right                 yes   integer_
   bottom                yes   integer_
   cx                    yes   integer_
   cy                    yes   integer_
   ====================  ====  ========================================

The sprite image is bounded by the rectangle contained in ``(left, top,
right, bottom)``. The center of the sprite is at ``(cx, cy)``.

.. include:: epilog.rsti
.. -*- tab-width: 3; indent-tabs-mode: nil; fill-column: 72 -*-
