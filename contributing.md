---
layout: md_page
title: Contributing to Nengo

footerClasses: gradient-bottom
---

We welcome all sorts of contributions!
The list below is by no means exhaustive.

- **Create**: Use Nengo to make a model and share it with the community.
- **Report bugs**: Let us know if Nengo crashes or does something
  that you don't expect.
- **Develop**: Add or modify some code in a Nengo project.
- **Document**: Teach others how to use Nengo by adding to or
  clarifying our documentation.

## Sharing your creations

There are several ways to share your Nengo creations with the community.
The quickest way is to make a post on the forum.

1. Head to [the examples category of the forum](
   https://forum.nengo.ai/c/examples-tutorials).
2. If you don't yet have an account, click the "Sign Up" button at the
   top-right of the page.
3. Click on the "New Topic" button at the top-right.
4. Write your post with the editor that pops up. Format your post with
   [Markdown](http://commonmark.org/help/) -- make sure you format code
   blocks so they're easier to read!

If your creation is too big for a forum post,
consider making a pull request on the
[the examples repository](https://github.com/nengo/nengo-examples).

## Reporting bugs and suggesting features

If you find a bug in any Nengo project, or you think a particular
feature would fill a need that you have, file an issue on project's
Github repository.

1.  Head to the project's Github page (e.g.,
    [nengo/nengo-gui](https://github.com/nengo/nengo-gui)).
2.  Click the "Issues" tab at the top of the page.
3.  Click the green "New issue" button at the top-right of the page.

Be sure to include as much detail as you can when filing issues,
especially when reporting bugs. The first thing we do to fix bugs is try
to reproduce them locally. Try to find the shortest script or sequence
of steps to reproduce the bug.

## Making pull requests

Whether you're sharing your creation, developing a Nengo project, or
adding documentation, we manage contributions with [pull
requests](https://help.github.com/articles/about-pull-requests/).

1.  Start by [forking the repository](
    https://help.github.com/articles/fork-a-repo/) you want to contribute to
    and cloning it locally.

2.  Before making any changes to the repository, create a new branch for
    your change -- you should never edit code on the `master` branch!
    To create a branch, use the command

    ```bash
    git checkout -b <branch name>
    ```

    Make sure to give your branch a meaningful name. Names like `patch`
    or `fix128` are hard to remember later on.

3.  Make the changes you want to make to the repository. If your changes
    are large, split the changes up into separate meaningful commits.

    ```bash
    git add <files>
    git commit
    ```

    Make sure you follow our style guide,
    including the commit message format.

    <!-- TODO: link to style guide once it's up on NengoBones docs -->

4.  Once your changes are done, push them to Github

    ```bash
    git push origin <branch name>
    ```

    and [make a pull request](
    https://help.github.com/articles/creating-a-pull-request/)
    on the Nengo project's repository.

5.  Your pull request will undergo at least one review. Keep in mind
    that reviewing is a process that can take multiple iterations. Please
    follow the [code of conduct]({{ site.baseurl }}{% link conduct.md %})
    when responding to reviews.
