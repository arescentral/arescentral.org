Issue Tracking
==============

The Antares `issue tracker`_ tracks bugs and feature requests.  If you
think you've found a bug, or want to request a feature, please first
search for it to see if someone has already reported the issue.  If so,
add any additional information there.  If not, then `create a new
issue`_.

..  _issue tracker: https://github.com/arescentral/antares/issues
..  _create a new issue: https://github.com/arescentral/antares/issues/new

Creating an issue requires a GitHub account. If you don’t have one, and
don’t want to create one, you can also `email the maintainers`_.

.. _email the maintainers: mailto:antares-dev@arescentral.org

Labels
------

Type
~~~~

Either ``Type:Defect`` for bugs, ``Type:Enhancement`` for feature
requests, or ``Type:Task`` for actions that need to be taken outside the
Antares code base. Always present.

Milestone and Priority
~~~~~~~~~~~~~~~~~~~~~~

The milestone indicates the point by which the issue is expected to be
resolved.  ``Priority`` labels indicates how important it is that the
issue be resolved by the given milestone. Always present.

Complexity
~~~~~~~~~~

``Complexity`` labels indicates a subjective assessment of how easy it
would be for a new-comer to fix the issue.  `Low-complexity issues`_ are
good candidates for getting your feet wet with the Antares code base.
`High-complexity issues`_ are to be avoided unless you're very familiar
with it. Always present.

.. _low-complexity issues: https://github.com/arescentral/antares/issues?q=is%3Aissue+is%3Aopen+label%3AComplexity%3ALow
.. _high-complexity issues: https://github.com/arescentral/antares/issues?q=is%3Aissue+is%3Aopen+label%3AComplexity%3AHigh

Project
~~~~~~~

Many issues are grouped into thematic projects_, like “improve OpenGL
support” or “port to Windows”. ``Project`` labels mark these. Often
present.

.. _projects: https://github.com/arescentral/antares/projects

OS and Arch
~~~~~~~~~~~

``OS`` and ``Arch`` labels mark the bug as specific to a particular
operating system or CPU architecture, such as ``OS:Mac Arch:arm`` for
Apple Silicon.

Input
~~~~~

Issues related to a specific mode of game input, such as mouse,
keyboard, gamepad, Touch Bar, or Power Glove.

Miscellaneous
~~~~~~~~~~~~~

``Classic``:
   Issues believed to date from the original Ares source code, and are
   not specific to Antares.

``Compatibility``:
   Issues that are difficult to resolve because replays, net games, and
   the test suite rely on the current behavior. Changing the behavior
   without due caution would cause desynchronization. Always
   ``Complexity:High``.

``Data``:
   Issues which require changes to the bundled data.

``Documentation``:
   Issues which require changes to documentation, in the docs/ directory
   or in the arescentral.org site.

``HiDPI``:
   Issues which manifest themselves on high-resolution displays, such as
   Apple Retina displays.

``Maintainability``:
   Issues concerning long-term maintainability of Antares.

``Performance``:
   Issues which cause slowness or other problems with responsiveness.

``Stability``:
   Issues which cause crashes or other severe problems.

``Testing``:
   Issues related to the test suite.

..  -*- tab-width: 3; fill-column: 72 -*-
