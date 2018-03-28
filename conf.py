#!/usr/bin/env python3

from datetime import datetime
import os
import sys

import guzzle_sphinx_theme

sys.path.extend(os.path.dirname(__file__))
extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "guzzle_sphinx_theme",
    "custom",  # Loaded from the current directory
]

suppress_warnings = ['image.nonlocal_uri']
source_suffix = ".rst"
master_doc = "index"
exclude_patterns = [
    "_build", "Thumbs.db", ".DS_Store", "_records/*.rst", "overview.rst",
]

project = "Nengo"
copyright = "2016, Applied Brain Research"
author = "Applied Brain Research"
version = release = datetime.now().strftime("%Y-%m-%d")
language = None

todo_include_todos = False

intersphinx_mapping = {
    "nengo": ("https://www.nengo.ai/nengo/", None)
}

# HTML theming
pygments_style = "sphinx"
templates_path = ["_templates"]
html_static_path = ["_static"]

html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = "guzzle_sphinx_theme"

html_theme_options = {
    "project_nav_name": "Nengo",
    "base_url": "https://www.nengo.ai/",
}

# Other builders
htmlhelp_basename = "Nengo"

latex_elements = {
    # "papersize": "letterpaper",
    # "pointsize": "11pt",
    # "preamble": "",
    # "figure_align": "htbp",
}

latex_documents = [
    (master_doc,  # source start file
     "nengo.tex",  # target name
     "Nengo Documentation",  # title
     "Applied Brain Research",  # author
     "manual"),  # documentclass
]

man_pages = [
    # (source start file, name, description, authors, manual section).
    (master_doc, "nengo", "Nengo Documentation", [author], 1)
]

texinfo_documents = [
    (master_doc,  # source start file
     "Nengo",  # target name
     "Nengo Documentation",  # title
     author,  # author
     "Nengo",  # dir menu entry
     "Large-scale brain modelling in Python",  # description
     "Miscellaneous"),  # category
]

# Redirects are in the form (src, dst) where
# - src is the relative path from the build output directory
# - dst is the arbitrary URL you want to redirect to
redirects = []


def add_redirects(project, prefix, pages):
    newproject = project.replace("_", "-")
    for page in pages:
        fullpage = "%s%s%s" % (prefix, "/" if prefix != "" else "", page)
        redirects.append((
            "%s/%s" % (project, fullpage),
            "https://www.nengo.ai/%s/%s" % (newproject, fullpage),
        ))


# enhancement_proposals redirects

add_redirects("enhancement_proposals", "", [
    "001-template.html",
    "004-rejected-template.html",
    "100-pynn-backend.html",
    "400-multidim-radius.html",
    "401-probe-outputs.html",
    "402-ndarray-representation.html",
    "403-variable-synapse-defaults.html",
    "404-java-backend.html",
    "index.html",
    "README.html",
])

# nengo_extras redirects

add_redirects("nengo_extras", "", [
    "deeplearning.html",
    "deeplearning-examples.html",
    "dists.html",
    "index.html",
    "learning_rules.html",
    "networks.html",
    "neurons.html",
    "processes.html",
    "vision.html",
    "vision-examples.html",
    "visualization.html",
    "visualization-examples.html",
])

