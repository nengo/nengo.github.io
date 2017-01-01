**************
How we use git
**************

Development happens on `Github <https://github.com/nengo>`_.
Feel free to fork any of our repositories and send a pull request!
However, note that we ask contributors to sign
:ref:`an assignment agreement <caa>`.

Rules
-----

We use a pretty strict ``git`` workflow
to ensure that the history of the ``master`` branch
is clean and readable.

1. Every commit in the ``master`` branch should pass testing,
   including static checks like ``flake8`` and ``pylint``.
2. Commit messages must follow guidelines (see below).
3. Developers should never edit code on the ``master`` branch.
   When changing code, create a new topic branch for your contribution.
   When your branch is ready to be reviewed,
   push it to Github and create a pull request.
4. Pull requests must be reviewed by at least two people before merging.
   There may be a fair bit of back and forth before
   the pull request is accepted.
5. Pull requests cannot be merged by the creator of the pull request.
6. Only `maintainers <https://github.com/orgs/nengo/teams>`_,
   can merge pull requests to ensure that the history remains clean.

Commit messages
---------------

We use several advanced ``git`` features that
rely on well-formed commit messages.
Commit messages should fit the following template.

.. code-block:: none

   Capitalized, short (50 chars or less) summary

   More detailed body text, if necessary.  Wrap it to around 72 characters.
   The blank line separating the summary from the body is critical.

   Paragraphs must be separated by a blank line.

   - Bullet points are okay, too.
   - Typically a hyphen or asterisk is used for the bullet, followed by
     single space, with blank lines before and after the list.
   - Use a hanging indent if the bullet point is longer than a
     single line (like in this point).
