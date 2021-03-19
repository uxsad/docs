# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import yaml
from urllib.request import urlopen
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'UX-SAD Documentation'
copyright = '2021, Andrea Esposito'
author = 'Andrea Esposito'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'default'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Subproject's links
rtd_version = os.environ.get("READTHEDOCS_VERSION", "latest")
intersphinx_mapping = {
    "emotion-analysis": (
        "https://uxsad.readthedocs.io/projects/emotion-analysis/en/%s/" % rtd_version,
        None,
    ),
    "ai-models": (
        "https://uxsad.readthedocs.io/projects/ai-models/en/%s/" % rtd_version,
        None,
    ),
}

PROJECT_SLUG = "uxsad"
d = yaml.safe_load(urlopen("https://raw.githubusercontent.com/uxsad/docs/master/sidebar.yml"))
with open(".sidebar.rst", "w") as f:
    for proj in d["projects"]:
        if proj not in d["toctrees"]:
            continue
        print(".. toctree::", file=f)
        print("   :maxdepth: 2", file=f)
        print("   :caption: {}".format(d["toctrees"][proj]["name"]), file=f)
        print(file=f)
        for item in d["toctrees"][proj]["items"]:
            if proj == PROJECT_SLUG:
                args = (item['title'], item['link'])
            else:
                args = (item['title'], d["projects"][proj] + '/en/' + rtd_version + '/' + item['link'] + ".html")
            print("   {} <{}>".format(*args), file=f)

