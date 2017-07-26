"""Custom docutils / Sphinx directives specific to nengo.github.io."""

from docutils import nodes
from docutils.parsers.rst import Directive, directives


class Project(Directive):
    """The Project directive is used to describe Nengo projects.

    It attempts to give an attractive and uniform appearance to
    each project listing with minimal effort for authors.
    """

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "repo": directives.unchanged_required,
        "maintainer": directives.unchanged_required,
        "contact": directives.unchanged,
        "pypi": directives.unchanged,
        "docs": directives.unchanged,
    }
    has_content = True

    @staticmethod
    def linked_image(img, href, **image_args):
        a = nodes.reference(refuri=href)
        a += nodes.image(uri=img, **image_args)
        return a

    def run(self):
        self.assert_has_content()

        # Get info from directive
        name = self.arguments[0].strip()
        org, repo = self.options["repo"].strip().split("/")
        maintainer = self.options["maintainer"]
        contact = self.options.get("contact", None)
        pypi = self.options.get("pypi", None)
        docs = self.options.get("docs", None)

        # Parent container holds info and description
        parent = nodes.container()
        parent["classes"].append("project")
        self.add_name(parent)

        # Make a container for meta-info about the project
        info = nodes.container()
        info["classes"].append("project-info")
        # Title contains name, linked to docs if available
        title = nodes.strong(self.block_text, name)
        if docs is not None:
            title = nodes.strong(self.block_text)
            title += nodes.reference(refuri=docs, text=name)
        info += title

        shields = "https://img.shields.io"
        # Badges contains links to Github, PyPI, etc
        badges = nodes.paragraph(self.block_text)
        badges["classes"].append("project-badges")

        if docs is not None:
            badges += self.linked_image(
                img="%s/badge/documentation--green.svg?style=social" % shields,
                href=docs)

        badges += self.linked_image(
            img="%s/github/stars/%s/%s.svg?style=social&label=Github" % (
                shields, org, repo),
            href="https://github.com/%s/%s" % (org, repo))

        if pypi is not None:
            badges += self.linked_image(
                img="%s/pypi/v/%s.svg" % (shields, pypi),
                href="https://pypi.python.org/pypi/%s" % (pypi,))
        info += badges

        # List maintainer
        maint = nodes.paragraph(self.block_text)
        maint["classes"].append("project-maintainer")

        maint += nodes.inline(self.block_text, "Maintainer: ")
        if org == "nengo":
            maint += self.linked_image(
                img="https://www.nengo.ai/design/_images/small-light.svg",
                href="https://github.com/nengo",
                alt="Managed by Nengo team",
                height="16px")
        if contact is not None:
            contact_node = nodes.reference(refuri="mailto:%s" % contact)
            maint += contact_node
        else:
            contact_node = maint
        contact_node += nodes.inline(self.block_text, maintainer)
        info += maint

        # Make a container for the description
        description = nodes.container()
        description["classes"].append("project-description")
        self.state.nested_parse(self.content, self.content_offset, description)

        # Add to parent container
        parent += info
        parent += description
        return [parent]


def setup(app):
    app.add_directive("project", Project)

    return {"version": "0.1.1"}
