#
# statsmodels documentation build configuration file, created by
# sphinx-quickstart on Sat Jan 22 11:17:58 2011.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import contextlib
from packaging.version import parse
import os
from os.path import dirname, join
import sys
from jinja2 import FileSystemLoader, Environment

import yaml
from numpydoc.xref import DEFAULT_LINKS

from statsmodels import __version__

# -- Monkey Patch ----------------------------------------------------------
#  Monkey patch contextlib.contextmanager.__doc__ to avoid noise
contextlib.contextmanager.__doc__ = ''

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../sphinxext'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc',
              # numpydoc or sphinx.ext.napoleon, but not both
              'numpydoc',
              'sphinx.ext.doctest',
              'sphinx.ext.extlinks',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.autosectionlabel',
              # One of mathjax or imgmath
              'nbsphinx',
              'sphinx.ext.mathjax',
              'sphinx.ext.viewcode',
              # 'sphinx.ext.autosummary',
              'sphinx.ext.inheritance_diagram',
              'matplotlib.sphinxext.plot_directive',
              'IPython.sphinxext.ipython_console_highlighting',
              'IPython.sphinxext.ipython_directive',
              "sphinx_immaterial",
              ]

try:
    import sphinxcontrib.spelling  # noqa: F401
except ImportError as err:  # noqa: F841
    pass
else:
    extensions.append('sphinxcontrib.spelling')

# nbsphinx options
nbsphinx_allow_errors = True
# sphinxcontrib-spelling options
spelling_word_list_filename = ['spelling_wordlist.txt', 'names_wordlist.txt']
spelling_ignore_pypi_package_names = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'statsmodels'
copyright = '2009-2023, Josef Perktold, Skipper Seabold, Jonathan Taylor, statsmodels-developers'

autosummary_generate = True
autoclass_content = 'class'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

release = __version__

parsed_version = parse(release)
commit = ''
full_version = short_version = version = release
if parsed_version.is_devrelease:
    short_version = parsed_version.base_version
    commit = parsed_version.dev
    version = short_version + f' (+{commit})'
project = f"{project} {version}"
# Remove release to prevent it triggering a conf change
del release

# set inheritance_graph_attrs
# you need graphviz installed to use this
# see: http://sphinx.pocoo.org/ext/inheritance.html
# and graphviz dot documentation http://www.graphviz.org/content/attrs
# NOTE: giving the empty string to size allows graphviz to figure out
# the size
inheritance_graph_attrs = dict(size='""', ratio='compress', fontsize=14,
                               rankdir='LR')

# inheritance_node_attrs = dict(shape='ellipse', fontsize=14, height=0.75,
#                              color='dodgerblue1', style='filled')

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '**.ipynb_checkpoints', '*/autosummary/*.rst',
                    'Thumbs.db', '.DS_Store']

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


# Options for HTML output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'sphinx_immaterial'
html_title = project
html_short_title = project
html_extra_path = ['version_info/versions-v3.json']
# material theme options (see theme.conf for more information)

site_url = 'https://statsmodels.org/'
site_url += 'stable/' if full_version == version else 'devel/'

# sphinx_immaterial theme options
html_theme_options = {
    "icon": {"repo": "fontawesome/brands/github"},
    "site_url": site_url,
    "repo_url": "https://github.com/statsmodels/statsmodels/",
    "repo_name": "statsmodels",
    "palette": {"primary": "indigo", "accent": "blue"},
    "globaltoc_collapse": True,
    "toc_title": "Contents",
    "version_dropdown": True,
    "version_json": "../versions-v3.json",
    "toc_title_is_page_title": True,
    "social": [
        {
            "icon": "fontawesome/brands/github",
            "link": "https://github.com/statsmodels/statsmodels/",
            "name": "Source on github.com",
        },
        {
            "icon": "fontawesome/brands/python",
            "link": "https://pypi.org/project/statsmodels/",
        },
        {
            "icon": "fontawesome/solid/quote-left",
            "link": "https://doi.org/10.5281/zenodo.593847",
        },
    ],
}

language = 'en'
html_last_updated_fmt = ''

# Disable typehints
autodoc_typehints = "none"

# html_theme = 'default'


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.

