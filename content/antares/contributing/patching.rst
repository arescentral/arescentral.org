Submitting Patches
==================

Requirements
------------

Before submitting a patch, please check the following:

1.  Your patch branches from or applies cleanly to the ``master``
    branch of the repository.
2.  Your code conforms to the `style guidelines
    <{filename}/antares/contributing/style.rst>`_.
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

There are two ways to submit a patch against Antares:

1.  Mail it to the `development mailing list`_ as an attachment.
2.  Create a pull request against the `GitHub repository`_.

You can prepare a patch to be uploaded or mailed with ``git
format-patch``.

..  _issue tracker: https://github.com/arescentral/antares/issues
..  _development mailing list: https://groups.google.com/a/arescentral.org/group/antares-dev
..  _github repository: https://github.com/arescentral/antares

..  include:: ../../epilog.rsti

..  -*- tab-width: 4; fill-column: 72 -*-
