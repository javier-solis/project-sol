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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

# The full version, including alpha/beta/rc tags
release = 'v1'

# == I added the following: ==
from datetime import date

todaysDate = date.today()

project = 'Project Sol'
copyright = str(todaysDate.year) + ", Javier Solis | Last Updated "+todaysDate.strftime("%b. %d, %Y") + " | Version " + release
author = 'Javier Solis'

	
# ===================



# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['myst_parser'] # Allows me to use .md files instead of .rst

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# == I added the following: ==
master_doc = 'index'
source_suffix = '.md'
# ====

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# == I added the following: ==

import furo

html_theme = 'furo'
html_logo = './images/logos/full-logo.png'
html_favicon = './images/favicon.ico'
html_title = "Project Sol"

html_theme_options = {
   "sidebar_hide_name": True  #This is Furo specific
}


# ====

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [ # I added this
    'css/custom.css'
]
