import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath('..'))

project = 'WeightLattice'
author = 'Giuseppe'
copyright = f"{datetime.now().year}, {author}"

extensions = [
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = {
    '.md': 'markdown',
}
master_doc = 'index'
html_theme = 'furo'
html_static_path = ['_static']

myst_enable_extensions = [
    'colon_fence',
    'deflist',
    'html_image',
    'substitution',
]