# The name for this set of Sphinx documents.  If None, it defaults to
# '<project> v<release> documentation'.
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'images/statsmodels-logo-v2-bw.svg'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'images/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, 'Created using Sphinx' is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, '(C) Copyright ...' is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. '.xhtml').
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'statsmodelsdoc'

# Options for LaTeX output

# The paper size ('letter' or 'a4').
# latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author,
# documentclass [howto/manual]).
latex_documents = [
    ('index', 'statsmodels.tex', 'statsmodels Documentation',
     'Josef Perktold, Skipper Seabold', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For 'manual' documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True

# imgmath options
imgmath_image_format = 'png'
imgmath_latex_preamble = r'\usepackage[active]{preview}'
imgmath_use_preview = True

# Options for manual page output

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'statsmodels', 'statsmodels Documentation',
     ['Josef Perktold, Skipper Seabold, Jonathan Taylor'], 1)
]

# Options for Epub output

# Bibliographic Dublin Core info.
epub_title = 'statsmodels'
epub_author = 'Josef Perktold, Skipper Seabold'
epub_publisher = 'Josef Perktold, Skipper Seabold'
epub_copyright = '2009-2023, Josef Perktold, Skipper Seabold, ' \
                 'Jonathan Taylor, statsmodels-developers'

# The language of the text. It defaults to the language option
# or en if the language is not set.
# epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
# epub_identifier = ''

# A unique identification for the text.
# epub_uid = ''

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_post_files = []

# A list of files that should not be packed into the epub file.
# epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
# epub_tocdepth = 3

# Allow duplicate toc entries.
# epub_tocdup = True

# Numpydoc options
# numpydoc_attributes_as_param_list = True
# numpydoc_show_class_members = False
# numpydoc_show_inherited_class_members = True

# Create xrefs
numpydoc_xref_param_type = True
numpydoc_class_members_toctree = False
numpydoc_xref_aliases = DEFAULT_LINKS.copy()
numpydoc_xref_aliases.update({
    'Figure': 'matplotlib.figure.Figure',
    'Axes': 'matplotlib.axes.Axes',
    'AxesSubplot': 'matplotlib.axes.Axes',
    'DataFrame': 'pandas.DataFrame',
    'Series': 'pandas.Series',
    'MLEResults': 'statsmodels.tsa.statespace.mlemodel.MLEResults'
})

# NBSphinx options
nbsphinx_execute = "never"

# Example configuration for intersphinx: refer to the Python standard library.
# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'python': ('https://docs.python.org/3/', None),
    'pydagogue': ('https://matthew-brett.github.io/pydagogue/', None),
    'matplotlib': ('https://matplotlib.org/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
}

plot_basedir = join(dirname(dirname(os.path.abspath(__file__))), 'source')

# ghissue config
github_project_url = 'https://github.com/statsmodels/statsmodels'

example_context = yaml.safe_load(open('examples/landing.yml', encoding="utf-8"))

example_loader = FileSystemLoader("examples")
example_env = Environment(loader=example_loader)
example_tmpl = example_env.get_template("index.jinja2")
with open("examples/index.rst", "w") as example_index:
    example_index.write(example_tmpl.render(examples=example_context))

# html_context.update({'examples': example_context})

# --------------- DOCTEST -------------------
doctest_global_setup = """
import statsmodels.api as sm
import statsmodels.tsa.api as tsa
import statsmodels.formula.api as smf
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
"""

extlinks = {'pr': ('https://github.com/statsmodels/statsmodels/pull/%s',
                   'PR #%s'),
            'issue': ('https://github.com/statsmodels/statsmodels/issues/%s',
                      'Issue #%s')
            }

autosectionlabel_prefix_document = True

def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    # http://ericholscher.com/blog/2016/jul/25/integrating-jinja-rst-sphinx/
    # Make sure we're outputting HTML
    if app.builder.format != "html":
        return
    src = source[0]
    # Skip converted notebooks
    if 'nbconvert_exporter' in src:
        return
    try:
        rendered = app.builder.templates.render_string(src,
                                                       app.config.html_context)
        source[0] = rendered
    except Exception as exc:
        from sphinx.util import logging
        logger = logging.getLogger(__name__)
        logger.warning(exc)
        logger.warning(source[0])


def setup(app):
    app.connect("source-read", rstjinja)
    return {'parallel_read_safe': True,
            'parallel_write_safe': True}
