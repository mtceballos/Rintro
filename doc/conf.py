# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Rintro'
copyright = '2013-2026, M.T. Ceballos (IFCA), N. Cardiel (UCM)'
author = 'M.T. Ceballos (IFCA), N. Cardiel (UCM)'
release = '10.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.duration',]

templates_path = ['_templates']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
#html_theme = 'classic'
html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
html_logo = '_static/Rlogo.jpg'

# from previous configuration
#===============================
# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'
exclude_patterns = []
