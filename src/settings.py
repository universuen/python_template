from pathlib import Path
import logging


src_path = Path(__file__).absolute().parent
project_path = src_path.parent


class Log:
    format = '[%(name)-10s] %(levelname)-8s: %(message)s'
    level = logging.DEBUG
