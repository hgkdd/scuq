# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'scuq'
copyright = '2025, Thomas Reidemeister, Hans Georg Krauthäuser'
author = 'Thomas Reidemeister, Hans Georg Krauthäuser'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_extra_path = ['../html']

import subprocess, os

read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'

if read_the_docs_build:
    subprocess.call('cd ..; doxygen readthedocs.cfg', shell=True)
#import subprocess
#subprocess.call('cd .. ; doxygen doc.cfg', shell=True)
