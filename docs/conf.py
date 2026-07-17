project = 'WeightLattice'
author = 'Pino Iulio'
release = '1.0.0'
version = '1.0.0'
copyright = '2026, Pino Iulio'

extensions = ['myst_parser']

source_suffix = {'.md': 'markdown'}
master_doc = 'index'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'furo'
html_title = 'WeightLattice'
html_static_path = ['_static']

myst_enable_extensions = [
    'colon_fence',
    'deflist',
    'html_image',
    'substitution',
]
