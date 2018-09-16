**********************
Making Python releases
**********************

There are three stages to this process,
which will result in at least
two ``git`` commits and one ``git`` tag.

Stage 1: Preparing
==================

Before making a release,
we do a few things to prepare:

1. Ensure ``master`` is up-to-date by doing ``git pull``.

2. Run `check-manifest <https://pypi.python.org/pypi/check-manifest>`_
   to ensure that all files are included in the release.

3. Run all tests to ensure they pass on all supported platforms,
   including slow tests that are normally skipped.
   The exact command will depend on the repository,
   but for Nengo core it's

   .. code-block:: bash

      pytest --pyargs nengo --plots --analytics --logs --slow

4. Review all of the outputs (e.g., plots)
   generated from the test suite for abnormalities.

5. Run all tests for projects that depend on your project.
   For example, Nengo OCL depends on Nengo core
   so we run those tests with

   .. code-block:: bash

      pytest --pyargs nengo --plots --simulator nengo_ocl.Simulator

   If any tests fail, attempt to fix them in your project.
   If they cannot be fixed and require upstream changes,
   then file an issue with that project or contact its maintainer
   to determine how to proceed.

6. Build documentation and review it for abnormalities.

7. Commit all changes from the above steps before moving on to the next stage.

Note that any fixes done as a result of
Stage 1 should be done through the normal process of making
a pull request and going through review.
However, from Stage 2 onward, the work is done directly
on the ``master`` branch.
Proceed with caution!

Stage 2: Releasing
==================

Once everything is prepared, we're ready to do the release.
It should be okay to work in the same directory that you
do development, but if you want to be extra safe,
you can do a fresh clone of the repository
into a separate directory.

1. Change the version information for your project.
   For most Python projects, it lives in ``project/version.py``.
   See that file for details.

2. Set the release date in the changelog (usually ``CHANGES.rst``).

3. Run ``collective.checkdocs`` to ensure proper formatting for PyPI.

   .. code-block:: bash

      python setup.py checkdocs

4. ``git add`` the changes above and make a release commit with

   .. code-block:: bash

      git commit -m "Release version X.Y.Z"

5. Create release packages.
   We build source distributions and wheels whenever possible.

   .. code-block:: bash

      python setup.py sdist bdist_wheel

6. Review the release packages to ensure extra files
   (like those in ``.ipynb_checkpoints``) are not included.
   The size of the package is a good indication of whether
   extra files are present.

7. Upload the release packages to PyPI.

   .. code-block:: bash

      twine upload dist/<package-version>.tar.gz
      twine upload dist/<package-version-extratags>.whl

8. Tag the release commit with the version number; i.e.,

   .. code-block:: bash

      git tag -a vX.Y.Z

   We use annotated tags for the authorship information;
   if you wish to provide a message with information about the release,
   feel free, but it is not necessary.

9. ``git push origin master`` and ``git push origin vX.Y.Z``.
   Pushing the tag will trigger a build and deployment of the documentation.

Stage 3: Cleaning up
====================

Your project is now released!
We need to do a few last things to
put it back in a development state.

1. Change the version information in ``project/version.py``.
   See that file for details.

2. Make a new changelog section in ``CHANGES.rst``
   in order to collect changes for the next release.

3. ``git add`` the changes above and make a commit describing
   the current state of the repository and commit with

   .. code-block:: bash

      git commit -m "Starting development of vX.Y.Z"

4. ``git push origin master``

Stage 4: Announcing
===================

Now we have to let the world know about the new release.
We do this in two ways for each release.

1. Copy the changelog into the tag details on the
   Github release tab.
   Note that the changelog is in reStructuredText,
   while Github expects Markdown.
   Use `Pandoc <http://pandoc.org/try/>`_ or a similar tool
   to convert between the two formats.
   For Pandoc, we recommend the following command

   .. code-block:: bash

      pandoc -t markdown_github -f rst+hard_line_breaks CHANGES.rst

2. Write a release announcement.
   Generally, it's easiest to start from
   the last release announcement
   and change it to make sense with the current release
   so that the overall template of each announcement is similar.

All release announcements should be posted
on the `forum <https://forum.nengo.ai/c/general/announcements>`_
and on the `ABR website <http://appliedbrainresearch.com/>`_.

For a major release
(e.g., the first release of a new backend,
or a milestone release like 1.0),
consider writing a more general and
elaborate announcement and posting it to wider-reaching venues, such as
`the comp-neuro mailing list <http://www.tnb.ua.ac.be/mailman/listinfo/comp-neuro>`_,
`Planet SciPy <https://planet.scipy.org/>`_,
and `Planet Python <http://planetpython.org/>`_.
