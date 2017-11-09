Antares 0.8.2 Released
======================

:date:      2017-11-09
:author:    sfiera
:tags:      antares, mac, linux, release

Antares 0.8.2 has been released.  This release runs on Mac OS X 10.7+
and Linux.

*   Download `Antares 0.8.2 for Mac OS X 10.7+`_.
*   Download the `Antares 0.8.2 sources`_.

Debian and Ubuntu users can also now install Antares directly through
the built-in package management system. Run the following commands from
a terminal:

..  code-block:: sh

    $ sudo -s
    $ curl https://raw.githubusercontent.com/sfiera/id/master/sfiera.asc | apt-key add -
    $ apt-add-repository "http://apt.arescentral.org contrib"
    $ apt-get update
    $ apt-get install antares
    $ exit

This is a minor release. It includes support for earlier versions of Mac
OS X, back to 10.7, and on Linux, integrates better with the system:

*   Issue 173 (Build .deb for Debian and Ubuntu)
*   Issue 184 (Look for scenarios in $PREFIX/share/games/antares/)
*   Issue 186 (Supported OS X version not set correctly)
*   Issue 181 (Use system libraries when possible)
*   Issue 185 (Linux preferences reset on each run)
*   Issue 183 (Warn when $PREFIX/share/antares/app is missing)
*   Issue 182 (.gn missing from 0.8.1 source release)

..  _Antares 0.8.2 sources: http://downloads.arescentral.org/Antares/antares-0.8.2.zip
..  _Antares 0.8.2 for Mac OS X 10.7+: http://downloads.arescentral.org/Antares/antares-mac-0.8.2.zip

..  -*- tab-width: 4; fill-column: 72 -*-
