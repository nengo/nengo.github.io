**************
Reviewer guide
**************

The Nengo team has
varying backgrounds in software development,
neuroscience, machine learning, and many other areas.
We rely on each other to review our work
and ensure that our code is
correct, consistent, and documented.
Every pull request (PR) is reviewed by at least one person,
though usually two.

Guidelines
==========

We expect reviewers to be respectful, kind,
and to focus on the code and not the author of the code.
Even when we mean well,
words on a screen don't always convey the right tone.
We've found these guidelines to be helpful
for keeping the tone positive.

- Accept that many programming decisions are opinions.
  Discuss tradeoffs, which you prefer, and reach a resolution quickly.
- Ask questions; don't make demands.
  ("What do you think about naming this ``n_neurons``?")
- Ask for clarification. ("I don't understand this line. Can you clarify?")
- Avoid selective ownership of code. ("mine", "not mine", "yours")
- Avoid using terms that could be seen as referring to personal traits
  ("dumb", "stupid").
  Assume everyone is attractive, intelligent, and well-meaning.
- Be explicit. People may not understand your intentions.
- Be humble. ("I'm not sure---let's look it up.")
- Don't use hyperbole ("always", "never", "endlessly", "nothing").
- Be careful about the use of sarcasm.
  What seems like good-natured ribbing to you
  and a long-time colleague might come off
  as mean and unwelcoming to a person new to the project.
- Move to one-on-one chats or video calls
  if there are too many "I didn't understand"
  or "Alternative solution:" comments.
  Post a follow-up comment summarizing the offline discussion.

Becoming a reviewer
===================

Any Nengo contributor can volunteer to be a reviewer.
Head to the `list of Nengo teams <https://github.com/orgs/nengo/teams>`_
and request to join
the `Active reviewers team <https://github.com/orgs/nengo/teams/active-reviewers>`_.
If you've contributed to a Nengo project,
then its maintainer will assign you reviews
based on your contributions thus far.

You will be assigned
at most two reviews concurrently.
The reviews currently assigned to you
can be viewed `here <https://github.com/pulls/review-requested>`_.
Please respond to review requests within a week.
If you cannot review within a week,
please let the :ref:`project maintainer <Nengo ecosystem>`
know so that they can assign the review to someone else.

Reviewing a pull request
========================

1. Read through the code changes and commit messages.
2. Test that the PR does what it claims to do.
3. Make commits to propose changes.
4. Submit a Github review.

If any of the above steps are unclear, read on.

1. Reading code changes
-----------------------

Reading through code changes (often called diffs)
is a skill that takes a fair bit
of practice---but the only way to practice is by doing it!
A useful exercise when starting out is to read diffs
for new PRs even if you aren't assigned to review that PR.

There are two ways to read code diffs.

1. Read the diff of the entire PR.

   In Github, this is found in the "Files changed" tab of the PR.
   This works best for quick and average length PRs
   that change only one area of the codebase.

2. Read the diff commit-by-commit.

   In Github, this is found in the "Commits" tabs of the PR.
   There are links in each commit to the previous and next commits
   to make reading the diff easier.
   This works best for lengthy PRs,
   or average length PRs that change multiple areas
   of the codebase.

In general, start by looking at the diff of the entire PR.
If it's difficult to read,
switch to reading the diff commit-by-commit.
If reading the diff commit-by-commit is difficult,
then ask the PR author to make the history of the PR easier to read.

In reading through the code diff:

- Try to be thorough to reduce the number of iterations.
- Seek to understand the author's perspective.
- Identify ways to simplify the code while still solving the problem.
- If you don't understand a piece of code, say so.
  There's a good chance someone else would be confused by it as well.

2. Testing the PR
-----------------

In general, we rely on automated testing to ensure that
the code introduced in a PR works as advertised.

- For new features, the PR should include tests
  to ensure the new code is correct.
- For bugfixes, the PR should include a test that fails
  without the changes in the PR.
- For refactorings, optimizations, and other improvements
  that do not fix bugs or add new features,
  existing tests should cover the new code.

In all of these cases,
run the appropriate parts of the test suite locally
to ensure that the tests pass.

If the PR does not include tests,
we encourage you to add those tests
as a part of your review.
Adding tests helps you understand the PR better,
and helps everyone in the project
by ensuring the codebase works as expected.
However, if you do not have time to write tests,
requesting that they be added
is a valid resolution to a review.

3. Making commits to propose changes
------------------------------------

Instead of asking the PR author to make changes,
we prefer reviewers make commits
to propose changes to a PR.
Commits allow the reviewer to propose explicit
changes that the PR author can say yes or no to,
rather than placing the burden on the PR author
and allowing for miscommunication.

There are three types of commits that reviewers can add,
depending on the type of change proposed.

1. ``fixup`` commits should be used for minor changes
   like style fixes, moving code from one location to another,
   and fixing small bugs.
   In the end, your ``fixup`` commit will not appear in
   the history of the ``master`` branch.

   To make a ``fixup`` commit, make your changes, then

   .. code:: bash

      git add -A
      git commit --fixup <commit>

   where ``<commit>`` corresponds to the commit
   that your ``fixup`` commit modifies
   (e.g., ``HEAD``, ``6be9830``).

2. ``squash`` commits should be used for minor changes
   that require some explanation.
   In the end, your ``squash`` commit will not appear in
   the history of the ``master`` branch,
   except in one or more commit messages.

   To make a ``squash`` commit, make your changes, then

   .. code:: bash

      git add -A
      git commit --squash <commit hash>

   Unlike with the ``--fixup`` option, git will now prompt you
   to enter a message to explain what your ``squash`` commit does.
   Since ``squash`` commits contain a commit message,
   maintainers will review the message when merging
   that branch into ``master`` and incorporate it in
   the squashed commit message if appropriate.

3. Normal commits should be used for major changes
   that should be reflected in the git history post-merge.
   If you're not sure whether it should be in the history,
   make a normal commit anyway
   as the maintainer will reorganize history as they see fit.

Please note that
all commits should be made at the end of the branch!
The history of the PR branch should not be rewritten
until it is being merged.

4. Submitting a Github review
-----------------------------

Once you've looked over the code
and made your changes,
finalize your review by submitting it through Github.

1. Click on the "Files changed" tab
   underneath the title of the PR.

2. If you wish to point out specific changes that you made,
   or specific parts of the code that need improvement,
   `make an inline comment
   <https://help.github.com/assets/images/help/commits/hover-comment-icon.gif>`_.
   With your first inline comment,
   click on the green "Start a review" button.

3. Once you've left all your comments,
   click on the "Review changes" button at the top-right of the page.

4. Write a review summary. This is **not** optional!

   The summary is a good place to sum up your thoughts on the PR
   and be explicit about next steps.
   Even if you've left lots of nitpicky inline comments,
   the tone of the review can be positive with a supportive review summary
   (e.g., "I made lots of little style fixes,
   but this improves the widget implementation significantly!").

5. Decide to approve the PR or request changes,
   and click "Submit review".

When writing feedback in comments or the review summary,
clearly communicate when you feel strongly about a change,
and when you are okay with the PR without that change.
Offer alternative implementations,
but assume the author has already considered them.

Keep in mind that there is a difference
in doing things right and doing things right now.
Ideally, we should do things right,
but a suboptimal PR often better than no PR at all.
Asking the PR author to do major refactoring
in the pull request is a big ask.
These things can always happen later,
unless you feel strongly that
the current design
will cause serious problems in the future.
