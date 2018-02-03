0.8.2 Release Candidate
=======================

:date:      2017-01-19
:author:    sfiera
:tags:      antares, mac, linux, preview

I've cut a release candidate for Antares 0.8.2:

*   Download |antares-0.8.2~rc1-mac|_.
*   Download the |antares-0.8.2~rc1-src|_.

As with all release candidates, bugs_ or reports_ are welcome.

The 0.8.2 release should fix the following issues:

*   Issue 173 (Build .deb for Debian and Ubuntu)
*   Issue 181 (Use system libraries when possible)
*   Issue 182 (.gn missing from 0.8.1 source release)
*   Issue 183 (Warn when $PREFIX/share/antares/app is missing)
*   Issue 184 (Look for scenarios in $PREFIX/share/games/antares/)
*   Issue 185 (Linux preferences reset on each run)
*   Issue 186 (Supported OS X version not set correctly)

As with 0.8.1, these are mostly of interest to Linux users, but for Mac
users, the supported version of OS X has been rolled back to 10.7+ (it
was formerly 10.9+).

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

..  _bugs: https://github.com/arescentral/antares/issues/new
..  _reports: mailto:sfiera@twotaled.com
..  |antares-0.8.2~rc1-mac| replace:: Antares 0.8.2~rc1 for Mac OS X 10.7+
..  |antares-0.8.2~rc1-src| replace:: Antares 0.8.2~rc1 sources
..  _antares-0.8.2~rc1-mac: http://downloads.arescentral.org/Antares/antares-mac-0.8.2~rc1.zip
..  _antares-0.8.2~rc1-src: http://downloads.arescentral.org/Antares/antares-0.8.2~rc1.zip

..  -*- tab-width: 4; fill-column: 72 -*-
