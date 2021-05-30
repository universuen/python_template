"""
This file is used to add current project path into the python path.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).absolute().parent.parent))
