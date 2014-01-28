Submitting Patches
==================

Requirements
------------

Before submitting a patch, please check the following:

1.  Your patch branches from or applies cleanly to the ``develop``
    branch of the repository.
2.  Your code conforms to the :doc:`style guidelines <style>`.
3.  You have run the tests, and all of them pass.
4.  If you've never committed to Antares before, your first commit must
    add your name and contact information to the ``AUTHORS`` file.  That
    commit's description must state your intent to license your work on
    Antares under the |lgpl3|.  That commit must be a parent of
    subsequent commits.

If you've fixed a bug, it would be great to add a test to prevent
regressions in the future.  If you do add a test, consider ordering your
commits so that the test is added before the fix, and submitting a
patch-set so that it's easy to verify before/after the bugfix.

Process
-------

There are three ways to submit a patch against Antares:

1.  Upload it to an issue in the `issue tracker`_.
2.  Mail it to the `development mailing list`_ as an attachment.
3.  Create a pull request against the `GitHub repository`_.

You can prepare a patch to be uploaded or mailed with ``git
format-patch``.

..  _issue tracker: http://code.google.com/p/antares/issues/list
..  _development mailing list: https://groups.google.com/a/arescentral.org/group/antares-dev
..  _github repository: https://github.com/arescentral/antares

..  -*- tab-width: 4; fill-column: 72 -*-
