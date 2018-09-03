Plugins
=======

.. sectnum::

Like Ares, Antares supports plugins. Unlike Ares, there is no need to
use a special editor (Hera), though you might want to (if one existed).

.. contents::
   :local:
   :backlinks: none

Basics
------

An Antares plugin is a `zip file`_ with the extension “.antaresplugin”.
That zip file contains an top-level file called info.pn_ with general
information about the plugin, plus directories with several types of
resources_, including levels_, objects_, and sprites_

The Antares `factory scenario`_ is the Ares campaign scenario that comes
with Antares. A plugin’s resources supersede the factory scenario’s
resources whenever a resource exists with the same name. Plugins may
also refer to the factory scenario’s resources if the plugin doesn’t
have a resource with the same name.

Most of the data files within a plugin archive are short text files in
procyon_ format.

.. _zip file: https://en.wikipedia.org/wiki/Zip_(file_format)

Resources
---------

A plugin may contain resources in the following locations:

.. table::
   :widths: auto

   =============  ========  ========================
   Directory      Needed    Format
   =============  ========  ========================
   info.pn_       yes       procyon_
   levels_/…      yes       procyon_
   objects_/…     probably  procyon_
   races_/…       maybe     procyon_
   sprites_/…     maybe     procyon_ + PNG_
   pictures_/…    maybe     PNG_
   sounds_/…      maybe     AIFF_
   music_/…       no        S3M_, XM_
   fonts_/…       no        procyon_ + PNG_
   interfaces_/…  no        procyon_
   replays_/…     no        procyon_
   =============  ========  ========================

There are also some important types that are used within other
resources, but never on their own:

.. table::
   :widths: auto

   ==========  ==============================
   Type        Used by
   ==========  ==============================
   briefing_   levels_
   condition_  levels_
   initial_    levels_
   action_     objects_ and conditions_
   ==========  ==============================

Tutorials
---------

.. admonition:: TODO(sfiera)

   write tutorials

.. include:: format/epilog.rsti
.. -*- tab-width: 3; indent-tabs-mode: nil; fill-column: 72 -*-
