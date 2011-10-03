Issue Tracking
==============

The Antares `issue tracker`_ tracks bugs and feature requests.  If you think
you've found a bug, or want to request a feature, please first `search for it`_
to see if someone has already reported the issue.  If so, add any additional
information there.  If not, then `create a new issue`_.

..  _issue tracker: http://code.google.com/p/antares/issues/list
..  _search for it: http://code.google.com/p/antares/issues/advsearch
..  _create a new issue: http://code.google.com/p/antares/issues/entry

Issue Lifecycle
---------------

New
~~~

When an issue is first reported, it will be marked as ``New``.  At this point,
no one has considered the bug or feature request yet.  If a developer
determines the issue to be valid, they will mark it ``Accepted`` and also add,
at a minimum, the ``Milestone`` and ``Priority`` labels.  If they determine
that the issue should be ``Invalid``, ``Duplicate``, or ``WontFix``, they will
mark the issue as one of those instead.

Accepted
~~~~~~~~

Once a developer has marked a issue as ``Accepted``, they are
responsible for ensuring it is fixed by its ``Milestone``.  That does
not necessarily entail fixing it themselves; they could delegate to
another developer by reassigning the issue.  When a developer commits a
fix, they will mark it ``FixPending``.

FixPending
~~~~~~~~~~

An issue marked as ``FixPending`` is fixed in the repository, but not in
the most recent release.  When a developer releases a new version of
Antares, they will mark all ``FixPending`` issues as ``Fixed``,
indicating that the fix is now available to users.

Fixed
~~~~~

An issue marked as ``Fixed`` has been fixed, and the fix is available to
users.  If it turns out that he issue is not actually fixed, or if it
regresses, then the status should be changed back to ``New`` or a new
issue created (either is OK).

Labels
------

Milestone and Priority
~~~~~~~~~~~~~~~~~~~~~~

The ``Milestone`` label indicates the point by which the issue is
expected to be resolved.  It takes one of four values: "Hotfix",
"Minor", "Major", or "Later".  For example, if the most recent release
of Antares were to be 1.2.3, then a Hotfix bug would be expected to be
fixed in 1.2.4, a Minor bug by 1.3.0, and a Major bug by 2.0.0.

The ``Priority`` label indicates how important it is that the issue be
resolved by the given milestone.  By nature, Hotfix bugs will almost
always be high-priority.  For other milestones, high-priority issues
will indicate the main goals of the release.

Complexity
~~~~~~~~~~

The ``Complexity`` label indicates a subjective assessment of how easy
it would be for a new-comer to fix the issue.  `Low-complexity bugs`_
are good candidates for getting your feed wet with the Antares code
base.  `High-complexity bugs`_ are to be avoided unless you're very
familiar with it.

..  _low-complexity bugs: http://code.google.com/p/antares/issues/list?q=Complexity%3DLow
..  _high-complexity bugs: http://code.google.com/p/antares/issues/list?q=Complexity%3DHigh

Miscellaneous
~~~~~~~~~~~~~

*   The ``Classic`` label indicates that an issue is believed to date from
    the original Ares source code, and was not introduced in Antares.

*   The ``Xsera`` label indicates that the resolution of the issue may
    be of interest to the `Xsera`_ project.

..  _xsera: http://xsera.org/

..  -*- tab-width: 4; fill-column: 72 -*-
