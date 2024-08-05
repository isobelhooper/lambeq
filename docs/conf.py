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

from lambeq import __version__ as version, __version_info__ as v
release = version


project = 'lambeq'
copyright = '2021-2024 Cambridge Quantum Computing Ltd.'
author = 'Cambridge Quantum QNLP Dev Team'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'nbsphinx',
    'numpydoc',
    'sphinx_mdinclude',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.graphviz',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.intersphinx',
    'sphinxarg.ext',
    'sphinxcontrib.jquery'
]

intersphinx_mapping = {
    'discopy': ("https://docs.discopy.org/en/main/", None),
    'pennylane': ("https://pennylane.readthedocs.io/en/stable/", None),
}

autodoc_default_options = {
    'members': True,
    'inherited-members': True,
    'undoc-members': True,
    'special-members': '__init__, __call__',
}

# This disables the need to document methods in the class docstring.
numpydoc_show_class_members = False

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
html_theme = 'sphinx_book_theme'
html_theme_options = {
  'navbar_start': ['navbar-root-logo'],
  'navbar_center': ['navbar-nav'],
  'navigation_depth': -1,
  'header_links_before_dropdown': 2,
}
html_context = {
  'display_github': True,
  'github_user': 'CQCL',
  'github_repo': 'lambeq',
  'github_version': 'main',
  'conf_py_path': '/docs/'
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_logo = '_static/images/lambeq_logo.png'
html_favicon = '_static/images/favicon.ico'

# CSS for allowing text wrapping within table cells
html_css_files = [
    'css/table-wrap.css',
    'css/custom.css',
]

def autodoc_skip_member(app, what, name, obj, skip, options):
    if name == 'Symbol':
        options['inherited-members'] = False
        return False
    return skip


def setup(app):
    app.connect('autodoc-skip-member', autodoc_skip_member)


numfig = True
