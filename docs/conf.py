# TaiESM documentation configuration (NorESM-style: single-root Sphinx)
from datetime import datetime

project = "TaiESM-docs"
author = "AC3/AS-RCEC"
release = "latest"
copyright = f"{datetime.now():%Y} {author}"
root_doc = "index"

extensions = [
    "myst_parser",            # allow Markdown via MyST
   #"sphinxcontrib.bibtex",   # bibliography support if needed
]

# MyST options (you can still write RST primarily)
myst_enable_extensions = [
    "deflist",
    "fieldlist",
    "colon_fence",
    "attrs_block",
    "substitution",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 3,
}

# Paths for resources
import os
if not os.path.exists("_static"):
    os.makedirs("_static", exist_ok=True)
if not os.path.exists("_templates"):
    os.makedirs("_templates", exist_ok=True)
