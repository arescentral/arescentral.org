Antares on Linux
================

Antares runs on Linux. The recommended installation method is through
your package manager, if possible. If that’s not possible, you can
`build it yourself`_.

..  _build it yourself: {filename}/antares/contributing/building.rst

Debian and Ubuntu
-----------------

Antares is available through the Debian and Ubuntu package managers. To
install it, run these commands in a terminal window:

..  code-block:: sh

    $ sudo -s
    $ curl https://raw.githubusercontent.com/sfiera/id/master/sfiera.asc | apt-key add -
    $ apt-add-repository "http://apt.arescentral.org contrib"
    $ apt-get update
    $ apt-get install antares
    $ exit

This will install Antares to ``/usr/games/antares``, along with a
.desktop file.

..  -*- tab-width: 4; fill-column: 72 -*-
