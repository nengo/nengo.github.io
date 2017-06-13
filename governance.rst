**********
Governance
**********

Roles
=====

Nengo is made by a
:ref:`team of contributors <People>`
who review each other's work.
New contributors join the team
when they make a pull request
that gets merged in a project
managed by the Nengo team.

In addition to being a contributor,
Nengo team members may
also be a maintainer and a reviewer.

Every Nengo project has a primary maintainer,
who is responsible for merging pull requests,
and making releases.
While the maintainer may delegate maintenance tasks
to other contributors,
they are always responsible for
guiding the project's overall direction.
The maintainer for each project is listed
on :ref:`the projects page <Nengo projects>`.

Nengo contributors can volunteer
to review a project's pull requests
by contacting the maintainer of that project.
Maintainers should ensure that all active reviewers
are listed in `the active reviewers Github team
<https://github.com/orgs/nengo/teams/active-reviewers>`_.

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
   be `proposed <https://github.com/nengo/enhancement_proposals>`_
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

Once a project has been deemed stable
by the project's maintainer,
it will have a version 1.0.0 release.
When a project hits this milestone,
it is considered stable.
Stable projects follow these additional policies.

7. We require that each commit passes all unit tests,
   including :ref:`style <Style guide>` checks.

8. We require that non-trivial pull requests include a changelog entry.

9. We require that every pull request be reviewed
   by at least two reviewers.

See the rest of the contributor guide
to further details on how to contribute
according to these policies.
