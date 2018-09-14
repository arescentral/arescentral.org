Sprite
======

.. sectnum::

A sprite is a collection of images used in-game. Depending on how a
sprite is used, the individual images may be frames of an `object’s
animation`_ or angles in an `object’s rotation`_. It is defined by three
files:

.. _object’s animation: /plugins/format/object#animation
.. _object’s rotation: /plugins/format/object#rotation

*  a procyon_ sprite map (|example-map|_)
*  a PNG_ sprite image (|example-image|_)
*  a PNG_ sprite overlay (|example-overlay|_)

.. |example-map| replace:: example
.. |example-image| replace:: example
.. |example-overlay| replace:: example
.. _example-map: https://github.com/arescentral/antares-data/blob/master/sprites/ish/hvd.pn
.. _example-image: https://github.com/arescentral/antares-data/blob/master/sprites/ish/hvd/image.png
.. _example-overlay: https://github.com/arescentral/antares-data/blob/master/sprites/ish/hvd/overlay.png

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
sprite map has the ``.pn`` extension. The sprite image ends in
``/image.png``. The overlay image ends in ``/overlay.png``.

By convention, sprites have the same name as the object that uses them.

Definition
----------

A sprite map is a procyon_ file with the following fields:

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   frames                yes   array_ of frames_
   ====================  ====  ========================================

A sprite’s image and overlay are PNG_ images. They must have the same
size. The frames_ in the sprite map reference parts of the image and
overlay.

By default, only the sprite image is used, and the sprite overlay is
ignored. The overlay is used to `re-color sprites <#re-coloring>`_ when
a player_ has a hue_.

.. _player: /plugins/format/level#solo-players

frames
~~~~~~

.. figure::    /plugins/format/images/sprite-hvd.png
   :target:    /plugins/format/images/sprite-hvd.png
   :align:     right
   :figclass:  w225
   :alt:       24 frames of a rotating Ishiman HVD, with the first three
               frames highlighted.

   Sprite image for the `Ishiman HVD
   <https://github.com/arescentral/antares-data/blob/master/sprites/ish/hvd.pn>`_.
   The ``{left, top, right, bottom}`` rectangles for the first three
   frames are highlighted, with a “+” mark at ``{cx, cy}``.

An array_ of maps_ specifying the individual frames, each with the
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

The sprite image is bounded by the rect_ contained in ``{left, top,
right, bottom}``. The center of the sprite is the point_ at ``{cx,
cy}``. Both are offset from the upper-left-hand corner of the image and
overlay.

Re-coloring
~~~~~~~~~~~

A sprite’s overlay image is used to re-color sprites when owned by a
player_ with a hue_. Re-coloring works as follows:

#. Discard the green, blue, and alpha channels from the overlay.
#. Map the shade of red to the corresponding shade from the new hue_.
#. Composite the re-colored overlay atop_ the original sprite.

.. _atop: https://en.wikipedia.org/wiki/Alpha_compositing

.. include:: epilog.rsti
.. -*- tab-width: 3; indent-tabs-mode: nil; fill-column: 72 -*-
