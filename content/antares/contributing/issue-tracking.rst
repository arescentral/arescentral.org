Issue Tracking
==============

The Antares `issue tracker`_ tracks bugs and feature requests.  If you think
you've found a bug, or want to request a feature, please first search for it
to see if someone has already reported the issue.  If so, add any additional
information there.  If not, then `create a new issue`_.

..  _issue tracker: https://github.com/arescentral/antares/issues
..  _create a new issue: https://github.com/arescentral/antares/issues/new

Issue Lifecycle
---------------

New
~~~

When an issue is first reported, a developer will look at it, and
determine its priority.  Then, they will assign it and add a milestone
and one each of the ``Type``, ``Priority``, and ``Complexity`` labels.
Alternatively, they may determine that the issue is invalid, a
duplicate, or not desirable, and close it out instead.

Accepted
~~~~~~~~

Once an issue has an assignee, that person is responsible for ensuring
it is fixed by its milestone.  That does not necessarily entail fixing
it themselves; they could delegate to another developer by reassigning
the issue.  When a developer commits a fix, they will add the
``FixPending`` label.

FixPending
~~~~~~~~~~

An issue marked as ``FixPending`` is fixed in the repository, but not in
the most recent release.  When a developer releases a new version of
Antares, they will close all ``FixPending`` issues, indicating that the
fix is now available to users.

Closed
~~~~~~

An closed issue has been fixed, and the fix is available to users.  If
it turns out that he issue is not actually fixed, or if it regresses,
then the issue should be reopened or a new issue created (either is OK).

Labels
------

Milestone and Priority
~~~~~~~~~~~~~~~~~~~~~~

The milestone indicates the point by which the issue is expected to be
resolved.  ``Priority`` labels indicates how important it is that the
issue be resolved by the given milestone.  By nature, bugs assigned to a
hotfix milestone (N.N.X) will almost always be high-priority.  For other
milestones (N.0, N.X), high-priority issues will indicate the main goals
of the release.

Complexity
~~~~~~~~~~

``Complexity`` labels indicates a subjective assessment of how easy it
would be for a new-comer to fix the issue.  `Low-complexity bugs`_ are
good candidates for getting your feed wet with the Antares code base.
`High-complexity bugs`_ are to be avoided unless you're very familiar
with it.

..  _low-complexity bugs: http://code.google.com/p/antares/issues/list?q=Complexity:Low
..  _high-complexity bugs: http://code.google.com/p/antares/issues/list?q=Complexity:High

Miscellaneous
~~~~~~~~~~~~~

*   The ``Classic`` label indicates that an issue is believed to date from
    the original Ares source code, and was not introduced in Antares.

..  -*- tab-width: 4; fill-column: 72 -*-
