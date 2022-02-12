__version__ = '0.1.0'

import shutil
from pathlib import Path

dest = Path('configuration.json')

if not dest.exists():
    src = Path('configuration.json.example')
    shutil.copy(src, dest)