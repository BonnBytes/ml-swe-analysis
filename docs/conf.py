"""Sphinx configuration."""

import os
import sys
from importlib.metadata import version as _pkg_version

sys.path.insert(0, os.path.abspath("../src"))

project = "paper_crawler"
author = "Moritz Wolter, Lokesh Veeramacheneni, Charles Tapley Hoyt"
copyright = "2026, Moritz Wolter, Lokesh Veeramacheneni, Charles Tapley Hoyt"
release = _pkg_version("paper_crawler")
version = release

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.bibtex",
]

# Your docstrings use Google style (Args:/Returns:).
napoleon_google_docstring = True
napoleon_numpy_docstring = False

autodoc_typehints = "description"
autodoc_member_order = "bysource"
autodoc_default_options = {"members": True, "undoc-members": False}

# plot_counters.py imports these, but they are not in pyproject dependencies.
# Without mocking them, autodoc import fails, and `-W` turns that into a build error.
autodoc_mock_imports = ["matplotlib", "matplot2tikz", "numpy"]

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

bibtex_bibfiles = ["../CITATION.bib"]

html_theme = "sphinx_book_theme"
html_title = "paper_crawler"
html_theme_options = {
    "repository_url": "https://github.com/BonnBytes/position_we_need_more_tests_in_ml",
    "use_repository_button": True,
}