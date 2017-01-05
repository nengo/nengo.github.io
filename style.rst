***********
Style guide
***********

Python
======

We adhere to
`PEP8 <http://www.python.org/dev/peps/pep-0008/>`_,
and use ``flake8`` to automatically check for adherence on all commits.
If you want to run this yourself,
then ``pip install flake8`` and run

.. code-block:: bash

   flake8 nengo

in the ``nengo`` repository you cloned.

Class member order
------------------

In general, we stick to the following order for members of Python classes.

1. Class-level member variables (e.g., ``nengo.Ensemble.probeable``).
2. Parameters (i.e., classes derived from `nengo.params.Parameter`)
   with the parameters in ``__init__`` going first in that order,
   then parameters that don't appear in ``__init__`` in alphabetical order.
   All these parameters should appear in the Parameters section of the docstring
   in the same order.
3. ``__init__``
4. Other special (``__x__``) methods in alphabetical order,
   except when a grouping is more natural
   (e.g., ``__getstate__`` and ``__setstate__``).
5. ``@property`` properties in alphabetical order.
6. ``@staticmethod`` methods in alphabetical order.
7. ``@classmethod`` methods in alphabetical order.
8. Methods in alphabetical order.

"Hidden" versions of the above (i.e., anything starting with an underscore)
should either be placed right after they're first used,
or at the end of the class.
Also consider converting long hidden methods
to functions placed in the ``nengo.utils`` module.

.. note:: These are guidelines that should be used in general,
          not strict rules.
          If there is a good reason to group differently,
          then feel free to do so, but please explain
          your reasoning in code comments or commit notes.

Docstrings
----------

We use ``numpydoc`` and
`NumPy's guidelines for docstrings
<https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt>`_,
as they are readable in plain text and when rendered with Sphinx.

We use the default role of ``obj`` in documentation,
so any strings placed in backticks in docstrings
will be cross-referenced properly if they
unambiguously refer to something in the Nengo documentation.
See `Cross-referencing syntax
<http://www.sphinx-doc.org/en/stable/markup/inline.html#cross-referencing-syntax>`_
and the `Python domain
<http://www.sphinx-doc.org/en/stable/domains.html>`_
for more information.

A few additional conventions that we have settled on:

1. Default values for parameters should be specified next to the type.
   For example::

     radius : float, optional (Default: 1.0)
         The representational radius of the ensemble.

2. Types should not be cross-referenced in the parameter list,
   but can be cross-referenced in the description of that parameter.
   For example::

     solver : Solver
         A `.Solver` used in the build process.

Git
===

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

.. todo:: JS, TS, CSS, HTML, etc
