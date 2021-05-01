#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# FluentValidation documentation build configuration file, created by
# sphinx-quickstart on Wed Feb  5 15:31:13 2020.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from docutils import nodes

from sphinx.errors import SphinxError
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

# -- Environment ----------------------------------------------------------

IS_READTHEDOCS = os.environ.get('READTHEDOCS') == 'True'

docs_dir = os.path.dirname(__file__)
project_dir = os.path.join(docs_dir, '..')
node_modules_bin_dir = os.path.join(project_dir, 'node_modules', '.bin')

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "recommonmark",
    "sphinx_markdown_tables",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# source_parsers = {
#    '.md': 'recommonmark.parser.CommonMarkParser'
# }

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Tabular Editor'
copyright = '2016-2020, Daniel Otykier'
author = 'Daniel Otykier'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_theme_options = {
    'display_version': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'TabularEditordoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'TabularEditor.tex', 'Tabular Editor Documentation',
     'Daniel Otykier', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'tabulareditor', 'Tabular Editor Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'TabularEditor', 'Tabular Editor Documentation',
     author, 'TabularEditor', 'One line description of project.',
     'Miscellaneous'),
]


def setup(app):
    # Fixing how references (local links) work with Markdown
    app.connect('doctree-read', collect_ref_data)
    app.connect('doctree-resolved', process_refs)

    app.add_config_value('recommonmark_config', {
            'enable_eval_rst': True,
            #'url_resolver': lambda url: github_doc_root + url,
			'enable_math': False,
			'enable_inline_math': False
            #'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)

# -- Markdown References --------------------------------------------------

def collect_ref_data(app, doctree):
    """
    Finds all anchors and references (local links) within documents,
    and saves them as meta data
    """
    filename = doctree.attributes['source'].replace(docs_dir, '').lstrip('/')
    docname = filename.replace('.md', '')

    anchors = []
    references = []

    for node in doctree.traverse(nodes.raw):
        if 'name=' in node.rawsource:
            match = re.search(r'name="([^\"]+)', node.rawsource)
            if match:
                anchors.append(match.group(1).replace('/', ''))
        elif 'id=' in node.rawsource:
            match = re.search(r'id="([^\"]+)', node.rawsource)
            if match:
                anchors.append(match.group(1).replace('/', ''))

    for node in doctree.traverse(nodes.section):
        for target in frozenset(node.attributes.get('ids', [])):
            anchors.append(target.replace('/', ''))

    for node in doctree.traverse(nodes.reference):
        uri = node.get('refuri')
        if uri and not uri.startswith(('http://', 'https://')):
            references.append(to_reference(uri, basedoc=docname))

    app.env.metadata[docname]['anchors'] = anchors
    app.env.metadata[docname]['references'] = references

def process_refs(app, doctree, docname):
    """
    Fixes all references (local links) within documents, breaks the build
    if it finds any links to non-existent documents or anchors.
    """
    if 'references' in app.env.metadata[docname]:
        for reference in app.env.metadata[docname]['references']:
            referenced_docname, anchor = parse_reference(reference)

            if referenced_docname not in app.env.metadata:
                message = "Document '{}' is referenced from '{}', but it could not be found"
                raise SphinxError(message.format(referenced_docname, docname))

            if anchor and anchor not in app.env.metadata[referenced_docname]['anchors']:
                message = "Section '{}#{}' is referenced from '{}', but it could not be found"
                raise SphinxError(message.format(referenced_docname, anchor, docname))

            for node in doctree.traverse(nodes.reference):
                uri = node.get('refuri')
                if to_reference(uri, basedoc=docname) == reference:
                    node['refuri'] = to_uri(app, referenced_docname, anchor)

def to_uri(app, docname, anchor=None):
    uri = ''
    language = app.config.language or 'en'
    version_name = os.environ.get('READTHEDOCS_VERSION')

    uri += '/projects/te3/{}/{}/{}.html'.format(language, version_name, docname)
    if anchor:
        uri += '#{}'.format(anchor)

    return uri

def to_reference(uri, basedoc=None):
    """
    Helper function, compiles a 'reference' from given URI and base
    document name
    """
    if '#' in uri:
        filename, anchor = uri.split('#', 1)
        filename = filename or basedoc
    else:
        filename = uri or basedoc
        anchor = None

    if not filename:
        message = "For self references like '{}' you need to provide the 'basedoc' argument".format(uri)
        raise ValueError(message)

    reference = os.path.splitext(filename.lstrip('/'))[0]
    if anchor:
        reference += '#' + anchor
    return reference

def parse_reference(reference):
    """
    Helper function, parses a 'reference' to document name and anchor
    """
    if '#' in reference:
        docname, anchor = reference.split('#', 1)
    else:
        docname = reference
        anchor = None
    return docname, anchor
