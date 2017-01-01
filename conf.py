#!/usr/bin/env python3

from datetime import datetime

import guzzle_sphinx_theme

extensions = ["sphinx.ext.intersphinx",
              "sphinx.ext.todo",
              "sphinx.ext.mathjax",
              "sphinx.ext.githubpages",
              "guzzle_sphinx_theme"]

source_suffix = ".rst"
master_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

project = "Nengo"
copyright = "2016, Applied Brain Research"
author = "Applied Brain Research"
version = release = datetime.now().strftime("%Y-%m-%d")
language = None

todo_include_todos = True

intersphinx_mapping = {
    "nengo": ("http://pythonhosted.org/nengo", None)
}

# HTML theming
pygments_style = "sphinx"
templates_path = ["_templates"]
html_static_path = []

html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = "guzzle_sphinx_theme"

html_theme_options = {
    "project_nav_name": "Nengo",
    "base_url": "https://nengo.github.io/",
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
