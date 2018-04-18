**************************
Making Nengo contributions
**************************

We welcome all sorts of contributions!
The list below is by no means exhaustive.

- **Create**: Use Nengo to make a model
  and share it with the community.
- **Report bugs**: Let us know if Nengo crashes
  or does something that you don't expect.
- **Develop**: Add or modify some code
  in a :ref:`Nengo project <Nengo ecosystem>`.
- **Document**: Teach others how to use Nengo
  by adding to or clarifying our documentation.

Sharing your creations
======================

There are several ways to
share your Nengo creations
with the community.
The quickest way is to make a post on the forum.

1. Head to `the examples category of the forum
   <https://forum.nengo.ai/c/examples-tutorials>`_.
2. If you don't yet have an account,
   click the "Sign Up" button at the top-right of the page.
3. Click on the "New Topic" button at the top-right.
4. Write your post with the editor that pops up.
   Format your post with
   `Markdown <http://commonmark.org/help/>`_ -- make
   sure you format code blocks so they're easier to read!

If your creation is too big for a forum post,
consider making a pull request on the
`the examples repository <https://github.com/nengo/nengo-examples>`_.

If your creation is already available online
(in Github, for example)
then consider making a pull request adding to the
`list of Nengo projects
<https://github.com/nengo/nengo.github.io/blob/src/projects.rst>`_.

Reporting bugs and suggesting features
======================================

If you find any bugs in any Nengo project,
or you think a particular feature would
fill a need that you have,
file an issue on project's Github repository.

1. Head to the project's Github page
   (e.g., `nengo/nengo-gui <https://github.com/nengo/nengo-gui>`_.
2. Click the "Issues" tab at the top of the page.
3. Click the green "New issue" button at the top-right of the page.

Be sure to include as much detail as you can
when filing issues,
especially when reporting bugs.
The first thing we do to fix bugs
is try to reproduce them locally.
Try to find the shortest script
or sequence of steps
to reproduce the bug.

Proposing a large change
========================

A large change is one that requires the public API
to change for more than one Nengo project,
or requires significant public API changes
for one core project.

To propose a large change,
make a pull request on the
`enhancement proposals repository
<https://github.com/nengo/enhancement-proposals>`_.
In your pull request, copy the `proposal template
<https://raw.githubusercontent.com/nengo/enhancement-proposals/master/000-template.rst>`_
to a new file with an appropriate title,
and edit the file to explain
the change you think should be made.

Making pull requests
====================

Whether you're sharing your creation,
developing a Nengo project,
or adding documentation,
we manage contributions with
`pull requests <https://help.github.com/articles/about-pull-requests/>`_.

1. If you are not yet a :ref:`contributor <People>`,
   then start by
   `forking the repository <https://help.github.com/articles/fork-a-repo/>`_
   you want to contribute to.
   If you are a contributor,
   then there is no need to make a fork.

2. Before making any changes to the repository,
   create a new branch for your change -- you
   should never edit code on the ``master`` branch!
   To create a branch, use the command

   .. code:: bash

      git checkout -b add-forum-link

   Make sure to give your branch a meaningful name.
   Names like ``patch`` or ``fix128``
   are hard to remember later on.

3. Make the changes you want to make to the repository.
   If your changes are large,
   split the changes up into separate meaningful commits.

   .. code:: bash

      git add README.rst
      git commit -m "Add forum link to README"

   Make sure you follow our :ref:`style guide <Style guide>`,
   including the :ref:`commit message format <Git>`.

4. Once your changes are done, push them to Github

   .. code:: bash

      git push origin add-forum-link

   and `make a pull request
   <https://help.github.com/articles/creating-a-pull-request/>`_.

5. Your pull request will undergo at least one review.
   Keep in mind that reviewing is a process
   that can take multiple iterations.
   Keep in mind the :ref:`code of conduct <Nengo Code of Conduct>`
   when responding to reviews.
