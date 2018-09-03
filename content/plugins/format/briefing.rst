Briefing
========

.. sectnum::

A briefing is a page in a level’s Mission Analysis. It explains some
information about the level, such as a win or loss condition, or an
important object. The mission analysis starts with a starmap_ location,
then a system-level overview, then displays all briefing points in
sequence on top of the system-level overview.

Non-tutorial solo_ levels_ should have at least one briefing point. The
briefing points should explain the success and failure conditions for
the mission. Net_ levels_ and training missions generally do not have
briefings.

`Example briefing <https://github.com/arescentral/antares-data/blob/master/levels/ch01.pn#L127-L133>`_

.. _starmap: {filename}/plugins/format/level.rst#starmap
.. _solo: {filename}/plugins/format/level.rst#solo
.. _net: {filename}/plugins/format/level.rst#net

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
   initial__             no    index_ of an initial_
   title_                yes   string_
   content_              yes   string_
   ====================  ====  ========================================

__

initial
~~~~~~~

Focuses on the given initial_ object in the system. Generally, the
object is a ship or base of interest. The initial_ must exist and not be
hidden_ at the start of the level.

If not provided, the briefing is shown centered, without focusing on any
particular object. To focus on an arbitrary location in space, create an
invisible object and focus on it.

.. _hidden: {filename}/plugins/format/initial.rst#hide

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

.. _portrait: {filename}/plugins/format/object.rst#portrait

If both objects and pictures exist with the given name, the object’s
portrait is shown. (usually it’s the same image, but this enables the
click-for-stats behavior)

Generally, the ``^P…^`` code should be at the beginning or end of a
paragraph, but not in-between. Images used in briefings must be exactly
200 pixels wide. Most are 200×100.

.. include:: epilog.rsti
.. -*- tab-width: 3; indent-tabs-mode: nil; fill-column: 72 -*-
