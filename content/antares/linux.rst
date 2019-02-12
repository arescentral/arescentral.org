Antares on Linux
================

Antares runs on Linux. The recommended installation method is through
your package manager, if possible. If that’s not possible, you can
`build it yourself`_.

..  _build it yourself: /antares/contributing/building

Ubuntu
------

Antares is available through the Ubuntu package manager. To install it,
run these commands in a terminal window:

..  code-block:: sh

    $ sudo -s
    $ curl https://raw.githubusercontent.com/sfiera/id/master/sfiera.asc | apt-key add -
    $ source /etc/lsb-release
    $ echo "deb [arch=amd64] http://apt.arescentral.org $DISTRIB_CODENAME contrib" | tee /etc/apt/sources.list.d/antares.list
    $ apt-get update
    $ apt-get install antares
    $ exit
    $

This will install Antares to ``/usr/games/antares``, along with a
.desktop file.

..  -*- tab-width: 4; fill-column: 72 -*-
