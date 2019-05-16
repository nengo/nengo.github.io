**********************
Making Python releases
**********************

These instructions assume that
your project is using
`Nengo Bones <https://www.nengo.ai/nengo-bones/>`__
to generate CI scripts.

Stage 1: Release candidate
==========================

1. Switch to ``master`` and ensure it is up-to-date by doing ``git pull``.

2. Create a new branch off of ``master`` with the name
   ``release-candidate-X.Y.Z`` where ``X.Y.Z`` is the new version number.

3. Run all tests to ensure they pass on all supported platforms,
   including slow tests that are normally skipped.
   The exact command will depend on the repository,
   but for Nengo core it's

   .. code-block:: bash

      pytest --pyargs nengo --plots --analytics --logs --slow

4. Review all of the outputs (e.g., plots)
   generated from the test suite for abnormalities.

5. Build documentation and review it for abnormalities.

6. Commit all changes from the above steps.

7. Change the version information for your project.
   For most Python projects, it lives in ``project/version.py``.
   See that file for details.

8. Set the release date in the changelog, ``CHANGES.rst``.

9. ``git add`` the changes above and make a release commit with

   .. code-block:: bash

      git commit -m "Release version X.Y.Z"

10. Push with ``git push origin release-candidate-X.Y.Z``
    to start a TravisCI build that will run several checks
    to ensure that the repository is in a good state for release.

11. If the TravisCI build fails, fix the issues, commit them before the
    release commit, and push again.

12. When the TravisCI build succeeds,
    inspect the release and associated metadata and files at
    https://test.pypi.org/project/<project>/

    In particular, make sure that extraneous files are not
    included in the released files.
    File sizes give a good indication of whether
    extra files are present.

    If there are any issues, fix them and commit them before
    the release commit.

13. If any non-trivial changes were made in this process,
    open a pull request on the ``release-candidate-X.Y.Z`` branch
    to have the changes reviewed.

Stage 2: Tagged release
=======================

1. Merge the ``release-candidate-X.Y.Z`` branch into ``master``.

2. Tag the release commit with the version number; i.e.,

   .. code-block:: bash

      git tag -a vX.Y.Z

   We use annotated tags to retain authorship information.
   If you wish to provide a message with information about the release,
   feel free, but it is not necessary.

3. Change the version information in ``project/version.py``.

4. Make a new changelog section in ``CHANGES.rst``
   in order to collect changes for the next release.

5. ``git add`` the changes above and commit with

   .. code-block:: bash

      git commit -m "Starting development of vX.Y.Z+1"

6. ``git push origin master`` and ``git push origin vX.Y.Z``.
   Pushing the tag will trigger another TravisCI build that will
   deploy the release and updated documentation.

7. Confirm the release has been done successfully
   at https://pypi.org/project/<project>/
   once the TravisCI build is complete.

Stage 3: Announcing
===================

1. Copy the changelog into the tag details on the
   Github release tab.
   Note that the changelog is in reStructuredText,
   while Github expects Markdown.
   Use `Pandoc <http://pandoc.org/try/>`_
   to convert between the two formats
   with the following command:

   .. code-block:: bash

      pandoc -t markdown_github -f rst+hard_line_breaks CHANGES.rst

2. Write a release announcement.
   Generally, it's easiest to start from
   the last release announcement
   and change it to make sense with the current release
   so that the overall template of each announcement is similar.
   Post the release announcement on the
   `forum <https://forum.nengo.ai/c/general/announcements>`_.

3. Make a PR on the
   `ABR website repo <https://github.com/abr/abr.github.io>`__
   modifying a file in the ``_releases`` folder to
   point to the announcement post on the forum.
