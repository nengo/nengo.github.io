**********
Governance
**********

Roles
=====

All contributors
----------------

Nengo is developed by a
:ref:`team of contributors <People>`.
New contributors join the team
when they make a pull request
that gets merged in a Nengo project.

New contributors will also be added
to the `active contributors team
<https://github.com/orgs/nengo/teams/active-contributors>`_.
Members of this team have write access
to the repositories in the Nengo organization.
For security reasons,
contributors who have not
participated in an issue or pull request
in the past six months will be
removed from the active contributors team.

Maintainers
-----------

Every Nengo project has a primary maintainer,
who is responsible for merging pull requests
and making releases.
While the maintainer may delegate maintenance tasks
to other contributors,
they are always responsible for
guiding the project's overall direction.
The maintainer for each project is listed
on :ref:`the projects page <Nengo ecosystem>`.

Reviewers
---------

Nengo contributors can volunteer
to review a project's pull requests
by contacting the maintainer of that project.
Maintainers should ensure that all active reviewers
are included on `the active reviewers team
<https://github.com/orgs/nengo/teams/active-reviewers>`_.
As with the active contributors team,
reviewers who have not reviewed in the past six months
will be removed from the active reviewers team.

Policies
========

Development of all Nengo projects
happens on `Github <https://github.com/nengo>`_.
For projects in the Nengo organization,
we follow these policies.

1. We require that all contributors sign the
   :ref:`Nengo Contributor Assignment Agreement`.

2. We follow the
   `semantic versioning specification <http://semver.org/>`_.

3. We require that large changes to multiple projects
   be `proposed <https://github.com/nengo/enhancement-proposals>`_
   prior to implementation.

Projects that have not yet been released
are considered experimental,
and the contributors to those projects
are free to follow whatever practices
they prefer prior to the initial public release.

Once a project has had an initial public release,
it is considered under active development,
and follows these additional policies.

4. We require that all changes,
   even those made by the project maintainer,
   be proposed as a pull request.

5. We require that all pull requests be well tested.

6. We require that every pull request be reviewed
   by at least one reviewer.

7. We require that all pull requests be merged
   by the project maintainer.

Once a project has been deemed stable
by the project's maintainer,
it will have a version 1.0.0 release.
When a project hits this milestone,
it is considered stable.
Stable projects follow these additional policies.

8. We require that each commit passes all unit tests,
   including :ref:`style <Style guide>` checks.

9. We require that non-trivial pull requests include a changelog entry.

10. We require that every pull request be reviewed
    by at least two reviewers.

See the rest of the contributor guide
to further details on how to contribute
according to these policies.
