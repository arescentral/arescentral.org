info.pn
=======

.. sectnum::

Every plugin must contain a file named ``info.pn`` at the top level. It
contains general information about the plugin, including the title_,
author_, and plugin format_ version.

`Example <https://github.com/arescentral/antares-data/blob/master/info.pn>`_

.. contents::
   :local:
   :backlinks: none

Do I need it?
-------------

Yes. Every plugin must have an ``info.pn`` file.

Naming
------

The file should be named ``info.pn``, not within any directory.

Definition
----------

An info.pn file is a procyon_ file with the following fields:

.. table::
   :widths: auto

   ====================  ====  ========================================
   Field                 Req?  Type
   ====================  ====  ========================================
   title_                yes   string_
   identifier_           no    sha1
   format_               yes   string_
   download_url_         no    url_
   author_               yes   string_
   author_url_           no    url_
   version_              yes   string_
   intro_                no    string_
   about_                no    string_
   ====================  ====  ========================================

title
~~~~~

A string_ containing the title of the plugin. This is shown when listing
installed plugins. By default, it is also used to record a player’s
progress within the scenario: if the title is changed, then players will
lose their progress and go back to chapter 1 (but an identifier_ can be
used to fix that).

identifier
~~~~~~~~~~

A 40-character SHA-1 hash, used to record a player’s progress in the
plugin. By default, the hash of title_ is used. To change the plugin’s
title without causing players to lose their progress, set ``identifier``
to the hash of the original title.

format
~~~~~~

This must be ``20``, indicating the current version of the Antares
plugin format.

download_url
~~~~~~~~~~~~

If provided, this will be shown as a link to download the latest version
of the scenario.

author
~~~~~~

A string_ crediting the author of the scenario. This is required, but
you may prefer to use a pseudonym instead of your real name.

author_url
~~~~~~~~~~

If provided, this will be shown as a link with the author_.

version
~~~~~~~

A string identifying the plugin version. No particular versioning scheme
is enforced, but `N.N.N` (for example, 1.2.0 or 0.9.1) is recommended.

If you update a plugin, be sure to update the version number too. In a
net game, all players must use identical copies of the plugin, and
version numbers help players coordinate.

intro
~~~~~

A text crawl that will be displayed on startup the first time that the
plugin is opened, or whenever the player selects “Replay Intro” from the
main menu.

Supports the same formatting codes as levels_’ `prologues and
epilogues`_.

.. _prologues and epilogues: {filename}/plugins/format/level.rst#prologue-epilogue

about
~~~~~

A text crawl that will be displayed whenever the player selects “About”
from the main menu. The Hera instructions for editing the about text
state:

   You may insert your own credit at the beginning of the `existing
   credits text`_. Do not delete or alter the rest of the text.

.. _existing credits text: https://github.com/arescentral/antares-data/blob/master/info.pn#L97-L173

For Antares, you may completely replace the credits text if you want to.
However, if you incorporate any part of the original text, you must
follow the instructions as given above.

Supports the same formatting codes as levels_’ `prologues and
epilogues`_.

.. include:: epilog.rsti
.. -*- tab-width: 3; indent-tabs-mode: nil; fill-column: 72 -*-
