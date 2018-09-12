Briefing
========

.. sectnum::

A briefing is a page in a level’s Mission Analysis. It explains some
information about the level, such as a win or loss condition, or an
important object. The mission analysis starts with a starmap_ location,
then a system-level overview, then displays all briefing points in
sequence on top of the system-level overview.

Non-tutorial `solo levels`_ should have at least one briefing point. The
briefing points should explain the success and failure conditions for
the mission. `Net levels`_ and training missions generally do not have
briefings.

`Example briefing <https://github.com/arescentral/antares-data/blob/master/levels/ch01.pn#L127-L133>`_

.. _starmap: /plugins/format/level#starmap
.. _solo levels: /plugins/format/level#solo
.. _net levels: /plugins/format/level#net

.. contents::
   :local:
   :backlinks: none

Definition
----------

A briefing is a procyon_ value with the following fields:

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   |initial-field|_      no    index_ of an |initial-resource|_
   title_                yes   string_
   content_              yes   string_
   ====================  ====  ========================================

initial
~~~~~~~

.. figure:: /plugins/format/images/briefing-freestanding.png
   :target:    /plugins/format/images/briefing-freestanding.png
   :align:     right
   :figclass:  w320
   :alt:       “Proteus. The Cantharan Order controls the Proteus
               System. In your first major offensive move against the
               Order, you will seize their base on Proteus Gamma.”

   A freestanding briefing point with a null |initial-field|_.

.. figure:: /plugins/format/images/briefing-object.png
   :target:    /plugins/format/images/briefing-object.png
   :align:     right
   :figclass:  w320
   :alt:       “Proteus Alpha. The base on Alpha can produce fighters
               and cruisers”

   A briefing point with a highlighted |initial-field|_.

Focuses on the given |initial-resource|_ object in the system.
Generally, the object is a ship or base of interest. The initial must
exist and not be hidden_ at the start of the level.

If not provided, the briefing is shown centered, without focusing on any
particular object. To focus on an arbitrary location in space, create an
invisible object and focus on it.

.. _hidden: /plugins/format/initial#hide

.. |initial-field| replace:: initial
.. _initial-field: #initial

.. |initial-resource| replace:: initial
.. _initial-resource: /plugins/format/initial

title
~~~~~

The title of the briefing, shown in the header of the briefing’s box.

content
~~~~~~~

The content of the briefing, shown within the briefing’s box.

Briefings can references pictures_ and objects_ by name:

======================  ==============================================
Example                 Meaning
======================  ==============================================
``^Pish/gunship^``      Show the portrait_ for the object_ named
                        ``ish/gunship`` (which must have a portrait).
                        The player can look at its data by clicking and
                        holding on the portrait.
``^Pbrf/jump-gate^``    Show the picture_ named ``brf/jump-gate``.
======================  ==============================================

.. _portrait: /plugins/format/object#portrait

If both objects and pictures exist with the given name, the object’s
portrait is shown. (usually it’s the same image, but this enables the
click-for-stats behavior)

Generally, the ``^P…^`` code should be at the beginning or end of a
paragraph, but not in-between. Images used in briefings must be exactly
200 pixels wide. Most are 200×100.

.. include:: epilog.rsti
.. -*- tab-width: 3; indent-tabs-mode: nil; fill-column: 72 -*-
